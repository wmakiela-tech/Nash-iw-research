#!/usr/bin/env python3
"""BADACZ (Claude) owner follow-up to AUD1-GROK-BADACZ002-REVIEW-001 (2026-10-28): TT projector bridge, non-normal branch.
  R  rank<=2 lemma: for ANY real linear E on Sym^2(R^3) with rank<=2 there is a unit n with
     ||E - P(n)|| >= 1 (no idempotence or symmetry); random rank-1/rank-2 E, idempotent or not.
  S  corollary: for ANY real 6x6 B, sup_n ||B - P(n)|| >= 1 - sigma_3(B) (dense directions).
  F  non-normal quantitative step: E = (I + sign(2B-I))/2 is a real idempotent with
     ||B - E|| <= psi = (||2B-I||/2) * ((1-4 delta)^(-1/2) - 1), delta = ||B^2-B|| < 1/4;
     any real idempotent E has sup_n ||E-P(n)|| >= 1 (rank<=2 lemma or rank>=3 kernel count), trivial floor 1/2;
     self-consistent frontier e >= max(1/2, (1-g/2)/(1+g)), g = (1-4 delta)^(-1/2) - 1, checked end to end;
     informative distance to the self-adjoint frontier 1 - tau(delta); rank-3/4 idempotents at every n.
numpy 2.1.3, scipy 1.14.1; seed 20261028.
Run: python3 badacz_aud1_followups_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.linalg import sqrtm
from scipy.optimize import brentq

SEED = 20261028
S2 = np.sqrt(2.0)
_B = []
for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
    M = np.zeros((3, 3))
    if i == j: M[i, i] = 1
    else: M[i, j] = M[j, i] = 1 / S2
    _B.append(M)


def vec(h):
    return np.array([h[0, 0], h[1, 1], h[2, 2], S2 * h[0, 1], S2 * h[0, 2], S2 * h[1, 2]])


def mat(v):
    return np.array([[v[0], v[3] / S2, v[4] / S2], [v[3] / S2, v[1], v[5] / S2], [v[4] / S2, v[5] / S2, v[2]]])


def tt(n):
    n = np.asarray(n, float) / np.linalg.norm(n); L = np.eye(3) - np.outer(n, n)
    return np.column_stack([vec(L @ B @ L - 0.5 * L * np.trace(L @ B)) for B in _B])


def fib(nd):
    i = np.arange(nd) + 0.5; z = i / nd; ph = np.pi * (1 + 5 ** 0.5) * i; r = np.sqrt(1 - z * z)
    return np.stack([r * np.cos(ph), r * np.sin(ph), z], 1)


def witness_direction(E, rng):
    """ker E ∩ traceless has dim >= 3; det is odd on a great circle -> singular traceless T, n in ker T."""
    U, s, Vt = np.linalg.svd(E)
    ker = Vt[int((s > 1e-12 * max(1, s[0])).sum()):].T
    tr = vec(np.eye(3)) / np.sqrt(3)
    c = ker.T @ tr
    Wc = np.linalg.svd(c[None, :])[2][1:].T
    W = ker @ Wc
    w0 = rng.normal(size=W.shape[1]); w0 /= np.linalg.norm(w0)
    w1 = rng.normal(size=W.shape[1]); w1 -= w1 @ w0 * w0; w1 /= np.linalg.norm(w1)
    f = lambda s_: np.linalg.det(mat(W @ (np.cos(np.pi * s_) * w0 + np.sin(np.pi * s_) * w1)))
    s0 = brentq(f, 0, 1, xtol=1e-15)
    T = mat(W @ (np.cos(np.pi * s0) * w0 + np.sin(np.pi * s0) * w1))
    lam, V = np.linalg.eigh(T)
    return V[:, int(np.argmin(np.abs(lam)))], vec(T), W.shape[1]


def part_R(rng):
    out = {"cases": 0, "min_ratio": np.inf, "min_dim_ker_cap_traceless": 99}
    for i in range(300):
        r = 1 + i % 2
        X = rng.normal(size=(6, r)); Y = rng.normal(size=(6, r))
        E = X @ Y.T * rng.uniform(0.1, 5)                 # generic rank-r, neither idempotent nor symmetric
        if i % 3 == 0:
            E = X @ np.linalg.solve(Y.T @ X, Y.T)          # oblique idempotent
        n, tv, dk = witness_direction(E, rng)
        P = tt(n)
        ratio = np.linalg.norm((E - P) @ tv) / np.linalg.norm(tv)
        out["min_ratio"] = min(out["min_ratio"], ratio); out["min_dim_ker_cap_traceless"] = min(out["min_dim_ker_cap_traceless"], dk)
        out["cases"] += 1
    return out


def part_S(rng):
    dirs = np.stack([tt(n) for n in fib(20000)])
    out = {"cases": 0, "violations": 0, "min_slack": np.inf}
    for i in range(200):
        B = rng.normal(size=(6, 6)) * rng.uniform(0.05, 1.0)
        if i % 4 == 0: B = 0.3 * np.eye(6) + 0.05 * rng.normal(size=(6, 6))
        if i % 4 == 1: B = tt(rng.normal(size=3)) + 0.1 * rng.normal(size=(6, 6))
        sup = np.max(np.linalg.norm(B[None] - dirs, 2, axis=(1, 2)))
        s3 = np.linalg.svd(B, compute_uv=False)[2]
        out["violations"] += int(sup < 1 - s3 - 1e-9)
        out["min_slack"] = min(out["min_slack"], sup - (1 - s3)); out["cases"] += 1
    # equality witnesses
    tau = 0.1
    out["tauI_sup"] = float(np.max(np.linalg.norm(tau * np.eye(6)[None] - dirs, 2, axis=(1, 2))))
    out["tauI_1-sigma3"] = 1 - tau
    return out


def sign_idempotent(B):
    X = 2 * B - np.eye(6)
    R = sqrtm(X @ X)
    imag = float(np.max(np.abs(np.imag(R))))
    S = X @ np.linalg.inv(np.real(R))
    return 0.5 * (np.eye(6) + S), imag


def part_F(rng):
    out = {"cases": 0, "viol_bound": 0, "max_idempotence_err": 0.0, "max_imag": 0.0, "max_ratio": 0.0,
           "rank_E_counts": {}, "min_sup_E_minus_P_over_dirs": np.inf}
    # trivial floor e >= 1/2: ||P(e_z) - P(e_x)|| = 1 (h_xy is TT for e_z and killed by P(e_x))
    out["norm_P(ez)-P(ex)"] = float(np.linalg.norm(tt([0, 0, 1]) - tt([1, 0, 0]), 2))
    dirs = np.stack([tt(n) for n in fib(4000)])
    for _ in range(400):
        P = tt(rng.normal(size=3))
        U = np.eye(6) + rng.normal(size=(6, 6)) * rng.uniform(0, 0.6)       # oblique conjugation
        E0 = U @ P @ np.linalg.inv(U)
        B = E0 + rng.normal(size=(6, 6)) * rng.uniform(0.001, 0.08)
        delta = np.linalg.norm(B @ B - B, 2)
        if delta >= 0.24: continue
        E, im = sign_idempotent(B)
        psi = np.linalg.norm(2 * B - np.eye(6), 2) / 2 * ((1 - 4 * delta) ** -0.5 - 1)
        err = np.linalg.norm(B - E, 2)
        out["viol_bound"] += int(err > psi * (1 + 1e-9) + 1e-12)
        out["max_ratio"] = max(out["max_ratio"], err / psi)
        out["max_idempotence_err"] = max(out["max_idempotence_err"], np.linalg.norm(E @ E - E, 2))
        out["max_imag"] = max(out["max_imag"], im)
        rk = str(int(round(np.trace(E))))
        out["rank_E_counts"][rk] = out["rank_E_counts"].get(rk, 0) + 1
        # any real idempotent E: sup_n ||E - P(n)|| >= 1 (rank<=2 lemma, or im E ∩ ker P(n) != 0 if rank>=3)
        out["min_sup_E_minus_P_over_dirs"] = min(out["min_sup_E_minus_P_over_dirs"],
                                                 float(np.max(np.linalg.norm(E[None] - dirs, 2, axis=(1, 2)))))
        # end-to-end pointwise statement: sup_n ||B - P(n)|| >= max(1/2, (1 - g/2)/(1 + g));
        # the grid underestimates the sup, so a zero violation count is conservative
        g = (1 - 4 * delta) ** -0.5 - 1
        supB = float(np.max(np.linalg.norm(B[None] - dirs, 2, axis=(1, 2))))
        lb = max(0.5, (1 - g / 2) / (1 + g))
        out["viol_final"] = out.get("viol_final", 0) + int(supB < lb - 1e-9)
        out["min_slack_final"] = min(out.get("min_slack_final", np.inf), supB - lb)
        # informative only (open question): distance to the self-adjoint frontier 1 - tau(delta)
        tau = (1 - np.sqrt(1 - 4 * delta)) / 2
        out["min_supB_minus_(1-tau)"] = min(out.get("min_supB_minus_(1-tau)", np.inf), supB - (1 - tau))
        out["cases"] += 1
    # idempotents of rank 3 and 4: ||E - P(n)|| >= 1 for EVERY n (im E ∩ ker P(n) != 0)
    m = np.inf
    for i in range(100):
        r = 3 + i % 2
        X_ = rng.normal(size=(6, r)); Y_ = rng.normal(size=(6, r))
        E = X_ @ np.linalg.solve(Y_.T @ X_, Y_.T)
        m = min(m, float(np.min(np.linalg.norm(E[None] - dirs, 2, axis=(1, 2)))))
    out["rank34_min_over_all_dirs"] = m
    rows = []
    for d in (0.01, 0.05, 0.09, 0.16, 0.21):
        g = (1 - 4 * d) ** -0.5 - 1
        e_star = (1 - g / 2) / (1 + g)                 # solves e = 1 - (1+2e)/2 * g
        tau = (1 - np.sqrt(1 - 4 * d)) / 2
        rows.append({"delta": d, "nonnormal_lower_bound_e": max(0.5, e_star), "selfadjoint_frontier_1-tau": 1 - tau})
    out["frontier_table"] = rows
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    R = part_R(rng); S = part_S(rng); F = part_F(rng)
    verdict = {"R_rank2_lemma": R["min_ratio"] > 1 - 1e-9 and R["min_dim_ker_cap_traceless"] >= 3,
               "S_sigma3_corollary": S["violations"] == 0 and abs(S["tauI_sup"] - S["tauI_1-sigma3"]) < 1e-9,
               "F_sign_bound": F["viol_bound"] == 0 and F["max_idempotence_err"] < 1e-9 and F["cases"] > 100
                               and F["max_imag"] < 1e-9 and F["min_sup_E_minus_P_over_dirs"] > 1 - 1e-3
                               and abs(F["norm_P(ez)-P(ex)"] - 1) < 1e-12,
               "F_end_to_end": F["viol_final"] == 0 and F["rank34_min_over_all_dirs"] > 1 - 1e-9}
    def clean(o):
        if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
        if isinstance(o, list): return [clean(v) for v in o]
        if isinstance(o, (np.floating,)): return float(o)
        if isinstance(o, (np.integer,)): return int(o)
        return o
    res = clean({"R": R, "S": S, "F": F, "verdict": verdict, "seed": SEED,
                 "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    (out / "badacz_aud1_followups_check.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
