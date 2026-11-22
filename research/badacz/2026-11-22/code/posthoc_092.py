"""POST-HOC diagnostic for PREREG_092 / REVIEW_093 (NOT preregistered; does not change the k/n score of analysis_092.py).
Usage: python3 -I posthoc_092.py <analysis092.json> <qa_B.csv (2026-11-16/data)> <out.json>
Purpose: estimate native-solver point noise in X from the PY plateau grid in qa_B (0.1-dex steps, log10 beta in [-16.5, -15.0]),
as the residual std of a quadratic fit of dX(log10 beta); propagate to the HER/PY ratio assuming the same point noise for
HER and PY runs and for the two base runs (log10 beta = -30); report z = (ratio - pred)/sigma_ratio per P1 cell, and the
ratio with PY replaced by its quadratic-smoothed value. Assumption flagged: HER noise ~ PY noise (only PY has a dense grid)."""
import csv, json, sys
import numpy as np

a_path, qa, dst = sys.argv[1:4]
A = json.load(open(a_path))
X = lambda Y: Y / (2 + Y)
G = {}
for r in csv.DictReader(l for l in open(qa) if not l.startswith("#")):
    G.setdefault(int(r["j"]), []).append((round(float(r["log10beta"]), 2), float(r["Y"])))
out = {"label": "POST_HOC_NOT_PREREGISTERED", "window": [-16.5, -15.0], "cells": {}, "per_mass": {}}
devs = []; zs = []
for j in (19, 22, 24):
    g = dict(G[j]); XS = X(g[-30.0])
    bs = np.array(sorted(b for b in g if -16.5 - 1e-9 <= b <= -15.0 + 1e-9)); dx = np.array([X(g[b]) - XS for b in bs])
    c = np.polyfit(bs, dx, 2); res = dx - np.polyval(c, bs); sig = float(np.sqrt(np.sum(res ** 2) / (len(bs) - 3)))
    out["per_mass"][str(j)] = {"n": int(len(bs)), "sigma_X_point": sig, "plateau_dX_mean": float(dx.mean()),
                               "dX_slope_end_per_dex": float(2 * c[0] * (-15.0) + c[1]), "quad_coef": [float(v) for v in c]}
    cell = A["cells"][str(j)]
    for lb in (-16, -15):
        h = cell[f"HER_dX_{lb}"]; p = cell[f"PY_dX_{lb}"]; ratio = h / p
        # dX = X(beta) - X(base): two independent points per table
        s_rel = np.sqrt(2 * sig ** 2 / h ** 2 + 2 * sig ** 2 / p ** 2); s_ratio = float(ratio * s_rel)
        pred = A["P1"][f"j{j}_{lb}"]["pred"]; dev = ratio - pred; z = dev / s_ratio
        p_s = float(np.polyval(c, lb))
        out["cells"][f"j{j}_{lb}"] = {"ratio": ratio, "pred": pred, "dev": dev, "sigma_ratio": s_ratio, "z": z,
                                      "ratio_PY_smoothed": h / p_s, "dev_PY_smoothed": h / p_s - pred}
        devs.append(dev); zs.append(z)
out["summary"] = {"mean_dev": float(np.mean(devs)), "n_negative_dev": int(sum(d < 0 for d in devs)), "n": len(devs),
                  "chi2_vs_pred": float(np.sum(np.square(zs))), "dof": len(zs),
                  "caveat": "cells of one mass share base runs and PY grid; deviations are not independent"}
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps(out["summary"])); print(json.dumps(out["per_mass"]))
for k, v in out["cells"].items():
    print(k, "ratio %.4f pred %.3f dev %+.4f sig %.4f z %+.2f | PYsmooth ratio %.4f dev %+.4f" % (v["ratio"], v["pred"], v["dev"], v["sigma_ratio"], v["z"], v["ratio_PY_smoothed"], v["dev_PY_smoothed"]))
