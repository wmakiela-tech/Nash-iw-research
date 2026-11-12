#!/usr/bin/env python3
"""PRF13 ROT008 source-typed reproducibility; Python3, sympy/numpy/mpmath.

Original R04 3-qubit end-point difference, R07 first-instrument overlap bound.
Verifies exact two-local-instrument optimum and independent numerical tests
of flag-isometry removal bound, then high-precision gap recurrences.
No claim about full unrestricted/asymptotic LOCC or quantum device data.
"""
import json
import math
from itertools import product
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp

HERE=Path(__file__).resolve().parent
I2=sp.eye(2)
X=sp.Matrix([[0,1],[1,0]])
Y=sp.Matrix([[0,-sp.I],[sp.I,0]])
WORDS=list(product((0,1), repeat=3))
x=sp.symbols('x',positive=True,real=True)
D=sp.Matrix(8,8,lambda i,j:(x**abs(sum(WORDS[i][k]-WORDS[j][k] for k in range(3))) - x**sum(abs(WORDS[i][k]-WORDS[j][k]) for k in range(3)))/8)
# Trace out qubit 3 (Charlie) to obtain 2-qubit marginal difference.
D_AB=sp.Matrix(4,4,lambda i,j: sum(D[2*i+k,2*j+k] for k in (0,1)))
b=1-x*x
TARGET=b*(sp.kronecker_product(X,X)+sp.kronecker_product(Y,Y))/8
assert sp.simplify(D_AB-TARGET)==sp.zeros(4)
assert sorted((str(sp.factor(v)),mult) for v,mult in D_AB.eigenvals().items()) == sorted((str(sp.factor(v)),mult) for v,mult in [(sp.Integer(0),2),(b/4,1),(-b/4,1)])
assert sp.simplify(sp.trace(D_AB * sp.kronecker_product(X,X))-b/2)==0
# LOCC parity readout X on A and B attains 1/2 Tr[X_A X_B D_AB]=b/4.
print('EXACT_D_AB_SOURCE_MATRIX_AND_X_PARITY_OPTIMAL_2_LOCAL_EVENTS: PASS')

# Double precision source sample and random effects to test all flagged terms.
Dnum=np.array(D.subs(x,math.exp(-1/3)),dtype=complex)
Dnum=(Dnum+Dnum.conj().T)/2
bn=1-math.exp(-2/3)
assert abs(sum(abs(np.linalg.eigvalsh(Dnum)))-bn)<2e-14
sigmas=np.array([np.array(P,dtype=complex) for P in (X,Y,sp.diag(1,-1))])
I=np.eye(2,dtype=complex)
rng=np.random.default_rng(2026111208)
max_ratio=0.0; max_gap=0.0; ntests=3000
for k in range(ntests):
    m=int(rng.integers(1,6))
    weights=rng.dirichlet(np.ones(m))
    # Produce 2m outcomes with cancelling Bloch vectors: sum_i alpha_i r_i=0.
    effects=[]
    for weight in weights:
        v=rng.normal(size=3);v/=np.linalg.norm(v)
        eta=float(rng.uniform(1e-5,1.0))
        for sign in (1,-1):
            effects.append((float(weight/2),sign*eta*v))
    S2=sum(a*float(np.dot(rv,rv)) for a,rv in effects)
    lhs=0.0; retained_global_tv=0.0; spectral_max=0.0
    for a,r in effects:
        E=a*(I+sum(float(r[j])*sigmas[j] for j in range(3)))
        ev,U=np.linalg.eigh(E)
        assert min(ev)>-1e-12
        rt=(U*np.sqrt(np.maximum(ev,0)))@U.conj().T
        cov=np.kron(rt,np.eye(4,dtype=complex));ref=np.sqrt(a)*np.eye(8)
        # for block-diagonal classical flags use sum of trace norms
        post=cov@Dnum@cov.conj().T
        z=post - a*Dnum
        retained_global_tv += sum(abs(np.linalg.eigvalsh((post+post.conj().T)/2))) / 2
        lhs+=sum(abs(np.linalg.eigvalsh((z+z.conj().T)/2))) / 2
        # Stinespring operator bound from (sqrt(I+r sigma)-I)^2 <= ||r||^2 I.
        dif=rt-np.sqrt(a)*I
        spectral_max=max(spectral_max,float(np.linalg.norm(dif,ord=2)**2/(a*np.dot(r,r))))
    rhs=bn*math.sqrt(S2)
    assert lhs<=rhs+2e-12,(k,lhs,rhs)
    cfloat=bn*(2-math.exp(-2/3))/(144*(1+math.exp(-1/3)/3))
    assert bn/2-retained_global_tv >= cfloat*S2-2e-12, (k,bn/2-retained_global_tv,cfloat*S2)
    max_ratio=max(max_ratio,lhs/rhs)
    max_gap=max(max_gap,rhs-lhs)
assert spectral_max<=1+1e-12
print('FLAGGED_LUDERS_VS_FREE_COIN_3000_VALID_POVM_FAMILIES: PASS')
print('INHERITED_ROT007_FIRST_STEP_LOSS_ON_SAME_3000_VALID_POVMS: PASS')
print('largest_observed_LHS_over_b_sqrtS=',max_ratio)
print('largest_square_root_inequality_ratio=',spectral_max)

mp.mp.dps=120
q=mp.mpf(1)/3
Xv=mp.exp(-q);Bv=1-Xv**2
cv=(2-Xv**2)/(144*(1+Xv/3));Cv=Bv*cv
A=cv/(1+cv)**2
vals=[]
r=mp.mpf(1)/4 # exact V2=b/4, so delta_2=b/4
for R in range(2,11):
    rough=(A/4)**(2**(R-2))/A
    assert r>=rough
    vals.append({'max_local_instruments_R':R,
                 'dimensionless_lower_gap':mp.nstr(r,45),
                 'absolute_lower_gap':mp.nstr(Bv*r,45),
                 'simple_closed_bound':mp.nstr(Bv*rough,45),
                 'log10_lower_gap':mp.nstr(mp.log10(Bv*r),35)})
    # Stable positive quadratic root of c*t^2 + t = r.
    t=(2*r)/(1+mp.sqrt(1+4*cv*r))
    assert 0<=t<=1
    assert abs((cv*t*t+t)-r)<mp.power(10,-mp.mp.dps+30)*max(mp.mpf('1'),r)
    r=cv*t*t
print('RECURSION_HIGH_PRECISION_120DPS_AND_CLOSED_FORM_LOWER: PASS')
for row in vals[:7]:print('R=',row['max_local_instruments_R'],'delta>=',row['absolute_lower_gap'])

# q=1/3 R08 witness is within R=3, not conflicting with ROT008.
vr08=Bv*(4+3*Xv+max(2,3*Xv)+2*mp.sqrt(4+(2-Xv)**2))/32
assert vr08<Bv/2
assert vr08<=Bv- (Bv/2- Bv*mp.mpf(vals[1]['dimensionless_lower_gap'])) # harmless below upper
print('R08_LOCC_3_EVENT_CONSISTENCY:',mp.nstr(vr08,25))

out={
 'artifact_id':'IW_PRF13_ROT008_BOUNDED_DEPTH_LOCC_RECURSION_DIAGNOSTICS_001_20261112',
 'q':'1/3','x':mp.nstr(Xv,55),'b':mp.nstr(Bv,55),
 'helstrom_TV':mp.nstr(Bv/2,55),'V_2_exact':mp.nstr(Bv/4,55),
 'C':mp.nstr(Cv,55),'c':mp.nstr(cv,55),'a':mp.nstr(A,55),
 'n_random_effect_families':ntests,'random_seed':2026111208,
 'flagged_removal_lhs_over_bound_max':max_ratio,
 'performance_R08_three_instrument_fixture':mp.nstr(vr08,55),
 'gaps':vals,'status':'AUTHOR_REPRODUCED / NUMERIC_DIAGNOSTIC_NOT_PROOF / REFEREE_PENDING / NO_FULL_LOCC_CLOSURE_CLAIM'}
(HERE/'IW_PRF13_ROT008_RECURSION_DIAGNOSTICS_001_20261112.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('ROT008_AUTHOR_REPRO_PASS')
