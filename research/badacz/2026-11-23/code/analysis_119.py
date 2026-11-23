#!/usr/bin/env python3
"""PREREG_119 analysis: (A) native no-PBH background of the Wu-Xu code (arms code/ad x solver def/r8/r9 x start j22/j62);
(B) G_EC+(a): BlackHawk v2.3 Page factor f(M) (fM.txt, a = 0) vs the code's mass-loss normalisation
f_code(M) = N_BH(T_BH) m_Pl^4, and energy consistency of the 090 primary spectra with fM.txt.
All thresholds below are frozen in PREREG_119 (do not edit after the run).
Usage: python3 -I analysis_119.py <run dir with bg_/summary_ files> <fcode_119.csv> <fM.txt> <primary_spectra_090.tsv(.gz)>
       <rates_w22.csv> <rates_w62.csv> <out.json>
"""
import csv, gzip, hashlib, json, math, sys
import numpy as np

RUN, FCODE, FM, PRIM, D22, D62, OUT = sys.argv[1:8]
HBAR = 6.582119569e-25          # GeV s (CODATA 2018)
ARMS = [(a, s, j) for a in ("code", "ad") for s in ("def", "r8", "r9") for j in (22, 62)]
REF = {"Y_code_reduced": 0.244893107963255, "Y_ad_reduced": 0.247963542410937, "dY_reduced": 0.0030704,
       "Qratio_code": 1.14678163340783, "dt_ratio": 1.02922284036883, "Y_def_baseline": 0.24473}
TOL = {"Y": 2e-4, "Q": 0.002, "dt": 0.002, "conv": 2e-5, "rep": 2e-5, "G1": (0.55, 0.62), "G2": 0.03, "G3": 0.005}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def rd(p):
    return list(csv.DictReader(open(p)))


out = {"inputs_sha256": {}, "A": {"runs": {}}, "B": {}, "gates": {}, "predictions": {}, "ref": REF, "tol": TOL}
for p in (FCODE, FM, PRIM, D22, D62):
    out["inputs_sha256"][p.split("/")[-1]] = sha(p)

# ---------------- A: no-PBH background ----------------
R = out["A"]["runs"]; ok_run = True
for a, s, j in ARMS:
    tag = f"{a}_{s}_j{j}"
    try:
        sm = rd(f"{RUN}/summary_{tag}.csv")[0]; bg = rd(f"{RUN}/bg_{tag}.csv")
        out["inputs_sha256"][f"bg_{tag}.csv"] = sha(f"{RUN}/bg_{tag}.csv")
        out["inputs_sha256"][f"summary_{tag}.csv"] = sha(f"{RUN}/summary_{tag}.csv")
    except (OSError, IndexError):
        ok_run = False; continue
    b = {round(float(r["T_target_MeV"]), 6): r for r in bg}
    T10, Tn = b[10.0], b[round(float(sm["T_nuc_MeV"]), 6)]
    R[tag] = {"Y": float(sm["Y"]), "retcode": sm["retcode"], "nsteps": int(sm["nsteps"]), "wall_s": float(sm["wall_s"]),
              "Qratio": float(Tn["Q_a3NsT3_GeV3"]) / float(T10["Q_a3NsT3_GeV3"]),
              "dt_10_to_nuc_s": float(Tn["t_s"]) - float(T10["t_s"]),
              "X_at": {k: float(v["X_n"]) for k, v in b.items()},
              "t_at": {k: float(v["t_s"]) for k, v in b.items()},
              "Qrel_at": {k: float(v["Q_a3NsT3_GeV3"]) / float(T10["Q_a3NsT3_GeV3"]) for k, v in b.items()}}
    ok_run &= sm["retcode"] == "Success"
out["gates"]["G_RUN"] = bool(ok_run and len(R) == len(ARMS))


def g(tag, k):
    return R[tag][k]


if out["gates"]["G_RUN"]:
    js = (22, 62)
    out["gates"]["G_AD"] = all(abs(g(f"ad_r9_j{j}", "Qratio") - 1) <= TOL["Q"] for j in js)
    out["gates"]["G_CONV"] = all(abs(g(f"{a}_r8_j{j}", "Y") - g(f"{a}_r9_j{j}", "Y")) <= TOL["conv"] for a in ("code", "ad") for j in js)
    out["gates"]["G_REP"] = all(abs(g(f"{a}_r9_j22", "Y") - g(f"{a}_r9_j62", "Y")) <= TOL["rep"] for a in ("code", "ad"))
    P = out["predictions"]
    P["P0_Y_code_r9"] = {"values": [g(f"code_r9_j{j}", "Y") for j in js], "ref": REF["Y_code_reduced"]}
    P["P0d_Y_code_def"] = {"values": [g(f"code_def_j{j}", "Y") for j in js], "ref": REF["Y_def_baseline"]}
    P["P1_Qratio_code_r9"] = {"values": [g(f"code_r9_j{j}", "Qratio") for j in js], "ref": REF["Qratio_code"]}
    P["P2_dt_ratio_r9"] = {"values": [g(f"code_r9_j{j}", "dt_10_to_nuc_s") / g(f"ad_r9_j{j}", "dt_10_to_nuc_s") for j in js],
                           "ref": REF["dt_ratio"]}
    P["P3_dY_ad_minus_code_r9"] = {"values": [g(f"ad_r9_j{j}", "Y") - g(f"code_r9_j{j}", "Y") for j in js], "ref": REF["dY_reduced"]}
    for k, tol in (("P0_Y_code_r9", TOL["Y"]), ("P0d_Y_code_def", TOL["Y"]), ("P1_Qratio_code_r9", TOL["Q"]),
                   ("P2_dt_ratio_r9", TOL["dt"]), ("P3_dY_ad_minus_code_r9", TOL["Y"])):
        P[k]["tol"] = tol; P[k]["PASS"] = all(abs(v - P[k]["ref"]) <= tol for v in P[k]["values"])
    out["A"]["reported"] = {
        "Y_ad_r9_vs_reduced": [g(f"ad_r9_j{j}", "Y") - REF["Y_ad_reduced"] for j in js],
        "dY_ad_minus_code_def": [g(f"ad_def_j{j}", "Y") - g(f"code_def_j{j}", "Y") for j in js],
        "solver_noise_Y_def_minus_r9": {a: [g(f"{a}_def_j{j}", "Y") - g(f"{a}_r9_j{j}", "Y") for j in js] for a in ("code", "ad")},
        "Qratio_def": {a: [g(f"{a}_def_j{j}", "Qratio") for j in js] for a in ("code", "ad")}}

# ---------------- B: G_EC+(a) ----------------
fc = rd(FCODE)
MG = np.array([float(r["M_GeV"]) for r in fc]); Mg = np.array([float(r["M_g"]) for r in fc])
fcode = np.array([float(r["f_code_GeV4"]) for r in fc]); GeV_per_g = float(np.median(MG / Mg))
fm = [l.split() for l in open(FM) if l.strip()]
fmM = np.array([float(x[0]) for x in fm[1:]]); fBH = np.array([float(x[1]) for x in fm[1:]])
assert fm[0][0] == "mass/a" and float(fm[0][1]) == 0.0 and np.allclose(fmM, MG, rtol=1e-12, atol=0)
Rm = fBH / fcode
win = (Mg >= 1.0) & (Mg <= 1e10)
B = out["B"]
B["GeV_per_g"] = GeV_per_g
B["R_window_1g_1e10g"] = {"min": float(Rm[win].min()), "max": float(Rm[win].max()), "n": int(win.sum())}
B["R_full_table"] = {"min": float(Rm.min()), "max": float(Rm.max()), "M_g_at_min": float(Mg[Rm.argmin()]),
                     "M_g_at_max": float(Mg[Rm.argmax()])}
B["f_code_GeV4_window"] = {"min": float(fcode[win].min()), "max": float(fcode[win].max())}
B["f_BH_GeV4_window"] = {"min": float(fBH[win].min()), "max": float(fBH[win].max())}
out["predictions"]["P_G1_R_in_band"] = {"band": TOL["G1"], "PASS": bool(TOL["G1"][0] <= Rm[win].min() and Rm[win].max() <= TOL["G1"][1])}


def lifetime(Minit_g, f):   # tau = int_0^M M'^2 / f(M') dM' (natural units -> s); f log-log interpolated, M < table min: f(min)
    lnM = np.log(MG); lnf = np.log(f)
    M = np.geomspace(MG[0] * 1e-3, Minit_g * GeV_per_g, 200001)
    fi = np.exp(np.interp(np.log(M), lnM, lnf))
    return float(np.trapezoid(M ** 2 / fi, M) * HBAR)


grid = np.geomspace(6e8, 1e10, 100)
B["lifetimes"] = {}
for j, dump in ((22, D22), (62, D62)):
    rows = rd(dump); t = np.array([float(r["t_s"]) for r in rows]); al = np.array([float(r["n_PBH_alive"]) for r in rows]) > 0.5
    tau_dump = float(t[al].max()); M0 = float(grid[j])
    tc, tb = lifetime(M0, fcode), lifetime(M0, fBH); tstd = 407.0 * (M0 / 1e10) ** 3
    B["lifetimes"][f"j{j}"] = {"M_init_g": M0, "tau_dump_s": tau_dump, "tau_from_f_code_s": tc, "tau_from_f_BH_s": tb,
                               "tau_407_s": tstd, "tau_BH_over_tau_code": tb / tc, "tau_BH_over_407": tb / tstd,
                               "tau_code_over_dump": tc / tau_dump}
out["gates"]["P_G3_code_side_extraction"] = all(abs(v["tau_code_over_dump"] - 1) <= TOL["G3"] for v in B["lifetimes"].values())

op = gzip.open if PRIM.endswith(".gz") else open
rows = [l.rstrip("\n").split("\t") for l in op(PRIM, "rt")]
h = rows[0]; d = np.array([[float(x) for x in r] for r in rows[1:]])
chan = [c for c in h if c not in ("k", "m_g", "energy")]
ms = np.unique(d[:, 1]); res = []
for mg in ms:
    s = d[d[:, 1] == mg]; s = s[np.argsort(s[:, h.index("energy")])]
    E = s[:, h.index("energy")]; Phi = sum(s[:, h.index(c)] for c in chan)
    Pspec = float(np.trapezoid(E * E * Phi, np.log(E)))                       # GeV/s per BH
    fM_here = float(np.exp(np.interp(np.log(mg * GeV_per_g), np.log(MG), np.log(fBH))))
    PfM = fM_here / (mg * GeV_per_g) ** 2 / HBAR
    e2 = E * E * Phi
    res.append({"M_g": float(mg), "P_spec_over_P_fM": Pspec / PfM, "edge_lo": float(e2[0] / e2.max()), "edge_hi": float(e2[-1] / e2.max())})
B["spectra_vs_fM"] = res
B["channels"] = chan
sel = [r for r in res if 2e9 <= r["M_g"] <= 1e11]
out["predictions"]["P_G2_spectra_energy_consistency"] = {"n": len(sel), "tol": TOL["G2"],
    "max_abs_dev": float(max(abs(r["P_spec_over_P_fM"] - 1) for r in sel)),
    "PASS": all(abs(r["P_spec_over_P_fM"] - 1) <= TOL["G2"] for r in sel)}
json.dump(out, open(OUT, "w"), indent=1, sort_keys=True)
print(json.dumps({"gates": out["gates"], "predictions": {k: v.get("PASS") for k, v in out["predictions"].items()}}, indent=1))
