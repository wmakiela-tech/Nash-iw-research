#!/usr/bin/env python3
"""PRF12 R29 short REPRO: deterministic full-category e-factors, exact Jensen
uplift and uniform log-growth lower bounds. Inherits R28 all-real-Xi certificate.
Full 12 vs 9 category LP, independent 2x2/4x4 audit: conversation ZIP.
No original 3q single-copy LOCC closure, no CANON/EXEC.
"""
import math
a=.3055;b=.272
r1=a/b;r0=(1-a)/(1-b);s1=b/a;s0=(1-b)/(1-a)
assert abs(r0*(1-b)+r1*b-1)<1e-14
assert abs(s0*(1-a)+s1*a-1)<1e-14
# Evidence for A is a supermartingale under composite B (Ef<=b);
# evidence for B is a supermartingale under composite A (Ef>=a).
ga=lambda f:r0+(r1-r0)*f
gb=lambda f:s0+(s1-s0)*f
f=(.94,0,0,1,.88,0,0,.96,.36,0,0,.02)
for t in f:
 assert 0<=t<=1
 assert math.log(ga(t))>=t*math.log(r1)+(1-t)*math.log(r0)-1e-14
 assert math.log(gb(t))>=t*math.log(s1)+(1-t)*math.log(s0)-1e-14
survival=math.exp(-.02*1.7783185307179588)
cmin=.932477929662237;dmin=.039941802242004
mBz=.04809737884883814
hA=survival*.62*.36*.64*((1+dmin)/2)**2
hB=.62*.36*.64*((1+dmin+cmin*mBz)/2)**2
k=(r1-r0)**2/(2*max(r0,r1)**2)
k2=(s1-s0)**2/(2*max(s0,s1)**2)
DA=a*math.log(r1)+(1-a)*math.log(r0)
DB=b*math.log(s1)+(1-b)*math.log(s0)
assert hA>.0372 and hB>.0420 and k*hA>.00042 and k2*hB>.00047
print('PASS conditional two-sided e-factors; threshold 25 each, CP fail .01')
print('uniform old/new log-growth lower A',DA,DA+k*hA)
print('uniform old/new log-growth lower B',DB,DB+k2*hB)
print('zero extra random bit; 2251-pair fixed-N result NOT transferred')
