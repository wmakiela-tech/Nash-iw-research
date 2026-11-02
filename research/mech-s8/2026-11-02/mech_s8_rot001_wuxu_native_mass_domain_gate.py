#!/usr/bin/env python3
"""Source-native mass-domain coverage gate, not a PBH/BBN calculation.
Source: Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d
  arXiv-2509.05618/main-scan-parameters.jl
  arXiv-2509.05618/data/out/hadrons_from_PBH.dat
Requires Python >=3.11, stdlib only.
"""
import json
from decimal import Decimal, getcontext
getcontext().prec = 70
D=Decimal
SCAN_MIN_G=D('6e8'); SCAN_MAX_G=D('1e10'); N=100
TABLE_FLOOR_G=D('1e9') # documented 1e9-g hadronic source floor
M_PL_G=D('0') # complete-evaporation approximation; NOT a remnant-model claim

def scan_mass(j):
    assert 0 <= j < N
    return SCAN_MIN_G * (((SCAN_MAX_G / SCAN_MIN_G).ln() * D(j) / D(N-1)).exp())

def subedge_mass_energy_fraction(m):
    if m <= TABLE_FLOOR_G: return D(1)
    return TABLE_FLOOR_G/m

rows=[{'zero_based_j':j,'M_init_g':str(scan_mass(j)),
       'fraction_of_evaporated_rest_mass_energy_released_below_table_floor':str(subedge_mass_energy_fraction(scan_mass(j)))}
      for j in [0,17,18,22,24,99]]
counts={'initially_below_table_floor':sum(scan_mass(j)<TABLE_FLOOR_G for j in range(N)),
        'fraction_below_table_floor_at_least_one_half':sum(subedge_mass_energy_fraction(scan_mass(j))>=D('.5') for j in range(N))}
result={'source_commit':'d395183674cace6c9906a8911bdeb7234ba4040d',
        'source_table_git_blob':'06d0883a27b108692720422294ba2baacd381a64',
        'source_scan_parameters_git_blob':'53faee65beda383348580c28d0424188da69b660',
        'assumptions':['monotonic mass loss','complete evaporation or negligible terminal mass',
                       'mass loss converted to total emitted energy; no assertion about hadronic or deposited energy'],
        'table_floor_g':'1e9','scan_initial_min_g':'6e8','scan_initial_max_g':'1e10','scan_n':100,
        'counts':counts,'selected':rows,
        'claim_ceiling':'SOURCE-DOMAIN/KINEMATIC-ACCOUNTING_ONLY;NO_HADRON_YIELD;NO_BBN_ENDPOINT;NO_PBH_BOUND;NO_EXEC_SIGN'}
if __name__=='__main__':
    assert counts['initially_below_table_floor']==18
    assert counts['fraction_below_table_floor_at_least_one_half']==43
    assert D(rows[3]['M_init_g'])>D('1.12e9')
    print(json.dumps(result,indent=2,ensure_ascii=False,sort_keys=True))
