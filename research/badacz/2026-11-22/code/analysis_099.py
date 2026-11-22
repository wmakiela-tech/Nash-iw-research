"""PREREG_099 analysis (frozen before the native run): threshold decomposition of the historical BlackHawk-HERWIG vs modern
Herwig 7.3 contrast (dhold, REVIEW_091/095, NOTE_096) into sqrt(s)-label, binning-convention and residual (kaon/vintage+tune).
Usage: python3 -I analysis_099.py <d90 = 2026-11-21/data> <run_dir> <cfg_dir> <out.json>
Arms: l = table L (my fold of the shipped BH tables as labelled; reproduces the 085 R2 table, G_CTRL), s = Sa (sqrt(s) fix,
constant above 5e4 GeV), b = Sb (sqrt(s) fix, H73-shaped above 5e4 GeV), u = Ua (sqrt(s) fix + PY binning convention),
k = driver control (R2 table, node 22 -17.20). References (frozen 090): HERBH (085 R2 table) and H73 roots.
Roots: linear crossing, exactly one bracket; cells j in {22, 62} x {code, net} x Y* in {0.251, 0.2484}.
Gates: G_TABLES (tables099.json: G_CTRL max|L/R2-1| <= 0.01, G_FINITE); G_COMPLETE; G_V2 (as 090/094); G_DRIVER (k22_1720
  code Y = 085 ho22_1720 and net Y = 085 net_ho22_1720 bitwise; net_base = 090 net_base bitwise); G_BASE (|Y_base - Y_base_085_HER|
  <= 5e-4).
Estimands per cell: d_ctrl = r_l - r_HERBH; d_label = r_s - r_l (and d_label_b = r_b - r_l); d_bin = r_u - r_s;
  d_resid = r_H73 - r_u; total = r_H73 - r_l = d_label + d_bin + d_resid (exact identity).
Link: G_LINK max |d_ctrl| <= 0.03 (else the decomposition is reported relative to L only, not to the 085/090 dhold).
Predictions (Badacz, frozen): Pr1 d_label < 0 in 8/8 cells; Pr2 |d_label| >= 0.3 |total| in >= 6/8; Pr3 d_resid < 0 in >= 6/8;
  Pr4 G_LINK PASS."""
import csv, json, os, sys

TARGETS = [0.251, 0.2484]; MASSES = [22, 62]; MODELS = ["code", "net"]; ARMS = "lsbu"


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


def main(d90, run, cfg_dir, dst):
    A = json.load(open(os.path.join(d90, "analysis090.json")))
    s85 = rd(os.path.join(d90, "summary_her_orig_085.csv")); n85 = rdj(os.path.join(d90, "net085_raw.jsonl"))
    n90 = rdj(os.path.join(d90, "net090_raw.jsonl"))
    S = {a: rd(os.path.join(run, f"dd_{a}", "summary_orig.csv")) for a in ARMS + "k"}
    N = rdj(os.path.join(run, "out", "net099_raw.jsonl"))
    TG = json.load(open(os.path.join(run, "tables", "tables099.json")))
    cfg = {a: [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg099_{a}.dat")) if l.strip() and not l.startswith("#")] for a in ARMS + "k"}
    out = {"gates": {}, "roots": {}, "cells": {}, "labels": {}, "predictions": {}}
    out["gates"]["G_TABLES"] = {"tables": TG["gates"], "pass": all(g["pass"] for g in TG["gates"].values())}
    nexp = 1 + sum(len(v) for v in cfg.values())
    okc = all(sorted(S[a]) == sorted(cfg[a]) for a in S) and len(N) == nexp and all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for a in cfg for i in cfg[a]) and N["net_base"].get("rc") == 0
    out["gates"]["G_COMPLETE"] = {"native": {a: len(S[a]) for a in S}, "net": len(N), "net_expected": nexp, "pass": okc}
    nb = [(a, k) for a in S for k in S[a] if not k.endswith("_base")]
    v2 = [float(S[a][k]["v2_max_rel"]) for a, k in nb]
    out["gates"]["G_V2"] = {"max": max(v2), "pass": max(v2) <= 1e-6 and all(int(S[a][k]["v2_n"]) > 0 for a, k in nb)
                            and all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for a in S for r in S[a].values())}
    drv = {"code": float(S["k"]["k22_1720"]["Y"]) == float(s85["ho22_1720"]["Y"]), "net": N["net_k22_1720"]["YP_BBN"] == n85["net_ho22_1720"]["YP_BBN"],
           "net_base": N["net_base"]["YP_BBN"] == n90["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    vb = {f"{a}{j}": abs(float(S[a][f"{a}{j}_base"]["Y"]) - float(s85[f"ho{j}_base"]["Y"])) for a in ARMS for j in MASSES}
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
                    r = cross(lb, ser[m], Y); nbr += r is None
                    R[(a, j, m, Y)] = r; out["roots"][f"{a}_{j}|{m}|{Y}"] = r
    f = lambda x, y: (x - y) if None not in (x, y) else None
    for j in MASSES:
        for m in MODELS:
            for Y in TARGETS:
                rH = A["roots"][f"HERBH_{j}|{m}|{Y}"]["lb"]; r73 = A["roots"][f"H73_{j}|{m}|{Y}"]["lb"]
                c = {"r_HERBH": rH, "r_H73": r73, "d_ctrl": f(R[("l", j, m, Y)], rH), "d_label": f(R[("s", j, m, Y)], R[("l", j, m, Y)]),
                     "d_label_b": f(R[("b", j, m, Y)], R[("l", j, m, Y)]), "d_bin": f(R[("u", j, m, Y)], R[("s", j, m, Y)]),
                     "d_resid": f(r73, R[("u", j, m, Y)]), "total": f(r73, R[("l", j, m, Y)])}
                if None not in c.values():
                    c["share_label"] = c["d_label"] / c["total"]; c["share_bin"] = c["d_bin"] / c["total"]; c["share_resid"] = c["d_resid"] / c["total"]
                    c["dominant"] = max(("label", "bin", "resid"), key=lambda k: abs(c["d_" + k]))
                out["cells"][f"{j}|{m}|{Y}"] = c
    if not gates_ok:
        out["labels"] = {"status": "GATE_FAIL_NO_LABEL"}
    elif nbr:
        out["labels"] = {"status": "NOT_BRACKETED", "n_unbracketed": nbr}
    else:
        C = list(out["cells"].values())
        link = max(abs(c["d_ctrl"]) for c in C) <= 0.03
        dom = {k: sum(c["dominant"] == k for c in C) for k in ("label", "bin", "resid")}
        out["labels"] = {"status": "DECOMPOSED", "G_LINK": link, "max_abs_d_ctrl": max(abs(c["d_ctrl"]) for c in C), "dominant_counts": dom,
                         "d_label_range": [min(c["d_label"] for c in C), max(c["d_label"] for c in C)],
                         "d_label_b_range": [min(c["d_label_b"] for c in C), max(c["d_label_b"] for c in C)],
                         "d_bin_range": [min(c["d_bin"] for c in C), max(c["d_bin"] for c in C)],
                         "d_resid_range": [min(c["d_resid"] for c in C), max(c["d_resid"] for c in C)],
                         "total_range": [min(c["total"] for c in C), max(c["total"] for c in C)]}
        out["predictions"] = {"Pr1_d_label_neg_8of8": sum(c["d_label"] < 0 for c in C) == 8,
                              "Pr2_label_share_ge_0.3_in_ge6": sum(abs(c["d_label"]) >= 0.3 * abs(c["total"]) for c in C) >= 6,
                              "Pr3_d_resid_neg_in_ge6": sum(c["d_resid"] < 0 for c in C) >= 6, "Pr4_G_LINK": link}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
