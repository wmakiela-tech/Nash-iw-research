#!/usr/bin/env python3
"""MT13 / XH-S4 Q88: exact symmetric two-Gaussian minmax source calibration.
Synthetic complex LTI transfer only; NOT a GW, BH, NR or PBH computation.
Requirements numpy, scipy. Source scientific note in same directory.
"""
import numpy as np
from math import exp, acosh, sqrt
from scipy.optimize import minimize_scalar

L, ETA = 2., .01
astar=acosh(exp(4))/4
def src(w,a):
    return np.array([np.exp(-.5*(w-a)**2),np.exp(-.5*(w+a)**2)],dtype=complex)
def coverage(w,a):
    s=src(w,a)
    return float(np.vdot(s,s).real)
def m(a):
    return min(coverage(0.,a),coverage(2.,a))

assert abs(astar-1.1732658260877076)<1e-14
assert abs(coverage(0,astar)-coverage(2,astar))<3e-15
assert abs(m(0)-.03663127777746836)<2e-15
assert abs(m(astar)-.5048946334524498)<2e-14
opt=minimize_scalar(lambda a:-m(a),bounds=(0,3),method="bounded",
                    options={"xatol":1e-12})
assert opt.success and abs(opt.x-astar)<1e-5
for a in np.linspace(0,3,201):
    min_grid=min(coverage(w,a) for w in np.linspace(-2,2,201))
    assert abs(min_grid-m(a))<2e-5
base_bound=ETA/sqrt(m(0))
opt_bound=ETA/sqrt(m(astar))
assert abs(base_bound-.0522485167412168)<2e-14
assert abs(opt_bound-.0140734191569283)<2e-14

# 4 x 13 x 400 = 20,800 arbitrary complex noise realizations, and
# 52 independent EXACT adversarial saturation directions.
rng=np.random.default_rng(20261024)
for a in [0.,.5,astar,1.6]:
    for w in np.linspace(-2,2,13):
        s=src(w,a); ss=np.vdot(s,s)
        h=complex(rng.normal(),rng.normal())
        for _ in range(400):
            e=rng.normal(size=2)+1j*rng.normal(size=2)
            e=e/np.linalg.norm(e)*ETA*rng.random()
            hhat=np.vdot(s,s*h+e)/ss
            assert abs(hhat-h)<=ETA/np.linalg.norm(s)+2e-14
        e=ETA*s/np.linalg.norm(s)
        hhat=np.vdot(s,s*h+e)/ss
        assert abs(abs(hhat-h)-ETA/np.linalg.norm(s))<3e-14

# Calibration gauge: H->qH, s_j->s_j/q preserves all complex observations
# and all relative source ratios. Phase-changing transfers preserve intensities.
w=np.linspace(-2,2,2001)
H=np.exp(1j*(.2+.13*w))/(.5+1j*(w-.3))
q=(1+.15*np.cos(w))*np.exp(1j*(.4+.3*w))
S=np.stack([np.exp(-.5*(w-astar)**2),np.exp(-.5*(w+astar)**2)])
Y=H[None,:]*S
assert np.max(np.abs(Y-(H*q)[None,:]*(S/q[None,:])))<8e-15
assert np.max(np.abs(S[0]/S[1]-(S/q[None,:])[0]/(S/q[None,:])[1]))<5e-12
phase_H=H*np.exp(1j*.8*w*w)
assert np.max(np.abs(np.abs(Y)**2-np.abs(S*phase_H[None,:])**2))<1e-13

s=src(1.2,astar)
h0=1+0j
assert np.linalg.norm(s*(h0+3*ETA/np.linalg.norm(s)-h0))>2*ETA
assert np.linalg.norm(s*(h0+ETA/np.linalg.norm(s)-h0))<2*ETA
assert abs(np.exp(-8)-.00033546262790251185)<1e-15

print("a_star",astar)
print("min_information_baseline",m(0),"min_information_opt",m(astar))
print("worst_error_baseline",base_bound,"worst_error_opt",opt_bound,
      "gain",base_bound/opt_bound)
print("PASS 20800 random noise, 52 sharp adversaries, gauge, phase, 2eta, scalar and grid optimization")
