#!/usr/bin/env python3
"""INT8-050 minimal actual byte-gated auxiliary K_C/K_B/K_A source witness."""
import argparse,hashlib,importlib.util,io,contextlib
from pathlib import Path
import numpy as np
SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
p=argparse.ArgumentParser();p.add_argument('--source',required=True);args=p.parse_args()
assert hashlib.sha256(Path(args.source).read_bytes()).hexdigest()==SHA
spec=importlib.util.spec_from_file_location('i50_retained_helper',args.source);m=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
for N in [7,9]:
 h=2*np.pi/N;idx=np.indices((N,N,N));x,y,z=h*idx[0],h*idx[1],h*idx[2]
 C1=np.zeros((N,N,N,3));C2=C1.copy();C1[...,2]=np.sin(x+2*y);C2[...,2]=np.sin(2*x-y)
 S=np.array([[1,.23,.31],[.23,-.5,-.21],[.31,-.21,.74]])
 H=np.broadcast_to(S,(N,N,N,3,3)).copy()
 for mode in ['Identity','E_lin']:
  KC=m.compute_K_C(C1,C2,H,mode,h,2,.05);KB=m.compute_K_B(C1,C2,H,mode,h,2,.05)
  KA=m.compute_K_A_out(C1,C2,H,mode,h,2,.05)
  s1=np.sin(h)/h;s2=np.sin(2*h)/h;d=2*s1-s2;t=(s1+2*s2)/5
  e=1 if mode=='Identity' else 1-4*.05*(np.sin(h/2)**2+np.sin(h)**2)
  expected=e*e*d*d*(t*t*S[2,2]**2/2+(s1*s1+s2*s2)*(S[0,2]**2+S[1,2]**2)/20)
  rms=lambda T:np.sqrt(np.mean(np.sum(T*T,axis=(-2,-1))))
  assert max(rms(KC),rms(KB))<2e-11 and abs(rms(KA)**2-expected)<2e-11
  print('ORIGINAL_SOURCE_PASS',N,mode,'KA_RMS',float(rms(KA)))
