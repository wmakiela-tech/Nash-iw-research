#!/usr/bin/env python3
"""Independent micro-EOS pressure-vs-entropy cooling check; no PBH claim."""
from pathlib import Path
import importlib.util, json, numpy as np
from scipy.integrate import trapezoid
from scipy.interpolate import CubicSpline
p=Path(__file__).with_name('reproduce_mech_s7_thermal_eos_event_010.py')
s=importlib.util.spec_from_file_location('v',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
from scipy.integrate import cumulative_trapezoid
out=Path(__file__).parent
Tcut=float(json.loads((out/'thermal_eos_010.json').read_text())['T_cut_MeV']);Tnu=m.TNUC
# Independently approximate derivatives from directly integrated energy and pressure,
# on a different grid from the numerical trajectory interpolation.
TL=np.geomspace(Tnu,Tcut,2801)
coef=m.micro_coefficients(TL,quad=180)
lT=np.log(TL)
r=np.gradient(np.log(coef['grho']),lT,edge_order=2)
s=np.gradient(np.log(coef['gsem']),lT,edge_order=2)
w=coef['w'];H=1.66053906660*(1/m.HBAR_GEV_SEC)/m.MPL_GEV/1e6*TL**2*np.sqrt(coef['grho'])
# Equivalence: entropy: dt/dlnT = -(3+s)/(3H)
# Energy+pressure: dt/dlnT=-(4+r)/(3H(1+w))
E=(3+s)/(3*H);P=(4+r)/(3*H*(1+w));
err=np.abs(P-E)/E
# highest numerical derivative noise near endpoints; report separately internals.
base=trapezoid(E,lT);press=trapezoid(P,lT)
# R22 linked author table at 0.1MeV Tnu/Tgam ~.7634424; independent ideal
# instantaneous-decoupling micro host need not agree precisely.
res={"Tcut_MeV":Tcut,"Tnuc_MeV":Tnu,"entropy_duration_s":base,"pressure_duration_s":press,"difference_s":press-base,"pressure_entropy_max_rel_local_mismatch_inner":float(np.max(err[10:-10])),"pressure_entropy_RMS_rel_mismatch_inner":float(np.sqrt(np.mean(err[10:-10]**2))),"ideal_Tnu_over_Tgamma_at_0p1":float(m.micro_coefficients(np.array([.1]),quad=180)['Tnu_over_Tgamma'][0]),"interpretation":"ideal instant-decoupling two-temperature host, numerical derivative residual only; no original source 10D"}
(out/'pressure_entropy_integrity_010.json').write_text(json.dumps(res,indent=2))
print(json.dumps(res,indent=2))