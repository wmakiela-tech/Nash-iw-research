#!/usr/bin/env python3
"""M14 ROT020 independent public stdlib rational witness; conditional synthetic source."""
from fractions import Fraction as F
v,d,E,bmax=F(1,2),F(1,5),F(1,10),F(1,20)
w=[F(7,40),F(7,20),F(7,40)]
x1,x2=F(1),F(2)
def K(z):return 1/(z*z+v)
def h(z):return 2*(3*z*z-v)/(z*z+v)**3
def m(sign,x,B,e=F(0),weights=w,back=(F(31,10),F(29,10))):
 return back[0 if sign==-1 else 1]-sum((a*K(x-e-sign*B-j*d) for j,a in zip([-1,0,1],weights)),F(0))
def T(B,e=F(0),weights=w):
 return m(-1,x1,B,e,weights)-m(1,x1,B,e,weights)-m(-1,x2,B,e,weights)+m(1,x2,B,e,weights)
a=x1-E-bmax-d;b=x2+E+bmax+d
hmin=min(h(a),h(b));L=2*(x2-x1)*sum(w)*hmin
assert hmin==F(2056640000,13980103929)
assert L==F(2879296000,13980103929)
assert T(F(1,20))==F(3682854498032917036928,74034073127208391069455)
for ee in [-E,F(0),E]:
 for B in [-bmax,F(0),bmax]:
  val=T(B,ee)
  assert (val>0)==(B>0) and (val<0)==(B<0)
  assert abs(val)>=L*abs(B)
# INDEPENDENT GAINS & OFFSETS, identical RELATIVE shape, exact 2-tone full alias.
shape=[F(1,4),F(1,2),F(1,4)]
for sign,base in [(-1,F(31,10)),(+1,F(29,10))]:
 r=lambda x,B:sum((q*K(x-sign*B-j*d) for j,q in zip([-1,0,1],shape)),F(0))
 old=[base-sum(w)*r(x,F(0)) for x in [x1,x2]]
 p,q=r(x1,bmax),r(x2,bmax)
 gain=(old[1]-old[0])/(p-q); beta=old[0]+gain*p
 assert gain>0 and beta>gain/v
 assert [beta-gain*p,beta-gain*q]==old
print("M14 ROT020 PUBLIC Fraction PASS: two-tail sign and exact calibration counterexample")
