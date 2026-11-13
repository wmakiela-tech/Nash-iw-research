#!/usr/bin/env python3
"""XH-S6 ROT013 — source-native ten-original-units falsifier.
Execute immutable original author DotsTasks/MT+dlPFC PsychRNN simulators and
trained weights. The author source generator metadata (five units per area)
is parsed, not manually retyped. Same source noise/onset within stim/sham,
reward_rel=180 (author-original generator). 16 seed-blocks per source unit,
72 shown bins per block, 11,520 paired model inputs / 23,040 arm trials.
Not original author 250-per-direction full experiment nor monkey data.
"""
from __future__ import annotations
import argparse, ast, csv, hashlib, importlib.util, json, math, sys, time
from pathlib import Path
import numpy as np
AUTHOR="7889a81e298c01532a313e02971c11dbc9db8eb0"
ROT009_BLOB="054299b6b0f0c0def7cfa6b3600d6f56665375ce"
SOURCE_GENERATOR_BLOB="e7a6666e0b600ea49bab9755d302c78110ba9bc4"

def blob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def get_original_wrapper(path):
 raw=path.read_bytes()
 if blob(raw)!=ROT009_BLOB:raise RuntimeError("ORIGINAL_XH_ROT009_SOURCE_MISMATCH")
 spec=importlib.util.spec_from_file_location("rot009_original_locked",path)
 m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m
 spec.loader.exec_module(m)
 if m.AUTHOR_COMMIT!=AUTHOR:raise RuntimeError("SOURCE_COMMIT_DRIFT")
 return m
def original_unit_cases(path):
 raw=path.read_bytes()
 if blob(raw)!=SOURCE_GENERATOR_BLOB:raise RuntimeError("AUTHOR_GENERATOR_SHA_DRIFT")
 tree=ast.parse(raw.decode("utf8"))
 vals={}
 needed=("MT_mstim_units_","MT_mstim_angles_","MT_mstim_strengths_",
         "DLPFC_mstim_units_","DLPFC_mstim_angles_","DLPFC_mstim_strengths_","reward_rel")
 for n in ast.walk(tree):
  if isinstance(n,ast.Assign):
   for target in n.targets:
    if isinstance(target,ast.Name) and target.id in needed:
     vals[target.id]=ast.literal_eval(n.value)
 if set(vals)!=set(needed):raise RuntimeError("ORIGINAL_AUTHOR_LIST_METADATA_MISSING")
 if vals["reward_rel"]!=180:raise RuntimeError("ORIGINAL_REWARD_OFFSET_CHANGED")
 configs=[]
 for module in ("MT","DLPFC"):
  units,angles,strengths=[vals[f"{module}_mstim_{s}_"] for s in ("units","angles","strengths")]
  if len(units)!=10 or len(angles)!=10 or len(strengths)!=10:raise RuntimeError("AUTHOR_TEN_CONDITIONS_EXPECTED")
  for k in range(0,10,2):
   if (units[k]!=units[k+1] or angles[k]!=angles[k+1]
       or strengths[k]!=0 or strengths[k+1]<=0):raise RuntimeError("AUTHOR_SHAM_STIM_PAIR_BAD")
   pref=int(angles[k])
   if pref%5:raise RuntimeError("SOURCE_PREFERENCE_NOT_BIN")
   configs.append({"module":module,"unit":int(units[k]),"preferred_deg":pref,
     "reward_deg":(pref+180)%360,"strength":int(strengths[k+1])})
 if len(configs)!=10 or len({(z["module"],z["unit"]) for z in configs})!=10:raise RuntimeError("AUTHOR_UNIT_SET_NOT_UNIQUE")
 return configs
def dist(a,b):return abs((int(a)-int(b)+180)%360-180)
def target_reward(choice,shown,good):
 d=dist(choice,shown)
 if d>45:return 0.
 return (3.5+1.5*math.cos(math.radians(1.8*d)))*(1+.75*math.cos(math.radians(dist(choice,good))))
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("--author-python-data-dir",type=Path,required=True)
 ap.add_argument("--rot009-source",type=Path,required=True)
 ap.add_argument("--output-dir",type=Path,required=True)
 ap.add_argument("--seed-blocks",type=int,default=16)
 args=ap.parse_args()
 if not 8<=args.seed_blocks<=20:raise RuntimeError("BOUNDED_BLOCKS_EXPECTED")
 x=get_original_wrapper(args.rot009_source)
 root=args.author_python_data_dir.resolve()
 for name,pin in x.PINS.items():
  if name.endswith(".py"):x.assert_original(root/name,pin)
 weights_mt=x.load_model(root/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
 weights_dp=x.load_model(root/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
 cases=original_unit_cases(root/"generate_microstim_testdata.py")
 sys.path.insert(0,str(root))
 import DotsTasks
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 args.output_dir.mkdir(parents=True,exist_ok=True)
 outfile=args.output_dir/"xh_s6_rot013_author_10units_16blocks_11520_source_pairs.csv"
 fields=["module","unit","preferred_deg","strength","reward_deg","seed_block","seed",
  "shown_deg","ring_ms","dots_ms","sham_choice_deg","stim_choice_deg","sham_to_pref_deg",
  "stim_to_pref_deg","pref_distance_delta_deg","choice_changed","moved_closer","moved_farther",
  "antipodal_sham_pref","strict_unique_arc_eligible","strict_unique_arc_interior",
  "exact_pref_capture","sham_exact_pref","exact_endpoint","near_endpoint_10deg",
  "sham_source_target","stim_source_target","source_target_delta",
  "sham_margin","sup_score_change","argmax_preserve_certified"]
 start=time.monotonic()
 reports=[];all_rows=0;stream_checks=0;sham_repeat_checks=0
 with outfile.open("w",newline="",encoding="utf8") as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
  for cfg in cases:
   n=args.seed_blocks*72
   tally={c:0 for c in ["choice_changed","moved_closer","moved_farther","antipodal_sham_pref",
     "strict_unique_arc_eligible","strict_unique_arc_interior","exact_pref_capture","sham_exact_pref",
     "exact_endpoint","near_endpoint_10deg","argmax_preserve_certified"]}
   dd=0.;dtarg=0.;shams=[];block_rates=[]
   for k in range(args.seed_blocks):
    # Disjoint deterministic pseudorandom streams across original source units/blocks
    seed=2026111300+500003*(cfg["module"]=="DLPFC")+3109*cfg["unit"]+1009*k
    sham=x.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,
               weights_mt,weights_dp,cfg,seed,0)
    stim=x.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,
               weights_mt,weights_dp,cfg,seed,cfg["strength"])
    if (sham["times"]!=stim["times"] or
       sham["params_digest"]!=stim["params_digest"] or
       sham["rng_digest"]!=stim["rng_digest"]):
     raise RuntimeError("PAIR_NOISE_OR_ONSET_NOT_MATCHED")
    stream_checks+=1
    if k==0:
     repeat=x.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,
                     weights_mt,weights_dp,cfg,seed,0)
     if not np.array_equal(sham["scores"],repeat["scores"]):
      raise RuntimeError("SOURCE_SHAM_BITWISE_REPEAT_FAILURE")
     sham_repeat_checks+=1
    shams.append(tuple(int(v) for v in sham["choice"]))
    bchanged=0;bgeodesic=0
    for i in range(72):
     shown=5*i;prev=int(sham["choice"][i]);nextv=int(stim["choice"][i])
     pref=cfg["preferred_deg"];d0=dist(prev,pref);d1=dist(nextv,pref);ds=dist(prev,nextv)
     unique=0<d0<180
     mid=unique and 0<ds<d0 and ds+d1==d0
     base_target=target_reward(prev,shown,cfg["reward_deg"])
     stim_target=target_reward(nextv,shown,cfg["reward_deg"])
     margin=x.margin(sham["scores"][i])
     sup=float(np.max(np.abs(stim["scores"][i]-sham["scores"][i])))
     cert=sup<margin/2
     if prev!=nextv and cert:raise RuntimeError("ARGMAX_CERTIFICATE_VIOLATION")
     row={"module":cfg["module"],"unit":cfg["unit"],"preferred_deg":pref,
      "strength":cfg["strength"],"reward_deg":cfg["reward_deg"],
      "seed_block":k,"seed":seed,"shown_deg":shown,
      "ring_ms":sham["times"][i][0],"dots_ms":sham["times"][i][1],
      "sham_choice_deg":prev,"stim_choice_deg":nextv,"sham_to_pref_deg":d0,
      "stim_to_pref_deg":d1,"pref_distance_delta_deg":d1-d0,"choice_changed":int(prev!=nextv),
      "moved_closer":int(d1<d0),"moved_farther":int(d1>d0),
      "antipodal_sham_pref":int(d0==180),"strict_unique_arc_eligible":int(unique),
      "strict_unique_arc_interior":int(mid),"exact_pref_capture":int(nextv==pref),
      "sham_exact_pref":int(prev==pref),"exact_endpoint":int(nextv in (prev,pref)),
      "near_endpoint_10deg":int(ds<=10 or d1<=10),
      "sham_source_target":format(base_target,".17g"),
      "stim_source_target":format(stim_target,".17g"),
      "source_target_delta":format(stim_target-base_target,".17g"),
      "sham_margin":format(margin,".17g"),
      "sup_score_change":format(sup,".17g"),"argmax_preserve_certified":int(cert)}
     for c in tally:tally[c]+=row[c]
     dd+=d1-d0;dtarg+=stim_target-base_target
     bchanged+=row["choice_changed"];bgeodesic+=row["strict_unique_arc_interior"]
     w.writerow(row);all_rows+=1
    block_rates.append({"seed_block":k,"changed":bchanged,"geodesic":bgeodesic})
   # Distinct-seed SHAM NULL: compare each pair of successive independent seed blocks at same shown
   null_changed=sum(sum(a!=b for a,b in zip(shams[k],shams[k+1])) for k in range(args.seed_blocks-1))
   null_n=(args.seed_blocks-1)*72
   rate=tally["strict_unique_arc_interior"]/tally["strict_unique_arc_eligible"] if tally["strict_unique_arc_eligible"] else None
   report={"module":cfg["module"],"unit":cfg["unit"],"strength":cfg["strength"],
    "preferred_deg":cfg["preferred_deg"],"reward_deg":cfg["reward_deg"],
    "n":n,"counts":tally,"mean_pref_distance_delta_deg":dd/n,
    "mean_source_training_target_delta":dtarg/n,
    "strict_unique_geodesic_interior_fraction":rate,
    "exact_endpoint_fraction":tally["exact_endpoint"]/n,
    "exact_preference_capture_fraction":tally["exact_pref_capture"]/n,
    "independent_seed_sham_null_choice_mismatch_n":null_changed,
    "independent_seed_sham_null_pairs":null_n,
    "source_unit_falsification_thresholds":{
       "MT_strict_geodesic_majority":(rate>0.5) if cfg["module"]=="MT" else None,
       "DLPFC_exact_endpoint_majority":(tally["exact_endpoint"]>n/2) if cfg["module"]=="DLPFC" else None
    },
    "block_records":block_rates}
   reports.append(report)
   print(f"UNIT_COMPLETED module={cfg['module']} unit={cfg['unit']} strength={cfg['strength']} n={n} strict_mid={tally['strict_unique_arc_interior']}/{tally['strict_unique_arc_eligible']} exact_endpoint={tally['exact_endpoint']}/{n} captured={tally['exact_pref_capture']}/{n}",flush=True)
 expected=10*args.seed_blocks*72
 if all_rows!=expected:raise RuntimeError(f"EXPECTED_ROWS_FAIL:{all_rows}!={expected}")
 summary={"artifact_id":"IW_XH_S6_ROT013_ALL_TEN_ORIGINAL_UNITS_SOURCE_GEOMETRY_FALSIFIER_001_20261113",
   "original_author_commit":AUTHOR,"original_source_generator_blob":SOURCE_GENERATOR_BLOB,
   "source_wrapper_blob":ROT009_BLOB,"source_unit_metadata_parsed_from_original_author_ast":cases,
   "original_reward_offset":180,"number_original_units":10,"blocks_per_unit":args.seed_blocks,
   "shown_angles_per_block":72,"paired_cases":all_rows,"source_model_arm_trials":all_rows*2,
   "matched_source_random_stream_checks":stream_checks,"sham_bitwise_repeat_checks":sham_repeat_checks,
   "argmax_theorem_no_violation":True,
   "source_unit_results":reports,
   "all_five_MT_strict_geodesic_majority":all(r["source_unit_falsification_thresholds"]["MT_strict_geodesic_majority"] for r in reports if r["module"]=="MT"),
   "all_five_DLPFC_exact_endpoint_majority":all(r["source_unit_falsification_thresholds"]["DLPFC_exact_endpoint_majority"] for r in reports if r["module"]=="DLPFC"),
   "scope":"10 SOURCE-selected model units at original source strength reward_rel 180, native source code/noise, 16 paired common-RNG seed blocks; no monkey data, original per-direction 250 trials NOT RUN",
   "elapsed_s":time.monotonic()-start,"no_novelty":True,"no_canon":True,"no_exec_sign":True,
   "status":"SOURCE_EXECUTED_PASS_FALSIFIERS_MAY_PASS_OR_FAIL"}
 outfile_json=args.output_dir/"xh_s6_rot013_10unit_native_source_runner_summary.json"
 outfile_json.write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf8")
 print("ROT013_FINAL_JSON_BEGIN")
 print(json.dumps({k:v for k,v in summary.items() if k!="source_unit_results"}|{"source_unit_results":[{k:v for k,v in r.items() if k!="block_records"} for r in reports]},sort_keys=True))
 print("ROT013_FINAL_JSON_END",flush=True)
if __name__=="__main__":main()
