#!/usr/bin/env python3
"""Independent SymPy exact source-family plane-intersection coefficient for ROT28."""
import sympy as S,contextlib,io,runpy
from pathlib import Path
R=Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()): v=runpy.run_path(str(R/'verify_m13_rot26_exact.py'))
A=v['a'];G=S.Rational(5917501,3499200000000000)

def ip(u,w):return sum(u[i,j]*S.conjugate(w[i,j]) for i in range(3) for j in range(3))/6
s=[];cross={}
for axis in range(3):
 z=S.Rational(0)
 for m,u in A.items():
  for n,w in A.items():
   if all(m[d]==n[d] for d in range(3) if d!=axis):z+=ip(u,w)
 s.append(S.factor(z))
for i,j in ((0,1),(0,2),(1,2)):
 z=S.Rational(0)
 for m,u in A.items():
  for n,w in A.items():
   if all(m[d]==n[d] for d in range(3) if d not in (i,j)):z+=ip(u,w)
 cross[(i,j)]=S.factor(z)
C=S.factor(24*G-12*sum(s)+4*sum(cross.values()))
r2=S.factor(-3*C/G)
assert s==[S.Rational(761233367,314928000000000000),S.Rational(1409179,656100000000000),S.Rational(123982963,62985600000000000)]
print('FULL_G',G)
print('PLANES',s)
print('INTERSECTION_LINES',cross)
print('C2_k_squared',C,'C2/G',S.factor(C/G))
print('N2_TIMES_RELATIVE_TWO_MASK_RMS_2_3',r2, 'decimal',S.N(r2,20))
print('EXPECTED_RAW_REL_N',S.factor(3*(3-sum(s)/G)))
print('PASS ROT28 EXACT')