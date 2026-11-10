#!/usr/bin/env python3
"""M14 ROT039: self-contained exact Fraction checks of four-axis common-mode gauge.
Global Gaussian adaptive minimax requires the analytic Bayes proof in the report.
"""
from fractions import Fraction as Q
from itertools import product
from math import prod
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
v0=(1,1,-1)
assert [sum(A[i][k]*v0[k] for k in range(3)) for i in range(4)]==[1,1,1,-3]
assert all(sum(A[i][k] for i in range(4))==0 for k in range(3))
assert [[sum(A[i][k]*A[i][j] for i in range(4)) for j in range(3)] for k in range(3)]==[[4,0,0],[0,4,0],[0,0,4]]
T=(Q(0),Q(1,4),Q(3,4),Q(1));m=3;N=144;H=Q(3,5)
w=[1/prod(T[j]-T[k] for k in range(m+1) if k!=j) for j in range(m+1)]
assert w==[-Q(16,3),Q(32,3),-Q(32,3),Q(16,3)]
assert all(sum(w[j]*T[j]**r for j in range(4))==int(r==3) for r in range(4))
C=sum(map(abs,w));eps=H/6
assert C==32 and eps==Q(1,10)

def variance(shots):return sum(w[j]**2/shots[j] for j in range(4))
noise4=3*variance([6,12,12,6])/4
noise3=3*variance([8,16,16,8])/2
assert noise4==Q(64,3) and noise3==32

def inv3(r):return ((r[0]+r[1])/2,(r[0]+r[2])/2,-(r[1]+r[2])/2)
def sq(v):return sum(z*z for z in v)
assert max(sq(tuple(sum(A[i][k]*e[i]*eps for i in range(4))/4 for k in range(3))) for e in product((-1,1),repeat=4))==eps*eps
assert sq(inv3((eps,eps,eps)))==3*eps*eps
# Same first THREE complete time-dependent observations for ANY q, but field differs.
for q in (Q(1,11),Q(10**8)):
  for t in (Q(0),Q(1,8),Q(1,3),Q(3,4),Q(1)):
    assert [sum(A[i][k]*q*v0[k]*t**m for k in range(3))-q*t**m for i in range(3)]==[0]*3
    assert sum(A[3][k]*q*v0[k]*t**m for k in range(3))-q*t**m==-4*q*t**m
assert noise4+eps*eps==Q(6403,300)
assert noise3+3*eps*eps==Q(3203,100)
print('ROT039 STD-LIB PASS: exact common 4 axes risk 64/3; 3 axes unbounded alias; near-common 4 axes 6403/300; bounded common 3 axes 3203/100')
