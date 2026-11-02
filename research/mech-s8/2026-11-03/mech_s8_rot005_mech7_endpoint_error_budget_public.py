#!/usr/bin/env python3
"""ROT005: Mech-S7 ROT035 reported endpoint arithmetic only; NOT ODE certificate."""
from decimal import Decimal as D, getcontext
import json
getcontext().prec=60
cases=[
 ("exact_three_moments","B_exec",D("0.4013457986033065"),D("0.4005731717792495")),
 ("exact_three_moments","B_sym",D("0.4002312008516105"),D("0.39993871354707966")),
 ("two_noisy_weights","B_exec",None,D("1.31287552213e-5")),
 ("two_noisy_weights","B_sym",None,D("5.56423334816e-6"))]
out=[]
for typ,group,a,b in cases:
 half=(a-b)/2 if a is not None else b
 assert half>0
 out.append({"type":typ,"map":group,"half_gap_numeric":str(half),
 "required_eps_plus_plus_eps_minus_STRICT_LT":str(2*half),
 "symmetric_each_eps_STRICT_LT":str(half)})
assert out[0]["required_eps_plus_plus_eps_minus_STRICT_LT"]=="0.0007726268240570"
assert out[1]["required_eps_plus_plus_eps_minus_STRICT_LT"]=="0.00029248730453084"
assert out[2]["required_eps_plus_plus_eps_minus_STRICT_LT"]=="0.0000262575104426"
assert out[3]["required_eps_plus_plus_eps_minus_STRICT_LT"]=="0.00001112846669632"
print(json.dumps({"input":"Mech-S7 ROT035 GitHub public endpoint values",
"mathematical_rule":"true half-gap >= num half-gap - (eps_plus+eps_minus)/2",
"results":out,"claim_ceiling":"ARITHMETIC_ONLY/NO_CERTIFICATE/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN"},indent=2))
