#!/usr/bin/env python3
"""M13 ROT30: five-mask identification threshold for x-only symmetric TT fields.

Reproduces all numerical checks from scratch and calls the UNMODIFIED source helper's
apply_P_TT and rms_norm for the two counterwitnesses. It is NOT replay of K_A.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
N = 41
KS = tuple(range(2, 7))
HELPER = ROOT / 'deepseek_python_20260627_a87249.py'
OUT = ROOT / 'IW_M13_ROT30_TT_bandwidth_identifiability_20261024.json'

spec = importlib.util.spec_from_file_location('source_helper_rot30', HELPER)
source = importlib.util.module_from_spec(spec)
spec.loader.exec_module(source)

def hashfile(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

j = np.arange(N)
c = (N-1)//2
angle = 2*np.pi*(j-c)/N
t = np.cos(angle)
roots = [float(t[k]) for k in range(2, 6)]
a = (t-roots[0])*(t-roots[1])
H = np.prod(np.stack([t-r for r in roots]), axis=0)
lam = float(np.dot(H[6:N-6], t[6:N-6])/np.sum(H[6:N-6]))
b = (t-roots[2])*(t-roots[3])*(t-lam)
eps = float(np.sqrt(np.mean(a*a)/np.mean(b*b)))
f_plus = a + eps*b
f_minus = a - eps*b

# W analytic proof H(t_k)=0 for k=2,3,4,5 and weighted inner sum H(t)(t-lambda)=0.
H_times = a*b
assert np.max(np.abs(H_times-H*(t-lam))) < 1e-13
cross_mask = {str(k):float(np.mean(H_times[k:N-k])) for k in KS}
assert max(abs(z) for z in cross_mask.values()) < 3e-14
assert np.mean(H_times) < -8e-5

# f_plus,f_minus have finite scalar Fourier degree <=3.
B3 = np.stack([np.cos(m*angle) for m in range(4)],axis=1)
fourier_checks = {}
for label,f in [('plus',f_plus),('minus',f_minus)]:
    co=np.linalg.lstsq(B3,f,rcond=None)[0]
    res=float(np.max(np.abs(f-B3@co)))
    assert res < 3e-14
    spectrum=np.fft.fft(f)/N
    integers=np.fft.fftfreq(N,d=1/N)
    outband=float(np.max(np.abs(spectrum[np.abs(integers)>3])))
    assert outband < 3e-14
    fourier_checks[label]={'cosine_coefficients':co.tolist(),'max_trig_degree3_fit_error':res,'max_fourier_beyond_3':outband}

# Real symmetric TT fields, with the same polarization at every Fourier mode.
# Frobenius |diag(0,+sqrt(3)f,-sqrt(3)f)|^2=6f^2, thus source rms_norm=sqrt(mean f^2).
Tplus=np.zeros((N,N,N,3,3));Tminus=np.zeros_like(Tplus)
for T,f in ((Tplus,f_plus),(Tminus,f_minus)):
    T[...,1,1]=math.sqrt(3)*f[:,None,None]
    T[...,2,2]=-math.sqrt(3)*f[:,None,None]

records={}
for k in (0,)+KS:
    mask=slice(k,N-k) if k else slice(None)
    actualp=source.rms_norm(Tplus,mask)
    actualm=source.rms_norm(Tminus,mask)
    expectp=float(np.sqrt(np.mean(f_plus[k:N-k]**2))) if k else float(np.sqrt(np.mean(f_plus*f_plus)))
    expectm=float(np.sqrt(np.mean(f_minus[k:N-k]**2))) if k else float(np.sqrt(np.mean(f_minus*f_minus)))
    assert abs(actualp-expectp)<1e-12 and abs(actualm-expectm)<1e-12
    records[str(k)]={'RMS_T_plus':actualp,'RMS_T_minus':actualm,'difference':actualp-actualm}
assert max(abs(records[str(k)]['difference']) for k in KS)<2e-14
full_diff=abs(records['0']['difference'])
assert full_diff>3.9e-4

# Unmodified Fourier TT projector, for both full fields.
proj_errors={}
for name,T in [('plus',Tplus),('minus',Tminus)]:
    P=source.apply_P_TT(T,dx=2*np.pi/N)
    err=float(np.linalg.norm(P-T)/np.linalg.norm(T))
    assert err<2e-14,(name,err)
    tr=float(np.max(np.abs(np.trace(T,axis1=-2,axis2=-1))))
    assert tr==0.
    fourier=np.fft.fftn(T[...,1,1])/N**3
    freq=np.fft.fftfreq(N,d=1/N)
    max_yz=float(np.max(np.abs(fourier[:,:,1:])))
    assert max_yz < 2e-14
    proj_errors[name]={'relative_source_TT_projector_error':err,'max_trace':tr,'max_abs_yy_spectrum_nonzero_z':max_yz}

# Sharp B<=4 scalar-energy identifiability. All 5 masks impose independent
# constraints on even energy density: Chebyshev degrees 0..4. For tensor x-band<=2,
# energy degree<=4; for tensor x-band=3, our constructed pair disproves identifiability.
angles=2*np.pi*(j-c)/N
matrix=np.array([[float(np.mean(np.cos(m*angles[k:N-k]))) for m in range(5)] for k in KS])
svals=np.linalg.svd(matrix)[1]
assert svals[-1] > 5e-5
weights=np.linalg.solve(matrix.T,np.array([1,0,0,0,0],dtype=float))
assert np.max(np.abs(weights@matrix-np.array([1,0,0,0,0]))) < 1e-12
assert np.linalg.norm(weights,1)>30
pred2_plus=sum(weights[i]*records[str(k)]['RMS_T_plus']**2 for i,k in enumerate(KS))
pred2_minus=sum(weights[i]*records[str(k)]['RMS_T_minus']**2 for i,k in enumerate(KS))
assert abs(pred2_plus-pred2_minus)<1e-12
assert min(abs(pred2_plus-records['0']['RMS_T_plus']**2),abs(pred2_minus-records['0']['RMS_T_minus']**2))>5e-4

# Positive test for tensor fields of degree <=2 (non-even components permitted).
rng=np.random.default_rng(2030)
positive_tests=[]
for trial in range(12):
    coef=rng.normal(size=5)
    f=coef[0]+sum(coef[2*m-1]*np.cos(m*angles)+coef[2*m]*np.sin(m*angles) for m in range(1,3))
    exact2=float(np.mean(f*f))
    observ=np.array([float(np.mean(f[k:N-k]**2)) for k in KS])
    pred=float(weights@observ)
    assert abs(pred-exact2)<6e-12
    positive_tests.append(abs(pred-exact2))

# Cross-grid analytic construction: the sharp identifiability transition holds
# for EVERY odd N>=13, not just historical N=41. Numeric examples support
# the general proof and show N41 is not a floating-point accident.
oddN_checks = []
for n in [13, 15, 17, 21, 31, 41, 61]:
    jj=np.arange(n); cc=(n-1)//2
    th=2*np.pi/n; tt=np.cos(th*(jj-cc))
    rr=[tt[k] for k in range(2,6)]
    aa=(tt-rr[0])*(tt-rr[1])
    hh=np.prod(np.stack([tt-x for x in rr]),axis=0)
    ll=float(np.dot(hh[6:n-6],tt[6:n-6])/np.sum(hh[6:n-6]))
    bb=(tt-rr[2])*(tt-rr[3])*(tt-ll)
    ee=np.sqrt(np.mean(aa*aa)/np.mean(bb*bb))
    pp,mm=aa+ee*bb,aa-ee*bb
    maskdiff=max(abs(np.sqrt(np.mean(pp[k:n-k]**2))-np.sqrt(np.mean(mm[k:n-k]**2))) for k in KS)
    fullgap=abs(np.sqrt(np.mean(pp*pp))-np.sqrt(np.mean(mm*mm)))
    mat=np.array([[np.mean(np.cos(m*th*(jj[k:n-k]-cc))) for m in range(5)] for k in KS])
    assert maskdiff<1e-12 and fullgap>1e-8 and np.linalg.matrix_rank(mat)==5
    oddN_checks.append({'N':n,'max_masked_RMS_difference':float(maskdiff),'global_RMS_difference':float(fullgap),'even_degree4_observation_condition_2norm':float(np.linalg.cond(mat))})

out={
 'return_id':'M13-ROT30-SHARP-TT-TENSOR-BANDWIDTH-2-VS-3-FIVE-MASK-IDENTIFIABILITY-001_20261024',
 'N':N,'mask_k':list(KS),'source_helper_sha256':hashfile(HELPER),
 'proof_source':'degree<=4 even trig energy uniquely identified from 5 nested averages; degree5 polynomial H(t)(t-lambda) is kernel with nonzero full average; TT source witnesses f_plus/minus=quadratic+-eps*cubic',
 'lambda':lam,'oddN_ge13_crossgrid_controls':oddN_checks,'eps':eps,'t_roots':roots,'pairwise_product_full_average':float(np.mean(a*b)),'pairwise_product_masked_averages':cross_mask,
 'tensor_degree':3,'strictly_TT_source_checks':proj_errors,'fourier':fourier_checks,
 'rms':records,'full_grid_RMS_difference':full_diff,
 'full_grid_RMS_relative_difference':full_diff/(.5*(records['0']['RMS_T_plus']+records['0']['RMS_T_minus'])),
 'degree4_mask_observation_matrix':matrix.tolist(),'degree4_min_singular_value':float(svals[-1]),
 'degree4_condition_number_2norm':float(svals[0]/svals[-1]),
 'degree4_exact_recovery_weights_float':weights.tolist(),
 'degree4_weights_L1':float(np.sum(np.abs(weights))),
 'degree4_paired_estimated_full_squared_energies':[float(pred2_plus),float(pred2_minus)],
 'degree2_tensor_positive_recovery_trials':len(positive_tests),'degree2_tensor_max_abs_squared_error':float(max(positive_tests)),
 'limits':['source helper synthetic only','not historical K_A/K_B/K_C tensors','one-coordinate fixed-flat periodic TT','no original runtime byte-exact','no novelty or physical upgrade'],
}
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({'PASS':'12/12 degree2 TT recovery; 5/5 masked counterexample; 2/2 source TT projector','masked_diff_max':max(abs(records[str(k)]['difference']) for k in KS),'full_RMS_plus':records['0']['RMS_T_plus'],'full_RMS_minus':records['0']['RMS_T_minus'],'full_relative_gap':out['full_grid_RMS_relative_difference'],'source_TT_error':proj_errors,'L1_degree4_recovery':out['degree4_weights_L1'],'condition_number':out['degree4_condition_number_2norm'],'output':str(OUT)},indent=2))