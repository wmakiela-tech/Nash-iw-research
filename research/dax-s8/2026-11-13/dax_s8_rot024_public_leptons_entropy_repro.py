#!/usr/bin/env python3
"""DAX-S8 ROT024 compact R68 lepton and entropy gate. Requires scipy.
Only IDEAL equilibrium plasma and adiabatic EM entropy; no physical screened
pion-electron transport, nuclear network, or PBH/BBN physical bound.
"""
import json,math
from scipy.integrate import quad
from scipy.special import expit,kv
T=.07818527068831995
me=.51099895069
hc=1.973269804e-11
eta_post=6.12e-10
Epi=718277.144397855197
mpi=139.57039
ctau_m=7.8045
z=me/T
f=lambda q:expit(-math.hypot(q,z))
n_e=(T/hc)**3/math.pi**2*quad(lambda q:q*q*f(q),0,65,epsrel=3e-13)[0]
rho_e=T**4/(math.pi**2*hc**3)*quad(lambda q:q*q*math.hypot(q,z)*f(q),0,65,epsrel=3e-13)[0]
p_e=T**4/(3*math.pi**2*hc**3)*quad(lambda q:q**4/math.hypot(q,z)*f(q),0,65,epsrel=3e-13)[0]
n_e_bessel=me*me*T/(math.pi**2*hc**3)*sum((-1)**(k+1)*kv(2,k*z)/k for k in range(1,20))
p_e_bessel=me*me*T*T/(math.pi**2*hc**3)*sum((-1)**(k+1)*kv(2,k*z)/k**2 for k in range(1,20))
assert abs(n_e_bessel/n_e-1)<1e-12
assert abs(p_e_bessel/p_e-1)<1e-12
zeta3=1.2020569031595942854
n_gamma=2*zeta3/math.pi**2*(T/hc)**3
rho_gamma=math.pi**2*T**4/(15*hc**3)
s_ratio=2*(rho_e+p_e)/(4*rho_gamma/3)
nb_post_eta=eta_post*n_gamma
nb_instant=(1+s_ratio)*nb_post_eta
Ldec_cm=ctau_m*100*math.sqrt((Epi/mpi)**2-1)
crit_piN_old_mb=1/(nb_post_eta*Ldec_cm)/1e-27
crit_piN_new_mb=1/(nb_instant*Ldec_cm)/1e-27
crit_pi_e_pair_nb=1/(2*n_e*Ldec_cm)/1e-33
assert abs(s_ratio-.08498004865733277)<1e-12
assert abs(crit_piN_new_mb-24.746415158830265)<1e-11
assert abs(crit_pi_e_pair_nb-.49841235997845445)<1e-12
print(json.dumps({
 'status':'PASS_DIRECT_FD_AND_BESSEL_INDEPENDENT_IDEAL_R68_PLASMA',
 'n_eplus_cm3':n_e,'n_gamma_cm3':n_gamma,
 'rho_pair_over_photons':2*rho_e/rho_gamma,
 'entropy_pair_over_photons':s_ratio,
 'eta_instant_over_eta_post':1+s_ratio,
 'n_baryons_using_post_eta_naively':nb_post_eta,
 'n_baryons_with_adiabatic_EM_entropy':nb_instant,
 'pair_leptons_per_baryon_corrected':2*n_e/nb_instant,
 'pion_nucleon_critical_mb_using_post_eta_naively':crit_piN_old_mb,
 'pion_nucleon_critical_mb_EM_entropy_corrected':crit_piN_new_mb,
 'pion_eplus_eminus_critical_cross_section_nb':crit_pi_e_pair_nb,
 'energy_weighted_stop_threshold_GeV_nb':Epi/1000*crit_pi_e_pair_nb,
 'limits':'Ideal equilibrium and adiabatic EM entropy only; no measured pion-lepton cross section, no charged-pion physical stopping, no BBN composition or PBH bound.'
},sort_keys=True,indent=2))
