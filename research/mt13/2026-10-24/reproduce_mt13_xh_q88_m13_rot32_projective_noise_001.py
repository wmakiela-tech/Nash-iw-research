#!/usr/bin/env python3
"""MT13 XH-Q88/M13-ROT32: exact positive-ray noise gates on published M13 decimal quartics.
This is a COMPANION condensed proof/numerical check. Full 3000-random + 20k-grid
suite is in the independently SHA-checked local Moderator ZIP. No DTC runtime here.
"""
import numpy as np
from scipy.optimize import minimize_scalar
G={
 31:{
 "A":[1.4352957736803108e-9,-3.6188941135989846e-10,5.54929093303773e-11,-4.9604750107845104e-12,1.6826637361246226e-13],
 "B":[9.00158383502143e-14,-4.4348529475060804e-14,4.3959298684780046e-11,-7.1981010841815505e-12,2.946829775272849e-13],
 "C":[2.345763839391682e-12,3.178047135258384e-11,2.4926375100707397e-10,-4.1463904285886896e-11,1.7063655863930431e-12]
 },41:{
 "A":[1.4829382294555582e-9,-2.10594866157198e-10,1.8086488163361196e-11,-9.184144348096345e-13,1.7840870305650078e-14],
 "B":[2.819256028822308e-14,-2.5174118330489876e-14,1.485550633961675e-11,-1.3926475619883742e-12,3.2641317949695024e-14],
 "C":[8.231147112474451e-13,1.1352793516081152e-11,8.854808605436023e-11,-8.377153395072092e-12,1.9694212505331718e-13]
 }}
def f(N,keys,a):return np.array([np.sqrt(np.polynomial.polynomial.polyval(a,G[N][k])) for k in keys])
def dist(y,g):
    s=max(0,float(y@g/(g@g)))
    return float(np.linalg.norm(y-s*g)),s
def Iperp(N,keys,a):
    F=f(N,keys,a)
    D=np.array([np.polynomial.polynomial.polyval(a,
        np.polynomial.polynomial.polyder(G[N][k]))/(2*F[i]) for i,k in enumerate(keys)])
    ort=D-F*(F@D)/(F@F)
    assert np.isclose(np.linalg.norm(ort),
        abs(F[0]*D[1]-F[1]*D[0])/np.linalg.norm(F),rtol=1e-10)
    return float(np.linalg.norm(ort))
for N in (31,41):
  for keys in [('A','C'),('A','B')]:
    y=f(N,keys,.05)
    d,s=dist(y,f(N,keys,.06))
    # Exact in-plane determinantal identity and sharp midpoint overlap
    d2=abs(np.linalg.det(np.vstack((y,f(N,keys,.06)))))/np.linalg.norm(f(N,keys,.06))
    assert abs(d-d2)<1e-14
    midpoint=(y+s*f(N,keys,.06))/2
    assert abs(np.linalg.norm(midpoint-y)-d/2)<1e-14
    assert abs(np.linalg.norm(midpoint-s*f(N,keys,.06))-d/2)<1e-14
    print('BINARY',N,keys,'d',d,'sharp_eta',d/2,'local_Iperp',Iperp(N,keys,.05))
  # The global nearest alternative is at an edge due to monotone A/C angle
  keys=('A','C');y=f(N,keys,.05)
  dmin=min(dist(y,f(N,keys,a))[0] for a in (.04,.06))
  scan=np.r_[np.linspace(0,.04,201),np.linspace(.06,.2,501)]
  assert min(dist(y,f(N,keys,a))[0] for a in scan)>=dmin-1e-13
  print('GLOBAL_DELTA_0.01',N,dmin/2)
for N,a2 in ((31,.0004926324643493085),(41,.0014253138279789676)):
  d_ab,_=dist(f(N,('A','B'),0),f(N,('A','B'),a2))
  d_ac,_=dist(f(N,('A','C'),0),f(N,('A','C'),a2))
  assert d_ab<1e-15 and d_ac>1e-9
  print('FOLD',N,d_ab,d_ac)
  v0=f(N,('A','C'),.05);v1=f(N,('A','C'),.051)
  ratio_gain=(v0[0]/v0[1])/(v1[0]/v1[1])
  assert 1<ratio_gain<1.01
  print('GAIN_0.001_ALPHA_CONFUSION',N,ratio_gain)
  # An INDEPENDENT B channel is a source-model falsifier
  y=f(N,('A','B','C'),.05);y[1]*=1.05
  res=minimize_scalar(lambda a:dist(y,f(N,('A','B','C'),a))[0],
      bounds=(0,.2),method='bounded',options={'xatol':1e-14})
  assert res.success and res.fun>1e-9
  print('THIRD_CHANNEL_B_GAIN_5PERCENT',N,res.fun,res.x)
d=.005
err=np.log((1+d)/(1-d))
assert .0124<err/.8<.0126
print('RELATIVE_NOISE_LOG_RATIO_GATE',err,'alpha_conservative',err/.8)
print('PASS exact source-decimal projective-margin and third-channel checks; no physical upgrade')