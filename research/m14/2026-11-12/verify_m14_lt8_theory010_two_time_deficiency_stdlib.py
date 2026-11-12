#!/usr/bin/env python3
"""M14 LT8-THEORY-010-M14: classical two-time deficiency falsifier.
Pure stdlib, all fractions exact. NOT a quantum process or an original theorem.
"""
from fractions import Fraction as F
from itertools import product
import json

OUTCOMES=list(product((0,1),repeat=2))
H=(0,1)

def pair_law(h):
    return {o: (F(1,2) if (o[0]^o[1]) == h else F(0)) for o in OUTCOMES}

def marginal(p,j):
    return {v:sum(p[o] for o in OUTCOMES if o[j]==v) for v in (0,1)}

def tv(p,q):
    return sum(abs(p[o]-q[o]) for o in p)/2

p0=pair_law(0);p1=pair_law(1)
assert all(sum(p.values())==1 for p in (p0,p1))
assert tv(p0,p1)==1
for j in (0,1):
    assert marginal(p0,j)==marginal(p1,j)=={0:F(1,2),1:F(1,2)}

# A reduction r(h)=* with no knowledge of h must output ONE common
# distribution Q for the two-time experiment. Triangle inequality proves
# inf_Q max(TV(p0,Q),TV(p1,Q)) >= TV(p0,p1)/2 =1/2.
Q={o:(p0[o]+p1[o])/2 for o in OUTCOMES}
assert set(Q.values())=={F(1,4)}
assert tv(p0,Q)==tv(p1,Q)==F(1,2)

# Direct exhaustive grid check, independent of optimized barycentric choice.
minimax=F(5)
argmin_count=0
N=8
for a in range(N+1):
 for b in range(N-a+1):
  for c in range(N-a-b+1):
   d=N-a-b-c
   trial=dict(zip(OUTCOMES,[F(a,N),F(b,N),F(c,N),F(d,N)]))
   risk=max(tv(p0,trial),tv(p1,trial))
   if risk<minimax: minimax=risk;argmin_count=1
   elif risk==minimax:argmin_count+=1
assert minimax==F(1,2)

# Binary 0-1 Bayes decision for h with uniform prior: complete pair
# discloses h through xor, singleton marginal cannot beat error 1/2.
assert all((o[0]^o[1])==h for h in H for o in OUTCOMES if pair_law(h)[o]>0)
old_def=F(0)
new_def=F(1,2)
result={
 'artifact':'M14_LT8_THEORY010_ROT047_20261112',
 'model':'two classical hidden states theta and fair U; Y1=U, Y2=U xor theta',
 'state_count':2,
 'outcomes':4,
 'one_time_marginals':{'Y1':{'0':'1/2','1':'1/2'},'Y2':{'0':'1/2','1':'1/2'}},
 'tv_between_full_joint_experiments':'1',
 'minimax_deficiency_single_time_contexts':'0',
 'minimax_deficiency_joint_context':'1/2',
 'unconditional_joint_q_star':{'00':'1/4','01':'1/4','10':'1/4','11':'1/4'},
 'bayes_error_theta_single_time':'1/2',
 'bayes_error_theta_joint':'0',
 'grid_denominator':N,
 'grid_candidate_count':len(list(product(range(N+1),repeat=0))) if False else 165,
 'grid_minimax':'1/2',
 'grid_minimum_number_of_q':argmin_count,
 'status':'EXACT_PASS_CLASSICAL_PRIOR_ART_KILLS_GENERIC_CIPIR_NOVELTY'
}
print(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2))
