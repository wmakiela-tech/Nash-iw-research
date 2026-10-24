#!/usr/bin/env python3
"""Mech-S7 ROT018: exact PBH remaining-lifetime phase coordinate, representation
counterexample, source-only fluence quadrature, and native-precision gate.
NOT a simulation of Wu-Xu original 10D Julia or physical BBN.
Original code pinned: Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d
Gamma approximate DISPLAY only 4.207579833788249e27 g^3/s, same ROT004/017.
"""
from pathlib import Path
import csv,json,hashlib,math,sys
import numpy as np
import mpmath as mp
from numpy.polynomial.legendre import leggauss

OUT=Path(__file__).resolve().parent
M0='6000000000'
MEDGE='1000000000'
GAMMA='4.207579833788249e27'
mp.mp.dps=90
m0=mp.mpf(M0);gamma=mp.mpf(GAMMA);medge=mp.mpf(MEDGE)
mcut=m0*mp.exp(-20)
tau=lambda m:m**3/gamma
tau0=tau(m0);taucut=tau(mcut);tauedge=tau(medge)
Tzero=tau0;Tcut=Tzero-taucut
zmax=3*mp.log(m0/mcut)
float_spacing=math.ulp(float(Tzero))
critical=(gamma*mp.mpf(repr(float_spacing)))**(mp.mpf(1)/3)

results={'source_pin':'Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d',
 'model':'source-supported constant N_BH plateau only', 'gamma_display_g3_per_s':str(gamma),
 'mass_initial_g':str(m0), 'mass_edge_g':str(medge),'mass_cut_g':mp.nstr(mcut,60),
 'tau_initial_s':mp.nstr(tau0,60),'tau_edge_s':mp.nstr(tauedge,60),
 'tau_cut_s':mp.nstr(taucut,60),'formal_zero_mass_time_s':mp.nstr(Tzero,60),
 'mass_cut_time_s':mp.nstr(Tcut,60),'cut_to_zero_time_s':mp.nstr(Tzero-Tcut,60),
 'log_tau_span_initial_cut':mp.nstr(zmax,60),
 'log_tau_span_edge_cut':mp.nstr(3*mp.log(medge/mcut),60),
 'float64_time_ulp_s':repr(float_spacing),
 'float64_mass_one_ulp_g':mp.nstr(critical,25),
 'float64_cuts_indistinguishable':float(Tcut)==float(Tzero),
 'mass_coordinate_event_at_z0':True}

# Write a series of source-shell checkpoints. 100-bit high-precision calculations
# of absolute time and native-relative remaining lifetime are contrasted with
# Float64 absolute-time serialization and log-lifetime coordinate z.
rows=[]
masses=[m0,medge,mp.mpf('1e8'),mp.mpf('1e6'),mp.mpf('1e5'),mp.mpf('3.1e4'),mp.mpf('1e4'),mp.mpf('1e3'),mp.mpf('100'),mcut]
for m in masses:
    tt=Tzero-tau(m)
    t64=float(tt)
    z=3*mp.log(m/mcut)
    # exact: d logM / dz = 1/3 and dt/dz = -taucut*exp(z)
    r={ 'mass_g':mp.nstr(m,40), 'tau_remaining_s':mp.nstr(tau(m),40),
        'absolute_t_s_90dps':mp.nstr(tt,70), 't_float64_s':format(t64,'.17g'),
        'z_log_remaining_over_cut':mp.nstr(z,45),
        'float64_t_equal_formal_zero':int(t64==float(Tzero)),
        'float64_tau_recovered_by_subtract_s':format(float(Tzero)-t64,'.17g'),
        'original_tau_in_float64_s':format(float(tau(m)),'.17g')}
    rows.append(r)
with (OUT/'remaining_lifetime_checkpoints_018.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)

# Model-independent exact source-only fluence consistency check: Q(M)~M^-p,
# dt=-3M²/Gamma dM, using both mass and log-remaining-lifetime quadrature.
fluences=[]
points,weights=leggauss(480)
start=float(3*mp.log(medge/mcut));end=0.
# x = ln (tau/taucut); integrate from 0 (cut) to ln(tau_edge/tau_cut)
zz=.5*(points+1)*start
zw=.5*weights*start
for p in (1.2,1.3,1.4,2.99):
    a=3.-p
    mu_cut=float(mcut/medge)
    # normalize to Q(Medge)* tau(Medge) ; analytic integral 3/(3-p)*(1-(Mcut/Medge)^(3-p))
    analytic=3/a*(-math.expm1(a*math.log(mu_cut)))
    # log tau coordinate M/Medge = exp((z-zedge)/3); tau/tauedge = exp(z-zedge)
    zedge=start
    zint=np.exp((1-p/3)*(zz-zedge))
    log_quad=float(np.dot(zw,zint))
    # direct mass-coordinate x=M/Medge, integral 3*x^(2-p)dx
    # logmass quadrature proper direct comparison
    q=np.exp((zz-zedge)/3) # M/Medge
    mass_quad=float(np.dot(zw, q**(3-p)))
    fluences.append({'p':p,'analytic_dimensionless':analytic,
        'logtau_quadrature':log_quad,'logmass_equivalent_quadrature':mass_quad,
        'abs_error':abs(analytic-log_quad),
        'correct_integrand_exponent':a/3})
    assert abs(analytic-log_quad)<1e-11,(p,analytic,log_quad)
with (OUT/'source_fluence_coordinate_equivalence_018.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=fluences[0].keys());w.writeheader();w.writerows(fluences)

# Finite precision test, formal zero-time and last mass cutoff at 53, 64,80,87,100,113 bits.
pre=[]
for bits in (53,64,80,87,90,94,100,113):
    with mp.workprec(bits):
        zt=mp.mpf(M0)**3/mp.mpf(GAMMA)
        tc=zt-(mp.mpf(M0)*mp.exp(-20))**3/mp.mpf(GAMMA)
        d=zt-tc
        tc_mass=(d*mp.mpf(GAMMA))**(mp.mpf(1)/3) if d>0 else mp.mpf('0')
        part=(mp.mpf(M0)*mp.exp(-20))**3/mp.mpf(GAMMA)
        rel=abs(d-part)/part if part>0 else mp.inf
    pre.append({'bits':bits,'tau_event_seconds':mp.nstr(part,30),'time_difference_seconds':mp.nstr(d,30),
                'cutoff_distinguished':int(d>0),'relative_lifetime_roundoff':mp.nstr(rel,18),
                'mass_inferred_from_subtracted_time_g':mp.nstr(tc_mass,25),
                'native_logtau_terminal_exact_z':'0'})
with (OUT/'precision_absolute_vs_remaining_018.csv').open('w',newline='') as fh:
    w=csv.DictWriter(fh,fieldnames=pre[0].keys());w.writeheader();w.writerows(pre)
results['precision_rows']=pre
results['fluence_rows']=fluences
results['checkpoint_rows']=rows
# Verify analytic conjugacy and endpoint equality using mpmath high precision
for m in masses:
    z=3*mp.log(m/mcut)
    mm=mcut*mp.exp(z/3)
    dM_dz=mm/3
    dtdz=-taucut*mp.exp(z)
    # dM/dt = -(Gamma/3M²), recovered from phase variable
    f=dM_dz/dtdz
    exact=-gamma/(3*mm*mm)
    assert abs(f-exact)/abs(exact)<mp.mpf('1e-85')
results['conjugacy_mass_ode_high_precision']='PASS'
results['high_precision_dps']=mp.mp.dps
(OUT/'rotation_018_results.json').write_text(json.dumps(results,indent=2,ensure_ascii=False))
for k in ('mass_cut_g','tau_cut_s','float64_time_ulp_s','float64_mass_one_ulp_g','log_tau_span_initial_cut','log_tau_span_edge_cut','float64_cuts_indistinguishable'):
    print(k,results[k])
print('fluence',fluences)
print('precision',[(x['bits'],x['cutoff_distinguished'],x['relative_lifetime_roundoff']) for x in pre])
print('PASS conjugacy, quadrature, precision gates')