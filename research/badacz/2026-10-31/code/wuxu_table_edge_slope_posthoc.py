#!/usr/bin/env python3
"""Badacz (Claude): POST-HOC comparison (after PREREG_041 gate B2 failed) of
 (i) the local log-log slope of the authors' hadron table hadrons_from_PBH.dat (Fenyutanchan/Primordial-Black-Hole @ d395183)
     row by row, and
 (ii) the slope of the PYTHIA-pilot rate model R_i(T) (from pythia_pilot.json, same convolution as the pilot script),
over T = 2-11 TeV (table interior up to the edge) and beyond.
Also: the deficit of the edge-row value relative to an extrapolation of the interior slope (rows 6..12) to the edge.
Run: python3 -I wuxu_table_edge_slope_posthoc.py --table <hadrons_from_PBH.dat> --pilot <pythia_pilot.json> --out <file.json>
"""
import argparse, json, math
import numpy as np

ap = argparse.ArgumentParser(); ap.add_argument("--table", required=True); ap.add_argument("--pilot", required=True)
ap.add_argument("--out", required=True); a = ap.parse_args()
GEV_PER_G = 5.60958860e23; TCONST = 1.058e13
rows = np.array([[float(x) for x in l.split()] for l in open(a.table).read().splitlines()[1:] if l.strip()])
names = ["pi", "K", "K0L", "p", "n"]
lm = np.log(rows[:, 0]); T = TCONST / (rows[:, 0] / GEV_PER_G)
loc = {h: (np.log(rows[1:, c + 1]) - np.log(rows[:-1, c + 1])) / (lm[1:] - lm[:-1]) for c, h in enumerate(names)}
Tmid = np.sqrt(T[1:] * T[:-1])

P = json.load(open(a.pilot)); E = np.array(P["E_TeV"], float) * 1e3; lnE = np.log(E)
n = {lab: {h: np.array(P["n_per_parton"][lab][h]) for h in names} for lab in ("q", "g")}
xs = np.exp(np.linspace(math.log(1e-3), math.log(60.), 4000))
wf = xs ** 3 / (np.exp(xs) + 1.0); wb = xs ** 3 / np.expm1(xs)
Wq = 72 * 1.5 * 1.2020569031595942; Wg = 16 * 2 * 1.2020569031595942


def nE(lab, h, e):
    y = np.log(n[lab][h]); x = np.log(e)
    s0 = (y[1] - y[0]) / (lnE[1] - lnE[0]); s1 = (y[-1] - y[-2]) / (lnE[-1] - lnE[-2])
    return np.exp(np.where(x < lnE[0], y[0] + s0 * (x - lnE[0]), np.where(x > lnE[-1], y[-1] + s1 * (x - lnE[-1]), np.interp(x, lnE, y))))


def lnR(h, t):
    return math.log(t * (Wq * (wf * nE("q", h, xs * t)).sum() / wf.sum() + Wg * (wb * nE("g", h, xs * t)).sum() / wb.sum()))


def model_slope(h, t, d=0.02):
    return -(lnR(h, t * math.exp(d)) - lnR(h, t * math.exp(-d))) / (2 * d)


out = {"rows": int(len(rows)), "per_row": [], "edge_deficit": {}}
for k in range(0, 13):
    out["per_row"].append({"row_pair": [k, k + 1], "T_mid_GeV": float(Tmid[k]),
                           "table_slope": {h: float(loc[h][k]) for h in names},
                           "pythia_model_slope": {h: model_slope(h, float(Tmid[k])) for h in names}})
for c, h in enumerate(names):
    s_int = float(np.polyfit(lm[6:13], np.log(rows[6:13, c + 1]), 1)[0])      # interior slope, rows 6..12 (T 3.9-6.4 TeV)
    pred0 = float(np.log(rows[6, c + 1]) + s_int * (lm[0] - lm[6]))
    out["edge_deficit"][h] = {"interior_slope_rows6_12": s_int, "ln_edge_table_minus_interior_extrap": float(np.log(rows[0, c + 1]) - pred0)}
d_int = [abs(r["table_slope"][h] - r["pythia_model_slope"][h]) for r in out["per_row"][6:] for h in names]
out["summary"] = {"max_abs_table_minus_model_rows6_12": max(d_int),
                  "edge_pair_table_slope_pi": out["per_row"][0]["table_slope"]["pi"],
                  "edge_pair_model_slope_pi": out["per_row"][0]["pythia_model_slope"]["pi"]}
json.dump(out, open(a.out, "w"), indent=1, sort_keys=True)
for r in out["per_row"]:
    print("T=%7.0f GeV  table s_pi=%+.3f  model s_pi=%+.3f" % (r["T_mid_GeV"], r["table_slope"]["pi"], r["pythia_model_slope"]["pi"]))
print(json.dumps(out["summary"]), json.dumps({h: round(v["ln_edge_table_minus_interior_extrap"], 4) for h, v in out["edge_deficit"].items()}))
