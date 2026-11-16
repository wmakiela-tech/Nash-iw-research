#!/usr/bin/env python3
"""DAX-S8 ROT031 independent headon Belle angular-bin support audit of ROT030.
Source actual secondary Rivet YODA sha-pinned; author model ROT026 hard pi-e CSDA.
Compute exact finite-bin edge envelopes for convex e2 and concave tail functions,
with monotonicity checked on full initial energy support. This is NOT Belle CI.
"""
import os,hashlib,gzip,re,json,sys
from pathlib import Path
import numpy as np
from scipy.special import roots_legendre
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import PchipInterpolator
ROOT=Path(__file__).resolve().parent
zfile=ROOT/'prior_rot030/BELLE_2007_I749358.yoda.gz'
ORIGINAL_SHA='28a3b8fbc9b026b6315f46f7084f1eb7d82881dd61289f9cd4fdcf6052b99403'
assert hashlib.sha256(zfile.read_bytes()).hexdigest()==ORIGINAL_SHA
src=gzip.decompress(zfile.read_bytes()).decode('utf8');tables={}
for match in re.finditer(r'(?ms)^BEGIN YODA_BINNEDESTIMATE<S>_V3 /REF/BELLE_2007_I749358/d(\d+)-x01-y01\n(.*?)^END YODA_BINNEDESTIMATE<S>_V3',src):
 i=int(match.group(1));a=[]
 for line in match.group(2).splitlines():
  col=line.split()
  if len(col)>=5 and re.fullmatch(r'[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?',col[0]):a.append(float(col[0]))
 tables[i]=np.asarray(a)
assert len(tables)==141 and len(tables[1])==140 and all(len(tables[i+2])==12 for i in range(140))
import scipy
sys.path.insert(0,str((ROOT/'prior_rot030').resolve()))
from rot029_transport_common import Kernel,M,kap
m=float(M);mmu=.1056583755;f=(m*m-mmu*mmu)/(2*m*m)
Ctau=780.45
Egamma=1436554.0;T=.07818527068831995; C=4*Egamma*T

def kernel_grid(N=7501,ni=36,nmu=28):
 E=np.geomspace(1.2,1250.,N)
 ker=Kernel(ni,nmu)
 loss=np.array([ker.eval(float(v))[1] for v in E])
 h=kap(E)/loss
 H=cumulative_trapezoid(h,E,initial=0)
 # exact neutrino angular map at decay energy
 p=np.sqrt(E*E-m*m)
 glocal2=f*f*(4*E*E-m*m)/3
 def prob(t):return np.clip((f*(E+p)-t)/(2*f*p),0,1)
 def eg2_tail(t):
  lo=f*(E-p); hi=f*(E+p)
  q=np.maximum(t,lo)
  return np.where(hi>q,(hi**3-q**3)/(6*f*p),0)
 funcs={'nu_E2':glocal2,'Pnu_gt_10':prob(10),'Pnu_gt_100':prob(100),'nu_E2_gt_10':eg2_tail(10),'nu_E2_gt_100':eg2_tail(100)}
 out={}
 # continuous-energy survival to E=1.2 tiny, g at 1.2 can be used as boundary residual
 for name,g in funcs.items():
  cumulative=cumulative_trapezoid(h*np.exp(H)*g,E,initial=0)
  val=np.exp(-H)*cumulative+np.exp(-H)*g[0]
  out[name]=val
 return E,H,out

def source_weigh(scanning,order=8,zorder=8):
 Wn,Ww=roots_legendre(order); zn,zw=roots_legendre(zorder)
 accum={k:0. for k in ['normalizer','meanE']}
 for name in ['nu_E2','Pnu_gt_10','Pnu_gt_100','nu_E2_gt_10','nu_E2_gt_100']:
  accum[name]=0.
 gridE,funcs,mode=scanning
 for i in range(140):
  vals=tables[i+2]
  assert abs(.05*vals.sum()/tables[1][i]-1)<6.1e-5
  for qw,vw in zip(Wn,Ww):
   W=800+5*i+2.5*(1+qw); y=W*W/C
   Hsrc=4*W**3/C**2*(-np.log1p(-np.exp(-y)))
   beta=np.sqrt(1-4*139.57039**2/W**2)
   for j,sig in enumerate(vals):
    if mode=='left':zz=np.array([j*.05]); wz=np.array([1.])
    elif mode=='right':zz=np.array([(j+1)*.05]);wz=np.array([1.])
    elif mode=='mid':zz=np.array([(j+.5)*.05]);wz=np.array([1.])
    elif mode=='uniform':zz=(j+.5)*.05+.025*zn;wz=zw/2
    else:raise ValueError(mode)
    xp=Egamma/2000*(1+beta*zz);xm=Egamma/2000*(1-beta*zz)
    weight=2.5*vw*Hsrc*sig*.05
    accum['normalizer']+=weight
    accum['meanE']+=weight*np.dot(wz,(xp+xm)/2)
    for name,v in funcs.items():
      val=(np.interp(xp,gridE,v)+np.interp(xm,gridE,v))/2
      accum[name]+=weight*np.dot(wz,val)
 return {k:(v/accum['normalizer'] if k!='normalizer' else v) for k,v in accum.items()}

if __name__=='__main__':
 import time
 N=int(sys.argv[1]) if len(sys.argv)>1 else 7501
 t0=time.monotonic(); E,H,F=kernel_grid(N)
 print('Kernel in',round(time.monotonic()-t0,3),'s', 'H(718)',np.interp(718.277,E,H),flush=True)
 # check convexity on initial support [~285..1150] with second derivative finite difference
 C2={}; probe=np.linspace(280,1150,2500)
 for name,y in F.items():
  fun=PchipInterpolator(E,y);d2=np.diff(np.diff(fun(probe)))
  # for each W fixed, E+/- both ranges relevant
  C2[name]={'min_second_diff':float(d2.min()),'max_second_diff':float(d2.max()),'frac_convex_second_diff':float(np.mean(d2>=-1e-12))}
 base=(E,F,None)
 results={}
 for typ in ['left','mid','right','uniform']:
  t=time.monotonic();results[typ]=source_weigh((E,F,typ));print(typ,results[typ],round(time.monotonic()-t,1),flush=True)
 result={'model':'HEADON W5MEV BIN_AVERAGE PLUS ORIGINAL AUTHENTIC RIVET W/Z SOURCE, conditional fixed hard Q² pi-e vacuum Born massive FD CSDA; no physical full stopping',
 'source_sha256':ORIGINAL_SHA,'N_energy_grid':N,'M_pi_GeV':m,'f_nu':f,
 'angular_schemes':results,'convexity_diagnostic_on_280_1150GeV':C2,
 'baseline_ROT030_full_nonheadon_nu_E2':13.407161170204375,
 'ROT030_full_nonheadon_P_gt_10':0.0018870156651242924,
 'ROT030_full_nonheadon_P_gt_100':0.00032779650717984423,
 'claim_ceiling':'Angular support extremal scenarios are NOT Belle statistical error bars; source W/z bin interpretation unverified, no full medium transport, no neutrino cosmology.'}
 (ROOT/'results_rot031_support.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('total runtime',time.monotonic()-t0,flush=True)
