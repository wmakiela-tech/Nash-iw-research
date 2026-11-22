"""PREREG_103 analysis (frozen before the native run): background-only switch of the Wu-Xu native code model (EKS1-DIR-010).
Usage: python3 -I analysis_103.py <d90 = 2026-11-21/data> <run_dir> <cfg_dir> <out.json>
Arm z: authors' hadron table x 1e-12 (hadronic n<->p injection effectively off; PBH background/evaporation unchanged),
j22 and j62, log10 beta -20..-13 step 0.25, plus base (-30). Reference: authors' table (PYBH) native code model from 083
(summary_orig_083.csv; roots from analysis090.json 'PYBH_{j}|code|Y*'). X = Y/(2+Y).
Gates: G_COMPLETE (all cfg IDs present in dump_z22/dump_z62/dump_k summaries); G_RUN (n_points >= 20000, i_last_alive > 200 for
  all runs); G_DRIVER (k22_1720 Y == 083 o22_1720 Y bitwise); G_BASE (|Y_z_base - Y_o_base(083)| <= 5e-4).
  v2 (hadronic-rate consistency) is reported, not gated: with hadrons ~0 the relative check is ill-conditioned.
Estimands per mass j:
  dXz(lb) = X_z(lb) - X_z(base); crossing of Y* in {0.251, 0.2484} on the grid (exactly one bracket -> root; none -> NONE;
  more -> MULTI); background fraction at the hadronic thresholds: f(Y*) = dXz(lb_PYBH_code(Y*)) / (X(Y*) - X_o(base)) with dXz
  linearly interpolated in lb; dXz at -16 and -15 (sign of the background effect where the hadronic curve saturates).
Predictions (Badacz, frozen): Pr1 Y_z(lb) < 0.2484 for every lb <= -15 at both masses (Wu-Xu thresholds in this mass range are
  hadronic, not background); Pr2 |f| < 0.1 for both Y* at both masses (4 values)."""
import csv, json, math, os, sys

X = lambda Y: Y / (2 + Y)
TARGETS = [0.251, 0.2484]


def rd(p):
    return {r["run_id"]: r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))}


def main(d90, run, cfg_dir, dst):
    o83 = rd(os.path.join(d90, "summary_orig_083.csv")); A = json.load(open(os.path.join(d90, "analysis090.json")))
    S = {}
    for d in ("dump_k", "dump_z22", "dump_z62"):
        S.update(rd(os.path.join(run, d, "summary_orig.csv")))
    cfg = [l.split()[0] for f in ("cfg103_z.dat", "cfg103_k.dat") for l in open(os.path.join(cfg_dir, f)) if l.strip() and not l.startswith("#")]
    out = {"gates": {}, "masses": {}, "labels": {}, "predictions": {}}
    out["gates"]["G_COMPLETE"] = {"n": len(S), "expected": len(cfg), "pass": sorted(S) == sorted(cfg)}
    out["gates"]["G_RUN"] = {"pass": all(int(r["n_points"]) >= 20000 and int(r["i_last_alive"]) > 200 for r in S.values())}
    out["gates"]["G_DRIVER"] = {"pass": float(S["k22_1720"]["Y"]) == float(o83["o22_1720"]["Y"])}
    vb = {j: abs(float(S[f"z{j}_base"]["Y"]) - float(o83[f"o{j}_base"]["Y"])) for j in (22, 62)}
    out["gates"]["G_BASE"] = {"absdiff": vb, "pass": all(v <= 5e-4 for v in vb.values())}
    out["v2_max_rel_reported"] = max(float(r["v2_max_rel"]) for k, r in S.items() if not k.endswith("_base"))
    ok = all(g["pass"] for g in out["gates"].values())
    pr1 = True; fs = []
    for j in (22, 62):
        ids = sorted([k for k in S if k.startswith(f"z{j}_") and not k.endswith("_base")], key=lambda k: float(S[k]["log10beta"]))
        lb = [float(S[k]["log10beta"]) for k in ids]; Y = [float(S[k]["Y"]) for k in ids]
        Xb = X(float(S[f"z{j}_base"]["Y"])); dX = [X(y) - Xb for y in Y]
        m = {"lb": lb, "Y": Y, "dX": dX, "Ymax": max(Y), "lb_at_Ymax": lb[Y.index(max(Y))], "crossings": {}, "f": {}}
        for t in TARGETS:
            br = [i for i in range(len(lb) - 1) if (Y[i] - t) * (Y[i + 1] - t) <= 0 and Y[i] != Y[i + 1]]
            if len(br) == 1:
                i = br[0]; m["crossings"][str(t)] = lb[i] + (t - Y[i]) * (lb[i + 1] - lb[i]) / (Y[i + 1] - Y[i])
            else:
                m["crossings"][str(t)] = "NONE" if not br else "MULTI"
            r = A["roots"][f"PYBH_{j}|code|{t}"]["lb"]
            dxz = float(__import__("numpy").interp(r, lb, dX))
            full = X(t) - X(float(o83[f"o{j}_base"]["Y"]))
            m["f"][str(t)] = {"lb_PYBH": r, "dXz": dxz, "dX_full": full, "f": dxz / full}
            fs.append(abs(dxz / full))
        for x0 in (-16.0, -15.0):
            m[f"dXz_at_{x0}"] = dX[lb.index(x0)]
        pr1 &= all(y < 0.2484 for x, y in zip(lb, Y) if x <= -15.0 + 1e-9)
        out["masses"][str(j)] = m
    out["labels"] = {"status": "OK" if ok else "GATE_FAIL_NO_LABEL"}
    if ok:
        out["predictions"] = {"Pr1_no_bg_crossing_2484_le_-15": pr1, "Pr2_abs_f_lt_0.1_all4": all(v < 0.1 for v in fs), "max_abs_f": max(fs)}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps({k: v["pass"] for k, v in out["gates"].items()})); print(json.dumps(out["predictions"]))
    for j, m in out["masses"].items():
        print(j, "Ymax %.6f at %.2f" % (m["Ymax"], m["lb_at_Ymax"]), "cross", m["crossings"], "f", {k: round(v["f"], 4) for k, v in m["f"].items()},
              "dXz(-16) %.2e dXz(-15) %.2e" % (m["dXz_at_-16.0"], m["dXz_at_-15.0"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
