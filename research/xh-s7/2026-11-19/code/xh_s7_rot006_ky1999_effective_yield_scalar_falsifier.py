#!/usr/bin/env python3
"""XH-S7 ROT006: historical source-number arithmetic ONLY.
Kohri-Yokoyama 1999 Eq(11),(13),(14); PDG 1998 Table38.1.
No physical PBH solve, no native Julia/BlackHawk, no author code run.
"""
import math, json
nch=1.73 + .268*math.exp(1.42*math.sqrt(math.log(91.2**2)))
pdg={"pion_charge_conjugates_included":17.1, "kaon_charge_conjugates_included":2.39, "proton_antiproton_included":0.964}
ky={"pion_charge_conjugates_included":14.1, "kaon_charge_conjugates_included":1.67, "proton_antiproton_included":0.772}
ratios={k:ky[k]/pdg[k] for k in pdg}
assert abs(nch-20.82461855454813)<1e-10
assert max(ratios.values())-min(ratios.values())>0.12
assert abs(ratios["pion_charge_conjugates_included"]-0.8245614035087718)<1e-12
assert 14.1<nch<28.2
out={"kind":"POSTHOC_PUBLISHED_NUMBER_ARITHMETIC_ONLY",
"source_ky":"https://arxiv.org/pdf/astro-ph/9908160",
"source_pdg":"https://pdg.lbl.gov/1998/hadronicrpp_page7.pdf",
"nch_91p2GeV_eq11":nch,"pdg1998_charge_conjugates_included_rows":pdg,
"ky1999_eq13_effective_yields":ky,"ky_div_pdg_ratios":ratios,
"one_common_scalar_fits_all_three":False,
"literal_two_distinct_pi_signs_over_charged_total":28.2/nch,
"one_pi_group_14p1_over_charged_total":14.1/nch,
"pdg_pi_group_17p1_over_charged_total":17.1/nch,
"scope":"source-stage and single-scalar negative control; not exact effective-decay transformation, paper error, or PBH bound"}
print(json.dumps(out,indent=2,sort_keys=True))
