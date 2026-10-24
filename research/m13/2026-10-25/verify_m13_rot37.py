#!/usr/bin/env python3
"""M13 ROT37: nonlocal source-conditional lower separation certificate.
NOT an exact optimizer. Intervals are from retained source formulas, not historical runtime bytes.
Assumptions: common positive gain of mean energy, independent equal-variance per-voxel
noise, fixed source, N41, masks 2..6, alpha in [0,1/5].
"""
import json,math,csv
from pathlib import Path
from mpmath import iv
from verify_m13_rot33_interval import tensor_polys,quartic,bernstein,polyd,ZERO
iv.dps=45
BASE=Path(__file__).resolve().parent
N=41; DELTA=iv.mpf(1)/100; TRUE_ALPHA=iv.mpf(1)/20
pairs=[('A',2,5),('B',5,6),('C',2,4)]

def polyeval(p,x):
 val=iv.mpf(0)
 for c in reversed(p):val=val*x+c
 return val

def lower(q):return q.a

def upper(q):return q.b

def enclosure_of_poly(p):
 bb=bernstein(p)
 lo=min((x.a for x in bb),key=lambda v:float(v))
 hi=max((x.b for x in bb),key=lambda v:float(v))
 return lo,hi

def sub(a,b):return [x-y for x,y in zip(a,b)]

def derivative(a):return [iv.mpf(i)*a[i] for i in range(1,len(a))]

def gamma_lower(g1,g2,sign,nsub=80):
 p=polyd(g1,g2); gammas=[]
 for i in range(nsub):
  left=iv.mpf(i)/(5*nsub);right=iv.mpf(i+1)/(5*nsub)
  I=iv.mpf([left.a,right.b]); d1=polyeval(g1,I);d2=polyeval(g2,I)
  assert d1.a>0 and d2.a>0
  derivative_log=p and polyeval(p,I)/(2*d1*d2)
  if sign=='UP':assert derivative_log.a>0; gammas.append(derivative_log.a)
  else: assert derivative_log.b<0;gammas.append(-derivative_log.b)
 return min(gammas,key=lambda v:float(v))

# Squared-RMS quartic representation for every channel/mask.
pols=tensor_polys(N)
G={}
for k in (2,3,4,5,6):
 cache={}
 for idx,ch in enumerate('ABC'):
  G[ch,k]=quartic(pols[idx],N,k,cache)

# Verify frozen source-matched historical numerical RMS.
frozen={(r['alpha'],int(r['interior_k'])):r for r in csv.DictReader((BASE/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open())}
err=0.
for ch in 'ABC':
 for k in (2,3,4,5,6):
  for an,a in [('0.0',iv.mpf(0)),('0.05',iv.mpf(1)/20),('0.2',iv.mpf(1)/5)]:
   found=math.sqrt(float(polyeval(G[ch,k],a).mid))
   target=float(frozen[an,k]['K_'+ch+'_RMS'])
   err=max(err,abs(found/target-1))
assert err<1e-11,err

results=[]
for ch,ki,kj in pairs:
 ni=(N-2*ki)**3;nj=(N-2*kj)**3;v=ni-nj
 gi,gj=G[ch,ki],G[ch,kj]
 lognumer=polyd(gi,gj)
 pb=bernstein(lognumer)
 sign='UP' if all(z.a>0 for z in pb) else ('DOWN' if all(z.b<0 for z in pb) else None)
 assert sign
 gamma=gamma_lower(gi,gj,sign)
 assert gamma.a>0
 imin,imax=enclosure_of_poly(gi); jmin,jmax=enclosure_of_poly(gj)
 assert imin.a>0 and jmin.a>0
 shell=[(ni*gi[l]-nj*gj[l])/v for l in range(5)]
 shellmin,shellmax=enclosure_of_poly(shell)
 assert shellmin.a>0 and shellmax.b>0
 # Upper bound on candidate profile norm: v*mean(shell)^2 + nj*mean(inner)^2.
 candidate_max=iv.mpf(v)*shellmax**2+iv.mpf(nj)*jmax**2
 # Exact determinant of inverse covariance (with tau^2 removed): ni^2*nj/(ni-nj).
 detW=iv.mpf(ni)**2*nj/v
 # All alpha_true, alpha_candidate in [0,.2], separated by DELTA:
 # |det(g(alpha),g(beta))| >= gi_min * gj_min * (exp(2 gamma Delta)-1)
 # because |log((gi/gj)(a)/(gi/gj)(b))| >= 2 gamma Delta.
 expdiff=iv.exp(2*gamma*DELTA)-1
 det_lower_all=imin*jmin*expdiff
 separation_all=det_lower_all*iv.sqrt(detW/candidate_max)
 # Sharper lower for fixed alpha_true=.05, using known true values in determinant.
 ait=polyeval(gi,TRUE_ALPHA);ajt=polyeval(gj,TRUE_ALPHA)
 true_min_prod=min([ait*jmin,ajt*imin],key=lambda q:float(q.a)).a
 separation_05=true_min_prod*expdiff*iv.sqrt(detW/candidate_max)
 tau=.01*polyeval(G[ch,2],TRUE_ALPHA) # synthetically calibrated 1% per voxel energy noise
 sigma_all=separation_all/tau
 sigma_05=separation_05/tau
 # Internal numerical check against independently archived ROT36 min distance to OTHER alpha .01
 prev=json.loads((BASE/'IW_M13_ROT36_global_shell_separation_20261025.json').read_text())
 row=next(r for r in prev['records'] if r['channel']==ch and r['alpha_true']==.05)
 p=next(r for r in row['all_pairs'] if r['masks']==[ki,kj])
 numeric_dist=p['global_min_distance_over_alpha_separated_0p01']
 assert float(separation_05.b)<numeric_dist,(ch, float(separation_05.b),numeric_dist)
 assert float(separation_all.b)<numeric_dist
 # Additional internal exact equality of 2x2 profile with weighted shell distance via deterministic doubles.
 testA=[float(ait.mid),float(ajt.mid)]
 testB=[float(polyeval(gi,iv.mpf(1)/10).mid),float(polyeval(gj,iv.mpf(1)/10).mid)]
 S=[[1/ni,1/ni],[1/ni,1/nj]]
 import numpy as np
 W=np.linalg.inv(np.array(S));a=np.array(testA);b=np.array(testB)
 t=a@W@b/(b@W@b)
 sq=(a-t*b)@W@(a-t*b)
 dq=(np.linalg.det(np.column_stack((a,b)))**2)*(np.linalg.det(W))/(b@W@b)
 assert abs(sq-dq)<1e-24,(ch,sq,dq)
 record={'channel':ch,'pair':[ki,kj],'sign':sign,'n_voxels':[ni,nj],
  'log_RMS_derivative_abs_lower':float(gamma.a),
  'bounds_gi':[float(imin.a),float(imax.b)],'bounds_gj':[float(jmin.a),float(jmax.b)],
  'bounds_outer_shell':[float(shellmin.a),float(shellmax.b)],
  'interval_certified_separation_any_true_alpha_energy_metric_lower':float(separation_all.a),
  'interval_certified_separation_true_alpha0p05_energy_metric_lower':float(separation_05.a),
  'interval_certified_min_distance_sigma_all_alphas_lower':float(sigma_all.a),
  'interval_certified_min_distance_sigma_alpha0p05_lower':float(sigma_05.a),
  'ROT36_uncertified_numerically_minimized_pair_distance':numeric_dist,
  'ROT36_numeric_distance_sigma':numeric_dist/float(tau.mid),
  'global_noise_calibration':'tau=0.01*g(channel,mask2,alpha=.05) per voxel (ENERGY, synthetic)',
  'conservatism': 'Bernstein extrema and pair determinant bound discard cross-component correlations; cert is NOT exact global minimum'}
 results.append(record)
 print(ch,ki,kj,'monotone',sign,'gamma>=',record['log_RMS_derivative_abs_lower'],
  'CERT sigma all alpha>=',record['interval_certified_min_distance_sigma_all_alphas_lower'],
  'alpha05>=',record['interval_certified_min_distance_sigma_alpha0p05_lower'],
  'ROT36 pair numeric sigma~',record['ROT36_numeric_distance_sigma'],flush=True)
# Tighter fixed-alpha_true=.05 result. Cover every beta in [0,.04] U [.06,.2]
# by 1000 closed subintervals per branch and interval-profile the exact 2D geometry.
# These are LOWER bounds on the infimum; they do not certify an exact argmin.
for record in results:
 ch,ki,kj=record['channel'],*record['pair'];gi,gj=G[ch,ki],G[ch,kj]
 ni,nj=(N-2*ki)**3,(N-2*kj)**3;v=ni-nj
 a_i=polyeval(gi,TRUE_ALPHA);a_j=polyeval(gj,TRUE_ALPHA)
 detW=iv.mpf(ni)**2*nj/v
 tau=.01*polyeval(G[ch,2],TRUE_ALPHA)
 lower_piece=[];num=1000
 for elo,ehi in [(iv.mpf(0),iv.mpf(4)/100),(iv.mpf(6)/100,iv.mpf(1)/5)]:
  for step in range(num):
   lo=elo+(ehi-elo)*step/num
   hi=elo+(ehi-elo)*(step+1)/num
   ib=iv.mpf([lo.a,hi.b]);b_i=polyeval(gi,ib);b_j=polyeval(gj,ib)
   b_shell=(ni*b_i-nj*b_j)/v
   assert b_i.a>0 and b_j.a>0 and b_shell.a>0
   det=a_i*b_j-a_j*b_i
   assert det.a>0 or det.b<0,('interval sign fail',ch,step,str(det))
   absdet=det if det.a>0 else -det
   q=v*b_shell*b_shell+nj*b_j*b_j
   assert q.a>0
   d=absdet*iv.sqrt(detW/q)
   assert d.a>0
   lower_piece.append(d/tau)
 best=min(lower_piece,key=lambda q:float(q.a))
 record['interval_partition_size_per_branch']=num
 record['interval_certified_min_separation_sigma_alpha0p05_subdivided_lower']=float(best.a)
 print(ch,'REFINED_CERT',record['interval_certified_min_separation_sigma_alpha0p05_subdivided_lower'],
  'ROT36 numeric',record['ROT36_numeric_distance_sigma'],flush=True)
 assert record['interval_certified_min_separation_sigma_alpha0p05_subdivided_lower'] <= record['ROT36_numeric_distance_sigma']*(1+1e-6)

# Stronger theorem for TWO nested masks only: the weighted shell vector
# L(g_i,g_j)=(sqrt(n_i-n_j)*(n_i*g_i-n_j*g_j)/(n_i-n_j), sqrt(n_j)*g_j)
# lies in the positive quadrant as long as shell/core energies are positive.
# Its polar angle is strictly monotone in r=g_i/g_j, because the transformation
# L is invertible (det !=0). For monotone r(alpha), angular separation from
# a fixed alpha increases along either alternative branch; positive-quadrant
# angular differences lie in [0, pi/2), where sine is strictly increasing.
# Therefore the global profile inf for |beta-alpha|>=Delta is EXACTLY achieved
# at beta=alpha-Delta and/or beta=alpha+Delta, if legal.
for record in results:
 ch,ki,kj=record['channel'],*record['pair'];gi,gj=G[ch,ki],G[ch,kj]
 ni,nj=(N-2*ki)**3,(N-2*kj)**3;v=ni-nj
 a_i=polyeval(gi,TRUE_ALPHA);a_j=polyeval(gj,TRUE_ALPHA)
 tau=.01*polyeval(G[ch,2],TRUE_ALPHA)
 endpoint=[]
 for beta in (iv.mpf(4)/100,iv.mpf(6)/100):
  b_i=polyeval(gi,beta);b_j=polyeval(gj,beta)
  shell=(ni*b_i-nj*b_j)/v
  assert b_i.a>0 and b_j.a>0 and shell.a>0
  det=a_i*b_j-a_j*b_i
  assert det.a>0 or det.b<0
  absdet=det if det.a>0 else -det
  q=v*shell**2+nj*b_j**2
  d=absdet*iv.sqrt((iv.mpf(ni)**2*nj/v)/q)/tau
  endpoint.append((float(beta.mid),d))
 best=min(endpoint,key=lambda p:float(p[1].a))
 record['exact_argmin_alpha_candidates']=[x[0] for x in endpoint]
 record['endpoint_distance_sigma_intervals']={str(x[0]):[float(x[1].a),float(x[1].b)] for x in endpoint}
 second=max(endpoint,key=lambda q:float(q[1].a))
 assert best[1].b < second[1].a,('endpoint minimizer not distinguished',ch)
 record['strict_endpoint_winner_interval_certified']=True
 record['certified_inf_distance_sigma_alpha0p05_lower']=float(best[1].a)
 record['certified_inf_distance_sigma_alpha0p05_upper']=float(best[1].b)
 record['exact_global_argmin_alpha']=best[0]
 record['numerical_ROТ36_gap_to_certified_inf']=record['ROT36_numeric_distance_sigma']-float(best[1].mid)
 assert abs(record['numerical_ROТ36_gap_to_certified_inf'])<1e-7,record
 print(ch,'EXACT_ENDPOINT_GLOBAL_INF ALPHA',best[0],
  'CERT SIGMA',float(best[1].a),float(best[1].b),
  'ROT36 delta',record['numerical_ROТ36_gap_to_certified_inf'],flush=True)

output={'return_id':'M13-ROT37-DTC0A-INTERVAL-CERTIFIED-GLOBAL-LOWER-SEPARATION-001_20261025',
 'N':N,'alpha_interval':['0','1/5'],'minimum_alpha_separation':'1/100',
 'statement':'source-formula interval-certified lower bounds for optimally re-gained 2-mask GLS distance for ANY alpha,beta with |alpha-beta|>=.01; five-mask GLS distance >= any pair distance',
 'positive_gain_reason':'channel energies and shell energy polynomials strictly positive over interval, so unconstrained positive projection valid',
 'source_arithmetic':'mpmath.iv 45 digits, exact rational modes and TT symbol, outward-rounded trigonometric stencil and masked sums',
 'certificate_type':'rigorous conditional arithmetic interval bound assuming mpmath.iv outward rounding and retained functional source',
 'noise_model':'iid Gaussian additive voxel ENERGY noise only for reporting normalized tau; positive distances independent of Gaussianity',
 'historical_RMS_45_max_rel_error':err,'results':results,
 'limitations':['DOES NOT certify ROT36 exact global MINIMIZER or sharpen numerical optimum','Different channels use different entirely synthetic tau; sigma values not empirical cross-channel comparisons','Only source-specific known generator and shared positive gain, no unknown channel/mask gains','Conditional on mpmath.iv outward rounding and correct source-formula reconstruction','Original historical runtime bytes absent; no physical, gauge, J3/K, TPE upgrade']}
path=BASE/'IW_M13_ROT37_interval_global_lower_20261025.json';path.write_text(json.dumps(output,indent=2,sort_keys=True,ensure_ascii=False)+'\n')
print('ROT37_CERTIFIED_GLOBAL_NONLOCAL_LOWER_PASS / FROZEN 45 / STATUS_NO_PHYSICS')
