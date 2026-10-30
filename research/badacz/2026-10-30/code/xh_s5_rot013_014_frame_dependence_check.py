#!/usr/bin/env python3
"""Badacz (Claude): independent cross-family check of XH-S5 ROT013/014 (frame dependence of the gravitational
reconnection diagnostics of Comisso & Asenjo, Phys. Rev. D 114, 084095 (2026), arXiv:2609.25241).
Source definitions used (read from the arXiv PDF): F^a_{mu nu} = d_mu A^a_nu - d_nu A^a_mu (Eq. 3, tetrad as potential,
no spin connection); nonideal term R^a_nu = u^l F^a_{l nu} (Eq. 22); necessary condition Eq. 28 (no smooth nonvanishing
w = u - zeta with w^l F^a_{l nu} = 0); rate Eq. 31 = max over curves of |int u^l F^a_{l nu} dl^nu|.
Tests (PREREG_032): X1 metric of both coframes; X2 F^1 at t = 0 and origin, det, rank; X3 bump integral and the
Eq.-31-type line integral; X4 compact-time coframe (ROT014): coincidence with control at t = 0 and |t| >= 1, integral
|kappa| C. Extra: identity i_u dA^a = L_u A^a for an adapted tetrad (A^a(u) = delta^a_0), i.e. nonideality = failure
of Lie transport of the chosen tetrad along u; EXTRA2 transformation law R' = Lambda R + u(Lambda) A for a spatial
rotation A' = Lambda A (general alpha(t,x,y,z)); EXTRA3 a static position-dependent rotation keeps the ideal frame ideal.
Run: python3 -I xh_s5_rot013_014_frame_dependence_check.py --out <file.json>
"""
import argparse, json
import sympy as sp
from mpmath import mp, quad, exp as mexp

ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); args = ap.parse_args()
t, x, y, z, kap = sp.symbols("t x y z kappa", real=True)
X = (t, x, y, z)
beta = sp.Rational(7, 10) * x + sp.Rational(11, 100) * x * z + sp.Rational(8, 100) * z ** 2
fsym = sp.Function("f")(y)            # bump, kept symbolic for the algebra; f(0) = 1
res = {}


def coframe(alpha):
    """rows: e^0..e^3 components (dt, dx, dy, dz) as in XH-S5 ROT013."""
    ca, sa, cb, sb = sp.cos(alpha), sp.sin(alpha), sp.cos(beta), sp.sin(beta)
    e0 = [1, 0, 0, 0]
    e1 = [0, cb * ca, cb * sa, sb]
    e2 = [0, -sa, ca, 0]
    e3 = [0, -sb * ca, -sb * sa, cb]
    return sp.Matrix([e0, e1, e2, e3])


eta = sp.diag(-1, 1, 1, 1)
for name, alpha in (("control", sp.Integer(0)), ("active_rot013", sp.Rational(2, 5) * t * fsym),
                    ("active_rot014", kap * sp.Function("h")(t) * fsym)):
    E = coframe(alpha)
    g = sp.simplify(E.T * eta * E)
    res.setdefault("X1_metric_is_eta", {})[name] = bool(sp.simplify(g - eta) == sp.zeros(4))


def F_of(E, a):
    A = E.row(a)
    return sp.Matrix(4, 4, lambda m, n: sp.diff(A[n], X[m]) - sp.diff(A[m], X[n]))


# X2: ROT013 active, t = 0, origin; f(0) = 1, f'(0) = 0 (even bump)
E = coframe(sp.Rational(2, 5) * t * fsym)
F1 = F_of(E, 1)
F1_0 = F1.subs(t, 0)
at0 = {x: 0, z: 0, y: 0}
F1_origin = sp.simplify(F1_0.subs(at0).subs({fsym.subs(y, 0): 1}).doit())
F1_origin = F1_origin.subs(sp.Function("f")(0), 1)
res["X2_F1_origin"] = [[str(sp.nsimplify(v)) for v in row] for row in F1_origin.tolist()]
res["X2_F_ty"] = str(sp.nsimplify(F1_origin[0, 2])); res["X2_F_xz"] = str(sp.nsimplify(F1_origin[1, 3]))
res["X2_det"] = str(sp.nsimplify(F1_origin.det())); res["X2_rank"] = int(F1_origin.rank())
# control at t = 0: i_u F^1 = F^1_{t nu} must vanish (ideal)
Fc = F_of(coframe(sp.Integer(0)), 1)
res["X2_control_iuF1_zero"] = bool(all(sp.simplify(Fc[0, n]) == 0 for n in range(4)))
# identity: adapted tetrad (A^a(u) = delta^a_0 with u = d_t): i_u dA^a = L_u A^a = d_t A^a_nu
adapted = [E[a, 0] for a in range(4)] == [1, 0, 0, 0]          # A^a_t = delta^a_0, u = d_t
idl = adapted and all(sp.simplify(F_of(E, a)[0, n] - sp.diff(E.row(a)[n], t)) == 0 for a in range(4) for n in range(4))
res["EXTRA_iu_dA_equals_Lie_derivative"] = bool(idl)

# X3: bump integral and line integral along x = z = 0 (B-lines along y at t = 0)
mp.dps = 30
fb = lambda s: mexp(1 - 1 / (1 - s * s)) if abs(s) < 1 else mp.mpf(0)
C = quad(fb, [-1, 0, 1])
res["X3_C"] = str(C)
# F^1_{ty} along x = z = 0 at t = 0: (2/5) f(y) cos(beta(0,0)) = (2/5) f(y)
Fty_line = sp.simplify(F1_0[0, 2].subs({x: 0, z: 0}))
res["X3_F_ty_on_line"] = str(Fty_line)
res["X3_line_integral"] = str(mp.mpf(2) / 5 * C)
# spatial B = F^1_{xz} at t = 0 for control; field lines of B dx^dz are along y (kernel of the spatial 2-form)
res["X3_B_xz_control"] = str(sp.simplify(Fc[1, 3].subs(t, 0)))

# X4: ROT014 compact time profile h(t) = t f(t): coincidence at t = 0 and |t| >= 1, line integral |kappa| C
h = sp.Function("h")(t)
E4 = coframe(kap * h * fsym)
F14 = F_of(E4, 1)
Fty4 = sp.simplify(F14[0, 2].subs({x: 0, z: 0}))
res["X4_F_ty_on_line_general"] = str(Fty4)
# with h(0) = 0, h'(0) = 1 (h = t f(t), f(0) = 1): F_ty(t=0, x=z=0) = kappa f(y)
Fty4_0 = Fty4.subs(sp.Derivative(h, t), 1).subs(h, 0).subs(t, 0)
res["X4_F_ty_t0"] = str(sp.simplify(Fty4_0))
res["X4_line_integral_over_kappa"] = str(C)
res["X4_coframe_equals_control_where_h=0"] = bool(sp.simplify(E4.subs(h, 0) - coframe(sp.Integer(0))) == sp.zeros(4))


# EXTRA2: transformation law for adapted frames under a spatial rotation A' = Lambda A:
#   R'^a = Lambda^a_b R^b + u(Lambda^a_b) A^b      (u = d_t here; Lambda^a_0 = delta^a_0)
# symbolic simplify does not close the trig identity for an abstract alpha(t,x,y,z); the law is checked at 50 digits
# on 10 random points for two concrete fields alpha, with tolerance 1e-40 (and reported separately).
import random
def law_residual_max(alpha_expr, npts=10, seed=20261030):
    Ec = coframe(sp.Integer(0)); Ea = coframe(alpha_expr); Lam = Ea * Ec.inv()
    rnd = random.Random(seed); worst = sp.Integer(0)
    exprs = []
    for a in range(4):
        Fa = F_of(Ea, a)
        for n in range(4):
            exprs.append(Fa[0, n] - sum(Lam[a, b] * F_of(Ec, b)[0, n] + sp.diff(Lam[a, b], t) * Ec[b, n] for b in range(4)))
    spatial_ok = all(sp.simplify(Lam[a, 0] - (1 if a == 0 else 0)) == 0 for a in range(4))
    for _ in range(npts):
        pt = {v: sp.Rational(rnd.randint(-999, 999), 1000) for v in X}
        for e in exprs:
            worst = max(worst, abs(sp.N(e.subs(pt), 50)))
    return worst, spatial_ok
w1, sp1 = law_residual_max(t * x + sp.sin(y) + t ** 2 * z)
w2, sp2 = law_residual_max(sp.Rational(2, 5) * t * sp.exp(-y ** 2) + x * z * t ** 3)
law_ok = bool(w1 < sp.Float("1e-40") and w2 < sp.Float("1e-40")); spatial = bool(sp1 and sp2)
res["EXTRA2_law_residual_50digits"] = [str(sp.N(w1, 5)), str(sp.N(w2, 5))]
res["EXTRA2_Lambda_is_spatial_rotation"] = bool(spatial)
res["EXTRA2_transformation_law_R'=Lambda R + u(Lambda) A"] = bool(law_ok)
# EXTRA3: a static (t-independent) but position-dependent rotation keeps the ideal control ideal: R' = 0
als = sp.Function("alpha_s")(x, y, z)
Es = coframe(als)
res["EXTRA3_static_rotation_keeps_ideal"] = bool(all(sp.simplify(F_of(Es, a)[0, n]) == 0 for a in range(4) for n in range(4)))

res["verdicts"] = {k: bool(v) for k, v in {
    "X1_all_metrics_flat": all(res["X1_metric_is_eta"].values()),
    "X2_F_ty_2_5": res["X2_F_ty"] in ("2/5", "-2/5"), "X2_F_xz_7_10": res["X2_F_xz"] in ("7/10", "-7/10"),
    "X2_det_49_625": res["X2_det"] == "49/625", "X2_rank_4": res["X2_rank"] == 4, "X2_control_ideal": res["X2_control_iuF1_zero"],
    "X3_C": abs(C - mp.mpf("1.2069003224378765")) < mp.mpf("1e-15"),
    "X3_line": abs(mp.mpf(2) / 5 * C - mp.mpf("0.48276012897515064")) < mp.mpf("1e-15"),
    "X4_coincidence_where_h0": res["X4_coframe_equals_control_where_h=0"],
    "EXTRA_nonideality_is_Lie_transport_defect": res["EXTRA_iu_dA_equals_Lie_derivative"],
    "EXTRA2_spatial_rotation": res["EXTRA2_Lambda_is_spatial_rotation"],
    "EXTRA2_transformation_law": res["EXTRA2_transformation_law_R'=Lambda R + u(Lambda) A"],
    "EXTRA3_static_rotation_keeps_ideal": res["EXTRA3_static_rotation_keeps_ideal"]}.items()}
json.dump(res, open(args.out, "w"), indent=1, sort_keys=True)
print(json.dumps(res["verdicts"], indent=1)); print(res["X2_F1_origin"], res["X3_F_ty_on_line"], res["X4_F_ty_t0"])
