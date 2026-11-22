#!/usr/bin/env python3
"""M16 ROT008: independent source-only 16-Pauli SO(3) I1, stdlib only.
Reimplementation; original PRF14 ROT024 not imported. Not quantum hardware.
For expanded executed exact certificate see M16 ROT008 report/local attachment.
"""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from decimal import Decimal, localcontext, ROUND_CEILING

C=((F(0),F(9,100),F(11,100)),(F(7,100),F(0),F(1,10)),(F(8,100),F(12,100),F(0)))
S=((F(2,7),F(6,7),F(3,7)),(F(-3,7),F(-2,7),F(6,7)),(F(6,7),F(-3,7),F(2,7)))
O=[(i,j) for i in range(3) for j in range(3) if i!=j]
J=[(0,1),(0,2),(1,0),(1,2)]
def ch(v):
    x=v&1; z=(v>>1)&1
    return (1-2*z,1-2*(z^x),1-2*x)
def law(M):
    return {(v,w):(1+sum(M[i][j]*ch(v)[j]*ch(w)[i] for i,j in O))/16
            for v,w in product(range(4),repeat=2)}
def scale(q):
    return tuple(tuple(q*a for a in row) for row in C)
def tv(a,b):
    return sum((abs(a[k]-b[k]) for k in a),F(0))/2
def trans(A):return tuple(zip(*A))
def mul(A,B):
    return tuple(tuple(sum((A[i][j]*B[j][k] for j in range(3)),F(0))
                       for k in range(3)) for i in range(3))
def det(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
          - M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
          + M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
I=tuple(tuple(F(int(i==j)) for j in range(3)) for i in range(3))
assert mul(S,trans(S))==I and det(S)==1
m0,m1=law(scale(F(1))),law(scale(F(26,25)))
b,u=law(scale(F(7,2))),law(scale(F(91,25)))
for q in (m0,m1,b,u):
    assert sum(q.values())==1 and min(q.values())>0
    f={(a,c):sum((p*(1 if a==0 else ch(v)[a-1])*
                  (1 if c==0 else ch(w)[c-1]) for (v,w),p in q.items()),F(0))
       for a in range(4) for c in range(4)}
    assert f[0,0]==1
    assert sum(z==0 for z in f.values())==9
    assert sum(z!=0 for z in f.values())==7
assert (min(m0.values()),min(m1.values()),tv(m0,m1))==(F(73,1600),F(899,20000),F(171,40000))
assert (min(b.values()),min(u.values()),tv(b,u))==(F(11,3200),F(43,40000),F(1197,80000))
X=tuple(tuple(F(26,25)*x for x in row) for row in S)
assert all(sum(X[i][j]**2 for j in range(3) if i!=j)==F(6084,6125) for i in range(3))
assert all(sum(X[i][j]**2 for i in range(3) if i!=j)==F(6084,6125) for j in range(3))
a,c,d,e=X[0][1],X[0][2],X[1][0],X[1][2]
A=d*d*(1-a*a-c*c);B=a*a*(1-d*d-e*e);W=c*e
assert (W*W-A-B)**2-4*A*B==F(409983535198224,17951812744140625)>0
def sqrt_up(q):
    if q<0:raise ValueError('negative radicand')
    N=10**44;t=q.numerator*N*N
    v=isqrt(t//q.denominator)
    if v*v*q.denominator!=t:v+=1
    ans=F(v,N)
    assert ans*ans>=q
    return ans
def gap(z,eu=F(0),ec=F(0),dg=F(0)):
    lo={};hi={}
    for i,j in J:
        cb=abs(F(7,2)*C[i][j]);cu=abs(F(91,25)*C[i][j])
        mean=cu*abs(S[i][j]);delta=cu*dg
        lo[i,j]=max(F(0),mean-delta-2*eu)/(cb+2*ec+2*z)
        denom=cb-2*ec-2*z
        hi[i,j]=F(1) if denom<=0 else min(F(1),(mean+delta+2*eu)/denom)
        assert 0<=lo[i,j]<=hi[i,j]<=1
    r0=1-lo[0,1]**2-lo[0,2]**2
    r1=1-lo[1,0]**2-lo[1,2]**2
    return lo[0,2]*lo[1,2]-hi[1,0]*sqrt_up(r0)-hi[0,1]*sqrt_up(r1)
assert gap(F(56,10000))>0 and gap(F(563,100000))<0
assert gap(F(26,100000),F(145,100000),F(3,1000),F(1,1000))>F(5,100000)
# Alternative two worlds with equal FULL 9 + 9 channels.
P=((F(0),F(0),F(1)),(F(1),F(0),F(0)),(F(0),F(1),F(0)))
R=(S[1],S[2],S[0])
t=F(1,1000)
Q=((F(1),F(0),F(0)),(F(0),(1-t*t)/(1+t*t),-2*t/(1+t*t)),
   (F(0),2*t/(1+t*t),(1-t*t)/(1+t*t)))
Sp=mul(P,mul(Q,R))
assert mul(Sp,trans(Sp))==I and det(Sp)==1
Cp=tuple(tuple(F(7,2)*C[i][j]*S[i][j]/Sp[i][j] if i!=j else F(0)
               for j in range(3)) for i in range(3))
p=law(Cp)
assert min(p.values())>0 and sum(p.values())==1
assert tv(b,p)==F(41979,50199950)
def transfer(prob,rot,dx=False):
    return tuple(tuple(sum((v*ch(w)[i]*rot[i][j]*ch(a)[j] for (a,w),v in prob.items()),F(0))*
                       (1 if not dx or i==0 else -1) for j in range(3)) for i in range(3))
assert transfer(b,S)==transfer(p,Sp)
assert transfer(b,S,True)==transfer(p,Sp,True)
with localcontext() as dc:
    dc.prec=80
    log=(Decimal(8)/Decimal('.025')).ln()
    nu=int((2*log/Decimal('.0013')**2).to_integral_value(rounding=ROUND_CEILING))
    nb=int((2*log/Decimal('.001')**2).to_integral_value(rounding=ROUND_CEILING))
    bound=8*(-nu*Decimal('.0013')**2/2).exp()+8*(-nb*Decimal('.001')**2/2).exp()
    assert (nu,nb,4*nu+nb)==(6826416,11536642,38842306) and bound<Decimal('.05')
print('PASS M16 different-cell I1: 16 physical source laws, 9 Walsh zeros, all six norms')
print('PASS nonzero exact quartic; conservative exact Fraction 95% power margin')
print('PASS 18/18 exact physical Bloch transfer alias; different source TV',tv(b,p))
print('PASS conditional confidence budget',4*nu+nb,'upper error',bound)
print('NO HARDWARE; NO GENERAL NOVELTY; NO CANON; NO EXEC SIGN')
