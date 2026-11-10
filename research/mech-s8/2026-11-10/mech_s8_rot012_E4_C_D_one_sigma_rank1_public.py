#!/usr/bin/env python3
"""Mech-S8 ROT012: SOURCE-TYPED math recheck of BADACZ REVIEW050 (8 Nov 2026).
Original: wmakiela-tech/Nash-iw-research commit 11eeb1c37c21f19b2510e3bba5ae50169cbd5d79
research/badacz/2026-11-08/data/kernel_analysis.json, Git blob 1df29aff025755f9042628ec85752178b991d398.
Below are verbatim derived[j].s_eff and se_s_eff transcriptions.
SE are FIT summaries; NOT guaranteed physical error bounds. No Julia/BBN run.
Requires numpy: python3 mech_s8_rot012_E4_C_D_one_sigma_rank1_public.py
"""
import json
import numpy as np

S = np.array([
 [0.006607919518822891,0.5660636697157013,0.33149064037701215,0.07657119271096934],
 [0.018898175831667974,0.7925095713860852,0.14403434880811905,0.02417064203027118],
 [0.24335163258786996,0.6152339609846904,0.07222330213977268,0.015854917529929135],
 [0.8749865617677965,0.10057548880223721,0.009823386811443235,0.001448640475406825]
])
U = np.array([
 [0.015961737197394375,0.020908856631092806,0.019338796164578266,0.010053782383820067],
 [0.006766868029692598,0.012265533970673394,0.01024755202092823,0.004714606199266071],
 [0.00971803896596604,0.012860933233379699,0.007458307303623503,0.006272781667606902],
 [0.012314843567321203,0.006719190265903869,0.0066087040141059135,0.004385856661583471]
])
D2=np.array([0.07774904762365242,0.027007298992924644,
 0.013659990316174264,-0.0013523344406164428])
D2_SE=np.array([0.015242227012227355,0.006778080310644534,
 0.008494816550050292,0.005893038700204892])
CD=S[:,2:]
Cstar=CD[:,0].copy()
Cstar[0]+=0.002
Dstar=Cstar/5
pert=np.column_stack([Cstar,Dstar])
ratio=np.abs((pert-CD)/U[:,2:])
ratio_direct=np.abs((Dstar-D2)/D2_SE)
assert np.max(ratio)<1 and np.max(ratio_direct)<1
assert np.all(pert[:,1]==pert[:,0]/5)
assert np.linalg.matrix_rank(pert)==1
sv_all=np.linalg.svd(S,compute_uv=False)
sv_cd=np.linalg.svd(CD[:3],compute_uv=False)
assert abs(sv_all[-1]-0.005170393794909517)<1e-12
assert abs(sv_cd[-1]-0.008150150633078149)<1e-12
unit=CD[:3]/np.linalg.norm(CD[:3],axis=0)
result={
 "status":"PASS_SOURCE_TRANSCRIPTION_CONDITIONAL_MATRIX_INVERSE_ONLY",
 "rows_j":[22,28,34,62],"columns":["A2","B2","C2","Dc"],
 "four_band_singular_values":sv_all.tolist(),
 "four_band_condition":float(sv_all[0]/sv_all[-1]),
 "CD_first_three_singular_values":sv_cd.tolist(),
 "CD_first_three_condition":float(sv_cd[0]/sv_cd[-1]),
 "CD_first_three_column_cosine":float(unit[:,0]@unit[:,1]),
 "rank1_witness_Cstar":Cstar.tolist(),
 "rank1_witness_Dstar":Dstar.tolist(),
 "rank1_witness_rank":int(np.linalg.matrix_rank(pert)),
 "max_abs_fit_SE_ratio_pooled_Dc":float(np.max(ratio)),
 "max_abs_fit_SE_ratio_direct_D2":float(np.max(ratio_direct)),
 "limits":"FIT_SE_NOT_CERTIFIED_BOUNDS/NO_JULIA_REPLAY/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN"
}
print(json.dumps(result,sort_keys=True,indent=2,allow_nan=False))
