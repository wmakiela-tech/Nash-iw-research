#!/usr/bin/env python3
"""XH-S6 ROT010: four-arm source-native stochastic attribution & null-control.
Uses frozen original author task/psychrnn and frozen ROT009 source code.
Every shown direction is a cluster member of each independently seeded batch.
NOT animal data or original author 250-per-direction full protocol.
"""
from __future__ import annotations
import argparse, csv, hashlib, importlib.util, json, statistics, sys, time
from pathlib import Path
import numpy as np

AUTHOR_COMMIT = "7889a81e298c01532a313e02971c11dbc9db8eb0"
ROT009_GIT_BLOB = "054299b6b0f0c0def7cfa6b3600d6f56665375ce"
REQUIRED_OLD_COUNTS = {"MT":862,"DLPFC":616}

def gitblob(data:bytes)->str:
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def import_locked_rot009(script:Path):
    raw=script.read_bytes();got=gitblob(raw)
    if got!=ROT009_GIT_BLOB:
        raise RuntimeError(f"ROT009_SOURCE_SCRIPT_IDENTITY_FAIL expected={ROT009_GIT_BLOB} got={got}")
    spec=importlib.util.spec_from_file_location("xh_s6_rot009_original_frozen",script)
    mod=importlib.util.module_from_spec(spec);sys.modules[spec.name]=mod
    spec.loader.exec_module(mod)
    if mod.AUTHOR_COMMIT!=AUTHOR_COMMIT:raise RuntimeError("SOURCE_COMMIT_DRIFT")
    return mod

def run_arm(p09,cfg,mt,dp,sim_mt,sim_dp,seed,strength):
    return p09.execute_pair_arm(p09.DotsTasks,sim_mt,sim_dp,mt,dp,cfg,seed,strength)

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--author-python-data-dir",type=Path,required=True)
    p.add_argument("--rot009-source",type=Path,required=True)
    p.add_argument("--output-dir",type=Path,required=True)
    p.add_argument("--seed-blocks",type=int,default=60)
    args=p.parse_args()
    if not 12<=args.seed_blocks<=100:
        raise ValueError("BOUNDED_SEED_BLOCKS_EXPECTED_12_TO_100")
    p09=import_locked_rot009(args.rot009_source)
    root=args.author_python_data_dir.resolve()
    for key in p09.PINS:
        if key.endswith(".py"):p09.assert_original(root/key,p09.PINS[key])
    mt=p09.load_model(root/"model_weights/MTbroadsharp_m10.npz","MTbroadsharp_m10.npz")
    dp=p09.load_model(root/"model_weights/DLPFCcombined_m4.npz","DLPFCcombined_m4.npz")
    sys.path.insert(0,str(root))
    import DotsTasks
    from psychrnn.backend.simulation import BasicSimulator_linOut,BasicSimulator
    p09.DotsTasks=DotsTasks
    t0=time.monotonic()
    args.output_dir.mkdir(parents=True,exist_ok=True)
    fields=["module","unit","stim_strength","seed_index","base_seed","alternative_seed",
      "shown_deg","reward_deg","base_ring_ms","base_dots_ms","alt_ring_ms","alt_dots_ms",
      "base_choice_deg","paired_stim_choice_deg","independent_stim_choice_deg",
      "independent_sham_choice_deg","paired_alt_stim_choice_deg",
      "paired_stim_flip","unpaired_stim_flip","sham_random_flip","paired_alt_stim_flip",
      "base_top2_margin","paired_score_sup_delta","paired_invariance_certificate"]
    counts={};clusters={};row_count=0;violations=0;regression={}
    file=args.output_dir/"xh_s6_rot010_4arm_original_native_noise_attribution_rows.csv"
    with file.open("w",newline="",encoding="utf8") as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
        for cfg in p09.PAIR_SETTINGS:
            module=cfg["module"];cl=[];counters={k:0 for k in
             ["paired_stim_flip","unpaired_stim_flip","sham_random_flip","paired_alt_stim_flip","different_onsets"]}
            first12=0
            for block in range(args.seed_blocks):
                base=20261112+1009*block+(0 if module=="MT" else 400001)
                alt=base+10000007
                a=run_arm(p09,cfg,mt,dp,BasicSimulator_linOut,BasicSimulator,base,0)
                b=run_arm(p09,cfg,mt,dp,BasicSimulator_linOut,BasicSimulator,base,cfg["strength"])
                c=run_arm(p09,cfg,mt,dp,BasicSimulator_linOut,BasicSimulator,alt,0)
                d=run_arm(p09,cfg,mt,dp,BasicSimulator_linOut,BasicSimulator,alt,cfg["strength"])
                if a["params_digest"]!=b["params_digest"] or a["rng_digest"]!=b["rng_digest"]:
                    raise RuntimeError("BASE_PAIRED_STREAMS_OR_TIMES_NOT_IDENTICAL")
                if c["params_digest"]!=d["params_digest"] or c["rng_digest"]!=d["rng_digest"]:
                    raise RuntimeError("ALTERNATE_PAIRED_STREAMS_OR_TIMES_NOT_IDENTICAL")
                if module=="DLPFC":
                    if not np.array_equal(a["inputs"][:,:,:-1],b["inputs"][:,:,:-1]):
                        raise RuntimeError("BASE_DLPFC_UNMODIFIED_INPUTS_DIFFER")
                    if not np.array_equal(c["inputs"][:,:,:-1],d["inputs"][:,:,:-1]):
                        raise RuntimeError("ALT_DLPFC_UNMODIFIED_INPUTS_DIFFER")
                perblock={k:0 for k in
                 ["paired_stim_flip","unpaired_stim_flip","sham_random_flip","paired_alt_stim_flip"]}
                for i in range(72):
                    ac=int(a["choice"][i]);bc=int(b["choice"][i]);cc=int(c["choice"][i]);dc=int(d["choice"][i])
                    flags={"paired_stim_flip":int(ac!=bc),
                           "unpaired_stim_flip":int(ac!=dc),
                           "sham_random_flip":int(ac!=cc),
                           "paired_alt_stim_flip":int(cc!=dc)}
                    for key,v in flags.items():
                        perblock[key]+=v;counters[key]+=v
                    if a["times"][i]!=c["times"][i]:counters["different_onsets"]+=1
                    if block<12:first12+=flags["paired_stim_flip"]
                    base_scores=a["scores"][i];paired_scores=b["scores"][i]
                    margin=float(p09.margin(base_scores))
                    eps=float(np.max(np.abs(base_scores-paired_scores)))
                    certificate=int(eps<margin/2)
                    if flags["paired_stim_flip"] and certificate:
                        violations+=1;raise RuntimeError("ARGMAX_MARGIN_THEOREM_FALSE")
                    w.writerow({"module":module,"unit":cfg["unit"],"stim_strength":cfg["strength"],
                      "seed_index":block,"base_seed":base,"alternative_seed":alt,
                      "shown_deg":5*i,"reward_deg":cfg["reward_deg"],
                      "base_ring_ms":a["times"][i][0],"base_dots_ms":a["times"][i][1],
                      "alt_ring_ms":c["times"][i][0],"alt_dots_ms":c["times"][i][1],
                      "base_choice_deg":ac,"paired_stim_choice_deg":bc,
                      "independent_stim_choice_deg":dc,"independent_sham_choice_deg":cc,
                      "paired_alt_stim_choice_deg":dc,**flags,
                      "base_top2_margin":format(margin,".17g"),
                      "paired_score_sup_delta":format(eps,".17g"),
                      "paired_invariance_certificate":certificate})
                    row_count+=1
                cl.append({key:perblock[key]/72 for key in perblock})
                if (block+1)%20==0:
                    print(f"progress module={module} seedblocks={block+1}/{args.seed_blocks}",flush=True)
            if first12!=REQUIRED_OLD_COUNTS[module]:
                raise RuntimeError(f"ROT009_FIRST12_REGRESSION_FAIL module={module} observed={first12} expected={REQUIRED_OLD_COUNTS[module]}")
            counts[module]={"source_unit":cfg["unit"],"source_stim_strength":cfg["strength"],
             "seed_blocks":args.seed_blocks,"directions_per_block":72,"n_per_arm":args.seed_blocks*72,
             "observed_counts":counters,"frequencies":{k:v/(args.seed_blocks*72) for k,v in counters.items()},
             "per_seed_block_rate_stddev":{k:statistics.stdev([x[k] for x in cl]) for k in cl[0]},
             "per_seed_block_mean_rate":{k:statistics.mean([x[k] for x in cl]) for k in cl[0]},
             "first12_paired_stim_changes":first12,
             "first12_ROT009_regression":"PASS"}
            clusters[module]=cl
    expected=2*args.seed_blocks*72
    if row_count!=expected:raise RuntimeError("UNEXPECTED_ROW_COUNT")
    summary={"artifact_id":"IW_XH_S6_ROT010_FOUR_ARM_NOISE_TIMING_ATTRIBUTION_SOURCE_CONTROL_001_20261112",
      "source_author_repo_commit":AUTHOR_COMMIT,"original_rot009_script_git_blob":ROT009_GIT_BLOB,
      "source_original_git_sha":p09.PINS,"original_author_classes_executed":True,
      "original_source_nonzero_noise":True,
      "design":"4 arms: base sham/base stimulated identical RNG; alternative sham/alternative stimulated identical RNG. Cross-seed sham and stimulated introduce independent noise AND independent original random onset draws.",
      "n_seed_blocks_per_module":args.seed_blocks,"n_directions_per_block":72,
      "n_4arm_cases_per_module":args.seed_blocks*72,"observations":row_count,
      "total_model_arm_trials":row_count*4,
      "module_summaries":counts,"margin_theorem_violations":violations,
      "source_sham_pairing":"PASS","ROT009_first12_regression":"PASS",
      "full_author_250_per_direction":"NOT_RUN",
      "source_monkey_experimental_data":"NOT_ACCESSED",
      "no_novelty":True,"no_canon":True,"no_exec_sign":True,
      "run_seconds":time.monotonic()-t0,"status":"PASS"}
    (args.output_dir/"xh_s6_rot010_original_native_four_arm_summary.json").write_text(
      json.dumps(summary,indent=2,sort_keys=True)+"\n",encoding="utf8")
    (args.output_dir/"xh_s6_rot010_seed_block_rates.json").write_text(
      json.dumps(clusters,indent=2,sort_keys=True)+"\n",encoding="utf8")
    print("FINAL_RESULT_JSON_BEGIN")
    print(json.dumps(summary,sort_keys=True))
    print("FINAL_RESULT_JSON_END",flush=True)

if __name__=="__main__":main()
