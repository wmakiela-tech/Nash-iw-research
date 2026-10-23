#!/usr/bin/env python3
"""MT13 synthetic source cap theorem: exact bang-bang intervals versus independent LP.
Uses NumPy/SciPy; NOT a Wu-Xu Julia run, PBH, or a physical BBN prediction.
"""
import math
import numpy as np
from scipy.optimize import brentq, linprog
T=1.; gamma=2.; lam=1.; kappa=.12
E=2.; N=1-math.exp(-2)
def q(t): return math.exp(-gamma*(T-t))
def iq(a,b):return (q(b)-q(a))/gamma
def iw(a,b):
    la=(math.exp(-lam*(T-b))-math.exp(-lam*(T-a)))/lam
    return kappa*gamma/(gamma-lam)*(la-iq(a,b))
def exact(cap,e=E,n=N):
    L=e/cap
    assert 0<L<=T
    assert cap*iq(0,L)-1e-12<=n<=cap*iq(T-L,T)+1e-12
    if L==T:
        v=cap*iw(0,T)
        return (0,0,v,v)
    u=brentq(lambda t:cap*iq(t,t+L)-n,0,T-L,xtol=1e-14)
    ell=brentq(lambda t:cap*(iq(0,t)+iq(T-L+t,T))-n,0,L,xtol=1e-14)
    lo=cap*(iw(0,ell)+iw(T-L+ell,T))
    hi=cap*iw(u,u+L)
    assert abs(cap*iq(u,u+L)-n)<2e-12
    assert abs(cap*(iq(0,ell)+iq(T-L+ell,T))-n)<2e-12
    assert lo<=hi+1e-12
    return (u,ell,lo,hi)
def independent_lp(cap,npts):
    d=T/npts
    ss=np.arange(npts)*d
    Q=np.array([iq(float(s),float(s+d))/d for s in ss])
    W=np.array([iw(float(s),float(s+d))/d for s in ss])
    constraints=dict(A_eq=np.vstack([np.ones(npts),Q]),b_eq=[E,N],
                     bounds=(0,cap*d),method='highs')
    lo=linprog(W,**constraints);hi=linprog(-W,**constraints)
    assert lo.success and hi.success
    return lo.fun,-hi.fun
for cap in (2,4,8):
    u,ell,lo,hi=exact(cap)
    print('cap',cap,'max_middle_start',u,'min_left_length',ell,
          'sharp_interval',[lo,hi],'minimax_risk',(hi-lo)/2)
    for npts in (120,400,1200):
        plo,phi=independent_lp(cap,npts)
        assert max(abs(plo-lo),abs(phi-hi))<8e-6
        print('  mesh',npts,'LP',[plo,phi])
assert abs(exact(2)[3]-exact(2)[2])<1e-14
low0=2*kappa*math.exp(-1)/(1+math.exp(-1))*(E-N)
hi0=2*kappa*(math.sqrt(E*N)-N)
assert low0<exact(8)[2]<exact(4)[2]<exact(2)[2]
assert hi0>exact(8)[3]>exact(4)[3]>exact(2)[3]
rng=np.random.default_rng(20261023)
for _ in range(100):
    cap=4.;bins=80;dt=T/bins
    vals=cap*rng.random(bins)
    e=float(sum(vals)*dt)
    n=sum(float(vals[j])*iq(j*dt,(j+1)*dt) for j in range(bins))
    J=sum(float(vals[j])*iw(j*dt,(j+1)*dt) for j in range(bins))
    _,_,lo,hi=exact(cap,e,n)
    assert lo-2e-12<=J<=hi+2e-12
print('PASS: theorem endpoints, 9 independent LPs, 100 random bounded histories')
