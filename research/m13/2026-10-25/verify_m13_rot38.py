#!/usr/bin/env python3
"""M13 ROT38: conditional direct-source interval certified FIVE-mask global argmin.
For true alpha=1/20, alternatives beta in [0,1/5] outside (1/25,3/50).
Uses original helper-matching source mode algebra from ROT33, NOT missing runtime bytes.
Assumes mpmath.iv correctly provides outward-enclosed arithmetic.
"""
import csv, json, math, hashlib
from pathlib import Path
from mpmath import iv
from verify_m13_rot33_interval import tensor_polys, quartic, bernstein, polyd, polymul

iv.dps=45
ROOT=Path(__file__).resolve().parent
N=41; MASKS=(2,3,4,5,6); n=[(N-2*k)**3 for k in MASKS]
v=[n[i]-n[i+1] for i in range(4)]+[n[-1]]
Z=iv.mpf(0); AL=iv.mpf(1)/20; BETA_LEFT=iv.mpf(1)/25; BETA_RIGHT=iv.mpf(3)/50; HIGH=iv.mpf(1)/5; LOW=iv.mpf(0)

def pe(p,x):
    ret=iv.mpf(0)
    for c in reversed(p):ret=ret*x+c
    return ret

def pa(a,b):
    return [(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))]

def ps(p,s):return [c*s for c in p]
def der(p):return [i*p[i] for i in range(1,len(p))]
def minus(a,b):return pa(a,ps(b,-1))
def lower(x):return float(x.a)
def upper(x):return float(x.b)
def directed_bounds_strings(x):
    # Preserve the OUTWARD printed interval endpoints, not only float-rounded UI values.
    return [str(x.a),str(x.b)]
def directed_bounds_dyadic(x):
    # Stable, exact dyadic binary interval endpoints: [sign,mantissa,exponent,bitcount].
    return [list(x.a._mpi_[0]),list(x.b._mpi_[1])]
def sqrtdistance(a,b,weights):
    # Cauchy-Binet/Lagrange identity for weighted orthogonal least squares,
    # no catastrophic subtraction of two nearly equal projection norms.
    cross=sum((iv.mpf(weights[i])*b[i]*b[i] for i in range(len(b))),Z)
    numerator=sum((iv.mpf(weights[i]*weights[j])*(a[i]*b[j]-a[j]*b[i])**2 for i in range(len(a)) for j in range(i+1,len(a))),Z)
    assert cross.a>0 and numerator.a>0
    return iv.sqrt(numerator/cross)

def bn(p,a,b):
    # Monomial -> Bernstein basis on x=a+(b-a)t, t in [0,1].
    degree=len(p)-1;length=b-a
    coeff=[sum((p[r]*math.comb(r,j)*a**(r-j)*length**j for r in range(j,degree+1)),Z) for j in range(degree+1)]
    return [sum((coeff[j]*iv.mpf(math.comb(i,j))/math.comb(degree,j) for j in range(i+1)),Z) for i in range(degree+1)]

def certify_positive(p,a=LOW,b=HIGH):
    coeff=bn(p,a,b)
    return min(lower(c) for c in coeff),max(upper(c) for c in coeff)

def cert_sign(p,a,b,expected):
    lo,hi=certify_positive(p,a,b)
    coeff=bn(p,a,b)
    if expected=='+':assert all(z.a>0 for z in coeff),(expected,lo,hi)
    else:assert all(z.b<0 for z in coeff),(expected,lo,hi)
    return {'interval':[lower(a),upper(b)],'min_bernstein_lower':lo,'max_bernstein_upper':hi,'sign':expected}

P=tensor_polys(N)
cache={};G={};shells={}
for idx,ch in enumerate('ABC'):
    gs=[quartic(P[idx],N,k,cache) for k in MASKS]
    for j,k in enumerate(MASKS):G[ch,k]=gs[j]
    shell=[[(n[j]*gs[j][i]-n[j+1]*gs[j+1][i])/v[j] for i in range(5)] for j in range(4)]+[gs[-1]]
    for j,p in enumerate(shell):
        lo,hi=certify_positive(p)
        assert lo>0,(ch,j,lo,hi)
    shells[ch]=shell

# Full, source-matched frozen 45 RMS check for historical N41 mask table.
ref={(r['alpha'],int(r['interior_k'])):r for r in csv.DictReader((ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open())}
maxrel=0.;check_count=0
for ch in 'ABC':
    for k in MASKS:
        for ans,alpha in [('0.0',LOW),('0.05',AL),('0.2',HIGH)]:
            observed=math.sqrt(float(pe(G[ch,k],alpha).mid));expected=float(ref[ans,k]['K_'+ch+'_RMS'])
            maxrel=max(maxrel,abs(observed/expected-1));check_count+=1
assert check_count==45 and maxrel<1e-11,(check_count,maxrel)

proofs=[]
for ch in 'ABC':
    sh=shells[ch]
    a=[pe(p,AL) for p in sh]
    p=[sum((iv.mpf(v[i])*a[i]*sh[i][j] for i in range(5)),Z) for j in range(5)]
    q=[Z]*9
    for i in range(5):q=pa(q,ps(polymul(sh[i],sh[i]),v[i]))
    # H = <a,b'>_W ||b||_W² - <a,b>_W <b,b'>_W.
    # D²=||a||²−<a,b>²/||b||² hence sign(D²') = -sign(H)
    H=minus(polymul(der(p),q),ps(polymul(p,der(q)),iv.mpf(1)/2))
    certs=[]
    if ch=='B':
        certs.append(cert_sign(H,iv.mpf(1)/50,BETA_LEFT,'+'))
    else:
        certs.append(cert_sign(H,LOW,BETA_LEFT,'+'))
    certs.append(cert_sign(H,BETA_RIGHT,HIGH,'-'))
    tau=iv.mpf(1)/100*pe(G[ch,2],AL)
    dist04=sqrtdistance(a,[pe(s,BETA_LEFT) for s in sh],v)/tau
    dist06=sqrtdistance(a,[pe(s,BETA_RIGHT) for s in sh],v)/tau
    assert dist04.a>dist06.b,(ch,'endpoints',dist04,dist06)
    out={'channel':ch,'five_mask_true_alpha':.05,'excluded_abs_alpha_distance':.01,
        'global_interval_derivative_sign_certificates':certs,
        'sigma_energy_per_voxel':float(tau.mid),
        'endpoint_left0p04_sigma_interval':[lower(dist04),upper(dist04)],
        'endpoint_right0p06_sigma_interval':[lower(dist06),upper(dist06)],
        'endpoint_left0p04_sigma_directed_decimal':directed_bounds_strings(dist04),
        'endpoint_right0p06_sigma_directed_decimal':directed_bounds_strings(dist06),
        'endpoint_right0p06_sigma_exact_dyadic':directed_bounds_dyadic(dist06),
        'exact_argmin_beta':.06,'global_min_five_sigma_interval':[lower(dist06),upper(dist06)]}
    if ch=='B':
        # All beta in [0,.02]: full-five d >= pair(5,6) d.
        # B 5/6 mask ratio certified strictly increasing over [0,.2].
        g5,g6=G['B',5],G['B',6]
        certpair=cert_sign(polyd(g5,g6),LOW,HIGH,'+')
        ni,nj=n[3],n[4];shellcount=ni-nj
        def twoshell(beta):
            ai,aj=pe(g5,AL),pe(g6,AL)
            bi,bj=pe(g5,beta),pe(g6,beta)
            a2=[(ni*ai-nj*aj)/shellcount,aj]
            b2=[(ni*bi-nj*bj)/shellcount,bj]
            return sqrtdistance(a2,b2,[shellcount,nj])/tau
        pair_at002=twoshell(iv.mpf(1)/50)
        assert pair_at002.a>dist06.b,('B left branch certificate',pair_at002,dist06)
        out['left_branch_0_to0p02_argument']='Full 5 masks >= B pair masks 5/6, which has monotonic polar angle: d_pair(beta) >= d_pair(.02) on [0,.02]'
        out['left_branch_pair_mask5_6_ratio_sign_certificate']=certpair
        out['pair_beta0p02_sigma_interval']=[lower(pair_at002),upper(pair_at002)]
        out['pair_beta0p02_sigma_directed_decimal']=directed_bounds_strings(pair_at002)
        out['pair_beta0p02_sigma_exact_dyadic']=directed_bounds_dyadic(pair_at002)
        out['full_five_H_beta0_directed_decimal']=directed_bounds_strings(pe(H,LOW))
        assert pe(H,LOW).b < 0
    proofs.append(out)
    print(ch,'exact five-mask argmin beta=.06, sigma=',[lower(dist06),upper(dist06)],
          'left endpoint beta=.04',float(dist04.mid),
          'Hleft_lower',certs[0]['min_bernstein_lower'],'Hright_upper',certs[1]['max_bernstein_upper'],flush=True)

# Independent numerical consistency vs archived ROT36 global optimizer values.
rot36=json.loads((ROOT/'IW_M13_ROT36_global_shell_separation_20261025.json').read_text())
max_gap=0
for p in proofs:
    prev=next(x for x in rot36['records'] if x['channel']==p['channel'] and x['alpha_true']==.05)
    num=prev['five_masks_sep_in_sigma_units']
    gap=abs(num-p['global_min_five_sigma_interval'][0]); max_gap=max(max_gap,gap)
    assert gap<3e-8,(p['channel'],num,p['global_min_five_sigma_interval'])
    p['ROT36_numeric_cross_check_sigma']=num
    p['ROT36_difference_sigma']=gap

result={'return_id':'M13-ROT38-DTC0A-EXACT-FIVE-MASK-GLOBAL-ARGMIN-ALPHA0P05_001_20261025',
 'N':N,'masks':list(MASKS),'alpha_true':.05,'alternative_constraint':'beta in [0,.2], |beta-.05|>=.01',
 'conditional_noise':'iid additive common-variance voxel ENERGY noise, tau_channel=0.01*g_channel,mask2(alpha=.05); common positive gain for 5 masks; no empirical calibration',
 'proof_class':'source-matching sparse Fourier direct mpmath.iv outward interval Bernstein signs plus analytic shell gain-profile geometry; assumes interval library sound; not formal proof assistant',
 'proof_algebra':'D²=||a||W²-(a^T W b)²/(b^T W b); H=p\'q-pq\'/2, p=a^T W b, q=b^T W b, sign derivative of D² opposite H; B left branch excluded using certified mask5/6 monotone pair',
 'source_file':'verify_m13_rot33_interval.py from ROT33 source-matched independent interval helper; missing historical dtc0a_runtime_v0_3_1.py is not asserted',
 'historical_45_max_relative_error':maxrel,'cases':proofs,'max_gap_vs_ROT36_uncertified_numerical_result':max_gap,
 'negative_knowledge':['NO blanket claim for all alpha_true: only alpha_true=0.05 fixed in exact 5-mask argmin proof','Full-five β derivative not globally monotone for B: excluded [0,.02] through a distinct pair-based lower certificate','Neither independence of channel errors nor voxel noise covariance is measured empirically','Raw K_A(h=fI) ambient puretrace diagnostic not TT restricted invariant','Original historical runtime byte-exact unavailable; no BW ingestion, independent referee or EXEC signoff','No physics, novelty, K/J3 or TPE upgrades']}
fn=ROOT/'IW_M13_ROT38_five_mask_exact_argmin_20261025.json'
fn.write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('ROT38 EXACT FIVE MASK SOURCE CONDITIONAL GLOBAL ARGMIN 3/3 PASS; HISTORIC 45/45; max_gap',max_gap)