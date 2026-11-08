#!/usr/bin/env python3
"""Badacz (Claude): PREREG_048 analysis (commit b7a2c14). Boundary per config = root of the 7-point linear fit Y_C(log10 beta)
at 0.251; Delta = root(config) - root(base_j); s_eff = (10^-Delta - 1)/(k - 1); W = s_eff / s_num (band_number_shares.json).
Evaluates P0-P4, sum rule, F1-F3 and N1 exactly as preregistered.
Usage: python3 -I wuxu_band_kernel_analysis.py --runs kernel_w1.csv kernel_w2.csv --shares band_number_shares.json
          [--n1 n1_base.csv n1_D10.csv] --out kernel_analysis.json
"""
import argparse, csv, json, math

ap = argparse.ArgumentParser()
ap.add_argument("--runs", nargs="+", required=True); ap.add_argument("--shares", required=True)
ap.add_argument("--n1", nargs="*", default=[]); ap.add_argument("--out", required=True)
a = ap.parse_args()
THR = 0.251
SH = json.load(open(a.shares))


def load(paths):
    rows = []
    for p in paths:
        rows += [r for r in csv.DictReader([l for l in open(p) if not l.startswith("#")])]
    return rows


def fit_root(pts):
    n = len(pts); xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    xm = sum(xs) / n; ym = sum(ys) / n; sxx = sum((x - xm) ** 2 for x in xs)
    c1 = sum((x - xm) * (y - ym) for x, y in zip(xs, ys)) / sxx; c0 = ym - c1 * xm
    res = [y - (c0 + c1 * x) for x, y in zip(xs, ys)]; s2 = sum(r * r for r in res) / (n - 2)
    root = (THR - c0) / c1
    # delta method: root = xm + (THR - ym)/c1 ; var(ym) = s2/n, var(c1) = s2/sxx, independent
    var = (s2 / n) / c1 ** 2 + ((THR - ym) ** 2 / c1 ** 4) * (s2 / sxx)
    return {"root": root, "se": math.sqrt(var), "slope": c1, "sigma_resid": math.sqrt(s2), "n": n}


def analyse(rows):
    cfg = {}
    for r in rows:
        if r["phase"] == "NOBRACKET":
            cfg.setdefault(r["id"], {"meta": r, "fit": [], "nobracket": True}); continue
        c = cfg.setdefault(r["id"], {"meta": r, "fit": [], "nobracket": False})
        if r["phase"] == "fit":
            c["fit"].append((float(r["log10beta"]), float(r["Yc"])))
    out = {}
    for i, c in cfg.items():
        m = c["meta"]
        d = {"j": int(m["j"]), "lo_g": float(m["lo_g"]), "hi_g": float(m["hi_g"]), "k": float(m["k"]), "nobracket": c["nobracket"]}
        if not c["nobracket"] and len(c["fit"]) == 7:
            d.update(fit_root(c["fit"]))
        out[i] = d
    return out


R = analyse(load(a.runs))
bands = {"A2": ("A", 2), "B2": ("B", 2), "C2": ("C", 2), "C10": ("C", 10), "D2": ("D", 2), "D10": ("D", 10), "D0": ("D", 0)}
res = {"configs": R, "derived": {}, "verdicts": {}}
for j in (22, 28, 34, 62):
    base = R.get(f"base_{j}")
    if not base or "root" not in base:
        continue
    dj = {}
    for name, (b, k) in bands.items():
        c = R.get(f"{name}_{j}")
        if not c or "root" not in c:
            dj[name] = {"missing_or_nobracket": True}; continue
        D = c["root"] - base["root"]; seD = math.hypot(c["se"], base["se"])
        s = (10 ** (-D) - 1) / (k - 1); ses = math.log(10) * 10 ** (-D) / abs(k - 1) * seD
        sn = SH["j"][str(j)]["bands"][b]["s_num_total"]
        dj[name] = {"Delta": D, "se_Delta": seD, "s_eff": s, "se_s_eff": ses, "s_num": sn, "W": s / sn, "se_W": ses / sn,
                    "pred_num_Delta": SH["j"][str(j)]["bands"][b]["pred_num_Delta"][str(k)]}
    res["derived"][str(j)] = dj

V = res["verdicts"]; Dv = res["derived"]
# DEVIATION (RUNLOG 8 XI 09:47, decided before any D-band result): C x10 and D x10 were computationally infeasible at the
# authors' default solver (first C10_22 point 1286 s; C10_28 process OOM-killed at 3.3 GB). Where D10 / C10 are missing, the
# D-band estimate is the inverse-variance combination of the preregistered D x2 and D x0 configs ("Dc"), P2 uses C x2 / Dc,
# and F3 compares D x0 with D x2.
res["deviation"] = "C10/D10 infeasible (time/OOM); D estimated from D2+D0 (inverse-variance), P2 from C2/Dc, F3 from D0 vs D2"
for j in Dv:
    if "W" not in Dv[j].get("D10", {}) and "s_eff" in Dv[j].get("D2", {}) and "s_eff" in Dv[j].get("D0", {}):
        x = [Dv[j]["D2"], Dv[j]["D0"]]; w = [1 / v["se_s_eff"] ** 2 for v in x]
        s = sum(wi * v["s_eff"] for wi, v in zip(w, x)) / sum(w); se = 1 / math.sqrt(sum(w)); sn = x[0]["s_num"]
        Dv[j]["Dc"] = {"s_eff": s, "se_s_eff": se, "s_num": sn, "W": s / sn, "se_W": se / sn, "from": "D2+D0"}
        Dv[j]["D10"] = Dv[j]["Dc"]
    if "W" not in Dv[j].get("C10", {}) and "W" in Dv[j].get("C2", {}):
        Dv[j]["C10"] = dict(Dv[j]["C2"], **{"from": "C2 (C10 infeasible)"})
p0 = {"22": (-0.015, 0.005), "28": (-0.015, 0.005), "34": (-0.128, -0.068), "62": (-0.304, -0.244)}
V["P0_A2_consistency_with_zero_variant"] = {j: {"Delta": Dv[j]["A2"].get("Delta"), "window": w,
                                              "pass": (w[0] <= Dv[j]["A2"]["Delta"] <= w[1]) if "Delta" in Dv[j]["A2"] else None,
                                              "deviation_gt_0p03": (min(abs(Dv[j]["A2"]["Delta"] - w[0]), abs(Dv[j]["A2"]["Delta"] - w[1])) > 0.03
                                                                    and not (w[0] <= Dv[j]["A2"]["Delta"] <= w[1])) if "Delta" in Dv[j]["A2"] else None}
                                          for j, w in p0.items() if j in Dv}
V["sum_rule_k2"] = {}
for j in Dv:
    try:
        lhs = Dv[j]["B2"]["s_eff"] + Dv[j]["C2"]["s_eff"] + Dv[j]["D2"]["s_eff"]; rhs = 1 - Dv[j]["A2"]["s_eff"]
        V["sum_rule_k2"][j] = {"sum_BCD": lhs, "one_minus_A": rhs, "diff": lhs - rhs, "pass_0p1": abs(lhs - rhs) <= 0.1}
    except KeyError:
        V["sum_rule_k2"][j] = None
V["P1_W_D10_ge_1p5"] = {j: (Dv[j]["D10"]["W"], Dv[j]["D10"]["se_W"], Dv[j]["D10"]["W"] >= 1.5) for j in ("22", "28") if j in Dv and "W" in Dv[j]["D10"]}
V["P2_W_C10_over_W_D10_in_0p8_1p25"] = {j: (Dv[j]["C10"]["W"] / Dv[j]["D10"]["W"], 0.8 <= Dv[j]["C10"]["W"] / Dv[j]["D10"]["W"] <= 1.25)
                                        for j in ("22", "28") if j in Dv and "W" in Dv[j]["C10"] and "W" in Dv[j]["D10"]}
V["P3_control_j62_W_A2_B2_in_0p7_1p4"] = {b: (Dv["62"][b]["W"], 0.7 <= Dv["62"][b]["W"] <= 1.4) for b in ("A2", "B2") if "62" in Dv and "W" in Dv["62"][b]}
V["P4_s_eff_D10_in_0p02_0p10"] = {j: (Dv[j]["D10"]["s_eff"], 0.02 <= Dv[j]["D10"]["s_eff"] <= 0.10) for j in ("22", "28") if j in Dv and "s_eff" in Dv[j]["D10"]}
V["F1_W_D10_below_1_by_2sigma"] = {j: Dv[j]["D10"]["W"] + 2 * Dv[j]["D10"]["se_W"] < 1 for j in ("22", "28") if j in Dv and "W" in Dv[j]["D10"]}
V["F3_D_linearity_k0_vs_k10"] = {}
for j in Dv:
    hi = "D2" if Dv[j]["D10"].get("from") == "D2+D0" else "D10"      # deviation: compare D0 with D2 when D10 is missing
    if "s_eff" in Dv[j]["D0"] and "s_eff" in Dv[j][hi]:
        d = abs(Dv[j]["D0"]["s_eff"] - Dv[j][hi]["s_eff"]); sig = math.hypot(Dv[j]["D0"]["se_s_eff"], Dv[j][hi]["se_s_eff"])
        V["F3_D_linearity_k0_vs_k10"][j] = {"compared": "D0 vs " + hi, "abs_diff": d, "sigma": sig,
                                            "threshold": max(0.5 * Dv[j][hi]["s_eff"], 3 * sig),
                                            "falsified": d > max(0.5 * Dv[j][hi]["s_eff"], 3 * sig)}
if a.n1:
    N = analyse(load(a.n1))
    nb, nd = N.get("base_22"), N.get("D10_22") or N.get("D2_22")   # deviation: N1 on D2 when D10 is infeasible
    if nb and nd and "root" in nb and "root" in nd and "22" in Dv:
        D1 = nd["root"] - nb["root"]; key = "D10" if "D10_22" in N else "D2"
        D0d = Dv["22"][key]["Delta"]
        res["N1"] = {"config": key, "Delta_tol1e-4": D1, "Delta_default": D0d, "change": D1 - D0d,
                     "flag_tolerance_limited": abs(D1 - D0d) > 0.02, "configs": N}
json.dump(res, open(a.out, "w"), indent=1, sort_keys=True)
for j in Dv:
    print(j, {n: (round(v["Delta"], 4), round(v["W"], 2)) if "W" in v else "NA" for n, v in Dv[j].items()})
for k, v in V.items():
    print(k, v)
if "N1" in res:
    print("N1", {k: v for k, v in res["N1"].items() if k != "configs"})
