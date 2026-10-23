import sympy as S,runpy,contextlib,io,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
start=time.time()
with contextlib.redirect_stdout(io.StringIO()): d=runpy.run_path(str(ROOT/'verify_m13_rot26_exact.py'))
C1,C2,h=d['C1'],d['C2'],d['h'];P=d['P'];I=S.I;a=S.symbols('alpha',real=True)
zero=(0,0,0)
# dual field X=(X0,X1) symbolic t=(2pi/N)^2, coefficients exact rationals
mk=lambda H:{k:(v,S.zeros(*v.shape)) for k,v in H.items()}
def add(A,B,coef=1):
 out={k:[v[0],v[1]] for k,v in A.items()}
 for k,v in B.items():
  if k in out:out[k]=[out[k][i]+coef*v[i] for i in range(2)]
  else:out[k]=[coef*v[i] for i in range(2)]
 return {k:tuple(v) for k,v in out.items()}
def multder(m,axis):return (I*m[axis], -I*S.Rational(m[axis]**3,6))
def derv(A,m,axis):
 p0,p1=multder(m,axis);return p0*A[0], p0*A[1]+p1*A[0]
def efactor(H):
 return {k:(v[0], v[1]-a*sum(i*i for i in k)*v[0]) for k,v in H.items()}
def Lie(C,F):
 out={}
 for p,c in C.items():
  for q,f in F.items():
   m=tuple(p[i]+q[i] for i in range(3)); val=[]
   for t in range(2):
    z=S.zeros(3,3)
    for k in range(3):
     p0,p1=multder(q,k)
     z+=(c[0][k]*((p0*f[t])+(p1*f[0] if t==1 else S.zeros(3,3))))
     if t==1: z+= c[1][k]*p0*f[0]
    for i in range(3):
     for j in range(3):
      w=0
      for k in range(3):
       for il,jl in ((i,j),(j,i)):
        p0,p1=multder(p,il)
        if t==0:w+=p0*c[0][k]*f[0][k,(j if il==i else i)]
        else:w+=p0*(c[0][k]*f[1][k,(j if il==i else i)]+c[1][k]*f[0][k,(j if il==i else i)])+p1*c[0][k]*f[0][k,(j if il==i else i)]
      z[i,j]+=w
    val.append(z)
   if m in out:out[m]=tuple(out[m][i]+val[i] for i in range(2))
   else:out[m]=tuple(val)
 return out
def Br(C,D):
 out={}
 for p,c in C.items():
  for q,d in D.items():
   m=tuple(p[i]+q[i] for i in range(3)); val=[]
   for t in range(2):
    z=S.zeros(3,1)
    for i in range(3):
     s=0
     for k in range(3):
      q0,q1=multder(q,k);p0,p1=multder(p,k)
      if t==0:s+=c[0][k]*q0*d[0][i]-d[0][k]*p0*c[0][i]
      else:s+=c[0][k]*(q0*d[1][i]+q1*d[0][i])+c[1][k]*q0*d[0][i]-d[0][k]*(p0*c[1][i]+p1*c[0][i])-d[1][k]*p0*c[0][i]
     z[i]=s
    val.append(z)
   if m in out:out[m]=tuple(out[m][i]+val[i] for i in range(2))
   else:out[m]=tuple(val)
 return out
def project(H):
 x0=P({k:v[0] for k,v in H.items()});x1=P({k:v[1] for k,v in H.items()})
 return {k:(x0.get(k,S.zeros(3,3)),x1.get(k,S.zeros(3,3))) for k in set(x0)|set(x1)}
A=mk(C1);B=mk(C2);h=mk(h)
br=Br(A,B)
def L(C,H):return Lie(C,efactor(H))
KC=add(add(L(A,L(B,h)),L(B,L(A,h)),-1),L(br,h),-1)
KB=project(KC)
for name,X in [('C',KC),('B',KB)]:
 print('CHANNEL',name,'modes',len(X))
 zz=S.Rational(0)
 for k,(v0,v1) in X.items():
  if any(c!=0 for c in v0):print('FAIL0',k,v0);break
  zz+=sum(v1[i,j]*S.conjugate(v1[i,j]) for i in range(3) for j in range(3))/6
 zz=S.factor(zz)
 print('R_SQ_ALPHA',zz)
 expected= ((1007*a*a+154*a+11)/S.Integer(4800000000)) if name=='C' else ((1213*a*a-8*a+2)/S.Integer(43200000000))
 assert S.simplify(zz-expected)==0
 for alpha in (0,S.Rational(1,20),S.Rational(1,5)):
  z=S.sqrt(zz.subs(a,alpha))*(2*S.pi)**2
  print('alpha',alpha,'N2_RMS_COEFF',S.N(z,16),'RATIONAL_SQ_FACTOR',S.factor(zz.subs(a,alpha)))
print('elapsed',time.time()-start)

# Exactly evaluate the limiting spectral K_A squared-energy surface profiles.
# First calculate K_A as an ambient, pure-trace, continuum projected-Lie residual.
base=runpy.run_path(str(ROOT/'verify_m13_rot26_exact.py'))
Aa=base['a']
G=S.Rational(0);surfaces=[]
for m,x in Aa.items():
 for n,y in Aa.items():
  if m==n:G+=sum(x[i,j]*S.conjugate(y[i,j]) for i in range(3) for j in range(3))/6
for dim in range(3):
 p=S.Rational(0)
 for m,x in Aa.items():
  for n,y in Aa.items():
   if all(m[j]==n[j] for j in range(3) if j!=dim):
    p+=sum(x[i,j]*S.conjugate(y[i,j]) for i in range(3) for j in range(3))/6
 surfaces.append(S.simplify(p))
assert G==S.Rational(5917501,3499200000000000)
expected_s=[S.Rational(761233367,314928000000000000),S.Rational(1409179,656100000000000),S.Rational(123982963,62985600000000000)]
assert surfaces==expected_s
relative_c=S.factor(3*(3-sum(surfaces)/G))
assert relative_c== -S.Rational(229914416,88762515)
print('K_A_LIMIT_GLOBAL_RMS_SQ',G)
print('PLANE_PROFILE_SQUARED',surfaces)
print('PLANE_RATIOS_TO_BULK',[S.factor(v/G) for v in surfaces])
print('K3_N_INV_RELATIVE_COEFFICIENT',relative_c)
print('K3_N_INV_ABSOLUTE_COEFFICIENT',S.simplify(relative_c*S.sqrt(G)),S.N(relative_c*S.sqrt(G),18))
print('ROT27_EXACT_PASS')