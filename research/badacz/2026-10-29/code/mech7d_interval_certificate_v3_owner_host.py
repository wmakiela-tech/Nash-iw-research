#!/usr/bin/env python3
"""BADACZ (Claude): v3 = the v2 interval error certificate (doc 025, AUD1 ROT010 conditional pass) executed on the
REAL public Mech-S7 ROT006 host instead of the synthetic background.

Host (public, sha256-pinned exactly as in Mech-S7 terminal_7d_exact_mass_common_background_006.py):
  PUB 75766c5b... = GitHub Actions artifact 12116193467 (mech-s6-wuxu-charge-pair-comparator, trajectory_current.csv)
  PAP 3b24f50c... = GitHub Actions artifact 12192535869 (mech-s6-wuxu-paper-charge-2x2-missing-cells)
  background T(t) and a(t): PchipInterpolator of the archived public_exec trajectory (as Mech 006);
  initial state: archived row 1469 reassigned to the exact table edge (Mech 006 'archive' initial);
  map 'exec', law 'public'; 7D field identical to Mech 006 (weak rates, conversions, decay + loss).
Source perturbation (exact-information class, Theorem E of doc 022, applied by Mech-S7 ROT035):
  Qpbar -> Qpbar + amp*Q1[3]*k(x)/u^3, Qnbar -> Qnbar - amp*Q1[3]*k(x)/u^3 on 0.07 < u < 0.92,
  k = (1-x^2)^4 sum_{l=3..10} a_l C_l^{(9/2)}(x): comoving moments j=0,1,2 of each species and the pair sum are
  EXACTLY unchanged. Direction a = finite-difference gradient of X_target (Euclidean), amp = 0.7 * positivity max.
NOT Mech ROT035's own witnesses (their repaired 10-component preedge initial state and Riesz directions are in a
Moderator-local ZIP). The interval machinery (DI, centred-form defect, whole-piece bootstrap, propagate_piece) is
imported UNCHANGED from v2; new here: interval/dual enclosure of the PCHIP background (hull over node intervals) and
piece cuts at every PCHIP node.
Run: python3 -I mech7d_interval_certificate_v3_owner_host.py --pub <artifact 12116193467 zip> --pap <artifact
12192535869 zip> --mech006 <path to terminal_7d_exact_mass_common_background_006.py> --out <dir>
"""
from __future__ import annotations

import argparse, hashlib, importlib.util, io, json, math, sys, time
from pathlib import Path
from zipfile import ZipFile

import numpy as np
import pandas as pd
from mpmath import iv, mp
from scipy.integrate import solve_ivp
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("v2", HERE / "mech7d_interval_certificate_v2.py")
v2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v2)
DI, K, I, EXP, LOG, POW, MODE = v2.DI, v2.K, v2.I, v2.EXP, v2.LOG, v2.POW, v2.MODE

PUB = '75766c5bcc38fe72b3405e32f5c8ef81a50237d6930f318780d49524ff6bafd5'
PAP = '3b24f50ce2f50272874593db3ad26e5e73e871f986ebae91ae6a4fdf8ab15a4e'
SPECIES = ['pi_minus', 'pi_plus', 'K_minus', 'K0L', 'pbar', 'nbar']
GAMMA, M_EDGE, M_CUT, U_CUT, DT_EDGE, T_NUC = v2.GAMMA, v2.M_EDGE, v2.M_CUT, v2.U_CUT, v2.DT_EDGE, v2.T_NUC
Q1, INDEX, SLOPES, HBAR, NSCALE = v2.Q1, v2.INDEX, v2.SLOPES, v2.HBAR_GEV_SEC, v2.NSCALE
Lz, ZM = v2.Lz, v2.ZM
H = {}  # host data


def load_host(pub, pap):
    b = Path(pub).read_bytes(); assert hashlib.sha256(b).hexdigest() == PUB
    with ZipFile(io.BytesIO(b)) as z:
        df = pd.read_csv(io.BytesIO(z.read('trajectory_current.csv')))
    bp = Path(pap).read_bytes(); assert hashlib.sha256(bp).hexdigest() == PAP
    assert len(df) == 1600 and df.source_active.iloc[1469] == 1 and df.source_active.iloc[1470] == 0
    time_ = df.t_sec.to_numpy(); temp = df.T_GeV.to_numpy() * 1000
    fT = PchipInterpolator(time_, temp, extrapolate=False)
    fa = PchipInterpolator(time_, np.log(df.a.to_numpy()), extrapolate=False)
    t0 = float(time_[0]); m0 = float(df.m_PBH_g.iloc[0])
    t_edge = t0 + (m0 ** 3 - M_EDGE ** 3) / GAMMA
    t_cut = t_edge + (M_EDGE ** 3 - M_CUT ** 3) / GAMMA
    end_idx = int(np.where(temp < T_NUC)[0][0])
    t_eval = float(brentq(lambda z: float(fT(z)) - T_NUC, float(time_[end_idx - 1]), float(time_[end_idx]), xtol=1e-12))
    y0 = np.concatenate([[float(df.Xn.iloc[1469])], np.array([float(df[f'n_{sp}_cm3'].iloc[1469]) for sp in SPECIES]) / NSCALE])
    H.update(dict(fT=fT, fa=fa, t_edge=t_edge, t_cut=t_cut, t_eval=t_eval, y0=y0,
                  nPBH0=float(df.n_PBH_cm3.iloc[1469]), L0=math.log(float(df.a.iloc[1469])),
                  factor=np.ones(6), expo=SLOPES[INDEX], edgeQ=Q1[INDEX]))
    H["Tx"] = [iv.mpf(float(v)) for v in fT.x]; H["Tc"] = [[iv.mpf(float(v)) for v in col] for col in fT.c.T]
    H["ax"] = [iv.mpf(float(v)) for v in fa.x]; H["ac"] = [[iv.mpf(float(v)) for v in col] for col in fa.c.T]
    H["xs"] = fT.x.copy()
    return df


# ---------------------------------------------------------------- PCHIP background: float and interval/dual
def pp_g(xs_iv, cs_iv, xs_f, t):
    """enclosure of a C^1 piecewise cubic (scipy PPoly coefficients, exactly the floats used by the float model)
    over an interval t (or dual t): hull over every node interval the argument meets."""
    tv = t.v if isinstance(t, DI) else I(t)
    lo, hi = float(mp.mpf(tv.a)), float(mp.mpf(tv.b))
    k0 = max(0, int(np.searchsorted(xs_f, lo, 'right')) - 1); k1 = min(len(xs_f) - 2, int(np.searchsorted(xs_f, hi, 'right')) - 1)
    assert xs_f[0] <= lo and hi <= xs_f[-1], "argument outside archived background"
    vals = []; ders = []
    for k in range(k0, k1 + 1):
        a = max(mp.mpf(tv.a), mp.mpf(xs_iv[k].a)); b = min(mp.mpf(tv.b), mp.mpf(xs_iv[k + 1].b))
        if a > b:
            continue
        seg = iv.mpf([a, b]); dt = seg - xs_iv[k]
        c0, c1, c2, c3 = cs_iv[k]
        vals.append(((c0 * dt + c1) * dt + c2) * dt + c3)
        ders.append((3 * c0 * dt + 2 * c1) * dt + c2)
    v = vals[0]; d = ders[0]
    for x in vals[1:]:
        v = iv.mpf([min(mp.mpf(v.a), mp.mpf(x.a)), max(mp.mpf(v.b), mp.mpf(x.b))])
    for x in ders[1:]:
        d = iv.mpf([min(mp.mpf(d.a), mp.mpf(x.a)), max(mp.mpf(d.b), mp.mpf(x.b))])
    if isinstance(t, DI):
        return DI(v, d * t.d)
    return v


def T_g(t):
    return pp_g(H["Tx"], H["Tc"], H["xs"], t)


def nPBH_g(t):
    return K(H["nPBH0"]) * EXP((pp_g(H["ax"], H["ac"], H["xs"], t) - K(H["L0"])) * K(-3))


def src_g(u, amp, inside):
    t = K(H["t_edge"]) + K(DT_EDGE) * (1 - u ** 3)
    nP = nPBH_g(t)
    s = [K(float(H["edgeQ"][i] * H["factor"][i])) * nP / K(HBAR) * POW(u, float(H["expo"][i])) / K(NSCALE) for i in range(6)]
    if inside:
        x = (LOG(u) - K(ZM)) * (2 / Lz)
        d = K(amp) * K(Q1[3]) * v2.k_eval(x, v2.DIRECTION_G) / u ** 3 * nP / K(HBAR) / K(NSCALE)
        s[4] = s[4] + d; s[5] = s[5] - d
    return s, t


def G_g_host(phase, s, y, amp, kc, inside):
    if phase == "A":
        u = -s; src, t = src_g(u, amp, inside); c = 3 * K(DT_EDGE) * u * u
    else:
        t = s; src = [K(0)] * 6; c = K(1)
    T = T_g(t)
    a, b, decay, l0, l1, nbs, g, ex = v2.rates_g(T)
    X = y[0]; n = y[1:]
    conv = K(0)
    for i in range(6):
        conv = conv + n[i] * K(v2.S) * ((1 - X) * a[i] - X * b[i])
    F = [g * ((1 - X) * ex - X) - X / K(v2.TAU_N) + conv]
    for i in range(6):
        F.append(src[i] - (decay[i] + (l0[i] + l1[i] * X) * nbs) * n[i])
    return [c * f for f in F], (a, b, l1, nbs, g, ex, c, decay, l0)


v2.G_g = G_g_host   # piece_enclosures / J_and_quad_interval resolve G_g in v2's globals


def G_f_host(phase, s, y, amp):
    if phase == "A":
        u = -s; t = H["t_edge"] + DT_EDGE * (1 - u ** 3)
        nP = H["nPBH0"] * math.exp(-3 * (float(H["fa"](t)) - H["L0"]))
        src = H["edgeQ"] * H["factor"] * nP / HBAR * u ** H["expo"] / NSCALE
        if 0.07 < u < 0.92:
            x = 2 * (math.log(u) - ZM) / Lz
            d = amp * Q1[3] * v2.k_eval_f(x, v2.DIRECTION_G) / u ** 3 * nP / HBAR / NSCALE
            src = src.copy(); src[4] += d; src[5] -= d
        c = 3 * DT_EDGE * u * u
    else:
        t = s; src = np.zeros(6); c = 1.0
    T = float(H["fT"](t))
    a, b, decay, l0, l1, nbs, g, ex = v2.rates_f(T)
    X = y[0]; n = y[1:]
    D = decay + (l0 + l1 * X) * nbs
    F = np.concatenate([[g * ((1 - X) * ex - X) - X / v2.TAU_N + np.sum(n * v2.S * ((1 - X) * a - X * b))], src - D * n])
    J = np.zeros((7, 7))
    J[0, 0] = -g * (ex + 1) - 1 / v2.TAU_N - v2.S * np.sum(n * (a + b)); J[0, 1:] = v2.S * ((1 - X) * a - X * b)
    J[1:, 0] = -l1 * nbs * n; J[1:, 1:] = np.diag(-D)
    return c * F, c * J


def solve(phase, y0, span, amp, rtol):
    return solve_ivp(lambda s, y: G_f_host(phase, s, y, amp)[0], span, y0, method="Radau", rtol=rtol, atol=rtol * 1e-3,
                     jac=lambda s, y: G_f_host(phase, s, y, amp)[1], max_step=(.02 if phase == "A" else 2.), dense_output=True)


def run(amp, rtol):
    solA = solve("A", H["y0"], (-1.0, -U_CUT), amp, rtol)
    solB = solve("B", solA.y[:, -1], (H["t_cut"], H["t_eval"]), amp, rtol)
    return solA, solB


def node_breaks(phase):
    xs = H["xs"]
    if phase == "A":
        br = [-0.92, -0.07]
        for x in xs:
            if H["t_edge"] < x < H["t_cut"]:
                br.append(-(1 - (x - H["t_edge"]) / DT_EDGE) ** (1 / 3))
        return sorted(br)
    return [float(x) for x in xs if H["t_cut"] < x < H["t_eval"]]


def certify(phase, sol, amp, eps0, sub=8, tol_piece=3e-12, maxdepth=6):
    """v2.certify with PCHIP-node cuts added (logic otherwise unchanged)."""
    eps = [v2.up(I(float(e)) if not isinstance(e, iv.mpf) else e) for e in eps0]
    breaks = node_breaks(phase)
    stats = {"pieces": 0, "refinements": 0, "breaks": len(breaks)}
    max_rho = [mp.mpf(0)] * 7

    def process(s0, h, Q, yo, a0, a1, depth):
        nonlocal eps
        u_mid = -(s0 + 0.5 * (a0 + a1) * h)
        inside = (phase == "A") and (0.07 < u_mid < 0.92)
        rho, diag, off, qx, qn = v2.piece_enclosures(phase, s0, h, Q, yo, a0, a1, amp, None, inside)
        hp = (a1 - a0) * h
        contrib = mp.mpf(0)
        for j in range(1, 7):
            dj = abs(mp.mpf(diag[j].b)); damp = max(dj, mp.mpf(1) / mp.mpf(hp))
            contrib += mp.mpf(off.get((0, j), iv.mpf(0)).b) * mp.mpf(rho[j].b) / damp * mp.mpf(hp)
        contrib += mp.mpf(rho[0].b) * mp.mpf(hp)
        if contrib > tol_piece and depth < maxdepth:
            stats["refinements"] += 1
            mid = 0.5 * (a0 + a1)
            process(s0, h, Q, yo, a0, mid, depth + 1); process(s0, h, Q, yo, mid, a1, depth + 1)
            return
        for k in range(7):
            max_rho[k] = max(max_rho[k], mp.mpf(rho[k].b))
        eps, _ = v2.propagate_piece(eps, diag, off, rho, qx, qn, I(hp), 7)
        stats["pieces"] += 1

    for itp in sol.sol.interpolants:
        s0 = itp.t_old; h = itp.h
        cuts = [0.0] + sorted(((b - s0) / h) for b in breaks if s0 < b < s0 + h) + [1.0]
        edges = []
        for a0, a1 in zip(cuts[:-1], cuts[1:]):
            edges += [a0 + (a1 - a0) * m / sub for m in range(sub)]
        edges.append(1.0)
        for a0, a1 in zip(edges[:-1], edges[1:]):
            process(s0, h, itp.Q, itp.y_old, a0, a1, 0)
    stats["max_rho_upper"] = [float(v) for v in max_rho]
    stats.update({"sub": sub, "tol_piece": tol_piece, "maxdepth": maxdepth})
    return eps, stats


def kmax_ratio(direction):
    """largest amp keeping both species sources positive on the support (dense check, float)."""
    v2.DIRECTION_G[:] = list(direction)
    best = math.inf
    for x in np.linspace(-1 + 1e-6, 1 - 1e-6, 20001):
        u = math.exp(ZM + x * Lz / 2)
        k = abs(v2.k_eval_f(x, direction))
        if k == 0:
            continue
        lim = min(Q1[3] * u ** SLOPES[3], Q1[4] * u ** SLOPES[4]) * u ** 3 / (Q1[3] * k)
        best = min(best, lim)
    return best


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pub", required=True); ap.add_argument("--pap", required=True)
    ap.add_argument("--mech006", required=True); ap.add_argument("--out", required=True)
    args = ap.parse_args(); out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df = load_host(args.pub, args.pap)
    res = {"host": {"t_edge": H["t_edge"], "t_cut": H["t_cut"], "t_eval": H["t_eval"], "T_edge_MeV": float(H["fT"](H["t_edge"])),
                    "X_edge": float(H["y0"][0]), "nPBH0": H["nPBH0"], "PUB": PUB, "PAP": PAP}}

    # 1. host fidelity: Mech's own public simulate() vs this re-implementation, unperturbed, rtol 3e-9
    s6 = importlib.util.spec_from_file_location("mech006", args.mech006); m6 = importlib.util.module_from_spec(s6)
    s6.loader.exec_module(m6)
    data = m6.load(args.pub, args.pap)
    bg = data['public_exec'].copy()
    ref = m6.simulate(bg, 'exec', 'public', 3e-9, 'archive')
    v2.DIRECTION_G[:] = [0.0] * 8
    _, solB0 = run(0.0, 3e-9)
    res["host_fidelity"] = {"mech006_X_target": ref['X_target'], "v3_X_target_unperturbed": float(solB0.y[0, -1]),
                            "abs_diff": abs(ref['X_target'] - float(solB0.y[0, -1])), "mech006_t_eval": ref['t_nuc_target'],
                            "v3_t_eval": H["t_eval"]}
    print("fidelity", res["host_fidelity"], flush=True)

    # 2. witness direction: finite-difference gradient of X_target in the 8 Gegenbauer coefficients
    grad = []
    for l in range(8):
        e = [0.0] * 8; e[l] = 1.0
        amp_l = 0.05 * kmax_ratio(e)
        v2.DIRECTION_G[:] = e
        xp = float(run(+amp_l, 1e-11)[1].y[0, -1]); xm = float(run(-amp_l, 1e-11)[1].y[0, -1])
        grad.append((xp - xm) / (2 * amp_l))
    nrm = math.sqrt(sum(g * g for g in grad)); direction = [g / nrm for g in grad]
    amp = 0.7 * kmax_ratio(direction)
    v2.DIRECTION_G[:] = direction
    res["witness"] = {"direction_a_l(l=3..10)": direction, "gradient": grad, "amp": amp, "amp_over_positivity_max": 0.7,
                      "moments_j012_and_pair_sum": "exactly unchanged (Gegenbauer orthogonality, Theorem E of doc 022)"}

    # 3. certificates for both witnesses
    runs = {}
    for sgn in (+1, -1):
        t0 = time.time()
        solA, solB = run(sgn * amp, 3e-9)
        refA, refB = run(sgn * amp, 1e-12)
        epsA, infA = certify("A", solA, sgn * amp, [0.0] * 7)
        epsB, infB = certify("B", solB, sgn * amp, epsA)
        X = float(solB.y[0, -1]); Xref = float(refB.y[0, -1])
        runs[str(sgn)] = {"X_target_rtol3e-9": X, "X_target_ref_rtol1e-12": Xref, "diagnostic_error": abs(X - Xref),
                          "bound_eps_X": float(mp.mpf(epsB[0].b)), "bound_eps_X_after_phaseA": float(mp.mpf(epsA[0].b)),
                          "bound_eps_all_components_end": [float(mp.mpf(e.b)) for e in epsB],
                          "phaseA": infA, "phaseB": infB}
        print(sgn, runs[str(sgn)]["X_target_rtol3e-9"], runs[str(sgn)]["bound_eps_X"], round(time.time() - t0), flush=True)
    half_gap = abs(runs["1"]["X_target_rtol3e-9"] - runs["-1"]["X_target_rtol3e-9"]) / 2
    floor = half_gap - (runs["1"]["bound_eps_X"] + runs["-1"]["bound_eps_X"]) / 2
    res.update({"runs": runs, "half_gap_numeric": half_gap, "two_point_floor": floor,
                "floor_over_half_gap": floor / half_gap if half_gap > 0 else None})
    res["verdict"] = {
        "host_fidelity_below_1e-8": res["host_fidelity"]["abs_diff"] < 1e-8,
        "covers_diagnostic_error": all(r["bound_eps_X"] >= r["diagnostic_error"] for r in runs.values()),
        "two_point_floor_positive": floor > 0,
    }
    res["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    res["v2_code_sha256"] = hashlib.sha256((HERE / "mech7d_interval_certificate_v2.py").read_bytes()).hexdigest()
    (out / "mech7d_interval_certificate_v3_owner_host.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res["verdict"], indent=1), half_gap, floor)


if __name__ == "__main__":
    main()
