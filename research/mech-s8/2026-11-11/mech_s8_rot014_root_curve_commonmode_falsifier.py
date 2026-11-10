#!/usr/bin/env python3
"""Mech-S8 ROT014: vertical-curve shifts and common-mode negative control.

Dependencies: Python >= 3.9 stdlib, the included ROT013 standalone fixture.
Data: Badacz REVIEW050, original pinned `kernel_analysis.json` Git blob
1df29aff025755f9042628ec85752178b991d398, configs with root, se,
`line fit slope`, `sigma_resid`. Source code recorded per 7-point regression.
SE is NOT a rigorous statistical/physical error bound.
This computes conditional algebra, NOT native Julia simulation or physical PBH error.
"""
from __future__ import annotations
import json, math, runpy
from pathlib import Path
from decimal import Decimal, getcontext
getcontext().prec=65
here=Path(__file__).resolve().parent
r13=runpy.run_path(str(here/'mech_s8_rot013_shared_root_rank1_reproducer.py'))
DATA=r13['DATA']; ALTS=r13['results']; q=r13['Q']
# Direct transcription of ORIGINAL `kernel_analysis.json`, configs[*].slope,
# configs[*].sigma_resid, four times four rows j=22,28,34,62 and
# configs base_j, C2_j, D2_j, D0_j. Each has n=7 original fit points.
FIT={
22:{'B':(.0068635167717214386,.00010022373541335079),'C':(.007128729345357588,.00005730201482493582),'D2':(.006742954894818917,.000047906251242929156),'D0':(.007173563521618199,.000055578924631739286)},
28:{'B':(.013869081041657101,.00007757558039880745),'C':(.01398773119168555,.00011851641882580774),'D2':(.013524245957699983,.00006842306644142272),'D0':(.013866641402985325,.00007267810608955356)},
34:{'B':(.01412480629042244,.00009841639570040989),'C':(.013868119636143596,.00005377845761662449),'D2':(.014185539674344131,.00009264352451795312),'D0':(.014243558602742769,.00011875663233484411)},
62:{'B':(.014186324245600434,.00008120532938616468),'C':(.01437158246660725,.00006970879221906887),'D2':(.014653785972629766,.00005156853387495272),'D0':(.0143774576432504,.0000698891530388489)}
}

def dd(x):return Decimal(str(x))
def dexp10(x):return (dd(10).ln()*x).exp()

def global_common_yc_enclosure(j):
    # One common Y_C offset h within this row, inducing root r'_g=r_g-h/slope_g.
    # Restrict h so ALL four roots move <= ONE original marginal root-fit SE.
    R=DATA[j]; F=FIT[j]
    hlim=min(dd(R[g][1])*dd(F[g][0]) for g in R)
    b,d2,d0=[dd(R[g][0]) for g in ['B','D2','D0']]
    slope_b,slope_d2,slope_d0=[dd(F[g][0]) for g in ['B','D2','D0']]
    t2=dd(1)/slope_d2-dd(1)/slope_b
    t0=dd(1)/slope_d0-dd(1)/slope_b
    # Algebraically exact enclosure: each positive exponential term is bounded
    # individually by +/- |t| hlim. Sum bounds are conservative and may be wider
    # than the true correlated-h range, so a sign-stable enclosure is sufficient.
    low=dexp10(b-d2-abs(t2)*hlim)+dexp10(b-d0-abs(t0)*hlim)-2
    high=dexp10(b-d2+abs(t2)*hlim)+dexp10(b-d0+abs(t0)*hlim)-2
    assert low>0 or high<0
    return {'common_h_abs_max':str(hlim),
            'enclosure_s_D2_minus_s_D0':{'low':str(low),'high':str(high)},
            'excludes_zero':True,
            'reason':'one common Y_C offset per j cannot exactly reconcile D0 and D2 under <=1 original root-fit-SE per configuration'}

result={'return_id':'IW_MECH_S8_ROT014_WUXU_CURVE_SHIFT_VS_COMMON_YC_CALIBRATION_FALSIFIER_001_20261111',
'status':'PASS_TWO_DIFFERENT_ERROR_MODELS_SEPARATED',
'source':{'owner':'Badacz REVIEW050','commit':'11eeb1c37c21f19b2510e3bba5ae50169cbd5d79','git_blob':'1df29aff025755f9042628ec85752178b991d398','data_kind':'7-point linear-fit root, marginal SE, slope and RMS regression residual per configuration'},
'offset_curve_witness':{}, 'common_mode_enclosures':{},
'ceiling':'SOURCE_FIT_METADATA_AND_CONDITIONAL_REGRESSION_ALGEBRA_ONLY/NO_NATIVE_JULIA_REPLAY/NO_PHYSICAL_ERROR_DISTRIBUTION/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN'}
maxratio=0.0
for j in DATA:
    result['offset_curve_witness'][str(j)]={}
    for name,(orig,se) in DATA[j].items():
        alt=ALTS[str(j)]['alternative_shared_base_roots'][{'B':'B','C':'C2','D2':'D2','D0':'D0'}[name]]
        slope,sigma=FIT[j][name];root_shift=alt-orig
        # On original 7 pairs (x_i,y_i), y'_i=y_i+delta_y, CONSTANT over all i
        # leaves c1=slope and regression residuals identical; root r'=r-delta_y/slope.
        delta_y=-slope*root_shift
        ratio=abs(delta_y)/sigma
        maxratio=max(maxratio,ratio)
        assert abs(root_shift/se)<.9
        assert ratio<.34
        result['offset_curve_witness'][str(j)][name]={
            'root_shift_in_original_fit_se':root_shift/se,
            'constant_shift_each_of_seven_Yc_values':delta_y,
            'abs_shift_div_original_sigma_resid':ratio,
            'slopes_and_regression_residuals_unchanged_exactly_under_constant_translation':True}
    result['common_mode_enclosures'][str(j)]=global_common_yc_enclosure(j)
assert maxratio<.334
assert len(result['offset_curve_witness'])==4
result['summary']={
 'root_configs':16,'seven_points_per_config':7,'hypothetically_shifted_Yc_points':112,
 'max_abs_curve_Yc_shift_over_original_fit_residual_sigma':maxratio,
 'constant_per_curve_translation_rank1_algebra_compatible':True,
 'one_common_Yc_offset_per_j_D0_D2_exact_consistency_possible':False,
 'interpretation':'The witness requires differential curve-level errors, NOT a single common additive calibration offset; no physical attainability or statistical confidence established.'}
if __name__=='__main__':
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))
