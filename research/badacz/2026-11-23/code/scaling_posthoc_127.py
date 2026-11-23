# POSTHOC_127 (exploratory, NOT preregistered): does STD_A follow a clock-relabeling law
# std(M) ~= base(M * R^(-1/3)) + c*log10(R) ?  Uses only existing roots:
#   base: REVIEW_071 orig_default M_D roots at j=22,28,38,51,62,90 (2026-11-16/data/analysis069.json)
#   std:  REVIEW_124 coarse roots (2026-11-23/data/run123/sa_std_j*_A.csv)
# No new Julia run.
import json, glob, re, math, sys
import numpy as np
from scipy.interpolate import PchipInterpolator
root = sys.argv[1]
R = 0.5817518
M = lambda j: 6e8 * (1e10/6e8)**(j/99)
a69 = json.load(open(f"{root}/2026-11-16/data/analysis069.json"))
bj = sorted(int(j) for j in a69["roots"]["orig_default"])
bx = np.array([math.log10(M(j)) for j in bj]); by = np.array([a69["roots"]["orig_default"][str(j)]["M_D"] for j in bj])
std = {}
for f in glob.glob(f"{root}/2026-11-23/data/run123/sa_std_j*_A.csv"):
    for line in open(f):
        if line.startswith("#ROOT") and ",root," in line:
            p = line.strip().split(","); std[int(p[3])] = float(p[6])
lin = lambda x: float(np.interp(x, bx, by)); pch = PchipInterpolator(bx, by)
shift_m = -math.log10(R)/3
out = {"status": "POSTHOC_EXPLORATORY_NOT_PREREGISTERED", "R": R, "log10R": math.log10(R), "mass_shift_dex": shift_m, "base_nodes": dict(zip(map(str,bj), by.tolist())), "rows": {}}
# c candidates: 1.0 (empirical), 0.9 = 1/2 + a/3 with beta at t_F ~ M (main-scan.jl l.154-159) and q ~ M^-a, a=1.2,
#   0.733 = (1+a)/3 (beta at a common initial T; NOT the code's convention), 1/6 = background-energy channel only
for c in (1.0, 0.9, 2.2/3, 1/6):
    for j in sorted(std):
        x = math.log10(M(j)) + shift_m
        out["rows"].setdefault(str(j), {"std_meas": std[j], "M_g": M(j), "relabel_M_g": 10**x})
        for name, f in (("lin", lin), ("pchip", lambda x: float(pch(x)))):
            out["rows"][str(j)][f"pred_{name}_c{c:.3f}"] = f(x) + c*math.log10(R)
            out["rows"][str(j)][f"res_{name}_c{c:.3f}"] = std[j] - (f(x) + c*math.log10(R))
json.dump(out, open(sys.argv[2], "w"), indent=1, allow_nan=False)
for j, r in out["rows"].items():
    print(j, f"{r['std_meas']:.3f}", " ".join(f"{k[4:]}={v:+.3f}" for k, v in r.items() if k.startswith("res_")))
