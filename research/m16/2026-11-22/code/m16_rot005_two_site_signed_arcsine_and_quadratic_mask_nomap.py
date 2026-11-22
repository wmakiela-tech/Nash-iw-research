#!/usr/bin/env python3
"""M16 ROT005, source-conditional two-site sign test and quadratic-mask no-map.
B/Bpi: M16 ROT004 permutation of Geeky-S12 ROT038 synthetic Gaussian noise.
Not original M13 tensor RMS hardware, not a sample-size optimality claim.
"""
from fractions import Fraction
import json
import numpy as np
import mpmath as mp
mp.mp.dps=90

B={'beta0':Fraction(1), 'x':Fraction(1,20), 'y':Fraction(3,100),
'z':Fraction(1,25),'xy':Fraction(1,30),'xz':Fraction(13,300),
'yz':Fraction(7,300),'body':Fraction(2,25)}
Bp=dict(B)
Bp['x'],Bp['y']=B['y'],B['x']
Bp['xz'],Bp['yz']=B['yz'],B['xz']
assert sum((B[k] for k in B if k!='beta0'),Fraction(0))==Fraction(3,10)
assert sum((Bp[k] for k in Bp if k!='beta0'),Fraction(0))==Fraction(3,10)
rB=B['x']/2
rP=Bp['x']/2
assert (rB,rP)==(Fraction(1,40),Fraction(3,200))
frac=lambda q:mp.mpf(q.numerator)/q.denominator
pB=mp.mpf('.5')+mp.asin(frac(rB))/mp.pi
pP=mp.mpf('.5')+mp.asin(frac(rP))/mp.pi
gap=pB-pP
assert gap>0

# Independent 1D orthant integral, not reusing the inverse sine formula.
def p_direct(r):
    r=frac(r)
    phi=lambda x:mp.exp(-x*x/2)/mp.sqrt(2*mp.pi)
    Phi=lambda x:(1+mp.erf(x/mp.sqrt(2)))/2
    return 2*mp.quad(lambda x:phi(x)*Phi(r*x/mp.sqrt(1-r*r)),[0,1,4,mp.inf])
assert abs(p_direct(rB)-pB)<mp.mpf('1e-55')
assert abs(p_direct(rP)-pP)<mp.mpf('1e-55')

gates={}
for alpha in (mp.mpf('.05'),mp.mpf('.01')):
    # Hoeffding: each conditional error <= exp(-n gap^2 / 2)
    nreal=2*mp.log(1/alpha)/gap**2
    n=int(mp.floor(nreal))+1
    assert mp.exp(-n*gap**2/2)<alpha<mp.exp(-(n-1)*gap**2/2)
    gates[str(alpha)]={'n_sufficient_not_sharp':n,
                      'real_threshold':mp.nstr(nreal,50)}
assert [gates[k]['n_sufficient_not_sharp'] for k in ('.05','.01')]==[591093,908653]

# Gains can depend on latent observations and vary SEPARATELY by channel.
raw=np.random.default_rng(20261122).normal(size=(100000,2))
x,y=raw[:,0],raw[:,1]
gx=np.exp(2*np.tanh(y)+np.tanh(x*y))
gy=np.exp(-2*np.tanh(x)+np.tanh(x*y))
assert np.array_equal((x*y)>0,((x*gx)*(y*gy))>0)

# Source ROT012's positive F2 vs its axis-swap: SIX QUADRATIC,
# not just the SIX LINEAR, cubical mask observations remain identical,
# whereas the four mode Fourier crossratio is inverted.
u=np.arange(41)
c20=np.cos(2*np.pi*20*u/41);c7=np.cos(2*np.pi*7*u/41)
F=1+(1/25)*(1.5*c20[:,None,None]+.5*c20[None,:,None]+
             c7[:,None,None]+c7[None,:,None])+np.zeros((41,41,41))
Fpi=np.swapaxes(F,0,1)
maskerr=max(abs(np.mean(F[t:41-t,t:41-t,t:41-t]**2)-
                np.mean(Fpi[t:41-t,t:41-t,t:41-t]**2))
            for t in (0,2,3,4,5,6))
def C(field):
    z=np.fft.fftn(field)
    return (abs(z[20,0,0])**2*abs(z[0,7,0])**2/
           (abs(z[0,20,0])**2*abs(z[7,0,0])**2))
c1,c2=C(F),C(Fpi)
assert np.min(F)>.84 and maskerr<1e-13
assert abs(c1-9)<1e-12 and abs(c2-1/9)<1e-13

result=dict(return_id='M16_ROT005_SOURCE_TWO_SITE_ARCSINE_AND_QUADRATIC_MASK_NOMAP',
rho_B=str(rB),rho_Bpi=str(rP),pB=mp.nstr(pB,75),
pBpi=mp.nstr(pP,75),gap=mp.nstr(gap,75),
threshold=(mp.nstr((pB+pP)/2,60)),Hoeffding_sufficient=gates,
adaptive_separate_positive_gain_sign_pathwise_PASS=True,
quadratic_mask_swap_witness=dict(max_error=float(maskerr),
C_F=float(c1),C_swap_F=float(c2),F_min=float(np.min(F))),
single_signed_site_marginal_equal='N(0,1)',
status='SOURCE_CONDITIONAL / NO_SHARP_BINOMIAL_FIRST_N / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN')
print(json.dumps(result,indent=2,ensure_ascii=False))
