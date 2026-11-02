#!/usr/bin/env python3
"""Mech-S8 ROT002: two typed Wu-Xu/BlackHawk source-support gates.

Original upstream Wu-Xu commit:
d395183674cace6c9906a8911bdeb7234ba4040d
Notebook blob 8a10396ae771b17059808fc2b91235dd194cba8d,
cell 12: source table PBH mass range 1e9..4e12 grams and
set_BlackHawk_energy_spectrum!(params, GeV(5), GeV(1e5), 100)
Source scan parameters blob 53faee65beda383348580c28d0424188da69b660:
initial PBH mass geomspace(6e8,1e10,100).
These are original source configuration values; no BlackHawk/Julia/PYTHIA
source run, greybody spectrum, hadron yield or BBN prediction is performed.
"""
from decimal import Decimal as D, localcontext
import json
PI=D("3.1415926535897932384626433832795028841971693993751")
with localcontext() as ctx:
    ctx.prec=54
    hbar=D("1.054571817e-34")
    c=D("299792458")
    G=D("6.67430e-11")
    joule_per_GeV=D("1.602176634e-10")
    temperature_mass_product=hbar*c**3*D(1000)/(D(8)*PI*G*joule_per_GeV)
    Emax=D("1e5")
    m_grid=temperature_mass_product/Emax
    m_table=D("1e9")
    assert D("1e8")<m_grid<D("1.1e8")
    def scan_mass(j):
        return D("6e8")*((D("1e10")/D("6e8")).ln()*D(j)/D(99)).exp()
    def values(j):
        m=scan_mass(j)
        below_table=min(D(1),m_table/m)
        below_grid=m_grid/m
        return {
            "j":j,"M0_g":str(+m),
            "TH_initial_GeV":str(+(temperature_mass_product/m)),
            "gross_energy_below_mass_table_fraction":str(+below_table),
            "gross_energy_between_gates_fraction":str(+(below_table-below_grid)),
            "gross_energy_where_TH_ge_100TeV_fraction":str(+below_grid)
        }
    a={
        "source_type":"WU_XU_PINNED_CONFIGURATION_AND_KINEMATIC_CONVERSION_ONLY",
        "table_mass_floor_g":"1e9",
        "author_primary_grid_Emax_GeV":"1e5",
        "TH_times_M_GeV_g":str(+temperature_mass_product),
        "M_where_TH_equals_Emax_g":str(+m_grid),
        "author_mass_scan_below_table":sum(scan_mass(i)<m_table for i in range(100)),
        "author_mass_scan_at_least_half_energy_below_table":sum(min(D(1),m_table/scan_mass(i))>=D(".5") for i in range(100)),
        "selected":[values(j) for j in (0,22,24,99)],
        "no_claim":"NO_HADRON_EMISSION_OR_BBN_BOUND;NO_PHYSICAL_SOURCE_VALIDATION;NO_CANON;NO_EXEC_SIGN"
    }
    assert a["author_mass_scan_below_table"]==18
    assert a["author_mass_scan_at_least_half_energy_below_table"]==43
    print(json.dumps(a,ensure_ascii=False,sort_keys=True,indent=2))
