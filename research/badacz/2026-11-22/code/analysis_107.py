"""PREREG_107 analysis (frozen before the native run): SCOPE12 ROT010 / AUD3 ROT015 six-probe test of the j22 interior
code x network interaction C at Y* = 0.25027090177105143 (an exact 083 CODE_e5 node at log10 beta = -17.05).
Usage: python3 -I analysis_107.py <d90 = 2026-11-21/data> <run_dir> <grid107.json> <out.json>
C = [r_NET_e5 - r_NET_orig] - [r_CODE_e5 - r_CODE_orig], r_CODE_e5 = -17.05 (exact node).
Probe roots: linear crossing between the two probe nodes (+-0.001 dex around the 083 linear root) of each bracket:
CODE_orig (code Y of o22_codelo/hi), NET_orig (net Y of o22_netlo/hi), NET_e5 (net Y of e22_netlo/hi).
A bracket is VALID if the two probe values straddle Y* (sign change); otherwise INVALID (no root, no interpolation outside).
Gates: G_COMPLETE (7 native + 8 net incl. net_base), G_RUN (n_points >= 20000, i_last_alive > 200), G_V2 (<= 1e-6),
  G_DRIVER (o22_1730 code Y and net Y bitwise = 083; net_base bitwise = 083).
Labels: CERTIFIED_WINDOW if all 3 brackets VALID and C_probe in (-0.030498, -0.024498) (SCOPE12 window);
  OUTSIDE_WINDOW if all VALID and C_probe outside; BRACKET_FAIL if any INVALID.
Descriptive: per bracket dY across the probes vs the expected slope x 0.002 dex, and the shift of each probe root from the 083 coarse
  linear root.
Prediction (Badacz, frozen): Pr1 label != CERTIFIED_WINDOW. Reason: the expected dY across a +-0.001 dex bracket (slope 0.006-0.008
  per dex -> 1.2-1.6e-5) is below the documented node-level variation of the native solver (rms 2-7e-5 per node, REVIEW_095), so the
  narrow brackets resolve solver variation rather than interpolation error, unless that variation is strongly correlated over 0.002 dex."""
import csv, json, os, sys

WIN = (-0.030498, -0.024498)


def rd(p):
    return {r["run_id"]: r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))}


def rdj(p):
    o = {}
    for l in open(p):
        d = json.loads(l); o[d["run_id"]] = d
    return o


def main(d90, run, grid, dst):
    G = json.load(open(grid)); Ys = G["Y_star"]
    o83 = rd(os.path.join(d90, "summary_orig_083.csv")); n83 = rdj(os.path.join(d90, "net083_raw.jsonl"))
    S = {}; S.update(rd(os.path.join(run, "dd_o", "summary_orig.csv"))); S.update(rd(os.path.join(run, "dd_e", "summary_e5.csv")))
    N = rdj(os.path.join(run, "out", "net107_raw.jsonl"))
    out = {"gates": {}, "brackets": {}, "labels": {}, "predictions": {}}
    ids = ["o22_codelo", "o22_codehi", "o22_netlo", "o22_nethi", "o22_1730", "e22_netlo", "e22_nethi"]
    out["gates"]["G_COMPLETE"] = {"pass": sorted(S) == sorted(ids) and len(N) == 8 and all(N.get("net_" + i, {}).get("rc") == 0 and "YP_BBN" in N["net_" + i] for i in ids) and N["net_base"].get("rc") == 0}
    out["gates"]["G_RUN"] = {"pass": all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for r in S.values())}
    out["gates"]["G_V2"] = {"max": max(float(r["v2_max_rel"]) for r in S.values()), "pass": all(float(r["v2_max_rel"]) <= 1e-6 for r in S.values())}
    drv = {"code": float(S["o22_1730"]["Y"]) == float(o83["o22_1730"]["Y"]), "net": N["net_o22_1730"]["YP_BBN"] == n83["net_o22_1730"]["YP_BBN"],
           "net_base": N["net_base"]["YP_BBN"] == n83["net_base"]["YP_BBN"]}
    out["gates"]["G_DRIVER"] = dict(drv, **{"pass": all(drv.values())})
    spec = {"CODE_orig": ("o22_codelo", "o22_codehi", "code"), "NET_orig": ("o22_netlo", "o22_nethi", "net"), "NET_e5": ("e22_netlo", "e22_nethi", "net")}
    R = {}
    for k, (lo, hi, m) in spec.items():
        x = [float(S[lo]["log10beta"]), float(S[hi]["log10beta"])]
        y = [float(S[i]["Y"]) for i in (lo, hi)] if m == "code" else [N["net_" + i]["YP_BBN"] for i in (lo, hi)]
        valid = (y[0] - Ys) * (y[1] - Ys) <= 0 and y[0] != y[1]
        r = x[0] + (Ys - y[0]) * (x[1] - x[0]) / (y[1] - y[0]) if valid else None
        R[k] = r
        out["brackets"][k] = {"lb": x, "Y": y, "dY": y[1] - y[0], "valid": valid, "root": r, "root_083": G["roots_083_linear"][k],
                              "shift_vs_083": (r - G["roots_083_linear"][k]) if r is not None else None}
    ok = all(g["pass"] for g in out["gates"].values())
    if not ok:
        out["labels"] = {"status": "GATE_FAIL_NO_LABEL"}
    else:
        if all(b["valid"] for b in out["brackets"].values()):
            C = (R["NET_e5"] - R["NET_orig"]) - (G["CODE_e5_exact_node"] - R["CODE_orig"])
            lab = "CERTIFIED_WINDOW" if WIN[0] < C < WIN[1] else "OUTSIDE_WINDOW"
        else:
            C = None; lab = "BRACKET_FAIL"
        out["labels"] = {"status": lab, "C_probe": C, "C_083_linear": -0.027497866601121284, "window": WIN,
                         "n_valid": sum(b["valid"] for b in out["brackets"].values())}
        out["predictions"] = {"Pr1_not_CERTIFIED_WINDOW": lab != "CERTIFIED_WINDOW"}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))
    for k, b in out["brackets"].items():
        print(k, "valid", b["valid"], "dY %.2e" % b["dY"], "root", b["root"], "shift", b["shift_vs_083"])


if __name__ == "__main__":
    main(*sys.argv[1:5])
