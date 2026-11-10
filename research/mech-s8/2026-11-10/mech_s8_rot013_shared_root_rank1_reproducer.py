#!/usr/bin/env python3
"""Mech-S8 ROT013: shared-baseline D0/D2 16-root rank-one witness (stdlib).
Data transcribed from BADACZ REVIEW050 pinned original:
wmakiela-tech/Nash-iw-research @11eeb1c37c21f19b2510e3bba5ae50169cbd5d79
research/badacz/2026-11-08/data/kernel_analysis.json
Git blob 1df29aff025755f9042628ec85752178b991d398.
Inputs are (root, SE) of 7-point source regression; NOT certified/independent
statistical errors or error bars on physical PBH source. No Julia replay.
"""
import json
import math

DATA={
22:{"B":(-17.219677940232263,.005522413653601175),"C":(-17.3440160581744,.0030480927626177993),
    "D2":(-17.25219558798461,.002688499247478976),"D0":(-17.185507770724637,.003000165000411359)},
28:{"B":(-18.36103744053763,.0021347922336004965),"C":(-18.419476504569705,.003252054986544184),
    "D2":(-18.37261097069877,.0019126371095701156),"D0":(-18.351592991229108,.001981287635689311)},
34:{"B":(-18.833796150513802,.002640655637085262),"C":(-18.86408139182946,.0014672765447464316),
    "D2":(-18.839688455518942,.002504627630983868),"D0":(-18.825692259663057,.003157234837791879)},
62:{"B":(-19.394162209551205,.002171693472415809),"C":(-19.39840763398707,.0018335399862307977),
    "D2":(-19.39357450068686,.0013607308346243474),"D0":(-19.392017391494527,.0018701196842160885)}
}
XY={22:(-.075,-.860),28:(-.565,.860),34:(.218,-.218),62:(.429,.429)}
q=.210
out={}
for j,d in DATA.items():
    b0,ub=d["B"];c0,uc=d["C"];d20,ud2=d["D2"];d00,ud0=d["D0"]
    x,y=XY[j]
    b=b0+x*ub;c=c0+y*uc
    sC=10**(b-c)-1
    sD=q*sC
    assert 0<sD<1
    d2=b-math.log10(1+sD)
    d0=b-math.log10(1-sD)
    z2=(d2-d20)/ud2
    z0=(d0-d00)/ud0
    assert max(abs(x),abs(y),abs(z2),abs(z0))<.9
    assert abs((10**(b-d2)-1)-sD)<1e-12
    assert abs((1-10**(b-d0))-sD)<1e-12
    out[j]={"shared_base":b,"C2_root":c,"D2_root":d2,"D0_root":d0,
            "shifts_in_own_nominal_fit_SE":{"base":x,"C":y,"D2":z2,"D0":z0},
            "s_C":sC,"s_D":sD,"ratio_D_over_C":sD/sC,
            "conditional_joint_shift_dex":-math.log10(1+sC+sD)}
assert len(out)==4
result={"status":"PASS_CONDITIONAL_16_ROOTS_SHARED_BASE_D0_D2_RANK1",
        "source_git_blob":"1df29aff025755f9042628ec85752178b991d398",
        "q":q,"cases":out,
        "max_abs_nominal_root_fit_SE":max(abs(v) for c in out.values()
                                          for v in c["shifts_in_own_nominal_fit_SE"].values()),
        "claim_ceiling":"NO_STATISTICAL_CONFIDENCE_NO_NATIVE_JULIA_NO_PHYSICAL_PBH_BOUND_NO_CANON_NO_EXEC_SIGN"}
print(json.dumps(result,sort_keys=True,indent=2,allow_nan=False))
