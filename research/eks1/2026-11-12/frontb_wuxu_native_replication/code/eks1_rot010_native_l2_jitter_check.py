#!/usr/bin/env python3
"""EKS1 ROT010 - data-only check on the ACTUAL native L2 archive (Mech-S9 ROT008, Actions run 43310359194).

Question: is the authors' native response, as a function of log10(beta) at default solver settings,
smooth at the level needed to locate the V0/V1/V2 roots to 0.02 dex?

Input: independent_L2_raw_calls.csv and independent_L2_roots.csv from artifact 13986347698
(ZIP sha256 88913fd22b95efd37d26d69e036f9e05a99f7bb411faa5c996deeb1aebc0b461), and the L1 reference
research/badacz/2026-11-08/data/yp051/yp_a.csv (Badacz REVIEW_053) from the public repo.
No model is fitted to physics; only low-order polynomial trends in x=log10(beta) are removed.
Ceiling: DIAGNOSTIC_ON_PUBLISHED_NATIVE_OUTPUTS / CLAUDE_FAMILY / NO_NEW_NATIVE_RUN / NO_PBH_BOUND.
Usage: python3 -I eks1_rot010_native_l2_jitter_check.py RAW.csv ROOTS.csv YP_A.csv [out.json]
"""
import csv, json, math, sys
import numpy as np

raw, roots, ypa = sys.argv[1], sys.argv[2], sys.argv[3]
out = {"ceiling": "DIAGNOSTIC_ON_PUBLISHED_NATIVE_OUTPUTS / CLAUDE_FAMILY / NO_NEW_NATIVE_RUN / NO_PBH_BOUND"}
X0S = {22: 0.109037947008919, 62: 0.109032060692695}   # NATIVE_L2_STDOUT of the same archive

rows = [r for r in csv.DictReader(open(raw))]
R = {}
for r in rows:
    j = int(r["j"]); R.setdefault(j, []).append((float(r["log10beta"]), float(r["X_T0"]), float(r["X_T1"]), float(r["Yc_author"])))
for j in R: R[j].sort()

def chan(j, name, x0, x1, yc):
    if name == "V0": return yc - 0.251
    if name == "V1": return 2 * x1 - 0.251
    return 2 * (x0 - X0S[22]) - 0.006          # V2 as coded in the L2 driver (j22 baseline for both masses)

res = {}
for j in sorted(R):
    a = np.array(R[j]); x = a[:, 0]
    res[j] = {"n_calls": len(x), "x_min": float(x.min()), "x_max": float(x.max())}
    for name in ("V0", "V1", "V2"):
        v = np.array([chan(j, name, r[1], r[2], r[3]) for r in R[j]])
        # (a) global smooth trend: polynomial in x, degree chosen 3 and 5 (report both)
        d = {}
        for deg in (3, 5):
            c = np.polyfit(x - x.mean(), v, deg); fit = np.polyval(c, x - x.mean())
            rr = v - fit
            slope = np.polyval(np.polyder(c), 0.0)
            d[f"deg{deg}"] = {"rms_resid": float(np.sqrt(np.mean(rr ** 2))), "max_abs_resid": float(np.max(np.abs(rr)))}
        # (b) model-free: adjacent pairs closer than 0.004 dex; compare |dv| with what the secant slope allows
        gslope = (v[-1] - v[0]) / (x[-1] - x[0])                  # mean slope over the scanned range, per dex
        pairs = [(x[i + 1] - x[i], v[i + 1] - v[i]) for i in range(len(x) - 1) if 0 < x[i + 1] - x[i] < 0.004]
        excess = [abs(dv) / max(abs(gslope) * dx, 1e-300) for dx, dv in pairs]
        nonmono = sum(1 for dx, dv in pairs if dv < 0)
        allnon = sum(1 for i in range(len(x) - 1) if v[i + 1] < v[i])
        d.update({"mean_slope_per_dex": float(gslope), "n_close_pairs": len(pairs),
                  "close_pair_abs_dv_median": float(np.median([abs(p[1]) for p in pairs])) if pairs else None,
                  "close_pair_abs_dv_max": float(max(abs(p[1]) for p in pairs)) if pairs else None,
                  "close_pair_excess_over_smooth_median": float(np.median(excess)) if pairs else None,
                  "close_pairs_decreasing": nonmono, "adjacent_decreasing_all": allnon, "n_adjacent_all": len(x) - 1})
        # (c) implied root band: all x where |trend(deg3)| < max_abs_resid(deg3)
        c3 = np.polyfit(x - x.mean(), v, 3)
        xs = np.linspace(x.min(), x.max(), 20001); t = np.polyval(c3, xs - x.mean())
        band = xs[np.abs(t) <= d["deg3"]["max_abs_resid"]]; band_rms = xs[np.abs(t) <= d["deg3"]["rms_resid"]]
        sgn = np.where(np.diff(np.sign(t)) != 0)[0]
        d["trend_root_deg3"] = float(xs[sgn[0]]) if len(sgn) else None
        d["root_band_maxresid"] = [float(band.min()), float(band.max())] if len(band) else None
        d["root_band_rms"] = [float(band_rms.min()), float(band_rms.max())] if len(band_rms) else None
        res[j][name] = d
out["by_mass"] = res

# (d) the final bisection brackets themselves
br = []
for r in csv.DictReader(open(roots)):
    j, name = int(r["j"]), r["criterion"]
    w = float(r["right_log10beta"]) - float(r["left_log10beta"]); jump = float(r["hi_residual"]) - float(r["lo_residual"])
    s = res[j][name]["mean_slope_per_dex"]
    br.append({"j": j, "criterion": name, "root": float(r["root_log10beta"]), "bracket_width_dex": w, "residual_jump": jump,
               "smooth_jump_expected": s * w, "ratio": jump / (s * w),
               "dex_equivalent_of_jump": jump / s})
out["final_brackets"] = br

# (e) the L1 reference grid (Badacz), same channels, same kind of trend test
L1 = {}
for line in open(ypa):
    if line.startswith("#") or line.startswith("id,"): continue
    p = line.strip().split(",")
    if len(p) < 8: continue
    L1.setdefault(int(p[1]), []).append((float(p[3]), float(p[4]), float(p[5]), float(p[6])))
l1 = {}
for j in sorted(L1):
    a = np.array(sorted(L1[j])); x = a[:, 0]
    l1[j] = {"n": len(x), "x": [float(t) for t in x]}
    for name in ("V0", "V1", "V2"):
        v = np.array([chan(j, name, r[1], r[2], r[3]) for r in a])
        if len(x) >= 5:
            c = np.polyfit(x - x.mean(), v, 3); rr = v - np.polyval(c, x - x.mean())
            l1[j][name] = {"deg3_rms_resid": float(np.sqrt(np.mean(rr ** 2))), "deg3_max_abs_resid": float(np.max(np.abs(rr))),
                           "second_diff_sign_changes": int(np.sum(np.diff(np.sign(np.diff(v, 2))) != 0))}
out["l1_reference_grid"] = l1

# (f) cross-check L2 against the L1 trend at the L2 abscissae (j22): L2 value minus deg-3 trend through L1 points
if 22 in L1 and len(L1[22]) >= 5:
    a = np.array(sorted(L1[22])); xl = a[:, 0]
    cx = np.polyfit(xl - xl.mean(), a[:, 1], 3)
    b = np.array(R[22]); m = (b[:, 0] >= xl.min()) & (b[:, 0] <= xl.max())
    dX = b[m, 1] - np.polyval(cx, b[m, 0] - xl.mean())
    out["l2_minus_l1trend_X_T0_j22"] = {"n": int(m.sum()), "mean": float(dX.mean()), "rms": float(np.sqrt(np.mean(dX ** 2))), "max_abs": float(np.max(np.abs(dX)))}


# (g) roots from UNSELECTED abscissae only (bisection points cluster where the sign flips, so they bias a trend root):
#     L1 regular grid (9 points) and the six L2 coarse anchors, j22; leave-one-out spread of the fitted root
if 22 in L1:
    rawrows = [r for r in rows if int(r["j"]) == 22 and r["eval_kind"] == "coarse"]
    c2 = sorted((float(r["log10beta"]), float(r["X_T0"]), float(r["X_T1"]), float(r["Yc_author"])) for r in rawrows)
    l1p = sorted(L1[22])
    def froot(pts, name, deg):
        x = np.array([q[0] for q in pts]); v = np.array([chan(22, name, q[1], q[2], q[3]) for q in pts])
        c = np.polyfit(x - x.mean(), v, deg); xs = np.linspace(x.min(), x.max(), 40001); t = np.polyval(c, xs - x.mean())
        k = np.where(np.diff(np.sign(t)) != 0)[0]
        return float(xs[k[0]]) if len(k) else None
    g = {}
    for name in ("V0", "V1", "V2"):
        e = {}
        for label, pts in (("L1_grid9", l1p), ("L2_coarse6", c2), ("pooled15", sorted(l1p + c2))):
            for deg in (2, 3):
                if len(pts) <= deg + 1: continue
                r0 = froot(pts, name, deg)
                loo = [froot(pts[:i] + pts[i + 1:], name, deg) for i in range(len(pts))]
                loo = [t for t in loo if t is not None]
                e[f"{label}_deg{deg}"] = {"root": r0, "loo_min": min(loo), "loo_max": max(loo), "loo_halfspread": (max(loo) - min(loo)) / 2}
        g[name] = e
    g["shift_V2_minus_V0_pooled15_deg3"] = g["V2"]["pooled15_deg3"]["root"] - g["V0"]["pooled15_deg3"]["root"]
    g["shift_V2_minus_V0_L1_grid9_deg3"] = g["V2"]["L1_grid9_deg3"]["root"] - g["V0"]["L1_grid9_deg3"]["root"]
    g["shift_V2_minus_V0_L2_coarse6_deg3"] = g["V2"]["L2_coarse6_deg3"]["root"] - g["V0"]["L2_coarse6_deg3"]["root"]
    # level offset between the two drivers on unselected points: L2 coarse X_T0 minus cubic trend through L1 grid
    xl = np.array([q[0] for q in l1p]); cx = np.polyfit(xl - xl.mean(), np.array([q[1] for q in l1p]), 3)
    dd = np.array([q[1] - np.polyval(cx, q[0] - xl.mean()) for q in c2 if xl.min() <= q[0] <= xl.max()])
    g["L2coarse_minus_L1trend_X_T0"] = {"n": len(dd), "mean": float(dd.mean()), "rms": float(np.sqrt(np.mean(dd ** 2))), "max_abs": float(np.max(np.abs(dd)))}
    out["unselected_roots_j22"] = g

print(json.dumps(out, indent=1))
if len(sys.argv) > 4: json.dump(out, open(sys.argv[4], "w"), indent=1)
