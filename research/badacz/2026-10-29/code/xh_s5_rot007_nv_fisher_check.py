#!/usr/bin/env python3
"""BADACZ (Claude): cross-family check of XH-S5 ROT007 (two-tone Lorentzian ODMR toy: Fisher information with common
gain / offset, centre-drift alias, sign control) and the gain+offset fibre (cross-check of M14 ROT010 item 2).
  X1  exact rational checks (f(a), f'(a), J = 1881800/103, weighted orthogonality of gain and offset scores,
      CR sd, alias witness, reference-calibrated bound), centre sign alias, Bhattacharyya affinity (closed form vs
      PMF sums), PSN optimum offsets, 16N limit at C = 1.
  X2  Monte Carlo of a ratio estimator under a common lognormal gain with E[g] = N (own implementation).
  X3  gain + offset unknown: explicit fibre g(d) = 2(m1 - m2)/(f(a+d) - f(a-d)), b(d) = m1 - g f(a+d)/2 gives
      identical means for every d with g(d) > 0 (exact rationals); efficient information J_eff(d) for
      gain-only (continuous, positive) and for gain+offset (zero for every d != 0, J at d = 0).
  X4  M14 ROT010 example (u = .16, (g, b) = (4000, 1000) -> u = .17) recomputed from the fibre formula.
Synthetic mathematics only (no source device data). numpy 2.1.3, scipy 1.14.1; seed 20261029.
Run: python3 -I xh_s5_rot007_nv_fisher_check.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.stats import poisson

SEED = 20261029


def f_fr(x, C):
    return 1 - C / (1 + 4 * x * x)


def fp_fr(x, C):
    return C * 8 * x / (1 + 4 * x * x) ** 2


def means(delta, g, b, a, C, e=0):
    """two tones at -a, +a; mu_i = (g/2) f(x_i - delta - e) + b."""
    return [g / 2 * f_fr(-a - delta - e, C) + b, g / 2 * f_fr(a - delta - e, C) + b]


def part_X1():
    C, a, N = Fr(97, 100), Fr(1, 2), Fr(10000)
    out = {"f(a)": str(f_fr(a, C)), "f'(a)": str(fp_fr(a, C))}
    mu = [N / 2 * f_fr(x, C) for x in (-a, a)]
    s_d = [-N / 2 * fp_fr(x, C) for x in (-a, a)]                # d mu / d delta
    s_g = [m for m in mu]                                         # g * d mu/dg (log-gain score)
    s_b = [1, 1]
    ip = lambda u, v: sum(ui * vi / mi for ui, vi, mi in zip(u, v, mu))
    J = ip(s_d, s_d)
    out.update({"mu": [str(m) for m in mu], "score_delta": [str(s) for s in s_d], "J": str(J),
                "J_equals_1881800/103": J == Fr(1881800, 103), "<s_d,s_g>": str(ip(s_d, s_g)), "<s_d,s_b>": str(ip(s_d, s_b)),
                "CR_sd": float(1 / np.sqrt(float(J)))})
    # alias delta+e
    out["alias_witness_equal_means"] = means(Fr(1, 100), N, 0, a, C, Fr(2, 100)) == means(Fr(-4, 100), N, 0, a, C, Fr(7, 100))
    se = Fr(2, 100)
    out["ref_bound_sd"] = float(np.sqrt(float(1 / J + se ** 2))); out["ref_ratio"] = out["ref_bound_sd"] / out["CR_sd"]
    # centre sign alias at C = 1, one tone with the whole budget
    out["centre_mean_C1"] = float(N * f_fr(Fr(1, 100), Fr(1))); out["centre_sign_alias_exact"] = f_fr(Fr(1, 100), C) == f_fr(Fr(-1, 100), C)
    # Bhattacharyya affinity of the two-tone joint law, delta = +-0.01
    lp = [float(m) for m in means(Fr(1, 100), N, 0, a, C)]; lm = [float(m) for m in means(Fr(-1, 100), N, 0, a, C)]
    closed = float(np.exp(-0.5 * sum((np.sqrt(x) - np.sqrt(y)) ** 2 for x, y in zip(lp, lm))))
    k = np.arange(0, 6000)
    pmf = 1.0
    for x, y in zip(lp, lm):
        pmf *= float(np.sum(np.sqrt(poisson.pmf(k, x) * poisson.pmf(k, y))))
    out.update({"bhattacharyya_closed": closed, "bhattacharyya_pmf": pmf})
    # PSN optimum of f'(x)^2/f(x) and the 16N limit at C = 1
    for Cv in (0.05, 0.97):
        r = minimize_scalar(lambda x: -(8 * Cv * x / (1 + 4 * x * x) ** 2) ** 2 / (1 - Cv / (1 + 4 * x * x)), bounds=(1e-6, 2), method="bounded",
                            options={"xatol": 1e-12})
        out[f"psn_opt_x_C{Cv}"] = float(r.x)
    out["C1_q_at_x=1e-4"] = float(16 / (1 + 4e-8) ** 3)
    return out


def part_X2(rng):
    C, a, N, sig = 0.97, 0.5, 10000, 0.25
    f = lambda x: 1 - C / (1 + 4 * x * x)
    # ratio R(delta) = mu_- / mu_+ = f(a + delta)/f(a - delta); invert by Newton around 0
    n_rep = 120000
    g = N * np.exp(sig * rng.normal(size=n_rep) - sig ** 2 / 2)          # E[g] = N
    n1 = rng.poisson(g / 2 * f(-a)); n2 = rng.poisson(g / 2 * f(a))
    r = n1 / n2
    d = np.zeros(n_rep)
    for _ in range(30):
        F = f(a + d) / f(a - d) - r
        dF = (8 * C * (a + d) / (1 + 4 * (a + d) ** 2) ** 2) / f(a - d) + f(a + d) * (8 * C * (a - d) / (1 + 4 * (a - d) ** 2) ** 2) / f(a - d) ** 2
        d = d - F / dF
    J = N * (8 * C * a / (1 + 4 * a * a) ** 2) ** 2 / f(a)
    return {"mc_sd": float(d.std()), "leading_order_sd": float(np.sqrt(np.exp(sig ** 2) / J)), "mc_mean": float(d.mean())}


def fibre(delta0, g0, b0, a, C, d):
    m1, m2 = means(delta0, g0, b0, a, C)
    g = 2 * (m1 - m2) / (f_fr(a + d, C) - f_fr(a - d, C))
    b = m1 - g / 2 * f_fr(a + d, C)
    return g, b


def J_eff(delta, g, b, a, C, nuis):
    """efficient information for delta with nuisances in nuis (subset of 'g','b'), two Poisson channels."""
    x = [-a - delta, a - delta]
    mu = [g / 2 * (1 - C / (1 + 4 * xi * xi)) + b for xi in x]
    sd = np.array([-g / 2 * (8 * C * xi / (1 + 4 * xi * xi) ** 2) for xi in x])
    cols = {"g": np.array([0.5 * (1 - C / (1 + 4 * xi * xi)) for xi in x]), "b": np.array([1.0, 1.0])}
    W = np.diag(1 / np.array(mu))
    if not nuis:
        return float(sd @ W @ sd)
    Nm = np.column_stack([cols[k] for k in nuis])
    Inn = Nm.T @ W @ Nm; Ind = Nm.T @ W @ sd
    return float(sd @ W @ sd - Ind @ np.linalg.pinv(Inn, rcond=1e-13) @ Ind)


def part_X3():
    C, a = Fr(97, 100), Fr(1, 2)
    out = {}
    exact = True
    for delta0 in (Fr(1, 100), Fr(1, 10), Fr(-3, 20)):
        m = means(delta0, Fr(10000), Fr(300), a, C)
        for d in (delta0 * Fr(1, 2), delta0 * Fr(3, 2), delta0 * 2):
            g, b = fibre(delta0, Fr(10000), Fr(300), a, C, d)
            exact &= (means(d, g, b, a, C) == m) and g > 0
    out["fibre_identical_means_exact_rational"] = bool(exact)
    out["fibre_example_delta0=0.1_d=0.2"] = [float(x) for x in fibre(Fr(1, 10), Fr(10000), Fr(300), a, C, Fr(1, 5))]
    rows = []
    J0 = J_eff(0.0, 10000, 0, 0.5, 0.97, [])
    for dl in (0.0, 0.01, 0.05, 0.1, 0.2):
        rows.append({"delta": dl, "J_known/J0": J_eff(dl, 10000, 0, 0.5, 0.97, []) / J0,
                     "J_eff_gain/J0": J_eff(dl, 10000, 0, 0.5, 0.97, ["g"]) / J0,
                     "J_eff_gain_offset/J0": J_eff(dl, 10000, 300, 0.5, 0.97, ["g", "b"]) / J_eff(dl, 10000, 300, 0.5, 0.97, [])})
    out["J_eff_table"] = rows
    return out


def part_X4():
    # M14 convention: mu_{-a} = (g/2) f(a+u) + b, mu_{+a} = (g/2) f(a-u) + b  (u = delta + e)
    C, a = Fr(97, 100), Fr(1, 2)
    g, b = fibre(Fr(16, 100), Fr(4000), Fr(1000), a, C, Fr(17, 100))
    return {"g_alt": float(g), "b_alt": float(b), "m14_reported": [3767.4071306, 1062.4826807]}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    X1 = part_X1(); X2 = part_X2(rng); X3 = part_X3(); X4 = part_X4()
    t = X3["J_eff_table"]
    verdict = {
        "X1_exact": X1["J_equals_1881800/103"] and X1["<s_d,s_g>"] == "0" and X1["<s_d,s_b>"] == "0" and X1["f(a)"] == "103/200"
                    and X1["f'(a)"] == "97/100" and abs(X1["CR_sd"] - 0.0073982990) < 1e-9 and X1["alias_witness_equal_means"]
                    and abs(X1["ref_bound_sd"] - 0.02132451238) < 1e-10 and abs(X1["centre_mean_C1"] - 3.99840063974) < 1e-9
                    and abs(X1["bhattacharyya_closed"] - 0.401018305184) < 1e-10 and abs(X1["bhattacharyya_pmf"] - X1["bhattacharyya_closed"]) < 1e-9
                    and abs(X1["psn_opt_x_C0.05"] - 0.2868125165) < 1e-7 and abs(X1["psn_opt_x_C0.97"] - 0.1504150546) < 1e-7,
        "X2_mc_close_to_leading_order": abs(X2["mc_sd"] / X2["leading_order_sd"] - 1) < 0.01,
        "X3_fibre_and_discontinuity": X3["fibre_identical_means_exact_rational"] and abs(t[0]["J_eff_gain_offset/J0"] - 1) < 1e-9
                    and all(r["J_eff_gain_offset/J0"] < 1e-8 for r in t[1:]) and all(r["J_eff_gain/J0"] > 0.5 for r in t),
        "X4_m14_example": abs(X4["g_alt"] - 3767.4071306) < 1e-6 and abs(X4["b_alt"] - 1062.4826807) < 1e-6,
    }
    res = {"X1": X1, "X2": X2, "X3": X3, "X4": X4, "verdict": verdict, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "xh_s5_rot007_nv_fisher_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
