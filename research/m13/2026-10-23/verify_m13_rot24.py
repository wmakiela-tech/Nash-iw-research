#!/usr/bin/env python3
"""ROT24 -- tensor-level alpha^2-coefficient identification in the ROT23
functionally reconstructed DTC0a source family. No byte-identical runner claim.
Requires deepseek_python_20260627_a87249.py and frozen odd-N CSV.
"""
import sys, os, math, json, csv, hashlib, time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import importlib.util, contextlib, io
spec=importlib.util.spec_from_file_location('dtc_old24',ROOT/'deepseek_python_20260627_a87249.py')
old=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(old)

class VectorTT:
    def __init__(self,N,dx):
        k=np.stack(np.meshgrid(*([np.fft.fftfreq(N,d=dx)]*3),indexing='ij'),axis=-1)
        k2=np.einsum('...i,...i->...',k,k)
        self.zero=k2==0
        u=k/np.sqrt(np.where(self.zero,1,k2))[...,None]
        self.P=np.eye(3)-np.einsum('...i,...j->...ij',u,u)
    def apply(self,h,dx):
        H=np.fft.fftn(h,axes=(0,1,2))
        trP=np.einsum('...ij,...ij->...',self.P,H)
        Z=np.einsum('...ia,...ab,...jb->...ij',self.P,H,self.P)-.5*self.P*trP[...,None,None]
        trH=np.trace(H,axis1=-2,axis2=-1)
        Z[self.zero]=H[self.zero]-np.eye(3)*trH[self.zero][...,None,None]/3
        z=np.fft.ifftn(Z,axes=(0,1,2)).real
        return .5*(z+z.swapaxes(-1,-2))

def dot(x,y):return float(np.sum(x*y,dtype=np.float64))
def norm(x):return math.sqrt(max(0,dot(x,x)))
def mask(x,N,k=3):return x[k:N-k,k:N-k,k:N-k,:,:]
def rms(x,N,k=3):return norm(mask(x,N,k))/math.sqrt(6*(N-2*k)**3)
def rdot(x,y,N,k=3):return dot(mask(x,N,k),mask(y,N,k))/(6*(N-2*k)**3)

hist={(int(r['N']),float(r['alpha'])):r for r in csv.DictReader((ROOT/'dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv').open())}
ALPHAS=(0.,.05,.2)
START=time.time();all_results=[]
for N in (31,33,35,37,39,41):
    dx=2*math.pi/N; c1,c2,h=old.generate_smooth_fields(N,2*math.pi);op=VectorTT(N,dx)
    original_tt=old.apply_P_TT
    tensors={}
    for alpha in ALPHAS:
        C=old.compute_K_C(c1,c2,h,'E_lin',dx,2,alpha)
        B=op.apply(C,dx)
        old.apply_P_TT=op.apply
        try:A=old.compute_K_A_out(c1,c2,h,'E_lin',dx,2,alpha)
        finally:old.apply_P_TT=original_tt
        tensors[alpha]={'C':C,'B':B,'A':A}
        for ch in ('C','B','A'):
            actual=rms(tensors[alpha][ch],N)
            ref=float(hist[(N,alpha)]['K_'+ch+'_RMS'])
            assert abs(actual/ref-1)<5e-12,(N,alpha,ch,actual,ref)
    entries=[]
    for ch in ('C','B','A'):
        u=tensors[0.][ch];a=tensors[.05][ch];b=tensors[.2][ch]
        slope_a=(a-u)/.05; slope_b=(b-u)/.2
        w=(slope_b-slope_a)/.15
        v=slope_a-.05*w
        nu,nv,nw=(rms(x,N) for x in (u,v,w))
        # original norm at 0.2, contributions relative to initial norm
        alpha=.2;uc=u;vc=alpha*v;wc=alpha*alpha*w
        final=u+vc+wc
        refb=rms(b,N)
        interp_error=rms(final-b,N)/(refb if refb else 1)
        # Cross-terms in squared norm at alpha=.2 (negative cancellations visible)
        pieces={
            'U2':rdot(uc,uc,N),'aV2':rdot(vc,vc,N),'a2W2':rdot(wc,wc,N),
            '2UV':2*rdot(uc,vc,N),'2UW':2*rdot(uc,wc,N),'2VW':2*rdot(vc,wc,N)}
        ratio={name:value/(refb**2) for name,value in pieces.items()}
        assert abs(sum(ratio.values())-1)<2e-10,(N,ch,ratio)
        entry={'channel':ch,'u_rms':nu,'v_coefficient_rms':nv,'w_coefficient_rms':nw,
          'U_V_cos':rdot(u,v,N)/(nu*nv) if nu*nv else None,
          'U_W_cos':rdot(u,w,N)/(nu*nw) if nu*nw else None,
          'V_W_cos':rdot(v,w,N)/(nv*nw) if nv*nw else None,
          'alpha02_V_over_U':rms(vc,N)/nu,
          'alpha02_W_over_U':rms(wc,N)/nu,
          'alpha02_W_over_final':rms(wc,N)/refb,
          'alpha02_sqnorm_contributions_relative_to_final':ratio,
          'interp_relative_error':interp_error,
          'alpha02_frozen_expected_rms':refb,
          'midpoint_alpha01_rms_from_interpolated_tensors':rms(u+.1*v+.01*w,N),
          'alpha015_rms_from_interpolated_tensors':rms(u+.15*v+.0225*w,N)}
        # test quartic difference with five interpolated tensor norms, stable vs leading coefficient
        delta=.05
        g=[rms(u+(k*delta)*v+(k*delta)**2*w,N)**2 for k in range(5)]
        fd=g[4]-4*g[3]+6*g[2]-4*g[1]+g[0]
        analytic=24*delta**4*nw**2
        entry['quartic_fifth_norm_interpolated_from_coefficients']={'finite_difference':fd,'theorem_value':analytic,'relative_error':fd/analytic-1 if analytic else None}
        # Alternative coefficient from α=0,.05,.2 and cross-evaluation (true direct only N31,41 below)
        entry['W_masked_nonzero']=bool(nw>1e-13)
        entries.append(entry)
    # source-level polynomial vs direct test at unseen alpha=.1, tests 2 N values and all 3 K channels
    holdouts=[]
    if N in (31,41):
        for alpha in (.1,.15):
            C=old.compute_K_C(c1,c2,h,'E_lin',dx,2,alpha)
            B=op.apply(C,dx)
            old.apply_P_TT=op.apply
            try:A=old.compute_K_A_out(c1,c2,h,'E_lin',dx,2,alpha)
            finally:old.apply_P_TT=original_tt
            for ch,actual in [('C',C),('B',B),('A',A)]:
                u=tensors[0.][ch];a=tensors[.05][ch];b=tensors[.2][ch]
                W=((b-u)/.2-(a-u)/.05)/.15
                V=(a-u)/.05-.05*W
                estimate=u+alpha*V+alpha**2*W
                e=rms(actual-estimate,N)/rms(actual,N)
                holdouts.append({'alpha':alpha,'channel':ch,'relative_tensor_error':e})
                assert e < 2e-10,(N,ch,alpha,e)
    all_results.append({'N':N,'entries':entries,'holdouts':holdouts})
    print('PASS',N,'W_A/U_A',entries[2]['alpha02_W_over_U'],'W_B/U_B',entries[1]['alpha02_W_over_U'], 'elapsed',round(time.time()-START,1),flush=True)

out={'return_id':'M13-ROT24-DTC0A-ALPHA2-TENSOR-COEFFICIENT-IDENTIFIED-FUNCTIONAL-REPLAY-001_20261023','sources':{'matching_helper':'deepseek_python_20260627_a87249.py','sha256':hashlib.sha256((ROOT/'deepseek_python_20260627_a87249.py').read_bytes()).hexdigest(),'historical_runner_byte_exact':False,'reference_csv':'dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv','historical_runner_declared_sha256':'2a35d357a6b19ce900917e31c8b4277235003c1f6298d95cb4f13dec0a392084'},'per_grid':all_results,'n_original_rms_matched':54,'n_unseen_alpha_tensor_holdouts':sum(len(x['holdouts']) for x in all_results),'duration_seconds':time.time()-START,'negative_knowledge':'U,V,W reconstructed under helper semantics, not unique from old CSV norms alone; no byte-exact runner or physical interpretation'}
path=ROOT/'IW_M13_ROT24_alpha_tensor_coefficients_20261023.json'
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('SUMMARY',json.dumps({'secs':round(time.time()-START,1),'max_holdout':max([z['relative_tensor_error'] for x in all_results for z in x['holdouts']]),'max_quartic_rel_err':max(abs(x['quartic_fifth_norm_interpolated_from_coefficients']['relative_error']) for d in all_results for x in d['entries']), 'w_ratio_A':[x['entries'][2]['alpha02_W_over_U'] for x in all_results]},indent=2))

# Source-native analytic W coefficient control (not interpolation):
# S = dx² Delta_h, L_i = Lie_Ci, P=Fourier TT.
# W_C=(L1 S L2 S - L2 S L1 S)h; W_A=(P L1 S P L2 S - P L2 S P L1 S)h.
def S(t):
    result=np.zeros_like(t)
    for axis in range(3):result+=np.roll(t,-1,axis=axis)-2*t+np.roll(t,1,axis=axis)
    return result
more=[]
for N in (31,41):
    dx=2*math.pi/N;c1,c2,h=old.generate_smooth_fields(N,2*math.pi);op=VectorTT(N,dx)
    L1=lambda t:old.lie_derivative_tensor(c1,t,dx,2)
    L2=lambda t:old.lie_derivative_tensor(c2,t,dx,2)
    Wc=L1(S(L2(S(h))))-L2(S(L1(S(h))))
    Wb=op.apply(Wc,dx)
    Wa=op.apply(L1(S(op.apply(L2(S(h)),dx)))-L2(S(op.apply(L1(S(h)),dx))),dx)
    actual={}
    five_norms={}
    for al in (0.,.05,.1,.15,.2):
        C=old.compute_K_C(c1,c2,h,'E_lin',dx,2,al)
        B=op.apply(C,dx)
        original=old.apply_P_TT;old.apply_P_TT=op.apply
        try:A=old.compute_K_A_out(c1,c2,h,'E_lin',dx,2,al)
        finally:old.apply_P_TT=original
        actual[al]={'C':C,'B':B,'A':A}
    for ch,W_explicit in [('C',Wc),('B',Wb),('A',Wa)]:
        u=actual[0.][ch]
        aa=actual[.05][ch]
        bb=actual[.2][ch]
        W_interp=(((bb-u)/.2)-((aa-u)/.05))/.15
        normw=rms(W_explicit,N)
        relative=rms(W_interp-W_explicit,N)/normw if normw else None
        assert relative <1e-7,(N,ch,relative)
        g=[rms(actual[round(k*.05,10)][ch],N)**2 for k in range(5)]
        fd=g[4]-4*g[3]+6*g[2]-4*g[1]+g[0]
        expected=24*.05**4*normw**2
        five_norms[ch]={'W_explicit_rms':normw,'W_interpolated_vs_analytic_relative_error':relative,'direct_five_alpha_fourth_difference':fd,'exact_polynomial_prediction':expected,'direct_diff_rel_error':fd/expected-1,'five_norm_squared':g}
        print('ANALYTIC_W',N,ch,'rel',relative,'delta4 direct rel',fd/expected-1,flush=True)
    # Check pure-trace ambient target observed independently by XH-S4; not claimed new.
    ph=op.apply(h,dx)
    more.append({'N':N,'W_direct_validations':five_norms,'initial_TT_input_ratio':rms(ph,N)/rms(h,N)})
out['direct_source_W_and_real_five_alpha'] = more
out['duration_seconds']=time.time()-START
path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('ANALYTIC_ALL_PASS',round(time.time()-START,1))