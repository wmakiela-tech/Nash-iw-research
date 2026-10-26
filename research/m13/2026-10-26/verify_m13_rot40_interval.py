#!/usr/bin/env python3
"""ROT40: globally radial monotone N41 full-five-mask profile for source A,C.
Uses preserved direct mpmath.iv coefficient enclosures from actual Fourier source
operator, NOT the rounded quartics from ROT32. No historical runtime claim.
"""
import json,csv,math,hashlib
from fractions import Fraction
from pathlib import Path
from mpmath import iv
iv.dps=45
ROOT=Path(__file__).resolve().parent
ZERO=iv.mpf(0);ONE=iv.mpf(1);ALPHA_MAX=ONE/5
N=41; KS=tuple(range(2,7));n=[(N-2*k)**3 for k in KS];w=[n[i]-n[i+1] for i in range(4)]+[n[-1]]

def lo(x):return float(x.a)
def hi(x):return float(x.b)
def end(x):return [str(x.a),str(x.b)]
def from_source(lo_str,hi_str):
    # Source intervals str(x.a)/str(x.b) produced by outward-rounded mp.iv.
    # Parsing their decimal renderings with directed interval re-rounding widens.
    def get(s):return s.removeprefix('[').split(',')[0].strip()
    return iv.mpf([get(lo_str),get(hi_str)])
def to_ber(p,a=ZERO,b=ALPHA_MAX):
    d=len(p)-1
    # t=(alpha-a)/(b-a) exact polynomial basis conversion.
    power=[sum((p[r]*math.comb(r,j)*a**(r-j)*(b-a)**j for r in range(j,d+1)),ZERO) for j in range(d+1)]
    return [sum((power[j]*iv.mpf(math.comb(i,j))/math.comb(d,j) for j in range(i+1)),ZERO) for i in range(d+1)]
def p_add(a,b):
    d=a.copy()
    for k,v in b.items():d[k]=d.get(k,ZERO)+v
    return d
def p_mul(a,b):
    o={}
    for (i,j),v in a.items():
        for (k,l),u in b.items():o[i+k,j+l]=o.get((i+k,j+l),ZERO)+v*u
    return o
def p_scale(a,v):return {k:x*v for k,x in a.items()}
def p_derbeta(a):return {(i,j-1):v*j for (i,j),v in a.items() if j>0}
def p_a(p):return {(i,0):val for i,val in enumerate(p)}
def p_b(p):return {(0,j):val for j,val in enumerate(p)}
def pq(poly,al,be):return sum((val*al**i*be**j for (i,j),val in poly.items()),ZERO)
def p_bern2(p):
    # All 2D tensor Bernstein coefficients on alpha,beta∈[0,1/5].
    da=max(i for i,j in p);db=max(j for i,j in p)
    coeff=[[ZERO for j in range(db+1)] for i in range(da+1)]
    for (ia,ib),c in p.items():
        t=c*ALPHA_MAX**(ia+ib)
        for i in range(ia,da+1):
            ai=iv.mpf(math.comb(i,ia))/math.comb(da,ia)
            for j in range(ib,db+1):
                coeff[i][j]+=t*ai*iv.mpf(math.comb(j,ib))/math.comb(db,ib)
    return coeff

def source_data(ch):
    raw=json.loads((ROOT/f'direct_{ch}.json').read_text())
    return [[from_source(*bounds) for bounds in raw[str(k)]] for k in KS]

def shells(g):
    return [[(n[i]*g[i][r]-n[i+1]*g[i+1][r])/w[i] for r in range(5)] for i in range(4)]+[g[4]]

def hquotient(sh):
    # p=<s(alpha),s(beta)>_W, q=||s(beta)||_W^2,
    # H=2 p_beta q - p q_beta = (beta-alpha)*Q.
    p={};q={}
    for i in range(5):
        aa=p_a(sh[i]);bb=p_b(sh[i]);p=p_add(p,p_scale(p_mul(aa,bb),w[i]))
        q=p_add(q,p_scale(p_mul(bb,bb),w[i]))
    H=p_add(p_scale(p_mul(p_derbeta(p),q),2),p_scale(p_mul(p,p_derbeta(q)),-1))
    degree=max(j for i,j in H)
    coeff=[{i:v for (i,jj),v in H.items() if jj==j} for j in range(degree+1)]
    # Synthetic division of H by beta-alpha in coefficient ring IV[alpha].
    Q=[{} for _ in range(degree)]
    Q[degree-1]=coeff[degree]
    for j in range(degree-1,0,-1):
        multiplied={i+1:v for i,v in Q[j].items()}
        Q[j-1]={i:coeff[j].get(i,ZERO)+multiplied.get(i,ZERO) for i in set(coeff[j])|set(multiplied)}
    # -Q is the positive radial certificate if β<α H>0 / β>α H<0.
    pos={(i,j):-val for j,poly in enumerate(Q) for i,val in poly.items()}
    return H,pos

def run():
    hist={(r['alpha'],int(r['interior_k'])):r for r in csv.DictReader((ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open())}
    res={};maxrel=0
    for ch in 'ABC':
        g=source_data(ch); sh=shells(g)
        shellbounds=[]
        for idx,p in enumerate(sh):
            b=to_ber(p)
            assert all(x.a>0 for x in b),(ch,idx,'nonpositive energy')
            shellbounds.append([str(min((z.a for z in b),key=lo))])
        for j,k in enumerate(KS):
            for alpha_label,alpha in [('0.0',ZERO),('0.05',ONE/20),('0.2',ONE/5)]:
                rms=iv.sqrt(sum((g[j][i]*alpha**i for i in range(5)),ZERO));truth=float(hist[alpha_label,k]['K_'+ch+'_RMS'])
                err=abs(float(rms.mid)/truth-1);maxrel=max(maxrel,err)
                assert err<1e-11,(ch,k,alpha_label,err)
        H,Q=hquotient(sh)
        tau=(ONE/100)*sum((g[0][i]*(ONE/20)**i for i in range(5)),ZERO)
        def pointdist(a0,b0):
            av=[sum((t*a0**j for j,t in enumerate(vec)),ZERO) for vec in sh]
            bv=[sum((t*b0**j for j,t in enumerate(vec)),ZERO) for vec in sh]
            nom=sum((iv.mpf(w[i]*w[j])*(av[i]*bv[j]-av[j]*bv[i])**2 for i in range(5) for j in range(i+1,5)),ZERO)
            den=sum((w[i]*bv[i]*bv[i] for i in range(5)),ZERO)
            return iv.sqrt(nom/den)/tau
        sample=[]
        for x in [Fraction(0),Fraction(1,50),Fraction(1,20),Fraction(1,10),Fraction(3,20),Fraction(9,50),Fraction(1,5)]:
            xi=iv.mpf(x.numerator)/x.denominator;d=ONE/100
            opts=[]
            for y in [x-Fraction(1,100),x+Fraction(1,100)]:
                if y<0 or y>Fraction(1,5):continue
                yi=iv.mpf(y.numerator)/y.denominator;sd=pointdist(xi,yi)
                opts.append({'beta':str(y),'sigma_interval_directed':end(sd),'sigma_mid_NONPROOF':float(sd.mid)})
            minopt=min(opts,key=lambda z:z['sigma_mid_NONPROOF'])
            # For these anchor values, strict interval comparison certifies selected endpoint.
            if len(opts)==2:
                vals=[pointdist(xi,iv.mpf(Fraction(o['beta']).numerator)/Fraction(o['beta']).denominator) for o in opts]
                assert (vals[0].b<vals[1].a) or (vals[1].b<vals[0].a)
            sample.append({'alpha':str(x),'endpoints':opts,'smaller_endpoint_CERTIFIED':minopt['beta']})

        coef=p_bern2(Q)
        allc=[x for row in coef for x in row]
        status=all(x.a>0 for x in allc)
        smallest=min((x.a for x in allc),key=lo)
        biggest=max((x.b for x in allc),key=hi)
        diag={'bernstein_degree':[len(coef)-1,len(coef[0])-1],
              'positive_radial_Bernstein_all':status,
              'min_bernstein_directed_lower':str(smallest),
              'max_bernstein_directed_upper':str(biggest),
              'n_bernstein_coeff':len(allc),
              'shell_positive':True,
              'seven_finite_delta0p01_endpoints_certified':sample,
              'source_relative_hist_max_error_so_far':maxrel}
        if ch in 'AC':
            assert status,(ch,'radial global failed',lo(smallest))
            # Certified whole domain: on β<α distance drops with β; β>α rises.
            # Positive p,q follows positivity of source shell means.
        else:
            vH=pq(H,ONE/20,ZERO)
            vQ=pq(Q,ONE/20,ZERO)
            # β=0, alpha=.05, H<0 means D^2 increases approaching alpha, violating radial criterion.
            diag['H_at_alpha0p05_beta0_directed']=end(vH)
            diag['radial_counterexample_at_alpha0p05_beta0']=vH.b<0
            assert vH.b<0,(ch,'B expected nonmonotonic left interval')
        print(ch, 'positive universal radial=',status,'min Bernstein=',lo(smallest),'max=',hi(biggest),flush=True)
        res[ch]=diag
    assert maxrel<1e-11
    out={'return_id':'M13-ROT40-SOURCE-DIRECT-UNIVERSAL-FIVE-MASK-RADIAL-MONOTONICITY-AC-001_20261026',
      'N':N,'masks':KS,'alpha_domain':['0','1/5'],'source_provenance':'15 source-direct Fourier quartic coefficient outward enclosures, mpmath.iv 45 dps, retained helper-matching code ROT33',
      'known_model':'fixed Fourier source generators, puretrace ambient h, 2nd-order stencil, E_lin(alpha), TT; one unknown common positive energy gain across masks; overlap covariance from independent voxel energy noise',
      'algebra':'H=2p_beta*q-p*q_beta, p=<shell(alpha),shell(beta)>_W, q=||shell(beta)||_W²; H=(beta-alpha)*Q. Positive (-Q) means D²(alpha,beta) strictly decreases for beta<alpha and increases for beta>alpha. The quotient is polynomial due to H(alpha,alpha)=0.',
      'proof_type':'source coefficient outward interval; 2D tensor Bernstein positive coefficient signs for full alpha-beta square; assumes sound mp.iv and source-code-to-runtime functional match',
      'cases':res,'max_45_frozen_RMS_relative_error':maxrel,
      'results':'A,C radial monotonicity for ALL alpha,beta∈[0,.2], and every delta>0 with valid alternative, exact full-five global minimizer belongs to nearest legal endpoint alpha±delta; B FAILS radial monotonicity, no universal B global minimizer proof',
      'negative_knowledge':['Neither exact historical runtime nor original byte-exact source available','Full5 all-alpha global argmin not proved for channel B; do not infer from numeric scan','No empirical noise model, no physical interpretation or novelty claims','No formal proof assistant; interval arithmetic trust hypothesis']}
    fn=ROOT/'IW_M13_ROT40_source_direct_radial_certificate_20261026.json';fn.write_text(json.dumps(out,sort_keys=True,ensure_ascii=False,indent=2)+'\n')
    print('ROT40 PASS; 45/45 history;',fn,flush=True)
if __name__=='__main__':run()