#!/usr/bin/env python3
"""M14 ROT025: independent public exact Fraction Poisson field FI replay."""
from fractions import Fraction as F
p=(F(1,4),F(1,2),F(1,100),F(1,50),F(1,2),F(1,5),F(31,10),F(4,5),F(29,10),F(6,5))
def solve(A,b):
 n=len(A);r=[list(row)+[y] for row,y in zip(A,b)]
 for j in range(n):
  k=next(i for i in range(j,n) if r[i][j]);r[j],r[k]=r[k],r[j]
  q=r[j][j];r[j]=[x/q for x in r[j]]
  for i in range(n):
   if i!=j:
    q=r[i][j];r[i]=[x-q*y for x,y in zip(r[i],r[j])]
 return [v[-1] for v in r]
def FI(tones):
 a,c,e,B,v,d,bm,Gm,bp,Gp=p;ws=(a,c,1-a-c);mu=[];J=[]
 for s in (-1,1):
  beta,G=(bm,Gm) if s==-1 else (bp,Gp)
  for x in tones:
   z=[x-e-s*B-j*d for j in (-1,0,1)]
   k=[1/(q*q+v) for q in z];du=[2*q/(q*q+v)**2 for q in z];dv=[-1/(q*q+v)**2 for q in z]
   S=lambda aa:sum((w*q for w,q in zip(ws,aa)),F(0))
   mean=S(k);shift=S(du);mu.append(beta-G*mean)
   J.append([-G*(k[0]-k[2]),-G*(k[1]-k[2]),-G*shift,-s*G*shift,-G*S(dv),-G*sum((w*j*q for w,j,q in zip(ws,(-1,0,1),du)),F(0))]+([F(1),-mean,F(0),F(0)] if s==-1 else [F(0),F(0),F(1),-mean]))
 b=[F(int(i==3)) for i in range(10)]
 z=solve(list(map(list,zip(*J))),b)
 assert all(sum((J[i][j]*z[i] for i in range(10)),F(0))==b[j] for j in range(10))
 assert min(mu)>0
 return 1/sum((t*a*a for t,a in zip(mu,z)),F(0))
def t(*x):return tuple(map(lambda y:F(str(y)),x))
old=FI(t(1,2,3,4,5));mid=FI(t('.85','1.35','2.25','3.55','3.95'))
new=FI(t('.75','1.25','1.75','2.25',5))
assert new>mid>old>0
assert abs(float(new/old)-7015.45916194)<1e-6
print('M14 ROT025 PUBLIC EXACT PASS',float(old),float(mid),float(new))
