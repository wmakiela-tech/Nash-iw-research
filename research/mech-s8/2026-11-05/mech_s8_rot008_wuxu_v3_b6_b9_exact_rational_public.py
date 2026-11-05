#!/usr/bin/env python3
"""Exact algebra audit of ORIGINAL Wu-Xu arXiv:2509.05618v3 Appendix B.6-B.9.
A manuscript-formula check only; NOT a PBH source, physical BBN or code replay.
Source: https://arxiv.org/html/2509.05618v3 ; Python >=3.8 stdlib.
Compare the polynomials after omitting COMMON G_F**2*m_p**2/16.
"""
from fractions import Fraction as Q
from itertools import product
def b6(v,a,E,N,d): # v3 B.6 substituted using B.7 and B.8
    return ((v+a)**2+(v-a)**2)*E*N+(v*v-a*a)*(E*N-d)
def b9(v,a,E,N,d): # printed v3 B.9
    return (v*v+3*a*a)*E*N+(v*v-a*a)*d
def delta(v,a,E,N,d):
    return 2*(v*v-a*a)*(E*N-d)
NTEST=0
for v,a in product(range(-3,4),repeat=2):
    for e,n,d in [(Q(1),Q(1),Q(0)),(Q(3),Q(4),Q(1,2)),(Q(2),Q(5),Q(10))]:
        assert b6(Q(v),Q(a),e,n,d)-b9(Q(v),Q(a),e,n,d)==delta(Q(v),Q(a),e,n,d)
        NTEST+=1
v=Q(1); a=Q(13,10); e=n=Q(1); d=Q(0)
assert b6(v,a,e,n,d)==Q(469,100)
assert b9(v,a,e,n,d)==Q(607,100)
assert delta(v,a,e,n,d)==Q(-69,50)
assert b6(Q(1),Q(1),e,n,d)==b9(Q(1),Q(1),e,n,d)
print({"exact_tests":NTEST,"B6_nr":str(b6(v,a,e,n,d)),
       "B9_printed":str(b9(v,a,e,n,d)),
       "difference":str(delta(v,a,e,n,d)),
       "status":"MANUSCRIPT_ALGEBRA_DISCREPANCY_ONLY",
       "claims":"NO_PHYSICAL_BOUND/NO_CANON/NO_EXEC_SIGN"})
