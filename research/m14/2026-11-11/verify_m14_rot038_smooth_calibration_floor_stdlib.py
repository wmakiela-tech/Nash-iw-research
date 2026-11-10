#!/usr/bin/env python3
"""M14 ROT038: pure-stdlib EXACT minimax smooth-drift witness and risks.
The general adaptive/Bayes proof is in the accompanying report.
"""
from fractions import Fraction as Q
from math import prod, factorial
from itertools import product

A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
t=(Q(0),Q(1,4),Q(3,4),Q(1)); m=3; N=144
w=[1/prod(t[j]-t[k] for k in range(4) if k!=j) for j in range(4)]
assert w==[-Q(16,3),Q(32,3),-Q(32,3),Q(16,3)]
H=Q(3,5); eps=H/factorial(m)
assert eps==Q(1,10)
for q in range(4):
    assert sum(w[j]*t[j]**q for j in range(4))==int(q==3)

def squared_norm(v):return sum(q*q for q in v)
def at(v):return [sum(a[k]*v[k] for k in range(3)) for a in A]
# For 4 axes, K=A^T/4 and max_{||r||inf<=eps} ||Kr||²=eps².
maxfour=max(squared_norm([sum(A[i][k]*s[i] for i in range(4))*eps/4 for k in range(3)]) for s in product((-1,1),repeat=4))
assert maxfour==eps**2
# A3^{-1}(r1,r2,r3)=((r1+r2)/2,(r1+r3)/2,-(r2+r3)/2).
def inv3(r):return ((r[0]+r[1])/2,(r[0]+r[2])/2,-(r[1]+r[2])/2)
maxthree=max(squared_norm(inv3(tuple(eps*q for q in s))) for s in product((-1,1),repeat=3))
assert maxthree==3*eps**2
# Exact two distinct field histories +/- v are indistinguishable at ALL t:
# b_s(t)=(u+s v)t³, eta_is=(a_i.u)(P3(t)-t³)-s(a_i.v)t³.
def P3(t):return t**3-Q(3,2)*t**2+Q(9,16)*t-Q(1,32)
u=(Q(4,5),Q(2,7),-Q(1,4))
for axes,v in ((4,(eps,0,0)),(3,(eps,eps,-eps))):
    assert all(abs(c)<=eps for c in at(v)[:axes])
    for time in (Q(0),Q(1,8),Q(1,4),Q(2,5),Q(3,4),Q(1)):
        for i in range(axes):
            baseline=sum(A[i][k]*u[k] for k in range(3))*P3(time)
            for world in (-1,1):
                b=[(u[k]+world*v[k])*time**3 for k in range(3)]
                eta=sum(A[i][k]*u[k] for k in range(3))*(P3(time)-time**3)-world*sum(A[i][k]*v[k] for k in range(3))*time**3
                assert sum(A[i][k]*b[k] for k in range(3))+eta==baseline
# Reproduces exact variance of Chebyshev balanced schedules, plus bias floors.
def variance_per_axis(shots):return sum(w[j]**2/shots[j] for j in range(4))
v4=variance_per_axis((6,12,12,6));v3=variance_per_axis((8,16,16,8))
assert v4==Q(256,9) and v3==Q(64,3)
R4=3*v4/4+maxfour;R3=3*v3/2+maxthree
assert R4==Q(6403,300) and R3==Q(3203,100)
print(f'ROT038 EXACT PASS: 4 axes R={R4}, 3 axes R={R3}, calibration floors {maxfour} and {maxthree}, full-history aliases')
