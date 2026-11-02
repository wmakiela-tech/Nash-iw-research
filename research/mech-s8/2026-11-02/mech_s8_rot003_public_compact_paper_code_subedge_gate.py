#!/usr/bin/env python3
"""Mech-S8 ROT003 compact reproducibility check, Python 3 stdlib only.
Pinned Wu-Xu original repo d395183674cace6c9906a8911bdeb7234ba4040d.
Original 100-row table git blob 06d0883a27b108692720422294ba2baacd381a64.
Two first table rows embedded; full table need not be downloaded for this
first-interval check. Source method discrepancy, NOT a physical BBN conclusion.
"""
import math
import json
names=["pi_pm","K_pm","K0L","p_plus_pbar","n_plus_nbar"]
first=[5.609588603804452e32,489105.5126008581,59105.93631247951,29086.774913348447,34849.08026691193,34656.17773724596]
second=[6.099798045788406e32,442306.73787501804,53467.712852971126,26311.795859614824,31504.591028094237,31328.963561830213]
res=[]
for i,name in enumerate(names,1):
    p=-math.log(second[i]/first[i])/math.log(second[0]/first[0])
    assert 1.19<p<1.22
    res.append({"channel":name,"source_extrapolation_exponent":p,
                "published_analytic_exponent":1.3,
                "scan_over_paper_at_3e8g":(1e9/3e8)**(p-1.3),
                "scan_over_paper_at_1e8g":(1e9/1e8)**(p-1.3)})
print(json.dumps({"scope":"pinned main-scan.jl pathway only",
 "upstream_commit":"d395183674cace6c9906a8911bdeb7234ba4040d",
 "table_git_blob":"06d0883a27b108692720422294ba2baacd381a64",
 "results":res,"no_claim":"NO_FIG5_ATTRIBUTION;NO_PHYSICAL_SOURCE_VALIDATION;NO_BBN_BOUND;NO_CANON;NO_EXEC_SIGN"},indent=2))
