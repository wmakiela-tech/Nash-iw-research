#!/usr/bin/env python3
"""Original SHA-pinned DTC0a source witness for 12D real dark sectors at N7 and N9."""
import argparse,hashlib,importlib.util,contextlib,io
from pathlib import Path
import numpy as np
SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
parser=argparse.ArgumentParser();parser.add_argument('--source',required=True);arg=parser.parse_args()
assert hashlib.sha256(Path(arg.source).read_bytes()).hexdigest()==SHA
sp=importlib.util.spec_from_file_location('int8_051_retained_original',arg.source)
mod=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(mod)
B=[]
for i in range(3):
 S=np.zeros((3,3));S[i,i]=1;B.append(S)
for i,j in [(0,1),(0,2),(1,2)]:
 S=np.zeros((3,3));S[i,j]=S[j,i]=1/np.sqrt(2);B.append(S)
for N,ell,alpha in [(7,3,1/7),(9,4,1/6)]:
 h=2*np.pi/N;ix=np.indices((N,N,N));x=h*ix[0];y=h*ix[1];z=h*ix[2]
 Ca=np.zeros((N,N,N,3));Cb=Ca.copy();Ca[...,2]=np.sin(x+2*y);Cb[...,2]=np.sin(2*x-y)
 S=np.eye(3)+.31*B[4]
 inner=mod.projected_T(Cb,np.cos(ell*z)[...,None,None]*S,'E_lin',h,2,alpha)
 post=mod.apply_E(inner,'E_lin',h,2,alpha)
 assert np.linalg.norm(inner)>1 and np.linalg.norm(post)<5e-10
 for T in B:
  for f in (np.cos,np.sin):
   H=f(ell*z)[...,None,None]*T
   K=mod.compute_K_A_out(Ca,Cb,H,'E_lin',h,2,alpha)
   assert np.max(np.abs(K))<5e-10
 # Near-parameter control: the SAME nonzero input is not dark for alpha=.05.
 H=np.cos(ell*z)[...,None,None]*S
 Knear=mod.compute_K_A_out(Ca,Cb,H,'E_lin',h,2,.05)
 assert np.linalg.norm(Knear)>1e-4
 print('SOURCE_PASS',N,'ell',ell,'alpha',alpha,'12 basis real inputs dark, intermediate nonzero, control visible')
