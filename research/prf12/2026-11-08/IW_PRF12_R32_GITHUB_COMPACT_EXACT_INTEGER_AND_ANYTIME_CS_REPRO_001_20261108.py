#!/usr/bin/env python3
"""PRF12 R32 COMPACT: exact integer Beta-CS boundary and binomial tails.
Full source-ON all-real-Xi mpmath.iv and independent 2x2/4x4 audit are
in the conversation ZIP, NOT executed by this compact mirror.
Counts are SYNTHETIC, Beta priors PREDECLARED, source hazard latent-Xi conditioned.
No real hardware, NO_CANON/NO_EXEC, original 3-qubit LOCC closure OPEN.
"""
import math

# Each tuple: (reference sample size, positive count, beta shape A, beta B,
# endpoint numerators with exact denominator 10^12).
cases=[
 ("uniform-0",46000,45540,1,1,987548070706,992109743728),
 ("uniform-1",69000,3705,1,1,49689260307,57899337470),
 ("predeclared-0",46000,45540,9900,100,988283083408,991541990495),
 ("predeclared-1",69000,3705,540,9460,50695035617,56805571466)]
def boundary_outside_mixture_CS(n,k,A,B,P,Q=10**12):
    # M_n(p)=((A)_k (B)_(n-k))/((A+B)_n p^k(1-p)^(n-k)).
    # Require M_n(p)>200 at the endpoint: all integers, no SciPy beta CDF.
    x=math.factorial(A+k-1)//math.factorial(A-1)
    y=math.factorial(B+n-k-1)//math.factorial(B-1)
    z=math.factorial(A+B+n-1)//math.factorial(A+B-1)
    return (x*y)*pow(Q,n)>200*z*pow(P,k)*pow(Q-P,n-k)
for name,n,k,A,B,l,u in cases:
    assert l/10**12<k/n<u/10**12
    assert boundary_outside_mixture_CS(n,k,A,B,l)
    assert boundary_outside_mixture_CS(n,k,A,B,u)
    print(name,'exact OUTER Beta-mixture CS endpoints PASS')

def binomial_cdf_integer(n,k,P,Q=100000):
    t=pow(Q-P,n);c=t
    for i in range(k):
        t,rem=divmod(t*(n-i)*P,(i+1)*(Q-P))
        assert rem==0
        c+=t
    return c,pow(Q,n)
# a,b rational safe source bounds inherited from FULL 7001-node all-Xi ZIP.
for mode,N,K,A,B in [
    ("uniform",1725,502,31022,27188),
    ("predeclared",1670,486,31054,27157)]:
    Aerr,den=binomial_cdf_integer(N,K-1,A)
    Bcdf,den2=binomial_cdf_integer(N,K-1,B)
    assert den==den2
    assert 25*Aerr<den and 25*(den-Bcdf)<den
    print(mode,'N=',N,'K>=',K,'both science errors EXACTLY <1/25',
          'reference failure <=.01, familywise wrong declaration <=.05')
print('R32 PASS scalar exact-integer witnesses; FULL global-Xi source certificate in ZIP')
