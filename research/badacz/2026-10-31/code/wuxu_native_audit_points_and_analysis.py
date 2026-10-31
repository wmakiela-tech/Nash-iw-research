#!/usr/bin/env python3
"""Badacz (Claude): point selection and analysis for the author-native Wu-Xu audit (PREREG_034, commit f170e2a).

Subcommand `points`: rebuilds the 74 audit points from the ORIGINAL scan file
  (Fenyutanchan/Primordial-Black-Hole @ d395183, arXiv-2509.05618/data/out/scanning.jld2, sha256 51844a46...):
  12 fixed mass columns (0-based j as below); for each, k = first beta index (beta ascending) with chi2 > 4,
  window k-3 .. k+2 (clipped); plus 2 below-table controls (j = 0, 17; beta = 1e-17, k = 99).
  Writes points.json (0-based j, k, stored Y, chi2) and points.dat (label, 1-based j, k) for wuxu_native_audit.jl.
Subcommand `analyze`: reads the CSV outputs of wuxu_native_audit.jl (default mode, any number of worker files;
  tight mode for N5) and evaluates N1-N5 exactly as preregistered, plus clearly labelled POST-HOC diagnostics.
Reading JLD2 needs h5py==3.12.1 (HDF5 1.14.4); h5py >= 3.16 refuses the JLD2 0.6 chunk encoding.
Run:
  python3 -I wuxu_native_audit_points_and_analysis.py points --jld2 <scanning.jld2> --outdir <dir>
  python3 -I wuxu_native_audit_points_and_analysis.py analyze --jld2 <scanning.jld2> --old-jld2 <scanning_old.jld2> \
      --points <points.json> --default <csv> [<csv> ...] --tight <csv> --out <file.json>
"""
import argparse, csv, hashlib, json, math, statistics
import numpy as np
import h5py

MASS_J = [22, 24, 26, 28, 31, 34, 38, 43, 51, 62, 80, 90]
CONTROLS = [(0, 99), (17, 99)]
N5_J = [26, 38, 62]
SHA_SCAN = "51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786"
Y_SBBN_AUTHORS = 0.24500000000000022          # main.ipynb cell 7 stored output
THR = 0.245 + 2 * 0.003                       # chi2 = 4 upper branch


def load(path):
    f = h5py.File(path, "r")
    Y = np.array(f["Y_P_mat"]); C2 = np.array(f["chi2_mat"])
    m = np.array(f["m_PBH_list [gram]"]); b = np.array(f["β_PBH_list"])
    if Y.shape == (len(b), len(m)):           # h5py axis0 = beta, axis1 = mass (Julia column-major)
        Y, C2 = Y.T, C2.T
    assert Y.shape == (len(m), len(b))
    assert np.all(np.diff(b) > 0) and np.all(np.diff(m) > 0)
    return Y, C2, m, b


def cmd_points(a):
    raw = open(a.jld2, "rb").read(); assert hashlib.sha256(raw).hexdigest() == SHA_SCAN
    Y, C2, m, b = load(a.jld2)
    pts, masses = [], {}
    for j in MASS_J:
        k = int(np.where(C2[j] > 4)[0][0])
        masses[str(j)] = {"m": float(m[j]), "k_first_excluded": k}
        for kk in range(max(0, k - 3), min(len(b), k + 3)):
            pts.append({"label": "band", "j": j, "k": kk, "m_g": float(m[j]), "beta": float(b[kk]),
                        "Y_stored": float(Y[j, kk]), "chi2_stored": float(C2[j, kk])})
    for j, k in CONTROLS:
        assert abs(b[k] - 1e-17) < 1e-30
        pts.append({"label": "control_below_table", "j": j, "k": k, "m_g": float(m[j]), "beta": float(b[k]),
                    "Y_stored": float(Y[j, k]), "chi2_stored": float(C2[j, k])})
    json.dump({"points": pts, "masses": masses}, open(f"{a.outdir}/points.json", "w"), indent=1)
    with open(f"{a.outdir}/points.dat", "w") as fh:
        for p in pts:
            fh.write(f"{p['label']} {p['j'] + 1} {p['k'] + 1}\n")
    print(len(pts), "points")


def read_csv(path):
    head = open(path).readline().strip()
    hdr = dict(kv.split("=") for kv in head[2:].split() if "=" in kv)
    rows = list(csv.DictReader([l for l in open(path) if not l.startswith("#")]))
    return hdr, rows


def crossing(pairs, thr=THR):
    """pairs (log10 beta, Y) sorted by beta; first upward crossing of thr, linear in log10 beta."""
    for (x0, y0), (x1, y1) in zip(pairs, pairs[1:]):
        if y0 <= thr < y1:
            return x0 + (thr - y0) * (x1 - x0) / (y1 - y0), "bracketed"
    return None, "not_bracketed"


def cmd_analyze(a):
    raw = open(a.jld2, "rb").read(); assert hashlib.sha256(raw).hexdigest() == SHA_SCAN
    Y, C2, m, b = load(a.jld2)
    Yo, C2o, mo, bo = load(a.old_jld2)
    P = json.load(open(a.points)); st = {(p["j"], p["k"]): p for p in P["points"]}
    res = {"h5py": h5py.__version__, "hdf5": h5py.version.hdf5_version, "scan_sha256": SHA_SCAN,
           "old_scan_sha256": hashlib.sha256(open(a.old_jld2, "rb").read()).hexdigest()}
    hdrs, rows = [], []
    for f in a.default:
        h, r = read_csv(f); hdrs.append(h); rows += r
    assert len({json.dumps(h, sort_keys=True) for h in hdrs}) == 1, "worker headers differ"
    H = hdrs[0]; res["default_header"] = H
    assert len(rows) == len(P["points"]) == len({(int(r["j"]), int(r["k"])) for r in rows})
    for r in rows:   # stored values in points.json must equal the scan file
        j, k = int(r["j"]), int(r["k"]); assert st[(j, k)]["Y_stored"] == float(Y[j, k])
        assert abs(float(r["Y_C"]) - float(r["Yp_returned"])) <= 1e-14

    # N1
    YC_sbbn = float(H["Y_C(T_nuc)"])
    res["N1"] = {"Y_SBBN_native": YC_sbbn, "Y_SBBN_authors_stored": Y_SBBN_AUTHORS,
                 "abs_diff": YC_sbbn - Y_SBBN_AUTHORS, "tolerance": 1e-12,
                 "verdict": "PASS" if abs(YC_sbbn - Y_SBBN_AUTHORS) < 1e-12 else "FAIL"}
    # N2
    d = []
    for r in rows:
        j, k = int(r["j"]), int(r["k"]); ys = st[(j, k)]["Y_stored"]; yn = float(r["Yp_returned"])
        d.append({"label": r["label"], "j": j, "k": k, "m_g": float(r["m_g"]), "beta": float(r["beta"]),
                  "Y_stored": ys, "Y_native": yn, "dY": yn - ys, "rel": (yn - ys) / ys})
    mx = max(abs(x["rel"]) for x in d)
    res["N2"] = {"n": len(d), "max_abs_rel": mx, "dY_min": min(x["dY"] for x in d), "dY_max": max(x["dY"] for x in d),
                 "dY_median": statistics.median(x["dY"] for x in d),
                 "dY_rms": math.sqrt(sum(x["dY"] ** 2 for x in d) / len(d)),
                 "verdict": "PASS" if mx < 1e-6 else ("INFO" if mx < 1e-4 else "FAIL"), "points": d}
    # N3
    res["N3"] = {"T_nuc_MeV": float(H["T_nuc_MeV"]), "T_nuc_prime_MeV": float(H["T_nuc_prime_MeV"]),
                 "X_SBBN_T_nuc": float(H["X_SBBN(T_nuc)"]), "X_SBBN_T_nuc_prime": float(H["X_SBBN(T_nuc_prime)"]),
                 "check_2X_prime_eq_0.245": abs(2 * float(H["X_SBBN(T_nuc_prime)"]) - 0.245) < 1e-12}
    # N4 and POST-HOC native-vs-stored contour
    lb = np.log10(b); per = {}; shifts = []; nat_vs_st = []
    for j in MASS_J:
        rj = sorted([r for r in rows if int(r["j"]) == j and r["label"] == "band"], key=lambda r: int(r["k"]))
        ks = [int(r["k"]) for r in rj]
        pC = [(float(lb[k]), float(r["Y_C"])) for k, r in zip(ks, rj)]
        pM = [(float(lb[k]), float(r["Y_M"])) for k, r in zip(ks, rj)]
        pS = [(float(lb[k]), float(Y[j, k])) for k in ks]
        bC, sC = crossing(pC); bM, sM = crossing(pM); bS, sS = crossing(pS)
        e = {"m_g": float(m[j]), "boundary_stored": bS, "boundary_native_C": bC, "boundary_native_M": bM,
             "status_C": sC, "status_M": sM, "status_stored": sS}
        if bM is None and bC is not None:     # boundary of Y_M beyond the window: lower bound + linear extrapolation
            (x0, y0), (x1, y1) = pM[-2], pM[-1]
            e["boundary_native_M_lower_bound"] = pM[-1][0]
            e["boundary_native_M_extrapolated"] = x1 + (THR - y1) * (x1 - x0) / (y1 - y0)
            e["shift_M_minus_C_lower_bound"] = pM[-1][0] - bC
            e["shift_M_minus_C_extrapolated"] = e["boundary_native_M_extrapolated"] - bC
        if bM is not None and bC is not None:
            e["shift_M_minus_C"] = bM - bC; shifts.append(bM - bC)
        if bC is not None and bS is not None:
            e["native_C_minus_stored"] = bC - bS; nat_vs_st.append(bC - bS)
        per[str(j)] = e
    all_sh = shifts + [per[k]["shift_M_minus_C_lower_bound"] for k in per if "shift_M_minus_C_lower_bound" in per[k]]
    res["N4"] = {"per_mass": per, "n_bracketed": len(shifts), "median_bracketed": statistics.median(shifts),
                 "min_bracketed": min(shifts), "max_bracketed": max(shifts),
                 "surrogate_REVIEW_031": {"direction": "weaker constraint (+)", "median": 0.10, "max": 0.15},
                 "falsifier": "any shift > 0.3 dex or opposite direction",
                 "any_opposite_direction": any(s < 0 for s in all_sh),
                 "any_gt_0.3_including_extrapolated": any(abs(v) > 0.3 for k in per for kk, v in per[k].items()
                                                         if kk.startswith("shift_M_minus_C") and v is not None)}
    res["N4"]["surrogate_falsified"] = res["N4"]["any_opposite_direction"] or res["N4"]["any_gt_0.3_including_extrapolated"]
    res["POSTHOC_contour_native_C_minus_stored"] = {"n": len(nat_vs_st), "median": statistics.median(nat_vs_st),
                                                    "min": min(nat_vs_st), "max": max(nat_vs_st)}
    # POST-HOC: SBBN limit of magic() (below-table controls) vs SBBN cell
    res["POSTHOC_controls"] = [{k: x[k] for k in ("m_g", "beta", "Y_stored", "Y_native", "dY")}
                               for x in d if x["label"] != "band"]
    # POST-HOC (exploratory): stored current scan vs stored v1 scan (scanning_old.jld2) at the same points
    same_grid = Yo.shape == Y.shape and np.allclose(mo, m, rtol=1e-12) and np.allclose(bo, b, rtol=1e-12)
    res["POSTHOC_old_scan_same_grid"] = bool(same_grid)
    if same_grid:
        dv = [float(Y[x["j"], x["k"]] - Yo[x["j"], x["k"]]) for x in d]
        res["POSTHOC_current_minus_v1_scan"] = {"min": min(dv), "max": max(dv), "median": statistics.median(dv)}
    # N5
    if a.tight:
        Ht, rt = read_csv(a.tight)
        n5 = []
        for r in rt:
            j, k = int(r["j"]), int(r["k"])
            dr = next(x for x in rows if int(x["j"]) == j and int(x["k"]) == k)
            n5.append({"j": j, "k": k, "m_g": float(r["m_g"]), "Y_tight": float(r["Yp_returned"]),
                       "Y_default": float(dr["Yp_returned"]), "Y_stored": st[(j, k)]["Y_stored"],
                       "dY_tight_minus_default": float(r["Yp_returned"]) - float(dr["Yp_returned"]),
                       "dY_tight_minus_stored": float(r["Yp_returned"]) - st[(j, k)]["Y_stored"],
                       "Y_M_tight": float(r["Y_M"]), "Y_M_default": float(dr["Y_M"])})
        res["N5"] = {"tight_header": Ht, "points": n5, "falsifier_abs_dY": 6e-4,
                     "max_abs_dY_tight_minus_default": max(abs(x["dY_tight_minus_default"]) for x in n5),
                     "Y_SBBN_tight": float(Ht["Y_C(T_nuc)"]), "T_nuc_prime_tight_MeV": float(Ht["T_nuc_prime_MeV"])}
        res["N5"]["verdict"] = "FALSIFIED" if res["N5"]["max_abs_dY_tight_minus_default"] > 6e-4 else "NOT_FALSIFIED"
        assert sorted(x["j"] for x in n5) == N5_J
    json.dump(res, open(a.out, "w"), indent=1, sort_keys=True)
    print(json.dumps({k: res[k]["verdict"] for k in ("N1", "N2", "N5") if k in res}),
          "N4 surrogate_falsified:", res["N4"]["surrogate_falsified"])


ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="cmd", required=True)
p1 = sp.add_parser("points"); p1.add_argument("--jld2", required=True); p1.add_argument("--outdir", required=True)
p2 = sp.add_parser("analyze"); p2.add_argument("--jld2", required=True); p2.add_argument("--old-jld2", required=True)
p2.add_argument("--points", required=True); p2.add_argument("--default", nargs="+", required=True)
p2.add_argument("--tight"); p2.add_argument("--out", required=True)
a = ap.parse_args()
cmd_points(a) if a.cmd == "points" else cmd_analyze(a)
