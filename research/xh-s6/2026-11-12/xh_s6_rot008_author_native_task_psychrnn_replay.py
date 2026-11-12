#!/usr/bin/env python3
"""XH-S6 ROT008 — author-native Task+Simulator 360-case source-frozen exact replay.

Source-author repository pinned to solkm/formattingRNN @7889a81e298c01532a313e02971c11dbc9db8eb0.
Only original author DotsTasks and vendored PsychRNN simulation/tasks are executed here.
Original trained weights pinned by Git blob SHA; prior 360 source NumPy results
are independently checked against frozen Git blob SHA before scientific comparison.
Zero noise; forced source-supported fixed onset pairs; no stimulation.
Not original published noisy experimental protocol, no animal data, no novelty.
"""
from __future__ import annotations
import argparse,csv,hashlib,json,math,os,sys,time
from pathlib import Path
import numpy as np

AUTHOR_COMMIT = "7889a81e298c01532a313e02971c11dbc9db8eb0"
PINS = {
 "MTbroadsharp_m10.npz":"c5e701740f8ab1d19ca07415c0de2d6e7f88c37f",
 "DLPFCcombined_m4.npz":"47142e3dee920a759406136449f0b12f9ce752ee",
 "motion":"88bd42f4ce793c823faf5bc8e804b466ce643624",
 "reward":"f8a4e12e7fd706112bbe273bd437675ec55ebc3a",
 "DotsTasks.py":"ac9e789c69a8ea46ac38303f9d0db524886ba0a9",
 "psychrnn/backend/simulation.py":"d187595af592a888192bfc2dde6f562776b88423",
 "psychrnn/tasks/task.py":"b3bc5a5ca3fb2b0d2b4b79a4cd5ce8930e142865",
 "circledots_fxns.py":"909a65d84174a7eebb0e19273d06ae400dc9094f",
}

def git_sha(content:bytes)->str:
 return hashlib.sha1(b"blob "+str(len(content)).encode()+b"\0"+content).hexdigest()

def assert_pin(path:Path,pin:str):
 raw=path.read_bytes()
 actual=git_sha(raw)
 if actual!=pin:raise RuntimeError(f"ORIGINAL_SOURCE_IDENTITY_FAIL path={path} expected={pin} observed={actual}")
 return raw

def load_source_weights(path:Path,pin:str):
 assert_pin(path,pin)
 with np.load(path,allow_pickle=False) as d:
  weights={k:d[k] for k in ("init_state","W_in","W_rec","W_out","b_rec","b_out")}
 assert weights["init_state"].shape==(1,150)
 assert weights["W_rec"].shape==(150,150)
 assert weights["W_in"].shape==(150,75)
 assert np.max(np.abs(weights["W_in"][:,-1]))==0
 return weights

def get_frozen_rows(path:Path,pin:str):
 raw=assert_pin(path,pin)
 rows=list(csv.DictReader(x for x in raw.decode("utf-8").splitlines() if x.strip() and not x.startswith("#")))
 if len(rows)!=180:raise RuntimeError("REFERENCE_ROW_COUNT_FAIL")
 return rows

def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--author-python-data-dir",type=Path,required=True)
 parser.add_argument("--motion-csv",type=Path,required=True)
 parser.add_argument("--reward-csv",type=Path,required=True)
 parser.add_argument("--output-dir",type=Path,required=True)
 parser.add_argument("--limit",type=int,default=0,help="0=all 360; optional source smoke subset")
 args=parser.parse_args()
 start=time.monotonic()
 root=args.author_python_data_dir.resolve()
 for name in ("DotsTasks.py","psychrnn/backend/simulation.py","psychrnn/tasks/task.py","circledots_fxns.py"):
  assert_pin(root/name,PINS[name])
 mt=load_source_weights(root/"model_weights/MTbroadsharp_m10.npz",PINS["MTbroadsharp_m10.npz"])
 dl=load_source_weights(root/"model_weights/DLPFCcombined_m4.npz",PINS["DLPFCcombined_m4.npz"])
 expected=[("motion",get_frozen_rows(args.motion_csv,PINS["motion"])),
           ("reward",get_frozen_rows(args.reward_csv,PINS["reward"]))]
 sys.path.insert(0,str(root))
 from DotsTasks import MT_broadInSharpOut_withR,DLPFC_combined
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 prior=[];failed=[];maxerr=0.;max_target_err=0.;checks=0
 for axis,rows in expected:
  for entry in rows:
   if args.limit and checks>=args.limit:break
   good=int(entry["reward_center_deg"])
   shown=int(entry["shown_deg"])
   ring=int(entry["ring_ms"])
   dots=int(entry["dots_ms"])
   mt_task=MT_broadInSharpOut_withR(
       N_batch=1,N_rec=150,in_noise=0.,coh=[0.6],k_in=0.3,k_out=0.8,
       M_mstim_strength=0,fix_shown=np.array([shown]),fix_reward=np.array([good]),
       catchP=0.,fix_onset=[ring,dots],test1ofEach=True)
   mt_sim=BasicSimulator_linOut(weights=mt,params={"dt":10,"tau":100,"rec_noise":0.})
   dp_task=DLPFC_combined(
       N_batch=1,N_rec=150,in_noise=0.,D_mstim_strength=0.,
       MT_task=mt_task,MT_simulator=mt_sim,MT_NdirOuts=72)
   dp_in,dp_target,dp_mask,parameters=dp_task.get_trial_batch()
   if dp_in.shape!=(1,120,75) or dp_target.shape!=(1,120,72):
    raise RuntimeError(f"AUTHOR_TASK_SHAPE_FAIL shape={dp_in.shape} target={dp_target.shape}")
   if not (parameters[0]["good_deg"]==good and parameters[0]["shown_deg"]==shown and
           parameters[0]["t_ring"]==ring and parameters[0]["t_dots"]==dots):
    raise RuntimeError("AUTHOR_TASK_PARAM_MISMATCH")
   dp_sim=BasicSimulator(weights=dl,params={"dt":10,"tau":100,"rec_noise":0.})
   dp_out,states=dp_sim.run_trials(dp_in)
   scores=dp_out[0,-1,:]
   order=np.argsort(scores)
   choice=int(5*np.argmax(scores))
   margin=float(scores[order[-1]]-scores[order[-2]])
   expected_choice=int(entry["trained_winner_deg"])
   expected_margin=float(entry["trained_top2_margin"])
   delta=abs(margin-expected_margin);maxerr=max(maxerr,delta)
   # Task source target should have exact mirror maxima in each antipodal case.
   target=parameters[0]["reward"]
   chosen_targets=np.sort(target)[-2:]
   target_error=float(abs(chosen_targets[-1]-chosen_targets[-2]))
   max_target_err=max(max_target_err,target_error)
   if target_error>1e-12:raise RuntimeError(f"AUTHOR_TARGET_MIRROR_TIE_FAIL {good} {shown} {target_error}")
   ok=(choice==expected_choice and delta<=2e-5)
   row=[axis,good,shown,ring,dots,expected_choice,choice,expected_margin,margin,delta,target_error,int(ok)]
   prior.append(row)
   if not ok:failed.append({"axis":axis,"good":good,"shown":shown,"ring":ring,"dots":dots,
     "expected_choice":expected_choice,"observed_choice":choice,
     "expected_margin":expected_margin,"observed_margin":margin,"margin_abs_error":delta})
   checks+=1
  if args.limit and checks>=args.limit:break
 args.output_dir.mkdir(parents=True,exist_ok=True)
 with (args.output_dir/"xh_s6_rot008_author_native_task_simulator_detailed.csv").open("w",newline="",encoding="utf-8") as f:
  writer=csv.writer(f)
  writer.writerow(["axis","reward_deg","shown_deg","ring_ms","dots_ms","expected_choice_deg","author_native_choice_deg",
                   "expected_margin","author_native_margin","margin_abs_error","target_tie_difference","pass"])
  writer.writerows(prior)
 outcome={"artifact_id":"IW_XH_S6_ROT008_AUTHOR_NATIVE_TASK_PSYCHRNN_ORIGINAL_NPZ_REPLAY_001_20261112",
  "execution_class":"SOURCE_AUTHOR_NATIVE_TASK_CLASSES_AND_VENDORED_PSYCHRNN_SIMULATOR_CLASSES",
  "author_source_commit":AUTHOR_COMMIT,"source_pins":PINS,
  "compared":checks,"expected_total":360 if not args.limit else args.limit,"passed":checks-len(failed),
  "failed":len(failed),"max_margin_abs_error":maxerr,
  "max_author_target_tie_difference":max_target_err,
  "native_task_classes":["MT_broadInSharpOut_withR","DLPFC_combined"],
  "native_simulator_classes":["BasicSimulator_linOut","BasicSimulator"],
  "noise":"source input/recurrent set zero, no microstimulation",
  "trained_weights":"original public pinned author NPZ",
  "status":"PASS" if not failed and checks==(360 if not args.limit else args.limit) else "FAIL",
  "failures":failed[:30],"elapsed_s":time.monotonic()-start,
  "no_monkey_data":True,"no_novelty":True,"no_canon":True,"no_exec_sign":True}
 (args.output_dir/"xh_s6_rot008_author_native_task_simulator_summary.json").write_text(json.dumps(outcome,indent=2,sort_keys=True)+"\n",encoding="utf-8")
 print(json.dumps(outcome,indent=2,sort_keys=True),flush=True)
 if outcome["status"]!="PASS":sys.exit(2)
if __name__=="__main__":main()
