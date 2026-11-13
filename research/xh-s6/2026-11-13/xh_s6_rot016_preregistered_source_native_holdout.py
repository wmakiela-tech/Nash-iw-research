#!/usr/bin/env python3
"""XH-S6 ROT016 preregistered source-native RNN out-of-sample preference gap test.

The preregistered science claims may FAIL and this code still exits 0 if source
and computation integrity checks pass; never conceal falsifier in CI status.
Uses original frozen author's Task and PsychRNN via SHA-locked ROT013/ROT009 wrappers.
"""
from __future__ import annotations
import argparse,csv,hashlib,importlib.util,json,sys,time,math
from pathlib import Path
import numpy as np
AUTHOR="7889a81e298c01532a313e02971c11dbc9db8eb0"
ROT013_BLOB="0cd2658ed6687380935ab5d8d6f2d9c4b591b0c8"
PREREG_BLOB="932b70a33357b3895845fa23193f404f739d2ad1"
AMENDMENT_BLOB="874151c6be754f98949b254ffabfc0937606dd65"
ALLOWED=(5,10,15,20,25,30,35,40,45,50,55,60,65)
BASE_SEED=202611160000
def blob(b):
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def import_rot013(path):
 b=path.read_bytes()
 if blob(b)!=ROT013_BLOB:raise RuntimeError("FROZEN_ROT013_BLOB_FAIL")
 spec=importlib.util.spec_from_file_location("xh_rot013_pinned",path)
 m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
 if m.AUTHOR!=AUTHOR:raise RuntimeError("ORIGINAL_AUTHOR_SOURCE_DRIFT")
 return m
def source_seed_key(cfg,k):
 return BASE_SEED+500003*int(cfg["module"]=="DLPFC")+3109*cfg["unit"]+1009*k
def seed_for(cfg,k):
 seed=source_seed_key(cfg,k) % (2**32)
 if not 0<=seed+171717<2**32:raise RuntimeError("LEGACY_NUMPY_SEED_RANGE_FAIL")
 return seed
def annulus_count(choices,angle,dist):
 return sum(1 for choice in choices if dist(choice,angle) in ALLOWED)
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--original-source-dir",type=Path,required=True)
 a.add_argument("--rot009-source",type=Path,required=True)
 a.add_argument("--rot013-source",type=Path,required=True)
 a.add_argument("--preregister",type=Path,required=True)
 a.add_argument("--amendment",type=Path,required=True)
 a.add_argument("--out",type=Path,required=True)
 a.add_argument("--seed-blocks",type=int,default=24)
 args=a.parse_args()
 if args.seed_blocks!=24:raise RuntimeError("PREREG_REQUIRES_24_BLOCKS")
 if blob(args.preregister.read_bytes())!=PREREG_BLOB:
  raise RuntimeError("PREREG_BYTE_IDENTITY_FAIL")
 if blob(args.amendment.read_bytes())!=AMENDMENT_BLOB:
  raise RuntimeError("SEED_AMENDMENT_BYTE_IDENTITY_FAIL")
 original=args.original_source_dir.resolve()
 src=import_rot013(args.rot013_source)
 wrapper=src.get_original_wrapper(args.rot009_source)
 for k,pin in wrapper.PINS.items():
  if k.endswith(".py"):wrapper.assert_original(original/k,pin)
 mt=wrapper.load_model(original/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
 dp=wrapper.load_model(original/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
 cfgs=src.original_unit_cases(original/"generate_microstim_testdata.py")
 sys.path.insert(0,str(original))
 import DotsTasks
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 t0=time.monotonic()
 args.out.mkdir(parents=True,exist_ok=True)
 rows=0;matched=0;repeat=0;all_units=[];all_fake=[]
 row_fields=["module","unit","strength","preferred_deg","reward_deg","seed_block","seed","seed_key","shown_deg",
  "ring_ms","dots_ms","sham_deg","stim_deg","sham_preference_distance_deg",
  "stim_preference_distance_deg","stim_in_frozen_gap_5_to_65","sham_in_frozen_gap_5_to_65",
  "stim_exact_preference","sham_exact_preference","changed","sham_margin","score_sup_delta","invariance_cert"]
 with (args.out/"xh_s6_rot016_new_original_model_17280_source_pairs.csv").open("w",newline="",encoding="utf8") as f:
  wr=csv.DictWriter(f,fieldnames=row_fields);wr.writeheader()
  for c in cfgs:
   mod=c["module"];pref=c["preferred_deg"];stimchoices=[];shamchoices=[];per_block=[]
   for k in range(24):
    seed=seed_for(c,k)
    sham=wrapper.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,mt,dp,c,seed,0)
    stim=wrapper.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,mt,dp,c,seed,c["strength"])
    if sham["times"]!=stim["times"] or sham["params_digest"]!=stim["params_digest"] or sham["rng_digest"]!=stim["rng_digest"]:
     raise RuntimeError("PAIRED_SOURCE_NOISE_ONSET_MISMATCH")
    matched+=1
    if k==0:
     dup=wrapper.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,mt,dp,c,seed,0)
     if not np.array_equal(sham["scores"],dup["scores"]):
      raise RuntimeError("SHAM_DUP_NOT_BITWISE")
     repeat+=1
    sc=[];bc=[]
    for i in range(72):
     b=int(sham["choice"][i]);s=int(stim["choice"][i]);shown=5*i
     if not(b in range(0,360,5) and s in range(0,360,5)):
      raise RuntimeError("OUTPUT_BIN_NOT_SOURCE_GRID")
     gap=int(src.dist(s,pref) in ALLOWED);shamgap=int(src.dist(b,pref) in ALLOWED)
     margin=float(wrapper.margin(sham["scores"][i]))
     sup=float(np.max(np.abs(sham["scores"][i]-stim["scores"][i])))
     cert=int(sup<margin/2)
     if b!=s and cert:raise RuntimeError("ARGMAX_STABILITY_IDENTITY_FAIL")
     wr.writerow(dict(module=mod,unit=c["unit"],strength=c["strength"],
       preferred_deg=pref,reward_deg=c["reward_deg"],seed_block=k,seed=seed,seed_key=source_seed_key(c,k),
       shown_deg=shown,ring_ms=sham["times"][i][0],dots_ms=sham["times"][i][1],
       sham_deg=b,stim_deg=s,sham_preference_distance_deg=src.dist(b,pref),
       stim_preference_distance_deg=src.dist(s,pref),stim_in_frozen_gap_5_to_65=gap,
       sham_in_frozen_gap_5_to_65=shamgap,stim_exact_preference=int(s==pref),
       sham_exact_preference=int(b==pref),changed=int(s!=b),
       sham_margin=format(margin,".17g"),score_sup_delta=format(sup,".17g"),invariance_cert=cert))
     rows+=1;sc.append(s);bc.append(b)
    per_block.append({"seed_block":k,
      "stim_gap_count":annulus_count(sc,pref,src.dist),
      "sham_gap_count":annulus_count(bc,pref,src.dist),
      "stim_capture_count":sum(x==pref for x in sc),
      "sham_capture_count":sum(x==pref for x in bc),
      "stim_changed_count":sum(x!=y for x,y in zip(sc,bc)),
      "stim_choices":sc,"sham_choices":bc})
    stimchoices+=sc;shamchoices+=bc
   tab=[]
   for l in range(0,360,5):
    count=annulus_count(stimchoices,l,src.dist)
    fake={"module":mod,"unit":c["unit"],"source_true_preference_deg":pref,
         "candidate_label_deg":l,"true_label":int(l==pref),
         "stim_gap_5_to_65_count":count,
         "sham_gap_5_to_65_count":annulus_count(shamchoices,l,src.dist)}
    tab.append(fake);all_fake.append(fake)
   zeros=[x["candidate_label_deg"] for x in tab if x["stim_gap_5_to_65_count"]==0]
   wrong=[x["stim_gap_5_to_65_count"] for x in tab if x["candidate_label_deg"]!=pref]
   result={"module":mod,"unit":c["unit"],"original_strength":c["strength"],"preference_deg":pref,
     "n_source_paired_conditions":len(stimchoices),"seed_blocks":24,
     "true_stim_gap_5_to_65_count":annulus_count(stimchoices,pref,src.dist),
     "true_sham_gap_5_to_65_count":annulus_count(shamchoices,pref,src.dist),
     "true_stim_exact_preference_count":sum(x==pref for x in stimchoices),
     "true_sham_exact_preference_count":sum(x==pref for x in shamchoices),
     "stim_changed_count":sum(a!=b for a,b in zip(stimchoices,shamchoices)),
     "all_72_label_gap_zero_labels":zeros,
     "min_wrong_label_gap_count":min(wrong),
     "preregister_frozen_dlPFC_gap_zero":(annulus_count(stimchoices,pref,src.dist)==0) if mod=="DLPFC" else None,
     "preregister_dlPFC_unique_zero_true_P":(zeros==[pref]) if mod=="DLPFC" else None,
     "preregister_MT_no_zero_any_label":(len(zeros)==0) if mod=="MT" else None,
     "per_seed_block_counts":[{k:v for k,v in b.items() if k not in ("stim_choices","sham_choices")} for b in per_block]}
   all_units.append(result)
   print("UNIT_RESULT "+json.dumps({k:v for k,v in result.items() if k!="per_seed_block_counts"},sort_keys=True),flush=True)
 if rows!=17280 or matched!=240 or repeat!=10:raise RuntimeError("GRID_OR_SOURCE_STREAM_COUNT_FAIL")
 with (args.out/"xh_s6_rot016_720_candidate_label_holdout.csv").open("w",newline="",encoding="utf8") as f:
  wr=csv.DictWriter(f,fieldnames=list(all_fake[0]));wr.writeheader();wr.writerows(all_fake)
 outcome={"artifact_id":"IW_XH_S6_ROT016_FROZEN_GAP_PROSPECTIVE_AUTHOR_MODEL_REPLAY_001_20261113",
 "status":"EXECUTION_INTEGRITY_PASS","author_repository_commit":AUTHOR,
 "prereg_git_blob":PREREG_BLOB,"seed_pre_data_amendment_blob":AMENDMENT_BLOB,"rot013_source_blob":ROT013_BLOB,
 "original_author_source_units":cfgs,"seed_formula":"key=202611160000+500003*int(module==DLPFC)+3109*unit+1009*block; source_seed=key modulo 2**32; 0<=block<24",
 "seed_blocks":24,"source_paired_trials":rows,"source_original_model_arm_trials":2*rows,
 "matched_source_RNG_and_onset_checks":matched,"sham_source_bitwise_repetition_checks":repeat,
 "frozen_gap_degree_bins":ALLOWED,"original_units_results":all_units,
 "dlPFC_primary_units_pass":sum(x["preregister_frozen_dlPFC_gap_zero"] for x in all_units if x["module"]=="DLPFC"),
 "dlPFC_secondary_unique_true_P_units_pass":sum(x["preregister_dlPFC_unique_zero_true_P"] for x in all_units if x["module"]=="DLPFC"),
 "MT_negative_no_zero_any_units_pass":sum(x["preregister_MT_no_zero_any_label"] for x in all_units if x["module"]=="MT"),
 "scientific_falsification_is_not_integrity_error":True,
 "original_author_250_per_direction":"NOT_RUN",
 "monkey_experiments":"NOT_ACCESSED",
 "new_models":"NONE, same pretrained author RNN weights",
 "no_novelty":True,"no_canon":True,"no_exec_sign":True,
 "elapsed_s":time.monotonic()-t0}
 (args.out/"xh_s6_rot016_new_original_model_holdout_actual_summary.json").write_text(json.dumps(outcome,indent=2,sort_keys=True)+"\n",encoding="utf8")
 print("ROT016_FINAL_JSON_BEGIN")
 print(json.dumps({k:v for k,v in outcome.items() if k!="original_units_results"}|{"original_units_results":[{k:v for k,v in u.items() if k!="per_seed_block_counts"} for u in all_units]},sort_keys=True))
 print("ROT016_FINAL_JSON_END",flush=True)
if __name__=="__main__":main()
