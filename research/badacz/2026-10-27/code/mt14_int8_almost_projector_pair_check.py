#!/usr/bin/env python3
"""Cross-family check (Claude -> GPT cells MT14, INT8) of the pair
  research/mt14/2026-10-26/iw_mt14_rot006_sharp_almost_projector_tt_locality_pareto_001.md
  research/int8/2026-10-26/iw_int8_rot038_robust_cubic_tt_idempotence_pareto_frontier_001.md
Written independently of the authors' scripts (not read). Parts:
  A  exact (SymPy): Sym^2 Frobenius basis, TT projectors, ranks, ||P_x-P_y||, cube commutant,
     D-block structure, both witnesses, the common frontier delta=e(1-e), MT14 condition (1)
     equivalence and table, INT8 sample numbers.
  B  MT14: Bernstein+sampling lemma on random Hermitian matrix trig polynomials; local optimisation
     of the line problem (real self-adjoint kernels, |d_x|<=R) under condition (1).
  C  INT8: 3D sampling lemma (5*pi/N covering); onsite cube-equivariant family at every k of N=9;
     finite-N certificate on radius-1 cube-equivariant kernels near the witness, N=61, all k.
  D  bridge [proposal]: INT8 ROT035 step C on random real rank-2 idempotents; rounding constant;
     continuum frontier for real symmetric onsite B; open-case probe for real non-symmetric B.
Run: python3 mt14_int8_almost_projector_pair_check.py --out <dir>
numpy 2.1.3, scipy 1.14.1, sympy 1.13.3; seed 20261026. Local optimisation is a falsification
attempt (no global optimality); grid sup/inf are not interval-rigorous.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.optimize import minimize, brentq

SEED = 20261026
S2 = np.sqrt(2.0)


# ----------------------------------------------------------------------------- basis & projectors
def basis_mats(sqrt2=S2):
    E = []
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
        M = np.zeros((3, 3))
        if i == j:
            M[i, i] = 1.0
        else:
            M[i, j] = M[j, i] = 1.0 / sqrt2
        E.append(M)
    return E


BAS = basis_mats()


def vec(h):
    return np.array([h[0, 0], h[1, 1], h[2, 2], S2 * h[0, 1], S2 * h[0, 2], S2 * h[1, 2]])


def tt_proj(n):
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    Lam = np.eye(3) - np.outer(n, n)
    P = np.zeros((6, 6))
    for i, B in enumerate(BAS):
        P[:, i] = vec(Lam @ B @ Lam - 0.5 * Lam * np.trace(Lam @ B))
    return P


def tt_proj_batch(ns):
    ns = ns / np.linalg.norm(ns, axis=1, keepdims=True)
    return np.stack([tt_proj(n) for n in ns])


Q6 = np.eye(6) - np.outer(vec(np.eye(3)), vec(np.eye(3))) / 3.0     # onsite tracefree projector
PI1 = np.eye(6) - Q6
PID = np.zeros((6, 6)); PID[:3, :3] = np.eye(3) - np.ones((3, 3)) / 3
PIO = np.zeros((6, 6)); PIO[3:, 3:] = np.eye(3)


def cube_rotations():
    G = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            R = np.zeros((3, 3))
            for i in range(3):
                R[i, perm[i]] = signs[i]
            if np.isclose(np.linalg.det(R), 1):
                G.append(R)
    return G


def rho(R):
    M = np.zeros((6, 6))
    for i, B in enumerate(BAS):
        M[:, i] = vec(R @ B @ R.T)
    return M


def fib_hemisphere(n):
    i = np.arange(n) + 0.5
    z = i / n                                  # z in (0,1): hemisphere suffices since P(n)=P(-n)
    phi = np.pi * (1 + 5 ** 0.5) * i
    r = np.sqrt(1 - z ** 2)
    return np.stack([r * np.cos(phi), r * np.sin(phi), z], axis=1)


# ----------------------------------------------------------------------------- Part A (exact)
def part_A():
    out = {}
    r2 = sp.sqrt(2)
    def svec(h):
        return sp.Matrix([h[0, 0], h[1, 1], h[2, 2], r2 * h[0, 1], r2 * h[0, 2], r2 * h[1, 2]])
    sb = []
    for (i, j) in [(0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)]:
        M = sp.zeros(3, 3)
        if i == j: M[i, i] = 1
        else: M[i, j] = M[j, i] = 1 / r2
        sb.append(M)
    def sP(n):
        n = sp.Matrix(n); n = n / sp.sqrt((n.T * n)[0])
        L = sp.eye(3) - n * n.T
        cols = [svec(L * B * L - sp.Rational(1, 2) * L * (L * B).trace()) for B in sb]
        return sp.simplify(sp.Matrix.hstack(*cols))
    Px, Py = sP([1, 0, 0]), sP([0, 1, 0])
    Pd = sP([1, 2, 2])
    Iv = svec(sp.eye(3)); Q = sp.eye(6) - Iv * Iv.T / 3
    for nm, P in [("Px", Px), ("P122", Pd)]:
        assert sp.simplify(P * P - P) == sp.zeros(6) and sp.simplify(P - P.T) == sp.zeros(6)
        assert P.rank() == 2 and sp.simplify(Q * P - P) == sp.zeros(6)
    assert Q.rank() == 5
    ev = sp.Matrix((Px - Py) ** 2).eigenvals()
    out["eig_(Px-Py)^2"] = sorted(str(k) for k in ev)
    out["norm_Px_minus_Py"] = str(sp.sqrt(max(ev)))
    # cube commutant (exact)
    G = cube_rotations()
    def srho(R):
        R = sp.Matrix(R.astype(int))
        return sp.Matrix.hstack(*[svec(R * B * R.T) for B in sb])
    X = sp.Matrix(6, 6, sp.symbols("x0:36"))
    eqs = []
    for R in G:
        rr = srho(R); eqs += list(rr * X - X * rr)
    A_, _ = sp.linear_eq_to_matrix(eqs, list(X))
    out["cube_group_order"] = len(G)
    out["commutant_equations"] = len(eqs)
    out["commutant_rank"] = int(A_.rank())
    out["commutant_dim"] = 36 - int(A_.rank())
    v = svec(sp.diag(0, 1, -1)); w = svec(sp.diag(-2, 1, 1))
    out["Px_accepts_diag(0,1,-1)"] = bool(sp.simplify(Px * v - v) == sp.zeros(6, 1))
    out["Px_rejects_diag(-2,1,1)"] = bool(sp.simplify(Px * w) == sp.zeros(6, 1))
    # witnesses and the common frontier
    d, e = sp.symbols("delta e", nonnegative=True)
    tau = (1 - sp.sqrt(1 - 4 * d)) / 2
    assert sp.simplify(tau * (1 - tau) - d) == 0
    s = sp.sqrt(1 - 4 * d)
    out["MT14_condition_forms_equal"] = bool(sp.simplify((1 - 2 * tau) / (5 - 4 * tau) - s / (3 + 2 * s)) == 0)
    rho_ = sp.symbols("rho", positive=True)
    bN = 2 * rho_ / (1 - rho_)
    ineq = sp.simplify(sp.expand((1 - 2 * tau) * (1 - rho_) - 2 * rho_ * (2 - tau)) - ((1 - 2 * tau) - rho_ * (5 - 4 * tau)))
    out["MT14_bN(2-tau)<1-2tau_iff_(1)"] = bool(ineq == 0)
    # tau I and (1-e)Q against P(n): eigenvalues exact for a generic rational direction
    tI = sp.Rational(1, 10) * sp.eye(6)
    out["tauI_minus_P122_eigs(tau=1/10)"] = sorted(str(x) for x in (tI - Pd).eigenvals())
    eq = sp.Rational(3, 5)
    W = (1 - eq) * Q
    out["(1-e)Q_minus_P122_eigs(e=3/5)"] = sorted(str(x) for x in (W - Pd).eigenvals())
    out["(1-e)Q_defect_matrix_is_-e(1-e)Q"] = bool(sp.simplify(W * W - W + eq * (1 - eq) * Q) == sp.zeros(6))
    out["frontier_MT14_equals_INT8"] = bool(sp.simplify((1 - tau) * tau - d) == 0)  # e=1-tau => delta=e(1-e)
    out["factorisation_b(1-b)-a(1-a)"] = str(sp.factor(sp.Symbol("b") * (1 - sp.Symbol("b")) - sp.Symbol("a") * (1 - sp.Symbol("a"))))
    # MT14 table and INT8 sample numbers
    tab = []
    for dv in [0, 0.01, 0.09, 0.16, 0.24]:
        sv = np.sqrt(1 - 4 * dv); tv = (1 - sv) / 2
        tab.append([dv, tv, 1 - tv, sv / (np.pi * (3 + 2 * sv))])
    out["MT14_table"] = tab
    smp = {}
    for ev_ in [0.5, 0.6, 0.8]:
        N, R = 10001, 1
        M = (1 + ev_) / (1 - 5 * np.pi * R / N); L = 2 * np.pi * R / N * M; a = ev_ + L
        smp[str(ev_)] = {"M": M, "L": L, "full_lower": a * (1 - a), "zero_lower": max(0, a * (1 - a) - L * (2 * M + 1))}
    out["INT8_N10001_R1"] = smp
    return out


# ----------------------------------------------------------------------------- helpers: norms & grads
def herm_norm_grad(X):
    w, V = np.linalg.eigh(X)
    i = int(np.argmax(np.abs(w)))
    u = V[:, i]
    return abs(w[i]), np.sign(w[i]) * np.outer(u, u.conj())


def svd_norm_grad(X):
    U, sv, Vh = np.linalg.svd(X)
    return sv[0], np.outer(U[:, 0], Vh[0, :])


# ----------------------------------------------------------------------------- Part B (MT14)
def part_B(rng):
    out = {}
    # B1: Bernstein + sampling on random Hermitian 6x6 trig polynomials of degree R
    worst = 0.0; worst_jump = 0.0
    for _ in range(300):
        R = int(rng.integers(1, 4)); N = int(rng.integers(8 * R + 1, 60)) | 1
        if np.pi * R / N >= 1: continue
        C0 = rng.normal(size=(6, 6)); C0 = C0 + C0.T
        Cd = [rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6)) for _ in range(R)]
        if rng.random() < 0.5:                            # spiky Dirichlet-like scalar direction
            u = rng.normal(size=6); u /= np.linalg.norm(u)
            C0 = C0 * 0.05 + np.outer(u, u); Cd = [c * 0.05 + np.outer(u, u) for c in Cd]
        A = lambda th: C0 + sum(Cd[d - 1] * np.exp(-1j * d * th) + Cd[d - 1].conj().T * np.exp(1j * d * th) for d in range(1, R + 1))
        grid = 2 * np.pi * np.arange(N) / N
        Mg = max(np.linalg.norm(A(t), 2) for t in grid)
        Mc = max(np.linalg.norm(A(t), 2) for t in np.linspace(0, 2 * np.pi, 40 * N, endpoint=False))
        worst = max(worst, Mc / (Mg / (1 - np.pi * R / N)))
        bN = (2 * np.pi * R / N) / (1 - np.pi * R / N)
        worst_jump = max(worst_jump, np.linalg.norm(A(0) - A(2 * np.pi / N), 2) / (bN * Mg))
    out["B1_max_ratio_Mcont_over_bound"] = worst
    out["B1_max_ratio_jump_over_bN*Mgrid"] = worst_jump
    # B2: line problem, real self-adjoint kernel K0=K0^T, K_d (d=1..R) arbitrary real; A(theta) Hermitian
    Px = tt_proj([1, 0, 0])
    res = []
    configs = [(41, 1, 0.01), (41, 1, 0.09), (41, 1, 0.16), (41, 2, 0.01), (41, 2, 0.09)]
    iu = np.triu_indices(6)
    for (N, R, dl) in configs:
        tau = (1 - np.sqrt(1 - 4 * dl)) / 2
        assert R / N < np.sqrt(1 - 4 * dl) / (np.pi * (3 + 2 * np.sqrt(1 - 4 * dl)))
        th = 2 * np.pi * np.arange(N) / N
        targets = [Q6] + [Px] * (N - 1)
        nK0 = 21; npar = nK0 + 36 * R
        def unpack(p):
            K0 = np.zeros((6, 6)); K0[iu] = p[:nK0]; K0 = K0 + K0.T - np.diag(np.diag(K0))
            Kd = [p[nK0 + 36 * i: nK0 + 36 * (i + 1)].reshape(6, 6) for i in range(R)]
            return K0, Kd
        def Aj(K0, Kd, t):
            return K0 + sum(Kd[d - 1] * np.exp(-1j * d * t) + Kd[d - 1].T * np.exp(1j * d * t) for d in range(1, R + 1))
        def grad_to_params(G, t):
            g0 = np.real(G + G.T); g0[np.diag_indices(6)] /= 2      # K0 symmetric param
            g = [g0[iu]]
            for d in range(1, R + 1):
                g.append((2 * np.real(G.conj() * np.exp(-1j * d * t))).ravel())
            return np.concatenate(g)
        def cons(z):
            p, tt = z[:-1], z[-1]
            K0, Kd = unpack(p); c = []
            for t, P in zip(th, targets):
                A = Aj(K0, Kd, t)
                c.append(tt - herm_norm_grad(A - P)[0])
                c.append(dl - herm_norm_grad(A @ A - A)[0])
            return np.array(c)
        def cons_jac(z):
            p, tt = z[:-1], z[-1]
            K0, Kd = unpack(p); J = []
            for t, P in zip(th, targets):
                A = Aj(K0, Kd, t)
                _, G = herm_norm_grad(A - P)
                J.append(np.concatenate([-grad_to_params(G, t), [1.0]]))
                _, G2 = herm_norm_grad(A @ A - A)
                G2 = G2 @ A + A @ G2 - G2
                J.append(np.concatenate([-grad_to_params(G2, t), [0.0]]))
            return np.array(J)
        best = np.inf; best_feas = None
        for rs in range(12):
            p0 = np.zeros(npar)
            # starts: the MT14 witness tau*I, the INT8 witness (1-e)Q = tau*Q, a random scalar*Q
            K0 = [tau * np.eye(6), tau * Q6, rng.uniform(0, 1) * Q6][rs % 3]
            p0[:nK0] = K0[iu]
            p0 += rng.normal(size=npar) * (0.02 if rs < 6 else 0.15)
            z0 = np.concatenate([p0, [1.2]])
            r = minimize(lambda z: z[-1], z0, jac=lambda z: np.eye(len(z))[-1], method="SLSQP",
                         constraints=[{"type": "ineq", "fun": cons, "jac": cons_jac}],
                         options={"maxiter": 400, "ftol": 1e-10})
            c = cons(r.x)
            feas = np.min(c[1::2]) >= -1e-8
            err = r.x[-1] - min(0, np.min(c[0::2]))
            if feas and err < best:
                best = err
        res.append({"N": N, "R": R, "delta": dl, "one_minus_tau": 1 - tau, "best_local_min_found": best,
                    "violation": bool(best < 1 - tau - 1e-6)})
    out["B2_line_problem"] = res
    return out


# ----------------------------------------------------------------------------- Part C (INT8)
def int8_symbols(K, N, ks):
    """F_hat(k) = sum_d K(d) exp(-2 pi i k.d/N) for kernels on d in [-1,1]^3."""
    ds = np.array(list(itertools.product([-1, 0, 1], repeat=3)))
    ph = np.exp(-2j * np.pi * (ks @ ds.T) / N)                   # (nk, 27)
    return np.einsum("kd,dab->kab", ph, K)


def part_C(rng):
    out = {}
    G = cube_rotations(); RH = [rho(R) for R in G]
    # C1: 3D sampling lemma with the 5*pi/N covering, random radius-1 matrix trig polynomials
    worst = 0.0
    for _ in range(40):
        N = int(rng.choice([17, 21, 25, 31]))
        K = rng.normal(size=(27, 6, 6)) * rng.uniform(0.1, 1)
        kk = np.array(list(itertools.product(range(N), repeat=3)))
        ks = np.where(kk > N // 2, kk - N, kk); nz = np.any(ks != 0, axis=1)
        F = int8_symbols(K, N, ks[nz])
        Mg = np.max(np.linalg.norm(F, 2, axis=(1, 2)))
        fine = rng.uniform(-N / 2, N / 2, size=(4000, 3))         # continuous angles (in grid units)
        Mc = np.max(np.linalg.norm(int8_symbols(K, N, fine), 2, axis=(1, 2)))
        worst = max(worst, Mc / (Mg / (1 - 5 * np.pi / N)))
    out["C1_max_ratio_Mcont_over_bound"] = worst
    # C2: onsite cube-equivariant F = a1 Pi1 + b PiD + g PiO at every k != 0 of N = 9
    N = 9
    kk = np.array(list(itertools.product(range(N), repeat=3)))
    ks = np.where(kk > N // 2, kk - N, kk); ks = ks[np.any(ks != 0, axis=1)]
    Pk = tt_proj_batch(ks.astype(float))
    viol = 0; tested = 0; min_slack = np.inf
    for _ in range(4000):
        a1, b, g = rng.uniform(-0.5, 1.5, size=3)
        F = a1 * PI1 + b * PID + g * PIO
        eps = np.max(np.linalg.norm(F[None] - Pk, 2, axis=(1, 2)))
        eta = np.linalg.norm(F @ F - F, 2)
        if 0.5 <= eps < 1:
            tested += 1
            min_slack = min(min_slack, eta - eps * (1 - eps))
            viol += int(eta < eps * (1 - eps) - 1e-12)
        if eps < 0.5 - 1e-12:
            viol += 1                                            # a < 1/2 must be infeasible
    out["C2_onsite_equivariant"] = {"tested": tested, "violations": viol, "min_slack_eta_minus_eps(1-eps)": min_slack}
    # C3: finite-N certificate for radius-1 cube-equivariant kernels near the witness, N = 61, all k
    N = 61
    kk = np.array(list(itertools.product(range(N), repeat=3)))
    ks = np.where(kk > N // 2, kk - N, kk)
    nz = np.any(ks != 0, axis=1)
    Pk = np.zeros((len(ks), 6, 6)); Pk[nz] = tt_proj_batch(ks[nz].astype(float))
    ds = np.array(list(itertools.product([-1, 0, 1], repeat=3)))
    idx = {tuple(d): i for i, d in enumerate(ds)}
    def symmetrise(K):
        Ks = np.zeros_like(K)
        for R, Rh in zip(G, RH):
            Rinv = R.T
            for i, d in enumerate(ds):
                j = idx[tuple((Rinv @ d).round().astype(int))]
                Ks[i] += Rh @ K[j] @ Rh.T
        return Ks / len(G)
    viol = 0; inst = []
    for it in range(24):
        e0 = [0.55, 0.7, 0.85][it % 3]; sc = [0.002, 0.01, 0.03][(it // 3) % 3]
        K = np.zeros((27, 6, 6)); K[idx[(0, 0, 0)]] = (1 - e0) * Q6
        K = K + sc * symmetrise(rng.normal(size=(27, 6, 6)))
        eps = eta_f = eta_z = 0.0
        for ch in np.array_split(np.arange(len(ks)), 40):
            F = int8_symbols(K, N, ks[ch])
            D = np.linalg.norm(F @ F - F, 2, axis=(1, 2))
            eta_f = max(eta_f, D.max())
            m = nz[ch]
            if m.any():
                eps = max(eps, np.linalg.norm(F[m] - Pk[ch][m], 2, axis=(1, 2)).max())
                eta_z = max(eta_z, D[m].max())
        M = (1 + eps) / (1 - 5 * np.pi / N); L = 2 * np.pi / N * M; a = eps + L
        lo_f = a * (1 - a) if 0.5 <= a < 1 else (np.inf if a < 0.5 else 0.0)
        lo_z = max(0.0, a * (1 - a) - L * (2 * M + 1)) if 0.5 <= a < 1 else (np.inf if a < 0.5 else 0.0)
        v = int(eta_f < lo_f - 1e-12) + int(eta_z < lo_z - 1e-12)
        viol += v
        inst.append({"e0": e0, "scale": sc, "eps": eps, "eta_full": eta_f, "eta_zero": eta_z, "a": a,
                     "lower_full": lo_f, "lower_zero": lo_z})
    out["C3_radius1_equivariant_N61"] = {"instances": len(inst), "violations": viol,
                                          "min_eta_full_minus_lower": min(i["eta_full"] - i["lower_full"] for i in inst),
                                          "min_eta_zero_minus_lower": min(i["eta_zero"] - i["lower_zero"] for i in inst),
                                          "max_a": max(i["a"] for i in inst)}
    return out


# ----------------------------------------------------------------------------- Part D (bridge, open case)
def tracefree_det_zero_direction(E, rng):
    """INT8 ROT035 step C: ker E (dim 4) meets tracefree (dim 5) in dim >= 3; det is odd on the sphere."""
    ker = np.linalg.svd(E)[2][2:].T                                # 6x4 basis of ker E (E rank 2)
    tr = vec(np.eye(3)) / np.sqrt(3)
    # intersection with tracefree: vectors in ker orthogonal to tr
    c = ker.T @ tr
    Wc = np.linalg.svd(c[None, :])[2][1:].T                         # 4x3 null space of c^T
    W = ker @ Wc                                                     # 6x3
    def mat(x):
        h = W @ x
        return np.array([[h[0], h[3] / S2, h[4] / S2], [h[3] / S2, h[1], h[5] / S2], [h[4] / S2, h[5] / S2, h[2]]])
    w0 = rng.normal(size=3); w0 /= np.linalg.norm(w0)
    w1 = rng.normal(size=3); w1 -= w1 @ w0 * w0; w1 /= np.linalg.norm(w1)
    f = lambda s: np.linalg.det(mat(np.cos(np.pi * s) * w0 + np.sin(np.pi * s) * w1))
    s0 = brentq(f, 0, 1, xtol=1e-15)
    T = mat(np.cos(np.pi * s0) * w0 + np.sin(np.pi * s0) * w1)
    lam, V = np.linalg.eigh(T)
    n = V[:, int(np.argmin(np.abs(lam)))]
    return n, vec(T)


def sup_dirs(B, dirs_P):
    return np.max(np.linalg.norm(B[None] - dirs_P, 2, axis=(1, 2)))


def optimise_onsite(rng, dl, symmetric, dirs_P, restarts):
    iu = np.triu_indices(6)
    def unpack(p):
        if symmetric:
            B = np.zeros((6, 6)); B[iu] = p; return B + B.T - np.diag(np.diag(B))
        return p.reshape(6, 6)
    def gpar(G):
        if symmetric:
            g = G + G.T; g[np.diag_indices(6)] /= 2; return g[iu]
        return G.ravel()
    npar = 21 if symmetric else 36
    def cons(z):
        B = unpack(z[:-1]); c = [z[-1] - np.linalg.norm(B - P, 2) for P in dirs_P]
        c.append(dl - np.linalg.norm(B @ B - B, 2)); return np.array(c)
    def jac(z):
        B = unpack(z[:-1]); J = []
        for P in dirs_P:
            _, G = svd_norm_grad(B - P); J.append(np.concatenate([-gpar(G), [1.0]]))
        _, G = svd_norm_grad(B @ B - B); G = G @ B.T + B.T @ G - G
        J.append(np.concatenate([-gpar(G), [0.0]])); return np.array(J)
    tau = (1 - np.sqrt(1 - 4 * dl)) / 2
    best = (np.inf, None)
    for rs in range(restarts):
        if rs % 3 == 0: B0 = tau * np.eye(6)
        elif rs % 3 == 1: B0 = tau * Q6
        else: B0 = rng.normal(size=(6, 6)) * 0.3
        if not symmetric and rs % 2 == 1:
            B0 = B0 + rng.normal(size=(6, 6)) * 0.3                   # explicitly non-normal starts
        p0 = (B0 + B0.T) / 2 if symmetric else B0
        p0 = p0[iu] if symmetric else p0.ravel()
        p0 = p0 + rng.normal(size=npar) * 0.05
        z0 = np.concatenate([p0, [1.5]])
        r = minimize(lambda z: z[-1], z0, jac=lambda z: np.eye(len(z))[-1], method="SLSQP",
                     constraints=[{"type": "ineq", "fun": cons, "jac": jac}], options={"maxiter": 500, "ftol": 1e-11})
        B = unpack(r.x[:-1])
        if np.linalg.norm(B @ B - B, 2) <= dl + 1e-9:
            val = sup_dirs(B, dirs_P)
            if val < best[0]: best = (val, B)
    return best


def part_D(rng):
    out = {}
    # D1: ROT035 step C on random real rank-2 idempotents (orthogonal and oblique)
    worst = np.inf
    for i in range(200):
        X = rng.normal(size=(6, 2)); Y = rng.normal(size=(6, 2))
        if i % 2 == 0:
            X, _ = np.linalg.qr(X); E = X @ X.T
        else:
            E = X @ np.linalg.solve(Y.T @ X, Y.T)
        n, t = tracefree_det_zero_direction(E, rng)
        P = tt_proj(n)
        ratio = np.linalg.norm((E - P) @ t) / np.linalg.norm(t)
        assert np.linalg.norm(E @ t) < 1e-8 * np.linalg.norm(t) * max(1, np.linalg.norm(E, 2))
        worst = min(worst, ratio)
    out["D1_min_over_idempotents_of_||(E-P(n))T||/||T||"] = worst
    # D2: rounding constant K*||P(q)-P(n)|| for q = round(K n)
    mx = 0.0
    for _ in range(4000):
        n = rng.normal(size=3); n /= np.linalg.norm(n); K = int(rng.integers(4, 400))
        q = np.round(K * n)
        mx = max(mx, K * np.linalg.norm(tt_proj(q) - tt_proj(n), 2))
    out["D2_max_K*||P(q)-P(n)||"] = mx
    # D3/D4: continuum frontier for onsite B (symmetric = bridge; non-symmetric = open case probe)
    work = tt_proj_batch(fib_hemisphere(160))
    dense = tt_proj_batch(fib_hemisphere(20000))
    rows = []
    for dl in [0.05, 0.09, 0.16, 0.21]:
        tau = (1 - np.sqrt(1 - 4 * dl)) / 2
        for symmetric in [True, False]:
            val, B = optimise_onsite(rng, dl, symmetric, work, restarts=15)
            dense_val = sup_dirs(B, dense) if B is not None else np.inf
            defect = np.linalg.norm(B @ B - B, 2) if B is not None else np.nan
            tau_B = (1 - np.sqrt(max(0.0, 1 - 4 * defect))) / 2
            rows.append({"delta": dl, "symmetric": symmetric, "one_minus_tau": 1 - tau,
                         "best_sup_working_160": val, "same_B_sup_dense_20000": dense_val,
                         "defect_of_B": defect, "one_minus_tau(defect_B)": 1 - tau_B,
                         "below_frontier_dense": bool(dense_val < 1 - tau_B - 1e-6),
                         "nonnormality_||BB^T-B^TB||": float(np.linalg.norm(B @ B.T - B.T @ B, 2)) if B is not None else None})
    out["D3_D4_onsite_continuum"] = rows
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    A = part_A(); B = part_B(rng); C = part_C(rng); D = part_D(rng)
    verdict = {
        "A_exact_structure": A["commutant_dim"] == 3 and A["norm_Px_minus_Py"] == "1" and A["MT14_condition_forms_equal"]
                             and A["MT14_bN(2-tau)<1-2tau_iff_(1)"] and A["frontier_MT14_equals_INT8"],
        "B_sampling_lemma_holds": B["B1_max_ratio_Mcont_over_bound"] <= 1 + 1e-9 and B["B1_max_ratio_jump_over_bN*Mgrid"] <= 1 + 1e-9,
        "B_MT14_no_local_counterexample": not any(r["violation"] for r in B["B2_line_problem"]),
        "C_sampling_lemma_3D_holds": C["C1_max_ratio_Mcont_over_bound"] <= 1 + 1e-9,
        "C_INT8_onsite_frontier": C["C2_onsite_equivariant"]["violations"] == 0,
        "C_INT8_finite_certificate": C["C3_radius1_equivariant_N61"]["violations"] == 0,
        "D_ROT035_stepC_reproduced": D["D1_min_over_idempotents_of_||(E-P(n))T||/||T||"] > 1 - 1e-9,
        "D_rounding_constant_below_32": D["D2_max_K*||P(q)-P(n)||"] < 32,
        "D_symmetric_bridge_no_violation": not any(r["below_frontier_dense"] for r in D["D3_D4_onsite_continuum"] if r["symmetric"]),
        "D_nonsymmetric_open_case_hit": any(r["below_frontier_dense"] for r in D["D3_D4_onsite_continuum"] if not r["symmetric"]),
    }
    def clean(o):
        if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
        if isinstance(o, (list, tuple)): return [clean(v) for v in o]
        if isinstance(o, (np.floating, float)): return float(o)
        if isinstance(o, (np.integer,)): return int(o)
        if isinstance(o, (np.bool_,)): return bool(o)
        return o
    res = clean({"A": A, "B": B, "C": C, "D": D, "verdict": verdict, "seed": SEED,
                 "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    (out / "mt14_int8_almost_projector_pair_check.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
