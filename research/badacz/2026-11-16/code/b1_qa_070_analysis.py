#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_070 (B1 question Q-A, native regime map). Written BEFORE any Q-A run.
Inputs (in <dir>): qa_A.csv, qa_B.csv from code/b1_t2_contour_069.jl (arm orig, tol default) with configs cfg070_*.dat.
Per mass j: X = Y/(2+Y) (exact inverse of Y_code = 2X/(1-X)); baseline X_S = X at log10 beta = -30 (SBBN proxy, as REVIEW_053/064);
dX = X - X_S, dY = Y - Y_S. Local log-slope s at grid node k = OLS slope of ln(dQ) on ln(beta) over the 5 nodes k-2..k+2
(span 0.4 dex), for Q in {X (primary), Y (EKS1-comparable)}.
Noise model: sigma_X = 1.4e-5 per point (REVIEW_067, measured solver noise floor at default tolerance; one point, assumed
transferable - stated assumption); sigma_Y = 3.6e-5. Node is RESOLVABLE if dQ >= 1e-3 at all 5 nodes (then sigma_s <~ 0.05).
Labels on resolvable nodes: LINEAR s >= 0.9; INTERMEDIATE 0.3 < s < 0.9; SATURATION s <= 0.3.
Frozen predictions (from EKS1 ROT011 archive analysis; native data are independent production, analysis idea is not):
  P-A1: grid A (beta <= 1e-17): no resolvable node with s_X <= 0.3 at any of the 6 masses       -> PASS/FAIL
  P-A2: s_Y at node log10 beta = -17.2 for j = 22, 28, 38 lies in [0.35, 0.70]                   -> PASS/FAIL/UNRESOLVED
  P-A3: s_Y at node log10 beta = -18.2 for j = 22, 28, 38 lies in [0.75, 1.05]                   -> PASS/FAIL/UNRESOLVED
  Grid B (OFF-SCAN, beta to 1e-15, j = 19, 22, 24): exploratory, no prediction; report first resolvable SATURATION node if any.
Usage: python3 -I b1_qa_070_analysis.py <dir> <out.json>
"""
import csv, json, os, sys, numpy as np
D, outp = sys.argv[1], sys.argv[2]
SIG = {"X": 1.4e-5, "Y": 3.6e-5}
def load(name):
    p = os.path.join(D, name)
    if not os.path.exists(p): return {}
    out = {}
    for r in csv.DictReader(l for l in open(p) if not l.startswith("#")):
        out.setdefault(int(r["j"]), {})[round(float(r["log10beta"]), 6)] = float(r["Y"])
    return out
def regime_map(series):
    res = {}
    for j, pts in series.items():
        if -30.0 not in pts: res[j] = {"error": "no SBBN baseline"}; continue
        YS = pts[-30.0]; XS = YS / (2 + YS)
        lb = np.array(sorted(k for k in pts if k > -29)); Y = np.array([pts[k] for k in lb]); X = Y / (2 + Y)
        dQ = {"X": X - XS, "Y": Y - YS}; nodes = []
        for k in range(2, len(lb) - 2):
            rec = {"log10beta": float(lb[k])}
            for q in ("X", "Y"):
                w = dQ[q][k - 2:k + 3]
                if np.all(w > 0):
                    sl, _ = np.polyfit(lb[k - 2:k + 3] * np.log(10), np.log(w), 1)
                    rel = SIG[q] / w; xs = lb[k - 2:k + 3] * np.log(10)
                    sig_s = float(np.sqrt(np.sum(rel ** 2 * ((xs - xs.mean()) / np.sum((xs - xs.mean()) ** 2)) ** 2)))
                    resolv = bool(np.all(w >= 1e-3))
                    lab = None if not resolv else ("LINEAR" if sl >= 0.9 else ("SATURATION" if sl <= 0.3 else "INTERMEDIATE"))
                    rec[q] = {"s": float(sl), "sigma_s": sig_s, "dQ": float(dQ[q][k]), "resolvable": resolv, "label": lab}
                else:
                    rec[q] = {"s": None, "dQ": float(dQ[q][k]), "resolvable": False, "label": None}
            nodes.append(rec)
        res[j] = {"X_SBBN": float(XS), "Y_SBBN": float(YS), "nodes": nodes}
    return res
A = regime_map(load("qa_A.csv")); B = regime_map(load("qa_B.csv"))
def node(m, j, lb):
    for n in m.get(j, {}).get("nodes", []):
        if abs(n["log10beta"] - lb) < 1e-9: return n
def pwin(m, lb, lo, hi):
    out = {}
    for j in (22, 28, 38):
        n = node(m, j, lb)
        if n is None or not n["Y"]["resolvable"]: out[j] = "UNRESOLVED"
        else: out[j] = "PASS" if lo <= n["Y"]["s"] <= hi else "FAIL"
    return out
v = {}
if A:
    sat = [(j, n["log10beta"]) for j, r in A.items() for n in r.get("nodes", []) if n["X"].get("label") == "SATURATION"]
    v["P-A1"] = {"verdict": "PASS" if not sat else "FAIL", "saturation_nodes": sat}
    v["P-A2"] = pwin(A, -17.2, 0.35, 0.70); v["P-A3"] = pwin(A, -18.2, 0.75, 1.05)
if B:
    v["B_first_saturation"] = {j: next((n["log10beta"] for n in r.get("nodes", []) if n["X"].get("label") == "SATURATION"), None) for j, r in B.items()}
json.dump({"A": A, "B": B, "verdicts": v}, open(outp, "w"), indent=1)
print(json.dumps(v, indent=1))
