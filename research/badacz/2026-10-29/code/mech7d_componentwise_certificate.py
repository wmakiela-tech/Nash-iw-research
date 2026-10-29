#!/usr/bin/env python3
"""BADACZ (Claude): componentwise (Mueller-Kamke) a posteriori error certificate for the Mech-S7 7D kinetics
(X plus six hadron densities), answering AUD1 ROT005 Gate A ("certified solver errors eps+-").

Structure taken from the PUBLIC Mech-S7 code research/mech-s7/2026-10-23/terminal_7d_exact_mass_common_background_006.py
(rates(), dXdt(), rhs_u(), rhs_post(); constants copied verbatim). The archived Wu-Xu background and PBH density are
NOT public, so the demo uses a SYNTHETIC radiation-era background and synthetic PBH density (see below).

Certificate: e = y - yhat with yhat the continuous piecewise Radau collocation polynomial (dense output); defect
r = yhat' - G(s, yhat). Because G is affine-bilinear (X couples to n_i; D_i is affine in X), each |e_i| obeys
  D+|e_i| <= J_ii |e_i| + sum_{j != i} |J_ij| |e_j| + q_i(|e|) + |r_i|,
with J = DG(yhat) and an explicit quadratic remainder q. The Metzler comparison system eps' = Mbar eps + rhobar is
propagated piece by piece with exact matrix exponentials and piecewise upper bounds of Mbar and rhobar (sampled on
each piece: semi-rigorous, see the report); monotonicity of Metzler systems gives |e| <= eps.
Synthetic background: T(t) = sqrt(1.32/t) MeV, t_edge = 150 s, X_edge = 0.14, nPBH0 = 1e-11 cm^-3.
Also: exact-information source pair +-A k (Gegenbauer class, see exact_information_source_class.py) inserted into the
pbar/nbar sources, both runs certified, and the certified two-point floor (|X+ - X-| - eps+ - eps-)/2 reported.
Synthetic demo only; not Mech's data, not physics. numpy 2.1.3, scipy 1.14.1, sympy 1.13.3.
Run: python3 -I mech7d_componentwise_certificate.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm

# ---------------------------------------------------------------- constants copied from Mech-S7 ROT006 (public)
GAMMA = 4.207579833788249e27
M_EDGE = 1e9; M_CUT = 6e9 * math.exp(-20); U_CUT = M_CUT / M_EDGE
DT_EDGE = M_EDGE ** 3 / GAMMA; T_NUC = .078185270688319950
M1 = 5.609588603804452e32; M2 = 6.099798045788406e32
Q1 = np.array([489105.5126008581, 59105.93631247951, 29086.774913348447, 34849.08026691193, 34656.17773724596])
Q2 = np.array([442306.73787501804, 53467.712852971126, 26311.795859614824, 31504.591028094237, 31328.963561830213])
SLOPES = np.log(Q2 / Q1) / math.log(M2 / M1)
INDEX = np.array([0, 0, 1, 2, 3, 4])
HBAR_GEV_SEC = 6.582119569e-25; C_CMS = 299792458e2; MBARN_CM2 = 1e-27; SIGMA_V_UNIT = MBARN_CM2 * C_CMS
M_P_MEV = 938.27208816; Q_MEV = 939.5654205 - M_P_MEV; TAU_N = 878.4; ALPHA = 1 / 137.035999084
ETA_B = 6.1e-10; ZETA3 = 1.202056903159594; HBARC_MEV_CM = 197.3269804e-13; NSCALE = 1e16
S = NSCALE * SIGMA_V_UNIT
LOSS_SLOPE_FIXED = None   # filled per T because of Coulomb factors


def coulomb(T, m):
    ve = math.sqrt(T / m) + math.sqrt(T / M_P_MEV); z = 2 * math.pi * ALPHA / ve
    return z / (-math.expm1(-z))


def rate_parts(T):
    """returns a, b, decay, loss0, loss1 (loss = loss0 + loss1*X), nB*sigma_v, weak coefficients (g, e^-x)."""
    nB = ETA_B * (2 * ZETA3 / math.pi ** 2) * (T / HBARC_MEV_CM) ** 3
    fp = coulomb(T, 139.57039); fk = coulomb(T, 493.677)
    a = np.array([1.5 * fp, 0, 31 * fk, 7, 0, 28.])
    b = np.array([0, 1.7, 26, 7, 28, 0.])
    decay = np.array([1 / 2.6033e-8, 1 / 2.6033e-8, 8.1e7, 2e7, 0, 0])
    loss0 = np.array([a[0], 0, (31 + 14.5) * fk, 17, 37, 28])
    loss1 = np.array([-a[0], 1.7, (34 + 26) - (31 + 14.5) * fk, 0, 28 - 37, 37 - 28])
    x = Q_MEV / T; g = (255 / TAU_N) * (12 + 6 * x + x * x) / x ** 5
    return a, b, decay, loss0, loss1, nB * SIGMA_V_UNIT, g, math.exp(-x)


def F_and_J(T, y, src):
    """7D RHS F = (X', n') with source src (scaled), and Jacobian. Matches Mech rates()/dXdt() exactly."""
    X = y[0]; n = y[1:]
    a, b, decay, l0, l1, nbs, g, ex = rate_parts(T)
    D = decay + (l0 + l1 * X) * nbs
    weak = g * ((1 - X) * ex - X) - X / TAU_N
    conv = np.sum(n * S * ((1 - X) * a - X * b))
    F = np.concatenate([[weak + conv], src - D * n])
    J = np.zeros((7, 7))
    J[0, 0] = -g * (ex + 1) - 1 / TAU_N - S * np.sum(n * (a + b))
    J[0, 1:] = S * ((1 - X) * a - X * b)
    J[1:, 0] = -l1 * nbs * n
    J[1:, 1:] = np.diag(-D)
    quad = (S * (a + b), np.abs(l1) * nbs)          # q_X <= sum_i quad0_i eps_ni eps_X ; q_ni <= quad1_i eps_X eps_ni
    return F, J, quad


# ---------------------------------------------------------------- synthetic background and sources
T_EDGE_TIME = 150.0     # synthetic: source phase near T ~ 0.094 MeV, as in Mech's late evaporation window
X_EDGE = 0.14           # synthetic frozen-out neutron fraction at the edge


def T_of_t(t):
    return math.sqrt(1.32 / t)


def t_of_u(u):
    return T_EDGE_TIME + DT_EDGE * (1 - u ** 3)


NPBH0 = 1e-11      # synthetic (gives O(1e-2) hadronic shift of X)


def base_src(u):
    t = t_of_u(u)
    nP = NPBH0 * (T_EDGE_TIME / t) ** 1.5
    return Q1[INDEX] * nP / HBAR_GEV_SEC * u ** SLOPES[INDEX] / NSCALE


# exact-information perturbation of pbar (index 4) / nbar (index 5): u^3 dQp = A k(x)
Lz = math.log(0.92 / 0.07); ZM = 0.5 * (math.log(0.07) + math.log(0.92))
_x = sp.symbols("x")
KL = [np.poly1d([float(c) for c in sp.Poly(sp.expand((1 - _x ** 2) ** 4 * sp.gegenbauer(l, sp.Rational(9, 2), _x)), _x).all_coeffs()])
      for l in range(3, 11)]
DIRECTION = np.zeros(8); DIRECTION[0] = 1.0       # coefficients a_l on k_3..k_10 (set in main)


def kfun(x):
    return sum(a * p(x) for a, p in zip(DIRECTION, KL) if a != 0)


def delta_src(u, amp):
    """u^3 * delta(u) = amp * scale * k(x): the u^3-weighted comoving moments of delta vanish exactly."""
    if u <= 0.07 or u >= 0.92:
        return 0.0
    x = 2 * (math.log(u) - ZM) / Lz
    nP = NPBH0 * (T_EDGE_TIME / t_of_u(u)) ** 1.5          # same PBH density factor as the base source
    return amp * Q1[3] * kfun(x) / u ** 3 * nP / HBAR_GEV_SEC / NSCALE


def src_u(u, amp):
    s = base_src(u).copy(); d = delta_src(u, amp)
    s[4] += d; s[5] -= d
    return s


# phase A in s = -u (increasing): dy/ds = 3*DT*u^2 * F(t(u), y; src(u))
def GA(s, y, amp):
    u = -s; T = T_of_t(t_of_u(u)); F, J, q = F_and_J(T, y, src_u(u, amp)); c = 3 * DT_EDGE * u * u
    return c * F, c * J, (c * q[0], c * q[1])


def GB(t, y, amp):
    F, J, q = F_and_J(T_of_t(t), y, np.zeros(6))
    return F, J, q


def solve(phase, y0, span, amp, rtol, atol_factor=1e-3):
    fun = (lambda s, y: GA(s, y, amp)[0]) if phase == "A" else (lambda t, y: GB(t, y, amp)[0])
    jac = (lambda s, y: GA(s, y, amp)[1]) if phase == "A" else (lambda t, y: GB(t, y, amp)[1])
    return solve_ivp(fun, span, y0, method="Radau", rtol=rtol, atol=rtol * atol_factor, jac=jac,
                     max_step=(.02 if phase == "A" else 2.), dense_output=True)


def certify(phase, sol, amp, eps0, sub=6, samples=5):
    """componentwise Metzler comparison along the Radau collocation polynomials (continuous, piecewise C^1);
    returns eps at the end and diagnostics."""
    G = (lambda s, y: GA(s, y, amp)) if phase == "A" else (lambda t, y: GB(t, y, amp))
    eps = np.array(eps0, float)
    max_def = np.zeros(7); logL = 0.0; worst_mu_inf = -np.inf; nseg = 0
    for itp in sol.sol.interpolants:
        nseg += 1
        h = itp.h; Q = itp.Q; yo = itp.y_old; order = Q.shape[1]
        for m in range(sub):
            a0, a1 = m / sub, (m + 1) / sub
            Mbar = None; rho = np.zeros(7); qx = None; qn = None
            for th in np.linspace(a0, a1, samples):
                pw = th ** np.arange(1, order + 1)
                dpw = np.arange(1, order + 1) * th ** np.arange(0, order) / h
                yh = yo + Q @ pw
                dyh = Q @ dpw
                Fv, Jv, qv = G(itp.t_old + th * h, yh)
                r = np.abs(dyh - Fv)
                Mv = np.abs(Jv); np.fill_diagonal(Mv, np.diag(Jv))
                Mbar = Mv if Mbar is None else np.maximum(Mbar, Mv)
                rho = np.maximum(rho, r)
                qx = qv[0] if qx is None else np.maximum(qx, qv[0]); qn = qv[1] if qn is None else np.maximum(qn, qv[1])
                logL = max(logL, np.abs(Jv).sum(axis=1).max())
                worst_mu_inf = max(worst_mu_inf, max(Jv[i, i] + np.abs(Jv[i]).sum() - abs(Jv[i, i]) for i in range(7)))
            max_def = np.maximum(max_def, rho)
            hh = (a1 - a0) * h
            ebar = eps * 2 + 1e-300
            for _ in range(5):                       # bootstrap the quadratic remainder
                Mq = Mbar.copy()
                Mq[0, 1:] += qx * ebar[0]; Mq[1:, 1:] += np.diag(qn * ebar[0])
                Aug = np.zeros((8, 8)); Aug[:7, :7] = Mq; Aug[:7, 7] = rho
                E = expm(Aug * hh)
                new = E[:7, :7] @ eps + E[:7, 7]
                if np.all(new <= ebar):
                    break
                ebar = np.maximum(ebar, 2 * new)
            assert np.all(new <= ebar * (1 + 1e-12)), "bootstrap failed"
            eps = new
    return eps, {"max_defect": max_def.tolist(), "max_row_abs_sum_J(Lipschitz_inf)": float(logL),
                 "max_mu_inf(J)": float(worst_mu_inf), "segments": nseg, "sub": sub, "samples_per_piece": samples}


def run_pair(amp, rtol):
    y0 = np.zeros(7); y0[0] = X_EDGE
    solA = solve("A", y0, (-1.0, -U_CUT), amp, rtol)
    t_cut = t_of_u(U_CUT); t_eval = 1.32 / T_NUC ** 2
    solB = solve("B", solA.y[:, -1], (t_cut, t_eval), amp, rtol)
    return solA, solB, t_cut, t_eval


def positivity_amp(target_ratio):
    us = np.exp(np.linspace(math.log(0.0701), math.log(0.9199), 20001))
    ratio = max(abs(delta_src(u, 1.0)) / min(base_src(u)[4], base_src(u)[5]) for u in us)
    return target_ratio / ratio


def X_nuc(amp, rtol=3e-9):
    solA, solB, _, _ = run_pair(amp, rtol)
    return float(solB.y[0, -1])


def main():
    global DIRECTION
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    # 1) linear response of X_nuc to each exact-class basis function (finite differences at 5% positivity load)
    X0 = X_nuc(0.0)
    resp = np.zeros(8)
    for l in range(8):
        DIRECTION = np.eye(8)[l]
        a = positivity_amp(0.05)
        resp[l] = (X_nuc(a) - X_nuc(-a)) / (2 * a)
    # 2) gradient direction (Euclidean in a_l) and amplitude at 50% positivity load
    DIRECTION = resp / np.linalg.norm(resp)
    amp = positivity_amp(0.5)
    res = {"synthetic": {"T(t)": "sqrt(1.32/t) MeV", "t_edge": T_EDGE_TIME, "X_edge": X_EDGE, "nPBH0": NPBH0, "amp": amp,
                         "max|delta|/min(src_pbar,src_nbar)": 0.5, "direction_a_l(l=3..10)": DIRECTION.tolist(),
                         "linear_response_per_unit_amp": resp.tolist(), "X_nuc_baseline": X0}}
    rows = {}
    for sgn in (+1, -1):
        solA, solB, t_cut, t_eval = run_pair(sgn * amp, 3e-9)
        refA, refB, _, _ = run_pair(sgn * amp, 1e-13)
        epsA, infA = certify("A", solA, sgn * amp, np.zeros(7))
        epsB, infB = certify("B", solB, sgn * amp, epsA)
        X = float(solB.y[0, -1]); Xref = float(refB.y[0, -1])
        LdtA = infA["max_row_abs_sum_J(Lipschitz_inf)"] * (1 - U_CUT); LdtB = infB["max_row_abs_sum_J(Lipschitz_inf)"] * (t_eval - t_cut)
        rows[sgn] = {"X_nuc_rtol3e-9": X, "X_nuc_ref_rtol1e-13": Xref, "actual_error": abs(X - Xref),
                     "certified_eps_X": float(epsB[0]), "certified_eps_all": epsB.tolist(),
                     "eps_after_phase_A": epsA.tolist(), "phaseA": infA, "phaseB": infB,
                     "log10_Lipschitz_Gronwall_factor_upper": float((LdtA + LdtB) / math.log(10))}
    # sensitivity of the certificate to the sampling density (semi-rigour check), + run only
    solA, solB, _, _ = run_pair(amp, 3e-9)
    eA2, _ = certify("A", solA, amp, np.zeros(7), sub=12, samples=9)
    eB2, _ = certify("B", solB, amp, eA2, sub=12, samples=9)
    floor = (abs(rows[1]["X_nuc_rtol3e-9"] - rows[-1]["X_nuc_rtol3e-9"]) - rows[1]["certified_eps_X"] - rows[-1]["certified_eps_X"]) / 2
    res.update({"runs": {str(k): v for k, v in rows.items()},
                "half_gap_numeric": abs(rows[1]["X_nuc_rtol3e-9"] - rows[-1]["X_nuc_rtol3e-9"]) / 2,
                "certified_two_point_floor": floor,
                "denser_sampling_eps_X_plus_run": float(eB2[0])})
    res["verdict"] = {
        "certificate_covers_actual_error": all(r["certified_eps_X"] >= r["actual_error"] for r in rows.values()),
        "certified_floor_positive": floor > 0,
        "lipschitz_gronwall_useless": all(r["log10_Lipschitz_Gronwall_factor_upper"] > 100 for r in rows.values()),
        "sampling_stable_within_factor_2": 0.5 <= res["denser_sampling_eps_X_plus_run"] / rows[1]["certified_eps_X"] <= 2,
    }
    res["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (out / "mech7d_componentwise_certificate.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
