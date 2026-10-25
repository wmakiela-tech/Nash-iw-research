#!/usr/bin/env python3
"""M13 ROT39: three-channel nearest-boundary side-switch of full five-mask profile.
Source-direct outward intervals; certifies sign of both endpoint comparisons
and root isolation, not global argmin for arbitrary alpha0.
"""
import json, csv, math
import mpmath
from fractions import Fraction
from pathlib import Path
from mpmath import iv
from verify_m13_rot33_interval import tensor_polys, quartic, polymul
iv.dps=45
Z=iv.mpf(0); O=iv.mpf(1);DEL=O/100;ROOT=Path(__file__).resolve().parent
N=41;ks=list(range(2,7));n=[(N-2*k)**3 for k in ks];v=[n[i]-n[i+1] for i in range(4)]+[n[4]]

def pp(p,x):
 a=Z
 for t in reversed(p):a=a*x+t
 return a

def pa(a,b):
 return [(a[i] if i<len(a) else Z)+(b[i] if i<len(b) else Z) for i in range(max(len(a),len(b)))]

def ps(p,k):return [x*k for x in p]
def sub(a,b):return pa(a,ps(b,-1))
def conv(a,b):return polymul(a,b)
def der(p):return [p[i]*i for i in range(1,len(p))]
def sqr(p):return conv(p,p)

def tshift(p,t):
 out=[Z]*len(p)
 for j,c in enumerate(p):
  for k in range(j+1):out[k]+=c*math.comb(j,k)*t**(j-k)
 return out

def shells(g):return [ps(sub(ps(g[i],n[i]),ps(g[i+1],n[i+1])),O/v[i]) for i in range(4)]+[g[-1]]

def make_S(poly):
 def side(sign):
  b=[tshift(p,sign*DEL) for p in poly];
  q=[Z]*9
  for i in range(5):q=pa(q,ps(sqr(b[i]),v[i]))
  cr=[]
  for i in range(5):
   for j in range(i+1,5):
    # a_i * (b_j-a_j)/DEL - a_j * (b_i-a_i)/DEL, polynomial, exact stable difference via shifts.
    di=ps(sub(b[i],poly[i]),O/DEL);dj=ps(sub(b[j],poly[j]),O/DEL)
    cr.append(ps(sqr(sub(conv(poly[i],dj),conv(poly[j],di))),v[i]*v[j]))
  numerator=[Z]
  for c in cr:numerator=pa(numerator,c)
  return numerator,q
 Nm,qm=side(-1);Np,qp=side(+1)
 S=sub(conv(Nm,qp),conv(Np,qm))
 return S

def bern(p,a,b):
 degree=len(p)-1;length=b-a
 coef=[sum((p[r]*math.comb(r,j)*a**(r-j)*length**j for r in range(j,degree+1)),Z) for j in range(degree+1)]
 return [sum((coef[j]*iv.mpf(math.comb(i,j))/math.comb(degree,j) for j in range(i+1)),Z) for i in range(degree+1)]

def sign_cert(p,a,b,sign):
 coeff=bern(p,a,b)
 if sign==1:return all(x.a>0 for x in coeff)
 return all(x.b<0 for x in coeff)

def exact_iv(x):
    if isinstance(x,Fraction):return iv.mpf(x.numerator)/x.denominator
    return iv.mpf(x)

def bisect_root(p,lo,hi,iterations=28):
    # Rational dyadic subdivision preserves exact coverage.
    assert pp(p,exact_iv(lo)).b<0 and pp(p,exact_iv(hi)).a>0
    for _ in range(iterations):
        m=(lo+hi)/2;val=pp(p,exact_iv(m))
        if val.b<0:lo=m
        elif val.a>0:hi=m
        else:raise AssertionError('root sign indeterminate')
    assert pp(p,exact_iv(lo)).b<0 and pp(p,exact_iv(hi)).a>0
    return lo,hi

def search_partition(p,a,b,exc_lo=None,exc_hi=None,depth=0):
    # Exact rational endpoints: no uncovered floating-point gaps.
    if exc_lo is not None and a>=exc_lo and b<=exc_hi:return []
    if exc_lo is not None and a<exc_lo<b:return search_partition(p,a,exc_lo,exc_lo,exc_hi,depth+1)+search_partition(p,exc_lo,b,exc_lo,exc_hi,depth+1)
    if exc_lo is not None and a<exc_hi<b:return search_partition(p,a,exc_hi,exc_lo,exc_hi,depth+1)+search_partition(p,exc_hi,b,exc_lo,exc_hi,depth+1)
    aiv,biv=exact_iv(a),exact_iv(b)
    m=(a+b)/2;val=pp(p,exact_iv(m))
    sg=1 if val.a>0 else (-1 if val.b<0 else 0)
    if sg and sign_cert(p,aiv,biv,sg):
        bs=bern(p,aiv,biv)
        return [{'from_rational':str(a),'to_rational':str(b),'certified_sign':sg,'recursive_depth':depth,'minimum_lower_directed':str(min((c.a for c in bs),key=lambda q:float(q))),'maximum_upper_directed':str(max((c.b for c in bs),key=lambda q:float(q)))}]
    if depth>35:raise AssertionError((a,b,'partition failed'))
    return search_partition(p,a,m,exc_lo,exc_hi,depth+1)+search_partition(p,m,b,exc_lo,exc_hi,depth+1)

def run():
 P=tensor_polys(N);cache={};res={}
 for ch,pol in zip('ABC',P):
  g=[quartic(pol,N,k,cache) for k in ks]
  sh=shells(g)
  # Strict shell positivity across the ENTIRE source domain, needed for gain>=0
  # and for the positive denominator of the projective ratio.
  assert all(sign_cert(s,Z,O/5,1) for s in sh),(ch,'source shell positivity')
  shell_min=[str(min((x.a for x in bern(s,Z,O/5)),key=lambda y:float(y))) for s in sh]
  # Independent frozen RMS comparison, not a replacement for source formula proof.
  frozen={(r['alpha'],int(r['interior_k'])):r for r in csv.DictReader((ROOT/'dtc0a_mask_sensitivity_N41_v0_3_1.csv').open())}
  maxrel=0.0
  for k,gk in zip(ks,g):
   for lab,al in [('0.0',Z),('0.05',O/20),('0.2',O/5)]:
    got=math.sqrt(float(pp(gk,al).mid))
    known=float(frozen[lab,k]['K_'+ch+'_RMS'])
    maxrel=max(maxrel,abs(got/known-1))
  assert maxrel<1e-11,(ch,maxrel)
  S=make_S(sh)
  # compare signed endpoints on domain [0.01,0.19], support root enclosure.
  lo=iv.mpf(1)/100;hi=iv.mpf(19)/100
  anchors=[.01,.02,.05,.1,.15,.19]
  f=[(a,float(pp(S,iv.mpf(a)).mid)) for a in anchors]
  print(ch,'endpoint difference S samples',f,flush=True)
  res[ch]={'S_degree':len(S)-1,'float_mid_coefficients_NONPROOF':[float(x.mid) for x in S], 'anchors_NONPROOF':f,'max_frozen_RMS_rel_error':maxrel,'positive_shell_bernstein_lower_directed':shell_min}
  if ch=='B': bracket=(Fraction('0.03265254'),Fraction('0.03265256'))
  elif ch=='C':bracket=(Fraction('0.04366607'),Fraction('0.04366610'))
  else:bracket=None
  if bracket:
   bracket=bisect_root(S,*bracket)
   a,b=map(exact_iv,bracket)
   fl=pp(S,a);fr=pp(S,b)
   print(ch,'root bracket',tuple(map(str,bracket)),'signs',float(fl.mid),float(fr.mid),'derivative sign',sign_cert(der(S),a,b,1),flush=True)
   assert fl.b<0 and fr.a>0 and sign_cert(der(S),a,b,1),ch
   res[ch]['root_bracket_exact_rational']=list(map(str,bracket))
   res[ch]['root_bracket_decimal']=list(map(float,bracket))
   res[ch]['root_S_derivative_Bernstein_min_directed']=str(min((x.a for x in bern(der(S),a,b)),key=lambda y:float(y)))
   res[ch]['source_root_left_directed_interval']=[str(fl.a),str(fl.b)]
   res[ch]['source_root_right_directed_interval']=[str(fr.a),str(fr.b)]
  exc=bracket if bracket else (None,None)
  segs=search_partition(S,Fraction(1,100),Fraction(19,100),*exc)
  if not bracket:assert all(z['certified_sign']==1 for z in segs),ch
  else:
   assert all(z['certified_sign']==-1 for z in segs if Fraction(z['to_rational'])<=bracket[0])
   assert all(z['certified_sign']==1 for z in segs if Fraction(z['from_rational'])>=bracket[1])
  print(ch,'CERTIFIED segments',len(segs),'max depth',max(x['recursive_depth'] for x in segs),'range sign counts', {i:sum(x['certified_sign']==i for x in segs) for i in(-1,1)},flush=True)
  res[ch]['signed_partitions']=segs
 result={'return_id':'M13-ROT39-SOURCE-DIRECT-FIVE-MASK-NEAREST-ENDPOINT-SIDE-SWITCH_001_20261025','mpmath_version':mpmath.__version__, 'interval_precision_digits':iv.dps, 'N':41,'masks':list(ks),'delta':.01,'compared_alpha_range':[.01,.19],'model':'one known channel, one common positive energy gain, five nested masks, source formulas of retained helper','certification':'source-direct outward intervals, exact rational domain partitions, bisection isolation with interval derivative, and strict Bernstein interval sign on every covering interval; mpmath.iv correctness assumed', 'logic':'S(alpha)=N_minus(alpha)*q_plus(alpha)-N_plus(alpha)*q_minus(alpha); global nearest endpoint comparison D(alpha,alpha-.01)^2-D(alpha,alpha+.01)^2 has same sign as S with positive denominator. DOES NOT certify that global minimizer is always one of these endpoints.', 'cases':res,'negative_knowledge':['NOT a global-all-beta minimizer theorem for every true alpha: only comparison of beta=alpha plus/minus delta; ROT38 proved exact full beta argmin only at alpha0=.05','Unknown source generators, gains varying by mask, real voxel noise and physical interpretation not covered','Original byte-exact DTC0a runtime unavailable; no novelty or owner signoff']}
 fn=ROOT/'IW_M13_ROT39_five_mask_side_switch_20261025.json';fn.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n')
 print('ROT39 SIGN PARTITION PASS')
if __name__=='__main__':run()
