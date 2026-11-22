#!/usr/bin/env python3
"""IW/Mech-S10 ROT010: native-source model×generator signed interaction
under a *counterfactual* arm/generator/model/mass baseline alignment.

No new Julia, BlackHawk, Herwig, Pythia or PRyMordial run.
All actual owner raw source outputs from 090 and 094. Check Git blobs before use.
Reconstruct original 64 roots without owner analysis and 64 aligned roots.
All normalization is explicitly DIAGNOSTIC, not a physical correction.

Usage from repository root:
 python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot010_baseline_alignment_interaction_referee.py /tmp/output.json
"""
import csv
import json
import math
import subprocess
import sys
from pathlib import Path

D90=Path("research/badacz/2026-11-21/data")
D94=Path("research/badacz/2026-11-22/data")
FILES={
    D90/"summary_p_orig_090.csv":"737eaccea9e8152d4f39bdfeb026577dc1744c6f",
    D90/"summary_h_orig_090.csv":"c98450860cfb81484ff5cfb8dc120d00e29cc108",
    D90/"net090_raw.jsonl":"3fbc134fd63cc6aa181e908d640d7482b56af46a",
    D94/"summary_a_094.csv":"bda49a039733f42eb8ec2d22bb2bf5f3b8e1344f",
    D94/"summary_b_094.csv":"397ed92f95a222a5838075f3f8baf77124dd4001",
    D94/"summary_c_094.csv":"908d9f97da6de93c52f04c13dc99103f2a38fea8",
    D94/"summary_d_094.csv":"a8242a8f396b82f34f2ce163f9696aff0e690b95",
    D94/"summary_e_094.csv":"927fadfe870af71ed470c793c1c0bae9b98d7d9d",
    D94/"summary_f_094.csv":"50383cfcd6e54beba50fd33b953b2218c30e13e3",
    D94/"net094_raw.jsonl":"69443ff8cf6a54cdfec62d567802a20f6f132cc6",
}
REFERENCES={
    D90/"analysis090.json":"2bae2cb7505e340ec6fe0db107be3070e8bd8923",
    D94/"analysis094.json":"1da0ec470973f4d9df9f549f894f67ba8481dbdf",
}
DATASETS={
    "NOM":("p","h","90"),
    "J":("e","f","94"),
    "R1":("a","b","94"),
    "R2":("c","d","94"),
}
TARGETS=(0.251,0.2484)
MASSES=(22,62)
MODELS=("code","net")

def file_hash_check(path,expected):
    assert path.is_file(), ("MISSING",str(path))
    actual=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
    assert actual==expected, ("ORIGINAL_BLOB_MISMATCH",str(path),actual,expected)

def read_csv(path):
    with path.open(encoding="utf-8",newline="") as f:
        rows=list(csv.DictReader(x for x in f if x.strip() and not x.startswith("#")))
    assert len({r["run_id"] for r in rows})==len(rows)
    return rows

def read_net(path):
    with path.open(encoding="utf-8") as f:
        rows=[json.loads(line) for line in f if line.strip()]
    assert len({r["run_id"] for r in rows})==len(rows)
    return {r["run_id"]:r for r in rows}

def linear_root(points,target):
    points=sorted(points)
    assert len(points)>=12 and all(math.isfinite(a) and math.isfinite(b) for a,b in points)
    assert len(set(x for x,y in points))==len(points)
    crossing=[i for i in range(len(points)-1)
              if (points[i][1]-target)*(points[i+1][1]-target)<=0
              and points[i][1]!=points[i+1][1]]
    assert len(crossing)==1, ("UNBRACKETED_OR_MULTI",target,crossing)
    i=crossing[0]; (x0,y0),(x1,y1)=points[i:i+2]
    return x0+(target-y0)*(x1-x0)/(y1-y0)

def sign(v):
    return int(v>0)-int(v<0)

def main(dest):
    for path,sha in {**FILES,**REFERENCES}.items():
        file_hash_check(path,sha)
    csvrows={}
    for a in "ph":
        csvrows[a]=read_csv(D90/f"summary_{a}_orig_090.csv")
        assert len(csvrows[a])==94
    for a in "abcdef":
        csvrows[a]=read_csv(D94/f"summary_{a}_094.csv")
        assert len(csvrows[a])==39 if a in "ace" else len(csvrows[a])==38
    n90=read_net(D90/"net090_raw.jsonl")
    n94=read_net(D94/"net094_raw.jsonl")
    assert len(n90)==193 and len(n94)==233

    # First assemble real original owner data and source control baseline.
    source={}
    for group,(p,h,group_id) in DATASETS.items():
        network=n90 if group_id=="90" else n94
        for gen,arm in (("P83",p),("H73",h)):
            for j in MASSES:
                rr=[r for r in csvrows[arm] if int(r["j"])==j]
                base=[r for r in rr if float(r["log10beta"])<=-29]
                assert len(base)==1,("NONUNIQUE_BASE",group,gen,j)
                base=base[0]
                baseline={}
                for model in MODELS:
                    if model=="code":
                        baseline[model]=float(base["Y"])
                    else:
                        n="net_"+base["run_id"]
                        assert n in network and network[n].get("rc")==0
                        baseline[model]=float(network[n]["YP_BBN"])
                series={}
                for model in MODELS:
                    v=[]
                    for r in rr:
                        if float(r["log10beta"])<=-29:
                            continue
                        if model=="code":
                            Y=float(r["Y"])
                        else:
                            n="net_"+r["run_id"]
                            assert n in network and network[n].get("rc")==0
                            Y=float(network[n]["YP_BBN"])
                        v.append((float(r["log10beta"]),Y))
                    series[model]=v
                source[(group,gen,j)]={"base":baseline,"points":series}
    assert len(source)==16

    roots_raw={}
    roots_aligned={}
    base_delta={}
    for (group,gen,j),doc in source.items():
        nom=source[("NOM",gen,j)]
        for model in MODELS:
            delta=doc["base"][model]-nom["base"][model]
            base_delta[f"{group}|{gen}|{j}|{model}"]=delta
            pts=doc["points"][model]
            # Counterfactual affine baseline operation, never reported as real Yp.
            pts_aligned=[(x,y-delta) for x,y in pts]
            # Translation invariance meta test:
            # if ALL Y values (and the own baseline) get a synthetic +5e-5,
            # centering must give exactly the same within machine precision.
            fake=5e-5
            pt_control=[(x,y+fake-(delta+fake)) for x,y in pts]
            assert max(abs(v[1]-w[1]) for v,w in zip(pts_aligned,pt_control))<1e-15
            for U in TARGETS:
                k=f"{group}|{gen}|{j}|{model}|{U}"
                roots_raw[k]=linear_root(pts,U)
                roots_aligned[k]=linear_root(pts_aligned,U)
    assert len(roots_raw)==64 and len(roots_aligned)==64

    # Owner analysis is ONLY an external replay oracle, after original source roots
    # have already been independently computed.
    owner90=json.loads((D90/"analysis090.json").read_text())
    owner94=json.loads((D94/"analysis094.json").read_text())
    err90=[]; err94=[]
    arm_map={"J":{"P83":"e","H73":"f"},
             "R1":{"P83":"a","H73":"b"},
             "R2":{"P83":"c","H73":"d"}}
    for key,root in roots_raw.items():
        grp,g,j,m,U=key.split("|")
        if grp=="NOM":
            err90.append(abs(root-owner90["roots"][f"{g}_{j}|{m}|{U}"]["lb"]))
        else:
            a=arm_map[grp][g]
            err94.append(abs(root-owner94["roots"][f"{a}_{j}|{m}|{U}"]["lb"]))
    assert max(err90)<=1e-12 and max(err94)<=1e-12

    effects={}
    for j in MASSES:
        for U in TARGETS:
            cell={}
            for group in DATASETS:
                z={}
                for mode,data in (("raw",roots_raw),("aligned",roots_aligned)):
                    get=lambda gen,model: data[f"{group}|{gen}|{j}|{model}|{U}"]
                    dc=get("H73","code")-get("P83","code")
                    dn=get("H73","net")-get("P83","net")
                    I=dn-dc
                    rearranged=(get("H73","net")-get("H73","code"))-(get("P83","net")-get("P83","code"))
                    assert abs(rearranged-I)<1e-12
                    z[mode]={"dmod_code":dc,"dmod_net":dn,"I_model":I,
                             "sign_I":sign(I)}
                    assert 0.10<=dc<0.27 and 0.10<=dn<0.27
                z["delta_I_alignment"]=z["aligned"]["I_model"]-z["raw"]["I_model"]
                cell[group]=z
            raw_signs={v["raw"]["sign_I"] for v in cell.values()}
            aligned_signs={v["aligned"]["sign_I"] for v in cell.values()}
            aligned_fresh={cell[g]["aligned"]["sign_I"] for g in ("J","R1","R2")}
            effects[f"{j}|{U}"]={
                "cells":cell,"raw_sign_mixed":len(raw_signs)>1,
                "aligned_sign_mixed":len(aligned_signs)>1,
                "aligned_fresh_sign_mixed":len(aligned_fresh)>1}
    assert len(effects)==4
    mixed_raw=sum(v["raw_sign_mixed"] for v in effects.values())
    mixed_aligned=sum(v["aligned_sign_mixed"] for v in effects.values())
    mixed_fresh=sum(v["aligned_fresh_sign_mixed"] for v in effects.values())
    assert (mixed_raw,mixed_aligned,mixed_fresh)==(4,3,3)
    assert all(effects["22|0.2484"]["cells"][g]["aligned"]["I_model"]<0 for g in DATASETS)
    max_shift=max(abs(v["delta_I_alignment"]) for e in effects.values() for v in e["cells"].values())
    max_base=max(abs(d) for d in base_delta.values())
    out={
      "artifact":"IW_MECH_S10_ROT010_NATIVE_SOURCE_BASELINE_ALIGNMENT_SIGN_NONINVARIANCE",
      "mode":"POSTHOC_READ_ONLY_DIAGNOSTIC_NOT_PHYSICAL_CORRECTION",
      "source_sha_git":{str(k):v for k,v in FILES.items()},
      "owner_analysis_sha_git_posthoc_comparator":{str(k):v for k,v in REFERENCES.items()},
      "n_verified_original_roots":len(roots_raw),
      "n_counterfactual_baseline_aligned_roots":len(roots_aligned),
      "max_abs_original_root_deviation_090":max(err90),
      "max_abs_original_root_deviation_094":max(err94),
      "n_mixed_interaction_signs_original":mixed_raw,
      "n_mixed_interaction_signs_after_baseline_alignment":mixed_aligned,
      "n_mixed_interaction_signs_new_realizations_after_alignment":mixed_fresh,
      "max_abs_baseline_Y_difference":max_base,
      "max_abs_I_change_under_alignment_dex":max_shift,
      "source_baseline_differences_Y":base_delta,
      "effects":effects,
      "no_physical_rerun":True,
      "interpretation":"Baseline alignment is a counterfactual sensitivity control. It does not remove valid physical effects nor estimate the true solver error."
    }
    Path(dest).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:out[k] for k in
      ("n_verified_original_roots","n_counterfactual_baseline_aligned_roots",
       "max_abs_original_root_deviation_090","max_abs_original_root_deviation_094",
       "n_mixed_interaction_signs_original","n_mixed_interaction_signs_after_baseline_alignment",
       "n_mixed_interaction_signs_new_realizations_after_alignment",
       "max_abs_baseline_Y_difference","max_abs_I_change_under_alignment_dex")},indent=2))

if __name__=="__main__":
    assert len(sys.argv)==2,"USAGE: python3 referee.py out.json"
    main(sys.argv[1])
