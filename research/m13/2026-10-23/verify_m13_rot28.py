#!/usr/bin/env python3
"""ROT28: source-frozen multi-mask RMS cross-validation and mask-bias cancellation.

All numerical fields are independently reconstructed by the sparse Fourier code
from ROT26; never the missing byte-exact historical production runner.
Input CSV read-only. No numerical giant-grid calculations.
"""
import csv, sys, json, math, hashlib, importlib.util
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from verify_m13_rot26 import calc,global_rms
from verify_m13_rot27 import masked_sq,A_INF,G,REL_K3
FROZEN='dtc0a_mask_sensitivity_N41_v0_3_1.csv'
CONV='dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv'

def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def val(r,ch):return float(r['K_'+ch+'_RMS'])
def two_extrap(g,k0,k1):
    # First-order in k/N cancellation of squared RMS. Negative estimates invalid.
    return (k1*g[k0]-k0*g[k1])/(k1-k0)
def poly_extrap(g,ks):
    # Lagrange polynomial extrapolation in mask index k toward k=0.
    return sum(g[k]*math.prod((-j)/(k-j) for j in ks if j!=k) for k in ks)
def dimless(v,vref):return v/vref-1

def main():
    observations=list(csv.DictReader((ROOT/FROZEN).open()))
    assert len(observations)==15
    observed={(float(r['alpha']),int(r['interior_k'])):r for r in observations}
    odd=list(csv.DictReader((ROOT/CONV).open()));oddkey={(int(r['N']),float(r['alpha'])):r for r in odd}
    assert len(odd)==18
    N=41
    cases=[];maxfrozen=0;maxodd=0;maxshellenergyneg=0
    for alpha in (0.,.05,.2):
        A,B,C,_=calc(N,alpha)
        chans={'A':A,'B':B,'C':C}
        for name,coeff in chans.items():
            gg={k:masked_sq(coeff,N,k) for k in range(2,7)}
            gr=global_rms(coeff)**2
            for k in range(2,7):
                rel=abs(math.sqrt(gg[k])/val(observed[alpha,k],name)-1)
                maxfrozen=max(maxfrozen,rel)
                assert rel<3e-11,(alpha,k,name,rel)
            # source match original k3 all channels, separate check
            maxodd=max(maxodd,abs(math.sqrt(gg[3])/val(oddkey[N,alpha],name)-1))
            assert maxodd<3e-11
            rec={}
            for ks in [(2,3),(3,4),(2,3,4),(2,4,6),(2,3,4,5),(2,3,4,5,6)]:
                est=two_extrap(gg,*ks) if len(ks)==2 else poly_extrap(gg,ks)
                assert est>0,(alpha,name,ks,est)
                rec['k'+''.join(str(k) for k in ks)]={'estimate_rms':math.sqrt(est),'relative_error_to_full':dimless(math.sqrt(est),math.sqrt(gr)),'relative_error_squared_to_full':dimless(est,gr),'weights_l1':sum(abs(math.prod((-j)/(k-j) for j in ks if j!=k)) for k in ks)}
            # exact shell energy sum identity for fixed unprojected/full tensor
            shell=[]
            for k in range(2,6):
                n0=(N-2*k)**3;n1=(N-2*(k+1))**3
                sg=(n0*gg[k]-n1*gg[k+1])/(n0-n1)
                maxshellenergyneg=min(maxshellenergyneg,sg)
                assert sg>0,(alpha,name,k,sg)
                shell.append({'outer_mask_index':k,'inner_mask_index':k+1,'shell_rms':math.sqrt(sg),'relative_to_inner_cube':math.sqrt(sg/gg[k+1]),'energy_share_of_outer_cube':(n0*gg[k]-n1*gg[k+1])/(n0*gg[k])})
            cases.append({'N':N,'alpha':alpha,'channel':name,'global_RMS':math.sqrt(gr),
                          'historical_mask_RMS':{str(k):math.sqrt(gg[k]) for k in gg},
                          'raw_k3_relative_error_to_full':dimless(math.sqrt(gg[3]),math.sqrt(gr)),
                          'corrected':rec,'shells':shell})
    print('PASS HISTORICAL MASK VALUES 45/45; max rel deviation',maxfrozen)
    print('PASS HISTORICAL N41 odd values 9/9; max rel deviation',maxodd)
    assert len(cases)==9 and maxfrozen<3e-11
    assert all(abs(c['corrected']['k23']['relative_error_to_full'])<abs(c['raw_k3_relative_error_to_full']) for c in cases)
    assert sum(len(c['shells']) for c in cases)==36
    # Main asymptotic O(N^-2) demonstration on source-matched bandlimited family.
    large=[]
    for N in (31,41,61,101,201,401,1001,2001,10001):
        alpha=.05
        A,B,C,_=calc(N,alpha)
        for name,coeff in [('A',A),('B',B),('C',C)]:
            gr=global_rms(coeff)**2
            g2=masked_sq(coeff,N,2);g3=masked_sq(coeff,N,3)
            assert g3>0
            ext=two_extrap({2:g2,3:g3},2,3)
            raw_rel=math.sqrt(g3/gr)-1
            corr_rel=math.sqrt(ext/gr)-1
            large.append({'N':N,'alpha':alpha,'channel':name,'global_RMS':math.sqrt(gr),'raw_k3_RMS':math.sqrt(g3),'two_mask_2_3_RMS':math.sqrt(ext),'raw_relative_error_to_full':raw_rel,'corrected_relative_error_to_full':corr_rel,'gain_absolute_relative_error':abs(raw_rel)/abs(corr_rel) if corr_rel else None,'N_times_raw_relative_error':N*raw_rel,'N2_times_corrected_relative_error':N*N*corr_rel,'full_relative_to_continuum_A':math.sqrt(gr)/A_INF-1 if name=='A' else None})
    for name in 'ABC':
        v=[z for z in large if z['channel']==name]
        print(name,'N31 raw/corr',v[0]['raw_relative_error_to_full'],v[0]['corrected_relative_error_to_full'],'N41',v[1]['raw_relative_error_to_full'],v[1]['corrected_relative_error_to_full'],'N10001',v[-1]['N2_times_corrected_relative_error'])
        # If leading cancellation is correct, corrected norm error is O(N^-2), raw O(N^-1)
        assert abs(v[-1]['N_times_raw_relative_error'] - v[-2]['N_times_raw_relative_error']) < .02
        print('TAIL',name,[(z['N'],z['N2_times_corrected_relative_error']) for z in v[-5:]])
        if name=='A':
            EXACT=42624128/17752503
            assert abs(v[-1]['N2_times_corrected_relative_error']-EXACT)<.11
            assert all(abs(w['corrected_relative_error_to_full'])<abs(w['raw_relative_error_to_full']) for w in v)
        elif name=='B':
            assert abs(v[-1]['N2_times_corrected_relative_error']/v[-2]['N2_times_corrected_relative_error']-1)<.01
        else:
            assert all(abs(w['corrected_relative_error_to_full'])<abs(w['raw_relative_error_to_full']) for w in v)
    # Do not assume generic extrapolation is positive / stable: higher order amplify noise
    for c in cases:
      if c['channel']=='A':
       print('N41 alpha',c['alpha'],'FULL',c['global_RMS'],'K3',c['historical_mask_RMS']['3'],'EX23',c['corrected']['k23']['estimate_rms'],'EX234',c['corrected']['k234']['estimate_rms'],'EX2345',c['corrected']['k2345']['estimate_rms'])
    report={'return_id':'M13-ROT28-DTC0A-TWO_MASK_FIRST_ORDER_BIAS_CANCELLATION_001_20261023',
            'provenance':{p:sha(p) for p in [FROZEN,CONV,'verify_m13_rot26.py','verify_m13_rot27.py','deepseek_python_20260627_a87249.py']},
            'historical_mask_scalar_values_checked':45,'historical_grid_N41_scalar_values_checked':9,
            'maximum_mask_csv_rel_deviation':maxfrozen,'maximum_N41_grid_csv_rel_deviation':maxodd,
            'N41_cases':cases,'large_N_diagnostics':large,
            'theory':'For fixed k and C^2 uniformly bounded energy F_N, g_k(N)=g_full(N)+a_N*k/N+O(k^2/N^2); thus extrapolation (k1 g_k0-k0 g_k1)/(k1-k0)=g_full+O(N^-2). Depends on same fields/N/alpha, not physical fixed-domain proof.',
            'status':'SOURCE_MATCH_54/54_EXTERNAL_45/45 / EXACT_CONDITIONAL_MASK_DEBIAS / REPLAY_NOT_ORIGINAL_BYTES / NO_CANON / TPE_HOLD'}
    out=ROOT/'IW_M13_ROT28_mask_extrapolation_and_shells_20261023.json'
    out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
    print('PASS',out)
if __name__=='__main__':main()