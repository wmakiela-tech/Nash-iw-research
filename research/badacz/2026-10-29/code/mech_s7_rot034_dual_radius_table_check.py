#!/usr/bin/env python3
"""Independent cross-family check of Mech-S7 ROT034 (Badacz, Claude thread).

C5: formula  max{|g^T b| : b^T H b <= R^2, |a_i^T b| <= d_i}
           = min_lam R ||g - A lam||_{H^-1} + sum_i d_i |lam_i|
    Primal solved EXACTLY by enumerating KKT faces (active slab sets with signs);
    dual minimised numerically (grid + Nelder-Mead). Random instances incl. eta=0,
    near-collinear slabs (corr 0.98) and large eta.
C7: internal consistency of the ROT034 table. From three reported numbers
    (one-statistic residual 5.05794%, two-statistic residual 1.35013%,
     H^-1 correlation of the two rows 0.9817345571012799) the normalised Gram
    of (g, a1, a2) is fixed up to one sign; the remaining table entries
    (eta = .001, .01, .02, .05, .10) are then PREDICTED and compared.
    Assumption: the worst of the six targets is the same target in every cell.
"""
import json, argparse, itertools, math
import numpy as np
from scipy.optimize import minimize

ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); args = ap.parse_args()
rng = np.random.default_rng(20261029)
res = {}


def primal_exact(gh, Ah, R, d):
    """max gh^T x s.t. ||x||<=R, |Ah[:,i]^T x| <= d_i  (whitened). Enumerate faces."""
    k = Ah.shape[1]; best = -np.inf
    for S in itertools.chain.from_iterable(itertools.combinations(range(k), r) for r in range(k + 1)):
        for sig in itertools.product([-1, 1], repeat=len(S)):
            if S:
                As = Ah[:, list(S)]; rhs = np.array(sig) * d[list(S)]
                G = As.T @ As
                if np.linalg.matrix_rank(G) < len(S):
                    continue
                coef = np.linalg.solve(G, rhs); x0 = As @ coef
                Pn = np.eye(len(gh)) - As @ np.linalg.solve(G, As.T)
            else:
                x0 = np.zeros(len(gh)); Pn = np.eye(len(gh))
            rem = R * R - x0 @ x0
            if rem < -1e-14:
                continue
            gn = Pn @ gh; ng = np.linalg.norm(gn)
            x = x0 + (gn / ng * math.sqrt(max(rem, 0)) if ng > 1e-300 else 0)
            if np.all(np.abs(Ah.T @ x) <= d + 1e-10 * R * np.linalg.norm(Ah, axis=0)) and x @ x <= R * R * (1 + 1e-12):
                best = max(best, gh @ x)
    return best


def dual_num(gh, Ah, R, d):
    f = lambda lam: R * np.linalg.norm(gh - Ah @ lam) + np.abs(lam) @ d
    k = Ah.shape[1]
    lam_ls = np.linalg.lstsq(Ah, gh, rcond=None)[0]
    best = None
    for s in [np.zeros(k), lam_ls, 0.5 * lam_ls] + [lam_ls * rng.uniform(0, 1.2, k) for _ in range(6)]:
        r = minimize(f, s, method="Nelder-Mead", options={"xatol": 1e-13, "fatol": 1e-15, "maxiter": 20000, "maxfev": 40000})
        if best is None or r.fun < best.fun:
            best = r
    return best.fun, best.x


# ---------------- C5 ----------------
rows = []
for trial in range(600):
    n = 8
    M = rng.standard_normal((n, n)); H = M @ M.T + 0.1 * np.eye(n)
    L = np.linalg.cholesky(H)  # H = L L^T ; whitening x = L^T b
    g = rng.standard_normal(n); a1 = rng.standard_normal(n)
    if trial % 3 == 0:  # near-collinear rows (H^-1 corr ~ .98)
        a2 = a1 + 0.2 * rng.standard_normal(n)
    else:
        a2 = rng.standard_normal(n)
    A = np.stack([a1, a2], 1)
    Linv = np.linalg.inv(L)
    gh = Linv @ g; Ah = Linv @ A  # ||g||_{H^-1} = ||gh||
    eta = [0.0, 0.001, 0.01, 0.05, 0.1, 0.3, 1.0][trial % 7]
    R = 1.0
    d = eta * R * np.linalg.norm(Ah, axis=0)
    p = primal_exact(gh, Ah, R, d)
    q, lam = dual_num(gh, Ah, R, d)
    rows.append({"eta": eta, "primal": p, "dual": q, "rel": abs(p - q) / max(abs(q), 1e-300)})
rel = [r["rel"] for r in rows]
res["C5_duality"] = {"instances": len(rows), "max_rel_primal_minus_dual": max(rel),
                     "max_rel_eta0": max(r["rel"] for r in rows if r["eta"] == 0),
                     "verdict": bool(max(rel) < 1e-7)}

# ---------------- C7 ----------------
s1 = 0.0505794; r2 = 0.0135013; c12 = 0.9817345571012799
reported_one = {0.0: 5.05794, 0.001: 5.1578, 0.01: 6.05641, 0.02: 7.05437, 0.05: 10.04522, 0.10: 15.01979}
reported_two = {0.0: 1.35013, 0.001: 1.4940, 0.01: 2.83973, 0.02: 4.32413, 0.05: 8.67591, 0.10: 15.01979}
c1 = math.sqrt(1 - s1 * s1)
a1 = np.array([1.0, 0, 0]); a2 = np.array([c12, math.sqrt(1 - c12 * c12), 0])
out = {}
for sgn in (+1, -1):
    y = sgn * math.sqrt(s1 * s1 - r2 * r2)
    g = np.array([c1, y, r2])
    A = np.stack([a1, a2], 1)
    pred = {}
    for eta, rep in reported_two.items():
        d = eta * np.ones(2)
        val = primal_exact(g, A, 1.0, d)
        dv, lam = dual_num(g, A, 1.0, d)
        one = primal_exact(g, A[:, :1], 1.0, d[:1])
        one_formula = eta * c1 + s1 * math.sqrt(1 - eta * eta) if eta < c1 else 1.0
        pred[str(eta)] = {"two_pred_pct": 100 * val, "two_reported_pct": rep,
                          "two_abs_diff_pct": abs(100 * val - rep), "dual_check": 100 * dv,
                          "lambda": lam.tolist(),
                          "one_pred_pct": 100 * one, "one_formula_pct": 100 * one_formula,
                          "one_reported_pct": reported_one[eta],
                          "one_abs_diff_pct": abs(100 * one - reported_one[eta])}
    out["y_sign_" + ("plus" if sgn > 0 else "minus")] = pred
res["C7_table_consistency"] = out
# inputs carry 6 significant digits (rounding <= 5e-6 percentage points); the eta=.001 cells are
# reported with 5 digits (1.4940, 5.1578). Tolerance: 2e-4 pp, and 1e-3 pp for the 5-digit cells.
match = {}
for k, pred in list(out.items()):
    tol = lambda e: 1e-3 if float(e) == 0.001 else 2e-4
    match[k] = bool(all(v["two_abs_diff_pct"] < tol(e) and v["one_abs_diff_pct"] < tol(e) for e, v in pred.items()))
res["C7_match_by_sign"] = match

# ---------------- C7b: two-target reading of the table ----------------
# The table is a max over six targets. T1 = one-statistic worst (s1 = 5.05794%). Its own two-statistic
# residual r2(T1) is unknown (<= 1.35013%). Fit r2(T1) on the eta=.01 cell, then predict the others.
from scipy.optimize import brentq
def two_rad(r2x, eta, sgn=-1):
    y = sgn * math.sqrt(s1 * s1 - r2x * r2x); gg = np.array([c1, y, r2x])
    return primal_exact(gg, np.stack([a1, a2], 1), 1.0, eta * np.ones(2))
c7b = {}
for sgn in (-1, +1):
    try:
        r2fit = brentq(lambda r: 100 * two_rad(r, 0.01, sgn) - 2.83973, 1e-6, 0.0135013, xtol=1e-14)
    except ValueError:
        c7b["sign_" + str(sgn)] = "no root"; continue
    pr = {str(e): {"T1_pred_pct": 100 * two_rad(r2fit, e, sgn), "reported_pct": rep}
          for e, rep in reported_two.items()}
    c7b["sign_" + str(sgn)] = {"r2_T1_fit_pct": 100 * r2fit, "pred": pr}
res["C7b_two_target_fit"] = c7b
fit = c7b.get("sign_-1")
c7b_ok = False
if isinstance(fit, dict):
    pr = fit["pred"]
    c7b_ok = (all(abs(pr[e]["T1_pred_pct"] - pr[e]["reported_pct"]) < 2e-4 for e in ("0.02", "0.05", "0.1"))
              and all(pr[e]["T1_pred_pct"] <= pr[e]["reported_pct"] + 1e-6 for e in ("0.0", "0.001")))
res["verdicts"] = {"C5": res["C5_duality"]["verdict"],
                   "C7_single_target_reading_matches_all_cells": any(match.values()),
                   "C7b_two_target_reading_consistent": bool(c7b_ok)}
json.dump(res, open(args.out, "w"), indent=1, sort_keys=True)
print(json.dumps(res["verdicts"], indent=1))
for k, pred in out.items():
    print(k, [(e, round(v["two_pred_pct"], 5), v["two_reported_pct"]) for e, v in pred.items()])
