#!/usr/bin/env python3
"""Badacz (Claude): POST HOC decomposition for PREREG_064 (written after reading the preregistered verdict J0).
1. Spread over the dense-grid methods only (M_B, M_C, M_D) at both tolerances.
2. V2 calibration swap: V2 criterion 2 X(T0) - 2 X0s - 0.006 evaluated on the 1e-4 dense data with the DEFAULT-tolerance X0s,
   and on the default dense data with the 1e-4 X0s -> separates the SBBN-reference (X0s) part of the tolerance shift from the
   change of the X(T0) curve itself.
3. REVIEW_053 coarse-grid method applied to the DEFAULT dense data restricted to the 9 g22 offsets is not possible (different
   points); instead the coarse-vs-dense contrast at default is taken from REVIEW_053 itself (-17.0209) vs dense M_B..M_D.
Usage: python3 -I wuxu_064_posthoc_decomp.py <data dir 2026-11-13> <analysis064.json> <out.json>
"""
import json, sys, os
D, a064, outp = sys.argv[1], sys.argv[2], sys.argv[3]
import numpy as np, csv, re

def load(name):
    txt = open(os.path.join(D, name)).read()
    m = re.search(r"SBBN j=22 .*?X0s=([0-9.]+) .*?T1_MeV=([0-9.]+)", txt)
    rows = list(csv.DictReader(l for l in txt.splitlines() if not l.startswith("#")))
    return float(m.group(1)), rows
def dense(rows, ids, X0s):
    pts = sorted((float(r["log10beta"]), r) for r in rows if r["id"] in ids)
    lb = np.array([p[0] for p in pts])
    v0 = np.array([float(r["Yc_native"]) - 0.251 for _, r in pts])
    v2 = np.array([2 * float(r["X_T0"]) - 2 * X0s - 0.006 for _, r in pts])
    return lb, v0, v2
def first_change(y):
    for i in range(len(y) - 1):
        if y[i] < 0 <= y[i + 1]: return i
def m_quad4(lb, y):
    i = first_change(y); sel = slice(max(0, i - 1), min(len(y), i + 3)); x0 = lb[i]
    c = np.polyfit(lb[sel] - x0, y[sel], 2); rr = np.roots(c); rr = rr[np.isreal(rr)].real + x0
    rr = [r for r in rr if lb[max(0, i - 1)] - 1e-9 <= r <= lb[min(len(y), i + 3) - 1] + 1e-9]
    return float(min(rr, key=lambda r: abs(r - lb[i])))
def m_lin(lb, y):
    i = first_change(y); return float(lb[i] - y[i] * (lb[i + 1] - lb[i]) / (y[i + 1] - y[i]))
def m_ols7(lb, y):
    r0 = m_lin(lb, y); idx = np.argsort(np.abs(lb - r0))[:7]; b, a = np.polyfit(lb[idx], y[idx], 1); return float(-a / b)
M = {"M_B": m_quad4, "M_C": m_lin, "M_D": m_ols7}
X0t, r1 = load("yp064_tol_p1.csv"); _, r2 = load("yp064_tol_p2.csv"); X0d, rd = load("yp064_default.csv")
out = {"X0s": {"tol_1e-4": X0t, "default": X0d, "diff": X0t - X0d}}
A = json.load(open(a064))
for tol in ("tol_1e-4", "default"):
    o = A[tol]; s = {}
    for v in ("V0", "V1", "V2"):
        vals = [o[v][k] for k in M]; s[v] = max(vals) - min(vals)
    for v in ("V1", "V2"):
        vals = [o["shift_%s_minus_V0" % v][k] for k in M]; s["%s_minus_V0" % v] = max(vals) - min(vals)
    out["dense_only_spread_" + tol] = s
lt, v0t, v2t_own = dense(r1 + r2, {"d22t_a", "d22t_b"}, X0t)
_, _, v2t_defX = dense(r1 + r2, {"d22t_a", "d22t_b"}, X0d)
ld, v0d, v2d_own = dense(rd, {"d22d"}, X0d)
_, _, v2d_tolX = dense(rd, {"d22d"}, X0t)
out["V2_root_swap"] = {k: {"tol_data_own_X0s": f(lt, v2t_own), "tol_data_default_X0s": f(lt, v2t_defX),
                           "default_data_own_X0s": f(ld, v2d_own), "default_data_tol_X0s": f(ld, v2d_tolX)} for k, f in M.items()}
json.dump(out, open(outp, "w"), indent=1, allow_nan=False)
print(json.dumps(out, indent=1))
