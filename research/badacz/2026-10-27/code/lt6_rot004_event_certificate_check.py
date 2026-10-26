#!/usr/bin/env python3
"""Cross-family check (Claude -> GPT cell LT6) of
research/lt6/2026-10-26/IW_LT6_ROT004_EVENT_ALIGNED_A_POSTERIORI_CERTIFICATE_001_20261026.md

Written independently of the author's script (not read). Four parts:
  A  exact (SymPy): 1D event example, boundary term, grazing guard, and an exact witness that the
     computable (numerical-side) variant of the event bound needs constant sign for piecewise-C1 xhat.
  B  reproduction of the author's synthetic numbers from the public text, plus computable variants.
  C  random falsification of the two inequalities (event time, event observable) with
       V1: m, F taken on the TRUE trajectory (author's statement),
       V2: mhat, Fhat taken on the NUMERICAL trajectory (orientation of LT5 eq. 2.2),
     and soundness of a computable first-crossing certificate built only from (f, x0, xhat, phi).
  D  random check of the event-time derivative and of the boundary term of an integral target.
Run: python3 lt6_rot004_event_certificate_check.py --out <dir>
Versions used: numpy 2.1.3, scipy 1.14.1, sympy 1.13.3. Seed 20261026.
Grid-based sup/inf are NOT interval-rigorous; this is a falsification attempt, not a proof.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq

SEED = 20261026


# ----------------------------------------------------------------------------- Part A (exact)
def part_A():
    e, t = sp.symbols("epsilon t", real=True)
    out = {}
    x = e + (1 - e) * sp.exp(-t)                       # x' = -x + eps, x(0) = 1
    assert sp.simplify(sp.diff(x, t) - (-x + e)) == 0
    tau = sp.log((1 - e) / (sp.Rational(1, 2) - e))
    assert sp.simplify(x.subs(t, tau) - sp.Rational(1, 2)) == 0
    J = sp.integrate(x, (t, 0, tau))                   # target integrand L = x
    out["J_minus_(1/2+eps*tau)"] = str(sp.simplify(J - (sp.Rational(1, 2) + e * tau)))
    Jp0 = sp.simplify(sp.diff(J, e).subs(e, 0))
    z = sp.diff(x, e)                                  # z = dx/deps
    fixed = sp.simplify(sp.integrate(z.subs(e, 0), (t, 0, tau.subs(e, 0))))
    taup_formula = sp.simplify((-(z) / (-x + e)).subs(t, tau).subs(e, 0))  # -(phi_x z + phi_e)/(phi_t + phi_x f)
    taup_direct = sp.simplify(sp.diff(tau, e).subs(e, 0))
    out.update({"Jprime0": str(Jp0), "fixed_time_derivative": str(fixed),
                "boundary_term": str(sp.simplify(Jp0 - fixed)),
                "tau_prime0_formula": str(taup_formula), "tau_prime0_direct": str(taup_direct)})
    assert sp.simplify(Jp0 - sp.log(2)) == 0 and sp.simplify(fixed - (sp.log(2) - sp.Rational(1, 2))) == 0
    assert sp.simplify(taup_formula - taup_direct) == 0
    # grazing: (t-1)^2 = eps, first crossing tau = 1 - sqrt(eps)
    tg = 1 - sp.sqrt(e)
    out["grazing_dtau_deps"] = str(sp.diff(tg, e))
    out["grazing_unbounded_at_0+"] = bool(sp.limit(sp.diff(tg, e), e, 0, "+") == -sp.oo)
    # V2 sign witness (exact rationals): true x = 1/2 - mu (t - tau), guard x = 1/2, tau = 9/10;
    # xhat = 1/2 + |t - 1| - 1/10 on I = [9/10, 11/10] (piecewise C1, |xhat'| = 1 a.e., sign flips at 1).
    mu, tau0 = sp.Rational(1, 10), sp.Rational(9, 10)
    xt = sp.Rational(1, 2) - mu * (t - tau0)
    xh = sp.Rational(1, 2) + sp.Abs(t - 1) - sp.Rational(1, 10)
    diff_pts = [sp.Rational(9, 10), sp.Integer(1), sp.Rational(11, 10)]
    kappa_I = max(abs(sp.nsimplify((xh - xt).subs(t, p))) for p in diff_pts)  # piecewise linear: max at knots
    tau_hat = sp.Rational(11, 10)                      # second root of the numerical guard in I
    assert (xh - sp.Rational(1, 2)).subs(t, tau_hat) == 0
    err = abs(tau_hat - tau0)
    out["V2_sign_witness"] = {"kappa_sup_I": str(kappa_I), "error": str(err),
                              "V2_bound_mhat=1_no_sign_condition": str(kappa_I / 1),
                              "V1_bound_true_m=1/10": str(kappa_I / mu),
                              "V2_violated": bool(err > kappa_I), "V1_holds": bool(err <= kappa_I / mu)}
    return out


# ----------------------------------------------------------------------------- Part B (author numbers)
def part_B():
    eps = 0.08
    x = lambda t: eps + (1 - eps) * np.exp(-t)
    p = lambda t: 0.004 * np.sin(5 * t)
    xh = lambda t: x(t) + p(t)
    tau = np.log((1 - eps) / (0.5 - eps))
    tauh = brentq(lambda t: xh(t) - 0.5, tau - 0.05, tau + 0.05, xtol=1e-15)
    err = abs(tauh - tau)
    m_true = 0.004 / 0.0118186166455                  # implied by the author's direct bound
    b = np.log((1 - eps) / m_true)                     # right end of I implied by m_true
    rsup = np.hypot(0.02, 0.004)                       # r = 0.02 cos5t + 0.004 sin5t
    kap_sup = rsup * (np.exp(b) - 1)                   # Gronwall with sup|r|, L = 1, e0 = 0
    kap_int = quad(lambda s: np.exp(b - s) * abs(0.02 * np.cos(5 * s) + 0.004 * np.sin(5 * s)), 0, b, limit=400)[0]
    # computable variants (no knowledge of x): numerical-side mhat on I and tube m
    I = np.linspace(tau - 0.2, b, 20001)              # any left end <= tauhat with |x'| > m works
    mhat = np.min(np.abs(-0.92 * np.exp(-I) + 0.02 * np.cos(5 * I)))
    m_tube_direct = np.min(xh(I) - 0.004 - eps)       # inf over |y - xhat| <= 0.004 of |-y + eps|
    m_tube_gron = np.min(xh(I) - kap_sup - eps)
    # general observable bound for Q = x^2 + t/2 (L_Qt = 1/2, L_Qx = 2 sup|x| on I, F = sup|x'| on I)
    LQx = 2 * np.max(np.abs(x(I)) + 0.004); F = np.max(np.abs(-x(I) + eps))
    q_general_direct = LQx * 0.004 + (0.5 + F * LQx) * 0.004 / m_true
    return {"tau": tau, "tauhat": tauh, "event_error": err, "author_event_error": 0.00644835308246,
            "implied_m": m_true, "implied_I_right_end": b,
            "direct_bound": 0.004 / m_true, "author_direct_bound": 0.0118186166455,
            "gronwall_sup_r_bound": kap_sup / m_true, "author_gronwall_bound": 0.1035494310814,
            "gronwall_integral_r_bound": kap_int / m_true,
            "Q_error": err / 2, "author_Q_error": 0.00322417654123,
            "Q_guard_specialised_bound": 0.5 * 0.004 / m_true, "author_Q_bound": 0.00590930832274,
            "Q_general_theorem_bound_direct_kappa": q_general_direct,
            "computable_mhat_numerical_side": mhat, "V2_direct_bound": 0.004 / mhat,
            "computable_m_tube_direct": m_tube_direct, "tube_direct_bound": 0.004 / m_tube_direct,
            "computable_m_tube_gronwall": m_tube_gron, "tube_gronwall_bound": kap_sup / m_tube_gron}


# ----------------------------------------------------------------------------- Part C (random bounds)
def make_problem(rng):
    d = int(rng.integers(1, 4))
    A = -0.4 * np.eye(d) + 0.6 * rng.normal(size=(d, d)) / np.sqrt(d)
    C = 0.4 * rng.normal(size=(d, d)); W = rng.normal(size=(d, d))
    sig = 0.5 * rng.normal(size=d); om = rng.uniform(0.5, 3); ps = rng.uniform(0, 2 * np.pi)
    L = np.linalg.norm(A, 2) + np.linalg.norm(C, 2) * np.linalg.norm(W, 2)
    f = lambda t, x: A @ x + C @ np.tanh(W @ x) + sig * np.sin(om * t + ps)
    x0 = rng.normal(size=d)
    a = rng.normal(size=d); beta = rng.normal() * 0.3
    K = int(rng.integers(1, 4))
    dl = [rng.normal(size=d) * 10 ** rng.uniform(-5, -2.5) for _ in range(K)]
    wk = rng.uniform(0.5, 15, size=K); ph = rng.uniform(0, 2 * np.pi, size=K)
    pfun = lambda t: sum(dl[k] * np.sin(wk[k] * t + ph[k]) for k in range(K))
    dpfun = lambda t: sum(dl[k] * wk[k] * np.cos(wk[k] * t + ph[k]) for k in range(K))
    return dict(d=d, A=A, C=C, W=W, L=L, f=f, x0=x0, a=a, beta=beta, p=pfun, dp=dpfun)


def first_root(tgrid, vals, fun):
    s = np.sign(vals)
    idx = np.where(s[:-1] * s[1:] <= 0)[0]
    if idx.size == 0:
        return None
    i = idx[0]
    if vals[i] == 0:
        return tgrid[i]
    return brentq(fun, tgrid[i], tgrid[i + 1], xtol=1e-14)


def part_C(rng, n_inst=300):
    st = {"instances": 0, "skipped": 0,
          "V1_event_viol": 0, "V1_Q_viol": 0, "V2_event_viol": 0, "V2_Q_viol": 0,
          "max_ratio_V1_event_oracle_kappa": 0.0, "max_ratio_V2_event_oracle_kappa": 0.0,
          "max_ratio_V1_Q_oracle_kappa": 0.0,
          "cert_tested": 0, "cert_pass": 0, "cert_false_pass": 0,
          "gronwall_kappa_ge_true_err_viol": 0}
    tol = 1e-9
    while st["instances"] < n_inst:
        P = make_problem(rng)
        T = 2.0
        sol = solve_ivp(P["f"], (0, T), P["x0"], method="DOP853", rtol=1e-12, atol=1e-13, dense_output=True)
        tg = np.linspace(0, T, 8001)
        X = sol.sol(tg).T
        Xh = X + np.array([P["p"](t) for t in tg])
        # guard: choose c0 so the TRUE guard crosses at a random time with good transversality
        tstar = rng.uniform(0.6, 1.6)
        xs = sol.sol(tstar)
        c0 = P["a"] @ xs + P["beta"] * np.sin(tstar)
        H = lambda t: P["a"] @ sol.sol(t) + P["beta"] * np.sin(t) - c0
        Hv = X @ P["a"] + P["beta"] * np.sin(tg) - c0
        Hh = lambda t: P["a"] @ (sol.sol(t) + P["p"](t)) + P["beta"] * np.sin(t) - c0
        Hhv = Xh @ P["a"] + P["beta"] * np.sin(tg) - c0
        tau = first_root(tg, Hv, H)
        if tau is None or tau > T - 0.3:
            st["skipped"] += 1; continue
        dH = lambda t, xx: P["beta"] * np.cos(t) + P["a"] @ P["f"](t, xx)
        w1, w2 = rng.uniform(0.02, 0.25), rng.uniform(0.02, 0.25)
        lo, hi = max(tau - w1, 0.0), min(tau + w2, T)
        Ig = np.linspace(lo, hi, 1501)
        XI = sol.sol(Ig).T; XhI = XI + np.array([P["p"](t) for t in Ig])
        dHtrue = np.array([dH(t, xx) for t, xx in zip(Ig, XI)])
        if np.min(np.abs(dHtrue)) < 0.05 or np.sign(dHtrue).min() != np.sign(dHtrue).max():
            st["skipped"] += 1; continue
        # numerical-side derivative: xhat' = x' + p' = f(t, x) + p'(t)
        dHhat = np.array([P["beta"] * np.cos(t) + P["a"] @ (P["f"](t, xt) + P["dp"](t)) for t, xt in zip(Ig, XI)])
        m_true = np.min(np.abs(dHtrue))
        same_sign_hat = np.sign(dHhat).min() == np.sign(dHhat).max()
        m_hat = np.min(np.abs(dHhat)) if same_sign_hat else 0.0
        # tauhat: exact numerical-guard root in I, or that root plus an offset (r_ev > 0)
        tr = first_root(Ig, np.array([Hh(t) for t in Ig]), Hh)
        if tr is None:
            st["skipped"] += 1; continue
        tauh = tr if rng.random() < 0.5 else float(np.clip(tr + rng.uniform(-0.3, 0.3) * min(w1, w2), lo, hi))
        r_ev = abs(Hh(tauh))
        La = np.linalg.norm(P["a"])
        kap_or = np.max(np.linalg.norm(XhI - XI, axis=1))            # sharpest legal kappa on I
        err = abs(tauh - tau)
        # observable Q = sin(q.x) + alpha t
        q = rng.normal(size=P["d"]); alpha = rng.normal() * 0.5
        Q = lambda t, xx: np.sin(q @ xx) + alpha * t
        LQx, LQt = np.linalg.norm(q), abs(alpha)
        F_true = np.max(np.linalg.norm([P["f"](t, xx) for t, xx in zip(Ig, XI)], axis=1))
        F_hat = np.max(np.linalg.norm([P["f"](t, xt) + P["dp"](t) for t, xt in zip(Ig, XI)], axis=1))
        Qerr = abs(Q(tauh, sol.sol(tauh) + P["p"](tauh)) - Q(tau, sol.sol(tau)))
        b1 = (r_ev + La * kap_or) / m_true
        q1 = LQx * kap_or + (LQt + F_true * LQx) * b1
        st["V1_event_viol"] += int(err > b1 * (1 + tol) + 1e-13)
        st["V1_Q_viol"] += int(Qerr > q1 * (1 + tol) + 1e-13)
        st["max_ratio_V1_event_oracle_kappa"] = max(st["max_ratio_V1_event_oracle_kappa"], err / b1 if b1 > 0 else 0)
        st["max_ratio_V1_Q_oracle_kappa"] = max(st["max_ratio_V1_Q_oracle_kappa"], Qerr / q1 if q1 > 0 else 0)
        if m_hat > 0:
            b2 = (r_ev + La * kap_or) / m_hat
            q2 = LQx * kap_or + (LQt + F_hat * LQx) * b2
            st["V2_event_viol"] += int(err > b2 * (1 + tol) + 1e-13)
            st["V2_Q_viol"] += int(Qerr > q2 * (1 + tol) + 1e-13)
            st["max_ratio_V2_event_oracle_kappa"] = max(st["max_ratio_V2_event_oracle_kappa"], err / b2 if b2 > 0 else 0)
        # Gronwall kappa from the computable residual r = xhat' - f(t, xhat)
        R = np.array([np.linalg.norm(P["f"](t, xt) + P["dp"](t) - P["f"](t, xt + P["p"](t))) for t, xt in zip(tg, X)])
        e0 = np.linalg.norm(P["p"](0.0))
        integrand = np.exp(-P["L"] * tg) * R
        cum = np.concatenate([[0], np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(tg))])
        kapG = np.exp(P["L"] * tg) * (e0 + cum)
        true_err = np.linalg.norm(Xh - X, axis=1)
        st["gronwall_kappa_ge_true_err_viol"] += int(np.any(true_err > kapG * (1 + 1e-6) + 1e-12))
        # computable first-crossing certificate on a bracket chosen from xhat only
        th = first_root(tg, Hhv, Hh)
        if th is not None and 0.1 < th < T - 0.3:
            st["cert_tested"] += 1
            a_, b_ = th - rng.uniform(0.01, 0.2), min(th + rng.uniform(0.01, 0.2), T)
            pre = tg <= a_
            kapGf = lambda t: np.interp(t, tg, kapG)
            no_root_before = np.all(np.abs(Hhv[pre]) > La * kapG[pre]) if pre.any() else True
            ends = (abs(Hh(a_)) > La * kapGf(a_) and abs(Hh(b_)) > La * kapGf(b_) and np.sign(Hh(a_)) != np.sign(Hh(b_)))
            Ib = np.linspace(a_, b_, 801)
            XIb = sol.sol(Ib).T
            # tube transversality: |phi_t + a.f(t,y)| >= |phi_t + a.f(t,xhat)| - |a| L kappa
            dHt = np.array([P["beta"] * np.cos(t) + P["a"] @ P["f"](t, xt + P["p"](t)) for t, xt in zip(Ib, XIb)])
            tube_ok = np.all(np.sign(dHt) == np.sign(dHt[0])) and np.all(np.abs(dHt) > La * P["L"] * kapGf(Ib))
            if no_root_before and ends and tube_ok:
                st["cert_pass"] += 1
                inI = (a_ <= tau <= b_)
                roots_in_I = np.sum(np.sign(Hv[(tg >= a_) & (tg <= b_)][:-1]) * np.sign(Hv[(tg >= a_) & (tg <= b_)][1:]) < 0)
                st["cert_false_pass"] += int(not (inI and roots_in_I == 1))
        st["instances"] += 1
    return st


# ----------------------------------------------------------------------------- Part D (event derivative)
def part_D(rng, n_inst=60):
    res = {"instances": 0, "skipped": 0, "max_rel_err_tau_prime": 0.0, "max_rel_err_J_prime": 0.0,
           "min_rel_size_boundary_term": np.inf}
    while res["instances"] < n_inst:
        P = make_problem(rng); d = P["d"]
        u = rng.normal(size=d); v0 = rng.normal(size=d); gam = rng.normal() * 0.3
        ell = rng.normal(size=d); lam = rng.normal() * 0.5
        A, C, W = P["A"], P["C"], P["W"]
        T = 2.0
        sol0 = solve_ivp(P["f"], (0, T), P["x0"], method="DOP853", rtol=1e-12, atol=1e-13, dense_output=True)
        tstar = rng.uniform(0.6, 1.5)
        c0 = P["a"] @ sol0.sol(tstar) + P["beta"] * np.sin(tstar)

        def run(eps):
            def rhs(t, Y):
                x = Y[:d]
                fx = P["f"](t, x) + eps * u
                return np.concatenate([fx, [np.sin(ell @ x) + lam * t]])
            ev = lambda t, Y: P["a"] @ Y[:d] + P["beta"] * np.sin(t) - c0 + gam * eps
            ev.terminal = True
            s = solve_ivp(rhs, (0, T), np.concatenate([P["x0"] + eps * v0, [0.0]]), method="DOP853",
                          rtol=1e-13, atol=1e-14, events=ev)
            if s.t_events[0].size == 0:
                return None
            return s.t_events[0][0], s.y_events[0][0][-1]

        base = run(0.0)
        if base is None:
            res["skipped"] += 1; continue
        tau, J = base
        if tau < 0.05:
            res["skipped"] += 1; continue
        # transversality at tau
        solb = solve_ivp(P["f"], (0, tau), P["x0"], method="DOP853", rtol=1e-13, atol=1e-14, dense_output=True)
        xt = solb.sol(tau)
        den = P["beta"] * np.cos(tau) + P["a"] @ P["f"](tau, xt)
        if abs(den) < 0.1:
            res["skipped"] += 1; continue
        # variational equation z' = f_x z + u, z(0) = v0; also accumulate int L_x z
        def var(t, Y):
            x, z = Y[:d], Y[d:2 * d]
            fx = A + C @ np.diag(1 - np.tanh(W @ x) ** 2) @ W
            return np.concatenate([P["f"](t, x), fx @ z + u, [np.cos(ell @ x) * (ell @ z)]])
        sv = solve_ivp(var, (0, tau), np.concatenate([P["x0"], v0, [0.0]]), method="DOP853", rtol=1e-13, atol=1e-14)
        zt, intLz = sv.y[d:2 * d, -1], sv.y[-1, -1]
        taup = -(P["a"] @ zt + gam) / den
        Ltau = np.sin(ell @ xt) + lam * tau
        Jp = Ltau * taup + intLz
        h = 1e-5
        pl, mi = run(h), run(-h)
        if pl is None or mi is None:
            res["skipped"] += 1; continue
        taup_fd = (pl[0] - mi[0]) / (2 * h); Jp_fd = (pl[1] - mi[1]) / (2 * h)
        res["max_rel_err_tau_prime"] = max(res["max_rel_err_tau_prime"], abs(taup - taup_fd) / max(1.0, abs(taup_fd)))
        res["max_rel_err_J_prime"] = max(res["max_rel_err_J_prime"], abs(Jp - Jp_fd) / max(1.0, abs(Jp_fd)))
        res["min_rel_size_boundary_term"] = min(res["min_rel_size_boundary_term"], abs(Ltau * taup) / max(1.0, abs(Jp_fd)))
        res["instances"] += 1
    return res


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    A = part_A(); B = part_B(); C = part_C(rng); D = part_D(rng)
    verdict = {
        "A_exact_example_and_boundary_term": True,
        "A_V2_needs_constant_sign": A["V2_sign_witness"]["V2_violated"] and A["V2_sign_witness"]["V1_holds"],
        "B_author_numbers_reproduced": all(abs(B[k] - B["author_" + k2]) < 1e-11 for k, k2 in
                                           [("event_error", "event_error"), ("direct_bound", "direct_bound"),
                                            ("gronwall_sup_r_bound", "gronwall_bound"), ("Q_error", "Q_error"),
                                            ("Q_guard_specialised_bound", "Q_bound")]),
        "C_V1_no_violation": C["V1_event_viol"] == 0 and C["V1_Q_viol"] == 0,
        "C_V2_no_violation": C["V2_event_viol"] == 0 and C["V2_Q_viol"] == 0,
        "C_gronwall_sound": C["gronwall_kappa_ge_true_err_viol"] == 0,
        "C_certificate_no_false_pass": C["cert_false_pass"] == 0,
        "D_event_derivative_matches_fd": D["max_rel_err_tau_prime"] < 1e-5 and D["max_rel_err_J_prime"] < 1e-5,
    }
    def clean(o):
        if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
        if isinstance(o, (np.floating, float)): return float(o)
        if isinstance(o, (np.integer,)): return int(o)
        if isinstance(o, (np.bool_,)): return bool(o)
        return o
    res = clean({"A": A, "B": B, "C": C, "D": D, "verdict": verdict, "seed": SEED,
                 "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    (out / "lt6_rot004_event_certificate_check.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
