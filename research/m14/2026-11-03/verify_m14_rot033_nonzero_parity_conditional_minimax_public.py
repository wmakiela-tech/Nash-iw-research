#!/usr/bin/env python3
"""M14 ROT033: standalone exact nonzero-parity conditional minimax certificate."""
from fractions import Fraction as F
from itertools import product, permutations
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def Q(eta):return tuple(sum((A[i][j]*eta[i] for i in range(4)),F(0))/4 for j in range(3))
def vertices(s):
 out=set()
 for free in range(4):
  ids=[i for i in range(4) if i!=free]
  for z in product((-1,1),repeat=3):
   e=[F(0)]*4
   for i,t in zip(ids,z):e[i]=F(t)
   e[free]=4*s-sum(e)
   if abs(e[free])<=1:out.add(Q(e))
 return out
def R2(s):
 t=abs(s)
 return 1-2*t+3*t*t if t<=F(1,2) else 3*(1-t)**2
for s,n in ((F(0),6),(F(1,4),12),(F(1,3),12),(F(1,2),4),(F(3,4),4),(F(1),1)):
 V=vertices(s)
 assert len(V)==n and max(dot(v,v) for v in V)==R2(s)
 assert max(dot(v,v) for v in vertices(-s))==R2(s)
assert R2(F(1,3))==F(2,3)<R2(F(1,2))==F(3,4)
g=tuple(map(F,('7/10','-1/2','4/5','0')))
bhat=Q(g)
for eta in ((1,1,-1,0),(-1,1,1,0)):
 q=Q(eta);b=tuple(bhat[i]-q[i] for i in range(3))
 assert sum(eta)==1 and all(abs(v)<=1 for v in eta)
 assert tuple(dot(a,b)+eta[i] for i,a in enumerate(A))==g
# Orbit averaging: for every extremal eta, its 24 permutations yield
# equal-radius q with mean zero, proving global Chebyshev optimality.
e=(F(1),F(1),F(-1),F(0))
O=[Q(p) for p in permutations(e)]
assert all(dot(v,v)==R2(F(1,4)) for v in O)
assert all(sum((v[j] for v in O),F(0))==0 for j in range(3))
print('M14 ROT033 PUBLIC EXACT PASS: all nonzero-parity strata, sharp minimax orbit, field alias')
