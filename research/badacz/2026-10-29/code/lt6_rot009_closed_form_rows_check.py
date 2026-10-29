#!/usr/bin/env python3
"""BADACZ (Claude): cross-family check of LT6 ROT009 / REV028 7.5l (exact H-projection repair) and 6.19, with one
constructive remark: under the explicit power-law sub-edge continuation used in the public Mech-S7 code
(Q_s(u) = edgeQ_s * u**slope_s, research/mech-s7/2026-10-23/terminal_7d_exact_mass_common_background_006.py), the
weight W(z) = u^3 (Qp + Qn) is a sum of two exponentials in z = ln u, so every moment row
int W z^j phi_k dz (phi_k = (1-x^2)^4 P_k) and every Gaussian row is a CLOSED FORM; epsilon_M can be made
arbitrarily small (computed here at 50 digits), so the T009.3 STOP does not bind for that conditional model.
  C1  T009.1 exact rational example; T009.1-T009.3 inequalities on random instances (incl. the Weyl second correction).
  C2  closed-form rows at 50 digits vs double Gauss-Legendre; a double-precision null direction has 50-digit residual
      e ~ 1e-16 relative; the 50-digit H-projection repair drives it to ~1e-45 with ||q||_H ~ 1e-16.
  C3  ROT033 bounded-noise radius rho(eta) = R[p eta + q sqrt(1-eta^2)] (eta < p/sqrt(p^2+q^2)) vs direct maximisation.
Uses Mech's public constants (Q1, Q2, M1, M2) only to fix the two exponents; no Mech data. numpy 2.1.3, scipy 1.14.1,
sympy 1.13.3, mpmath 1.3.0; seed 20261029.
Run: python3 -I lt6_rot009_closed_form_rows_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as Fr
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial import legendre as npleg
from scipy.optimize import minimize

SEED = 20261029
Q1 = [489105.5126008581, 59105.93631247951, 29086.774913348447, 34849.08026691193, 34656.17773724596]
Q2 = [442306.73787501804, 53467.712852971126, 26311.795859614824, 31504.591028094237, 31328.963561830213]
M1 = 5.609588603804452e32; M2 = 6.099798045788406e32


# ---------------------------------------------------------------- C1
def part_C1(rng):
    H = [Fr(1), Fr(4), Fr(9)]; Mrow = [Fr(1), Fr(1), Fr(0)]; c = [Fr(3, 5), Fr(-3, 10), Fr(2, 5)]
    e = sum(m * x for m, x in zip(Mrow, c))
    MHM = sum(m * m / h for m, h in zip(Mrow, H))
    q = [m / h / MHM * e for m, h in zip(Mrow, H)]
    p = [x - y for x, y in zip(c, q)]
    nH = lambda v: sum(h * x * x for h, x in zip(H, v))
    T = lambda v: v[0] + 5 * v[2] + v[2] ** 3 / 10
    ex = {"q": [str(v) for v in q], "p": [str(v) for v in p], "Mp": str(sum(m * x for m, x in zip(Mrow, p))),
          "|c|^2": str(nH(c)), "|p|^2": str(nH(p)), "|q|^2": str(nH(q)), "target_gap": str(T(p) - T([-v for v in p]))}
    # random instances
    worst = {"pyth": 0.0, "q_bound": -np.inf, "weyl_second": -np.inf, "target_bound": -np.inf}
    for _ in range(400):
        n = int(rng.integers(3, 13)); m = int(rng.integers(1, n))
        A = rng.normal(size=(n, n)); Hm = A @ A.T + 0.1 * np.eye(n)
        M = rng.normal(size=(m, n)); c = rng.normal(size=n)
        Hi = np.linalg.inv(Hm); e = M @ c
        J = Hi @ M.T @ np.linalg.inv(M @ Hi @ M.T); q = J @ e; p = c - q
        nh = lambda v: float(v @ Hm @ v)
        worst["pyth"] = max(worst["pyth"], abs(nh(c) - nh(p) - nh(q)) / nh(c))
        w, V = np.linalg.eigh(Hm); Hmh = V @ np.diag(w ** -0.5) @ V.T
        s = np.linalg.svd(M @ Hmh, compute_uv=False).min()
        worst["q_bound"] = max(worst["q_bound"], math.sqrt(nh(q)) - np.linalg.norm(e) / s)
        # T009.3: Mtrue = Mhat + Delta
        Delta = rng.normal(size=(m, n)) * 1e-3
        Mt = M + Delta
        epsM = np.linalg.norm(Delta @ Hmh, 2)
        if s > epsM:
            r = Mt @ p                                         # p repaired for Mhat = M
            Jt = Hi @ Mt.T @ np.linalg.inv(Mt @ Hi @ Mt.T); q2 = Jt @ r
            R = math.sqrt(nh(c))
            worst["weyl_second"] = max(worst["weyl_second"], math.sqrt(nh(q2)) - epsM * R / (s - epsM))
        # T009.2 target bound with a Lipschitz target T(v) = sin(g.v) * |g|_{H^-1} scaled: L_T = ||g||_{H^-1}
        g = rng.normal(size=n); LT = math.sqrt(g @ Hi @ g)
        Tf = lambda v: math.sin(g @ v)
        lhs = abs(Tf(p) - Tf(-p)) / 2; rhs = abs(Tf(c) - Tf(-c)) / 2 - LT * np.linalg.norm(e) / s
        worst["target_bound"] = max(worst["target_bound"], rhs - lhs)
    return {"example": ex, "random_worst": worst}


# ---------------------------------------------------------------- C2 closed-form rows
def phi_polys():
    x = sp.symbols("x")
    return x, [sp.Poly(sp.expand((1 - x ** 2) ** 4 * sp.legendre(k, x)), x) for k in range(11)]


def closed_rows(gammas, amps, dps=50):
    """rows R_jk = int_{za}^{zb} sum_s amps_s e^{gamma_s z} z^j phi_k(x(z)) dz, exact antiderivatives at dps digits."""
    mp.mp.dps = dps
    za, zb = mp.log(mp.mpf("0.07")), mp.log(mp.mpf("0.92"))
    Lm = zb - za; zm = (za + zb) / 2
    x, ph = phi_polys()
    z = sp.symbols("z")
    rows = []
    for j in range(3):
        row = []
        for k in range(11):
            # polynomial in z: z^j * phi_k(2(z - zm)/L) -> coefficients in mp
            pk = ph[k].all_coeffs()[::-1]                     # coefficients in x
            # build polynomial in z numerically (mp): sum_m c_m (2(z-zm)/L)^m * z^j
            coeffs = [mp.mpf(0)] * (len(pk) + j + 1)
            for m_, cm in enumerate(pk):
                if cm == 0:
                    continue
                cmf = mp.mpf(sp.Rational(cm).p) / mp.mpf(sp.Rational(cm).q)
                # (2/L)^m (z - zm)^m = (2/L)^m sum_i binom(m,i) z^i (-zm)^(m-i)
                for i in range(m_ + 1):
                    coeffs[i + j] += cmf * (2 / Lm) ** m_ * mp.binomial(m_, i) * (-zm) ** (m_ - i)
            tot = mp.mpf(0)
            for gam, A in zip(gammas, amps):
                # int e^{g z} P(z) dz = e^{g z} sum_r (-1)^r P^{(r)}(z) / g^{r+1}
                def anti(zz):
                    acc = mp.mpf(0); deriv = list(coeffs)
                    r = 0
                    while any(d != 0 for d in deriv):
                        val = mp.polyval(deriv[::-1], zz)
                        acc += (-1) ** r * val / gam ** (r + 1)
                        deriv = [i * deriv[i] for i in range(1, len(deriv))]
                        r += 1
                    return mp.e ** (gam * zz) * acc
                tot += A * (anti(zb) - anti(za))
            row.append(tot)
        rows.append(row)
    return rows, Lm, zm


def part_C2():
    slopes = [math.log(Q2[i] / Q1[i]) / math.log(M2 / M1) for i in range(5)]
    gammas = [mp.mpf(3) + mp.mpf(slopes[3]), mp.mpf(3) + mp.mpf(slopes[4])]   # pbar (INDEX 3), nbar (INDEX 4)
    amps = [mp.mpf(Q1[3]), mp.mpf(Q1[4])]
    rows, Lm, zm = closed_rows(gammas, amps)
    # double Gauss-Legendre comparison
    xg, wg = npleg.leggauss(512)
    L = float(Lm); zmf = float(zm); zq = zmf + L * xg / 2; dz = wg * L / 2
    W = Q1[3] * np.exp(float(gammas[0]) * zq) + Q1[4] * np.exp(float(gammas[1]) * zq)
    x, ph = phi_polys()
    P = np.array([[float(ph[k].eval(float(t))) for t in xg] for k in range(11)])
    Rq = np.array([(W * zq ** j * P) @ dz for j in range(3)])
    Rc = np.array([[float(v) for v in r] for r in rows])
    reldiff = float(np.max(np.abs(Rq - Rc)) / np.max(np.abs(Rc)))
    # a double-precision null direction (as a numerical solver would produce)
    Z = np.linalg.svd(Rq)[2][3:].T
    c = Z[:, 0] / np.linalg.norm(Z[:, 0]) * 0.1
    # H exact: int phi_i'' phi_j'' dz = (2/L)^3 int phi_i''(x) phi_j''(x) dx (rational part exact)
    Hx = sp.Matrix(11, 11, lambda i, j: sp.integrate(sp.diff(ph[i].as_expr(), x, 2) * sp.diff(ph[j].as_expr(), x, 2), (x, -1, 1)))
    mp.mp.dps = 50
    Hm = mp.matrix(11, 11)
    for i in range(11):
        for j in range(11):
            r_ = sp.Rational(Hx[i, j]); Hm[i, j] = mp.mpf(r_.p) / mp.mpf(r_.q) * (2 / Lm) ** 3
    Cm = mp.matrix(rows)
    cm = mp.matrix([mp.mpf(float(v)) for v in c])
    e = Cm * cm
    scale = max(abs(sum(abs(Cm[j, k] * cm[k]) for k in range(11))) for j in range(3))
    Hi = Hm ** -1
    MHM = Cm * Hi * Cm.T
    q = Hi * Cm.T * (MHM ** -1) * e
    p = cm - q
    e_after = Cm * p
    qH = mp.sqrt((q.T * Hm * q)[0])
    cH = mp.sqrt((cm.T * Hm * cm)[0])
    return {"slopes_pbar_nbar": [slopes[3], slopes[4]], "rows_closed_vs_gauss512_rel": reldiff,
            "residual_double_null_rel": float(max(abs(v) for v in e) / scale),
            "residual_after_50digit_repair_rel": float(max(abs(v) for v in e_after) / scale),
            "q_H_over_c_H": float(qH / cH)}


# ---------------------------------------------------------------- C3 ROT033 bounded-noise radius
def part_C3(rng):
    worst = 0.0
    for _ in range(300):
        p, q = abs(rng.normal()), abs(rng.normal()); eta = rng.uniform(0, 1); R = 1.0
        rho = R * (p * eta + q * math.sqrt(1 - eta * eta)) if eta < p / math.hypot(p, q) else R * math.hypot(p, q)
        # direct: maximise p s + q t subject to s^2 + t^2 <= 1, |s| <= eta (grid over s)
        s = np.linspace(-eta, eta, 20001); t = np.sqrt(np.maximum(0, 1 - s * s))
        direct = float(np.max(p * s + q * t)) * R
        worst = max(worst, abs(direct - rho) / rho)
    return {"cases": 300, "max_rel_diff_formula_vs_direct": worst}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    C1 = part_C1(rng); C2 = part_C2(); C3 = part_C3(rng)
    ex = C1["example"]; w = C1["random_worst"]
    verdict = {
        "C1_example_exact": ex["p"] == ["9/25", "-9/25", "2/5"] and ex["Mp"] == "0" and ex["|c|^2"] == "54/25"
                            and ex["|p|^2"] == "261/125" and ex["|q|^2"] == "9/125" and ex["target_gap"] == "2958/625",
        "C1_random_inequalities": bool(w["pyth"] < 1e-10 and w["q_bound"] <= 1e-10 and w["weyl_second"] <= 1e-10 and w["target_bound"] <= 1e-10),
        "C2_closed_form_rows": C2["rows_closed_vs_gauss512_rel"] < 1e-12 and C2["residual_after_50digit_repair_rel"] < 1e-40,
        "C3_noise_radius_formula": C3["max_rel_diff_formula_vs_direct"] < 1e-6,
    }
    res = {"C1": C1, "C2": C2, "C3": C3, "verdict": verdict, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "lt6_rot009_closed_form_rows_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
