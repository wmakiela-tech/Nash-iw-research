#!/usr/bin/env python3
"""DAX-S8 ROT021 public simple one-dimensional soft pion Compton Born gate.
Requires mpmath. Uses *mean* pion energy from ROT020 fiducial Belle source,
not its full distribution. Not a physical hadronic rate or a neutrino yield.
"""
import json
import mpmath as mp
mp.mp.dps=45
D=mp.mpf
E=D('1436554.2887957103949794121053812220057194965')/2
m=D('139.57039'); T=D('0.07818527068831995')
ctau_m=D('7.8045'); alpha=1/D('137.035999084')
hbarc_cm=D('1.973269804e-11'); cap=m/20
n=2*mp.zeta(3)/mp.pi**2*(T/hbarc_cm)**3
sigmaT=8*mp.pi/3*(alpha/m)**2*hbarc_cm**2
z,w=mp.gauss_quadrature(16,'legendre')
def R(omega):
 a=omega/m
 return D(3)/8*sum(v*(1+x*x)/(1+a*(1-x))**2 for x,v in zip(z,w))
gamma=E/m;beta=mp.sqrt(1-1/gamma**2)
gt=gamma*T;tmin=1-beta;tmax=1+beta
def lw(omega):
 if omega==0:return D(0)
 return mp.log(-mp.expm1(-omega/(gt*tmin)))-mp.log(-mp.expm1(-omega/(gt*tmax)))
pts=[D(0),gt*tmin,cap/10,cap/2,cap]
def integral(scale):
 return sum(mp.quad(lambda om:om*lw(om)*scale(om),[a,b]) for a,b in zip(pts,pts[1:]))/(4*beta*mp.zeta(3)*gt**2)
fth=integral(lambda om:D(1));fb=integral(R)
mean_free_m=beta/(n*sigmaT*fb)/100
mean_decay_m=beta*gamma*ctau_m
tau=mean_decay_m/mean_free_m
floor=(1+2*cap/m)**(-2)
tau_lower=gamma*(ctau_m*100)*n*sigmaT*fth*floor
assert mp.almosteq(tau,gamma*(ctau_m*100)*n*sigmaT*fb,rel_eps=D('1e-35'))
assert tau>=tau_lower
assert abs(tau-D('83.7872064457678'))<D('1e-10')
print(json.dumps({'status':'PASS_POINT_SCALAR_SOFT_BORN_TWO_PROCESS_ONLY',
 'n_photon_cm3':mp.nstr(n,22),'soft_flux_fraction_Thomson':mp.nstr(fth,22),
 'mfp_soft_Compton_m':mp.nstr(mean_free_m,22),
 'mfp_vacuum_decay_m':mp.nstr(mean_decay_m,22),
 'scatter_over_decay_first_hazard':mp.nstr(tau,22),
 'P_decay_first':mp.nstr(1/(1+tau),22),
 'lower_scatter_over_decay_bound_in_point_Born':mp.nstr(tau_lower,22),
 'limitations':'No pion energy distribution folding, physical composite-pion corrections, post-scattering energy transfer, eventual pion survival or PBH/BBN result'},indent=2,sort_keys=True))
