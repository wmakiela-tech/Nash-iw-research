"""PREREG_092: scoring of EKS1 DIR-008 frozen predictions (EKS1 ROT014, Nash-Priv research/eks1/2026-11-21/) on native runs.
Usage: python3 -I analysis_092.py <run_dir> <qa_B.csv (2026-11-16/data)> <out.json>
Definitions (as in PREREG_070/REVIEW_072 and EKS1 ROT014): X = Y/(2+Y); X_S = X at log10 beta = -30 (same mass, same table);
dX = X - X_S; threshold V0: X_c = 0.251/2.251;  r = dX / (X_c - X_S)  (r > 1 <=> Y > 0.251 at that beta).
P1 (6 numbers, tolerance +-0.02): ratio dX_HER/dX_PY at beta = 1e-16 and 1e-15 for j19, j22, j24; predicted
  j19 0.964/0.975, j22 0.964/0.977, j24 0.965/0.981.  PY values for j19/22/24 from qa_B.csv (driver-identity control:
  fresh PY j22 at -16 must equal qa_B bitwise).
P2 (2 labels): j21 no crossing up to 1e-15 for both tables (r < 1 at -16 and -15); j22 crossing for both (r > 1 at -15).
Rejection of the thesis (EKS1): any P1 ratio at 1e-15 below 0.90, or P2 reversed for a table.
Noise note (not a gate): native solver noise in Y ~ 1e-5..1e-4 (REVIEW_086 r2, 089) -> ratio noise ~ 1e-4/dX."""
import csv, json, sys

run, qa, dst = sys.argv[1:4]
rd = lambda p: {r["run_id"]: r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))}
H = rd(f"{run}/dump_h/summary_orig.csv"); P = rd(f"{run}/dump_p/summary_orig.csv")
Q = {}
for r in csv.DictReader(l for l in open(qa) if not l.startswith("#")):
    Q[(int(r["j"]), round(float(r["log10beta"]), 2))] = float(r["Y"])
X = lambda Y: Y / (2 + Y)
Xc = 0.251 / 2.251
def py(j, lb):
    if j == 21:
        key = {-30: "p21_base", -16: "p21_1600", -15: "p21_1500"}[lb]
        return float(P[key]["Y"])
    return Q[(j, float(lb))]
def her(j, lb):
    key = {-30: f"h{j}_base", -16: f"h{j}_1600", -15: f"h{j}_1500"}[lb]
    return float(H[key]["Y"])
out = {"control": {}, "cells": {}, "P1": {}, "P2": {}}
out["control"]["py_j22_m16_fresh_vs_qaB"] = {"fresh": float(P["p22_1600"]["Y"]), "qa_B": Q[(22, -16.0)], "bitwise": float(P["p22_1600"]["Y"]) == Q[(22, -16.0)]}
pred = {19: (0.964, 0.975), 22: (0.964, 0.977), 24: (0.965, 0.981)}
k1 = 0; rej = False
for j in (19, 21, 22, 24):
    c = {}
    for name, f in (("PY", py), ("HER", her)):
        XS = X(f(j, -30))
        for lb in (-16, -15):
            dX = X(f(j, lb)) - XS
            c[f"{name}_dX_{lb}"] = dX; c[f"{name}_r_{lb}"] = dX / (Xc - XS)
    out["cells"][str(j)] = c
    if j in pred:
        for i, lb in enumerate((-16, -15)):
            ratio = c[f"HER_dX_{lb}"] / c[f"PY_dX_{lb}"]
            ok = abs(ratio - pred[j][i]) <= 0.02
            k1 += ok
            out["P1"][f"j{j}_{lb}"] = {"ratio": ratio, "pred": pred[j][i], "pass": ok}
            if lb == -15 and ratio < 0.90:
                rej = True
c21 = out["cells"]["21"]; c22 = out["cells"]["22"]
p2a = {t: (c21[f"{t}_r_-16"] < 1 and c21[f"{t}_r_-15"] < 1) for t in ("PY", "HER")}
p2b = {t: (c22[f"{t}_r_-15"] > 1) for t in ("PY", "HER")}
out["P2"] = {"j21_no_crossing": p2a, "j22_crossing": p2b, "j21_pass": all(p2a.values()), "j22_pass": all(p2b.values()),
             "pred_model_r": {"j21_PY": 0.93, "j21_HER": 0.91, "j22_PY": 1.51, "j22_HER": 1.48}}
if not all(p2a.values()) or not all(p2b.values()):
    rej = True
out["score"] = {"P1": f"{k1}/6", "P2": f"{int(out['P2']['j21_pass']) + int(out['P2']['j22_pass'])}/2", "thesis_rejected": rej}
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps(out["score"])); print(json.dumps(out["P1"])); print(json.dumps(out["P2"])); print(json.dumps(out["control"]))
