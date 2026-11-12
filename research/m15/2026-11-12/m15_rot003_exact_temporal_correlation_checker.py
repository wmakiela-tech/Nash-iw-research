#!/usr/bin/env python3
"""M15 ROT003: exact Fraction checker for the separable temporal/cross-channel Gaussian minimax model.

Checks are algebraic negative controls, not an independent proof or sensor replay.
The full all-estimator diffuse Gaussian Bayes minimax proof is in the science report.
"""
from fractions import Fraction as F
from pathlib import Path
import json

A = ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1))

def dot(x, y):
    return sum(F(a)*F(b) for a,b in zip(x,y))

def eye(n):
    return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))

def equicorr(n, rho):
    rho=F(rho)
    return tuple(tuple(F(1) if i==j else rho for j in range(n)) for i in range(n))

def summatrix(M):
    return sum(sum(row) for row in M)

def tr_risk(m, K, C, sigma2=F(1)):
    # Exact trace of Cov[(1/(4m)) sum_k A^T epsilon_k] for Cov(vec eps)=sigma2 K tensor C.
    g = sum(C[i][j]*dot(A[i],A[j]) for i in range(4) for j in range(4))
    return F(sigma2)*summatrix(K)*g/F(16*m*m)

def frac(x):
    x=F(x)
    return str(x.numerator) if x.denominator==1 else f'{x.numerator}/{x.denominator}'

assert all(dot(tuple(A[i][j] for i in range(4)),tuple(A[i][k] for i in range(4)))==4*int(j==k) for j in range(3) for k in range(3))
assert all(sum(A[i][j] for i in range(4))==0 for j in range(3))
Cstar = tuple(tuple(F(1) if i==j else F(-1,3) for j in range(4)) for i in range(4))
assert summatrix(Cstar)==0
assert all(Cstar[i][i]==1 and sum(Cstar[i])==0 for i in range(4))
# Cstar=(4/3)P, eigenvalues (0,4/3,4/3,4/3): legal PSD; worst within-group.

checks=0
out=[]
for m in (1,2,3,4,7):
    for kap in (F(0),F(1,5),F(1,2),F(1)):
        K=equicorr(m,kap)
        # K=(1-kap)I + kap 11^T, eigenvalues 1-kap and 1+(m-1)*kap: legal PSD.
        assert summatrix(K)==m*(1+(m-1)*kap)
        checks+=1
        robust=F(1+(m-1)*kap,m)
        assert tr_risk(m,K,Cstar)==robust
        checks+=1
        assert tr_risk(m,K,eye(4))==F(3,4)*robust
        checks+=1
        assert tr_risk(m,K,equicorr(4,F(1)))==0
        checks+=1
        if kap<1:
            # K^{-1}1 = 1/(1+(m-1)kap) 1; Gaussian posterior likelihood
            # precision for each location component: 3/sigma2 * m/(1+(m-1)kap).
            gls_variance_component=F(1+(m-1)*kap,3*m)
            assert 3*gls_variance_component==robust
            checks+=1
        out.append({'m':m,'kappa':frac(kap),'risk_robust_per_sigma2':frac(robust),'independent_channels_same_time_K_risk':frac(F(3,4)*robust)})

assert tr_risk(4,equicorr(4,F(1,2)),Cstar)==F(5,8)
assert tr_risk(4,eye(4),Cstar)==F(1,4)
assert tr_risk(4,equicorr(4,F(1)),Cstar)==F(1)
checks+=3

report={
 'artifact_id':'IW_M15_ROT003_TETRAHEDRAL_SEPARABLE_TEMPORAL_CORRELATION_SHARP_MINIMAX_001_20261112',
 'status':'EXACT_FRACTION_CONTROLS_PASS_NOT_AN_INDEPENDENT_ALL_ESTIMATOR_PROOF_NOT_SENSOR_DATA',
 'exact_assertions_passed':checks,
 'marginal_variance':'sigma2',
 'model':'Cov(vec eps)=sigma2 K tensor C, diag K=diag C=1, |Kkl|<=kappa for k!=l, K,C PSD',
 'minimax_total_risk':'sigma2 * [1+(m-1)*kappa] / m',
 'limit_fixed_kappa':'sigma2 * kappa',
 'cases':out,
}
with Path(__file__).with_name('m15_rot003_results.json').open('w',encoding='utf-8') as f:
    json.dump(report,f,ensure_ascii=False,indent=2,sort_keys=True)
    f.write('\n')
print(json.dumps({'exact_assertions_passed':checks,'m4_kappa_half_risk':'5/8','m4_kappa0_risk':'1/4','m4_kappa1_risk':'1','status':'PASS'},sort_keys=True))
