#!/usr/bin/env python3
"""Public M14 ROT041 -- exact Fraction proof witnesses. Does not prove abstract Bayes theorem by tests."""
from fractions import Fraction as F
from itertools import combinations
A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def det3(M):
    a,b,c=M
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def inverse3(M):
    D=det3(M)
    if not D:raise ValueError('Unidentifiable: disconnected co-time graph')
    from itertools import product
    out=[]
    for j in range(3):
        rhs=[F(int(k==j)) for k in range(3)]
        # Cramer columns
        out.append(tuple(F(det3([[rhs[i] if k==q else M[i][k] for k in range(3)] for i in range(3)]),D) for q in range(3)))
    return tuple(tuple(out[k][j] for k in range(3)) for j in range(3))

def fisher(groups,N=240):
    n=F(N,len(groups)*len(groups[0]))
    M=[[F(0) for _ in range(3)] for _ in range(3)]
    for group in groups:
        mean=[F(sum(A[i][j] for i in group),len(group)) for j in range(3)]
        for i in group:
            d=[F(A[i][j])-mean[j] for j in range(3)]
            for a in range(3):
                for b in range(3):M[a][b]+=n*d[a]*d[b]
    return M

N=240
for r in (2,3,4):
    g=list(combinations(range(4),r));M=fisher(g,N)
    scalar=F(4*(r-1)*N,3*r)
    assert M==[[scalar if i==j else F(0) for j in range(3)] for i in range(3)]
    inv=inverse3(M)
    assert sum(inv[i][i] for i in range(3))==F(9*r,4*(r-1)*N)

edges=list(combinations(range(4),2))
for title,g,expected in [('star',[(0,1),(0,2),(0,3)],F(9,320)),('path',[(0,1),(1,2),(2,3)],F(1,32)),('all pairs',edges,F(3,160))]:
    im=inverse3(fisher(g))
    assert sum(im[i][i] for i in range(3))==expected

# Two separate pair sessions lack a connected graph despite touching all 4 axes.
for q in (F(7,13),F(10**9)):
    changes=[sum(F(A[i][j])*(q if j==0 else 0) for j in range(3)) for i in range(4)]
    assert changes==[q,q,-q,-q]
    assert changes[0]-q==changes[1]-q==changes[2]+q==changes[3]+q==0
print('M14 ROT041 PASS | full r2/r3/r4 isotropic Fisher exact | star/path | arbitrarily large disconnected drift gauge')
