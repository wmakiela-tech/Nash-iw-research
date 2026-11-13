#!/usr/bin/env python3
"""DAX-S8 ROT027: public source-typed restricted hard Q2 pion/e+-e- CSDA.
NOT full physical R68 pion stopping, full transport or neutrino production.
Actual 500+200 discrete trajectories and original inherited bytes are in the full ZIP.
"""
import json,math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq
from scipy.integrate import quad
M=.13957039; m=.00051099895069; T=.00007818527068831995
alpha=1/137.035999084; E0=718.2771443978552
n=4.9953665820687041e26;hc=1.973269804e-14;ctau_cm=780.45
qa=.001;qb=.010
q,wq=leggauss(36);mu,wm=leggauss(28)
x=16*(q+1);k=x*T;eps=np.hypot(k,m)
weights=16*wq*x*x*np.exp(-eps/T)/(1+np.exp(-eps/T))
weights/=weights.sum()
def rate_loss(E):
 p=math.sqrt(E*E-M*M);z=M*M+m*m+2*(E*eps[:,None]-p*k[:,None]*mu[None,:])
 lam=(z-(M+m)**2)*(z-(M-m)**2)
 A=z-M*M-m*m;B=z-m*m
 upper=np.minimum(qb,lam/z);u=np.where(upper>qa,upper,qa)
 fac=4*math.pi*alpha*alpha/lam
 sig=fac*(A*A*(1/qa-1/u)-B*np.log(u/qa))
 C=((E+eps[:,None])*(z+m*m-M*M)-2*z*eps[:,None])/lam
 loss=fac*C*(A*A*np.log(u/qa)-B*(u-qa))
 flux=np.sqrt(lam)/(2*p*eps[:,None])
 v=weights[:,None]*wm[None,:]*flux/2
 return float((v*sig).sum()*n*hc**2),float((v*loss).sum()*n*hc**2)
def decay_rate(E):return M/(ctau_cm*math.sqrt(E*E-M*M))
def survival(E):
 hazard=quad(lambda u:decay_rate(u)/rate_loss(u)[1],E,E0,epsrel=5e-8,limit=160)[0]
 return math.exp(-hazard)
R0,B0=rate_loss(E0)
Ecross=brentq(lambda E:rate_loss(E)[0]-decay_rate(E),1.5,2.2)
result={'status':'PASS_AUTHOR_RESTRICTED_HARD_WINDOW_CSDA_REPRO',
 'E_initial_GeV':E0,'Q2_range_GeV2':[qa,qb],
 'hard_collision_rate_initial_per_cm':R0,'initial_energy_loss_GeV_per_cm':B0,
 'instantaneous_scatter_decay_rate_crossover_E_GeV':Ecross,
 'survival_without_decay_to_100GeV_CSDA':survival(100),
 'survival_without_decay_to_20GeV_CSDA':survival(20),
 'limitations':'Only artificial vacuum one-photon hard Q2 slice, ideal massive FD source. Not full medium stopping, pion source ensemble, neutrino yield or PBH/BBN.'}
assert abs(result['initial_energy_loss_GeV_per_cm']/0.235819456140115-1)<1e-7
assert abs(Ecross/1.795145972-1)<1e-6
print(json.dumps(result,indent=2,sort_keys=True))
