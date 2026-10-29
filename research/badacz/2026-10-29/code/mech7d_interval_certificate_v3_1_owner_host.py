#!/usr/bin/env python3
"""BADACZ (Claude): v3.1 = v3 repaired after AUD1 ROT014 (private audit, 29 X):
  (1) PCHIP segment selection now uses exact high-precision comparisons of the interval endpoints with the binary64
      knots, padded by one segment on each side (v3 rounded the endpoints to float64 first and could skip the left
      segment at a knot: AUD1 counterexample t = [1 - 1e-20, 1 + 1e-20]);
  (2) explicit support-edge policy: the Gegenbauer source term is defined on |x(u)| < 1 (x with the float constants
      of the model); on a piece whose x-enclosure straddles +-1 the term is enclosed by hull(term on the clamped part,
      0), valid because k vanishes to order 3 at x = +-1 (v3 decided inside/outside from a float midpoint);
  (3) rigorous interval certificate of source positivity (v3 used a dense float grid);
  (4) regression self-tests run first (AUD1 cross-knot examples, random cross-knot value/derivative tests, a support
      edge test); the run aborts if any fails.
Everything else is v3 unchanged.
Original v3 docstring:
v3 = the v2 interval error certificate (doc 025, AUD1 ROT010 conditional pass) executed on the
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

import argparse, bisect, hashlib, importlib.util, io, json, math, sys, time
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
    H["xs"] = fT.x.copy(); H["xs_mp"] = [mp.mpf(float(v)) for v in fT.x]
    assert np.array_equal(fT.x, fa.x)
    return df


# ---------------------------------------------------------------- PCHIP background: float and interval/dual
def _hull(a, b):
    return iv.mpf([min(mp.mpf(a.a), mp.mpf(b.a)), max(mp.mpf(a.b), mp.mpf(b.b))])


def pp_g(xs_iv, cs_iv, xs_f, t):
    """enclosure of a C^1 piecewise cubic (scipy PPoly coefficients, exactly the floats used by the float model)
    over an interval t (or dual t): hull over every node interval the argument meets.
    v3.1: segment indices from EXACT comparisons (mp) of the interval endpoints with the knots, padded by one
    segment on each side; empty intersections skipped; coverage of [a, b] asserted."""
    tv = t.v if isinstance(t, DI) else I(t)
    a_t, b_t = mp.mpf(tv.a), mp.mpf(tv.b)
    xs_mp = H["xs_mp"] if xs_iv is H.get("Tx") or xs_iv is H.get("ax") else [mp.mpf(x.a) for x in xs_iv]
    if not (xs_mp[0] <= a_t and b_t <= xs_mp[-1]):
        raise AssertionError("argument outside archived background")
    m = len(xs_mp) - 2
    k0 = max(0, bisect.bisect_right(xs_mp, a_t) - 2); k1 = min(m, bisect.bisect_left(xs_mp, b_t) + 0)
    vals = []; ders = []; cover_lo = None; cover_hi = None
    for k in range(k0, k1 + 1):
        a = max(a_t, xs_mp[k]); b = min(b_t, xs_mp[k + 1])
        if a > b:
            continue
        cover_lo = a if cover_lo is None else min(cover_lo, a); cover_hi = b if cover_hi is None else max(cover_hi, b)
        seg = iv.mpf([a, b]); dt = seg - xs_iv[k]
        c0, c1, c2, c3 = cs_iv[k]
        vals.append(((c0 * dt + c1) * dt + c2) * dt + c3)
        ders.append((3 * c0 * dt + 2 * c1) * dt + c2)
    assert vals and cover_lo == a_t and cover_hi == b_t, "PCHIP segment cover incomplete"
    v = vals[0]; d = ders[0]
    for x in vals[1:]:
        v = _hull(v, x)
    for x in ders[1:]:
        d = _hull(d, x)
    if isinstance(t, DI):
        return DI(v, d * t.d)
    return v


def T_g(t):
    return pp_g(H["Tx"], H["Tc"], H["xs"], t)


def nPBH_g(t):
    return K(H["nPBH0"]) * EXP((pp_g(H["ax"], H["ac"], H["xs"], t) - K(H["L0"])) * K(-3))


def src_g(u, amp, inside):
    """v3.1: the 'inside' flag is ignored; the Gegenbauer term is enclosed from the x-enclosure itself:
    x entirely in [-1, 1] -> term; x entirely outside (-1, 1) -> 0; straddling -> hull(term on clamped x, 0)."""
    t = K(H["t_edge"]) + K(DT_EDGE) * (1 - u ** 3)
    nP = nPBH_g(t)
    s = [K(float(H["edgeQ"][i] * H["factor"][i])) * nP / K(HBAR) * POW(u, float(H["expo"][i])) / K(NSCALE) for i in range(6)]
    if amp != 0:
        x = (LOG(u) - K(ZM)) * (2 / Lz)
        xv = x.v if isinstance(x, DI) else x
        xa, xb = mp.mpf(xv.a), mp.mpf(xv.b)
        if xb <= -1 or xa >= 1:
            return s, t
        straddle = xa < -1 or xb > 1
        if straddle:
            xc = iv.mpf([max(xa, mp.mpf(-1)), min(xb, mp.mpf(1))])
            x = DI(xc, x.d) if isinstance(x, DI) else xc
        d = K(amp) * K(Q1[3]) * v2.k_eval(x, v2.DIRECTION_G) / u ** 3 * nP / K(HBAR) / K(NSCALE)
        if straddle:
            if isinstance(d, DI):
                d = DI(_hull(d.v, iv.mpf(0)), _hull(d.d, iv.mpf(0)))
            else:
                d = _hull(d, iv.mpf(0))
            STATS["support_straddles"] += 1
        s[4] = s[4] + d; s[5] = s[5] - d
    return s, t


STATS = {"support_straddles": 0}


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


def certify_positivity(amp, nseg=4000):
    """rigorous: |amp Q1[3] k(x(u))| / u^3 < min(Q1[3] u^s3, Q1[4] u^s4) on |x(u)| <= 1, by interval subdivision in x
    (u = exp(ZM + x Lz/2) with the model's float constants; slack: the map is monotone, its float inverse only
    defines the subdivision). Returns the largest ratio upper bound (must be < 1)."""
    worst = mp.mpf(0)
    for j in range(nseg):
        xI = iv.mpf([mp.mpf(-1) + mp.mpf(2) * j / nseg, mp.mpf(-1) + mp.mpf(2) * (j + 1) / nseg])
        uI = iv.exp(iv.mpf(ZM) + xI / iv.mpf(2 / Lz))
        lhs = abs(iv.mpf(amp) * iv.mpf(Q1[3]) * v2.k_eval(xI, v2.DIRECTION_G)) / uI ** 3
        rhs = min(mp.mpf((iv.mpf(Q1[3]) * iv.exp(iv.mpf(float(SLOPES[3])) * iv.log(uI))).a),
                  mp.mpf((iv.mpf(Q1[4]) * iv.exp(iv.mpf(float(SLOPES[4])) * iv.log(uI))).a))
        worst = max(worst, mp.mpf(lhs.b) / rhs)
    return worst


def self_tests():
    out = {}
    from scipy.interpolate import PchipInterpolator as PI
    saved = dict(H)
    ok_all = True
    for name, ys in (("aud1_linear", [0., 1., 2.]), ("aud1_nonlinear", [0., 1., 1.1])):
        f = PI([0., 1., 2.], ys)
        xs_iv = [iv.mpf(float(v)) for v in f.x]; cs = [[iv.mpf(float(v)) for v in col] for col in f.c.T]
        e = mp.mpf("1e-20"); tI = iv.mpf([1 - e, 1 + e])
        enc = pp_g(xs_iv, cs, f.x, tI)
        truth_left = ((mp.mpf(f.c[0, 0]) * (1 - e) + mp.mpf(f.c[1, 0])) * (1 - e) + mp.mpf(f.c[2, 0])) * (1 - e) + mp.mpf(f.c[3, 0])
        truth_right = mp.mpf(f.c[3, 1]) + e * (mp.mpf(f.c[2, 1]) + e * (mp.mpf(f.c[1, 1]) + e * mp.mpf(f.c[0, 1])))
        ok = mp.mpf(enc.a) <= truth_left <= mp.mpf(enc.b) and mp.mpf(enc.a) <= truth_right <= mp.mpf(enc.b)
        out[name] = bool(ok); ok_all &= ok
    # random cross-knot tests on the real background (values and dual derivatives)
    rng = np.random.default_rng(20261029)
    xs = H["xs_mp"]; fT = H["fT"]; bad = 0; n = 0
    for _ in range(300):
        k = int(rng.integers(1, len(xs) - 1))
        w = mp.mpf(10) ** (-int(rng.integers(3, 22))) * (xs[k + 1] - xs[k - 1])
        tI = iv.mpf([xs[k] - w * mp.mpf(rng.random()), xs[k] + w * mp.mpf(rng.random())])
        enc = pp_g(H["Tx"], H["Tc"], H["xs"], tI)
        encD = pp_g(H["Tx"], H["Tc"], H["xs"], DI(tI, iv.mpf(1)))
        for frac in (0, 0.25, 0.5, 0.75, 1):
            tp = mp.mpf(tI.a) + (mp.mpf(tI.b) - mp.mpf(tI.a)) * frac
            j = max(0, min(len(xs) - 2, bisect.bisect_right(xs, tp) - 1))
            dt = tp - xs[j]; c = [mp.mpf(float(v)) for v in fT.c[:, j]]
            val = ((c[0] * dt + c[1]) * dt + c[2]) * dt + c[3]; der = (3 * c[0] * dt + 2 * c[1]) * dt + c[2]
            n += 1
            if not (mp.mpf(enc.a) <= val <= mp.mpf(enc.b) and mp.mpf(encD.d.a) <= der <= mp.mpf(encD.d.b)):
                bad += 1
    # negative control: the v3 selector (float-rounded endpoints) skips the left segment on the AUD1 example
    nodes = np.array([0., 1., 2.]); e = mp.mpf("1e-20"); tv = iv.mpf([1 - e, 1 + e])
    lo, hi = float(mp.mpf(tv.a)), float(mp.mpf(tv.b))
    old = (max(0, int(np.searchsorted(nodes, lo, 'right')) - 1), min(1, int(np.searchsorted(nodes, hi, 'right')) - 1))
    out["negative_control_v3_selector_on_aud1_example"] = {"k0_k1": list(old), "skips_left_segment": old[0] == 1}
    out["random_cross_knot_points"] = n; out["random_cross_knot_failures"] = bad; ok_all &= bad == 0
    # support edge: a u-interval straddling the support edge must enclose the true source at points on BOTH sides
    v2.DIRECTION_G[:] = [1.0, 0, 0, 0, 0, 0, 0, 0]
    ue = mp.exp(mp.mpf(ZM) + mp.mpf(1) / mp.mpf(2 / Lz))          # u where x(u) = +1 (upper support edge)
    uI = iv.mpf([ue * (1 - mp.mpf("0.02")), ue * (1 + mp.mpf("0.02"))])
    amp_t = 0.05 * kmax_ratio([1.0, 0, 0, 0, 0, 0, 0, 0]); v2.DIRECTION_G[:] = [1.0, 0, 0, 0, 0, 0, 0, 0]
    s_enc, _ = src_g(uI, amp_t, False)
    ok_edge = True; pts = 0; inside_pts = 0
    for frac in [mp.mpf(j) / 40 for j in range(41)]:
        up_ = mp.mpf(uI.a) + (mp.mpf(uI.b) - mp.mpf(uI.a)) * frac
        s_pt, _ = src_g(iv.mpf(up_), amp_t, False)          # degenerate interval: tight enclosure at the point
        xx = (mp.log(up_) - mp.mpf(ZM)) * mp.mpf(2 / Lz); inside_pts += int(abs(xx) < 1)
        for i in (4, 5):
            ok_edge &= mp.mpf(s_enc[i].a) <= mp.mpf(s_pt[i].a) and mp.mpf(s_pt[i].b) <= mp.mpf(s_enc[i].b)
        pts += 1
    out["support_edge_points"] = pts; out["support_edge_points_inside"] = inside_pts
    out["support_edge_enclosure_contains_pointwise_sources"] = bool(ok_edge); ok_all &= ok_edge
    H.update(saved)
    out["all_pass"] = bool(ok_all)
    if not ok_all:
        raise SystemExit("self-tests FAILED: " + json.dumps(out))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pub", required=True); ap.add_argument("--pap", required=True)
    ap.add_argument("--mech006", required=True); ap.add_argument("--out", required=True)
    args = ap.parse_args(); out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    df = load_host(args.pub, args.pap)
    tests = self_tests()
    print("self-tests", tests, flush=True)
    res = {"self_tests_v3_1": tests,"host": {"t_edge": H["t_edge"], "t_cut": H["t_cut"], "t_eval": H["t_eval"], "T_edge_MeV": float(H["fT"](H["t_edge"])),
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
    pos = certify_positivity(amp)
    print("positivity ratio upper bound", float(pos), flush=True)
    res["positivity_certificate"] = {"max_ratio_upper_bound": float(pos), "nseg": 4000, "pass": bool(pos < 1)}
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
    res["support_edge_straddling_pieces"] = STATS["support_straddles"]
    res["verdict"] = {
        "self_tests_pass": tests["all_pass"],
        "positivity_certified": res["positivity_certificate"]["pass"],
        "host_fidelity_below_1e-8": res["host_fidelity"]["abs_diff"] < 1e-8,
        "covers_diagnostic_error": all(r["bound_eps_X"] >= r["diagnostic_error"] for r in runs.values()),
        "two_point_floor_positive": floor > 0,
    }
    res["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    res["v2_code_sha256"] = hashlib.sha256((HERE / "mech7d_interval_certificate_v2.py").read_bytes()).hexdigest()
    (out / "mech7d_interval_certificate_v3_1_owner_host.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res["verdict"], indent=1), half_gap, floor)


if __name__ == "__main__":
    main()
