#!/usr/bin/env python3
"""Badacz (Claude): PREREG_043 T1 (commit ec6d473) - charge semantics of the columns of the Wu-Xu hadron table
hadrons_from_PBH.dat (Fenyutanchan/Primordial-Black-Hole @ d395183, blob 06d0883a...), using K0_L (a single state, no
separate antiparticle) as the charge-unambiguous anchor.
Model: PYTHIA 8.318 pilot (research/badacz/2026-10-31/data/subedge_pilot/pythia_pilot.json), per-parton multiplicities of
pi+- (sum), K+- (sum), K0_L, p+pbar (sum), n+nbar (sum) for quark and gluon jets, convolved with the geometric-optics Hawking
shape exactly as in the pilot: R_i(T) ~ T [w_q <n_iq>_T + w_g <n_ig>_T].
r_i = (Q_i / Q_K0L)_table / (R_i / R_K0L)_model at table rows 6..12 (T = 3.9-6.4 TeV, interior); H_agg if median r_i > 1/sqrt2.
Run: python3 -I wuxu_column_semantics_k0l.py --table <hadrons_from_PBH.dat> --pilot <pythia_pilot.json> --out <file.json>
"""
import argparse, json, math, statistics
import numpy as np

ap = argparse.ArgumentParser(); ap.add_argument("--table", required=True); ap.add_argument("--pilot", required=True)
ap.add_argument("--out", required=True); a = ap.parse_args()
GEV_PER_G = 5.60958860e23; TCONST = 1.058e13
rows = np.array([[float(x) for x in l.split()] for l in open(a.table).read().splitlines()[1:] if l.strip()])
names = ["pi", "K", "K0L", "p", "n"]; col = {h: c + 1 for c, h in enumerate(names)}
T = TCONST / (rows[:, 0] / GEV_PER_G)
P = json.load(open(a.pilot)); E = np.array(P["E_TeV"], float) * 1e3; lnE = np.log(E)
n = {lab: {h: np.array(P["n_per_parton"][lab][h]) for h in names} for lab in ("q", "g")}
xs = np.exp(np.linspace(math.log(1e-3), math.log(60.), 4000))
wf = xs ** 3 / (np.exp(xs) + 1.0); wb = xs ** 3 / np.expm1(xs)
Wq = 72 * 1.5 * 1.2020569031595942; Wg = 16 * 2 * 1.2020569031595942


def nE(lab, h, e):
    y = np.log(n[lab][h]); x = np.log(e)
    s0 = (y[1] - y[0]) / (lnE[1] - lnE[0]); s1 = (y[-1] - y[-2]) / (lnE[-1] - lnE[-2])
    return np.exp(np.where(x < lnE[0], y[0] + s0 * (x - lnE[0]), np.where(x > lnE[-1], y[-1] + s1 * (x - lnE[-1]), np.interp(x, lnE, y))))


def R(h, t):
    return t * (Wq * (wf * nE("q", h, xs * t)).sum() / wf.sum() + Wg * (wb * nE("g", h, xs * t)).sum() / wb.sum())


out = {"rows_used": list(range(6, 13)), "per_row": [], "decision_threshold": 1 / math.sqrt(2)}
r = {h: [] for h in names if h != "K0L"}
for k in range(6, 13):
    e = {"row": k, "T_GeV": float(T[k])}
    for h in r:
        tab = rows[k, col[h]] / rows[k, col["K0L"]]; mod = R(h, T[k]) / R("K0L", T[k])
        e[h] = {"table_ratio_to_K0L": float(tab), "model_ratio_to_K0L": float(mod), "r": float(tab / mod)}
        r[h].append(tab / mod)
    out["per_row"].append(e)
out["median_r"] = {h: float(statistics.median(v)) for h, v in r.items()}
out["decision"] = {h: ("H_agg" if out["median_r"][h] > 1 / math.sqrt(2) else "H_single") for h in r}
out["prediction_r_in_[0.75,1.33]"] = {h: bool(0.75 <= out["median_r"][h] <= 1.33) for h in r}
out["H_agg_falsified_for_nucleons"] = bool(out["median_r"]["p"] < 1 / math.sqrt(2) or out["median_r"]["n"] < 1 / math.sqrt(2))
# POST-HOC context (not part of the decision): the same ratios at the edge row 0 and at a low-T row
out["POSTHOC_rows_0_and_60"] = {str(k): {h: float((rows[k, col[h]] / rows[k, col["K0L"]]) / (R(h, T[k]) / R("K0L", T[k]))) for h in r}
                                for k in (0, 60)}
json.dump(out, open(a.out, "w"), indent=1, sort_keys=True)
print(json.dumps({"median_r": {h: round(v, 4) for h, v in out["median_r"].items()}, "decision": out["decision"],
                  "pred": out["prediction_r_in_[0.75,1.33]"], "falsified_nucleons": out["H_agg_falsified_for_nucleons"]}))
