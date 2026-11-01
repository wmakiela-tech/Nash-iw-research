#!/usr/bin/env python3
"""Public minimal INT8-048 native source witness, with exact SHA gate and full-field identity."""
import argparse,hashlib,importlib.util,contextlib,io
from pathlib import Path
import numpy as np
SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
def source(path):
 assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==SHA
 sp=importlib.util.spec_from_file_location('frozen_dtc048',path);m=importlib.util.module_from_spec(sp)
 with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(m)
 return m
def check(N,mode,alpha,mod):
 h=2*np.pi/N;x=np.indices((N,N,N));u=h*(x[0]+2*x[1]);v=h*(2*x[0]-x[1]);
 C1=np.zeros((N,N,N,3));C2=C1.copy();C1[...,2]=np.sin(u);C2[...,2]=np.sin(v)
 H=np.broadcast_to(np.eye(3),(N,N,N,3,3)).copy()
 s1=np.sin(h)/h;s2=np.sin(2*h)/h;d=2*s1-s2;t=(s1+2*s2)/5
 e=1 if mode=='Identity' else 1-4*alpha*(np.sin(h/2)**2+np.sin(h)**2)
 z=np.array([0.,0.,1.]);np_=np.array([1.,-3.,0.])/np.sqrt(10);nm=np.array([3.,1.,0.])/np.sqrt(10)
 Wp=np.outer(np_,np_)-np.outer(z,z);Wm=np.outer(nm,nm)-np.outer(z,z)
 want=-e*d*t/2*(np.cos(u+v)[...,None,None]*Wp+np.cos(u-v)[...,None,None]*Wm)
 rms=np.sqrt(np.mean(np.sum(want*want,axis=(-2,-1))))
 assert abs(rms-e*d*t/np.sqrt(2))<2e-12
 if mod is None:print('ANALYTIC_PASS',N,mode,'RMS',round(float(rms),12),'SOURCE_SKIPPED_NO_HELPER');return
 kc=mod.compute_K_C(C1,C2,H,mode,h,2,alpha)
 kb=mod.compute_K_B(C1,C2,H,mode,h,2,alpha)
 ka=mod.compute_K_A_out(C1,C2,H,mode,h,2,alpha)
 err=max(np.max(abs(kc)),np.max(abs(kb)),np.max(abs(ka-want)))
 assert err<2e-11 and rms>0
 print('ORIGINAL_SHA_VERIFIED_PASS',N,mode,'RMS',round(float(rms),12),'max_error',float(err))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--source',default=None);args=ap.parse_args()
 m=source(args.source) if args.source else None
 for N in [7,9,15,31]:
  for mode in ['Identity','E_lin']:check(N,mode,.05,m)
