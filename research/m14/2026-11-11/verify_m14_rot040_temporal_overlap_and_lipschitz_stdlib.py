#!/usr/bin/env python3
"""M14 ROT040: compact public pure-stdlib exact rational synchronization certificate."""
from fractions import Fraction as Q
from itertools import product

a=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
t=(Q(0),Q(1,2),Q(1))
groups=((1,2,3),(0,2,3),(0,1,3))

def det(M):
    A=[list(map(Q,row)) for row in M];n=len(A);v=Q(1)
    for c in range(n):
        k=next(i for i in range(c,n) if A[i][c]);
        if k!=c:A[k],A[c]=A[c],A[k];v=-v
        d=A[c][c];v*=d
        for i in range(c+1,n):
            f=A[i][c]/d
            for j in range(c+1,n):A[i][j]-=f*A[c][j]
    return v
D=[]
for time,grp in zip(t,groups):
    for i in grp[1:]:
        d=[a[i][k]-a[grp[0]][k] for k in range(3)]
        D.append(d+[time*q for q in d])
assert det(D)==64
assert len(D)==6
# Sequential snapshot: D_s z = successive differences. Candidate v=H*gap*(1,1/2,0)
H=Q(3,4);gap=Q(1,20);v=[H*gap,H*gap/2,0]
assert all(sum((a[i+1][k]-a[i][k])*v[k] for k in range(3))==-H*gap for i in range(3))
assert sum(x*x for x in v)==Q(5,4)*H*H*gap*gap
# A linear common drift h(t)=H(t-3gap/2) exactly masks +v at all four staggered slots.
for i in range(4):
    assert sum(a[i][k]*v[k] for k in range(3))+H*(i*gap-Q(3,2)*gap)==0
N=40; sigma2=Q(3,10)
assert Q(3)*sigma2/N+sum(x*x for x in v)==Q(9,400)+Q(5,4)*H*H*gap*gap
print('M14 ROT040 pure stdlib PASS: 3 staggered triple groups determinant=64; four sequential slots sharp Lipschitz bias²=5/4 (H gap)²')
