#!/usr/bin/env python3
"""Badacz (Claude): POST HOC companion to PREREG_066 (written after the run; not part of the preregistered verdicts).
1) Rebuilds arm_*.jsonl from data/b1_066_raw_outputs.json into a temp dir, re-runs code/b1_066_analysis.py and checks the
   result is byte-identical to data/analysis066.json (reproducibility of the verdicts from the committed raw outputs).
2) Extras: X(T0) ladder table, gate-S sensitivity to the choice of default-tolerance reference (A0 = rational 1//10^3 default,
   A1 = explicit Float64 1e-3), archive-difference spread, stop bracket and M^3-clock spread on accepted steps.
Usage: python3 -I b1_066_posthoc.py <research/badacz/2026-11-15 dir> <scanning.jld2> <out.json>
"""
import json, os, sys, subprocess, tempfile, numpy as np
D, jld, outp = sys.argv[1], sys.argv[2], sys.argv[3]
raw = json.load(open(os.path.join(D, "data", "b1_066_raw_outputs.json")))
with tempfile.TemporaryDirectory() as td:
    for a, v in raw["arms"].items():
        open(os.path.join(td, "arm_%s.jsonl" % a), "w").write("\n".join(v["jsonl_lines"]) + "\n")
    rerun = os.path.join(td, "analysis_rerun.json")
    subprocess.run([sys.executable, "-I", os.path.join(D, "code", "b1_066_analysis.py"), td, jld, rerun], check=True, capture_output=True)
    same = open(rerun, "rb").read() == open(os.path.join(D, "data", "analysis066.json"), "rb").read()
an = json.load(open(os.path.join(D, "data", "analysis066.json")))
B = an["B_records"]; X = {k: B[k]["X_T0"] for k in B}; Y = {k: B[k]["Y"] for k in B}
def gate(ref):
    d03 = X["A3"] - X[ref]; d34 = X["A4"] - X["A3"]
    return {"reference": ref, "dX_A3_minus_ref": d03, "dX_A4_minus_A3": d34, "cond1_abs_le_1e-5": abs(d34) <= 1e-5,
            "cond2_le_half": abs(d34) <= 0.5 * abs(d03), "release": abs(d34) <= 1e-5 and abs(d34) <= 0.5 * abs(d03)}
diffs = np.array([p["diff"] for p in an["A"]["points"]])
res = {"analysis_rerun_byte_identical": same,
       "ladder": {k: {"Y": Y[k], "X_T0": X[k], "naccept": B[k].get("naccept"), "nreject": B[k].get("nreject"),
                      "Kclock_rel_spread": B[k].get("Kclock_rel_spread"), "Kclock_n": B[k].get("Kclock_n"),
                      "stop_bracket_M_g": B[k].get("stop_bracket_M_g"), "stop_bracket_t_s": B[k].get("stop_bracket_t_s"),
                      "M_after_over_Mstop": (B[k]["stop_bracket_M_g"][1] / B[k]["M_stop_g"]) if "stop_bracket_M_g" in B[k] else None,
                      "first_output_zero_index": B[k].get("first_nPBH_zero_index_1based"), "t_last_live_output_s": B[k].get("t_s_at_last_live")}
                  for k in ("A0", "A1", "A2", "A3", "A4")},
       "noise_C0b_dX_A1_minus_A0": X["A1"] - X["A0"], "noise_C0b_dY_A1_minus_A0": Y["A1"] - Y["A0"],
       "gate_ref_A0_prereg": gate("A0"), "gate_ref_A1_posthoc": gate("A1"),
       "spread_X_all_tolerance_arms": max(X[k] for k in ("A0", "A1", "A3", "A4")) - min(X[k] for k in ("A0", "A1", "A3", "A4")),
       "archive_diff": {"mean": float(diffs.mean()), "std": float(diffs.std(ddof=1)), "n_positive": int((diffs > 0).sum()), "n": int(len(diffs))},
       "archive_betamax_minus_A4_Y": an["A"]["points"][-1]["Y_archive"] - Y["A4"],
       "evap_stop_time_A0_over_A4_minus_1": B["A0"]["stop_bracket_t_s"][1] / B["A4"]["stop_bracket_t_s"][1] - 1}
json.dump(res, open(outp, "w"), indent=1)
print(json.dumps(res, indent=1))
