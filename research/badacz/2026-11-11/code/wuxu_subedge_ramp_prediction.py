#!/usr/bin/env python3
"""Badacz (Claude): PREREG_060 prediction, written and run BEFORE any native ramp run.
Alternative sub-edge extrapolation of the Wu-Xu hadron rate table (Mech-S8 ROT017): below the first table mass m1 = 1e9 g the
authors' code extrapolates ln R_h linearly in ln M with the first-pair slope (-p2_h); the alternative uses the OLS slope over the
first 12 rows (-p12_h), anchored at row 1. Equivalent multiplier on the native rate: k_h(M) = (M/m1)^(-(p12_h - p2_h)) for M < m1.
Prediction from the REVIEW_050 band kernel (s_eff per band at k = 2, default tolerance) under A1:
    Delta = -log10(1 + sum_b (k_b - 1) s_b),  b in {B: 3e8-1e9 g, C: M_grid-3e8 g, D: < M_grid}.
k(M) rises monotonically toward small M, so (assuming the root responds monotonically to a pointwise rate increase) the effective
k_b of a band lies between k at its upper and at its lower edge. Bracket:
    weak end : k_B = k(1e9) = 1, k_C = k(3e8), k_D = k(M_grid); s_b - se_b; smallest dp over species
    strong end: k_B = k(3e8), k_C = k(M_grid), k_D = number-weighted mean over D; s_b + se_b; largest dp over species
D band: all D hadrons are emitted within ~3e-4 s at the end of evaporation, so the per-hadron response is taken as uniform in D and
k_D is weighted by hadron number (dN ~ R M^2 dM with R ~ M^-p2): k_D,num = k(M_grid) (3 - p2) / (3 - p2 - dp).
Window for the native Delta (prereg criterion): [Delta_strong - 0.010, Delta_weak + 0.010] dex; 0.010 dex = largest Delta change
between solver tolerances seen in REVIEW_059. Central value (diagnostic only): geometric band midpoints for B and C, k_D,num, nominal s, mean dp.
Usage: python3 -I wuxu_subedge_ramp_prediction.py <hadrons_from_PBH.dat> <2026-11-08/data/kernel_analysis.strict.json> <out.json>
"""
import json, math, sys

M1_G, MB_G = 1e9, 3e8
G_PER_GEV = 1 / 5.60958860380445e23           # as in the band-kernel CSV header (g_GeV)
ALLOW = 0.010
rows = [list(map(float, l.split())) for l in open(sys.argv[1]).read().splitlines()[1:] if l.strip()]
species = ["pi_charged", "K_charged", "K0L", "p_pbar", "n_nbar"]
slopes = {}
for c, name in enumerate(species, start=1):
    lm = [math.log(r[0]) for r in rows[:12]]; lr = [math.log(r[c]) for r in rows[:12]]
    p2 = -(lr[1] - lr[0]) / (lm[1] - lm[0])
    mx, my = sum(lm) / 12, sum(lr) / 12
    p12 = -sum((a - mx) * (b - my) for a, b in zip(lm, lr)) / sum((a - mx) ** 2 for a in lm)
    slopes[name] = {"p2": p2, "p12": p12, "dp": p12 - p2}
m1_check = rows[0][0] * G_PER_GEV
dps = [v["dp"] for v in slopes.values()]; p2s = [v["p2"] for v in slopes.values()]
dp_min, dp_max, dp_mean = min(dps), max(dps), sum(dps) / len(dps)
kern = json.load(open(sys.argv[2]))
M_GRID = 105726119.5158
k = lambda M, dp: (M / M1_G) ** (-dp)
def kD_num(dp, p2):
    return k(M_GRID, dp) * (3 - p2) / (3 - p2 - dp)
out = {"slopes": slopes, "m1_g_from_table": m1_check, "dp_range": [dp_min, dp_max], "allowance_dex": ALLOW, "j": {}}
for j in ("22", "28"):
    d = kern["derived"][j]
    s = {"B": (d["B2"]["s_eff"], d["B2"]["se_s_eff"]), "C": (d["C2"]["s_eff"], d["C2"]["se_s_eff"]), "D": (d["Dc"]["s_eff"], d["Dc"]["se_s_eff"])}
    def delta(kB, kC, kD, sign):
        tot = sum((kb - 1) * (s[b][0] + sign * s[b][1]) for b, kb in (("B", kB), ("C", kC), ("D", kD)))
        return -math.log10(1 + tot), tot
    weak, tw = delta(1.0, k(MB_G, dp_min), k(M_GRID, dp_min), -1)
    strong, ts = delta(k(MB_G, dp_max), k(M_GRID, dp_max), kD_num(dp_max, min(p2s)), +1)
    central, tc = delta(k(math.sqrt(MB_G * M1_G), dp_mean), k(math.sqrt(M_GRID * MB_G), dp_mean), kD_num(dp_mean, sum(p2s) / 5), 0)
    out["j"][j] = {"s_eff_used": {b: {"s": v[0], "se": v[1]} for b, v in s.items()},
                   "Delta_weak": weak, "Delta_strong": strong, "Delta_central": central,
                   "window": [strong - ALLOW, weak + ALLOW],
                   "k_values": {"B_top": 1.0, "B_bottom_dpmax": k(MB_G, dp_max), "C_top_dpmin": k(MB_G, dp_min), "C_bottom_dpmax": k(M_GRID, dp_max),
                                "D_top_dpmin": k(M_GRID, dp_min), "D_num_dpmax": kD_num(dp_max, min(p2s))}}
json.dump(out, open(sys.argv[3], "w"), indent=1, allow_nan=False)
for name, v in slopes.items():
    print("%-10s p2 %.5f p12 %.5f dp %.5f" % (name, v["p2"], v["p12"], v["dp"]))
for j, v in out["j"].items():
    print("j=%s Delta weak %+.4f strong %+.4f central %+.4f  window [%+.4f, %+.4f]" % (j, v["Delta_weak"], v["Delta_strong"], v["Delta_central"], *v["window"]))
