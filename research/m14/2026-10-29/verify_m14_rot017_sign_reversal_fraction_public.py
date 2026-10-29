#!/usr/bin/env python3
"""Public standalone ROT017 fraction witness (Python standard library)."""
from fractions import Fraction as F
from math import log
G,V,BETA=F(7,20),F(1,2),F(3)
def atoms(d,sign,h):
    if not h:return [(-d,G/2),(F(0),G),(d,G/2)]
    c=F(sign,4)
    return [((c-1)*d,G*(c*c+c+F(1,2))),
            (c*d,G*(1-2*c*c)),
            ((c+1)*d,G*(c*c-c+F(1,2)))]
def ms(a):
    return [sum((w*z**i for z,w in a),F(0)) for i in range(4)]
def reading(a,x):
    return BETA-sum((w/((x-z)**2+V) for z,w in a),F(0))
for d in [F(1,3),F(1,4),F(1,5),F(1,10),F(1,20),F(1,50)]:
    for sign in (-1,+1):
        a,b=atoms(d,sign,False),atoms(d,sign,True)
        assert all(w>0 for z,w in a+b)
        assert ms(a)[:3]==ms(b)[:3]
        assert ms(b)[3]-ms(a)[3]==sign*F(9,32)*G*d**3
        for x in [-2,-1,0,1,2,3]:
            assert reading(a,F(x))>=F(8,5)
            assert reading(b,F(x))>=F(8,5)
            gap=reading(b,F(x))-reading(a,F(x))
            assert gap**2 <= ((F(1007,512)*G*d**3)**2 * F(1,V)**5)
C=F(149065203,5242880)
for d,n in [(F(1,5),158),(F(1,10),10118),(F(1,20),647569)]:
    assert float(n*C*d**6)<=log(F(4,3))
print('PASS ROT017 12 exact positive triplet witnesses and shot lower bound')
