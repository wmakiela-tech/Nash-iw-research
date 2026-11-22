#!/usr/bin/env python3
"""IW/Mech-S10 ROT009: ORIGINAL-RAW source-only generator x model interaction sign referee.

Reads 6 original 094 native Julia CSV, 094 network JSONL, 2 original 090 native
CSV, 090 network JSONL, optional 094 k identity CSV, plus READ-ONLY 094
author analysis for comparison AFTER roots are derived.
Enforces exact Git SHA provenance before using source. Standard library only.
Independent bracketed linear roots, 48 new 094 +16 nominal 090=64.
No native Julia, BlackHawk, PYTHIA, Herwig or PRyMordial execution.
Numerical findings are post hoc exploratory diagnostics, not registered hypotheses.
"""
import csv
import json
import math
from pathlib import Path
import subprocess
import sys

B94=Path("research/badacz/2026-11-22/data")
B90=Path("research/badacz/2026-11-21/data")
SOURCE={
  B94/"summary_a_094.csv":"bda49a039733f42eb8ec2d22bb2bf5f3b8e1344f",
  B94/"summary_b_094.csv":"397ed92f95a222a5838075f3f8baf77124dd4001",
  B94/"summary_c_094.csv":"908d9f97da6de93c52f04c13dc99103f2a38fea8",
  B94/"summary_d_094.csv":"a8242a8f396b82f34f2ce163f9696aff0e690b95",
  B94/"summary_e_094.csv":"927fadfe870af71ed470c793c1c0bae9b98d7d9d",
  B94/"summary_f_094.csv":"50383cfcd6e54beba50fd33b953b2218c30e13e3",
  B94/"summary_k_094.csv":"2a55be306502feb1ed10833939709edd60d62589",
  B94/"net094_raw.jsonl":"69443ff8cf6a54cdfec62d567802a20f6f132cc6",
  B90/"summary_p_orig_090.csv":"737eaccea9e8152d4f39bdfeb026577dc1744c6f",
  B90/"summary_h_orig_090.csv":"c98450860cfb81484ff5cfb8dc120d00e29cc108",
  B90/"net090_raw.jsonl":"3fbc134fd63cc6aa181e908d640d7482b56af46a"
}
POSTHOC_SOURCE={
  B94/"analysis094.json":"1da0ec470973f4d9df9f549f894f67ba8481dbdf",
  B90/"analysis090.json":"2bae2cb7505e340ec6fe0db107be3070e8bd8923",
}
CELLS=[(j,t) for j in (22,62) for t in (0.251,0.2484)]
REAL={"NOM":("p","h"),"J":("e","f"),"R1":("a","b"),"R2":("c","d")}
ARM_N={"a":39,"b":38,"c":39,"d":38,"e":39,"f":38,"k":1}

def hashcheck(path,sha):
    assert path.is_file(),("MISSING",str(path))
    seen=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
    assert seen==sha,("WRONG_GIT_BLOB",str(path),seen,sha)

def csv_read(path):
    with path.open(newline="",encoding="utf-8") as f:
        rr=list(csv.DictReader(line for line in f if line.strip() and not line.startswith("#")))
    assert len({x["run_id"] for x in rr})==len(rr),("DUPLICATE",str(path))
    return rr

def net_read(path):
    with path.open(encoding="utf-8") as f:
        rr=[json.loads(l) for l in f if l.strip()]
    assert len({v["run_id"] for v in rr})==len(rr)
    return {x["run_id"]:x for x in rr}

def bracketed_linear(records, model, target):
    assert len(records)>=12
    data=sorted((float(r["log10beta"]),float(r["Y"]) if model=="code" else float(r["YP_BBN"])) for r in records)
    xs=[z[0] for z in data]
    assert len(set(xs))==len(xs)
    assert all(math.isfinite(v) for tup in data for v in tup)
    candidates=[i for i in range(len(data)-1) if
                (data[i][1]-target)*(data[i+1][1]-target)<=0 and data[i][1]!=data[i+1][1]]
    assert len(candidates)==1,("MULTIPLE_OR_NO_ROOT",model,target,candidates)
    i=candidates[0]; (l,a),(r,b)=data[i:i+2]
    return {"root":l+(target-a)*(r-l)/(b-a),
            "bracket":[l,r],"slope":(b-a)/(r-l)}

def main(path):
    for p,s in {**SOURCE,**POSTHOC_SOURCE}.items():
        hashcheck(p,s)
    N94=net_read(B94/"net094_raw.jsonl")
    N90=net_read(B90/"net090_raw.jsonl")
    assert len(N94)==233 and len(N90)==193
    docs={}
    for arm in "abcdefk":
        docs[arm]=csv_read(B94/f"summary_{arm}_094.csv")
        assert len(docs[arm])==ARM_N[arm]
    for arm in "ph":
        docs[arm]=csv_read(B90/f"summary_{arm}_orig_090.csv")
        assert len(docs[arm])==94
    k=docs["k"][0]
    p90=next(x for x in docs["p"] if x["run_id"]=="p22_1720")
    assert float(k["Y"])==float(p90["Y"])
    assert N94["net_k22_1720"]["YP_BBN"]==N90["net_p22_1720"]["YP_BBN"]
    assert N94["net_base"]["YP_BBN"]==N90["net_base"]["YP_BBN"]
    R={}
    for instance,(pa,ha) in REAL.items():
        for arm in (pa,ha):
            net=N90 if instance=="NOM" else N94
            for j in (22,62):
                rows=[]
                for r in docs[arm]:
                    if int(r["j"])!=j or float(r["log10beta"])<=-29:
                        continue
                    key="net_"+r["run_id"]
                    assert key in net,(instance,arm,key)
                    assert net[key].get("rc")==0 and "YP_BBN" in net[key]
                    rows.append({**r,"YP_BBN":net[key]["YP_BBN"]})
                assert len(rows)>=12
                for model in ("code","net"):
                    for target in (0.251,0.2484):
                        R[f"{instance}|{arm}|{j}|{model}|{target}"]=bracketed_linear(rows,model,target)
    assert len(R)==64

    # Only NOW consult owners' analysis as an external test oracle. It never
    # supplies roots to the interaction calculation.
    a94=json.loads((B94/"analysis094.json").read_text())
    a90=json.loads((B90/"analysis090.json").read_text())
    e94=[];e90=[]
    for k,z in R.items():
        instance,arm,j,model,target=k.split("|")
        if instance=="NOM":
            owner=f'{"P83" if arm=="p" else "H73"}_{j}|{model}|{target}'
            e90.append(abs(z["root"]-a90["roots"][owner]["lb"]))
        else:
            owner=f"{arm}_{j}|{model}|{target}"
            e94.append(abs(z["root"]-a94["roots"][owner]["lb"]))
    assert max(e94)<=1e-12 and max(e90)<=1e-12

    bycell={};all_dmods=[]
    for j,target in CELLS:
        key=f"{j}|{target}"
        cell={}
        for instance,(pa,ha) in REAL.items():
            def root(arm,model):
                return R[f"{instance}|{arm}|{j}|{model}|{target}"]["root"]
            dcode=root(ha,"code")-root(pa,"code")
            dnet=root(ha,"net")-root(pa,"net")
            I=dnet-dcode
            I2=(root(ha,"net")-root(ha,"code"))-(root(pa,"net")-root(pa,"code"))
            assert abs(I-I2)<1e-12
            assert 0.10<=dcode<0.27 and 0.10<=dnet<0.27
            cell[instance]={"dmod_code":dcode,"dmod_net":dnet,
                            "I_model_generator":I,"I_rearranged":I2,"sign":(I>0)-(I<0)}
            all_dmods.extend((dcode,dnet))
        signs=[cell[r]["sign"] for r in REAL]
        fresh=[cell[r]["sign"] for r in ("J","R1","R2")]
        vi=[cell[r]["I_model_generator"] for r in REAL]
        bycell[key]={"j":j,"target":target,"instances":cell,
                     "sign_mixed_including_nominal":len(set(signs))>1,
                     "sign_mixed_fresh_only":len(set(fresh))>1,
                     "interaction_span":max(vi)-min(vi)}
    mixed_all=sum(x["sign_mixed_including_nominal"] for x in bycell.values())
    mixed_fresh=sum(x["sign_mixed_fresh_only"] for x in bycell.values())
    assert mixed_all==4 and mixed_fresh==3
    result={
      "artifact":"IW_MECH_S10_ROT009_B1_GENERATOR_BY_BBN_MODEL_INTERACTION_SIGN_INSTABILITY_SOURCE_REFEREE",
      "status":"POSTHOC_EXPLORATORY_SOURCE_ONLY_INTERNAL_I1",
      "source_git_blob_checks":{str(k):v for k,v in SOURCE.items()},
      "owner_analysis_used_only_as_output_oracle":{str(k):v for k,v in POSTHOC_SOURCE.items()},
      "n_root_total":64,"n_new_094_roots":len(e94),"n_nominal_090_roots":len(e90),
      "max_source_root_vs_owner_094":max(e94),"max_source_root_vs_owner_090":max(e90),
      "n_dmod_evaluations":len(all_dmods),"dmod_min":min(all_dmods),"dmod_max":max(all_dmods),
      "n_cells":len(CELLS),"n_cells_sign_flips_incl_nominal":mixed_all,
      "n_cells_sign_flips_fresh_only":mixed_fresh,
      "max_interaction_span":max(x["interaction_span"] for x in bycell.values()),
      "cells":bycell,
      "claim_ceiling":"NUMERICAL_SAME_ORIGINAL_PHYSICS / NO_INFERRED_SIGN_FOR_PHYSICAL_INTERACTION / NO_CONFIDENCE_INTERVAL / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN",
      "no_native_physics_rerun":True
    }
    Path(path).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in
      ("n_root_total","n_new_094_roots","n_nominal_090_roots",
       "max_source_root_vs_owner_094","max_source_root_vs_owner_090","n_dmod_evaluations",
       "dmod_min","dmod_max","n_cells_sign_flips_incl_nominal",
       "n_cells_sign_flips_fresh_only","max_interaction_span")},indent=2))
if __name__=="__main__":
    assert len(sys.argv)==2,"USAGE: python3 referee.py results.json"
    main(sys.argv[1])
