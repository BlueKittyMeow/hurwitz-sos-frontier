#!/usr/bin/env python3
"""Schema, provenance, arithmetic, symmetry, and regeneration checks."""
from pathlib import Path
from math import comb
from collections import Counter
import csv
import json
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from build import build, COLUMNS, hopf, phi, rho

ROOT=Path(__file__).resolve().parents[1]

def validate(rows, sources_doc, derivations_doc, tables_doc):
    errors=[]
    def check(ok,message):
        if not ok:errors.append(message)
    converted=[]
    for raw in rows:
        row=dict(raw)
        try:
            for key in ('r','s','lower','upper'):row[key]=int(row[key])
            if row['exact'] not in ('true','false'):raise ValueError('invalid exact')
            row['exact']=row['exact']=='true'
            for key in ('lower_source_ids','upper_source_ids','derivation_ids'):
                row[key]=row[key].split(';') if row[key] else []
            converted.append(row)
        except (ValueError,KeyError) as exc:
            errors.append(f'Invalid CSV row: {exc}')
    for name,doc in [('frontier',converted),('sources',sources_doc),('derivations',derivations_doc),('source_tables',tables_doc)]:
        validator=Draft202012Validator(json.loads((ROOT/f'schemas/{name}.schema.json').read_text()),format_checker=FormatChecker())
        errors.extend(f'{name}: {e.json_path}: {e.message}' for e in validator.iter_errors(doc))
    if errors:return errors
    sources={s['id']:s for s in sources_doc['sources']}
    ds={d['id']:d for d in derivations_doc['derivations']}
    check(len(sources)==len(sources_doc['sources']),'duplicate source ID')
    check(len(ds)==len(derivations_doc['derivations']),'duplicate derivation ID')
    seen=set();bycell={}
    for row in converted:
        r,s,l,u=row['r'],row['s'],row['lower'],row['upper'];key=(r,s)
        check(key not in seen,f'duplicate cell {key}');seen.add(key);bycell[key]=row
        check(r<=s,f'noncanonical symmetry ordering {key}')
        check(s<=l<=u,f'inconsistent bounds {key}')
        check(row['exact']==(l==u),f'inconsistent exact flag {key}')
        check(hopf(r,s)==hopf(s,r),f'Hopf symmetry failed {key}')
        for side in ('lower','upper'):
            ids=row[side+'_source_ids']
            check(all(id in sources for id in ids),f'missing source {key} {side}')
            matching=[ds[id] for id in row['derivation_ids'] if id in ds and ds[id]['side']==side]
            check(len(matching)==1,f'missing/ambiguous {side} proof {key}')
            if len(matching)==1:
                d=matching[0]
                check(d['result']==dict(field='C',r=r,s=s,**{side:row[side]}),f'proof result mismatch {key} {side}')
                check(set(ids)==set(d['source_ids']),f'proof source mismatch {key} {side}')
            if all(id in sources for id in ids):
                actual=';'.join(sorted({sources[id]['publication_status'] for id in ids}))
                check(row[side+'_status']==actual,f'publication status mismatch {key} {side}')
    if errors:return errors
    # Symmetric lookup must use the canonical entry; no mirrored rows are stored.
    def lookup(r,s):return bycell[tuple(sorted((r,s)))]
    for r,s in bycell:check(lookup(r,s)==lookup(s,r),f'lookup symmetry failed {(r,s)}')
    active=set();done=set()
    def visit(id):
        if id not in ds:errors.append(f'missing derivation {id}');return
        if id in active:errors.append(f'cyclic derivation {id}');return
        if id in done:return
        active.add(id)
        for parent in ds[id]['inputs']:visit(parent)
        active.remove(id);done.add(id)
    for id in ds:visit(id)
    if errors:return errors
    tab=tables_doc['tables']
    for d in ds.values():
        id=d['id'];out=d['result'];r,s=out['r'],out['s'];p=d['parameters']
        check(all(sid in sources for sid in d['source_ids']),f'{id}: missing source')
        parents=[ds[k] for k in d['inputs']]
        if parents and d['operation']!='published generalized doubling':
            check(set(d['source_ids'])=={sid for parent in parents for sid in parent['source_ids']},f'{id}: lost source ancestry')
        if d['side']=='upper':
            n=out['upper']
            if d['operation']=='source restriction':
                check(len(parents)==1,f'{id}: restriction arity')
                q=parents[0]['result']
                check(r<=q['r'] and s<=q['s'] and n==q['upper'],f'{id}: invalid restriction')
            elif d['operation']=='direct sum':
                pair=p['oriented_input_cells'];axis=p['axis']
                check(len(parents)==2 and len(pair)==2,f'{id}: direct sum arity')
                for q,cell in zip(parents,pair):
                    check(sorted(cell)==[q['result']['r'],q['result']['s']],f'{id}: invalid input orientation')
                check(n==sum(q['result']['upper'] for q in parents),f'{id}: output sum')
                a,b=pair
                check((a[0]+b[0]==r and a[1]==b[1]==s) if axis=='r' else (a[1]+b[1]==s and a[0]==b[0]==r),f'{id}: input split')
            elif d['operation']=='published generalized doubling':
                check(len(parents)==1 and 'zhang-huang-2017' in d['source_ids'],f'{id}: doubling authority')
                q=parents[0]['result'];x,y=p['oriented_input_cell'];a,b=p['oriented_output_cell'];m=p['m']
                check(sorted((x,y))==[q['r'],q['s']] and m>=1 and a==x+rho(2**(m-1)) and b==2**m*y and sorted((a,b))==[r,s] and n==2**m*q['upper'],f'{id}: doubling formula')
                check(set(d['source_ids'])==set(parents[0]['source_ids'])|{'zhang-huang-2017'},f'{id}: doubling ancestry')
            elif p.get('theorem')=='table_construction':
                check(any(t['r']==r and t['s']==s and t['upper']==n for t in tab[p['table']]),f'{id}: table mismatch')
            elif p.get('theorem')=='small_construction':
                check(r<=9 and n==hopf(r,s),f'{id}: small theorem mismatch')
            elif p.get('theorem')=='zhang_zhu':check((r,s,n)==(12,12,18),f'{id}: Zhang–Zhu mismatch')
            else:errors.append(f'{id}: unsupported upper rule')
        else:
            l=out['lower'];theorem=p['theorem']
            if theorem=='rank':check(l==s,f'{id}: rank mismatch')
            elif theorem=='hopf':
                n,i=p['n'],p['i'];check(l==n+1 and n-r<i<s and comb(n,i)%2==1,f'{id}: Hopf witness')
            elif theorem=='xie':
                a,b=p['oriented_cell'];n,i=p['n'],p['i'];power=phi(b-1)-i+1
                check(sorted((a,b))==[r,s] and n-a<i<=phi(b-1) and l==n+1 and power>=1 and comb(n,i)%2**power!=0,f'{id}: Xie witness')
            elif theorem=='sigma':
                a,b=p['oriented_input_cell'];u,v=sorted((a,b))
                check(u<=r and v<=s and l==p['sigma'] and any(t['r']==a and t['s']==b and t['sigma']==l for t in tab['shapiro_2000_sigma']),f'{id}: sigma restriction')
            elif theorem=='bp2':
                a,b,m,k=p['a'],p['b'],p['m'],p['k'];d0=a+b-m;u,v=sorted((2*a+1,2*b+1))
                check(u<=r and v<=s and max(a,b)<m<=a+b and 0<=k<=d0-(d0+1)//3 and l==2*m+1,f'{id}: BP range/restriction')
                check(p['top']==m+k//2 and p['bottom']==a-(k+1)//2 and p['value']==comb(p['top'],p['bottom']) and p['divisor']==2**(k//2+1) and p['value']%p['divisor']!=0,f'{id}: BP divisibility')
            elif theorem=='axial':check(r>=2 and s>=17 and l==r+(s+1)//2,f'{id}: axial range')
            else:errors.append(f'{id}: unsupported lower theorem')
    for (r,s),row in bycell.items():
        for (a,b),other in bycell.items():
            if r<=a and s<=b:
                check(row['lower']<=other['upper'],f'contradictory restriction {(r,s)} -> {(a,b)}')
    return errors

def main():
    with (ROOT/'data/complex_frontier.csv').open(newline='') as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==COLUMNS,'CSV column schema mismatch'
        rows=list(reader)
    sources=yaml.safe_load((ROOT/'data/sources.yaml').read_text())
    derivations=yaml.safe_load((ROOT/'data/derivations.yaml').read_text())
    tables=yaml.safe_load((ROOT/'data/source_tables.yaml').read_text())
    errors=validate(rows,sources,derivations,tables)
    expected,expected_d=build()
    checkrows=[{k:str(v) for k,v in row.items()} for row in expected]
    if rows!=checkrows:errors.append('Canonical CSV differs from deterministic rebuild')
    if derivations!={'schema_version':1,'derivations':expected_d}:errors.append('Derivations differ from deterministic rebuild')
    if errors:raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(rows)} cells; {sum(r["exact"]=="true" for r in rows)} exact; all schema, arithmetic, DAG, source, symmetry and regeneration checks.')

if __name__=='__main__':main()
