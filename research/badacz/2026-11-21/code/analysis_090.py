"""PREREG_090 analysis (frozen before any production MC or native run).
Usage: python3 -I analysis_090.py <data_dir(2026-11-21/data)> <run_dir> <out.json>
Cells: j in {22, 62}, orig arm, model in {code, net}, Y* in {0.251, 0.2484}.
Series: PYBH = authors' table (analysis083.json orig_j), HERBH = BlackHawk HERWIG R2 (analysis085.json HER_orig_j),
        P83 = PYTHIA 8.3 table, H73 = Herwig 7.3 table (this run; dd_p, dd_h, out/net090_raw.jsonl).
Estimands (linear crossing, exactly one bracket):
  dmod   = lb_H73 - lb_P83      (modern generator systematic)
  drepro = lb_P83 - lb_PYBH     (does modern PYTHIA reproduce the authors' table at threshold level?)
  dhold  = lb_HERBH - lb_H73    (BlackHawk HERWIG table vs modern Herwig)
  dgenBH = lb_HERBH - lb_PYBH   (GAP-005 value, recomputed);  share = (dgenBH - dmod) / dgenBH
Noise: N_Y = max(|Y_base_v - Y_base_083|, 2.77e-5); per root N_Y / |dY/dlb|.
Labels (all gates PASS, all crossings bracketed), over the 8 (j, model, Y*) cells:
  LM: max|dmod| < 0.10 MOD_SMALL ; >= 0.27 MOD_COMPARABLE ; else MOD_INTERMEDIATE  (+ flag if max|dmod| < 5 x max root noise)
  LR: max|drepro| <= 0.05 AUTHORS_PY_REPRODUCED else PY_NOT_REPRODUCED
  LS: all dmod > 0 HER_WEAKER ; all < 0 HER_STRONGER ; else MIXED
Predictions (informed by pilot uu-bar multiplicities, PREREG_090 sec. 6): P1 LR reproduced; P2 all dmod in (0, 0.25);
  P3 all dhold >= +0.10.
"""
import csv, json, os, sys

TARGETS = [0.251, 0.2484]
MASSES = [22, 62]


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


def main(dd, run, dst):
    A83 = json.load(open(os.path.join(dd, "analysis083.json"))); A85 = json.load(open(os.path.join(dd, "analysis085.json")))
    s83 = rd(os.path.join(dd, "summary_orig_083.csv")); n83 = rdj(os.path.join(dd, "net083_raw.jsonl"))
    S = {v: rd(os.path.join(run, f"dd_{v}", "summary_orig.csv")) for v in "ph"}
    N = rdj(os.path.join(run, "out", "net090_raw.jsonl"))
    TG = json.load(open(os.path.join(run, "tables", "tables090.json")))
    C = os.path.dirname(os.path.abspath(__file__))
    exp = {v: [l.split()[0] for l in open(os.path.join(C, f"cfg090_{v}_orig.dat")) if l.strip() and not l.startswith("#")] for v in "ph"}
    out = {"gates": dict(TG["gates"]), "series": {}, "roots": {}, "estimands": {}, "labels": {}, "predictions": {}}
    vt = json.load(open(os.path.join(run, "out", "v_table.json")))
    out["gates"]["V_TABLE"] = vt
    exp_net = ["net_base"] + ["net_" + i for v in "ph" for i in exp[v]] + [f"net_{x}_{s}" for x in ("p22_1720", "p62_1940") for s in ("tol", "stride2")]
    ok7 = all(sorted(S[v]) == sorted(exp[v]) for v in "ph") and len(N) == len(exp_net) and all(i in N and N[i].get("rc") == 0 and "YP_BBN" in N[i] for i in exp_net)
    out["gates"]["V7_COMPLETENESS"] = {"native": {v: len(S[v]) for v in "ph"}, "net": len(N), "net_expected": len(exp_net), "pass": ok7}
    nb = [k for v in "ph" for k in S[v] if not k.endswith("_base")]
    v2 = [float(S[k[0]][k]["v2_max_rel"]) for k in nb]
    out["gates"]["V2_RATE_CONSISTENCY"] = {"max": max(v2), "pass": max(v2) <= 1e-6 and all(int(S[k[0]][k]["v2_n"]) > 0 for k in nb)}
    out["gates"]["V6_REFINED"] = {"pass": all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for v in "ph" for r in S[v].values())}
    vb = {f"{v}{j}": abs(float(S[v][f"{v}{j}_base"]["Y"]) - float(s83[f"o{j}_base"]["Y"])) for v in "ph" for j in MASSES}
    out["gates"]["V_BASE"] = {"absdiff": vb, "pass": all(x <= 5e-4 for x in vb.values())}
    y0n = N["net_base"]["YP_BBN"]
    zr = {f"{v}{j}": N[f"net_{v}{j}_base"]["YP_BBN"] - y0n for v in "ph" for j in MASSES}
    out["gates"]["V3_NET_ZERO"] = {"dev": zr, "pass": all(abs(z) <= 1e-5 for z in zr.values()) and abs(y0n - n83["net_base"]["YP_BBN"]) <= 1e-12}
    v45 = {}
    for x in ("p22_1720", "p62_1940"):
        b = N["net_" + x]["YP_BBN"] - y0n
        v45[x] = {"tol_rel": abs((N[f"net_{x}_tol"]["YP_BBN"] - y0n) / b - 1), "stride2_rel": abs((N[f"net_{x}_stride2"]["YP_BBN"] - y0n) / b - 1)}
    out["gates"]["V4_NET_TOL"] = {"cases": v45, "pass": all(c["tol_rel"] <= 0.01 for c in v45.values())}
    out["gates"]["V5_INTERP"] = {"pass": all(c["stride2_rel"] <= 0.01 for c in v45.values())}
    gates_ok = all(g["pass"] for g in out["gates"].values())
    N_Y = max(list(vb.values()) + [2.766994020661495e-05])
    for j in MASSES:
        s = A83["series"][f"orig_{j}"]; out["series"][f"PYBH_{j}"] = {"lb": s["lb"], "Y_code": s["Y_code"], "Y_net": s["Y_net"]}
        s = A85["series"][f"HER_orig_{j}"]; out["series"][f"HERBH_{j}"] = {"lb": s["lb"], "Y_code": s["Y_code"], "Y_net": s["Y_net"]}
        for v, tag in (("p", "P83"), ("h", "H73")):
            nodes = sorted([k for k in S[v] if k.startswith(f"{v}{j}_") and not k.endswith("_base")], key=lambda k: float(S[v][k]["log10beta"]))
            out["series"][f"{tag}_{j}"] = {"lb": [float(S[v][k]["log10beta"]) for k in nodes], "Y_code": [float(S[v][k]["Y"]) for k in nodes],
                                           "Y_net": [N["net_" + k]["YP_BBN"] for k in nodes]}
    nbr = 0; noise = []
    for key, s in out["series"].items():
        for m in ("code", "net"):
            for Ys in TARGETS:
                r, sl = cross(s["lb"], s["Y_code" if m == "code" else "Y_net"], Ys)
                nbr += r is None
                out["roots"][f"{key}|{m}|{Ys}"] = {"lb": r, "slope": sl, "noise_dex": (N_Y / abs(sl)) if sl else None}
                if sl:
                    noise.append(N_Y / abs(sl))
    out["noise"] = {"N_Y": N_Y, "max_root_noise_dex": max(noise) if noise else None}
    R = lambda k, j, m, Y: out["roots"][f"{k}_{j}|{m}|{Y}"]["lb"]
    f = lambda a, b: (a - b) if None not in (a, b) else None
    for j in MASSES:
        for m in ("code", "net"):
            for Y in TARGETS:
                e = {"dmod": f(R("H73", j, m, Y), R("P83", j, m, Y)), "drepro": f(R("P83", j, m, Y), R("PYBH", j, m, Y)),
                     "dhold": f(R("HERBH", j, m, Y), R("H73", j, m, Y)), "dgenBH": f(R("HERBH", j, m, Y), R("PYBH", j, m, Y))}
                e["share_of_dgenBH_not_explained_by_modern"] = ((e["dgenBH"] - e["dmod"]) / e["dgenBH"]) if None not in (e["dmod"], e["dgenBH"]) else None
                out["estimands"][f"{j}|{m}|{Y}"] = e
    if not gates_ok:
        out["labels"] = {"LM": "GATE_FAIL_NO_LABEL"}
    elif nbr:
        out["labels"] = {"LM": "NOT_BRACKETED", "n_unbracketed": nbr}
    else:
        E = out["estimands"].values()
        dm = [e["dmod"] for e in E]; dr = [e["drepro"] for e in E]; dh = [e["dhold"] for e in E]
        mx = max(abs(x) for x in dm)
        out["labels"] = {"LM": "MOD_SMALL" if mx < 0.10 else ("MOD_COMPARABLE" if mx >= 0.27 else "MOD_INTERMEDIATE"),
                         "max_abs_dmod": mx, "resolution_flag": ("UNRESOLVED_FROM_ZERO" if mx < 5 * out["noise"]["max_root_noise_dex"] else "RESOLVED"),
                         "LR": "AUTHORS_PY_REPRODUCED" if max(abs(x) for x in dr) <= 0.05 else "PY_NOT_REPRODUCED", "max_abs_drepro": max(abs(x) for x in dr),
                         "LS": "HER_WEAKER" if all(x > 0 for x in dm) else ("HER_STRONGER" if all(x < 0 for x in dm) else "MIXED")}
        out["predictions"]["P1_LR_reproduced"] = (out["labels"]["LR"] == "AUTHORS_PY_REPRODUCED", max(abs(x) for x in dr))
        out["predictions"]["P2_all_dmod_in_(0,0.25)"] = (all(0 < x < 0.25 for x in dm), dm)
        out["predictions"]["P3_all_dhold_ge_0.10"] = (all(x >= 0.10 for x in dh), dh)
    json.dump(out, open(dst, "x"), indent=1, default=str)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"]))
    print(json.dumps(out["estimands"])); print(json.dumps(out["predictions"], default=str)); print(json.dumps(out["noise"]))


if __name__ == "__main__":
    main(*sys.argv[1:4])
