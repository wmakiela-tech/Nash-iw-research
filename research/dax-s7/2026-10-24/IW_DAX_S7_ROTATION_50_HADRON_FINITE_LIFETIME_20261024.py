#!/usr/bin/env python3
"""DAX-S7 rotation 50: source-matched LOCAL hadronic branch test.

This is NOT the complete Wu-Xu Julia solver. It uses:
- the source background crossing times from rotation 49;
- a constant T=T_nuc and a constant PBH number density across 0.0238 s;
- all six source hadron channels, including finite decay/annihilation times;
- the two low-mass-end rows of source hadron table: both suffice EXACTLY for
  the *extrapolated* source emission curves because M<M_min during this window.

Source: Fenyutanchan/Primordial-Black-Hole,
arXiv-2509.05618/data/out/hadrons_from_PBH.dat
blob SHA 06d0883a27b108692720422294ba2baacd381a64
and tool_script-parameters.jl, main-scan.jl.
The results depend critically on the source's log-log EXTRAPOLATION below 1e9 g.
No physical claim, no PBH bound, no canon promotion.

Run: python IW_DAX_S7_ROTATION_50_HADRON_FINITE_LIFETIME_20261024.py
"""
from __future__ import annotations
import csv
import json
import math
from pathlib import Path

# Source rows [PBH mass GeV, charged pion, charged kaon, neutral-long kaon,
#              antiproton/proton, antineutron/neutron emission rate, all GeV].
ROWS = (
    (5.609588603804452e32, 489105.5126008581, 59105.93631247951,
     29086.774913348447, 34849.08026691193, 34656.17773724596),
    (6.099798045788406e32, 442306.73787501804, 53467.712852971126,
     26311.795859614824, 31504.591028094237, 31328.963561830213),
)
# Four refinement levels in rotation 49, finest as default:
M_F_G = 9672500000.0
BETA = 1e-17
TAU_EVAP_S = 215.07211197892192
T_FIRST = 215.05755469059486
T_SECOND = 215.07087213610447
T_THIRD = 215.08133566390094
LN_A_FIRST = 35.071137473435506
T_NUC_MEV = 0.07818527068831995
G_RHO_NUC = 3.722254946361439
T_FORMATION_MEV = 43213506455750.82
G_RHO_FORMATION = 104.86508083893959
HBAR_GEV_S = 6.582119569e-25
GEV_PER_GRAM = 5.609588603804452e23
MBARN_TO_GEV2 = 1 / 0.389379338
PROTON_MASS_GEV = 0.93827208816
ALPHA_EM = 1 / 137.035999084
ETA_B = 6.1e-10
ZETA3 = 1.2020569031595942
TAU_NEUTRON_S = 878.4
Q_MEV = 939.5654205 - 938.27208816

# Order pi-, pi+, K-, K0L, anti-proton, anti-neutron.
NAMES = ["pi-", "pi+", "K-", "K0L", "pbar", "nbar"]
PI = math.pi
T = T_NUC_MEV * 1e-3
M_F_GEV = M_F_G * GEV_PER_GRAM
RHO_SM_GEV4 = PI**2 / 30 * G_RHO_NUC * T**4
N_B_GEV3 = ETA_B * 2 * ZETA3 / PI**2 * T**3
B0 = BETA * math.exp(
    math.log(G_RHO_FORMATION / G_RHO_NUC)
    + 4 * math.log(T_FORMATION_MEV / T_NUC_MEV)
    - 3 * LN_A_FIRST
)
N_PBH_GEV3 = B0 * RHO_SM_GEV4 / M_F_GEV


def fc(mass_gev):
    v = math.sqrt(T / mass_gev) + math.sqrt(T / PROTON_MASS_GEV)
    a = 2 * PI * ALPHA_EM / v
    return a / (-math.expm1(-a))


# Source cross-sections in GeV^-2, with the source's Fc(T) prescription.
SIGMA = {
    "pi_m": 1.5 * MBARN_TO_GEV2 * fc(0.13957039),
    "pi_p": 1.7 * MBARN_TO_GEV2,
    "K_pn": 31 * MBARN_TO_GEV2 * fc(0.493677),
    "K_po": 14.5 * MBARN_TO_GEV2 * fc(0.493677),
    "K_np": 26 * MBARN_TO_GEV2,
    "K_no": 34 * MBARN_TO_GEV2,
    "K0_pn": 7 * MBARN_TO_GEV2,
    "K0_po": 10 * MBARN_TO_GEV2,
    "K0_np": 7 * MBARN_TO_GEV2,
    "K0_no": 10 * MBARN_TO_GEV2,
    "pb_n": 28 * MBARN_TO_GEV2,
    "pb_p": 37 * MBARN_TO_GEV2,
    "nb_p": 28 * MBARN_TO_GEV2,
    "nb_n": 37 * MBARN_TO_GEV2,
}
EXPONENTS = [
    math.log(ROWS[1][j] / ROWS[0][j])
    / math.log(ROWS[1][0] / ROWS[0][0])
    for j in range(1, 6)
]


def emitted_rates(y, extrapolation="source"):
    """Emission GeV. Controls alter only the below-table extrapolation rule."""
    if extrapolation == "clamp":
        y = max(y, ROWS[0][0] / M_F_GEV)
    elif extrapolation == "zero" and M_F_GEV*y < ROWS[0][0]:
        return [0.0] * 6
    elif extrapolation != "source" and extrapolation not in ("clamp", "zero"):
        raise ValueError(extrapolation)
    mass = M_F_GEV * y
    factor = mass / ROWS[0][0]
    vals = [ROWS[0][j] * factor**EXPONENTS[j - 1] for j in range(1, 6)]
    return [vals[0], vals[0], vals[1], vals[2], vals[3], vals[4]]


def removal_rates(X):
    """Six hadron disappearance rates in 1/second (source decay + annihilation)."""
    s = SIGMA
    k = N_B_GEV3 / HBAR_GEV_S
    return [
        1 / 2.6033e-8 + s["pi_m"] * (1-X) * k,
        1 / 2.6033e-8 + s["pi_p"] * X * k,
        8.1e7 + k * (X*(s["K_np"]+s["K_no"])
                       + (1-X)*(s["K_pn"]+s["K_po"])),
        2.0e7 + k * (X*(s["K0_np"]+s["K0_no"])
                       + (1-X)*(s["K0_pn"]+s["K0_po"])),
        k * (X*s["pb_n"] + (1-X)*s["pb_p"]),
        k * (X*s["nb_n"] + (1-X)*s["nb_p"]),
    ]


def source_rates(y, mask=None, extrapolation="source"):
    vals = [v*N_PBH_GEV3/HBAR_GEV_S for v in emitted_rates(y, extrapolation)]
    return [v if (mask is None or mask[i]) else 0.0 for i,v in enumerate(vals)]


def equilibrium_hadrons(y, X, mask=None, extrapolation="source"):
    d = removal_rates(X)
    q = source_rates(y, mask, extrapolation)
    return [q[i]/d[i] for i in range(6)]


def neutron_rate(X, n):
    s = SIGMA
    x = Q_MEV / T_NUC_MEV
    gamma = (255 / TAU_NEUTRON_S) * (12 + 6*x + x*x) / x**5
    weak = -gamma * (X - (1-X)*math.exp(-x)) - X/TAU_NEUTRON_S
    had = (
        (1-X)*(n[0]*s["pi_m"] + n[2]*s["K_pn"] +
                n[3]*s["K0_pn"] + n[5]*s["nb_p"])
        -X*(n[1]*s["pi_p"] + n[2]*s["K_np"] +
             n[3]*s["K0_np"] + n[4]*s["pb_n"])
    ) / HBAR_GEV_S
    return weak, had


def shift_populations(n, d, q, dt):
    # Stable exact n'=q-d*n for piecewise constant source and removal rate.
    return [
        n[i] * math.exp(-d[i]*dt)
        + (-math.expm1(-d[i]*dt)) * q[i]/d[i]
        for i in range(6)
    ]


def integrate_finite_lifetime(x0=0.11, intervals=24000, post_intervals=400,
                              mask=None, extrapolation="source"):
    y0 = ((TAU_EVAP_S-T_FIRST)/TAU_EVAP_S)**(1/3)
    y2 = ((TAU_EVAP_S-T_SECOND)/TAU_EVAP_S)**(1/3)
    delta_y = -y0 / intervals
    X = x0
    n = equilibrium_hadrons(y0, X, mask, extrapolation)
    x2 = None
    y = y0
    for _ in range(intervals):
        yp = y + delta_y
        ym = (y+yp)/2
        dt = TAU_EVAP_S*(y**3-yp**3)
        Q = source_rates(ym, mask, extrapolation)
        d = removal_rates(X)
        mid = shift_populations(n, d, Q, dt/2)
        weak, had = neutron_rate(X, mid)
        xm = X + (weak+had)*dt/2
        dm = removal_rates(xm)
        mid = shift_populations(n, dm, Q, dt/2)
        weak, had = neutron_rate(xm, mid)
        xn = X + (weak+had)*dt
        nn = shift_populations(n, dm, Q, dt)
        if x2 is None and yp < y2:
            weight = (y-y2)/(y-yp)
            x2 = X + weight*(xn-X)
        X = xn
        n = nn
        y = yp
    xev = X
    tpost = (T_THIRD-TAU_EVAP_S) / post_intervals
    for _ in range(post_intervals):
        d = removal_rates(X)
        mid = shift_populations(n, d, [0]*6, tpost/2)
        weak, had = neutron_rate(X, mid)
        xm = X + (weak+had)*tpost/2
        dm = removal_rates(xm)
        mid = shift_populations(n, dm, [0]*6, tpost/2)
        weak, had = neutron_rate(xm, mid)
        X += (weak+had)*tpost
        n = shift_populations(n, dm, [0]*6, tpost)
    return dict(X_first=x0, X_second=x2, X_evap=xev, X_third=X,
                delta_X=X-x0, delta_X_after_evap=X-xev,
                delta_Y_code=2*X/(1-X)-2*x0/(1-x0),
                delta_Y_standard=2*(X-x0),
                intervals=intervals)


def main():
    print("SOURCE EXTRAPOLATION EXPONENTS:", EXPONENTS)
    print("MASS at first crossing [g]:",
          M_F_G*((TAU_EVAP_S-T_FIRST)/TAU_EVAP_S)**(1/3))
    print("PBH number density [GeV^3]:", N_PBH_GEV3)
    print("Source minimum tabulated PBH mass [g]:",
          ROWS[0][0] / GEV_PER_GRAM)
    rows = [integrate_finite_lifetime(x0) for x0 in
            (0.08, 0.11, 0.20, 0.40, 0.60, 0.80)]
    for row in rows:
        print(json.dumps(row, ensure_ascii=False))
    convergence = [integrate_finite_lifetime(0.11, n) for n in
                   (3000, 6000, 12000, 24000, 48000)]
    print("CONVERGENCE", json.dumps(convergence))
    masks = {
        "all": None,
        "weak_only": [0,0,0,0,0,0],
        "pions": [1,1,0,0,0,0],
        "kaons": [0,0,1,1,0,0],
        "antinucleons": [0,0,0,0,1,1],
        "antineutron": [0,0,0,0,0,1],
        "antiproton": [0,0,0,0,1,0],
    }
    controls = {name:integrate_finite_lifetime(.11,12000,mask=mask)
                for name,mask in masks.items()}
    controls.update({"emission_clamped":integrate_finite_lifetime(
                        .11,12000,extrapolation="clamp"),
                     "emission_zero_below_table":integrate_finite_lifetime(
                        .11,12000,extrapolation="zero")})
    print("CHANNEL_CONTROLS",json.dumps(controls))
    output = {"source_blob_sha":"06d0883a27b108692720422294ba2baacd381a64",
              "scope":"Conditional constant-T local branch, finite six-hadron kinetics",
              "not_full_julia":True,
              "background_crossings":[T_FIRST,T_SECOND,T_THIRD],
              "source_extrapolation_exponents":EXPONENTS,
              "assumed_initial_Xn":0.11,
              "cases":rows,"convergence":convergence,"controls":controls}
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print('JSON_OUTPUT',str(out))
    x = rows[1]
    assert abs(x["delta_X"]-0.00192640917165) < 1e-8
    assert abs(x["X_second"]-0.11146321504548) < 1e-8
    assert max(abs(row["delta_X"]-x["delta_X"]) for row in convergence) < 1e-8
    print("SELF-CHECK PASS: source low-mass log-log extrapolation, transient hadrons.")


if __name__ == "__main__":
    main()
