#!/usr/bin/env python3
"""ROT31: 3-D, coordinate-band-1 genuine Fourier TT nonidentifiability.
Numeric construction with 26 real cosine TT basis vectors. Independent
finite-field determinant certificate is in verify_m13_rot31_exact.py.
"""
import itertools, hashlib, json, importlib.util, os, time
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent
N=41; masks=(2,3,4,5,6); theta=2*np.pi/N
helper=ROOT/'deepseek_python_20260627_a87249.py'
sha=hashlib.sha256(helper.read_bytes()).hexdigest()
assert sha=='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
spec=importlib.util.spec_from_file_location('retained_dtc0a',helper)
dtc=importlib.util.module_from_spec(spec);spec.loader.exec_module(dtc)

modes=[k for k in itertools.product((-1,0,1),repeat=3) if k!=(0,0,0) and k<=tuple(-v for v in k)]
assert len(modes)==13
symmetric=[]
for i in range(3):
 for j in range(i,3):
  A=np.zeros((3,3));A[i,j]=1/np.sqrt(2 if i!=j else 1);A[j,i]=A[i,j]
  symmetric.append(A)

def proj(k,A):
 k=np.asarray(k,float);p=np.eye(3)-np.outer(k,k)/np.dot(k,k)
 return p@A@p-.5*p*np.trace(p@A)

pol=[];mode_list=[]
for k in modes:
 frame=[]
 for E in symmetric:
  Q=proj(k,E)
  for X in frame:Q-=np.sum(X*Q)*X
  qn=np.linalg.norm(Q)
  if qn>1e-8:frame.append(Q/qn)
  if len(frame)==2:break
 assert len(frame)==2
 for B in frame:mode_list.append(k);pol.append(B)
pol=np.array(pol);d=len(pol)
assert d==26

def dirichlet(q,n):
 if q==0:return 1.
 return np.sin(n*q*np.pi/N)/(n*np.sin(q*np.pi/N))
def cc(k,l,n):
 return .5*(np.prod([dirichlet(k[i]-l[i],n) for i in range(3)])+np.prod([dirichlet(k[i]+l[i],n) for i in range(3)]))

def Gram(mask):
 n=N-2*mask
 G=np.empty((d,d))
 for a,k in enumerate(mode_list):
  for b,l in enumerate(mode_list):
   G[a,b]=2*np.einsum('ij,ij->',pol[a],pol[b])*cc(k,l,n)
 return G
Gs={m:Gram(m) for m in (0,)+masks}
assert np.max(np.abs(Gs[0]-np.eye(d)))<1e-12

rng=np.random.default_rng(20261024);best=(-1,None,None)
for _ in range(2000):
 u=rng.normal(size=d);u/=np.linalg.norm(u)
 R=np.array([Gs[m]@u for m in masks])
 U,S,Vt=np.linalg.svd(R,full_matrices=True)
 v=u-Vt[:5].T@(Vt[:5]@u)
 nrm=np.linalg.norm(v)
 if nrm>best[0]:best=(nrm,u,v/nrm)
closeness,u,v=best
assert closeness>.0025

coords=np.arange(N)-(N-1)//2
xx,yy,zz=np.meshgrid(coords,coords,coords,indexing='ij')
Tplus=np.zeros((N,N,N,3,3),float);Tminus=Tplus.copy()
for a,(k,B) in enumerate(zip(mode_list,pol)):
 ph=theta*(k[0]*xx+k[1]*yy+k[2]*zz)
 base=np.cos(ph)[...,None,None]*np.sqrt(2)*B
 Tplus+=(u[a]+v[a])*base
 Tminus+=(u[a]-v[a])*base

dx=2*np.pi/N
checks=[]
for mask in (0,)+masks:
 rp=float(dtc.rms_norm(Tplus,slice(mask,N-mask)))
 rm=float(dtc.rms_norm(Tminus,slice(mask,N-mask)))
 checks.append({'mask':mask,'rms_plus':rp,'rms_minus':rm,'abs_delta':abs(rp-rm)})
assert max(x['abs_delta'] for x in checks[1:])<3e-12
assert abs(checks[0]['rms_plus']-checks[0]['rms_minus'])>1e-4

# DIRECT user retained original source FFT TT operator, not just analytical TT test.
t0=time.time()
Pplus=dtc.apply_P_TT(Tplus,dx)
Pminus=dtc.apply_P_TT(Tminus,dx)
err_plus=float(np.linalg.norm((Pplus-Tplus).ravel())/np.linalg.norm(Tplus.ravel()))
err_minus=float(np.linalg.norm((Pminus-Tminus).ravel())/np.linalg.norm(Tminus.ravel()))
assert max(err_plus,err_minus)<5e-14

allcomps=np.array(mode_list,dtype=int)
assert np.max(abs(allcomps))==1
relative_gap=abs(checks[0]['rms_plus']-checks[0]['rms_minus'])/np.mean([checks[0]['rms_plus'],checks[0]['rms_minus']])
result={
'cell':'M13','return_id':'M13-ROT31-3D-TT-ONE-BAND-FIVE-MASK-NONMAP-001_20261024',
'source_sha256':sha,'N':N,'coordinate_bandwidth':1,'dimension_real_cos_TT':d,'masks':list(masks),
'numerical_construction':'fixed-seed 2000 random u, v orthogonal to five masked cross Gram rows via SVD',
'projection_distance':closeness,'mask_gram_max_abs_diff':max(x['abs_delta'] for x in checks[1:]),
'full_grid_relative_RMS_gap':relative_gap,'source_TT_relative_errors':[err_plus,err_minus],
'RMS':checks,'SVD_verification_sec':time.time()-t0,
'coefficients':{'u':u.tolist(),'v':v.tolist(),'wavevectors':[list(x) for x in mode_list],'polarizations':pol.tolist()},
'limitations':'EXACT_FOURIER_TT_SUBSPACE / SYNTHETIC_LOW_BAND_TENSORS / NOT_HISTORICAL_K / NO_PHYSICAL_CLAIM / NO_CANON / NO_EXEC_SIGN / TPE HOLD'}
( ROOT/'IW_M13_ROT31_lowband_TT_nonmap_20261024.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('26-mode full vs masked:',[(x['mask'],x['rms_plus'],x['rms_minus']) for x in checks])
print('relative full gap:',relative_gap)
print('original helper TT relative errors:',err_plus,err_minus)
print('PASS')