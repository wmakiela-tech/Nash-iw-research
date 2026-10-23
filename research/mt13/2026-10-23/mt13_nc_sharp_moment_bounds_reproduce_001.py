#!/usr/bin/env python3
"""MT13 classical positive-source two-moment sharp bounds.
Independent finite-grid LP and random nonnegative source verification.
Requires numpy/scipy. NOT a physical Wu-Xu/BBN calculation.
"""
from math import exp, log, sqrt
import numpy as np
from scipy.optimize import linprog

T=1.0; GAMMA=2.0; LAMBDA=1.0; KAPPA=.12; E=2.0
N=1-exp(-2); a=exp(-GAMMA*T); qbar=N/E
def q(s): return exp(-GAMMA*(T-s))
def w(s): return KAPPA*GAMMA/(GAMMA-LAMBDA)*(exp(-LAMBDA*(T-s))-q(s))

lower=2*KAPPA*sqrt(a)/(1+sqrt(a))*(E-N)
upper=2*KAPPA*(sqrt(E*N)-N)
sstar=T+log(qbar)/GAMMA
assert abs(E*w(sstar)-upper)<1e-14
m0=E*(1-qbar)/(1-a)
mT=E-m0
assert abs(m0+mT-E)<1e-13
assert abs(m0*q(0)+mT*q(T)-N)<1e-13
assert abs(m0*w(0)+mT*w(T)-lower)<1e-13

for points in (121,401,1201):
    ss=np.linspace(0,T,points)
    qq=np.exp(-GAMMA*(T-ss))
    ww=KAPPA*GAMMA/(GAMMA-LAMBDA)*(np.exp(-LAMBDA*(T-ss))-qq)
    Aeq=np.vstack([np.ones(points),qq])
    lo=linprog(ww,A_eq=Aeq,b_eq=[E,N],bounds=(0,None),method="highs")
    hi=linprog(-ww,A_eq=Aeq,b_eq=[E,N],bounds=(0,None),method="highs")
    assert lo.success and hi.success
    assert abs(lo.fun-lower)<1e-9
    assert -hi.fun<=upper+1e-9
    assert upper+hi.fun<5e-6
    print(f"mesh={points}: min={lo.fun:.12f}, max={-hi.fun:.12f}, upper gap={upper+hi.fun:.3g}")

rng=np.random.default_rng(18181)
for _ in range(10000):
    time=rng.uniform(0,T,10)
    weights=rng.dirichlet(np.ones(10))
    nj=E*np.dot(weights,np.exp(-GAMMA*(T-time)))
    actual=E*np.dot(weights,np.array([w(t) for t in time]))
    lb=2*KAPPA*sqrt(a)/(1+sqrt(a))*(E-nj)
    ub=2*KAPPA*(sqrt(E*nj)-nj)
    assert lb-1e-12<=actual<=ub+1e-12

print("E,N,reactions",E,N,E-N)
print("exact lower/upper",lower,upper)
print("minimax midpoint,risk",(lower+upper)/2,(upper-lower)/2)
print("extremizer masses at endpoints",m0,mT,"upper event time",sstar)
print("PASS sharp analytic extremizers + 3 LP grids + 10,000 positive source distributions")
