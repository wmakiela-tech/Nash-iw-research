#!/usr/bin/env python3
"""XH-S6 ROT018: original author MT Task input-direction RANDOM scheduler.

Stream the exact original Task implementation: generate_trial_params followed
by generate_trial for each original N_batch=18000 trial, recording parameters
and discarding bulky source input/target/mask arrays. This reproduces the
author original Task RNG-advance sequence, NOT the full RNN author experiment.
Prior first compare original get_trial_batch versus stream on 72 trials,
including every trial's MT input/output/mask and exact final source RNG state.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,sys,time
from pathlib import Path
import numpy as np
AUTHOR="7889a81e298c01532a313e02971c11dbc9db8eb0"
PREREG_BLOB="66171ec720d1ea3bd676ef21d336ae26fbfeaf4b"
PINS={
"DotsTasks.py":"ac9e789c69a8ea46ac38303f9d0db524886ba0a9",
"psychrnn/tasks/task.py":"b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865",
"circledots_fxns.py":"909a65d84174a7eebb0e19273d06ae400dc9094f",
"generate_microstim_testdata.py":"e7a6666e0b600ea49bab9755d302c78110ba9bc4"}
UNITS=[(25,160,340,1900000025),(53,295,115,1900000053)]
def gitblob(b):return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def pin(path,identity):
 got=gitblob(path.read_bytes())
 if got!=identity:raise RuntimeError(f"SOURCE_GIT_BLOB_INTEGRITY_FAIL: {path} {got}!={identity}")
def new_task(dots,pref,good,n):
 return dots.MT_broadInSharpOut_withR(
  N_batch=n,N_rec=150,in_noise=0.4,coh=[0.6],M_mstim_strength=0,
  fix_shown=(np.arange(0,360,5)+pref)%360,
  fix_reward=np.array([good]))  # default test1ofEach=False identical to author
def seed_source(dots,seed):
 dots.rng=np.random.default_rng(seed)
 np.random.seed(seed+171717)
def native_params(p):
 return (int(p["shown_deg"]),int(p["good_deg"]),int(p["t_ring"]),
         int(p["t_dots"]),float(p["coherence"]))
def source_rng_state(dots):
 return json.dumps(dots.rng.bit_generator.state,sort_keys=True)
def first_source_class_equivalence(dots,pref,good,seed):
 # source default actual get_trial_batch, N_batch=72
 seed_source(dots,seed)
 src=new_task(dots,pref,good,72)
 x,y,m,params=src.get_trial_batch()
 state_1=source_rng_state(dots)
 gen=[]
 seed_source(dots,seed)
 stream=new_task(dots,pref,good,72)
 for i in range(72):
  p=stream.generate_trial_params(1,i)
  a,b,c=stream.generate_trial(p)
  gen.append((native_params(p),a,b,c))
 state_2=source_rng_state(dots)
 if state_1!=state_2:raise RuntimeError("STREAM_VS_ORIGINAL_GET_BATCH_RNG_MISMATCH")
 for i in range(72):
  p,a,b,c=gen[i]
  if p!=native_params(params[i]):raise RuntimeError(f"TRIAL_{i}_PARAM_MISMATCH")
  if not np.array_equal(a,x[i]) or not np.array_equal(b,y[i]) or not np.array_equal(c,m[i]):
   raise RuntimeError(f"TRIAL_{i}_INPUT_TARGET_MASK_MISMATCH")
 return {"trial_batch_n":72,"params_full_match":True,"all_72_input_target_mask_bitwise":True,
         "source_final_rng_exact_match":True,
         "final_rng_state_sha256":hashlib.sha256(state_1.encode()).hexdigest()}
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--original-source-dir",type=Path,required=True)
 a.add_argument("--preregister",type=Path,required=True)
 a.add_argument("--out",type=Path,required=True)
 args=a.parse_args()
 if gitblob(args.preregister.read_bytes())!=PREREG_BLOB:raise RuntimeError("PREREG_NOT_EXACT_SOURCE_BLOB")
 root=args.original_source_dir.resolve()
 for k,v in PINS.items():pin(root/k,v)
 sys.path.insert(0,str(root))
 import DotsTasks as dots
 args.out.mkdir(parents=True,exist_ok=True)
 t0=time.monotonic();records=[]
 with (args.out/"xh_s6_rot018_original_author_streamed_36000_task_direction_trials.csv").open("w",newline="",encoding="utf8") as file:
  fields=["source_unit","source_preference_deg","source_reward_deg","source_seed",
          "trial_index","shown_deg","shown_relative_deg","ring_ms","dots_ms","coherence"]
  w=csv.DictWriter(file,fieldnames=fields);w.writeheader()
  for unit,pref,good,seed in UNITS:
   check=first_source_class_equivalence(dots,pref,good,seed)
   seed_source(dots,seed)
   n=18000
   task=new_task(dots,pref,good,n)
   if task.test1ofEach is not False:
    raise RuntimeError("SOURCE_DEFAULT_RANDOM_SCHEDULER_NOT_ACTIVE")
   dirs=[0]*72;ring=[0]*10;dots_bins=[0]*10;onset=[[0]*10 for _ in range(10)]
   for i in range(n):
    p=task.generate_trial_params(1,i)
    task.generate_trial(p)  # executes exact source MT per-time noise RNG; discards arrays
    s,g,ring_ms,dots_ms,coh=native_params(p)
    if g!=good or s not in range(0,360,5) or (ring_ms-50)%10 or not 50<=ring_ms<=140 or (dots_ms-450)%10 or not 450<=dots_ms<=540 or coh!=0.6:
     raise RuntimeError("AUTHOR_SOURCE_PARAMETER_RANGE_OR_REWARD_ERROR")
    dirs[s//5]+=1;ring[(ring_ms-50)//10]+=1;dots_bins[(dots_ms-450)//10]+=1
    onset[(ring_ms-50)//10][(dots_ms-450)//10]+=1
    w.writerow(dict(source_unit=unit,source_preference_deg=pref,source_reward_deg=good,
     source_seed=seed,trial_index=i,shown_deg=s,shown_relative_deg=(s-pref)%360,
     ring_ms=ring_ms,dots_ms=dots_ms,coherence=coh))
   if sum(dirs)!=18000 or sum(map(sum,onset))!=18000:
    raise RuntimeError("SOURCE_SCHEDULER_TRIALS_MISSING")
   result={"source_unit":unit,"source_preference_deg":pref,"source_reward_deg":good,
      "source_seed":seed,"n_source_task_trials":n,
      "native_source_task_stream_equivalence":check,
      "source_task_test1ofEach_default":task.test1ofEach,
      "source_direction_72_bin_counts":dirs,"source_ring_onset_10_bin_counts":ring,
      "source_dots_onset_10_bin_counts":dots_bins,"source_onset_grid_counts":onset,
      "source_direction_count_min":min(dirs),"source_direction_count_max":max(dirs),
      "source_direction_count_mean":sum(dirs)/72,
      "source_angle_bins_not_equal250":sum(x!=250 for x in dirs),
      "source_direction_count_population_sd":float(np.std(dirs)),
      "source_random_final_rng_sha256":hashlib.sha256(source_rng_state(dots).encode()).hexdigest(),
      "source_falsifier_balanced_exact250":all(x==250 for x in dirs)}
   records.append(result)
   print("SOURCE_UNIT_RESULT "+json.dumps({k:v for k,v in result.items() if k not in ("source_onset_grid_counts","source_direction_72_bin_counts","source_ring_onset_10_bin_counts","source_dots_onset_10_bin_counts")},sort_keys=True),flush=True)
 with (args.out/"xh_s6_rot018_native_source_144_direction_occupancies.csv").open("w",newline="",encoding="utf8") as f:
  w=csv.DictWriter(f,fieldnames=["source_unit","pref_deg","shown_deg","source_draw_count","rot017_balanced_count","source_minus_balanced_count"]);w.writeheader()
  for r in records:
   for i,v in enumerate(r["source_direction_72_bin_counts"]):
    w.writerow(dict(source_unit=r["source_unit"],pref_deg=r["source_preference_deg"],
     shown_deg=i*5,source_draw_count=v,rot017_balanced_count=250,source_minus_balanced_count=v-250))
 result={"artifact_id":"IW_XH_S6_ROT018_ORIGINAL_SOURCE_RANDOM_INPUT_SCHEDULER_36000_NATIVE_TASK_TRIALS_001_20261113",
  "original_author_commit":AUTHOR,"original_author_DotsTasks_git_blob":PINS["DotsTasks.py"],
  "original_author_Task_git_blob":PINS["psychrnn/tasks/task.py"],
  "original_author_generator_git_blob":PINS["generate_microstim_testdata.py"],
  "rot018_preregister_git_blob":PREREG_BLOB,
  "source_original_reward180":True,"source_original_stochastic_direction_choice":True,
  "source_default_test1ofEach":False,
  "actual_original_task_trial_generator_run":True,
  "neural_network_weighted_RNN_NOT_RUN":True,
  "original_author_full_18000_input_batch_not_materialized":True,
  "two_unit_source_task_trials":36000,
  "source_conditions":records,
  "source_mathematical_expected_count_per_angle":250,
  "source_random_angle_distribution_not_forced_balanced":True,
  "status":"SOURCE_AUTHOR_NATIVE_TASK_RNG_STREAM_EXECUTION_PASS",
  "elapsed_seconds":time.monotonic()-t0,
  "no_novelty":True,"no_canon":True,"no_exec_sign":True}
 (args.out/"xh_s6_rot018_native_source_task_scheduler_summary.json").write_text(
  json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf8")
 print("ROT018_FINAL_JSON_BEGIN")
 print(json.dumps({k:v for k,v in result.items() if k!="source_conditions"}|{"source_conditions":[
  {k:v for k,v in r.items() if k not in ("source_onset_grid_counts","source_direction_72_bin_counts","source_ring_onset_10_bin_counts","source_dots_onset_10_bin_counts")}
 for r in records]},sort_keys=True))
 print("ROT018_FINAL_JSON_END",flush=True)
if __name__=="__main__":main()
