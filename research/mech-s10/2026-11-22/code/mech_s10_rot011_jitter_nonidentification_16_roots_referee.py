#!/usr/bin/env python3
"""ROT011: exact Wu-Xu parameter-vs-table scaling NO-GO and 16 genuine 094 J roots.

Scientific status: source-only exploratory I1. No original physics Julia/PRyMordial
run and no physical error or solver-noise decomposition. Python3 stdlib + git only.

From repository root:
 python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot011_jitter_nonidentification_16_roots_referee.py rot011.json

The external exact original Wu-Xu author source checked independently through GitHub:
Fenyutanchan/Primordial-Black-Hole @ d395183674cace6c9906a8911bdeb7234ba4040d
arXiv-2509.05618/main-scan.jl original blob
b368ba55d5a493f7bc185909730f7fe5691f10d6:
- nPBH ∝ beta, rhoPBH=m*nPBH, H=sqrt((rhoSM+rhoPBH)/(3MPl^2)).
- hadron S=hadron_table(m)*nPBH; d rhoSM/d eta contains
  -(dm/dt)*nPBH/(H*rhoSM). A table×f changes only hadron S,
  beta×f changes PBH background, H, thermal injection and hadron S.
This program verifies the resulting elementary exact dimensionless formula,
and quantifies the effect on raw owner roots without measuring its physical size.
"""
import csv
import json
import math
import statistics
import subprocess
import sys
from decimal import Decimal, getcontext
from pathlib import Path

D90=Path("research/badacz/2026-11-21/data")
D94=Path("research/badacz/2026-11-22/data")
SOURCES={
  D90/"summary_p_orig_090.csv":"737eaccea9e8152d4f39bdfeb026577dc1744c6f",
  D90/"summary_h_orig_090.csv":"c98450860cfb81484ff5cfb8dc120d00e29cc108",
  D90/"net090_raw.jsonl":"3fbc134fd63cc6aa181e908d640d7482b56af46a",
  D94/"summary_e_094.csv":"927fadfe870af71ed470c793c1c0bae9b98d7d9d",
  D94/"summary_f_094.csv":"50383cfcd6e54beba50fd33b953b2218c30e13e3",
  D94/"net094_raw.jsonl":"69443ff8cf6a54cdfec62d567802a20f6f132cc6",
  # Owner analyzed roots only as an AFTER-THE-FACT oracle
  D90/"analysis090.json":"2bae2cb7505e340ec6fe0db107be3070e8bd8923",
  D94/"analysis094.json":"1da0ec470973f4d9df9f549f894f67ba8481dbdf",
}
F=1.001
TARGETS=(0.251,0.2484)
MASSES=(22,62)
M=("code","net")

def lock_sources():
    for path,sha in SOURCES.items():
        assert path.is_file(),("MISSING",str(path))
        seen=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
        assert seen==sha,("SRC_WRONG_GIT_BLOB",str(path),seen,sha)

def csvrows(path):
    with path.open(encoding="utf8",newline="") as f:
        rows=list(csv.DictReader(l for l in f if l.strip() and not l.startswith("#")))
    assert len(rows)==len({r["run_id"] for r in rows})
    return rows

def netrows(path):
    with path.open(encoding="utf8") as f:
        rows=[json.loads(l) for l in f if l.strip()]
    assert len(rows)==len({r["run_id"] for r in rows})
    return {r["run_id"]:r for r in rows}

def crossed_root(points,Y):
    v=sorted(points)
    assert len(v)>=12 and len({x for x,y in v})==len(v)
    assert all(math.isfinite(x) and math.isfinite(y) for x,y in v)
    ii=[i for i in range(len(v)-1)
        if (v[i][1]-Y)*(v[i+1][1]-Y)<=0 and v[i][1]!=v[i+1][1]]
    assert len(ii)==1,("BAD_BRACKET",Y,ii)
    i=ii[0]; x0,y0=v[i];x1,y1=v[i+1]
    return x0+(Y-y0)*(x1-x0)/(y1-y0)

def exact_vector_field_witness():
    """At same eta, state (rhoSM, mPBH, T,...), with rhoPBH/rhoSM=r:
    H(beta*f)/H(beta)=sqrt((1+f*r)/(1+r)).
    heating_source(beta*f)/heating_source(table*f)
          =f*sqrt((1+r)/(1+f*r)).
    Both differ from unity for any r>0, f>1.
    J source table scaling does NOT change initial rhoPBH nor H or heating.
    """
    getcontext().prec=65
    f=Decimal("1.001")
    rvalues=[Decimal("1e-17"),Decimal("0.01"),Decimal("0.1"),Decimal("1")]
    results={}
    for r in rvalues:
        hb=((1+f*r)/(1+r)).sqrt()
        rt=f/hb
        assert hb>1 and rt>1
        results[str(r)]={"H_beta_scaled_over_H_table_scaled":str(hb),
                         "heating_beta_scaled_over_table_scaled":str(rt),
                         "dimensionless_rhoPBH_over_rhoSM":str(r)}
    # f=1 exact identity for all r; r=0 H equivalence is trivial.
    assert ((1+Decimal("1")*Decimal(".1"))/(1+Decimal(".1"))).sqrt()==1
    assert ((1+f*Decimal(0))/(1+Decimal(0))).sqrt()==1
    return results

def main(dst):
    lock_sources()
    N90=netrows(D90/"net090_raw.jsonl")
    N94=netrows(D94/"net094_raw.jsonl")
    assert len(N90)==193 and len(N94)==233
    table={
        "P83":(csvrows(D90/"summary_p_orig_090.csv"),csvrows(D94/"summary_e_094.csv"),N90,N94,"e"),
        "H73":(csvrows(D90/"summary_h_orig_090.csv"),csvrows(D94/"summary_f_094.csv"),N90,N94,"f"),
    }
    # Calculate independent all 16 nominal, J and aligned J roots, never use
    # owner's analyzed roots to calculate epsilon.
    observed={}
    for g,(raw,alter,net0,net1,arm) in table.items():
        assert len(raw)==94 and len(alter)==(39 if arm=="e" else 38)
        for j in MASSES:
            a=[x for x in raw if int(x["j"])==j]
            b=[x for x in alter if int(x["j"])==j]
            abase=[x for x in a if float(x["log10beta"])<=-29]
            bbase=[x for x in b if float(x["log10beta"])<=-29]
            assert len(abase)==len(bbase)==1
            for model in M:
                def val(row,net):
                    if model=="code":
                        return float(row["Y"])
                    key="net_"+row["run_id"]
                    assert key in net and net[key]["rc"]==0
                    return float(net[key]["YP_BBN"])
                diff=val(bbase[0],net1)-val(abase[0],net0)
                a_pts=[(float(x["log10beta"]),val(x,net0)) for x in a if float(x["log10beta"])>-29]
                b_pts=[(float(x["log10beta"]),val(x,net1)) for x in b if float(x["log10beta"])>-29]
                for U in TARGETS:
                    nominal=crossed_root(a_pts,U)
                    jroot=crossed_root(b_pts,U)
                    aligned=crossed_root([(x,y-diff) for x,y in b_pts],U)
                    eps=jroot-nominal+math.log10(F)
                    eps_aligned=aligned-nominal+math.log10(F)
                    observed[f"{g}|{j}|{model}|{U}"]={
                       "nominal_root":nominal,"J_root":jroot,"J_aligned_root":aligned,
                       "baseline_diff_Y":diff,
                       "epsilon_raw_dex":eps,"epsilon_aligned_dex":eps_aligned,
                       "root_delta_from_nom":jroot-nominal}
    assert len(observed)==16
    # Now post-computation check owner numerical roots (not source inputs).
    own90=json.loads((D90/"analysis090.json").read_text())
    own94=json.loads((D94/"analysis094.json").read_text())
    dif0=[];dif1=[]
    for key,v in observed.items():
        gen,j,model,t=key.split("|")
        dif0.append(abs(v["nominal_root"]-own90["roots"][f"{gen}_{j}|{model}|{t}"]["lb"]))
        dif1.append(abs(v["J_root"]-own94["roots"][f"{'e' if gen=='P83' else 'f'}_{j}|{model}|{t}"]["lb"]))
    assert max(dif0)<=1e-12 and max(dif1)<=1e-12

    raw=[abs(x["epsilon_raw_dex"]) for x in observed.values()]
    aligned=[abs(x["epsilon_aligned_dex"]) for x in observed.values()]
    assert len(raw)==len(aligned)==16
    verdict={
       "artifact":"IW_MECH_S10_ROT011_J_TABLE_SCALING_IS_NOT_BETA_SCALING_AND_NO_PURE_SOLVER_NOISE_ID",
       "original_author_source":{
          "git_repo":"Fenyutanchan/Primordial-Black-Hole",
          "git_commit":"d395183674cace6c9906a8911bdeb7234ba4040d",
          "path":"arXiv-2509.05618/main-scan.jl",
          "git_blob":"b368ba55d5a493f7bc185909730f7fe5691f10d6",
          "read_live_independently":True,
          "not_fetched_in_this_source_only_GHA":True,
       },
       "source_git_blob_locked":{str(k):v for k,v in SOURCES.items()},
       "source_native_16_nominal_roots_owner_match_max_abs":max(dif0),
       "source_native_16_J_roots_owner_match_max_abs":max(dif1),
       "n_source_roots_nominal":16,"n_source_roots_J":16,
       "n_diagnostic_roots_aligned":16,
       "f":F,"ideal_uniform_beta_shift_dex":-math.log10(F),
       "abs_epsilon_raw_median_dex":statistics.median(raw),
       "abs_epsilon_raw_max_dex":max(raw),
       "abs_epsilon_aligned_median_dex":statistics.median(aligned),
       "abs_epsilon_aligned_max_dex":max(aligned),
       "n_abs_epsilon_raw_gt005":sum(x>.005 for x in raw),
       "n_abs_epsilon_aligned_gt005":sum(x>.005 for x in aligned),
       "vector_field_exact_dimensionless_witness":exact_vector_field_witness(),
       "observed":observed,
       "claim_ceiling":"epsilon = source-table-to-beta-model-non-equivalence + numerical perturbations + other model effects; decomposition unresolved, not a certified solver sigma",
       "no_native_physics_executed":True
    }
    assert verdict["abs_epsilon_raw_max_dex"]>.009
    assert verdict["abs_epsilon_aligned_max_dex"]>.017
    assert verdict["n_abs_epsilon_raw_gt005"]==8
    assert verdict["n_abs_epsilon_aligned_gt005"]==9
    Path(dst).write_text(json.dumps(verdict,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:verdict[k] for k in [
       "n_source_roots_nominal","n_source_roots_J","n_diagnostic_roots_aligned",
       "source_native_16_nominal_roots_owner_match_max_abs",
       "source_native_16_J_roots_owner_match_max_abs",
       "ideal_uniform_beta_shift_dex",
       "abs_epsilon_raw_median_dex","abs_epsilon_raw_max_dex",
       "abs_epsilon_aligned_median_dex","abs_epsilon_aligned_max_dex",
       "n_abs_epsilon_raw_gt005","n_abs_epsilon_aligned_gt005"
       ]},indent=2))
if __name__=="__main__":
    assert len(sys.argv)==2,"Usage: python3 script.py OUT.json"
    main(sys.argv[1])
