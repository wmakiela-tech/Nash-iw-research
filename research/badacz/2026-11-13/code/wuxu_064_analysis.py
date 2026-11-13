#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_064 (written before any result was read).
Inputs: yp064_tol_p1.csv (g22t + d22t_a, reltol 1e-4), yp064_tol_p2.csv (d22t_b, 1e-4), yp064_default.csv (d22d, default).
Criteria per variant: V0 = Yc_native - 0.251; V1 = 2 X_T1 - 0.251; V2 = 2 X_T0 - 2 X0s - 0.006, X0s from the same file's SBBN j=22 line.
Methods: M_A REVIEW_053 quadratic through the 4 points around the first sign change, on g22t;
         M_B same on the dense grid; M_C linear interpolation between the bracketing dense points; M_D 7-point OLS line on the
         dense points nearest the sign change. S = max - min over methods (1e-4); J1 if S(V2) <= 0.010 and S(V2-V0) <= 0.010,
         J0 if either >= 0.020, else INCONCLUSIVE. Diagnostics: same methods M_B..M_D on the default dense grid; rms residual
         about a quadratic through all dense points; SBBN T1/X0s per file.
Usage: python3 -I wuxu_064_analysis.py <data dir 2026-11-13> <out.json>
"""
import csv, json, math, os, re, sys
import numpy as np

D, outp = sys.argv[1], sys.argv[2]
def load(name):
    txt = open(os.path.join(D, name)).read()
    m = re.search(r"SBBN j=22 .*?X0s=([0-9.]+) .*?T1_MeV=([0-9.]+)", txt)
    rows = list(csv.DictReader(l for l in txt.splitlines() if not l.startswith("#")))
    return {"X0s": float(m.group(1)), "T1": float(m.group(2)), "rows": rows}
def series(rows, ids, X0s):
    pts = sorted((float(r["log10beta"]), r) for r in rows if r["id"] in ids)
    lb = np.array([p[0] for p in pts])
    f = {"V0": np.array([float(r["Yc_native"]) - 0.251 for _, r in pts]),
         "V1": np.array([2 * float(r["X_T1"]) - 0.251 for _, r in pts]),
         "V2": np.array([2 * float(r["X_T0"]) - 2 * X0s - 0.006 for _, r in pts])}
    return lb, f
def first_change(y):
    for i in range(len(y) - 1):
        if y[i] < 0 <= y[i + 1]:
            return i
    return None
def m_quad4(lb, y):                       # REVIEW_053 rule: quadratic LSQ through the 4 points around the first sign change
    i = first_change(y)
    if i is None: return None
    sel = slice(max(0, i - 1), min(len(y), i + 3)); x0 = lb[i]
    c = np.polyfit(lb[sel] - x0, y[sel], 2); rr = np.roots(c); rr = rr[np.isreal(rr)].real + x0
    rr = [r for r in rr if lb[max(0, i - 1)] - 1e-9 <= r <= lb[min(len(y), i + 3) - 1] + 1e-9]
    return float(min(rr, key=lambda r: abs(r - lb[i]))) if rr else None
def m_lin(lb, y):
    i = first_change(y)
    if i is None: return None
    return float(lb[i] - y[i] * (lb[i + 1] - lb[i]) / (y[i + 1] - y[i]))
def m_ols7(lb, y):
    r0 = m_lin(lb, y)
    if r0 is None: return None
    idx = np.argsort(np.abs(lb - r0))[:7]
    b, a = np.polyfit(lb[idx], y[idx], 1)
    return float(-a / b)
def rms_quad(lb, y):
    c = np.polyfit(lb - lb.mean(), y, 2)
    return float(np.sqrt(np.mean((y - np.polyval(c, lb - lb.mean())) ** 2)))
T1, T2, TD = load("yp064_tol_p1.csv"), load("yp064_tol_p2.csv"), load("yp064_default.csv")
res = {"sbbn": {"tol_p1": {"X0s": T1["X0s"], "T1": T1["T1"]}, "tol_p2": {"X0s": T2["X0s"], "T1": T2["T1"]},
                "default": {"X0s": TD["X0s"], "T1": TD["T1"]}, "REVIEW_053": {"X0s": 0.109037947009, "T1": 0.099688851247}}}
X0t = T1["X0s"]
lg, fg = series(T1["rows"], {"g22t"}, X0t)
ld, fd = series(T1["rows"] + T2["rows"], {"d22t_a", "d22t_b"}, X0t)
lD, fD = series(TD["rows"], {"d22d"}, TD["X0s"])
out = {"tol_1e-4": {}, "default": {}}
for v in ("V0", "V1", "V2"):
    out["tol_1e-4"][v] = {"M_A": m_quad4(lg, fg[v]), "M_B": m_quad4(ld, fd[v]), "M_C": m_lin(ld, fd[v]), "M_D": m_ols7(ld, fd[v]),
                          "rms_about_quadratic_dense": rms_quad(ld, fd[v])}
    out["default"][v] = {"M_B": m_quad4(lD, fD[v]), "M_C": m_lin(lD, fD[v]), "M_D": m_ols7(lD, fD[v]),
                         "rms_about_quadratic_dense": rms_quad(lD, fD[v])}
def spread(d, keys):
    vals = [d[k] for k in keys if d.get(k) is not None]
    return (max(vals) - min(vals)) if len(vals) == len(keys) else None
for tol, keys in (("tol_1e-4", ("M_A", "M_B", "M_C", "M_D")), ("default", ("M_B", "M_C", "M_D"))):
    o = out[tol]
    for v in ("V1", "V2"):
        o["shift_%s_minus_V0" % v] = {k: (o[v][k] - o["V0"][k]) if (o[v].get(k) is not None and o["V0"].get(k) is not None) else None for k in keys}
    o["S"] = {"V0": spread(o["V0"], keys), "V1": spread(o["V1"], keys), "V2": spread(o["V2"], keys),
              "V1_minus_V0": spread(o["shift_V1_minus_V0"], keys), "V2_minus_V0": spread(o["shift_V2_minus_V0"], keys)}
S = out["tol_1e-4"]["S"]
if S["V2"] is None or S["V2_minus_V0"] is None:
    verdict = "NO_RESULT"
elif S["V2"] <= 0.010 and S["V2_minus_V0"] <= 0.010:
    verdict = "J1_JAGGEDNESS_EXPLANATION_HOLDS"
elif S["V2"] >= 0.020 or S["V2_minus_V0"] >= 0.020:
    verdict = "J0_JAGGEDNESS_EXPLANATION_FALSIFIED"
else:
    verdict = "INCONCLUSIVE"
res.update(out); res["verdict"] = verdict
res["reference"] = {"REVIEW_053_default": {"V0": -17.215, "V1": -17.140, "V2": -17.020870078767746, "shift_V2": 0.194243854464240},
                    "L2_GPT_bisection_default": {"V2": -16.9974609375, "shift_V2": 0.2265625}}
json.dump(res, open(outp, "w"), indent=1, allow_nan=False)
print(json.dumps(res, indent=1))
