#!/usr/bin/env python3
"""Badacz (Claude): PREREG_043 T2/T3 (commit ec6d473) - boundary (Y_C = 0.251) from paired 15-point grids per variant and
mass by least squares (linear; quadratic as curvature check), bootstrap of residuals (2000, seed 20261102) for SE; shifts
variant - native with combined SE; comparison with the bisection shifts of REVIEW_038/042; T3 tolerance check at j = 22.
Run: python3 -I wuxu_paired_root_analysis.py --grid-native g_n.csv --grid-nsym g_s.csv --grid-p13 g_p.csv \
        --bis-native e2_native.csv --bis-nsym e5b_native_nsym.csv --bis-p13 e2_p13.csv \
        --tol-native t_n.csv --tol-nsym t_s.csv --out paired_root.json
"""
import argparse, csv, json, math
import numpy as np

ap = argparse.ArgumentParser()
for k in ("grid-native", "grid-nsym", "grid-p13", "bis-native", "bis-nsym", "bis-p13", "tol-native", "tol-nsym", "out"):
    ap.add_argument("--" + k, required=True)
a = ap.parse_args()
THR = 0.251


def rows(p):
    return list(csv.DictReader([l for l in open(p) if not l.startswith("#")]))


def grid(p):
    d = {}
    for r in rows(p):
        d.setdefault(int(r["j"]), []).append((float(r["log10beta"]), float(r["Yp"])))
    return {j: np.array(sorted(v)) for j, v in d.items()}


def bis(p):
    return {int(r["j"]): float(r["boundary_log10beta"]) for r in rows(p)}


rng = np.random.default_rng(20261102)


def fit(xy, nboot=2000):
    x, y = xy[:, 0], xy[:, 1]
    A = np.vstack([np.ones_like(x), x]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    res = y - A @ coef; sig = float(np.sqrt((res ** 2).sum() / (len(x) - 2)))
    root = (THR - coef[0]) / coef[1]
    boots = []
    for _ in range(nboot):
        yb = A @ coef + rng.choice(res, size=len(res), replace=True)
        cb, *_ = np.linalg.lstsq(A, yb, rcond=None)
        boots.append((THR - cb[0]) / cb[1])
    q = np.polyfit(x, y, 2); rq = np.roots([q[0], q[1], q[2] - THR]).real
    rootq = float(rq[np.argmin(abs(rq - root))])
    return {"root_lin": float(root), "se_boot": float(np.std(boots, ddof=1)), "slope_Y_per_dex": float(coef[1]),
            "sigma_resid": sig, "root_quad": rootq, "quad_minus_lin": float(rootq - root), "n": int(len(x))}


G = {"native": grid(a.grid_native), "nsym": grid(a.grid_nsym), "p13": grid(a.grid_p13)}
B = {"native": bis(a.bis_native), "nsym": bis(a.bis_nsym), "p13": bis(a.bis_p13)}
F = {v: {j: fit(G[v][j]) for j in G[v]} for v in G}
out = {"fits": {v: {str(j): F[v][j] for j in F[v]} for v in F}, "shifts": {}, "T2": {}, "T3": {}}
fals = []; preds = []
for v in ("nsym", "p13"):
    for j in sorted(F[v]):
        s = F[v][j]["root_lin"] - F["native"][j]["root_lin"]
        se = math.hypot(F[v][j]["se_boot"], F["native"][j]["se_boot"])
        sb = B[v][j] - B["native"][j]
        e = {"shift_regression": s, "se": se, "shift_bisection": sb, "reg_minus_bis": s - sb, "abs_over_se": abs(s) / se}
        out["shifts"][f"{v}_j{j}"] = e
        preds.append(abs(s - sb) <= max(0.015, 3 * se) and math.copysign(1, s) == math.copysign(1, sb) and abs(s) / se > 5)
        fals.append(math.copysign(1, s) != math.copysign(1, sb) or abs(s - sb) > max(0.02, 4 * se))
sig_max = max(F[v][j]["sigma_resid"] for v in F for j in F[v])
out["T2"] = {"sigma_resid_max": sig_max, "pred_sigma_le_2e-4": sig_max <= 2e-4, "pred_shifts_all": all(preds),
             "falsified": any(fals) or sig_max > 4e-4}
# T3: tolerance (reltol 1e-5) at j = 22, 3 points per variant
tn, ts = grid(a.tol_native)[22], grid(a.tol_nsym)[22]


def lin_root(xy):
    c = np.polyfit(xy[:, 0], xy[:, 1], 1); return float((THR - c[1]) / c[0]), float(c[0])


rn, sn = lin_root(tn); rs, ss = lin_root(ts)
s_tol = rs - rn; s_def = B["nsym"][22] - B["native"][22]
out["T3"] = {"root_native_tol": rn, "root_nsym_tol": rs, "slope_native": sn, "slope_nsym": ss, "shift_tol": s_tol,
             "shift_default_bisection": s_def, "diff": s_tol - s_def, "pred_within_0.02": abs(s_tol - s_def) <= 0.02,
             "falsified": abs(s_tol - s_def) > 0.04 or math.copysign(1, s_tol) != math.copysign(1, s_def),
             "native_default_bisection_root": B["native"][22], "native_tol_minus_default": rn - B["native"][22]}
json.dump(out, open(a.out, "w"), indent=1, sort_keys=True)
print(json.dumps({"T2_sigma_max": sig_max, "T2_pred": out["T2"]["pred_shifts_all"], "T2_falsified": out["T2"]["falsified"],
                  "T3_shift_tol": round(s_tol, 4), "T3_shift_def": round(s_def, 4), "T3_falsified": out["T3"]["falsified"]}))
for k, e in out["shifts"].items():
    print(k, "reg %+.4f ± %.4f  bis %+.4f  diff %+.4f" % (e["shift_regression"], e["se"], e["shift_bisection"], e["reg_minus_bis"]))
