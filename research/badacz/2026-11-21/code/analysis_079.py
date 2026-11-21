"""PREREG_079 analysis (frozen before any measurement run).

Usage: python3 -I analysis_079.py <dump_dir> <net_out_dir> <t2_data_dir(2026-11-16/data)> <review078_analysis.json> <out.json>
Definitions (PREREG_079 sec. 1-5):
  dY_code(case,node) = Y_native - Y0_code(j) ;  dY_net = Y_net(rates of that native run) - Y0_net
  rho = dY_net / dY_code
  D_code(j): lb where dY_code(E5) = d0 minus lb where dY_code(orig) = d0, d0 = 0.251 - Y0_code(j)
  D_net(j) : lb where dY_net(E5) = d*  minus lb_orig_root_code(j), d* = dY_net(orig) interpolated at lb_orig_root_code
  (linear interpolation in log10 beta between the bracketing nodes of the 9-node grid; exactly one bracket required)
"""
import csv, json, math, os, sys

Q_MEV = 1.29333236          # m_n - m_p [MeV] (PDG); only used in the V2 consistency check
TAU_N = 878.4
T2_D = {22: 0.2722992609128987, 62: 0.2981235851866195}   # REVIEW_071 / analysis069.json (OLS7)


def rd(path):
    return [r for r in csv.DictReader(l for l in open(path) if not l.startswith("#"))]


def crossing(xs, ys, level):
    br = [i for i in range(len(xs) - 1) if (ys[i] - level) * (ys[i + 1] - level) <= 0 and ys[i] != ys[i + 1]]
    if len(br) != 1:
        return None, len(br)
    i = br[0]
    return xs[i] + (level - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i]), 1


def interp(xs, ys, x):
    for i in range(len(xs) - 1):
        if xs[i] <= x <= xs[i + 1]:
            return ys[i] + (x - xs[i]) * (ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i])
    return None


def v2_check(rates_csv):
    rows = rd(rates_csv)
    T = [float(r["T_MeV"]) for r in rows]; t = [float(r["t_s"]) for r in rows]; X = [float(r["X"]) for r in rows]
    p = [float(r["r_p2n"]) for r in rows]; n = [float(r["r_n2p"]) for r in rows]; al = [r["n_PBH_alive"] == "1" for r in rows]
    errs = []
    for i in range(1, len(rows) - 1):
        if not al[i] or T[i] > 20.0:
            continue
        x = Q_MEV / T[i]
        gam = (255.0 / TAU_N) * (12 + 6 * x + x * x) / x ** 5
        sm = -gam * (X[i] - (1 - X[i]) * math.exp(-x)) - X[i] / TAU_N
        had = (1 - X[i]) * p[i] - X[i] * n[i]
        if abs(had) <= abs(sm):
            continue
        fd = (X[i + 1] - X[i - 1]) / (t[i + 1] - t[i - 1])
        rhs = sm + had
        if rhs != 0:
            errs.append(abs(fd / rhs - 1))
    if len(errs) < 20:
        return {"status": "NOT_APPLICABLE", "n": len(errs)}
    errs.sort()
    med = errs[len(errs) // 2]
    return {"status": "PASS" if med <= 0.02 else "FAIL", "n": len(errs), "median_rel_err": med}


def conv_diag(rates_csv, G):
    """Descriptive: integral of G(T) * s(t) dt with REVIEW_078 G table (log-T linear interpolation, 0 outside)."""
    rows = rd(rates_csv)
    Ts = sorted(G)  # ascending T
    def g(T):
        if T < Ts[0] or T > Ts[-1]:
            return 0.0
        lt = math.log(T)
        for a, b in zip(Ts, Ts[1:]):
            if a <= T <= b:
                w = (lt - math.log(a)) / (math.log(b) - math.log(a))
                return G[a] + w * (G[b] - G[a])
        return 0.0
    tot = 0.0
    for r0, r1 in zip(rows, rows[1:]):
        s0 = (1 - float(r0["X"])) * float(r0["r_p2n"]) - float(r0["X"]) * float(r0["r_n2p"])
        s1 = (1 - float(r1["X"])) * float(r1["r_p2n"]) - float(r1["X"]) * float(r1["r_n2p"])
        T0, T1 = float(r0["T_MeV"]), float(r1["T_MeV"])
        tot += 0.5 * (g(T0) * s0 + g(T1) * s1) * (float(r1["t_s"]) - float(r0["t_s"]))
    return tot


def main(dump, netout, t2dir, a078, dst):
    summ = {}
    for arm in ("orig", "e5"):
        for r in rd(os.path.join(dump, f"summary_{arm}.csv")):
            summ[r["run_id"]] = r
    net = {}
    for l in open(os.path.join(netout, "net079_raw.jsonl")):
        d = json.loads(l); net[d["run_id"]] = d
    qa = {r["j"]: float(r["Y"]) for r in rd(os.path.join(t2dir, "qa_A.csv")) if r["log10beta"] == "-30.000000" and r["arm"] == "orig"}
    t2 = {}
    for arm in ("orig", "e5"):
        for r in rd(os.path.join(t2dir, f"t2_{arm}_default.csv")):
            t2[(arm, int(r["j"]), round(float(r["log10beta"]), 2))] = float(r["Y"])
    out = {"gates": {}, "cases": {}, "D": {}, "labels": {}, "predictions": {}, "diagnostics": {}}
    # V1
    v1 = []
    for rid, r in summ.items():
        j = int(r["j"]); lb = round(float(r["log10beta"]), 2); y = float(r["Y"])
        ref = qa.get(str(j)) if rid.endswith("_base") else t2.get((r["arm"], j, lb))
        v1.append({"run_id": rid, "Y": y, "ref": ref, "absdiff": None if ref is None else abs(y - ref)})
    out["gates"]["V1_NATIVE_REPRO"] = {"pass": all(x["ref"] is not None and x["absdiff"] <= 1e-12 for x in v1),
                                       "bitwise": sum(1 for x in v1 if x["absdiff"] == 0.0), "n": len(v1), "rows": v1}
    # V3
    y0n = net["net_base"]["YP_BBN"]
    zero = [net[k]["YP_BBN"] for k in ("net_o22_base", "net_o62_base")]
    out["gates"]["V3_NET_ZERO"] = {"Y0_net": y0n, "with_base_rates": zero, "pass": all(abs(z - y0n) <= 1e-10 for z in zero)}
    # cases
    Y0c = {22: float(summ["o22_base"]["Y"]), 62: float(summ["o62_base"]["Y"])}
    for arm, a in (("orig", "o"), ("e5", "e")):
        for j in (22, 62):
            nodes = sorted([rid for rid in summ if rid.startswith(f"{a}{j}_n")])
            lbs = [float(summ[n]["log10beta"]) for n in nodes]
            dyc = [float(summ[n]["Y"]) - Y0c[j] for n in nodes]
            dyn = [net["net_" + n]["YP_BBN"] - y0n for n in nodes]
            out["cases"][f"{arm}_{j}"] = {"nodes": nodes, "lb": lbs, "dY_code": dyc, "dY_net": dyn,
                                         "rho": [b / a_ if a_ else None for a_, b in zip(dyc, dyn)],
                                         "T_last_alive_MeV": [float(summ[n]["T_last_alive_MeV"]) for n in nodes]}
    # V2, V4, V5
    v2 = {n: v2_check(os.path.join(dump, f"rates_{n}.csv")) for n in ("o22_n08", "o62_n08", "e22_n08", "e62_n08")}
    out["gates"]["V2_RATE_CONSISTENCY"] = {"cases": v2, "pass": all(v["status"] != "FAIL" for v in v2.values())}
    v45 = {}
    for v in ("o22_n08", "o62_n08"):
        base = net["net_" + v]["YP_BBN"] - y0n
        v45[v] = {"dY_net": base,
                  "tol_rel": abs((net[f"net_{v}_tol"]["YP_BBN"] - y0n) / base - 1),
                  "stride2_rel": abs((net[f"net_{v}_stride2"]["YP_BBN"] - y0n) / base - 1)}
    out["gates"]["V4_NET_TOL"] = {"cases": v45, "pass": all(x["tol_rel"] <= 0.01 for x in v45.values())}
    out["gates"]["V5_INTERP"] = {"pass": all(x["stride2_rel"] <= 0.01 for x in v45.values())}
    # D
    oor = False
    for j in (22, 62):
        co, ce = out["cases"][f"orig_{j}"], out["cases"][f"e5_{j}"]
        d0 = 0.251 - Y0c[j]
        ro, no = crossing(co["lb"], co["dY_code"], d0); re_, ne = crossing(ce["lb"], ce["dY_code"], d0)
        Dc = (re_ - ro) if (ro is not None and re_ is not None) else None
        dstar = interp(co["lb"], co["dY_net"], ro) if ro is not None else None
        rn, nn = crossing(ce["lb"], ce["dY_net"], dstar) if dstar is not None else (None, 0)
        Dn = (rn - ro) if (rn is not None and ro is not None) else None
        oor |= Dn is None or Dc is None
        out["D"][str(j)] = {"d0_code": d0, "lb_root_orig_code": ro, "lb_root_e5_code": re_, "D_code_9node": Dc,
                            "D_code_T2_OLS7": T2_D[j], "dstar_net": dstar, "lb_e5_at_dstar_net": rn, "D_net": Dn,
                            "D_net_minus_D_code": (Dn - Dc) if (Dn is not None and Dc is not None) else None,
                            "rho_at_orig_root": (dstar / d0) if dstar is not None else None,
                            "n_brackets": [no, ne, nn]}
    gates_ok = all(out["gates"][g]["pass"] for g in ("V1_NATIVE_REPRO", "V3_NET_ZERO", "V2_RATE_CONSISTENCY", "V4_NET_TOL", "V5_INTERP"))
    if not gates_ok:
        lab = "GATE_FAIL_NO_LABEL"
    elif oor:
        lab = "OUT_OF_RANGE"
    elif all(abs(out["D"][str(j)]["D_net_minus_D_code"]) <= 0.02 for j in (22, 62)):
        lab = "SHIFT_TRANSFERS"
    else:
        lab = "SHIFT_MODIFIED"
    out["labels"]["primary"] = lab
    r62 = out["D"]["62"]["rho_at_orig_root"]
    out["predictions"]["P1_rho62_in_0.75_0.95"] = (r62 is not None and 0.75 <= r62 <= 0.95, r62)
    out["predictions"]["P3_absDnet_minus_Dcode_le_0.02_both"] = (lab == "SHIFT_TRANSFERS",
        [out["D"][str(j)]["D_net_minus_D_code"] for j in (22, 62)])
    # descriptive convolution diagnostic with REVIEW_078 G tables
    A = json.load(open(a078))
    Gc = {float(T): e["G_code"] for T, e in A["per_T"].items() if e["G_code"] is not None}
    Gn = {float(T): e["G_net"] for T, e in A["per_T"].items() if e["G_net"] is not None}
    for n in ("o22_n08", "o62_n08", "e22_n08", "e62_n08"):
        f = os.path.join(dump, f"rates_{n}.csv")
        j = int(n[1:3])
        out["diagnostics"][n] = {"conv_G_code": conv_diag(f, Gc), "native_dY_code": float(summ[n]["Y"]) - Y0c[j],
                                 "conv_G_net": conv_diag(f, Gn), "rate_transfer_dY_net": net["net_" + n]["YP_BBN"] - y0n}
    json.dump(out, open(dst, "w"), indent=1, default=str)
    print(json.dumps({k: (v["pass"] if isinstance(v, dict) and "pass" in v else v) for k, v in out["gates"].items()}))
    print(json.dumps(out["D"], default=str)); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"], default=str))


if __name__ == "__main__":
    main(*sys.argv[1:6])
