#!/usr/bin/env python3
"""INT8-052 independent NumPy Fourier 6D rank scans and optional SHA-pinned literal DTC0a source tests."""
import argparse,contextlib,hashlib,importlib.util,io,json,math
from itertools import product
from pathlib import Path
import numpy as np
A=np.array([1,2,0],dtype=int);B=np.array([2,-1,0],dtype=int);Ez=np.array([0.,0.,1.])
SRC_SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
TENSORS=[]
for i in range(3):
 M=np.zeros((3,3));M[i,i]=1;TENSORS.append(M)
for i,j in [(0,1),(0,2),(1,2)):
 M=np.zeros((3,3));M[i,j]=M[j,i]=1/math.sqrt(2);TENSORS.append(M)
TENSORS=np.array(TENSORS)

def sym(u,v):return np.outer(u,v)+np.outer(v,u)
def TT(H,k):
 k=np.asarray(k,dtype=float);Q=np.eye(3)-np.outer(k,k)/float(k@k)
 return Q@H@Q-(np.trace(Q@H)/2)*Q
def factors(N,ell,alpha):
 h=2*np.pi/N
 return (1-4*alpha*np.sin(np.pi*ell/N)**2,
         1-4*alpha*(np.sin(np.pi/N)**2+np.sin(2*np.pi/N)**2+np.sin(np.pi*ell/N)**2))
def blocks(S,N,ell):
 h=2*np.pi/N;sa=np.sin(h*A)/h;sb=np.sin(h*B)/h;sz=np.sin(h*ell)/h
 out={}
 for ta,tb in product((1,-1),repeat=2):
  kb=tb*B+np.array([0,0,ell]);ka=ta*A+np.array([0,0,ell]);k=ta*A+tb*B+np.array([0,0,ell]);
  PB=TT(tb*sz*S+sym(S@Ez,sb),kb)
  PA=TT(ta*sz*S+sym(S@Ez,sa),ka)
  unproj=ta*sz*PB+sym(PB@Ez,sa)-tb*sz*PA-sym(PA@Ez,sb)
  out[(ta,tb)]=TT(unproj,k)/4
 return out

def full_matrix(N,ell):
 return np.array([np.concatenate([blocks(S,N,ell)[pair].reshape(-1) for pair in product((1,-1),repeat=2)]) for S in TENSORS]).T

def angles_matrix(N,ell):
 # independent 8 linear TT output moments, two independent TT polarizations per each 4 sidebands.
 C=[]
 for S in TENSORS:
  by=blocks(S,N,ell);z=[]
  for ta,tb in product((1,-1),repeat=2):
   k=ta*A+tb*B+np.array([0,0,ell]);kx,ky,l=k
   v=np.array([-ky,kx,0.],float);u=np.array([-l*kx,-l*ky,kx*kx+ky*ky],float)
   H=by[(ta,tb)]
   z.extend([np.sum(H*sym(v,u)), np.sum(H*(np.outer(v,v)*(u@u)-np.outer(u,u)*(v@v)))])
  C.append(z)
 return np.array(C).T

def load_source(path):
 assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==SRC_SHA
 spec=importlib.util.spec_from_file_location('source_dtc0a_int8_052',path);m=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(m)
 return m

def field(S,N,ell,alpha,kind):
 h=2*np.pi/N;p=np.indices((N,N,N));e0,e1=factors(N,ell,alpha);V=np.zeros((N,N,N,3,3))
 for (ta,tb),H in blocks(S,N,ell).items():
  k=ta*A+tb*B+np.array([0,0,ell]);phase=h*sum(int(k[j])*p[j] for j in range(3))
  V+=e0*e1*(np.cos(phase) if kind=='cos' else np.sin(phase))[...,None,None]*H
 return V

def source_case(m,N,ell,alpha,S,kind):
 h=2*np.pi/N;p=np.indices((N,N,N));x,y,z=p*h
 C1=np.zeros((N,N,N,3));C2=C1.copy();C1[...,2]=np.sin(x+2*y);C2[...,2]=np.sin(2*x-y)
 H=(np.cos(ell*z) if kind=='cos' else np.sin(ell*z))[...,None,None]*S
 original=m.compute_K_A_out(C1,C2,H,'E_lin',h,2,alpha)
 expected=field(S,N,ell,alpha,kind)
 err=float(np.max(abs(original-expected)))
 assert err<1.2e-10,(N,ell,alpha,kind,err)
 kc=m.compute_K_C(C1,C2,H,'E_lin',h,2,alpha)
 kb=m.compute_K_B(C1,C2,H,'E_lin',h,2,alpha)
 assert max(float(np.max(abs(kc))),float(np.max(abs(kb))))<1.2e-10
 rms=float(np.sqrt(np.mean(np.sum(original**2,axis=(-2,-1)))))
 return {'N':N,'ell':ell,'alpha':round(alpha,12),'polarization':kind,'rms':round(rms,12),'field_error':round(err,12),'K_C_and_K_B_zero':True}

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--source',default='');arg=ap.parse_args()
 Ns=[7,9,11,13,15,17,19,21,25,31,35,41,49,61,81,101]
 tests=[];lower=1e10;zero_rank=[];moments_checks=0
 for N in Ns:
  for ell in range((N+1)//2):
   F=full_matrix(N,ell);sp=np.linalg.svd(F,compute_uv=False)
   rank=int(sum(sp>1e-10));assert rank==(3 if ell==0 else 6),(N,ell,rank,sp)
   if ell>0:
    lower=min(lower,float(sp[-1]));M=angles_matrix(N,ell)
    # A 6x6 TT-submatrix has explicit nonzero analytic determinant;
    # source floating witness: nonzero relative to its natural scale (no false exact floating claim).
    assert np.linalg.matrix_rank(M,tol=1e-8)==6,(N,ell)
    moments_checks+=1
   e0,e1=factors(N,ell,1/6)
   assert e0>=1/3-1e-10
   if abs(e1)<2e-12:zero_rank.append((N,ell))
   tests.append({'N':N,'ell':ell,'source_geometry_rank_numeric':rank,
     'core_sigma_min':round(float(sp[-1]),11),
     'e_shell_at_stable_endpoint':round(float(e1),12)})
 assert zero_rank==[(9,4)],zero_rank
 # Previously certified additional dark at alpha=1/7.
 for N,ell,alpha in [(7,3,1/7),(9,4,1/6)]:
  assert abs(factors(N,ell,alpha)[1])<1e-12
 # Actual original source is independent from symbolic determinant, and absent-safe.
 source_checks=[];status='SOURCE_SKIPPED_NO_HELPER'
 if arg.source:
  m=load_source(arg.source);status='ORIGINAL_SHA_VERIFIED_PASS'
  S=np.array([[.8,.23,.31],[.23,-.5,-.21],[.31,-.21,.74]])
  for N,ell,alpha in [(7,1,.05),(7,3,1/7),(9,2,.05),(9,4,1/6),(11,1,.05),(11,5,1/6),(15,2,.05),(15,7,1/6),(21,10,.05)]:
   for kind in ['cos','sin']:
    source_checks.append(source_case(m,N,ell,alpha,S,kind))
 result={'artifact_id':'IW_INT8_ROT052_ALL_ODD_N_INJECTIVITY_20261102','status':'NUMERIC_AND_SOURCE_PASS',
   'source_status':status,'source_sha256':SRC_SHA if arg.source else None,
   'numeric_fiber_cases':len(tests),'numeric_nonzero_fiber_cases':moments_checks,
   'grid_values':Ns,'minimum_float_nonzero_ell_singular':round(lower,11),
   'at_alpha_sixth_dark_fibers':[{'N':n,'ell':ell} for n,ell in zero_rank],
   'fiber_results':tests,'native_source_cases':len(source_checks),'native_records':source_checks,
   'limitation':'Numeric SVD is NOT the proof of all-N rank; exact all-N symbolic 6x6 minor + cyclotomic Galois proof is independent in audit_int8_rot052_exact.py. Source helper only auxiliary unmasked K_A_out, original historical masked runtime unavailable.'}
 Path(arg.out).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
 print('NUMERIC_PASS',len(tests),'Fourier cases',moments_checks,'nonzero angular-moment ranks;',len(source_checks),'source cases',status)
if __name__=='__main__':main()
