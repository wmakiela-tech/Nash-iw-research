#!/usr/bin/env python3
"""XH-S7 ROT007: original Badacz REVIEW078 published four-decimal kernel values.
Exact finite rational two-pulse counterexample and 0.00005 display-rounding guards.
NOT a native source history, physical PBH result, or numerical BBN solver rerun.
Source: research/badacz/2026-11-20/IW_BADACZ_B1_RESPONSE_GAIN_REVIEW_078_20261120.md
"""
from fractions import Fraction as Q
import json
E=Q("0.8024") # G_net at T=0.8 MeV
L=Q("1.7143") # G_net at T=0.105 MeV
EC=Q("0.8538") # G_code at T=0.8 MeV
LC=Q("2.2027") # G_code at T=0.105 MeV
r=Q("0.00005") # only assumed rounding of four decimal digits
def net(k): return E-L*k
def code(k): return EC-LC*k
def box_net(k): return [E-r-(L+r)*k, E+r-(L-r)*k]
def box_code(k): return [EC-r-(LC+r)*k, EC+r-(LC-r)*k]
k=Q("0.46")
kright=Q("0.47")
assert all(x>0 for x in box_net(k))
assert all(x<0 for x in box_code(k))
assert all(x<0 for x in box_net(kright))
assert all(x<0 for x in box_code(kright))
assert all(x<0 for x in box_code(Q("0.465")))
k_cancel=E/L
assert Q("0.46")<k_cancel<Q("0.47")
assert net(k_cancel)==0 and code(k_cancel)<0
assert EC/E>1 and LC/L>1
# For two nonnegative impulse weights, R is a weighted mean of the two point gains.
for lweight in [Q(0),Q("0.1"),Q(1),Q(10)]:
    R=(EC+LC*lweight)/(E+L*lweight)
    assert min(EC/E,LC/L)<=R<=max(EC/E,LC/L)
def asfloat(x): return float(x)
result={
 "science_class":"CONDITIONAL_LINEAR_RESPONSE_TWO_PULSE_FALSIFIER_NOT_PBH_DATA",
 "temperature_early_MeV":0.8, "temperature_late_MeV":0.105,
 "G_net_early":asfloat(E),"G_net_late":asfloat(L),
 "G_code_early":asfloat(EC),"G_code_late":asfloat(LC),
 "nonnegative_two_point_ratio_range":[asfloat(EC/E),asfloat(LC/L)],
 "source_impulses_in_neutron_fraction_units":["+epsilon", "-0.46*epsilon"],
 "signed_impulse_net_response_over_epsilon":asfloat(net(k)),
 "signed_impulse_code_response_over_epsilon":asfloat(code(k)),
 "signed_response_ratio":asfloat(code(k)/net(k)),
 "source_late_early_cancellation_exact_rational":str(k_cancel),
 "source_late_early_cancellation_value":asfloat(k_cancel),
 "code_response_over_epsilon_at_net_zero":asfloat(code(k_cancel)),
 "rounding_assumption":"published four-decimal values rounded to nearest, error at most 0.00005 each",
 "rounded_values_net_bounds_k046":list(map(asfloat,box_net(k))),
 "rounded_values_code_bounds_k046":list(map(asfloat,box_code(k))),
 "rounded_values_net_bounds_k047":list(map(asfloat,box_net(kright))),
 "rounded_values_code_bounds_k047":list(map(asfloat,box_code(kright))),
 "mathematical_gate":"for every permitted rounded set, a net-zero ratio k exists in (0.46,0.47) while code remains negative",
 "limitations":["linear-response assumption; epsilon sufficiently small",
                "kernels are published 2026 Badacz source model approximations not new I1",
                "the two-impulse signed source is hypothetical, not demonstrated for any native PBH trace",
                "does not reproduce Badacz original network or Mech T2R and does not establish physical PBH bound",
                "global 77-parameter BBN atlas is NOT an injection-time response kernel"]
}
print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
