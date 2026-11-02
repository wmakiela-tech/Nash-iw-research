#!/usr/bin/env python3
"""INT8-051: source-free exact cyclotomic roots + finite-field rank certificates for all N7/N9 z Fourier fibers."""
import argparse,json
from pathlib import Path
import sympy as sp
from itertools import product

# Mathematical exact primitive root identities: 4 sin²(j*pi/N)=2-zeta^j-zeta^-j.
x=sp.Symbol('x')
def trig_sum_rem(N,modes,target):
 poly=sp.Poly(sum(2-x**j-x**(N-j) for j in modes)-4*sp.Rational(target),x,domain=sp.QQ)
 cycl=sp.Poly(sp.cyclotomic_poly(N,x),x,domain=sp.QQ)
 assert poly.rem(cycl).is_zero
 return str(poly.as_expr()),str(cycl.as_expr())

A=(1,2,0);B=(2,-1,0);Ez=(0,0,1)
def mat_add(M,T,p):return [[(M[i][j]+T[i][j])%p for j in range(3)] for i in range(3)]
def mat_sub(M,T,p):return [[(M[i][j]-T[i][j])%p for j in range(3)] for i in range(3)]
def mat_scale(c,M,p):return [[c*M[i][j]%p for j in range(3)] for i in range(3)]
def matmul(M,T,p):return [[sum(M[i][k]*T[k][j] for k in range(3))%p for j in range(3)] for i in range(3)]
def outer(u,v,p):return [[(u[i]*v[j])%p for j in range(3)] for i in range(3)]
def transpose(M):return [list(r) for r in zip(*M)]
def tr(M,p):return sum(M[i][i] for i in range(3))%p
def sym(u,v,p):return mat_add(outer(u,v,p),outer(v,u,p),p)
def mat_vec(M,v,p):return [sum(M[i][j]*v[j] for j in range(3))%p for i in range(3)]
def proj(M,k,p):
 k2=sum(c*c for c in k)%p
 assert k2!=0,('bad field',p,k)
 inv=pow(k2,-1,p)
 Q=mat_sub([[int(i==j) for j in range(3)] for i in range(3)],mat_scale(inv,outer(k,k,p),p),p)
 X=matmul(matmul(Q,M,p),Q,p)
 # tr(QM) is the transverse trace.
 c=tr(matmul(Q,M,p),p)*pow(2,-1,p)%p
 return mat_sub(X,mat_scale(c,Q,p),p)
def chebyU(ell,t,p):
 if ell==0:return 0
 a,b=0,1
 for j in range(1,ell):a,b=b,(t*b-a)%p
 return b

def fiber_map(N,ell,p,t):
 s1,s2,sz=1,t,chebyU(ell,t,p)
 sa=(s1,s2,0);sb=(s2,-s1,0)
 v=[]
 for i in range(3):
  M=[[0]*3 for _ in range(3)];M[i][i]=1;v.append(M)
 for i,j in ((0,1),(0,2),(1,2)):
  M=[[0]*3 for _ in range(3)];M[i][j]=M[j][i]=1;v.append(M)
 col=[]
 for S in v:
  Mvals=[]
  for ta,ss in product((1,-1),repeat=2):
   k=[ta*A[j]+ss*B[j]+(ell if j==2 else 0) for j in range(3)]
   Be=mat_vec(S,Ez,p)
   SB=mat_add(mat_scale(ss*sz,S,p),sym(Be,sb,p),p)
   PB=proj(SB,[ss*B[j]+(ell if j==2 else 0) for j in range(3)],p)
   AB=proj(mat_add(mat_scale(ta*sz,PB,p),sym(mat_vec(PB,Ez,p),sa,p),p),k,p)
   SA=mat_add(mat_scale(ta*sz,S,p),sym(Be,sa,p),p)
   PA=proj(SA,[ta*A[j]+(ell if j==2 else 0) for j in range(3)],p)
   BA=proj(mat_add(mat_scale(ss*sz,PA,p),sym(mat_vec(PA,Ez,p),sb,p),p),k,p)
   H=mat_scale(pow(4,-1,p),mat_sub(AB,BA,p),p)
   Mvals.extend(x for row in H for x in row)
  col.append(Mvals)
 return [list(row) for row in zip(*col)]

def rank_mod(M,p):
 R=[r.copy() for r in M];nr=len(R);nc=len(R[0]);i=0;pivots=[];row_ids=list(range(nr))
 for j in range(nc):
  q=next((k for k in range(i,nr) if R[k][j]%p),None)
  if q is None:continue
  R[i],R[q]=R[q],R[i];row_ids[i],row_ids[q]=row_ids[q],row_ids[i]
  v=pow(R[i][j],-1,p);R[i]=[(v*w)%p for w in R[i]]
  for k in range(i+1,nr):
   t=R[k][j]
   if t:R[k]=[(R[k][u]-t*R[i][u])%p for u in range(nc)]
  pivots.append(j);i+=1
  if i==nc:break
 return i,pivots,row_ids[:i]

def det_mod(Q,p):
 A=[r.copy() for r in Q];n=len(A);ans=1
 for j in range(n):
  row=next((i for i in range(j,n) if A[i][j]%p),None)
  if row is None:return 0
  if row!=j:A[j],A[row]=A[row],A[j];ans=-ans
  v=A[j][j]%p;ans=ans*v%p;inv=pow(v,-1,p)
  for i in range(j+1,n):
   factor=A[i][j]*inv%p
   for k in range(j,n):A[i][k]=(A[i][k]-factor*A[j][k])%p
 return ans%p

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
 identities=[]
 for N,modes,value in [(7,(1,2,3),sp.Rational(7,4)),(9,(1,2,4),sp.Rational(3,2))]:
  a,b=trig_sum_rem(N,modes,value)
  identities.append({'N':N,'j':list(modes),'exact_sum':str(value),'cyclotomic_polynomial':b,'remainder_zero':True})
 # Minimal polynomials of t=2cos(2pi/N), irreducible over Q (checked exactly).
 f7=sp.Poly(x**3+x**2-2*x-1,x);f9=sp.Poly(x**3-3*x+1,x)
 assert f7.is_irreducible and f9.is_irreducible
 certificates=[]
 for N,p,t,ff in [(7,41,14,f7),(9,53,4,f9)]:
  assert int(ff.eval(t))%p==0
  for ell in range((N+1)//2):
   M=fiber_map(N,ell,p,t)
   rank,pivs,rows=rank_mod(M,p)
   assert rank==(3 if ell==0 else 6),(N,ell,rank)
   witness=det_mod([[M[i][j] for j in pivs] for i in rows],p)
   assert witness!=0
   certificates.append({'N':N,'ell':ell,'prime':p,'root_of_minpoly_mod_prime':t,'rank_mod_prime':rank,'pivot_columns':pivs,'witness_rows':rows,'witness_minor_mod_prime':witness})
 out={'artifact_id':'IW_INT8_ROT051_STABLE_FILTER_DARK_Z_FIBERS_001_20261102','status':'EXACT_CYCLOTOMIC_MODULAR_PASS','identities':identities,'rank_certificates':certificates,'rank_theorem':'Because minimal polynomial of 2cos(2pi/N) is irreducible over Q, an exact polynomial 6x6 minor vanishing at the real root would be divisible by that polynomial, hence vanish at each modular root. Rank6 mod a prime at a modular root proves rank6 over Q(2cos(2pi/N)).','limitation':'Ranks established exactly for N7 and N9 ALL z harmonic ell; rank scans at N>=11 not converted to mathematical proof. Dark e_shell factor proven analytically.'}
 Path(args.out).write_text(json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
 print('EXACT_CYCLOTOMIC_MODULAR_PASS',len(identities),'root-of-unity identities;',len(certificates),'fiber rank checks')
if __name__=='__main__':main()
