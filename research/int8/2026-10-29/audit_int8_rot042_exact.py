#!/usr/bin/env python3
"""Independent source-free SymPy/Fraction exact TT norm census at N3/5, no import from numerical program."""
import argparse,json,math
from itertools import product
from pathlib import Path
import sympy as s
A_CASES={
 'xy_shear':s.Matrix([[1,1,0],[0,1,0],[0,0,1]]),
 'long_middle':s.Matrix([[1,0,-1],[0,1,2],[0,0,1]]),
 'irreducible_mix':s.Matrix([[1,1,0],[0,1,1],[0,0,1]]),
}

def gram_exact(k,D,Di):
 q=s.Matrix(k)
 p=next(i for i in range(3) if q.cross(s.eye(3)[:,i])!=s.zeros(3,1))
 u=q.cross(s.eye(3)[:,p]);v=q.cross(u)
 H1=u*u.T/u.dot(u)-v*v.T/v.dot(v)
 H2=u*v.T+v*u.T
 H=[H1,H2]
 G=s.Matrix(2,2,lambda i,j:s.trace(H[i]*H[j]))
 S=s.Matrix(2,2,lambda i,j:s.trace(H[i]*D*H[j]*D))
 T=s.Matrix(2,2,lambda i,j:s.trace(H[i]*Di*H[j]*Di))
 Z=G.inv()*S*G.inv()*T
 return s.factor(s.trace(Z)),s.factor(Z.det())

def rational_sqrt_bounds(p,precision=10**12):
 p=s.Rational(p); assert p>=0
 n=(int(p.p)*precision**2)//int(p.q)
 floor=math.isqrt(n)
 lo=s.Rational(floor,precision);hi=s.Rational(floor+1,precision)
 assert lo*lo<=p and hi*hi>p
 return lo,hi

def largest_sq_bounds(tr,det):
 discr=s.factor(tr**2-4*det); assert discr>=0
 lo,hi=rational_sqrt_bounds(discr)
 return (tr+lo)/2,(tr+hi)/2

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
 detail=[];checked=0
 for name,A in A_CASES.items():
  D=A*A.T;Di=D.inv();assert A.det()==D.det()==1
  z=s.symbols('z');ch=s.factor(D.charpoly(z).as_expr())
  if name=='irreducible_mix':
   assert ch==z**3-5*z**2+6*z-1
   assert D.det()!=0 and (D-s.eye(3)).det()!=0
   assert s.factor(ch.subs(z,1))==1 and s.factor(ch.subs(z,-1))==-13
   # Rational root theorem: monic integer polynomial with constant -1 has only +-1 candidates.
   no_rational_middle=True
  else:
   assert (D-s.eye(3)).det()==0
   no_rational_middle=False
  for N in [3,5]:
   m=(N-1)//2;results=[]
   for q in product(range(-m,m+1),repeat=3):
    if q==(0,0,0) or next((v for v in q if v),1)<0:continue
    tr,det=gram_exact(q,D,Di)
    lo,hi=largest_sq_bounds(tr,det)
    results.append((lo,hi,q,tr,det));checked+=1
   winner=max(results,key=lambda z:z[0])
   # This is an exact interval certificate, not float sorting.
   # Accept exact equal maxima (e.g. signed multiples along a shearing-invariant axis),
   # but certify STRICT ordering of every genuinely smaller quadratic root by rational intervals.
   tied=[]
   for r in results:
    if r[2]==winner[2]:continue
    if r[3]==winner[3] and r[4]==winner[4]:tied.append(r[2]);continue
    assert r[1]<winner[0],(name,N,'unresolved ordering',r[2],winner[2])
   detail.append({'case':name,'N':N,'tested_projective_directions':len(results),
       'winning_q':list(winner[2]),'other_equal_winning_modes':len(tied),'winning_eigen_sq_trace':str(winner[3]),
       'winning_eigen_sq_det':str(winner[4]),'certified_norm_sq_lower':str(winner[0]),
       'certified_norm_sq_upper':str(winner[1]),'rational_middle_eigenspace':not no_rational_middle})
  if name=='long_middle':
   v=s.Matrix([2,1,0]);assert D*v==v
  if name=='xy_shear':
   v=s.Matrix([0,0,1]);assert D*v==v
 # Exact source zero-mode operator, no special Fourier k0 used in meanzero result.
 result={'artifact_id':'IW_INT8_ROT042_INDEPENDENT_EXACT_TT_20261029','status':'EXACT_RATIONAL_PASS','cases':detail,'total_mode_directions':checked,
         'generic_characteristic':'z^3-5*z^2+6*z-1; no rational root and no integer middle eigendirection',
         'independence':'exact SymPy q-Gram and integer-square-root rational interval; no numpy, no original helper'}
 Path(args.out).write_text(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf8')
 print('EXACT PASS',len(detail),'case/grid pairs and',checked,'rational two-plane matrices')
if __name__=='__main__':main()
