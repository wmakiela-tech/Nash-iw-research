#!/usr/bin/env python3
"""Separate deterministic positive-gain profiling on published ROT32 quartics."""
import math,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
D=json.loads((ROOT/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').read_text())
C={(r['N'],r['mask_k']):r['G_quartic_squared_RMS'] for r in D['cases']}
def horner(p,a):
    v=0
    for c in reversed(p):v=v*a+c
    return v
def obs(ch,k,a):return math.sqrt(horner(C[41,k][ch],a))
records=[]
for ch,k1,k2 in [('A',2,6),('B',5,6),('C',2,4),('C',2,3)]:
    true_a=.05;alternative_a=.1
    t1=obs(ch,k1,alternative_a)/obs(ch,k1,true_a)
    t2=obs(ch,k2,alternative_a)/obs(ch,k2,true_a)
    s=2/(t1+t2)
    eps=abs(t1-t2)/(t1+t2)
    rels=[s*t1-1,s*t2-1]
    assert abs(abs(rels[0])-eps)<1e-12 and abs(rels[0]+rels[1])<1e-12
    records.append({'channel':ch,'mask1':k1,'mask2':k2,'alpha_true':true_a,'alpha_alternative':alternative_a,'alternative_common_amplitude_best_relative_Linf':s,'minimax_relative_mismatch':eps,'residuals_relative':rels,'alternative_indistinguishable_under_point5_percent_each':eps<.005})
print('GAIN_PROFILED_RESULTS')
for rec in records:print(rec)
assert all(x['alternative_indistinguishable_under_point5_percent_each'] for x in records)
p=ROOT/'IW_M13_ROT34_gain_profile_20261024.json'
p.write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('NOISE_WITNESSES_4_OF_4_PASS')
