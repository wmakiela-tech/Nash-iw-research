#!/usr/bin/env python3
"""XH-S6 ROT009: author-native paired stochastic microstimulation, bounded source test.

Author original code unchanged: DotsTasks and vendored psychrnn from pinned commit.
Controlled common-random-number pairing is NEW test design; source manuscript
used independent sampling. No animal data or author full Monte Carlo claim.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,os,sys,time
from pathlib import Path
import numpy as np

AUTHOR_COMMIT="7889a81e298c01532a313e02971c11dbc9db8eb0"
PINS={
"MTbroadsharp_m10.npz":"c5e701740f8ab1d19ca07415c0de2d6e7f88c37f",
"DLPFCcombined_m4.npz":"47142e3dee920a759406136449f0b12f9ce752ee",
"DotsTasks.py":"ac9e789c69a8ea46ac38303f9d0db524886ba0a9",
"psychrnn/backend/simulation.py":"d187595af592a888192bfc2dde6f562776b88423",
"psychrnn/tasks/task.py":"b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865",
"circledots_fxns.py":"909a65d84174a7eebb0e19273d06ae400dc9094f",
"generate_microstim_testdata.py":"e7a6666e0b600ea49bab9755d302c78110ba9bc4"
}
PAIR_SETTINGS=[
 {"module":"MT","unit":37,"preferred_deg":110,"reward_deg":290,"strength":11},
 {"module":"DLPFC","unit":53,"preferred_deg":295,"reward_deg":115,"strength":45}
]
def sha_blob(b):
 return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
def assert_original(path,pin):
 raw=Path(path).read_bytes(); got=sha_blob(raw)
 if got!=pin:raise RuntimeError(f"SOURCE_IDENTITY_FAIL path={path} got={got} expected={pin}")
 return raw
def load_model(path,name):
 assert_original(path,PINS[name])
 with np.load(path,allow_pickle=False) as src:
  m={k:src[k].copy() for k in ("init_state","W_in","W_rec","W_out","b_rec","b_out")}
 assert m["init_state"].shape==(1,150)
 assert m["W_in"].shape==(150,75)
 assert m["W_rec"].shape==(150,150)
 assert np.max(np.abs(m["W_in"][:,-1]))==0
 return m
def margin(row):
 top=np.partition(row,-2)[-2:]
 return float(top[-1]-top[-2])
def rand_digest(dots):
 return hashlib.sha256((repr(dots.rng.bit_generator.state)+"\n"+repr(np.random.get_state())).encode()).hexdigest()
def trial_params_digest(params):
 return hashlib.sha256(json.dumps([
  (int(z["shown_deg"]),int(z["good_deg"]),int(z["t_ring"]),int(z["t_dots"]))
  for z in params],separators=(",",":")).encode()).hexdigest()
def execute_pair_arm(dots,mt_type,dl_type,mt_original,dl_original,config,seed,strength):
 dots.rng=np.random.default_rng(seed)
 np.random.seed(seed+171717)
 MT= {k:v.copy() for k,v in mt_original.items()}
 DL= {k:v.copy() for k,v in dl_original.items()}
 if config["module"]=="MT":MT["W_in"][config["unit"],-1]=1.
 else:DL["W_in"][config["unit"],-1]=1.
 mstim=strength if config["module"]=="MT" else 0
 dstim=strength if config["module"]=="DLPFC" else 0
 directions=np.arange(0,360,5)
 mt_task=dots.MT_broadInSharpOut_withR(
   N_batch=72,N_rec=150,in_noise=0.4,coh=[0.6],
   fix_shown=directions,fix_reward=np.array([config["reward_deg"]]),
   M_mstim_strength=mstim,test1ofEach=True,catchP=0.)
 mt_sim=mt_type(weights=MT,params={"dt":10,"tau":100,"rec_noise":0.2})
 dp_task=dots.DLPFC_combined(
   N_batch=72,N_rec=150,in_noise=0.2,D_mstim_strength=dstim,
   MT_task=mt_task,MT_simulator=mt_sim,MT_NdirOuts=72)
 dp_inputs,_,_,params=dp_task.get_trial_batch()
 assert dp_inputs.shape==(72,120,75)
 dp_sim=dl_type(weights=DL,params={"dt":10,"tau":100,"rec_noise":0.2})
 dp_outputs,_=dp_sim.run_trials(dp_inputs)
 scores=np.asarray(dp_outputs[:,-1,:],dtype=np.float64)
 assert scores.shape==(72,72) and np.isfinite(scores).all()
 shown=[int(p["shown_deg"]) for p in params]
 assert shown==list(range(0,360,5))
 reward=[int(p["good_deg"]) for p in params]
 assert reward==[config["reward_deg"]]*72
 return {"scores":scores,"choice":np.argmax(scores,axis=1)*5,
         "params_digest":trial_params_digest(params),"rng_digest":rand_digest(dots),
         "times":[(int(p["t_ring"]),int(p["t_dots"])) for p in params],
         "inputs":dp_inputs}
def main():
 a=argparse.ArgumentParser()
 a.add_argument("--author-python-data-dir",type=Path,required=True)
 a.add_argument("--output-dir",type=Path,required=True)
 a.add_argument("--seeds",type=int,default=12)
 args=a.parse_args()
 if not 1<=args.seeds<=24:raise RuntimeError("BOUNDED_SEEDS_EXPECTED_1_TO_24")
 root=args.author_python_data_dir.resolve()
 for name,pin in PINS.items():
  if name.endswith(".py"):assert_original(root/name,pin)
 MT=load_model(root/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
 DL=load_model(root/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
 sys.path.insert(0,str(root))
 import DotsTasks
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 t0=time.monotonic()
 args.output_dir.mkdir(parents=True,exist_ok=True)
 rows=[];stats=[];fail=[]
 for c in PAIR_SETTINGS:
  for kk in range(args.seeds):
   seed=20261112+1009*kk+(0 if c["module"]=="MT" else 400001)
   ctl=execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,MT,DL,c,seed,0)
   stm=execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,MT,DL,c,seed,c["strength"])
   if ctl["params_digest"]!=stm["params_digest"] or ctl["times"]!=stm["times"]:
    raise RuntimeError("PAIRED_TIMES_OR_INPUT_CONDITIONS_MISMATCH")
   if ctl["rng_digest"]!=stm["rng_digest"]:
    raise RuntimeError("PAIRED_RNG_CONSUMPTION_MISMATCH")
   if kk==0:
    null=execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,MT,DL,c,seed,0)
    if not np.array_equal(ctl["scores"],null["scores"]):
     raise RuntimeError("SHAM_REPLAY_NOT_BIT_EXACT")
   if c["module"]=="DLPFC":
    # DLPFC stimulation changes only its last noisy/stimulus input channel.
    if not np.array_equal(ctl["inputs"][:,:,:-1],stm["inputs"][:,:,:-1]):
     raise RuntimeError("DLPFC_PAIRED_PRESTIM_INPUT_MISMATCH")
   for j in range(72):
    b=ctl["scores"][j];s=stm["scores"][j];base_margin=margin(b)
    eps=float(np.max(np.abs(s-b)));flip=bool(ctl["choice"][j]!=stm["choice"][j])
    certified=bool(eps<base_margin/2)
    if flip and certified:raise RuntimeError("ARGMAX_MARGIN_THEOREM_VIOLATION")
    rows.append({
      "module":c["module"],"unit":c["unit"],"strength":c["strength"],
      "seed_index":kk,"seed":seed,"shown_deg":int(j*5),"reward_deg":c["reward_deg"],
      "t_ring_ms":ctl["times"][j][0],"t_dots_ms":ctl["times"][j][1],
      "baseline_choice_deg":int(ctl["choice"][j]),
      "stim_choice_deg":int(stm["choice"][j]),
      "choice_changed":int(flip),"baseline_top2_margin":format(base_margin,".17g"),
      "paired_final_score_sup_delta":format(eps,".17g"),
      "certified_invariant_by_margin":int(certified),
      "paired_random_streams_same":1
    })
 for c in PAIR_SETTINGS:
  subset=[r for r in rows if r["module"]==c["module"]]
  changed=sum(r["choice_changed"] for r in subset)
  certified=sum(r["certified_invariant_by_margin"] for r in subset)
  group={"module":c["module"],"unit":c["unit"],"strength":c["strength"],
         "n_paired_trials":len(subset),"n_changed":changed,
         "changed_fraction_in_bounded_sample":changed/len(subset),
         "n_invariance_certified":certified,"n_unchanged":len(subset)-changed,
         "paired_rng_digest_pass":True,"sham_bitwise_repeat_pass":True}
  stats.append(group)
 fields=list(rows[0])
 with (args.output_dir/"xh_s6_rot009_author_native_noisy_paired_trials.csv").open("w",encoding="utf-8",newline="") as f:
  writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader();writer.writerows(rows)
 summary={"artifact_id":"IW_XH_S6_ROT009_AUTHOR_NATIVE_PAIRED_NOISY_MICROSTIM_SOURCE_CONTROL_001_20261112",
   "author_commit":AUTHOR_COMMIT,"source_git_blobs":PINS,
   "execution":"actual author DotsTasks + original vendored PsychRNN classes on original trained NPZ",
   "design":"72 shown directions x fixed finite seeds per source unit, common random numbers paired, source noise and random onset",
   "source_noise":{"MT_input":0.4,"MT_recurrent":0.2,"DLPFC_input":0.2,"DLPFC_recurrent":0.2},
   "stimulations":PAIR_SETTINGS,"per_module_seed_count":args.seeds,
   "per_module_paired_trials":72*args.seeds,"total_paired_trials":len(rows),
   "pairing_author_protocol":False,"original_author_noisy_18000_per_condition_replayed":False,
   "rng_and_trial_condition_pairing_check":"PASS","sham_source_replay_exact":"PASS",
   "margin_theorem_control":"PASS","group_summaries":stats,
   "elapsed_s":time.monotonic()-t0,
   "no_monkey_data":True,"no_novelty":True,"no_canon":True,"no_exec_sign":True,
   "status":"PASS"}
 (args.output_dir/"xh_s6_rot009_author_native_noisy_paired_summary.json").write_text(
   json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print(json.dumps(summary,indent=2,sort_keys=True),flush=True)
if __name__=="__main__":main()
