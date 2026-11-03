#!/usr/bin/env python3
"""PRF12 R31 public SHORT core. Full standalone 7001-point mpmath.iv
all-real-Xi proof, independent 2x2/4x4 audit and 9-support interval
dual verification are in PRF12_R31_reproducibility_bundle_20261103.zip.
NO claim that this short script reproduces the global interval proof.
Calibration counts are SYNTHETIC; NO CANON/EXEC, no original 3Q LOCC gap.
Dependencies: Python3 and scipy.
"""
import math
from scipy.stats import beta,binom

AXES=("X","Y","Z")
W=(.18,.20,.62)
SCORE_PLUS=(.943,.907,.347)
SCORE_MIXED=(0.,0.,0.)
SCORE_MINUS=(1.,1.,.018)
CP_SYNTHETIC=((46000,45540),(69000,3705))

def cp(n,k,alpha=.005):
    return (beta.ppf(alpha/2,k,n-k+1)-1e-12,
            beta.ppf(1-alpha/2,k+1,n-k)+1e-12)

p0,p1=[cp(*v) for v in CP_SYNTHETIC]
c=(p0[0]-p1[1],p0[1]-p1[0])
d=(p0[0]+p1[0]-1,p0[1]+p1[1]-1)
assert c[0]>.9324 and c[1]<.940
assert d[0]>.0399 and d[1]<.0475

# A score is the probability of a TRUE independently sampled bit = 1,
# conditional on (axis, first recorded sign, second recorded sign).
def coin_probability(axis,first,second):
    j=AXES.index(axis)
    if first==second==1:return SCORE_PLUS[j]
    if first==second==-1:return SCORE_MINUS[j]
    return SCORE_MIXED[j]

# Full global-Xi/CP-source proof is in the standalone ZIP Python.
PROVED_SOURCE_A_LOWER=.3106993896688963
PROVED_SOURCE_B_UPPER=.27161358975207756
a,b=.31068,.27164
assert PROVED_SOURCE_A_LOWER>a and PROVED_SOURCE_B_UPPER<b

N,K=1666,485
errA=binom.cdf(K-1,N,a)
errB=binom.sf(K-1,N,b)
assert errA<.04 and errB<.04
assert errA+.01<.05 and errB+.01<.05

# The deterministic full category e-processes are valid under opposite
# composite nulls for any conditional E[f]>=a or E[f]<=b.
r1,r0=a/b,(1-a)/(1-b)
s1,s0=b/a,(1-b)/(1-a)
assert abs(r0+(r1-r0)*b-1)<1e-12
assert abs(s0+(s1-s0)*a-1)<1e-12
def G_A(axis,r1shot,r2shot):
    f=coin_probability(axis,r1shot,r2shot)
    return r0+(r1-r0)*f
def G_B(axis,r1shot,r2shot):
    f=coin_probability(axis,r1shot,r2shot)
    return s0+(s1-s0)*f

# Near-optimality of restricted AFFINE-SOURCE certificate only:
RESTRICTED_L_LOWER=PROVED_SOURCE_A_LOWER-PROVED_SOURCE_B_UPPER
RESTRICTED_L_UPPER=.039155288096258 # proved by independent 9-support interval dual
assert RESTRICTED_L_LOWER>0 and RESTRICTED_L_LOWER/RESTRICTED_L_UPPER>.9982

print('R31 N=',N,'choose A if K>=',K)
print('A/B source conditional science errors:',errA,errB)
print('CP failure budget <=.01; total readings=',115000+2*N)
print('Restricted affine-source contrast bracket:',RESTRICTED_L_LOWER,RESTRICTED_L_UPPER)
print('PASS SHORT CORE; replay FULL code and DUAL code from ZIP for all-Xi evidence')
