#!/usr/bin/env python3
"""Cross-family check of LT5 'correlated preparation and memory' (REV021 Ch1 §5a source).

Source under review: research/lt5/2026-10-23/lt5_correlated_preparation_semigroup_memory_001.md
(Git blob at corpus head d0d3cbf: see report). Linear system
    x' = A x + B y,   y' = C x + D y,   preparation y0 = R x0,
z = y - R x gives x' = E x + B z, z' = G x + H z with
    E = A + B R,  H = D - R B,  G = C + D R - R A - R B R,  K_R(t) = B exp(tH) G.

Part A (exact, SymPy): reproduce every explicit LT5 claim; exact kick responses.
Part B (numerical, seeded): theorem T1 (K_R == 0 iff G(R) maps into N0 = unobs(B, D),
independent of R) and theorem T2 (prepared closure survives an intervention channel
(F, F_y) iff F_y - R F maps into N0) on random families, positive and negative cases.

Run: python3 lt5_ch1_prepared_closure_check.py --out <dir>
Deps: sympy 1.13.3, numpy 2.1.3, scipy 1.14.1 (pinned in the report).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.linalg import expm, null_space

t, tau, d = sp.symbols("t tau delta", real=True)


def blocks(A, B, C, D, R):
    E = A + B * R
    H = D - R * B
    G = C + D * R - R * A - R * B * R
    return E, H, G


def part_a():
    out = {}
    # A1: change of variables, generic symbols n=1, m=2
    a = sp.Symbol("a")
    B = sp.Matrix([[sp.Symbol("b1"), sp.Symbol("b2")]])
    C = sp.Matrix([sp.Symbol("c1"), sp.Symbol("c2")])
    D = sp.Matrix(2, 2, sp.symbols("d11 d12 d21 d22"))
    R = sp.Matrix([sp.Symbol("r1"), sp.Symbol("r2")])
    A = sp.Matrix([[a]])
    L = sp.BlockMatrix([[A, B], [C, D]]).as_explicit()
    T = sp.BlockMatrix([[sp.eye(1), sp.zeros(1, 2)], [R, sp.eye(2)]]).as_explicit()
    E, H, G = blocks(A, B, C, D, R)
    target = sp.BlockMatrix([[E, B], [G, H]]).as_explicit()
    out["A1_shear_identity_residual_zero"] = sp.simplify(T.inv() * L * T - target) == sp.zeros(3, 3)

    # A2: LT5 example: A=0, B=[1,0], C=(-1,1)^T, D=diag(2,-2), R=(1,0)^T
    A = sp.Matrix([[0]]); B = sp.Matrix([[1, 0]]); C = sp.Matrix([-1, 1])
    D = sp.diag(2, -2); R = sp.Matrix([1, 0])
    E, H, G = blocks(A, B, C, D, R)
    K_R = sp.simplify(B * (H * t).exp() * G)
    K_0 = sp.simplify(B * (D * t).exp() * C)
    L = sp.BlockMatrix([[A, B], [C, D]]).as_explicit()
    eL = sp.simplify((L * t).exp())
    prep = sp.simplify(eL * sp.Matrix([1, 1, 0]))        # x0=1, y0=R x0
    kick_x_only = sp.simplify(eL * sp.Matrix([1, 0, 0]))  # kick (delta, 0) from zero state
    kick_graph = sp.simplify(eL * sp.Matrix([1, 1, 0]))   # kick (delta, R delta)
    out["A2"] = {
        "E": str(E), "H": str(H), "G": str(G.T), "G_nonzero": G != sp.zeros(2, 1),
        "K_R": str(K_R), "K_R_identically_zero": K_R == sp.zeros(1, 1),
        "K_0": str(K_0), "K_0_equals_minus_exp_2t": sp.simplify(K_0[0] + sp.exp(2 * t)) == 0,
        "prepared_x": str(prep[0]), "prepared_x_equals_exp_t": sp.simplify(prep[0] - sp.exp(t)) == 0,
        "prepared_y2": str(prep[2]),
        "prepared_y2_equals_LT5": sp.simplify(prep[2] - (sp.exp(t) - sp.exp(-2 * t)) / 3) == 0,
        "kick_x_only_response": str(sp.factor(kick_x_only[0])),
        "kick_x_only_equals_(1-t)exp(t)": sp.simplify(kick_x_only[0] - (1 - t) * sp.exp(t)) == 0,
        "kick_graph_response_equals_exp(t)": sp.simplify(kick_graph[0] - sp.exp(t)) == 0,
        "unobs_N0_of_(B,D)": "span(e2)", "G_mod_N0_first_row": str(G[0]),
        "quotient_riccati_at_Rbar": str(sp.factor(-1 + 2 * sp.Symbol("r") - sp.Symbol("r") ** 2)),
        "B_R": str(B * R),
    }

    # A3: saddle x'=y, y'=x
    A = sp.Matrix([[0]]); B = sp.Matrix([[1]]); C = sp.Matrix([[1]]); D = sp.Matrix([[0]])
    L = sp.Matrix([[0, 1], [1, 0]])
    eL = sp.simplify((L * t).exp())
    res = {}
    for r in (1, -1):
        Rm = sp.Matrix([[r]])
        E, H, G = blocks(A, B, C, D, Rm)
        x = sp.simplify((eL * sp.Matrix([1, r]))[0])
        res[f"R={r}"] = {"E": str(E), "H": str(H), "G": str(G), "prepared_x": str(x),
                         "equals_exp(Et)": sp.simplify(x - sp.exp(E[0] * t)) == 0}
    res["y0=0_x"] = str(sp.simplify((eL * sp.Matrix([1, 0]))[0]))
    # robustness kernel M_R for R=1: int_0^t exp((t-s)E) B exp(sH) ds
    s_ = sp.Symbol("s")
    M = sp.simplify(sp.integrate(sp.exp((t - s_) * 1) * 1 * sp.exp(-s_), (s_, 0, t)))
    res["M_R(R=1)"] = str(M)
    res["M_R_equals_sinh"] = sp.simplify(M - sp.sinh(t)) == 0
    # kick on x only, R=1: true response vs prepared semigroup prediction exp(t)
    kx = sp.simplify((eL * sp.Matrix([1, 0]))[0])
    res["kick_x_only_response"] = str(kx)
    res["kick_x_only_equals_cosh"] = sp.simplify(kx - sp.cosh(t)) == 0
    res["kick_graph_response_equals_exp"] = sp.simplify((eL * sp.Matrix([1, 1]))[0] - sp.exp(t)) == 0
    out["A3_saddle"] = res
    return out


def unobs(Bm, Hm):
    m = Hm.shape[0]
    O = np.vstack([Bm @ np.linalg.matrix_power(Hm, k) for k in range(m)])
    return null_space(O)


def krylov_max(Bm, Hm, Gm):
    m = Hm.shape[0]
    return max(np.abs(Bm @ np.linalg.matrix_power(Hm, k) @ Gm).max() for k in range(m))


def random_case(rng, n, m1, p):
    """Hidden w=(w1 in R^m1, w0 in R^p). Quotient block L_bar real-diagonalizable."""
    N = n + m1
    S = rng.normal(size=(N, N))
    lam = np.sort(rng.uniform(-2.0, 1.0, size=N))
    Lbar = S @ np.diag(lam) @ np.linalg.inv(S)
    A = Lbar[:n, :n]; B1 = Lbar[:n, n:]; C1 = Lbar[n:, :n]; D11 = Lbar[n:, n:]
    Rbar = S[n:, :n] @ np.linalg.inv(S[:n, :n])          # invariant graph of L_bar
    D01 = rng.normal(size=(p, m1)); D00 = rng.normal(size=(p, p)); C0 = rng.normal(size=(p, n))
    B = np.hstack([B1, np.zeros((n, p))])
    C = np.vstack([C1, C0])
    D = np.block([[D11, np.zeros((m1, p))], [D01, D00]])
    return A, B, C, D, Rbar


def part_b(seed=20261026, trials=200):
    rng = np.random.default_rng(seed)
    stats = {"T1_pos_max_Krylov": 0.0, "T1_pos_min_G_norm": np.inf, "T1_neg_min_Krylov": np.inf,
             "T1_N0_R_independent_fail": 0, "prepared_traj_max_err": 0.0,
             "T2_graph_kick_max_dev": 0.0, "T2_xonly_kick_min_dev": np.inf,
             "T2_w1_perturbed_kick_min_dev": np.inf, "T2_multikick_graph_max_dev": 0.0,
             "trials": trials}
    taus = np.linspace(0.05, 1.5, 12)
    for _ in range(trials):
        n, m1, p = int(rng.integers(1, 3)), int(rng.integers(1, 3)), int(rng.integers(1, 3))
        A, B, C, D, Rbar = random_case(rng, n, m1, p)
        m = m1 + p
        R0 = rng.normal(size=(p, n))
        R = np.vstack([Rbar, R0])
        E, H, G = A + B @ R, D - R @ B, C + D @ R - R @ A - R @ B @ R
        scale = 1.0 + max(np.abs(M).max() for M in (A, B, C, D, R))
        # T1 positive
        stats["T1_pos_max_Krylov"] = max(stats["T1_pos_max_Krylov"], krylov_max(B, H, G) / scale ** 3)
        stats["T1_pos_min_G_norm"] = min(stats["T1_pos_min_G_norm"], np.linalg.norm(G))
        N0_D = unobs(B, D); N0_H = unobs(B, H)
        if N0_D.shape[1] != p or N0_H.shape[1] != p or np.linalg.matrix_rank(np.hstack([N0_D, N0_H]), tol=1e-8) != p:
            stats["T1_N0_R_independent_fail"] += 1
        # T1 positive, typed: quotient residual G_bar = G mod N0 (N0 = last p coords by construction)
        stats["T1_pos_max_Gbar_rel"] = max(stats.get("T1_pos_max_Gbar_rel", 0.0),
                                           np.linalg.norm(G[:m1]) / scale ** 3)
        # T1 negative: perturb the observable quotient part of R.
        # Typed falsifier (replaces an earlier scale**3 yardstick that misfired on
        # ill-conditioned draws): theorem predicts O_H G = O_bar G_bar, hence
        # ||O_H G||_F >= sigma_min(O_bar) ||G_bar||_F with G_bar != 0.
        Rn = R.copy(); Rn[:m1] += rng.normal(size=(m1, n)) * 0.3
        Hn, Gn = D - Rn @ B, C + D @ Rn - Rn @ A - Rn @ B @ Rn
        OH = np.vstack([B @ np.linalg.matrix_power(Hn, k) for k in range(m)])
        Hbar = Hn[:m1, :m1]; B1 = B[:, :m1]
        Obar = np.vstack([B1 @ np.linalg.matrix_power(Hbar, k) for k in range(m)])
        smin = np.linalg.svd(Obar, compute_uv=False)[-1]
        Gbar = Gn[:m1]
        lhs, rhs = np.linalg.norm(OH @ Gn), smin * np.linalg.norm(Gbar)
        stats["T1_neg_inequality_violations"] = stats.get("T1_neg_inequality_violations", 0) + int(lhs < rhs * (1 - 1e-9))
        stats["T1_neg_identity_max_err"] = max(stats.get("T1_neg_identity_max_err", 0.0),
                                               np.abs(OH @ Gn - Obar @ Gbar).max() / (1 + np.abs(OH @ Gn).max()))
        stats["T1_neg_min_Gbar"] = min(stats.get("T1_neg_min_Gbar", np.inf), np.linalg.norm(Gbar))
        stats["T1_neg_min_raw_Krylov"] = min(stats["T1_neg_min_Krylov"], krylov_max(B, Hn, Gn))
        stats["T1_neg_min_Krylov"] = stats["T1_neg_min_raw_Krylov"]
        # prepared trajectory equals exp(tE) x0
        L = np.block([[A, B], [C, D]])
        x0 = rng.normal(size=n)
        for tt in taus:
            full = expm(tt * L) @ np.concatenate([x0, R @ x0])
            stats["prepared_traj_max_err"] = max(stats["prepared_traj_max_err"],
                                                 np.abs(full[:n] - expm(tt * E) @ x0).max())
        # T2: kicks from zero state (linearity); visible response vs exp(tau E) F u
        u = rng.normal(size=n)
        F = np.eye(n)
        def dev(Fy):
            return max(np.abs((expm(tt * L) @ np.concatenate([F @ u, Fy @ u]))[:n]
                              - expm(tt * E) @ F @ u).max() for tt in taus)
        Fy_graph = R @ F + np.vstack([np.zeros((m1, n)), rng.normal(size=(p, n))])
        stats["T2_graph_kick_max_dev"] = max(stats["T2_graph_kick_max_dev"], dev(Fy_graph))
        stats["T2_xonly_kick_min_dev"] = min(stats["T2_xonly_kick_min_dev"],
                                             dev(np.zeros((m, n))) / (1 + np.abs(Rbar).max()))
        Fy_bad = R @ F + np.vstack([rng.normal(size=(m1, n)) * 0.3, np.zeros((p, n))])
        stats["T2_w1_perturbed_kick_min_dev"] = min(stats["T2_w1_perturbed_kick_min_dev"], dev(Fy_bad))
        # multi-kick history with graph-respecting kicks: full vs reduced
        state = np.concatenate([x0, R @ x0]); xr = x0.copy()
        for _k in range(3):
            dt = rng.uniform(0.1, 0.5)
            state = expm(dt * L) @ state; xr = expm(dt * E) @ xr
            kick = rng.normal(size=n)
            state = state + np.concatenate([kick, R @ kick + np.vstack([np.zeros((m1, n)), rng.normal(size=(p, n))]) @ rng.normal(size=n)])
            xr = xr + kick
        state = expm(0.7 * L) @ state; xr = expm(0.7 * E) @ xr
        stats["T2_multikick_graph_max_dev"] = max(stats["T2_multikick_graph_max_dev"],
                                                  np.abs(state[:n] - xr).max())
    return {k: (float(v) if isinstance(v, (float, np.floating)) else v) for k, v in stats.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    a = part_a()
    b = part_b()
    verdict = {
        "LT5_explicit_claims_reproduced": all([
            a["A1_shear_identity_residual_zero"], a["A2"]["G_nonzero"], a["A2"]["K_R_identically_zero"],
            a["A2"]["K_0_equals_minus_exp_2t"], a["A2"]["prepared_x_equals_exp_t"],
            a["A2"]["prepared_y2_equals_LT5"], a["A3_saddle"]["R=1"]["equals_exp(Et)"],
            a["A3_saddle"]["R=-1"]["equals_exp(Et)"], a["A3_saddle"]["M_R_equals_sinh"]]),
        "x_only_kick_breaks_prepared_closure_in_both_LT5_examples":
            a["A2"]["kick_x_only_equals_(1-t)exp(t)"] and a["A3_saddle"]["kick_x_only_equals_cosh"],
        "graph_respecting_kick_preserves_closure_in_both_LT5_examples":
            a["A2"]["kick_graph_response_equals_exp(t)"] and a["A3_saddle"]["kick_graph_response_equals_exp"],
        "T1_random_numerics_consistent": b["T1_pos_max_Krylov"] < 1e-8 and b["T1_pos_max_Gbar_rel"] < 1e-8
            and b["T1_neg_inequality_violations"] == 0 and b["T1_neg_identity_max_err"] < 1e-8
            and b["T1_neg_min_Gbar"] > 1e-3 and b["T1_neg_min_raw_Krylov"] > 0.0
            and b["T1_N0_R_independent_fail"] == 0 and b["prepared_traj_max_err"] < 1e-7,
        "T2_random_numerics_consistent": b["T2_graph_kick_max_dev"] < 1e-7 and b["T2_xonly_kick_min_dev"] > 1e-6
            and b["T2_w1_perturbed_kick_min_dev"] > 1e-6 and b["T2_multikick_graph_max_dev"] < 1e-7,
    }
    result = {"part_a_exact": a, "part_b_numeric": b, "verdict": verdict,
              "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "versions": {"sympy": sp.__version__, "numpy": np.__version__}}
    (out / "lt5_ch1_prepared_closure_check.json").write_text(json.dumps(result, indent=1, default=str))
    print(json.dumps(verdict, indent=1))
    print(json.dumps(b, indent=1))


if __name__ == "__main__":
    main()
