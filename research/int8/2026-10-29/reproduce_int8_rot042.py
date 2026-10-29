#!/usr/bin/env python3
"""INT8-042 numerical finite Fourier audit, independent two-dimensional Gram spectrum, optional native DTC0a helper."""
import argparse,hashlib,importlib.util,json,math,contextlib,io
from pathlib import Path
from itertools import product
import numpy as np
SHA='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
A_CASES={
 'xy_shear':np.array([[1,1,0],[0,1,0],[0,0,1]],int),
 'long_middle':np.array([[1,0,-1],[0,1,2],[0,0,1]],int),
 'irreducible_mix':np.array([[1,1,0],[0,1,1],[0,0,1]],int),
}
B=[]
for i in range(3):
 M=np.zeros((3,3));M[i,i]=1;B.append(M)
for i,j in [(0,1),(0,2),(1,2)]:
 M=np.zeros((3,3));M[i,j]=M[j,i]=1/math.sqrt(2);B.append(M)
B=np.array(B)
def coords(H):return np.einsum('aij,ij->a',B,H)
def tensor(x):return np.einsum('a,aij->ij',x,B)
def rep(A):return np.array([[np.sum(bi*(A.T@bj@A)) for bj in B] for bi in B])
def TT(k):
 k=np.array(k,float);n=float(k@k)
 if n<.5:raise ValueError('nonzero mode required')
 Q=np.eye(3)-np.outer(k,k)/n
 return np.array([[np.sum(bi*(Q@bj@Q-np.trace(Q@bj)*Q/2)) for bj in B] for bi in B])
def fiber_gram_norm(k,D,Di):
 k=np.array(k,float);k/=np.linalg.norm(k)
 u=np.eye(3)[int(np.argmin(np.abs(k)))];u-=k*(k@u);u/=np.linalg.norm(u)
 v=np.cross(k,u);v/=np.linalg.norm(v)
 X=(np.outer(u,u)-np.outer(v,v))/math.sqrt(2)
 Y=(np.outer(u,v)+np.outer(v,u))/math.sqrt(2)
 H=[X,Y]
 S=np.array([[np.trace(a@D@b@D) for b in H] for a in H])
 T=np.array([[np.trace(a@Di@b@Di) for b in H] for a in H])
 M=S@T
 val=max(0.,(float(np.trace(M))+math.sqrt(max(0.,float(np.trace(M))**2-4*float(np.linalg.det(M)))))/2)
 return math.sqrt(val)
def r9(x):return float(round(float(x),9))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);ap.add_argument('--source',default='');args=ap.parse_args()
 records=[];total=0;worst_cross=0;native={'status':'SOURCE_SKIPPED_NO_HELPER','cases':0};max_violation=0
 for name,A in A_CASES.items():
  assert round(np.linalg.det(A))==1
  D=A@A.T;Di=np.linalg.inv(D);ev,V=np.linalg.eigh(D)
  W=((ev[-1]/ev[0])+(ev[0]/ev[-1]))/2
  mid=V[:,1];root_1=bool(abs(np.linalg.det(D-np.eye(3)))<1e-9)
  g=A.T@A;Q0=np.linalg.norm(g,'fro')*np.linalg.norm(np.linalg.inv(g),'fro')/3
  for N in [3,5,7,9,15,21,31]:
   m=(N-1)//2;best=0.;arg=[0,0,0]
   for k in product(range(-m,m+1),repeat=3):
    if k==(0,0,0) or next((v for v in k if v!=0),1)<0:continue
    y=fiber_gram_norm(k,D,Di);total+=1
    if y>W+2e-8:max_violation+=1
    if y>best+1e-12:best=y;arg=list(k)
   gap=max(0,W-best)
   # Independent full 6x6 Frobenius source-TT congruence at the maximizing input.
   C=rep(A);Ci=rep(np.linalg.inv(A));actual=np.linalg.svd(C@TT(arg)@Ci,compute_uv=False)[0]
   worst_cross=max(worst_cross,abs(actual-best))
   assert abs(actual-best)<1e-8,(name,N,'gram-vs-6d',best,actual)
   if name=='xy_shear':assert gap<1e-8
   if name=='long_middle':assert (gap>1e-4 if N==3 else gap<1e-7),(name,N,gap)
   if name=='irreducible_mix':assert gap>1e-6,(name,N,gap)
   records.append({'A_case':name,'A':A.tolist(),'N':N,'modes_half_grid':(N**3-1)//2,'Wielandt_universal_bound':r9(W),'max_nonzero_TT_norm':r9(best),'full_including_k0':r9(max(best,Q0)),'zero_mode_Qg':r9(Q0),'strict_gap':r9(gap),'maximizer_q':arg,'middle_eigenvector_root1':root_1,'attained':bool(gap<1e-7)})
 assert max_violation==0
 if args.source and Path(args.source).exists():
  source=Path(args.source);assert hashlib.sha256(source.read_bytes()).hexdigest()==SHA
  spec=importlib.util.spec_from_file_location('source042',source);mod=importlib.util.module_from_spec(spec)
  with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(mod)
  tests=[]
  for name,N in [('xy_shear',3),('long_middle',3),('long_middle',5),('irreducible_mix',3),('irreducible_mix',5),('irreducible_mix',7)]:
   A=A_CASES[name];C=rep(A);Ci=rep(np.linalg.inv(A));found=next(r for r in records if r['A_case']==name and r['N']==N)
   k=np.array(found['maximizer_q'],int);F=C@TT(k)@Ci;U,s,Vt=np.linalg.svd(F);z=Vt[0]
   hsource=tensor(Ci@z);grid=np.indices((N,N,N));phase=sum(k[i]*grid[i] for i in range(3));wave=np.cos(2*np.pi*phase/N)
   srcfield=wave[...,None,None]*hsource
   assert srcfield.shape==(N,N,N,3,3)
   with contextlib.redirect_stdout(io.StringIO()):out=mod.apply_P_TT(srcfield,dx=2*np.pi/N)
   idx=[sum(int(A[i,j])*grid[j] for j in range(3))%N for i in range(3)]
   out_g=np.einsum('ia,xyzab,bj->xyzij',A.T,out[tuple(idx)],A)
   target_q=A.T@k;target_wave=np.cos(2*np.pi*sum(int(target_q[i])*grid[i] for i in range(3))/N)
   want=target_wave[...,None,None]*tensor(F@z)
   rel=float(np.linalg.norm(out_g-want)/max(np.linalg.norm(want),1e-12))
   ratio=float(np.linalg.norm(out_g)/max(np.linalg.norm(target_wave[...,None,None]*tensor(z)),1e-12))
   assert rel<3e-10 and abs(ratio-s[0])<4e-10,(name,N,rel,ratio,s[0])
   tests.append({'case':name,'N':N,'relative_native_residual':r9(rel),'source_amplification':r9(ratio),'six_dimensional_singular':r9(s[0]),'input_mean_zero':True})
  native={'status':'SOURCE_SHA_VERIFIED_PASS','sha256':SHA,'cases':len(tests),'tests':tests}
 result={'artifact_id':'IW_INT8_ROT042_GENERAL_INTEGER_METRIC_TT_NORM_20261029','status':'PASS','total_half_grid_modes':total,'crosscheck_max_abs':r9(worst_cross),'bound_violations':max_violation,'records':records,'source':native,'boundaries':'Odd N, full 6D tensor space, fixed flat integral metrics, unchanged auxiliary TT; no historic K_A; no physical claim'}
 Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf8')
 print('PASS',len(records),'grid/matrix pairs;',total,'half-grid mode spectra; source',native['status'])
if __name__=='__main__':main()
