#!/usr/bin/env python3
"""Exact SymPy checks for MT13-GROK-LT4-D1 (not a physics or novelty claim)."""
import sympy as s
x,y=s.symbols('x y',real=True);c=s.symbols('c',nonzero=True)
def lie1(C,h):
    zz=[x,y]
    return s.Matrix([s.expand_trig(sum(C[j]*s.diff(h[i],zz[j]) for j in range(2))+sum(h[j]*s.diff(C[j],zz[i]) for j in range(2))) for i in range(2)])
def p01(h):
    return s.Matrix([s.simplify(s.integrate(s.integrate(s.trigsimp(z),(x,0,2*s.pi)),(y,0,2*s.pi))/(2*s.pi)**2) for z in h])
def F(h):return h+(c-1)*p01(h)
def T(C,h):return lie1(C,F(h))
X=s.Matrix([s.cos(x),0]);Y=s.Matrix([0,s.sin(x)]);h=s.Matrix([0,s.sin(x)])
delta=s.simplify(T(X,T(Y,h))-T(Y,T(X,h))-T(lie1(X,Y),h))
assert all(s.trigsimp(z)==0 for z in delta-s.Matrix([-(c-1)*s.cos(x)/2,0]))
print("PASS rank1 d2:",delta)
def mu(n):return c if n==0 else 1
def step(k,n,a,r):return n+k,s.expand(a*s.I*(n+r*k)*mu(n))
for r in range(6):
    n1,a1=step(-1,1,1,r);n2,a2=step(1,n1,a1)
    n3,a3=step(1,1,1,r);n4,a4=step(-1,n3,a3)
    assert n2==n4==1 and s.simplify(a2-a4-2-r*(r-1)*(c-1))==0
print("PASS rank 0..5 one-dimensional embedded witnesses")
for r in [1,2,3]:
    for k in [-4,-2,-1,1,2,5]:
        z=s.symbols("mu")
        assert s.solve(-c*r*k*k*(z-1),z)==[1]
print("PASS translation pinning for 18 frequencies")
v=s.Matrix([s.Rational(2,3),-s.Rational(1,5)])
w=s.Matrix([s.Rational(1,4),s.Rational(3,7)])
k=s.Matrix([2,-3]);n=s.Matrix([1,2]);A=s.Matrix([[2,3],[3,5]])
B=(w.dot(n))*A+k*(A*w).T+(A*w)*k.T
mn,mm=s.symbols("mn mm")
left=-mn*mm*v.dot(n+k)*B+mn**2*v.dot(n)*B+mn*v.dot(k)*B
right=-mn*v.dot((n+k)*mm-n*mn-k)*B
assert B!=s.zeros(2) and s.simplify(left-right)==s.zeros(2)
print("PASS independent nonaxis rank2 Fourier commutator factorization")
