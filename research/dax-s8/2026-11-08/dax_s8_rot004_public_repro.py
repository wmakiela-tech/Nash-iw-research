#!/usr/bin/env python3
"""Exact audit of CRPropa DPP two-secondary thinning (source model, not native C++).
Based on CRPropa3 v3.3 EMDoublePairProduction.cpp pinned blob:
682f001a264a741ba9615ed86490d9f216a52cfe.
"""
from fractions import Fraction as F
from itertools import product
from math import ceil
import json


def witness(q, t):
    q, t = F(q), int(t)
    assert q > 2 and t in (0, 1)  # exact rational exponent only, documented range
    eh, f = (q-2)/2, (q-2)/(2*q)
    pe, pp = (1-f)**t, f**t
    weights = []
    for i,j in product((0,1),repeat=2):
        pr = (pe if i else 1-pe)*(pp if j else 1-pp)
        h = eh*(i/pe+j/pp)
        weights.append((i,j,pr,h))
    E = lambda fn: sum(pr*fn(i,j,h) for i,j,pr,h in weights)
    mean_h = E(lambda i,j,h:h)
    var_h = E(lambda i,j,h:h*h)-mean_h*mean_h
    out = {
      'q': str(q), 'thinning': t, 'f': str(f),
      'p_electron': str(pe), 'p_positron': str(pp),
      'P_no_secondaries': str(E(lambda i,j,h:int(i+j==0))),
      'P_both_secondaries': str(E(lambda i,j,h:i*j)),
      'P_at_least_one': str(E(lambda i,j,h:int(i+j>0))),
      'mean_raw_count': str(E(lambda i,j,h:i+j)),
      'mean_weighted_energy':str(mean_h),
      'relative_weighted_energy_variance':str(var_h/mean_h**2),
      'corrected_pair_variance':str(F(1)/(pe*pp)-1),
    }
    assert mean_h == 2*eh
    assert var_h/mean_h**2 == (1/pe+1/pp-2)/4
    return out

plain,thin = witness(12,0),witness(12,1)
assert plain['P_no_secondaries']=='0'
assert plain['relative_weighted_energy_variance']=='0'
assert thin['p_electron']=='7/12'
assert thin['p_positron']=='5/12'
assert thin['P_no_secondaries']=='35/144'
assert thin['P_both_secondaries']=='35/144'
assert thin['P_at_least_one']=='109/144'
assert thin['mean_raw_count']=='1'
assert thin['mean_weighted_energy']=='10'
assert thin['relative_weighted_energy_variance']=='37/70'
assert thin['corrected_pair_variance']=='109/35'
assert ceil(float(F(37,70)*10000))==5286
print(json.dumps({'PASS_EXACT_FRACTION':True,'t0':plain,'t1':thin},indent=2,sort_keys=True))
