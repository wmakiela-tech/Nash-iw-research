#!/usr/bin/env python3
"""Badacz (Claude), POST HOC bridge check: does the native band kernel of REVIEW_050 (s_eff per band) predict the measured
contour shift of the p13 sub-edge variant of REVIEW_042 (Q_i(m) = Q_i(m1)(m/m1)^-1.3 below the table edge m1 = 1e9 g,
instead of the authors' first-interval log-log extrapolation)? Both inputs were measured earlier; nothing here is a prediction
made before the data. Zero free parameters: band-averaged number ratio r_b (p13/native, all five channels summed, mass clock
dM/dt = -K/M^2) and Delta_pred = -log10(1 + sum_b (r_b - 1) s_b), b in {B, C, D} (band A lies above the table edge).
Usage: python3 -I wuxu_kernel_p13_bridge_posthoc.py --table hadrons_from_PBH.dat --kernel data/kernel_analysis.json --out out.json
"""
import argparse, json, math
ap = argparse.ArgumentParser(); ap.add_argument("--table", required=True); ap.add_argument("--kernel", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
G_GEV = 5.60958860380445e23
rows = [list(map(float, l.split())) for l in open(a.table) if l.strip() and not l.startswith("m_PBH")]
m1 = rows[0][0]/G_GEV; m2 = rows[1][0]/G_GEV
Q1 = [rows[0][c] for c in range(1, 6)]; S_NAT = [math.log(rows[1][c]/rows[0][c])/math.log(m2/m1) for c in range(1, 6)]
M_GRID = 1.0572611951580e8
BANDS = {"B": (3e8, 1e9), "C": (M_GRID, 3e8), "D": (0.0, M_GRID)}
MEASURED_P13 = {22: -0.048, 28: -0.030, 34: -0.028, 62: -0.005}     # REVIEW_042 table A (bisection to 0.005 dex)
def integ(q0, s, lo, hi):            # int_lo^hi q0 (M/m1)^s M^2 dM
    return q0*m1**(-s)*(hi**(3 + s) - lo**(3 + s))/(3 + s)
K = json.load(open(a.kernel))["derived"]
res = {"native_first_interval_slopes": S_NAT, "table_edge_g": m1, "j": {}}
for j, meas in MEASURED_P13.items():
    d = K[str(j)]; s = {"B": (d["B2"]["s_eff"], d["B2"]["se_s_eff"]), "C": (d["C2"]["s_eff"], d["C2"]["se_s_eff"]), "D": (d["Dc"]["s_eff"], d["Dc"]["se_s_eff"])}
    sn = {"B": d["B2"]["s_num"], "C": d["C2"]["s_num"], "D": d["Dc"]["s_num"]}
    rb = {}
    for b, (lo, hi) in BANDS.items():
        nat = sum(integ(Q1[c], S_NAT[c], lo, hi) for c in range(5)); p13 = sum(integ(Q1[c], -1.3, lo, hi) for c in range(5))
        rb[b] = p13/nat
    arg = 1 + sum((rb[b] - 1)*s[b][0] for b in BANDS); argn = 1 + sum((rb[b] - 1)*sn[b] for b in BANDS)
    se = math.sqrt(sum(((rb[b] - 1)*s[b][1])**2 for b in BANDS))/(math.log(10)*arg)
    pred = -math.log10(arg)
    res["j"][str(j)] = {"r_band": rb, "pred_kernel": pred, "se_pred_kernel": se, "pred_number_only": -math.log10(argn),
                        "measured_REVIEW042": meas, "kernel_minus_measured": pred - meas}
json.dump(res, open(a.out, "w"), indent=1)
print("native slopes", [round(x, 4) for x in S_NAT])
for j, r in res["j"].items():
    print(j, "r_B %.4f r_C %.4f r_D %.4f" % (r["r_band"]["B"], r["r_band"]["C"], r["r_band"]["D"]),
          "| kernel %+.4f +- %.4f | number-only %+.4f | measured %+.3f | diff %+.4f" % (r["pred_kernel"], r["se_pred_kernel"], r["pred_number_only"], r["measured_REVIEW042"], r["kernel_minus_measured"]))
