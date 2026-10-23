#!/usr/bin/env python3
"""M13 ROT27 reproducible source-matched sparse Fourier finite-window RMS asymptotics.

This code does not rebuild dtc0a_runtime_v0_3_1.py, nor claim physical invariants.
All operator tensors are evaluated by the independently implemented sparse Fourier
pipeline from ROT26. Window RMS is calculated algebraically from coefficient pairs;
no large NxNxN tensor grids are used.
"""
import csv, json, math, cmath, hashlib
from pathlib import Path
import numpy as np
from verify_m13_rot26 import calc, global_rms
ROOT=Path(__file__).resolve().parent
SOURCE_CSV='dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv'
G = 5917501/3499200000000000
A_INF=math.sqrt(G)
SURFACES=[761233367/314928000000000000,1409179/656100000000000,123982963/62985600000000000]
REL_K3= -229914416/88762515

def window_mean_of_mode(q,N,k):
    """Exact arithmetic identity from finite periodic truncated-index geometric sum.

    For nonzero low-band q, mean retained exponential equals minus the removed
    2k boundary samples, divided by retained N-2k nodes.
    """
    if q==0:return 1+0j
    dx=2*math.pi/N
    removed=sum(cmath.exp(1j*q*j*dx) for j in range(k))
    removed+=sum(cmath.exp(-1j*q*j*dx) for j in range(1,k+1))
    return -removed/(N-2*k)

def masked_sq(coeff,N,k):
    keys=list(coeff)
    win={q:window_mean_of_mode(q,N,k) for q in range(-6,7)}
    s=0+0j
    for m in keys:
        x=coeff[m]
        for n in keys:
            z=np.vdot(coeff[n],x)
            for d in range(3):z*=win[m[d]-n[d]]
            s+=z
    if abs(s.imag)>1e-13*max(abs(s.real),1e-25):
        raise AssertionError(f'Imaginary leakage beyond rounding {s}')
    if s.real<-1e-26:raise AssertionError(f'Negative energy {s.real}')
    return s.real/6

def coefficient_C_B(alpha):
    C=4*math.pi**2*math.sqrt((1007*alpha*alpha+154*alpha+11)/4800000000)
    B=4*math.pi**2*math.sqrt((1213*alpha*alpha-8*alpha+2)/43200000000)
    return C,B

def source_sha(filename):return hashlib.sha256((ROOT/filename).read_bytes()).hexdigest()

def main():
    csv_rows=list(csv.DictReader((ROOT/SOURCE_CSV).open()))
    observed={(int(r['N']),float(r['alpha'])):r for r in csv_rows}
    out=[];maxerr=0
    for N in [31,33,35,37,39,41]:
        for alpha in [0.,.05,.2]:
            A,B,C,D=calc(N,alpha)
            vals={key:math.sqrt(masked_sq(t,N,3)) for key,t in [('A',A),('B',B),('C',C)]}
            errs={key:abs(vals[key]/float(observed[N,alpha]['K_'+key+'_RMS'])-1) for key in 'ABC'}
            maxerr=max(maxerr,*errs.values())
            assert max(errs.values())<3e-11,(N,alpha,errs)
            bulk_A=global_rms(A)
            out.append({'N':N,'alpha':alpha,'masked_RMS':vals,'full_A':bulk_A,'ratio_A_B_masked':vals['A']/vals['B'], 'finite_mask_shift_A':vals['A']-bulk_A,'max_rel_historical_err':max(errs.values())})
    assert len(out)==18
    print('HISTORICAL_FROZEN_RMS_MATCH_54_OF_54',maxerr)
    alpha=.05
    selected=[]
    for N in [31,41,101,201,401,1001,2001,10001]:
        A,B,C,_=calc(N,alpha)
        rms=math.sqrt(masked_sq(A,N,3));global_A=global_rms(A)
        coeffC,coeffB=coefficient_C_B(alpha)
        eC=abs((N*N*global_rms(C))/coeffC-1)
        eB=abs((N*N*global_rms(B))/coeffB-1)
        leading=A_INF*(1+REL_K3/N)
        scaled=(rms/A_INF-1)*N
        selected.append({'N':N,'masked_KA':rms,'global_KA':global_A,'asymptotic_Ninv_prediction':leading,'N_times_relative_difference_to_limit':scaled,'N2_times_global_KC':N*N*global_rms(C),'N2_times_global_KB':N*N*global_rms(B),'C_lead_relerr':eC,'B_lead_relerr':eB,'finite_mask_shift':rms-global_A})
        print('TEST',N,'KA',rms,'scaled relative',scaled,'N²C',N*N*global_rms(C),'N²B',N*N*global_rms(B))
    assert abs(selected[-1]['N_times_relative_difference_to_limit']/REL_K3-1)<.002
    assert selected[-1]['C_lead_relerr']<1e-5 and selected[-1]['B_lead_relerr']<1e-5
    assert all(y['masked_KA']>0 and y['finite_mask_shift']<0 for y in selected)
    # Check first-order boundary plane expression with finite-band limiting tensor.
    Ain=calc(None,0)[0]
    surf=[]
    for dim in range(3):
        p=0+0j
        for m,x in Ain.items():
            for n,y in Ain.items():
                if all(m[j]==n[j] for j in range(3) if j!=dim):p+=np.vdot(y,x)
        surf.append(p.real/6)
    assert np.allclose(surf,SURFACES,rtol=3e-12,atol=0),surf
    assert abs(3*(3-sum(surf)/G)-REL_K3)<1e-10
    result={'return_id':'M13-ROT27-DTC0A-MASK_FIRST_ORDER_VS_STENCIL_SECOND_ORDER_AND_EXACT_RATIO_SCALING-001_20261023','source_sha256':{SOURCE_CSV:source_sha(SOURCE_CSV),'verify_m13_rot26.py':source_sha('verify_m13_rot26.py')},'exact_limit_KA_global_RMS_squared':'5917501/3499200000000000','exact_surface_plane_squares':['761233367/314928000000000000','1409179/656100000000000','123982963/62985600000000000'],'exact_k3_relative_Ninv_KA_coefficient':'-229914416/88762515','exact_KC_leading_N2_squared_factor':'(2*pi)^4*(1007*alpha^2+154*alpha+11)/4800000000','exact_KB_leading_N2_squared_factor':'(2*pi)^4*(1213*alpha^2-8*alpha+2)/43200000000','historical_scalar_norms_checked':54,'max_historical_rel_err':maxerr,'historical_series':out,'largeN_validation':selected,'status':'EXACT_FIXED_SOURCE_FINITE_BAND / NO_BYTE_EXACT_RUNTIME / NO_PHYSICAL_OR_CANONICAL_UPGRADE'}
    dest=ROOT/'IW_M13_ROT27_mask_stencil_asymptotics_20261023.json';dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
    print('PASS',dest)
if __name__=='__main__':main()