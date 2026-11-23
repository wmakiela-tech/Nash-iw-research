"""PREREG_116 analysis (frozen before the run): native threshold shifts from changes confined to the sub-1e9 g extrapolation
channel (p13, s15) or to the top endpoint (x0, x3), relative to table Sc (r_c from analysis109.json), and test of the
exposure-weighted proxy D (tables116.json) as a predictor: dr = r_arm - r_c, mean over the 4 cells (code/net x Y* 0.251/0.2484).
Usage: python3 -I analysis_116.py <d99 = 2026-11-22/data> <run_dir> <cfg_dir> <out.json>
Gates: G_TABLES (tables116.json: G_REBUILD_SC, G_FINITE), G_COMPLETE, G_V2 (as 112), G_DRIVER (k22_1720 code and net Y bitwise =
  099 s22_1720; net_base bitwise = 099), G_BASE (|Y_base(arm, j) - Y_base_l(099, j)| <= 5e-4).
Roots: linear crossing, exactly one bracket. Labels: GATE_FAIL_NO_LABEL / NOT_BRACKETED (per arm-mass) / MEASURED.
Prediction (Badacz, frozen), for each arm-mass A with proxy D_A: mean dr in [min(-0.8 D, -1.5 D) - 0.03, max(-0.8 D, -1.5 D) + 0.03]
  (c = -dr/D in [0.8, 1.5] from the binning calibration of 099/112, margin 0.03 = documented single-root maximum).
  Arm-masses: x0|22, x3|22, p13|22, p13|62, s15|22, s15|62. Descriptive: c_hat = -mean dr / D, per-cell dr."""
import csv, json, os, sys

TARGETS = [0.251, 0.2484]; MODELS = ["code", "net"]
AM = [("x0", 22), ("x3", 22), ("p13", 22), ("p13", 62), ("s15", 22), ("s15", 62)]


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
    out = {"gates": {}, "roots": {}, "cells": {}, "arm_mass": {}, "labels": {}, "predictions": {}}
    B = json.load(open(os.path.join(d99, "analysis109.json")))
    s99 = rd(os.path.join(d99, "summary_s_099.csv")); l99 = rd(os.path.join(d99, "summary_l_099.csv")); n99 = rdj(os.path.join(d99, "net099_raw.jsonl"))
    arms = ["k", "x0", "x3", "p13", "s15"]
    S = {a: rd(os.path.join(run, f"dd_{a}", "summary_orig.csv")) for a in arms}
    N = rdj(os.path.join(run, "out", "net116_raw.jsonl")); TG = json.load(open(os.path.join(run, "tables", "tables116.json")))
    cfg = {a: [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg116_{a}.dat")) if l.strip() and not l.startswith("#")] for a in arms}
    out["gates"]["G_TABLES"] = {"pass": all(g["pass"] for g in TG["gates"].values())}
    nexp = 1 + sum(len(v) for v in cfg.values())
    out["gates"]["G_COMPLETE"] = {"pass": all(sorted(S[a]) == sorted(cfg[a]) for a in arms) and len(N) == nexp and
                                  all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for a in arms for i in cfg[a])}
    nb = [(a, k) for a in S for k in S[a] if not k.endswith("_base")]
    out["gates"]["G_V2"] = {"pass": max(float(S[a][k]["v2_max_rel"]) for a, k in nb) <= 1e-6 and
                            all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for a in S for r in S[a].values())}
    drv = {"code": float(S["k"]["k22_1720"]["Y"]) == float(s99["s22_1720"]["Y"]), "net": N["net_k22_1720"]["YP_BBN"] == n99["net_s22_1720"]["YP_BBN"],
           "net_base": N["net_base"]["YP_BBN"] == n99["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    vb = {f"{a}{j}": abs(float(S[a][f"{a}{j}_base"]["Y"]) - float(l99[f"l{j}_base"]["Y"])) for a, j in AM}
    out["gates"]["G_BASE"] = {"absdiff": vb, "pass": all(v <= 5e-4 for v in vb.values())}
    if not all(g["pass"] for g in out["gates"].values()):
        out["labels"]["status"] = "GATE_FAIL_NO_LABEL"
    else:
        out["labels"]["status"] = "MEASURED"
        for a, j in AM:
            ids = sorted([i for i in cfg[a] if i.startswith(f"{a}{j}_") and not i.endswith("_base")], key=lambda i: float(S[a][i]["log10beta"]))
            lb = [float(S[a][i]["log10beta"]) for i in ids]
            ser = {"code": [float(S[a][i]["Y"]) for i in ids], "net": [N["net_" + i]["YP_BBN"] for i in ids]}
            drs = []
            for m in MODELS:
                for Y in TARGETS:
                    r = cross(lb, ser[m], Y); k = f"{j}|{m}|{Y}"; out["roots"][f"{a}_{k}"] = r
                    if r is not None:
                        dr = r - B["cells"][k]["r_c"]; out["cells"][f"{a}_{k}"] = {"r": r, "r_c": B["cells"][k]["r_c"], "dr": dr}; drs.append(dr)
            D = TG["D"][f"j{j}|{a}"]; lo = min(-0.8 * D, -1.5 * D) - 0.03; hi = max(-0.8 * D, -1.5 * D) + 0.03
            am = {"D": D, "interval": [lo, hi], "n_cells": len(drs)}
            if len(drs) != 4:
                am["status"] = "NOT_BRACKETED"; out["predictions"][f"{a}|{j}"] = None
            else:
                mean = sum(drs) / 4; am.update({"status": "MEASURED", "mean_dr": mean, "min_dr": min(drs), "max_dr": max(drs),
                                                "c_hat": (-mean / D) if D != 0 else None})
                out["predictions"][f"{a}|{j}"] = lo <= mean <= hi
            out["arm_mass"][f"{a}|{j}"] = am
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))
    print(json.dumps({k: {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items() if kk != "interval"} for k, v in out["arm_mass"].items()}))


if __name__ == "__main__":
    main(*sys.argv[1:5])
