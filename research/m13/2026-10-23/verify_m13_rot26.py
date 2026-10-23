#!/usr/bin/env python3
"""M13 ROT26. Independent *sparse Fourier dictionary* formulation of the
DTC0a source-matched generators. No historical runtime loaded, no grid
finite differences or FFT for operator evaluation. FFT only verifies spatial
RMS from Fourier coefficient arrays. Not physical, not production code.
"""
import numpy as np, math, csv, json, hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
ZERO=(0,0,0)

def add(a,b,sa=1,sb=1):
 out={}
 for m,v in a.items():out[m]=sa*v.copy()
 for m,v in b.items():out[m]=out.get(m,np.zeros_like(v))+sb*v
 return {m:v for m,v in out.items() if np.any(v!=0)}

def convolve(a,b,fun,sign=1):
 out={}
 for p,u in a.items():
  for q,v in b.items():
   m=tuple(p[i]+q[i] for i in range(3));val=sign*fun(p,q,u,v)
   if m in out:out[m]+=val
   else:out[m]=val.copy()
 return out

def deriv_multiplier(m,axis,N=None):
 if N is None:return 1j*m[axis]
 return 1j*math.sin(m[axis]*2*math.pi/N)/(2*math.pi/N)

def efactor(m,alpha,N=None):
 if N is None:return 1.
 dx=2*math.pi/N
 return 1+2*alpha*sum(math.cos(v*dx)-1 for v in m)

def filter_E(h,alpha,N):return {m:v*efactor(m,alpha,N) for m,v in h.items()}

def lie(C,H,N=None):
 out={}
 def acc(m,v):
  if m in out:out[m]+=v
  else:out[m]=v.copy()
 for p,c in C.items():
  for q,h in H.items():
   m=tuple(p[i]+q[i] for i in range(3))
   adv=sum(c[k]*deriv_multiplier(q,k,N) for k in range(3))*h
   stretch=np.zeros((3,3),complex)
   for i in range(3):
    for j in range(3):
     for k in range(3):
      stretch[i,j]+=h[k,j]*deriv_multiplier(p,i,N)*c[k]+h[i,k]*deriv_multiplier(p,j,N)*c[k]
   acc(m,adv+stretch)
 return out

def bracket(C1,C2,N=None):
 out={}
 for p,c in C1.items():
  for q,d in C2.items():
   m=tuple(p[i]+q[i] for i in range(3))
   v=np.array([sum(c[k]*deriv_multiplier(q,k,N)*d[i]-d[k]*deriv_multiplier(p,k,N)*c[i] for k in range(3)) for i in range(3)],complex)
   if m in out:out[m]+=v
   else:out[m]=v.copy()
 return out

def proj(H):
 out={}
 for q,h in H.items():
  if q==ZERO: z=h-np.eye(3)*np.trace(h)/3
  else:
   k=np.array(q,float); pk=np.eye(3)-np.outer(k,k)/np.dot(k,k)
   z=pk@h@pk-.5*pk*np.einsum('ij,ij->',pk,h)
  out[q]=(z+z.T)/2
 return out

def source():
 C1={};C2={};H={}
 for s in (-1,1):
  q=(s,0,0)
  a=np.zeros(3,complex);a[0]=-.025j*s;C1[q]=a
  b=np.zeros(3,complex);b[2]=-.02j*s;C2[q]=b
  q=(0,s,0)
  a=np.zeros(3,complex);a[1]=.025;C1[q]=a
  q=(0,0,s)
  b=np.zeros(3,complex);b[0]=.02;C2[q]=b
  for t in (-1,1):H[(s,t,0)]=(-.025j*s)*np.eye(3)
 return C1,C2,H

def calc(N,alpha):
 C1,C2,h=source();b=bracket(C1,C2,N)
 def L(C,H):return lie(C,filter_E(H,alpha,N),N)
 C=add(add(L(C1,L(C2,h)),L(C2,L(C1,h)),sb=-1),L(b,h),sb=-1)
 B=proj(C)
 A=add(add(proj(L(C1,proj(L(C2,h)))),proj(L(C2,proj(L(C1,h)))),sb=-1),proj(L(b,h)),sb=-1)
 D=add(A,B,sb=-1)
 return A,B,C,D

def frobmode_energy(coeffs):return {k:float(np.sum(np.abs(v)**2)) for k,v in coeffs.items()}

def global_rms(z):return math.sqrt(sum(frobmode_energy(z).values())/6)

def grid(z,N):
 F=np.zeros((N,N,N,3,3),complex)
 for m,v in z.items():F[tuple(x%N for x in m)]+=v*N**3
 y=np.fft.ifftn(F,axes=(0,1,2))
 assert np.max(abs(y.imag)) < 1e-12,('imag',N,np.max(abs(y.imag)))
 return y.real

def mask_rms(z,N,k=3):
 H=grid(z,N)[k:N-k,k:N-k,k:N-k]
 return math.sqrt(float(np.mean(np.sum(H*H,axis=(-2,-1)))/6))

def info(z,N,k=3):
 E=frobmode_energy(z);tot=sum(E.values()); relative={m:val/tot for m,val in E.items()}
 active=sorted([m for m,p in relative.items() if p>1e-12]);bad=sum(v for m,v in relative.items() if m not in active)
 family_four=sum(v for m,v in relative.items() if m[0]==0 and abs(m[1])==1 and abs(m[2])==1)
 return {'global_RMS':global_rms(z),'masked_RMS':mask_rms(z,N,k),'masked_to_global':mask_rms(z,N,k)/global_rms(z),
 'support_count':len(active),'support_box':[max(abs(x[i]) for x in active) for i in range(3)],
 'fraction_energy_on_four_0pm1pm1_modes':family_four,'outside_active_energy_share':bad,
 'top_modes':[{'mode':list(m),'energy_fraction':p} for m,p in sorted(relative.items(),key=lambda x:-x[1])[:8]],
 'zero_mode_energy_fraction':relative.get(ZERO,0)}

def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()

def main():
 rows=list(csv.DictReader((ROOT/'dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv').open()))
 dat={(int(r['N']),float(r['alpha'])):r for r in rows}
 result=[]; maxrel=0; maxoutside=0
 for N in (31,33,35,37,39,41):
  for alpha in (0.,.05,.2):
   A,B,C,D=calc(N,alpha)
   for coeff in (A,B,C,D):
    support=[x for x,e in frobmode_energy(coeff).items() if e>1e-22]
    assert all(abs(x[0])<=3 and abs(x[1])<=2 and abs(x[2])<=1 for x in support)
   metrics={k:info(z,N) for k,z in [('A',A),('B',B),('C',C),('D',D)]}
   eps=max(abs(metrics[k]['masked_RMS']/float(dat[N,alpha]['K_'+k+'_RMS'])-1) for k in ('A','B','C'))
   assert eps<2e-11,(N,alpha,eps)
   maxrel=max(maxrel,eps)
   result.append({'N':N,'alpha':alpha,'hist_maxrel_error':eps,**metrics})
   print('PASS',N,alpha,'error',eps,'support A',metrics['A']['support_count'],'four_A',round(metrics['A']['fraction_energy_on_four_0pm1pm1_modes'],7),'A glob',metrics['A']['global_RMS'],flush=True)
 # Cross-code check independent grid generator on one case
 import importlib.util,contextlib,io
 spec=importlib.util.spec_from_file_location('old26',ROOT/'deepseek_python_20260627_a87249.py');old=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(old)
 N=31; alpha=.05; dx=2*math.pi/N;c1,c2,h=old.generate_smooth_fields(N,2*math.pi)
 oldA=old.compute_K_A_out(c1,c2,h,'E_lin',dx,2,alpha)
 newA=grid(calc(N,alpha)[0],N)
 sample_rel=float(np.linalg.norm(oldA-newA)/np.linalg.norm(oldA))
 assert sample_rel<2e-11,sample_rel
 # Exact alpha-independent continuum limit: all central difference Fourier multipliers -> ik,
 # and alpha*dx^2Delta -> 0 for fixed finite harmonics as N -> infinity.
 Ac,Bc,Cc,Dc=calc(None,0.); lim={k:global_rms(z) for k,z in [('A',Ac),('B',Bc),('C',Cc),('D',Dc)]}
 assert lim['A']>0 and lim['B']<1e-12 and lim['C']<1e-12
 lim_A_spectrum=frobmode_energy(Ac);E_tot=sum(lim_A_spectrum.values())
 lim_four=sum(v for m,v in lim_A_spectrum.items() if m[0]==0 and abs(m[1])==1 and abs(m[2])==1)/E_tot
 # Verify continuum numerical consistency independent small-lattice analytic limit
 for N in (101,1001):
  pred=global_rms(calc(N,.2)[0]);print('LARGE-N exact sparse',N,pred,'limit',lim['A'],'relative',pred/lim['A']-1)
 summary={'return_id':'M13-ROT26-SPARSE-FOURIER-SOURCE-FAMILY-REPLAY-AND-CONTINUUM-LIMIT-001_20261023',
 'data_source_sha256':sha('dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv'),
 'historical_source_matching_helper_sha256':sha('deepseek_python_20260627_a87249.py'),
 'historical_runtime_exact_byte_available':False,
 'historical_runtime_expected_sha256':'2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084',
 'operator_calculation':'independent sparse Fourier mode convolutions; no numpy grids/FFT for operator, FFT synthesis only for historical mask RMS',
 'rows':result,'n_cases':len(result),'n_historical_scalar_norms_compared':len(result)*3,
 'max_historical_relative_error':maxrel,'direct_native_source_3D_tensor_rel_error_N31_alpha005':sample_rel,
 'limit_alpha_independent_source_family':lim,'limit_KA_four_mode_energy_fraction':lim_four,
 'support_range_A':[min(x['A']['support_count'] for x in result),max(x['A']['support_count'] for x in result)],
 'support_range_B':[min(x['B']['support_count'] for x in result),max(x['B']['support_count'] for x in result)],
 'certified_source_monomial_band_box':[3,2,1],
 'status':'EXACT_FINITE_MODE_HOST / SOURCE_MATCHED_54/54 / FIXED_P_AMBIENT_PURE_TRACE / NO_PHYSICAL_UPGRADE'}
 p=ROOT/'IW_M13_ROT26_sparse_fourier_spectrum_20261023.json';p.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
 print('SUMMARY',json.dumps({k:summary[k] for k in ('n_cases','n_historical_scalar_norms_compared','max_historical_relative_error','direct_native_source_3D_tensor_rel_error_N31_alpha005','limit_alpha_independent_source_family','limit_KA_four_mode_energy_fraction','support_range_A','support_range_B')},indent=2))
if __name__=='__main__':main()