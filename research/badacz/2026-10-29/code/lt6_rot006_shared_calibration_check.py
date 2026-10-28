#!/usr/bin/env python3
"""BADACZ (Claude): cross-family check of LT6 ROT006 (one shared calibration error across k preparations)
and one development (uncertain preparation matrix C, Oettli-Prager).
  P1  exact rational certificates for W1-W3: a primal point and a dual point with equal value give r* exactly.
  P2  200 random problems: primal min_{||e||_1<=eta} ||C^T e - b||_inf and dual max_{||lam||_1<=1}
      (lam^T b - eta ||C lam||_inf) as two separate LPs (different HiGHS methods); duality gap.
      Heterogeneous delta: LP feasibility vs the support-function criterion (sign of the normalised dual LP).
  P3  separate (per-preparation) acceptance versus joint acceptance on random problems.
  P4  development: C = C0 + D with |D_ij| <= Delta_ij (entrywise box). For fixed e the set of C^T e is a box,
      so consistency <=> exists e, ||e||_1 <= eta: |b_j - c0_j.e| <= delta_j + sum_i Delta_ij |e_i|
      (Oettli-Prager form). Exact test = 2^d LPs over sign orthants. Validated against a dense grid in e
      (d <= 2) and by an explicit constructed (C, n) for every feasible case; exact falsifier of the convex
      outer relaxation sum_i Delta_ij|e_i| <= eta max_i Delta_ij.
Synthetic mathematics only. numpy 2.1.3, scipy 1.14.1; seed 20261029.
Run: python3 -I lt6_rot006_shared_calibration_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

SEED = 20261029


# ---------------------------------------------------------------- P1 exact certificates
def exact_cert(C, b, eta, e, lam):
    """value of primal at e (must satisfy ||e||_1 <= eta) and dual at lam (||lam||_1 <= 1), in Fractions."""
    d, k = len(C), len(C[0])
    assert sum(abs(x) for x in e) <= eta and sum(abs(x) for x in lam) <= 1
    res = [sum(C[i][j] * e[i] for i in range(d)) - b[j] for j in range(k)]
    primal = max(abs(r) for r in res)
    Clam = [sum(C[i][j] * lam[j] for j in range(k)) for i in range(d)]
    dual = sum(lam[j] * b[j] for j in range(k)) - eta * max(abs(x) for x in Clam)
    return primal, dual


def part_P1():
    W = {
        "W1": ([[Fr(1), Fr(-1)]], [Fr(1), Fr(1)], Fr(1), [Fr(0)], [Fr(1, 2), Fr(1, 2)]),
        "W2": ([[Fr(1), Fr(0)], [Fr(0), Fr(1)]], [Fr(3, 4), Fr(3, 4)], Fr(1), [Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]),
        "W3": ([[Fr(1), Fr(-1)], [Fr(0), Fr(1)]], [Fr(1, 4), Fr(-13, 20)], Fr(1), [Fr(1, 4), Fr(-2, 5)], [Fr(0), Fr(0)]),
    }
    out = {}
    for name, (C, b, eta, e, lam) in W.items():
        p, dval = exact_cert(C, b, eta, e, lam)
        sep = all(abs(b[j]) <= eta * max(abs(C[i][j]) for i in range(len(C))) for j in range(len(b)))
        out[name] = {"primal_at_e": str(p), "dual_at_lam": str(dval), "r_star_exact": str(p) if p == dval else None,
                     "each_preparation_separately_consistent": sep}
    return out


# ---------------------------------------------------------------- P2 LP primal / dual
def primal_lp(C, b, eta, method="highs-ds"):
    d, k = C.shape
    # x = (e+, e-, t)
    c = np.r_[np.zeros(2 * d), 1.0]
    A, ub = [], []
    for j in range(k):
        row = np.r_[C[:, j], -C[:, j], -1.0]; A.append(row); ub.append(b[j])       #  C^T e - b <= t
        A.append(np.r_[-C[:, j], C[:, j], -1.0]); ub.append(-b[j])                   # -(C^T e - b) <= t
    A.append(np.r_[np.ones(2 * d), 0.0]); ub.append(eta)
    r = linprog(c, A_ub=np.array(A), b_ub=ub, bounds=[(0, None)] * (2 * d) + [(None, None)], method=method)
    return r.fun, r.x[:d] - r.x[d:2 * d]


def dual_lp(C, b, eta, delta=None, method="highs-ipm"):
    """max lam^T b - eta ||C lam||_inf - sum_j delta_j |lam_j| over ||lam||_1 <= 1."""
    d, k = C.shape
    delta = np.zeros(k) if delta is None else delta
    # x = (lam+, lam-, s);  minimise -(lam^T b) + eta s + delta.(lam+ + lam-)
    c = np.r_[-b + delta, b + delta, eta]
    A, ub = [], []
    for i in range(d):
        A.append(np.r_[C[i], -C[i], -1.0]); ub.append(0.0)
        A.append(np.r_[-C[i], C[i], -1.0]); ub.append(0.0)
    A.append(np.r_[np.ones(2 * k), 0.0]); ub.append(1.0)
    r = linprog(c, A_ub=np.array(A), b_ub=ub, bounds=[(0, None)] * (2 * k + 1), method=method)
    return -r.fun


def feasible_lp(C, b, eta, delta):
    d, k = C.shape
    A, ub = [], []
    for j in range(k):
        A.append(np.r_[C[:, j], -C[:, j]]); ub.append(b[j] + delta[j])
        A.append(np.r_[-C[:, j], C[:, j]]); ub.append(-b[j] + delta[j])
    A.append(np.ones(2 * d)); ub.append(eta)
    r = linprog(np.zeros(2 * d), A_ub=np.array(A), b_ub=ub, bounds=[(0, None)] * (2 * d), method="highs")
    return r.status == 0


def part_P2_P3(rng):
    gaps, agree, n_iff, sep_acc_joint_rej, joint_acc, n_sep = [], 0, 0, 0, 0, 0
    for it in range(200):
        d = int(rng.integers(1, 5)); k = int(rng.integers(2, 6))
        C = rng.normal(size=(d, k)); eta = float(rng.uniform(0.2, 2.0))
        e0 = rng.normal(size=d); e0 *= eta * rng.uniform(0.2, 1.6) / np.abs(e0).sum()
        b = C.T @ e0 + rng.normal(size=k) * rng.uniform(0, 0.4)
        p, _ = primal_lp(C, b, eta); dv = dual_lp(C, b, eta)
        gaps.append(abs(p - dv))
        delta = rng.uniform(0, 0.5, size=k)
        feas = feasible_lp(C, b, eta, delta)
        crit_violated = dual_lp(C, b, eta, delta) > 1e-9
        agree += int(feas == (not crit_violated)); n_iff += 1
        sep = all(abs(b[j]) <= eta * np.abs(C[:, j]).max() + delta[j] for j in range(k))
        n_sep += int(sep); joint_acc += int(feas)
        sep_acc_joint_rej += int(sep and not feas)
    return {"P2_cases": 200, "P2_max_primal_dual_gap": float(max(gaps)),
            "P2_iff_agreement": f"{agree}/{n_iff}",
            "P3_separately_accepted": n_sep, "P3_jointly_accepted": joint_acc,
            "P3_separate_accepts_but_joint_rejects": sep_acc_joint_rej}


# ---------------------------------------------------------------- P4 uncertain C (Oettli-Prager)
def op_orthant_min(C0, Dl, b, eta):
    """r_OP = min_{||e||_1<=eta} max_j (|b_j - c0_j.e| - sum_i Dl_ij |e_i|), exact via 2^d LPs; returns (r, e, sigma)."""
    d, k = C0.shape
    best = (np.inf, None, None)
    for sig in itertools.product((1.0, -1.0), repeat=d):
        s = np.array(sig)
        # x = (e, t); constraints: s_i e_i >= 0, sum s_i e_i <= eta,
        #  (b_j - c0_j e) - sum_i Dl_ij s_i e_i <= t ;  -(b_j - c0_j e) - sum_i Dl_ij s_i e_i <= t
        A, ub = [], []
        for j in range(k):
            A.append(np.r_[-C0[:, j] - Dl[:, j] * s, -1.0]); ub.append(-b[j])
            A.append(np.r_[C0[:, j] - Dl[:, j] * s, -1.0]); ub.append(b[j])
        A.append(np.r_[s, 0.0]); ub.append(eta)
        for i in range(d):
            row = np.zeros(d + 1); row[i] = -s[i]; A.append(row); ub.append(0.0)
        r = linprog(np.r_[np.zeros(d), 1.0], A_ub=np.array(A), b_ub=ub, bounds=[(None, None)] * (d + 1), method="highs")
        if r.status == 0 and r.fun < best[0]:
            best = (r.fun, r.x[:d], s)
    return best


def g_val(C0, Dl, b, E):
    """g(e) = max_j (|b_j - c0_j.e| - sum_i Dl_ij |e_i|) for rows of E."""
    R = np.abs(b[None, :] - E @ C0) - np.abs(E) @ Dl
    return R.max(axis=1)


def construct_witness(C0, Dl, b, e, delta):
    """explicit C = C0 + D (|D| <= Dl) and n (|n| <= delta) with C^T e + n = b, if g(e) <= max... (uses clipping)."""
    r = b - C0.T @ e
    m = Dl.T @ np.abs(e)
    take = np.clip(r, -m, m)
    D = np.zeros_like(C0)
    for j in range(C0.shape[1]):
        if m[j] > 0:
            D[:, j] = Dl[:, j] * np.sign(e) * (take[j] / m[j])
    n = r - take
    return D, n


def part_P4(rng):
    out = {}
    # exact falsifier of the convex outer relaxation (d=1, k=2)
    C0 = np.array([[1.0, -1.0]]); Dl = np.array([[0.5, 0.5]]); b = np.array([0.4, 0.4]); eta = 1.0
    r_op, e_op, _ = op_orthant_min(C0, Dl, b, eta)
    relax = primal_lp(C0, b, eta)[0] - eta * Dl.max()
    out["falsifier"] = {"r_OP_exact": float(r_op), "r_OP_closed_form": 0.4, "argmin_e": e_op.tolist(),
                        "outer_relaxation_value": float(relax),
                        "exact_rejects_with_delta_0": bool(r_op > 1e-12), "relaxation_accepts_with_delta_0": bool(relax <= 0)}
    # inner error: ignoring Delta rejects a consistent model (d=1, k=2)
    b2 = np.array([1.2, -1.2])
    r_ign = primal_lp(C0, b2, eta)[0]; r_op2, e2, _ = op_orthant_min(C0, Dl, b2, eta)
    D2, n2 = construct_witness(C0, Dl, b2, e2, np.zeros(2))
    out["inner_error"] = {"r_ignoring_Delta": float(r_ign), "r_OP": float(r_op2), "e": e2.tolist(),
                          "constructed_C": (C0 + D2).tolist(), "constructed_n": n2.tolist(),
                          "construct_residual": float(np.abs((C0 + D2).T @ e2 + n2 - b2).max())}
    # random validation against a dense grid (d = 1, 2) and constructive certificates
    grid_gap_max, lp_above_grid, n_feas, cert_ok, n_cases = 0.0, 0, 0, 0, 0
    h_rec = []
    for it in range(120):
        d = 1 + it % 2; k = int(rng.integers(2, 5)); eta = float(rng.uniform(0.3, 1.5))
        C0 = rng.normal(size=(d, k)); Dl = rng.uniform(0, 0.8, size=(d, k))
        e0 = rng.normal(size=d); e0 *= eta * rng.uniform(0.2, 1.3) / np.abs(e0).sum()
        b = (C0 + Dl * rng.uniform(-1.3, 1.3, size=(d, k))).T @ e0 + rng.normal(size=k) * 0.1
        r, e_star, _ = op_orthant_min(C0, Dl, b, eta)
        if d == 1:
            h = eta / 4000; E = np.linspace(-eta, eta, 8001)[:, None]
        else:
            h = eta / 400; g1 = np.linspace(-eta, eta, 801); E = np.array([(x, y) for x in g1 for y in g1 if abs(x) + abs(y) <= eta + 1e-12])
        gmin = float(g_val(C0, Dl, b, E).min())
        L = float((np.abs(C0) + Dl).max()) * d       # Lipschitz bound of g in the inf-norm on e
        lp_above_grid += int(r > gmin + 1e-9)
        grid_gap_max = max(grid_gap_max, (gmin - r) / (L * h))
        if r <= 1e-12:
            n_feas += 1
            D, n = construct_witness(C0, Dl, b, e_star, np.zeros(k))
            ok = (np.all(np.abs(D) <= Dl + 1e-12) and np.abs((C0 + D).T @ e_star + n - b).max() < 1e-12
                  and np.abs(n).max() <= max(r, 0) + 1e-9 and np.abs(e_star).sum() <= eta + 1e-9)
            cert_ok += int(ok)
        n_cases += 1
    out["random"] = {"cases": n_cases, "LP_value_above_grid_min": lp_above_grid,
                     "max_(grid_min - LP)/(L h)": grid_gap_max, "feasible_cases": n_feas, "constructive_certificates_ok": cert_ok}
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    P1 = part_P1(); P23 = part_P2_P3(rng); P4 = part_P4(rng)
    verdict = {
        "P1_exact_r_star": [P1["W1"]["r_star_exact"], P1["W2"]["r_star_exact"], P1["W3"]["r_star_exact"]] == ["1", "1/4", "0"]
                           and P1["W1"]["each_preparation_separately_consistent"] and P1["W2"]["each_preparation_separately_consistent"],
        "P2_duality": P23["P2_max_primal_dual_gap"] < 1e-8 and P23["P2_iff_agreement"] == "200/200",
        "P4_falsifier": P4["falsifier"]["exact_rejects_with_delta_0"] and P4["falsifier"]["relaxation_accepts_with_delta_0"]
                        and abs(P4["falsifier"]["r_OP_exact"] - 0.4) < 1e-9,
        "P4_inner_error": P4["inner_error"]["r_ignoring_Delta"] > 1e-3 and P4["inner_error"]["r_OP"] <= 1e-9
                          and P4["inner_error"]["construct_residual"] < 1e-12,
        "P4_exact_vs_grid": P4["random"]["LP_value_above_grid_min"] == 0 and P4["random"]["max_(grid_min - LP)/(L h)"] <= 1.0
                            and P4["random"]["constructive_certificates_ok"] == P4["random"]["feasible_cases"] > 0,
    }
    res = {"P1": P1, "P2_P3": P23, "P4": P4, "verdict": verdict, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "lt6_rot006_shared_calibration_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
