#!/usr/bin/env python3
"""MT13 classical four-cell fixed-T event-clock ledger. Synthetic only, NOT Wu-Xu."""
from math import exp
import numpy as np
from scipy.integrate import solve_ivp
keys=('00','10','01','11')
rates={'00':(.2,.4),'10':(.3,.5),'01':(.4,.2),'11':(.5,.3)}
speed={'00':1.,'10':.8,'01':1.2,'11':.7}
w={'00':1,'10':-1,'01':-1,'11':1}
def x(k,t):
    a,b=rates[k];r=a+b
    return a/r+(.5-a/r)*exp(-r*t)
def fact(y):return sum(w[k]*y[k] for k in keys)
assert all(abs(fact({k:rates[k][j] for k in keys}))<1e-15 for j in (0,1))
common=fact({k:x(k,1) for k in keys})
event=fact({k:x(k,1/speed[k]) for k in keys})
clock=sum(w[k]*(x(k,1/speed[k])-x(k,1)) for k in keys)
assert common<0<event and abs(event-common-clock)<2e-15
def rhs(s,z):
    y={k:z[i] for i,k in enumerate(keys)}
    f={k:rates[k][0]/speed[k] for k in keys}
    q={k:sum(rates[k])/speed[k] for k in keys}
    d=[f[k]-q[k]*y[k] for k in keys]
    L=y['10']-y['00'];M=y['01']-y['00']
    direct=fact(f)-y['00']*fact(q)
    fb_m=-M*(q['11']-q['01'])
    fb_l=-L*(q['11']-q['10'])
    return d+[-q['11']*z[4]+direct,-q['11']*z[5]+fb_m,
              -q['11']*z[6]+fb_l]
sol=solve_ivp(rhs,(0,1),[.5]*4+[0]*3,method='DOP853',
              rtol=1e-13,atol=1e-15,max_step=.005,dense_output=True)
assert sol.success
errs=[]
for s in np.linspace(0,1,101):
    z=sol.sol(s)
    errs.append(abs(z[3]-z[1]-z[2]+z[0]-sum(z[4:])))
    for i,k in enumerate(keys):
        assert abs(z[i]-x(k,s/speed[k]))<2e-13
assert max(errs)<2e-13
pure_clock=.1*sum(w[k]/speed[k] for k in keys)
assert abs(pure_clock-.034523809523809526)<1e-15
print('common-time I=',common)
print('clock correction=',clock)
print('fixed-T I=',event)
print('effective direct, feedback M, feedback L=',sol.y[4:,-1])
print('max dynamic ledger residual=',max(errs))
print('pure-clock factorial witness=',pure_clock)
print('PASS exact source-to-event and 3-term ledger tests; synthetic only')
