#!/usr/bin/env python3
"""M13 ROT29. Read-only frozen-CSV estimator/noise audit and smooth positive
low-band mask non-identifiability witness; all computations on saved data.
"""
import csv, json, math, hashlib, sys, importlib.util
from pathlib import Path
from fractions import Fraction as F
from statistics import mean
import numpy as np

ROOT=Path(__file__).resolve().parent
INPUT=ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv'
REFERENCE=ROOT/'IW_M13_ROT28_mask_extrapolation_and_shells_20261023.json'
OUT=ROOT/'IW_M13_ROT29_mask_minimax_and_nonidentifiability_20261024.json'
SHA=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()

# Exact, coefficient-space moment cancellation in k=2..6.
SPECS={
 'raw_k3': {3:F(1)},
 'first_order_k23':{2:F(3),3:F(-2)},
 'first_order_k26_minimax_L1':{2:F(3,2),6:F(-1,2)},
 'second_order_k246_minimax_L1':{2:F(3),4:F(-3),6:F(1)},
 'second_order_k234':{2:F(6),3:F(-8),4:F(3)},
 'second_order_k2345':{2:F(10),3:F(-20),4:F(15),5:F(-4)},
 'second_order_k23456':{2:F(15),3:F(-40),4:F(45),5:F(-24),6:F(5)},
 'second_order_minL2_all5':{2:F(3),3:F(-2,5),4:F(-9,5),5:F(-6,5),6:F(7,5)},
}
for name,w in SPECS.items():
    degree=0 if name=='raw_k3' else 1 if name.startswith('first_order') else 4 if name=='second_order_k23456' else 3 if name=='second_order_k2345' else 2
    for p in range(degree+1):
        val=sum((v*k**p for k,v in w.items()),F(0))
        assert val == int(p==0), (name,p,val)
assert sum(abs(t) for t in SPECS['second_order_k246_minimax_L1'].values())==7
assert sum(abs(t) for t in SPECS['first_order_k26_minimax_L1'].values())==2
# Dual certificate: q(k)=(k-4)^2/2 -1, |q(k)|<=1 for all k=2..6.
dual={k:F((k-4)**2,2)-1 for k in range(2,7)}
assert all(abs(x)<=1 for x in dual.values()) and F((0-4)**2,2)-1 ==7
# First order q(k)=(4-k)/2 -> q(0)=2.
assert all(abs(F(4-k,2))<=1 for k in range(2,7))

csv_rows=list(csv.DictReader(INPUT.open(encoding='utf-8-sig',newline='')))
assert len(csv_rows)==15
ref=json.loads(REFERENCE.read_text(encoding='utf-8'))
refs={(float(x['alpha']),x['channel']):x for x in ref['N41_cases']}
assert len(refs)==9
hist={}
for row in csv_rows:
    key=(float(row['alpha']),int(row['interior_k']))
    assert key not in hist
    hist[key]=row

cases=[]
for a in [0.,.05,.2]:
 for ch in 'ABC':
    z=refs[(a,ch)]; r0=float(z['global_RMS']); raw={k:float(hist[(a,k)][f'K_{ch}_RMS']) for k in range(2,7)}
    assert max(abs(raw[k]-z['historical_mask_RMS'][str(k)])/raw[k] for k in raw)<3e-14
    out={'alpha':a,'channel':ch,'full_grid_RMS_from_ROT28':r0,'masked_RMS':raw,'estimators':{}}
    for name,w in SPECS.items():
        estimate2=sum(float(c)*raw[k]**2 for k,c in w.items())
        estimate=math.sqrt(estimate2) if estimate2>=0 else None
        out['estimators'][name]={'weights':{str(k):str(c) for k,c in w.items()},'l1':float(sum(abs(c) for c in w.values())),'l2':math.sqrt(sum(float(c*c) for c in w.values())), 'estimate_squared':estimate2,'estimate_RMS':estimate,'relative_RMS_error':(estimate/r0-1 if estimate is not None else None)}
    cases.append(out)

stats={}
for name in SPECS:
    x=[abs(z['estimators'][name]['relative_RMS_error']) for z in cases]
    stats[name]={'mean_absolute_RMS_relative_error':mean(x),'maximum_absolute_RMS_relative_error':max(x),'improved_over_raw_count':sum(abs(z['estimators'][name]['relative_RMS_error'])<abs(z['estimators']['raw_k3']['relative_RMS_error']) for z in cases),'l1':float(sum(abs(v) for v in SPECS[name].values())),'l2':math.sqrt(sum(float(v*v) for v in SPECS[name].values()))}

# A constructive nonidentifiability witness: smooth band <= 5 energy density.
N=41;c=(N-1)//2;theta=2*math.pi/N
j=np.arange(N,dtype=float);t=np.cos(theta*(j-c))
roots=np.array([math.cos(theta*(c-k)) for k in range(2,6)])
H=np.prod(t[:,None]-roots,axis=1)
inside=slice(6,N-6)
lambda0=float(np.dot(H[inside],t[inside])/np.sum(H[inside]))
V=H*(t-lambda0)
maxabs=float(np.max(np.abs(V)))
scaled=V/maxabs
masked=[float(np.mean(scaled[k:N-k])) for k in range(2,7)]
glob=float(np.mean(scaled))
assert max(abs(q) for q in masked)<4e-14
assert glob <0 and max(abs(scaled))<=1.000000000001
assert all(V[k]==0 for k in (2,3,4,5)) and all(abs(V[N-1-k])<1e-14 for k in (2,3,4,5))
assert all(x>0 for x in H[6:N-6]) and roots[0] < roots[1] < roots[2] < roots[3]
# F_+ and F_- remain positive and have EXACT same masked mean (within roundoff)
eps=.5
plus=1+eps*scaled;minus=1-eps*scaled
assert min(plus)>0 and min(minus)>0
assert max(abs(np.mean(plus[k:N-k])-np.mean(minus[k:N-k])) for k in range(2,7))<4e-14
assert abs(np.mean(plus)-np.mean(minus))>1e-5
# Degree check via explicit regression onto cos(m*(x-x_c)) for m<=5
ang=theta*(j-c)
B=np.stack([np.ones(N)]+[np.cos(m*ang) for m in range(1,6)],axis=1)
coef=np.linalg.lstsq(B,scaled,rcond=None)[0]
assert max(abs(B@coef-scaled))<3e-14

# Directly validate source-native weighted tensor RMS on two synthetic real tensor fields.
helper_path=ROOT/'deepseek_python_20260627_a87249.py'
spec=importlib.util.spec_from_file_location('dtc0a_rot29_retained_helper',helper_path)
helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
field_plus=np.zeros((N,N,N,3,3));field_minus=np.zeros_like(field_plus)
field_plus[...,0,0]=np.sqrt(6*plus[:,None,None]);field_minus[...,0,0]=np.sqrt(6*minus[:,None,None])
helper_checks={}
for k in [0,2,3,4,5,6]:
 mask=slice(k,N-k) if k else slice(None)
 pp=helper.rms_norm(field_plus,mask);mm=helper.rms_norm(field_minus,mask)
 expectedp=math.sqrt(float(np.mean(plus[k:N-k])) if k else float(np.mean(plus)))
 expectedm=math.sqrt(float(np.mean(minus[k:N-k])) if k else float(np.mean(minus)))
 assert abs(pp-expectedp)<5e-14 and abs(mm-expectedm)<5e-14
 helper_checks[str(k)]={'plus_RMS':pp,'minus_RMS':mm,'difference':pp-mm}
assert max(abs(helper_checks[str(k)]['difference']) for k in range(2,7))<5e-14
assert abs(helper_checks['0']['difference'])>1e-5

# Test deterministic worst-case squared-RMS noise amplification at N41, a=.05, channel A.
example=next(z for z in cases if z['alpha']==.05 and z['channel']=='A')
true2=example['full_grid_RMS_from_ROT28']**2
noise_ex={}
for name in ['first_order_k23','second_order_k246_minimax_L1','second_order_k234']:
 w=SPECS[name];sig=.005*true2 # bounded ±0.5% of squared full RMS
 perturb=sum(float(v)*sig*(1 if v>0 else -1) for v in w.values())
 base=example['estimators'][name]['estimate_squared'];adversarial=math.sqrt(base+perturb)
 noise_ex[name]={'unperturbed_relative_RMS_error':math.sqrt(base/true2)-1, 'worst_case_positive_perturbation_squared_relative':perturb/true2,'perturbed_relative_RMS_error':adversarial/math.sqrt(true2)-1}

out={
 'return_id':'M13-ROT29-DTC0A-MASKED-NORM-MINIMAX-AND-FIVE-MASK-NONIDENTIFIABILITY-001_20261024',
 'source_csv_SHA256':SHA(INPUT),'ROT28_reference_SHA256':SHA(REFERENCE),
 'source_cases':cases,'stats':stats,
 'minimax_dual_certificate':{'k_values':list(range(2,7)),'q_values':{str(k):str(dual[k]) for k in dual},'q_0':7,'sharp_noise_l1_min':7,'attaining_weights':{'2':3,'4':-3,'6':1},'first_order_minL1':2,'first_order_attaining_weights':{'2':'3/2','6':'-1/2'}},
 'nonidentifiability_witness':{'N':41,'cosine_degree':5,'roots':[float(x) for x in roots],'lambda':lambda0,'max_abs_unscaled':maxabs,'global_mean_normalized_V':glob,'masked_means_normalized_V':masked,'F_plus_global_mean':float(np.mean(plus)),'F_minus_global_mean':float(np.mean(minus)),'F_plus_F_minus_masked_difference_max':float(max(abs(np.mean(plus[k:N-k])-np.mean(minus[k:N-k])) for k in range(2,7))),'cosine_coefficients':coef.tolist(),'four_outside_nodes':[float(V[k]) for k in [0,1,39,40]],'smooth_positivity_min_F':float(min(minus.min(),plus.min()))},
 'adversarial_squared_RMS_error_example':noise_ex,'source_native_RMS_synthetic_field_witness':helper_checks,'source_helper_SHA256':SHA(helper_path),
 'claim_ceiling':'MATURE_CLASSICAL_FINITE_DIMENSIONAL_GEOMETRY / FROZEN_CSV_POSTPROCESS / ABSTRACT_POSITIVE_SMOOTH_LOW_BAND_COUNTERMODEL / NO_HISTORICAL_FULL_GRID_RECOVERY_FROM_MASKS / NO_CANON / NO_EXEC_SIGN / TPE_HOLD'
}
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8')
print(json.dumps({'return_id':out['return_id'],'cases':len(cases),'source_rows':len(csv_rows),'minimax_L1':7,'mean_abs_errors_percent':{k:round(100*v['mean_absolute_RMS_relative_error'],4) for k,v in stats.items()},'low_band_witness_global_mean':glob,'witness_mask_means_max':max(abs(x) for x in masked),'witness_plus_minus_full_RMS': [math.sqrt(np.mean(plus)),math.sqrt(np.mean(minus))],'witness_cos_degree':5,'adversarial':noise_ex,'json_sha256':SHA(OUT)},indent=2))