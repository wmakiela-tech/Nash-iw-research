#!/usr/bin/env python3
"""Badacz (Claude), PREREG_048: hadron-NUMBER shares of instantaneous-mass bands for the Wu-Xu native source, and the
time-uniform (number-weighted) prediction for the chi2 = 4 boundary shift under a band multiplier k.

Source: authors' hadrons_from_PBH.dat (rates dN/dt per PBH vs mass, GeV units, rows 1e9..4e12 g), log-log linear interpolation
between rows and the authors' log-linear extrapolation below the first row (slope of the first two rows), as in
tool_script-hadrons_from_PBH.jl. Mass clock: dM/dt = -K/M^2 with K constant (MT14 ROT025: constant N_BH above ~1 TeV), so the
number emitted while M is in [a,b] is proportional to int_a^b R(M) M^2 dM. Total = integral over [0, M0].
Number-weighted (time-uniform) prediction: Delta(k) = -log10(1 + (k-1) s_num).
Usage: python3 -I wuxu_band_number_shares.py --table hadrons_from_PBH.dat --out shares.json
"""
import argparse, json, math

ap = argparse.ArgumentParser(); ap.add_argument("--table", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
G_GEV = 5.60958860380445e23          # 1 g in GeV (driver header; table first mass / 1e9 g)
rows = [list(map(float, l.split())) for l in open(a.table) if l.strip() and not l.startswith("m_PBH")]
lm = [math.log(r[0] / G_GEV) for r in rows]                  # ln M[g]
lr = [[math.log(r[c]) for r in rows] for c in range(1, 6)]   # ln rate per channel
M_GRID = 1.0572611951580e8                                   # T_H = 100 TeV (MT14 ROT025 / Mech-S8 ROT002)
BANDS = {"A": (1e9, math.inf), "B": (3e8, 1e9), "C": (M_GRID, 3e8), "D": (0.0, M_GRID)}
J = {22: None, 28: None, 34: None, 62: None}


def m0(j):
    return 6e8 * (1e10 / 6e8) ** (j / 99)


def lnrate(c, x):                     # x = ln M[g]
    if x <= lm[1]:                    # below second row: first-interval line (authors' extrapolation below row 1)
        s = (lr[c][1] - lr[c][0]) / (lm[1] - lm[0]); return lr[c][0] + s * (x - lm[0])
    i = max(k for k in range(len(lm) - 1) if lm[k] <= x)
    s = (lr[c][i + 1] - lr[c][i]) / (lm[i + 1] - lm[i]); return lr[c][i] + s * (x - lm[i])


def number(c, lo, hi, n=4000):        # int_lo^hi R(M) M^2 dM, substitution x = ln M, Simpson; lo = 0 handled analytically
    out = 0.0
    if lo == 0.0:                     # below lm[0]: R = R0 (M/M1)^s -> int_0^M R M^2 dM = R(M) M^3 / (3 + s)
        s = (lr[c][1] - lr[c][0]) / (lm[1] - lm[0]); top = min(hi, math.exp(lm[0]))
        out += math.exp(lnrate(c, math.log(top)) + 3 * math.log(top)) / (3 + s)
        lo = top
        if hi <= lo:
            return out
    x0, x1 = math.log(lo), math.log(hi); h = (x1 - x0) / n
    f = lambda x: math.exp(lnrate(c, x) + 3 * x)
    out += h / 3 * (f(x0) + f(x1) + sum((4 if k % 2 else 2) * f(x0 + k * h) for k in range(1, n)))
    return out


res = {"M_grid_g": M_GRID, "bands_g": {b: [lo, (None if math.isinf(hi) else hi)] for b, (lo, hi) in BANDS.items()}, "j": {}}
for j in J:
    M0 = m0(j); per = {}
    tot = [number(c, 0.0, M0) for c in range(5)]
    for b, (lo, hi) in BANDS.items():
        hi2 = min(hi, M0)
        nb = [number(c, lo, hi2) if hi2 > lo else 0.0 for c in range(5)]
        per[b] = {"s_num_total": sum(nb) / sum(tot), "s_num_by_channel": [nb[c] / tot[c] for c in range(5)],
                  "pred_num_Delta": {str(k): -math.log10(1 + (k - 1) * sum(nb) / sum(tot)) for k in (0, 2, 10)}}
    res["j"][str(j)] = {"M0_g": M0, "tau_s": 0.2376664163901 * (M0 / 1e9) ** 3, "bands": per,
                        "check_sum_shares": sum(per[b]["s_num_total"] for b in per)}
json.dump(res, open(a.out, "w"), indent=1, sort_keys=True)
for j in J:
    r = res["j"][str(j)]
    print(j, f"M0={r['M0_g']:.4e} tau={r['tau_s']:.3f}s", {b: round(r["bands"][b]["s_num_total"], 4) for b in BANDS},
          "sum", round(r["check_sum_shares"], 6))
