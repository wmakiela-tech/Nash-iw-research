"""PREREG_083 analysis (frozen before any measurement run).

Usage: python3 -I analysis_083.py <dump_dedup> <net_out> <t2_data_dir(2026-11-16/data)> <cfg_dir> <out.json>
Estimands per mass j in {22,38,62,90} and target Y* in {0.251, 0.2484} (absolute helium, each model its own baseline):
  lb_code_<arm>(Y*) : log10 beta where native Y_C crosses Y*   ; lb_net_<arm>(Y*) : where Y_net (rate transfer) crosses Y*
  D_code(Y*) = lb_code_e5 - lb_code_orig ; D_net(Y*) = lb_net_e5 - lb_net_orig
  T_orig(Y*) = lb_net_orig - lb_code_orig (shift of the Wu-Xu-code threshold when its own conversion history is carried
               by the full network with the full-network baseline); T_e5 likewise.
Crossing: linear interpolation in log10 beta between bracketing nodes of the 0.05-dex grid; exactly one bracket required.
"""
import csv, json, os, sys

MASSES = [22, 38, 62, 90]
TARGETS = [0.251, 0.2484]


def rd(path):
    return [r for r in csv.DictReader(l for l in open(path) if not l.startswith("#"))]


def crossing(xs, ys, level):
    br = [i for i in range(len(xs) - 1) if (ys[i] - level) * (ys[i + 1] - level) <= 0 and ys[i] != ys[i + 1]]
    if len(br) != 1:
        return None, len(br)
    i = br[0]
    return xs[i] + (level - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i]), 1


def main(dump, netout, t2dir, cfgdir, dst):
    summ = {}
    for arm in ("orig", "e5"):
        for r in rd(os.path.join(dump, f"summary_{arm}.csv")):
            summ[r["run_id"]] = r
    net = {}
    for l in open(os.path.join(netout, "net083_raw.jsonl")):
        d = json.loads(l); net[d["run_id"]] = d
    grid = json.load(open(os.path.join(cfgdir, "grid083.json")))
    exp = []
    for arm in ("orig", "e5"):
        for l in open(os.path.join(cfgdir, f"cfg083_{arm}.dat")):
            s = l.strip()
            if s and not s.startswith("#"):
                exp.append(s.split()[0])
    out = {"gates": {}, "series": {}, "estimands": {}, "labels": {}, "predictions": {}}
    # V7 completeness
    vc = [grid["orig_22"]["nearest_root_node"], grid["orig_62"]["nearest_root_node"]]
    exp_net = ["net_base"] + ["net_" + i for i in exp] + [f"net_{v}_{s}" for v in vc for s in ("tol", "stride2")]
    ok7 = sorted(summ) == sorted(exp) and all(i in net and net[i].get("rc") == 0 and "YP_BBN" in net[i] for i in exp_net) and len(net) == len(exp_net)
    out["gates"]["V7_COMPLETENESS"] = {"native": len(summ), "native_expected": len(exp), "net": len(net), "net_expected": len(exp_net), "pass": ok7}
    # V1 native reproduction against owner T2/QA rows where nodes coincide
    qa = {}
    for r in rd(os.path.join(t2dir, "qa_A.csv")):
        qa[(int(r["j"]), round(float(r["log10beta"]), 2))] = float(r["Y"])
    t2 = {}
    for arm in ("orig", "e5"):
        for r in rd(os.path.join(t2dir, f"t2_{arm}_default.csv")):
            t2[(arm, int(r["j"]), round(float(r["log10beta"]), 2))] = float(r["Y"])
    v1 = []
    for rid, r in summ.items():
        key = (int(r["j"]), round(float(r["log10beta"]), 2)); y = float(r["Y"])
        ref = qa.get(key) if r["arm"] == "orig" else None
        if ref is None:
            ref = t2.get((r["arm"],) + key)
        if ref is not None:
            v1.append({"run_id": rid, "absdiff": abs(y - ref)})
    per = {(a, j): sum(1 for x in v1 if x["run_id"].startswith(f"{a[0]}{j}_")) for a in ("orig", "e5") for j in MASSES}
    out["gates"]["V1_NATIVE_REPRO"] = {"n_matched": len(v1), "bitwise": sum(1 for x in v1 if x["absdiff"] == 0.0),
                                       "per_case_matched": {f"{a}_{j}": n for (a, j), n in per.items()},
                                       "pass": len(v1) > 0 and all(x["absdiff"] <= 1e-12 for x in v1) and all(n >= 1 for n in per.values())}
    # V2_EXACT, V6
    v2 = {rid: (float(r["v2_max_rel"]), int(r["v2_n"])) for rid, r in summ.items() if not rid.endswith("_base")}
    out["gates"]["V2_RATE_CONSISTENCY"] = {"max": max(x[0] for x in v2.values()), "pass": all(n > 0 and m <= 1e-6 for m, n in v2.values())}
    out["gates"]["V6_REFINED"] = {"pass": all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for r in summ.values())}
    # V3
    y0n = net["net_base"]["YP_BBN"]
    zr = {j: net[f"net_o{j}_base"]["YP_BBN"] - y0n for j in MASSES}
    out["gates"]["V3_NET_ZERO"] = {"Y0_net": y0n, "dev": zr, "pass": all(abs(z) <= 1e-5 for z in zr.values())}
    # V4, V5
    v45 = {}
    for v in vc:
        base = net["net_" + v]["YP_BBN"] - y0n
        v45[v] = {"dY_net": base, "tol_rel": abs((net[f"net_{v}_tol"]["YP_BBN"] - y0n) / base - 1),
                  "stride2_rel": abs((net[f"net_{v}_stride2"]["YP_BBN"] - y0n) / base - 1)}
    out["gates"]["V4_NET_TOL"] = {"cases": v45, "pass": all(x["tol_rel"] <= 0.01 for x in v45.values())}
    out["gates"]["V5_INTERP"] = {"pass": all(x["stride2_rel"] <= 0.01 for x in v45.values())}
    # series and estimands
    Y0c = {j: float(summ[f"o{j}_base"]["Y"]) for j in MASSES}
    for arm, a in (("orig", "o"), ("e5", "e")):
        for j in MASSES:
            nodes = sorted([rid for rid in summ if rid.startswith(f"{a}{j}_") and not rid.endswith("_base")],
                           key=lambda rid: float(summ[rid]["log10beta"]))
            lb = [float(summ[n]["log10beta"]) for n in nodes]
            yc = [float(summ[n]["Y"]) for n in nodes]
            yn = [net["net_" + n]["YP_BBN"] for n in nodes]
            rho = [(b - y0n) / (c - Y0c[j]) if c != Y0c[j] else None for c, b in zip(yc, yn)]
            out["series"][f"{arm}_{j}"] = {"lb": lb, "Y_code": yc, "Y_net": yn, "rho": rho}
    nb = False
    for j in MASSES:
        e = {}
        for Ys in TARGETS:
            row = {}
            for arm in ("orig", "e5"):
                s = out["series"][f"{arm}_{j}"]
                row[f"lb_code_{arm}"], row[f"nb_code_{arm}"] = crossing(s["lb"], s["Y_code"], Ys)
                row[f"lb_net_{arm}"], row[f"nb_net_{arm}"] = crossing(s["lb"], s["Y_net"], Ys)
            f = lambda a, b: (a - b) if (a is not None and b is not None) else None
            row["D_code"] = f(row["lb_code_e5"], row["lb_code_orig"]); row["D_net"] = f(row["lb_net_e5"], row["lb_net_orig"])
            row["T_orig"] = f(row["lb_net_orig"], row["lb_code_orig"]); row["T_e5"] = f(row["lb_net_e5"], row["lb_code_e5"])
            nb |= any(row[k] is None for k in ("D_code", "D_net", "T_orig", "T_e5"))
            e[str(Ys)] = row
        out["estimands"][str(j)] = e
    gates_ok = all(out["gates"][g]["pass"] for g in out["gates"])
    if not gates_ok:
        L1 = L2 = "GATE_FAIL_NO_LABEL"
    elif nb:
        L1 = L2 = "NOT_BRACKETED"
    else:
        d = [abs(out["estimands"][str(j)]["0.2484"]["D_net"] - out["estimands"][str(j)]["0.251"]["D_net"]) for j in MASSES]
        L1 = "SHIFT_ANCHOR_ROBUST" if all(x <= 0.02 for x in d) else "SHIFT_ANCHOR_DEPENDENT"
        L2 = "TRANSFER_MATERIAL" if any(abs(out["estimands"][str(j)]["0.251"]["T_orig"]) > 0.05 for j in MASSES) else "TRANSFER_SMALL"
    out["labels"] = {"L1_charge_shift_anchor": L1, "L2_threshold_transfer": L2}
    E = out["estimands"]
    g = lambda j, Ys, k: E[str(j)][str(Ys)][k]
    out["predictions"]["P1_Torig_0.251_j22_lt_-0.15"] = (g(22, 0.251, "T_orig") is not None and g(22, 0.251, "T_orig") < -0.15, g(22, 0.251, "T_orig"))
    out["predictions"]["P2_Torig_0.251_j62_in_-0.25_0"] = (g(62, 0.251, "T_orig") is not None and -0.25 <= g(62, 0.251, "T_orig") <= 0.0, g(62, 0.251, "T_orig"))
    out["predictions"]["P3_SHIFT_ANCHOR_ROBUST"] = (L1 == "SHIFT_ANCHOR_ROBUST", L1)
    p4 = [(g(j, 0.2484, "T_orig"), g(j, 0.251, "T_orig")) for j in MASSES]
    out["predictions"]["P4_Torig_LBT_lt_Torig_0.251_all"] = (all(a is not None and b is not None and a < b for a, b in p4), p4)
    json.dump(out, open(dst, "w"), indent=1, default=str)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()}))
    print(json.dumps(out["labels"])); print(json.dumps(out["predictions"], default=str))


if __name__ == "__main__":
    main(*sys.argv[1:6])
