#!/usr/bin/env python3
"""Independent numerical diagnostics for PRF13 ROT006; not the exact proof.
Direct characteristic-function 8x8 D, independent partial trace over first qubit,
random generalized rank-one POVMs and one-way postmeasurement joint Helstrom.
"""
import math
import numpy as np
from numpy.linalg import eigvalsh
from itertools import product

X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex);I=np.eye(2,dtype=complex)
W=np.array(list(product((0,1),repeat=3)),dtype=int)

def D_exact(x):
    return np.array([[ (x**abs(sum(u-v)) - x**sum(abs(u-v)))/8
                for v in W] for u in W],dtype=complex)

def contract_A(D,n):
    # <n| D |n> on 4D BC via projector ((I+n·sigma)/2).
    A=(I+n[0]*X+n[1]*Y+n[2]*Z)/2
    D6=D.reshape(2,4,2,4)
    return np.einsum('ji,iajb->ab',A,D6,optimize=True)

def N(A,B):return np.kron(A,B)

def trn(A):return float(sum(abs(eigvalsh(A))))

def projective_value(x,n):
    D=D_exact(x);return (trn(contract_A(D,n))+trn(contract_A(D,-n)))/2

def random_povm_value(x,rng):
    # E_{j,+/-}=v_j (I +/- n_j.sigma)/2, each pair sums v_j I.
    # v_j>=0, sum_j v_j=1: Alice POVM has arbitrary 2R refined outputs.
    R=int(rng.integers(1,9));weights=rng.dirichlet(np.ones(R));D=D_exact(x)
    ans=0
    for weight in weights:
        n=rng.normal(size=3);n/=np.linalg.norm(n)
        ans+=weight*(trn(contract_A(D,n))+trn(contract_A(D,-n)))/2
    return ans


def main():
    rng=np.random.default_rng(2026111106)
    # Independent direct 8D partial contraction versus 4D Pauli pencil.
    for x in (0.7,math.exp(-1/3),.75):
        b=1-x*x
        for _ in range(64):
            r=rng.normal(size=3);r/=np.linalg.norm(r)
            rx,ry,_=r
            C=b*((N(X,X)+N(Y,Y)+rx*(N(X,I)+N(I,X))+ry*(N(Y,I)+N(I,Y)))/16
                 +x*(rx*(3*N(X,X)+N(Y,Y))+ry*(N(X,Y)+N(Y,X)))/32)
            assert np.max(np.abs(C-contract_A(D_exact(x),r)))<3e-15
    print('DIRECT_8X8_VS_PAULI_CONTRACTION: PASS')
    for x in (0.7,math.exp(-1/3),.75):
        b=1-x*x;bound=.48*b;HEL=.5*b
        peak=0;peakp=0
        for _ in range(2500):
            n=rng.normal(size=3);n/=np.linalg.norm(n)
            peak=max(peak,projective_value(x,n))
        for _ in range(2500):peakp=max(peakp,random_povm_value(x,rng))
        assert peak<=bound+1e-12 and peakp<=bound+1e-12
        assert HEL>bound
        print(f'x={x:.16f} exact_helstrom={HEL:.12f} bound={bound:.12f} '+
              f'certified_gap={HEL-bound:.12f} numeric_projective_sup_sample={peak:.12f} '+
              f'numeric_random_povm_sup_sample={peakp:.12f} projective_X={projective_value(x,np.array([1,0,0])):.12f}')
    # Witness that finite-round adaptive R08 is contained: exact closed expression.
    x=math.exp(-1/3);b=1-x*x
    V08=b*(4+3*x+max(2,3*x)+2*math.sqrt(4+(2-x)**2))/32
    assert abs(V08-.198464903476238)<1e-13
    assert V08<=.48*b
    print('R08_WITHIN_RESTRICTED_CLASS:',V08)
    print('PASS diagnostic only: independent 8x8 reconstruction / arbitrary-axis first projective / random POVM finite families')

if __name__=='__main__':main()
