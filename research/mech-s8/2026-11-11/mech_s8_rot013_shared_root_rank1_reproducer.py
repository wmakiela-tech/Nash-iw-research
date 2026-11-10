#!/usr/bin/env python3
"""Mech-S8 ROT013, root-level shared-baseline rank-one countermodel.

Sources: BADACZ REVIEW050 original kernel_analysis.json,
wmakiela-tech/Nash-iw-research commit 11eeb1c37c21f19b2510e3bba5ae50169cbd5d79,
Git blob 1df29aff025755f9042628ec85752178b991d398.
Transcribed only: `configs` (base_j, C2_j, D2_j, D0_j), root and SE.
SE = numerical seven-point linear-fit estimates, NOT rigorous intervals,
NOT independent statistical confidence bounds, NOT physical model/systematic error.

The same base root b_j is used for C2, D2, D0 within each j.
Conditionally assumes affine band response in the root-inferred 10**(-Delta)
source coefficient under k=0/2, not a proven joint source simulation.
Python 3.8+ standard library, offline.
"""
import json, math
from pathlib import Path
DATA = {
 22: {"B":(-17.219677940232263,0.005522413653601175),
      "C":(-17.3440160581744,0.0030480927626177993),
      "D2":(-17.25219558798461,0.002688499247478976),
      "D0":(-17.185507770724637,0.003000165000411359)},
 28: {"B":(-18.36103744053763,0.0021347922336004965),
      "C":(-18.419476504569705,0.003252054986544184),
      "D2":(-18.37261097069877,0.0019126371095701156),
      "D0":(-18.351592991229108,0.001981287635689311)},
 34: {"B":(-18.833796150513802,0.002640655637085262),
      "C":(-18.86408139182946,0.0014672765447464316),
      "D2":(-18.839688455518942,0.002504627630983868),
      "D0":(-18.825692259663057,0.003157234837791879)},
 62: {"B":(-19.394162209551205,0.002171693472415809),
      "C":(-19.39840763398707,0.0018335399862307977),
      "D2":(-19.39357450068686,0.0013607308346243474),
      "D0":(-19.392017391494527,0.0018701196842160885)},
}
# A deliberately simple explicit witness, not a fit-derived "true response".
# B_j/C_j shifts are in units of their OWN root-fit SE. D0/D2 shifts derived.
SHIFT_B_C = {
 22: (-0.075, -0.860),
 28: (-0.565, +0.860),
 34: (+0.218, -0.218),
 62: (+0.429, +0.429),
}
Q = 0.210
MAX_ALLOWED_ROOT_FIT_SE = 0.900
def response(b, r, k):
    assert k in (0, 2)
    return (10.0 ** (b-r) - 1.0)/(k-1.0)
def joint_shift(c, d):
    return -math.log10(1.0+c+d)

results = {}
max_norm = 0.0
for j, obs in DATA.items():
    B,C,D2,D0 = (obs[k] for k in ("B","C","D2","D0"))
    x,y = SHIFT_B_C[j]
    b = B[0]+x*B[1]
    croot = C[0]+y*C[1]
    sC = response(b,croot,2)
    sD = Q*sC
    assert sC>0 and 0<sD<1
    # DEFINE root-compatible k=2 and k=0 evaluations with SAME baseline:
    root_d2 = b-math.log10(1.0+sD)
    root_d0 = b-math.log10(1.0-sD)
    z_d2 = (root_d2-D2[0])/D2[1]
    z_d0 = (root_d0-D0[0])/D0[1]
    z = {"B":x,"C":y,"D2":z_d2,"D0":z_d0}
    max_norm = max(max_norm,*map(abs,z.values()))
    assert abs(response(b,root_d2,2)-sD)<1e-12
    assert abs(response(b,root_d0,0)-sD)<1e-12
    assert abs(sD-Q*sC)<1e-14
    assert all(abs(t)<MAX_ALLOWED_ROOT_FIT_SE for t in z.values())
    nominal_sC = response(B[0],C[0],2)
    nominal_sD2 = response(B[0],D2[0],2)
    nominal_sD0 = response(B[0],D0[0],0)
    results[str(j)]={
      "nominal": {"s_C2":nominal_sC,"s_D2":nominal_sD2,
         "s_D0":nominal_sD0,
         "joint_C2_D2_surrogate_dex":joint_shift(nominal_sC,nominal_sD2)},
      "alternative_shared_base_roots":
         {"B":b,"C2":croot,"D2":root_d2,"D0":root_d0},
      "root_deltas_in_individual_fit_SE":z,
      "alternative_response":
         {"s_C":sC,"s_D_from_D2":response(b,root_d2,2),
          "s_D_from_D0":response(b,root_d0,0),
          "s_D_div_s_C":sD/sC,
          "joint_C_D_surrogate_dex":joint_shift(sC,sD)}
     }
assert len(results)==4
assert max_norm<0.9
summary={
 "status":"PASS_CONDITIONAL_ROOT_LEVEL_RANK_ONE_EXISTENCE",
 "return_id":"IW_MECH_S8_ROT013_WUXU_C_D_SHARED_BASE_D0_D2_ROOT_SE_RANKONE_FALSIFIER_001_20261110",
 "source":{"repo":"wmakiela-tech/Nash-iw-research","commit":"11eeb1c37c21f19b2510e3bba5ae50169cbd5d79",
           "source_path":"research/badacz/2026-11-08/data/kernel_analysis.json",
           "git_blob":"1df29aff025755f9042628ec85752178b991d398"},
 "witness": {"q_sD_over_sC":Q,
             "max_abs_nominal_root_fit_SE":max_norm,
             "criterion_less_than":MAX_ALLOWED_ROOT_FIT_SE,
             "roots_within_criterion":16,
             "same_baseline_for_all_three_variants_per_j":True,
             "D0_and_D2_constrained_to_same_sD":True,
             "exact_column_rank_one_by_construction":True},
 "cases":results,
 "claim_ceiling":"HYPOTHETICAL_PER_ROOT_FIT_SE_BOX_EXISTENCE_ONLY / NOT_STATISTICAL_CONFIDENCE / NOT_NATIVE_JULIA_DOUBLE_BAND / NOT_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN"
}
if __name__=="__main__":
    print(json.dumps(summary,indent=2,sort_keys=True,allow_nan=False))
