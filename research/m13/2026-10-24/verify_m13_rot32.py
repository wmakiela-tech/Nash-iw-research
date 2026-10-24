#!/usr/bin/env python3
"""M13 ROT32: source-model parameter identification, uniform Bernstein
coefficient sign audit, and A/B ratio fold. All scientific claims are
conditional on archived source-matching DTC0a helper definitions.

This program uses an independent sparse Fourier implementation (ROT26).
The expected byte-exact 2026 v0.3.1 production runtime is unavailable.
Bernstein sign checks are FLOAT computations, not directed interval proofs.
"""
from __future__ import annotations
from pathlib import Path
import math,csv,json,hashlib,sys
import numpy as np
from verify_m13_rot26 import calc, global_rms
from verify_m13_rot27 import masked_sq,window_mean_of_mode
ROOT=Path(__file__).resolve().parent
ZERO=np.zeros((3,3),complex)
ALPHA_HI=.2

def combine(coeff,weights):
    out={}
    for col,c in zip(coeff,weights):
        for mode,v in col.items():
            out[mode]=out.get(mode,ZERO.copy())+c*v
    return out

def decompose(N):
    x0=calc(N,0.);xp=calc(N,1.);xm=calc(N,-1.)
    out={}
    for ci,ch in enumerate('ABC'):
        u=x0[ci];v=combine([xp[ci],xm[ci]],[.5,-.5]);w=combine([xp[ci],xm[ci],u],[.5,.5,-1.]);out[ch]=[u,v,w]
    return out

def inner_mask(x,y,N,k):
    if k==0:
        return float(sum(np.vdot(y[m],x[m]).real for m in x.keys() & y.keys())/6.)
    ds=set(tuple(a[d]-b[d] for d in range(3)) for a in x for b in y)
    qset={v for m in ds for v in m};win={q:window_mean_of_mode(q,N,k) for q in qset}
    s=0j
    for m,a in x.items():
        for n,b in y.items():
            val=np.vdot(b,a)
            if abs(val)==0:continue
            for j in range(3):val*=win[m[j]-n[j]]
            s+=val
    assert abs(s.imag)<1e-11*max(abs(s.real),1e-20),(s,N,k)
    return float(s.real/6.)

def quartic(uvw,N,k):
    u,v,w=uvw
    return np.array([inner_mask(u,u,N,k),2*inner_mask(u,v,N,k),inner_mask(v,v,N,k)+2*inner_mask(u,w,N,k),2*inner_mask(v,w,N,k),inner_mask(w,w,N,k)])

def polyval(p,a):return float(np.polynomial.polynomial.polyval(a,p))
def polynomial_d(a,b):
    d1=np.polynomial.polynomial.polymul(np.polynomial.polynomial.polyder(a),b)
    d2=np.polynomial.polynomial.polymul(a,np.polynomial.polynomial.polyder(b))
    return np.polynomial.polynomial.polysub(d1,d2)

def bernstein(p,hi=ALPHA_HI):
    n=len(p)-1
    return np.array([sum(p[j]*hi**j*math.comb(i,j)/math.comb(n,j) for j in range(i+1)) for i in range(n+1)])

def root_bisect(fun,left,right,tol=1e-13):
    fa,fb=fun(left),fun(right)
    if abs(fa)<1e-18:return left
    if abs(fb)<1e-18:return right
    assert fa*fb<0,(left,right,fa,fb)
    for z in range(100):
        mid=(left+right)/2;fm=fun(mid)
        if right-left<tol:return mid
        if fm*fa>0:left=mid;fa=fm
        else:right=mid;fb=fm
    return (left+right)/2

def poly_ratio(G,pair,a):
    return math.sqrt(polyval(G[pair[0]],a)/polyval(G[pair[1]],a))

def log_deriv(G,pair,a):
    p,q=G[pair[0]],G[pair[1]]
    return .5*(polyval(np.polynomial.polynomial.polyder(p),a)/polyval(p,a)-polyval(np.polynomial.polynomial.polyder(q),a)/polyval(q,a))

def main():
    hist=list(csv.DictReader((ROOT/'dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv').open()))
    masks=list(csv.DictReader((ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open()))
    frozen={(int(r['N']),float(r['alpha'])):r for r in hist}
    frozen_mask={(float(r['alpha']),int(r['interior_k'])):r for r in masks}
    assert len(frozen)==18 and len(frozen_mask)==15
    cases=[];max_frozen_err=0.;max_mask_err=0.;max_alphaerr=0;min_bern=1e100;max_bern=-1e100
    worst_log_sensitivity=1e100; max_poly_direct_err=0.;abc_derivative_by_N={}
    for N in (31,33,35,37,39,41):
        src=decompose(N)
        for k in ((2,3,4,5,6) if N==41 else (3,)):
            G={ch:quartic(src[ch],N,k) for ch in 'ABC'}
            for a in (0.,.05,.2):
                reference=frozen[N,a] if k==3 else frozen_mask[a,k]
                for ch in 'ABC':
                    r=math.sqrt(polyval(G[ch],a));want=float(reference['K_'+ch+'_RMS'])
                    e=abs(r/want-1)
                    if k==3:max_frozen_err=max(max_frozen_err,e)
                    else:max_mask_err=max(max_mask_err,e)
                    assert e<1e-10,(N,k,a,ch,e)
            # Method: exact expression for derivative of squared ratio g_A/g_C,
            # then Bernstein polynomial coefficients on [0,0.2].
            dp=polynomial_d(G['A'],G['C'])
            B=bernstein(dp)
            scales=G['A'][0]*G['C'][0]
            vals=B/scales
            min_bern=min(min_bern,float(vals.min()));max_bern=max(max_bern,float(vals.max()))
            assert np.all(vals < -10),(N,k,vals)
            # second certificate: use Bernstein upper bounds on normalized g_A,g_C
            ba=bernstein(G['A']);bc=bernstein(G['C'])
            assert min(ba)>0 and min(bc)>0
            # For any alpha the denominator is <= (max ba)*(max bc),
            # and -numerator>= -max(B); hence dlnR/dalpha <= -C below.
            numeric_bernstein_lower_abs_log=-float(B.max())/(2*float(ba.max())*float(bc.max()))
            worst_log_sensitivity=min(worst_log_sensitivity,numeric_bernstein_lower_abs_log)
            assert numeric_bernstein_lower_abs_log>.1, (N,k,numeric_bernstein_lower_abs_log)
            direct_diff=[]
            for a in (0.03125,.113,.177):
                data=calc(N,a)
                for ch,ci in [('A',0),('B',1),('C',2)]:
                    actual=(masked_sq(data[ci],N,k))
                    predicted=polyval(G[ch],a)
                    e=abs(actual/predicted-1);max_poly_direct_err=max(max_poly_direct_err,e)
                    assert e<1e-9,(N,k,a,ch,e)
            # Invert from ratio A/C and independent scale s; tested on historic levels.
            recovered=[]
            for a in (0.,.05,.2):
                R=math.sqrt(float((frozen[N,a] if k==3 else frozen_mask[a,k])['K_A_RMS'])**2/float((frozen[N,a] if k==3 else frozen_mask[a,k])['K_C_RMS'])**2)
                # avoid endpoint numerical root instability by endpoint clamp
                R0=poly_ratio(G,'AC',0.);Rend=poly_ratio(G,'AC',.2)
                if R>=R0:ahat=0.
                elif R<=Rend:ahat=.2
                else:ahat=root_bisect(lambda x:poly_ratio(G,'AC',x)-R,0.,.2)
                max_alphaerr=max(max_alphaerr,abs(ahat-a))
                s_est=float((frozen[N,a] if k==3 else frozen_mask[a,k])['K_A_RMS'])/math.sqrt(polyval(G['A'],ahat))
                assert abs(ahat-a)<1e-9 and abs(s_est-1)<1e-9,(N,k,a,ahat,s_est)
                recovered.append({'alpha_true':a,'alpha_inferred':ahat,'scale_inferred':s_est})
            points={str(a):{'A_over_C':poly_ratio(G,'AC',a),'A_over_B':poly_ratio(G,'AB',a),'B_over_C':poly_ratio(G,'BC',a),'d_log_A_over_C':log_deriv(G,'AC',a)} for a in (0.,.05,.2)}
            # A/B fold: alpha near zero can be double-valued, though A/C remains injective.
            dAB=polynomial_d(G['A'],G['B'])
            # Derivative at alpha0 positive for many source masks, decreases soon.
            fold=None
            if polyval(dAB,0)>0 and polyval(dAB,.01)<0:
                peak=root_bisect(lambda x:polyval(dAB,x)/(G['A'][0]*G['B'][0]),0,.01)
                a0=poly_ratio(G,'AB',0.)
                second=root_bisect(lambda x:poly_ratio(G,'AB',x)-a0,peak,.01)
                fold={'turning_alpha':peak,'second_alpha_equal_to_alpha0_ratio':second,'R_AB_at_alpha0':a0,'R_AB_at_peak':poly_ratio(G,'AB',peak),'direct_second_ratio_rel_difference':poly_ratio(G,'AB',second)/a0-1}
            cases.append({'N':N,'mask_k':k,'G_quartic_squared_RMS':{ch:G[ch].tolist() for ch in 'ABC'},'bernstien_d_squared_A_over_C_normalized':[float(x) for x in vals],'bernstein_sign_max':float(vals.max()),'numeric_bernstein_lower_bound_abs_log_derivative':numeric_bernstein_lower_abs_log,'historical_alpha_scale_inversion':recovered,'points':points,'AB_fold':fold})
    assert len(cases)==10
    # Sensitivity: +/-0.5% independent multiplicative errors in A,C gives
    # worst relative ratio (1.005/.995); inverse error via deterministic bisection.
    sensitivity=[]
    for row in cases:
        N,k=row['N'],row['mask_k'];G={ch:np.array(v) for ch,v in row['G_quartic_squared_RMS'].items()}
        for true_alpha in (.05,.1,.15):
            base=poly_ratio(G,'AC',true_alpha)
            for sign in (-1,1):
                noisy=base*(1+sign*.005)/(1-sign*.005)
                if noisy>poly_ratio(G,'AC',0):guess=0
                elif noisy<poly_ratio(G,'AC',.2):guess=.2
                else:guess=root_bisect(lambda x:poly_ratio(G,'AC',x)-noisy,0,.2)
                sensitivity.append({'N':N,'k':k,'alpha_true':true_alpha,'noise_ratio_sign':sign,'alpha_inferred':guess,'absolute_error':abs(guess-true_alpha)})
    # A finite-N identifiability theorem need not be uniformly stable as N increases.
    # For parameters (u=ln s, alpha), Jacobian in absolute RMS units is
    # [[A, dA/dalpha],[C,dC/dalpha]]. Its smallest singular value decays
    # as N^-2 for fixed finite-mode source and fixed integer mask.
    largeN_condition=[]
    for N in (31,41,81,161,321):
        src=decompose(N)
        A=quartic(src['A'],N,3);C=quartic(src['C'],N,3);a=.05
        ra=math.sqrt(polyval(A,a));rc=math.sqrt(polyval(C,a))
        da=polyval(np.polynomial.polynomial.polyder(A),a)/(2*ra)
        dc=polyval(np.polynomial.polynomial.polyder(C),a)/(2*rc)
        J=np.array([[ra,da],[rc,dc]])
        sigma=np.linalg.svd(J,compute_uv=False)
        largeN_condition.append({'N':N,'alpha':a,'KA_RMS':ra,'KC_RMS':rc,'Jacobian_det':float(np.linalg.det(J)),'Jacobian_cond_2':float(sigma[0]/sigma[-1]),'cond_2_div_N2':float(sigma[0]/sigma[-1]/N**2),'singular_values':sigma.tolist()})
    assert all(z['Jacobian_det']>0 for z in largeN_condition)
    assert .5 < largeN_condition[-1]['cond_2_div_N2']/largeN_condition[-2]['cond_2_div_N2'] < 1.5
    # Independent direct native source check N31 alpha .05 for K_A and K_C,
    # omitted from default to keep verifier fast; ROT23 already established.
    assert max_alphaerr<1e-9
    print('NUMERIC_BERNSTEIN_SIGN_PASS',len(cases),'max_normalized_coeff',max_bern,'min',min_bern)
    print('POLYNOMIAL_DIRECT_CHECK',max_poly_direct_err)
    print('FROZEN HISTORICAL RMS k3 54/54 maxrel',max_frozen_err,'N41 extras 36/36 maxrel',max_mask_err)
    print('PARAMETER_RECOVERY 30/30 max_alpha_abs_err',max_alphaerr)
    print('FOLD_EXAMPLE_N41_K3',next(c['AB_fold'] for c in cases if c['N']==41 and c['mask_k']==3))
    print('SENSITIVITY max abs alpha error with 0.5% each channel',max(r['absolute_error'] for r in sensitivity))
    print('JACOBIAN ABSOLUTE-RMS CONDITIONING',[(x['N'],x['Jacobian_cond_2'],x['cond_2_div_N2']) for x in largeN_condition])
    out={'return_id':'M13-ROT32-FROZEN-GENERATOR-JOINT-CHANNEL-ALPHA-AMPLITUDE-IDENTIFIABILITY_001_20261024','provenance_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ('verify_m13_rot26.py','verify_m13_rot27.py','deepseek_python_20260627_a87249.py','dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv','dtc0a_mask_sensitivity_N41_v0_3_1.csv')},'cases':cases,'max_54_historical_rel_error':max_frozen_err,'max_36_extra_mask_rel_error':max_mask_err,'max_30_inversion_alpha_abs_error':max_alphaerr,'max_approx_Bernstein':max_bern,'min_numeric_analytic_log_sensitivity_certificate':worst_log_sensitivity,'max_polynomial_offgrid_tensor_norm_rel_error':max_poly_direct_err,'sensitivity_plus_minus_half_percent':sensitivity,'max_alpha_error_pm_half_percent':max(r['absolute_error'] for r in sensitivity),'largeN_absolute_RMS_Jacobian_conditioning':largeN_condition,'typing':'SOURCE_MATCHING_ALTERNATIVE_HELPER / NUMERIC_BERNSTEIN_SIGN_CERTIFICATE_NOT_DIRECTED_INTERVAL / KNOWN_C1_C2_h / ONE_COMMON_UNKNOWN_POSITIVE_SCALE / STENCIL_FIXED / NO_BYTE_EXACT_ORIGINAL_RUNTIME / NO_PHYSICS'}
    (ROOT/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':main()