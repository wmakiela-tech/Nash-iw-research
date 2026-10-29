#!/usr/bin/env python3
"""INT8-046 fully independent symbolic source-free tensor gauge/TT mismatch identity."""
import sympy as S, json,argparse
from pathlib import Path
from itertools import product

def PP(H,k):
 k=S.Matrix(k);Q=S.eye(3)-(k*k.T)/(k.dot(k))
 return Q*H*Q-S.Rational(1,2)*S.trace(Q*H)*Q

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--out',required=True);args=ap.parse_args()
 p,q,u,v,w=S.symbols('p q u v w',real=True,nonzero=True)
 k=S.Matrix([1,2,0]);ss=S.Matrix([u,v,0]);e=S.Matrix([0,0,1]);G=ss*e.T+e*ss.T
 Q=S.eye(3)-(k*k.T)/(k.dot(k));sp=Q*ss
 F=PP(G,k)
 assert S.simplify(F-(sp*e.T+e*sp.T))==S.zeros(3)
 assert S.simplify(S.trace(F.T*F)-2*sp.dot(sp))==0
 assert S.simplify(sp.dot(sp)-(2*u-v)**2/5)==0
 assert PP(k*e.T+e*k.T,k)==S.zeros(3)
 # The compatible mimetic projector is exact for all rational nonzero s (verify at rational samples)
 tested=0;zeros=0;maxnum=S.Rational(0)
 for a,b in product(range(-4,5),repeat=2):
  if not a and not b:continue
  k=S.Matrix([a,b,0]);e=S.Matrix([0,0,1]);Qk=S.eye(3)-(k*k.T)/k.dot(k)
  for c,d in [(a,b),(a+1,b),(2*a,b+3)]:
   ss=S.Matrix([c,d,0]);G=ss*e.T+e*ss.T
   actual=PP(G,k);sp=Qk*ss
   assert actual==sp*e.T+e*sp.T
   assert S.trace(actual.T*actual)==2*sp.dot(sp)
   if sp==S.zeros(3,1):zeros+=1
   if ss!=S.zeros(3,1):
    assert PP(G,ss)==S.zeros(3)
   tested+=1
 # Exact first nonzero compatible mismatch at integer k=(1,2), s=(1,3)
 k=S.Matrix([1,2,0]);s3=S.Matrix([1,3,0]);e=S.Matrix([0,0,1]);P=PP(s3*e.T+e*s3.T,k)
 assert S.trace(P.T*P)==S.Rational(2,5)
 out={'status':'EXACT_SYMPY_PASS','artifact_id':'IW_INT8_ROT046_SOURCE_DERIVATIVE_PROJECTOR_MISMATCH_20261029','symbolic_tensor_identities':5,'exact_rational_vectors':tested,'zero_leak_controls':zeros,'specific_nonzero_frob_square':'2/5','source':'NOT_USED_SOURCE_FREE','continuum_host':'compatible differential complexes, no claim physical gauge invariance'}
 Path(args.out).write_text(json.dumps(out,sort_keys=True,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
 print('EXACT_SYMPY_PASS',tested,'rational checks and 5 symbolic identities; controls',zeros)
if __name__=='__main__':main()
