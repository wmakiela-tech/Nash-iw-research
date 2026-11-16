#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_069 (B1 Q-B, test T2). Written and committed BEFORE any T2 run.
Inputs: CSVs of code/b1_t2_contour_069.jl: t2_orig_default.csv, t2_e5_default.csv, t2_orig_1e-4.csv, t2_e5_1e-4.csv (in <dir>).
Root of y = Y - 0.251 by the REVIEW_065 methods (copied unchanged from 2026-11-13/code/wuxu_064_analysis.py):
  M_B quadratic LSQ through the 4 points around the first sign change; M_C linear between bracketing points;
  M_D 7-point OLS line around the M_C root  (PRIMARY).
Shift D_j = root_e5 - root_orig (M_D, default tolerance).
Frozen verdicts:  W  : all 6 D_j in [+0.20, +0.35] dex  -> W-PASS, else W-FAIL (any missing root -> W-INCOMPLETE)
                  ORD: D_90 >= D_22                       -> ORD-PASS / ORD-FAIL
                  TOL: |D_j(1e-4) - D_j(default)| <= 0.03 for j = 22 and 62 -> TOL-STABLE / TOL-UNSTABLE
Descriptive: method spread of D_j; OLS standard error of each root; number of sign changes per series (jaggedness);
D_j - REVIEW_038 shift; D_j vs log10(2); orig roots vs authors' archive roots (scanning.jld2 row j, linear interpolation).
Usage: python3 -I b1_t2_069_analysis.py <dir> <scanning.jld2> <out.json>
"""
import csv, json, os, sys, zlib, numpy as np
D, jld, outp = sys.argv[1], sys.argv[2], sys.argv[3]
THR = 0.251; MASSES = (22, 28, 38, 51, 62, 90)
S038 = {22: 0.279, 28: 0.268, 38: 0.281, 51: 0.287, 62: 0.295, 90: 0.301}
def first_change(y):
    for i in range(len(y) - 1):
        if y[i] < 0 <= y[i + 1]:
            return i
    return None
def m_quad4(lb, y):
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
def ols7_se(lb, y):
    r0 = m_lin(lb, y)
    if r0 is None: return None
    idx = np.argsort(np.abs(lb - r0))[:7]; x = lb[idx]; yy = y[idx]
    b, a = np.polyfit(x, yy, 1); res = yy - (a + b * x); n = len(x)
    s2 = float(np.sum(res ** 2) / (n - 2)); root = -a / b; sxx = float(np.sum((x - x.mean()) ** 2))
    return float(np.sqrt(s2) / abs(b) * np.sqrt(1.0 / n + (root - x.mean()) ** 2 / sxx))
def load(name):
    p = os.path.join(D, name)
    if not os.path.exists(p): return {}
    rows = list(csv.DictReader(l for l in open(p) if not l.startswith("#")))
    out = {}
    for r in rows:
        out.setdefault(int(r["j"]), []).append((float(r["log10beta"]), float(r["Y"])))
    return {j: (np.array([a for a, _ in sorted(v)]), np.array([b for _, b in sorted(v)]) - THR) for j, v in out.items()}
def roots(series):
    res = {}
    for j, (lb, y) in series.items():
        res[j] = {"M_B": m_quad4(lb, y), "M_C": m_lin(lb, y), "M_D": m_ols7(lb, y), "se_M_D": ols7_se(lb, y),
                  "n_sign_changes": int(np.sum(np.diff(np.sign(y)) != 0)), "n": int(len(lb))}
    return res
b = open(jld, "rb").read(); streams = []; i = 0
while i < len(b) - 2:
    if b[i] == 0x78 and b[i + 1] in (0x01, 0x5e, 0x9c, 0xda):
        try:
            d = zlib.decompressobj(); o = d.decompress(b[i:]); used = len(b[i:]) - len(d.unused_data)
            if len(o) >= 64: streams.append(np.frombuffer(o, "<f8")); i += used; continue
        except Exception: pass
    i += 1
lb_arch = np.log10(streams[1]); Ymat = [s for s in streams[2:] if s.max() < 2][0].reshape((100, 100), order="F")
R = {k: roots(load("t2_%s.csv" % k)) for k in ("orig_default", "e5_default", "orig_1e-4", "e5_1e-4")}
out = {"roots": R, "shift": {}, "verdicts": {}}
for j in MASSES:
    ro, re_ = R["orig_default"].get(j), R["e5_default"].get(j)
    if not ro or not re_ or ro["M_D"] is None or re_["M_D"] is None:
        out["shift"][j] = None; continue
    dm = {m: (re_[m] - ro[m]) if (re_[m] is not None and ro[m] is not None) else None for m in ("M_B", "M_C", "M_D")}
    vals = [v for v in dm.values() if v is not None]
    r = Ymat[j]; k = np.where((r[:-1] < THR) & (r[1:] >= THR))[0][0]
    arch_root = float(lb_arch[k] + (THR - r[k]) * (lb_arch[k + 1] - lb_arch[k]) / (r[k + 1] - r[k]))
    out["shift"][j] = {"D_M_D": dm["M_D"], "D_by_method": dm, "method_spread": max(vals) - min(vals),
                       "se_D_M_D": float(np.hypot(ro["se_M_D"], re_["se_M_D"])), "D_minus_REVIEW038": dm["M_D"] - S038[j],
                       "D_minus_log10_2": dm["M_D"] - float(np.log10(2)), "orig_root_minus_archive_root": ro["M_D"] - arch_root,
                       "archive_root": arch_root}
D_ = {j: (out["shift"][j]["D_M_D"] if out["shift"][j] else None) for j in MASSES}
if any(v is None for v in D_.values()):
    out["verdicts"]["W"] = "W-INCOMPLETE"
else:
    out["verdicts"]["W"] = "W-PASS" if all(0.20 <= v <= 0.35 for v in D_.values()) else "W-FAIL"
out["verdicts"]["ORD"] = None if (D_[90] is None or D_[22] is None) else ("ORD-PASS" if D_[90] >= D_[22] else "ORD-FAIL")
tolc = {}
for j in (22, 62):
    a, c = R["orig_1e-4"].get(j), R["e5_1e-4"].get(j)
    if a and c and a["M_D"] is not None and c["M_D"] is not None and D_[j] is not None:
        tolc[j] = {"D_1e-4": c["M_D"] - a["M_D"], "diff_vs_default": (c["M_D"] - a["M_D"]) - D_[j],
                   "orig_root_1e-4_minus_default": a["M_D"] - R["orig_default"][j]["M_D"]}
out["tol_check"] = tolc
out["verdicts"]["TOL"] = None if len(tolc) < 2 else ("TOL-STABLE" if all(abs(v["diff_vs_default"]) <= 0.03 for v in tolc.values()) else "TOL-UNSTABLE")
json.dump(out, open(outp, "w"), indent=1, default=lambda o: None)
print(json.dumps({"verdicts": out["verdicts"], "D_M_D": D_, "tol_check": tolc}, indent=1))
