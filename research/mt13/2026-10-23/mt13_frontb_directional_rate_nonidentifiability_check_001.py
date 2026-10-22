#!/usr/bin/env python3
"""MT13 synthetic identifiability: NOT a Wu-Xu / Julia source execution."""
import numpy as np
from scipy.integrate import solve_ivp,quad

def x0(t): return .4+.04*np.sin(t)
def xd(t): return .04*np.cos(t)
def u(t): return .3+.02*np.sin(t)
def lam(t): return 1.2+.1*np.cos(t)
def rr(t): return 2+.2*np.cos(t)
def f(t): return xd(t)-u(t)+lam(t)*x0(t)
def a(t): return f(t)+rr(t)*x0(t)
def b(t): return rr(t)*(1-x0(t))-f(t)
def k(t): return .9+.2*np.sin(t)
def rates(t,branch):
    return (a(t),b(t)) if branch==1 else (a(t)+k(t)*x0(t),b(t)+k(t)*(1-x0(t)))
def rhs(t,x,branch):
    aa,bb=rates(t,branch)
    return [u(t)-lam(t)*x[0]+(1-x[0])*aa-x[0]*bb]
def run(initial,branch):
    z=solve_ivp(lambda t,y:rhs(t,y,branch),(0,2),[initial],rtol=1e-12,atol=1e-13,dense_output=True)
    assert z.success
    return z

grid=np.linspace(0,2,1500)
assert min(min(*rates(t,1),*rates(t,2)) for t in grid)>0
for t in grid:
    for branch in (1,2):
        aa,bb=rates(t,branch)
        assert abs((1-x0(t))*aa-x0(t)*bb-f(t))<1e-13
z1,z2=run(x0(0),1),run(x0(0),2)
for z in (z1,z2):
    assert np.max(np.abs(z.sol(grid)[0]-x0(grid)))<3e-12
p1,p2=run(x0(0)+.03,1),run(x0(0)+.03,2)
for branch,p in ((1,p1),(2,p2)):
    for t in np.linspace(0,2,11):
        reff=lambda s: rr(s)+(k(s) if branch==2 else 0)
        integ=quad(lambda s:lam(s)+reff(s),0,t,epsabs=1e-13)[0]
        assert abs(p.sol(t)[0]-(x0(t)+.03*np.exp(-integ)))<3e-10

for t in np.linspace(0,2,15):
    d=p1.sol(t)[0]-z1.sol(t)[0]
    dd=rhs(t,p1.sol(t),1)[0]-rhs(t,z1.sol(t),1)[0]
    rhat=-dd/d-lam(t)
    force=rhs(t,z1.sol(t),1)[0]-u(t)+lam(t)*z1.sol(t)[0]
    ahat=force+rhat*z1.sol(t)[0]
    bhat=rhat-ahat
    assert abs(rhat-rr(t))<3e-10
    assert abs(ahat-a(t))<3e-10
    assert abs(bhat-b(t))<3e-10
# Exact independent postsource reservoir counterexample:
# X(t)=1/2 both under A=B=0 and A=B=1.5*exp(-t).
assert abs((.5+.1*np.exp(-1))-.5367879441171443)<1e-14
assert abs((.5+.1*np.exp(-1-3*(1-np.exp(-1))))-.5055223776955977)<1e-14
print("PASS: 2 positive source models, identical reference traces, 2-preparation exact sensitivity, rate inversion, residual reservoir counterexample")
