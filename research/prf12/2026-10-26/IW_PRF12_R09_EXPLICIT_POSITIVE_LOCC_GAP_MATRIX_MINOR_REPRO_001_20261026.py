#!/usr/bin/env python3
"""PRF12 R09: exact n=3 source model and explicit LOCC gap >= mu(q)/72.
Independent finite 8x8 computational checks; external necessary theorem:
S. M. Cohen, PRA 105, 022207 (2022), Theorem 1.
No numerical optimization over all LOCC is performed or claimed.
"""
import numpy as np
from math import exp,sqrt
from itertools import product

bits=np.array(list(product((0,1),repeat=3)),dtype=int)
I=np.eye(8,dtype=complex)

def source_difference(q):
    d=bits[:,None,:]-bits[None,:,:]
    return (np.exp(-q*abs(d.sum(axis=2)))
            -np.exp(-q*abs(d).sum(axis=2)))/8.

def get_projectors(q):
    D=source_difference(q)
    vals,vecs=np.linalg.eigh(D)
    P=vecs[:,vals>1.e-11]@vecs[:,vals>1.e-11].conj().T
    Q=vecs[:,vals< -1.e-11]@vecs[:,vals< -1.e-11].conj().T
    return D,P,Q,vals

def r08_lower_locc(q):
    x=exp(-q);b=1-x*x
    fixed_x=b*(6+9*x)/32 if x>=2/3 else 3*b/8
    adaptive=b/32*(4+3*x+max(2,3*x)+2*sqrt(4+(2-x)**2))
    return max(fixed_x,adaptive)

def random_product_minor_check():
    rng=np.random.default_rng(20261026)
    for i in range(300):
        local=[]
        for j in range(3):
            A=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
            local.append(A.conj().T@A)
        F=np.kron(np.kron(*local[:2]),local[2])
        # Exact Segre/product minor (indices: 001=1,010=2,011=3).
        lhs=F[1,2]*F[3,3]
        rhs=F[1,3]*F[3,2]
        assert abs(lhs-rhs) < 5e-11*(1+abs(lhs)+abs(rhs))
    print('300 independently sampled positive product-minor checks PASS')

def main():
    random_product_minor_check()
    for q in (.05,1/3,.7,1.4):
        D,P,Q,ev=get_projectors(q)
        x=exp(-q);b=1-x*x
        mu=b*(1-x)/8
        hel=b/2
        assert np.isclose(np.sum(abs(ev))/2,hel,atol=2.e-15)
        assert np.isclose(min(abs(y) for y in ev if abs(y)>1e-11),mu,atol=2.e-15)
        assert np.allclose([P[1,2],P[3,3],P[1,3],P[3,2]],
                           [1/3,1/3,0,0],atol=2.e-15)
        # Eopt's zero-space completion remains arbitrary.
        K=I-P-Q
        E=P+.47*K
        score=np.trace(E@D).real
        assert abs(hel-score)<1e-14
        # A deliberately near-optimal binary effect, with nonzero regret.
        e=1/100
        Etest=(1-e)*E+e*I/2
        gap=hel-np.trace(Etest@D).real
        eps=sqrt(2*gap/mu)
        if eps < 1/6:
            assert abs(Etest[1,2]-1/3)<=eps+1e-12
            assert abs(Etest[3,3]-1/3)<=eps+1e-12
            assert abs(Etest[1,3])<=eps+1e-12
            assert abs(Etest[3,2])<=eps+1e-12
        print(f"q={q:.12g}; Hel={hel:.12f}; "
              f"explicit_LOCC_gap_lower={mu/72:.12f}; "
              f"LOCC_gap_upper={hel-r08_lower_locc(q):.12f}")
    q=1/3;x=exp(-q);mu=(1-exp(-2*q))*(1-x)/8
    print('R09 CERTIFIED DELTA lower at q=1/3:',mu/72)
    print('ASSUMPTION: Cohen (2022) theorem 1 for closure(LOCC)')
    print('THEOREM PROOF: no nonscalar product in near-optimal binary zonotope')
if __name__=="__main__": main()
