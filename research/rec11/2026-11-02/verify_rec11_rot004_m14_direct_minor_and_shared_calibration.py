#!/usr/bin/env python3
"""REC11 ROT004. Independent direct 13x13 determinant rather than M14's
cofactor-reduced 10x10; exact interpolation + Bernstein + 100-digit FI.
Requires sympy and mpmath. Synthetic model only.
"""
from fractions import Fraction as Q
import sympy as S
import mpmath as mp

def det_bareiss(rows):
    A=[list(r) for r in rows]; n=len(A); prev=Q(1); sign=1
    for k in range(n-1):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None: return Q(0)
        if pivot!=k: A[k],A[pivot]=A[pivot],A[k];sign=-sign
        p=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*p-A[i][k]*A[k][j])/prev
            A[i][k]=Q(0)
        prev=p
    return sign*A[-1][-1]

old_x=list(map(Q,('3/4','5/4','7/4','9/4','5')))
new_x=list(map(Q,('11/2','6','13/2','7')))

def jac(t):
    t=Q(t)
    w=[(Q(155)+t)/1000,Q(51,100),(Q(335)-t)/1000]
    e,B,v,d=Q(1,25),-Q(3,100),Q(53,100),Q(11,50)
    out=[]; mus=[]
    for sg,beta,g in [(-1,Q(31,10),Q(4,5)),(1,Q(29,10),Q(6,5))]:
        xs=old_x+(new_x if sg==-1 else [])
        for x in xs:
            z=[x-e-sg*B-j*d for j in (-1,0,1)]
            k=[1/(zz*zz+v) for zz in z]
            dz=[2*zz/(zz*zz+v)**2 for zz in z]
            dv=[-1/(zz*zz+v)**2 for zz in z]
            f=sum(a*b for a,b in zip(w,k))
            fd=sum(a*b for a,b in zip(w,dz))
            fv=sum(a*b for a,b in zip(w,dv))
            fj=sum(a*j*b for a,j,b in zip(w,(-1,0,1),dz))
            mu=beta-g*f
            assert mu>0 and all(a>0 for a in w)
            source=[-g*(k[0]-k[2]),-g*(k[1]-k[2]),-g*fd,
                    -sg*g*fd,-g*fv,-g*fj]
            source+=([Q(1),-f,Q(0),Q(0)] if sg==-1
                     else [Q(0),Q(0),Q(1),-f])
            cal=[Q(1),mu,(x-6)*mu] if sg==-1 and x in new_x else [Q(0)]*3
            out.append(source+cal);mus.append(mu)
    return out,mus

def D(t):
    J,_=jac(t)
    return det_bareiss([J[i] for i in (1,2,3,4,9,10,11,12,13,5,6,7,8)])

def C(t):
    _,M=jac(t)
    return det_bareiss([[Q(1),M[5+i],(new_x[i]-6)*M[5+i]]
                        for i in range(3)])

t=S.Symbol('t')
def poly(points):
    return S.Poly(S.interpolate([(S.Rational(i),S.Rational(y.numerator,y.denominator))
                                  for i,y in points],t),t,domain=S.QQ)
# A single constant eta-column in the direct 13x13 Jacobian limits
# polynomial determinant degree to <=12; 13 exact nodes are complete.
P=poly([(i,D(i)) for i in range(-6,7)])
# Calibration 3x3 determinant has a constant first column and two affine
# mean columns: degree <=2; 3 exact nodes suffice.
Qp=poly([(i,C(i)) for i in (-2,-1,0)])
assert P.degree()==7 and Qp.degree()==2

def bern(a):
    n=a.degree()
    return [sum(a.nth(j)*S.binomial(i,j)/S.binomial(n,j)
                for j in range(i+1)) for i in range(n+1)]
pb=bern(P); cb=bern(Qp)
assert all(x<=pb[0]<0 for x in pb)
assert all(x>=cb[-1]>0 for x in cb)
assert P.count_roots(0,1)==Qp.count_roots(0,1)==0
for u in (Q(1,7),Q(2,3),Q(5,11),Q(133,1000),Q(998,1000)):
    a=S.Rational(u.numerator,u.denominator)
    assert P.eval(a)==S.Rational(D(u).numerator,D(u).denominator)
    assert Qp.eval(a)==S.Rational(C(u).numerator,C(u).denominator)
print('EXACT PASS: D degree7, Q degree2; Bernstein uniform signs')
print('D(0)',float(D(0)),'D(1/2)',float(D(Q(1,2))),'D(1)',float(D(1)))
print('min Bernstein Q',float(min(cb)))

mp.mp.dps=100
fold=Q(279418103510806400758,10**21)
JJ,means=jac(fold)
mpq=lambda q:mp.mpf(q.numerator)/mp.mpf(q.denominator)
J=mp.matrix([[mpq(x) for x in row] for row in JJ])
I=J.T*mp.diag([1/mpq(x) for x in means])*J
nu=[0,1,2,4,5,6,7,8,9,10,11,12]
A=mp.matrix([[I[i,j] for j in nu] for i in nu])
b=mp.matrix([I[i,3] for i in nu])
Ie=I[3,3]-(b.T*mp.lu_solve(A,b))[0]
assert Ie>0
print('100-digit FI',mp.nstr(Ie,26))

# Separating model with old calibration: old Poisson mu=eta,
# new Poisson mu=eta+theta, nominal eta=1,theta=0.
# With new count alone effective FI_theta=0; old count
# jointly constrains eta and increases FI_theta to 1/2.
Ionly=S.Matrix([[1,1],[1,1]])
Ishared=S.Matrix([[1,1],[1,2]])
assert Ionly[0,0]-Ionly[0,1]**2/Ionly[1,1]==0
assert Ishared[0,0]-Ishared[0,1]**2/Ishared[1,1]==S.Rational(1,2)
print('SHARP DOMAIN CONTROL: old shared calibration changes 0 to 1/2')
