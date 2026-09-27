#!/usr/bin/env python3
"""Rebuild the audited finite frontier; no network access or private inputs."""
from pathlib import Path
from math import comb
import csv
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
CHECKED = '2026-09-26T00:00:00Z'
LIMIT = 32
COLUMNS = ['field','r','s','lower','upper','exact','lower_source_ids',
           'upper_source_ids','lower_kind','upper_kind','lower_status','upper_status',
           'lower_direct_or_derived','upper_direct_or_derived','derivation_ids',
           'last_checked_utc','audit_status','notes']

def hopf(r, s):
    """Least n satisfying the Hopf condition; integer arithmetic only."""
    return next(n for n in range(max(r,s),r+s)
                if all(comb(n,i)%2 == 0 for i in range(n-r+1,s)))

def phi(m):
    return sum(j%8 in (0,1,2,4) for j in range(1,m+1))

def rho(n):
    t=0
    while n%2 == 0:
        t+=1
        n//=2
    return 8*(t//4)+2**(t%4)

def bp_obstructions():
    # DI 2008 Theorem 1.1 and corrected Proposition 2.15, BOTH orientations.
    out=[]
    for a in range(1,LIMIT//2):
        for b in range(1,LIMIT//2):
            for m in range(max(a,b)+1,a+b+1):
                d=a+b-m
                for k in range(d-(d+1)//3+1):
                    top=m+k//2
                    bottom=a-(k+1)//2
                    value=comb(top,bottom)
                    divisor=2**(k//2+1)
                    if value%divisor:
                        out.append(dict(a=a,b=b,m=m,d=d,k=k,top=top,
                                        bottom=bottom,value=value,divisor=divisor))
                        break
    return out

def build():
    tables=yaml.safe_load((ROOT/'data/source_tables.yaml').read_text())['tables']
    sources={s['id']:s for s in yaml.safe_load((ROOT/'data/sources.yaml').read_text())['sources']}
    derivations={}
    def deriv(id,side,r,s,value,source_ids,operation,locator,proof,inputs=None,parameters=None):
        d=dict(id=id,side=side,source_ids=sorted(source_ids),source_locator=locator,
               operation=operation,inputs=inputs or [],result=dict(field='C',r=r,s=s,**{side:value}),
               proof=proof,parameters=parameters or {})
        if id in derivations:
            assert derivations[id] == d
        derivations[id]=d
        return d

    cells=[(r,s) for r in range(1,LIMIT+1) for s in range(r,LIMIT+1)]
    upper={}
    for r,s in cells:
        if r<=9:
            n=hopf(r,s)
            upper[r,s]=deriv(f'U-SY-{r}-{s}','upper',r,s,n,['smith-yiu-1992'],
                'explicit specialization','Theorem (9), p.485; Proposition (7), p.484',
                [f'Theorem (9) constructs an integer-coefficient [{r},{s},{n}] formula: r <= 9 and r o s = {n}.',
                 'Embed its integer coefficients in C; the polynomial identity remains valid.'],
                parameters={'theorem':'small_construction','source_field':'Z'})
    for key,sid in [('smith_yiu_1992_upper','smith-yiu-1992'),('shapiro_2000_upper','shapiro-2000')]:
        for t in tables[key]:
            r,s,n=t['r'],t['s'],t['upper']
            upper[r,s]=deriv(f'U-TABLE-{sid}-{r}-{s}','upper',r,s,n,[sid],
                'scalar extension',f"{t['locator']}, p.{t['page']}",
                [f'The construction table states an integer-coefficient [{r},{s},{n}] formula.',
                 'The embedding Z -> C preserves this polynomial identity. Integer optimality is not used.'],
                parameters={'theorem':'table_construction','table':key,'source_field':'Z'})
    upper[12,12]=deriv('U-ZZ-12-12','upper',12,12,18,['zhang-zhu-2026'],
        'direct statement','Theorem 1.1, p.3; equation (3.2), p.6',
        ['Theorem 1.1 explicitly includes C and constructs [12,12,18].',
         'The 20736 coefficient equations are independently checked by scripts/verify_zhang_zhu.py.'],
        parameters={'theorem':'zhang_zhu'})
    # Frozen derivation nodes prevent circular provenance when a bound improves.
    count=0
    def improve(r,s,n,operation,parents,proof,parameters,extra_sources=()):
        nonlocal count
        if n>=upper[r,s]['result']['upper']:
            return False
        count+=1
        ids={sid for p in parents for sid in p['source_ids']} | set(extra_sources)
        upper[r,s]=deriv(f'U-D{count:04d}','upper',r,s,n,ids,operation,
                            'Input derivations below',proof,[p['id'] for p in parents],parameters)
        return True
    # Close this finite window under published generalized doubling, source
    # restriction, and direct sum. Each improvement freezes its parent node.
    changed=True
    while changed:
        changed=False
        for r,s in cells:
            p=upper[r,s]; n=p['result']['upper']
            for m in range(1,6):
                q=2**m; extra=rho(2**(m-1))
                for x,y in ((r,s),(s,r)):
                    a,b=x+extra,q*y
                    if max(a,b)>LIMIT: continue
                    target=sorted((a,b))
                    changed |= improve(*target,q*n,'published generalized doubling',[p],
                        [f'Orient the parent as [{x},{y},{n}]. Zhang–Huang generalized doubling with m={m} gives [{a},{b},{q*n}].',
                         'Swap source inputs to the canonical ordered cell when needed.'],
                        {'m':m,'oriented_input_cell':[x,y],'oriented_output_cell':[a,b]},['zhang-huang-2017'])
        for r,s in reversed(cells):
            for a,b in cells:
                if r<=a and s<=b:
                    p=upper[a,b];n=p['result']['upper']
                    changed |= improve(r,s,n,'source restriction',[p],
                        [f'In the [{a},{b},{n}] identity set x_{r+1},...,x_{a} and y_{s+1},...,y_{b} to zero (empty ranges do nothing).',
                         f'The remaining output forms are bilinear and give [{r},{s},{n}].'],{})
        for r,s in sorted(cells,key=lambda c:(sum(c),c)):
            for axis,size in [('r',r),('s',s)]:
                for k in range(1,size):
                    pair=((k,s),(r-k,s)) if axis=='r' else ((r,k),(r,s-k))
                    parents=[upper[tuple(sorted(c))] for c in pair]
                    n=sum(p['result']['upper'] for p in parents)
                    changed |= improve(r,s,n,'direct sum',parents,
                        [f'Orient the two input identities as {pair[0]} and {pair[1]} by swapping x and y if necessary.',
                         f'Split the {axis} input into disjoint blocks of sizes {k} and {size-k}; keep the other input common.',
                         f'Concatenate the output forms. Adding the two identities gives [{r},{s},{n}].'],
                        {'axis':axis,'split':k,'oriented_input_cells':[list(c) for c in pair]})

    bp=bp_obstructions()
    lower={}
    for r,s in cells:
        candidates=[]
        # Candidate tuples: value, kind, source ids, operation, locator, proof, parameters.
        candidates.append((s,'rank',['shapiro-2000'],'rank specialization','Chapter 14, p.300',
            [f'Set x=(1,0,...,0). The induced n by {s} matrix A satisfies A^t A=I_{s}.',
             f'Hence rank(A)={s} and n >= {s}.'],{'theorem':'rank'}))
        h=hopf(r,s)
        if h>s:
            n=h-1;i=next(i for i in range(n-r+1,s) if comb(n,i)%2)
            candidates.append((h,'Hopf-Stiefel',['dugger-isaksen-2007'],'explicit specialization',
                'Theorem 1.2, p.943',
                [f'If length <= {n} existed, append zero outputs to obtain length {n}.',
                 f'{n}-{r} < {i} < {s}, but binomial({n},{i})={comb(n,i)} is odd, contradicting Theorem 1.2.'],
                {'theorem':'hopf','n':n,'i':i}))
        for a,b in [(r,s),(s,r)]:
            for n in range(s,upper[r,s]['result']['upper']):
                p=phi(b-1)
                bad=next((i for i in range(n-a+1,p+1) if comb(n,i)%2**(p-i+1)),None)
                if bad is not None:
                    i=bad;div=2**(p-i+1)
                    candidates.append((n+1,'Hermitian K-theory',['xie-2014'],'explicit specialization',
                        'Theorem 1.1, p.195',
                        [f'Pad any length <= {n} to {n}, and orient inputs as ({a},{b}).',
                         f'phi({b-1})={p}; {n}-{a} < {i} <= {p}.',
                         f'The theorem requires {div} to divide binomial({n},{i})={comb(n,i)}; remainder {comb(n,i)%div} is nonzero.'],
                        {'theorem':'xie','oriented_cell':[a,b],'n':n,'i':i,'phi':p,'divisor':div}))
        for t in tables['shapiro_2000_sigma']:
            a,b=t['r'],t['s'];small=sorted((a,b))
            if small[0]<=r and small[1]<=s:
                value=t['sigma']
                candidates.append((value,'nonsingular-map obstruction',['shapiro-2000'],
                    'source restriction and Lam-Lam transfer','Theorem 12.21, p.245; Lemma 14.1, p.300',
                    [f'Restrict a putative [{r},{s},n] complex formula to ({small[0]},{small[1]}), then orient it as ({a},{b}).',
                     'Write its complex output as U+iV on real inputs. The identity gives ||U||^2-||V||^2=||x||^2||y||^2, so U is a nonsingular real bilinear map (Lemma 14.1).',
                     f'Theorem 12.21 gives sigma({a},{b})={value}; sigma({a},{b}) <= {a} # {b} <= n.'],
                    {'theorem':'sigma','oriented_input_cell':[a,b],'sigma':value}))
        for w in bp:
            a,b,m,k=w['a'],w['b'],w['m'],w['k']
            small=sorted((2*a+1,2*b+1))
            if small[0]<=r and small[1]<=s:
                candidates.append((2*m+1,'BP2 obstruction',['dugger-isaksen-2008'],
                    'source restriction and explicit specialization','Theorem 1.1, p.3; Definition 2.13 and Proposition 2.15, p.8 (author final manuscript)',
                    [f'If [{r},{s},n] existed with n <= {2*m}, pad to {2*m}, restrict and orient to [{2*a+1},{2*b+1},{2*m}].',
                     f'Set a={a}, b={b}, m={m}, d={w["d"]}; max(a,b)<m<=a+b and 0<=k={k}<=d-floor((d+1)/3).',
                     f'Theorem 1.1 and Proposition 2.15 require {w["divisor"]} | S_{k}=binomial({w["top"]},{w["bottom"]})={w["value"]}, but the remainder is {w["value"]%w["divisor"]}.'],
                    {'theorem':'bp2',**w}))
        if r>=2 and s>=17:
            value=r+(s+1)//2
            candidates.append((value,'axial-map obstruction',['antoniano-gitler-1984','shapiro-2000'],
                'Lam-Lam transfer and explicit specialization',
                'Shapiro Lemma 14.1 p.300; Antoniano–Gitler Theorem (1.6) p.6 and exception analysis pp.7–9',
                ['A complex formula gives a nonsingular real bilinear map by the Lam–Lam lemma. Projectivizing gives an axial map.',
                 f'Its projective dimensions are (m,n,k)=({r-1},{s-1},N-1). The exception analysis has n<=15; here n={s-1}>=16.',
                 f'Theorem (1.6) requires {s-1}<2(N-{r}), hence N>={value}.'],
                {'theorem':'axial','projective_sources':[r-1,s-1]}))
        # Stable preference: earlier independent certificates win ties.
        value,kind,ids,op,loc,proof,params=max(candidates,key=lambda c:c[0])
        assert value<=upper[r,s]['result']['upper'],(r,s,value,upper[r,s])
        lower[r,s]=deriv(f'L-{r}-{s}','lower',r,s,value,ids,op,loc,proof,parameters=params)
        lower[r,s]['kind']=kind

    # Retain only actual provenance, including all intermediate inputs.
    used=set()
    def visit(id):
        if id in used:return
        used.add(id)
        for parent in derivations[id]['inputs']:visit(parent)
    for d in [*upper.values(),*lower.values()]:visit(d['id'])
    kept=[d for id,d in derivations.items() if id in used]
    rows=[]
    for r,s in cells:
        lo,up=lower[r,s],upper[r,s]
        l,u=lo['result']['lower'],up['result']['upper']
        status=lambda d:';'.join(sorted({sources[id]['publication_status'] for id in d['source_ids']}))
        rows.append(dict(zip(COLUMNS,['C',r,s,l,u,str(l==u).lower(),';'.join(lo['source_ids']),';'.join(up['source_ids']),
            lo['kind'],'published construction' if not up['inputs'] else up['operation'],status(lo),status(up),
            'derived','direct' if up['id']=='U-ZZ-12-12' else 'derived',lo['id']+';'+up['id'],
            CHECKED,'audited',
            'Bounds are best found in the audited sources and stated elementary closure; global literature completeness is not claimed.'])))
    return rows,kept

def main():
    rows,derivations=build()
    with (ROOT/'data/complex_frontier.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=COLUMNS);w.writeheader();w.writerows(rows)
    (ROOT/'data/derivations.yaml').write_text(yaml.safe_dump(dict(schema_version=1,derivations=derivations),sort_keys=False,allow_unicode=True,width=100))
    print(f'Built {len(rows)} cells, {sum(r["exact"]=="true" for r in rows)} exact, {len(derivations)} derivation records.')

if __name__=='__main__':main()
