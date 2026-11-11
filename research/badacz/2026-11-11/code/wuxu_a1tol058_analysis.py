#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_058 (two-direction A1 test at j = 22 under BADACZ_TOL = 1e-4:1e-7).
Root per config: linear least squares of Y_C on log10(beta) over the 7 'fit' points, root at Y_C = 0.251 (as REVIEW_050/054);
Delta = root(config) - root(base, same run). G = 10^(-Delta2) + 10^(-Delta0); A1 with one shared s requires G = 2.
Also re-evaluates the default-tolerance REVIEW_054 run (research/badacz/2026-11-08/data/kernel_cd052.csv) with the same code.
Usage: python3 -I wuxu_a1tol058_analysis.py <kernel_a1tol058.csv> <kernel_cd052.csv> <out.json>
"""
import csv, json, math, sys
import numpy as np
def fits(path, ids):
    rows = list(csv.DictReader(l for l in open(path) if not l.startswith("#")))
    out = {}
    for cid in ids:
        p = [(float(r["log10beta"]), float(r["Yc"])) for r in rows if r["id"] == cid and r["phase"] == "fit"]
        x, y = np.array([a for a, _ in p]), np.array([b for _, b in p])
        A = np.vstack([x, np.ones_like(x)]).T; (b, a), *_ = np.linalg.lstsq(A, y, rcond=None)
        s2 = float(np.sum((y - (a + b*x))**2)/(len(x) - 2)); cov = s2*np.linalg.inv(A.T @ A)
        r0 = (0.251 - a)/b; g = np.array([-(0.251 - a)/b**2, -1/b])
        out[cid] = {"root": float(r0), "se": float(math.sqrt(g @ cov @ g)), "slope": float(b), "sigma_resid": math.sqrt(s2), "n": len(x)}
    return out
def evaluate(F, base, c2, c0):
    d2 = F[c2]["root"] - F[base]["root"]; d0 = F[c0]["root"] - F[base]["root"]
    G = 10**(-d2) + 10**(-d0)
    # +/-1 fit-SE cube on the three roots (as AUD1 ROT035 / REC11 ROT012): extreme G
    sb, s2_, s0 = F[base]["se"], F[c2]["se"], F[c0]["se"]
    Gmax = 10**(-(d2 - sb - s2_)) + 10**(-(d0 - sb - s0))
    Gmin = 10**(-(d2 + sb + s2_)) + 10**(-(d0 + sb + s0))
    dstar = 0.5*math.log10(2/G) if G < 2 else -0.5*math.log10(G/2)     # REC11 ROT012 sharp uniform root budget
    return {"Delta2": d2, "Delta0": d0, "s_k2": 10**(-d2) - 1, "s_k0": 1 - 10**(-d0), "G": G, "G_fitSE_cube": [Gmin, Gmax], "d_star_dex": dstar}
Ft = fits(sys.argv[1], ("base22t", "CD2_22t", "CD0_22t")); Fd = fits(sys.argv[2], ("base22r", "CD2_22", "CD0_22"))
et = evaluate(Ft, "base22t", "CD2_22t", "CD0_22t"); ed = evaluate(Fd, "base22r", "CD2_22", "CD0_22")
G = et["G"]
verdict = "R_A1_FAILURE_ROBUST" if G <= 1.95 else ("N_FAILURE_WAS_NUMERICAL" if G >= 1.98 else "INCONCLUSIVE")
shift = {"base": Ft["base22t"]["root"] - Fd["base22r"]["root"], "CD2": Ft["CD2_22t"]["root"] - Fd["CD2_22"]["root"], "CD0": Ft["CD0_22t"]["root"] - Fd["CD0_22"]["root"]}
res = {"tol_1e-4": {"fits": Ft, **et}, "default_REVIEW054": {"fits": Fd, **ed}, "root_shift_tol_minus_default": shift, "verdict": verdict}
json.dump(res, open(sys.argv[3], "w"), indent=1, allow_nan=False)
for k in ("tol_1e-4", "default_REVIEW054"):
    e = res[k]; print(k, "D2 %+.4f D0 %+.4f s_k2 %.4f s_k0 %.4f G %.4f cube [%.4f, %.4f] d* %.4f" % (e["Delta2"], e["Delta0"], e["s_k2"], e["s_k0"], e["G"], *e["G_fitSE_cube"], e["d_star_dex"]))
    for c, f in e["fits"].items():
        print("   ", c, "root %.4f se %.4f slope %.5f sigma_resid %.2e" % (f["root"], f["se"], f["slope"], f["sigma_resid"]))
print("root shifts tol-default:", {k: round(v, 4) for k, v in shift.items()}); print("VERDICT", verdict)
