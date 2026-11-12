#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_062 (written before any result was read).
A: Mech-S8 ROT022 smoke CSVs (variants native=C1, p13=C2, native_sym=C3, p13_sym=C4) + cross-check CSV from the REVIEW_053 driver.
   S2 = driver's own SBBN gate value |SBBN_j22_Yp - 0.245| <= 5e-5 (read from the CSV header); S3 = same-runtime T1 printed
   by the REVIEW_053 driver equals 0.099688851247; S4 = |Yp(C1) - 2 X_T1(REVIEW_053 driver)| <= 2e-4 at every smoke point.
   Descriptive only: C2-C1, C3-C1, C4-C1 and interaction (C4-C3)-(C2-C1) per point (Yp units, not roots).
B: REVIEW_061 configs at the default tolerance: 7-point fit roots, Delta = ramp - base; T1: |Delta_default - Delta_1e-4| <= 0.010 dex;
   T2: Delta_default < 0.
Usage: python3 -I wuxu_062_analysis.py <data dir 2026-11-12> <2026-11-11/data/subedge060_analysis.json> <out.json>
"""
import csv, json, math, os, re, sys
import numpy as np

D, ref061, outp = sys.argv[1], sys.argv[2], sys.argv[3]
res = {"A": {}, "B": {}}
# ---------------- A ----------------
var = {"C1": "native", "C2": "p13", "C3": "native_sym", "C4": "p13_sym"}
Y, sbbn, s1 = {}, {}, {}
for c, v in var.items():
    p = os.path.join(D, "rot022_smoke_%s.csv" % v)
    if not os.path.exists(p):
        s1[c] = "NO_OUTPUT"; continue
    txt = open(p).read()
    m = re.search(r"SBBN_j22_Yp=([0-9.eE+-]+)", txt)
    sbbn[c] = float(m.group(1)) if m else None
    rows = list(csv.DictReader(l for l in txt.splitlines() if not l.startswith("#")))
    Y[c] = {(int(r["j"]), r["log10beta"]): float(r["Yp"]) for r in rows}
    s1[c] = "PASS" if len(rows) == 4 else "ROWS_%d" % len(rows)
res["A"]["S1_outputs"] = s1
res["A"]["S2_sbbn_j22_Yp"] = sbbn
res["A"]["S2"] = all(v is not None and abs(v - 0.245) <= 5e-5 for v in sbbn.values()) and len(sbbn) == 4
xp = os.path.join(D, "xcheck062a.csv")
if os.path.exists(xp):
    txt = open(xp).read()
    t1 = re.search(r"SBBN j=22 .*?T1_MeV=([0-9.]+)", txt)
    res["A"]["T1_same_runtime_MeV"] = float(t1.group(1)) if t1 else None
    res["A"]["S3"] = bool(t1) and t1.group(1) == "0.099688851247"
    rows = list(csv.DictReader(l for l in txt.splitlines() if not l.startswith("#")))
    X = {(int(r["j"]), "%.6f" % float(r["log10beta"])): 2 * float(r["X_T1"]) for r in rows}
    d4 = {}
    for k, y in Y.get("C1", {}).items():
        if k in X:
            d4["%d,%s" % k] = y - X[k]
    res["A"]["S4_C1_minus_mine"] = d4
    res["A"]["S4"] = len(d4) == 4 and all(abs(v) <= 2e-4 for v in d4.values())
if all(c in Y for c in var):
    desc = {}
    for k in Y["C1"]:
        a, b, c3, c4 = (Y[c][k] for c in ("C1", "C2", "C3", "C4"))
        desc["%d,%s" % k] = {"C1": a, "C2_minus_C1": b - a, "C3_minus_C1": c3 - a, "C4_minus_C1": c4 - a, "interaction": (c4 - c3) - (b - a)}
    res["A"]["descriptive"] = desc
# ---------------- B ----------------
def fits(path):
    rows = list(csv.DictReader(l for l in open(path) if not l.startswith("#")))
    out = {}
    for cid in sorted({r["id"] for r in rows}):
        pts = [(float(r["log10beta"]), float(r["Yc"])) for r in rows if r["id"] == cid and r["phase"] == "fit"]
        if len(pts) != 7:
            out[cid] = {"n": len(pts)}; continue
        x = np.array([a for a, _ in pts]); y = np.array([b for _, b in pts])
        A = np.vstack([x, np.ones_like(x)]).T; (b, a), *_ = np.linalg.lstsq(A, y, rcond=None)
        s2 = float(np.sum((y - (a + b * x)) ** 2) / 5); cov = s2 * np.linalg.inv(A.T @ A)
        r0 = (0.251 - a) / b; g = np.array([-(0.251 - a) / b ** 2, -1 / b])
        out[cid] = {"root": float(r0), "se": float(math.sqrt(g @ cov @ g)), "sigma_resid": math.sqrt(s2), "n": 7}
    return out
bp = os.path.join(D, "p12_default062b.csv")
if os.path.exists(bp):
    F = fits(bp); ref = json.load(open(ref061))
    res["B"]["fits"] = F
    for j, base, ramp in (("22", "base22d", "ramp22d"), ("28", "base28d", "ramp28d")):
        if "root" not in F.get(base, {}) or "root" not in F.get(ramp, {}):
            res["B"][j] = {"verdict": "NO_RESULT"}; continue
        d = F[ramp]["root"] - F[base]["root"]; d4 = ref["j"][j]["Delta"]
        res["B"][j] = {"Delta_default": d, "se_fit": math.hypot(F[ramp]["se"], F[base]["se"]), "Delta_1e-4": d4,
                       "diff": d - d4, "T1": abs(d - d4) <= 0.010, "T2": d < 0}
json.dump(res, open(outp, "w"), indent=1, allow_nan=False)
print(json.dumps(res, indent=1))
