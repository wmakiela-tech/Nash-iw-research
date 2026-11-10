#!/usr/bin/env python3
"""DAX-S8 ROT005: exact CRPropa DPP input-domain witness and scalar thermal rate.
Source-model mathematics only: NOT compiled CRPropa, QED differential, or PBH.
"""
from fractions import Fraction as Q
from math import expm1,log,comb
import json
M=.51099895
T=.07818527068831995
ZETA3=1.2020569031595943

# k1=(3,0,0,3), k2=(2,0,0,-2), so P=(5,0,0,1).
assert Q(5)**2-Q(1)**2 == 24>16
# Four on-shell leptons have p=(5/4,+/-sqrt(1/2),0,1/4)
# or p=(5/4,0,+/-sqrt(1/2),1/4).
assert Q(5,4)**2-Q(1,2)-Q(1,4)**2==1
assert Q(5,4)*4==5 and Q(1,4)*4==1
assert (Q(3)-2)/2==Q(1,2)<1 # impossible hard lepton energy
assert 4*Q(1)*Q(5)>16 and (Q(1)-2)/2==Q(-1,2)
# src/Common.cpp interpolator returns first grid value below grid.
def interpolate(x,X,Y):
    if x<X[0]:return Y[0]
    if x>=X[-1]:return Y[-1]
    for j in range(len(X)-1):
        if X[j]<=x<X[j+1]:
            return Y[j]+(x-X[j])*(Y[j+1]-Y[j])/(X[j+1]-X[j])
assert interpolate(Q(3),[Q(1000)/Q('0.51099895'),Q(10000)/Q('0.51099895')],[7,11])==7

def integrate(f,a,b,n):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,n)))
def angle(a):
    if a>=1:return 0.
    if a<.25:
        return max(0,2*sum((-1)**k*comb(6,k)*a**k*(log(1/a) if k==2 else (1-a**(2-k))/(2-k)) for k in range(7)))
    return 2*integrate(lambda t:t*(1-a/t)**6,a,1,96)
def fraction(q,n):
    chi=4*M/(q*T)
    return integrate(lambda x:0 if x<=chi else x*x/expm1(x)*angle(chi/x),chi,120,n)/(2*ZETA3)
out={}
for label,q in [('3m',3),('1GeV',1000/M)]:
    coarse,refined=fraction(q,8192),fraction(q,16384)
    assert abs(refined-coarse)/refined<7e-7
    out[label]=refined
ratio=out['1GeV']/out['3m']
assert 6e6<ratio<6.2e6
print(json.dumps({'PASS':True,'F_3m':out['3m'],'F_1GeV':out['1GeV'],
                  'rate_ratio':ratio,
                  'scope':'Conditional hot-bath surrogate only; no native C++ and no default bug verdict'},
                 indent=2,sort_keys=True))
