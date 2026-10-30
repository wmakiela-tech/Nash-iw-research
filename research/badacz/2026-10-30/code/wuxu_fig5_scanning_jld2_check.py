#!/usr/bin/env python3
"""Badacz (Claude): independent cross-family check of MT14 ROT018 on the ORIGINAL Wu-Xu scan file.

Source: github.com/Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d,
        arXiv-2509.05618/data/out/scanning.jld2 (git blob 10cc9b3f..., sha256 51844a46...).
Author code (same commit), main-scan.jl:  Y_p = 2*X_n_nuc/(1 - X_n_nuc);  chi2 = ((Y_p - .245)/.003)^2;
main.ipynb Fig. 5: heatmap of Y_P_mat and contour chi2 = 4.
Reading: JLD2 is HDF5; h5py 3.16 (HDF5 >= 1.14.6) refuses the chunk-dimension encoding written by JLD2 0.6,
h5py 3.12.1 (HDF5 1.14.4) reads it. No Julia used.
Tests (PREREG_030): T1 sha256; T2 chi2 identity; T3 counts chi2>4 and Y>1; T4 MT14 relabel C=2X/(1-X) -> M=2X
(X = Y/(2+Y)) flips; T6 X > 1/3 <=> Y > 1.  EXPLORATORY (beyond prereg, labelled): SBBN-anchored linear-in-X
surrogates Y = Y0 + c (X - X0) with c in {2, 2.245 (= Y0/X0)} and the shift of the chi2 = 4 contour in beta.
Run (needs h5py==3.12.1): python3 -I wuxu_fig5_scanning_jld2_check.py --jld2 <scanning.jld2> --out <file.json>
"""
import argparse, hashlib, json, math
import numpy as np
import h5py

ap = argparse.ArgumentParser(); ap.add_argument("--jld2", required=True); ap.add_argument("--out", required=True)
args = ap.parse_args()
raw = open(args.jld2, "rb").read()
res = {"T1_sha256": hashlib.sha256(raw).hexdigest(),
       "T1_expected": "51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786",
       "h5py": h5py.__version__, "hdf5": h5py.version.hdf5_version}
res["T1_pass"] = res["T1_sha256"] == res["T1_expected"]
f = h5py.File(args.jld2, "r")
Y = np.array(f["Y_P_mat"]); C2 = np.array(f["chi2_mat"]); m = np.array(f["m_PBH_list [gram]"]); b = np.array(f["β_PBH_list"])
# orientation: Julia (m, beta) column-major -> h5py axis0 = beta, axis1 = m. Check monotonicity in beta.
inc_ax0 = float(np.mean(np.diff(Y, axis=0) >= -1e-12)); inc_ax1 = float(np.mean(np.diff(Y, axis=1) >= -1e-12))
res["orientation"] = {"shape": list(Y.shape), "frac_nondecreasing_along_axis0": inc_ax0, "frac_nondecreasing_along_axis1": inc_ax1,
                      "m_range_g": [float(m.min()), float(m.max())], "beta_range": [float(b.min()), float(b.max())]}
Yb = Y if inc_ax0 >= inc_ax1 else Y.T     # rows = beta, columns = mass
C2b = C2 if inc_ax0 >= inc_ax1 else C2.T

# T2
pred = ((Y - 0.245) / 0.003) ** 2
res["T2_max_abs_diff"] = float(np.abs(pred - C2).max()); res["T2_max_rel_diff"] = float((np.abs(pred - C2) / np.maximum(C2, 1e-300)).max())
# T3
res["T3_chi2_gt_4"] = int((C2 > 4).sum()); res["T3_Y_gt_1"] = int((Y > 1).sum()); res["T3_total"] = int(Y.size)
res["Y_range"] = [float(Y.min()), float(Y.max())]
# T4 (MT14 relabel without recalibration)
X = Y / (2 + Y); M = 2 * X; C2M = ((M - 0.245) / 0.003) ** 2
old = C2 > 4; new = C2M > 4
res["T4_flips"] = int((old != new).sum()); res["T4_allowed_to_excluded"] = int((~old & new).sum()); res["T4_excluded_to_allowed"] = int((old & ~new).sum())
# T6
res["T6_X_gt_one_third"] = int((X > 1 / 3).sum()); res["T6_equals_T3_Y_gt_1"] = res["T6_X_gt_one_third"] == res["T3_Y_gt_1"]
X0 = 0.245 / 2.245
res["T6_SBBN_X_at_Tnuc_implied"] = X0
res["T6_note"] = "Y = 2X/(1-X) = 2 n/p for X = n/(n+p); the standard mass fraction is Y = 2X = 2(n/p)/(1+n/p)."

# EXPLORATORY: SBBN-anchored linear surrogates and contour shift
def boundary(chi, level=4.0):
    """per mass column: log10 beta where chi crosses level (first crossing from below, linear in log beta)."""
    lb = np.log10(np.sort(b)); order = np.argsort(b); out = []
    for j in range(chi.shape[1]):
        col = chi[order, j]
        idx = np.where(col > level)[0]
        if len(idx) == 0 or idx[0] == 0:
            out.append(np.nan if len(idx) == 0 else lb[0]); continue
        k = idx[0]; y0, y1 = col[k - 1], col[k]
        out.append(lb[k - 1] + (level - y0) / (y1 - y0) * (lb[k] - lb[k - 1]))
    return np.array(out)

bd0 = boundary(C2b)
expl = {}
for name, c in (("c=2 (standard slope)", 2.0), ("c=Y0/X0=2.245 (proportional)", 0.245 / X0)):
    Ya = 0.245 + c * (X - X0); C2a = ((Ya - 0.245) / 0.003) ** 2
    Ca = C2a if inc_ax0 >= inc_ax1 else C2a.T
    bd = boundary(Ca)
    ok = ~np.isnan(bd) & ~np.isnan(bd0)
    expl[name] = {"flips_vs_original": int(((C2a > 4) != old).sum()),
                  "allowed_to_excluded": int(((C2a > 4) & ~old).sum()), "excluded_to_allowed": int((~(C2a > 4) & old).sum()),
                  "contour_shift_log10_beta_max": float(np.nanmax(np.abs(bd[ok] - bd0[ok]))) if ok.any() else None,
                  "contour_shift_log10_beta_median": float(np.nanmedian(bd[ok] - bd0[ok])) if ok.any() else None,
                  "slope_ratio_vs_author_at_SBBN": c / (2 / (1 - X0) ** 2)}
res["EXPLORATORY_sbbn_anchored_linear_surrogates"] = expl
res["EXPLORATORY_note"] = ("Not a physical recalibration: a correct standard treatment would retune T_nuc so that 2X = 0.245, "
                           "which changes X itself; only stored Y at the author's T_nuc is available. Indicates sensitivity only.")
res["contour_columns_with_boundary"] = int(np.sum(~np.isnan(bd0)))
res["verdicts"] = {k: bool(v) for k, v in {
    "T1_sha256": res["T1_pass"],
    "T2_chi2_identity": res["T2_max_abs_diff"] < 1e-9,
    "T3_chi2_gt4_5531": res["T3_chi2_gt_4"] == 5531, "T3_Y_gt1_158": res["T3_Y_gt_1"] == 158,
    "T4_flips_4982_4469_513": (res["T4_flips"], res["T4_allowed_to_excluded"], res["T4_excluded_to_allowed"]) == (4982, 4469, 513),
    "T6_X_gt_third_iff_Y_gt_1": res["T6_equals_T3_Y_gt_1"]}.items()}
json.dump(res, open(args.out, "w"), indent=1, sort_keys=True)
print(json.dumps(res["verdicts"], indent=1)); print(json.dumps(expl, indent=1))
