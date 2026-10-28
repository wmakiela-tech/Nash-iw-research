#!/usr/bin/env python3
"""Cross-family check (Claude -> GPT cell LT6) of
research/lt6/2026-10-28/IW_LT6_ROT007_QUANTITATIVE_NONLINEAR_TARGET_ALIAS_001_20261028.md
Written from the public text only (author scripts not read). Parts:
  A  exact (SymPy): the author's example F=(x+z^2/2, y+z^2), T=z+0.2x; fibre, target values,
     hypotheses of T007.1 at t=0.1 with certified L, K, G, beta; the flat and even warnings.
  B  T007.1 on random C^2 maps with certified Hessian bounds (quadratic + sine terms):
     fixed point by the contraction of the proof, then checks F(c+-)=F(0), ||y||<=L t^2,
     ||c+ - c-||>=2t, |T(c+)-T(c-)|>=|alpha| t at the largest admissible t.
  C  T007.2 on random and adversarial perturbations: dist(g,row A) >= ||(I-P_rowAt) gt|| - eps_g
     - eps_A/(s-eps_A) ||gt||.
Run: python3 lt6_rot007_ift_alias_check.py --out <dir>
numpy 2.1.3, sympy 1.13.3; seed 20261028.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import sympy as sp

SEED = 20261028


def part_A():
    x, y, z, t = sp.symbols("x y z t", real=True)
    F = sp.Matrix([x + z ** 2 / 2, y + z ** 2]); T = z + sp.Rational(1, 5) * x
    cp = {x: -t ** 2 / 2, y: -t ** 2, z: t}; cm = {x: -t ** 2 / 2, y: -t ** 2, z: -t}
    out = {"F(c+)": str(sp.simplify(F.subs(cp))), "F(c-)": str(sp.simplify(F.subs(cm)))}
    tv = sp.Rational(1, 10)
    out["T(c+)"] = str(T.subs(cp).subs(t, tv)); out["T(c-)"] = str(T.subs(cm).subs(t, tv))
    # certified constants: D2F(h,k) = (h_z k_z, 2 h_z k_z) -> L = sqrt(5); K = 0; G = ||(1/5,0,1)||; beta = 1
    L = sp.sqrt(5); K = 0; G = sp.sqrt(sp.Rational(26, 25)); beta = 1; alpha = 1
    Dc = G * beta * L + sp.Rational(25, 32) * K
    out["hyp_betaLt<=1/4"] = bool(beta * L * tv <= sp.Rational(1, 4))
    out["hyp_Dt<=|alpha|/2"] = bool(Dc * tv <= sp.Rational(alpha, 2))
    out["certified_lower_|alpha|t"] = str(alpha * tv)
    out["actual_difference"] = str(T.subs(cp).subs(t, tv) - T.subs(cm).subs(t, tv))
    y_norm = sp.sqrt(sp.Rational(1, 4) + 1) * tv ** 2
    out["||y||<=L t^2"] = bool(y_norm <= L * tv ** 2)
    Tflat = F[0] + F[1]; Teven = z ** 2
    out["T_flat_on_fibre_minus_T(0)"] = str(sp.simplify(Tflat.subs(cp) - Tflat.subs({x: 0, y: 0, z: 0})))
    out["T_even(c+)-T_even(c-)"] = str(sp.simplify(Teven.subs(cp) - Teven.subs(cm)))
    out["naive_first_order_null_F(0,0,t)"] = str(F.subs({x: 0, y: 0, z: t}).T)
    return out


def part_B(rng, n_inst=400):
    st = {"instances": 0, "viol_F": 0, "viol_y": 0, "viol_dist": 0, "viol_T": 0, "max_F_residual": 0.0,
          "min_ratio_Tgap_over_alpha_t": np.inf, "max_contraction_iters": 0,
          "viol_taylor_step": 0, "max_ratio_taylor_err_over_Dt2": 0.0, "max_ratio_y_over_Lt2": 0.0}
    while st["instances"] < n_inst:
        m = int(rng.integers(1, 4)); n = m + int(rng.integers(1, 4))
        A = rng.normal(size=(m, n))
        sv = np.linalg.svd(A, compute_uv=False)
        if sv[-1] < 0.2: continue
        beta = 1 / sv[-1]; Ap = np.linalg.pinv(A)
        M = [rng.normal(size=(n, n)) for _ in range(m)]; M = [(Mi + Mi.T) / 2 * rng.uniform(0.2, 2) for Mi in M]
        eps = rng.normal(size=m) * 0.5; W = rng.normal(size=(m, n))
        L = np.sqrt(sum((np.linalg.norm(M[i], 2) + abs(eps[i]) * np.linalg.norm(W[i]) ** 2) ** 2 for i in range(m)))
        def F(c):
            return A @ c + 0.5 * np.array([c @ M[i] @ c for i in range(m)]) + eps * (np.sin(W @ c) - W @ c)
        # sin(w.c) - w.c has zero gradient at 0, so DF(0) = A exactly
        g = rng.normal(size=n); Kq = rng.normal(size=(n, n)); Kq = (Kq + Kq.T) / 2 * rng.uniform(0, 1)
        kap = rng.normal() * 0.5; u = rng.normal(size=n)
        K = np.linalg.norm(Kq, 2) + abs(kap) * np.linalg.norm(u) ** 2
        def T(c):
            return g @ c + 0.5 * c @ Kq @ c + kap * (np.sin(u @ c) - u @ c)
        N0 = np.linalg.svd(A)[2][m:].T                       # orthonormal basis of ker A
        w = N0 @ rng.normal(size=N0.shape[1]); v = w / np.linalg.norm(w)
        alpha = g @ v
        if abs(alpha) < 0.05: continue
        G = np.linalg.norm(g); Dc = G * beta * L + 25 * K / 32
        tmax = min(1 / (4 * beta * L), abs(alpha) / (2 * Dc))      # R = infinity (entire maps)
        t = tmax * rng.uniform(0.3, 1.0) if rng.random() < 0.5 else tmax
        sols = []
        for sgn in (1, -1):
            yv = np.zeros(m); it = 0
            for it in range(200):
                c = sgn * t * v + Ap @ yv
                ynew = -(F(c) - A @ c)
                if np.linalg.norm(ynew - yv) < 1e-15 * max(1, np.linalg.norm(ynew)): yv = ynew; break
                yv = ynew
            st["max_contraction_iters"] = max(st["max_contraction_iters"], it)
            c = sgn * t * v + Ap @ yv
            sols.append((c, yv))
        (cp, yp), (cm, ym) = sols
        res = max(np.linalg.norm(F(cp)), np.linalg.norm(F(cm)))
        st["max_F_residual"] = max(st["max_F_residual"], res)
        st["viol_F"] += int(res > 1e-12)
        st["viol_y"] += int(max(np.linalg.norm(yp), np.linalg.norm(ym)) > L * t ** 2 * (1 + 1e-12))
        st["viol_dist"] += int(np.linalg.norm(cp - cm) < 2 * t * (1 - 1e-12))
        for sgn, c in ((1, cp), (-1, cm)):                    # intermediate Taylor step of the proof
            terr = abs(T(c) - T(np.zeros(n)) - sgn * alpha * t)
            st["viol_taylor_step"] += int(terr > Dc * t ** 2 * (1 + 1e-12) + 1e-15)
            st["max_ratio_taylor_err_over_Dt2"] = max(st["max_ratio_taylor_err_over_Dt2"], terr / (Dc * t ** 2))
        st["max_ratio_y_over_Lt2"] = max(st["max_ratio_y_over_Lt2"], max(np.linalg.norm(yp), np.linalg.norm(ym)) / (L * t ** 2))
        gap = abs(T(cp) - T(cm))
        st["viol_T"] += int(gap < abs(alpha) * t * (1 - 1e-12))
        st["min_ratio_Tgap_over_alpha_t"] = min(st["min_ratio_Tgap_over_alpha_t"], gap / (abs(alpha) * t))
        st["instances"] += 1
    return st


def part_C(rng, n_inst=4000):
    st = {"instances": 0, "violations": 0, "min_slack": np.inf, "positive_certificates": 0}
    for i in range(n_inst):
        m = int(rng.integers(1, 5)); n = m + int(rng.integers(1, 5))
        A = rng.normal(size=(m, n)); g = rng.normal(size=n)
        epsA = rng.uniform(0, 0.5) * np.linalg.svd(A, compute_uv=False)[-1]; epsg = rng.uniform(0, 0.3)
        if i % 2 == 0:                                         # random direction
            E = rng.normal(size=(m, n)); E *= epsA / np.linalg.norm(E, 2)
        else:                                                  # adversarial: rotate the weakest row direction into ker A
            U, s, Vt = np.linalg.svd(A)
            kv = Vt[m:][0] if n > m else Vt[-1]
            E = epsA * np.outer(U[:, -1], kv)
        At = A + E
        e = rng.normal(size=n); e *= epsg / np.linalg.norm(e) * rng.uniform(0.5, 1); gt = g + e
        s_t = np.linalg.svd(At, compute_uv=False)[-1]
        if s_t <= epsA: continue
        Pa = np.linalg.pinv(A) @ A; Pt = np.linalg.pinv(At) @ At
        dist = np.linalg.norm(g - Pa @ g)
        bound = np.linalg.norm(gt - Pt @ gt) - epsg - epsA / (s_t - epsA) * np.linalg.norm(gt)
        st["instances"] += 1
        st["violations"] += int(dist < bound - 1e-12)
        st["min_slack"] = min(st["min_slack"], dist - bound)
        st["positive_certificates"] += int(bound > 0)
    return st


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True)
    out = Path(ap.parse_args().out); out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(SEED)
    A = part_A(); B = part_B(rng); C = part_C(rng)
    verdict = {
        "A_example_exact": A["F(c+)"] == "Matrix([[0], [0]])" and A["F(c-)"] == "Matrix([[0], [0]])"
                           and A["T(c+)"] == "99/1000" and A["T(c-)"] == "-101/1000" and A["hyp_betaLt<=1/4"]
                           and A["hyp_Dt<=|alpha|/2"],
        "B_T007_1_no_violation": B["viol_F"] == 0 and B["viol_y"] == 0 and B["viol_dist"] == 0 and B["viol_T"] == 0
                                 and B["viol_taylor_step"] == 0,
        "C_T007_2_no_violation": C["violations"] == 0,
    }
    res = {"A": A, "B": B, "C": C, "verdict": {k: bool(v) for k, v in verdict.items()}, "seed": SEED,
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (out / "lt6_rot007_ift_alias_check.json").write_text(json.dumps(res, indent=1, default=float))
    print(json.dumps(res, indent=1, default=float))


if __name__ == "__main__":
    main()
