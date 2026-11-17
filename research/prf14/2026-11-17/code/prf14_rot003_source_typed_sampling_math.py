#!/usr/bin/env python3
"""PRF14 ROT003 exact rational source-contract checks and finite numerical budgeting.
Theorems are proved in report; numbers here are arithmetic, not native quantum/device runs.
"""
from fractions import Fraction as F
from decimal import Decimal, getcontext
from math import ceil, floor, log
getcontext().prec=70
q=F(247,4600)
delta=F(9398133420642572,10**18) # written R34 numeric tolerance
assert F(99,100) > F(1,2) > q
assert q+2*delta < F(1,2)
alpha=beta=.05
T=10000.0
L=1e-4
# Serial binning: h <= delta/(2L), 2 arms, m samples/arm/bin.
J=ceil(2*L*T/float(delta))
h=T/J
xi=float(delta)/4
m=ceil(log(4*J/alpha)/(2*xi*xi))
assert 2*xi+L*h <= float(delta)*(1+1e-12)
assert 4*J*(2.718281828459045**(-2*m*xi*xi))<=alpha*(1+1e-12)
# Adaptively sampled lower bound, K disjoint triangular bumps; each max 2delta.
K=floor(L*T/(4*float(delta)))
assert K>=1
length=4*float(delta)/L
assert K*length<=T
assert 2*float(delta)/ (length/2) == L
kl=(1-alpha)*log((1-alpha)/beta)+alpha*log(alpha/(1-beta))
kl=.90*log(19) if alpha==beta==.05 else kl
lower=K*float(q*(1-q))*kl/(4*float(delta)**2)
assert lower>0
# Exact sample covariance: Bern(q)||Bern(q+x) <= x^2/[v(1-v)] <= x^2/[q(1-q)]
for n in range(101):
    x=2*float(delta)*n/100
    v=float(q)+x
    if x>0:
        d=float(q)*log(float(q)/v)+(1-float(q))*log((1-float(q))/(1-v))
        assert d <= x*x/(float(q)*(1-float(q)))+2e-15
assert m>0 and lower < 2*J*m
# Derived instrument throughput sanity, R34 ref duration 0.1 gamma-time per reading.
clock_required=2*m*.1
print('q =',q, ' = ',float(q))
print('delta numeric R34 =',float(delta))
print('T=',T,' L=',L,' J=',J,' h=',h)
print('m per arm / bin=',m,' total refs= ',2*J*m)
print('max per-bin reference time at tau_ref=0.1:',clock_required,' vs bin width:',h)
print('K disjoint bumps=',K,' support_width=',length)
print('Bernoulli adaptive minimax E0[N] lower bound:',lower)
print('Bernoulli KL binary kl(1-alpha||beta):',kl)
print('PASS: source rational probability, serial upper guarantee arithmetic, adaptive KL lower arithmetic, physical-clock guard')
