#!/usr/bin/env python3
"""Posthoc source-number verification only, not native BBN physics.
Reno & Seckel 1988 PRD37 Table I, charged pion fractions.
Kohri & Yokoyama arxiv:astro-ph/9908160v1 Eq 11,13.
PDG 1998 original Table 38.1 (hadronicrpp_page7.pdf).
"""
import math, json
sqrts=91.2
nch=1.73 + .268*math.exp(1.42*math.sqrt(math.log(sqrts*sqrts)))
ky_pi_each=14.1
ky_k_each=1.67
ky_proton_each=.772
pdg_pi_charge_conjugates_included=17.1
reno_pi_plus_frac=reno_pi_minus_frac=.4230
result={
 "kind":"PUBLISHED_SOURCE_VALUES_ARITHMETIC_NO_NATIVE_RUN",
 "KY_nch_eq11_91p2GeV":nch,
 "KY_pi_each_eq13":ky_pi_each,
 "KY_pi_sum_if_literal_separate_charge":2*ky_pi_each,
 "KY_pi_sum_over_nch":2*ky_pi_each/nch,
 "KY_charged_pi_K_p_pair_count_if_all_literal":2*(ky_pi_each+ky_k_each+ky_proton_each),
 "KY_pi_K_p_over_nch":2*(ky_pi_each+ky_k_each+ky_proton_each)/nch,
 "PDG1998_Table38p1_pi_plus_label_INCLUDES_CHARGE_CONJUGATE":pdg_pi_charge_conjugates_included,
 "KY14p1_div_PDG1998_17p1":ky_pi_each/pdg_pi_charge_conjugates_included,
 "KY14p1_minus_PDG1998_17p1":ky_pi_each-pdg_pi_charge_conjugates_included,
 "RenoSeckel_table_I_fraction_pi_plus":reno_pi_plus_frac,
 "RenoSeckel_table_I_fraction_pi_minus":reno_pi_minus_frac,
 "RenoSeckel_fraction_sum":reno_pi_plus_frac+reno_pi_minus_frac,
 "limitations":["literal per-charge KY Eq13 fails charged subset upper-bound, not author-error proof",
                "KY14.1 exact source transformation from PDG1998 is unresolved",
                "Reno TPC fraction at 29GeV cannot be numerically transplanted to PDG91GeV",
                "Kohri2001 charge-resolved source-code implementation not verified",
                "no new physical PBH bound or novel physics"]
}
assert abs(nch-20.82461855454813)<1.e-10
assert 2*ky_pi_each>nch
assert 2*(ky_pi_each+ky_k_each+ky_proton_each)>nch
assert abs(reno_pi_plus_frac+reno_pi_minus_frac-.8460)<1e-12
assert abs(ky_pi_each/pdg_pi_charge_conjugates_included-0.8245614035087718)<1e-12
print(json.dumps(result,sort_keys=True,indent=2))
