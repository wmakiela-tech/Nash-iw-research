#!/usr/bin/env python3
"""Independent cross-family check of MT14 ROT012 (Badacz, Claude thread).

Target: MT14 ROT012 bracket 4.87e-6 < m_B < 4.904e-6, where
  m_B = inf_{a,b in [0,.2], |a-b|>=.01} rho^2(a,b),  rho^2 = 1 - p^2/(P Q).
Source: research/m13/2026-10-26/direct_B.json (M13 owner data, public).

Independent route (does NOT use MT14 ROT011 nearest-boundary theorem, nor the
divided-difference factorisation of ROT012): a direct two-dimensional exact
Bernstein certificate on the whole legal triangle.
  By symmetry rho^2(a,b) = rho^2(b,a), so it suffices to take b >= a + 1/100.
  Duffy-type map of the unit square onto the triangle:
     alpha = 19 u/100,  beta = (1 + 19 u + 19 w - 19 u w)/100,  u,w in [0,1].
  For a level m, G_m(u,w) = sum_{i<j} w_i w_j M_ij^2 - m P(alpha) Q(beta),
  M_ij = s_i(alpha) s_j(beta) - s_j(alpha) s_i(beta)  (Lagrange identity:
  sum w_i w_j M_ij^2 = P Q - p^2). rho^2 >= m on the legal set iff G_m >= 0.
  G_m has bidegree (16, 8) in (u, w). Its Bernstein coefficients are computed
  exactly (Fractions), rounded to dyadic integers (error tracked), then
  subdivided by exact integer de Casteljau. A leaf is certified when every
  Bernstein coefficient >= E, where E bounds the effect of the coefficient
  uncertainty radius plus the dyadic rounding.
Also: exact rational rho^2(1/5, 19/100), float scan for the argmin, shell
positivity, check of MT14's nine-decimal boxes, and the Gaussian resource
formula (closed form + Monte Carlo).
"""
import json, sys, time, argparse, hashlib, math, random
from fractions import Fraction as Fr
from math import comb

ap = argparse.ArgumentParser()
ap.add_argument("--src", default="research/m13/2026-10-26/direct_B.json")
ap.add_argument("--out", required=True)
args = ap.parse_args()

raw = open(args.src, "rb").read()
src_sha = hashlib.sha256(raw).hexdigest()
D = json.loads(raw)
N = 41
keys = ["2", "3", "4", "5", "6"]
nk = [(N - 2 * int(k)) ** 3 for k in keys]
w = [nk[i] - nk[i + 1] for i in range(4)] + [nk[4]]
assert nk == [50653, 42875, 35937, 29791, 24389] and w == [7778, 6938, 6146, 5402, 24389]
SC = Fr(10) ** 14  # scale (exact)


def parse_entry(e):
    vals = []
    for s in e:
        a, b = s.strip()[1:-1].split(",")
        vals += [Fr(a.strip()), Fr(b.strip())]
    return min(vals) * SC, max(vals) * SC


G_LO, G_HI = [], []
for k in keys:
    lo, hi = zip(*[parse_entry(e) for e in D[k]])
    G_LO.append(list(lo)); G_HI.append(list(hi))

# shell coefficients s_i = (n_i g_i - n_{i+1} g_{i+1}) / w_i, s_4 = g_4 (linear map, exact)
def shells(G):
    S = []
    for i in range(4):
        S.append([(nk[i] * G[i][c] - nk[i + 1] * G[i + 1][c]) / w[i] for c in range(5)])
    S.append(list(G[4]))
    return S


def shell_ball(Glo, Ghi):
    """midpoint + radius of shell coefficients from coefficient intervals (exact)."""
    Gm = [[(Glo[i][c] + Ghi[i][c]) / 2 for c in range(5)] for i in range(5)]
    Gr = [[(Ghi[i][c] - Glo[i][c]) / 2 for c in range(5)] for i in range(5)]
    Sm = shells(Gm)
    Sr = []
    for i in range(4):
        Sr.append([(nk[i] * Gr[i][c] + nk[i + 1] * Gr[i + 1][c]) / w[i] for c in range(5)])
    Sr.append(list(Gr[4]))
    return Sm, Sr


res = {"source": args.src, "source_sha256": src_sha, "w": w, "n": nk}

# ---------- MT14 nine-decimal boxes: C_ij = round(1e14 c, 9), radius 1e-8 ----------
C9 = [[Fr(round((G_LO[i][c] + G_HI[i][c]) / 2 * 10**9), 10**9) for c in range(5)] for i in range(5)]
inbox = sum(1 for i in range(5) for c in range(5)
            for x in (G_LO[i][c], G_HI[i][c]) if abs(x - C9[i][c]) <= Fr(1, 10**8))
res["mt14_box_check"] = {"endpoints_inside_C_pm_1e-8": inbox, "of": 50,
                         "note": "each source coefficient interval has 2 distinct directed endpoints (4 strings, pairwise equal)",
                         "max_source_halfwidth_scaled": float(max((G_HI[i][c] - G_LO[i][c]) / 2 for i in range(5) for c in range(5))),
                         "max_center_minus_C9": float(max(abs((G_LO[i][c] + G_HI[i][c]) / 2 - C9[i][c]) for i in range(5) for c in range(5)))}

# ---------- polynomial helpers (bivariate dict-free: list of lists [i][j] for u^i w^j) ----------
def pzero(n, m):
    return [[Fr(0)] * (m + 1) for _ in range(n + 1)]


def padd(A, B, cb=1):
    n = max(len(A), len(B)) - 1; m = max(len(A[0]), len(B[0])) - 1
    R = pzero(n, m)
    for i, r in enumerate(A):
        for j, x in enumerate(r):
            R[i][j] += x
    for i, r in enumerate(B):
        for j, x in enumerate(r):
            R[i][j] += cb * x
    return R


def pmul(A, B):
    R = pzero(len(A) + len(B) - 2, len(A[0]) + len(B[0]) - 2)
    for i, r in enumerate(A):
        for j, x in enumerate(r):
            if x == 0:
                continue
            for k, r2 in enumerate(B):
                for l, y in enumerate(r2):
                    if y:
                        R[i + k][j + l] += x * y
    return R


def pscale(A, c):
    return [[c * x for x in r] for r in A]


ALPHA = [[Fr(0)], [Fr(19, 100)]]                       # 19u/100
BETA = [[Fr(1, 100), Fr(19, 100)], [Fr(19, 100), Fr(-19, 100)]]  # (1+19u+19w-19uw)/100


def compose(coef, X):
    R = [[Fr(0)]]
    Pk = [[Fr(1)]]
    for c in coef:
        R = padd(R, pscale(Pk, c))
        Pk = pmul(Pk, X)
    return R


def pabs(A):
    return [[abs(x) for x in r] for r in A]


def bmul(A, B):
    """ball polynomial product: (mid, rad) with rad coefficients >= 0."""
    (Am, Ar), (Bm, Br) = A, B
    mid = pmul(Am, Bm)
    rad = padd(padd(pmul(pabs(Am), Br), pmul(Ar, pabs(Bm))), pmul(Ar, Br))
    return mid, rad


def bcompose(cm, cr, X):
    mid = [[Fr(0)]]; rad = [[Fr(0)]]
    Pk = [[Fr(1)]]
    for c, r in zip(cm, cr):
        mid = padd(mid, pscale(Pk, c))
        rad = padd(rad, pscale(pabs(Pk), r))
        Pk = pmul(Pk, X)
    return mid, rad


def build_G(Sm, Sr, m):
    """G = sum w_i w_j M_ij^2 - m P Q as a ball polynomial in (u, w)."""
    sa = [bcompose(Sm[i], Sr[i], ALPHA) for i in range(5)]
    sb = [bcompose(Sm[i], Sr[i], BETA) for i in range(5)]
    Gm = [[Fr(0)]]; Gr = [[Fr(0)]]
    for i in range(5):
        for j in range(i + 1, 5):
            X1 = bmul(sa[i], sb[j]); X2 = bmul(sa[j], sb[i])
            Mij = (padd(X1[0], X2[0], -1), padd(X1[1], X2[1]))
            M2 = bmul(Mij, Mij)
            Gm = padd(Gm, pscale(M2[0], w[i] * w[j])); Gr = padd(Gr, pscale(M2[1], w[i] * w[j]))
    P = ([[Fr(0)]], [[Fr(0)]]); Q = ([[Fr(0)]], [[Fr(0)]])
    for i in range(5):
        a2 = bmul(sa[i], sa[i]); b2 = bmul(sb[i], sb[i])
        P = (padd(P[0], pscale(a2[0], w[i])), padd(P[1], pscale(a2[1], w[i])))
        Q = (padd(Q[0], pscale(b2[0], w[i])), padd(Q[1], pscale(b2[1], w[i])))
    PQ = bmul(P, Q)
    Gm = padd(Gm, pscale(PQ[0], m), -1); Gr = padd(Gr, pscale(PQ[1], m))
    return Gm, Gr


def peval(A, u, v):
    return sum(x * u**i * v**j for i, r in enumerate(A) for j, x in enumerate(r))


def to_bernstein(G):
    n = len(G) - 1; m = len(G[0]) - 1
    B = pzero(n, m)
    for i in range(n + 1):
        for j in range(m + 1):
            s = Fr(0)
            for k in range(i + 1):
                ck = Fr(comb(i, k), comb(n, k))
                for l in range(j + 1):
                    if G[k][l]:
                        s += ck * Fr(comb(j, l), comb(m, l)) * G[k][l]
            B[i][j] = s
    return B


# ---------- exact integer de Casteljau subdivision ----------
KBITS = 200


def split_u(B, n):
    """B: list of rows over u (len n+1), each row list over w. returns (L, R) scaled by 2^n."""
    m1 = len(B[0])
    L = [[0] * m1 for _ in range(n + 1)]; R = [[0] * m1 for _ in range(n + 1)]
    for j in range(m1):
        y = [B[i][j] << n for i in range(n + 1)]
        L[0][j] = y[0]; R[n][j] = y[n]
        for r in range(1, n + 1):
            for i in range(n - r + 1):
                y[i] = (y[i] + y[i + 1]) >> 1
            L[r][j] = y[0]; R[n - r][j] = y[n - r]
    return L, R


def split_w(B, m):
    L = []; R = []
    for row in B:
        y = [x << m for x in row]
        l = [0] * (m + 1); rr = [0] * (m + 1)
        l[0] = y[0]; rr[m] = y[m]
        for r in range(1, m + 1):
            for i in range(m - r + 1):
                y[i] = (y[i] + y[i + 1]) >> 1
            l[r] = y[0]; rr[m - r] = y[m - r]
        L.append(l); R.append(rr)
    return L, R


def certify_level(S_mid, S_rad, m, maxleaves=2_000_000, label=""):
    t0 = time.time()
    G, Grad = build_G(S_mid, S_rad, m)
    n = len(G) - 1; mm = len(G[0]) - 1
    # self-check of the polynomial against a direct evaluation at random exact points
    rng = random.Random(7)
    for _ in range(12):
        u = Fr(rng.randrange(0, 1001), 1000); v = Fr(rng.randrange(0, 1001), 1000)
        al = Fr(19, 100) * u; be = (1 + 19 * u + 19 * v - 19 * u * v) / 100
        sa = [sum(S_mid[i][k] * al**k for k in range(5)) for i in range(5)]
        sb = [sum(S_mid[i][k] * be**k for k in range(5)) for i in range(5)]
        P_ = sum(w[i] * sa[i] ** 2 for i in range(5)); Q_ = sum(w[i] * sb[i] ** 2 for i in range(5))
        p_ = sum(w[i] * sa[i] * sb[i] for i in range(5))
        assert peval(G, u, v) == P_ * Q_ - p_ * p_ - m * P_ * Q_, "polynomial self-check failed"
    B = to_bernstein(G)
    RND = Fr(1, 2 ** (KBITS + 1))
    E = peval(Grad, Fr(1), Fr(1)) + RND  # global (reported only)
    Bi = [[round(x * 2 ** KBITS) for x in r] for r in B]
    stack = [(Bi, KBITS, Fr(0), Fr(1), Fr(0), Fr(1), 0)]
    leaves = 0; maxdepth = 0; minlead = None
    while stack:
        Bc, e, u0, u1, w0, w1, d = stack.pop()
        thr = math.ceil((peval(Grad, u1, w1) + RND) * 2 ** e)  # rad poly has coeffs >= 0: max at (u1, w1)
        mn = min(min(r) for r in Bc)
        if mn >= thr:
            leaves += 1; maxdepth = max(maxdepth, d)
            v = Fr(mn, 2 ** e)
            if minlead is None or v < minlead[0]:
                minlead = (v, (u0, u1, w0, w1))
            if leaves > maxleaves:
                return {"verdict": False, "reason": "leaf budget"}
            continue
        corners = [Bc[0][0], Bc[0][-1], Bc[-1][0], Bc[-1][-1]]
        cpts = [(u0, w0), (u0, w1), (u1, w0), (u1, w1)]
        cthr = [math.ceil((peval(Grad, cu, cw) + RND) * 2 ** e) for cu, cw in cpts]
        if any(c < t for c, t in zip(corners, cthr)):  # value at a point within its own uncertainty: give up
            return {"verdict": False, "reason": "corner value below threshold",
                    "box_u": [float(u0), float(u1)], "box_w": [float(w0), float(w1)],
                    "corner_values": [float(Fr(c, 2 ** e)) for c in corners], "local_E": float(Fr(thr, 2 ** e))}
        if d > 60:
            return {"verdict": False, "reason": "depth"}
        # split along the direction with larger coefficient spread per unit degree
        du = max(abs(Bc[i + 1][j] - Bc[i][j]) for i in range(n) for j in range(mm + 1))
        dw = max(abs(Bc[i][j + 1] - Bc[i][j]) for i in range(n + 1) for j in range(mm))
        if du * n >= dw * mm:
            L, R = split_u(Bc, n); um = (u0 + u1) / 2
            stack.append((L, e + n, u0, um, w0, w1, d + 1)); stack.append((R, e + n, um, u1, w0, w1, d + 1))
        else:
            L, R = split_w(Bc, mm); wm = (w0 + w1) / 2
            stack.append((L, e + mm, u0, u1, w0, wm, d + 1)); stack.append((R, e + mm, u0, u1, wm, w1, d + 1))
    return {"verdict": True, "level_m": str(m), "level_m_float": float(m), "leaves": leaves,
            "max_depth": maxdepth, "global_E_rad_poly_at_(1,1)": float(E), "polynomial_self_check_points": 12,
            "bidegree": [n, mm],
            "smallest_leaf_min_bernstein": float(minlead[0]),
            "smallest_leaf_box_u": [float(minlead[1][0]), float(minlead[1][1])],
            "smallest_leaf_box_w": [float(minlead[1][2]), float(minlead[1][3])]}


# ---------- shell positivity on [0, 1/5] (exact Bernstein, univariate) ----------
def shell_positive(S_mid, S_rad):
    out = []
    for i in range(5):
        c = [S_mid[i][k] * Fr(1, 5) ** k for k in range(5)]  # x = t/5
        b = [sum(Fr(comb(j, k), comb(4, k)) * c[k] for k in range(j + 1)) for j in range(5)]
        e = sum(S_rad[i][k] * Fr(1, 5) ** k for k in range(5))
        out.append({"min_bernstein": float(min(b)), "radius_bound": float(e), "positive": bool(min(b) > e)})
    return out


def rho2_exact(S, a, b):
    sa = [sum(S[i][k] * a**k for k in range(5)) for i in range(5)]
    sb = [sum(S[i][k] * b**k for k in range(5)) for i in range(5)]
    P = sum(w[i] * sa[i] ** 2 for i in range(5)); Q = sum(w[i] * sb[i] ** 2 for i in range(5))
    p = sum(w[i] * sa[i] * sb[i] for i in range(5))
    lag = sum(w[i] * w[j] * (sa[i] * sb[j] - sa[j] * sb[i]) ** 2 for i in range(5) for j in range(i + 1, 5))
    assert lag == P * Q - p * p
    return 1 - p * p / (P * Q), p > 0


# ===================== run =====================
S_lo = shells(G_LO); S_hi = shells(G_HI)
S_mid, S_rad = shell_ball(G_LO, G_HI)
S_c9 = shells(C9)
S_c9_rad = shell_ball([[x - Fr(1, 10**8) for x in r] for r in C9], [[x + Fr(1, 10**8) for x in r] for r in C9])[1]

res["shell_positivity_source"] = shell_positive(S_mid, S_rad)
res["shell_positivity_mt14_box"] = shell_positive(S_c9, S_c9_rad)

# C1: exact rho^2 at the claimed hard pair
claimed_lo, claimed_hi = Fr("4.903744074886575e-6"), Fr("4.903774041472931e-6")
c1 = {}
for name, S in (("lo_endpoints", S_lo), ("hi_endpoints", S_hi), ("midpoints", S_mid), ("mt14_C9_centres", S_c9)):
    r, ppos = rho2_exact(S, Fr(1, 5), Fr(19, 100))
    c1[name] = {"rho2": float(r), "rho2_30digits": f"{r.numerator * 10**30 // r.denominator}e-30",
                "inside_claimed_enclosure": bool(claimed_lo < r < claimed_hi), "p_positive": bool(ppos)}
res["C1_hard_pair_exact"] = c1

# C2a: float scan of the legal triangle (non-rigorous locator)
import numpy as np
Sf = np.array([[float(x) for x in r] for r in S_mid])
wf = np.array(w, float)


def rho2_np(a, b):
    sa = np.stack([np.polyval(Sf[i][::-1], a) for i in range(5)])
    sb = np.stack([np.polyval(Sf[i][::-1], b) for i in range(5)])
    lag = 0
    for i in range(5):
        for j in range(i + 1, 5):
            lag = lag + wf[i] * wf[j] * (sa[i] * sb[j] - sa[j] * sb[i]) ** 2
    P = (wf[:, None] * sa**2).sum(0); Q = (wf[:, None] * sb**2).sum(0)
    return lag / (P * Q)


h = 0.0002
A, Bv = np.meshgrid(np.arange(0, 0.19 + 1e-12, h), np.arange(0.01, 0.2 + 1e-12, h), indexing="ij")
mask = Bv >= A + 0.01 - 1e-12
Rg = rho2_np(A[mask], Bv[mask])
k = int(np.argmin(Rg))
amin, bmin = float(A[mask][k]), float(Bv[mask][k])
# boundary curve rho^2(alpha, alpha+.01) and per-alpha check that min over beta is at nearest boundary
alphas = np.arange(0, 0.19 + 1e-12, 0.001)
viol = 0
for a in alphas:
    bs = np.arange(a + 0.01, 0.2 + 1e-12, 0.0005)
    r = rho2_np(np.full_like(bs, a), bs)
    if np.argmin(r) != 0:
        viol += 1
for a in np.arange(0.01, 0.2 + 1e-12, 0.001):  # left side beta <= alpha - .01
    bs = np.arange(a - 0.01, -1e-12, -0.0005)
    r = rho2_np(np.full_like(bs, a), bs)
    if np.argmin(r) != 0:
        viol += 1
res["C2a_float_scan"] = {"grid_step": h, "points": int(mask.sum()), "argmin_alpha_beta": [amin, bmin],
                         "min_rho2": float(Rg[k]),
                         "nearest_boundary_violations_on_1e-3_alpha_grid_both_sides": viol,
                         "note": "non-rigorous locator only"}

# C2b: rigorous 2D certificates (independent of ROT011)
levels = [("mt14_box", S_c9, S_c9_rad, Fr(487, 10**8)),
          ("mt14_box", S_c9, S_c9_rad, Fr(489, 10**8)),
          ("source", S_mid, S_rad, Fr(487, 10**8)),
          ("source", S_mid, S_rad, Fr(49037, 10**10)),
          ("source", S_mid, S_rad, Fr(4903759, 10**12)),
          ("source", S_mid, S_rad, Fr(490375906, 10**14)),
          # negative controls: levels ABOVE the attained value must be refused
          ("source", S_mid, S_rad, Fr(49037591, 10**13)),
          ("mt14_box", S_c9, S_c9_rad, Fr(4904, 10**9))]
c2b = []
for lab, Sm_, Sr_, m in levels:
    r = certify_level(Sm_, Sr_, m, label=lab)
    r["coefficients"] = lab
    c2b.append(r)
    print(lab, float(m), r.get("verdict"), r.get("leaves"), flush=True)
res["C2b_rigorous_2d_lower"] = c2b

# C3: Gaussian resource
from statistics import NormalDist
z = NormalDist().inv_cdf(0.75)
thr = 4 * z * z / 4.904e-6
r2 = float(c1["midpoints"]["rho2"])
rng = random.Random(20261029)
# Monte Carlo of the simple-vs-simple Gaussian test in the 5-shell W metric (whitened)
a = np.array([float(sum(S_mid[i][c] * Fr(1, 5) ** c for c in range(5))) for i in range(5)])
b = np.array([float(sum(S_mid[i][c] * Fr(19, 100) ** c for c in range(5))) for i in range(5)])
Wh = np.sqrt(wf)
P_ = float((wf * a * a).sum()); p_ = float((wf * a * b).sum()); Q_ = float((wf * b * b).sum())
nSNR2 = 2 * 4 * z * z / r2  # pick a budget giving d = 2*sqrt(2)*z -> P = Phi(sqrt(2) z)
tau = 1.0; t = math.sqrt(nSNR2 * tau**2 / P_)  # n=1 replicate with this SNR^2
mu1 = Wh * t * a; mu0 = Wh * (t * p_ / Q_) * b
npr = np.random.default_rng(20261029)
M = 200000
lab = npr.integers(0, 2, M)
X = np.where(lab[:, None] == 1, mu1, mu0) + npr.standard_normal((M, 5)) * tau
stat = X @ (mu1 - mu0) - 0.5 * (mu1 @ mu1 - mu0 @ mu0)
acc = float(np.mean((stat > 0) == (lab == 1)))
pred = NormalDist().cdf(math.sqrt(nSNR2 * r2) / 2)
res["C3_gaussian"] = {"Phi_inv_0.75": z, "threshold_4z2_over_4.904e-6": thr,
                      "claimed": 371073.75, "match": abs(thr - 371073.75) < 0.01,
                      "mc_budget_nSNR2": nSNR2, "mc_success": acc, "closed_form_success": pred,
                      "mc_abs_diff": abs(acc - pred), "mc_samples": M}

res["verdicts"] = {
    "C1_hard_pair_in_enclosure": all(v["inside_claimed_enclosure"] for k_, v in c1.items() if k_ != "mt14_C9_centres") and c1["mt14_C9_centres"]["inside_claimed_enclosure"],
    "C2b_lower_4.87e-6_on_mt14_box": bool(c2b[0]["verdict"]),
    "C2b_lower_4.89e-6_on_mt14_box": bool(c2b[1]["verdict"]),
    "C2b_lower_4.87e-6_on_source": bool(c2b[2]["verdict"]),
    "C2b_lower_4.9037e-6_on_source": bool(c2b[3]["verdict"]),
    "C2b_lower_4.903759e-6_on_source": bool(c2b[4]["verdict"]),
    "C2b_lower_4.90375906e-6_on_source": bool(c2b[5]["verdict"]),
    "NEG_control_4.9037591e-6_source_refused": not c2b[6]["verdict"],
    "NEG_control_4.904e-6_mt14_box_refused": not c2b[7]["verdict"],
    "C3_threshold": bool(res["C3_gaussian"]["match"]),
    "C3_mc_within_3sigma": bool(res["C3_gaussian"]["mc_abs_diff"] < 3 * math.sqrt(0.25 / M)),
    "shells_positive": all(x["positive"] for x in res["shell_positivity_source"] + res["shell_positivity_mt14_box"]),
}
json.dump(res, open(args.out, "w"), indent=1, sort_keys=True)
print(json.dumps(res["verdicts"], indent=1))
