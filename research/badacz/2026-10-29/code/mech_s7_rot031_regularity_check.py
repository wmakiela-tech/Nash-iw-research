#!/usr/bin/env python3
"""BADACZ (Claude): cross-family check of Mech-S7 ROT031 (regularity-basis confounder) and a constraint-independent
bound.
  C1  exact integrals of sin^4 windows (sympy), closed-form H1/L2 and H2/L2 ratios, Mech's numbers at N = 11, 21.
  C2  clamped-beam eigenvalues on [-1, 1]: roots of cos(b) cosh(b) = 1 (b = beta*length), cross-checked by
      Rayleigh-Ritz in the clamped basis (1-x^2)^2 P_j.
  C3  Courant-Fischer: for ANY 9 linear functionals, min over their kernel of ||f''||/||f|| (z units) is at most
      (b_10/L)^2 (infimum over H^2_0; C^3-flat class has the same infimum). Tested with 300 random functionals in a
      large C^3-flat Galerkin space; Mech's 11-mode basis: kernel minimum lies between the 1st and 10th Ritz values.
  C4  Gauss-512 over the whole interval vs exact per-window integration for piecewise sin^4 sources (artifact size).
  C5  arithmetic of Mech's reported ratios.
Synthetic mathematics only (no Wu-Xu data, no adjoint functions). numpy 2.1.3, scipy 1.14.1, sympy 1.13.3; seed 20261029.
Run: python3 -I mech_s7_rot031_regularity_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp
from numpy.polynomial import legendre as npleg
from numpy.polynomial import polynomial as P
from scipy.linalg import eigh
from scipy.optimize import brentq

SEED = 20261029
L = float(np.log(0.92 / 0.07))     # z-length of the support (Mech: M in [7e7, 9.2e8] g)


def part_C1():
    th = sp.symbols("theta")
    s4 = sp.sin(th) ** 4
    I0 = sp.simplify(sp.integrate(s4 ** 2, (th, 0, sp.pi)))
    I1 = sp.simplify(sp.integrate(sp.diff(s4, th) ** 2, (th, 0, sp.pi)))
    I2 = sp.simplify(sp.integrate(sp.diff(s4, th, 2) ** 2, (th, 0, sp.pi)))
    out = {"int_sin8": str(I0), "int_d1sq": str(I1), "int_d2sq": str(I2),
           "match_35pi/128_5pi/8_4pi": bool(sp.simplify(I0 - 35 * sp.pi / 128) == 0 and sp.simplify(I1 - 5 * sp.pi / 8) == 0
                                           and sp.simplify(I2 - 4 * sp.pi) == 0)}
    rows = {}
    for N in (10, 11, 13, 15, 21):
        h = L / N
        r1 = float(np.sqrt(float(I1 / I0)) * np.pi / h)            # (pi/h) sqrt(I1/I0) = 4 pi N/(sqrt7 L)
        r2 = float(np.sqrt(float(I2 / I0)) * (np.pi / h) ** 2)     # sqrt(512/35) (pi N/L)^2
        rows[N] = {"H1/L2": r1, "H2/L2": r2, "closed_H1": 4 * np.pi * N / (np.sqrt(7) * L),
                   "closed_H2": np.sqrt(512 / 35) * (np.pi * N / L) ** 2}
    out["ratios"] = rows
    out["mech_N11"] = [20.2828120877, 688.391263351]; out["mech_N21"] = [38.7217321675, 2508.93014163]
    return out


def clamped_roots(k):
    f = lambda b: np.cos(b) * np.cosh(b) - 1
    roots, b = [], 1.0
    while len(roots) < k:
        if f(b) * f(b + 0.01) < 0:
            roots.append(brentq(f, b, b + 0.01, xtol=1e-14))
        b += 0.01
    return np.array(roots)


def basis_poly(power, nmodes):
    """Legendre-series coefficient arrays of (1-x^2)^power * P_j(x), j < nmodes (Legendre basis for stability)."""
    w = npleg.poly2leg(P.polypow([1.0, 0.0, -1.0], power))
    return [npleg.legmul(w, np.eye(nmodes)[j]) for j in range(nmodes)]


def gram(polys, deriv):
    x, wq = npleg.leggauss(200)
    V = np.array([npleg.legval(x, npleg.legder(p, deriv) if deriv else p) for p in polys])
    return (V * wq) @ V.T


def ritz(polys):
    M = gram(polys, 0); K = gram(polys, 2)
    return eigh(K, M, eigvals_only=True)


def part_C2():
    b = clamped_roots(10)                       # beta * length, length = 2 for [-1, 1]
    mu = (b / 2) ** 4                           # eigenvalues of d^4 (Rayleigh quotient of ||F''||^2/||F||^2) on [-1, 1]
    th = ritz(basis_poly(2, 40))[:10]          # clamped basis, Rayleigh-Ritz upper bounds
    return {"beta_length": b.tolist(), "mu_x": mu.tolist(), "ritz_clamped40_first10": th.tolist(),
            "max_rel_ritz_minus_mu": float(np.max(th / mu - 1)), "min_rel_ritz_minus_mu": float(np.min(th / mu - 1)),
            "z_bound_k1": float((b[0] / L) ** 2), "z_bound_k10": float((b[9] / L) ** 2)}


def part_C3(rng, C2):
    zfac = (2 / L) ** 2                         # ||f''||/||f|| in z = zfac * ||F''||/||F|| in x
    big = basis_poly(4, 36)                     # C^3-flat Galerkin space (Mech's class), 36 modes
    M = gram(big, 0); K = gram(big, 2)
    x, wq = npleg.leggauss(200)
    Vb = np.array([npleg.legval(x, p) for p in big])
    worst, ratios = 0.0, []
    for _ in range(300):
        # 9 random functionals: integrals against random smooth weights (Legendre combos + Gaussian bumps)
        W = np.array([npleg.legval(x, rng.normal(size=8)) + rng.normal() * np.exp(-((x - rng.uniform(-1, 1)) / rng.uniform(0.05, 0.5)) ** 2)
                      for _ in range(9)])
        A = (W * wq) @ Vb.T                     # 9 x 36
        Z = np.linalg.svd(A)[2][9:].T           # kernel basis (27-dim)
        lam = eigh(Z.T @ K @ Z, Z.T @ M @ Z, eigvals_only=True)[0]
        val = zfac * np.sqrt(lam)
        ratios.append(val / C2["z_bound_k10"]); worst = max(worst, val - C2["z_bound_k10"])
    # Mech's 11-mode global basis: kernel minimum must lie between the 1st and 10th Ritz values (z units)
    th11 = zfac * np.sqrt(ritz(basis_poly(4, 11)))
    th10 = zfac * np.sqrt(ritz(basis_poly(4, 10)))
    return {"random_functionals": 300, "max_(kernel_min - CF_bound)": float(worst),
            "max_ratio_kernel_min_over_bound": float(max(ratios)), "median_ratio": float(np.median(ratios)),
            "mech_basis11_ritz_z_first": float(th11[0]), "mech_basis11_ritz_z_10th": float(th11[9]),
            "mech_basis10_ritz_z_first": float(th10[0]), "mech_basis10_ritz_z_10th": float(th10[9]),
            "mech_reported_N11": 111.30478343, "mech_reported_N10": 112.97}


def part_C4(rng):
    N = 11; h = L / N; edges = np.arange(N + 1) * h
    xg, wg = npleg.leggauss(512)
    zq = 0.5 * L * (xg + 1); wqz = 0.5 * L * wg
    errs = []
    for _ in range(50):
        c = rng.normal(size=N)
        def f(z):
            j = np.minimum((z // h).astype(int), N - 1)
            return c[j] * np.sin(np.pi * (z - edges[j]) / h) ** 4
        for p in range(3):
            g = rng.normal(size=3)
            wfun = lambda z: np.exp(g[0] * z / L) * (1 + 0.3 * g[1] * np.cos(3 * z)) * (z / L) ** p
            whole = np.sum(wqz * f(zq) * wfun(zq))
            xw, ww = npleg.leggauss(64)
            per = 0.0; absint = 0.0
            for j in range(N):
                zz = edges[j] + 0.5 * h * (xw + 1); w_ = 0.5 * h * ww
                per += np.sum(w_ * f(zz) * wfun(zz)); absint += np.sum(w_ * np.abs(f(zz) * wfun(zz)))
            errs.append(abs(whole - per) / absint)
    return {"N": N, "gauss512_whole_vs_perwindow_rel_err_max": float(max(errs)),
            "median": float(np.median(errs))}


def part_C5():
    return {"curvature_ratio_local/global": 688.39126335 / 111.30478343,
            "L2_ratio": 0.68496372 / 0.43199873, "RMS_ratio": 0.06401712 / 0.04037486,
            "response_ratio_range_after_RMS": [4.33 / (0.06401712 / 0.04037486), 5.71 / (0.06401712 / 0.04037486)]}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    C1 = part_C1(); C2 = part_C2(); C3 = part_C3(rng, C2); C4 = part_C4(rng); C5 = part_C5()
    r11 = C1["ratios"][11]; r21 = C1["ratios"][21]
    verdict = {
        "C1_exact_integrals_and_numbers": C1["match_35pi/128_5pi/8_4pi"]
            and abs(r11["H1/L2"] / 20.2828120877 - 1) < 1e-9 and abs(r11["H2/L2"] / 688.391263351 - 1) < 1e-9
            and abs(r21["H1/L2"] / 38.7217321675 - 1) < 1e-9 and abs(r21["H2/L2"] / 2508.93014163 - 1) < 1e-9,
        "C2_clamped_eigen_crosscheck": -1e-10 <= C2["min_rel_ritz_minus_mu"] and C2["max_rel_ritz_minus_mu"] < 1e-6,
        "C3_courant_fischer_no_violation": C3["max_(kernel_min - CF_bound)"] <= 1e-9,
        "C3_mech_numbers_within_ritz_window": C3["mech_basis11_ritz_z_first"] <= 111.30478343 <= C3["mech_basis11_ritz_z_10th"]
            and C3["mech_basis10_ritz_z_first"] <= 112.97 <= C3["mech_basis10_ritz_z_10th"],
    }
    res = {"L": L, "C1": C1, "C2": C2, "C3": C3, "C4": C4, "C5": C5, "verdict": verdict, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "mech_s7_rot031_regularity_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
