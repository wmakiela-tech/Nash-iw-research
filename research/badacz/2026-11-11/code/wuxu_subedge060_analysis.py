#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_060 (native root shift under the p12 sub-edge extrapolation, j = 22 and 28).
Root per config: linear least squares of Y_C on log10(beta) over the 7 'fit' points, root at Y_C = 0.251 (as REVIEW_050/054/059).
Delta = root(ramp) - root(base, same run, same j). Verdicts P1 (j22) / P2 (j28): Delta inside the preregistered window.
Diagnostics: location l = (Delta - Delta_weak)/(Delta_strong - Delta_weak); fit SE of Delta (quadrature of the two root SEs),
reported separately from the 0.010 dex solver allowance.
Usage: python3 -I wuxu_subedge060_analysis.py <subedge060_p1.csv> <subedge060_p2.csv> <subedge_ramp060_prediction.json> <out.json>
"""
import csv, json, math, sys
import numpy as np

def fits(paths):
    rows = []
    for p in paths:
        rows += list(csv.DictReader(l for l in open(p) if not l.startswith("#")))
    out = {}
    for cid in sorted({r["id"] for r in rows}):
        pts = [(float(r["log10beta"]), float(r["Yc"])) for r in rows if r["id"] == cid and r["phase"] == "fit"]
        if len(pts) != 7:
            out[cid] = {"n": len(pts), "error": "expected 7 fit points"}; continue
        x = np.array([a for a, _ in pts]); y = np.array([b for _, b in pts])
        A = np.vstack([x, np.ones_like(x)]).T; (b, a), *_ = np.linalg.lstsq(A, y, rcond=None)
        s2 = float(np.sum((y - (a + b * x)) ** 2) / (len(x) - 2)); cov = s2 * np.linalg.inv(A.T @ A)
        r0 = (0.251 - a) / b; g = np.array([-(0.251 - a) / b ** 2, -1 / b])
        out[cid] = {"root": float(r0), "se": float(math.sqrt(g @ cov @ g)), "slope": float(b), "sigma_resid": math.sqrt(s2), "n": len(x),
                    "evaluations": sum(1 for r in rows if r["id"] == cid), "seconds": sum(float(r["seconds"]) for r in rows if r["id"] == cid)}
    return out

F = fits(sys.argv[1:3]); pred = json.load(open(sys.argv[3]))
res = {"fits": F, "j": {}}
for j, base, ramp, crit in (("22", "base22u", "ramp22", "P1"), ("28", "base28u", "ramp28", "P2")):
    pj = pred["j"][j]
    if "root" not in F.get(base, {}) or "root" not in F.get(ramp, {}):
        res["j"][j] = {"verdict": crit + "_NO_RESULT"}; continue
    d = F[ramp]["root"] - F[base]["root"]; se = math.hypot(F[ramp]["se"], F[base]["se"])
    lo, hi = pj["window"]
    loc = (d - pj["Delta_weak"]) / (pj["Delta_strong"] - pj["Delta_weak"])
    res["j"][j] = {"Delta": d, "se_fit_Delta": se, "window": [lo, hi], "inside": lo <= d <= hi,
                   "verdict": crit + ("_PASS" if lo <= d <= hi else "_FAIL"),
                   "Delta_weak": pj["Delta_weak"], "Delta_strong": pj["Delta_strong"], "Delta_central": pj["Delta_central"],
                   "location_l": loc, "minus_central": d - pj["Delta_central"],
                   "s_total_equivalent_k_uniform": None}
json.dump(res, open(sys.argv[4], "w"), indent=1, allow_nan=False)
for c, f in F.items():
    print(c, {k: (round(v, 5) if isinstance(v, float) else v) for k, v in f.items()})
for j, v in res["j"].items():
    print("j=%s" % j, {k: (round(x, 4) if isinstance(x, float) else x) for k, x in v.items() if x is not None})
