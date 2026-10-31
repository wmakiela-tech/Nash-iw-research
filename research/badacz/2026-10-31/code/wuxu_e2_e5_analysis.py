#!/usr/bin/env python3
"""Badacz (Claude): verdicts for E2 (PREREG_036, commit 61bfd3f), E5 (PREREG_037, commit 52f597f) and E5b (PREREG_040,
commit 04cb097) from the CSV outputs
of wuxu_subedge_variant_boundary.jl, plus the method control against the window boundaries of REVIEW_035 (analysis.json).
Shift convention: shift = boundary(variant) - boundary(native), in log10(beta); positive = weaker constraint.
Run: python3 -I wuxu_e2_e5_analysis.py --native e2_native.csv --ols8 e2_ols8.csv --zero e2_zero.csv \
         --sym e5_native_sym.csv --nsym e5b_native_nsym.csv --analysis035 analysis.json --out e2_e5_analysis.json
"""
import argparse, csv, json, math, statistics

ap = argparse.ArgumentParser()
for k in ("native", "ols8", "zero", "sym", "nsym", "analysis035", "out"):
    ap.add_argument("--" + k, required=k not in ("sym", "nsym"))
# PREREG_040 predictions (from v1/v2 scan boundaries, linear-response model), 0-based mass index -> dex
PRED_NSYM = {22: 0.023, 24: 0.053, 26: 0.067, 28: 0.079, 31: 0.100, 34: 0.123, 38: 0.155, 43: 0.185, 51: 0.230,
             62: 0.269, 80: 0.292, 90: 0.296}
a = ap.parse_args()


def read(path):
    head = open(path).readline().strip()
    rows = list(csv.DictReader([l for l in open(path) if not l.startswith("#")]))
    return head, {int(r["j"]): r for r in rows}


def bnd(r):
    return float(r["boundary_log10beta"]) if r["status"] == "bracketed" else None


H = {}; D = {}
for k in ("native", "ols8", "zero", "sym", "nsym"):
    p = getattr(a, k)
    if p:
        H[k], D[k] = read(p)
A = json.load(open(a.analysis035))
J = sorted(D["native"])
res = {"headers": H, "per_mass": {}}
for j in J:
    e = {"m_g": float(D["native"][j]["m_g"]), "native": bnd(D["native"][j]),
         "native_window_035": A["N4"]["per_mass"][str(j)]["boundary_native_C"]}
    e["control_bisection_minus_window"] = e["native"] - e["native_window_035"]
    for k in ("ols8", "zero", "sym", "nsym"):
        if k in D:
            b = bnd(D[k][j]); e[k] = b; e[k + "_status"] = D[k][j]["status"]
            e["shift_" + k] = None if b is None else b - e["native"]
    res["per_mass"][str(j)] = e
pm = res["per_mass"]
ctrl = [abs(pm[str(j)]["control_bisection_minus_window"]) for j in J]
res["control"] = {"max_abs": max(ctrl), "threshold_prereg": 0.01, "pass": max(ctrl) < 0.01,
                  "n_over": sum(c >= 0.01 for c in ctrl)}
heavy = [j for j in J if pm[str(j)]["m_g"] >= 3.5e9]
light = J[0]
v = {}
if "ols8" in D:
    s = [pm[str(j)]["shift_ols8"] for j in J]
    v["E2_V1_ols8"] = {"shifts": s, "max_abs": max(abs(x) for x in s),
                      "opposite_direction_gt_0.03": any(x > 0.03 for x in s),   # expected direction: negative (stronger)
                      "any_abs_gt_0.1": any(abs(x) > 0.1 for x in s)}
    v["E2_V1_ols8"]["falsified"] = v["E2_V1_ols8"]["opposite_direction_gt_0.03"] or v["E2_V1_ols8"]["any_abs_gt_0.1"]
if "zero" in D:
    s0 = pm[str(light)]["shift_zero"]; st0 = pm[str(light)]["zero_status"]
    sh = [pm[str(j)]["shift_zero"] for j in heavy]
    v["E2_V2_zero"] = {"shift_at_1.12e9": s0, "status_at_1.12e9": st0,
                      "shifts_m_ge_3.5e9": sh, "shifts_all": [pm[str(j)]["shift_zero"] for j in J],
                      "falsifier_light_lt_0.1": (s0 is not None and s0 < 0.1),
                      "falsifier_heavy_gt_0.3": any(x is not None and x > 0.3 for x in sh)}
    v["E2_V2_zero"]["falsified"] = v["E2_V2_zero"]["falsifier_light_lt_0.1"] or v["E2_V2_zero"]["falsifier_heavy_gt_0.3"]
if "sym" in D:
    s = [pm[str(j)]["shift_sym"] for j in J]
    v["E5_sym"] = {"shifts": s, "min": min(x for x in s if x is not None), "max": max(x for x in s if x is not None),
                   "median": statistics.median(x for x in s if x is not None),
                   "any_lt_0.05": any(x is None or x < 0.05 for x in s), "any_negative": any(x is not None and x < 0 for x in s),
                   "any_gt_0.40": any(x is not None and x > 0.40 for x in s),
                   "linear_response_reference_log10_2": math.log10(2)}
    v["E5_sym"]["falsified"] = v["E5_sym"]["any_lt_0.05"] or v["E5_sym"]["any_negative"] or v["E5_sym"]["any_gt_0.40"]
if "nsym" in D:
    s = [pm[str(j)]["shift_nsym"] for j in J]
    dev = [None if x is None else x - PRED_NSYM[j] for x, j in zip(s, J)]
    v["E5b_nsym"] = {"shifts": s, "predicted": [PRED_NSYM[j] for j in J], "obs_minus_pred": dev,
                     "max_abs_dev": max(abs(x) for x in dev if x is not None),
                     "any_dev_gt_0.1": any(x is None or abs(x) > 0.1 for x in dev),
                     "order_reversed": (s[0] is not None and s[-1] is not None and s[0] > s[-1])}
    v["E5b_nsym"]["falsified"] = v["E5b_nsym"]["any_dev_gt_0.1"] or v["E5b_nsym"]["order_reversed"]
    if "sym" in D:   # POST-HOC: fraction of the full B_sym shift carried by the source-supported nucleon split
        v["POSTHOC_nsym_over_sym"] = [None if (pm[str(j)]["shift_nsym"] is None or not pm[str(j)]["shift_sym"]) else
                                      pm[str(j)]["shift_nsym"] / pm[str(j)]["shift_sym"] for j in J]
res["verdicts"] = v
json.dump(res, open(a.out, "w"), indent=1, sort_keys=True)
print(json.dumps({k: x.get("falsified") for k, x in v.items() if isinstance(x, dict)}),"control pass:", res["control"]["pass"], "max", round(max(ctrl), 4))
