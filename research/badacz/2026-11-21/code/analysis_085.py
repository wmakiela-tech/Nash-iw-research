"""PREREG_085 / GAP-005 analysis (frozen before any HERWIG table or run exists).

Usage: python3 -I analysis_085.py <data_083_dir> <run_dir> <cfg_dir> <authors_table> <out.json>
  data_083_dir : research/badacz/2026-11-21/data (summary_{orig,e5}_083.csv, net083_raw.jsonl) -> PYTHIA (PY) cells
  run_dir      : /home/claude/run085 (tables/, dump_her_dedup/, out/) -> HERWIG rule R2 (HER) cells + gates
2x2 factorial per mass j in {22, 62}: generator g in {PY, HER} x arm a in {orig, e5}; model m in {code, net};
target Y* in {0.251, 0.2484}. lb[g][m][a](Y*) = log10 beta where Y crosses Y* (linear interpolation between the
bracketing nodes of the 0.05-dex grid; exactly one bracket required), each model against its own baseline.
  Delta_gen[m][a] = lb[HER][m][a] - lb[PY][m][a]                       (generator systematic)
  D[g][m]         = lb[g][m][e5] - lb[g][m][orig]                       (E5 / T2 shift under generator g)
  I[m]            = D[HER][m] - D[PY][m]                               (generator x E5 interaction)
Interpolation-noise estimate: every crossing is recomputed with a quadratic through the bracket and the next node
(next lower if the bracket is last); N_I = max |I_quad - I_lin|, N_gen = max |Delta_quad - Delta_lin| (over j, m, Y*).
Labels (only if all gates PASS and all 32 crossings bracketed; primary at Y* = 0.251, LBT reported with same rules):
  LG: max over (j, m, a) |Delta_gen| < 0.10 -> GEN_SMALL ; >= 0.27 -> GEN_COMPARABLE ; else GEN_INTERMEDIATE
  LI: if 0.02 < 5 N_I -> I_UNRESOLVED ; elif max over (j, m) |I| <= 0.02 -> ADDITIVE ; else INTERACTING
  LS: all 8 Delta_gen > 0 -> HER_WEAKER ; all < 0 -> HER_STRONGER ; else MIXED
"""
import csv, json, os, sys
import numpy as np

MASSES = [22, 62]
TARGETS = [0.251, 0.2484]
SPECIES = ["pipm", "Kpm", "K0L", "proton", "neutron"]


def rd(p):
    return {r["run_id"]: r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))}


def rdj(p):
    out = {}
    for l in open(p):
        d = json.loads(l); out[d["run_id"]] = d
    return out


def bracket(xs, ys, level):
    br = [i for i in range(len(xs) - 1) if (ys[i] - level) * (ys[i + 1] - level) <= 0 and ys[i] != ys[i + 1]]
    return br[0] if len(br) == 1 else None, len(br)


def cross_lin(xs, ys, level):
    i, n = bracket(xs, ys, level)
    if i is None:
        return None, n
    return xs[i] + (level - ys[i]) * (xs[i + 1] - xs[i]) / (ys[i + 1] - ys[i]), 1


def cross_quad(xs, ys, level):
    i, n = bracket(xs, ys, level)
    if i is None:
        return None
    k = i + 2 if i + 2 < len(xs) else i - 1
    if k < 0:
        return None
    idx = sorted([i, i + 1, k])
    c = np.polyfit([xs[t] for t in idx], [ys[t] - level for t in idx], 2)
    roots = [r.real for r in np.roots(c) if abs(r.imag) < 1e-12 and xs[i] - 1e-12 <= r.real <= xs[i + 1] + 1e-12]
    return roots[0] if len(roots) == 1 else None


def series(summ, net, prefix):
    nodes = sorted([r for r in summ if r.startswith(prefix) and not r.endswith("_base")], key=lambda r: float(summ[r]["log10beta"]))
    lb = [float(summ[n]["log10beta"]) for n in nodes]
    yc = [float(summ[n]["Y"]) for n in nodes]
    yn = [net["net_" + n]["YP_BBN"] for n in nodes]
    return {"nodes": nodes, "lb": lb, "Y_code": yc, "Y_net": yn}


def main(d83, run, cfgdir, authors_table, dst):
    out = {"gates": {}, "series": {}, "roots": {}, "estimands": {}, "labels": {}, "predictions": {}, "descriptive": {}}
    # --- inputs
    s83 = {}; [s83.update(rd(os.path.join(d83, f"summary_{a}_083.csv"))) for a in ("orig", "e5")]
    n83 = rdj(os.path.join(d83, "net083_raw.jsonl"))
    dh = os.path.join(run, "dump_her_dedup")
    sh = {}; [sh.update(rd(os.path.join(dh, f"summary_{a}.csv"))) for a in ("orig", "e5")]
    nh = rdj(os.path.join(run, "out", "net085_raw.jsonl"))
    tg = json.load(open(os.path.join(run, "out", "table_gates085.json")))
    ij = json.load(open(os.path.join(run, "out", "inj085.json")))
    grid = json.load(open(os.path.join(cfgdir, "grid085.json")))
    exp = []
    for a in ("orig", "e5"):
        for l in open(os.path.join(cfgdir, f"cfg085_her_{a}.dat")):
            s = l.strip()
            if s and not s.startswith("#"):
                exp.append(s.split()[0])
    # --- gates
    A = np.loadtxt(authors_table, skiprows=1); G0 = np.loadtxt(os.path.join(run, "tables", "G0.dat"), skiprows=1)
    g0 = float(np.max(np.abs(G0[:, 1:] / A[:, 1:] - 1)))
    out["gates"]["G0_PYTHIA_TABLE_REPRO"] = {"max_rel": g0, "mass_col_equal": bool(np.array_equal(A[:, 0], G0[:, 0])), "pass": g0 <= 1e-6 and bool(np.array_equal(A[:, 0], G0[:, 0]))}
    out["gates"]["G1_SPLIT_ADDITIVITY"] = tg["G1_SPLIT_ADDITIVITY"]
    out["gates"]["G2_RULE_IRRELEVANCE"] = tg["G2_RULE_IRRELEVANCE"]
    out["gates"]["V_INJ_NEG"] = ij["V_INJ_NEG"]
    out["gates"]["V_INJ_POS"] = dict(ij["V_INJ_POS"], **{"pass": ij["V_INJ_POS"]["pass_"]})
    vb = {j: abs(float(sh[f"ho{j}_base"]["Y"]) - float(s83[f"o{j}_base"]["Y"])) for j in MASSES}
    out["gates"]["V_BASE"] = {"absdiff": vb, "pass": all(v <= 1e-12 for v in vb.values())}
    exp_net = ["net_base"] + ["net_" + i for i in exp] + [f"net_{v}_{s}" for v in grid["V45_cases"] for s in ("tol", "stride2")]
    ok7 = sorted(sh) == sorted(exp) and len(nh) == len(exp_net) and all(i in nh and nh[i].get("rc") == 0 and "YP_BBN" in nh[i] for i in exp_net)
    out["gates"]["V7_COMPLETENESS"] = {"native": len(sh), "native_expected": len(exp), "net": len(nh), "net_expected": len(exp_net), "pass": ok7}
    v2 = [float(r["v2_max_rel"]) for rid, r in sh.items() if not rid.endswith("_base")]
    out["gates"]["V2_RATE_CONSISTENCY"] = {"max": max(v2), "pass": all(int(r["v2_n"]) > 0 for rid, r in sh.items() if not rid.endswith("_base")) and max(v2) <= 1e-6}
    out["gates"]["V6_REFINED"] = {"pass": all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for r in sh.values())}
    y0n = nh["net_base"]["YP_BBN"]; y0n83 = n83["net_base"]["YP_BBN"]
    zr = {j: nh[f"net_ho{j}_base"]["YP_BBN"] - y0n for j in MASSES}
    out["gates"]["V3_NET_ZERO"] = {"Y0_net": y0n, "Y0_net_083": y0n83, "dev": zr,
                                   "pass": all(abs(z) <= 1e-5 for z in zr.values()) and abs(y0n - y0n83) <= 1e-12}
    v45 = {}
    for v in grid["V45_cases"]:
        b = nh["net_" + v]["YP_BBN"] - y0n
        v45[v] = {"dY_net": b, "tol_rel": abs((nh[f"net_{v}_tol"]["YP_BBN"] - y0n) / b - 1), "stride2_rel": abs((nh[f"net_{v}_stride2"]["YP_BBN"] - y0n) / b - 1)}
    out["gates"]["V4_NET_TOL"] = {"cases": v45, "pass": all(x["tol_rel"] <= 0.01 for x in v45.values())}
    out["gates"]["V5_INTERP"] = {"pass": all(x["stride2_rel"] <= 0.01 for x in v45.values())}
    gates_ok = all(g["pass"] for g in out["gates"].values())
    # --- series and roots
    Y0c = {j: float(s83[f"o{j}_base"]["Y"]) for j in MASSES}
    for j in MASSES:
        for a, c in (("orig", "o"), ("e5", "e")):
            out["series"][f"PY_{a}_{j}"] = series(s83, n83, f"{c}{j}_")
            out["series"][f"HER_{a}_{j}"] = series(sh, nh, f"h{c}{j}_")
    nb = 0; lin = {}; quad = {}
    for key, s in out["series"].items():
        for m in ("code", "net"):
            ys = s["Y_code"] if m == "code" else s["Y_net"]
            for Ys in TARGETS:
                r, n = cross_lin(s["lb"], ys, Ys)
                q = cross_quad(s["lb"], ys, Ys)
                lin[(key, m, Ys)] = r; quad[(key, m, Ys)] = q
                nb += (r is None)
                out["roots"][f"{key}|{m}|{Ys}"] = {"lin": r, "quad": q, "n_brackets": n}
    # --- estimands
    f = lambda a, b: (a - b) if (a is not None and b is not None) else None
    NI = []; NG = []
    for j in MASSES:
        e = {}
        for Ys in TARGETS:
            row = {}
            for m in ("code", "net"):
                for a in ("orig", "e5"):
                    row[f"dgen_{m}_{a}"] = f(lin[(f"HER_{a}_{j}", m, Ys)], lin[(f"PY_{a}_{j}", m, Ys)])
                    dq = f(quad[(f"HER_{a}_{j}", m, Ys)], quad[(f"PY_{a}_{j}", m, Ys)])
                    if row[f"dgen_{m}_{a}"] is not None and dq is not None:
                        NG.append(abs(dq - row[f"dgen_{m}_{a}"]))
                for g in ("PY", "HER"):
                    row[f"D_{g}_{m}"] = f(lin[(f"{g}_e5_{j}", m, Ys)], lin[(f"{g}_orig_{j}", m, Ys)])
                row[f"I_{m}"] = f(row[f"D_HER_{m}"], row[f"D_PY_{m}"])
                dqH = f(quad[(f"HER_e5_{j}", m, Ys)], quad[(f"HER_orig_{j}", m, Ys)]); dqP = f(quad[(f"PY_e5_{j}", m, Ys)], quad[(f"PY_orig_{j}", m, Ys)])
                iq = f(dqH, dqP)
                if row[f"I_{m}"] is not None and iq is not None:
                    NI.append(abs(iq - row[f"I_{m}"]))
                row[f"ratio_absdgen_over_DPY_{m}"] = (max(abs(row[f"dgen_{m}_orig"]), abs(row[f"dgen_{m}_e5"])) / row[f"D_PY_{m}"]) if None not in (row[f"dgen_{m}_orig"], row[f"dgen_{m}_e5"], row[f"D_PY_{m}"]) else None
            e[str(Ys)] = row
        out["estimands"][str(j)] = e
    N_I = max(NI) if NI else None; N_gen = max(NG) if NG else None
    out["noise"] = {"N_I": N_I, "N_gen": N_gen}
    # --- labels
    def labels(Ys):
        E = out["estimands"]
        dg = [E[str(j)][str(Ys)][f"dgen_{m}_{a}"] for j in MASSES for m in ("code", "net") for a in ("orig", "e5")]
        ii = [E[str(j)][str(Ys)][f"I_{m}"] for j in MASSES for m in ("code", "net")]
        mx = max(abs(x) for x in dg)
        LG = "GEN_SMALL" if mx < 0.10 else ("GEN_COMPARABLE" if mx >= 0.27 else "GEN_INTERMEDIATE")
        LI = "I_UNRESOLVED" if (N_I is None or 0.02 < 5 * N_I) else ("ADDITIVE" if max(abs(x) for x in ii) <= 0.02 else "INTERACTING")
        LS = "HER_WEAKER" if all(x > 0 for x in dg) else ("HER_STRONGER" if all(x < 0 for x in dg) else "MIXED")
        return {"LG": LG, "LI": LI, "LS": LS, "max_abs_dgen": mx, "max_abs_I": max(abs(x) for x in ii)}
    if not gates_ok:
        out["labels"] = {"primary_0.251": "GATE_FAIL_NO_LABEL"}
    elif nb:
        out["labels"] = {"primary_0.251": "NOT_BRACKETED", "n_unbracketed": nb}
    else:
        out["labels"] = {"primary_0.251": labels(0.251), "LBT_0.2484": labels(0.2484)}
        E = out["estimands"]
        p1 = [E[str(j)]["0.251"]["dgen_code_orig"] for j in MASSES]
        out["predictions"]["P1_dgen_code_orig_0.251_positive_j22_j62"] = (all(x > 0 for x in p1), p1)
        out["predictions"]["P2_LG_not_GEN_SMALL"] = (out["labels"]["primary_0.251"]["LG"] != "GEN_SMALL", out["labels"]["primary_0.251"]["LG"])
        out["predictions"]["P3_max_absI_0.251_le_0.03"] = (out["labels"]["primary_0.251"]["max_abs_I"] <= 0.03, out["labels"]["primary_0.251"]["max_abs_I"])
    # --- descriptive: native and net response ratios at shared nodes (HER grid contains the PY grid)
    rr = {}
    for j in MASSES:
        for a, c in (("orig", "o"), ("e5", "e")):
            P = out["series"][f"PY_{a}_{j}"]; H = out["series"][f"HER_{a}_{j}"]
            hm = dict(zip(H["lb"], zip(H["Y_code"], H["Y_net"])))
            rows = []
            for lb, yc, yn in zip(P["lb"], P["Y_code"], P["Y_net"]):
                if lb in hm:
                    rows.append([lb, (hm[lb][0] - Y0c[j]) / (yc - Y0c[j]), (hm[lb][1] - y0n) / (yn - y0n83)])
            rr[f"{a}_{j}"] = rows
    out["descriptive"]["dY_ratio_HER_over_PY_at_shared_nodes[lb, code, net]"] = rr
    out["descriptive"]["table"] = tg.get("descriptive")
    json.dump(out, open(dst, "x"), indent=1, default=str)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()}))
    print(json.dumps(out["labels"], default=str)); print(json.dumps(out["predictions"], default=str)); print(json.dumps(out["noise"]))


if __name__ == "__main__":
    main(*sys.argv[1:6])
