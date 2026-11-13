#!/usr/bin/env python3
"""DAX-S8 ROT022 public standalone POINT-SCALAR QED soft pion Compton
first and second photon LAB energy gain moments; not physical hadron QCD.
Fixed pion input is the ROT020 *source-conditional mean*, NOT full Belle source.
Requires mpmath>=1.3. See full ROT022 bundle for independently executed
direct x/t/z SciPy source and explicit on-shell 4-vectors.
"""
import json
import mpmath as mp
mp.mp.dps=36
D=mp.mpf
E=D('718277.144397855197489706052690611') # MeV, ROT020 real Rivet-conditioned MEAN
m=D('139.57039');T=D('0.07818527068831995')
alpha=1/D('137.035999084');hc=D('1.973269804e-11')
ctau=D('7.8045');gamma=E/m;beta=mp.sqrt(1-gamma**-2)
gt=gamma*T;cap=m/20
z,w=mp.gauss_quadrature(20,'legendre')
def J(om):
    lo=om/(gt*(1+beta));hi=om/(gt*(1-beta))
    log=lambda a:mp.log(-mp.expm1(-a))
    q1=lambda a:-a*log(a)+mp.polylog(2,mp.exp(-a))
    q2=lambda a:-a*a*log(a)+2*a*mp.polylog(2,mp.exp(-a))+2*mp.polylog(3,mp.exp(-a))
    return log(hi)-log(lo),q1(lo)-q1(hi),q2(lo)-q2(hi)
def integrand(om):
    if om==0:return D(0),D(0),D(0)
    j0,j1,j2=J(om)
    r0=r1=r2=D(0)
    for zz,ww in zip(z,w):
        rr=1/(1+(om/m)*(1-zz))
        kernel=D(3)/8*ww*(1+zz*zz)*rr*rr
        A=gamma*om*rr*(1-zz);B=T*(1-rr*zz)
        moment2=A*A*j0-2*A*B*j1+B*B*j2
        moment2+=rr*rr*(1-zz*zz)/2*(-om*om*j0+2*gamma*om*T*j1-T*T*j2)
        r0+=kernel*j0;r1+=kernel*(A*j0-B*j1);r2+=kernel*moment2
    return om*r0,om*r1,om*r2
segments=[D(0),gt*(1-beta),cap/10,cap/2,cap]
V=[sum(mp.quad(lambda om:integrand(om)[k],[a,b]) for a,b in zip(segments,segments[1:])) for k in range(3)]
F=V[0]/(4*beta*mp.zeta(3)*gt*gt)
mean=V[1]/V[0];sq=V[2]/V[0]
sd=mp.sqrt(sq-mean*mean)
n=2*mp.zeta(3)/mp.pi**2*(T/hc)**3
sTh=8*mp.pi*alpha**2/(3*m*m)*hc*hc
collision_mfp=beta/(n*sTh*F)/100
decay_path=beta*gamma*ctau
local_loss_length=collision_mfp*E/mean
assert abs(mean/1000-D('21.267977425758641'))<D('1e-12')
assert abs(sd/1000-D('16.397213044002213'))<D('1e-12')
assert abs(local_loss_length-D('16189.445644439734'))<D('1e-9')
fmt=lambda y:mp.nstr(y,24)
print(json.dumps({
 'status':'PASS_DEFINED_POINT_SCALAR_BORN_SOFT_PION_ENERGY_MOMENTS',
 'source':'ROT020 Belle/Rivet source conditional MEAN only; original reference YODA SHA256=28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403',
 'E_pi_MeV':fmt(E),'cap_pion_rest_MeV':fmt(cap),
 'F_scatter_weighted_soft_fraction':fmt(F),
 'mean_photon_energy_gain_GeV':fmt(mean/1000),
 'std_photon_energy_gain_GeV':fmt(sd/1000),
 'raw_second_moment_gain_GeV2':fmt(sq/1e6),
 'soft_scatter_mfp_m':fmt(collision_mfp),
 'local_pion_loss_length_m':fmt(local_loss_length),
 'initial_vacuum_pion_decay_length_m':fmt(decay_path),
 'limitation':'NO physical composite pion QCD rate, NO full parent-energy distribution, NO repeated energy-changing scatter/death process, NO final neutrino yield or PBH/BBN'
},indent=2,sort_keys=True))
