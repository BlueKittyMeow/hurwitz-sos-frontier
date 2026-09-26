#!/usr/bin/env python3
"""Generate readable tables and citation/proof indexes from canonical data."""
from pathlib import Path
from collections import Counter
import csv
import json
import yaml
ROOT=Path(__file__).resolve().parents[1]

def render():
    rows=list(csv.DictReader((ROOT/'data/complex_frontier.csv').open()))
    sources=yaml.safe_load((ROOT/'data/sources.yaml').read_text())['sources']
    derivations=yaml.safe_load((ROOT/'data/derivations.yaml').read_text())['derivations']
    out={}
    def table(title,selection):
        text=f'# {title}\n\nAudit date: 2026-09-26. Ordinary complex algebraic squares, with bilinear outputs. '
        text+='Bounds are the strongest found in the audited sources and documented elementary deductions. '
        text+='An unequal bracket does not assert that the exact value is unknown throughout all literature.\n\n'
        text+='Each bound links to its sources and its separate proof. See [known gaps](../audits/KNOWN_GAPS.md).\n\n'
        text+='| r | s | Lower | Upper | Exact? | Lower authority | Upper authority |\n|---:|---:|---:|---:|:---:|---|---|\n'
        for row in selection:
            dids=row['derivation_ids'].split(';')
            links=lambda side:' + '.join(f'[{id}](sources.md#{id})' for id in row[side+'_source_ids'].split(';'))
            def bound(side,index):return f'[{row[side]}](derivations.md#{dids[index].lower()})'
            text+=f'| {row["r"]} | {row["s"]} | {bound("lower",0)} | {bound("upper",1)} | {"yes" if row["exact"]=="true" else "no"} | {links("lower")} | {links("upper")} |\n'
        return text
    out['diagonal.md']=table('Complex diagonal frontier',[r for r in rows if r['r']==r['s']])
    out['exact_cells.md']=table('Exact complex cells',[r for r in rows if r['exact']=='true'])
    out['open_cells.md']=table('Complex cells with unequal audited bounds',[r for r in rows if r['exact']=='false'])
    out['rectangular.md']=table('Selected rectangular frontier',[r for r in rows if r['r']!=r['s'] and (int(r['r'])>=10 or int(r['s']) in (8,16,32))])
    out['all_cells.md']=table('All audited complex cells',rows)
    text='# Source index\n\nPublication status and exact locators are retained for every source. '
    text+='Sources marked as context or comparison supply no canonical bound.\n\n'
    for s in sources:
        text+=f'## {s["id"]}\n\n{s["citation"]}\n\n'
        text+=f'**Status:** {s["publication_status"]}. **Role:** {s["role"]}. **Checked:** {s["audit_date"]}.\n\n'
        if s['doi']:text+=f'DOI: [{s["doi"]}](https://doi.org/{s["doi"]}).\n\n'
        text+='Public access: '+', '.join(f'[source {i+1}]({url})' for i,url in enumerate(s['public_urls']))+'.\n\n'
        text+='Locators: '+'; '.join(s['locators'])+'.\n\n'
        text+='\n'.join('- '+note for note in s['interpretation_notes'])+'\n\n'
    out['sources.md']=text
    text='# Bound derivations\n\nGenerated from `data/derivations.yaml`. Input links preserve an acyclic proof graph.\n\n'
    for d in derivations:
        q=d['result'];side=d['side'];relation='>=' if side=='lower' else '<='
        text+=f'## {d["id"]}\n\nN_C({q["r"]},{q["s"]}) {relation} {q[side]}. Operation: {d["operation"]}.\n\n'
        text+='Sources: '+', '.join(f'[{id}](sources.md#{id})' for id in d['source_ids'])+'. '+d['source_locator']+'.\n\n'
        if d['inputs']:text+='Inputs: '+', '.join(f'[{id}](#{id.lower()})' for id in d['inputs'])+'.\n\n'
        text+='\n'.join(f'{i+1}. {line}' for i,line in enumerate(d['proof']))+'\n\n'
    out['derivations.md']=text
    active={id for row in rows for side in ['lower','upper'] for id in row[side+'_source_ids'].split(';')}
    used=[s for s in sources if s['id'] in active]
    stats=dict(audit_date='2026-09-26',scope='1 <= r <= s <= 32',cells=len(rows),exact=sum(r['exact']=='true' for r in rows),bounded=sum(r['exact']=='false' and r['audit_status']=='audited' for r in rows),unresolved=sum(r['audit_status']=='unresolved' for r in rows),source_count=len(sources),sources_by_status=dict(sorted(Counter(s['publication_status'] for s in sources).items())),numerical_source_count=len(used),numerical_sources_by_status=dict(sorted(Counter(s['publication_status'] for s in used).items())),oldest_numerical_sources=[s['id'] for s in used if s['year']==min(s['year'] for s in used)],newest_numerical_sources=[s['id'] for s in used if s['year']==max(s['year'] for s in used)],derivation_count=len(derivations))
    out['statistics.json']=json.dumps(stats,indent=2)+'\n'
    return out

if __name__=='__main__':
    import sys
    files=render()
    if '--check' in sys.argv:
        stale=[name for name,text in files.items() if not (ROOT/'generated'/name).exists() or (ROOT/'generated'/name).read_text()!=text]
        if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
        print('PASS: generated tables and indexes match canonical data.')
    else:
        for name,text in files.items():(ROOT/'generated'/name).write_text(text)
        print(f'Generated {len(files)} files.')
