#!/usr/bin/env python3
"""PRF12 R15: exact one-sided B heralding with arbitrary static-Xi reset partition.

A: within each group of runs, ONE common Cauchy Xi for all sensor exposures
   and runs in that group; groups have independent Xi.
B: independent Levy increments across all runs and sensor exposures.
There are 3 spatial labs; each holds one qubit per run and can jointly measure
its own qubits, but has no shared entanglement or quantum communication.
Each run contains 3 equal ideal SWAP exposures, gamma*Delta=q, memory kappa=0.

This code numerically checks the independent analytical result:
    P(B-only | B, LOCC optimum) = 1 - (product_g h_{m_g})^3
    P(B-only | B, global optimum) = 1 - product_g h_{3*m_g}
where h_m(p+,p-)=sum_{k=0}^m p+**(m-k)*p-**k and p+=(1+e^-q)/2.
No full single-run minimum-error LOCC closure gap is claimed.
"""
import math
from itertools import product
import numpy as np

I2=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)

def h(m,q):
    x=math.exp(-q); a=(1+x)/2; b=(1-x)/2
    return sum(a**(m-k)*b**k for k in range(m+1))

def sym_projector(m):
    assert m>=1
    P=np.zeros((2**m,2**m),complex)
    for weight in range(m+1):
        indices=[i for i in range(2**m) if i.bit_count()==weight]
        u=np.zeros(2**m,complex)
        u[indices]=1/math.sqrt(len(indices))
        P+=np.outer(u,u.conj())
    assert np.linalg.norm(P@P-P)<1e-12
    assert abs(np.trace(P)-(m+1))<1e-12
    return P

def kron_all(M):
    v=np.array([[1.]],complex)
    for x in M:v=np.kron(v,x)
    return v

def local_group_projector(groups):
    return kron_all([sym_projector(m) for m in groups])

def rho_runs(q,r):
    x=math.exp(-q)
    rho=(I2+x*X)/2
    return kron_all([rho for _ in range(r)])

def predicted(q,groups):
    local=math.prod(h(m,q) for m in groups)
    global_support=math.prod(h(3*m,q) for m in groups)
    return 1-local**3,1-global_support

def phase_qubit(z):
    return np.array([1,z],complex)/math.sqrt(2)

def a_local_pure(groups,phases):
    assert len(groups)==len(phases)
    return kron_all([phase_qubit(z) for (m,z) in zip(groups,phases)
                         for _ in range(m)]).reshape(-1)

def verify():
    tests=0
    for q in (.05,1/3,1.,3.):
        for group in ((1,), (2,), (3,), (4,), (1,1), (2,1), (2,2), (3,1), (1,1,1,1)):
            group=list(group)
            m=sum(group);V=local_group_projector(group)
            r=rho_runs(q,m)
            local_trace=np.trace(V@r).real
            exact_local=math.prod(h(k,q) for k in group)
            assert abs(local_trace-exact_local)<2e-12
            sep,glob=predicted(q,group)
            assert abs(sep-(1-local_trace**3))<2e-12
            assert -1e-12<=sep<=glob+1e-12<=1+1e-12
            # Global projector is tensor product over (3m) qubits in each segment.
            # There is no need to materialize a 2**(3m) full Hilbert space.
            if 3*m<=9:
                Sglob=kron_all([sym_projector(3*k) for k in group])
                Bglob=rho_runs(q,3*m)
                directglob=1-np.trace(Sglob@Bglob).real
                assert abs(directglob-glob)<3e-12
            # Under A, each spatial lab has tensor of pure equal-spinors per group.
            angles=[np.exp(2j*math.pi*(j+.37)/(len(group)+2)) for j in range(len(group))]
            a=a_local_pure(group,angles)
            assert abs(np.vdot(a,V@a)-1)<1e-12
            tests+=1
    print('independent 3-lab/group/global trace tests PASS',tests)

    q=1/3
    for group in ((1,),(2,),(3,),(4,),(6,),(1,1,1,1),(2,1,1),(2,2),(3,1)):
        lo,gl=predicted(q,group)
        print('partition',group,'LOCC=',f'{lo:.12f}',
              'GLOBAL=',f'{gl:.12f}','global-LOCC=',f'{gl-lo:.12f}')
    p2,_=predicted(q,[2])
    cycles=math.ceil(math.log(.05)/math.log(1-p2))
    assert cycles==8
    print('Repeated independent two-run macro-experiments for >=95% B herald: ',cycles)

if __name__=='__main__':verify()
