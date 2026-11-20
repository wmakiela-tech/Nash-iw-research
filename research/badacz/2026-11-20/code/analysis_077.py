"""PREREG_077 analysis (frozen before any measurement run).

Usage: python3 -I analysis_077.py <out_dir> <qa_A.csv> <analysis077.json>
Inputs in <out_dir>: net_raw.jsonl, code_default.csv, code_1e-4.csv.
Definitions (PREREG_077 sec. 3):
  NET : G_net(T)  = (Y+ - Y-) / (A * (Yn_before + Yp_before))   [Y = PRyMordial YP_BBN]
  CODE: G_code(T) = (Y+ - Y-) / A                                 [Y = authors' Y_C = 2X/(1-X) at T_nuc]
  R(T) = G_code / G_net on the core set, where |G_net| >= 0.05 and the T passes V4/V5.
"""
import csv, json, statistics, sys

T_GRID = [3.0, 2.0, 1.5, 1.2, 0.8, 0.6, 0.45, 0.35, 0.25, 0.18, 0.13, 0.105, 0.095, 0.088, 0.082, 0.075, 0.068, 0.06]
CORE = [2.0, 1.5, 1.2, 0.8, 0.6, 0.45, 0.35, 0.25, 0.18, 0.13, 0.105]
QA_J22_BETA30 = None  # read from qa_A.csv


def load_net(path):
    d = {}
    for line in open(path):
        r = json.loads(line)
        d[r["run_id"]] = r
    return d


def load_code(path):
    rows = [r for r in csv.DictReader(l for l in open(path) if not l.startswith("#"))]
    return {r["run_id"]: r for r in rows}


def g_net(net, T, A, prefix="net"):
    tag = f"{prefix}_T{T}_A{A}" if prefix == "net" else f"{prefix}_T{T}"
    p, m = net.get(f"{tag}_s+1"), net.get(f"{tag}_s-1")
    if not p or not m or "YP_BBN" not in p or "YP_BBN" not in m or not p.get("kick_applied") or not m.get("kick_applied"):
        return None, {"missing_or_not_applied": True}
    lp, lm = p["kick_log"], m["kick_log"]
    S = lp["Yn_before"] + lp["Yp_before"]
    same_pre = abs(lp["Yn_before"] - lm["Yn_before"]) <= 1e-12 and abs(lp["Yp_before"] - lm["Yp_before"]) <= 1e-12
    G = (p["YP_BBN"] - m["YP_BBN"]) / (A * S)
    return G, {"Yp_plus": p["YP_BBN"], "Yp_minus": m["YP_BBN"], "Yn_before": lp["Yn_before"], "Yp_before": lp["Yp_before"],
               "X_before": lp["Yn_before"] / S, "t_k": lp["t_k"], "same_pre_state": same_pre}


def g_code(code, T, A, prefix="code"):
    tag = f"{prefix}_T{T}_A{A}" if prefix == "code" else f"{prefix}_T{T}"
    p, m = code.get(f"{tag}_s+1"), code.get(f"{tag}_s-1")
    if not p or not m:
        return None, {"missing": True}
    nk_ok = int(p["n_kicks"]) == 1 and int(m["n_kicks"]) == 1
    G = (float(p["Y"]) - float(m["Y"])) / A
    same_pre = nk_ok and abs(float(p["X_before"]) - float(m["X_before"])) <= 1e-12
    return G, {"Y_plus": float(p["Y"]), "Y_minus": float(m["Y"]), "n_kicks_ok": nk_ok, "X_before": float(p["X_before"]) if nk_ok else None,
               "eta_kick": float(p["eta_kick"]) if nk_ok else None, "same_pre_state": same_pre}


def ratio_ok(a, b, tol):
    return a is not None and b is not None and b != 0 and abs(a / b - 1) <= tol


def main(out, qa_path, dst):
    net = load_net(f"{out}/net_raw.jsonl")
    cd = load_code(f"{out}/code_default.csv")
    ct = load_code(f"{out}/code_1e-4.csv")
    qa = [r for r in csv.DictReader(l for l in open(qa_path) if not l.startswith("#"))
          if r["j"] == "22" and r["log10beta"] == "-30.000000"]
    qa_y = float(qa[0]["Y"])
    res = {"gates": {}, "per_T": {}, "labels": {}, "predictions": {}}
    y0n = net["net_base"]["YP_BBN"]; y0c = float(cd["code_base"]["Y"])
    res["gates"]["V0_NET_BASELINE"] = {"Y0_net": y0n, "pass": 0.2460 <= y0n <= 0.2480}
    res["gates"]["V3_CODE_ZERO"] = {"Y0_code": y0c, "qa_native": qa_y, "abs_diff": abs(y0c - qa_y), "pass": abs(y0c - qa_y) <= 1e-15}
    res["baseline_offset_code_minus_net"] = y0c - y0n
    v2_all = True
    for T in T_GRID:
        e = {}
        Gn2, dn2 = g_net(net, T, 2e-3); Gn1, _ = g_net(net, T, 1e-3)
        Gc2, dc2 = g_code(cd, T, 2e-3); Gc1, _ = g_code(cd, T, 1e-3)
        e.update({"G_net": Gn2, "G_net_A1e-3": Gn1, "net_detail": dn2, "G_code": Gc2, "G_code_A1e-3": Gc1, "code_detail": dc2})
        v2 = (Gn2 is not None and Gc2 is not None and dn2.get("same_pre_state") and dc2.get("same_pre_state") and dc2.get("n_kicks_ok"))
        v2_all &= bool(v2)
        e["V2_KICK_OK"] = bool(v2)
        e["V4_LIN_NET"] = (abs(Gn2 or 0) < 0.05) or ratio_ok(Gn1, Gn2, 0.03)
        e["V4_LIN_CODE"] = (abs(Gc2 or 0) < 0.05) or ratio_ok(Gc1, Gc2, 0.03)
        Gct, _ = g_code(ct, T, 2e-3, prefix="code_tol")
        e["G_code_tol1e-4"] = Gct
        e["V5_TOL_CODE"] = (abs(Gc2 or 0) < 0.05) or ratio_ok(Gct, Gc2, 0.03)
        if T in (1.5, 0.45, 0.18, 0.105):
            Gnt, _ = g_net(net, T, 2e-3, prefix="net_tol")
            e["G_net_tol1e-2"] = Gnt
            e["V5_TOL_NET"] = (abs(Gn2 or 0) < 0.05) or ratio_ok(Gnt, Gn2, 0.01)
        if T in (0.45, 0.13):
            Gnl, _ = g_net(net, T, 2e-3, prefix="net_large")
            e["G_net_large"] = Gnl
            e["LARGE_NET_DIAG"] = ratio_ok(Gnl, Gn2, 0.01)
        e["R"] = (Gc2 / Gn2) if (Gn2 and Gc2 is not None and abs(Gn2) >= 0.05) else None
        res["per_T"][str(T)] = e
    res["gates"]["V2_KICK_APPLIED_ALL"] = v2_all
    tol_fail_net = [T for T in ("1.5", "0.45", "0.18", "0.105") if not res["per_T"][T].get("V5_TOL_NET", True)]
    res["gates"]["V5_TOL_NET_ALL"] = {"failed_T": tol_fail_net, "pass": not tol_fail_net}
    core = []
    for T in CORE:
        e = res["per_T"][str(T)]
        ok = e["V2_KICK_OK"] and e["V4_LIN_NET"] and e["V4_LIN_CODE"] and e["V5_TOL_CODE"] and e.get("V5_TOL_NET", True) and e["R"] is not None
        e["IN_CORE_SET"] = bool(ok)
        if ok:
            core.append((T, e["R"]))
    Rs = [r for _, r in core]
    if not (res["gates"]["V0_NET_BASELINE"]["pass"] and res["gates"]["V3_CODE_ZERO"]["pass"]):
        label = "GATE_FAIL_NO_LABEL"
    elif len(Rs) < 5:
        label = "INSUFFICIENT"
    elif all(abs(r - 1) <= 0.05 for r in Rs):
        label = "GAIN_MATCH"
    elif max(Rs) / min(Rs) <= 1.05:
        label = "GAIN_CONSTANT_OFFSET"
    else:
        label = "GAIN_T_DEPENDENT"
    res["labels"] = {"primary": label, "n_core": len(Rs), "R_core": core,
                     "r_median": statistics.median(Rs) if Rs else None,
                     "R_min": min(Rs) if Rs else None, "R_max": max(Rs) if Rs else None}
    pt = res["per_T"]
    p1 = [pt[str(T)]["R"] for T in (0.25, 0.18, 0.13)]
    res["predictions"]["P1_R_late_in_1.10_1.45"] = (all(r is not None and 1.10 <= r <= 1.45 for r in p1), p1)
    gn3, gn25, gc3, gc25 = pt["3.0"]["G_net"], pt["0.25"]["G_net"], pt["3.0"]["G_code"], pt["0.25"]["G_code"]
    res["predictions"]["P2_early_erased"] = (None not in (gn3, gn25, gc3, gc25) and abs(gn3) < 0.1 * abs(gn25) and abs(gc3) < 0.1 * abs(gc25),
                                             [gn3, gn25, gc3, gc25])
    gc_late = [pt[str(T)]["G_code"] for T in (0.075, 0.068, 0.06)]
    res["predictions"]["P3_code_zero_below_Tnuc_net_positive"] = (
        all(g is not None and abs(g) < 1e-3 for g in gc_late) and (pt["0.075"]["G_net"] or 0) > 0.5, gc_late + [pt["0.075"]["G_net"]])
    json.dump(res, open(dst, "w"), indent=1, default=str)
    print(json.dumps(res["gates"], default=str)); print(json.dumps(res["labels"], default=str)); print(json.dumps(res["predictions"], default=str))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
