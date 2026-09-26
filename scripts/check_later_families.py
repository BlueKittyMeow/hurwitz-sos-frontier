"""Finite comparison: LMO2011 and Hu–Huang–Zhang2018 families, parameter n=4..32.
See audits/RECENT_LITERATURE.md for primary sources and limitations.
"""
from math import comb
from pathlib import Path
import re
import yaml
root=Path(__file__).resolve().parents[1]
table={(t['r'],t['s']):t['upper'] for t in yaml.safe_load((root/'data/source_tables.yaml').read_text())['tables']['shapiro_2000_upper']}
def rho_pow(n):return 8*(n//4)+2**(n%4)
trip=[]
def add(r,s,N,src):
 if min(r,s,N)>0: trip.append((r,s,N,src))
for n in range(4,33):
 # Hu Theorems3–5
 if n%4 in (0,1,2):
  off=n%4
  add(2*n+2,2**n-2**off*comb(n-off,(n-off)//2),2**n,'Hu Thm3–5')
 # Hu Theorem6 and subtraction Cor5.4
 for k in range(2,n+1):
  for l in range(1,k):
   s=2*(comb(k-1,2)+l+1)
   if n%4 in (1,2):
    N=s*n-4*comb(k,3)-2*k*l
    if k==n-1:s+=2*l+(2 if l==n-2 else 0)
    if k==n:s+=2*(n-1-l)
   else:
    N=s*(n+1)-4*comb(k,3)-2*k*l
    if k==n:s+=2*l+(2 if l==n-1 else 0)
   if n==4 or (n==7 and not(k<=5 or(k==6 and l==1))):continue
   add(rho_pow(n),s,N,'Hu Thm6 addition')
   add(rho_pow(n),2**n-N,2**n-s,'Hu Cor5.4 subtraction')
   if n>=8 and n%4==0:add(rho_pow(n)+1,s,N,'Hu Prop5.7')
 # Hu Theorem7
 if n%4 in (0,1):
  for k in range((n-n%4)//2-1):
   add(2*n+2,2*sum(comb(n,i) for i in range(k+1)),2*sum(comb(n,i) for i in range(k+2)),'Hu Thm7')
 if n%4==2:
  for k in range((n-2)//2-1):
   add(2*n+2,4*sum(comb(n-1,i) for i in range(k+1)),4*sum(comb(n-1,i) for i in range(k+2)),'Hu Thm7')
 # LMO theorem1
 for k in range(2,n+1):
  for l in range(1,k):
   A=2*(comb(k-1,2)+l+1)
   s=2**n-A*n+4*comb(k,3)+2*k*l;N=2**n-A
   add(2*n,s,N,'LMO Thm1')
   if n%4==3:add(2*n+2,s-2,N,'LMO Thm1ii')
 if n%2:
  m=(n-1)//2
  for k in range(1,m+1):
   add(2*n+(2 if n%4==3 else 0),2*sum(comb(n,m-i) for i in range(k)),2*sum(comb(n,m-i) for i in range(k+1)),'LMO Thm2')
for a,b,c in [(16,24,98),(16,20,88),(16,16,74),(16,12,56),(16,10,52),(16,8,46),(16,6,38),(16,4,28),(16,2,16)]:add(a,b,c,'Hu7special')
imp=[]
for cell,N in table.items():
 r,s=cell
 cand=[t for t in trip if ((t[0]>=r and t[1]>=s)or(t[1]>=r and t[0]>=s))and t[2]<N]
 if cand:imp.append((cell,N,min(cand,key=lambda t:t[2])))
print('p292 cells',len(table),'triples',len(trip),'direct/restriction improvements',imp)
