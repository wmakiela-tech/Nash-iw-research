#!/usr/bin/env python3
"""M13 ROT36: global source-model projective separation with nested-mask covariance.
Uses ROT32 source-matched polynomial coefficients; does NOT reimplement DTC operators.
Noise: independent equal-variance additive voxel ENERGY errors (ROT35 conditional host).
All distances in source squared-RMS energy units weighted by 1/voxel std.
"""
from pathlib import Path
import itertools, json, csv, math
import numpy as np
from scipy.optimize import minimize_scalar,brentq
from scipy.stats import chi2
ROOT=Path(__file__).resolve().parent
N=41
KS=list(range(2,7))
n=np.array([(N-2*k)**3 for k in KS],float)
v=np.r_[n[:-1]-n[1:],n[-1]]
B=np.zeros((5,5))
for i in range(4):
 B[i,i]=n[i]/v[i];B[i,i+1]=-n[i+1]/v[i]
B[4,4]=1.
S=np.array([[1/n[min(i,j)] for j in range(5)] for i in range(5)])
assert np.max(np.abs(B@S@B.T-np.diag(1/v)))<1e-16
modelsjson=json.loads((ROOT/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').read_text())
models={(x['N'],x['mask_k']):x['G_quartic_squared_RMS'] for x in modelsjson['cases']}
assert all((41,k) in models for k in KS)
with (ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open() as f:
 frozen={(float(r['alpha']),int(r['interior_k'])):r for r in csv.DictReader(f)}
def gvec(ch,a):
 return np.array([np.polynomial.polynomial.polyval(a,models[(N,k)][ch]) for k in KS])
def deriv(ch,a):
 return np.array([np.polynomial.polynomial.polyval(a,np.polynomial.polynomial.polyder(models[(N,k)][ch])) for k in KS])
def mat(indices):
 if indices==tuple(KS): return B,np.diag(v)
 ii=[KS.index(k) for k in indices]
 U=np.eye(5)[ii]
 Sigma=S[np.ix_(ii,ii)]
 W=np.linalg.inv(Sigma)
 return U,W
ALL={p:mat(p) for r in range(2,6) for p in itertools.combinations(KS,r)}
# Profile test for known true amplitude t0=1 against any positive refitted t(beta).
def profile(ch,a,b,indices=tuple(KS)):
 M,W=ALL[indices]
 A=M@gvec(ch,a);C=M@gvec(ch,b)
 gain=max(0.,float(C@W@A/(C@W@C)))
 err=A-gain*C
 dist=float(np.sqrt(max(0.,err@W@err)))
 return dist,gain

def efficient_tangent(ch,a,indices=tuple(KS)):
 M,W=ALL[indices]
 A=M@gvec(ch,a);D=M@deriv(ch,a)
 tproj=A@W@D/(A@W@A)
 x=D-tproj*A
 return float(np.sqrt(max(0.,x@W@x)))

def other_min(ch,a,indices,Delta=.01):
 # Numerical bounded search, vectorized quadratic-gain elimination, dense validation.
 M,W=ALL[indices]
 A=M@gvec(ch,a)
 AW=W@A
 AA=float(A@AW)
 def batch(beta):
  beta=np.asarray(beta,dtype=float)
  Cs=np.column_stack([np.polynomial.polynomial.polyval(beta,models[(N,k)][ch]) for k in KS])@M.T
  cross=Cs@AW
  denom=np.einsum('ni,ij,nj->n',Cs,W,Cs)
  ratio=np.maximum(0,cross/denom)
  error=A[None,:]-ratio[:,None]*Cs
  residual=np.sqrt(np.maximum(0,np.einsum('ni,ij,nj->n',error,W,error)))
  return residual
 bounds=[]
 if a-Delta>=0:bounds.append((0.,a-Delta))
 if a+Delta<=.2:bounds.append((a+Delta,.2))
 evals=[]
 for low,high in bounds:
  grid=np.linspace(low,high,513)
  vv=batch(grid)
  imin=int(np.argmin(vv))
  candidates=[(float(vv[0]),low),(float(vv[-1]),high),(float(vv[imin]),float(grid[imin]))]
  if imin not in [0,len(grid)-1]:
   opt=minimize_scalar(lambda x:float(batch([x])[0]),bounds=(grid[imin-1],grid[imin+1]),method='bounded',options={'xatol':5e-15})
   candidates.append((float(opt.fun),float(opt.x)))
  best=min(candidates)
  validationgrid=np.linspace(low,high,4097)
  valmin=float(np.min(batch(validationgrid)))
  assert best[0] <= valmin+2e-11*max(1.,valmin)
  evals.append(best)
 return min(evals) if evals else (float('nan'),float('nan'))

# Frozen, currentness and design assertions.
frozen_checks=[]
for ch in 'ABC':
 for a in (0.,.05,.2):
  g=gvec(ch,a)
  assert np.min(g)>0
  for i,k in enumerate(KS):
   measured=float(frozen[(a,k)]['K_'+ch+'_RMS'])
   frozen_checks.append(abs(np.sqrt(g[i])/measured-1))
assert max(frozen_checks)<3e-14

# Local small-delta asymptotic, disjoint-shell weighted norm and full nested covariance equivalence.
local_checks=[]
for ch in 'ABC':
 for a in (.02,.05,.1):
  tangent=efficient_tangent(ch,a)
  for h in [1e-3,1e-4,1e-5]:
   d,_=profile(ch,a,a+h)
   rel=abs(d/abs(h)/tangent-1)
   local_checks.append({'ch':ch,'a':a,'delta':h,'relative_vs_Fisher_tangent':rel})
assert max(x['relative_vs_Fisher_tangent'] for x in local_checks if x['delta']==1e-5)<5e-4

# Profile three source channels at 7 anchor alphas, for all five masks and all 10 pairs.
anchors=[0.,.02,.05,.10,.15,.18,.2]
records=[]
for ch in 'ABC':
 tau=.01*gvec(ch,.05)[0] # per-voxel ENERGY Gaussian standard deviation
 for a in anchors:
  d5,alt5=other_min(ch,a,tuple(KS))
  pairdata=[]
  for pair in itertools.combinations(KS,2):
   d,beta=other_min(ch,a,pair)
   local=efficient_tangent(ch,a,pair)
   assert d<=d5+1e-12*max(1.,d5),('data processing',ch,a,pair,d,d5)
   pairdata.append({'masks':pair,'global_min_distance_over_alpha_separated_0p01':d,'nearest_alt_alpha':beta,
     'local_eff_tangent':local,'separation_ratio_vs_all5':d/d5 if d5>0 else np.nan})
  pairdata.sort(key=lambda x:-x['global_min_distance_over_alpha_separated_0p01'])
  localdata=sorted(pairdata,key=lambda x:-x['local_eff_tangent'])
  records.append({'channel':ch,'alpha_true':a,'voxel_sigma_tau_1pct_mask2_baseline':tau,
    'five_masks_min_separation':d5,'five_masks_nearest_alt_alpha':alt5,
    'five_masks_sep_in_sigma_units':d5/tau,
    'five_masks_symmetric_ball_radius_threshold_in_sigma_units':d5/(2*tau),
    'all_pairs':pairdata,'best_global_pair':pairdata[0],
    'best_local_pair':localdata[0],
    'best_global_vs_best_local_identical':pairdata[0]['masks']==localdata[0]['masks'],
    'full5_vs_bestpair_gain':d5/pairdata[0]['global_min_distance_over_alpha_separated_0p01']})

# Analytic exact quadratic-root fold experiment for B two-mask 2/6, alpha=0.
base=0.
ratio=lambda x:gvec('B',float(x))[0]/gvec('B',float(x))[4]
f=lambda x:ratio(x)-ratio(base)
scan=np.linspace(.00001,.2,4001)
cross=[(float(x),float(y)) for x,y in zip(scan[:-1],scan[1:]) if f(x)*f(y)<0]
assert len(cross)==1,cross
beta=brentq(f,*cross[0],xtol=1e-15)
dpair,gainpair=profile('B',base,beta,(2,6))
dfull,gainfull=profile('B',base,beta,tuple(KS))
assert dpair<1e-9*np.linalg.norm(gvec('B',base))
assert dfull>0
# For same two-mask data, independent amplitude fit exactly. For 5mask strictly detects conditional mismatch.
fold={'channel':'B','true_alpha':base,'fold_alternative_alpha':beta,
 'B_masks2_6_projective_distance':dpair,'optimal_common_gain_B_2_6':gainpair,
 'B_full5_projective_distance':dfull,'optimal_common_gain_B_full5':gainfull,
 'five_mask_divided_by_voxel_sigma':dfull/(.01*gvec('B',.05)[0]),
 'source_conditional_noiseless_2mask_nonmap':True,'full5_conditional_sep_positive':True}
# Global 5mask injectivity in known model follows from ROT34 strictly monotone B masks5/6, A all, C some.
ci95=math.sqrt(chi2.ppf(.95,df=5))
result={'return_id':'M13-ROT36-DTC0A-GLOBAL-NOISE-PROFILE-FULL-SHELL-VS-MASKPAIR-001_20261025',
 'source':'ROT32 source-matched numeric quartic squared-RMS; ROT34 directed interval monotone mask pairs; ROT35 exact covariance; original runtime not byte exact',
 'formula':'d= min_{t>=0} ||U[g(alpha_true)-t*g(beta)]||_W; U=B shells and W=diag(voxel counts), or pair selector U with W=Cov(mask pair)^-1 * tau^2',
 'domain_alpha':[0.,.2], 'separation_requirement_abs_alpha':.01,
 'unknown_common_gain':'t=s^2 positive shared within one channel across all masks',
 'noise_assumption':'per-voxel additive iid Gaussian ENERGY noise with per-channel tau=0.01*g(mask2,alpha=.05); no empirical noise calibration',
 'global_continuous_minimization_status':'bounded optimization plus 4097 point per branch test; not a rigorous interval global optimality certificate',
 'n_anchors':len(anchors), 'records':records,'B_pair2_6_fold_control':fold,
 'five_dimensional_95pct_Gaussian_norm_threshold':ci95,
 'two_95pct_Gaussian_error_balls_sufficient_separation':2*ci95,
 'max_historical_45_RMS_relative_error':max(frozen_checks),
 'max_local_tangent_relative_error_delta1e5':max(x['relative_vs_Fisher_tangent'] for x in local_checks if x['delta']==1e-5),
 'max_local_tangent_relative_error_delta1e3':max(x['relative_vs_Fisher_tangent'] for x in local_checks if x['delta']==1e-3),
 'local_diagnostics':local_checks,
 'limitations':['Source quartic generated numerically from retained helper not the unavailable byte-exact production file',
  'All global minimum values numerical, with dense checks, not certified interval minima',
  'One channel at a time; five nested mask readings with shared common positive gain',
  'Gaussian iid per-voxel additive ENERGY noise wholly synthetic, no experimental tau or channel cross-covariance',
  'Distances in noise whitened shell geometry; 95 percent radius interpretation assumes isotropic normal shell measurement noise',
  'A local Fisher optimum need not optimize nonlocal parameter separation; B2/6 has noiseless fold',
  'No general tensor TT/full field identifiability, no physical claim, no novelty, no canon, no EXEC']}
out=ROOT/'IW_M13_ROT36_global_shell_separation_20261025.json'
out.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('FROZEN',len(frozen_checks),max(frozen_checks),'LOCAL_FISHER_CHECK',result['max_local_tangent_relative_error_delta1e5'])
print('95PCT_GAUSSIAN_RADIUS',ci95)
for row in records:
 if row['alpha_true'] in (.0,.05,.10):
  z=row['best_global_pair'];l=row['best_local_pair']
  print(row['channel'],'a',row['alpha_true'],'five_sigma',round(row['five_masks_sep_in_sigma_units'],6),'nearest',round(row['five_masks_nearest_alt_alpha'],9),
   'global_best',z['masks'],'pair_sigma',round(z['global_min_distance_over_alpha_separated_0p01']/row['voxel_sigma_tau_1pct_mask2_baseline'],6),
   'local_best',l['masks'],'ratio_5_to_pair',round(row['full5_vs_bestpair_gain'],4))
print('FOLD_B26',fold)
print('STATUS_ROT36_GLOBAL_PROFILE_PASS')