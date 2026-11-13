#!/usr/bin/env python3
"""XH-S6 ROT019: original Task stochastic choice of motion direction + actual trained author RNN.

Same author source Task/PsychRNN frozen models and conditions, but 250 independent
72-trial matched sham/stimulation batches per selected unit, ORIGINAL source
test1ofEach=False random-angle rule. Distinct from author's one 18000 batch.
Scientific exceptions are data and NEVER treated as a program error.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,sys,time
from pathlib import Path
import numpy as np

AUTHOR="7889a81e298c01532a313e02971c11dbc9db8eb0"
PREREG_GIT_BLOB="143b2a5de2481abbc96c1f89a4a1478350c17674"
ROT009_GIT_BLOB="054299b6b0f0c0def7cfa6b3600d6f56665375ce"
ROT013_GIT_BLOB="0cd2658ed6687380935ab5d8d6f2d9c4b591b0c8"
SEED_BASE=2000000000
BLOCKS=250
N_PER_BLOCK=72
UNIT_IDS=(25,53)
GAP_BINS=tuple(range(5,66,5))

def gitblob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def fixed_seed(unit,block):
 seed=SEED_BASE+300071*unit+1009*block
 if not 0<=seed+171717<2**32:raise RuntimeError("ORIGINAL_SOURCE_NUMPY_SEED_LIMIT")
 return seed
def source_model_arm(dots,mt_type,dl_type,w,original_mt,original_dl,config,seed,strength):
 dots.rng=np.random.default_rng(seed)
 np.random.seed(seed+171717)
 mt={k:v.copy() for k,v in original_mt.items()}
 dp={k:v.copy() for k,v in original_dl.items()}
 assert config["module"]=="DLPFC"
 dp["W_in"][config["unit"],-1]=1.0
 pref=config["preferred_deg"]
 fix_shown=(np.arange(0,360,5)+pref)%360
 mt_task=dots.MT_broadInSharpOut_withR(N_batch=72,N_rec=150,in_noise=0.4,
    coh=[0.6],fix_shown=fix_shown,fix_reward=np.array([config["reward_deg"]]),
    M_mstim_strength=0,catchP=0.0)  # test1ofEach DEFAULT False as ORIGINAL AUTHOR
 if mt_task.test1ofEach is not False:raise RuntimeError("ORIGINAL_RANDOM_SCHEDULING_NOT_SELECTED")
 mt_sim=mt_type(weights=mt,params={"dt":10,"tau":100,"rec_noise":0.2})
 dp_task=dots.DLPFC_combined(N_batch=72,N_rec=150,in_noise=0.2,
    D_mstim_strength=strength,MT_task=mt_task,MT_simulator=mt_sim,MT_NdirOuts=72)
 inputs,_,_,params=dp_task.get_trial_batch()
 if inputs.shape!=(72,120,75):raise RuntimeError("ORIGINAL_SOURCE_INPUT_SHAPE")
 sim=dl_type(weights=dp,params={"dt":10,"tau":100,"rec_noise":0.2})
 output,_=sim.run_trials(inputs)
 scores=np.asarray(output[:,-1,:],dtype=np.float64)
 if scores.shape!=(72,72) or not np.isfinite(scores).all():raise RuntimeError("ORIGINAL_SOURCE_RNN_OUTPUT_SHAPE_OR_FINITE")
 return {"scores":scores,"choice":np.argmax(scores,axis=1)*5,
    "inputs":inputs,
    "shown":[int(z["shown_deg"]) for z in params],
    "reward":[int(z["good_deg"]) for z in params],
    "times":[(int(z["t_ring"]),int(z["t_dots"])) for z in params],
    "param_digest":w.trial_params_digest(params),
    "rng_digest":w.rand_digest(dots)}
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--original-source-dir",type=Path,required=True)
 a.add_argument("--rot009-source",type=Path,required=True)
 a.add_argument("--rot013-source",type=Path,required=True)
 a.add_argument("--preregister",type=Path,required=True)
 a.add_argument("--out",type=Path,required=True)
 args=a.parse_args()
 if gitblob(args.preregister.read_bytes())!=PREREG_GIT_BLOB:raise RuntimeError("PREREGISTRATION_IDENTITY_FAIL")
 if gitblob(args.rot009_source.read_bytes())!=ROT009_GIT_BLOB:raise RuntimeError("ROT009_FROZEN_SOURCE_IDENTITY_FAIL")
 if gitblob(args.rot013_source.read_bytes())!=ROT013_GIT_BLOB:raise RuntimeError("ROT013_FROZEN_SOURCE_IDENTITY_FAIL")
 root=args.original_source_dir.resolve()
 # Frozen independent source module loader (also verifies author generation source AST).
 import importlib.util
 spec=importlib.util.spec_from_file_location("rot019_pinned_rot013",args.rot013_source)
 m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
 w=m.get_original_wrapper(args.rot009_source)
 if w.AUTHOR_COMMIT!=AUTHOR:raise RuntimeError("AUTHOR_COMMIT_PIN_MISMATCH")
 for name,pin in w.PINS.items():
  if name.endswith(".py"):w.assert_original(root/name,pin)
 mt=w.load_model(root/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
 dp=w.load_model(root/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
 configs=[c for c in m.original_unit_cases(root/"generate_microstim_testdata.py")
          if c["module"]=="DLPFC" and c["unit"] in UNIT_IDS]
 if len(configs)!=2 or sorted(c["unit"] for c in configs)!=[25,53]:
  raise RuntimeError("ORIGINAL_SOURCE_UNIT_SELECTION_FAIL")
 for c in configs:
  if (c["unit"],c["strength"],c["preferred_deg"],c["reward_deg"]) not in (
     (25,45,160,340),(53,45,295,115)):
   raise RuntimeError("ORIGINAL_AUTHOR_UNIT_METADATA_DRIFT")
 sys.path.insert(0,str(root))
 import DotsTasks
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 args.out.mkdir(parents=True,exist_ok=True)
 start=time.monotonic()
 fields=["module","unit","preferred_deg","stim_strength","reward_deg","seed_block","seed",
 "trial_index","shown_deg","ring_ms","dots_ms","sham_choice_deg","stim_choice_deg",
 "sham_dist_pref_deg","stim_dist_pref_deg","gap5_65","gap5_60","gap_at_5","gap_at_65",
 "sham_gap5_65","exact_pref_stim","exact_pref_sham","choice_changed",
 "sham_margin","score_sup_delta","argmax_preserve_cert"]
 all_report=[];blocks_out=[];labels_out=[];rows=0;pair_checks=0;repeat_checks=0
 with (args.out/"xh_s6_rot019_author_native_random_direction_36000_paired_rnn.csv").open("w",encoding="utf8",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
  for cfg in configs:
   unit=cfg["unit"];pref=cfg["preferred_deg"];source_counts=[0]*72;both_choices=[]
   tally={k:0 for k in ("gap5_65","gap5_60","gap_at_5","gap_at_65",
         "sham_gap5_65","exact_pref_stim","exact_pref_sham","choice_changed","argmax_preserve_cert")}
   sham_choices=[];witnesses=[];by_shown=[0]*72;gap_by_shown=[0]*72;per_block=[]
   for block in range(BLOCKS):
    seed=fixed_seed(unit,block)
    base=source_model_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,w,mt,dp,cfg,seed,0)
    stim=source_model_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,w,mt,dp,cfg,seed,cfg["strength"])
    if base["param_digest"]!=stim["param_digest"] or base["times"]!=stim["times"] or base["rng_digest"]!=stim["rng_digest"] or base["shown"]!=stim["shown"]:
     raise RuntimeError("SOURCE_RANDOM_INPUT_OR_ONSET_PAIRING_FAIL")
    if not np.array_equal(base["inputs"][:,:,:-1],stim["inputs"][:,:,:-1]):
     raise RuntimeError("SOURCE_STIM_SHAM_DIFFERENT_NONSTIM_INPUT")
    pair_checks+=1
    if block==0:
     check=source_model_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,w,mt,dp,cfg,seed,0)
     if not np.array_equal(check["scores"],base["scores"]):
      raise RuntimeError("ORIGINAL_SHAM_BITWISE_REPEAT_FAIL")
     repeat_checks+=1
    t={k:0 for k in tally}
    for i in range(72):
     shown=base["shown"][i];reward=base["reward"][i]
     if shown not in range(0,360,5) or reward!=cfg["reward_deg"]:
      raise RuntimeError("ORIGINAL_AUTHOR_SOURCE_SHOWN_OR_REWARD_FAIL")
     b=int(base["choice"][i]);s=int(stim["choice"][i])
     db=m.dist(b,pref);ds=m.dist(s,pref)
     margin=w.margin(base["scores"][i])
     sup=float(np.max(np.abs(stim["scores"][i]-base["scores"][i])))
     cert=int(sup<margin/2)
     if s!=b and cert:raise RuntimeError("ARGMAX_MARGIN_PRESERVATION_CONTRADICTION")
     ring,dots=base["times"][i]
     if ring not in range(50,141,10) or dots not in range(450,541,10):
      raise RuntimeError("ORIGINAL_AUTHOR_ONSET_SUPPORT_FAIL")
     row={"module":"DLPFC","unit":unit,"preferred_deg":pref,
     "stim_strength":cfg["strength"],"reward_deg":cfg["reward_deg"],
     "seed_block":block,"seed":seed,"trial_index":i,"shown_deg":shown,
     "ring_ms":ring,"dots_ms":dots,"sham_choice_deg":b,"stim_choice_deg":s,
     "sham_dist_pref_deg":db,"stim_dist_pref_deg":ds,
     "gap5_65":int(5<=ds<=65),"gap5_60":int(5<=ds<=60),"gap_at_5":int(ds==5),
     "gap_at_65":int(ds==65),"sham_gap5_65":int(5<=db<=65),
     "exact_pref_stim":int(s==pref),"exact_pref_sham":int(b==pref),
     "choice_changed":int(s!=b),"sham_margin":format(margin,".17g"),
     "score_sup_delta":format(sup,".17g"),"argmax_preserve_cert":cert}
     writer.writerow(row);rows+=1
     source_counts[shown//5]+=1;by_shown[shown//5]+=1;gap_by_shown[shown//5]+=row["gap5_65"]
     both_choices.append(s);sham_choices.append(b)
     for k in tally:t[k]+=row[k];tally[k]+=row[k]
     if row["gap5_65"]:
      witnesses.append({k:row[k] for k in ("unit","seed_block","seed","trial_index",
        "shown_deg","ring_ms","dots_ms","sham_choice_deg","stim_choice_deg",
        "stim_dist_pref_deg","choice_changed")})
    blocks_out.append({"unit":unit,"seed_block":block,"source_seed":seed,**t})
    per_block.append(t)
    if (block+1)%50==0:print(f"PROGRESS unit={unit} completed_block={block+1}/250 pairs={rows}",flush=True)
   if sum(source_counts)!=18000:raise RuntimeError("SOURCE_TRIAL_ANGLE_COUNTS_INCONSISTENT")
   candidate=[]
   for label in range(0,360,5):
    stim_gap=sum(1 for s in both_choices if 5<=m.dist(s,label)<=65)
    sham_gap=sum(1 for b in sham_choices if 5<=m.dist(b,label)<=65)
    candidate.append({"unit":unit,"original_pref_deg":pref,"candidate_deg":label,
       "source_unit_true_label":int(label==pref),"stim_gap5_65_count":stim_gap,
       "sham_gap5_65_count":sham_gap})
    labels_out.append(candidate[-1])
   minimum=min(x["stim_gap5_65_count"] for x in candidate)
   argmins=[x["candidate_deg"] for x in candidate if x["stim_gap5_65_count"]==minimum]
   summary={"unit":unit,"source_original_pref_deg":pref,"strength":cfg["strength"],
    "reward_deg":cfg["reward_deg"],"original_source_random_test1ofEach":False,
    "N_source_paired_trials":18000,"source_rng_seed_blocks":BLOCKS,
    "source_shown_counts_72":source_counts,
    "number_source_angle_counts_not_250":sum(x!=250 for x in source_counts),
    "source_angle_counts_min":min(source_counts),"source_angle_counts_max":max(source_counts),
    "source_angle_counts_population_sd":float(np.std(source_counts)),
    "counts":tally,"true_pref_gap_count":tally["gap5_65"],
    "min_wrong_label_gap_count":min(x["stim_gap5_65_count"] for x in candidate if x["candidate_deg"]!=pref),
    "source_true_pref_unique_global_minimum":(argmins==[pref]),
    "all_gap_witnesses":witnesses,
    "source_per_shown_gap_counts":[{"shown":i*5,"n":by_shown[i],"gap":gap_by_shown[i]} for i in range(72)]}
   all_report.append(summary)
   print("UNIT_FINAL "+json.dumps({k:v for k,v in summary.items()
       if k not in ("source_shown_counts_72","all_gap_witnesses","source_per_shown_gap_counts")},sort_keys=True),flush=True)
 if rows!=36000 or pair_checks!=500 or repeat_checks!=2:
  raise RuntimeError("PAIRED_ORIGINAL_SOURCE_GRID_OR_STREAM_COUNTS_FAIL")
 for name,records in [("xh_s6_rot019_500_native_block_profiles.csv",blocks_out),
                      ("xh_s6_rot019_144_candidate_label_profiles.csv",labels_out)]:
  with (args.out/name).open("w",encoding="utf8",newline="") as f:
   writer=csv.DictWriter(f,fieldnames=list(records[0]));writer.writeheader();writer.writerows(records)
 result={"artifact_id":"IW_XH_S6_ROT019_ORIGINAL_AUTHOR_RANDOM_DIRECTION_RNN_TWO_UNIT_SOURCE_GATE_001_20261113",
 "source_firstness":"Ruff Markman Kim Cohen Nature Neuroscience 2026-11-10 DOI 10.1038/s41593-026-02514-7",
 "author_frozen_source_commit":AUTHOR,"source_preregister_git_blob":PREREG_GIT_BLOB,
 "original_rot009_wrapper_blob":ROT009_GIT_BLOB,"original_rot013_parser_blob":ROT013_GIT_BLOB,
 "source_scheduler":"N_batch=72; original MT Task test1ofEach=False, fix_shown=(pref+np.arange(0,360,5))%360, random rng.choice shown",
 "original_author_one_single_18000_batch":"NOT_EXECUTED",
 "original_source_model_RNN_executed":True,"source_pair_rows":rows,"source_arm_simulations":rows*2,
 "matched_original_source_rng_and_onset_blocks":pair_checks,"bitwise_source_sham_repeat_checks":repeat_checks,
 "unit_reports":all_report,"elapsed_seconds":time.monotonic()-start,
 "no_novelty":True,"no_canon":True,"no_exec_sign":True,"bw":"GITHUB_PENDING_BW_INGEST"}
 (args.out/"xh_s6_rot019_author_native_random_direction_actual_runner_summary.json").write_text(
   json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf8")
 print("ROT019_FINAL_JSON_BEGIN")
 print(json.dumps({k:v for k,v in result.items() if k!="unit_reports"}|
   {"unit_reports":[{k:v for k,v in u.items() if k not in ("all_gap_witnesses","source_shown_counts_72","source_per_shown_gap_counts")} for u in all_report]},sort_keys=True))
 print("ROT019_FINAL_JSON_END",flush=True)
if __name__=="__main__":main()
