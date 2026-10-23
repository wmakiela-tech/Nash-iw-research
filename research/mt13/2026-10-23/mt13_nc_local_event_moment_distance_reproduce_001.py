#!/usr/bin/env python3
"""MT13: best affine approximation to LT5 event sensitivity kernel.
Classical synthetic signed measure TV duality; NOT finite-amplitude positive-source bound.
"""
from math import exp, expm1
import numpy as np
from scipy.optimize import linprog,brentq,minimize_scalar
G=2.; MU=.7; LA=1.;K=.12;BETA=.4;C=1.37;X0=.1;S0=2.
def H(r,t):return -expm1(-r*t)/r
def n(t):return S0*H(G,t)
def h(t):return S0*H(MU,t)
def x(t):return X0*exp(-LA*t)+K*G/(G-LA)*S0*(H(LA,t)-H(G,t))
def theta(t):return 2-C*t+BETA/MU*(S0*t-h(t))
tau=brentq(lambda t:theta(t)-1,.7,1.1,xtol=1e-14)
xdot=-LA*x(tau)+K*G*n(tau)
thetadot=-C+BETA*h(tau)
def q(s):return exp(-G*(1-s))
def ww(s):
    dt=tau-s
    kx=K*G/(G-LA)*(exp(-LA*dt)-exp(-G*dt))
    kth=BETA/MU*(-expm1(-MU*dt))
    return kx-xdot/thetadot*kth
ss=np.linspace(0,.7,1701)
qs=np.array([q(t) for t in ss]); ws=np.array([ww(t) for t in ss])
nn=len(ss)
mat=np.vstack([np.column_stack([-np.ones(nn),-qs,-np.ones(nn)]),
               np.column_stack([np.ones(nn),qs,-np.ones(nn)])])
res=linprog([0,0,1],A_ub=mat,b_ub=np.r_[-ws,ws],
            bounds=[(None,None),(None,None),(0,None)],method="highs")
assert res.success
a,b,d=res.x
error=lambda s:ww(s)-a-b*q(s)
dense=np.linspace(0,.7,20001)
dmax=max(abs(error(float(t))) for t in dense)
assert dmax-d<4e-8
middle=minimize_scalar(lambda t:-error(t),bounds=(.3,.55),method="bounded",
                       options={'xatol':1e-14}).x
times=np.array([0.,middle,.7])
q3=np.array([q(t) for t in times])
w3=np.array([ww(t) for t in times])
z=np.array([q3[1]-q3[2],q3[2]-q3[0],q3[0]-q3[1]])
z=z/np.sum(np.abs(z))
assert abs(np.sum(z))<1e-14 and abs(np.dot(z,q3))<1e-14
signed_witness=np.dot(z,w3)
assert abs(abs(signed_witness)-dmax)<2e-9
print("baseline crossing tau",tau,"Xd/Theta_d",xdot/thetadot)
print("best affine a,b",a,b,"LP radius",d,"dense upper",dmax)
print("annihilator event times",times.tolist(),"signed weights",z.tolist())
print("lower witness",signed_witness)
print("PASS two-moment Hahn-Banach TV dual numerical upper+lower witness")
