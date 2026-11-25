# PREREG_134 analysis (frozen in commit 4fa5fbd before computation). Existing STOP A CSVs only.
# Usage: python3 -I pev_sign_split_134.py <dir_with_unzipped_artifacts> <out_json>
import sys, csv, glob, json, math, os, hashlib
src, out = sys.argv[1], sys.argv[2]
TOL = 1e-6
def load(path):
    rows = []; idx = []
    with open(path) as fh:
        for r in csv.DictReader(fh):
            idx.append(int(r["accepted"]))
            # column "accepted" is the running index of accepted events (1..2000); every row is an accepted event (correction to PREREG_134 §1 wording, made before any statistic was seen)
            res = float(r["Efinal_over_2E"]) - 1.0
            n = int(r["n_211"]) + int(r["n_-211"]); e = float(r["E_211"]) + float(r["E_-211"])
            rows.append((res, n, e / n if n > 0 else float("nan")))
    assert [i + 1 for i in range(len(rows))] == idx, "accepted index not contiguous"

    return rows
def ms(x):
    x = [v for v in x if not math.isnan(v)]; k = len(x)
    if k < 2: return k, float("nan"), float("nan")
    m = sum(x) / k; v = sum((t - m) ** 2 for t in x) / (k - 1); return k, m, math.sqrt(v / k)
def z(a, b):
    ka, ma, sa = ms(a); kb, mb, sb = ms(b)
    if ka < 10 or kb < 10: return None
    return {"diff": ma - mb, "se": math.hypot(sa, sb), "z": (ma - mb) / math.hypot(sa, sb), "n_a": ka, "n_b": kb}
files = sorted(glob.glob(os.path.join(src, "*", "*_w[01]_e[0-5].csv")))
cells = {}
for f in files:
    name = os.path.basename(f)[:-4]
    rows = load(f)
    P = [r for r in rows if abs(r[0]) <= TOL]; D = [r for r in rows if r[0] < -TOL]; S = [r for r in rows if r[0] > TOL]
    c = {"file_sha256": hashlib.sha256(open(f, "rb").read()).hexdigest(), "n_accepted": len(rows), "n_pass": len(P), "n_def": len(D), "n_sur": len(S),
         "N_mean": {k: ms([r[1] for r in g])[1:] for k, g in (("pass", P), ("def", D), ("sur", S))},
         "N_def_minus_pass": z([r[1] for r in D], [r[1] for r in P]), "N_sur_minus_pass": z([r[1] for r in S], [r[1] for r in P]),
         "N_sur_minus_def": z([r[1] for r in S], [r[1] for r in D]), "Epi_fail_minus_pass": z([r[2] for r in D + S], [r[2] for r in P])}
    cells[name] = c
def stouffer(names, key):
    zs = [cells[n][key]["z"] for n in names if n in cells and cells[n][key] is not None]
    return {"z_tot": sum(zs) / math.sqrt(len(zs)) if zs else None, "k": len(zs), "cells": [n for n in names if n in cells and cells[n][key] is not None]}
main = ["up_w0_e4", "up_w0_e5", "gluon_w0_e4", "gluon_w0_e5"]
tot = {k: stouffer(main, k) for k in ("N_def_minus_pass", "N_sur_minus_pass", "N_sur_minus_def", "Epi_fail_minus_pass")}
zd, zs_, zsd = (tot[k]["z_tot"] for k in ("N_def_minus_pass", "N_sur_minus_pass", "N_sur_minus_def"))
if None not in (zd, zs_, zsd) and zd <= -3 and zs_ <= -3 and abs(zsd) < 3: verdict = "H_T"
elif zsd is not None and zsd >= 3: verdict = "H_C"
else: verdict = "UNDETERMINED"
desc = {grp: {k: stouffer(grp_cells, k) for k in ("N_def_minus_pass", "N_sur_minus_pass", "N_sur_minus_def", "Epi_fail_minus_pass")}
        for grp, grp_cells in (("on_arm_e4_e5", ["up_w1_e4", "up_w1_e5", "gluon_w1_e4", "gluon_w1_e5"]), ("off_arm_e3", ["up_w0_e3", "gluon_w0_e3"]))}
def clean(o):
    if isinstance(o, float) and math.isnan(o): return None
    if isinstance(o, dict): return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    return o
json.dump(clean({"prereg": "IW_BADACZ_PEV_GENERATOR_DIAGNOSTIC_SIGN_SPLIT_PREREG_134_20261125 @4fa5fbd", "tol": TOL, "main_cells": main,
           "main_stouffer": tot, "verdict": verdict, "descriptive": desc, "cells": cells}), open(out, "w"), indent=1, allow_nan=False)
print("verdict", verdict); print({k: (round(v["z_tot"], 2) if v["z_tot"] is not None else None, v["k"]) for k, v in tot.items()})
for n in main + ["up_w1_e4", "up_w1_e5", "gluon_w1_e4", "gluon_w1_e5", "up_w0_e3", "gluon_w0_e3"]:
    c = cells.get(n)
    if not c: print(n, "missing"); continue
    f = lambda key: (None if c[key] is None else f"{c[key]['diff']:+.1f}({c[key]['z']:+.1f})")
    print(n, c["n_pass"], c["n_def"], c["n_sur"], "means P/D/S", [None if (isinstance(v[0], float) and math.isnan(v[0])) else round(v[0], 1) for v in c["N_mean"].values()],
          "D-P", f("N_def_minus_pass"), "S-P", f("N_sur_minus_pass"), "S-D", f("N_sur_minus_def"), "Epi F-P", f("Epi_fail_minus_pass"))
