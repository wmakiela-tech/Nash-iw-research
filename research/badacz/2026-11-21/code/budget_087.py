"""SYNTH_087 helper (descriptive, post-hoc; no new solver call except the BlackHawk rows below 1e9 g).
Usage: python3 -I budget_087.py <data_dir(2026-11-21/data)> <rows_below_1e9.dat> <authors_table> <out.json>
(1) Network-baseline sensitivity (method credit: LT9 ROT010): a common additive shift delta of the network curve,
    Y_net -> Y_net + delta, is equivalent to crossing Y* - delta. Recomputed on public 083 (PYTHIA, 4 masses) and 085
    (HERWIG, j22/j62) series for delta in {-5e-4, -3e-4, +3e-4, +5e-4}; reports lb_net_orig, D_net, Delta_gen shifts.
(2) Table domain below 1e9 g (E4): BlackHawk PYTHIA-BBN rows (authors' settings, E_prim <= 1e5 GeV) vs the authors'
    log-log extrapolation from rows 0-1; local slopes of the authors' table; untruncated-trend estimate.
(3) Hadron-emission weight of m < m* for initial mass m0, with dN/dt ~ m^s and dt ~ m^2 dm: (m*/m0)^(s+3).
"""
import json, sys
import numpy as np

d, rows_p, auth_p, dst = sys.argv[1:5]
A83 = json.load(open(f"{d}/analysis083.json")); A85 = json.load(open(f"{d}/analysis085.json"))


def cross(xs, ys, lev):
    br = [i for i in range(len(xs) - 1) if (ys[i] - lev) * (ys[i + 1] - lev) <= 0 and ys[i] != ys[i + 1]]
    if len(br) != 1:
        return None
    i = br[0]
    return xs[i] + (lev - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i])


out = {"baseline_shift": {}, "E4_table": {}, "emission_weight": {}}
DEL = [-5e-4, -3e-4, 0.0, 3e-4, 5e-4]
for Ys in (0.251, 0.2484):
    for j in (22, 38, 62, 90):
        row = {}
        for dl in DEL:
            s_o = A83["series"][f"orig_{j}"]; s_e = A83["series"][f"e5_{j}"]
            lo = cross(s_o["lb"], s_o["Y_net"], Ys - dl); le = cross(s_e["lb"], s_e["Y_net"], Ys - dl)
            r = {"lb_net_orig_PY": lo, "D_net_PY": (le - lo) if None not in (lo, le) else None}
            if j in (22, 62):
                h_o = A85["series"][f"HER_orig_{j}"]
                ho = cross(h_o["lb"], h_o["Y_net"], Ys - dl)
                r["dgen_net_orig"] = (ho - lo) if None not in (ho, lo) else None
            row[f"{dl:+.0e}"] = r
        out["baseline_shift"][f"{j}|{Ys}"] = row
A = np.loadtxt(auth_p, skiprows=1); R = np.loadtxt(rows_p, skiprows=1)
G = 5.609588603804452e23; lm0, lm1 = np.log(A[0, 0]), np.log(A[1, 0])
ext = lambda m, k: np.exp(np.log(A[0, k]) + (np.log(A[1, k]) - np.log(A[0, k])) / (lm1 - lm0) * (np.log(m) - lm0))
out["E4_table"]["direct_over_extrap_log10_pi_p"] = [[float(r[0] / G), float(np.log10(r[1] / ext(r[0], 1))), float(np.log10(r[4] / ext(r[0], 4)))] for r in R]
lm = np.log(A[:, 0])
slope = lambda i, k: float((np.log(A[i + 1, k]) - np.log(A[i, k])) / (lm[i + 1] - lm[i]))
out["E4_table"]["local_slope_pi"] = {str(i): slope(i, 1) for i in (0, 1, 2, 3, 5, 10, 15, 20)}
# untruncated-trend estimate at 1e9 g: continue row 5 with the mean local slope of rows 5-10
for k, name in ((1, "pi"), (4, "p")):
    s510 = float(np.mean([slope(i, k) for i in range(5, 11)]))
    y_tr = np.log(A[5, k]) + s510 * (lm[0] - lm[5])
    out["E4_table"][f"row0_truncation_deficit_log10_{name}"] = float(np.log10(A[0, k]) - y_tr / np.log(10))
    out["E4_table"][f"mean_slope_rows5_10_{name}"] = s510
for m0, lab in ((1.121e9, "j22"), (3.494e9, "j62")):
    out["emission_weight"][lab] = {f"m<{ms:.0e}": (ms / m0) ** (-1.20 + 3) for ms in (1e9, 6.3e8, 5e8, 4e8, 2e8)}
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps(out["E4_table"], indent=0)[:1500]); print(json.dumps(out["emission_weight"]))
for k, v in out["baseline_shift"].items():
    print(k, {dl: {a: (round(b, 3) if b is not None else None) for a, b in r.items()} for dl, r in v.items()})
