#!/usr/bin/env python3
"""M14 ROT032 PUBLIC: exact stdlib minimax/polytope and hidden-drift certificates."""
from fractions import Fraction as F
from itertools import product
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
def av(b):return tuple(sum((x*y for x,y in zip(a,b)),F(0)) for a in A)
def proj(d):return tuple(sum((A[i][j]*d[i] for i in range(4)),F(0))/4 for j in range(3))
def avg(z):return sum(z,F(0))/4
E=F(1,40)
V={tuple(E*q for q in proj(tuple(map(F,s)))) for s in product((-1,1),repeat=4)}
axes={tuple(E*s if j==k else F(0) for j in range(3)) for k in range(3) for s in (-1,1)}
diag={tuple(E*s/2 for s in z) for z in product((-1,1),repeat=3)}
assert V==axes|diag|{(F(0),)*3} and len(V)==15
assert max(sum(q*q for q in z) for z in V)==E*E
assert all(max(abs(z[0])+abs(z[1]),abs(z[0])+abs(z[2]),abs(z[1])+abs(z[2]))<=E for z in V)
# Two different fields generate identical all four resonance centers with bounded drift.
for sign in (-1,1):
 b=(sign*E,F(0),F(0));shift=tuple(-q for q in av(b))
 assert all(abs(q)<=E for q in shift)
 assert tuple(x+y for x,y in zip(av(b),shift))==(F(0),)*4
# Every orientation-dependent free nuisance mode decomposes as common shift plus field.
for z in product((-1,0,1),repeat=4):
 h=tuple(map(F,z));c=avg(h);q=proj(h)
 assert tuple(c+v for v in av(q))==h
# Four +/- branch pairs have only one parity; eta=A*(E,0,0) is undetectable.
eta=av((E,F(0),F(0)))
assert eta==(E,E,-E,-E) and sum(eta)==0
# With zero parity, feasible paired field errors are the l1 octahedron.
for q in product((-E,F(0),E),repeat=3):
 if sum(map(abs,q))<=E:assert all(abs(v)<=E for v in av(q))
print('M14 ROT032 PUBLIC EXACT PASS: sharp eps minimax, rhombic dodecahedron, noncommon drift gauge and parity-dark offset')
