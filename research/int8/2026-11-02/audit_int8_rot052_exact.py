#!/usr/bin/env python3
"""INT8-052 independent symbolic all-odd-grid rank certificate; no NumPy or DTC0a import."""
import argparse, json, math
from itertools import product
from pathlib import Path
import sympy as sp
T,W=sp.symbols('t w',real=True)
a=sp.Matrix([1,2,0]);b=sp.Matrix([2,-1,0]);ez=sp.Matrix([0,0,1]);sa=sp.Matrix([1,T,0]);sb=sp.Matrix([T,-1,0])

def sym(u,v):return u*v.T+v*u.T

def P(H,k):
 Q=sp.eye(3)-k*k.T/(k.dot(k))
 return sp.expand(Q*H*Q-sp.trace(Q*H)*Q/2)

def tt_measurements(H,k):
 kx,ky,ell=k
 v=sp.Matrix([-ky,kx,0]);u=sp.Matrix([-ell*kx,-ell*ky,kx*kx+ky*ky])
 B1=sym(v,u);B2=v*v.T*u.dot(u)-u*u.T*v.dot(v)
 assert sp.expand(k.dot(v))==sp.expand(k.dot(u))==0
 assert sp.expand(sp.trace(B1))==sp.expand(sp.trace(B2))==0
 return [sp.expand(sp.trace(H*B1)),sp.expand(sp.trace(H*B2))]

def transfer(S,ta,tb):
 kb=tb*b+sp.Matrix([0,0,W]);ka=ta*a+sp.Matrix([0,0,W]);k=ta*a+tb*b+sp.Matrix([0,0,W])
 HB=P(tb*W*S+sym(S*ez,sb),kb)
 HA=P(ta*W*S+sym(S*ez,sa),ka)
 unprojected=ta*W*HB+sym(HB*ez,sa)-tb*W*HA-sym(HA*ez,sb)
 # These TT tests are in the RANGE of P_k; the omitted final P_k is exactly self-adjoint.
 return tt_measurements(unprojected,k)

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--out',required=True);args=parser.parse_args()
 F=[]
 for i in range(3):
  S=sp.zeros(3);S[i,i]=1;F.append(S)
 for i,j in [(0,1),(0,2),(1,2)]:
  S=sp.zeros(3);S[i,j]=S[j,i]=1;F.append(S)
 rows=[]
 for ta,tb in product((1,-1),repeat=2):
  values=[transfer(S,ta,tb) for S in F]
  for z in range(2):rows.append([sp.factor(x[z]) for x in values])
 M=sp.Matrix(rows);idx=(0,1,3,4,5,7)
 det=sp.factor(M[list(idx),:].det(method='domain-ge'))
 r=W**2
 Fcritical=(T-2)*r**2+(10*T-15)*r+5*T-10
 P1=10*T+r**2+10*r+5
 P2=20*T+2*r**2+15*r+10
 A=20*r**4+624*r**3+6520*r**2+25200*r+36500
 B=16*r**5+416*r**4+3304*r**3+7120*r**2-13800*r-56000
 C=4*r**6+88*r**5+688*r**4+2496*r**3+6805*r**2+23050*r+44125
 Q=A*T**2+B*T+C
 expected=sp.Rational(128000000000000)*W**6*(T-2)**4*(2*r+5)*P1*P2*Fcritical*Q/(r+5)**10
 assert sp.factor(det/expected)==1, 'FULL symbolic determinant factor FAIL'
 # Exact adversarial controls: F really can vanish at artificial (t,w), and ell=0 has rank3.
 assert M.subs({T:sp.Rational(27,16),W:sp.Integer(1)}).rank()==5
 assert M.subs({T:sp.Rational(3,2),W:sp.Integer(0)}).rank()==3
 assert M.subs({T:sp.Rational(3,2),W:sp.Integer(1)}).rank()==6
 discr=sp.factor(B**2-4*A*C)
 D_expected=-16*(r+5)**2*(2*r**4+48*r**3+485*r**2+2150*r+2875)**2
 assert sp.expand(discr-D_expected)==0
 # A(r)>0 and discriminant<0 for real r>=0: Q(t,r)>0 for all real t.
 assert all(c>0 for c in sp.Poly(A,W).all_coeffs() if c!=0)
 # For t'<0, all coefficients in F(t',w') as polynomial in w'^2 are <0.
 # For odd N, (N-1)//2 is coprime to N and maps 2cos(2pi/N) to -2cos(pi/N).
 samples=[]
 for N in range(7,102,2):
  j=(N-1)//2;assert math.gcd(j,N)==1
  tm=-2*math.cos(math.pi/N)
  for ell in sorted(set([1,2,j])):
   # w' is a real Galois conjugate of U_{ell-1}(t/2).
   wm=float(sp.chebyshevu(ell-1,sp.Float(tm/2,30)))
   ff=(tm-2)*wm**4+(10*tm-15)*wm**2+5*tm-10
   assert ff<0
   samples.append({'N':N,'ell':ell,'critical_factor_at_negative_conjugate':round(ff,6)})
 # Original output Fourier kxy norms are all 10; intermediate ones 5.
 assert all(sum(x*x for x in (ta*a+tb*b)[:2])==10 for ta,tb in product((1,-1),repeat=2))
 result={'artifact_id':'IW_INT8_ROT052_ALL_ODD_N_GEOMETRIC_RANK_CERT_20261102','status':'SYMBOLIC_ALL_N_THEOREM_PASS',
 'chosen_tt_measurement_rows':list(idx),'symbolic_measurement_matrix_shape':[8,6],
 'determinant_factorization_verified':True,
 'determinant_factorization':str(expected),'nontrivial_factor_F':str(Fcritical),
 'quadratic_Q':str(Q),'quadratic_discriminant':str(D_expected),
 'Q_positive_certificate':'A(r)>0, discriminant(t)=-16(r+5)^2*(2r^4+48r^3+485r^2+2150r+2875)^2<0 for all r>=0',
 'F_nonzero_proof':'For odd N, j=(N-1)/2 coprime to N. Algebraic conjugate t_prime=2cos(2pi*j/N)=-2cos(pi/N)<0. Since w=U_(ell-1)(t/2) in Z[t], vanishing F(t,w) would imply vanishing F(t_prime,U_(ell-1)(t_prime/2)), but every coefficient of polynomial in w_prime^2 is negative at t_prime<0. Contradiction.',
 'adversarial_exact_controls':{'artificial_t_27_over_16_w_1_rank':5,'zero_harmonic_w_0_rank':3,'off_zero_t_3_over_2_w_1_rank':6},'sampling_only_nonproof':samples,'sample_count':len(samples),
 'conclusion':'For every odd N>=7 and every nonzero ell in signed cube, rank_C G_ell=6. Combined with ROT050 rank3 at ell0 and ROT051 only two stable e_shell zeros: real ker dim3 generally, dim15 at (N7,alpha1/7) and (N9,alpha1/6).',
 'scope':'Source-auxiliary K_A_out, two fixed z-shears and H(z). No historic masked K_A or physical upgrade.'}
 Path(args.out).write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n',encoding='utf8')
 print('EXACT_ALL_N_PASS 8x6 tensor moments, 6x6 determinant, negative quadratic discriminant and Galois factor;',len(samples),'nonproof sanity tests')
if __name__=='__main__':main()
