#!/usr/bin/env python3
"""Independent pure-Fraction positive source/decay/scattering balance toy."""
import json
from fractions import Fraction as F
from pathlib import Path

J,sigma=F(1),F(1)
code_nB, corrected_nB = F(1),F(11,4)
rows=[]
for gamma in [F(0),F(1),F(10),F(100),F(10000)]:
    h_code=J/(gamma+sigma*code_nB)
    h_true=J/(gamma+sigma*corrected_nB)
    ratio=h_code/h_true
    assert h_code>0 and h_true>0 and ratio>=1
    assert ratio==(gamma+sigma*corrected_nB)/(gamma+sigma*code_nB)
    rows.append({'gamma':str(gamma),'h_code':str(h_code),'h_true':str(h_true),'code_over_corrected':str(ratio)})
assert rows[0]['code_over_corrected']=='11/4'
assert rows[1]['code_over_corrected']=='15/8'
assert F(rows[-1]['code_over_corrected']) < F(1001,1000)
result={'artifact_id':'IW_MT14_ROT015_INDEPENDENT_HADRON_RATE_TOY','scope':'EXACT DECLARED STEADY RATE TOY, NOT MECH/WUXU SOLVER', 'rate_equation':'dh/dt=J-(Gamma+sigma*n_B)*h', 'correction_factor':'11/4','rows':rows,'PASS':True}
Path(__file__).with_name('hadron_loss_results.json').write_text(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)+'\n')
print('PASS independent toy hadron-loss exact, 5 decay/scattering regimes')
