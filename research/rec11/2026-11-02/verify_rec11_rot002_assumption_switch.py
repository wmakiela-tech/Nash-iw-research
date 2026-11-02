#!/usr/bin/env python3
"""REC11 ROT002: independent exact-rational negative control for LT7 ROT002.
Only Python standard library. Does not replay source-native physical experiments.
"""
import json
from fractions import Fraction as F
from math import sqrt
from pathlib import Path

N = 90
count = 0
max_error_squared = F(0)
for i in range(-N, N + 1):
    for j in range(-N, N + 1):
        if i*i + j*j > N*N:
            continue
        x, y = F(i, N), F(j, N)
        # w=(1,-1)/sqrt(2), epsilon=0. Source unknown to estimator.
        # For model A, z=(x-y)/(2sqrt(2)), for B the sign reverses.
        # Universal estimator: sqrt(2)*z, so no irrational arithmetic needed.
        pred_A, pred_B = (x-y)/2, -(x-y)/2
        error_A, error_B = x-pred_A, y-pred_B
        assert error_A == error_B == (x+y)/2
        squared = error_A * error_A
        assert squared <= F(1, 2)
        max_error_squared = max(max_error_squared, squared)
        count += 1
assert count == 25445

# Analytic lower witness: s+=(1,1)/sqrt(2), s-=-(1,1)/sqrt(2).
# In either model, z=0 at both sources; targets under A are +/-1/sqrt(2).
# Exact optimal lower radius is therefore 1/sqrt(2).

# Numerical sanity for LT7's known-source formula, using an unrelated derivation.
def risk_known_source(c, epsilon):
    from math import sqrt
    d = min(1., 2.*epsilon)
    q = sqrt(max(0., 1.-c*c))
    return (1. if d >= c else c*d+q*sqrt(1.-d*d))/sqrt(2.)
assert abs(risk_known_source(1., .1)-sqrt(2.)*.1)<1e-14
assert abs(risk_known_source(0., .1)-1./sqrt(2.))<1e-14
assert abs(risk_known_source(1., 0.))<1e-14

result={
  'return_id':'IW_REC11_ROT002_LT7_MODEL_READOUT_FULL_SOURCE_SEPARATOR_001_20261102',
  'role':'independent nonblind exact-rational negative-control and proof',
  'target':'IW_LT7_ROT002_TARGET_ALIGNED_MODEL_DISCRIMINATION_20261102',
  'N':N,'rational_disk_points':count,
  'source_unknown_model_sensitive_oracle_risk_epsilon_zero':'1/sqrt(2)',
  'source_known_model_sensitive_oracle_risk_epsilon_zero':'0',
  'max_rational_grid_squared_error':str(max_error_squared),
  'exact_proof':'w-target-aligned: estimator sqrt(2)*z has error (x+y)/2; antipodal source witness at w.s=0 forces radius 1/sqrt(2)',
  'claim_ceiling':'exact toy only / no physical instrument / no source-native FrontB / no canon / no exec'
}
path=Path(__file__).with_name('rec11_rot002_result.json')
path.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,sort_keys=True))
