# Figure for brief v1 (133): base vs STD_A threshold nodes and the similarity-mapped base curve.
# Inputs (existing data only, no new runs):
#   base nodes: 2026-11-16/data/analysis069.json roots.orig_default.*.M_D (REVIEW_071)
#   std nodes:  2026-11-23/data/run123/sa_std_j*_A.csv '#ROOT' lines (REVIEW_124)
#   prospective std roots: Mech-S11 ROT012 (public report, research/mech-s11/2026-11-25), transcribed below
# Usage: python3 -I figure_brief_133.py <badacz_root> <out_png> <out_json>
import sys, json, glob, math
import numpy as np
from scipy.interpolate import PchipInterpolator
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
root, out_png, out_json = sys.argv[1:4]
R = 0.5817518; L = math.log10(R); r3 = R**(1/3)
Mj = lambda j: 6e8*(1e10/6e8)**(j/99)
a69 = json.load(open(f"{root}/2026-11-16/data/analysis069.json"))["roots"]["orig_default"]
bj = sorted(int(j) for j in a69); bx = np.array([math.log10(Mj(j)) for j in bj]); by = np.array([a69[str(j)]["M_D"] for j in bj])
std = {}
for f in glob.glob(f"{root}/2026-11-23/data/run123/sa_std_j*_A.csv"):
    for line in open(f):
        if line.startswith("#ROOT") and ",root," in line:
            p = line.strip().split(","); std[int(p[3])] = float(p[6])
mech = {1474765000.0: -19.221910866204908, 2133869000.0: -19.52216040167406, 6464011000.0: -19.587029783120567}
pch = PchipInterpolator(bx, by)
xs = np.linspace(bx[0] + math.log10(r3), bx[-1] + math.log10(r3), 300)
base_at = pch(xs - math.log10(r3))
c_lo, c_hi = 0.900, 0.938   # REC14 ROT016 source c_eff band
fig, ax = plt.subplots(figsize=(6.4, 4.2), dpi=150)
ax.plot(10**bx, by, "o", color="#3b6ea5", label="base (code), native roots")
ax.plot(10**np.array([math.log10(Mj(j)) for j in sorted(std)]), [std[j] for j in sorted(std)], "s", color="#c0504d", label="STD_A (clock × R), native roots")
ax.plot(list(mech), list(mech.values()), "^", color="#2e7d32", ms=7, label="STD_A prospective test (Mech-S11)")
ax.fill_between(10**xs, base_at + c_hi*L, base_at + c_lo*L, color="#c0504d", alpha=0.35, lw=1.2, edgecolor="#c0504d", label="mapped base: β(M R^-1/3)·R^c, c∈[0.900,0.938]")
ax.axvspan(8.5e8, 1e9, color="0.88", lw=0); ax.text(8.7e8, -19.68, "M < 1e9 g:\nsource extrapolated", fontsize=6)
ax.set_xscale("log"); ax.set_xlabel("PBH mass M [g]"); ax.set_ylabel("log10 β threshold at Y_code = 0.251")
ax.set_xlim(8.5e8, 9e9); ax.legend(fontsize=7, loc="upper right"); ax.set_title("Model-level thresholds of the public Wu–Xu code (no physical bound)", fontsize=8)
fig.tight_layout(); fig.savefig(out_png)
json.dump({"status": "POSTHOC_FIGURE_EXISTING_DATA", "R": R, "c_band": [c_lo, c_hi],
           "base_nodes": dict(zip(map(str, bj), by.tolist())), "std_nodes_review124": {str(k): v for k, v in sorted(std.items())},
           "std_prospective_mech_s11_rot012": {f"{k:.0f}": v for k, v in mech.items()},
           "note": "base has no root in [-21,-16] at j16-j21 (REVIEW_124); shaded strip marks M<1e9 g where the code's hadron source is extrapolated"},
          open(out_json, "w"), indent=1, allow_nan=False)
print("ok", len(bj), len(std), len(mech))
