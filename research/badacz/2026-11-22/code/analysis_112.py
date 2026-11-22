"""PREREG_112 analysis (frozen before the run): split of the threshold contrast r_H73 - r_HERBH along the path
HERBH -> L -> Sc (label, 109) -> V (PY binning on Sc) -> W (own Herwig 7.1.5 MC, 090 construction) -> H73 (Herwig 7.3, 090).
Usage: python3 -I analysis_112.py <d99 = 2026-11-22/data> <run_dir> <cfg_dir> <out.json>
Roots: arms w and v on the 099/109 nodes (linear crossing, exactly one bracket); r_HERBH, r_H73, r_l from analysis099.json;
  r_c from analysis109.json.
Gates: G_TABLES (tables112.json: G_MC, G_STAT, G_REBUILD_H73, G_REBUILD_SC, G_FINITE), G_COMPLETE, G_V2 (as 099/109),
  G_DRIVER (k22_1720 code and net Y bitwise = 099 s22_1720; net_base bitwise = 099), G_BASE (|Y_base_a - Y_base_l(099)| <= 5e-4,
  a in {w, v}, j in {22, 62}).
Estimands per cell (dex): bin_c = r_V - r_c; proc = r_W - r_V (table processing at fixed vintage 7.1.5); vint = r_H73 - r_W
  (generator vintage 7.1.5 -> 7.3 at fixed recipe and fold). Closure: (r_c - r_l) + bin_c + proc + vint = total(099) = r_H73 - r_l (d_ctrl = r_l - r_HERBH is reported, not part of total).
Predictions (Badacz, frozen; tolerances >= 0.03, the documented maximum single-root variation):
  Pr1 |proc| <= 0.03 in >= 6/8 cells; Pr2 vint <= -0.03 in >= 3/4 j22 cells; Pr3 |vint| <= 0.03 in >= 3/4 j62 cells;
  Pr4 |bin_c - d_bin(099)| <= 0.03 in 8/8 cells."""
import csv, json, os, sys

TARGETS = [0.251, 0.2484]; MASSES = [22, 62]; MODELS = ["code", "net"]


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
    out = {"gates": {}, "roots": {}, "cells": {}, "labels": {}, "predictions": {}}
    A = json.load(open(os.path.join(d99, "analysis099.json"))); B = json.load(open(os.path.join(d99, "analysis109.json")))
    s99 = rd(os.path.join(d99, "summary_s_099.csv")); l99 = rd(os.path.join(d99, "summary_l_099.csv")); n99 = rdj(os.path.join(d99, "net099_raw.jsonl"))
    S = {a: rd(os.path.join(run, f"dd_{a}", "summary_orig.csv")) for a in "kwv"}
    N = rdj(os.path.join(run, "out", "net112_raw.jsonl")); TG = json.load(open(os.path.join(run, "tables", "tables112.json")))
    cfg = {a: [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg112_{a}.dat")) if l.strip() and not l.startswith("#")] for a in "kwv"}
    out["gates"]["G_TABLES"] = {"pass": all(g["pass"] for g in TG["gates"].values())}
    nexp = 1 + sum(len(v) for v in cfg.values())
    out["gates"]["G_COMPLETE"] = {"pass": all(sorted(S[a]) == sorted(cfg[a]) for a in S) and len(N) == nexp and all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for a in cfg for i in cfg[a])}
    nb = [(a, k) for a in S for k in S[a] if not k.endswith("_base")]
    out["gates"]["G_V2"] = {"pass": max(float(S[a][k]["v2_max_rel"]) for a, k in nb) <= 1e-6 and all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for a in S for r in S[a].values())}
    drv = {"code": float(S["k"]["k22_1720"]["Y"]) == float(s99["s22_1720"]["Y"]), "net": N["net_k22_1720"]["YP_BBN"] == n99["net_s22_1720"]["YP_BBN"],
           "net_base": N["net_base"]["YP_BBN"] == n99["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    vb = {f"{a}{j}": abs(float(S[a][f"{a}{j}_base"]["Y"]) - float(l99[f"l{j}_base"]["Y"])) for a in "wv" for j in MASSES}
    out["gates"]["G_BASE"] = {"absdiff": vb, "pass": all(v <= 5e-4 for v in vb.values())}
    nbr = 0
    for a in "wv":
        for j in MASSES:
            ids = sorted([i for i in cfg[a] if i.startswith(f"{a}{j}_") and not i.endswith("_base")], key=lambda i: float(S[a][i]["log10beta"]))
            lb = [float(S[a][i]["log10beta"]) for i in ids]
            ser = {"code": [float(S[a][i]["Y"]) for i in ids], "net": [N["net_" + i]["YP_BBN"] for i in ids]}
            for m in MODELS:
                for Y in TARGETS:
                    r = cross(lb, ser[m], Y); nbr += r is None; out["roots"][f"{a}_{j}|{m}|{Y}"] = r
    gok = all(g["pass"] for g in out["gates"].values())
    if not gok:
        out["labels"]["status"] = "GATE_FAIL_NO_LABEL"
    elif nbr:
        out["labels"]["status"] = "NOT_BRACKETED"
    else:
        for j in MASSES:
            for m in MODELS:
                for Y in TARGETS:
                    k = f"{j}|{m}|{Y}"; c99 = A["cells"][k]; rl = A["roots"][f"l_{j}|{m}|{Y}"]
                    rc = B["cells"][k]["r_c"]; rv = out["roots"][f"v_{j}|{m}|{Y}"]; rw = out["roots"][f"w_{j}|{m}|{Y}"]
                    cell = {"r_HERBH": c99["r_HERBH"], "r_l": rl, "r_c": rc, "r_V": rv, "r_W": rw, "r_H73": c99["r_H73"],
                            "d_ctrl": c99["d_ctrl"], "label_c": rc - rl, "bin_c": rv - rc, "proc": rw - rv, "vint": c99["r_H73"] - rw,
                            "total": c99["total"], "d_bin_099": c99["d_bin"]}
                    cell["closure"] = cell["label_c"] + cell["bin_c"] + cell["proc"] + cell["vint"] - cell["total"]  # total(099) = r_H73 - r_l
                    out["cells"][k] = cell
        C = out["cells"]; j22 = [v for k, v in C.items() if k.startswith("22")]; j62 = [v for k, v in C.items() if k.startswith("62")]
        out["labels"]["status"] = "MEASURED"
        out["labels"]["max_abs_closure"] = max(abs(v["closure"]) for v in C.values())
        for q in ("bin_c", "proc", "vint"):
            out["labels"][f"{q}_j22"] = [min(v[q] for v in j22), max(v[q] for v in j22)]
            out["labels"][f"{q}_j62"] = [min(v[q] for v in j62), max(v[q] for v in j62)]
        out["predictions"] = {"Pr1_abs_proc_le_0.03_ge6of8": sum(abs(v["proc"]) <= 0.03 for v in C.values()) >= 6,
                              "Pr2_j22_vint_le_-0.03_ge3of4": sum(v["vint"] <= -0.03 for v in j22) >= 3,
                              "Pr3_j62_abs_vint_le_0.03_ge3of4": sum(abs(v["vint"]) <= 0.03 for v in j62) >= 3,
                              "Pr4_abs_binc_minus_dbin099_le_0.03_8of8": all(abs(v["bin_c"] - v["d_bin_099"]) <= 0.03 for v in C.values())}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
