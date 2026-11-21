"""PREREG_090 r2: replicate spread of the folded tables (declared in PREREG_090 sec. 8).
Usage: python3 -I compare_replicates_090.py <orig_tables_dir> <rep1_tables_dir> <rep2_tables_dir> <rep1_mc> <rep2_mc> <out.json>
S = max over rows 0-28, 5 species, variants P83/H73 of |log10(Y_rep/Y_orig)|, and of the H73/P83 log-ratio difference.
Also reports eventwise energy residual maxima from the replicate MC JSONs."""
import glob, json, sys
import numpy as np

o, r1, r2, m1, m2, dst = sys.argv[1:7]
L = lambda d, t: np.loadtxt(f"{d}/{t}.dat", skiprows=1)[:29, 1:]
out = {"per_replicate": {}, "eventwise_Eresidual_max": {}}
S = 0.0; SR = 0.0
for name, d in (("R1", r1), ("R2", r2)):
    rec = {}
    for t in ("P83", "H73"):
        x = np.abs(np.log10(L(d, t) / L(o, t)))
        rec[t] = {"max": float(x.max()), "per_species_max": x.max(axis=0).tolist()}
        S = max(S, float(x.max()))
    dr = np.abs(np.log10(L(d, "H73") / L(d, "P83")) - np.log10(L(o, "H73") / L(o, "P83")))
    rec["H73_over_P83_shift_max"] = float(dr.max()); SR = max(SR, float(dr.max()))
    out["per_replicate"][name] = rec
for name, m in (("R1", m1), ("R2", m2)):
    em = 0.0
    for f in glob.glob(f"{m}/*_*.json"):
        if f.endswith("requested.json"):
            continue
        for e in json.load(open(f))["energies"]:
            em = max(em, e.get("max_abs_event_Eresidual", float("nan")))
    out["eventwise_Eresidual_max"][name] = em
out["S_yield"] = S; out["S_ratio"] = SR; out["S"] = max(S, SR)
out["verdict"] = "SPREAD_OK_G_STAT_REPLACED" if out["S"] <= 0.01 else "SPREAD_REPORTED_AS_MC_UNCERTAINTY"
out["rerun_native_needed"] = out["S"] > 0.02
out["energy_eventwise_ok"] = all(v <= 1e-3 for v in out["eventwise_Eresidual_max"].values())
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps({k: out[k] for k in ("S_yield", "S_ratio", "S", "verdict", "rerun_native_needed", "energy_eventwise_ok", "eventwise_Eresidual_max")}))
