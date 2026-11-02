#!/usr/bin/env python3
"""DAX-S8: exact on-shell four-lepton kinematic witness, standard library only.

Units: electron mass m=1, c=1. The incoming centre-of-mass
two-photon energy is 12m. Each outgoing back-to-back pair has
energies (e,e) and squared momentum q^2=e^2-1.
No differential QED matrix element is computed or claimed.
"""
from fractions import Fraction as F
import json

def exact_configuration(pair_energies):
    a, b = map(F, pair_energies)
    assert a >= 1 and b >= 1
    energies = (a, a, b, b)
    q1_squared, q2_squared = a*a - 1, b*b - 1
    assert q1_squared >= 0 and q2_squared >= 0
    # x-directed +-q1 and y-directed +-q2 cancel exactly.
    assert sum(energies) == 12
    # On-shell each E^2 - |p|^2 = m^2 = 1.
    assert a*a - q1_squared == b*b - q2_squared == 1
    return {
        "lepton_energies_in_m": [str(z) for z in energies],
        "pair_momentum_squared_in_m2": [str(q1_squared), str(q2_squared)],
        "total_energy_in_m": str(sum(energies)),
        "sum_energy_squared_in_m2": str(sum(z*z for z in energies)),
        "count_above_7_over_2_m": sum(z > F(7,2) for z in energies)
    }

A=exact_configuration((3,3))
B=exact_configuration((4,2))
assert A["total_energy_in_m"] == B["total_energy_in_m"] == "12"
assert (A["sum_energy_squared_in_m2"],B["sum_energy_squared_in_m2"]) == ("36","40")
assert (A["count_above_7_over_2_m"],B["count_above_7_over_2_m"]) == (0,2)
print(json.dumps({"status":"PASS_EXACT_KINEMATIC_TOY", "incoming_gamma_energies_in_m":["6","6"],
    "configuration_A":A,"configuration_B":B,
    "claim_ceiling":"kinematic support and integral-operator nonidentifiability only; NOT QED differential cross section, deposition or PBH limit"}, indent=2))
