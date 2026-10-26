#!/usr/bin/env python3
"""Cross-family check (Claude -> GPT cell Geeky-S11) of
research/geeky-s11/2026-10-26/geeky_s11_rot027_uniform_Lie_insertion_logmean_001.md
Rebuilt only from the public text (author scripts and the source helper were not read). Parts:
  A  exact (SymPy): product-rule derivative, closed forms, u/g = sinh identity, polarisation
     coefficients c+- from the continuum Lie derivative + raw-k TT projection, series (L-G)/G, (A-L)/G.
  B  strict inequalities g < u < e on random (a, b, m); alpha = 0 equality.
  C  continuum numbers at beta = .02 (mpmath, 30 digits) and convergence of the finite-N formula.
  D  direct 3D grid check (FFT, centered differences, 3-term Lie, raw-k TT projector) of
     ||(U_m - S_m) H_p|| / ||H_p|| and of the claim that only sidebands p+-1 appear.
Run: python3 geeky_s11_rot027_logmean_check.py --out <dir>
numpy 2.1.3, sympy 1.13.3, mpmath 1.3.0; seed 20261026.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp

SEED = 20261026
CPM = {2: (Fraction(71, 200), Fraction(31, 40)), 3: (Fraction(261, 680), Fraction(141, 200))}
AUTHOR_CONT = {(2, "0.05"): (0.0005827429243, 0.0011658869501), (3, "0.05"): (0.0011135669619, 0.0022286508917),
               (2, "1/6"): (0.0039849969164, 0.0079955364093), (3, "1/6"): (0.0053006802967, 0.0106692890730)}


def part_A():
    out = {}
    a, b, eps, z = sp.symbols("a b epsilon z", positive=True)
    E, T = sp.symbols("E T", commutative=False)
    for m in [2, 4]:
        expr = sp.expand((E + eps * T / (m + 1)) ** (m + 1))
        der = sp.expand(sp.diff(expr, eps).subs(eps, 0))
        U = sp.expand(sum(E ** (m - l) * T * E ** l for l in range(m + 1)) / (m + 1))
        out[f"product_rule_m{m}"] = bool(sp.expand(der - U) == 0)
    m = sp.Integer(6)
    u = sum(a ** (m - l) * b ** l for l in range(int(m) + 1)) / (m + 1)
    out["closed_form_m6"] = bool(sp.simplify(u - (a ** (m + 1) - b ** (m + 1)) / ((m + 1) * (a - b))) == 0)
    r = sp.exp(z)
    ug = sp.simplify(sum(r ** k for k in range(int(m) + 1)) / ((m + 1) * r ** (m / 2)))
    out["u/g_sinh_identity_m6"] = bool(sp.simplify((ug - sp.sinh((m + 1) * z / 2) / ((m + 1) * sp.sinh(z / 2))).rewrite(sp.exp)) == 0)
    # polarisation coefficients from first principles
    ex, ey, ez = sp.eye(3)[:, 0], sp.eye(3)[:, 1], sp.eye(3)[:, 2]
    def tt(k, M):
        k = sp.Matrix(k); L = sp.eye(3) - k * k.T / (k.T * k)[0]
        return sp.simplify(L * M * L - L * (L * M).trace() / 2)
    cs = {}
    for p in [2, 3]:
        v = sp.Matrix([-1, p, 0]); Tp = sp.Rational(3, 10) * (ez * ez.T - v * v.T / (p ** 2 + 1))
        assert sp.simplify(sum(x ** 2 for x in Tp) - sp.Rational(9, 50)) == 0
        assert tt([p, 1, 0], Tp) == Tp
        W = ex * (Tp * ey).T + (Tp * ey) * ex.T
        for s in [1, -1]:
            Ms = -(Tp + s * W) / 2          # coefficient of sin((p+s)x + y) in L_C H_p, C = (0, cos x, 0)
            c2 = sp.nsimplify(sum(x ** 2 for x in tt([p + s, 1, 0], Ms)) / sp.Rational(9, 50))
            cs[f"p{p}_s{s:+d}"] = str(sp.sqrt(c2))
    out["polarisation_c"] = cs
    out["polarisation_matches_author"] = all(sp.Rational(cs[f"p{p}_s+1"]) == sp.Rational(CPM[p][0].numerator, CPM[p][0].denominator)
                                             and sp.Rational(cs[f"p{p}_s-1"]) == sp.Rational(CPM[p][1].numerator, CPM[p][1].denominator)
                                             for p in [2, 3])
    LG = sp.sinh(z / 2) / (z / 2) - 1
    AL = sp.cosh(z / 2) - sp.sinh(z / 2) / (z / 2)
    out["(L-G)/G_series"] = str(sp.series(LG, z, 0, 6).removeO())
    out["(A-L)/G_series"] = str(sp.series(AL, z, 0, 6).removeO())
    return out


def part_B(rng):
    """Exact rational check of g < u < e (g compared through g^2 = (ab)^m), and the sinh identity in
    mpmath at 50 digits; floating point underflows for large m and is not used here."""
    viol = 0
    for _ in range(3000):
        a = Fraction(int(rng.integers(1, 1000)), 1000); b = Fraction(int(rng.integers(1, 1000)), 1000)
        if a == b:
            continue
        m = 2 * int(rng.integers(1, 21))
        u = sum(a ** (m - l) * b ** l for l in range(m + 1)) / (m + 1)
        e = (a ** m + b ** m) / 2
        g2 = (a * b) ** m                                       # g = sqrt(g2) > 0, u > 0
        if not (u * u > g2 and u < e):
            viol += 1
    mp.mp.dps = 50
    worst = mp.mpf(0)
    for _ in range(2000):
        a = mp.mpf(rng.uniform(0.05, 1.0)); b = mp.mpf(rng.uniform(0.05, 1.0)); m = 2 * int(rng.integers(1, 200))
        u = (a ** (m + 1) - b ** (m + 1)) / ((m + 1) * (a - b)); g = (a * b) ** (mp.mpf(m) / 2)
        z = mp.log(a / b)
        worst = max(worst, abs(u / g - mp.sinh((m + 1) * z / 2) / ((m + 1) * mp.sinh(z / 2))) / (u / g))
    k = np.arange(5)
    eq0 = float(np.mean(0.7 ** (4 - k) * 0.7 ** k) - 0.7 ** 4)
    return {"rational_pairs": 3000, "strict_violations": viol, "max_rel_err_sinh_identity_mp50": float(worst),
            "a=b_u_minus_g_float": eq0}


def part_C():
    mp.mp.dps = 30
    rows = {}
    for (p, al), (aUS, aAU) in AUTHOR_CONT.items():
        alpha = mp.mpf(1) / 6 if al == "1/6" else mp.mpf(al)
        beta = mp.mpf("0.02")
        d = lambda j: mp.e ** (-4 * mp.pi ** 2 * alpha * beta * (j ** 2 + 1))
        def LGA(j):
            x, y = d(j), d(p)
            Lm = (x - y) / (mp.log(x) - mp.log(y)); G = mp.sqrt(x * y); A = (x + y) / 2
            return Lm, G, A
        cp, cm = [mp.mpf(c.numerator) / c.denominator for c in CPM[p]]
        Lp, Gp, Ap = LGA(p + 1); Lm_, Gm, Am = LGA(p - 1)
        US = mp.sqrt(cp ** 2 * (Lp - Gp) ** 2 + cm ** 2 * (Lm_ - Gm) ** 2)
        AU = mp.sqrt(cp ** 2 * (Ap - Lp) ** 2 + cm ** 2 * (Am - Lm_) ** 2)
        # finite N with m_N = 2 ceil(beta N^2 / 2)
        fin = {}
        for N in [64, 512, 8192]:
            mN = 2 * int(mp.ceil(beta * N ** 2 / 2))
            q = lambda j: 1 - 4 * alpha * (mp.sin(mp.pi * j / N) ** 2 + mp.sin(mp.pi / N) ** 2)
            dN = mp.sin(2 * mp.pi / N) / (2 * mp.pi / N)
            def ug(j):
                x, y = q(j), q(p)
                return (x ** (mN + 1) - y ** (mN + 1)) / ((mN + 1) * (x - y)) - (x * y) ** (mN // 2)
            fin[N] = float(dN * mp.sqrt(cp ** 2 * ug(p + 1) ** 2 + cm ** 2 * ug(p - 1) ** 2))
        rows[f"p{p}_alpha{al}"] = {"U-S": float(US), "author_U-S": aUS, "A-U": float(AU), "author_A-U": aAU,
                                   "abs_diff_U-S": float(abs(US - aUS)), "abs_diff_A-U": float(abs(AU - aAU)),
                                   "finite_N_U-S": fin}
    return rows


def part_D():
    """Direct 3D grid: fields (3,3,N,N,N) on [0,2pi)^3."""
    res = []; worst = 0.0; worst_leak = 0.0
    for N in [12, 16]:
        h = 2 * np.pi / N
        k1 = np.fft.fftfreq(N, d=1.0 / N)
        KX, KY, KZ = np.meshgrid(k1, k1, k1, indexing="ij")
        x = np.arange(N) * h
        X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
        def d_(f, axis):                                     # centered difference
            return (np.roll(f, -1, axis=axis) - np.roll(f, 1, axis=axis)) / (2 * h)
        lapsym = -4 * (np.sin(np.pi * KX / N) ** 2 + np.sin(np.pi * KY / N) ** 2 + np.sin(np.pi * KZ / N) ** 2) / h ** 2
        kv = np.stack([KX, KY, KZ]); kk = (kv ** 2).sum(0); kk[0, 0, 0] = 1
        Lam = np.eye(3)[:, :, None, None, None] - kv[:, None] * kv[None, :] / kk
        def Bop(Hf):                                         # raw-k orthogonal TT projector per mode
            F = np.fft.fftn(Hf, axes=(2, 3, 4))
            LFL = np.einsum("ik...,kl...,lj...->ij...", Lam, F, Lam)
            tr = np.einsum("kl...,lk...->...", Lam, F)
            out = LFL - 0.5 * Lam * tr
            out[:, :, 0, 0, 0] = F[:, :, 0, 0, 0]
            return np.real(np.fft.ifftn(out, axes=(2, 3, 4)))
        Cy = np.cos(X); dxCy = d_(Cy, 0)
        def Lie(Hf):                                          # (L_C h)_ij = C^k d_k h_ij + h_kj d_i C^k + h_ik d_j C^k
            out = Cy * d_(Hf, 3)                              # C^y d_y h (field axes: 2->x, 3->y, 4->z)
            add = np.zeros_like(Hf)
            add[0, :] += dxCy * Hf[1, :]                      # i = x, k = y: h_yj d_x C^y
            add[:, 0] += dxCy * Hf[:, 1]
            return out + add
        for alpha in [0.05, 1 / 6]:
            Esym = 1 + alpha * h ** 2 * lapsym
            def Eop(Hf, n=1):
                F = np.fft.fftn(Hf, axes=(2, 3, 4)); return np.real(np.fft.ifftn(F * Esym ** n, axes=(2, 3, 4)))
            Top = lambda Hf: Bop(Lie(Bop(Hf)))
            for p in [2, 3]:
                v = np.array([-1.0, p, 0]); ez = np.array([0, 0, 1.0])
                Tp = 0.3 * (np.outer(ez, ez) - np.outer(v, v) / (p ** 2 + 1))
                Hp = Tp[:, :, None, None, None] * np.cos(p * X + Y)[None, None]
                for m in [2, 4, 6]:
                    U = sum(Eop(Top(Eop(Hp, l)), m - l) for l in range(m + 1)) / (m + 1)
                    S = Eop(Top(Eop(Hp, m // 2)), m // 2)
                    ratio = np.sqrt(((U - S) ** 2).sum() / (Hp ** 2).sum())
                    q = lambda j: 1 - 4 * alpha * (np.sin(np.pi * j / N) ** 2 + np.sin(np.pi / N) ** 2)
                    def ug(j):
                        a, b = q(j), q(p); kk_ = np.arange(m + 1)
                        return np.mean(a ** (m - kk_) * b ** kk_) - (a * b) ** (m / 2)
                    dN = np.sin(2 * np.pi / N) / (2 * np.pi / N)
                    cp, cm = [float(c) for c in CPM[p]]
                    formula = dN * np.sqrt(cp ** 2 * ug(p + 1) ** 2 + cm ** 2 * ug(p - 1) ** 2)
                    # leakage outside the four sideband modes (+-(p+-1), +-1, 0)
                    F = np.fft.fftn(U - S, axes=(2, 3, 4)); mask = np.ones((N, N, N), bool)
                    for sx in [p + 1, p - 1]:
                        for sg in [1, -1]:
                            mask[(sg * sx) % N, sg % N, 0] = False
                    leak = np.sqrt((np.abs(F[:, :, mask]) ** 2).sum() / max((np.abs(F) ** 2).sum(), 1e-300))
                    rel = abs(ratio - formula) / formula
                    worst = max(worst, rel); worst_leak = max(worst_leak, leak)
                    res.append({"N": N, "alpha": alpha, "p": p, "m": m, "grid": ratio, "formula": formula, "rel_diff": rel,
                                "leak_fraction": leak})
    return {"cases": len(res), "max_rel_diff_grid_vs_formula": worst, "max_leak_fraction": worst_leak, "detail": res}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    A = part_A(); B = part_B(rng); C = part_C(); D = part_D()
    verdict = {
        "A_algebra_and_polarisation": all(A[k] for k in ["product_rule_m2", "product_rule_m4", "closed_form_m6", "u/g_sinh_identity_m6", "polarisation_matches_author"]),
        "B_strict_inequalities": B["strict_violations"] == 0,
        "C_author_continuum_numbers": all(r["abs_diff_U-S"] < 5e-13 and r["abs_diff_A-U"] < 5e-13 for r in C.values()),
        "D_grid_matches_formula": D["max_rel_diff_grid_vs_formula"] < 1e-10 and D["max_leak_fraction"] < 1e-10,
    }
    verdict = {k: bool(v) for k, v in verdict.items()}
    res = {"A": A, "B": B, "C": C, "D": D, "verdict": verdict, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "geeky_s11_rot027_logmean_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps({k: v for k, v in res.items() if k != "D"}, indent=1, default=float))
    print(json.dumps({k: v for k, v in D.items() if k != "detail"}, indent=1, default=float))


if __name__ == "__main__":
    main()
