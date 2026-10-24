#!/usr/bin/env python3
"""M13/ROT33: directed interval arithmetic over source-native sparse Fourier operators.
mpmath.iv is outward-rounded arbitrary-precision interval arithmetic.
Certifies sign of Bernstein coefficients for derivative of KA²/KC², not merely
on decimal-rounded output from ROT32. Not a byte-exact production runtime audit.
"""
from __future__ import annotations
import csv,json,time,sys,math
from pathlib import Path
from mpmath import iv

iv.dps=45
Z=iv.mpc(0,0);I=iv.mpc(0,1);ONE=iv.mpf(1);ZERO=iv.mpf(0)
ROOT=Path(__file__).resolve().parent
T=(3,3);ORIGIN=(0,0,0)

def zm(): return [[Z for j in range(3)] for i in range(3)]
def mz(a,b,sa=1,sb=1):return [[sa*a[i][j]+sb*b[i][j] for j in range(3)] for i in range(3)]
def zmul(a,c):return [[x*c for x in row] for row in a]
def matmul(a,b):return [[sum((a[i][k]*b[k][j] for k in range(3)),Z) for j in range(3)] for i in range(3)]
def tr(a):return sum((a[i][i] for i in range(3)),Z)
def cbasis(a):return [v for v in a]
def madd(a,b):return [a[i]+b[i] for i in range(3)]
def scale(a,c):return [x*c for x in a]

def add(a,b,sa=1,sb=1):
 out={p:zmul(v,sa) for p,v in a.items()}
 for p,v in b.items():out[p]=mz(out[p],v,sb=1*sb) if p in out else zmul(v,sb)
 return out

def source():
 C1={};C2={};h={}
 for s in (-1,1):
  q=(s,0,0);C1[q]=[-I*s/40,Z,Z];C2[q]=[Z,Z,-I*s/50]
  q=(0,s,0);C1[q]=[Z,iv.mpc(ONE/40),Z]
  q=(0,0,s);C2[q]=[iv.mpc(ONE/50),Z,Z]
  for t in (-1,1):
   mat=zm()
   for i in range(3):mat[i][i]=-I*s/40
   h[(s,t,0)]=mat
 return C1,C2,h

def delta(m,N):
 dx=2*iv.pi/N
 return [I*iv.sin(m[i]*dx)/dx for i in range(3)]

def em(m,N,alpha):
 dx=2*iv.pi/N
 return ONE+2*alpha*sum((iv.cos(m[i]*dx)-ONE for i in range(3)),ZERO)

def addv(out,m,v):
 if m in out:out[m]=madd(out[m],v)
 else:out[m]=v

def addm(out,m,v):
 if m in out:out[m]=mz(out[m],v)
 else:out[m]=v

def bracket(C1,C2,N,D):
 out={}
 for p,c in C1.items():
  dp=D[p]
  for q,d in C2.items():
   dq=D[q]
   m=tuple(p[i]+q[i] for i in range(3))
   v=[sum((c[k]*dq[k]*d[i]-d[k]*dp[k]*c[i] for k in range(3)),Z) for i in range(3)]
   addv(out,m,v)
 return out

def lie(C,H,N,D):
 out={}
 for p,c in C.items():
  dp=D[p]
  for q,h in H.items():
   dq=D[q];m=tuple(p[i]+q[i] for i in range(3))
   adv=sum((c[k]*dq[k] for k in range(3)),Z)
   term=[[adv*h[i][j]+sum((h[k][j]*dp[i]*c[k]+h[i][k]*dp[j]*c[k] for k in range(3)),Z) for j in range(3)] for i in range(3)]
   addm(out,m,term)
 return out

def proj(H):
 out={}
 for m,h in H.items():
  if m==ORIGIN:
   trace=tr(h)/3
   v=[[h[i][j]-(trace if i==j else Z) for j in range(3)] for i in range(3)]
  else:
   mm=sum(i*i for i in m)
   P=[[iv.mpf(1 if i==j else 0)-iv.mpf(m[i]*m[j])/mm for j in range(3)] for i in range(3)]
   # trace(P h) / 2 ; P is real-valued
   ph=matmul(P,h);php=matmul(ph,P);trace=tr(ph)/2
   v=[[php[i][j]-trace*P[i][j] for j in range(3)] for i in range(3)]
  out[m]=[[(v[i][j]+v[j][i])/2 for j in range(3)] for i in range(3)]
 return out

def calc(N,alpha):
 C1,C2,h=source()
 # D exact from source mode closure, includes all up to 4 harmonics
 modes={(i,j,k) for i in range(-4,5) for j in range(-4,5) for k in range(-3,4)}
 D={p:delta(p,N) for p in modes}
 b=bracket(C1,C2,N,D)
 def L(C,H):return lie(C,{m:zmul(v,em(m,N,alpha)) for m,v in H.items()},N,D)
 C=add(add(L(C1,L(C2,h)),L(C2,L(C1,h)),sb=-1),L(b,h),sb=-1)
 B=proj(C)
 A=add(add(proj(L(C1,proj(L(C2,h)))),proj(L(C2,proj(L(C1,h)))),sb=-1),proj(L(b,h)),sb=-1)
 return A,B,C

def lin(a,b,sa=1,sb=1):return add(a,b,sa,sb)
def tensor_polys(N):
 a0=calc(N,iv.mpf(0));ap=calc(N,iv.mpf(1));am=calc(N,iv.mpf(-1))
 pol=[]
 for channel in range(3):
  U=a0[channel];V=lin(ap[channel],am[channel],iv.mpf(1)/2,-iv.mpf(1)/2)
  W=lin(lin(ap[channel],am[channel],iv.mpf(1)/2,iv.mpf(1)/2),U,1,-1)
  pol.append((U,V,W))
 return pol

def conj(z):return iv.mpc(z.real,-z.imag)

def window_mode(q,N,k,win_cache):
 ky=(q,N,k)
 if ky in win_cache:return win_cache[ky]
 if q==0:res=iv.mpc(ONE)
 else:
  dx=2*iv.pi/N
  rem=sum((iv.cos(q*j*dx) for j in range(k)),ZERO)+sum((iv.cos(q*j*dx) for j in range(1,k+1)),ZERO)
  ims=sum((iv.sin(q*j*dx) for j in range(k)),ZERO)-sum((iv.sin(q*j*dx) for j in range(1,k+1)),ZERO)
  res=-iv.mpc(rem,ims)/(N-2*k)
 win_cache[ky]=res;return res

def dot(X,Y):return sum((conj(Y[i][j])*X[i][j] for i in range(3) for j in range(3)),Z)

def inner(X,Y,N,k,cache):
 if k==0:
  return sum((dot(X[m],Y[m]) for m in X.keys() & Y.keys()),Z).real/6
 out=Z
 for m,tx in X.items():
  for n,ty in Y.items():
   v=dot(tx,ty)
   for j in range(3):v*=window_mode(m[j]-n[j],N,k,cache)
   out+=v
 return out.real/6

def quartic(pol,N,k,cache):
 u,v,w=pol
 A=inner(u,u,N,k,cache);B=inner(u,v,N,k,cache)
 C=inner(v,v,N,k,cache);D=inner(u,w,N,k,cache)
 E=inner(v,w,N,k,cache);F=inner(w,w,N,k,cache)
 return [A,2*B,C+2*D,2*E,F]

def polymul(a,b):
 r=[ZERO]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]+=x*y
 return r

def polydif(a):return [(i+1)*a[i+1] for i in range(len(a)-1)]
def polyd(a,b):
 x=polymul(polydif(a),b);y=polymul(a,polydif(b));return [x[i]-y[i] for i in range(len(x))]

def bernstein(poly,high=iv.mpf(1)/5):
 n=len(poly)-1
 return [sum((poly[j]*high**j*iv.mpf(math.comb(i,j))/math.comb(n,j) for j in range(i+1)),ZERO) for i in range(n+1)]

def mid(r):return float(r.mid)
def bounds(r):return [float(r.a),float(r.b)]
def all_negative(coeff):return all(float(c.b)<0 for c in coeff)

def run():
 t=time.monotonic();print('INTERVAL_PROOF_START mp.iv.dps=',iv.dps,flush=True)
 rows=[];worst=-float('inf');maxwidth=0;best_log_bound=float('inf');hist_max_rel=0.;frozen={(int(r['N']),r['alpha']):r for r in csv.DictReader((ROOT/'dtc0a_N31_N33_N35_N37_N39_N41_sparse_convergence_v0_3_1.csv').open())};masks={(r['alpha'],int(r['interior_k'])):r for r in csv.DictReader((ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open())}
 for N in (31,33,35,37,39,41):
  pols=tensor_polys(N)
  for k in ((2,3,4,5,6) if N==41 else (3,)):
   cache={}
   gA=quartic(pols[0],N,k,cache)
   gC=quartic(pols[2],N,k,cache)
   B=bernstein(polyd(gA,gC));normalized=[b/(gA[0]*gC[0]) for b in B]
   gAb=bernstein(gA);gCb=bernstein(gC)
   passed=all(x.b < 0 for x in normalized) and all(x.a > 0 for x in gAb+gCb)
   if not passed:raise AssertionError((N,k,[str(x) for x in normalized]))
   worst=max(worst,max(float(x.b) for x in normalized))
   maxwidth=max(maxwidth,max(float(x.b-x.a) for x in normalized))
   log_bound=-max(x.b for x in B)/(2*max(x.b for x in gAb)*max(x.b for x in gCb))
   log_lower=float(log_bound.a)
   best_log_bound=min(best_log_bound,log_lower)
   
   historical=[]
   for numer,aname in [(0,'0.0'),(1,'0.05'),(4,'0.2')]:
    alpha=iv.mpf(numer)/20
    reference=frozen[(N,aname)] if k==3 else masks[(aname,k)]
    for ch,poly in [('A',gA),('C',gC)]:
     sq=sum((poly[j]*alpha**j for j in range(5)),ZERO)
     estimate=math.sqrt(float(sq.mid))
     actual=float(reference['K_'+ch+'_RMS'])
     rel=abs(estimate/actual-1)
     hist_max_rel=max(hist_max_rel,rel)
     historical.append({'alpha':aname,'ch':ch,'approx_source_RMS':estimate,'frozen_RMS':actual,'rel_error':rel})
   row={'N':N,'k':k,'historical_comparisons':historical,'Bernstein_normalized_bounds':[bounds(x) for x in normalized], 'normalized_max_upper':max(float(x.b) for x in normalized),'interval_certified_log_derivative_abs_lower':log_lower,'max_width':max(float(x.b-x.a) for x in normalized), 'positive_A_C_Bernstein_lower':min(float(x.a) for x in gAb+gCb), 'source_exact_interval':True}
   rows.append(row);print('PASS',N,k,'normalized max upper',row['normalized_max_upper'],'width',row['max_width'],'elapsed',int(time.monotonic()-t),flush=True)
 print('ALL_PASS',len(rows),'worst normalized upper',worst,'max interval width',maxwidth,'historical_A_C_maxrel',hist_max_rel,'uniform_log_derivative_lower',best_log_bound,'seconds',time.monotonic()-t,flush=True)
 result={'return_id':'M13_ROT33_DIRECTED_INTERVAL_FOURIER_SOURCE_CERT_20261024','precision_decimal_digits':iv.dps,'exact_sources':['N integer','mode Fourier coefficient rational','P_TT integer mode rational','E_lin exact alpha linear','centered derivative sin(dx*m)/dx with outward-rounded interval pi/sine','window exact Fourier geometric sum using outward-rounded cos/sin'], 'source_reconstruction':'Unmodified retained helper not reimplemented byte-for-byte; sparse mode analytic exact formulas with directed outward rounding','model_gate':'ONLY KNOWN SOURCE C1,C2,h, order2 stencil, fixed alpha range 0..1/5; known scale positive and same for A,C', 'cases':rows,'pass_count':len(rows),'normalized_bernstein_worst_upper':worst,'maximum_interval_width':maxwidth,'uniform_interval_certified_log_derivative_abs_lower':best_log_bound,'max_frozen_relative_error_A_C':hist_max_rel,'status':'INTERVAL_MONOTONICITY_FOR_RETAINED_FORMULAS_PASS / NOT ORIGINAL HISTORICAL_RUNTIME / NO_PHYSICS'}
 (ROOT/'IW_M13_ROT33_directed_interval_certificates_20261024.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':run()