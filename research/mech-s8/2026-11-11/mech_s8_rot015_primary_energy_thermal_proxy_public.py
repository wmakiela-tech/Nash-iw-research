#!/usr/bin/env python3
"""Mech-S8 ROT015 public compact reproduction; Python standard library only.
Source: Wu-Xu v2 author Git d395183674cace6c9906a8911bdeb7234ba4040d.
Author notebook valid_hadrons_from_BlackHawk.ipynb uses PRIMARY energy grid
GeV(5) ... GeV(1e5), 100 points, and mass grid 1e9...4e12 g.
This is a PHASE-SPACE BLACKBODY PROXY, NOT actual Hawking/BlackHawk
greybody radiation, hadron fragmentation, BBN response or PBH beta bound.
The full report, independent SciPy check and manifest are in ROT015 ZIP.
"""
import json
import math

C = 1.057261195158e13  # T_H [GeV] * PBH mass [g]
EMAX = 1e5  # CONFIGURED PRIMARY energy max [GeV]
ZETA3 = 1.2020569031595942854

def frac(x, n, fermion=False):
    assert x > 0 and n in (2, 3)
    total = 0.0
    for k in range(1, 700):
        y = k*x
        polynomial = sum(y**j/math.factorial(j) for j in range(n+1))
        term = math.factorial(n)*math.exp(-y)*polynomial/k**(n+1)
        if fermion and k%2 == 0:
            term = -term
        total += term
        if k >= 5 and abs(term) < 1e-16*max(abs(total), 1e-30):
            break
    norm = (2*ZETA3 if n == 2 else math.pi**4/15)
    if fermion:
        norm *= 1-2**(-n)
    return total/norm

def half_mass(n, f):
    a,b = 0.1,20.0
    for _ in range(85):
        m = (a+b)/2
        if frac(m,n,f) > .5:
            a = m
        else:
            b = m
    x = (a+b)/2
    return C*x/EMAX

rows = []
for M in [1e10,1e9,6e8,3e8,C/EMAX,1e8]:
    x = EMAX*M/C
    rows.append(dict(mass_g=M, T_H_TeV=C/M/1000,
       primary_Emax_over_T=x,
       thermal_B_number_tail=frac(x,2),
       thermal_F_number_tail=frac(x,2,True),
       thermal_B_energy_tail=frac(x,3),
       thermal_F_energy_tail=frac(x,3,True)))
assert 0.64 < rows[3]["thermal_B_energy_tail"] < 0.65
assert 0.70 < rows[3]["thermal_F_energy_tail"] < 0.72
assert 0.96 < rows[4]["thermal_B_energy_tail"] < 0.97
out = {"status":"PASS_IDEAL_THERMAL_PRIMARY_ENERGY_PROXY_ONLY",
       "source":"Wu-Xu original author 2025-12-30 v2, Git d395183",
       "rows":rows,
       "M_half_thermal_B_energy_g":half_mass(3,False),
       "M_half_thermal_F_energy_g":half_mass(3,True),
       "excludes":["greybody","secondary hadron spectrum","BBN response",
                   "source validation","PBH abundance bound","CANON","EXEC_SIGN"]}
print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))
