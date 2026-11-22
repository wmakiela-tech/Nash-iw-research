#!/usr/bin/env python3
"""PRF14 ROT014 concise deterministic certificate; standard Python+SymPy.
The native/full executed code with SO3+POVM perturbation/binomial simulations
is supplied separately as ROT014 local artifact rot014.py.
This compact PUBLIC GitHub copy is source-readback verified, not externally run.
"""
import math, itertools, sympy as s
R=s.Matrix([[-3,-2,6],[6,-3,2],[2,6,3]])/7
P=s.Matrix([[0,0,1],[1,0,0],[0,1,0]])
L=s.Matrix([[0,1/s.sqrt(2),1/s.sqrt(2)],[1,0,0],[0,1/s.sqrt(2),-1/s.sqrt(2)]])
C=s.Matrix([[0,s.Rational(9,100),s.Rational(11,100)],
            [s.Rational(7,100),0,s.Rational(1,10)],
            [s.Rational(8,100),s.Rational(12,100),0]])
DS=((1,1,1),(-1,-1,1),(-1,1,-1),(1,-1,-1))
assert all(X.T*X==s.eye(3) and X.det()==1 for X in (R,P,L))
assert P**3==s.eye(3)
G=list(itertools.product((0,1),repeat=2))
chi=lambda i,v:((-1)**v[1],(-1)**(v[0]+v[1]),(-1)**v[0])[i]
for d in DS:
 p=[s.factor((1+sum(d[i]*C[i,j]*chi(j,v)*chi(i,w)
     for i in range(3) for j in range(3) if i!=j))/16) for v in G for w in G]
 assert sum(p)==1 and min(p)==s.Rational(73,1600)
 assert max(p)==s.Rational(157,1600)
Q=s.Matrix(s.symbols('q0:9')).reshape(3,3)
for d in DS:
 D=s.diag(*d)
 for i in range(3):
  for j in range(3):
   assert s.simplify((D*C)[i,j]*(D*R*Q)[i,j]-C[i,j]*(R*Q)[i,j])==0

delta=27*math.sqrt(2)/700
a=(.09,.10,.12)
def bound(e):
 rho=[2*math.sqrt(3)*e/z for z in a]
 eg=(rho[1]+rho[2])/math.sqrt(2)
 ep=math.sqrt(3)*e*(9/(7*math.sqrt(2))+eg)+a[0]*eg
 eother=[(e+c*rho[i])/(6/7-rho[i]) for i,c in enumerate((.11,.07,.08))]
 margin=delta-2*(ep+e)
 p_min=73/1600-(3*math.sqrt(3)*e+sum(eother))/16
 rproject=2*math.sqrt(sum(r*r for r in rho))
 assert all(rho[i]<[6/7,2/7,3/7][i] for i in range(3))
 return margin,p_min,rproject
cmax=.12
critical=s.nsolve(s.Float(delta)-2*((1+s.sqrt(3)*9/(7*s.sqrt(2)))*s.Symbol('e')+
  s.sqrt(3)*s.Symbol('e')*(2*s.sqrt(3)*s.Symbol('e')*(1/s.Float(.1)+1/s.Float(.12))/s.sqrt(2))+
  s.Float(.09)*(2*s.sqrt(3)*s.Symbol('e')*(1/s.Float(.1)+1/s.Float(.12))/s.sqrt(2))),
  s.Symbol('e'),.00394)
assert abs(float(critical)-.0039397683823995)<1e-11
for tag, prep, meas, bias, stat, n_expected in (
 ('A',.00005,.00005,.00005,.0035,1021034),
 ('B',.0001,.0001,.0001,.00296,1427555)):
 # Operator SO3 calibration of one repeated right pulse and post-gate control
 deltaP=deltaL=.001
 mu=max(2*cmax*deltaP,cmax*deltaL)+prep+meas+bias
 e=stat+mu
 n=math.ceil(2*math.log(26/.05)/stat**2)
 assert n==n_expected
 margin,pmin,rproj=bound(e)
 assert margin>0 and pmin>0
 assert 26*math.exp(-n*stat**2/2)<=.05
 print(tag,'systematic_mu=',mu,'sample_eta=',stat,'total_eta=',e,
       '95pc sufficient total shots=',13*n,'margin=',margin,
       'source_probability_min_lower=',pmin,
       'nearest_physical_SO3_Frobenius_err_upper=',rproj)
print('SOURCE-RESTRICTED CERT PASS; not unbounded-SPAM tomography, not hardware')
