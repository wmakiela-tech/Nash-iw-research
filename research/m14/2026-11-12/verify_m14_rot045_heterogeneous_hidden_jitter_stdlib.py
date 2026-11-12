#!/usr/bin/env python3
"""ROT045 exact heterogeneous hidden-jitter certificate, standard library only."""
from fractions import Fraction as Q
from itertools import product
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def dot(u,v):return sum(x*y for x,y in zip(u,v))
def projection(v):return tuple(dot(tuple(Q(A[i][j]) for i in range(4)),v)/4 for j in range(3))
def norm2(v):return dot(v,v)
def bias(e,H=Q(1)):
    choices=list(product((-1,1),repeat=4))
    discrepancy=min(abs(dot(s,e)) for s in choices)
    form=H*H*(4*dot(e,e)-discrepancy*discrepancy)/16
    assert form==max(norm2(projection([H*s[i]*e[i] for i in range(4)])) for s in choices)
    return form
examples=[((1,1,1,1),Q(1)),((1,1,1,0),Q(11,16)),((1,1,0,0),Q(1,2)),((1,0,0,0),Q(3,16)),((2,1,1,0),Q(3,2))]
for e,answer in examples:assert bias(tuple(map(Q,e)))==answer
E=tuple(map(Q,(Q(1,20),Q(1,30),Q(1,50),Q(1,100))))
H=Q(3,5);sig2=Q(7,10);N=80
assert bias(E,H)==Q(369,1000000)
assert Q(3)*sig2/N+bias(E,H)==Q(26619,1000000)
# Exact two worlds, signed maximizing vertex, one COMMON affine calibration h_s.
signs=max(product((-1,1),repeat=4),key=lambda s:norm2(projection([H*s[i]*E[i] for i in range(4)])))
alpha=[H*signs[i]*E[i] for i in range(4)]
v=projection(alpha); c=sum(alpha)/4
u=(Q(3,2),Q(-2,3),Q(5,7))
for S in (-1,1):
 for i in range(4):
  true_t=-S*signs[i]*E[i]
  mean=dot(A[i],(u[j]+S*v[j] for j in range(3)))+H*true_t+S*c
  assert mean==dot(A[i],u)
print('ROT045 STDLIB PASS: exact heterogeneous epsilon partition discrepancy and global two-world witness')
