#!/usr/bin/env python3
"""Minimal source-aware INT8-046 test. Needs NumPy and optional exact SHA-pinned user DTC0a helper."""
import argparse,hashlib,importlib.util,contextlib,io,math
from pathlib import Path
import numpy as np
SOURCE_SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
def verify(N,k,src):
 h=2*math.pi/N
 k=np.array(k,float);s=np.sin(k*h)/h;sp=s-k*(k@s)/(k@k)
 x=np.indices((N,N,N));phase=h*sum(int(k[i])*x[i] for i in range(3))
 C=np.zeros((N,N,N,3));C[...,2]=np.sin(phase)
 I=np.broadcast_to(np.eye(3),(N,N,N,3,3)).copy()
 v=np.zeros_like(I)
 for i in range(3):
  v[...,i,2]+=sp[i]*np.cos(phase)
  v[...,2,i]+=sp[i]*np.cos(phase)
 if src is not None:
  actual=src.projected_T(C,I,'E_lin',h,2,.05)
  err=np.max(abs(v-actual))
  assert err<9e-12,(N,err)
 else:err=None
 rms=np.sqrt(np.mean(np.sum(v*v,axis=(-2,-1))))
 assert abs(rms-np.linalg.norm(sp))<3e-12
 print('PASS',N,tuple(k.astype(int)),'RMS',round(float(rms),12),'source_residual',err)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',default=None);arg=p.parse_args()
 src=None
 if arg.source:
  data=Path(arg.source).read_bytes();assert hashlib.sha256(data).hexdigest()==SOURCE_SHA
  sp=importlib.util.spec_from_file_location('source_dtc046',arg.source);src=importlib.util.module_from_spec(sp)
  with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(src)
 for N,k in [(5,(1,2,0)),(9,(1,4,0)),(15,(1,7,0)),(31,(1,15,0)),(9,(1,1,0))]:verify(N,k,src)
 print('END', 'SOURCE_SHA_VERIFIED_PASS' if src else 'SOURCE_SKIPPED_NO_HELPER')
