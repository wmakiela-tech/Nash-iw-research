#!/usr/bin/env python3
"""MT13 NC-OPN017 exact pure-point collision sharp constant; classic Schur pinching.
Independent matrix falsifier. Only NumPy needed. NO NOVELTY / NO PHYSICAL CLAIM.
"""
import json
import numpy as np

def norm(z):
    return float(np.linalg.svd(z,compute_uv=False)[0])

def collision(eigen_A,eigen_B,J):
    x=np.asarray(eigen_A);y=np.asarray(eigen_B)
    return J*(y[:,None]!=x[None,:])

def cyclic_average_collision(eigen_A,eigen_B,J):
    labels=list(dict.fromkeys(list(eigen_A)+list(eigen_B)))
    r=len(labels);code={v:k for k,v in enumerate(labels)}
    pa=np.array([code[v] for v in eigen_A])
    pb=np.array([code[v] for v in eigen_B])
    omega=np.exp(2j*np.pi/r)
    matched=sum(omega**(k*(pb[:,None]-pa[None,:]))*J for k in range(r))/r
    return J-matched,r

def main():
    rows=[]
    for r in [1,2,3,4,5,8,16,32,64]:
        J=np.eye(r)-2*np.ones((r,r))/r
        C=collision(list(range(r)),list(range(r)),J)
        rho=norm(C)/norm(J);target=2*(1-1/r)
        assert abs(rho-target)<5e-13,(r,rho,target)
        rows.append([r,rho,target])
    print("SHARP RATIOS (r, ||Jcoll||/||J||, exact)")
    for row in rows: print(row)
    rng=np.random.default_rng(20261024)
    nc=0
    for nA,nB in [(2,2),(2,4),(3,5),(5,3),(7,8)]:
        for _ in range(120):
            pa=rng.integers(0,nA+2,size=nA).tolist()
            pb=rng.integers(0,nB+2,size=nB).tolist()
            J=rng.normal(size=(nB,nA))+1j*rng.normal(size=(nB,nA))
            C=collision(pa,pb,J)
            C2,r=cyclic_average_collision(pa,pb,J)
            assert np.max(np.abs(C-C2))<2e-12
            assert norm(C)<=2*(1-1/r)*norm(J)+5e-12
            nc+=1
    print("RECTANGULAR_PHASE_AVERAGE_PASS",nc)
    nm=0
    for _ in range(150):
        fiber=np.repeat(np.arange(3),4)
        J=rng.normal(size=(12,12))+1j*rng.normal(size=(12,12))
        J*=fiber[:,None]==fiber[None,:]
        C=J*(np.arange(12)[:,None]!=np.arange(12)[None,:])
        assert norm(C)<=1.5*norm(J)+5e-12
        nm+=1
    print("THREE_H_FIBERS_PASS",nm)
    # NC/REC9 historical falsifier for the REJECTED sup-single-block bound:
    J=np.ones((2,2))/2
    C=collision([0,1],[2,3],J)
    assert abs(2*norm(J)-2)<1e-13
    assert abs(2*np.max(abs(C))-1)<1e-13
    assert abs(2*norm(C)-2)<1e-13
    print("REC9_OLD_BOUND_FAILURE_REPLICATED, NC_NEW_BOUND_PASS")
    print("PASS / 750 randomized tests / proof-independent falsifiers")
if __name__=="__main__":
    main()
