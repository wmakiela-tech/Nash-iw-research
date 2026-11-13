#!/usr/bin/env python3
"""XH-S6 ROT012 original author source-reward-alignment parameter intervention.

Original frozen Task and PsychRNN and trained NPZ; source-author ROT009 wrapper
Git blob prechecked. Reward centers 0,90,180,270 degrees relative to original
stimulated unit preference. Only 180 is original author stimulation protocol;
other reward offsets are NEW controlled XH task-generalization probes.
Common original stochastic source streams per seed/direction/offset pair AND
matched across reward offsets. No animal inference, no novelty, no canon.
"""
from __future__ import annotations
import argparse,csv,hashlib,importlib.util,json,math,sys,time
from pathlib import Path
import numpy as np

AUTHOR="7889a81e298c01532a313e02971c11dbc9db8eb0"
ROT009_SHA="054299b6b0f0c0def7cfa6b3600d6f56665375ce"
OFFSETS=(0,90,180,270)
SHOWN=np.arange(0,360,5)
CIRCULAR_BINS={int(i) for i in SHOWN}

def git_blob(data):
 return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def import_source(path:Path):
 got=git_blob(path.read_bytes())
 if got!=ROT009_SHA:raise RuntimeError(f"ROT009_SOURCE_GIT_BLOB_FAIL {got}")
 spec=importlib.util.spec_from_file_location("xh_s6_rot009_source_locked",str(path))
 mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
 if mod.AUTHOR_COMMIT!=AUTHOR:raise RuntimeError("ORIGINAL_AUTHOR_REVISION_MISMATCH")
 return mod

def dist(a,b):
 return abs((int(a)-int(b)+180)%360-180)

def task_reward(choice,shown,good):
 x=dist(choice,shown)
 if x>45:return 0.
 return (3.5+1.5*math.cos(math.radians(1.8*x)))*(1.+.75*math.cos(math.radians(dist(choice,good))))

def metrics(a,b,pref,shown,good):
 d0,d1=dist(a,pref),dist(b,pref)
 geodesic=0<d0<180 and 0<dist(a,b)<d0 and dist(a,b)+d1==d0
 return dict(
  flipped=int(a!=b),closer=int(d1<d0),farther=int(d1>d0),
  distance_delta_deg=d1-d0,
  antipodal=int(d0==180),
  unique_geodesic_eligible=int(d0<180),
  unique_short_arc_interior=int(geodesic),
  exactly_preferred=int(b==pref),
  baseline_preferred=int(a==pref),
  exact_endpoint=int(b==a or b==pref),
  baseline_target=task_reward(a,shown,good),
  stim_target=task_reward(b,shown,good),
  target_delta=task_reward(b,shown,good)-task_reward(a,shown,good),
  baseline_to_reward_distance=dist(a,good),
  stim_to_reward_distance=dist(b,good)
 )

def run():
 ap=argparse.ArgumentParser()
 ap.add_argument("--author-python-data-dir",required=True,type=Path)
 ap.add_argument("--rot009-source",required=True,type=Path)
 ap.add_argument("--output-dir",required=True,type=Path)
 ap.add_argument("--seed-blocks",type=int,default=24)
 args=ap.parse_args()
 if not 8<=args.seed_blocks<=40:raise RuntimeError("BLOCKS_NOT_BOUNDED")
 p09=import_source(args.rot009_source)
 root=args.author_python_data_dir.resolve()
 for name,pin in p09.PINS.items():
  if name.endswith(".py"):p09.assert_original(root/name,pin)
 mt=p09.load_model(root/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
 dp=p09.load_model(root/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
 sys.path.insert(0,str(root))
 import DotsTasks
 from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
 if git_blob((root/"DotsTasks.py").read_bytes())!=p09.PINS["DotsTasks.py"]:
  raise RuntimeError("ORIGINAL_DOTSTASKS_IDENTITY_FAIL")
 p09.DotsTasks=DotsTasks
 start=time.monotonic()
 args.output_dir.mkdir(parents=True,exist_ok=True)
 rows=[];counts={};context_checks=0;paired_checks=0
 for cfg in p09.PAIR_SETTINGS:
  mod=cfg["module"];pref=cfg["preferred_deg"]
  for k in range(args.seed_blocks):
   seed=2026111301+1009*k+(0 if mod=="MT" else 400001)
   reference_times=None;reference_rng=None
   for offset in OFFSETS:
    context=dict(cfg)
    good=(pref+offset)%360
    context["reward_deg"]=good
    sham=p09.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,mt,dp,context,seed,0)
    stim=p09.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,mt,dp,context,seed,context["strength"])
    if sham["params_digest"]!=stim["params_digest"] or sham["times"]!=stim["times"] or sham["rng_digest"]!=stim["rng_digest"]:
     raise RuntimeError("NOISE_ONSET_PAIRING_FAIL")
    paired_checks+=1
    if reference_times is None:
     reference_times=sham["times"];reference_rng=sham["rng_digest"]
    else:
     if sham["times"]!=reference_times or sham["rng_digest"]!=reference_rng:
      raise RuntimeError("REWARD_CONTEXT_NOT_COMMON_RANDOM_NUMBERS")
     context_checks+=1
    if k==0 and offset==180:
     check=p09.execute_pair_arm(DotsTasks,BasicSimulator_linOut,BasicSimulator,mt,dp,context,seed,0)
     if not np.array_equal(sham["scores"],check["scores"]):
      raise RuntimeError("ZERO_STIM_REPLAY_NOT_BIT_IDENTICAL")
    for j in range(72):
     shown=int(SHOWN[j])
     a=int(sham["choice"][j]);b=int(stim["choice"][j])
     if a not in CIRCULAR_BINS or b not in CIRCULAR_BINS:raise RuntimeError("CHOICE_NOT_5DEG_BIN")
     m=metrics(a,b,pref,shown,good)
     baseline_margin=float(p09.margin(sham["scores"][j]))
     delta=float(np.max(np.abs(stim["scores"][j]-sham["scores"][j])))
     invariant=int(delta<baseline_margin/2.)
     if m["flipped"] and invariant:raise RuntimeError("ARGMAX_MARGIN_CERT_VIOLATION")
     rows.append(dict(module=mod,unit=cfg["unit"],strength=cfg["strength"],
       preference_deg=pref,reward_offset_deg=offset,reward_center_deg=good,
       seed_block=k,seed=seed,shown_deg=shown,ring_ms=sham["times"][j][0],
       dots_ms=sham["times"][j][1],sham_choice_deg=a,stim_choice_deg=b,
       baseline_margin=baseline_margin,score_sup_delta=delta,
       argmax_invariance_cert=invariant,**m))
   if (k+1)%8==0:print(f"PROGRESS module={mod} blocks={k+1}/{args.seed_blocks}",flush=True)
 if len(rows)!=len(p09.PAIR_SETTINGS)*len(OFFSETS)*args.seed_blocks*72:
  raise RuntimeError("OUTPUT_ROW_COUNT_FAIL")
 keys=["module","reward_offset_deg"];counts={}
 for mod in ("MT","DLPFC"):
  counts[mod]={}
  for offset in OFFSETS:
   a=[x for x in rows if x["module"]==mod and x["reward_offset_deg"]==offset]
   n=len(a);eligible=sum(x["unique_geodesic_eligible"] for x in a)
   mean=lambda col:sum(float(x[col]) for x in a)/n
   totals={c:sum(int(x[c]) for x in a) for c in ("flipped","closer","farther","unique_short_arc_interior","antipodal","exactly_preferred","baseline_preferred","exact_endpoint","argmax_invariance_cert")}
   counts[mod][str(offset)]=dict(reward_center_deg=a[0]["reward_center_deg"],
      n=n,counts=totals,
      mean_preference_distance_delta_deg=mean("distance_delta_deg"),
      mean_source_training_target_change=mean("target_delta"),
      mean_baseline_source_target=mean("baseline_target"),
      mean_stim_source_target=mean("stim_target"),
      mean_baseline_reward_distance=mean("baseline_to_reward_distance"),
      mean_stim_reward_distance=mean("stim_to_reward_distance"),
      strict_short_arc_eligible_n=eligible,
      strict_short_arc_interior_fraction=(totals["unique_short_arc_interior"]/eligible if eligible else None))
 outcsv=args.output_dir/"xh_s6_rot012_author_native_reward_alignment_4contexts_13824_pairs.csv"
 with outcsv.open("w",newline="",encoding="utf8") as f:
  writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
 summary=dict(artifact_id="IW_XH_S6_ROT012_REWARD_ALIGNMENT_FOUR_CONTEXTS_SOURCE_MODEL_GATE_001_20261113",
 source_author_commit=AUTHOR,source_rot009_wrapper_git_blob=ROT009_SHA,
 original_paper_180deg_only=True,
 newly_intervened_reward_offsets_deg=OFFSETS,
 source_author_original_task_class_rerun=True,
 n_blocks=args.seed_blocks,n_shown_per_block=72,n_reward_contexts=4,n_units=2,
 paired_condition_rows=len(rows),source_model_arm_trials=2*len(rows),
 within_context_stochastic_pair_checks=paired_checks,cross_context_stream_identity_checks=context_checks,
 first_block_180deg_sham_repeat_bitwise="PASS",
 numeric_groups=counts,original_noisy_source_generator_250per_direction="NOT_RUN",
 monkey_behavior="NOT_ACCESSED",no_novelty=True,no_canon=True,no_exec_sign=True,
 elapsed_s=time.monotonic()-start,status="PASS")
 (args.output_dir/"xh_s6_rot012_author_native_reward_alignment_runner_summary.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf8")
 print("ROT012_FINAL_JSON_BEGIN")
 print(json.dumps(summary,sort_keys=True))
 print("ROT012_FINAL_JSON_END",flush=True)

if __name__=="__main__":run()
