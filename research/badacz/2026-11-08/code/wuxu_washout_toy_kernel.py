#!/usr/bin/env python3
"""Badacz (Claude), POST HOC illustration for REVIEW_050 (not part of PREREG_048 verdicts).
Toy wash-out kernel: a hadron injected at time t kicks X_n instantaneously; the kick relaxes with the SM weak rate
lambda(T) = Gamma_np + Gamma_pn, Gamma_np = (1/tau_n)(1 + 253.9 (12+6x+x^2)/x^5), Gamma_pn = e^-x Gamma_np, x = Q/T
(Wu-Xu arXiv:2509.05618v3 Eqs. (B.15)-(B.17)). Radiation era t = 1/(2H), H = 1.66 sqrt(g*) T^2/m_pl, g* = 10.75.
Weight of a hadron emitted at t: w(t) = exp(-int_t^{tau0} lambda dt') (common factors after tau0 cancel in ratios).
Emission history: native hadron table (same interpolation as wuxu_band_number_shares.py), dN ~ R(M) M^2 dM,
t(M) = tau(M0) - tau(M), tau(M) = 0.2376664 s (M/1e9 g)^3 (MT14 ROT025 source clock).
Output: toy W(b) = <w>_b / <w>_all for the PREREG_048 bands, to compare with the native measurement.
Usage: python3 -I wuxu_washout_toy_kernel.py --table hadrons_from_PBH.dat --out toy.json
"""
import argparse, json, math

ap = argparse.ArgumentParser(); ap.add_argument("--table", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
G_GEV = 5.60958860380445e23; TAU_N = 879.4; Q = 1.29333e-3; MPL = 1.22091e19; HBAR = 6.582119569e-25; GSTAR = 10.75
rows = [list(map(float, l.split())) for l in open(a.table) if l.strip() and not l.startswith("m_PBH")]
lm = [math.log(r[0] / G_GEV) for r in rows]; lrt = [math.log(sum(r[1:6])) for r in rows]     # total hadron rate
M_GRID = 1.0572611951580e8; TAU9 = 0.2376664163901
BANDS = {"A": (1e9, math.inf), "B": (3e8, 1e9), "C": (M_GRID, 3e8), "D": (0.0, M_GRID)}


def lnR(x):
    if x <= lm[1]:
        return lrt[0] + (lrt[1] - lrt[0]) / (lm[1] - lm[0]) * (x - lm[0])
    i = max(k for k in range(len(lm) - 1) if lm[k] <= x)
    return lrt[i] + (lrt[i + 1] - lrt[i]) / (lm[i + 1] - lm[i]) * (x - lm[i])


def T_of_t(t):                     # GeV
    return math.sqrt(1 / (2 * t * 1.66 * math.sqrt(GSTAR) / MPL / HBAR))


def lam(t):
    x = Q / T_of_t(t); g = (1 / TAU_N) * (1 + 253.9 * (12 + 6 * x + x * x) / x ** 5); return g * (1 + math.exp(-x))


def Lint(t0, t1, n=400):           # int_t0^t1 lambda dt, log-spaced Simpson in u = ln(t1 - t + eps)? use plain log grid in t
    if t1 <= t0:
        return 0.0
    u0, u1 = math.log(t0), math.log(t1); h = (u1 - u0) / n
    f = lambda u: lam(math.exp(u)) * math.exp(u)
    return h / 3 * (f(u0) + f(u1) + sum((4 if k % 2 else 2) * f(u0 + k * h) for k in range(1, n)))


res = {"note": "POST HOC toy illustration; not a PREREG_048 verdict", "j": {}}
for j in (22, 28, 34, 62):
    M0 = 6e8 * (1e10 / 6e8) ** (j / 99); tau0 = TAU9 * (M0 / 1e9) ** 3
    # integrate over M on a log grid down to 1e-6 M0 (the remainder below is negligible in number)
    n = 6000; xs = [math.log(M0 * 1e-6) + (math.log(M0) - math.log(M0 * 1e-6)) * k / n for k in range(n + 1)]
    acc = {b: [0.0, 0.0] for b in BANDS}; tot = [0.0, 0.0]
    for k, x in enumerate(xs):
        M = math.exp(x); wq = (1 if k in (0, n) else (4 if k % 2 else 2))
        dn = math.exp(lnR(x) + 3 * x) * wq               # R(M) M^2 dM = R M^3 dx
        t = max(tau0 - TAU9 * (M / 1e9) ** 3, 1e-6)
        w = math.exp(-Lint(t, tau0)) if t < tau0 else 1.0
        tot[0] += dn; tot[1] += dn * w
        for b, (lo, hi) in BANDS.items():
            if lo <= M < hi:
                acc[b][0] += dn; acc[b][1] += dn * w
    wbar = tot[1] / tot[0]
    res["j"][str(j)] = {"tau0_s": tau0, "T_at_tau0_MeV": 1e3 * T_of_t(tau0), "lambda_at_tau0_per_s": lam(tau0),
                        "toy_W": {b: (acc[b][1] / acc[b][0]) / wbar if acc[b][0] > 0 else None for b in BANDS},
                        "toy_s_eff": {b: acc[b][1] / tot[1] for b in BANDS}}
    print(j, f"tau0={tau0:.3f}s T={1e3*T_of_t(tau0):.2f}MeV lambda={lam(tau0):.1f}/s", {b: round(v, 3) if v else v for b, v in res["j"][str(j)]["toy_W"].items()})
json.dump(res, open(a.out, "w"), indent=1, sort_keys=True)
