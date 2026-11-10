#!/usr/bin/env python3
"""DAX-S8 ROT007. 2006 collider-cut 4-lepton support and Planck NUMBER tail.
No QED differential amplitude, no event-weighted or PBH/BBN inference.
Source: https://arxiv.org/abs/hep-ph/0604020
"""
from decimal import Decimal as D, localcontext
from math import comb
import json

with localcontext() as c:
    c.prec = 65
    E = D("1436.554")*1000  # incoming gamma, MeV
    T = D("0.07818527068831995")  # bath, MeV
    me = D("0.51099895")  # electron rest energy, MeV
    cut = D(4000)  # four outgoing leptons each >= 1 GeV in COM
    # zeta(3) via Apery convergent series, no external constant.
    def zeta3(N):
        return D(5)/2 * sum((D(1) if n%2 else D(-1)) /
                            (D(n)**3*D(comb(2*n,n)))
                            for n in range(1,N+1))
    z = zeta3(110)
    assert abs(z-zeta3(105)) < D("1e-65")
    rows=[]
    for label,k in [("T",D(1)),("2.701178T",D("2.701178")),("10T",D(10))]:
        eps = k*T
        s = 4*E*eps
        w = s.sqrt()
        assert abs(w-2*(E*eps).sqrt()) < D("1e-55")
        assert 4*me < w < cut
        rows.append({"epsilon":label,"sqrt_s_MeV":format(w,".16f"),
                     "physical_4e_open":True,"collider_1GeV_each_cut_accepted":False})
    eps_min=cut**2/(4*E)
    a=eps_min/T
    # Planck photon number tail: exactly sum over exp(-n*a).
    term1=(-a).exp()*(a*a+2*a+2)
    tail_integral=sum((-D(n)*a).exp()*
                      (a*a/D(n)+2*a/D(n)**2+2/D(n)**3)
                      for n in range(1,11))
    fraction=tail_integral/(2*z)
    lower=term1/(2*z)
    upper=lower/(1-(-a).exp())
    assert lower <= fraction <= upper
    assert abs(fraction-D("1.905274252983205879e-13")) < D("1e-30")
    print(json.dumps({"status":"PASS_EXACT_CUT_SUPPORT_AND_NUMBER_TAIL",
        "E_gamma_GeV":"1436.554","T_gamma_MeV":str(T),
        "min_accepted_COM_GeV":"4",
        "sampled_head_on_cases":rows,
        "min_epsilon_MeV":str(eps_min),
        "min_epsilon_over_T":str(a),
        "Planck_photon_NUMBER_tail":str(fraction),
        "provable_tail_lower":str(lower),"provable_tail_upper":str(upper),
        "not_inferred":"No QED differential, interaction-weighted event fraction, or deposition"},
        indent=2,sort_keys=True))
