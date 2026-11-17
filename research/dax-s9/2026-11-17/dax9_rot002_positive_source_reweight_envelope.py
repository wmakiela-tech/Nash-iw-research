#!/usr/bin/env python3
"""DAX9 ROT002: pure positive-source-reweighting analytic audit. Standard library.
W integrated max-stat 0.83/25.07 from Belle Appendix B, verified ROT001.
DAX8 ROT030/031 frozen conditional q values; not experimental CI.
"""
from math import isclose
E2=13.4071611702
COMPARATOR=12.1835701169
Q10_LEFT=0.979147
Q100_LEFT=0.76184
P10=0.0018870156651242924
def box(q,e):
    assert 0<=q<=1 and 0<=e<1
    lo=(1-e)*q/((1-e)*q+(1+e)*(1-q))
    hi=(1+e)*q/((1+e)*q+(1-e)*(1-q))
    return lo,hi
def mbox(m,e):
    return (1-e)/(1+e)*m,(1+e)/(1-e)*m
for e in (0.83/25.07,0.123):
    print('assumed cap',e,'q10',box(Q10_LEFT,e),
          'q100',box(Q100_LEFT,e),'P10',box(P10,e),
          'E2',mbox(E2,e),'uplift_sign_certified',mbox(E2,e)[0]>COMPARATOR)
ratio=E2/COMPARATOR
print('uplift_eps_sufficient_threshold',(ratio-1)/(ratio+1))
odds=Q10_LEFT/(1-Q10_LEFT)
print('eps_sufficient_for_gt95pct_tail_share',(odds-19)/(odds+19))
# Test common normalization exact cancellation with positive source weights.
w=[0.3,1.0,0.9,2.0]
g=[2.0,0.4,1.2,5.0]
b=sum(a*x for a,x in zip(w,g))/sum(w)
for scale in (0.5,0.9,1.1,2.5):
    v=sum(scale*a*x for a,x in zip(w,g))/sum(scale*a for a in w)
    assert isclose(v,b,rel_tol=1e-14)
print('PASS conditional analytic tests; no source covariance or physical upgrade')
