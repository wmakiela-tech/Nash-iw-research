"""PREREG_088 (E4) analysis, frozen before any run.
Usage: python3 -I analysis_088.py <data_083_dir> <run_dir> <tables_json> <out.json>
Cells (j22, orig arm, code and net; Y* in {0.251, 0.2484}): PY = PREREG_083 authors' table (series orig_22 of
analysis083.json); A = direct truncated BlackHawk rows below 1e9 g; C = untruncated-trend rows (build_tables_088.py).
Estimands: E4_C = lb_C - lb_PY (physically preferred variant), E4_A = lb_A - lb_PY (lower bracket, ceiling artifact).
Crossing: linear interpolation, exactly one bracket (as 083/085). Solver-noise scale per root: N_Y / |dY/dlb| with
N_Y = max(|Y_base_A - Y_base_PY|, |Y_base_C - Y_base_PY|, 2.77e-5 from REVIEW_086).
Gates: V7 completeness (47+47 native, 97 net), V2_EXACT <= 1e-6, V6 refined, V_TABLE (rows 5-99 verbatim),
V_BASE <= 5e-4, V3 net zero <= 1e-5 and net base = 083 (<= 1e-12), V4/V5 on c22_1720 <= 1 %.
Labels (all gates PASS and all 16 crossings bracketed): over code/net x two targets,
  LC: max |E4_C| < 0.05 -> E4_SMALL ; >= 0.10 -> E4_MATERIAL ; else E4_INTERMEDIATE
  LA: max E4_A reported as the lower-bracket magnitude (descriptive; artifact by construction)
"""
import csv, json, os, sys

TARGETS = [0.251, 0.2484]


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


def main(d83, run, tj, dst):
    A83 = json.load(open(os.path.join(d83, "analysis083.json")))
    s83 = rd(os.path.join(d83, "summary_orig_083.csv")); n83 = rdj(os.path.join(d83, "net083_raw.jsonl"))
    S = {v: rd(os.path.join(run, f"dd_{v}", "summary_orig.csv")) for v in ("a", "c")}
    N = rdj(os.path.join(run, "out", "net088_raw.jsonl"))
    T = json.load(open(tj))
    C = os.path.dirname(os.path.abspath(__file__))
    exp = {v: [l.split()[0] for l in open(os.path.join(C, f"cfg088_{v}_orig.dat")) if l.strip() and not l.startswith("#")] for v in ("a", "c")}
    out = {"gates": {}, "series": {}, "roots": {}, "estimands": {}, "labels": {}, "predictions": {}}
    exp_net = ["net_base"] + ["net_" + i for v in "ac" for i in exp[v]] + ["net_c22_1720_tol", "net_c22_1720_stride2"]
    ok7 = all(sorted(S[v]) == sorted(exp[v]) for v in "ac") and len(N) == len(exp_net) and all(i in N and N[i].get("rc") == 0 and "YP_BBN" in N[i] for i in exp_net)
    out["gates"]["V7_COMPLETENESS"] = {"native": {v: len(S[v]) for v in "ac"}, "net": len(N), "net_expected": len(exp_net), "pass": ok7}
    v2 = [float(r["v2_max_rel"]) for v in "ac" for k, r in S[v].items() if not k.endswith("_base")]
    out["gates"]["V2_RATE_CONSISTENCY"] = {"max": max(v2), "pass": max(v2) <= 1e-6 and all(int(r["v2_n"]) > 0 for v in "ac" for k, r in S[v].items() if not k.endswith("_base"))}
    out["gates"]["V6_REFINED"] = {"pass": all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for v in "ac" for r in S[v].values())}
    out["gates"]["V_TABLE"] = {"pass": bool(T["rows_5_99_verbatim"])}
    y0 = float(s83["o22_base"]["Y"])
    vb = {v: abs(float(S[v][f"{v}22_base"]["Y"]) - y0) for v in "ac"}
    out["gates"]["V_BASE"] = {"absdiff": vb, "pass": all(x <= 5e-4 for x in vb.values())}
    y0n = N["net_base"]["YP_BBN"]
    zr = {v: N[f"net_{v}22_base"]["YP_BBN"] - y0n for v in "ac"}
    out["gates"]["V3_NET_ZERO"] = {"dev": zr, "Y0_net": y0n, "pass": all(abs(z) <= 1e-5 for z in zr.values()) and abs(y0n - n83["net_base"]["YP_BBN"]) <= 1e-12}
    b = N["net_c22_1720"]["YP_BBN"] - y0n
    t4 = abs((N["net_c22_1720_tol"]["YP_BBN"] - y0n) / b - 1); t5 = abs((N["net_c22_1720_stride2"]["YP_BBN"] - y0n) / b - 1)
    out["gates"]["V4_NET_TOL"] = {"rel": t4, "pass": t4 <= 0.01}
    out["gates"]["V5_INTERP"] = {"rel": t5, "pass": t5 <= 0.01}
    gates_ok = all(g["pass"] for g in out["gates"].values())
    N_Y = max(list(vb.values()) + [2.766994020661495e-05])
    sp = A83["series"]["orig_22"]
    out["series"]["PY"] = {"lb": sp["lb"], "Y_code": sp["Y_code"], "Y_net": sp["Y_net"]}
    for v in "ac":
        nodes = sorted([k for k in S[v] if not k.endswith("_base")], key=lambda k: float(S[v][k]["log10beta"]))
        out["series"][v.upper()] = {"lb": [float(S[v][k]["log10beta"]) for k in nodes], "Y_code": [float(S[v][k]["Y"]) for k in nodes],
                                    "Y_net": [N["net_" + k]["YP_BBN"] for k in nodes]}
    nb = 0; noise = []
    for key, s in out["series"].items():
        for m in ("code", "net"):
            for Ys in TARGETS:
                r, slope = cross(s["lb"], s["Y_code" if m == "code" else "Y_net"], Ys)
                nb += r is None
                out["roots"][f"{key}|{m}|{Ys}"] = {"lb": r, "slope": slope}
                if slope:
                    noise.append(N_Y / abs(slope))
    out["noise"] = {"N_Y": N_Y, "N_solver_dex_per_root": max(noise) if noise else None}
    R = out["roots"]
    for m in ("code", "net"):
        for Ys in TARGETS:
            p = R[f"PY|{m}|{Ys}"]["lb"]
            out["estimands"][f"{m}|{Ys}"] = {f"E4_{v}": (R[f"{v}|{m}|{Ys}"]["lb"] - p) if None not in (p, R[f"{v}|{m}|{Ys}"]["lb"]) else None for v in "AC"}
    if not gates_ok:
        out["labels"] = {"LC": "GATE_FAIL_NO_LABEL"}
    elif nb:
        out["labels"] = {"LC": "NOT_BRACKETED", "n_unbracketed": nb}
    else:
        ec = [abs(e["E4_C"]) for e in out["estimands"].values()]; ea = [e["E4_A"] for e in out["estimands"].values()]
        mx = max(ec)
        out["labels"] = {"LC": "E4_SMALL" if mx < 0.05 else ("E4_MATERIAL" if mx >= 0.10 else "E4_INTERMEDIATE"), "max_abs_E4_C": mx,
                         "LA_max_E4_A": max(ea), "LA_min_E4_A": min(ea)}
        E = out["estimands"]
        out["predictions"]["P1_E4_C_code_both_targets_in_[-0.05,0)"] = (all(-0.05 <= E[f"code|{Y}"]["E4_C"] < 0 for Y in TARGETS), [E[f"code|{Y}"]["E4_C"] for Y in TARGETS])
        out["predictions"]["P2_E4_A_code_0.251_ge_0.10"] = (E["code|0.251"]["E4_A"] >= 0.10, E["code|0.251"]["E4_A"])
        out["predictions"]["P3_code_net_E4_C_agree_within_0.02"] = (all(abs(E[f"code|{Y}"]["E4_C"] - E[f"net|{Y}"]["E4_C"]) <= 0.02 for Y in TARGETS),
                                                                    [E[f"code|{Y}"]["E4_C"] - E[f"net|{Y}"]["E4_C"] for Y in TARGETS])
    json.dump(out, open(dst, "x"), indent=1, default=str)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"]))
    print(json.dumps(out["estimands"])); print(json.dumps(out["predictions"], default=str)); print(json.dumps(out["noise"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
