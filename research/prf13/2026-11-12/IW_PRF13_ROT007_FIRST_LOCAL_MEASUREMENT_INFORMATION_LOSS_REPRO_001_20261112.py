#!/usr/bin/env python3
"""PRF13 ROT007: exact first local measurement irrecoverable loss (source D(q)).
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_FULL_LOCC_CLOSURE_PROOF.
Python 3, sympy, numpy; direct theorem verifications and seeded diagnostics.
"""
import math
from itertools import product
import sympy as s
import numpy as np

I=s.eye(2);X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-s.I],[s.I,0]]);Z=s.diag(1,-1)
SX=[s.kronecker_product(v,s.eye(4)) for v in (X,Y,Z)]
words=list(product((0,1),repeat=3))
x=s.symbols('x',real=True)
D=s.Matrix(8,8,lambda i,j:(x**abs(sum(words[i][k]-words[j][k] for k in range(3)))
    -x**sum(abs(words[i][k]-words[j][k]) for k in range(3)))/8)
W=s.zeros(8,1);WB=s.zeros(8,1)
for i,w in enumerate(words):
    if sum(w)==1:W[i]=1/s.sqrt(3)
    if sum(w)==2:WB[i]=1/s.sqrt(3)
P=W*W.T+WB*WB.T
K=s.zeros(8);K[0,0]=K[7,7]=1
Q=s.eye(8)-P-K
DP=s.simplify(P*D*P)
DN=s.simplify(-Q*D*Q)
b=1-x*x
assert s.simplify(D-DP+DN)==s.zeros(8)
assert s.simplify(s.trace(DP+DN)-b)==0

H=s.Matrix(3,3,lambda i,j:s.factor(s.trace(DP*SX[i]*DN*SX[j])))
assert s.simplify(H[0,0]-b*b*(2-x*x)/144)==0
assert s.simplify(H[1,1]-b*b*(2+x*x)/144)==0
assert s.simplify(H[2,2]-b*b*(2+x*x)/36)==0
assert s.simplify(H[0,1])==0 and s.simplify(H[0,2])==0
assert s.simplify(H[1,2]+H[2,1])==0 # imaginary antisymmetry -> no real quadratic cross-term
assert s.simplify(s.trace((DP+DN)*SX[0])-b*x/3)==0
assert s.simplify(s.trace((DP+DN)*SX[1]))==0
assert s.simplify(s.trace((DP+DN)*SX[2]))==0
print('EXACT_SYMBOLIC_D_P_Q_AND_CROSS_PSD_H: PASS')
print('H_x/b²=',s.factor(H[0,0]/b**2),'H_y/b²=',s.factor(H[1,1]/b**2),
      'H_z/b²=',s.factor(H[2,2]/b**2))
print('H_yz=',H[1,2],'; hermitian pairing cancels for real Bloch vector')

xv=math.exp(-1/3);bv=1-xv*xv
lamb=s.lambdify(x,D,'numpy');lp=s.lambdify(x,DP,'numpy');ln=s.lambdify(x,DN,'numpy')
Dn=np.asarray(lamb(xv),dtype=complex);Dp=np.asarray(lp(xv),dtype=complex);Dm=np.asarray(ln(xv),dtype=complex)
Pnp=np.array(P,complex);Qnp=np.array(Q,complex)
assert np.linalg.norm(Dn-(Dp-Dm),ord='fro')<1e-12
assert min(np.linalg.eigvalsh(Dp))>-1e-12 and min(np.linalg.eigvalsh(Dm))>-1e-12
sigmas=[np.array(v,complex) for v in (X,Y,Z)]
N=lambda M: float(np.sum(np.abs(np.linalg.eigvalsh((M+M.conj().T)/2))))

rng=np.random.default_rng(20261112)
min_gap_bound=1e9;max_trace_error=0.
for k in range(2500):
    m=int(rng.integers(1,6))
    alpha=rng.dirichlet(np.ones(m))
    directions=rng.normal(size=(m,3));directions/=np.linalg.norm(directions,axis=1)[:,None]
    # valid POVM with balanced Bloch vectors: each direction has outcomes ±, weights alpha/2.
    data=[]
    for a,v in zip(alpha,directions):
        eta=float(rng.uniform(.0001,1))
        for sign in (1,-1):
            data.append((a/2,sign*eta*v))
    loss=0.;lb_exact=0.;strength=0.
    for a,r in data:
        Em=a*(np.eye(2,dtype=complex)+sum(r[j]*sigmas[j] for j in range(3)))
        evals,U=np.linalg.eigh(Em)
        assert min(evals)>-1e-13
        sqrtE=(U*np.sqrt(np.maximum(evals,0)))@U.conj().T
        S=np.kron(sqrtE,np.eye(4))
        Ap=S@Dp@S; Bp=S@Dm@S
        Ti=np.trace(Ap+Bp).real
        Zi=np.trace(Ap@Bp).real
        actual=(Ti-N(Ap-Bp))/2
        # Trace-distance vs trace-product overlap inequality:
        assert actual>=Zi/Ti-3e-13,(actual,Zi/Ti)
        formula_T=bv*a*(1+xv*r[0]/3)
        formula_Z=(bv*bv*a*a/144)*((2-xv*xv)*r[0]**2+
          (2+xv*xv)*r[1]**2+4*(2+xv*xv)*r[2]**2)
        max_trace_error=max(max_trace_error,abs(formula_T-Ti),abs(formula_Z-Zi))
        assert abs(formula_T-Ti)<4e-13
        assert abs(formula_Z-Zi)<4e-13
        lb_exact+=formula_Z/formula_T
        loss+=actual
        strength+=a*np.dot(r,r)
    c=bv*(2-xv*xv)/(144*(1+xv/3))
    assert loss>=lb_exact-1e-12
    assert lb_exact>=c*strength-1e-12
    min_gap_bound=min(min_gap_bound,loss-c*strength)
print('INDEPENDENT_NUMERIC_2500_RANDOM_POVMS: PASS')
print('max_formula_trace_error=',max_trace_error)
print('min_actual_loss_minus_universal_bound=',min_gap_bound)
print('q=1/3','x=',xv,'b=',bv,'C(x)=',c,'C(x)/Helstrom=',2*c/bv)

# Exact small-eta continuity: norm after measurement is continuous in eta,
# and at eta=0 the two outcomes each preserve half the operator D.
for eta in (0.0,1e-3,0.01,0.1,0.5,1.):
    kept=0.0
    for sign in (+1,-1):
        Em=(np.eye(2,dtype=complex)+sign*eta*np.array(X,complex))/2
        vals,UU=np.linalg.eigh(Em)
        sqE=(UU*np.sqrt(np.maximum(vals,0)))@UU.conj().T
        S=np.kron(sqE,np.eye(4));kept+=N(S@Dn@S)
    hel=bv/2
    delta=(bv-kept)/2
    assert delta>=c*eta*eta-1e-12
    if eta==0:assert abs(delta)<2e-14
    print('X_LUDERS_ETA',eta,'global_achievable_after_first=',kept/2,'global_loss=',delta,
        'quadratic_lower_bound=',c*eta*eta)
print('ROT007_ALL_CHECKS_PASS')
