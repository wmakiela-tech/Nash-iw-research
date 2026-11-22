#!/usr/bin/env python3
"""Mech-S10 ROT012: source-only independent 146 SAME-BETA J vs nominal pairs.

New comparator (distinct from LT9 ROT015 deltaY=.001*(Y-Ybase) test):
the LOCAL FINITE-GRID beta-rescaling counterfactual
  Y_nom(beta*1.001)-Y_nom(beta)
estimated from nearest RIGHT and LEFT nominal original beta slopes.
The physically EXACT rescaled-beta solver result is UNKNOWN; the 0.05 dex
grid proxy is NOT a theorem or actual original Wu-Xu β-rescale run.
No Julia, Herwig, PYTHIA, PRyMordial, BlackHawk or new physics calls.

Requires Python3 standard library + git hash-object on approved source checkout.
Run from Nash-iw-research repository root:
  python3 -I research/mech-s10/2026-11-22/code/mech_s10_rot012_local_beta_derivative_vs_J_source_146_pairs_referee.py rot012.json
"""
import csv
import json
import math
from pathlib import Path
import statistics
import subprocess
import sys

BASE90=Path("research/badacz/2026-11-21/data")
BASE94=Path("research/badacz/2026-11-22/data")
SOURCES={
    BASE90/"summary_p_orig_090.csv":"737eaccea9e8152d4f39bdfeb026577dc1744c6f",
    BASE90/"summary_h_orig_090.csv":"c98450860cfb81484ff5cfb8dc120d00e29cc108",
    BASE90/"net090_raw.jsonl":"3fbc134fd63cc6aa181e908d640d7482b56af46a",
    BASE94/"summary_e_094.csv":"927fadfe870af71ed470c793c1c0bae9b98d7d9d",
    BASE94/"summary_f_094.csv":"50383cfcd6e54beba50fd33b953b2218c30e13e3",
    BASE94/"net094_raw.jsonl":"69443ff8cf6a54cdfec62d567802a20f6f132cc6",
}
F=1.001
D=math.log10(F)
def rms(vals):
    assert vals
    return math.sqrt(sum(x*x for x in vals)/len(vals))
def sig(x):
    return (x>0)-(x<0)

def file_authenticity():
    for p, expected in SOURCES.items():
        assert p.is_file(), ("MISSING",str(p))
        h=subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
        assert h==expected, ("WRONG_GIT_SOURCE",str(p),h,expected)

def csv_read(path):
    with path.open(encoding="utf8",newline="") as f:
        a=list(csv.DictReader(l for l in f if l.strip() and not l.startswith("#")))
    assert len(a)==len({row["run_id"] for row in a})
    return a

def net_read(path):
    with path.open(encoding="utf8") as f:
        a=[json.loads(line) for line in f if line.strip()]
    assert len(a)==len({row["run_id"] for row in a})
    return {row["run_id"]:row for row in a}

def one_group(gen,j,model,nom,J,net_nom,net_J):
    def Y(r,net):
        if model=="code":
            return float(r["Y"])
        ref="net_"+r["run_id"]
        assert ref in net and net[ref].get("rc")==0,("INVALID_NETWORK_ROW",ref)
        return float(net[ref]["YP_BBN"])
    base_nom=[r for r in nom if int(r["j"])==j and float(r["log10beta"])<=-29]
    base_J=[r for r in J if int(r["j"])==j and float(r["log10beta"])<=-29]
    assert len(base_nom)==len(base_J)==1
    dbase=Y(base_J[0],net_J)-Y(base_nom[0],net_nom)
    original=sorted([(float(r["log10beta"]),Y(r,net_nom))
                     for r in nom if int(r["j"])==j and float(r["log10beta"])>-29])
    assert len(original)==46 and len(original)==len({x for x,y in original})
    new=sorted([(float(r["log10beta"]),Y(r,net_J))
                for r in J if int(r["j"])==j and float(r["log10beta"])>-29])
    assert len(new)>=15 and len(new)==len({x for x,y in new})
    result=[]
    for x,yn in new:
        idx=next((i for i,p in enumerate(original) if abs(p[0]-x)<1e-10),None)
        assert idx is not None and 0<idx<len(original)-1,("NOT_IN_NATIVE_INTERIOR",gen,j,model,x)
        left=original[idx-1];cur=original[idx];right=original[idx+1]
        hL=cur[0]-left[0]; hR=right[0]-cur[0]
        assert hL>0 and hR>0 and D<hR,("OUTSIDE_FINITE_GRID_CELL",x,D,hR)
        slope_left=(cur[1]-left[1])/hL
        slope_right=(right[1]-cur[1])/hR
        proxy_right=D*slope_right
        proxy_left=D*slope_left
        observed=yn-cur[1]
        result.append({
          "log10beta":x,
          "Y_nominal":cur[1],
          "Y_J":yn,
          "deltaY_J_observed":observed,
          "deltaY_beta_proxy_right":proxy_right,
          "deltaY_beta_proxy_left":proxy_left,
          "residual_right":observed-proxy_right,
          "residual_left":observed-proxy_left,
          "residual_right_baseline_aligned":observed-dbase-proxy_right,
          "two_sided_positive":proxy_left>0 and proxy_right>0,
          "sign_mismatch_right":sig(observed)!=sig(proxy_right),
          "sign_mismatch_left":sig(observed)!=sig(proxy_left),
          "sign_mismatch_both_two_sided_positive":proxy_left>0 and proxy_right>0 and observed<0,
          "slope_left":slope_left,"slope_right":slope_right,
          "deltaY_beta_proxy_secant_span":abs(proxy_right-proxy_left),
          "original_step_right":hR,
          "nominal_baseline_difference_to_J":dbase
        })
    return result

def stats(group):
    raw=[x["deltaY_J_observed"] for x in group]
    R=[x["deltaY_beta_proxy_right"] for x in group]
    L=[x["deltaY_beta_proxy_left"] for x in group]
    resid=[x["residual_right"] for x in group]
    residL=[x["residual_left"] for x in group]
    aligned=[x["residual_right_baseline_aligned"] for x in group]
    return {
        "n":len(group),
        "RMS_deltaY_J":rms(raw),
        "RMS_beta_proxy_right":rms(R),
        "RMS_beta_proxy_left":rms(L),
        "RMS_J_minus_beta_proxy_right":rms(resid),
        "RMS_J_minus_beta_proxy_left":rms(residL),
        "RMS_alignedJ_minus_beta_proxy_right":rms(aligned),
        "ratio_RMS_J_minus_beta_proxy_to_RMS_proxy":rms(resid)/rms(R),
        "sign_mismatches_right":sum(x["sign_mismatch_right"] for x in group),
        "sign_mismatches_left":sum(x["sign_mismatch_left"] for x in group),
        "sign_mismatches_both_positive_secants":sum(x["sign_mismatch_both_two_sided_positive"] for x in group),
        "two_sided_positive_secants":sum(x["two_sided_positive"] for x in group),
        "negative_J_observed":sum(x["deltaY_J_observed"]<0 for x in group),
        "negative_beta_proxy_right":sum(x["deltaY_beta_proxy_right"]<0 for x in group),
        "max_neighbor_secant_proxy_span":max(x["deltaY_beta_proxy_secant_span"] for x in group)
    }

def main(out_path):
    file_authenticity()
    files={
        "p":csv_read(BASE90/"summary_p_orig_090.csv"),
        "h":csv_read(BASE90/"summary_h_orig_090.csv"),
        "e":csv_read(BASE94/"summary_e_094.csv"),
        "f":csv_read(BASE94/"summary_f_094.csv")
    }
    assert len(files["p"])==len(files["h"])==94
    assert len(files["e"])==39 and len(files["f"])==38
    net90=net_read(BASE90/"net090_raw.jsonl")
    net94=net_read(BASE94/"net094_raw.jsonl")
    assert len(net90)==193 and len(net94)==233
    groups={}
    for gen,nom,J in (("P83","p","e"),("H73","h","f")):
        for j in (22,62):
            for model in ("code","net"):
                key=f"{gen}|{j}|{model}"
                groups[key]=one_group(gen,j,model,files[nom],files[J],net90,net94)
    allrows=[row for group in groups.values() for row in group]
    assert len(allrows)==146,("WRONG_NMATCHED",len(allrows))
    s=stats(allrows)
    assert s["n"]==146
    assert s["RMS_J_minus_beta_proxy_right"]>10*s["RMS_beta_proxy_right"]
    assert s["sign_mismatches_right"]>=65
    assert s["negative_J_observed"]>=65
    # Explicit negative knowledge: the original 0.05dex source-grid
    # derivative/linear interpolation is not the true β-rescaled solver
    # output, nor is residual a certified solver noise distribution.
    result={
      "artifact":"IW_MECH_S10_ROT012_LOCAL_BETA_DERIVATIVE_146_SOURCE_PAIR_REFEREE",
      "lineage":"IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10",
      "mode":"POSTHOC_ORIGINAL_RAW_SOURCE_ONLY_COUNTERFACTUAL_FINITE_GRID",
      "owner_badacz_firstness":"REVIEW_095 J_232_native_233_PRyMordial",
      "lt9_prior_different_null_firstness":"LT9_ROT015_NULL001 proportional_excess 146 data pairs",
      "new_counterfactual":"Y_nom(beta*1.001)-Y_nom(beta) estimated via right nominal local secant; left nominal slope alternative; no actual beta rescale",
      "original_source_git_blobs":{str(k):v for k,v in SOURCES.items()},
      "scaling_factor_f":F,
      "delta_log10_beta":D,
      "groups":groups,
      "per_group":{k:stats(v) for k,v in groups.items()},
      "total":s,
      "caveat":"Not a numerical tolerance/solver-only noise estimation or a physical exact beta-rescaling experiment. Cannot infer deterministic-versus-noise fractional contributions or CI.",
      "native_physics_executed":False,
      "canon":False,"exec_sign":False,"novelty_claim":False
    }
    Path(out_path).write_text(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps({"total":s,"per_group":result["per_group"]},indent=2))

if __name__=="__main__":
    assert len(sys.argv)==2,"usage: python3 source_only.py out.json"
    main(sys.argv[1])
