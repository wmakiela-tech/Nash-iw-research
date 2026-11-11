#!/usr/bin/env python3
"""DAX-S8 ROT010 public exact massive 4e endpoint and charge-orbit control.
Non-QED kinematics only; no native MadGraph or physical DPP differential spectrum.
"""
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
from itertools import product
import json

getcontext().prec=75
E=D('1436554'); eps=D('0.07818527068831995'); m=D('0.51099895')
Q=E+eps; s=4*E*eps; W=s.sqrt()
h=(s-8*m*m)/(2*W)
p=((s-16*m*m)*(s-4*m*m)).sqrt()/(2*W)
gamma=Q/W; beta=(E-eps)/Q
assert W>5*m and gamma*m>h
L=gamma*(h-beta*p); U=gamma*(h+beta*p)
Lstable=gamma*(m*m/(h+p)+(1-beta)*p)
assert abs(L-Lstable)<D('1e-60')
assert abs(h*h-p*p-m*m)<D('1e-60')
assert m<L<U<Q
for sigma in (-1,1):
    # Selected 4-vector plus three identical recoil 4-vectors, in COM.
    e3=(W-h)/3
    p3=-D(sigma)*p/3
    assert abs(e3*e3-p3*p3-m*m)<D('1e-60')
    en1=gamma*(h+beta*D(sigma)*p)
    pz1=gamma*(D(sigma)*p+beta*h)
    en3=gamma*(e3+beta*p3)
    pz3=gamma*(p3+beta*e3)
    assert abs(en1*en1-pz1*pz1-m*m)<D('1e-50')
    assert abs(en3*en3-pz3*pz3-m*m)<D('1e-50')
    assert abs(en1+3*en3-Q)<D('1e-60')
    assert abs(pz1+3*pz3-(E-eps))<D('1e-60')
    assert abs(en1-(L if sigma==-1 else U))<D('1e-60')

id4=(0,1,2,3)
generators=((1,0,2,3),(0,1,3,2),(2,3,0,1))
def compose(a,b): return tuple(a[b[i]] for i in range(4))
group={id4}
while True:
    new=group|{compose(g,t) for g in group for t in generators}
    if new==group: break
    group=new
assert len(group)==8
base=(F(3,10),F(3,10),F(1,5),F(1,5))
points=[tuple(base[g[i]] for i in range(4)) for g in group]
means=[sum(row[i] for row in points)/len(points) for i in range(4)]
assert means==[F(1,4)]*4
cov=[[sum((row[i]-means[i])*(row[j]-means[j]) for row in points)/len(points)
      for j in range(4)] for i in range(4)]
v,a,b=cov[0][0],cov[0][1],cov[0][2]
assert (v,a,b)==(F(1,400),F(1,400),-F(1,400))
assert v+a+2*b==0 and a!=b
# The physical on-shell COM realization is two transverse +/- momentum pairs.
EA=D(3)*W/10; EB=W/5
assert (EA*EA-m*m)>0 and (EB*EB-m*m)>0
assert 2*EA+2*EB==W
print(json.dumps({
    'status':'PASS_EXACT_MASSIVE_SUPPORT_AND_CHARGE_ORBIT',
    'R68_selected_lepton_lab_min_MeV':str(L),
    'R68_selected_lepton_lab_max_MeV':str(U),
    'R68_allowed_range_ratio':str(U/L),
    'charge_orbit_size':len(group),
    'mean_energy_over_total':'1/4',
    'variance_over_total_squared':str(v),
    'same_charge_covariance_over_total_squared':str(a),
    'opposite_charge_covariance_over_total_squared':str(b),
    'identity':'variance+same_charge_cov+2*opposite_charge_cov=0',
    'scope':'NO_QED_AMPLITUDE / NO_RATE / NO_PHYSICAL_DEPOSITION / NO_CANON'
},indent=2,sort_keys=True))
