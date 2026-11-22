"""PREREG_109 analysis (frozen before the run): (A) seam check of the Herwig 7.1.5 channel recipes against the BlackHawk
HERWIG table row E' = 1e5 GeV (= sqrt(s) 1e5, primary 5e4 GeV) for all 10 hadronic channels; (B) native threshold shift of table
Sc (sqrt(s)-label fix with the 5e4-1e5 GeV primary range filled by Herwig 7.1.5) against L, Sa, Sb of PREREG_099.
Usage: python3 -I analysis_109.py <herwig_tables_dir> <d99 = 2026-11-22/data> <run_dir> <cfg_dir> <out.json>
(A) For channel c in {up,down,strange,charm,bottom,top,gluon->gluons,Wpm,Z0,tau}: N_BH = 2 x sum of column c at node E' = 1e5;
    N_71 = per-event multiplicity of mc109/herwig71_<c>.json at E = 5e4 (sqrt(s) = 1e5). L = log10(N_BH/N_71) for pi+-, K+-, K0L,
    p, n; tol = max(0.04, 4 se_L); cells with fewer than 20 counted particles in the MC (N_71 x events < 20) are reported, not gated.
    SEAM_PASS if every gated cell passes. G_MC: every MC energy rc 0, events 2000, |<E_final/sqrt(s)> - 1| <= 1e-3.
(B) Arm c roots (linear, exactly one bracket) on the 099 nodes; L/Sa/Sb roots from analysis099.json (l_, s_, b_).
    Gates: G_COMPLETE, G_V2 (as 099), G_DRIVER (k22_1720 code and net Y bitwise = 099 s22_1720; net_base bitwise = 099),
    G_BASE (|Y_base_c - Y_base_l(099)| <= 5e-4), G_TABLES (tables109.json G_CTRL/G_FINITE).
    Estimands per cell: d_label_c = r_c - r_l; r_c - r_s; r_c - r_b.
Predictions (Badacz, frozen; tolerances >= the documented max single-root variation 0.03): Pr1 SEAM_PASS; Pr2 |r_c - r_s| <= 0.03 in
  4/4 j62 cells (the 5e4-1e5 GeV range is irrelevant at j62); Pr3 r_c within [min(r_s, r_b) - 0.03, max(r_s, r_b) + 0.03] in >= 3/4 j22
  cells."""
import csv, json, math, os, sys
import numpy as np

SP = {"pipm": "211", "Kpm": "321", "K0L": "130", "proton": "2212", "neutron": "2112"}
CH = {"up": "up", "down": "down", "strange": "strange", "charm": "charm", "bottom": "bottom", "top": "top", "gluon": "gluons", "Wpm": "Wpm", "Z0": "Z0", "tau": "tau"}
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


def main(tdir, d99, run, cfg_dir, dst):
    out = {"seam": {}, "gates": {}, "roots": {}, "cells": {}, "labels": {}, "predictions": {}}
    tab = {}
    for name in SP:
        L = open(os.path.join(tdir, name + ".txt")).read().splitlines(); hdr = L[0].split()
        a = np.array([[float(x) for x in l.split()] for l in L[1:]]); tab[name] = (hdr, a)
    okmc = True; seam_ok = True
    for c, col in CH.items():
        d = json.load(open(os.path.join(run, "mc109", f"herwig71_{c}.json")))
        for e in d["energies"]:
            okmc &= e.get("rc_read") == 0 and e.get("rc_run") == 0 and e.get("events") == 2000 and abs(e["Efinal_over_sqrts"] - 1) <= 1e-3
        e5 = min(d["energies"], key=lambda e: abs(e["E"] - 5e4))
        cell = {"max_abs_event_Eresidual": max(e.get("max_abs_event_Eresidual", 0) for e in d["energies"])}
        for s, p in SP.items():
            hdr, a = tab[s]; iu = hdr.index(col); top = a[:, 0].max()
            nbh = float(2 * a[a[:, 0] == top][:, iu].sum()); n71 = e5[p]; se = e5["se_" + p]
            gated = n71 * e5["events"] >= 20 and nbh > 0
            L = math.log10(nbh / n71) if (nbh > 0 and n71 > 0) else None
            tol = max(0.04, 4 * se / n71 / math.log(10)) if n71 > 0 else None
            ok = (abs(L) <= tol) if gated else None
            if gated and not ok:
                seam_ok = False
            cell[s] = {"N_BH": nbh, "N_71": n71, "L": L, "tol": tol, "gated": gated, "pass": ok}
        out["seam"][c] = cell
    out["gates"]["G_MC"] = {"pass": okmc}
    out["labels"]["SEAM"] = "SEAM_PASS" if seam_ok else "SEAM_FAIL"
    A = json.load(open(os.path.join(d99, "analysis099.json")))
    s99 = rd(os.path.join(d99, "summary_s_099.csv")); l99 = rd(os.path.join(d99, "summary_l_099.csv")); n99 = rdj(os.path.join(d99, "net099_raw.jsonl"))
    S = {a: rd(os.path.join(run, f"dd_{a}", "summary_orig.csv")) for a in "kc"}
    N = rdj(os.path.join(run, "out", "net109_raw.jsonl")); TG = json.load(open(os.path.join(run, "tables", "tables109.json")))
    cfg = {a: [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg109_{a}.dat")) if l.strip() and not l.startswith("#")] for a in "kc"}
    out["gates"]["G_TABLES"] = {"pass": all(g["pass"] for g in TG["gates"].values())}
    nexp = 1 + sum(len(v) for v in cfg.values())
    out["gates"]["G_COMPLETE"] = {"pass": all(sorted(S[a]) == sorted(cfg[a]) for a in S) and len(N) == nexp and all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for a in cfg for i in cfg[a])}
    nb = [(a, k) for a in S for k in S[a] if not k.endswith("_base")]
    out["gates"]["G_V2"] = {"pass": max(float(S[a][k]["v2_max_rel"]) for a, k in nb) <= 1e-6 and all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for a in S for r in S[a].values())}
    drv = {"code": float(S["k"]["k22_1720"]["Y"]) == float(s99["s22_1720"]["Y"]), "net": N["net_k22_1720"]["YP_BBN"] == n99["net_s22_1720"]["YP_BBN"],
           "net_base": N["net_base"]["YP_BBN"] == n99["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    vb = {j: abs(float(S["c"][f"c{j}_base"]["Y"]) - float(l99[f"l{j}_base"]["Y"])) for j in MASSES}
    out["gates"]["G_BASE"] = {"absdiff": vb, "pass": all(v <= 5e-4 for v in vb.values())}
    nbr = 0
    for j in MASSES:
        ids = sorted([i for i in cfg["c"] if i.startswith(f"c{j}_") and not i.endswith("_base")], key=lambda i: float(S["c"][i]["log10beta"]))
        lb = [float(S["c"][i]["log10beta"]) for i in ids]
        ser = {"code": [float(S["c"][i]["Y"]) for i in ids], "net": [N["net_" + i]["YP_BBN"] for i in ids]}
        for m in MODELS:
            for Y in TARGETS:
                r = cross(lb, ser[m], Y); nbr += r is None; out["roots"][f"c_{j}|{m}|{Y}"] = r
                rl, rs, rb = (A["roots"][f"{x}_{j}|{m}|{Y}"] for x in "lsb")
                out["cells"][f"{j}|{m}|{Y}"] = {"r_c": r, "r_l": rl, "r_s": rs, "r_b": rb,
                                                "d_label_c": (r - rl) if r is not None else None, "c_minus_s": (r - rs) if r is not None else None,
                                                "c_minus_b": (r - rb) if r is not None else None,
                                                "in_band": (min(rs, rb) - 0.03 <= r <= max(rs, rb) + 0.03) if r is not None else None}
    gok = all(g["pass"] for g in out["gates"].values())
    if not gok:
        out["labels"]["status"] = "GATE_FAIL_NO_LABEL"
    elif nbr:
        out["labels"]["status"] = "NOT_BRACKETED"
    else:
        C = out["cells"]
        j22 = [v for k, v in C.items() if k.startswith("22")]; j62 = [v for k, v in C.items() if k.startswith("62")]
        out["labels"]["status"] = "MEASURED"
        out["labels"]["d_label_c_j22"] = [min(v["d_label_c"] for v in j22), max(v["d_label_c"] for v in j22)]
        out["labels"]["d_label_c_j62"] = [min(v["d_label_c"] for v in j62), max(v["d_label_c"] for v in j62)]
        out["predictions"] = {"Pr1_SEAM_PASS": seam_ok, "Pr2_j62_abs_c_minus_s_le_0.03_4of4": all(abs(v["c_minus_s"]) <= 0.03 for v in j62),
                              "Pr3_j22_in_band_ge3of4": sum(v["in_band"] for v in j22) >= 3}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))


if __name__ == "__main__":
    main(*sys.argv[1:6])
