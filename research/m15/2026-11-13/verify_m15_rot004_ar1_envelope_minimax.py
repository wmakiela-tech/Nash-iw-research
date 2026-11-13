#!/usr/bin/env python3
"""M15 ROT004 pure Python exact-arithmetic algebra checks (not a minimax proof).
Run: python verify_m15_rot004_ar1_envelope_minimax.py
Writes a deterministic JSON adjacent to this script. Third party can rerun on Python3 stdlib.
"""
from fractions import Fraction as F
from pathlib import Path
import json

A=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))

def eye(n): return tuple(tuple(F(i==j) for j in range(n)) for i in range(n))
def matmul(A,B): return tuple(tuple(sum(a*b for a,b in zip(row,col)) for col in zip(*B)) for row in A)
def transpose(A): return tuple(zip(*A))
def sumall(A): return sum(sum(row) for row in A)
def ar1(m,rho): return tuple(tuple(rho**abs(i-j) for j in range(m)) for i in range(m))
def scorr_worst(): return tuple(tuple(F(1) if i==j else F(-1,3) for j in range(4)) for i in range(4))
def mmrisk(A,C,K,weights):
    # direct 4x3 linear propagator: E||sum w_k * A^T eps_k/4||² per sigma²
    S = matmul(matmul(transpose(A),C),A)
    temporal = sum(weights[i]*K[i][j]*weights[j] for i in range(len(weights)) for j in range(len(weights)))
    return temporal * sum(S[i][i] for i in range(3)) / 16

def inverse(M):
    n=len(M)
    work=[[F(x) for x in M[i]]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if work[i][k])
        work[k],work[pivot]=work[pivot],work[k]
        scale=work[k][k]
        work[k]=[x/scale for x in work[k]]
        for i in range(n):
            if i!=k:
                mul=work[i][k]
                work[i]=[x-mul*y for x,y in zip(work[i],work[k])]
    return tuple(tuple(row[n:]) for row in work)

def fmt(q):
    q=F(q)
    return str(q.numerator) if q.denominator==1 else f'{q.numerator}/{q.denominator}'

assert matmul(transpose(A),A)==tuple(tuple(F(4)*F(i==j) for j in range(3)) for i in range(3))
assert matmul(A,transpose(A))==tuple(tuple(F(4)*F(i==j)-1 for j in range(4)) for i in range(4))
assert all(sum(row[j] for row in A)==0 for j in range(3))
Cstar=scorr_worst(); Cind=eye(4); Ccommon=tuple(tuple(F(1) for j in range(4)) for i in range(4))
checks=3
cases=[]
for m in (1,2,3,4,5,7,10):
  for rho in (F(0),F(1,5),F(1,2),F(3,4),F(9,10)):
    Q=ar1(m,rho)
    den=F(m)-(m-2)*rho # equivalent m(1-rho)+2rho
    weights=[F(1)] if m==1 else [F(1)/den]+[ (1-rho)/den for i in range(m-2)]+[F(1)/den]
    exact=(1+rho)/den
    assert sum(weights)==1; checks+=1
    assert all(w>=0 for w in weights); checks+=1
    assert mmrisk(A,Cstar,Q,weights)==exact; checks+=1
    assert mmrisk(A,Cind,Q,weights)==F(3,4)*exact; checks+=1
    assert mmrisk(A,Ccommon,Q,weights)==0; checks+=1
    assert exact<=sumall(Q)/(m*m) # GLS no worse than uniform average at AR1 boundary
    checks+=1
    inv=inverse(Q)
    oneprec=sumall(inv)
    assert oneprec == 1/exact; checks+=1
    actual_weights=[sum(inv[i][j] for j in range(m))/oneprec for i in range(m)]
    assert actual_weights == weights; checks+=1
    if m>=3 and rho>0:
      # Lag-one bound alone permits equicorrelation at all distances, violating AR1 envelope.
      K_lag1only=tuple(tuple(F(1) if i==j else rho for j in range(m)) for i in range(m))
      assert K_lag1only[0][1]<=rho and K_lag1only[0][2]>rho**2
      checks+=1
    cases.append({'m':m,'rho':fmt(rho),'optimal_weights':[fmt(w) for w in weights],
                  'risk_per_sigma2':fmt(exact),'uniform_AR1_boundary_risk_per_sigma2':fmt(F(sumall(Q),m*m)),
                  'ratio_independent_within_group':fmt(F(3,4)*exact)})
assert mmrisk(A,Cstar,ar1(4,F(1,2)),[F(1,4)]*4)==F(33,64)
assert mmrisk(A,Cstar,ar1(4,F(1,2)),[F(1,3),F(1,6),F(1,6),F(1,3)])==F(1,2)
checks+=2
summary={'artifact_id':'IW_M15_ROT004_GEOMETRIC_DECAY_AR1_ENVELOPE_SHARP_MINIMAX_001_20261113',
 'class':'EXACT_CLASSICAL_FRACTION_TESTS_NOT_EMPIRICAL_SENSOR_OR_INDEPENDENT_REFEREE',
 'checks_passed':checks, 'rho_domain':'0 <= rho < 1',
 'k_envelope':'K PSD diag1; abs(K_ij)<=rho**abs(i-j); separable Sigma=sigma2*(K tensor C)',
 'sharp_minimax_risk':'sigma2*(1+rho)/(m*(1-rho)+2*rho)',
 'weight_pattern':'endpoints 1/[m-(m-2)*rho]; interiors (1-rho)/[m-(m-2)*rho] when m>=2',
 'cases':cases}
res=Path(__file__).with_name('m15_rot004_exact_results.json')
res.write_text(json.dumps(summary,sort_keys=True,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','checks_passed':checks,'m4_rho_half_sharp':'1/2','m4_rho_half_simple_average':'33/64','output':res.name},sort_keys=True))
