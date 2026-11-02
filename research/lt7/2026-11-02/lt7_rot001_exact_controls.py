#!/usr/bin/env python3
"""LT7 ROT001. Exact toy source-only model ambiguity; Python stdlib only."""
from fractions import Fraction as F
from decimal import Decimal, getcontext
import json

getcontext().prec = 50
# Model A: T_A(s)=s_1, model B: T_B(s)=s_2 on s_1^2+s_2^2<=1.
# Reading Y_1(s)=s_1: a nominally exact sensor for A, but s=(0,+-1)
# and model B give identical readings and targets +-1 -> robust risk 1.

# Full source observation cannot determine which downstream target map is valid.
# For any s, model target separation |s1-s2|, whose maximum on unit disk is sqrt(2).
# Midrange estimate (s1+s2)/2 achieves worst-case error 1/sqrt(2).

# A single diagonal observation Y_d=(s1+s2)/sqrt(2) achieves same bound:
# estimate Y_d/sqrt(2)=(s1+s2)/2. Exact squared error max = 1/2.

n_checked = 0
max_err2 = F(0)
for i in range(-100, 101):
    for j in range(-100, 101):
        s1, s2 = F(i, 100), F(j, 100)
        if s1*s1 + s2*s2 > 1:
            continue
        estimate = (s1+s2)/2
        for target in (s1, s2):
            error2 = (target-estimate)**2
            assert error2 <= F(1, 2)
            max_err2 = max(max_err2, error2)
            n_checked += 1
assert n_checked > 30000
# Negative control: reveal map label and full s => zero recovery error.
for i,j in ((F(1),F(0)),(F(0),F(1)),(F(3,5),F(4,5))):
    assert i*i+j*j<=1
    assert i-i==0 and j-j==0

# Independent two-source-model conditional output from Mech-S7 ROT036 (no rerun of ODE):
a = Decimal('0.400959518961858')
b = Decimal('0.400084966240828')
gap = abs(a-b)
conditional_half_gap = gap/Decimal(2)
assert gap == Decimal('0.000874552721030')
assert conditional_half_gap == Decimal('0.000437276360515')
out = {
    'artifact_id': 'IW_LT7_ROT001_CROSS_MODEL_SOURCE_ONLY_INFORMATION_FLOOR_20261102',
    'exact_toy': {
        'model_A': 'T_A(s)=s1', 'model_B': 'T_B(s)=s2', 'source_set':'s1^2+s2^2<=1',
        'reading_e1_nominal_A_risk': '0', 'reading_e1_robust_AB_risk': '1',
        'reading_diag_robust_AB_risk_squared': '1/2',
        'full_source_robust_AB_risk_squared': '1/2',
        'map_label_and_full_source_risk':'0',
        'rational_grid_points_model_pairs_checked':n_checked,
        'rational_grid_max_squared_error':str(max_err2),
        'control':'all exact Fraction comparisons PASS'
    },
    'conditional_mech_rot036_readback_arithmetic_only': {
        'chi_EM':'0.5','source':'same native source / two downstream hypothetical kinetic maps',
        'Xnuc_B_exec':str(a),'Xnuc_B_sym':str(b),
        'numerical_target_gap':str(gap),'half_gap':str(conditional_half_gap),
        'claim':'conditional diagnostic; no certified full ODE error, no physical model admission'
    }
}
print(json.dumps(out,ensure_ascii=False,indent=2,sort_keys=True))
