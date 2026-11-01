#!/usr/bin/env python3
"""M14 ROT024 public stdlib replay; n=2 NC-NUM-005 only."""
from math import sqrt,log,exp
root=sqrt(34)
alpha=(5+root)/10
beta=(root-5)/10
mu=-13/5+root/2
t=log(51*beta/alpha)/5
U,V=exp(-t/10),exp(-51*t/10)
r=alpha*U-beta*V
ell=-beta*U+alpha*V
kappa=3*(U-V)/10
detE=U*V
ucr=(r-1)/(detE-ell)
def readout_norm(m):
 return kappa*sqrt((r**(2*m)-1)/(r*r-1))
assert mu>0 and r>1
assert abs(r-1.033277247747221)<1e-12
assert abs(t-0.272846861447588)<1e-12
assert abs(ucr-0.622014181832008)<1e-11
assert readout_norm(8)<1.0858
assert readout_norm(15)<1.0858<readout_norm(16)
assert readout_norm(16)>1.08661357036757
assert (1-r+.001*(detE-ell))<0
assert (1-r+.9*(detE-ell))>0
print('M14 ROT024 PUBLIC PASS')
print('tstar',t,'rho',r,'ucrit',ucr)
print('m8',readout_norm(8),'m15',readout_norm(15),'m16',readout_norm(16))
