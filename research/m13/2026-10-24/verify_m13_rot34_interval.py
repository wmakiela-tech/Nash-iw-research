#!/usr/bin/env python3
"""M13 ROT34 source-native directed interval, one-channel multi-mask alpha ID.

This is conditional on the retained functional source formula, NOT original
historical production runner. Requires mpmath 1.3.0. Prints pass certificates.
"""
from __future__ import annotations
import json,math,sys,time,csv
from pathlib import Path
from mpmath import iv
from verify_m13_rot33_interval import (tensor_polys, quartic, bernstein, polyd,
    ZERO, ONE, ROOT, bounds, mid, all_negative)

iv.dps=45
N=41
ks=(2,3,4,5,6)
alpha_hi=iv.mpf(1)/5

def peval(coeff,x):
    acc=ZERO
    for c in reversed(coeff):acc=acc*x+c
    return acc

def sign_at_endpoint(p,alpha):
    a=peval(p,iv.mpf(alpha))
    return 'POS' if a.a>0 else 'NEG' if a.b<0 else 'UNCERTIFIED'

def bounded_alpha_log_slope(g1,g2,sign,nsub=80):
    # On each interval, Horner range enclosure of p,g1,g2. Conservative.
    p=polyd(g1,g2); lower=float('inf'); upper=0.
    for i in range(nsub):
        a=iv.mpf(i)/(5*nsub);b=iv.mpf(i+1)/(5*nsub)
        x=iv.mpf([a.a,b.b]);pp=peval(p,x);d1=peval(g1,x);d2=peval(g2,x)
        if d1.a <= 0 or d2.a <=0: return (0.,float('inf'),False)
        d=pp/(2*d1*d2)
        if sign=='UP' and d.a<=0:return (0.,float('inf'),False)
        if sign=='DOWN' and d.b>=0:return (0.,float('inf'),False)
        lo=float(d.a) if sign=='UP' else -float(d.b)
        hi=float(d.b) if sign=='UP' else -float(d.a)
        lower=min(lower,lo);upper=max(upper,hi)
    return (lower,upper,True)

def main():
    t=time.monotonic()
    pols=tensor_polys(N)
    source_quartics={}
    for k in ks:
        cache={}
        source_quartics[k]={channel:quartic(pols[idx],N,k,cache) for idx,channel in enumerate('ABC')}
    rows=[]
    for ch in 'ABC':
        for k1 in ks:
            for k2 in ks:
                if k2<=k1:continue
                a=source_quartics[k1][ch];b=source_quartics[k2][ch]
                ba=bernstein(a);bb=bernstein(b)
                assert all(v.a>0 for v in ba+bb),(ch,k1,k2,'not positive')
                p=polyd(a,b);bp=bernstein(p)
                sign='UP' if all(v.a>0 for v in bp) else 'DOWN' if all(v.b<0 for v in bp) else 'UNDECIDED'
                endpoint0=sign_at_endpoint(p,0);endpoint2=sign_at_endpoint(p,alpha_hi)
                fold=endpoint0!=endpoint2 and endpoint0!='UNCERTIFIED' and endpoint2!='UNCERTIFIED'
                if fold:assert sign=='UNDECIDED',(ch,k1,k2,'fold and monotone')
                lbound=0.;ubound=float('inf');subpass=False
                if sign in ('UP','DOWN'):
                    lbound,ubound,subpass=bounded_alpha_log_slope(a,b,sign)
                    assert subpass and lbound>0,(ch,k1,k2,'subdivision')
                v0=math.sqrt(float((a[0]/b[0]).mid))
                ealpha=alpha_hi
                v2=math.sqrt(float((peval(a,ealpha)/peval(b,ealpha)).mid))
                eps=.005
                guaranteed_error=math.log((1+eps)/(1-eps))/lbound if lbound>0 else None
                rows.append(dict(channel=ch,k1=k1,k2=k2,bernstein_sign=sign,
                    endpoint_derivative_sign0=endpoint0,endpoint_derivative_sign_point2=endpoint2,
                    strict_fold_witness=fold, normalized_Bernstein_bounds=[bounds(v/(a[0]*b[0])) for v in bp],
                    RMS_ratio_at_alpha0=v0,RMS_ratio_at_alpha_point2=v2,
                    total_log_ratio_shift=math.log(v2/v0),
                    rigorous_lower_abs_dlogR_dalpha=lbound,
                    rigorous_upper_abs_dlogR_dalpha=ubound if lbound>0 else None,
                    worst_case_alpha_error_bound_for_0point5_percent_per_mask=guaranteed_error))
    assert len(rows)==30
    c=lambda ch,k1,k2:next(r for r in rows if r['channel']==ch and r['k1']==k1 and r['k2']==k2)
    assert all(r['bernstein_sign']=='UP' for r in rows if r['channel']=='A')
    assert all(c('C',2,k)['bernstein_sign']=='DOWN' for k in (3,4,5,6))
    assert c('B',2,3)['strict_fold_witness'] and c('B',3,4)['strict_fold_witness']
    assert c('B',5,6)['bernstein_sign']=='UP'
    frozen={(r['alpha'],int(r['interior_k'])):r for r in csv.DictReader((ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open())}
    assert len(frozen)==15
    max_frozen=0
    for k in ks:
        for aname,an in [('0.0',iv.mpf(0)),('0.05',iv.mpf(1)/20),('0.2',iv.mpf(1)/5)]:
            for ch in 'ABC':
                calc=math.sqrt(float(peval(source_quartics[k][ch],an).mid));want=float(frozen[(aname,k)]['K_'+ch+'_RMS'])
                max_frozen=max(max_frozen,abs(calc/want-1))
                assert abs(calc/want-1)<1e-11,(k,aname,ch,calc,want)
    cert={'return_id':'M13-ROT34-DTC0A-ONE-CHANNEL-FIVE-MASK-SOURCE-INTERVAL-IDENTIFIABILITY-001_20261024',
          'source_family':'retained helper matching historic RMS, fixed N41, five nested masks 2..6, alpha 0..0.2, channel amplitudes common ONLY across masks, polynomial source operator',
          'arithmetic':'mpmath.iv outward rounded 45 decimal digits; generated directly from modal operator, all Bernstein coefficients intervals',
          'source_model_and_target_limits':'not full historical runtime; no physics; no arbitrary TT tensors; assumption all mask reads use same gain',
          'rows':rows,'n_pair_channel_certificates':len(rows),'n_monotone_up':sum(r['bernstein_sign']=='UP' for r in rows),
          'n_monotone_down':sum(r['bernstein_sign']=='DOWN' for r in rows),
          'n_endpoint_certified_fold':sum(r['strict_fold_witness'] for r in rows),
          'n_unresolved':sum(r['bernstein_sign']=='UNDECIDED' and not r['strict_fold_witness'] for r in rows),
          'max_relative_frozen_RMS_error_45_samples':max_frozen,
          'best_C_pair_by_certified_min_slope':sorted([r for r in rows if r['channel']=='C' and r['bernstein_sign'] in ('UP','DOWN')],key=lambda r:-r['rigorous_lower_abs_dlogR_dalpha'])[0]['k1:k2'] if False else None}
    p=ROOT/'IW_M13_ROT34_one_channel_mask_ratio_certificates_20261024.json'
    p.write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n')
    print('INTERVAL_ALL',len(rows),'monotone-up',cert['n_monotone_up'],'monotone-down',cert['n_monotone_down'],
          'fold',cert['n_endpoint_certified_fold'],'unresolved',cert['n_unresolved'])
    for ch,k1,k2 in [('A',2,3),('A',2,6),('B',2,3),('B',5,6),('C',2,3),('C',2,4),('C',3,6)]:
        r=c(ch,k1,k2)
        print(ch,k1,k2, r['bernstein_sign'],'end sign',r['endpoint_derivative_sign0'],r['endpoint_derivative_sign_point2'],'shift',r['total_log_ratio_shift'],'rigorous lower slope',r['rigorous_lower_abs_dlogR_dalpha'],'eps 0.5% alpha bound',r['worst_case_alpha_error_bound_for_0point5_percent_per_mask'])
    print('FROZEN_45_MAX_REL',max_frozen,'TIME',time.monotonic()-t,'s')
if __name__=='__main__':main()