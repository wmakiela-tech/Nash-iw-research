#!/usr/bin/env python3
"""M16 ROT006, source-conditional robust sign observer; no physical sensors."""
from fractions import Fraction
import mpmath as mp
import numpy as np
import json
mp.mp.dps=100
rB,rP=Fraction(1,40),Fraction(3,200)
f=lambda q: mp.mpf(q.numerator)/q.denominator
pB=mp.mpf('.5')+mp.asin(f(rB))/mp.pi
pP=mp.mpf('.5')+mp.asin(f(rP))/mp.pi
gap=pB-pP
eta_star=gap/2
pbar=(pB+pP)/2
assert eta_star>0
# Exact legal alias at eta=eta_star: under B 1->0, under Bpi 0->1.
a=eta_star/pB
b=eta_star/(1-pP)
assert 0<a<1 and 0<b<1
assert abs(pB*(1-a)-pbar)<mp.mpf('1e-90')
assert abs(pP+(1-pP)*b-pbar)<mp.mpf('1e-90')
assert abs(pB*a-eta_star)<mp.mpf('1e-90')
assert abs((1-pP)*b-eta_star)<mp.mpf('1e-90')
# With conditional bit flip probability <=eta given every past history,
# and independent clean Bernoulli(pX) per shot, the midpoint empirical
# test has each error <= exp(-2*n*(eta_star-eta)**2), eta<eta_star.
samples=[]
for es in ('0','.0001','.0005','.001','.0015'):
    eta=mp.mpf(es);margin=eta_star-eta
    assert margin>0
    d={'eta':es}
    for alpha in ('.05','.01'):
        A=mp.mpf(alpha)
        bound=mp.log(1/A)/(2*margin*margin)
        n=int(mp.floor(bound))+1
        assert mp.exp(-2*n*margin*margin)<A
        assert mp.exp(-2*(n-1)*margin*margin)>A
        d['n_sufficient_error_'+alpha]=n
    samples.append(d)
assert [d['n_sufficient_error_.05'] for d in samples]==[591093,672990,1256399,4275765,177452948]
assert [d['n_sufficient_error_.01'] for d in samples]==[908653,1034550,1931392,6572892,272788403]
# Independent 80-dps outward interval confirmation of critical eta
# via asin(x)=atan2(x,sqrt(1-x*x)) for positive small x.
iv=mp.iv;iv.dps=80
arcs=lambda x:iv.atan2(x,iv.sqrt(1-x*x))
eiv=(arcs(iv.mpf(1)/40)-arcs(iv.mpf(3)/200))/(2*iv.pi)
assert eiv > iv.mpf('.00159')
assert eiv < iv.mpf('.00160')
for es,n95,n99 in [('0',591093,908653),('.001',4275765,6572892),('.0015',177452948,272788403)]:
    mar=eiv-iv.mpf(es)
    for n,alph in [(n95,'.05'),(n99,'.01')]:
        assert iv.exp(-2*n*mar*mar) < iv.mpf(alph)
        assert iv.exp(-2*(n-1)*mar*mar) > iv.mpf(alph)
# Positive per-channel calibration plus non-Gaussian common volatility
# leave clean signs identically unchanged, even if gains adapt to data.
rg=np.random.default_rng(16006)
core=rg.multivariate_normal([0,0],[[1,float(f(rB))],[float(f(rB)),1]],size=200000)
S=rg.choice([.5,1.5],size=len(core))
X=core*np.sqrt(S)[:,None]
gx=np.exp(2*np.tanh(core[:,1])+np.tanh(np.roll(core[:,0],1)))
gy=np.exp(-2*np.tanh(core[:,0])+np.tanh(S))
assert np.array_equal(core[:,0]*core[:,1]>0,(X[:,0]*gx)*(X[:,1]*gy)>0)
print(json.dumps({
  'return_id':'IW_M16_ROT006_SOURCE_B_BPI_SHARP_ADAPTIVE_SIGN_BIT_FLIP_RADIUS',
  'pB':mp.nstr(pB,85),'pBpi':mp.nstr(pP,85),
  'gap':mp.nstr(gap,85),'eta_star':mp.nstr(eta_star,85),
  'eta_star_iv80':str(eiv),
  'least_favourable_alias_parameter':mp.nstr(pbar,60),
  'rate_B_given_clean_1':mp.nstr(a,55),
  'rate_Bpi_given_clean_0':mp.nstr(b,55),
  'sufficient_not_sharp_hoeffding_counts':samples,
  'gain_and_scale_mixture_200000_pairs':'PASS',
  'analytic_all_n_alias':'PASS',
  'limits':'MODEL_DEPENDENT_BIT_ERRORS; CONDITIONAL_HISTORY_BOUND; IID_GAUSSIAN_CORE; NO_HARDWARE, NO_NOVELTY, NO_CANON, NO_EXEC_SIGN'
},indent=2))
