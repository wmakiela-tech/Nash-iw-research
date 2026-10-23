#!/usr/bin/env python3
"""MT13 NC+LT5 event-conditioned source sufficiency witness; CLASSICAL SYNTHETIC ONLY.
Requires scipy,numpy. Analytic pulse convolutions independently checked by ODE DOP853.
"""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import solve_ivp
G, MU, LA, K, BETA, C = 2.,.7,1.,.12,.4,1.37
A=(.05,.30,.57);WIDTH=.08;BASE=2.;X0=.1
def H(r,t):return -math.expm1(-r*t)/r
def P(r,t,a):
    hi=min(t,a+WIDTH)
    if hi<=a:return 0.
    return (math.exp(-r*(t-hi))-math.exp(-r*(t-a)))/(r*WIDTH)
q=np.array([P(G,1,a) for a in A])
v=np.array([q[1]-q[2],q[2]-q[0],q[0]-q[1]])
v=v/max(abs(v))
assert abs(sum(v))<1e-14 and abs(q@v)<1e-14
def E(t,z):return BASE*t+sum(z[i]*max(0.,min(1.,(t-a)/WIDTH)) for i,a in enumerate(A))
def n(r,t,z):return BASE*H(r,t)+sum(z[i]*P(r,t,a) for i,a in enumerate(A))
def X(t,z):
    return (math.exp(-LA*t)*X0+K*G/(G-LA)*
            (BASE*(H(LA,t)-H(G,t))+sum(z[i]*(P(LA,t,a)-P(G,t,a)) for i,a in enumerate(A))))
def TH(t,z):return 2-C*t+BETA/MU*(E(t,z)-n(MU,t,z))
def event(z):return brentq(lambda t:TH(t,z)-1,.7,1.1,xtol=1e-14)
def S(t,z):return BASE+sum(z[i]/WIDTH for i,a in enumerate(A) if a<=t<a+WIDTH)
zp,zm=.1*v,-.1*v
assert abs(E(1,zp)-E(1,zm))<1e-14 and abs(n(G,1,zp)-n(G,1,zm))<1e-14
assert min(S(t,z) for z in (zp,zm) for t in np.linspace(0,1.2,10001))>.7
for z in (zp,zm):
    assert max(BETA*n(MU,t,z) for t in np.linspace(0,1.2,2001))<C
tp,tm=event(zp),event(zm)
yp,ym=X(tp,zp),X(tm,zm)
assert abs(tp-tm)>1e-4 and abs(yp-ym)>1e-5
def independent(z):
    tbreak=sorted(set([0.,1.2]+[x for a in A for x in (a,a+WIDTH)]))
    y=np.array([0.,0.,X0,2.])
    for lo,hi in zip(tbreak[:-1],tbreak[1:]):
        s=S((lo+hi)/2,z)
        def f(t,y):return [s-G*y[0],s-MU*y[1],-LA*y[2]+K*G*y[0],-C+BETA*y[1]]
        sol=solve_ivp(f,(lo,hi),y,method='DOP853',rtol=1e-12,atol=1e-14,dense_output=True)
        assert sol.success
        if (sol.sol(lo)[3]-1)*(sol.sol(hi)[3]-1)<=0:
            t=brentq(lambda u:sol.sol(u)[3]-1,lo,hi,xtol=1e-14)
            return t,sol.sol(t)[2]
        y=sol.y[:,-1]
    raise AssertionError('No event')
for z,t,x in [(zp,tp,yp),(zm,tm,ym)]:
    tc,xc=independent(z)
    assert abs(tc-t)<4e-11 and abs(xc-x)<4e-11
zero=np.zeros(3)
t0=event(zero)
xdot=-LA*X(t0,zero)+K*G*n(G,t0,zero)
Tdot=-C+BETA*n(MU,t0,zero)
wx=np.array([K*G/(G-LA)*(P(LA,t0,a)-P(G,t0,a)) for a in A])
wt=np.array([BETA/MU*(1-P(MU,t0,a)) for a in A])
w=wx-xdot/Tdot*wt
slope=float(w@v)
for eps in (.1,.01,.001):
    yplus=X(event(eps*v),eps*v)
    yminus=X(event(-eps*v),-eps*v)
    assert abs((yplus-yminus)/(2*eps)-slope)<2e-5*eps**2+2e-10
print('v',v,'same E',E(1,zp),E(1,zm),'same survivor',n(G,1,zp),n(G,1,zm))
print('same reactions',E(1,zp)-n(G,1,zp),E(1,zm)-n(G,1,zm))
print('event times',tp,tm,'event X',yp,ym,'delta',yp-ym)
print('fixed-time X',X(1,zp),X(1,zm))
print('baseline clock sensitivity',Tdot,'event moment vector',w,'slope',slope)
print('PASS moment kernel, positivity, event slope, independent DOP853, IFT finite difference')
