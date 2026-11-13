#!/usr/bin/env python3
"""XH-S6 ROT017 — preregistered 250 per angle, source-author native two unit audit.

Authors' exact frozen Task and vendored PsychRNN and original trained weights;
ROT013 source-unit AST parser; ROT009 original simulator wrapper, SHA pinned.
NOT the author original single 18,000-batch draw. Same author's source model
parameters, 250 distinct 72-angle batches/unit, paired common noise.
A counterexample is source science, not program failure.
"""
from __future__ import annotations
import argparse, csv, hashlib, importlib.util, json, sys, time
from pathlib import Path
import numpy as np

AUTHOR_COMMIT="7889a81e298c01532a313e02971c11dbc9db8eb0"
ROT013_BLOB="0cd2658ed6687380935ab5d8d6f2d9c4b591b0c8"
PREREG_BLOB="72a22b3b90831ff29674a8273068b24f97f5416d"
START_SEED=1800000000
OFFSETS=tuple(range(5,66,5))
UNITS=(25,53)
BLOCKS=250
ANGLES=72

def gitblob(b):
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def load_rot013(path):
 if gitblob(path.read_bytes())!=ROT013_BLOB:raise RuntimeError("FROZEN_ROT013_SOURCE_BLOB_MISMATCH")
 spec=importlib.util.spec_from_file_location("xh_s6_rot013_frozen",path)
 m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
 if m.AUTHOR!=AUTHOR_COMMIT:raise RuntimeError("SOURCE_AUTHOR_REVISION_MISMATCH")
 return m
def seed_at(unit,k):
 seed=START_SEED+300071*unit+1009*k
 if not 0<=seed+171717<2**32:raise RuntimeError("LEGACY_SOURCE_SEED_RANGE_FAIL")
 return seed
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--source-root",type=Path,required=True)
 parser.add_argument("--rot009",type=Path,required=True)
 parser.add_argument("--rot013",type=Path,required=True)
 parser.add_argument("--prereg",type=Path,required=True)
 parser.add_argument("--out",type=Path,required=True)
 args=parser.parse_args()
 if gitblob(args.prereg.read_bytes())!=PREREG_BLOB:raise RuntimeError("ROT017_PREREG_NOT_THE_PINNED_BLOB")
 src=load_rot013(args.rot013)
 original=args.source_root.resolve()
 original_wrapper=src.get_original_wrapper(args.rot009)
 for k,v in original_wrapper.PINS.items():
  if k.endswith(".py"):original_wrapper.assert_original(original/k,v)
 mt=original_wrapper.load_model(original/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
 dp=original_wrapper.load_model(original/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
 allcfg=src.original_unit_cases(original/"generate_microstim_testdata.py")
 units=[c for c in allcfg if c["module"]=="DLPFC" and c["unit"] in UNITS]
 if len(units)!=2 or sorted(c["unit"] for c in units)!=list(UNITS):
  raise RuntimeError("ORIGINAL_AUTHOR_TWO_UNIT_SELECTION_FAIL")
 for c in units:
  if c["strength"]!=45 or (c["unit"],c["preferred_deg"],c["reward_deg"]) not in (
   (25,160,340),(53,295,115)):
   raise RuntimeError("ORIGINAL_AUTHOR_UNIT_STRENGTH_PREFERENCE_DRIFT")
 sys.path.insert(0,str(original))
 import DotsTasks
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 args.out.mkdir(parents=True,exist_ok=True)
 now=time.monotonic()
 rows=0;matched=0;repeats=0;all_summary=[];source_boot_counts=[]
 fields=["module","unit","strength","pref_deg","reward_deg","seed_block","source_seed","shown_deg",
  "ring_ms","dots_ms","sham_choice_deg","stim_choice_deg","sham_distance_to_pref","stim_distance_to_pref",
  "gap5_65","gap5_60","boundary65","sham_gap5_65","stim_exact_pref","sham_exact_pref",
  "choice_changed","baseline_top2_margin","final_scores_sup_delta","argmax_preservation_certificate",
  "source_target_delta"]
 outfile=args.out/"xh_s6_rot017_author_native_dlpfc25_53_250x72_paired_rows.csv"
 with outfile.open("w",newline="",encoding="utf8") as f:
  wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader()
  for cfg in units:
   pref=cfg["preferred_deg"];unit=cfg["unit"]
   stm_all=[];shm_all=[];stim_by_shown=[0]*72;gap_by_shown=[0]*72
   counts={k:0 for k in ("gap5_65","gap5_60","boundary65","sham_gap5_65",
    "stim_exact_pref","sham_exact_pref","choice_changed","argmax_preservation_certificate")}
   distance_hist={str(k):0 for k in range(0,181,5)}
   boundary_witnesses=[]
   blockrows=[];old_sham_choices=None
   null_sham_pair_changed=0
   for block in range(BLOCKS):
    seed=seed_at(unit,block)
    a=original_wrapper.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,
      mt,dp,cfg,seed,0)
    b=original_wrapper.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,
      mt,dp,cfg,seed,cfg["strength"])
    if a["times"]!=b["times"] or a["params_digest"]!=b["params_digest"] or a["rng_digest"]!=b["rng_digest"]:
     raise RuntimeError("ORIGINAL_SOURCE_RANDOM_INPUT_ONSET_PAIR_MISMATCH")
    matched+=1
    if block==0:
     check=original_wrapper.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,
       mt,dp,cfg,seed,0)
     if not np.array_equal(a["scores"],check["scores"]):raise RuntimeError("ORIGINAL_SOURCE_SHAM_REPLAY_NOT_BITWISE")
     repeats+=1
    chosen_a=[int(x) for x in a["choice"]];chosen_b=[int(x) for x in b["choice"]]
    if old_sham_choices is not None:
     null_sham_pair_changed+=sum(x!=y for x,y in zip(chosen_a,old_sham_choices))
    old_sham_choices=chosen_a
    shm_all+=chosen_a;stm_all+=chosen_b
    blockcounts={k:0 for k in counts}
    for i,(sham,stim) in enumerate(zip(chosen_a,chosen_b)):
     shown=i*5
     if (sham%5 or stim%5 or not (0<=sham<360 and 0<=stim<360)):
      raise RuntimeError("ORIGINAL_OUTPUT_ANGLE_GRID_FAIL")
     d0=src.dist(sham,pref);d=src.dist(stim,pref)
     gap=int(5<=d<=65);interior=int(5<=d<=60);boundary=int(d==65)
     margin=float(original_wrapper.margin(a["scores"][i]))
     sup=float(np.max(np.abs(a["scores"][i]-b["scores"][i])))
     cert=int(sup<margin/2.)
     if sham!=stim and cert:raise RuntimeError("ELEMENTARY_ARGMAX_MARGIN_FALSE")
     target_delta=src.target_reward(stim,shown,cfg["reward_deg"])-src.target_reward(sham,shown,cfg["reward_deg"])
     row=dict(module="DLPFC",unit=unit,strength=cfg["strength"],pref_deg=pref,
      reward_deg=cfg["reward_deg"],seed_block=block,source_seed=seed,shown_deg=shown,
      ring_ms=a["times"][i][0],dots_ms=a["times"][i][1],
      sham_choice_deg=sham,stim_choice_deg=stim,sham_distance_to_pref=d0,
      stim_distance_to_pref=d,gap5_65=gap,gap5_60=interior,boundary65=boundary,
      sham_gap5_65=int(5<=d0<=65),stim_exact_pref=int(stim==pref),
      sham_exact_pref=int(sham==pref),choice_changed=int(sham!=stim),
      baseline_top2_margin=format(margin,".17g"),
      final_scores_sup_delta=format(sup,".17g"),argmax_preservation_certificate=cert,
      source_target_delta=format(target_delta,".17g"))
     wr.writerow(row);rows+=1
     stim_by_shown[i]+=1;gap_by_shown[i]+=gap
     distance_hist[str(d)]+=1
     for key in counts:
      blockcounts[key]+=int(row[key])
      counts[key]+=int(row[key])
     if gap and len(boundary_witnesses)<500:
      boundary_witnesses.append({k:row[k] for k in ("unit","seed_block","source_seed","shown_deg",
        "stim_choice_deg","sham_choice_deg","stim_distance_to_pref","ring_ms","dots_ms","gap5_60","boundary65")})
    blockrows.append(dict(unit=unit,seed_block=block,source_seed=seed,
      **{key:blockcounts[key] for key in counts}))
    if (block+1)%50==0:
     print(f"PROGRESS unit={unit} blocks={block+1}/{BLOCKS} source_pairs={rows}",flush=True)
   candidates=[]
   for label in range(0,360,5):
    cnt=sum(1 for choice in stm_all if 5<=src.dist(choice,label)<=65)
    candidates.append(dict(unit=unit,true_pref=pref,candidate_label_deg=label,
      matches_source_pref=int(label==pref),stim_gap5_65_count=cnt,
      sham_gap5_65_count=sum(1 for choice in shm_all if 5<=src.dist(choice,label)<=65)))
   min_cnt=min(v["stim_gap5_65_count"] for v in candidates)
   min_labels=[v["candidate_label_deg"] for v in candidates if v["stim_gap5_65_count"]==min_cnt]
   all_summary.append(dict(module="DLPFC",source_unit=unit,source_preference=pref,
    source_strength=cfg["strength"],source_reward_center=cfg["reward_deg"],
    seeded_blocks=BLOCKS,shown_directions=ANGLES,
    source_model_pairs=len(stm_all),source_model_arms=2*len(stm_all),
    observed_counts=counts,observed_stim_preference_distance_histogram=distance_hist,
    by_shown_gap_5to65=[{"shown_deg":i*5,"n":stim_by_shown[i],"events":gap_by_shown[i]} for i in range(72)],
    original_true_P_label_gap=counts["gap5_65"],minimal_gap_count_among_all_72_labels=min_cnt,
    all_candidate_label_minima=min_labels,
    original_P_unique_minimum=(min_labels==[pref]),original_P_zero=(counts["gap5_65"]==0),
    consecutive_independent_sham_pairs=(BLOCKS-1)*72,
    consecutive_sham_choice_mismatch=null_sham_pair_changed,
    observed_source_gap_witnesses=boundary_witnesses))
   source_boot_counts+=blockrows
   if unit==25: unit25_candidates=candidates
   else: unit53_candidates=candidates
 if rows!=2*250*72 or matched!=500 or repeats!=2:raise RuntimeError("ORIGINAL_GRID_SIZE_FAIL")
 for path,candidates in [
   (args.out/"xh_s6_rot017_dlpfc25_72_candidate_labels.csv",unit25_candidates),
   (args.out/"xh_s6_rot017_dlpfc53_72_candidate_labels.csv",unit53_candidates)]:
  with path.open("w",newline="",encoding="utf8") as f:
   w=csv.DictWriter(f,fieldnames=list(candidates[0]));w.writeheader();w.writerows(candidates)
 with (args.out/"xh_s6_rot017_500_seed_block_profiles.csv").open("w",newline="",encoding="utf8") as f:
  w=csv.DictWriter(f,fieldnames=list(source_boot_counts[0]));w.writeheader();w.writerows(source_boot_counts)
 summary=dict(artifact_id="IW_XH_S6_ROT017_ORIGINAL_AUTHOR_DLPFC25_53_250_REPS_DIRECTION_RATE_GATE_001_20261113",
  actual_execution_status="PASS",source_author_commit=AUTHOR_COMMIT,
  source_preregister_git_blob=PREREG_BLOB,rot013_source_git_blob=ROT013_BLOB,
  seed_formula="1800000000 + 300071*unit + 1009*block, blocks0..249",
  seed_blocks_per_unit=250,original_shown_directions_per_block=72,
  original_source_model_paired_rows=rows,original_source_model_arm_trials=2*rows,
  sham_stim_identical_source_rng_onset_checks=matched,bitwise_sham_duplicate_checks=repeats,
  same_72x250_nominal_count_as_author_generator=True,
  identical_author_generator_Nbatch18000_rng_protocol=False,
  author_full_10unit_paper_trial_generator_not_executed=True,
  source_units=all_summary,scientific_falsification_must_not_fail_program=True,
  no_monkey_data=True,no_novelty=True,no_canon=True,no_exec_sign=True,
  elapsed_s=time.monotonic()-now)
 (args.out/"xh_s6_rot017_author_native_250_per_angle_actual_summary.json").write_text(
  json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf8")
 print("ROT017_FINAL_JSON_BEGIN")
 print(json.dumps({**{k:v for k,v in summary.items() if k!="source_units"},
  "source_units":[{k:v for k,v in u.items() if k not in ("by_shown_gap_5to65","observed_source_gap_witnesses","observed_stim_preference_distance_histogram")} for u in all_summary]},sort_keys=True))
 print("ROT017_FINAL_JSON_END",flush=True)
if __name__=="__main__":main()
