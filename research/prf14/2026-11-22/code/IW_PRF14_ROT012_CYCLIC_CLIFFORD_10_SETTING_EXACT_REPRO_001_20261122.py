#!/usr/bin/env python3
"""ROT012 source-conditional Pauli memory C3 Clifford witness.
Requires SymPy. Exact finite-group/source checks and Hoeffding bound; no device.
A more extensive executed source, including 1200 binomial trials, is recorded
in the full ROT012 report and the conversation artifact.
"""
import itertools
import math
import sympy as s

R = s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]]) / 7
WC = s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
WL = s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],
               [1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
DSET = ((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))
c = s.Rational(1,10)
G = list(itertools.product((0,1),repeat=2))
def chi(i,v):
    return ((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]

assert all(M.T*M == s.eye(3) and M.det()==1 for M in (R,WC,WL))
assert WC**3 == s.eye(3)
all_third = []
for d in DSET:
    D = s.diag(*d)
    rot = D*R
    q = {(i,j):d[i]*c for i in range(3) for j in range(3) if i!=j}
    p = [s.factor((1+sum(q[i,j]*chi(j,v)*chi(i,w)
         for i,j in q))/16) for v in G for w in G]
    assert sum(p)==1 and min(p)==s.Rational(1,20)
    assert max(p)==s.Rational(1,10)
    A = {(i,j):s.simplify(q[i,j]*rot[i,j]) for i,j in q}
    B = {(i,j):s.simplify(q[i,j]*(rot*WC)[i,j]) for i,j in q}
    M = s.Matrix(3,3,lambda i,j:A[i,j] if i!=j else B[i,(i-1)%3])
    assert M==c*R
    for i in range(3):
        assert s.simplify((M.row(i)*M.row(i).T)[0]-c**2)==0
        j=(i+1)%3
        assert B[i,j]==M[i,(j+1)%3]
    z=s.simplify(q[0,1]*(WL*rot)[0,1])
    z_predict=s.simplify(d[0]*(d[1]*B[1,0]+d[2]*A[2,1])/s.sqrt(2))
    assert z==z_predict
    all_third.append(z)

assert len(set(all_third))==4
gap=min(abs(a-b) for i,a in enumerate(all_third) for b in all_third[i+1:])
assert s.simplify(gap-3/(35*s.sqrt(2)))==0

eta=s.Rational(3,250)
model_eta=s.Rational(1,100)
delta=s.Rational(3,1000)
margin=s.simplify(gap-2*(1+s.sqrt(2))*eta)
model_margin=s.simplify(gap-2*(1+s.sqrt(2))*model_eta
                       -4*(s.Rational(9,7)/s.sqrt(2))*delta)
assert margin>0 and model_margin>0
n=math.ceil(2*math.log(400)/float(eta)**2)
n_model=math.ceil(2*math.log(400)/float(model_eta)**2)
assert n==83215 and n_model==119830
print("EXACT_SOURCE_PASS: FOUR_PHYSICAL_WORLDS, 9_MEAN_ALIAS, 10TH_MEAN_SEPARATES")
print("four third means", [str(x) for x in all_third])
print("gap",gap,"exact margin",margin)
print("95pct ten-setting sufficient shots",10*n)
print("3pct source model misspec robustness margin",model_margin)
print("95pct ten-setting sufficient shots WITH 3pct model deviation",10*n_model)
print("SCOPE: row-flat hidden Fourier source, independently calibrated controls/SPAM")
