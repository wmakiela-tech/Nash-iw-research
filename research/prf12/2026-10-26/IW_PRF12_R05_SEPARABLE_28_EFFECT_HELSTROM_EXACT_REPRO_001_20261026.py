#!/usr/bin/env python3
"""PRF12 R05 — self-contained exact ideal-n3 28-effect separable Helstrom POVM.
Requirements: NumPy. No hardware/LOCC realization is implied.
Optional local 6-parameter product-basis search: pip install scipy; run --search.
"""
import sys
import numpy as np
from math import pi
from itertools import product, permutations

bits=np.array(list(product((0,1),repeat=3)))
def ket(phi):
    return np.array((1,np.exp(1j*phi)))/np.sqrt(2)
def kron(*xs):
    y=xs[0]
    for x in xs[1:]: y=np.kron(y,x)
    return y
def source_difference(q):
    d=bits[:,None,:]-bits[None,:,:]
    return (np.exp(-q*abs(d.sum(axis=-1)))-np.exp(-q*abs(d).sum(axis=-1)))/8
def effects():
    plus=np.zeros((8,8),complex);minus=np.zeros((8,8),complex)
    elementary=[]
    for phi in (0,pi/2,pi,3*pi/2):
        v=kron(ket(phi),ket(phi),ket(phi))
        e=(2/3)*np.outer(v,v.conj())
        plus+=e;elementary.append(e)
        for phases in permutations((0,2*pi/3,4*pi/3)):
            w=kron(*(ket(phi+t) for t in phases))
            e=(2/9)*np.outer(w,w.conj())
            minus+=e;elementary.append(e)
    return plus,minus,elementary
def local(theta,phi):
    c,s=np.cos(theta/2),np.sin(theta/2);e=np.exp(1j*phi)
    return np.array(((c,-e.conjugate()*s),(e*s,c)))
def tv_basis(D,angles):
    U=kron(*(local(*angles[2*k:2*k+2]) for k in range(3)))
    return sum(abs(np.diag(U.conj().T@D@U).real))/2
def main():
    Eplus,Eminus,fin=effects()
    W=(bits.sum(axis=1)==1).astype(float)/np.sqrt(3)
    Wbar=(bits.sum(axis=1)==2).astype(float)/np.sqrt(3)
    Pplus=np.outer(W,W)+np.outer(Wbar,Wbar)
    Pzero=np.zeros((8,8));Pzero[0,0]=Pzero[7,7]=1
    assert len(fin)==28
    assert np.max(abs(Eplus-Pplus-Pzero/3))<1e-12
    assert np.max(abs(Eplus+Eminus-np.eye(8)))<1e-12
    assert all(np.linalg.eigvalsh(e).min()>-1e-12 for e in fin)
    print("28 positive rank-1 PRODUCT effects; completeness error",
          np.max(abs(Eplus+Eminus-np.eye(8))))
    CNOT=np.zeros((8,8),complex)
    for i,b in enumerate(bits):
        v=b.copy();v[1]^=v[0]
        CNOT[4*v[0]+2*v[1]+v[2],i]=1
    for q in (0.05,1/3,0.7,1.4):
        D=source_difference(q)
        hel=sum(abs(np.linalg.eigvalsh(D)))/2
        x=tv_basis(D,(pi/2,0)*3)
        cnot=tv_basis(CNOT@D@CNOT.conj().T,
             (pi/2,0,1.0002537236512625,0,pi/2,0))
        sep=abs(np.trace(Eplus@D))
        assert abs(hel-(1-np.exp(-2*q))/2)<1e-12
        assert abs(hel-sep)<1e-12
        print("q",q,"Helstrom",hel,"Xfull",x,"one_CNOT",cnot,"SEP",sep)
    if "--search" in sys.argv:
        from scipy.optimize import differential_evolution
        D=source_difference(1/3)
        for label,A in (("product",D),("CNOT_product",CNOT@D@CNOT.conj().T)):
            for seed in (11,19,27):
                r=differential_evolution(lambda a:-tv_basis(A,a),
                    [(0,pi),(0,2*pi)]*3,seed=seed,maxiter=300,
                    popsize=15,tol=1e-10)
                print("NUMERIC_NONCERTIFIED",label,seed,-r.fun,r.x)
if __name__=="__main__":
    main()
