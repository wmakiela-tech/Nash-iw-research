#!/usr/bin/env python3
"""INT8-049: independent EXACT Fraction grid stencil audit; no NumPy, source or other script."""
from fractions import Fraction as F
from itertools import product
import json,argparse
from pathlib import Path

N=3
S=[F(0),F(1),F(-1)]
C=[F(1),F(-1,2),F(-1,2)]
zero=F(0)
ids=[tuple(t) for t in product(range(N),repeat=3)]

def eye_field(f):
 return {t:[[f(t) if i==j else zero for j in range(3)] for i in range(3)] for t in ids}
def arbitrary_tensor():
 return {t:[[F((1+t[0]*7+t[1]*11+t[2]*13+i*5+j*3)%23-11,17) for j in range(3)] for i in range(3)] for t in ids}
def field(fun):return {t:fun(t) for t in ids}
def shift(t,axis,k):
 q=list(t);q[axis]=(q[axis]+k)%N;return tuple(q)
def diff(arr,axis,t):return (arr[shift(t,axis,1)]-arr[shift(t,axis,-1)])/2
def lap(arr,t):return sum((arr[shift(t,a,1)]-2*arr[t]+arr[shift(t,a,-1)]) for a in range(3))
def E(H,alpha):
 if not alpha:return {t:[v[:] for v in H[t]] for t in ids}
 out={t:[[zero]*3 for _ in range(3)] for t in ids}
 for i in range(3):
  for j in range(3):
   arr={t:H[t][i][j] for t in ids}
   for t in ids:out[t][i][j]=arr[t]+alpha*lap(arr,t)
 return out

def L(g,H):
 grads=[{t:diff(g,axis,t) for t in ids} for axis in range(3)]
 out={t:[[zero]*3 for _ in range(3)] for t in ids}
 for i in range(3):
  for j in range(3):
   arr={t:H[t][i][j] for t in ids}
   for t in ids:
    out[t][i][j]=g[t]*diff(arr,2,t)+H[t][2][j]*grads[i][t]+H[t][i][2]*grads[j][t]
 return out

def comm(g,h,H,alpha):
 return minus(L(g,E(L(h,E(H,alpha)),alpha)),L(h,E(L(g,E(H,alpha)),alpha)))
def minus(A,B):return {t:[[A[t][i][j]-B[t][i][j] for j in range(3)] for i in range(3)] for t in ids}
def iszero(A):return all(A[t][i][j]==0 for t in ids for i in range(3) for j in range(3))
def squares(A):return sum(A[t][i][j]**2 for t in ids for i in range(3) for j in range(3))

def main():
 p=argparse.ArgumentParser();p.add_argument('--out',required=True);args=p.parse_args()
 # Two rational real standing waves with xy lattice eigenvalues exactly -6, as in modes (1,2),(2,-1) modulo 3.
 g=field(lambda t:S[(t[0]+2*t[1])%3]);h=field(lambda t:S[(2*t[0]-t[1])%3]);alpha=F(1,20)
 assert all(lap(g,t)==-6*g[t] and lap(h,t)==-6*h[t] for t in ids)
 constant=eye_field(lambda t:F(1))
 fz=eye_field(lambda t:1+F(1,4)*C[t[2]])
 fx=eye_field(lambda t:1+F(1,4)*C[t[0]])
 fxy=eye_field(lambda t:1+F(1,6)*C[(t[0]+t[1])%3])
 gen=arbitrary_tensor()
 checks=[]
 for name,H in [('constant',constant),('z_nonconstant',fz),('x_nonconstant',fx),('xy_nonconstant',fxy),('arbitrary_tensor',gen)]:
  for mode,a in [('Identity',F(0)),('E_lin',alpha)]:
   K=comm(g,h,H,a);is_z=iszero(K)
   if mode=='Identity':assert is_z,(name,mode)
   if mode=='E_lin' and name in ('constant','z_nonconstant'):assert is_z
   if mode=='E_lin' and name in ('x_nonconstant','xy_nonconstant','arbitrary_tensor'):assert not is_z,(name,mode)
   checks.append({'name':name,'mode':mode,'zero':is_z,'sum_of_squares_exact':str(squares(K))})
 result={'artifact_id':'IW_INT8_ROT049_EXACT_RATIONAL_GRID_PURETRACE_20261101','status':'EXACT_FRACTION_PASS','N':N,'tests':checks,'scaling':'grid spacing unit1 and E=I+alpha Delta; exact rational 3-grid source-independent structural controls','source_status':'NO_SOURCE_IMPORT','negative_controls':'E_lin with planar f and generic H yields nonzero K_C despite bracket identically zero; Identity K_C zero on all tensor fields'}
 Path(args.out).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
 print('EXACT_FRACTION_PASS',len(checks),'full 3^3 x 3 x 3 rational tensor field cases')
if __name__=='__main__':main()
