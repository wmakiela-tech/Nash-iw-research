#!/usr/bin/env python3
"""Mech-S10 ROT016: independent original-source multichannel baseline anomaly
for Wu-Xu native hadron-table x1e-12 switch and control G_DRIVER coverage.

- Source-only, Python3 standard library. No original Julia / MC / BBN run.
- Original native source summary_z{22,62}_103.csv, source k control and
  original 083 control, plus the frozen 103 analysis/runner and original
  081 rate-dump implementation. All exact Git blob SHA gated fail-closed.
- Four *jointly observed*, NOT statistically independent, output channels
  of native solver run: Y, T_last_alive_MeV, n_points, i_last_alive.
  The latter two are sample-count and PBH-evaporation localization indices,
  NOT independent physics observables nor a proof of numerical solver error.
- Two explicit source-only empirical reference pools: 7 or 13 DIFFERENT beta
  parameter inputs, so cross-beta SD is NOT calibrated solver error or p-value.
- Check G_DRIVER actual code tests one scalar Y equality, not bytewise whole
  rate trajectories; original control in fact matches 9 deterministic summary
  columns exactly (not whole rate dumps). Exclude run_id and elapsed seconds.
- Synthetic in-memory mutation of a non-Y summary field illustrates semantic
  blind spot of scalar-only G_DRIVER. NOT real owner source, not physical run.
- Preserve original GATE_FAIL_NO_LABEL and unassessed prereg Pr1/Pr2.

Usage from public Nash-iw-research repository root:
python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot016_review104_multichannel_baseline_coanomaly_and_driver_guard.py OUT.json
"""
import csv
import json
import math
import statistics
from pathlib import Path
import subprocess
import sys

D=Path("research/badacz/2026-11-22")
O=Path("research/badacz/2026-11-21")
SOURCES={
    D/"data/summary_z22_103.csv":"921d7aeb225f822e359f9e2338a4beb2ee80057c",
    D/"data/summary_z62_103.csv":"2d22e83d2046ca6f0c0d86488c46bdef1b10de2c",
    D/"data/summary_k_103.csv":"5fc470583885885b7ea54d2b88b9a7f8cd93438f",
    O/"data/summary_orig_083.csv":"f7ea90eb3202933e9f52336315c1f36b3d40b019",
    D/"data/analysis103.json":"4d1bce4e9a546a2b646075fd160b00bb81e7c46a",
    D/"code/analysis_103.py":"cd41b2b60c9691eb5b882678d27e3a52d9f0d03a",
    D/"code/run103.sh":"d746889306f2125aaf950d42722bd2afe7b63cac",
    O/"code/rate_dump_081.jl":"4b415a6ddd7d102ad03194af75aa1fb9203c11fb",
    D/"IW_BADACZ_B1_DIR010_BACKGROUND_ONLY_SWITCH_PREREG_103_20261122.md":"e8cbfd766ac88548fb651eb6adc1b28de7964eb0",
    D/"IW_BADACZ_B1_DIR010_BACKGROUND_ONLY_SWITCH_REVIEW_104_20261122.md":"efd8bfba573b92739bc781acdddf6d04c6ebda98",
}
FIELDS=("Y","T_last_alive_MeV","n_points","i_last_alive")
DETERMINISTIC_SUMMARY_COLUMNS=("arm","j","log10beta","Y","T_last_alive_MeV",
                               "n_points","i_last_alive","v2_max_rel","v2_n")
CUTOFFS=(-18.5,-17.0)

def fetch_pinned():
    res={}
    for p,sha in SOURCES.items():
        assert p.is_file(),("MISSING_SOURCE",str(p))
        got=subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
        assert got==sha,("MUTATED_SOURCE",str(p),got,sha)
        res[str(p)]=p.read_text(encoding="utf-8")
    return res

def csvrows(txt):
    lines=[s for s in txt.splitlines() if s.strip() and not s.startswith("#")]
    rows=list(csv.DictReader(lines))
    assert rows and len(rows)==len({r["run_id"] for r in rows})
    return rows

def main(dst):
    src=fetch_pinned()
    nativeimpl=src[str(O/"code/rate_dump_081.jl")]
    testimpl=src[str(D/"code/analysis_103.py")]
    runner=src[str(D/"code/run103.sh")]
    assert 'i_d = isnothing(fe) ? length(a_l) : fe - 1' in nativeimpl
    assert 'alive && (Tlast = Float64(EUval(MeV, T)))' in nativeimpl
    assert 'Float64(EUval(MeV, T)) > 30.0 && continue' in nativeimpl
    assert "nwritten += 1" in nativeimpl
    # ONLY one scalar float equality, not a full trajectory or 9-channel bitwise gate
    literal_gate='float(S["k22_1720"]["Y"]) == float(o83["o22_1720"]["Y"])'
    assert literal_gate in testimpl
    assert "G_BASE" in testimpl and "G_RUN" in testimpl
    assert "table_scale_085.py" in runner and "1e-12" in runner
    frozen=json.loads(src[str(D/"data/analysis103.json")])
    assert frozen["gates"]["G_COMPLETE"]["pass"]
    assert frozen["gates"]["G_RUN"]["pass"]
    assert frozen["gates"]["G_DRIVER"]["pass"]
    assert frozen["gates"]["G_BASE"]["pass"] is False
    assert frozen["labels"]["status"]=="GATE_FAIL_NO_LABEL"
    assert frozen["predictions"]=={}
    ctrl_old={r["run_id"]:r for r in csvrows(src[str(O/"data/summary_orig_083.csv")])}
    ctrl_k=csvrows(src[str(D/"data/summary_k_103.csv")])
    assert len(ctrl_k)==1 and ctrl_k[0]["run_id"]=="k22_1720"
    assert "o22_1720" in ctrl_old
    r_k=ctrl_k[0]
    r_o=ctrl_old["o22_1720"]
    all_det_match={k:(r_k[k]==r_o[k]) for k in DETERMINISTIC_SUMMARY_COLUMNS}
    assert len(all_det_match)==9 and all(all_det_match.values())
    assert float(r_k["Y"])==float(r_o["Y"])
    assert r_k["run_id"]!=r_o["run_id"]
    assert r_k["seconds"]!=r_o["seconds"]
    mutated=dict(r_k)
    mutated["T_last_alive_MeV"]=repr(float(r_k["T_last_alive_MeV"])+0.1)
    assert float(mutated["Y"])==float(r_o["Y"])
    assert mutated["T_last_alive_MeV"]!=r_o["T_last_alive_MeV"]
    assert not all(mutated[k]==r_o[k] for k in DETERMINISTIC_SUMMARY_COLUMNS)
    # The above only illustrates the gate's ability to miss a *constructed*
    # non-Y change; the actual 9 fields match as source strings.
    groups={}
    for j in ("22","62"):
        raw=csvrows(src[str(D/f"data/summary_z{j}_103.csv")])
        assert len(raw)==30
        b=[r for r in raw if r["run_id"]==f"z{j}_base"]
        assert len(b)==1 and float(b[0]["log10beta"])==-30.
        rest=sorted([r for r in raw if r["run_id"]!=f"z{j}_base"],
                    key=lambda r:float(r["log10beta"]))
        assert len(rest)==29 and all(float(rest[i]["log10beta"])<float(rest[i+1]["log10beta"]) for i in range(28))
        assert all(abs(float(rest[i]["log10beta"])-(-20.0+i*.25))<1e-8 for i in range(29))
        ownerbase=ctrl_old[f"o{j}_base"]
        rec={
          "mass_j":int(j),
          "actual_native_z_base_source_run_id":b[0]["run_id"],
          "actual_z_base_parameter_beta":1e-30,
          "actual_orig083_original_physical_table_base_Y":float(ownerbase["Y"]),
          "owner_103_G_BASE_absdiff":frozen["gates"]["G_BASE"]["absdiff"][j],
          "source_z_base_fields":{key:float(b[0][key]) for key in FIELDS},
          "reference_pools":{}
        }
        assert abs(float(b[0]["Y"])-float(ownerbase["Y"]))==frozen["gates"]["G_BASE"]["absdiff"][j]
        for cutoff in CUTOFFS:
            pool=[r for r in rest if float(r["log10beta"])<=cutoff+1e-10]
            N=7 if cutoff==-18.5 else 13
            assert len(pool)==N
            stats={}
            for col in FIELDS:
                values=[float(r[col]) for r in pool]
                vl=min(values);vh=max(values)
                bl=float(b[0][col])
                direction="BELOW_ALL" if bl<vl else "ABOVE_ALL" if bl>vh else "INSIDE_MINMAX"
                # A descriptive cross-input SD is not an estimated solver precision
                descriptive_sd=statistics.stdev(values)
                stats[col]={
                   "base":bl,
                   "source_beta_pool_min":vl,
                   "source_beta_pool_max":vh,
                   "source_beta_pool_mean":statistics.mean(values),
                   "source_beta_pool_distinct_input_SD_NOT_SOLVER_NOISE":descriptive_sd,
                   "source_beta_pool_distinct_beta_values":N,
                   "base_vs_pool":direction,
                   "closest_source_empirical_boundary_gap":
                      (vl-bl if direction=="BELOW_ALL"
                       else bl-vh if direction=="ABOVE_ALL" else 0.),
                   "base_difference_from_pool_mean":bl-statistics.mean(values),
                   "source_beta_pool_only_NOT_CONFIDENCE_INTERVAL":True
                }
            assert all(v["base_vs_pool"]!="INSIDE_MINMAX" for v in stats.values())
            rec["reference_pools"][str(cutoff)]={
                "n_physically_distinct_beta_inputs":len(pool),
                "source_beta_min":float(pool[0]["log10beta"]),
                "source_beta_max":float(pool[-1]["log10beta"]),
                "coanomalous_channels":len([v for v in stats.values() if v["base_vs_pool"]!="INSIDE_MINMAX"]),
                "fields":stats
            }
        groups[j]=rec
    # Exact data-specific sign pattern, not an independent-probability result
    exp7={"22":{"Y":"ABOVE_ALL","T_last_alive_MeV":"BELOW_ALL","n_points":"ABOVE_ALL","i_last_alive":"BELOW_ALL"},
          "62":{"Y":"BELOW_ALL","T_last_alive_MeV":"BELOW_ALL","n_points":"BELOW_ALL","i_last_alive":"ABOVE_ALL"}}
    for j in ("22","62"):
        for cutoff in CUTOFFS:
            for k,v in exp7[j].items():
                assert groups[j]["reference_pools"][str(cutoff)]["fields"][k]["base_vs_pool"]==v
    answer={
      "artifact":"IW_MECH_S10_ROT016_BADACZ103_MULTICHANNEL_BASELINE_COANOMALY_AND_DRIVER_GATE_SEMANTICS",
      "exposure":"PUBLIC",
      "mode":"ORIGINAL_NATIVE_SUMMARY_SOURCE_ONLY_POSTHOC",
      "source_gits":{str(p):v for p,v in SOURCES.items()},
      "frozen_owner_native_103_gates":frozen["gates"],
      "frozen_owner_native_labels":frozen["labels"],
      "unassessed_owner_prereg_predictions_still_empty":frozen["predictions"]=={},
      "correct_operator_semantics":{
         "T_last_alive_MeV":"last exported source sample at which native PBH alive is true, NOT integrator termination temperature",
         "i_last_alive":"native sampled event last PBH-alive index from first evaporation threshold crossing",
         "n_points":"number of exported source data points at T_SM<=30MeV after up to 20000 local interpolation nodes",
         "channels_not_statistically_independent":True,
         "T_or_index_correlation_NOT_solver_failure_proof":True
      },
      "source_actual_driver_control":{
          "control_original":"o22_1720 / authors physical hadron table",
          "control_103":"k22_1720 / authors physical hadron table",
          "original_G_DRIVER_gate_tests_only_single_float_Y":True,
          "all_nine_available_deterministic_summary_columns_string_exact":all(all_det_match.values()),
          "which_nine_columns_match":all_det_match,
          "source_run_id_and_wall_seconds_differ_expected":True,
          "whole_native_trajectory_bitwise_identity_not_checked_by_this_gate":True,
          "mutant_in_memory_Tlast_changed_but_original_Y_only_gate_would_pass":True,
          "mutation_is_synthetic_not_in_actual_original_outputs":True
      },
      "n_actual_native_z_no_base_beta_nodes":58,
      "n_actual_native_z_beta_1e_minus30_bases":2,
      "n_original_control_physical_table_083_base_source":2,
      "groups":groups,
      "verdict":"Both anomalous z base rows fall outside all 7 and all 13 distinct-beta low-input intervals in 4 jointly-observed response/trajectory channels per j; branch-specific cause unresolved. Owner GATE_FAIL_NO_LABEL preserved. G_DRIVER currently certifies only Y scalar though current nine summary deterministic columns also match; cannot infer full trajectory bitwise identity or validity of scaled source branch.",
      "no_native_physics_executed":True,
      "no_physical_pbh_bound":True,
      "no_canon":True,
      "no_exec_sign":True
    }
    Path(dst).write_text(json.dumps(answer,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"source_native_beta_nodes":58,
          "source_exact_nine_control_fields":all(all_det_match.values()),
          "frozen_gate":frozen["labels"]["status"],
          "seven_pool_outside":{j:groups[j]["reference_pools"]["-18.5"]["coanomalous_channels"] for j in groups},
          "thirteen_pool_outside":{j:groups[j]["reference_pools"]["-17.0"]["coanomalous_channels"] for j in groups},
          "base_T_gap_vs_lowmean":{j:groups[j]["reference_pools"]["-18.5"]["fields"]["T_last_alive_MeV"]["base_difference_from_pool_mean"] for j in groups}},indent=2))

if __name__=="__main__":
    assert len(sys.argv)==2,"Usage: python3 rot016.py result.json"
    main(sys.argv[1])
