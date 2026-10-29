#!/usr/bin/env python3
"""BADACZ (Claude): repaired a posteriori error bound for the Mech-S7-structured 7D kinetics (v2), after the external
AUD1 ROT009 audit of doc 022 found two errors in v1: (a) sampled majorants, (b) an endpoint-only bootstrap of the
quadratic remainder. v2 changes:
  1. Every majorant is an INTERVAL enclosure over the whole sub-piece (mpmath.iv, outward rounding):
     - Jacobian J(s, yhat(s)) by natural interval extension over the sub-piece;
     - defect r = yhat' - G(s, yhat) by the CENTRED (mean-value) form r(theta_m) + r'(P)(P - theta_m), with r'(P)
       from forward-mode dual-interval arithmetic (DI class) through the full model (time, source, rates, y).
  2. The error is bounded on the WHOLE sub-piece, not only at its end: componentwise scalar comparison with frozen
     off-diagonal forcing at the bootstrap level Phi (|e_j| <= Phi_j on the piece), and the bootstrap is accepted only
     under STRICT inclusion sup_piece phi < Phi (continuity argument). All scalar exponentials are interval-evaluated.
  3. The quadratic remainder (bilinear field) is bounded with Phi, i.e. over the whole sub-piece.
Tested first on both AUD1 ROT009 countermodels (sampled-zero defect; endpoint bootstrap), then on the synthetic
Mech-structured demo of v1 (same trajectories, same synthetic background and exact-information source pair).
Remaining non-interval steps (stated, not hidden): the Radau trajectory itself is only an approximation (that is what
is being bounded), and model constants are the binary floats used by the code.
numpy 2.1.3, scipy 1.14.1, sympy 1.13.3, mpmath 1.3.0.
Run: python3 -I mech7d_interval_certificate_v2.py --out <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from mpmath import iv, mp
from scipy.integrate import solve_ivp, quad

iv.dps = 25
mp.dps = 25


# ---------------------------------------------------------------- interval helpers
def I(x):
    return x if isinstance(x, (iv.mpf, DI)) else iv.mpf(x)


def up(x):
    """rigorous upper endpoint as a degenerate interval."""
    return iv.mpf(x.b)


def mag(x):
    a = abs(x)
    return iv.mpf(a.b)


def lt(a, b):
    """a < b for degenerate/upper-bound intervals (strict, using endpoints)."""
    return mp.mpf(a.b) < mp.mpf(b.a)


class DI:
    """forward-mode dual numbers over intervals: value v and derivative d (w.r.t. the local piece variable)."""
    __slots__ = ("v", "d")

    def __init__(self, v, d):
        self.v = I(v); self.d = I(d)

    def __add__(self, o):
        o = o if isinstance(o, DI) else DI(o, 0); return DI(self.v + o.v, self.d + o.d)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, DI) else DI(o, 0); return DI(self.v - o.v, self.d - o.d)

    def __rsub__(self, o):
        return DI(o, 0) - self

    def __neg__(self):
        return DI(-self.v, -self.d)

    def __mul__(self, o):
        o = o if isinstance(o, DI) else DI(o, 0); return DI(self.v * o.v, self.d * o.v + self.v * o.d)
    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, DI) else DI(o, 0); q = self.v / o.v
        return DI(q, (self.d - q * o.d) / o.v)

    def __rtruediv__(self, o):
        return DI(o, 0) / self

    def __pow__(self, n):
        assert isinstance(n, int)
        if n == 0:
            return DI(1, 0)
        return DI(self.v ** n, n * self.v ** (n - 1) * self.d)


MODE = {"dual": False}


def K(c):
    """constant in the current arithmetic (interval, or dual-interval with zero derivative)."""
    v = c if isinstance(c, iv.mpf) else iv.mpf(c)
    return DI(v, 0) if MODE["dual"] else v


def EXP(x):
    if isinstance(x, DI):
        e = iv.exp(x.v); return DI(e, e * x.d)
    return iv.exp(I(x))


def LOG(x):
    if isinstance(x, DI):
        return DI(iv.log(x.v), x.d / x.v)
    return iv.log(I(x))


def SQRT(x):
    if isinstance(x, DI):
        r = iv.sqrt(x.v); return DI(r, x.d / (2 * r))
    return iv.sqrt(I(x))


def POW(x, p):
    return EXP(LOG(x) * iv.mpf(p)) if isinstance(x, DI) else iv.exp(iv.mpf(p) * iv.log(I(x)))


# ---------------------------------------------------------------- model constants (verbatim from Mech-S7 ROT006, public)
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
T_EDGE_TIME = 150.0; X_EDGE = 0.14; NPBH0 = 1e-11
Lz = math.log(0.92 / 0.07); ZM = 0.5 * (math.log(0.07) + math.log(0.92))
_x = sp.symbols("x")
KL = [[float(c) for c in sp.Poly(sp.expand((1 - _x ** 2) ** 4 * sp.gegenbauer(l, sp.Rational(9, 2), _x)), _x).all_coeffs()] for l in range(3, 11)]


def k_eval(x, direction):
    """k(x) = (1-x^2)^4 sum_l a_l C_l^{(9/2)}(x), l = 3..10, by the stable three-term recurrence (generic arithmetic)."""
    lam = 4.5
    Cm1 = K(1) if MODE["dual"] else iv.mpf(1)
    C0 = x * (2 * lam)
    vals = [Cm1, C0]
    for n in range(1, 10):
        vals.append((x * (2 * (n + lam)) * vals[-1] - vals[-2] * (n + 2 * lam - 1)) / (n + 1))
    tot = None
    for a, l in zip(direction, range(3, 11)):
        term = vals[l] * float(a)
        tot = term if tot is None else tot + term
    w = 1 - x * x
    return (w * w) * (w * w) * tot


def k_eval_f(x, direction):
    lam = 4.5
    vals = [1.0, 2 * lam * x]
    for n in range(1, 10):
        vals.append((2 * (n + lam) * x * vals[-1] - (n + 2 * lam - 1) * vals[-2]) / (n + 1))
    w = 1 - x * x
    return w ** 4 * sum(a * vals[l] for a, l in zip(direction, range(3, 11)))


def kcoeffs(direction):
    deg = max(len(c) for c in KL)
    tot = np.zeros(deg)
    for a, c in zip(direction, KL):
        tot[deg - len(c):] += a * np.array(c)
    return [float(v) for v in tot]


DIRECTION_G = [0.0] * 8      # set in main (coefficients a_l used by the interval model)

# ---------------------------------------------------------------- float model (for the solver), identical formulas
def coulomb_f(T, m):
    ve = math.sqrt(T / m) + math.sqrt(T / M_P_MEV); z = 2 * math.pi * ALPHA / ve
    return z / (-math.expm1(-z))


def rates_f(T):
    nB = ETA_B * (2 * ZETA3 / math.pi ** 2) * (T / HBARC_MEV_CM) ** 3
    fp = coulomb_f(T, 139.57039); fk = coulomb_f(T, 493.677)
    a = np.array([1.5 * fp, 0, 31 * fk, 7, 0, 28.]); b = np.array([0, 1.7, 26, 7, 28, 0.])
    decay = np.array([1 / 2.6033e-8, 1 / 2.6033e-8, 8.1e7, 2e7, 0, 0])
    l0 = np.array([a[0], 0, (31 + 14.5) * fk, 17, 37, 28]); l1 = np.array([-a[0], 1.7, (34 + 26) - (31 + 14.5) * fk, 0, 28 - 37, 37 - 28])
    x = Q_MEV / T; g = (255 / TAU_N) * (12 + 6 * x + x * x) / x ** 5
    return a, b, decay, l0, l1, nB * SIGMA_V_UNIT, g, math.exp(-x)


def src_f(u, amp, kc):
    t = T_EDGE_TIME + DT_EDGE * (1 - u ** 3); nP = NPBH0 * (T_EDGE_TIME / t) ** 1.5
    s = Q1[INDEX] * nP / HBAR_GEV_SEC * u ** SLOPES[INDEX] / NSCALE
    if 0.07 < u < 0.92:
        x = 2 * (math.log(u) - ZM) / Lz
        d = amp * Q1[3] * k_eval_f(x, DIRECTION_G) / u ** 3 * nP / HBAR_GEV_SEC / NSCALE
        s = s.copy(); s[4] += d; s[5] -= d
    return s, t


def G_f(phase, s, y, amp, kc):
    if phase == "A":
        u = -s; src, t = src_f(u, amp, kc); c = 3 * DT_EDGE * u * u
    else:
        t = s; src = np.zeros(6); c = 1.0
    T = math.sqrt(1.32 / t)
    a, b, decay, l0, l1, nbs, g, ex = rates_f(T)
    X = y[0]; n = y[1:]
    D = decay + (l0 + l1 * X) * nbs
    F = np.concatenate([[g * ((1 - X) * ex - X) - X / TAU_N + np.sum(n * S * ((1 - X) * a - X * b))], src - D * n])
    J = np.zeros((7, 7))
    J[0, 0] = -g * (ex + 1) - 1 / TAU_N - S * np.sum(n * (a + b)); J[0, 1:] = S * ((1 - X) * a - X * b)
    J[1:, 0] = -l1 * nbs * n; J[1:, 1:] = np.diag(-D)
    return c * F, c * J


def solve(phase, y0, span, amp, kc, rtol):
    return solve_ivp(lambda s, y: G_f(phase, s, y, amp, kc)[0], span, y0, method="Radau", rtol=rtol, atol=rtol * 1e-3,
                     jac=lambda s, y: G_f(phase, s, y, amp, kc)[1], max_step=(.02 if phase == "A" else 2.), dense_output=True)


# ---------------------------------------------------------------- generic (interval / dual-interval) model
def rates_g(T):
    nB = K(ETA_B) * (2 * K(ZETA3) / K(iv.pi) ** 2) * (T / K(HBARC_MEV_CM)) ** 3
    def coul(m):
        ve = SQRT(T / K(m)) + SQRT(T / K(M_P_MEV)); z = 2 * K(iv.pi) * K(ALPHA) / ve
        return z / (1 - EXP(-z))
    fp = coul(139.57039); fk = coul(493.677)
    a = [K(1.5) * fp, K(0), K(31) * fk, K(7), K(0), K(28)]
    b = [K(0), K(1.7), K(26), K(7), K(28), K(0)]
    decay = [1 / K(2.6033e-8), 1 / K(2.6033e-8), K(8.1e7), K(2e7), K(0), K(0)]
    l0 = [a[0], K(0), K(45.5) * fk, K(17), K(37), K(28)]
    l1 = [-a[0], K(1.7), K(60) - K(45.5) * fk, K(0), K(-9), K(9)]
    x = K(Q_MEV) / T; g = (K(255) / K(TAU_N)) * (12 + 6 * x + x * x) / x ** 5
    return a, b, decay, l0, l1, nB * K(SIGMA_V_UNIT), g, EXP(-x)


def src_g(u, amp, kc, inside):
    t = K(T_EDGE_TIME) + K(DT_EDGE) * (1 - u ** 3)
    nP = K(NPBH0) * POW(K(T_EDGE_TIME) / t, 1.5)
    s = [K(Q1[INDEX[i]]) * nP / K(HBAR_GEV_SEC) * POW(u, float(SLOPES[INDEX[i]])) / K(NSCALE) for i in range(6)]
    if inside:
        x = (LOG(u) - K(ZM)) * (2 / Lz)
        k = k_eval(x, DIRECTION_G)
        d = K(amp) * K(Q1[3]) * k / u ** 3 * nP / K(HBAR_GEV_SEC) / K(NSCALE)
        s[4] = s[4] + d; s[5] = s[5] - d
    return s, t


def G_g(phase, s, y, amp, kc, inside):
    if phase == "A":
        u = -s; src, t = src_g(u, amp, kc, inside); c = 3 * K(DT_EDGE) * u * u
    else:
        t = s; src = [K(0)] * 6; c = K(1)
    T = SQRT(K(1.32) / t)
    a, b, decay, l0, l1, nbs, g, ex = rates_g(T)
    X = y[0]; n = y[1:]
    conv = K(0)
    for i in range(6):
        conv = conv + n[i] * K(S) * ((1 - X) * a[i] - X * b[i])
    F = [g * ((1 - X) * ex - X) - X / K(TAU_N) + conv]
    for i in range(6):
        F.append(src[i] - (decay[i] + (l0[i] + l1[i] * X) * nbs) * n[i])
    return [c * f for f in F], (a, b, l1, nbs, g, ex, c, decay, l0)


def J_and_quad_interval(phase, s, y, amp, kc, inside):
    """interval Jacobian bounds (upper diagonal, magnitude off-diagonal) and quadratic coefficients on a box."""
    _, (a, b, l1, nbs, g, ex, c, decay, l0) = G_g(phase, s, y, amp, kc, inside)
    X = y[0]; n = y[1:]
    sumn = I(0)
    for i in range(6):
        sumn = sumn + n[i] * (a[i] + b[i])
    diag = [up(c * (-g * (ex + 1) - 1 / I(TAU_N) - I(S) * sumn))]
    off = {}
    for i in range(6):
        off[(0, i + 1)] = mag(c * I(S) * ((1 - X) * a[i] - X * b[i]))
        off[(i + 1, 0)] = mag(c * l1[i] * nbs * n[i])
        diag.append(up(c * (-(decay[i] + (l0[i] + l1[i] * X) * nbs))))
    qx = [mag(c * I(S) * (a[i] + b[i])) for i in range(6)]
    qn = [mag(c * l1[i] * nbs) for i in range(6)]
    return diag, off, qx, qn


# ---------------------------------------------------------------- piece propagation (rigorous scalar comparison)
def psi(d, h):
    """(e^{d h} - 1)/d for an interval d (with d = 0 handled), interval-valued."""
    if mp.mpf(d.a) == 0 and mp.mpf(d.b) == 0:
        return h
    dh = d * h
    # stable for small |dh|: series bound if tiny
    if mp.mpf(abs(dh).b) < mp.mpf("1e-8"):
        return h * (1 + dh / 2 + dh * dh)        # crude enclosure: e^x - 1 = x(1 + x/2 + O(x^2)), |O| <= x^2 for |x|<1e-8
    return (iv.exp(dh) - 1) / d


def psi2(d, h):
    """int_0^h psi(d, t) dt = (psi(d,h) - h)/d, interval upper-safe."""
    if mp.mpf(d.a) == 0 and mp.mpf(d.b) == 0:
        return h * h / 2
    dh = d * h
    if mp.mpf(abs(dh).b) < mp.mpf("1e-8"):
        return h * h / 2 * (1 + abs(dh))
    return (psi(d, h) - h) / d


def propagate_piece(eps0, diag, off, rho, qx, qn, h, nvar, floor=iv.mpf("1e-300")):
    """Rigorous componentwise bound on one piece. Rows 1..nvar-1 (hadrons) couple only to row 0 (X); row 0 couples to all.
    Bootstrap levels Phi bound |e| on the WHOLE piece; accepted only under strict inclusion.
    Returns (endpoint bound, piece-supremum bound)."""
    Phi = [up(e * iv.mpf("1.000000001") + floor) for e in eps0]
    one = iv.mpf(1)
    for _ in range(400):
        end, sup, integ = [None] * nvar, [None] * nvar, [None] * nvar
        for i in range(1, nvar):
            d = diag[i] + qn[i - 1] * Phi[0]
            f = rho[i] + off.get((i, 0), iv.mpf(0)) * Phi[0]
            end[i] = up(iv.exp(d * h) * eps0[i] + f * psi(d, h))
            sup[i] = up(iv.mpf([0, max(mp.mpf(eps0[i].b), mp.mpf(end[i].b))]))
            integ[i] = up(eps0[i] * psi(diag[i] + qn[i - 1] * Phi[0], h) + f * psi2(d, h))     # >= int_0^h |e_i|
        d0 = diag[0]
        growth = up(iv.mpf([0, max(mp.mpf(1), mp.mpf(iv.exp(d0 * h).b))]))
        coupling = iv.mpf(0)
        for j in range(1, nvar):
            coupling = coupling + (off.get((0, j), iv.mpf(0)) + qx[j - 1] * Phi[0]) * integ[j]
        end[0] = up(iv.exp(d0 * h) * eps0[0] + rho[0] * psi(d0, h) + growth * coupling)
        sup[0] = up(growth * (eps0[0] + rho[0] * h + coupling))
        if all(lt(sup[i], Phi[i]) for i in range(nvar)):
            return end, sup
        Phi = [up(iv.mpf(max(mp.mpf(Phi[i].b), mp.mpf(sup[i].b) * mp.mpf("1.000001") + mp.mpf("1e-300")))) for i in range(nvar)]
    raise RuntimeError("bootstrap did not close")


# ---------------------------------------------------------------- certify a Radau trajectory
def piece_enclosures(phase, s0, h, Q, yo, a0, a1, amp, kc, inside):
    order = Q.shape[1]
    P = iv.mpf([a0, a1]); hI = I(h); s0I = I(s0)
    def yv(th):
        return [I(yo[k]) + sum(I(Q[k, j]) * th ** (j + 1) for j in range(order)) for k in range(7)]
    def yd(th):
        return [sum(I(Q[k, j]) * (j + 1) * th ** j for j in range(order)) / hI for k in range(7)]
    def ydd(th):
        return [sum(I(Q[k, j]) * (j + 1) * j * (th ** (j - 1) if j >= 1 else I(0)) for j in range(order)) / hI ** 2 for k in range(7)]
    tm = I(0.5 * (a0 + a1))
    Gm, _ = G_g(phase, s0I + tm * hI, yv(tm), amp, kc, inside)
    ydm = yd(tm)
    rm = [ydm[k] - Gm[k] for k in range(7)]
    yD = [DI(v, dv * hI) for v, dv in zip(yv(P), yd(P))]
    MODE["dual"] = True
    try:
        GD, _ = G_g(phase, DI(s0I + P * hI, hI), yD, amp, kc, inside)
    finally:
        MODE["dual"] = False
    yddP = ydd(P)
    rho = [mag(rm[k] + (yddP[k] * hI - GD[k].d) * (P - tm)) for k in range(7)]
    diag, off, qx, qn = J_and_quad_interval(phase, s0I + P * hI, yv(P), amp, kc, inside)
    return rho, diag, off, qx, qn


def certify(phase, sol, amp, kc, eps0, sub=8, tol_piece=3e-12, maxdepth=6):
    """certify along the Radau collocation polynomials; pieces are refined adaptively (bisection) where the estimated
    X-error contribution of the hadron defect enclosures exceeds tol_piece (enclosure overestimation is O(|P|^2))."""
    eps = [up(I(float(e)) if not isinstance(e, iv.mpf) else e) for e in eps0]
    breaks = [-0.92, -0.07] if phase == "A" else []
    stats = {"pieces": 0, "refinements": 0}
    max_rho = [mp.mpf(0)] * 7

    def process(s0, h, Q, yo, a0, a1, depth):
        nonlocal eps
        u_mid = -(s0 + 0.5 * (a0 + a1) * h)
        inside = (phase == "A") and (0.07 < u_mid < 0.92)
        rho, diag, off, qx, qn = piece_enclosures(phase, s0, h, Q, yo, a0, a1, amp, kc, inside)
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
        eps, _ = propagate_piece(eps, diag, off, rho, qx, qn, I(hp), 7)
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


# ---------------------------------------------------------------- AUD1 countermodels
def test_aud1_bootstrap():
    """x' = -10x + 100n + 10xn, n' = -10n, yhat = 0, eps0 = (0, 1): bound must cover x(1) = 0.0051380657..."""
    true_x1 = 100 * math.exp(-10) * quad(lambda s: math.exp(math.exp(-10 * s) - math.exp(-10)), 0, 1, epsabs=1e-15)[0]
    out = {"true_x(1)": true_x1}
    for npieces in (1, 10, 100, 1000):
        eps = [iv.mpf(0), iv.mpf(1)]
        h = I(1) / npieces
        try:
            for _ in range(npieces):
                eps, sup = propagate_piece(eps, [iv.mpf(-10), iv.mpf(-10)], {(0, 1): iv.mpf(100)}, [iv.mpf(0), iv.mpf(0)],
                                           [iv.mpf(10)], [iv.mpf(0)], h, 2)
            out[f"bound_x(1)_{npieces}_pieces"] = float(mp.mpf(eps[0].b))
        except RuntimeError:
            out[f"refused_{npieces}_pieces"] = "bootstrap did not close (no bound issued)"
    return out


def test_aud1_sampled_zero():
    """y' = -y + g(t), yhat = 0, g = p^2/int p^2, p = prod_{j=0}^{8}(8t - j): g vanishes on 5- and 9-point grids."""
    import sympy as sps
    t = sps.symbols("t"); p = 1
    for j in range(9):
        p *= (8 * t - j)
    norm = sps.integrate(sps.expand(p ** 2), (t, 0, 1))
    normI = I(sps.Rational(norm).p) / I(sps.Rational(norm).q)
    def g_int(P):                                   # product form keeps the enclosure tight
        v = I(1)
        for j in range(9):
            v = v * (8 * P - j)
        return v * v / normI
    nf = float(norm)
    gf = lambda x: float(np.prod([8 * x - j for j in range(9)])) ** 2 / nf
    true_y1 = quad(lambda x: math.exp(-(1 - x)) * gf(x), 0, 1, epsabs=1e-13, limit=500, points=[k / 8 for k in range(1, 8)])[0]
    out = {"true_y(1)": true_y1, "sampled_defect_on_5_and_9_grids": [gf(k / 4) for k in range(5)] + [gf(k / 8) for k in range(9)]}
    for npieces in (16, 64, 256, 1024):
        eps = [iv.mpf(0)]
        for m in range(npieces):
            P = iv.mpf([m / npieces, (m + 1) / npieces])
            rho = [mag(g_int(P))]                          # natural enclosure of the defect |0 - (-0 + g)|
            eps, _ = propagate_piece(eps, [iv.mpf(-1)], {}, rho, [], [], I(1) / npieces, 1)
        out[f"bound_y(1)_{npieces}_pieces"] = float(mp.mpf(eps[0].b))
    return out


# ---------------------------------------------------------------- demo (same as v1 r1 synthetic setting)
def run(amp, kc, rtol):
    y0 = np.zeros(7); y0[0] = X_EDGE
    solA = solve("A", y0, (-1.0, -U_CUT), amp, kc, rtol)
    t_cut = T_EDGE_TIME + DT_EDGE * (1 - U_CUT ** 3); t_eval = 1.32 / T_NUC ** 2
    solB = solve("B", solA.y[:, -1], (t_cut, t_eval), amp, kc, rtol)
    return solA, solB


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--v1json", required=True)
    args = ap.parse_args(); out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
    v1 = json.loads(Path(args.v1json).read_text())
    direction = v1["synthetic"]["direction_a_l(l=3..10)"]; amp = v1["synthetic"]["amp"]
    kc = kcoeffs(direction)
    DIRECTION_G[:] = list(direction)
    res = {"aud1_bootstrap_countermodel": test_aud1_bootstrap(), "aud1_sampled_zero_countermodel": test_aud1_sampled_zero()}
    runs = {}
    for sgn in (+1, -1):
        solA, solB = run(sgn * amp, kc, 3e-9)
        refA, refB = run(sgn * amp, kc, 1e-13)
        epsA, infA = certify("A", solA, sgn * amp, kc, [0.0] * 7)
        epsB, infB = certify("B", solB, sgn * amp, kc, epsA)
        X = float(solB.y[0, -1]); Xref = float(refB.y[0, -1])
        runs[str(sgn)] = {"X_nuc_rtol3e-9": X, "X_nuc_ref_rtol1e-13": Xref, "diagnostic_error": abs(X - Xref),
                          "bound_eps_X_v2": float(mp.mpf(epsB[0].b)), "bound_eps_X_after_phaseA": float(mp.mpf(epsA[0].b)),
                          "phaseA": infA, "phaseB": infB}
    half_gap = abs(runs["1"]["X_nuc_rtol3e-9"] - runs["-1"]["X_nuc_rtol3e-9"]) / 2
    floor = half_gap - (runs["1"]["bound_eps_X_v2"] + runs["-1"]["bound_eps_X_v2"]) / 2
    res.update({"runs": runs, "half_gap_numeric": half_gap, "two_point_floor_v2": floor, "amp": amp, "direction": direction})
    b = res["aud1_bootstrap_countermodel"]; z = res["aud1_sampled_zero_countermodel"]
    res["verdict"] = {
        "covers_aud1_bootstrap_countermodel": all(b[k] >= b["true_x(1)"] for k in b if k.startswith("bound")),
        "covers_aud1_sampled_zero_countermodel": all(z[k] >= z["true_y(1)"] for k in z if k.startswith("bound")),
        "covers_diagnostic_error": all(r["bound_eps_X_v2"] >= r["diagnostic_error"] for r in runs.values()),
        "two_point_floor_positive": floor > 0,
    }
    res["code_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    (out / "mech7d_interval_certificate_v2.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
