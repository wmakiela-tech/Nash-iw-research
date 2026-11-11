#!/usr/bin/env python3
"""M14 ROT042 -- pure stdlib, exact rational finite-cotime full-field Fisher checks.
The nonattainment theorem and Bayesian minimax proof are in the separate science report.
"""
from fractions import Fraction as F
from itertools import combinations
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def solve(a,rhs):
    n=len(a); M=[list(map(F,a[i]))+[F(rhs[i])] for i in range(n)]
    for j in range(n):
        k=next(k for k in range(j,n) if M[k][j])
        if k!=j:M[j],M[k]=M[k],M[j]
        pivot=M[j][j]
        for q in range(j,n+1):M[j][q]/=pivot
        for k in range(n):
            if k==j:continue
            z=M[k][j]
            for q in range(j,n+1):M[k][q]-=z*M[j][q]
    return [row[-1] for row in M]

def risk(m,r,epsilon):
    assert m==1
    groups=list(combinations(range(4),r))
    B=len(groups);alpha=1-(B-1)*epsilon
    I=[[F(0) for _ in range(6)] for _ in range(6)]
    n=F(240,2*B*r)
    assert n==10
    for g,G in enumerate(groups):
        avg=[sum(F(A[i][k]) for i in G)/r for k in range(3)]
        for t in (g*epsilon,g*epsilon+alpha):
            for i in G:
                direction=[F(A[i][k])-avg[k] for k in range(3)]
                x=direction+[t*v for v in direction]
                for a in range(6):
                    for b in range(6):I[a][b]+=n*x[a]*x[b]
    trace=sum(solve(I,[int(i==3+k) for i in range(6)])[3+k] for k in range(3))
    C=2
    floor=F(9*r,4*(r-1))*C*C/240
    explicit=floor/alpha**2
    assert floor<trace<explicit
    return trace,floor,explicit

for r in (2,3):
    a,low,upper=risk(1,r,F(1,100))
    b,low2,upper2=risk(1,r,F(1,1000))
    assert low==low2 and low<b<a<upper
    assert b<upper2
    assert (r,low)==((2,F(3,40)) if r==2 else (3,F(9,160)))
    print(f'r={r} | lower={float(low):.9f} | exact finite e=.01 {float(a):.12f} | e=.001 {float(b):.12f} | analytical upper(e=.001)={float(upper2):.12f}')
print('M14 ROT042 PURE-STDLIB EXACT PASS: strict finite-calendar gap and explicit Chebyshev cluster convergence')
