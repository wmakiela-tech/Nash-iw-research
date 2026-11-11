#!/usr/bin/env python3
"""Badacz (Claude): POST HOC (not in PREREG_060), written after the PREREG_060 verdicts.
Band-kernel map for the Mech-S8 ROT017 flat C-infinity multiplier k(M) = 1 + (c-1) w(t), t = log10(1e9 g / M),
w(t) = 0 (t<=0), 1 (t>=1), exp(-1/t)/(exp(-1/t)+exp(-1/(1-t))) otherwise. Same kernel and weighting rules as the PREREG_060
prediction: Delta = -log10(1 + sum_b (k_b - 1) s_b); central = k at the geometric band midpoint for B and C, hadron-number
weighting in D (dN ~ M^(2-p2) dM, p2 = species mean); bracket = band-edge values of k (monotone in M for c > 1), s -/+ SE.
Reports Delta(c) for c in [1, 2] (A1 checked locally at k = 2, REVIEW_054/059; it FAILS at k = 0, so c < 1 is not reported)
and c needed for a 0.1 dex root shift. Validated range: PREREG_060 checked one smooth multiplier with k <= ~1.27.
Usage: python3 -I wuxu_subedge060_posthoc_cmap.py <2026-11-08/data/kernel_analysis.strict.json> <subedge_ramp060_prediction.json> <out.json>
"""
import json, math, sys

kern = json.load(open(sys.argv[1])); pred = json.load(open(sys.argv[2]))
p2 = sum(v["p2"] for v in pred["slopes"].values()) / 5
M_GRID, MB, M1 = 105726119.5158, 3e8, 1e9
def w(t):
    if t <= 0: return 0.0
    if t >= 1: return 1.0
    a, b = math.exp(-1 / t), math.exp(-1 / (1 - t))
    return a / (a + b)
t_of = lambda M: math.log10(M1 / M)
def wD_num(n=200000):                     # number-weighted mean of w over D: weight M^(2-p2) dM on (0, M_GRID)
    e = 3 - p2; num = den = 0.0
    for i in range(n):                    # substitute u = (M/M_GRID)^e (uniform in hadron number)
        u = (i + 0.5) / n; M = M_GRID * u ** (1 / e)
        num += w(t_of(M)); den += 1
    return num / den
WD = wD_num()
W = {"B": {"top": w(t_of(M1)), "bottom": w(t_of(MB)), "mid": w(t_of(math.sqrt(MB * M1)))},
     "C": {"top": w(t_of(MB)), "bottom": w(t_of(M_GRID)), "mid": w(t_of(math.sqrt(M_GRID * MB)))},
     "D": {"top": w(t_of(M_GRID)), "num": WD}}
out = {"posthoc": True, "w_band": W, "j": {}}
for j in ("22", "28"):
    d = kern["derived"][j]
    s = {"B": (d["B2"]["s_eff"], d["B2"]["se_s_eff"]), "C": (d["C2"]["s_eff"], d["C2"]["se_s_eff"]), "D": (d["Dc"]["s_eff"], d["Dc"]["se_s_eff"])}
    S_c = W["B"]["mid"] * s["B"][0] + W["C"]["mid"] * s["C"][0] + W["D"]["num"] * s["D"][0]
    S_lo = W["B"]["top"] * (s["B"][0] - s["B"][1]) + W["C"]["top"] * (s["C"][0] - s["C"][1]) + W["D"]["top"] * (s["D"][0] - s["D"][1])
    S_hi = W["B"]["bottom"] * (s["B"][0] + s["B"][1]) + W["C"]["bottom"] * (s["C"][0] + s["C"][1]) + W["D"]["num"] * (s["D"][0] + s["D"][1])
    row = {"S_central": S_c, "S_bracket": [S_lo, S_hi], "Delta": {}}
    for c in (1.1, 1.2, 1.5, 2.0):
        row["Delta"][str(c)] = {"central": -math.log10(1 + (c - 1) * S_c), "weak": -math.log10(1 + (c - 1) * S_lo), "strong": -math.log10(1 + (c - 1) * S_hi)}
    need = 10 ** 0.1 - 1
    row["c_for_0p1_dex"] = {"central": 1 + need / S_c, "range": [1 + need / S_hi, 1 + need / S_lo]}
    out["j"][j] = row
# AUD1 ROT038 bridge (post hoc): sharp conditional sup of inter-node log-midpoint relative rate error inside the table
# (M >= 1e9 g, i.e. band A) = 7.7443 % over all 99 cells and species. Treated as a uniform multiplier 1 +/- e on band A for
# all species (conservative: the sup is attained only at log-midpoints of countermodels); |Delta| <= -log10(1 - e (s_A + SE)).
E_AUD1 = 0.077443
out["aud1_rot038_bandA_bound"] = {}
for j in ("22", "28", "34", "62"):
    sA = kern["derived"][j]["A2"]["s_eff"] + kern["derived"][j]["A2"]["se_s_eff"]
    out["aud1_rot038_bandA_bound"][j] = {"s_A_plus_se": sA, "abs_Delta_max_dex": -math.log10(1 - E_AUD1 * sA)}
json.dump(out, open(sys.argv[3], "w"), indent=1, allow_nan=False)
print("AUD1 ROT038 band-A bound |Delta| [dex]:", {j: round(v["abs_Delta_max_dex"], 4) for j, v in out["aud1_rot038_bandA_bound"].items()})
print("w bands:", {b: {k: round(v, 4) for k, v in x.items()} for b, x in W.items()})
for j, r in out["j"].items():
    print("j=%s S_central %.4f bracket [%.4f, %.4f]  c(0.1 dex) central %.3f range [%.3f, %.3f]" % (j, r["S_central"], *r["S_bracket"], r["c_for_0p1_dex"]["central"], *r["c_for_0p1_dex"]["range"]))
    for c, v in r["Delta"].items():
        print("   c=%s Delta central %+.4f [%+.4f, %+.4f]" % (c, v["central"], v["strong"], v["weak"]))
