#!/usr/bin/env python3
"""DAX-S8 ROT015: source-model angular-bin closure and synthetic POINTDATA envelope.
No actual Belle HEPData/YODA numeric rows were read. NOT a physical pion rate.
Requires scipy and mpmath. The complete full-replay controls are in local ZIP.
"""
from math import expm1, log
import mpmath as mp
from scipy.integrate import quad
import json

# Source-Born angular Eq21 closure in twelve |cos(theta*)| bins.
mp.mp.dps=50
mev_pi=mp.mpf('139.57039')
alpha=1/mp.mpf('137.035999084')
closure=[]
for W in [mp.mpf(900),mp.mpf(1200),mp.mpf(1450)]:
    s=W**2
    b=mp.sqrt(1-4*mev_pi**2/s)
    b2=b*b
    F=lambda z: ((1-b2)/(1-b2*z*z))**2+(b2*(1-z*z)/(1-b2*z*z))**2
    primitive=lambda z: z+(1-b2)**2*z/(1-b2*z*z)-(1-b2*b2)*mp.atanh(b*z)/b
    differential=lambda z: 2*mp.pi*alpha**2*b/s * F(z)
    width=mp.mpf('0.05')
    bins=[mp.quad(differential,[j*width,(j+1)*width]) for j in range(12)]
    sigma_from_12=sum(bins)
    sigma_closed=2*mp.pi*alpha**2*b/s*primitive(mp.mpf('0.6'))
    err=abs(sigma_from_12/sigma_closed-1)
    assert err<mp.mpf('1e-43')
    closure.append({'W_MeV':int(W),'angular_bins':12,'closure_relative_error':mp.nstr(err,12)})

# Conditional L-Lipschitz point data: exact sharp envelope fixture y_i=1.
E=1436554.0
T=0.07818527068831995
C=4*E*T
H=lambda w: w**3/(4*E*E*T*T)*(-log(-expm1(-(w*w/C))))
h=5.0
L=0.1 # invented, not measured, arbitrary sigma unit / MeV
K0=quad(H,800,1500,epsabs=1e-12,epsrel=1e-12)[0]
distH=0
for j in range(140):
    c=802.5+5*j
    distH+=quad(lambda w:H(w)*(c-w),c-2.5,c)[0]
    distH+=quad(lambda w:H(w)*(w-c),c,c+2.5)[0]
Klo=K0-L*distH;Khi=K0+L*distH
assert 0<Klo<K0<Khi
assert abs((Khi-K0)/K0-.125)<1e-5
print(json.dumps({
  'status':'PASS_SOURCE_BORN_ANGULAR_CLOSURE_AND_CONDITIONAL_SYNTHETIC_POINT_ENVELOPE',
  'Born_angular_fixture':closure,
  'synthetic_point_count':140,
  'synthetic_sample_values':'ALL 1.0, arbitrary cross-section units',
  'invented_L_per_MeV':L,
  'K_low':Klo,'K_nominal':K0,'K_high':Khi,
  'synthetic_relative_envelope':(Khi-K0)/K0,
  'limits':'Not Belle numeric tables, not known physical slope, not true QCD pion cross-section or PBH bound'
},sort_keys=True,indent=2))
