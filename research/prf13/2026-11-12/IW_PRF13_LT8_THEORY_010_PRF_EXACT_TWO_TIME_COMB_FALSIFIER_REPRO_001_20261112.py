#!/usr/bin/env python3
"""PRF13 for LT8-THEORY-010-PRF: exact qubit 2-step process-comb falsifier.

All matrices and outcome probabilities in exact SymPy rational Gaussian arithmetic.
Single-time and endpoint CPTP channels coincide, complete CP-instrument
histories do not. No novel theory, LOCC claim, or physical-device data.
"""
from itertools import product
from sympy import Matrix, eye, I, Rational, kronecker_product, zeros, simplify

Id=eye(2)
X=Matrix([[0,1],[1,0]])
Z=Matrix([[1,0],[0,-1]])
Y=Matrix([[0,-I],[I,0]])
labels=list(product([0,1],repeat=2))
unitary={v: X**v[0]*Z**v[1] for v in labels}
F=lambda v: (v[1],v[0]^v[1])
add=lambda v,w: (v[0]^w[0],v[1]^w[1])
p_corr={(v,w):(Rational(1,4) if w==F(v) else 0) for v in labels for w in labels}
p_ind={(v,w):Rational(1,16) for v in labels for w in labels}

# End-to-end map without a laboratory intervention; exact Pauli basis suffices.
def noise_channel(p,step,B):
    out=zeros(2)
    for (v,w),prob in p.items():
        u=unitary[v if step==1 else w]
        out+=prob*u*B*u.H
    return out

def endpoint_channel(p,B):
    out=zeros(2)
    for (v,w),prob in p.items():
        u=unitary[w]*unitary[v]
        out+=prob*u*B*u.H
    return out

for v in labels:
    assert sum(p_corr[(v,w)] for w in labels)==Rational(1,4)
    assert sum(p_corr[(w,v)] for w in labels)==Rational(1,4)
    assert sum(p_ind[(v,w)] for w in labels)==Rational(1,4)
    assert sum(p_ind[(w,v)] for w in labels)==Rational(1,4)
    assert sum(p_corr[(u,w)] for u in labels for w in labels if add(u,w)==v)==Rational(1,4)
    assert sum(p_ind[(u,w)] for u in labels for w in labels if add(u,w)==v)==Rational(1,4)
assert len(set(F(v) for v in labels))==4
assert len(set(add(v,F(v)) for v in labels))==4
for B in (Id,X,Y,Z):
    expected=Id if B==Id else zeros(2)
    for p in (p_corr,p_ind):
        for k in (1,2):assert noise_channel(p,k,B)==expected
        assert endpoint_channel(p,B)==expected
print('PASS: both stepwise CPTP maps and endpoint CPTP map equal completely depolarizing qubit channel')

# Legitimate instrument A_a(sigma)=K_a sigma K_a^dagger, K_a=|Y+><a|.
ket0=Matrix([1,0]);ket1=Matrix([0,1]);ketY=(ket0+I*ket1)/2**Rational(1,2)
P0=ket0*ket0.H
Ka={0:ketY*ket0.H,1:ketY*ket1.H}
assert simplify(sum((k.H*k for k in Ka.values()),zeros(2))-Id)==zeros(2)
Mp={+1:(Id+Y)/2,-1:(Id-Y)/2}
assert sum(Mp.values(),zeros(2))==Id
assert simplify(ketY.H*Y*ketY)[0,0]==1

def distribution(p):
    out={}
    for a in (0,1):
        for y in (+1,-1):
            chance=0
            for (v,w),prob in p.items():
                rho=unitary[v]*P0*unitary[v].H
                sigma=Ka[a]*rho*Ka[a].H
                tau=unitary[w]*sigma*unitary[w].H
                chance+=prob*(Mp[y]*tau).trace()
            out[(a,y)]=simplify(chance)
    assert sum(out.values())==1
    return out

Pc=distribution(p_corr);Pi=distribution(p_ind)
for a,y in Pc:
    assert Pc[(a,y)]==(Rational(1,2) if y==(-1)**a else 0)
    assert Pi[(a,y)]==Rational(1,4)
tv=sum(abs(Pc[z]-Pi[z]) for z in Pc)/2
assert tv==Rational(1,2)
print('Correlated instrument+Y outcome: ',Pc)
print('Independent instrument+Y outcome:',Pi)
print('PASS: matched endpoint CPTP yet legal history total variation=',tv)

# Choi J_U = |U>> <<U| with output index first and input index second,
# J_{1} (S1_in,S0) tensor J_{2} (S2,S1_out), dimension 16x16.
def J(U):
    vec=Matrix([U[i,j] for i in range(2) for j in range(2)])
    return vec*vec.H

def comb(p):
    W=zeros(16)
    for (v,w),prob in p.items():
        W+=prob*kronecker_product(J(unitary[v]),J(unitary[w]))
    return W

def tr_subsystem(A,dims,sub):
    # generic exact partial trace, with output indices interpreted tensorially
    out_dims=[d for j,d in enumerate(dims) if j!=sub]
    N=1
    for d in out_dims:N*=d
    dsub=dims[sub]
    def flatten(t,ds):
        r=0
        for value,d in zip(t,ds):r=r*d+value
        return r
    R=zeros(N)
    others=list(product(*(range(d) for d in out_dims)))
    for ia,a in enumerate(others):
        for ib,b in enumerate(others):
            for k in range(dsub):
                ax=list(a);bx=list(b)
                ax.insert(sub,k);bx.insert(sub,k)
                R[ia,ib]+=A[flatten(ax,dims),flatten(bx,dims)]
    return R

Wc=comb(p_corr);Wi=comb(p_ind)
assert Wc!=Wi
assert Wc.trace()==Wi.trace()==4
# A PSD certificate exists constructively since convex mixtures of J(U1) x J(U2).
for W in (Wc,Wi):
    # order (S1_in,S0,S2,S1_out): trace future output S2 (index2)
    first=tr_subsystem(W,[2,2,2,2],2)
    # remaining order (S1_in,S0,S1_out) -> J_depol(S1_in,S0) tensor I(S1_out)
    Jdep=kronecker_product(Id,Id)/2
    assert first==kronecker_product(Jdep,Id)
    assert tr_subsystem(Jdep,[2,2],0)==Id
    assert W.is_hermitian
    ev=W.eigenvals()
    assert all(lam.is_nonnegative for lam in ev)
print('PASS: Choi 2-step comb PSD, trace=4, recursive causal identities for both processes')
print('W_corr - W_ind Frobenius norm squared=',((Wc-Wi).H*(Wc-Wi)).trace())
print('PASS ALL exact quantum two-time instrument / comb tests')
