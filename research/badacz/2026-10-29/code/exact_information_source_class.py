#!/usr/bin/env python3
"""BADACZ (Claude): exact-information source pairs for the Mech-S7 ROT032/033 moment problem (answer to AUD1 ROT005
CHECK 2 / Gate C and LT6 ROT009 T009.3 STOP).

Idea: parametrise the antinucleon redistribution in SOURCE space, u^3 dQp(u) = A k(x), dQn = -dQp, with
k(x) = (1-x^2)^4 sum_{l=3}^{10} a_l C_l^{(9/2)}(x) (Gegenbauer, weight (1-x^2)^4), x = 2(z - zmid)/L, z = ln u.
Then every comoving moment int u^3 dQ z^j dz (j = 0, 1, 2) is EXACTLY zero for every source spectrum, because
z^j is a polynomial of degree <= 2 in x and C_l^{(9/2)} (l >= 3) is orthogonal to it in the weight (1-x^2)^4.
The data (Qp + Qn) enter only positivity and the target, never the observation operator.

  E1  exact rational/symbolic checks (sympy): orthogonality, z-moments with symbolic L and zmid, class dimension 8.
  E2  ROT033 Gaussian-weighted yields are data-independent linear functionals of k; closed-form values at
      60 digits (erf recursion), exact-real constraint coefficients, residual of the float representative.
  E3  synthetic comparison of the worst-case linear target radius under the same share-H2 budget: Mech-type
      share class (moments imposed numerically) versus the exact source class, for synthetic W and kernels.
Synthetic mathematics only; no Wu-Xu data, no adjoint data. numpy 2.1.3, scipy 1.14.1, sympy 1.13.3,
mpmath 1.3.0; deterministic.
Run: python3 -I exact_information_source_class.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from numpy.polynomial import legendre as npleg
from scipy.linalg import eigh

L = math.log(0.92 / 0.07)
ZMID = 0.5 * (math.log(0.07) + math.log(0.92))
LMAX = 10
LS = list(range(3, LMAX + 1))


def gegen_k_polys():
    x = sp.symbols("x")
    out = []
    for l in LS:
        k = sp.expand((1 - x ** 2) ** 4 * sp.gegenbauer(l, sp.Rational(9, 2), x))
        out.append(sp.Poly(k, x))
    return x, out


def part_E1():
    x, ks = gegen_k_polys()
    Ls, zm = sp.symbols("L zmid", positive=True)
    orth = all(sp.integrate(k.as_expr() * x ** i, (x, -1, 1)) == 0 for k in ks for i in range(3))
    zmom = all(sp.simplify(sp.integrate(k.as_expr() * (zm + Ls * x / 2) ** j * Ls / 2, (x, -1, 1))) == 0
               for k in ks for j in range(3))
    # dimension: span{(1-x^2)^4 x^m, m <= 10} intersected with the three exact moment conditions
    M = sp.Matrix([[sp.integrate((1 - x ** 2) ** 4 * x ** (m + i), (x, -1, 1)) for m in range(LMAX + 1)] for i in range(3)])
    dim_kernel = (LMAX + 1) - M.rank()
    # k_l lie in that span and are independent
    coeff = sp.Matrix([[k.as_expr().expand().coeff(x, m + 0) for m in range(LMAX + 9)] for k in ks])
    return {"orthogonality_x_moments_exact": bool(orth), "z_moments_symbolic_L_zmid_exact_zero": bool(zmom),
            "kernel_dim_of_degree10_class": int(dim_kernel), "gegenbauer_family_rank": int(coeff.rank()),
            "example_k3_leading_coeffs": [str(c) for c in ks[0].all_coeffs()[:3]]}


def gaussian_row_mp(ks, zc, sig, dps=60):
    """int_{-1}^{1} k_l(x) exp(-(z(x)-zc)^2/(2 sig^2)) (L/2) dx for each l, closed form (erf recursion) at dps digits."""
    mp.mp.dps = dps
    Lm = mp.log(mp.mpf("0.92") / mp.mpf("0.07")); zmm = (mp.log(mp.mpf("0.07")) + mp.log(mp.mpf("0.92"))) / 2
    mu = 2 * (mp.mpf(zc) - zmm) / Lm; s = 2 * mp.mpf(sig) / Lm
    a, b = -1 - mu, 1 - mu
    deg = max(k.degree() for k in ks)
    J = [mp.mpf(0)] * (deg + 1)
    J[0] = s * mp.sqrt(mp.pi / 2) * (mp.erf(b / (s * mp.sqrt(2))) - mp.erf(a / (s * mp.sqrt(2))))
    ea, eb = mp.exp(-a ** 2 / (2 * s ** 2)), mp.exp(-b ** 2 / (2 * s ** 2))
    if deg >= 1:
        J[1] = s ** 2 * (ea - eb)
    for i in range(2, deg + 1):
        J[i] = s ** 2 * (a ** (i - 1) * ea - b ** (i - 1) * eb) + (i - 1) * s ** 2 * J[i - 2]
    rows = []
    for k in ks:
        coeffs = k.all_coeffs()[::-1]                     # c_m x^m
        tot = mp.mpf(0)
        for m, c in enumerate(coeffs):
            if c == 0:
                continue
            # x^m = (y + mu)^m, y = x - mu
            tot += mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) * mp.fsum(mp.binomial(m, i) * mu ** (m - i) * J[i] for i in range(m + 1))
        rows.append(tot * Lm / 2)
    return rows


def part_E2():
    x, ks = gegen_k_polys()
    out = {}
    designs = {"G1": (math.log(832396936.244 / 1e9), 1.0), "G2": (math.log(477318736.294 / 1e9), 0.65)}
    rows = {name: gaussian_row_mp(ks, zc, sg) for name, (zc, sg) in designs.items()}
    # independent cross-check: tanh-sinh quadrature at 50 digits with exact rational polynomial coefficients
    mp.mp.dps = 50
    Lm = mp.log(mp.mpf("0.92") / mp.mpf("0.07")); zmm = (mp.log(mp.mpf("0.07")) + mp.log(mp.mpf("0.92"))) / 2
    for name, (zc, sg) in designs.items():
        diffs = []
        for k, rv in zip(ks, rows[name]):
            cf = [mp.mpf(sp.Rational(c).p) / mp.mpf(sp.Rational(c).q) for c in k.all_coeffs()]
            f = lambda t: mp.polyval(cf, t) * mp.exp(-((zmm + Lm * t / 2) - mp.mpf(zc)) ** 2 / (2 * mp.mpf(sg) ** 2)) * Lm / 2
            q = mp.quad(f, [-1, 0, 1])
            diffs.append(abs(q - rv))
        rnorm = mp.sqrt(mp.fsum(v ** 2 for v in rows[name]))
        out[f"{name}_max_abs_diff_vs_tanhsinh50_over_rownorm"] = float(max(diffs) / rnorm)
    # exact-real constraint: k = k_a - (G(k_a)/G(k_b)) k_b with a = 3 (l index 0), b = the l with largest |G|
    r1 = rows["G1"]
    ib = int(np.argmax([abs(float(v)) for v in r1]))
    ia = 0 if ib != 0 else 1
    coef = -r1[ia] / r1[ib]
    resid_exact = r1[ia] + coef * r1[ib]
    coef_float = float(coef)
    resid_float = r1[ia] + mp.mpf(coef_float) * r1[ib]
    out.update({"G1_row_60digits_first3": [mp.nstr(v, 20) for v in r1[:3]], "G1_pivot_l": LS[ib], "G1_partner_l": LS[ia],
                "G1_exact_coefficient": mp.nstr(coef, 40), "G1_residual_exact_object": mp.nstr(resid_exact, 5),
                "G1_residual_float_representative_rel": float(abs(resid_float) / max(abs(r1[ia]), mp.mpf(1e-300)))})
    # conditioning of stacked Gaussian rows in the coefficient space (Euclidean on a_l, normalised rows)
    A = np.array([[float(v) for v in rows["G1"]], [float(v) for v in rows["G2"]]])
    An = A / np.linalg.norm(A, axis=1, keepdims=True)
    sv = np.linalg.svd(An, compute_uv=False)
    out["two_gaussian_rows_normalised_singular_values"] = sv.tolist()
    return out, ks


# ---------------------------------------------------------------- E3 synthetic radius comparison
def phis_share(xq):
    """Mech share class: (1-x^2)^4 P_j(x), j = 0..10, with first and second x-derivatives."""
    w = (1 - xq ** 2) ** 4
    dw = -8 * xq * (1 - xq ** 2) ** 3
    d2w = -8 * (1 - xq ** 2) ** 3 + 48 * xq ** 2 * (1 - xq ** 2) ** 2
    P, dP, d2P = [], [], []
    for j in range(LMAX + 1):
        c = np.eye(LMAX + 1)[j]
        P.append(npleg.legval(xq, c)); dP.append(npleg.legval(xq, npleg.legder(c))); d2P.append(npleg.legval(xq, npleg.legder(c, 2)))
    P, dP, d2P = map(np.array, (P, dP, d2P))
    return w * P, dw * P + w * dP, d2w * P + 2 * dw * dP + w * d2P


def k_values(ks, xq):
    out = []
    for k in ks:
        p = np.poly1d([float(c) for c in k.all_coeffs()])
        out.append((p(xq), p.deriv(1)(xq), p.deriv(2)(xq)))
    return np.array([o[0] for o in out]), np.array([o[1] for o in out]), np.array([o[2] for o in out])


def radius_share(Wz, psi, xq, wq, R):
    zq = ZMID + L * xq / 2; dz = wq * L / 2
    f, f1, f2 = phis_share(xq)
    f2z = f2 * (2 / L) ** 2
    C = np.array([(Wz * zq ** j * f) @ dz for j in range(3)])        # numerical moment rows (11 cols)
    Z = np.linalg.svd(C)[2][3:].T
    G2 = (f2z * dz) @ f2z.T
    b = f @ (psi * dz)
    H = Z.T @ G2 @ Z; g = Z.T @ b
    val = R * math.sqrt(g @ np.linalg.solve(H, g))
    cstar = Z @ np.linalg.solve(H, g); cstar *= R / math.sqrt(cstar @ G2 @ cstar)
    h = cstar @ f
    return val, float(np.abs(h).max())


def radius_exact(ks, Wfun, psi, xq, wq, R):
    zq = ZMID + L * xq / 2; dz = wq * L / 2
    k0, k1, k2 = k_values(ks, xq)
    W, W1, W2 = Wfun(zq)
    iw = 1 / W; iw1 = -W1 / W ** 2; iw2 = (2 * W1 ** 2 - W * W2) / W ** 3
    a = 2 / L
    h = k0 * iw
    h2 = k2 * a * a * iw + 2 * k1 * a * iw1 + k0 * iw2
    G2 = (h2 * dz) @ h2.T
    b = h @ (psi * dz)
    val = R * math.sqrt(b @ np.linalg.solve(G2, b))
    cst = np.linalg.solve(G2, b); cst *= R / math.sqrt(cst @ G2 @ cst)
    # exact moments of the represented direction (diagnostic: numeric quadrature of the exact object)
    mom = [float(abs(((cst @ k0) * zq ** j) @ dz)) for j in range(3)]
    return val, float(np.abs(cst @ h).max()), max(mom)


def part_E3(ks):
    xq, wq = npleg.leggauss(400)
    R = 11.435960696834389
    def Wa(z):     # u^3 * Q_sum with Q_sum ~ u^-1.3 (synthetic)
        W = np.exp(1.7 * z); return W, 1.7 * W, 1.7 ** 2 * W
    def Wb(z):     # with a smooth modulation
        e = np.exp(1.7 * z); m = 1 + 0.3 * np.sin(2 * z)
        return e * m, e * (1.7 * m + 0.6 * np.cos(2 * z)), e * (1.7 ** 2 * m + 2 * 1.7 * 0.6 * np.cos(2 * z) - 1.2 * np.sin(2 * z))
    rows = []
    for wname, Wfun in (("u^1.7", Wa), ("u^1.7(1+.3 sin 2z)", Wb)):
        zq = ZMID + L * xq / 2
        W = Wfun(zq)[0]
        kernels = {"in_moment_span_control": W * (1 + 0.5 * zq), "cubic": W * (1 + 0.5 * zq + 0.2 * zq ** 3),
                   "bump": W * np.exp(-((zq + 1.0) / 0.6) ** 2), "oscill": W * np.cos(3 * zq)}
        for kname, psi in kernels.items():
            rs, sup_s = radius_share(W, psi, xq, wq, R)
            re, sup_e, mom = radius_exact(ks, Wfun, psi, xq, wq, R)
            rows.append({"W": wname, "kernel": kname, "radius_share_class": rs, "radius_exact_class": re,
                         "ratio_exact/share": re / rs, "sup|h|_share": sup_s, "sup|h|_exact": sup_e,
                         "exact_class_moment_quadrature_residual": mom})
    return rows


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    E1 = part_E1(); E2, ks = part_E2(); E3 = part_E3(ks)
    verdict = {
        "E1_exact_zero_moments_any_spectrum": E1["orthogonality_x_moments_exact"] and E1["z_moments_symbolic_L_zmid_exact_zero"]
                                              and E1["kernel_dim_of_degree10_class"] == 8 and E1["gegenbauer_family_rank"] == 8,
        "E2_gaussian_rows_closed_form": E2["G1_max_abs_diff_vs_tanhsinh50_over_rownorm"] < 1e-30 and E2["G2_max_abs_diff_vs_tanhsinh50_over_rownorm"] < 1e-30
                                        and E2["G1_residual_float_representative_rel"] < 1e-15,
        "E3_control_radius_zero_both": all(r["radius_share_class"] < 1e-12 and r["radius_exact_class"] < 1e-12 for r in E3 if r["kernel"] == "in_moment_span_control"),
    }
    res = {"L": L, "zmid": ZMID, "E1": E1, "E2": E2, "E3": E3, "verdict": verdict,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "exact_information_source_class.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
