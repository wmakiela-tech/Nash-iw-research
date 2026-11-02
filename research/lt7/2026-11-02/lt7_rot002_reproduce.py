#!/usr/bin/env python3
"""LT7 ROT002: deterministic bounded-noise model-discrimination toy. Stdlib only."""
import json
import math
from fractions import Fraction as Q
from pathlib import Path

SQ2 = math.sqrt(2)

def formula(c, s, eps):
    assert c >= 0 and s >= 0 and abs(c*c+s*s-1) < 1e-14
    d = min(1., 2*eps)
    return (1 if d >= c else c*d+s*math.sqrt(1-d*d))/SQ2

def primal_scan(c, s, eps, n=16000):
    d = min(1., 2*eps)
    return max(c*t+s*math.sqrt(max(0,1-t*t))
               for t in (-d+2*d*k/n for k in range(n+1)))/SQ2

angles = ((1.,0.), (0.,1.), (3/5,4/5), (4/5,3/5),
          (1/SQ2,1/SQ2))
noise = (0., 0.01, 0.1, 0.25, 0.6)
errors = [abs(formula(c,s,e)-primal_scan(c,s,e))
          for c,s in angles for e in noise]
assert len(errors)==25 and max(errors)<4e-4

count = 0
max_half_gap = Q(0)
for i in range(-100,101):
    for j in range(-100,101):
        x,y = Q(i,100),Q(j,100)
        if x*x+y*y > 1 or abs(x)>Q(1,5):
            continue
        count+=1
        max_half_gap=max(max_half_gap,abs(x-y)/2)
assert count==8133 and max_half_gap==Q(117,200)
assert float(max_half_gap)<(0.2+math.sqrt(0.96))/2

for e in (0.,0.01,0.1,0.25,0.5):
    assert abs(formula(1.,0.,e)-min(SQ2*e,1/SQ2))<1e-14
assert abs(formula(0.,1.,0.1)-1/SQ2)<1e-14
assert formula(1.,0.,0)==0.

result = {
  'id':'IW_LT7_ROT002_TARGET_ALIGNED_MODEL_DIAGNOSTIC_20261102',
  'source':'s1^2+s2^2 <= 1; full source s observed',
  'targets':'T_A(s)=s1; T_B(s)=s2',
  'diagnostic':'z_A=+(w.s)/2; z_B=-(w.s)/2; |error|<=epsilon',
  'optimal_formula':'min(sqrt(2)*epsilon,1/sqrt(2)) for ||w||<=1',
  'epsilon_0.1_aligned':formula(1.,0.,0.1),
  'epsilon_0.1_orthogonal':formula(0.,1.,0.1),
  'epsilon_0.1_oblique_3_5':formula(3/5,4/5,0.1),
  'epsilon_0.1_sensor_e1':formula(1/SQ2,1/SQ2,0.1),
  'independent_angle_noise_cases':len(errors),
  'max_primal_scan_difference':max(errors),
  'rational_source_checks':count,
  'rational_grid_max_half_gap':str(max_half_gap),
  'status':'PASS / MATURE_CONVEX_GEOMETRY / SYNTHETIC_ONLY'
}
path=Path(__file__).with_name('lt7_rot002_reproduce_result.json')
path.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
