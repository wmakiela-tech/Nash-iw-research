#!/usr/bin/env python3
"""Badacz (Claude): PREREG_046 (commit f720f80) - boundary (Y_C = 0.251) at j = 22, 24 versus solver tolerance.
Default level: regression root of REVIEW_044 T2 (paired_root.json, 15-point grid). Other levels: linear fit through 3 points
(wuxu_variant_grid_v2.jl, native). j = 22 at 1e-5 reuses REVIEW_044 T3 (tol_native.csv).
Run: python3 -I wuxu_leftwall_convergence_analysis.py --paired paired_root.json --t5j22 tol_native.csv \
        --t4j22 t4_j22.csv --t4j24 t4_j24.csv --t5j24 t5_j24.csv --t6j22 t6_j22.csv --t6j24 t6_j24.csv --out conv.json
Missing files (e.g. an aborted level) may be given as '-'.
"""
import argparse, csv, json
import numpy as np

ap = argparse.ArgumentParser()
for k in ("paired", "t5j22", "t4j22", "t4j24", "t5j24", "t6j22", "t6j24", "out"):
    ap.add_argument("--" + k, required=True)
a = ap.parse_args()
THR = 0.251


def root3(p, j):
    if p == "-":
        return None
    rows = [r for r in csv.DictReader([l for l in open(p) if not l.startswith("#")]) if int(r["j"]) == j]
    if len(rows) < 2:
        return None
    x = np.array([float(r["log10beta"]) for r in rows]); y = np.array([float(r["Yp"]) for r in rows])
    c = np.polyfit(x, y, 1)
    return {"root": float((THR - c[1]) / c[0]), "slope": float(c[0]), "n": int(len(x)), "Y": list(map(float, y))}


P = json.load(open(a.paired))
lv = {22: {"1e-3(default)": {"root": P["fits"]["native"]["22"]["root_lin"], "slope": P["fits"]["native"]["22"]["slope_Y_per_dex"], "n": 15},
           "1e-4": root3(a.t4j22, 22), "1e-5": root3(a.t5j22, 22), "1e-6": root3(a.t6j22, 22)},
      24: {"1e-3(default)": {"root": P["fits"]["native"]["24"]["root_lin"], "slope": P["fits"]["native"]["24"]["slope_Y_per_dex"], "n": 15},
           "1e-4": root3(a.t4j24, 24), "1e-5": root3(a.t5j24, 24), "1e-6": root3(a.t6j24, 24)}}
out = {"levels": {str(j): v for j, v in lv.items()}, "verdicts": {}}
order = ["1e-3(default)", "1e-4", "1e-5", "1e-6"]
fals = False
for j in (22, 24):
    r = [lv[j][k]["root"] if lv[j][k] else None for k in order]
    steps = [None if (r[i] is None or r[i + 1] is None) else r[i + 1] - r[i] for i in range(3)]
    conv = None if steps[2] is None else abs(steps[2])
    total = None if (r[0] is None or r[3] is None) else r[3] - r[0]
    rev = any(steps[i] is not None and steps[i + 1] is not None and steps[i] * steps[i + 1] < 0 and abs(steps[i + 1]) > 0.02
              for i in range(2))
    v = {"roots": dict(zip(order, r)), "steps": steps, "abs_step_1e-5_to_1e-6": conv, "total_default_to_1e-6": total,
         "pred_converged_le_0.015": None if conv is None else conv <= 0.015,
         "pred_total": None if total is None else ((0.015 <= total <= 0.045) if j == 22 else abs(total) <= 0.04),
         "monotone_toward_higher_beta": all(s is None or s >= -0.015 for s in steps),
         "falsifier_nonconvergence_gt_0.03": None if conv is None else conv > 0.03, "falsifier_reversal_gt_0.02": rev}
    fals = fals or bool(v["falsifier_nonconvergence_gt_0.03"]) or rev
    out["verdicts"][str(j)] = v
out["falsified"] = fals
json.dump(out, open(a.out, "w"), indent=1, sort_keys=True)
for j in (22, 24):
    v = out["verdicts"][str(j)]
    print(j, {k: (None if x is None else round(x, 4)) for k, x in v["roots"].items()}, "steps", [None if s is None else round(s, 4) for s in v["steps"]])
print("falsified:", fals)
