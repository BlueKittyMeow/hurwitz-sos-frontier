"""Independent review checker, authored separately from build.py and validate.py."""
import csv,yaml,collections,math,json,hashlib
from pathlib import Path
base=Path(__file__).resolve().parents[1]/'data'
raw={p.name:p.read_bytes() for p in base.iterdir()}
rows=list(csv.DictReader(raw['complex_frontier.csv'].decode().splitlines()))
ds=yaml.safe_load(raw['derivations.yaml'])['derivations'];D={x['id']:x for x in ds}
ss=yaml.safe_load(raw['sources.yaml'])['sources'];S={x['id']:x for x in ss}
T=yaml.safe_load(raw['source_tables.yaml'])['tables']
assert len(D)==len(ds);assert len(S)==len(ss)
# Independent manual transcription of Shapiro Table12.21, 10..17 square, from public text.
sigma_rows='''16 17 17 19 20 20 22 26
17 17 17 19 20 21 23 27
17 17 17 19 20 21 23 28
19 19 19 19 23 23 23 29
20 20 20 23 23 23 23 30
20 20 20 23 23 23 23 31
22 23 23 23 23 23 23 32
26 27 28 29 30 31 32 32'''
sigma={(r,s):v for r,line in enumerate(sigma_rows.splitlines(),10) for s,v in enumerate(map(int,line.split()),10)}
assert all(sigma[x['r'],x['s']]==x['sigma'] for x in T['shapiro_2000_sigma'])
# Independent parity search, not builder implementation.
def hopf(r,s):
 for n in range(max(r,s),r+s):
  if all(math.comb(n,j)%2==0 for j in range(max(0,n-r+1),s)):
   return n
 raise AssertionError
color={}
def visit(i):
 assert color.get(i)!=1,('cycle',i)
 if color.get(i)==2:return
 color[i]=1
 for j in D[i]['inputs']:assert j in D;visit(j)
 color[i]=2
for i in D:visit(i)
counts=collections.Counter();strict=collections.Counter();maxdepth={}
def depth(i):
 if i not in maxdepth:maxdepth[i]=1+max([depth(j) for j in D[i]['inputs']] or [0])
 return maxdepth[i]
for x in ds:
 i=x['id'];p=x['parameters'];res=x['result'];r,s=res['r'],res['s'];side=x['side'];n=res[side]
 assert res['field']=='C' and 1<=r<=s<=32
 assert set(x['source_ids'])<=S.keys();assert x['proof'];counts[(side,x['operation'])]+=1
 inputs=[D[j] for j in x['inputs']]
 if side=='upper':
  op=x['operation']
  if op=='source restriction':
   assert len(inputs)==1;z=inputs[0]['result'];assert r<=z['r'] and s<=z['s'] and n==z['upper']
   assert set(x['source_ids'])==set(inputs[0]['source_ids'])
   strict['upper restriction']+=int((r,s)!=(z['r'],z['s']))
  elif op=='direct sum':
   assert len(inputs)==2 and n==sum(z['result']['upper'] for z in inputs)
   oriented=p['oriented_input_cells'];assert len(oriented)==2
   for z,c in zip(inputs,oriented):assert sorted(c)==[z['result']['r'],z['result']['s']]
   a,b=oriented
   if p['axis']=='r':assert a[1]==b[1]==s and a[0]+b[0]==r and a[0]==p['split']
   elif p['axis']=='s':assert a[0]==b[0]==r and a[1]+b[1]==s and a[1]==p['split']
   else:raise AssertionError
   assert set(x['source_ids'])==set().union(*(set(z['source_ids']) for z in inputs))
  elif op=='scalar extension':
   tab={(z['r'],z['s']):z['upper'] for z in T[p['table']]}
   assert tab[r,s]==n and p['source_field']=='Z'
  elif p.get('theorem')=='small_construction':assert r<=9 and n==hopf(r,s)
  elif p.get('theorem')=='zhang_zhu':assert (r,s,n)==(12,12,18)
  else:raise AssertionError(x)
 else:
  assert not inputs
  theorem=p['theorem']
  if theorem=='rank':assert n==s
  elif theorem=='hopf':
   nn,j=p['n'],p['i'];assert nn==n-1 and nn-r<j<s and math.comb(nn,j)%2
  elif theorem=='sigma':
   a,b=p['oriented_input_cell'];assert sorted([a,b])[0]<=r and sorted([a,b])[1]<=s
   assert n==p['sigma']==sigma[a,b]
   strict['lower sigma restriction']+=int(sorted([a,b])!=[r,s])
  elif theorem=='bp2':
   a,b,m,d,k=(p[t] for t in ['a','b','m','d','k'])
   small=sorted([2*a+1,2*b+1]);assert small[0]<=r and small[1]<=s
   assert max(a,b)<m<=a+b and d==a+b-m and 0<=k<=d-(d+1)//3
   top=m+k//2;bottom=a-k//2-(k%2);value=math.comb(top,bottom);div=2**(k//2+1)
   assert (top,bottom,value,div)==tuple(p[t] for t in ['top','bottom','value','divisor'])
   assert value%div!=0 and n==2*m+1
   strict['lower BP restriction']+=int(small!=[r,s])
  elif theorem=='xie':
   a,b=p['oriented_cell'];assert sorted([a,b])==[r,s]
   nn,j=p['n'],p['i'];phi=sum(k%8 in [0,1,2,4] for k in range(1,b))
   assert phi==p['phi'] and nn-a<j<=phi and nn==n-1
   div=2**(phi-j+1);assert div==p['divisor'] and math.comb(nn,j)%div!=0
  elif theorem=='axial':
   a,b=p['projective_sources'];assert [a,b]==[r-1,s-1] and b>=16
   assert n==(b+2*r)//2+1
  else:raise AssertionError(x)
for row in rows:
 r,s,nl,nu=map(int,[row['r'],row['s'],row['lower'],row['upper']]);assert nl<=nu
 assert row['exact']==str(nl==nu).lower()
 for side,n in [('lower',nl),('upper',nu)]:
  matching=[D[i] for i in row['derivation_ids'].split(';') if D[i]['side']==side]
  assert len(matching)==1
  x=matching[0];assert x['result']==dict(field='C',r=r,s=s,**{side:n})
  ids=row[side+'_source_ids'].split(';');assert set(ids)==set(x['source_ids'])
  statuses=set(S[j]['publication_status'] for j in ids)
  assert set(row[side+'_status'].split(';'))==statuses,(row,side,statuses)
assert len({(x['r'],x['s']) for x in rows})==len(rows)
print('PASS',len(rows),'canonical rows;',len(ds),'derivations;',len(S),'sources; DAG depth',max(depth(i) for i in D))
print('operations',dict(counts));print('strict nonidentity restrictions',dict(strict))
for r in [21,22,31,32]:
 row=next(x for x in rows if int(x['r'])==int(x['s'])==r)
 print('BENCHMARK',r,row['lower'],row['upper'],row['derivation_ids'])
 print(yaml.safe_dump(D[row['derivation_ids'].split(';')[1]],sort_keys=False))
print('SHA256', {p:hashlib.sha256(v).hexdigest() for p,v in raw.items()})
