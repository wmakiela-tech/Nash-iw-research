#!/usr/bin/env python3
"""M13 ROT25. Exact insertion/leakage identity evaluated on 18 DTC0a
functionally recovered, historical-RMS-matching cases. Does NOT claim
byte-exact original runner or physical meaning. Requires frozen CSV and
matching source helper deepseek_python_20260627_a87249.py in same folder.
"""
from pathlib import Path
import numpy as np, csv, math, importlib.util, contextlib, io, json, hashlib, time
ROOT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('dtc_older25',ROOT/'deepseek_python_20260627_a87249.py')
old=importlib.util.module_from_spec(sp)
with contextlib.redirect_stdout(io.StringIO()):sp.loader.exec_module(old)

class VectorTT:
    def __init__(self,N,dx):
        k=np.stack(np.meshgrid(*([np.fft.fftfreq(N,d=dx)]*3),indexing='ij'),axis=-1)
        k2=np.einsum('...i,...i->...',k,k)
        self.zero=k2==0
        u=k/np.sqrt(np.where(self.zero,1,k2))[...,None]
        self.P=np.eye(3)-np.einsum('...i,...j->...ij',u,u)
    def apply(self,h,dx):
        H=np.fft.fftn(h,axes=(0,1,2));P=self.P
        trP=np.einsum('...ij,...ij->...',P,H)
        Z=np.einsum('...ia,...ab,...jb->...ij',P,H,P)-.5*P*trP[...,None,None]
        trH=np.trace(H,axis1=-2,axis2=-1)
        Z[self.zero]=H[self.zero]-np.eye(3)*trH[self.zero][...,None,None]/3
        z=np.fft.ifftn(Z,axes=(0,1,2)).real
        return .5*(z+z.swapaxes(-1,-2))

def norm(x,N,k=3):return math.sqrt(float(np.sum(x[k:N-k,k:N-k,k:N-k]**2))/(6*(N-2*k)**3))
def fullnorm(x):return math.sqrt(float(np.sum(x*x)))
def inner(x,y,N,k=3):return float(np.sum(x[k:N-k,k:N-k,k:N-k]*y[k:N-k,k:N-k,k:N-k]))/(6*(N-2*k)**3)
def cosine(x,y,N,k=3):
    a,b=norm(x,N,k),norm(y,N,k)
    return inner(x,y,N,k)/(a*b) if a*b>0 else None

def sha(f):return hashlib.sha256((ROOT/f).read_bytes()).hexdigest()
hist={(int(x['N']),float(x['alpha'])):x for x in csv.DictReader((ROOT/'dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv').open())}
start=time.time(); rows=[];max_source_error=0.;max_identity_error=0.;max_strain_error=0.
for N in (31,33,35,37,39,41):
    dx=2*math.pi/N; c1,c2,h=old.generate_smooth_fields(N,2*math.pi);Pobj=VectorTT(N,dx);P=lambda t:Pobj.apply(t,dx)
    ph=P(h);input_ptt_over_input=fullnorm(ph)/fullnorm(h)
    assert input_ptt_over_input<5e-13
    bracket=old.lie_bracket(c1,c2,dx,2)
    for alpha in (0.,.05,.2):
        E=lambda t:old.apply_E(t,'E_lin',dx,2,alpha)
        L1=lambda t:old.lie_derivative_tensor(c1,E(t),dx,2)
        L2=lambda t:old.lie_derivative_tensor(c2,E(t),dx,2)
        Lb=lambda t:old.lie_derivative_tensor(bracket,E(t),dx,2)
        ell1=L1(h);ell2=L2(h)
        f1=P(ell1);f2=P(ell2)
        q1=ell1-f1;q2=ell2-f2
        # Source-native commutator source, projected on ambient tensors.
        C=L1(ell2)-L2(ell1)-Lb(h)
        B=P(C)
        A=P(L1(f2)-L2(f1)-Lb(h))
        # Exact known host decomposition from XH-S4 018/019:
        d_plus=P(L2(q1));d_minus=-P(L1(q2));D=d_plus+d_minus
        # Trace -> TT first-stage: E(f I) = g I; advective scalar part annihilates under TT.
        g=E(h)[...,0,0]
        assert fullnorm(E(h)-g[...,None,None]*np.eye(3)) / fullnorm(E(h))<5e-13
        def source_strain(c):
            # For E(f I)=g I: Lie_C(Eh)=(C·Dg)I + g(D_i C_j+D_j C_i).
            # P kills the scalar advection term exactly on the full Fourier grid.
            grad=np.zeros((N,N,N,3,3))
            for i in range(3):
                for j in range(3):
                    grad[...,i,j]=old.derivative(c[...,j],axis=i,dx=dx,order=2)
            return g[...,None,None]*(grad+grad.swapaxes(-1,-2))
        strain1=P(source_strain(c1));strain2=P(source_strain(c2))
        first_stage_err=max(fullnorm(strain1-f1)/(fullnorm(f1)+1e-100),fullnorm(strain2-f2)/(fullnorm(f2)+1e-100))
        # Direct original helper computation of A is expensive for N31 only; operator implementation is exact source-identical.
        op_err=norm(A-B-D,N)/(norm(A,N)+1e-100)
        source_error=max(abs(norm(x,N)/float(hist[(N,alpha)]['K_'+ch+'_RMS'])-1) for x,ch in [(C,'C'),(B,'B'),(A,'A')])
        max_source_error=max(max_source_error,source_error);max_identity_error=max(max_identity_error,op_err);max_strain_error=max(max_strain_error,first_stage_err)
        assert source_error<1e-12,(N,alpha,source_error)
        assert op_err<1e-11,(N,alpha,op_err)
        assert first_stage_err<1e-11,(N,alpha,first_stage_err)
        direct_original_A_rel_error=None
        if N==31 and alpha==.05:
            native_A=old.compute_K_A_out(c1,c2,h,'E_lin',dx,2,alpha)
            direct_original_A_rel_error=fullnorm(native_A-A)/(fullnorm(native_A)+1e-100)
            assert direct_original_A_rel_error<5e-13
        nrA,nrB,nrD,nrp,nrm=map(lambda z:norm(z,N),(A,B,D,d_plus,d_minus))
        rows.append({'N':N,'alpha':alpha,'trace_TT_input_relative_global_norm':input_ptt_over_input,
          'K_A_RMS':nrA,'K_B_RMS':nrB,'K_C_RMS':norm(C,N),'direct_unmodified_native_A_tensor_rel_error':direct_original_A_rel_error,
          'D_insertion_RMS':nrD,'D_over_A':nrD/nrA,'B_over_A':nrB/nrA,
          'cos_A_B':cosine(A,B,N),'cos_B_D':cosine(B,D,N),
          'dplus_RMS':nrp,'dminus_RMS':nrm,
          'dplus_over_A':nrp/nrA,'dminus_over_A':nrm/nrA,
          'cos_dplus_dminus':cosine(d_plus,d_minus,N),
          'firststage_TT_C1_RMS':norm(f1,N),
          'firststage_TT_C2_RMS':norm(f2,N),
          'firststage_strain_reproduction_rel_error':first_stage_err,
          'exact_projector_insertion_identity_relative_error':op_err,
          'historical_3RMS_max_relative_error':source_error})
        print('PASS N',N,'alpha',alpha,'D/A',round(nrD/nrA,9),'B/A',round(nrB/nrA,9),'subterms',round(nrp/nrA,6),round(nrm/nrA,6),'elapsed_s',round(time.time()-start,1),flush=True)
        del C,B,A,D,d_plus,d_minus,ell1,ell2,q1,q2,f1,f2

summary={'return_id':'M13-ROT25-DTC0A-REPRODUCED-TRACE-TO-TT-INSERTION-QUANTIFICATION-001_20261023',
 'source_matching_helper_sha256':sha('deepseek_python_20260627_a87249.py'),
 'frozen_csv_sha256':sha('dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv'),
 'historical_runner_byte_exact_available':False,'historical_runner_declared_sha256':'2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084',
 'n_recovered_cases':len(rows),'n_historical_norms_matched':len(rows)*3,
 'max_historical_relative_error':max_source_error,'max_exact_identity_relative_error':max_identity_error,'max_trace_strain_identity_relative_error':max_strain_error,
 'ranges':{k:[min(z[k] for z in rows),max(z[k] for z in rows)] for k in ('D_over_A','B_over_A','cos_B_D','dplus_over_A','dminus_over_A','cos_dplus_dminus','trace_TT_input_relative_global_norm')},
 'rows':rows,
 'scope':'18 source-matching functional source helper cases; XH-S4 first derived insertion identity and trace-domain warning; not physical NCDG or novel mathematics',
 'elapsed_seconds':time.time()-start}
out=ROOT/'IW_M13_ROT25_trace_to_TT_insertion_summary_20261023.json';out.write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n')
print('SUMMARY',json.dumps({k:v for k,v in summary.items() if k in ['n_recovered_cases','max_historical_relative_error','max_exact_identity_relative_error','max_trace_strain_identity_relative_error','ranges','elapsed_seconds']},indent=2))