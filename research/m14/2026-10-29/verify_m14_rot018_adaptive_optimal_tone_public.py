#!/usr/bin/env python3
"""M14 ROT018 public exact rational check; synthetic known pair, not sensor data."""
from fractions import Fraction as F
z,w=F(49140907,10**9),F(49140908,10**9)
def P(t):return 150*t**3-103*t**2-36*t+2
def c(t):return F(3969)*t*(2*t-1)**2/(640*(2*t+1)**7*(15*t+4))
assert P(z)>0>P(w)
assert c(F(1,20))>F(3969,235520)
assert c(F(1))==F(49,328320)
grid=2*sum((c(F(x*x)) for x in (-2,-1,0,1,2,3)),F(0))
assert grid==F(11515665443451841,18782029547400522240)
assert 12*F(49688401,20971520)==F(149065203,5242880)
g,v,d,tone=F(7,20),F(1,2),F(1,5),F(1,5)
def atoms(s,h):
 if not h:return [(-d,g/2),(F(0),g),(d,g/2)]
 a=F(s,4)
 return [((a-1)*d,g*(a*a+a+F(1,2))),(a*d,g*(1-2*a*a)),((a+1)*d,g*(a*a-a+F(1,2)))]
def absorb(a):return sum((ww/((tone-xx)**2+v) for xx,ww in a),F(0))
for s in (-1,1):
 t0,t1=absorb(atoms(s,False)),absorb(atoms(s,True))
 b0=F(3);b1=b0+t1-t0
 assert b1>2*g/v and b0-t0==b1-t1
print('PASS M14 ROT018 rational optimum bracket, grid coefficient, single-tone nuisance alias')
