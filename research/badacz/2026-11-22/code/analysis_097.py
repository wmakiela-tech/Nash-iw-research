"""PREREG_097 analysis (frozen before production runs): fingerprint of the BlackHawk v2.3 HERWIG BBN tables.
Usage: python3 -I analysis_097.py <herwig_tables_dir> <mc_dir> <out.json>
BH side: for primary 'up' and each table node E' (grid of herwig_scripts main.cpp: 25..1e5 GeV, 100 log nodes), per-event
  multiplicity N_BH(E') = 2 x sum over the 100 final-energy entries (entries are per-primary counts per final-energy bin;
  verified: sum x 2 reproduces event multiplicities, the density reading does not).
  Endpoint: highest final-energy node with a nonzero pi+- entry, compared with E'/2 and E'.
MC side: mc_dir/{H72_f1,H73_f1,H73_f2}.json from mult_herwig_097.py (sqrt(s) = f x E').
Species: pi+- (211), K+- (321), K0L (130), p (2212), n (2112). R = N_BH / N_MC; L = log10 R.
Gates: G_MC every requested energy present, rc 0, events = requested, |<E_final/sqrt(s)> - 1| <= 1e-3; G_NODES the MC energies
  are table nodes to 1e-5 relative (table prints 6 significant digits).
Labels:
  L_SQRTS (convention test, H73): SQRTS_EQ_E if max_E |L_pi(H73_f1)| < max_E |L_pi(H73_f2)| and max_E |L_pi(H73_f1)| <= 0.04;
          SQRTS_EQ_2E if the reverse with max |L_pi(H73_f2)| <= 0.04; else UNRESOLVED.
  L_VER (version, at the convention chosen by L_SQRTS; f1 arm for 7.2): MATCH_v if all 5 species x 6 energies |L| <= 0.04 for
          version v; NO_MATCH otherwise, with PRE_72_CANDIDATE if both versions miss and L_K+-(E') falls by >= 0.10 dex from the
          lowest to the highest node for both versions (kaon deficit growing with energy in the table).
Predictions (Badacz, frozen): Pr1 L_SQRTS = SQRTS_EQ_E. Pr2 L_VER = NO_MATCH with PRE_72_CANDIDATE (BlackHawk v1.0 manual,
  May 2019, already describes the HERWIG tables, before the Herwig 7.2 release with its strangeness changes, Dec 2019)."""
import json, math, os, sys
import numpy as np

SP = {"pipm": "211", "Kpm": "321", "K0L": "130", "proton": "2212", "neutron": "2112"}
TOL = 0.04


def main(tdir, mdir, dst):
    BH = {}; end = {}
    for name in SP:
        L = open(os.path.join(tdir, name + ".txt")).read().splitlines(); iu = L[0].split().index("up")
        a = np.array([[float(x) for x in l.split()] for l in L[1:]]); Ep = np.unique(a[:, 0])
        BH[name] = {float(e): float(2 * a[a[:, 0] == e][:, iu].sum()) for e in Ep}
        if name == "pipm":
            for e in Ep:
                r = a[a[:, 0] == e]; nz = r[r[:, iu] > 0][:, 1]
                end[float(e)] = float(nz.max()) if len(nz) else None
    MC = {k: json.load(open(os.path.join(mdir, k + ".json"))) for k in ("H72_f1", "H73_f1", "H73_f2")}
    out = {"gates": {}, "bh": {}, "ratios": {}, "endpoint": {}, "labels": {}, "predictions": {}}
    nodes = sorted(BH["pipm"])
    okmc = True; okn = True; req = {}
    for k, d in MC.items():
        for e in d["energies"]:
            ok = e.get("rc_read") == 0 and e.get("rc_run") == 0 and "events" in e and abs(e["Efinal_over_sqrts"] - 1) <= 1e-3
            okmc &= ok
            okn &= min(abs(e["E"] / x - 1) for x in nodes) <= 1e-5
        req[k] = len(d["energies"])
    out["gates"]["G_MC"] = {"n_energies": req, "pass": okmc and len(set(req.values())) == 1}
    out["gates"]["G_NODES"] = {"pass": okn}
    Es = [e["E"] for e in MC["H73_f1"]["energies"]]
    near = lambda E: min(nodes, key=lambda x: abs(x / E - 1))
    for E in Es:
        n = near(E); out["bh"][f"{E:.6g}"] = {s: BH[s][n] for s in SP}
        out["endpoint"][f"{E:.6g}"] = {"max_nonzero_pi_node": end[n], "E_half": n / 2, "E": n}
    for k, d in MC.items():
        out["ratios"][k] = {}
        for e in d["energies"]:
            n = near(e["E"]); out["ratios"][k][f"{e['E']:.6g}"] = {s: math.log10(BH[s][n] / e[p]) for s, p in SP.items()}
    if not all(g["pass"] for g in out["gates"].values()):
        out["labels"] = {"status": "GATE_FAIL_NO_LABEL"}
    else:
        mx = lambda k, s: max(abs(v[s]) for v in out["ratios"][k].values())
        m1, m2 = mx("H73_f1", "pipm"), mx("H73_f2", "pipm")
        ls = "SQRTS_EQ_E" if (m1 < m2 and m1 <= TOL) else ("SQRTS_EQ_2E" if (m2 < m1 and m2 <= TOL) else "UNRESOLVED")
        f = "f2" if ls == "SQRTS_EQ_2E" else "f1"
        ver = {}
        for v, k in (("7.2", "H72_f1"), ("7.3", f"H73_{f}")):
            allmax = max(mx(k, s) for s in SP)
            rk = [out["ratios"][k][f"{E:.6g}"]["Kpm"] for E in Es]
            ver[v] = {"max_abs_L_all": allmax, "match": allmax <= TOL, "L_K_lowest": rk[0], "L_K_highest": rk[-1], "K_drop": rk[0] - rk[-1]}
        match = [v for v in ver if ver[v]["match"]]
        lv = ("MATCH_" + "_".join(match)) if match else ("NO_MATCH_PRE_72_CANDIDATE" if all(ver[v]["K_drop"] >= 0.10 for v in ver) else "NO_MATCH")
        out["labels"] = {"L_SQRTS": ls, "pi_max_abs_L": {"H73_f1": m1, "H73_f2": m2}, "L_VER": lv, "versions": ver}
        out["predictions"] = {"Pr1_SQRTS_EQ_E": ls == "SQRTS_EQ_E", "Pr2_NO_MATCH_PRE_72_CANDIDATE": lv == "NO_MATCH_PRE_72_CANDIDATE"}
    json.dump(out, open(dst, "x"), indent=1)
    print(json.dumps(out["gates"])); print(json.dumps(out["labels"])); print(json.dumps(out["predictions"]))


if __name__ == "__main__":
    main(*sys.argv[1:4])
