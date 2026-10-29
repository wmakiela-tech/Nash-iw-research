#!/usr/bin/env python3
"""Independent cross-family checks (Badacz, Claude thread) of
  (A) M14 ROT016: unknown-centre triple Lorentz, 5-tone Fisher fold and 6-tone repair (exact SymPy + mpmath 60 digits);
  (B) MT14 ROT013: robust-ball criterion d > 2 eps and eps* bracket, tightened with REVIEW_027's m_B bracket.
Model (A), from the public M14 ROT016 report: K(t) = 1/(t^2 + 1/2), m(x) = beta - (a+q)K(x-u+d) - (2g-2a)K(x-u)
- (a-q)K(x-u-d), base u = q = 0, a = g/2. Scores at the base: Q(x) = dm/dq = K(x-d) - K(x+d),
U(x) = dm/du = (g/2)K'(x+d) + g K'(x) + (g/2)K'(x-d); even block (beta, g, a) evaluated on tones 0, 1, 2.
Run: python3 -I m14_rot016_mt14_rot013_exact_checks.py --out <file.json>
"""
import argparse, json
import sympy as sp
from mpmath import mp, mpf, matrix, sqrt

ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); args = ap.parse_args()
d, g, x, z = sp.symbols('d g x z', positive=True)
K = lambda t: 1 / (t ** 2 + sp.Rational(1, 2))
Kp = lambda t: sp.diff(K(x), x).subs(x, t)
Q = lambda X: K(X - d) - K(X + d)
U = lambda X: g / 2 * Kp(X + d) + g * Kp(X) + g / 2 * Kp(X - d)
P = 64 * z ** 5 - 528 * z ** 4 + 2016 * z ** 3 - 832 * z ** 2 - 8172 * z + 729
T = 352 * z ** 5 - 6544 * z ** 4 + 42288 * z ** 3 - 42016 * z ** 2 - 187706 * z + 42237
res = {"A_m14_rot016": {}, "B_mt14_rot013": {}}
A = res["A_m14_rot016"]
for (i, j, poly, name) in [(1, 2, P, "O12_vs_P"), (1, 3, T, "O13_vs_T")]:
    num, den = sp.fraction(sp.together(sp.simplify(U(i) * Q(j) - U(j) * Q(i))))
    qq, rr = sp.div(sp.expand(num), sp.expand(poly.subs(z, d ** 2)), d)
    A[name] = {"exactly_divisible": bool(sp.simplify(rr) == 0), "cofactor": str(sp.factor(qq)),
               "denominator": str(sp.factor(den))}
A["gcd_P_T"] = str(sp.gcd(P, T))
roots = [r for r in sp.real_roots(P) if 0 < r < 1]
A["P_roots_z_in_(0,1)"] = [str(sp.N(r, 20)) for r in roots]
A["dstar"] = str(sp.N(sp.sqrt(roots[0]), 20)) if roots else None
A["dstar_bracket_.29761682_.29761684"] = [bool(P.subs(z, sp.Rational(29761682, 10 ** 8) ** 2) > 0),
                                          bool(P.subs(z, sp.Rational(29761684, 10 ** 8) ** 2) < 0)]
A["Pprime_bound_on_[0,1]"] = "P'(z) = 320z^4 - 2112z^3 + 6048z^2 - 1664z - 8172 <= 320 + 6048 - 8172 = -1804"
M = sp.Matrix([[1, -2 * K(X), -K(X + d) - K(X - d) + 2 * K(X)] for X in [0, 1, 2]])
claimed = -1024 * d ** 2 * (2 * d ** 2 - 5) * (2 * d ** 2 + 5) / (3 * (2 * d ** 2 + 1) * (2 * d ** 2 - 8 * d + 9) * (2 * d ** 2 - 4 * d + 3) * (2 * d ** 2 + 4 * d + 3) * (2 * d ** 2 + 8 * d + 9))
A["even_det_equals_claimed"] = bool(sp.simplify(M.det() / claimed) == 1)

mp.dps = 60


def Ieff(dv, tones=(-2, -1, 0, 1, 2), beta=mpf(3), gv=mpf(7) / 20):
    Kf = lambda t: 1 / (t * t + mpf(1) / 2); Kd = lambda t: -2 * t / (t * t + mpf(1) / 2) ** 2
    a = gv / 2
    F = matrix(5, 5)
    for X in tones:
        X = mpf(X)
        m = beta - a * Kf(X + dv) - (2 * gv - 2 * a) * Kf(X) - a * Kf(X - dv)
        r = [1, -2 * Kf(X), -Kf(X + dv) + 2 * Kf(X) - Kf(X - dv), -Kf(X + dv) + Kf(X - dv),
             a * Kd(X + dv) + (2 * gv - 2 * a) * Kd(X) + a * Kd(X - dv)]
        for i in range(5):
            for j in range(5):
                F[i, j] += r[i] * r[j] / m
    Bm = F[0:4, 0:4]; b = F[0:4, 4]
    return F[4, 4] - (b.T * (Bm ** -1) * b)[0]


A["Ieff5_over_d4"] = {dv: str(Ieff(mpf(dv)) / mpf(dv) ** 4) for dv in ["1e-2", "1e-3", "1e-4", "1e-5"]}
A["claimed_limit_12544/399466485"] = str(mpf(12544) / 399466485)
ds = mpf(str(sp.N(sp.sqrt(roots[0]), 50)))
A["Ieff5_at_dstar"] = str(Ieff(ds)); A["Ieff6_at_dstar"] = str(Ieff(ds, tones=(-2, -1, 0, 1, 2, 3)))
A["Ieff7_at_dstar"] = str(Ieff(ds, tones=(-3, -2, -1, 0, 1, 2, 3)))
A["claimed_Ieff6_Ieff7"] = ["2.23563461214e-8", "7.83201427065e-8"]

B = res["B_mt14_rot013"]
eps = lambda m: sqrt(2 * (1 - sqrt(1 - mpf(m)))) / 2
B["mt14_bracket_from_rot012"] = [str(eps("4.87e-6")), str(eps("4.904e-6"))]
B["claimed"] = ["0.0011034044962", "0.0011072495216"]
B["tightened_with_review027_m_B_[4.90375906e-6, 4.9037590616143884e-6]"] = [str(eps("4.90375906e-6")), str(eps("4.9037590616143884e-6"))]
B["criterion_note"] = ("cones over balls B(u_i, eps) around unit vectors have half-angle arcsin(eps); "
                       "chord d = 2 sin(theta/2); cones meet iff theta/2 <= arcsin(eps) iff d <= 2 eps: "
                       "the ball criterion is unchanged when the positive gain is profiled")
res["verdicts"] = {
    "A_O12_factor_P": A["O12_vs_P"]["exactly_divisible"], "A_O13_factor_T": A["O13_vs_T"]["exactly_divisible"],
    "A_gcd_1": A["gcd_P_T"] == "1", "A_single_root_bracket": len(roots) == 1 and all(A["dstar_bracket_.29761682_.29761684"]),
    "A_even_det": A["even_det_equals_claimed"],
    "A_limit_converges": abs(Ieff(mpf("1e-5")) / mpf("1e-5") ** 4 - mpf(12544) / 399466485) < mpf("1e-10"),
    "A_Ieff5_zero_at_dstar": abs(Ieff(ds)) < mpf("1e-40"),
    "A_Ieff6_matches": abs(Ieff(ds, tones=(-2, -1, 0, 1, 2, 3)) - mpf("2.23563461214e-8")) < mpf("1e-18"),
    "A_Ieff7_matches": abs(Ieff(ds, tones=(-3, -2, -1, 0, 1, 2, 3)) - mpf("7.83201427065e-8")) < mpf("1e-18"),
    "B_bracket_matches": abs(eps("4.87e-6") - mpf("0.0011034044962")) < mpf("1e-13") and abs(eps("4.904e-6") - mpf("0.0011072495216")) < mpf("1e-13"),
}
json.dump(res, open(args.out, "w"), indent=1, sort_keys=True)
print(json.dumps(res["verdicts"], indent=1))
