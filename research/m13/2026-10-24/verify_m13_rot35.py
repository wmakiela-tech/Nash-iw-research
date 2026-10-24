#!/usr/bin/env python3
"""M13 ROT35: nested-mask covariance, exact shell unmixing, profiled Fisher information.
Conditional synthetic iid additive voxel ENERGY noise, NOT independent mask noise.
"""
import json, math, csv
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
N=41; ks=np.arange(2,7); counts=np.array([(N-2*k)**3 for k in ks], dtype=float)
volumes=np.r_[counts[:-1]-counts[1:],counts[-1]]
assert np.all(volumes>0)
# Y_k= mean per voxel of square-norm/6 plus zero-mean iid error var sigma_voxel^2.
# B: Y -> shellmeans; x_shell_i=(n_i Y_i - n_i+1 Y_i+1)/v_i ; final=Y_6.
B=np.zeros((5,5))
for i in range(4):B[i,i]=counts[i]/volumes[i];B[i,i+1]=-counts[i+1]/volumes[i]
B[4,4]=1
Bi=np.linalg.inv(B)
S=np.array([[1/counts[min(i,j)] for j in range(5)] for i in range(5)])
D=np.diag(1/volumes)
assert np.allclose(B@S@B.T,D,rtol=1e-11,atol=1e-15)
assert np.linalg.norm(S-Bi@D@Bi.T)/np.linalg.norm(S)<1e-11
# Shell sum covariance diagonal across disjoint shells.
T=np.linalg.inv(S)
assert np.all(np.linalg.eigvalsh(S)>0)
coeff=json.loads((ROOT/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').read_text())
models={(z['N'],z['mask_k']):z['G_quartic_squared_RMS'] for z in coeff['cases']}
sourcecsv={}
with (ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open() as fp:
 for r in csv.DictReader(fp): sourcecsv[(float(r['alpha']),int(r['interior_k']))]=r

def poly(c,x):return sum(v*x**j for j,v in enumerate(c))
def dpoly(c,x):return sum(j*v*x**(j-1) for j,v in enumerate(c) if j)

def fisher(m,dm,w):
 # conditional on a SINGLE unknown positive scale t=s^2, with known covariance
 uu=np.dot(m,w@m) if np.ndim(w)==2 else np.dot(m*w,m)
 vv=np.dot(dm,w@dm) if np.ndim(w)==2 else np.dot(dm*w,dm)
 uv=np.dot(m,w@dm) if np.ndim(w)==2 else np.dot(m*w,dm)
 score=vv-uv*uv/uu
 assert score>0
 return score,uv/uu,uu

def profile(ch,alpha,pair=None):
 arr=np.array([poly(models[N,k][ch],alpha) for k in ks]);der=np.array([dpoly(models[N,k][ch],alpha) for k in ks])
 if pair is None:
  sh=B@arr; dh=B@der
  score,proj,uu=fisher(sh,dh,volumes)
 else:
  idx=[int(np.where(ks==k)[0][0]) for k in pair]
  sm=S[np.ix_(idx,idx)]; w=np.linalg.inv(sm)
  score,proj,uu=fisher(arr[idx],der[idx],w)
 return score,arr,der,proj,uu

# independent 5x mask covariance GLS vs shell independent analysis, plus 10 covariance-aware pairs
records=[];historical_checks=[]
for ch in 'ABC':
 for alpha in [0,.05,.2]:
  for k in ks:
   source=sourcecsv[(alpha,int(k))];v=math.sqrt(poly(models[N,int(k)][ch],alpha))
   frozen=float(source['K_'+ch+'_RMS'])
   historical_checks.append(abs(v/frozen-1))
 for alpha in [0,.05,.113,.2]:
  score,arr,der,proj,uu=profile(ch,alpha)
  scorecov,_,_=fisher(arr,der,T)
  assert abs(scorecov/score-1)<2e-11,(ch,alpha,score,scorecov)
  allpairs=[]
  for i in range(5):
   for j in range(i+1,5):
    kpair=(int(ks[i]),int(ks[j]));pscore,_,_,_,_=profile(ch,alpha,kpair)
    allpairs.append({'pair':list(kpair),'info_fraction_full':float(pscore/score),'J0':float(pscore)})
    assert pscore<=score*(1+2e-10),(ch,alpha,kpair,pscore,score)
  allpairs.sort(key=lambda x:x['J0'],reverse=True)
  # Compare to historical ROT34 sensitivity-based C2/4 pair and A/C cross-channel not comparable (different data/noise model).
  reference=poly(models[N,2][ch],.05)
  # for sigma_voxel = 1%*g_2(alpha=.05); conditional CRLB variance = sigma² / J
  sigma=.01*reference
  records.append({'channel':ch,'alpha':alpha,'info_J0_units_of_squared_energy2':float(score),
      'sigma_alpha_Cramer_Rao_per_voxel_1pct_reference_energy':float(sigma/math.sqrt(score)),
      'common_gain_logderivative_proj':float(proj),
      'top_pairs':allpairs[:3],
      'C_2_4_info_fraction':next((r['info_fraction_full'] for r in allpairs if r['pair']==[2,4]),None),
      'A_2_6_info_fraction':next((r['info_fraction_full'] for r in allpairs if r['pair']==[2,6]),None),
      'all_pairs':allpairs})
# Derived deterministic individual shell profiles and contrast at .05:
shells=[]
for ch in 'ABC':
 p=.05;g=np.array([poly(models[N,k][ch],p) for k in ks]);dg=np.array([dpoly(models[N,k][ch],p) for k in ks]);e=B@g;de=B@dg
 assert np.all(e>0),(ch,e)
 for i,(E,dE) in enumerate(zip(e,de)):
  shells.append({'channel':ch,'shell':f'{ks[i]}→{ks[i+1]}' if i<4 else 'k6_core', 'voxels':int(volumes[i]), 'mean_energy':float(E), 'relative_alpha_sensitivity_dlog_energy':float(dE/E)})
# Local nuisance-profiled influence function verification under Gaussian shell noise.
# This is the linearized estimator at known truth, NOT a practical algorithm guaranteed to locate the global solution.
linearized=[]
for ch in 'ABC':
 a=.05
 _,g,d,gainproj,_=profile(ch,a)
 shell=B@g;der=B@d
 tangent=der-gainproj*shell
 baseJ=float(np.dot(volumes*tangent,tangent))
 assert baseJ>0
 tau=.01*poly(models[N,2][ch],.05)
 rng_lin=np.random.default_rng(4242)
 draws=20000
 noise=rng_lin.normal(size=(draws,5))*tau/np.sqrt(volumes)
 estimates=(noise@(volumes*tangent))/baseJ
 expected=tau/math.sqrt(baseJ)
 empirical=float(np.std(estimates,ddof=1))
 assert abs(empirical/expected-1)<.035,(ch,empirical,expected)
 linearized.append({'channel':ch,'n':draws,'sigma_empirical':empirical,'sigma_Fisher':expected,'ratio':empirical/expected})
# Diagonal-covariance naive treatment yields a DIFFERENT inference, in these data understating the available information.
naive=[]
for ch in 'ABC':
 _,g,d,_,_=profile(ch,.05)
 realJ,_,_=fisher(g,d,T)
 naiveJ,_,_=fisher(g,d,1/np.diag(S))
 naive.append({'channel':ch,'naive_diagonal_information_fraction_of_correct':float(naiveJ/realJ)})
# generic covariance and independent-shell algebra Monte Carlo using fixed seed
rng=np.random.default_rng(20261024);shots=30000
z=rng.normal(size=(shots,5))/np.sqrt(volumes)
y=(Bi@z.T).T
mc_S=np.cov(y,rowvar=False,ddof=1)
max_mc_cov_dev=float(np.max(np.abs(mc_S-S)/S))
assert max_mc_cov_dev<.055,max_mc_cov_dev
maxrel=max(historical_checks)
assert maxrel<3e-14,maxrel
result={'return_id':'M13-ROT35-NESTED-SHELL-COVARIANCE-AND-CONDITIONAL-FISHER-001_20261024',
        'noise_host':'iid per voxel additive errors in squared Frobenius RMS energy; same variance tau², NOT observed experimental noise; units arbitrarily normalized; independent across voxels and one channel only',
        'N':N,'masks':ks.tolist(),'sample_counts':counts.astype(int).tolist(),'independent_shell_counts':volumes.astype(int).tolist(),
        'covariance_S_normalized_by_tau2':S.tolist(), 'shell_unmixing_B':B.tolist(),
        'covariance_exact_algebra_relative_residual':float(np.linalg.norm(B@S@B.T-D)/np.linalg.norm(D)),
        'max_historical_relative_error_45_values':maxrel,'monte_carlo_shots':shots,'monte_carlo_max_pairwise_relative_covariance_error':max_mc_cov_dev,
        'fisher_profiles':records,'shell_energy_at_alpha005':shells,'linearized_gaussian_monte_carlo':linearized,'incorrect_diagonal_covariance_control':naive,
        'limitations':['Classical nested-sample Gaussian/quasi-Gaussian Fisher conditional on error model; does not infer actual voxel independence',
                       'No independent gains for masks; one common positive source amplitude; original helper functional replacement only',
                       'Fisher local CRLB is not a global error guarantee; parameter folding may occur for individual mask pairs',
                       'Comparisons between distinct channels require unknown cross-channel covariance, not assumed']}
result_path=ROOT/'IW_M13_ROT35_nested_shell_covariance_fisher_20261024.json'
result_path.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('SHELL_COUNTS',volumes.astype(int).tolist(),'GEOMETRY_TOTAL',int(counts[0]))
print('MAX_45_FROZEN_RMS_REL',maxrel)
print('COVARIANCE_SHELL_MATCH',result['covariance_exact_algebra_relative_residual'],'MC_PAIRWISE_MAX',max_mc_cov_dev)
for z in records:
 if z['alpha']==.05:
  print(z['channel'],'alpha=.05','sigma_alpha_1pct_per_voxel',z['sigma_alpha_Cramer_Rao_per_voxel_1pct_reference_energy'],'BEST_PAIR',z['top_pairs'][0],'C2/4fraction',z['C_2_4_info_fraction'])
print('LINEARIZED_MONTE_CARLO',linearized)
print('NAIVE_INDEPENDENT_MASK_INFO_FRACTIONS',naive)
print('CONDITIONAL_FISHER_ROT35_PASS')