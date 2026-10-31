#!/usr/bin/env python3
"""Badacz (Claude): verdicts for PREREG_041 (commit ad6ab99): A (paper-declared T^1.3 law below 1e9 g, variant p13, against
the native E2 boundaries), B (PYTHIA pilot gate and predictions, from pythia_pilot.json) and the C decision; plus the
POST-HOC table-edge comparison (table_edge_posthoc.json). Shift = boundary(p13) - boundary(native), log10(beta).
Run: python3 -I wuxu_prereg041_analysis.py --native e2_native.csv --p13 e2_p13.csv --ols8 e2_ols8.csv \
         --pilot pythia_pilot.json --posthoc table_edge_posthoc.json --out prereg041_analysis.json
"""
import argparse, csv, json

ap = argparse.ArgumentParser()
for k in ("native", "p13", "ols8", "pilot", "posthoc", "out"):
    ap.add_argument("--" + k, required=True)
a = ap.parse_args()


def rd(p):
    return {int(r["j"]): r for r in csv.DictReader([l for l in open(p) if not l.startswith("#")])}


N, P, O = rd(a.native), rd(a.p13), rd(a.ols8)
J = sorted(N)
per = {}
for j in J:
    bn, bp, bo = (float(X[j]["boundary_log10beta"]) for X in (N, P, O))
    per[str(j)] = {"m_g": float(N[j]["m_g"]), "native": bn, "p13": bp, "shift_p13": bp - bn, "shift_ols8": bo - bn}
light = [j for j in J if per[str(j)]["m_g"] <= 1.58e9]
heavy = [j for j in J if per[str(j)]["m_g"] >= 2.0e9]
sl = [per[str(j)]["shift_p13"] for j in light]; sh = [per[str(j)]["shift_p13"] for j in heavy]
A = {"shifts_light_m_le_1.58e9": sl, "shifts_heavy_m_ge_2.0e9": sh,
     "pred_light_in_[-0.06,-0.02]": all(-0.06 <= x <= -0.02 for x in sl),
     "pred_heavy_abs_le_0.01": all(abs(x) <= 0.01 for x in sh),
     "falsifier_positive_gt_0.03_light": any(x > 0.03 for x in sl),
     "falsifier_abs_gt_0.1_any": any(abs(per[str(j)]["shift_p13"]) > 0.1 for j in J)}
A["falsified"] = A["falsifier_positive_gt_0.03_light"] or A["falsifier_abs_gt_0.1_any"]
Pi = json.load(open(a.pilot))
B = {"gate": Pi["gate"], "predictions": Pi["predictions"], "falsified": Pi["falsified_B"],
     "failed_events": Pi["failed_events"], "C_run_allowed": Pi["run_C_allowed"]}
C = {"run": False, "reason": "PREREG_041: C runs only if B1 and B2 pass; B2 failed (|s_pi(T1) - table edge slope| > 0.10)"}
H = json.load(open(a.posthoc))
res = {"per_mass": per, "A_p13": A, "B_pythia": B, "C_pyt": C,
       "POSTHOC_table_edge": H["summary"], "POSTHOC_edge_deficit": H["edge_deficit"]}
json.dump(res, open(a.out, "w"), indent=1, sort_keys=True)
print(json.dumps({"A_falsified": A["falsified"], "A_pred_light": A["pred_light_in_[-0.06,-0.02]"],
                  "A_pred_heavy": A["pred_heavy_abs_le_0.01"], "B_falsified": B["falsified"],
                  "B1": B["gate"]["B1_pass"], "B2": B["gate"]["B2_pass"]}))
for j in J:
    e = per[str(j)]; print("%.3e  p13 %+.3f  ols8 %+.3f" % (e["m_g"], e["shift_p13"], e["shift_ols8"]))
