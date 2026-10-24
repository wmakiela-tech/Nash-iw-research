#!/usr/bin/env python3
"""NC-NUM-007: independent finite pure-point collision norm audit.
NO novelty, canon, executable physical/quantum model or owner adoption.
Requires NumPy. Full original 818-case test and JSON in Moderator ZIP.
"""
import numpy as np
S=lambda x:float(np.linalg.svd(x,compute_uv=False)[0])
def test(A,B,J,mA,mB,hA,hB,r):
    A=np.asarray(A); B=np.asarray(B)
    J=np.asarray(J,dtype=complex)
    coll=(B[:,None]!=A[None,:])&(np.asarray(hB)[:,None]==np.asarray(hA)[None,:])
    assert np.max(abs(J*(np.asarray(hB)[:,None]-np.asarray(hA)[None,:])))<1e-14
    # mA and mB must be restrictions of THE SAME global function m.
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            if a==b: assert abs(mA[i]-mB[j])<1e-14
    C=J*coll
    D=J*np.asarray(mA)[None,:]-np.asarray(mB)[:,None]*J
    normm=max(np.max(np.abs(mA)),np.max(np.abs(mB)))
    assert S(D)<=2*normm*S(C)+1e-12
    assert S(C)<=2*(1-1/r)*S(J)+1e-12
    return S(D),S(C),S(J)
J=np.ones((2,2))/2
d,c,j=test([0,1],[2,3],J,[1,1],[-1,-1],[1,1],[1,1],4)
assert abs(d-2)<1e-12 and abs(c-1)<1e-12
assert d>2*np.max(np.abs(J))  # REC9 false old supremum-block bound
d,c,j=test([0,1],[0,1],J,[1,-1],[1,-1],[1,1],[1,1],2)
assert abs(d-1)<1e-12 and abs(c-.5)<1e-12
for r in (2,3,4,8,16,32):
    J=np.eye(r)-2*np.ones((r,r))/r
    d,c,j=test(range(r),range(r),J,[1]*r,[1]*r,[1]*r,[1]*r,r)
    assert abs(c/j-2*(1-1/r))<1e-12
for n in (2,3,4,8,16,32,64):
    d,c,j=test(range(n),range(n,2*n),np.ones((n,n))/n,
               [1]*n,[-1]*n,[1]*n,[1]*n,2*n)
    assert abs(d-2)<1e-12
print("PASS NC-NUM-007 exact REC9 and r2 mixed sources; distinct r-bound; old inequality falsified")
