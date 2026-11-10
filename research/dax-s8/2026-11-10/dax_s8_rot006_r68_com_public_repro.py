#!/usr/bin/env python3
"""DAX-S8 ROT006: head-on gamma-gamma R68 COM gate, not a QED run.
No MadGraph, CRPropa, 4-body amplitude, transport or bath integral executed.
"""
from decimal import Decimal as D, getcontext
import json
getcontext().prec = 54
E_GEV = D('1436.554')
E_MEV = E_GEV * 1000
T = D('0.07818527068831995')
ME = D('0.51099895')
out = []
for label, mult in [('T', D(1)), ('2.701178T', D('2.701178')), ('10T', D(10))]:
    eps = mult*T
    s = 4*E_MEV*eps
    w1 = s.sqrt()
    w2 = 2*(E_MEV*eps).sqrt()
    assert abs(w1-w2) < D('1e-45')
    assert s/(16*ME**2) > 1
    out.append({
        'epsilon': label,
        'epsilon_MeV': str(eps),
        'sqrt_s_MeV': str(w1),
        's_over_16me2': str(s/(16*ME**2))
    })
assert 4*D(3)*D(2) == 24 > 16
print(json.dumps({
  'status':'PASS_DECIMAL_KINEMATICS',
  'scope':'STRICT_HEAD_ON; NOT FULL_PLANCK_OR_ANGLE_AVERAGE; NO_QED_DIFFERENTIAL_RUN',
  'E_gamma_GeV':str(E_GEV),'T_gamma_MeV':str(T),
  'points':out
},indent=2,sort_keys=True))
