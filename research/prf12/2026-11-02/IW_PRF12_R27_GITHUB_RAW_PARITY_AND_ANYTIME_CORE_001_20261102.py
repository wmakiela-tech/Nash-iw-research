#!/usr/bin/env python3
"""PRF12 R27 short runnable reproducer.
Complete 7001-node mpmath.iv source control and 2x2/4x4 independent
matrix audit are in the R27 ZIP; this short mirror checks finite CP
calibration, conditional Bernoulli dominance, and anytime e-values.
SYNTHETIC calibration counts, NO experimental data or original LOCC gap.
"""
import math
from scipy.stats import beta,binom
n0,k0,n1,k1=46000,45540,69000,3705
alpha=.005
def cp(n,k):
    lo=0. if k==0 else beta.ppf(alpha/2,k,n-k+1)-1e-12
    hi=1. if k==n else beta.ppf(1-alpha/2,k+1,n-k)+1e-12
    return max(0.,lo),min(1.,hi)
l0,u0=cp(n0,k0);l1,u1=cp(n1,k1)
cl,cu=l0-u1,u0-l1
dl,du=l0+l1-1,u0+u1-1
assert cl>abs(du)
# A global no-reset lower .56661431766 and B upper .52895685259
# follow from the ALL-REAL-XI interval+tail proof in the ZIP.
s=math.exp(-.02*1.7783185307179588)
a_lower=s*.5666143176611008+(1-s)*(.5-.5*cu**2)
b_upper=.5289568525891072
a,b=.548,.529
assert a_lower>a and b_upper<b
N,k=8497,4576
eA=binom.cdf(k-1,N,a)
eB=binom.sf(k-1,N,b)
assert max(eA,eB)<.04
# Composite-null one-step e-values for any conditional p in [0,b] (B)
# or [a,1] (A). Thus optional stopping is valid by Ville's inequality.
assert b*(a/b)+(1-b)*((1-a)/(1-b))<=1+1e-14
assert a*(b/a)+(1-a)*((1-b)/(1-a))<=1+1e-14
print('CP_99',cl,cu,dl,du)
print('safe pA>=',a,'pB<=',b,'pairs',N,'choose A if K>=',k)
print('conditional tails',eA,eB,'total wrong <=.01+.04')
print('readouts',115000+2*N,'gamma_time',11500+N*1.8283185307179588)
print('PASS; no full-quartet minimax optimality or hardware evidence')
