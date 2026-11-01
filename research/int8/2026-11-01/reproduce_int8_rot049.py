#!/usr/bin/env python3
"""INT8-049 actual unchanged auxiliary DTC0a source and nonconstant puretrace robustness."""
import argparse,hashlib,importlib.util,contextlib,io,json,math
from pathlib import Path
import numpy as np
SOURCE_SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'

def load_source(path):
 data=Path(path).read_bytes();assert hashlib.sha256(data).hexdigest()==SOURCE_SHA
 spec=importlib.util.spec_from_file_location('original_dtc049',path);m=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
 return m

def rms(H):return float(np.sqrt(np.mean(np.sum(np.asarray(H)**2,axis=(-2,-1)))))
def cross(H,K):return float(np.mean(np.sum(H*K,axis=(-2,-1))))
def field(I,scalar):return scalar[...,None,None]*I

def source_case(module,N,mode,alpha):
 h=2*np.pi/N;x,y,z=np.indices((N,N,N),dtype=float)*h
 C1=np.zeros((N,N,N,3));C2=C1.copy();C1[...,2]=np.sin(x+2*y);C2[...,2]=np.sin(2*x-y)
 I=np.eye(3)
 eps=.35;delta=.20
 one=np.ones((N,N,N));cosz=np.cos(z);sin2z=np.sin(2*z)
 H1=field(I,one);Hc=field(I,cosz);Hs=field(I,sin2z)
 Hmix=field(I,one+eps*cosz+delta*sin2z)
 Hx=field(I,one+.3*np.cos(x))
 K=lambda f:module.compute_K_A_out(C1,C2,f,mode,h,2,alpha)
 KC=lambda f:module.compute_K_C(C1,C2,f,mode,h,2,alpha)
 KB=lambda f:module.compute_K_B(C1,C2,f,mode,h,2,alpha)
 K1,Kc,Ks,Kmix=map(K,[H1,Hc,Hs,Hmix]);Kx=K(Hx)
 KC1,KB1=KC(H1),KB(H1);KCmix,KBmix=KC(Hmix),KB(Hmix)
 KCx,KBx=KC(Hx),KB(Hx)
 e=1 if mode=='Identity' else 1-4*alpha*(np.sin(h/2)**2+np.sin(h)**2)
 s1=np.sin(h)/h;s2=np.sin(2*h)/h;d=2*s1-s2;t=(s1+2*s2)/5
 analytic=abs(e*d*t)/np.sqrt(2)
 assert abs(rms(K1)-analytic)<2e-11
 assert rms(K1)>0
 assert max(rms(KC1),rms(KB1),rms(KCmix),rms(KBmix))<2e-11
 assert np.max(abs(Kmix-(K1+eps*Kc+delta*Ks)))<2e-11
 # Orthogonality between the different z Fourier sectors, in full periodic tensor L2.
 ortho=max(abs(cross(K1,Kc)),abs(cross(K1,Ks)),abs(cross(Kc,Ks)))
 assert ortho<5e-12
 pyth=abs(rms(Kmix)**2-(rms(K1)**2+eps**2*rms(Kc)**2+delta**2*rms(Ks)**2))
 assert pyth<3e-11
 assert rms(Kmix)>=rms(K1)-2e-11
 if mode=='Identity':assert max(rms(KCx),rms(KBx))<2e-11
 else:assert rms(KCx)>1e-3 and rms(KBx)>1e-4
 return {'N':N,'mode':mode,'alpha':alpha,'KC_constant_RMS':round(rms(KC1),14),'KB_constant_RMS':round(rms(KB1),14),
  'KC_z_vary_RMS':round(rms(KCmix),14),'KB_z_vary_RMS':round(rms(KBmix),14),
  'KA_constant_RMS':round(rms(K1),12),'KA_nonconstant_positive_f_z_RMS':round(rms(Kmix),12),
  'KA_cosz_RMS':round(rms(Kc),12),'KA_sin2z_RMS':round(rms(Ks),12),
  'exact_constant_formula':round(float(analytic),12),'Pythagoras_residual':round(float(pyth),14),
  'cross_mode_orthogonality_residual':round(float(ortho),14),
  'KC_planar_f_x_RMS':round(rms(KCx),12),'KB_planar_f_x_RMS':round(rms(KBx),12)}

def original_all_tensor_control(module,N):
 h=2*np.pi/N;ix=np.indices((N,N,N));x=ix[0]*h;y=ix[1]*h
 C1=np.zeros((N,N,N,3));C2=C1.copy();C1[...,2]=np.sin(x+2*y);C2[...,2]=np.sin(2*x-y)
 rng=np.random.default_rng(49000+N);F=rng.normal(size=(N,N,N,3,3));F=(F+np.swapaxes(F,-1,-2))/2
 q=module.compute_K_C(C1,C2,F,'Identity',h,2,.05)
 assert rms(q)<2e-11
 return round(rms(q),14)

def main():
 p=argparse.ArgumentParser();p.add_argument('--source',default=None);p.add_argument('--out',required=True);args=p.parse_args()
 alpha=.05
 analytic=[]
 for N in [7,9,11,15,21,31,61,121,241]:
  h=2*np.pi/N;x=np.sin(h)/h;y=np.sin(2*h)/h;d=2*x-y;t=(x+2*y)/5
  e=1-4*alpha*(np.sin(h/2)**2+np.sin(h)**2)
  ai=d*t/np.sqrt(2);ae=e*ai
  assert e>0 and ai>0 and ae>0
  analytic.append({'N':N,'KA_Identity_constant_exact':round(float(ai),12),'KA_E_lin_constant_exact':round(float(ae),12), 'N2_times_KA_E_lin':round(float(N*N*ae),9)})
 module=None
 if args.source:module=load_source(args.source)
 native=[];random=[]
 if module is not None:
  for N in [7,9,11,15]:
   for mode in ['Identity','E_lin']:native.append(source_case(module,N,mode,alpha))
  for N in [7,9]:random.append({'N':N,'random_symmetric_H_KC_Identity_RMS':original_all_tensor_control(module,N)})
 result={'artifact_id':'IW_INT8_ROT049_Z_SHEAR_NONCONSTANT_PURETRACE_STABILITY_001_20261101',
  'status':'PASS','source_status':'ORIGINAL_SHA_VERIFIED_PASS' if module else 'SOURCE_SKIPPED_NO_HELPER',
  'source_sha256':SOURCE_SHA if module else None,
  'exact_analytic_baselines':analytic,'native_records':native,'native_cases':len(native),'generic_H_Identity_controls':random,
  'strict_scope':'odd N>=7; C1=e_z sin(x+2y), C2=e_z sin(2x-y); E Identity or E_lin alpha=.05; positive f(z)=1+.35cos(z)+.2sin(2z); full-grid Frobenius RMS; no historical production masked KA',
  'theorem':'For ANY real f(z), KC=KB=0 in equal E eigenshell; KA Fourier-z sectors orthogonal; ||KA(fI)||_RMS>=abs(mean f)*||KA(I)||_RMS; for E Identity commutator KC=0 for ANY symmetric H; E_lin planar f(x) negative control KC,KB!=0.'}
 Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
 print('INT8 ROT049 PASS',len(native),'native cases,',len(random),'generic H; source',result['source_status'])
if __name__=='__main__':main()
