#!/usr/bin/env python3
"""Follow-up to the external audit (Grok) of REVIEW_004 T2. Two checks:
  A  exact (SymPy):
     A1 saddle x'=y, y'=x, R=1, adaptive state feedback u=k x through channel (F,F_y):
        (1,1) keeps the reduced model exact, (1,0) does not;
     A2 Grok point 2: with R_bar != 0, x-only impulses along ker R_bar are harmless, other x-only
        directions are not (so 'full rank F' is load-bearing in the fragility corollary).
  B  numeric: random linear systems with a nontrivial N0 (largest H-invariant subspace in ker B)
     and K_R == 0. Channels satisfying T2 with a NONZERO shift F_y - R F inside N0, and violating
     channels. Inputs: (i) feedback on the observed x, (ii) feedback on the hidden y replayed as a
     recorded signal, (iii) adaptive impulses whose sizes depend on x just before each kick.
Run: python3 review004_grok_audit_followup_check.py --out <dir>
numpy 2.1.3, scipy 1.14.1, sympy 1.13.3; seed 20261028.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm

SEED = 20261028


def part_A():
    t, k = sp.symbols("t k", real=True)
    out = {}
    # A1: saddle with feedback u = k x
    res = {}
    for (F, Fy) in [(1, 1), (1, 0)]:
        x, y = sp.Function("x"), sp.Function("y")
        sol = sp.dsolve([sp.Eq(x(t).diff(t), y(t) + F * k * x(t)), sp.Eq(y(t).diff(t), x(t) + Fy * k * x(t))],
                        ics={x(0): 1, y(0): 1})
        xs = [s.rhs for s in sol if s.lhs == x(t)][0]
        red = sp.exp((1 + F * k) * t)                     # reduced: x' = E x + F u, E = A + B R = 1
        res[f"F={F},Fy={Fy}"] = {"x_minus_reduced_is_zero": bool(sp.simplify(xs - red) == 0),
                                 "x_minus_reduced_at_k=1/2,t=1": str(sp.N((xs - red).subs({k: sp.Rational(1, 2), t: 1}), 12))}
    out["A1_saddle_adaptive_feedback"] = res
    # A2: n=2 visible, m=1 hidden, R = [1, 0], K_R == 0 by construction (G = 0), R_bar != 0
    A = sp.Matrix([[0, 1], [-2, -3]]); B = sp.Matrix([[1], [1]]); D = sp.Matrix([[-1]]); R = sp.Matrix([[1, 0]])
    C = -(D * R - R * A - R * B * R)
    G = C + D * R - R * A - R * B * R
    assert G == sp.zeros(1, 2)
    H = D - R * B
    out2 = {}
    for name, Fv in [("F=e2 (in ker R)", sp.Matrix([0, 1])), ("F=e1", sp.Matrix([1, 0]))]:
        shift = -R * Fv                                   # F_y = 0
        crit = [(B * H ** j * shift)[:, 0].T.tolist() for j in range(1)]
        out2[name] = {"F_y - R F": str(shift.T.tolist()), "B H^0 (F_y-RF)": str(crit[0]),
                      "robust": bool(all(v == 0 for v in (B * shift)))}
    out["A2_partial_rank_x_only_impulses"] = out2
    return out


def make_system(rng):
    n = int(rng.integers(1, 3)); mo = int(rng.integers(1, 3)); mu = int(rng.integers(1, 3)); m = mo + mu
    A = rng.normal(size=(n, n)) * 0.6 - 0.3 * np.eye(n)
    Bo = rng.normal(size=(n, mo))
    B = np.hstack([Bo, np.zeros((n, mu))])
    Doo = rng.normal(size=(mo, mo)) * 0.6 - 0.5 * np.eye(mo)
    Duo = rng.normal(size=(mu, mo)); Duu = rng.normal(size=(mu, mu)) * 0.6 - 0.5 * np.eye(mu)
    D = np.block([[Doo, np.zeros((mo, mu))], [Duo, Duu]])
    Ro = rng.normal(size=(mo, n)) * 0.7; Ru = rng.normal(size=(mu, n)) * 0.7
    R = np.vstack([Ro, Ru])
    Co = -(Doo @ Ro - Ro @ A - Ro @ Bo @ Ro)               # quotient Riccati: G_bar = 0
    Cu = rng.normal(size=(mu, n))
    C = np.vstack([Co, Cu])
    E = A + B @ R; H = D - R @ B; G = C + D @ R - R @ A - R @ B @ R
    KR = max(np.abs(B @ expm(s * H) @ G).max() for s in np.linspace(0, 2, 9))
    # observability of the quotient (Bo, Hoo)
    Hoo = H[:mo, :mo]
    O = np.vstack([Bo @ np.linalg.matrix_power(Hoo, j) for j in range(mo)])
    obs = np.linalg.svd(O, compute_uv=False)[-1]
    return dict(n=n, mo=mo, mu=mu, m=m, A=A, B=B, C=C, D=D, R=R, E=E, H=H, KR=KR, obs=obs)


def simulate(S, F, Fy, law, rng_vec, T=2.0, kicks=None):
    n, m = S["n"], S["m"]
    c, d = rng_vec
    x0 = np.ones(n) * 0.7
    y0 = S["R"] @ x0
    def u_of(t, x, y):
        if law == "observed": return np.sin(c @ x) + 0.5 * np.cos(3 * t)
        if law == "hidden": return np.tanh(d @ y) + 0.3 * np.sin(2 * t)
        return 0.0
    def full(t, w):
        x, y = w[:n], w[n:]
        u = u_of(t, x, y)
        return np.concatenate([S["A"] @ x + S["B"] @ y + F * u, S["C"] @ x + S["D"] @ y + Fy * u])
    ts = np.linspace(0, T, 401)
    if kicks is None:
        sf = solve_ivp(full, (0, T), np.concatenate([x0, y0]), method="DOP853", rtol=1e-12, atol=1e-13, dense_output=True)
        Xf = sf.sol(ts)[:n].T
        if law == "observed":
            red = lambda t, x: S["E"] @ x + F * u_of(t, x, None)
            sr = solve_ivp(red, (0, T), x0, method="DOP853", rtol=1e-12, atol=1e-13, dense_output=True)
        else:                                               # replay the recorded hidden-feedback signal
            useq = lambda t: u_of(t, None, sf.sol(t)[n:])
            red = lambda t, x: S["E"] @ x + F * useq(t)
            sr = solve_ivp(red, (0, T), x0, method="DOP853", rtol=1e-12, atol=1e-13, dense_output=True)
        Xr = sr.sol(ts).T
        return np.max(np.abs(Xf - Xr)) / max(1.0, np.max(np.abs(Xf)))
    # adaptive impulses, sizes chosen from x just before each kick (same rule in both models)
    wf = np.concatenate([x0, y0]); xr = x0.copy(); t0 = 0.0; worst = 0.0
    lin = lambda t, w: np.concatenate([S["A"] @ w[:n] + S["B"] @ w[n:], S["C"] @ w[:n] + S["D"] @ w[n:]])
    for sk in list(kicks) + [T]:
        sf = solve_ivp(lin, (t0, sk), wf, method="DOP853", rtol=1e-12, atol=1e-13, dense_output=True)
        tt = np.linspace(t0, sk, 50)
        Xf = sf.sol(tt)[:n].T
        Xr = np.array([expm((s - t0) * S["E"]) @ xr for s in tt])
        worst = max(worst, np.max(np.abs(Xf - Xr)) / max(1.0, np.max(np.abs(Xf))))
        wf = sf.y[:, -1].copy(); xr = expm((sk - t0) * S["E"]) @ xr
        if sk < T:
            uf = np.cos(c @ wf[:n]); ur = np.cos(c @ xr)
            wf[:n] += F * uf; wf[n:] += Fy * uf; xr = xr + F * ur
        t0 = sk
    return worst


def part_B(rng):
    rows = {"satisfying": [], "violating": []}
    nonzero_shift = 0; built = 0
    while built < 60:
        S = make_system(rng)
        if S["KR"] > 1e-9 or S["obs"] < 1e-3:
            continue
        built += 1
        n, mo, mu = S["n"], S["mo"], S["mu"]
        F = rng.normal(size=n)
        shift_u = rng.normal(size=mu)                       # nonzero shift inside N0 = span(y_u)
        Fy_ok = np.concatenate([S["R"][:mo] @ F, S["R"][mo:] @ F + shift_u])
        Fy_bad = rng.normal(size=S["m"])
        nonzero_shift += int(np.linalg.norm(Fy_ok - S["R"] @ F) > 1e-6)
        cvec = rng.normal(size=n); dvec = rng.normal(size=S["m"])
        for tag, Fy in [("satisfying", Fy_ok), ("violating", Fy_bad)]:
            r = {"observed_feedback": simulate(S, F, Fy, "observed", (cvec, dvec)),
                 "hidden_feedback_replayed": simulate(S, F, Fy, "hidden", (cvec, dvec)),
                 "adaptive_impulses": simulate(S, F, Fy, "none", (cvec, dvec), kicks=[0.4, 0.9, 1.3])}
            rows[tag].append(r)
    summ = {}
    for tag in rows:
        for key in ["observed_feedback", "hidden_feedback_replayed", "adaptive_impulses"]:
            v = [r[key] for r in rows[tag]]
            summ[f"{tag}_{key}"] = {"max": float(max(v)), "min": float(min(v))}
    summ["systems"] = built; summ["satisfying_channels_with_nonzero_shift_in_N0"] = nonzero_shift
    return summ


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    A = part_A(); B = part_B(rng)
    verdict = {
        "A1_adaptive_feedback_exact_iff_T2": A["A1_saddle_adaptive_feedback"]["F=1,Fy=1"]["x_minus_reduced_is_zero"]
                                           and not A["A1_saddle_adaptive_feedback"]["F=1,Fy=0"]["x_minus_reduced_is_zero"],
        "A2_partial_rank_robust_direction_exists": A["A2_partial_rank_x_only_impulses"]["F=e2 (in ker R)"]["robust"]
                                                  and not A["A2_partial_rank_x_only_impulses"]["F=e1"]["robust"],
        "B_T2_channels_exact_under_adaptive_inputs": all(B[f"satisfying_{k}"]["max"] < 1e-8 for k in
                                                         ["observed_feedback", "hidden_feedback_replayed", "adaptive_impulses"]),
        "B_violating_channels_detectably_inexact": all(B[f"violating_{k}"]["min"] > 1e-6 for k in
                                                       ["observed_feedback", "hidden_feedback_replayed", "adaptive_impulses"]),
    }
    res = {"A": A, "B": B, "verdict": {k: bool(v) for k, v in verdict.items()}, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "review004_grok_audit_followup_check.json").write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
