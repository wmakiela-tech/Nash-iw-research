#!/usr/bin/env python3
"""PRF13 ROT012: exact six-parameter minimax sensitivity for two-time Pauli memory.

Source-restricted to exogenous two-step classical Pauli-label qubit combs.
Proof of global SO(3) optimality is algebraic in report; tests are not a substitute.
NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_DEVICE / REFEREE_PENDING.
"""
from itertools import product
from math import ceil, log, sqrt
import random
import sympy as sp

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
P = {'X': X, 'Y': Y, 'Z': Z}
G = list(product((0, 1), repeat=2))
PAIRS = list(product(G, G))
U = {v: X**v[0] * Z**v[1] for v in G}
ch = {'0': lambda v: 1,
      'X': lambda v: (-1)**v[1],
      'Y': lambda v: (-1)**(v[0] + v[1]),
      'Z': lambda v: (-1)**v[0]}
axes = ['X','Y','Z']

# Original source ROT011: first marginal, second marginal, xor law.
A = sp.Matrix([[int(v==g) for (v,w) in PAIRS] for g in G] +
              [[int(w==g) for (v,w) in PAIRS] for g in G] +
              [[int((v[0]^w[0],v[1]^w[1])==g) for (v,w) in PAIRS] for g in G])
assert A.shape==(12,16) and A.rank()==10 and len(A.nullspace())==6
B=[]
for a in axes:
    for b in axes:
        if a==b: continue
        d=sp.Matrix([sp.Rational(ch[a](v)*ch[b](w),16) for v,w in PAIRS])
        assert A*d==sp.zeros(12,1)
        B.append((a,b,d))
assert sp.Matrix.hstack(*(z[2] for z in B)).rank()==6
print('PASS_R011_SIX_DIMENSION_KERNEL_REDERIVATION')

V = -sp.I*(X+Y+Z)/sp.sqrt(3)
assert sp.simplify(V.H*V-I2)==sp.zeros(2)
R = sp.Matrix(3,3,lambda i,j:sp.simplify(sp.trace(P[axes[i]]*V*P[axes[j]]*V.H)/2))
Ropt=(sp.ones(3)*2-3*sp.eye(3))/3
assert R==Ropt and R*R.T==sp.eye(3) and R.det()==1
assert all(abs(R[i,j])==sp.Rational(2,3) for i in range(3) for j in range(3) if i!=j)
Rold=sp.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
min_old=min(abs(Rold[i,j]) for i in range(3) for j in range(3) if i!=j)
min_new=min(abs(R[i,j]) for i in range(3) for j in range(3) if i!=j)
assert min_old==sp.Rational(2,7)
assert min_new==sp.Rational(2,3)
assert min_new/min_old==sp.Rational(7,3)
assert (min_new/min_old)**2==sp.Rational(49,9)
print('PASS_UNITARY_SO3_EXACT_MINIMAX_CONSTRUCTION')
print('R_STAR =',R.tolist(),'old min =',min_old,'new min =',min_new)

# Exact physical Pauli comb distributions, any six small correlations.
cs=[sp.Rational(1,10),-sp.Rational(1,12),sp.Rational(1,15),
    -sp.Rational(1,20),sp.Rational(1,30),-sp.Rational(1,40)]
assert sum(abs(c) for c in cs)<1
p={(v,w):(1+sum(c*ch[a](v)*ch[b](w) for c,(a,b,_) in zip(cs,B)))/16 for (v,w) in PAIRS}
assert sum(p.values())==1 and all(z>0 for z in p.values())
assert A*sp.Matrix([p[z]-sp.Rational(1,16) for z in PAIRS])==sp.zeros(12,1)

# For ANY distribution p in the Pauli model, one fixed unitary gives
# E[Pauli_i at output | input +Pauli_j] = R_ij * C_(j,i).
for i,ai in enumerate(axes):
    for j,aj in enumerate(axes):
        rho=(I2+P[aj])/2
        obs=sp.simplify(sum(prob*sp.trace(P[ai]*U[w]*V*U[v]*rho*U[v].H*V.H*U[w].H)
                          for (v,w),prob in p.items()))
        coefficient=sp.simplify(sum(prob*ch[aj](v)*ch[ai](w) for (v,w),prob in p.items()))
        assert sp.simplify(obs - R[i,j]*coefficient)==0
        if i!=j:
            idx=next(k for k,(a,b,_) in enumerate(B) if a==aj and b==ai)
            assert coefficient==cs[idx]
            assert obs==sp.Rational(2,3)*cs[idx]
print('PASS_ALL_NINE_PHYSICAL_EXPECTATION_IDENTITIES_WITH_NONTRIVIAL_POSITIVE_DISTRIBUTION')

# Fourier inversion reconstructs entire joint Pauli-label probability table.
def ccoef(a,b):
    return sum(prob*ch[a](v)*ch[b](w) for (v,w),prob in p.items())
CH={a+b:ccoef(a,b) for a in ['0']+axes for b in ['0']+axes}
for v,w in PAIRS:
    recon=sum(CH[a+b]*ch[a](v)*ch[b](w) for a in ['0']+axes for b in ['0']+axes)/16
    assert recon==p[v,w]
print('PASS_COMPLETE_16_POINT_FOURIER_INVERSION_FOR_SOURCE_RESTRICTED_PAULI_COMB')

# Finite-shot quantitative bound for independent fresh repetitions, not a
# hardware assertion; an entirely synthetic witness at pre-specified n/alpha.
alpha=sp.Rational(1,100)
delta=sp.Rational(1,20)
n=ceil((sp.Rational(9,2)/delta**2)*log(12/float(alpha)))
nold=ceil((sp.Rational(49,2)/delta**2)*log(12/float(alpha)))
assert (n,nold)==(12763,69483)
print('n_per_setting_optimal =',n,'n_per_setting_previous =',nold)
print('six_setting_shots_optimal =',6*n,'previous =',6*nold)
print('Hoeffding simultaneous alpha = 0.01, max |C_hat-C| <= 0.05')
rng=random.Random(20261112)
observed=[]
for c in cs:
    mu=float(sp.Rational(2,3)*c)
    nplus=sum(rng.random()<(1+mu)/2 for _ in range(n))
    c_hat=sp.Rational(3,2)*sp.Rational(2*nplus-n,n)
    observed.append(float(c_hat-c))
assert max(abs(z) for z in observed)<float(delta)
print('PASS_PRESEEDED_SYNTHETIC_HOEFFDING_DEMONSTRATION max_error=',max(abs(z) for z in observed))
print('PASS_ROT012')
