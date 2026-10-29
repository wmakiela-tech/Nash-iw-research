#!/usr/bin/env python3
"""Minimal original helper test of commuting z-shear projected commutator, odd grids."""
import argparse,hashlib,importlib.util,contextlib,io
import numpy as np
SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
def source(path):
 assert hashlib.sha256(open(path,'rb').read()).hexdigest()==SHA
 spec=importlib.util.spec_from_file_location('dtc0a_rot047',path)
 m=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
 return m
def witness(m,N):
 h=2*np.pi/N;ix=np.indices((N,N,N));x=h*ix[0];y=h*ix[1]
 A=np.zeros((N,N,N,3));B=A.copy()
 A[...,2]=np.sin(x+2*y);B[...,2]=np.sin(x+y)
 H=np.broadcast_to(np.eye(3),(N,N,N,3,3)).copy()
 kc=m.compute_K_C(A,B,H,'Identity',h,2,.05)
 kb=m.compute_K_B(A,B,H,'Identity',h,2,.05)
 ka=m.compute_K_A_out(A,B,H,'Identity',h,2,.05)
 s1=np.sin(h)/h;s2=np.sin(2*h)/h;d=2*s1-s2
 ez=np.array([0.,0.,1.]);wp=np.array([3.,-2.,0.])/np.sqrt(13);wm=np.array([1.,0.,0.])
 target=-(4*s1*d/65)*np.cos(2*x+3*y)[...,None,None]*(np.outer(wp,wp)-np.outer(ez,ez))-(s1*d/5)*np.cos(y)[...,None,None]*(np.outer(wm,wm)-np.outer(ez,ez))
 err=np.max(abs(ka-target));rms=np.sqrt(np.mean(np.sum(ka*ka,axis=(-2,-1))))
 expected=abs(s1*d)*np.sqrt(185)/65
 assert max(np.max(abs(kc)),np.max(abs(kb)))<2e-11
 assert err<2e-11 and abs(rms-expected)<2e-11
 print('SOURCE PASS',N,'KC~0 KB~0 KA_RMS=',round(float(rms),12),'field error=',round(float(err),13))
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--source',required=True);a=p.parse_args()
 m=source(a.source)
 for N in [7,9,11,15]:witness(m,N)
