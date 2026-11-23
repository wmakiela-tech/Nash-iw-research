#!/usr/bin/env python3
"""PREREG_123 analysis (STD_A native). Reads the per-process CSVs of std_a_123.jl; thresholds frozen here and in PREREG_123.
Usage: python3 -I analysis_123.py <dir with sa_*.csv> <out.json>"""
import glob, json, sys
import numpy as np

D, OUT = sys.argv[1:3]
R_FAC = 0.5817518
AUTH = {22: -17.220222662721067, 62: -19.389217861290064}          # authors' JLD2 roots (EKS1 ROT016, REC13 ROT017)
EKS1 = {"d22": -1.39, "d62": -0.24, "r18": -18.13, "r20": -18.36}   # EKS1 ROT026 reduced model (tau = 407 s)
TOL = {"base": 0.05, "tau": 0.01, "rep": 0.05, "mono": 3e-4, "d22": 0.20, "d62": 0.10, "wall": 0.25}
pts, roots = {}, {}
for f in sorted(glob.glob(f"{D}/sa_*.csv")):
    for l in open(f):
        x = l.strip().split(",")
        if l.startswith("#ROOT"):
            roots[(x[1], int(x[3]), x[4])] = (x[5], float(x[6]))
        elif l.strip():
            key = (x[0], int(x[2]), f.split("_")[-1].split(".")[0])     # arm, j, grid tag A/B from file name
            pts.setdefault(key, []).append({"lb": float(x[4]), "Y": float(x[5]), "tau": float(x[6]), "ret": x[9]})
out = {"roots": {f"{a}|j{j}|{m}": v for (a, j, m), v in roots.items()}, "gates": {}, "predictions": {}, "tol": TOL, "ref": {"auth": AUTH, "eks1": EKS1}}
r = lambda a, j, m="coarse": roots.get((a, j, m), ("missing", float("nan")))
out["gates"]["G_RUN"] = all(p["ret"] == "Success" for v in pts.values() for p in v) and len(roots) > 0
out["gates"]["G_BASE"] = {f"j{j}": [r("base", j)[1], AUTH[j]] for j in (22, 62)}
out["gates"]["G_BASE"]["PASS"] = all(abs(r("base", j)[1] - AUTH[j]) <= TOL["base"] for j in (22, 62))
taus = {}
for (a, j, g), v in pts.items():
    if g == "A":
        t = [p["tau"] for p in v if p["tau"] == p["tau"]]
        if t: taus[(a, j)] = t[0]
tr = {j: taus[("std", j)] / taus[("base", j)] for (a, j) in taus if a == "std" and ("base", j) in taus}
out["gates"]["G_TAU"] = {"ratios": {str(j): v for j, v in tr.items()}, "expected": 1 / R_FAC,
                         "PASS": all(abs(v * R_FAC - 1) <= TOL["tau"] for v in tr.values()) and len(tr) > 0}
mono = []
for (a, j, g), v in pts.items():
    c = sorted([p for p in v if p["lb"] in (-21, -20, -19, -18, -17, -16, -20.5, -19.5, -18.5, -17.5, -16.5, -15.5)], key=lambda p: p["lb"])
    mono.append(all(c[i + 1]["Y"] >= c[i]["Y"] - TOL["mono"] for i in range(len(c) - 1)))
out["gates"]["G_MONO"] = all(mono)
rep = {}
for (a, j, m), (st, val) in roots.items():
    if m == "coarseB":
        rep[f"{a}|j{j}"] = [r(a, j)[1], val, val - r(a, j)[1]]
out["gates"]["G_REP"] = {"pairs": rep, "PASS": all(abs(v[2]) <= TOL["rep"] for v in rep.values()) and len(rep) > 0}
P = out["predictions"]
d22 = r("std", 22)[1] - r("base", 22)[1]; d62 = r("std", 62)[1] - r("base", 62)[1]
P["P_S1_j22_shift_NONBLIND"] = {"value": d22, "ref": EKS1["d22"], "tol": TOL["d22"], "PASS": abs(d22 - EKS1["d22"]) <= TOL["d22"]}
P["P_S2_j62_shift"] = {"value": d62, "ref": EKS1["d62"], "tol": TOL["d62"], "PASS": abs(d62 - EKS1["d62"]) <= TOL["d62"]}
P["P_S3_left_wall_std_roots"] = {"j18": r("std", 18), "j20": r("std", 20), "ref": [EKS1["r18"], EKS1["r20"]], "tol": TOL["wall"],
    "PASS": r("std", 18)[0] == "root" and r("std", 20)[0] == "root" and abs(r("std", 18)[1] - EKS1["r18"]) <= TOL["wall"]
            and abs(r("std", 20)[1] - EKS1["r20"]) <= TOL["wall"]}
P["P_S4_base_no_root_below_m17_for_j16_21"] = {"base": {f"j{j}": r("base", j) for j in range(16, 22)},
    "PASS": all(r("base", j)[0] != "root" or r("base", j)[1] > -17.0 for j in range(16, 22))}
# secondary target 0.2484: lowest upward crossing by linear interpolation over all evaluated points (no prediction)
sec = {}
for (a, j, g), v in pts.items():
    c = sorted(v, key=lambda p: p["lb"]); lb = np.array([p["lb"] for p in c]); Y = np.array([p["Y"] for p in c])
    k = [i for i in range(len(c) - 1) if Y[i] < 0.2484 <= Y[i + 1]]
    sec[f"{a}|j{j}|{g}"] = float(lb[k[0]] + (0.2484 - Y[k[0]]) * (lb[k[0] + 1] - lb[k[0]]) / (Y[k[0] + 1] - Y[k[0]])) if k else None
out["secondary_root_Y02484"] = sec
out["shifts_all_masses"] = {f"j{j}": [r("base", j), r("std", j)] for j in (16, 17, 18, 19, 20, 21, 22, 62)}
out["points"] = {f"{a}|j{j}|{g}": v for (a, j, g), v in pts.items()}
json.dump(out, open(OUT, "w"), indent=1, sort_keys=True)
print(json.dumps({"gates": {k: (v if isinstance(v, bool) else v.get("PASS")) for k, v in out["gates"].items()},
                  "predictions": {k: v["PASS"] for k, v in P.items()}}, indent=1))
