#!/usr/bin/env python3
"""PRF12 R17 reproducible source-specific X/Y witness and Cauchy error control.
NumPy + SciPy. Ideal idle storage exact; active pulse perturbation is an UPPER
BOUND, not a device simulation; full LOCC closure gap is OPEN.
"""
import math
import numpy as np
from scipy.stats import binom
from scipy.linalg import expm
I=np.eye(2,dtype=complex)
X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
S=np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]],complex)
def t3(a,b,c):return np.kron(np.kron(a,b),c)
def same(A):return t3((I+A)/2,(I+A)/2,(I+A)/2)+t3((I-A)/2,(I-A)/2,(I-A)/2)
def axis(a):return math.cos(a)*X+math.sin(a)*Y
def event(eps):return (same(X)+same(axis(math.pi/2+eps)))/2
def rho(d,phase):return (I+d*(math.cos(phase)*X+math.sin(phase)*Y))/2
def H(z):return z/math.pi*math.log1p(z**-2)+(2/math.pi)*math.atan(z)
def stats(q,kT,tauT,eps):
    x=math.exp(-q)
    d=[math.exp(-2*kT/3),math.exp(-kT/3),1]
    s=sum(d[i]*d[j] for i in range(3) for j in range(i+1,3))
    pa=.25+s/8;pb=.25+x*x*s/8
    z=3*q*tauT
    an=s/8*(abs(math.sin(eps))+x*x*math.sin(eps)**2)
    avg=pa-pb-H(z)-z-6*kT*tauT-an
    conf=lambda a:pa-pb-z/math.tan(math.pi*a/2)-z-6*kT*tauT-an
    return pa,pb,avg,conf(.01),conf(.05),d,s
def sample_counts(a,b):
    for n in range(1,1000):
        k=math.ceil(n*math.log((1-b)/(1-a))/(math.log(a/b)+math.log((1-b)/(1-a)))-1e-12)
        ea=binom.cdf(k-1,n,a);eb=binom.sf(k-1,n,b)
        if (ea+eb)/2<.05:avg=n;break
    for n in range(1,1000):
        k=math.ceil(n*math.log((1-b)/(1-a))/(math.log(a/b)+math.log((1-b)/(1-a)))-1e-12)
        if max(binom.cdf(k-1,n,a),binom.sf(k-1,n,b))<.05:return avg,n
def run():
    rng=np.random.default_rng(17)
    for kT in (0,.1,.3,1.2):
      for q in (.05,1/3,.7,1.4):
        x=math.exp(-q)
        _,_,_,_,_,d,s=stats(q,kT,.001,0)
        E=event(0)
        for phi in rng.uniform(-400,400,30):
            A=t3(*[rho(v,phi) for v in d])
            assert abs(np.trace(E@A).real-(.25+s/8))<1e-13
        for eps in (-.1,-.02,0,.015,.1):
          F=event(eps)
          for phi in (-3,-.91,0,.23,1.51,3):
            A=t3(*[rho(v,phi) for v in d])
            expect=.25+s/8*(1-math.sin(eps)*math.sin(2*phi-eps))
            assert abs(np.trace(F@A).real-expect)<1e-13
          B=t3(*[rho(x*v,0) for v in d])
          expect=.25+s*x*x/8*(1+math.sin(eps)**2)
          assert abs(np.trace(F@B).real-expect)<1e-13
    a,b,avg,c01,c05,_,_=stats(1/3,.3,.001,.02)
    assert abs(avg-.13583298559024673)<1e-13
    assert abs(c01-.07721047789912257)<1e-13
    assert sample_counts(a,b)==(119,121)
    print('exact 8x8 storage/phase/angle and binomial tests PASS')
    print('pA_ref',a,'pB_ref',b,'one_run_averaged_lower_gap',avg)
    print('single Xi persisted: high-confidence gaps tail01',c01,'tail05',c05)
    print('no source-averaged iid claim for persistent Xi')
if __name__=='__main__':run()
