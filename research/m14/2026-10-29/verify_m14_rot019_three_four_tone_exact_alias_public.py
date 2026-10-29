#!/usr/bin/env python3
"""M14 ROT019: standalone rational six/eight-Poisson-law alias check."""
from fractions import Fraction as F
D,V,G,BETA=F(1,5),F(1,2),F(7,20),F(3)
def k(x,z):return 1/((x-z)**2+V)
def solve(a,b):
 r=[list(x)+[y] for x,y in zip(a,b)];n=len(r)
 for j in range(n):
  q=next(i for i in range(j,n) if r[i][j]);r[q],r[j]=r[j],r[q]
  m=r[j][j];r[j]=[z/m for z in r[j]]
  for i in range(n):
   if i!=j:
    m=r[i][j];r[i]=[p-m*z for p,z in zip(r[i],r[j])]
 return [row[-1] for row in r]
basez=[-D,F(0),D];basew=[G/2,G,G/2]
def mu(x,zz,ww,beta=BETA):return beta-sum((w*k(x,z) for z,w in zip(zz,ww)),F(0))
for nt in [3,4]:
 xx=[-D,F(0),D]+([2*D] if nt==4 else [])
 obs=[mu(x,basez,basew) for x in xx]
 for sign in [-1,1]:
  zz=[(F(sign,4)+j)*D for j in [-1,0,1]]
  a=[[k(x,z) for z in zz] for x in xx]
  if nt==3:ww=solve(a,[BETA-y for y in obs]); beta=BETA
  else:
   t=solve([[F(1)]+[-u for u in row] for row in a],obs)
   beta,ww=t[0],t[1:]
  assert beta>0 and all(w>0 for w in ww)
  assert all(mu(x,zz,ww,beta)==y for x,y in zip(xx,obs))
  assert beta-sum(ww,F(0))/V>0
  assert mu((nt-1)*D,zz,ww,beta)!=mu((nt-1)*D,basez,basew)
print('ROT019 PUBLIC EXACT PASS: 6 and 8 identical Poisson means, positive globally, heldouts nonzero')
