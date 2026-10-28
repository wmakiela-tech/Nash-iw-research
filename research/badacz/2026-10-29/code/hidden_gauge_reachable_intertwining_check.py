#!/usr/bin/env python3
"""BADACZ (Claude): public developments of SCOPE9 top-down proposals (published with Moderator consent, 2026-10-29).
  DA  hidden-coordinate gauge: the SCOPE9 TOPDOWN 007 family (A_K, B_K) is one similarity orbit of a hidden
      coordinate; invariant quantities; gauge dependence of a norm-split convolution bound and of a
      Gronwall-type constant ||L|| exp(T||L||); invariant L1 small-gain bound for the memoryless reduction,
      sharp on the SCOPE9 family.
  DB  reachable-set intertwining: exact reduction (or model equality) for all intervention histories from a
      preparation set <=> intertwining on the reachable subspace W; instances: constructed linear case,
      weak vs strong lumpability, SCOPE9 TOPDOWN 005 qubit case, non-closure of compatible instrument
      families under union.
The private verification of SCOPE9 notes (part V of the private script) is not included; DA and DB use their own
seed streams, so their random-sample statistics differ from the private run. Synthetic mathematics only.
numpy 2.1.3, scipy 1.14.1; seeds [20261028, 1] (DA) and [20261028, 2] (DB).
Run: python3 -I hidden_gauge_reachable_intertwining_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.integrate import quad, simpson
from scipy.linalg import expm
from scipy.optimize import linprog

SEED = 20261028

def tv(p, q):
    return 0.5 * np.abs(np.asarray(p) - np.asarray(q)).sum()


def tv_radius(points):
    """min_q max_i TV(points_i, q) over the simplex, as an LP."""
    P = np.asarray(points, float); k, Y = P.shape
    # variables: q (Y), s_iy (k*Y) >= |P_iy - q_y|, t
    nv = Y + k * Y + 1
    c = np.zeros(nv); c[-1] = 1
    A, b = [], []
    for i in range(k):
        for y in range(Y):
            r1 = np.zeros(nv); r1[y] = -1; r1[Y + i * Y + y] = -1; A.append(r1); b.append(-P[i, y])
            r2 = np.zeros(nv); r2[y] = 1; r2[Y + i * Y + y] = -1; A.append(r2); b.append(P[i, y])
        r = np.zeros(nv); r[Y + i * Y: Y + (i + 1) * Y] = 0.5; r[-1] = -1; A.append(r); b.append(0)
    Aeq = np.zeros((1, nv)); Aeq[0, :Y] = 1
    res = linprog(c, A_ub=np.array(A), b_ub=np.array(b), A_eq=Aeq, b_eq=[1],
                  bounds=[(0, None)] * (nv - 1) + [(None, None)], method="highs")
    return res.fun



# ============================================================================ DA: hidden gauge
def visible_response(L, n, t):
    return expm(t * L)[:n, :n]


def part_DA(rng):
    out = {}
    c = 0.81
    A1 = np.array([[-1, 1], [0, -1.]]); B1 = np.array([[-1, 1], [c, -1.]])
    rows = []
    for K in (1, 10, 100, 1000):
        S = np.diag([1, 1 / K]); Si = np.diag([1, K])
        AK = S @ A1 @ Si; BK = S @ B1 @ Si
        assert np.allclose(AK, [[-1, K], [0, -1]]) and np.allclose(BK, [[-1, K], [c / K, -1]])
        sym = (AK + AK.T) / 2
        rows.append({"K": K, "visible_err_t3": float(expm(3 * BK)[0, 0] - expm(3 * AK)[0, 0]),
                     "kernel_at_t1": float(BK[0, 1] * np.exp(-1) * BK[1, 0]),
                     "norm_B_minus_A": float(np.linalg.norm(BK - AK, 2)), "norm_L": float(np.linalg.norm(BK, 2)),
                     "max_transient_A": float(max(np.linalg.norm(expm(t * AK), 2) for t in np.linspace(0, 5, 501))),
                     "sym_part_max_eig_A": float(np.linalg.eigvalsh(sym).max())})
    out["DA1_scope9_family_orbit"] = rows
    # invariant L1 small gain on the family: ell = 1, k = c -> ||x - x_M||_L1 <= c/(1-c), exact equality
    rc = np.sqrt(c)
    e_l1 = quad(lambda t: 0.5 * (np.exp(-(1 - rc) * t) + np.exp(-(1 + rc) * t)) - np.exp(-t), 0, np.inf, limit=400)[0]
    out["DA1_L1_error_exact"] = e_l1; out["DA1_L1_bound_c/(1-c)"] = c / (1 - c)
    # threshold sharpness: abscissa of B_K = -1 + sqrt(c), zero exactly at small-gain product c = 1
    out["DA1_threshold"] = [{"c": cv, "ell*k": cv, "abscissa": -1 + np.sqrt(cv)} for cv in (0.5, 0.81, 0.99, 1.0, 1.21)]
    # ---- DA2: random systems, random hidden similarity T: invariants and a norm-split convolution bound
    inv_err = 0.0; ratios = []; split_vs_tri = []
    for _ in range(60):
        n = int(rng.integers(1, 3)); m = int(rng.integers(2, 4))
        A = rng.normal(size=(n, n)) - 1.5 * np.eye(n); D = rng.normal(size=(m, m)) - 1.5 * np.eye(m)
        B = rng.normal(size=(n, m)); C = rng.normal(size=(m, n)); G = rng.normal(size=(1, n)); x0 = rng.normal(size=n)
        L = np.block([[A, B], [C, D]])
        U, _, Vt = np.linalg.svd(rng.normal(size=(m, m)))
        T = U @ np.diag(np.exp(rng.uniform(-3, 3, size=m))) @ Vt
        Ti = np.linalg.inv(T)
        LT = np.block([[A, B @ Ti], [T @ C, T @ D @ Ti]])
        for t in (0.3, 1.0, 2.5):
            inv_err = max(inv_err, np.abs(visible_response(L, n, t) - visible_response(LT, n, t)).max())
            inv_err = max(inv_err, np.abs(B @ expm(t * D) @ C - (B @ Ti) @ expm(t * T @ D @ Ti) @ (T @ C)).max())
        tt = 2.0
        sgrid = np.linspace(0, tt, 201)
        def M_of(Lm, u): return (G @ expm(u * Lm)[:n, n:])
        def rhs_split(Lm, Cm):
            vals = [np.linalg.norm(M_of(Lm, tt - s), 2) * np.linalg.norm(Cm @ expm(s * A) @ x0) for s in sgrid]
            return np.trapezoid(vals, sgrid)
        r_I = rhs_split(L, C); r_T = rhs_split(LT, T @ C)
        tight = np.trapezoid([np.linalg.norm(M_of(L, tt - s) @ C @ expm(s * A) @ x0) for s in sgrid], sgrid)
        ratios.append(max(r_I, r_T) / min(r_I, r_T)); split_vs_tri.append(r_I / max(tight, 1e-300))
    out["DA2_max_invariance_error"] = inv_err
    out["DA2_rhs_split_gauge_ratio_max"] = float(max(ratios)); out["DA2_rhs_split_gauge_ratio_median"] = float(np.median(ratios))
    out["DA2_rhs_split_over_invariant_triangle_bound_median"] = float(np.median(split_vs_tri))
    # ---- DA3: Gronwall-type constant ||L|| exp(T||L||) along the SCOPE9 gauge orbit (T = 3)
    rows = []
    for K in (1, 10, 100):
        BK = np.array([[-1, K], [c / K, -1.]]); nL = np.linalg.norm(BK, 2)
        rows.append({"K": K, "norm_L": float(nL), "log10_normL_exp_T_normL": float(np.log10(nL) + 3 * nL / np.log(10))})
    out["DA3_gronwall_constant_vs_K"] = rows
    # ---- DA4: invariant L1 small-gain bound on random systems (h(0) = 0)
    viol = 0; tested = 0; tight_ratio = []; tight_x = []
    for _ in range(300):
        n = int(rng.integers(1, 3)); m = int(rng.integers(1, 4))
        A = rng.normal(size=(n, n)) * 0.7 - 1.2 * np.eye(n); D = rng.normal(size=(m, m)) * 0.7 - 1.2 * np.eye(m)
        if np.linalg.eigvals(A).real.max() > -0.2 or np.linalg.eigvals(D).real.max() > -0.2: continue
        B = rng.normal(size=(n, m)); C = rng.normal(size=(m, n)) * rng.uniform(0.05, 0.6)
        Tend = 40.0
        ell = quad(lambda t: np.linalg.norm(expm(t * A), 2), 0, Tend, limit=200)[0]
        k = quad(lambda t: np.linalg.norm(B @ expm(t * D) @ C, 2), 0, Tend, limit=200)[0]
        if ell * k >= 0.95: continue
        L = np.block([[A, B], [C, D]]); x0 = rng.normal(size=n); x0 /= np.linalg.norm(x0)
        ts = np.linspace(0, Tend, 16001)
        X = np.array([expm(t * L)[:n, :n] @ x0 for t in ts]); XM = np.array([expm(t * A) @ x0 for t in ts])
        xl1 = simpson(np.linalg.norm(X, axis=1), x=ts); el1 = simpson(np.linalg.norm(X - XM, axis=1), x=ts)
        bx = ell / (1 - ell * k); be = ell ** 2 * k / (1 - ell * k)
        viol += int(xl1 > bx * (1 + 1e-6)) + int(el1 > be * (1 + 1e-6))
        tight_ratio.append(el1 / be); tight_x.append(xl1 / bx); tested += 1
    out["DA4_tested"] = tested; out["DA4_violations"] = viol
    out["DA4_max_ratio_error_over_bound"] = float(max(tight_ratio)); out["DA4_median_ratio"] = float(np.median(tight_ratio))
    out["DA4_max_ratio_xL1_over_bound"] = float(max(tight_x))
    return out



# ============================================================================ DB: reachable-set intertwining
def krylov_span(maps, P0, tol=1e-10):
    """Orthonormal basis of the smallest subspace containing columns of P0 and invariant under maps."""
    U0, s0, _ = np.linalg.svd(np.atleast_2d(P0), full_matrices=False)
    Q = U0[:, : int((s0 > tol * max(1.0, s0[0] if s0.size else 1.0)).sum())]
    changed = True
    while changed:
        changed = False
        for Mx in maps:
            cand = np.hstack([Q, Mx @ Q])
            U, s, _ = np.linalg.svd(cand, full_matrices=False)
            r = int((s > tol * max(1, s[0])).sum())
            if r > Q.shape[1]:
                Q = U[:, :r]; changed = True
    return Q


def part_DB(rng):
    out = {}
    # ---- DB1: constructed linear model; W-intertwining holds, global intertwining fails
    k, wv, wo = 2, 2, 2                    # W = (u in R^k, v in R^wv), outside block in R^wo
    N = k + wv + wo
    maps, phis = [], []
    for a in range(3):
        alpha = rng.normal(size=(k, k)) * 0.6
        Pa = np.zeros((k + wv, k + wv)); Pa[:k, :k] = alpha; Pa[k:, :k] = rng.normal(size=(wv, k)); Pa[k:, k:] = rng.normal(size=(wv, wv)) * 0.6
        Phi = np.zeros((N, N)); Phi[:k + wv, :k + wv] = Pa
        Phi[:k + wv, k + wv:] = rng.normal(size=(k + wv, wo)); Phi[k + wv:, k + wv:] = rng.normal(size=(wo, wo)) * 0.6
        maps.append(Phi); phis.append(alpha)
    Pi = np.zeros((k, N)); Pi[:, :k] = np.eye(k); Pi[:, k + wv:] = rng.normal(size=(k, wo))   # readout also sees outside block
    P0 = np.zeros((N, 3)); P0[:k + wv, :] = rng.normal(size=(k + wv, 3))                        # preparations inside W
    W = krylov_span(maps, P0)
    inter_W = max(np.abs(Pi @ Mx @ W - ph @ Pi @ W).max() for Mx, ph in zip(maps, phis))
    glob = max(np.abs(Pi @ Mx - ph @ Pi).max() for Mx, ph in zip(maps, phis))
    worst = 0.0
    for L_ in range(1, 7):
        for _ in range(40):
            h = rng.integers(0, 3, size=L_); p = P0 @ rng.normal(size=3)
            full, red = p.copy(), Pi @ p
            for a in h: full = maps[a] @ full; red = phis[a] @ red
            worst = max(worst, np.abs(Pi @ full - red).max())
    out["DB1_dimW"] = W.shape[1]; out["DB1_intertwining_on_W_err"] = float(inter_W)
    out["DB1_global_intertwining_err"] = float(glob); out["DB1_history_exactness_err"] = float(worst)
    # add one instrument that leaks W into the outside block -> W grows, exactness fails
    leak = np.eye(N); leak[k + wv, 0] = 1.0
    W2 = krylov_span(maps + [leak], P0)
    p = P0[:, 0]; full = maps[0] @ (leak @ p); red = phis[0] @ (Pi @ p)
    out["DB1_after_leak_dimW"] = W2.shape[1]; out["DB1_after_leak_error"] = float(np.abs(Pi @ full - red).max())
    # ---- DB2: weak vs strong lumpability (macro A={0}, B={1,2})
    P = np.array([[0.4, 0.3, 0.3], [0.1, 0.6, 0.3], [0.5, 0.1, 0.4]])
    Pbar = np.array([[0.4, 0.6], [0.3, 0.7]])
    agg = np.array([[1, 0], [0, 1], [0, 1.]])
    def macro_path_law(mu, n):
        law = {}
        for path in itertools.product(range(3), repeat=n + 1):
            pr = mu[path[0]] * np.prod([P[path[i], path[i + 1]] for i in range(n)])
            key = tuple(0 if s == 0 else 1 for s in path); law[key] = law.get(key, 0) + pr
        return law
    def reduced_law(mu, n):
        mb = mu @ agg; law = {}
        for path in itertools.product(range(2), repeat=n + 1):
            law[path] = mb[path[0]] * np.prod([Pbar[path[i], path[i + 1]] for i in range(n)])
        return law
    def law_tv(l1, l2):
        keys = set(l1) | set(l2); return 0.5 * sum(abs(l1.get(k_, 0) - l2.get(k_, 0)) for k_ in keys)
    mu_good = np.array([0.2, 0.4, 0.4]); mu_bad = np.array([0.0, 1.0, 0.0])
    out["DB2_strongly_lumpable"] = bool(np.allclose((P @ agg)[1], (P @ agg)[2]))
    out["DB2_TV_good_prep_n4"] = law_tv(macro_path_law(mu_good, 4), reduced_law(mu_good, 4))
    out["DB2_TV_bad_prep_n4"] = law_tv(macro_path_law(mu_bad, 4), reduced_law(mu_bad, 4))
    Wrow = krylov_span([P.T], np.array([[1.0, 0, 0], [0, 0.5, 0.5]]).T)          # row-vector dynamics
    out["DB2_dimW_good"] = Wrow.shape[1]
    # SCOPE9 002 FD06 bound uses the microstate-uniform one-step defect; on fibre B it is the TV radius
    rad = tv_radius([(P @ agg)[1], (P @ agg)[2]])
    out["DB2_microstate_radius_fibreB"] = rad
    out["DB2_FD06_bound_n4"] = 1 - (1 - rad) ** 4
    # belief-refined defect: on reachable beliefs (mass in B split 1/2:1/2) the macro row equals Pbar exactly
    beliefB = np.array([0, 0.5, 0.5]) @ P @ agg
    out["DB2_belief_refined_defect"] = tv(beliefB, Pbar[1])
    out["DB2_intertwining_on_W_err"] = float(np.abs((Wrow.T @ P @ agg) - (Wrow.T @ agg @ Pbar)).max())
    # ---- DB3: SCOPE9 005 in Pauli-transfer form
    def Dm(e): return np.diag([1, e, e, 1.0])
    AdZ = np.diag([1, -1, -1, 1.0]); AdH = np.array([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0], [0, 1, 0, 0.]])
    Wp = krylov_span([], Dm(0.0))                                                   # range of D_0
    Wa = krylov_span([], AdH @ Dm(0.0))                                             # after the H intervention
    out["DB3_dim_W_passive"] = Wp.shape[1]
    out["DB3_VA_eq_VB_on_W_passive"] = bool(np.allclose(np.eye(4) @ Wp, AdZ @ Wp))
    out["DB3_VA_eq_VB_on_W_active"] = bool(np.allclose(np.eye(4) @ Wa, AdZ @ Wa))
    out["DB3_identification_conditioning_eps0.001"] = float(1 / np.linalg.svd(Dm(0.001), compute_uv=False).min())
    # ---- DB4: compatible families not closed under union (exact)
    Pi2 = np.array([[1.0, 0.0]]); prep = np.array([[1.0], [0.0]])
    I1 = np.array([[1.0, 0], [1, 1]]); I2 = np.array([[1.0, 1], [0, 1]])
    def compatible(fam):
        Wf = krylov_span(fam, prep)
        # need Pi M w to depend only on Pi w for w in W: Pi M (W ∩ ker Pi) = 0
        Z = Wf @ np.linalg.svd(Pi2 @ Wf)[2][np.linalg.matrix_rank(Pi2 @ Wf):].T if Wf.shape[1] > np.linalg.matrix_rank(Pi2 @ Wf) else np.zeros((2, 0))
        return all(np.allclose(Pi2 @ M @ Z, 0) for M in fam), Wf.shape[1]
    out["DB4_I1_alone"] = compatible([I1]); out["DB4_I2_alone"] = compatible([I2]); out["DB4_I1_I2_together"] = compatible([I1, I2])
    out["DB4_history_I1_then_I2_full_vs_reduced"] = [float((Pi2 @ I2 @ I1 @ prep)[0, 0]), float((Pi2 @ prep)[0, 0])]
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    DA = part_DA(np.random.default_rng([SEED, 1])); DB = part_DB(np.random.default_rng([SEED, 2]))
    verdict = {
        "DA_orbit_and_invariance": DA["DA2_max_invariance_error"] < 1e-8,
        "DA_small_gain_sharp_on_family": abs(DA["DA1_L1_error_exact"] - DA["DA1_L1_bound_c/(1-c)"]) < 1e-6,
        "DA_small_gain_no_violation": DA["DA4_violations"] == 0 and DA["DA4_tested"] > 50,
        "DB_W_iff": DB["DB1_intertwining_on_W_err"] < 1e-10 and DB["DB1_history_exactness_err"] < 1e-9
                    and DB["DB1_global_intertwining_err"] > 1e-3 and DB["DB1_after_leak_error"] > 1e-3,
        "DB_weak_vs_strong": (not DB["DB2_strongly_lumpable"]) and DB["DB2_TV_good_prep_n4"] < 1e-12 and DB["DB2_TV_bad_prep_n4"] > 1e-3
                             and DB["DB2_TV_bad_prep_n4"] <= DB["DB2_FD06_bound_n4"] + 1e-12 and DB["DB2_belief_refined_defect"] < 1e-12,
        "DB_scope9_005": DB["DB3_VA_eq_VB_on_W_passive"] and not DB["DB3_VA_eq_VB_on_W_active"],
        "DB_union_not_closed": DB["DB4_I1_alone"][0] and DB["DB4_I2_alone"][0] and not DB["DB4_I1_I2_together"][0],
    }
    def clean(o):
        if isinstance(o, dict): return {kk: clean(v) for kk, v in o.items()}
        if isinstance(o, (list, tuple)): return [clean(v) for v in o]
        if isinstance(o, (np.floating,)): return float(o)
        if isinstance(o, (np.integer,)): return int(o)
        if isinstance(o, (np.bool_,)): return bool(o)
        return o
    res = clean({"DA": DA, "DB": DB, "verdict": {kk: bool(v) for kk, v in verdict.items()}, "seeds": [[SEED, 1], [SEED, 2]],
                 "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    (out / "hidden_gauge_reachable_intertwining_check.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
