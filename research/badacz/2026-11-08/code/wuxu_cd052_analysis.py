#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_052 (joint C+D band, j = 22) from data/kernel_cd052.csv.
Root per config: linear least-squares fit of Y_C on log10(beta) over the 7 'fit' points, root at Y_C = 0.251 (as REVIEW_050).
Delta = root(config) - root(base22r); se from the fit residuals (delta method), combined in quadrature.
Usage: python3 -I wuxu_cd052_analysis.py data/kernel_cd052.csv data/kernel_analysis.json out.json
"""
import csv, json, math, sys
import numpy as np
rows = list(csv.DictReader(l for l in open(sys.argv[1]) if not l.startswith("#")))
der = json.load(open(sys.argv[2]))["derived"]["22"]
def fit(cid):
    p = [(float(r["log10beta"]), float(r["Yc"])) for r in rows if r["id"] == cid and r["phase"] == "fit"]
    x, y = np.array([a for a, _ in p]), np.array([b for _, b in p])
    A = np.vstack([x, np.ones_like(x)]).T; (b, a), res, *_ = np.linalg.lstsq(A, y, rcond=None)
    s2 = float(np.sum((y - (a + b*x))**2)/(len(x) - 2)); cov = s2*np.linalg.inv(A.T @ A)
    r0 = (0.251 - a)/b; g = np.array([-(0.251 - a)/b**2, -1/b])
    return {"root": r0, "se": float(math.sqrt(g @ cov @ g)), "slope": float(b), "n": len(x)}
F = {c: fit(c) for c in ("base22r", "CD2_22", "CD0_22")}
sC, sD = der["C2"]["s_eff"], der["Dc"]["s_eff"]; seC, seD = der["C2"]["se_s_eff"], der["Dc"]["se_s_eff"]
sCn, sDn = der["C2"]["s_num"], der["Dc"]["s_num"]
out = {"fits": F, "inputs": {"s_C": sC, "s_D": sD, "se_s_C": seC, "se_s_D": seD, "s_num_C": sCn, "s_num_D": sDn}}
for cid, k in (("CD2_22", 2.0), ("CD0_22", 0.0)):
    D = F[cid]["root"] - F["base22r"]["root"]; seD_ = math.hypot(F[cid]["se"], F["base22r"]["se"])
    a1 = -math.log10(1 + (k - 1)*(sC + sD)); a1se = abs(k - 1)*math.hypot(seC, seD)/(math.log(10)*(1 + (k - 1)*(sC + sD)))
    cnt = -math.log10(1 + (k - 1)*(sCn + sDn))
    s_joint = (10**(-D) - 1)/(k - 1)
    out[cid] = {"Delta": D, "se_Delta": seD_, "pred_A1": a1, "se_pred_A1": a1se, "pred_count": cnt,
                "pred_logadd": (der["C2"]["Delta"] + der["D2"]["Delta"]) if k == 2 else None,
                "s_joint": s_joint, "s_C_plus_s_D": sC + sD, "z_vs_A1": (D - a1)/math.hypot(seD_, a1se)}
v = {"base_drift": bool(abs(F["base22r"]["root"] - (-17.219677940232263)) <= 0.01),
     "P1_CD2_window": bool(-0.174 <= out["CD2_22"]["Delta"] <= -0.124),
     "P2_CD0_window": bool(0.18 <= out["CD0_22"]["Delta"] <= 0.28),
     "F1_CD2_toward_count": bool(out["CD2_22"]["Delta"] > -0.10),
     "F2_CD0_outside_wide": bool(not (0.13 <= out["CD0_22"]["Delta"] <= 0.33))}
out["verdicts"] = v
json.dump(out, open(sys.argv[3], "w"), indent=1)
print(json.dumps(v))
for c in ("base22r", "CD2_22", "CD0_22"):
    print(c, "root %.4f se %.4f slope %.5f" % (F[c]["root"], F[c]["se"], F[c]["slope"]))
for c in ("CD2_22", "CD0_22"):
    o = out[c]; print(c, "Delta %+.4f +- %.4f | A1 %+.4f +- %.4f | count %+.4f | s_joint %.4f vs s_C+s_D %.4f | z %.2f" % (
        o["Delta"], o["se_Delta"], o["pred_A1"], o["se_pred_A1"], o["pred_count"], o["s_joint"], o["s_C_plus_s_D"], o["z_vs_A1"]))
