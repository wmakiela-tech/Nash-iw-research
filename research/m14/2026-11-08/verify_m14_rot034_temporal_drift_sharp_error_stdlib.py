#!/usr/bin/env python3
"""M14 ROT034 public pure-stdlib exact temporal drift gauge and sharp error."""
from fractions import Fraction as F
from itertools import product
from math import comb
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
def dot(a,b):return sum((F(x)*y for x,y in zip(a,b)),F(0))
def diff(a,n):return sum((F((-1)**(n-j)*comb(n,j))*a[j] for j in range(n+1)),F(0))
def inv3(d):return ((d[0]+d[1])/2,(d[0]+d[2])/2,-(d[1]+d[2])/2)
def inv4(d):return tuple(sum((A[i][j]*d[i] for i in range(4)),F(0))/4 for j in range(3))
def pol(coef,k):return sum((F(q)*F(comb(k,j)) for j,q in enumerate(coef) if k>=j),F(0))
for p in range(4):
 n=p+1;kk=list(range(n+1))
 b=[tuple(F((j+1)*k*k+k+3,97) for j in range(3)) for k in kk]
 eta=[[pol([F((i+1)*(j+1),1000) for j in range(p+1)],k) for k in kk] for i in range(4)]
 h=[tuple(pol([F((a+1)*(j+2),700) for j in range(p+1)],k) for a in range(3)) for k in kk]
 g=[[dot(A[i],b[k])+eta[i][k] for k in kk] for i in range(4)]
 g2=[[dot(A[i],tuple(b[k][a]+h[k][a] for a in range(3)))+eta[i][k]-dot(A[i],h[k]) for k in kk] for i in range(4)]
 assert g==g2
 d=tuple(diff(g[i],n) for i in range(4))
 z=tuple(diff([b[k][j] for k in kk],n) for j in range(3))
 assert inv3(d[:3])==z and inv4(d)==z and sum(d)==0
 delta=F(1,100);kap=2**n*delta
 for signs in product((-1,1),repeat=4):
  e=[[F(signs[i])*delta*(-1)**(n-j) for j in kk] for i in range(4)]
  noisy=tuple(diff(e[i],n) for i in range(4))
  assert noisy==tuple(F(t)*kap for t in signs)
 assert max(sum(q*q for q in inv3(tuple(kap*t for t in signs))) for signs in product((-1,1),repeat=3))==3*kap*kap
 assert max(sum(q*q for q in inv4(tuple(kap*t for t in signs))) for signs in product((-1,1),repeat=4))==kap*kap
print('M14 ROT034 PUBLIC EXACT PASS: polynomial drift quotient and sharp sqrt(3)/1 finite-error radii, p=0..3')
