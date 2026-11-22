"""PREREG_094 analysis (frozen before any native run): does the modern-generator label survive real MC replicas run
through the native solver, and how large is pure solver jitter at the roots?
Usage: python3 -I analysis_094.py <d90 = 2026-11-21/data> <run_dir> <cfg_dir> <out.json>
Arms: a/b = P83/H73 replica R1, c/d = R2 (tables from REVIEW_091 r2), e/f = nominal x 1.001 (J, solver-jitter probe),
k = driver control (nominal P83, j22 -17.20). Nominal = frozen 090 (analysis090.json).
Roots: linear crossing, exactly one bracket, on the window nodes (cfg094_*), Y* in {0.251, 0.2484}, model in {code, net}.
Gates (all must PASS for labels): G_COMPLETE, G_V2 (v2_max_rel <= 1e-6, v2_n > 0, n_points >= 20000, i_last_alive > 200),
  G_TABLES (a-d, k SHA as 090 manifest; e/f = nominal x 1.001 to 1e-12 rel), G_DRIVER (k22_1720 code Y and net Y, and
  net_base, bitwise equal to 090), G_WINDOW (nominal 090 roots recomputed on window nodes equal 090 roots, |d| <= 1e-12),
  G_BASE (|Y_base_arm - Y_base_090| <= 5e-4, as 090 V_BASE).
Estimands per realization X in {J, R1, R2} and cell (j, model, Y*): droot_T,X = root_T,X - root_T,nom;
  dmod_X = root_H73,X - root_P83,X; ddmod_X = dmod_X - dmod_nom.
  Jitter root estimate eps = droot_J + log10(1.001) (removes the expected physical shift -log10 f of a uniform yield scale f);
  ratio |eps| / noise_dex(090, N_Y-based).
  Node level: dY = Y_arm - Y_nom at identical (j, lb) nodes, for code and net.
Labels: LM_X by the frozen 090 rule on the 8 dmod_X (max|dmod| < 0.10 SMALL; >= 0.27 COMPARABLE; else INTERMEDIATE).
Predictions (Badacz, frozen): Pr1 LM_X = MOD_INTERMEDIATE for J, R1, R2; Pr2 max |ddmod_R| over 16 (cell, R) <= 0.04;
  Pr3 median |eps|/noise_dex <= 1 and max <= 3 over the 16 jitter roots.
Status: LM_STABLE_IN_3_REALIZATIONS if all LM_X INTERMEDIATE and all 24 dmod_X in [0.10, 0.27);
  LM_STABLE_CELLWISE_EXCURSIONS if all LM_X INTERMEDIATE but some dmod_X outside; LM_FLIPS otherwise.
  Three realizations are not a confidence interval; the status does not by itself lift the HOLD of REVIEW_091 r3."""
import csv, hashlib, json, math, os, statistics, sys

TARGETS = [0.251, 0.2484]; MASSES = [22, 62]; MODELS = ["code", "net"]
ARMS = {"a": ("P83", "R1"), "b": ("H73", "R1"), "c": ("P83", "R2"), "d": ("H73", "R2"), "e": ("P83", "J"), "f": ("H73", "J")}
REAL = {"R1": ("a", "b"), "R2": ("c", "d"), "J": ("e", "f")}
F = 1.001
SHA = {"a": "afb4dddcd3c78088ed21afd5b7609b6f10d8bfcc17fa46e9fd95990b0e4386a1", "b": "041b0bb6d09dd3f606f7ac167eb0a718c1e158060c90f775d2548d61cd3bf18b",
       "c": "536d0546259dcb158d6e1dafbdf10299eb3fc2f99b5c4f9f438242bedcc3f499", "d": "5708993c33ec81a0c878d58477243f49c08d35d267f25065127c267c991f1e68",
       "k": "67dad44eeb44004a916f7fa5cfda33f4660c7424524893e5e9c4f715d49d5289"}
NOM = {"P83": "67dad44eeb44004a916f7fa5cfda33f4660c7424524893e5e9c4f715d49d5289", "H73": "5e5334ca7c8efdf4ebde8c72583f94f6257355d2d16326b52cfb79a7d6a8ec66"}


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
        return None, None
    i = br[0]
    return xs[i] + (lev - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i]), (ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i])


def label(dm):
    mx = max(abs(x) for x in dm)
    return "MOD_SMALL" if mx < 0.10 else ("MOD_COMPARABLE" if mx >= 0.27 else "MOD_INTERMEDIATE")


def tab(p):
    L = open(p).read().splitlines()[1:]
    return [[float(x) for x in l.split("\t")] for l in L]


def main(d90, run, cfg_dir, dst):
    A = json.load(open(os.path.join(d90, "analysis090.json")))
    s90 = {v: rd(os.path.join(d90, f"summary_{v}_orig_090.csv")) for v in "ph"}
    n90 = rdj(os.path.join(d90, "net090_raw.jsonl"))
    S = {a: rd(os.path.join(run, f"dd_{a}", "summary_orig.csv")) for a in list(ARMS) + ["k"]}
    N = rdj(os.path.join(run, "out", "net094_raw.jsonl"))
    cfg = {a: [l.split()[0] for l in open(os.path.join(cfg_dir, f"cfg094_{a}.dat")) if l.strip() and not l.startswith("#")] for a in list(ARMS) + ["k"]}
    out = {"gates": {}, "nominal": {}, "series": {}, "roots": {}, "cells": {}, "jitter": {}, "node_level": {}, "labels": {}, "predictions": {}}
    # gates
    nexp = 1 + sum(len(v) for v in cfg.values())
    okc = all(sorted(S[a]) == sorted(cfg[a]) for a in S) and len(N) == nexp and all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for a in cfg for i in cfg[a]) and N["net_base"].get("rc") == 0
    out["gates"]["G_COMPLETE"] = {"native": {a: len(S[a]) for a in S}, "net": len(N), "net_expected": nexp, "pass": okc}
    nb = [(a, k) for a in S for k in S[a] if not k.endswith("_base")]
    v2 = [float(S[a][k]["v2_max_rel"]) for a, k in nb]
    out["gates"]["G_V2"] = {"max": max(v2), "pass": max(v2) <= 1e-6 and all(int(S[a][k]["v2_n"]) > 0 for a, k in nb)
                            and all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for a in S for r in S[a].values())}
    sh = {}
    for l in open(os.path.join(run, "out", "tables_sha256.log")):
        h, p = l.split(); sh[os.path.basename(p)[0]] = h
    tn = {g: tab(os.path.join(d90, f"hadrons_090_{g}.dat")) for g in ("P83", "H73")}
    sc = {}
    for a, g in (("e", "P83"), ("f", "H73")):
        t = tab(os.path.join(run, "tables", f"{a}.dat"))
        sc[a] = max(abs(r[i] / (F * q[i]) - 1) for r, q in zip(t, tn[g]) for i in range(1, 6)) if len(t) == len(tn[g]) and all(r[0] == q[0] for r, q in zip(t, tn[g])) else 1.0
    out["gates"]["G_TABLES"] = {"sha_ok": {a: sh.get(a) == SHA[a] for a in SHA}, "scale_max_rel": sc,
                                "pass": all(sh.get(a) == SHA[a] for a in SHA) and all(v <= 1e-12 for v in sc.values())}
    drv = {"code": float(S["k"]["k22_1720"]["Y"]) == float(s90["p"]["p22_1720"]["Y"]),
           "net": N["net_k22_1720"]["YP_BBN"] == n90["net_p22_1720"]["YP_BBN"], "net_base": N["net_base"]["YP_BBN"] == n90["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    vb = {f"{a}{j}": abs(float(S[a][f"{a}{j}_base"]["Y"]) - float(s90["p" if ARMS[a][0] == "P83" else "h"][f"{'p' if ARMS[a][0] == 'P83' else 'h'}{j}_base"]["Y"])) for a in ARMS for j in MASSES}
    out["gates"]["G_BASE"] = {"absdiff": vb, "pass": all(x <= 5e-4 for x in vb.values())}
    # nominal on window nodes
    wmax = 0.0; nom = {}
    for g, a in (("P83", "a"), ("H73", "b")):
        for j in MASSES:
            s = A["series"][f"{g}_{j}"]
            win = sorted(float(S[a][i]["log10beta"]) for i in cfg[a] if i.startswith(f"{a}{j}_") and not i.endswith("_base"))
            idx = [s["lb"].index(x) for x in win]
            nom[(g, j)] = {"lb": win, "code": [s["Y_code"][i] for i in idx], "net": [s["Y_net"][i] for i in idx]}
            for m in MODELS:
                for Y in TARGETS:
                    r, _ = cross(win, nom[(g, j)][m], Y)
                    r90 = A["roots"][f"{g}_{j}|{m}|{Y}"]["lb"]
                    wmax = max(wmax, abs(r - r90) if r is not None else 1.0)
                    out["nominal"][f"{g}_{j}|{m}|{Y}"] = {"lb": r90, "noise_dex": A["roots"][f"{g}_{j}|{m}|{Y}"]["noise_dex"]}
    out["gates"]["G_WINDOW"] = {"max_abs_diff": wmax, "pass": wmax <= 1e-12}
    gates_ok = all(g["pass"] for g in out["gates"].values())
    # arm series, roots, node level
    nbr = 0
    for a, (g, X) in ARMS.items():
        for j in MASSES:
            ids = sorted([i for i in cfg[a] if i.startswith(f"{a}{j}_") and not i.endswith("_base")], key=lambda i: float(S[a][i]["log10beta"]))
            s = {"lb": [float(S[a][i]["log10beta"]) for i in ids], "code": [float(S[a][i]["Y"]) for i in ids], "net": [N["net_" + i]["YP_BBN"] for i in ids]}
            out["series"][f"{a}_{j}"] = s
            for m in MODELS:
                dY = [y - y0 for y, y0 in zip(s[m], nom[(g, j)][m])]
                out["node_level"][f"{a}_{j}|{m}"] = {"max_abs_dY": max(abs(x) for x in dY), "rms_dY": math.sqrt(sum(x * x for x in dY) / len(dY)), "n": len(dY)}
                for Y in TARGETS:
                    r, sl = cross(s["lb"], s[m], Y); nbr += r is None
                    r0 = out["nominal"][f"{g}_{j}|{m}|{Y}"]["lb"]
                    out["roots"][f"{a}_{j}|{m}|{Y}"] = {"lb": r, "slope": sl, "droot": (r - r0) if r is not None else None}
    for X, (p, h) in REAL.items():
        for j in MASSES:
            for m in MODELS:
                for Y in TARGETS:
                    rp = out["roots"][f"{p}_{j}|{m}|{Y}"]["lb"]; rh = out["roots"][f"{h}_{j}|{m}|{Y}"]["lb"]
                    d0 = A["estimands"][f"{j}|{m}|{Y}"]["dmod"]
                    dm = (rh - rp) if None not in (rp, rh) else None
                    out["cells"][f"{X}|{j}|{m}|{Y}"] = {"dmod": dm, "dmod_nom": d0, "ddmod": (dm - d0) if dm is not None else None}
    eps = []
    for a in ("e", "f"):
        g = ARMS[a][0]
        for j in MASSES:
            for m in MODELS:
                for Y in TARGETS:
                    dr = out["roots"][f"{a}_{j}|{m}|{Y}"]["droot"]
                    if dr is None:
                        continue
                    e = dr + math.log10(F); nd = out["nominal"][f"{g}_{j}|{m}|{Y}"]["noise_dex"]
                    out["jitter"][f"{a}_{j}|{m}|{Y}"] = {"eps": e, "noise_dex": nd, "ratio": abs(e) / nd}
                    eps.append(abs(e) / nd)
    if not gates_ok:
        out["labels"] = {"status": "GATE_FAIL_NO_LABEL"}
    elif nbr:
        out["labels"] = {"status": "NOT_BRACKETED", "n_unbracketed": nbr}
    else:
        LM = {}; allin = True
        for X in REAL:
            dm = [c["dmod"] for k, c in out["cells"].items() if k.startswith(X + "|")]
            LM[X] = {"LM": label(dm), "min": min(dm), "max": max(dm)}
            allin &= all(0.10 <= x < 0.27 for x in dm)
        allI = all(v["LM"] == "MOD_INTERMEDIATE" for v in LM.values())
        out["labels"] = {"LM": LM, "status": "LM_STABLE_IN_3_REALIZATIONS" if (allI and allin) else ("LM_STABLE_CELLWISE_EXCURSIONS" if allI else "LM_FLIPS")}
        ddR = [c["ddmod"] for k, c in out["cells"].items() if not k.startswith("J|")]
        ddJ = [c["ddmod"] for k, c in out["cells"].items() if k.startswith("J|")]
        out["predictions"] = {"Pr1_LM_intermediate_all": allI, "Pr2_max_abs_ddmod_R_le_0.04": [max(abs(x) for x in ddR) <= 0.04, max(abs(x) for x in ddR)],
                              "Pr3_jitter_median_le_1_max_le_3": [statistics.median(eps) <= 1 and max(eps) <= 3, statistics.median(eps), max(eps)]}
        out["descriptive"] = {"rms_ddmod_R": math.sqrt(sum(x * x for x in ddR) / len(ddR)), "rms_ddmod_J": math.sqrt(sum(x * x for x in ddJ) / len(ddJ)),
                              "max_abs_ddmod_J": max(abs(x) for x in ddJ), "max_abs_droot_R": max(abs(r["droot"]) for k, r in out["roots"].items() if k[0] in "abcd"),
                              "max_abs_eps_J": max(abs(v["eps"]) for v in out["jitter"].values())}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"]))
    print(json.dumps(out["predictions"])); print(json.dumps(out.get("descriptive", {})))


if __name__ == "__main__":
    main(*sys.argv[1:5])
