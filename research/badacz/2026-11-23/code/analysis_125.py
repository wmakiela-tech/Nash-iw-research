#!/usr/bin/env python3
"""PREREG_125 analysis (STOP A control). Thresholds frozen here and in PREREG_125.
Usage: python3 -I analysis_125.py <dir with sa_<arm>_j<j>_<slope>.csv> <analysis123_strict.json> <tables125.json> <out.json>"""
import glob, json, sys

D, A123, T125, OUT = sys.argv[1:5]
ref = json.load(open(A123))["roots"]
code = {(a, j): ref[f"{a}|j{j}|coarse"] for a in ("base", "std") for j in (20, 22, 62)}
TOL = {"A1": 0.15, "A2": 0.05}
roots, ok = {}, True
for f in sorted(glob.glob(f"{D}/sa_*.csv")):
    sl = f.split("_")[-1].split(".")[0]
    for l in open(f):
        x = l.strip().split(",")
        if l.startswith("#ROOT"):
            roots[(x[1], int(x[3]), sl)] = (x[5], float(x[6]) if x[6] != "NaN" else None)
        elif l.strip():
            ok &= x[9] == "Success"
out = {"gates": {"G_RUN": bool(ok and len(roots) == 18)}, "tol": TOL, "roots": {}, "shifts": {}, "predictions": {},
       "code_reference_run123": {f"{a}|j{j}": v for (a, j), v in code.items()}, "tables125": json.load(open(T125))}
out["gates"]["G_TAB"] = out["tables125"]["gates"]["G_TAB"]
for (a, j, sl), v in roots.items():
    out["roots"][f"{a}|j{j}|{sl}"] = v
d = lambda j, sl: (roots[("std", j, sl)][1] - roots[("base", j, sl)][1]) if roots.get(("std", j, sl), ("", None))[1] is not None and roots.get(("base", j, sl), ("", None))[1] is not None else None
dc = {j: code[("std", j)][1] - code[("base", j)][1] for j in (22, 62)}
for j in (22, 62):
    out["shifts"][f"j{j}"] = {"code": dc[j], **{sl: d(j, sl) for sl in ("m10", "m13", "m15")}}
P = out["predictions"]
v22 = [out["shifts"]["j22"][s] for s in ("m10", "m13", "m15")]
v62 = [out["shifts"]["j62"][s] for s in ("m10", "m13", "m15")]
P["P_A1_j22_shift_robust"] = {"values": v22, "ref": dc[22], "tol": TOL["A1"], "PASS": all(v is not None and abs(v - dc[22]) <= TOL["A1"] for v in v22)}
P["P_A2_j62_shift_robust"] = {"values": v62, "ref": dc[62], "tol": TOL["A2"], "PASS": all(v is not None and abs(v - dc[62]) <= TOL["A2"] for v in v62)}
P["P_A3_left_wall_std_root_j20"] = {"values": {s: roots.get(("std", 20, s)) for s in ("m10", "m13", "m15")},
                                   "PASS": all(roots.get(("std", 20, s), ("",))[0] == "root" for s in ("m10", "m13", "m15"))}
json.dump(out, open(OUT, "w"), indent=1, sort_keys=True, allow_nan=False)
print(json.dumps({"gates": out["gates"], "predictions": {k: v["PASS"] for k, v in P.items()}}, indent=1))
