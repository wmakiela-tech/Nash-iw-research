#!/usr/bin/env python3
"""Cross-family check (Claude -> GPT cell MT14) of
research/mt14/2026-10-27/iw_mt14_rot009_frontb_borsuk_ulam_exact_nonlinear_source_alias_001.md
From the public text only (author scripts not read). Synthetic positive weights, NOT Mech sources.
  A  moment matrix of the eleven disjoint sin^4 log-mass bins: all 165 ordered 3-column minors
     positive (log moments z^j, power moments e^{jz}, centred moments); rank 3, ker dim 8.
  B  positivity: the author's mu is sufficient; the sharp inf-norm constant mu* = min_i min_z
     r(z)/phi_i(z) >= mu is computed and tested on both sides.
  C  Borsuk-Ulam numerics on the radius-r sphere of V = ker M: for random smooth nonlinear
     Y: R^11 -> R^p, p = 6, 7, an antipodal coincidence Y(c) = Y(-c) is found to machine
     precision; for p = 8 with an injective-type Y no coincidence exists (threshold check).
Run: python3 mt14_rot009_borsuk_ulam_check.py --out <dir>
numpy 2.1.3, scipy 1.14.1; seed 20261028.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares

SEED = 20261028
NB = 11
ZA, ZB = np.log(0.07), np.log(0.92)
HW = (ZB - ZA) / NB
GX, GW = np.polynomial.legendre.leggauss(160)


def bin_nodes(i):
    a = ZA + i * HW
    z = a + (GX + 1) / 2 * HW
    return z, GW * HW / 2, np.sin(np.pi * (z - a) / HW) ** 4


def weight_factory(rng):
    a1, a2, b1, b2 = rng.uniform(0.2, 2), rng.uniform(0.2, 2), rng.uniform(-1, 1), rng.uniform(-1, 1)
    return lambda z: np.exp(3 * z) * (a1 * np.exp(b1 * z) + a2 * np.exp(b2 * z) * (1.5 + np.sin(3 * z)))


def moment_matrix(wfun, family):
    M = np.zeros((3, NB))
    zbar = (ZA + ZB) / 2
    for i in range(NB):
        z, w, phi = bin_nodes(i)
        for j in range(3):
            f = {"log": z ** j, "power": np.exp(j * z), "centred": (z - zbar) ** j}[family]
            M[j, i] = np.sum(w * wfun(z) * phi * f)
    return M


def part_A(rng):
    out = {"weights_tested": 0, "minors_tested": 0, "nonpositive_minors": 0, "min_rank": 3, "max_rank": 3}
    for _ in range(20):
        wf = weight_factory(rng)
        for fam in ["log", "power", "centred"]:
            M = moment_matrix(wf, fam)
            sign = None
            for cols in itertools.combinations(range(NB), 3):
                d = np.linalg.det(M[:, cols])
                if fam == "centred":                          # same Chebyshev system up to a fixed triangular change
                    sign = sign or np.sign(d)
                    out["nonpositive_minors"] += int(np.sign(d) != sign)
                else:
                    out["nonpositive_minors"] += int(d <= 0)
                out["minors_tested"] += 1
            r = np.linalg.matrix_rank(M)
            out["min_rank"] = min(out["min_rank"], r); out["max_rank"] = max(out["max_rank"], r)
        out["weights_tested"] += 1
    return out


def part_B(rng):
    """Positivity. Author: ||c||_2 < mu, mu = min_z min(q_p,q_n)/(q_p+q_n), is sufficient.
    Sharp constant for ||c||_inf (disjoint bins): mu* = min_i min_{z in bin i} r_s(z)/phi_i(z), where
    r_s is the ratio of the species being decreased; mu* >= mu. Test both sides of mu*."""
    out = {"trials": 0, "violations_below_mu": 0, "violations_below_mu_star": 0,
           "negative_found_just_above_mu_star": 0, "min_mu_star_over_mu": np.inf, "max_mu_star_over_mu": 0.0}
    zg = np.concatenate([bin_nodes(i)[0] for i in range(NB)])
    ph = np.zeros((NB, zg.size))
    for i in range(NB):
        z, _, phi = bin_nodes(i); ph[i, i * GX.size:(i + 1) * GX.size] = phi
    owner = np.repeat(np.arange(NB), GX.size)
    for _ in range(200):
        qp = 0.5 + rng.uniform(0, 1) * (1.2 + np.sin(rng.uniform(1, 4) * zg))
        qn = 0.5 + rng.uniform(0, 1) * (1.2 + np.cos(rng.uniform(1, 4) * zg))
        rp, rn = qp / (qp + qn), qn / (qp + qn)
        mu = np.minimum(rp, rn).min()
        phi_at = ph[owner, np.arange(zg.size)]
        with np.errstate(divide="ignore"):
            mu_star = np.min(np.where(phi_at > 0, np.minimum(rp, rn) / phi_at, np.inf))
        out["min_mu_star_over_mu"] = min(out["min_mu_star_over_mu"], mu_star / mu)
        out["max_mu_star_over_mu"] = max(out["max_mu_star_over_mu"], mu_star / mu)
        def minspecies(c):
            h = c @ ph
            return min((qp + (qp + qn) * h).min(), (qn - (qp + qn) * h).min())
        for rho, key in ((0.999 * mu, "violations_below_mu"), (0.999 * mu_star, "violations_below_mu_star")):
            for _k in range(5):
                c = rng.choice([-1.0, 1.0], size=NB) * rho            # corners of the inf-ball are worst
                out[key] += int(minspecies(c) <= 0)
        k = int(np.argmin(np.where(phi_at > 0, np.minimum(rp, rn) / phi_at, np.inf)))
        c2 = np.zeros(NB); c2[owner[k]] = (-1.0 if rp[k] <= rn[k] else 1.0) * 1.001 * mu_star
        out["negative_found_just_above_mu_star"] += int(minspecies(c2) < 0)
        out["trials"] += 1
    return out


def random_Y(rng, p, n=NB):
    a = rng.normal(size=(p, n)); B = rng.normal(size=(p, n, n)) * 0.5
    gam = rng.normal(size=p); d = rng.normal(size=(p, n)); dl = rng.normal(size=p) * 0.3; e = rng.normal(size=(p, n))
    def Y(c):
        return a @ c + np.einsum("kij,i,j->k", B, c, c) + gam * np.sin(d @ c) + dl * (e @ c) ** 3
    return Y


def part_C(rng):
    out = {}
    wf = weight_factory(rng)
    M = moment_matrix(wf, "log")
    Q = np.linalg.svd(M)[2][3:].T                            # 11x8 orthonormal basis of V = ker M
    out["moment_residual_basis"] = float(np.abs(M @ Q).max() / np.abs(M).max())
    r = 0.1
    def solve(Y, p, starts):
        best = np.inf
        for _ in range(starts):
            x0 = rng.normal(size=8)
            fun = lambda x: np.concatenate([Y(r * Q @ (x / np.linalg.norm(x))) - Y(-r * Q @ (x / np.linalg.norm(x))),
                                            [np.linalg.norm(x) - 1.0]])
            s = least_squares(fun, x0, xtol=1e-15, ftol=1e-15, gtol=1e-15, max_nfev=4000)
            best = min(best, np.linalg.norm(s.fun[:-1]))
            if best < 1e-13: break
        return best
    for p in [6, 7]:
        found = 0; worst = 0.0
        for _ in range(40):
            Y = random_Y(rng, p)
            b = solve(Y, p, 30)
            found += int(b < 1e-12); worst = max(worst, b)
        out[f"p{p}_maps"] = 40; out[f"p{p}_alias_found_to_1e-12"] = found; out[f"p{p}_worst_residual"] = worst
    # p = 8 threshold: Y = Q^T c + small even nonlinearity -> odd part 2 Q^T c never vanishes on the sphere
    mins = []
    for _ in range(10):
        Yn = random_Y(rng, 8)
        Y = lambda c, Yn=Yn: Q.T @ c + 0.01 * (Yn(c) + Yn(-c))          # nonlinear, but odd part = Q^T c
        mins.append(solve(Y, 8, 20))
    out["p8_injective_type_min_odd_residual"] = float(min(mins)); out["p8_lower_bound_2r"] = 2 * r
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    A = part_A(rng); B = part_B(rng); C = part_C(rng)
    verdict = {
        "A_all_minors_positive_rank3": A["nonpositive_minors"] == 0 and A["min_rank"] == 3 and A["max_rank"] == 3,
        "B_mu_and_mu_star_suffice": B["violations_below_mu"] == 0 and B["violations_below_mu_star"] == 0,
        "B_mu_star_sharp": B["negative_found_just_above_mu_star"] == B["trials"],
        "C_alias_found_p6_p7": C["p6_alias_found_to_1e-12"] == C["p6_maps"] and C["p7_alias_found_to_1e-12"] == C["p7_maps"],
        "C_no_alias_p8_injective_type": C["p8_injective_type_min_odd_residual"] > 1.9 * 0.1,
    }
    res = {"A": A, "B": B, "C": C, "verdict": {k: bool(v) for k, v in verdict.items()}, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "mt14_rot009_borsuk_ulam_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
