#!/usr/bin/env python3
"""Badacz (Claude): independent check of Wu-Xu arXiv:2509.05618v3 Appendix B, Eqs. (B.5)-(B.11) (neutron decay matrix element).

Lagrangian (B.5): L = (G_F/sqrt2) [pbar g^mu (gV - gA g5) n] [ebar g_mu (1 - g5) nu]; process n -> p e nubar.
Sum over ALL spins: S = (G_F^2/2) Tr[(pp+mp) g^mu (gV-gA g5)(pn+mn)(gV+gA g5) g^nu] * Tr[(pe+me) g_mu (1-g5) pnu (1+g5) g_nu].
Method 1 (exact): explicit 4x4 Dirac matrices in sympy, on-shell momenta with INTEGER components (Pythagorean quadruples), exact
rational traces, compared with candidate closed forms
   F(s) = (gV+gA)^2 (pn.pnu)(pp.pe) + (gV-gA)^2 (pn.pe)(pp.pnu) + s (gV^2-gA^2) mn mp (pe.pnu),  s = +1 (printed B.6) or -1.
Method 2 (independent of traces): numpy, explicit Dirac spinors u, v for random momenta, |M|^2 summed over the 16 spin states.
Then the nucleon-rest reduction (B.7)-(B.9), the normalization implied by (B.11) line 1 -> line 2, the rate (B.11) with
lambda_0 = 1.636 (B.12), and the beta-nubar correlation a = (gV^2-gA^2)/(gV^2+3gA^2) of each candidate.
Usage: python3 -I wuxu_v3_appendixB_dirac_trace_check.py --out appB.json
"""
import argparse, json, math, random
import numpy as np
import sympy as sp

ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); a = ap.parse_args()
I2, Z2 = sp.eye(2), sp.zeros(2)
sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
def blk(A, B, C, D): return sp.Matrix(sp.BlockMatrix([[A, B], [C, D]]))
g = [blk(I2, Z2, Z2, -I2)] + [blk(Z2, s, -s, Z2) for s in sig]          # Dirac representation
g5 = sp.I * g[0] * g[1] * g[2] * g[3]
eta = sp.diag(1, -1, -1, -1); E4 = sp.eye(4)
def slash(p): return sum((eta[m, m] * p[m] * g[m] for m in range(4)), sp.zeros(4))
def dot(p, q): return p[0] * q[0] - p[1] * q[1] - p[2] * q[2] - p[3] * q[3]
gV, gA, GF = sp.symbols("gV gA GF")

def S_trace(pn, mn, pp, mp, pe, me, pnu):
    H = [[None] * 4 for _ in range(4)]; L = [[None] * 4 for _ in range(4)]
    A = slash(pp) + mp * E4; B = slash(pn) + mn * E4; C = slash(pe) + me * E4; D = slash(pnu)
    for m in range(4):
        for n in range(4):
            H[m][n] = (A * g[m] * (gV * E4 - gA * g5) * B * (gV * E4 + gA * g5) * g[n]).trace()
            L[m][n] = (C * g[m] * (E4 - g5) * D * (E4 + g5) * g[n]).trace()
    tot = sum(H[m][n] * L[m][n] * eta[m, m] * eta[n, n] for m in range(4) for n in range(4))   # contract with lower indices
    return sp.expand(GF**2 / 2 * tot)

def F(s, pn, mn, pp, mp, pe, pnu):
    return sp.expand((gV + gA)**2 * dot(pn, pnu) * dot(pp, pe) + (gV - gA)**2 * dot(pn, pe) * dot(pp, pnu)
                     + s * (gV**2 - gA**2) * mn * mp * dot(pe, pnu))

# integer on-shell momenta (E, px, py, pz); masses m = sqrt(E^2 - |p|^2) kept exact; neutrino massless
def mass(p): return sp.sqrt(p[0]**2 - p[1]**2 - p[2]**2 - p[3]**2)
sets = [((25, 2, 3, 6), (15, 2, 5, 10), (5, 1, 2, 2), (7, 2, 3, 6)),      # mn=24, mp=sqrt96, me=4
        ((13, 3, 4, 0), (17, 1, 2, 2), (3, 1, 2, 2), (13, 3, 4, 12)),      # mn=12, mp=sqrt280, me=0
        ((27, 2, 10, 11), (19, 6, 6, 7), (9, 1, 4, 4), (9, 1, 4, 8))]      # mn=sqrt504, mp=sqrt240, me=sqrt48
exact = []
for (pn, pp, pe, pnu) in sets:
    mn, mp, me = mass(pn), mass(pp), mass(pe)
    pnu_m = mass(pnu)
    assert pnu_m == 0
    S = S_trace(pn, mn, pp, mp, pe, me, pnu)
    r = {}
    for s in (+1, -1):
        for k in (16, 32):
            r[f"S - {k}*GF^2*F(s={s:+d})"] = str(sp.simplify(S - k * GF**2 * F(s, pn, mn, pp, mp, pe, pnu)))
    exact.append({"pn": pn, "pp": pp, "pe": pe, "pnu": pnu, "masses": [str(mn), str(mp), str(me), str(pnu_m)], "residuals": r})
    print("exact set", pn, pp, pe, pnu, "masses", mn, mp, me, pnu_m)
    for kk, v in r.items(): print("   ", kk, "=", v)

# Method 2: explicit spinors, numerical sum over 16 spin states
gn = [np.array(m.evalf(), dtype=complex) for m in g]; g5n = np.array(g5.evalf(), dtype=complex)
def u_sp(p, m, s):
    E = p[0]; pv = np.array(p[1:]); chi = np.array([1, 0] if s == 0 else [0, 1], dtype=complex)
    sp_ = sum(pv[i] * np.array(sig[i].evalf(), dtype=complex) for i in range(3))
    return np.concatenate([math.sqrt(E + m) * chi, (sp_ @ chi) / math.sqrt(E + m)])
def v_sp(p, m, s):
    E = p[0]; pv = np.array(p[1:]); chi = np.array([0, 1] if s == 0 else [1, 0], dtype=complex)
    sp_ = sum(pv[i] * np.array(sig[i].evalf(), dtype=complex) for i in range(3))
    return np.concatenate([(sp_ @ chi) / math.sqrt(E + m), math.sqrt(E + m) * chi])
def bar(x): return x.conj() @ gn[0]
def onshell(m, rng):
    v = np.array([rng.gauss(0, 1) for _ in range(3)]) * rng.uniform(0.1, 3); return np.array([math.sqrt(m * m + v @ v), *v])
def dotn(p, q): return p[0] * q[0] - p[1:] @ q[1:]
rng = random.Random(20261108); num = []
for t in range(5):
    gv, ga = 1.0, rng.uniform(0.8, 1.6); mn_, mp_, me_ = 1.3, 1.1, 0.2
    pn, pp, pe, pnu = onshell(mn_, rng), onshell(mp_, rng), onshell(me_, rng), onshell(0.0, rng)
    tot = 0.0
    for sn in (0, 1):
        for spp in (0, 1):
            for se in (0, 1):
                for snu in (0, 1):
                    up, un, ue, vn = u_sp(pp, mp_, spp), u_sp(pn, mn_, sn), u_sp(pe, me_, se), v_sp(pnu, 0.0, snu)
                    Mval = sum(eta[m, m] * (bar(up) @ gn[m] @ (gv * np.eye(4) - ga * g5n) @ un) *
                               (bar(ue) @ gn[m] @ (np.eye(4) - g5n) @ vn) for m in range(4)) / math.sqrt(2)
                    tot += abs(Mval)**2
    Fm = (gv + ga)**2 * dotn(pn, pnu) * dotn(pp, pe) + (gv - ga)**2 * dotn(pn, pe) * dotn(pp, pnu)
    Fx = (gv**2 - ga**2) * mn_ * mp_ * dotn(pe, pnu)
    num.append({"S_over_GF2": tot, "ratio_to_32F_minus": tot / (32 * (Fm - Fx)), "ratio_to_32F_plus": tot / (32 * (Fm + Fx))})
    print("spinor sum", t, "S/(32 F_-) =", tot / (32 * (Fm - Fx)), " S/(32 F_+) =", tot / (32 * (Fm + Fx)))

# Reduction at nucleon rest (B.7)-(B.8): pn = pp = (m,0); pe.pnu = Ee Enu - D
m_, Ee, En, Dv = sp.symbols("m Ee Enu D", positive=True)
red = {}
for s in (+1, -1):
    expr = (gV + gA)**2 * (m_ * En) * (m_ * Ee) + (gV - gA)**2 * (m_ * Ee) * (m_ * En) + s * (gV**2 - gA**2) * m_**2 * (Ee * En - Dv)
    red[f"s={s:+d}"] = str(sp.factor(sp.collect(sp.expand(expr / m_**2), [Ee * En, Dv])))
printed_B9 = sp.expand((gV**2 + 3 * gA**2) * Ee * En + (gV**2 - gA**2) * Dv)
red["matches_printed_B9"] = {f"s={s:+d}": bool(sp.expand(((gV + gA)**2 + (gV - gA)**2) * Ee * En + s * (gV**2 - gA**2) * (Ee * En - Dv)) == printed_B9) for s in (+1, -1)}
print("reduction:", red)

# Normalization: (B.11) line 1 -> line 2 needs |Mbar|^2 = 2 GF^2 mp^2 [bracket] (all-spin average, g_p g_nu g_e in dPi);
# all-spin average of S = 32 GF^2 F is 32/16 = 2 GF^2 F. Printed (B.6)/(B.9) prefactor 1/2^4 * GF^2 = GF^2/16.
# Rate (B.11) with g_p g_nu g_e = 8 and lambda_0 (B.12), gV=1, gA=1.3; and with the printed B.6 coefficient (3gV^2+gA^2).
GFv, me_GeV, hbar = 1.1663787e-5, 0.51099895e-3, 6.582119569e-25
Q = 1.29333236e-3
lam0 = sum(((Q - math.sqrt(x * x + me_GeV**2))**2 * x * x) for x in np.linspace(0, math.sqrt(Q * Q - me_GeV**2), 200001)[1:-1]) * (math.sqrt(Q * Q - me_GeV**2) / 200000) / me_GeV**5
rate = lambda gva2: 8 * GFv**2 * gva2 * me_GeV**5 * lam0 / (16 * math.pi**3) / hbar
res = {"source": "arXiv:2509.05618v3 Appendix B (read via alphaXiv PDF text, 2026-11-08)",
       "exact_trace_residuals": exact, "spinor_sum": num, "nucleon_rest_reduction": red,
       "lambda0_numeric": lam0,
       "tau_n_B11_s": {"gV2+3gA2 (printed B.9, s=-1 form)": 1 / rate(1 + 3 * 1.3**2), "3gV2+gA2 (printed B.6 reduced, s=+1)": 1 / rate(3 + 1.3**2)},
       "beta_nubar_correlation_a": {"s=-1 (B.9)": (1 - 1.3**2) / (1 + 3 * 1.3**2), "s=+1 (B.6 reduced)": -(1 - 1.3**2) / (3 + 1.3**2),
                                    "lambda=1.2754 s=-1": (1 - 1.2754**2) / (1 + 3 * 1.2754**2)},
       "normalization": {"all_spin_sum_coefficient": 32, "all_spin_average_coefficient": 2, "printed_prefactor": "1/2^4 = 0.0625",
                         "implied_by_B11_line2": 2}}
json.dump(res, open(a.out, "w"), indent=1, sort_keys=True, default=str)
print("lambda0 =", lam0, " tau(B.9 form) =", res["tau_n_B11_s"], " a:", res["beta_nubar_correlation_a"])
