#!/usr/bin/env python3
"""LT4 ROT04: exact symbolic controls, not a physical simulation.
Requires sympy. No RNG; raises on failure.
"""
import sympy as s
x, y = s.symbols("x y", real=True)
def avg(f):
    return s.trigsimp(s.integrate(f, (x, 0, 2*s.pi), (y, 0, 2*s.pi))/(4*s.pi**2))
def F(w):
    return tuple(s.trigsimp(a + avg(a)) for a in w)
def L(C,w):
    cx,cy=C; wx,wy=w
    return tuple(s.trigsimp(s.expand_trig(v)) for v in (
        cx*s.diff(wx,x)+cy*s.diff(wx,y)+wx*s.diff(cx,x)+wy*s.diff(cy,x),
        cx*s.diff(wy,x)+cy*s.diff(wy,y)+wx*s.diff(cx,y)+wy*s.diff(cy,y)))
def bracket(C,D):
    return tuple(s.trigsimp(C[0]*s.diff(D[i],x)+C[1]*s.diff(D[i],y)
                           -D[0]*s.diff(C[i],x)-D[1]*s.diff(C[i],y))
                 for i in (0,1))
def T(C,w):
    return L(C,F(w))
def J(C,D,w):
    return tuple(s.trigsimp(s.expand_trig(a-b-c)) for a,b,c in
        zip(T(C,T(D,w)),T(D,T(C,w)),T(bracket(C,D),w)))
C=(s.cos(x),s.Integer(0)); D=(s.Integer(0),s.sin(x))
j1=J(C,D,(s.Integer(0),s.sin(x)))
assert j1 == (-s.cos(x)/2,s.Integer(0))
jclosed=J(C,D,(s.Integer(1),s.Integer(0)))
assert jclosed == (s.Integer(0),s.Integer(0))
def Lt(C,u):
    return s.trigsimp(s.expand_trig(s.diff(C[0]*u,x)+s.diff(C[1]*u,y)))
def Ft(u):
    return s.trigsimp(u+avg(u))
def Tt(C,u):
    return Lt(C,Ft(u))
jtop=s.trigsimp(s.expand_trig(Tt(C,Tt(D,s.sin(x)))
                         -Tt(D,Tt(C,s.sin(x)))
                         -Tt(bracket(C,D),s.sin(x))))
assert jtop == 0
assert s.simplify(Tt(C,s.Integer(1))+2*s.sin(x))==0
def Fl(u):
    return s.expand(u+s.integrate(u,(x,0,1)))
def Tl(C,u):
    return s.expand(s.diff(C*Fl(u),x))
Cb=x; Db=x*x
jboundary=s.expand(Tl(Cb,Tl(Db,s.Integer(1)))
                  -Tl(Db,Tl(Cb,s.Integer(1)))
                  -Tl(Cb*s.diff(Db,x)-Db*s.diff(Cb,x),s.Integer(1)))
assert jboundary == 2-4*x
for V in (x*(1-x),x*x*(1-x)):
    assert s.integrate(s.diff(V*(x*x+1),x),(x,0,1))==0
print("T2 nonclosed 1-form J =",j1)
print("T2 closed 1-form J =",jclosed)
print("T2 top-form J =",jtop)
print("T2 top constant transported =",Tt(C,s.Integer(1)))
print("Interval non-tangent J =",jboundary)
print("Tangent boundary fluxes = 0")
print("EXACT_CONTROLS_PASS")
