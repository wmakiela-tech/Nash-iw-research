#!/usr/bin/env python3
"""M16 ROT007, rank-comparison 2-snapshot blocks, source B vs its x/y permute Bpi.
SOURCE CONDITIONAL ONLY; classical Kendall tau identity, not general novelty.
"""
import json
import math
from fractions import Fraction
import mpmath as mp
import numpy as np

mp.mp.dps=85
r_B=Fraction(1,40)
r_P=Fraction(3,200)
f=lambda x:mp.mpf(x.numerator)/x.denominator
p_B=mp.mpf('0.5')+mp.asin(f(r_B))/mp.pi
p_P=mp.mpf('0.5')+mp.asin(f(r_P))/mp.pi
dp=p_B-p_P
eta_star=dp/2

# Two source snapshots per block. Stable within-block unknown spatial mean,
# arbitrary monotone site distortions, and positive scale mixture drawn per shot.
N=500_000
rng=np.random.default_rng(16226)
outputs={}
for name,r in [('B',r_B),('Bpi',r_P)]:
    rho=float(r)
    z=rng.standard_normal(size=(N,2,2)) # block, shot, sensor axis
    g0=z[:,:,0]
    g1=rho*g0+math.sqrt(1-rho*rho)*z[:,:,1]
    core=np.stack([g0,g1],axis=2)
    # S varying across both shots and across blocks (not a common block scale).
    scale=rng.choice([0.5,1.5],size=(N,2))
    source=np.sqrt(scale[:,:,None])*core
    # Mean profile varies adversarially per block, is constant between two shots.
    mu0=0.4+3.0*np.sin(np.arange(N)*.004)
    mu1=-2.0+2.0*np.cos(np.arange(N)*.007)
    shifted=source+np.stack([mu0,mu1],axis=1)[:,None,:]
    # Both strictly inc functions are VERY different per sensor and block.
    # g0 = asinh(x) + a ; g1 = exp(.1*(x-b)) (safe x range).
    offs=np.sin(np.arange(N)*.05)
    cal=np.empty_like(shifted)
    cal[:,:,0]=np.arcsinh(shifted[:,:,0])+offs[:,None]
    cal[:,:,1]=np.exp(.1*(shifted[:,:,1]-offs[:,None]))
    clean=((core[:,0,0]-core[:,1,0])*(core[:,0,1]-core[:,1,1])>0)
    mix=((source[:,0,0]-source[:,1,0])*(source[:,0,1]-source[:,1,1])>0)
    observed=((cal[:,0,0]-cal[:,1,0])*(cal[:,0,1]-cal[:,1,1])>0)
    # This equality is FALSE when positive volatility differs by shot; only the LAW is equal.
    assert np.array_equal(mix,observed)
    # Note: clean vs mix need not be pathwise same if scales vary across shots.
    outputs[name]={
      'blocks':N,'empirical_p_rank':float(observed.mean()),
      'theoretical_p':float(p_B if name=='B' else p_P),
      'absolute_sampling_error':float(abs(observed.mean()-float(p_B if name=='B' else p_P))),
      'gain_offset_monotone_pair_equal_fraction':float(np.mean(mix==observed)),
      'core_vs_mixed_pair_equal_fraction':float(np.mean(clean==mix)),
    }

assert dp>0
n_table=[]
for eta in ('0','0.0005','0.001','0.0015'):
  em=mp.mpf(eta)
  if em>=eta_star: raise AssertionError('selected eta must have positive robust gap')
  margin=eta_star-em
  row={'eta':eta}
  for alpha in ('0.05','0.01'):
    real=mp.log(1/mp.mpf(alpha))/(2*margin**2)
    blocks=int(mp.floor(real))+1
    assert mp.exp(-2*blocks*margin**2)<mp.mpf(alpha)
    assert mp.exp(-2*(blocks-1)*margin**2)>=mp.mpf(alpha)
    row['alpha_'+alpha+'_sufficient_blocks']=blocks
    row['alpha_'+alpha+'_raw_two_site_snapshot_pairs']=2*blocks
  n_table.append(row)

# adversarial per-comparison flips can make the observed paired-rank bits alias;
# legal kernel exactly follows M16 ROT006 with clean p_B,p_P.
pbar=(p_B+p_P)/2
a=eta_star/p_B
b=eta_star/(1-p_P)
assert 0<a<1 and 0<b<1
assert mp.almosteq(p_B*(1-a),pbar)
assert mp.almosteq(p_P+(1-p_P)*b,pbar)
# Same sign-bit distribution applies beyond normal marginal scales, but
# not arbitrary non-elliptical distributions or nonstable within-block means.
result={
  'return_id':'M16_ROT007_BLOCK_RANK_CALIBRATION_EXTERNAL_PRIOR_ART_SUBTRACTED',
  'correlations':{'B':str(r_B),'Bpi':str(r_P)},
  'p_B':mp.nstr(p_B,70),'p_Bpi':mp.nstr(p_P,70),
  'delta_p':mp.nstr(dp,70),'critical_model_dependent_pair_bit_error':mp.nstr(eta_star,70),
  'resource_table':n_table,
  'nonGaussian_scale_mixture_monte_carlo':outputs,
  'alias_two_hypothesis_markov_kernels':{'B_1_to_0':mp.nstr(a,30),'Bpi_0_to_1':mp.nstr(b,30)},
  'scope':'Two IID Gaussian core pairs per block, independent positive shot scales, block-stable spatial means, each channel identical strict monotone function across its 2 shots, source conditional, no hardware, classical Kendall 2001, no novelty, no canon, no exec sign'
}
with open('/mnt/data/m16_rot007/m16_rot007_result.json','w',encoding='utf-8') as q: json.dump(result,q,indent=2,ensure_ascii=False)
print(json.dumps(result,indent=2,ensure_ascii=False))
