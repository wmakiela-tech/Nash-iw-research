"""DAX-S7 rotation 47: controlled radiation-dominated PBH reheating crossing audit.
NOT the Wu-Xu Julia solver. Dependencies: numpy, scipy. Source-grid 100x100.
"""
import csv
import json
import math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from scipy.special import beta as beta_func, betainc

OUT = Path(__file__).resolve().parent
M_PL_GRAM = 2.176434e-5
T_PL_S = 5.391247e-44
GAMMA = 1 / (3 * math.sqrt(3))
G_RHO_HIGH = 104.86508083893959
N_BH = (27 / 4) * G_RHO_HIGH / (30720 * math.pi)
T_NUC_MEV = 0.078185270688319950
G_RHO_NUC = 3.722254946361439
H_COEFF = 0.2066
REFERENCE_T_S = 1 / (2 * H_COEFF * math.sqrt(G_RHO_NUC) * T_NUC_MEV**2)
F0 = float(beta_func(1 / 3, 3 / 2) / 3)

def F(y):
    """Exact integral of sqrt(1-u^3) from y to 1 via incomplete beta."""
    return F0 * (1 - float(betainc(1 / 3, 3 / 2, y**3)))

def row(m, b):
    tf = m / M_PL_GRAM * T_PL_S / GAMMA
    tau = (m / M_PL_GRAM)**3 * T_PL_S / (3 * N_BH)
    eps = b * math.sqrt(tau / tf)
    def heating_ratio(y):
        return (2 * eps / 3) * (1 - y**3)**1.5 / (y*y*(1 + eps*F(y)))
    ymin = brentq(lambda y: heating_ratio(y)-4, 1e-9, 0.9, xtol=1e-15)
    tmin = tau*(1-ymin**3)
    tlo = tau / math.sqrt(1+eps*F0)
    thi = tmin / math.sqrt(1+eps*F(ymin))
    return dict(mass_g=m,beta=b,formation_s=tf,evap_s=tau,epsilon=eps,
        y_at_min=ymin,reference_window_low_s=tlo,reference_window_high_s=thi,
        window_width_s=thi-tlo,q_min=(REFERENCE_T_S/thi)**2,
        q_end=(REFERENCE_T_S/tlo)**2,
        triple_cross=int(tlo<REFERENCE_T_S<thi),
        triple_cross_tref_208_853=int(tlo<208.85253295051325<thi),
        triple_cross_tref_214_956=int(tlo<214.95558106551593<thi))

def mass_root(b, fn):
    return brentq(lambda m: row(m,b)[fn]-REFERENCE_T_S,9e9,1e10,xtol=1e-3)

def main():
    masses=np.geomspace(6e8,1e10,100)
    betas=np.geomspace(1e-20,1e-17,100)
    rows=[row(float(m),float(b)) for m in masses for b in betas]
    csvpath=OUT/'IW_DAX_S7_ROTATION_47_REHEATING_SOURCE_GRID_10000_20261023.csv'
    with open(csvpath,'w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    lower_mass=[r for r in rows if r['mass_g']<=9.447484474143e9]
    upper_mass=[r for r in rows if r['mass_g']>=9.719817114606e9]
    gap=(max(r['reference_window_high_s'] for r in lower_mass),
         min(r['reference_window_low_s'] for r in upper_mass))
    lower=mass_root(1e-17,'reference_window_high_s')
    upper=mass_root(1e-17,'reference_window_low_s')
    summary=dict(status='RADIATION_DOMINATED_SURROGATE_ONLY',
        reference_t_s=REFERENCE_T_S,source_grid_total=len(rows),
        triples_at_constant_g_tref=sum(r['triple_cross'] for r in rows),
        triples_at_code_clock_surrogate=sum(r['triple_cross_tref_214_956'] for r in rows),
        triples_at_adiabatic_clock_surrogate=sum(r['triple_cross_tref_208_853'] for r in rows),
        nbh=N_BH,F0=F0,conservative_no_triple_tref_gap_s=gap,
        continuous_mass_window_beta_1e_17_g=(lower,upper),
        continuous_mass_window_g=upper-lower,
        continuous_mass_window_rel=(upper-lower)/lower,
        max_window_width_s=max(r['window_width_s'] for r in rows),
        grid_mass_step_ratio=float(masses[1]/masses[0]),
        csv=csvpath.name)
    (OUT/'IW_DAX_S7_ROTATION_47_REHEATING_GRID_SUMMARY_20261023.json').write_text(
        json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
