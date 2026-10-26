#!/usr/bin/env python3
"""PRF12 R08. Exact three-party sequential LOCC witness for ideal equal n=3
static-Cauchy (A) versus independent Cauchy-Levy (B). No source-active pulses,
no dephasing of stored probes. Only NumPy required.

A: measure X. B: measure X if Alice got +, Y if Alice got -.
C: perform Helstrom optimal LOCAL qubit decision for the conditional pair.
The code independently diagonalizes the 8x8 density difference and the four
unnormalized conditional 2x2 states, then checks the closed-form LOCC witness.

This is a LOCC LOWER WITNESS (an UPPER bound on the unknown Helstrom-LOCC gap),
not an LOCC optimum and not a quantitative lower bound on that gap.
"""
import numpy as np
from itertools import product
from math import exp,sqrt,log

bitstrings=np.array(list(product((0,1),repeat=3)))
X=np.array([[0.,1.],[1.,0.]],complex)
Y=np.array([[0.,-1.j],[1.j,0.]],complex)
I=np.eye(2,dtype=complex)
H=np.array([[1.,1.],[1.,-1.]])/sqrt(2)

def difference(q):
    delta=bitstrings[:,None,:]-bitstrings[None,:,:]
    return (np.exp(-q*np.abs(np.sum(delta,axis=-1)))-
            np.exp(-q*np.sum(np.abs(delta),axis=-1)))/8

def closed_LOCC(q):
    x=exp(-q);b=1-x*x
    return b/32*(4+3*x+max(2,3*x)+2*sqrt(4+(2-x)**2))

def closed_X(q):
    x=exp(-q);b=1-x*x
    return b*(6+9*x)/32 if x>=2/3 else 3*b/8

def conditional_C(D,first,second,s,t):
    Pa=(I+s*first)/2;Pb=(I+t*second)/2
    Pab=np.kron(Pa,Pb)
    op=D.reshape(4,2,4,2)
    return np.einsum('ba,aibj->ij',Pab,op)

def witness(q):
    D=difference(q)
    tr_norm=lambda M:float(np.abs(np.linalg.eigvalsh((M+M.conj().T)/2)).sum())
    tv=.0
    blocks={}
    for s in (+1,-1):
        Bobs=X if s==+1 else Y
        for t in (+1,-1):
            C=conditional_C(D,X,Bobs,s,t)
            blocks[(s,t)]=C
            tv+=tr_norm(C)/2
    hel=tr_norm(D)/2
    U=np.kron(np.kron(H,H),H)
    xfull=np.abs(np.diag(U@D@U.conj().T).real).sum()/2
    return tv,hel,xfull,blocks

def check_block_formula(q,blocks):
    x=exp(-q);b=1-x*x;a=x*b
    target={
        (1,1):b/16*I+(b/8+3*a/32)*X,
        (1,-1):-b/16*I-3*a/32*X,
        (-1,1):-b/16*X+(b/16-a/32)*Y,
        (-1,-1):-b/16*X-(b/16-a/32)*Y
    }
    return max(np.max(np.abs(target[k]-blocks[k])) for k in target)

def main():
    for q in (.01,.05,.1,1/3,.8,1.,1.5,2.,5.):
        tv,hel,xfull,blocks=witness(q)
        x=exp(-q);b=1-x*x
        assert abs(hel-b/2)<1e-13
        assert abs(tv-closed_LOCC(q))<1e-13
        assert abs(xfull-closed_X(q))<1e-13
        assert check_block_formula(q,blocks)<1e-13
        print(f"q={q:.12g} Hel={hel:.12f} Xfull={xfull:.12f} "
              f"adaptive_LOCC={tv:.12f} improved={tv-xfull:+.12f}")
    xlo=2-4*sqrt(5)/5
    xhi=(-14+4*sqrt(21))/5
    assert xlo < 2/3 < xhi < 1
    print("strict_X_improvement_interval_in_q:",
          -log(xhi),-log(xlo))
    tv,hel,xfull,_=witness(1/3)
    print("q=1/3 positive_LOCC_gap_UNKNOWN; proved upper bound",
          hel-tv,"(from adaptive witness)")
    print("gap upper bound with old X witness",hel-xfull)
if __name__=="__main__":
    main()
