#!/usr/bin/env python3
"""PRF12 R25 compact reproduction: T1+asym readout, reset hazards, Cauchy bound.
Full 2x2/4x4 independent auditing and extended reproducible script in ZIP.
Not a hardware proof or original 3-qubit LOCC closure claim.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.stats import binom

ep,em=.01,.03
T1inv,td,tr=.5,.05,.05
g=math.exp(-T1inv*td)
c=(1-ep-em)*g
d=(1-ep-em)*(1-g)+em-ep
W=(1+abs(d))/c**2
L=2*(.5+2*math.pi/20+td)+tr
T=2*(.5+2*math.pi/20+td+tr)
a0,b0=.576,.526
def Nbound(lam,floor=0.,dc=0.,dd=0.):
    a=math.exp(-lam*L)*a0+(1-math.exp(-lam*L))*floor
    eps=(dc+dd)/abs(c)
    bias=eps+eps**2/2
    D=a-b0-2*bias
    if D<=0:return None
    return math.ceil(2*W*W*math.log(20)/D**2),D
assert Nbound(0.)[0]==3397
assert Nbound(.01)[0]==5349
assert Nbound(.02)[0]==9516
assert Nbound(.02,.31)[0]==5126
assert Nbound(.02,dc=.0005,dd=.0005)[0]==11039

# Direct two-outcome detector probabilities and unbiased pair cross-moment.
for m1,m2 in [(-1.,1.),(.2,-.8),(1.,1.),(-.31,.7)]:
    exact=.5*(1+m1*m2)
    test=0.
    for r1 in (-1,1):
        for r2 in (-1,1):
            p=(1+r1*(c*m1+d))*(1+r2*(c*m2+d))/4
            score=.5*(1+(r1-d)*(r2-d)/c**2)
            test+=p*score
    assert abs(test-exact)<1e-14

def J4(z):
    return z/math.pi*math.log1p((4/z)**2)+8/math.pi*math.atan(z/4)
def diamond_upper(h,T=1.,Hmax=5.,gamma=1.):
    return min(2.,T*Hmax*(J4(gamma*h)+2*gamma*h))
for h in (.1,.02,.001,.0001,.00001):
    print('h',h,'fast-Cauchy-refresh channel diamond upper',diamond_upper(h))
assert diamond_upper(.00001)<.001
assert math.isclose(math.exp(-1/1000)**1000,math.exp(-1),abs_tol=1e-12)
print('R25 PASS c=',c,'d=',d,'W=',W,'N=',Nbound(.02),
      'N_cal_uncertain=',Nbound(.02,dc=.0005,dd=.0005))
