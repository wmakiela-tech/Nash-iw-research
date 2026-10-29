#!/usr/bin/env python3
"""MT14 ROT015: exact algebra checks, NOT upstream Wu-Xu Julia runtime."""
from fractions import Fraction as F
import json
from pathlib import Path

g_early, g_late = F(11,2), F(2)
heating = g_early / g_late
code_early_relative_to_physical_if_late_matched = 1 / heating
assert heating == F(11,4)
assert code_early_relative_to_physical_if_late_matched == F(4,11)

cases = []
for name, cube_aT_ratio in (
    ('conformal_aT_constant', F(1)),
    ('PBH_entropy_injection_3_over_2', F(3,2)),
    ('idealized_electron_positron_heating', heating),
    ('cooling_without_adiabaticity', F(7,5)),
):
    ratio = cube_aT_ratio
    assert ratio == F(1) if name == 'conformal_aT_constant' else ratio != F(1)
    cases.append({'name':name, 'code_comoving_baryon_final_over_initial':str(ratio), 'conserved_baryon_ratio':'1', 'relative_defect':str(ratio-F(1))})

assert (g_early / g_late) * (g_late / g_early) == 1
result={'artifact_id':'IW_MT14_ROT015_BARYON_CONTINUITY_FRACTION_CHECK',
        'scope':'SYNTHETIC EXACT COMOVING BARYON CONSERVATION; NO JULIA/PHYSICAL RATE REPLAY',
        'WuXu_frozen_code_assumption':'eta_B=6.1e-10 constant, n_gamma proportional to T^3, n_B=eta_B*n_gamma',
        'idealized_EM_gs_high':str(g_early), 'idealized_EM_gs_low':str(g_late),
        'idealized_photon_heat_factor_cubed':str(heating),
        'early_nB_code_over_true_if_calibrated_late':str(code_early_relative_to_physical_if_late_matched),
        'cases':cases, 'PASS':True}
Path(__file__).with_name('baryon_continuity_results.json').write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('PASS baryon continuity exact, 4 scenarios; 11/4 and 4/11 exact')
