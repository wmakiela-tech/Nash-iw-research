"""PREREG_105 analysis (frozen before production runs): does Herwig 7.1.5 (default tune, built from source) reproduce the
BlackHawk v2.3 HERWIG BBN tables at sqrt(s) = E' (the convention established in REVIEW_098)?
Usage: python3 -I analysis_105.py <herwig_tables_dir> <mc105_dir> <analysis097.json> <out.json>
BH side as in analysis_097 (N_BH(E') = 2 x sum of the 100 final-energy entries of column 'up' at node E').
MC side: mc105/H71_f1.json from mult_herwig_097.py (Herwig 7.1.5, primary up, sqrt(s) = E', 10000 events at the same 6 nodes).
L = log10(N_BH/N_MC) for pi+-, K+-, K0L, p, n; se_L = MC standard error in dex (BH tables: 1e5 events, neglected).
Gates: G_MC (rc 0, events = 10000, |<E_final/sqrt(s)> - 1| <= 1e-3 at all 6 nodes),
G_NODES (energies = table nodes to 1e-5 relative), G_SAME_NODES (identical energies to the 097 arms).
Label: MATCH_7.1 if all 30 |L| <= tol_cell = max(0.04, 4 se_L) (tolerance not below the documented MC noise; lesson of
REVIEW_100); NO_MATCH otherwise. Reported with it: L_K at the lowest and highest node and the
K drop, next to the 097 values for 7.2.0 and 7.3.0 (f1).
Prediction (Badacz, frozen): Pr1 MATCH_7.1 (tables of BlackHawk v1.0, May 2019, made with the then-current Herwig 7.1.x
default tune)."""
import json, math, os, sys
import numpy as np

SP = {"pipm": "211", "Kpm": "321", "K0L": "130", "proton": "2212", "neutron": "2112"}
TOL = 0.04


def main(tdir, mdir, a97, dst):
    BH = {}
    for name in SP:
        L = open(os.path.join(tdir, name + ".txt")).read().splitlines(); iu = L[0].split().index("up")
        a = np.array([[float(x) for x in l.split()] for l in L[1:]]); Ep = np.unique(a[:, 0])
        BH[name] = {float(e): float(2 * a[a[:, 0] == e][:, iu].sum()) for e in Ep}
    nodes = sorted(BH["pipm"]); near = lambda E: min(nodes, key=lambda x: abs(x / E - 1))
    d = json.load(open(os.path.join(mdir, "H71_f1.json"))); A97 = json.load(open(a97))
    out = {"gates": {}, "ratios": {}, "labels": {}, "predictions": {}}
    en = d["energies"]
    out["gates"]["G_MC"] = {"pass": len(en) == 6 and all(e.get("rc_read") == 0 and e.get("rc_run") == 0 and e.get("events") == 10000 and abs(e["Efinal_over_sqrts"] - 1) <= 1e-3 for e in en)}
    out["gates"]["G_NODES"] = {"pass": all(abs(e["E"] / near(e["E"]) - 1) <= 1e-5 for e in en)}
    e97 = sorted(float(k) for k in A97["ratios"]["H73_f1"])
    out["gates"]["G_SAME_NODES"] = {"pass": all(abs(float(f"{e['E']:.6g}") / x - 1) <= 1e-9 for e, x in zip(en, e97))}
    for e in en:
        n = near(e["E"]); out["ratios"][f"{e['E']:.6g}"] = {s: math.log10(BH[s][n] / e[p]) for s, p in SP.items()}
        out.setdefault("tol", {})[f"{e['E']:.6g}"] = {s: max(TOL, 4 * e["se_" + p] / e[p] / math.log(10)) for s, p in SP.items()}
    if not all(g["pass"] for g in out["gates"].values()):
        out["labels"] = {"status": "GATE_FAIL_NO_LABEL"}
    else:
        mx = max(abs(v) for r in out["ratios"].values() for v in r.values())
        ok = all(abs(out["ratios"][E][s]) <= out["tol"][E][s] for E in out["ratios"] for s in SP)
        ks = [out["ratios"][k]["Kpm"] for k in sorted(out["ratios"], key=float)]
        cmp97 = {k: [A97["ratios"][k][x]["Kpm"] for x in sorted(A97["ratios"][k], key=float)] for k in ("H72_f1", "H73_f1")}
        out["labels"] = {"L_VER": "MATCH_7.1" if ok else "NO_MATCH", "max_abs_L": mx, "L_K_lowest": ks[0], "L_K_highest": ks[-1], "K_drop": ks[0] - ks[-1],
                         "K_097": {k: {"lowest": v[0], "highest": v[-1], "drop": v[0] - v[-1]} for k, v in cmp97.items()}}
        out["predictions"] = {"Pr1_MATCH_7.1": ok}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps(out["gates"])); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))
    for E, r in out["ratios"].items():
        print("E'=%-9s" % E, " ".join("%s %+.3f" % (s, x) for s, x in r.items()))


if __name__ == "__main__":
    main(*sys.argv[1:5])
