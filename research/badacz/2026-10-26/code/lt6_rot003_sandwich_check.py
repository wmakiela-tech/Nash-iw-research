#!/usr/bin/env python3
"""Cross-family numerical falsification attempt for LT6 ROT003 (public note
research/lt6/2026-10-26/IW_LT6_ROT003_VARIABLE_OPERATOR_TARGET_TRANSFER_CERTIFICATE_001_20261026.md).

B(g;A,d) = max_{|c|_inf<=1, |A c|<=d} g.c, computed as an LP (scipy HiGHS) and
cross-checked against the LP dual min_lambda ||g - A^T lambda||_1 + sum_j d_j |lambda_j|.
Claims tested on random instances (seed 20261026):
  U: B(g_t;A_t,d) <= B(g0;A0,d+eta) + rho
  L: B(g_t;A_t,d) >= max(0, B(g0;A0,d-eta) - rho)   (only when d >= eta)
  G: for A_theta = A0 + theta E, g_theta = g0 + theta v on [0,1], grid cover radius h,
     max_i B(g_i;A_i,d) <= sup_theta B <= max_i [B(g_i;A_i,d+h L_A) + h L_g]
     with L_A,j = ||E_j||_1, L_g = ||v||_1; sup_theta estimated on a dense grid.
  N: the rank-loss example A0=[0,eps], A1=[0,0], g=[0,1], d=0 -> 0 and 1.
Run: python3 lt6_rot003_sandwich_check.py --out <dir>   (numpy 2.1.3, scipy 1.14.1)
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def B_primal(g, A, d):
    n = g.size
    A_ub = np.vstack([A, -A])
    b_ub = np.concatenate([d, d])
    r = linprog(-g, A_ub=A_ub, b_ub=b_ub, bounds=[(-1, 1)] * n, method="highs")
    assert r.status == 0
    return -r.fun


def B_dual(g, A, d):
    m, n = A.shape
    # variables: lambda (m, free), s (n, >=|g - A^T lambda|), w (m, >= |lambda|)
    cvec = np.concatenate([np.zeros(m), np.ones(n), d])
    rows, rhs = [], []
    for k in range(n):        #  (g - A^T l)_k <= s_k  and  -(g - A^T l)_k <= s_k
        r1 = np.zeros(m + n + m); r1[:m] = -A[:, k]; r1[m + k] = -1; rows.append(r1); rhs.append(-g[k])
        r2 = np.zeros(m + n + m); r2[:m] = A[:, k]; r2[m + k] = -1; rows.append(r2); rhs.append(g[k])
    for j in range(m):        #  |l_j| <= w_j
        r1 = np.zeros(m + n + m); r1[j] = 1; r1[m + n + j] = -1; rows.append(r1); rhs.append(0)
        r2 = np.zeros(m + n + m); r2[j] = -1; r2[m + n + j] = -1; rows.append(r2); rhs.append(0)
    bounds = [(None, None)] * m + [(0, None)] * n + [(0, None)] * m
    r = linprog(cvec, A_ub=np.array(rows), b_ub=np.array(rhs), bounds=bounds, method="highs")
    assert r.status == 0
    return r.fun


def perturb_rows(rng, A, eta):
    E = rng.normal(size=A.shape)
    E = E / np.abs(E).sum(axis=1, keepdims=True) * eta[:, None] * rng.uniform(0, 1, size=(A.shape[0], 1))
    return A + E


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(20261026)
    tol = 1e-8
    st = {"dual_gap_max": 0.0, "U_viol": 0, "L_viol": 0, "U_min_slack": np.inf, "L_min_slack": np.inf,
          "G_viol": 0, "G_min_slack_low": np.inf, "G_min_slack_up": np.inf, "instances": 0}
    for _ in range(300):
        n, m = int(rng.integers(2, 7)), int(rng.integers(1, 5))
        A0 = rng.normal(size=(m, n)); g0 = rng.normal(size=n)
        d = rng.uniform(0.05, 1.0, size=m)
        eta = rng.uniform(0, 1, size=m) * d * rng.choice([0.5, 1.0, 1.5])
        rho = rng.uniform(0, 0.3)
        At = perturb_rows(rng, A0, eta)
        v = rng.normal(size=n); gt = g0 + v / np.abs(v).sum() * rho * rng.uniform(0, 1)
        Bt = B_primal(gt, At, d)
        st["dual_gap_max"] = max(st["dual_gap_max"], abs(Bt - B_dual(gt, At, d)))
        up = B_primal(g0, A0, d + eta) + rho
        st["U_min_slack"] = min(st["U_min_slack"], up - Bt); st["U_viol"] += int(Bt > up + tol)
        if np.all(d >= eta):
            lo = max(0.0, B_primal(g0, A0, d - eta) - rho)
            st["L_min_slack"] = min(st["L_min_slack"], Bt - lo); st["L_viol"] += int(Bt < lo - tol)
        st["instances"] += 1
    for _ in range(40):  # grid certificate on linear families
        n, m = int(rng.integers(2, 6)), int(rng.integers(1, 4))
        A0 = rng.normal(size=(m, n)); E = rng.normal(size=(m, n)) * 0.2
        g0 = rng.normal(size=n); v = rng.normal(size=n) * 0.3
        d = rng.uniform(0.1, 1.0, size=m)
        LA = np.abs(E).sum(axis=1); Lg = np.abs(v).sum()
        nodes = np.linspace(0, 1, 6); h = 0.1
        Bn = [B_primal(g0 + t * v, A0 + t * E, d) for t in nodes]
        Bu = [B_primal(g0 + t * v, A0 + t * E, d + h * LA) + h * Lg for t in nodes]
        dense = max(B_primal(g0 + t * v, A0 + t * E, d) for t in np.linspace(0, 1, 401))
        lo, up = max(Bn), max(Bu)
        st["G_min_slack_low"] = min(st["G_min_slack_low"], dense - lo)
        st["G_min_slack_up"] = min(st["G_min_slack_up"], up - dense)
        st["G_viol"] += int(dense < lo - tol or dense > up + tol)
    eps = 1e-6
    N0 = B_primal(np.array([0., 1.]), np.array([[0., eps]]), np.array([0.]))
    N1 = B_primal(np.array([0., 1.]), np.array([[0., 0.]]), np.array([0.]))
    N2 = B_primal(np.array([0., 1.]), np.array([[0., eps]]), np.array([eps]))
    st.update({"N_rank_loss": [N0, N1, N2]})
    verdict = {"U_holds": st["U_viol"] == 0, "L_holds": st["L_viol"] == 0, "grid_holds": st["G_viol"] == 0,
               "dual_matches": st["dual_gap_max"] < 1e-7,
               "rank_loss_example": abs(N0) < 1e-9 and abs(N1 - 1) < 1e-9 and abs(N2 - 1) < 1e-9}
    res = {"stats": {k: (float(x) if isinstance(x, (float, np.floating)) else x) for k, x in st.items()},
           "verdict": verdict, "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "lt6_rot003_sandwich_check.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
