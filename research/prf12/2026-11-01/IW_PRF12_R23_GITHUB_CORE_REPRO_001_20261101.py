#!/usr/bin/env python3
"""PRF12 R23 compact independent core. NumPy/SciPy only.
The FULL mpmath.iv all-xi certificates and density audit are in R23 ZIP.
NO source-reset-within-pair; NO hardware or original 3q-LOCC claim.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.stats import binom
D=np.diag([1.,1.,0.]);ez=np.array([0.,0.,1.])
ex=np.array([1.,0.,0.]);ey=np.array([0.,1.,0.])
w=np.array([.18,.20,.62])
def cr(a):return np.array([[0,-a[2],a[1]],[a[2],0,-a[0]],[-a[1],a[0],0.]])
def angles(mode):
 if mode=='rect':return [math.pi/2]
 k=math.asin(math.sin(math.pi/4)/2)
 return [2*math.pi+math.pi/4-k,2*math.pi-2*k,math.pi/4-k]
def prepare_B(mode,axis,sign=1,v=ez):
 a=angles(mode)
 for j,theta in enumerate(a):
  direction=sign*(1 if j%2==0 else -1)*10*axis
  v=expm((cr(direction)-D)*(theta/10))@v
 return v
def prob_B(mode):
 v=prepare_B(mode,ey);v=expm(-.5*D)@v
 outputs=np.array([prepare_B(mode,ey,-1,v)[2],
                   prepare_B(mode,ex, 1,v)[2],v[2]])
 return .5+.5*w@(outputs**2)
def trial(N,a,b):
 u=math.log(a/b);v=math.log((1-b)/(1-a))
 k=math.ceil(N*v/(u+v)-1e-12)
 return k,float(binom.cdf(k-1,N,a)),float(binom.sf(k-1,N,b))
for mode,N,a,b,expected in [
 ('rect',1075,.576,.526,.5252387409109164),
 ('corpse',1134,.553,.504,.5026455303750631)]:
 p=prob_B(mode)
 assert abs(p-expected)<1e-12
 k,ea,eb=trial(N,a,b)
 assert max(ea,eb)<.05
 print(mode,'pB',p,'certified pA>=',a,'chosen pB<=',b,
       'N',N,'K',k,'error_A',ea,'error_B',eb)
 assert all(max(trial(n,a,b)[1:])>=.05 for n in range(1,N))
print('PASS exact source-B Bloch and all binomial thresholds')
print('GLOBAL all-xi enclosure requires full mpmath.iv reproducer in ZIP')
