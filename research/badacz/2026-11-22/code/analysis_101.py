"""PREREG_101 analysis (frozen before the native run): 2x2 factorial completion of PREREG_099 and a second solver-jitter sample.
Usage: python3 -I analysis_101.py <d99 = 2026-11-22/data> <run_dir> <cfg_dir> <out.json>
Arms (this run): v = table V (old sqrt(s) label, PY binning convention), e = table E = L x 1.0001, k = driver control (table L,
node 22 -17.20). From PREREG_099 (analysis099.json, same native code and nodes): l = L (old label, HER binning), s = Sa (new
label, HER binning), u = Ua (new label, PY binning); and the summaries summary_l_099.csv / net099_raw.jsonl for G_DRIVER.
Roots: linear crossing, exactly one bracket; 8 cells j in {22, 62} x {code, net} x Y* in {0.251, 0.2484}.
Factorial (label in {old,new} x bin in {old,new}): L=(o,o), Sa=(n,o), V=(o,n), Ua=(n,n).
  main_label = [(r_Sa - r_L) + (r_Ua - r_V)]/2 ; main_bin = [(r_V - r_L) + (r_Ua - r_Sa)]/2 ; I = (r_Ua - r_Sa) - (r_V - r_L)
  (for two factors the Shapley allocation equals the main effects).
Jitter: dj = r_E - r_L - (-log10 1.0001) per cell (uniform scale ~ beta shift; nonequivalence noted in REVIEW_095 r2).
Gates: G_TABLES (tables101.json G_CTRL/G_FINITE; V/L in rows 0-28 = log10(BIN_HW/BIN_PY) to 1e-6 dex), G_COMPLETE, G_V2, G_DRIVER
  (k22_1720 code and net Y bitwise = 099 l22_1720; net_base bitwise = 099 net_base), G_BASE (|Y_base - Y_base_l099| <= 5e-4).
Predictions (Badacz, frozen; tolerances from the documented maximum noise, max |d_ctrl| 0.031 in 099):
  Pr1 |I| <= 0.04 in >= 7/8 cells; Pr2 main_label < 0 in >= 7/8 cells; Pr3 max |dj| <= 0.04 and median |dj| <= 0.01."""
import csv, json, math, os, statistics, sys

TARGETS = [0.251, 0.2484]; MASSES = [22, 62]; MODELS = ["code", "net"]; ARMS = "ve"


def rd(p):
    return {r["run_id"]: r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))}


def rdj(p):
    o = {}
    for l in open(p):
        d = json.loads(l); o[d["run_id"]] = d
    return o


def cross(xs, ys, lev):
    br = [i for i in range(len(xs) - 1) if (ys[i] - lev) * (ys[i + 1] - lev) <= 0 and ys[i] != ys[i + 1]]
    if len(br) != 1:
        return None
    i = br[0]
    return xs[i] + (lev - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i])


def main(d99, run, cfg_dir, dst):
    A = json.load(open(os.path.join(d99, "analysis099.json")))
    sl = rd(os.path.join(d99, "summary_l_099.csv")); n99 = rdj(os.path.join(d99, "net099_raw.jsonl"))
    S = {a: rd(os.path.join(run, f"dd_{a}", "summary_orig.csv")) for a in ARMS + "k"}
    N = rdj(os.path.join(run, "out", "net101_raw.jsonl"))
    TG = json.load(open(os.path.join(run, "tables", "tables101.json")))
    cfg = {a: [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg101_{a}.dat")) if l.strip() and not l.startswith("#")] for a in ARMS + "k"}
    out = {"gates": {}, "roots": {}, "cells": {}, "labels": {}, "predictions": {}}
    vl = TG["descriptive"]["log10_V_over_L_rows0_28_min_max"]; tgt = math.log10(1.1395656964503507 / 1.0258141014810933)
    okv = all(abs(x - tgt) <= 1e-6 for v in vl.values() for x in v)
    out["gates"]["G_TABLES"] = {"tables": TG["gates"], "V_over_L_ok": okv, "pass": okv and all(g["pass"] for g in TG["gates"].values())}
    nexp = 1 + sum(len(v) for v in cfg.values())
    okc = all(sorted(S[a]) == sorted(cfg[a]) for a in S) and len(N) == nexp and all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for a in cfg for i in cfg[a]) and N["net_base"].get("rc") == 0
    out["gates"]["G_COMPLETE"] = {"native": {a: len(S[a]) for a in S}, "net": len(N), "net_expected": nexp, "pass": okc}
    nb = [(a, k) for a in S for k in S[a] if not k.endswith("_base")]
    v2 = [float(S[a][k]["v2_max_rel"]) for a, k in nb]
    out["gates"]["G_V2"] = {"max": max(v2), "pass": max(v2) <= 1e-6 and all(int(S[a][k]["v2_n"]) > 0 for a, k in nb)
                            and all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for a in S for r in S[a].values())}
    drv = {"code": float(S["k"]["k22_1720"]["Y"]) == float(sl["l22_1720"]["Y"]), "net": N["net_k22_1720"]["YP_BBN"] == n99["net_l22_1720"]["YP_BBN"],
           "net_base": N["net_base"]["YP_BBN"] == n99["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    vb = {f"{a}{j}": abs(float(S[a][f"{a}{j}_base"]["Y"]) - float(sl[f"l{j}_base"]["Y"])) for a in ARMS for j in MASSES}
    out["gates"]["G_BASE"] = {"absdiff": vb, "pass": all(x <= 5e-4 for x in vb.values())}
    gates_ok = all(g["pass"] for g in out["gates"].values())
    R = {}; nbr = 0
    for a in ARMS:
        for j in MASSES:
            ids = sorted([i for i in cfg[a] if i.startswith(f"{a}{j}_") and not i.endswith("_base")], key=lambda i: float(S[a][i]["log10beta"]))
            lb = [float(S[a][i]["log10beta"]) for i in ids]
            ser = {"code": [float(S[a][i]["Y"]) for i in ids], "net": [N["net_" + i]["YP_BBN"] for i in ids]}
            for m in MODELS:
                for Y in TARGETS:
                    r = cross(lb, ser[m], Y); nbr += r is None; R[(a, j, m, Y)] = r; out["roots"][f"{a}_{j}|{m}|{Y}"] = r
    for j in MASSES:
        for m in MODELS:
            for Y in TARGETS:
                rL = A["roots"][f"l_{j}|{m}|{Y}"]; rS = A["roots"][f"s_{j}|{m}|{Y}"]; rU = A["roots"][f"u_{j}|{m}|{Y}"]
                rV = R[("v", j, m, Y)]; rE = R[("e", j, m, Y)]
                c = {"r_L": rL, "r_Sa": rS, "r_Ua": rU, "r_V": rV, "r_E": rE}
                if None not in (rV, rE):
                    c.update({"main_label": ((rS - rL) + (rU - rV)) / 2, "main_bin": ((rV - rL) + (rU - rS)) / 2, "I": (rU - rS) - (rV - rL),
                              "bin_on_old": rV - rL, "bin_on_new": rU - rS, "label_on_old": rS - rL, "label_on_new": rU - rV,
                              "dj": rE - rL + math.log10(1.0001)})
                out["cells"][f"{j}|{m}|{Y}"] = c
    if not gates_ok:
        out["labels"] = {"status": "GATE_FAIL_NO_LABEL"}
    elif nbr:
        out["labels"] = {"status": "NOT_BRACKETED", "n_unbracketed": nbr}
    else:
        C = list(out["cells"].values()); dj = [abs(c["dj"]) for c in C]
        out["labels"] = {"status": "FACTORIAL_COMPLETE", "I_range": [min(c["I"] for c in C), max(c["I"] for c in C)],
                         "main_label_range": [min(c["main_label"] for c in C), max(c["main_label"] for c in C)],
                         "main_bin_range": [min(c["main_bin"] for c in C), max(c["main_bin"] for c in C)],
                         "dj_abs_median": statistics.median(dj), "dj_abs_max": max(dj)}
        out["predictions"] = {"Pr1_absI_le_0.04_in_ge7": sum(abs(c["I"]) <= 0.04 for c in C) >= 7,
                              "Pr2_main_label_neg_in_ge7": sum(c["main_label"] < 0 for c in C) >= 7,
                              "Pr3_jitter_max_le_0.04_median_le_0.01": max(dj) <= 0.04 and statistics.median(dj) <= 0.01}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
