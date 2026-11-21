"""PREREG_090: build variant hadron tables and run the table-level gates.
Usage: python3 -I make_tables_090.py <bh_tables_dir(hadronization_tables)> <primary.tsv> <authors_table> <mc_dir> <out_dir>
mc_dir holds pythia_<prim>.json and herwig_<prim>.json for the 11 hadronic primaries.
Gates (rows 0-28 = table masses <= 1.08e10 g, 5 species):
  G_FOLD   my folding of the BlackHawk PYTHIA table / BlackHawk's own totals = BIN_PY = dl/(exp(dl)-1)^-1 ... i.e. the ratio
           must be constant and equal to 1.025814 (500-bin log final-energy grid, forward-difference density) within 1e-3
  G_COARSE BH PYTHIA multiplicities sampled at the MC energies + log-log interpolation reproduce the fine fold within 1 %
  G_STAT   1-sigma MC statistical error of each folded yield <= 1 %
  G_MC     every requested energy generated (events = requested, no init failure), |E_final/2E - 1| <= 1e-3,
           K0S and hyperons absent from the final state (BBN stable set)
Variant tables (authors' format, BlackHawk-PYTHIA pipeline convention: true fold / 1.025814):
  P83.dat (PYTHIA 8.3), H73.dat (Herwig 7.3), BHc.dat (coarse control).
Exit 7 if any gate fails."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fold_090 as F

bhdir, prim, auth, mcdir, out = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
DL_PY = np.log(1e11) / 499; BIN_PY = (np.exp(DL_PY) - 1) / DL_PY
DL_HW = np.log(1e11) / 99; BIN_HW = (np.exp(DL_HW) - 1) / DL_HW
ELO = {c: 25.0 for c in F.MCNAME}; ELO.update({"Wpm": 100.0, "Z0": 100.0, "top": 200.0, "gluons": 100.0, "higgs": 100.0, "tau": 100.0})
bh = F.load_bh(os.path.join(bhdir, "pythia_tables")); bhH = F.load_bh(os.path.join(bhdir, "herwig_tables"))
m, E, Phi = F.load_primary(prim)
T = np.loadtxt(prim + ".secondary_totals.tsv", skiprows=1)[:, 2:]
A = np.loadtxt(auth, skiprows=1)
K = slice(0, 29)
res = {"gates": {}, "descriptive": {}, "constants": {"BIN_PY": BIN_PY, "BIN_HW": BIN_HW, "HBAR": F.HBAR, "ELO": ELO}}
Yfine = F.fold("BH", bh, m, E, Phi)
r = Yfine[K] / T[K]
res["gates"]["G_FOLD"] = {"ratio_min": float(r.min()), "ratio_max": float(r.max()), "expected": BIN_PY,
                          "pass": bool(np.all(np.abs(r / BIN_PY - 1) <= 1e-3))}
res["gates"]["G_AUTHORS_UNITS"] = {"max_rel": float(np.max(np.abs(T * F.HBAR / A[:, 1:] - 1))), "pass": bool(np.max(np.abs(T * F.HBAR / A[:, 1:] - 1)) <= 1e-6)}
mc = {}; gm = []
for g in ("pythia", "herwig"):
    mc[g] = {}
    for c, name in F.MCNAME.items():
        d = json.load(open(os.path.join(mcdir, f"{g}_{name}.json")))
        for e in d["energies"]:
            ok = (e.get("events", 0) > 0 and not e.get("init_failed") and e.get("rc_run", 0) == 0 and abs(e["Efinal_over_2E"] - 1) <= 1e-3
                  and all(e.get(str(i), 0.0) == 0.0 for i in (310, 3122, 3222, 3112, 3312, 3322, 3334)))
            gm.append({"gen": g, "prim": name, "E": e["E"], "events": e.get("events"), "ok": bool(ok)})
        mc[g][name] = F.load_mc(os.path.join(mcdir, f"{g}_{name}.json"))
req = json.load(open(os.path.join(mcdir, "requested.json")))
okn = all(x["ok"] for x in gm) and all(x["events"] == req[x["prim"]][f"{x['E']:g}"] for x in gm) and len(gm) == 2 * sum(len(v) for v in req.values())
res["gates"]["G_MC"] = {"n_energy_runs": len(gm), "failed": [x for x in gm if not x["ok"]], "pass": bool(okn)}
Ybc = F.fold("BHc", bh, m, E, Phi, mc["pythia"], ELO)
rc = np.abs(Ybc[K] / Yfine[K] - 1)
res["gates"]["G_COARSE"] = {"max_rel": float(rc.max()), "pass": bool(rc.max() <= 0.01)}
Y = {}; st = {}
for g, tag in (("pythia", "P83"), ("herwig", "H73")):
    Y[tag] = F.fold("MC", bh, m, E, Phi, mc[g], ELO)
    st[tag] = F.stat_err(bh, m, E, Phi, mc[g], ELO) / Y[tag]
res["gates"]["G_STAT"] = {"max_rel": {t: float(st[t][K].max()) for t in st}, "pass": bool(max(st[t][K].max() for t in st) <= 0.01)}
for tag, YY in (("P83", Y["P83"]), ("H73", Y["H73"]), ("BHc", Ybc)):
    F.write_table(os.path.join(out, f"{tag}.dat"), m, YY / BIN_PY)
Gpy = A[:, 1:]
res["descriptive"]["log10_P83_over_authors_rows0_28"] = np.log10(Y["P83"][K] / BIN_PY / (Gpy[K] / F.HBAR)).tolist()
res["descriptive"]["log10_H73_over_P83_rows0_28"] = np.log10(Y["H73"][K] / Y["P83"][K]).tolist()
YbhH = F.fold("BH", bhH, m, E, Phi)
res["descriptive"]["log10_BHHER_over_BHPY_truecounts_rows0_28"] = np.log10(YbhH[K] / Yfine[K]).tolist()
res["descriptive"]["binning_artifact_log10_HER_minus_PY"] = float(np.log10(BIN_PY / BIN_HW))
res["descriptive"]["log10_H73_over_BHHER_truecounts_rows0_28"] = np.log10(Y["H73"][K] / YbhH[K]).tolist()
res["descriptive"]["mc_multiplicity_ratio_H_over_P_per_primary"] = {
    name: {s: (mc["herwig"][name][s][1] / np.where(mc["pythia"][name][s][1] > 0, mc["pythia"][name][s][1], np.nan)).tolist() for s in F.SPEC}
    for name in F.MCNAME.values()}
res["descriptive"]["mc_energies"] = {name: mc["pythia"][name]["pipm"][0].tolist() for name in F.MCNAME.values()}
json.dump(res, open(os.path.join(out, "tables090.json"), "x"), indent=1, default=float)
ok = all(v["pass"] for v in res["gates"].values())
print(json.dumps({k: v["pass"] for k, v in res["gates"].items()}))
sys.exit(0 if ok else 7)
