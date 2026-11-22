#!/usr/bin/env python3
"""ROT015: independent source-only original 103/104 GATE_FAIL preservation and
low-beta reference-choice partial-identification envelope.

Input: exactly ORIGINAL 103 Wu-Xu Julia summary source files for each mass,
the 083 baseline input, original 090 PYBH roots, original 103 gate output,
plus posthoc103 owner analysis as oracle only; every source Git blob pinned.

Method deliberately refuses to make new physical-model or stochastic solver
claims. Low-beta nodes are DIFFERENT beta input values, NOT i.i.d. replicates:
sample SD over nodes is descriptive, not solver noise sigma.
An envelope of f over individual source nodes is NOT a confidence interval,
nor a bound on the unknown real physical background effect under input change
of original hadron table times 1e-12.
No new native physics run. Python 3 stdlib only.
Execute at public Nash-iw-research checkout root with OUT.json argument.
"""
import csv
import json
import math
from pathlib import Path
import statistics
import subprocess
import sys

B=Path("research/badacz/2026-11-22")
D=Path("research/badacz/2026-11-21/data")
SOURCES={
    B/"data/analysis103.json":"4d1bce4e9a546a2b646075fd160b00bb81e7c46a",
    B/"data/posthoc103.json":"0f620491451c185f95eb1f5b782e78aeed837304",
    B/"data/summary_z22_103.csv":"921d7aeb225f822e359f9e2338a4beb2ee80057c",
    B/"data/summary_z62_103.csv":"2d22e83d2046ca6f0c0d86488c46bdef1b10de2c",
    B/"code/posthoc_103.py":"c8974b7afce63fd42cc279f65e58c64cf757291a",
    D/"analysis090.json":"2bae2cb7505e340ec6fe0db107be3070e8bd8923",
    D/"summary_orig_083.csv":"f7ea90eb3202933e9f52336315c1f36b3d40b019",
}
TARGETS=(0.251,0.2484)
CUTOFFS=(-19.5,-19.,-18.5,-18.,-17.75,-17.5,-17.25,-17.)
def source(path):
    assert path.is_file(),("MISSING",str(path))
    sha=subprocess.check_output(["git","hash-object",str(path)],text=True).strip()
    assert sha==SOURCES[path],("ORIGINAL_BLOB_MUTATED",str(path),sha,SOURCES[path])
    return path.read_text(encoding="utf-8")

def csv_rows(s):
    ll=[v for v in s.splitlines() if v.strip() and not v.startswith("#")]
    records=list(csv.DictReader(ll))
    assert len(records)==len({r["run_id"] for r in records})
    return records

def xhelium(Y):
    return Y/(2.0+Y)

def local_interp(grid,values,p):
    assert len(grid)==len(values) and len(grid)>=2
    assert all(grid[i]<grid[i+1] for i in range(len(grid)-1))
    assert grid[0]<=p<=grid[-1],("EXTRAPOLATION_REFUSED",p)
    for i in range(len(grid)-1):
        if grid[i]<=p<=grid[i+1]:
            h=(p-grid[i])/(grid[i+1]-grid[i])
            return (1-h)*values[i]+h*values[i+1],i
    raise ValueError("outside grid")

def pchip_derivatives(x,y):
    """Fritsch-Butland PCHIP, pure Python independent sensitivity only."""
    n=len(x)
    h=[x[i+1]-x[i] for i in range(n-1)]
    s=[(y[i+1]-y[i])/h[i] for i in range(n-1)]
    d=[0.]*n
    def edge(h0,h1,s0,s1):
        m=((2*h0+h1)*s0-h0*s1)/(h0+h1)
        if m*s0<=0: return 0.
        if s0*s1<0 and abs(m)>3*abs(s0):return 3*s0
        return m
    d[0]=edge(h[0],h[1],s[0],s[1])
    d[-1]=edge(h[-1],h[-2],s[-1],s[-2])
    for k in range(1,n-1):
        if s[k-1]*s[k]<=0:continue
        w1=2*h[k]+h[k-1]
        w2=h[k]+2*h[k-1]
        d[k]=(w1+w2)/(w1/s[k-1]+w2/s[k])
    return d

def pchip_one(x,y,level):
    d=pchip_derivatives(x,y)
    cross=[i for i in range(len(x)-1) if (y[i]-level)*(y[i+1]-level)<0]
    if len(cross)!=1:return None
    i=cross[0];h=x[i+1]-x[i]
    def at(t):
        a=2*t**3-3*t*t+1
        b=t**3-2*t*t+t
        c=-2*t**3+3*t*t
        e=t**3-t*t
        return a*y[i]+b*h*d[i]+c*y[i+1]+e*h*d[i+1]
    left=0.;right=1.
    sign=y[i]-level
    for _ in range(75):
        mid=(left+right)/2
        if (at(mid)-level)*sign>0:left=mid
        else:right=mid
    p=x[i]+(left+right)/2*h
    assert x[i]<p<x[i+1]
    return p, i

def main(dst):
    c={p:source(p) for p in SOURCES}
    a103=json.loads(c[B/"data/analysis103.json"])
    post=json.loads(c[B/"data/posthoc103.json"])
    a090=json.loads(c[D/"analysis090.json"])
    summary=csv_rows(c[D/"summary_orig_083.csv"])
    bases={row["run_id"]:float(row["Y"]) for row in summary}
    assert a103["gates"]["G_COMPLETE"]["pass"]
    assert a103["gates"]["G_RUN"]["pass"]
    assert a103["gates"]["G_DRIVER"]["pass"]
    assert not a103["gates"]["G_BASE"]["pass"]
    assert a103["labels"]["status"]=="GATE_FAIL_NO_LABEL"
    assert a103["predictions"]=={}
    assert post["label"]=="POST_HOC_NOT_PREREGISTERED"
    groups={}
    all_fraction_abs_7=[]
    all_fraction_abs_13=[]
    for j in ("22","62"):
        orig_csv=csv_rows(c[B/f"data/summary_z{j}_103.csv"])
        base=[r for r in orig_csv if r["run_id"]==f"z{j}_base"]
        source_nodes=[r for r in orig_csv if r["run_id"]!=f"z{j}_base"]
        assert len(base)==1 and len(source_nodes)==29
        assert len(orig_csv)==30
        source_nodes.sort(key=lambda r:float(r["log10beta"]))
        xx=[float(r["log10beta"]) for r in source_nodes]
        yy=[float(r["Y"]) for r in source_nodes]
        m=a103["masses"][j]
        assert xx==m["lb"] and yy==m["Y"],("SOURCE_NODE_ANALYSIS_MISMATCH",j)
        assert abs(float(base[0]["Y"])-statistics.mean(yy[:7]))>0.0001
        base_rel=(float(base[0]["Y"])-statistics.mean(yy[:7])) / statistics.stdev(yy[:7])
        assert abs(base_rel)>5 # descriptive standardization, NOT solver sigma
        cutoffs=[]
        for cmax in CUTOFFS:
            candidates=[val for x,val in zip(xx,yy) if x<=cmax+1e-9]
            assert len(candidates)>=3
            ymin,ymax=min(candidates),max(candidates)
            mref=statistics.mean(candidates)
            row={"max_logbeta_reference":cmax,
                "n_distinct_beta_reference_nodes":len(candidates),
                "Y_reference_mean":mref,
                "Y_reference_range":[ymin,ymax],
                "Y_reference_SD_across_beta_nodes_NOT_noise_sigma":statistics.stdev(candidates),
                "thresholds":{}}
            for t in TARGETS:
                key=str(t)
                lr=a090["roots"][f"PYBH_{j}|code|{t}"]["lb"]
                yz,idx=local_interp(xx,yy,lr)
                den=xhelium(t)-xhelium(bases[f"o{j}_base"])
                assert den>0
                fmean=(xhelium(yz)-xhelium(mref))/den
                fmin=(xhelium(yz)-xhelium(ymax))/den
                fmax=(xhelium(yz)-xhelium(ymin))/den
                assert fmin<=fmean<=fmax
                item={"PYBH_hadronic_threshold_original_logbeta":lr,
                      "Yz_source_linear_at_threshold":yz,
                      "native_bracketing_nodes_logbeta":[xx[idx],xx[idx+1]],
                      "f_mean":fmean,
                      "f_point_reference_envelope":[fmin,fmax],
                      "max_abs_fraction_over_any_selected_real_reference_node":max(abs(fmin),abs(fmax)),
                      "f_reference_mean_range_only_NOT_CONFIDENCE_INTERVAL":True,
                      "denominator_X_target_minus_original_083_base":den}
                if cmax==-18.5:
                    owner=post["masses"][j]["f"][key]
                    assert abs(owner["Yz"]-yz)<=1e-12
                    assert abs(owner["f"]-fmean)<=1e-12
                    assert abs(post["masses"][j]["Yref_mean"]-mref)<=1e-12
                    all_fraction_abs_7.append(item["max_abs_fraction_over_any_selected_real_reference_node"])
                if cmax==-17.:
                    all_fraction_abs_13.append(item["max_abs_fraction_over_any_selected_real_reference_node"])
                row["thresholds"][key]=item
            cutoffs.append(row)
        cross={}
        for t in TARGETS:
            v=post["masses"][j]["crossings"][str(t)]
            inds=[i for i in range(len(yy)-1)
                  if (yy[i]-t)*(yy[i+1]-t)<0]
            if j=="22":
                assert not inds and v=="NONE"
                cross[str(t)]={"native_bracket":"NONE","linear_root":"NONE","pchip_root":"NONE"}
                continue
            assert len(inds)==1 and isinstance(v,float)
            q=inds[0]
            lin=xx[q]+(t-yy[q])*(xx[q+1]-xx[q])/(yy[q+1]-yy[q])
            pchip=pchip_one(xx,yy,t)
            assert pchip is not None and abs(lin-v)<=1e-12
            cross[str(t)]={"native_bracket_logbeta":[xx[q],xx[q+1]],
                           "linear_root_logbeta":lin,
                           "pchip_interpolant_root_logbeta":pchip[0],
                           "pchip_minus_linear_dex":pchip[0]-lin,
                           "note":"Both are interpolants through existing 0.25-dex model samples, not a new native run or continuum error bound."}
        groups[j]={"native_original_source_rows":len(orig_csv),
                   "raw_beta1e_minus30_base_Y":float(base[0]["Y"]),
                   "predeclared_base_deviation_owner":a103["gates"]["G_BASE"]["absdiff"][j],
                   "descriptive_rawbase_distance_over_7distinct_beta_nodes_sample_SD_NOT_solver_sigma":base_rel,
                   "posthoc_reference_window_sensitivity":cutoffs,
                   "native_z_background_only_threshold_crossings":cross}
    assert len(all_fraction_abs_7)==len(all_fraction_abs_13)==4
    assert max(all_fraction_abs_7)<0.017
    assert max(all_fraction_abs_13)<0.031
    result={
        "id":"IW_MECH_S10_ROT015_BADACZ_REVIEW104_FAIL_GATE_AND_REF_RANGE_SENSITIVITY",
        "scientific_status":"ORIGINAL_NATIVE_SOURCE_POSTHOC_SENSITIVITY_ONLY; GATE_FAIL_NO_LABEL REMAINS",
        "all_source_git_blobs":{str(p):sha for p,sha in SOURCES.items()},
        "n_native_source_beta_nodes":58,
        "n_native_source_baselines":2,
        "original_prereg_gate_status":a103["labels"]["status"],
        "original_prereg_predictions_evaluated":False,
        "owner_fractions_replayed_exact_7node_window":True,
        "worst_abs_f_over_4_targets_and_any_reference_node_cutoff_minus18p5":max(all_fraction_abs_7),
        "worst_abs_f_over_4_targets_and_any_reference_node_cutoff_minus17":max(all_fraction_abs_13),
        "groups":groups,
        "negative_knowledge":["The 7 or 13 nodes use DIFFERENT beta physical inputs, are NOT replicate same-input solver runs; their sample SD cannot certify solver noise 1sigma.",
                              "The observed f envelopes are partially-identified calculations over an explicitly selected finite reference pool, not confidence intervals or physical model bounds.",
                              "The 0.25-dex source-grid linear and PCHIP roots do not certify continuum true physical threshold; no new native solver.",
                              "PREREG103 fail G_BASE cannot be promoted to PASS; all posthoc f and root summaries are observational only.",
                              "Cannot transfer the Wu-Xu background-only contrast to Kohri/Keith or settle 0.5–2.2dex difference without native source-typed external models."],
        "owner_firstness":"Badacz PREREG103 REVIEW104 actual 61 Julia runs, failed G_BASE, posthoc owner 7 nodes",
        "firstness_scope":"Mech source-only reference-pool envelope and alternative interpolant, not owner raw physics",
        "no_new_native_physics":True,"NO_CANON":True,"NO_EXEC_SIGN":True
    }
    Path(dst).write_text(json.dumps(result,sort_keys=True,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
    print(json.dumps({"src_native_beta_nodes":58,"max_f_abs_7":max(all_fraction_abs_7),
       "max_f_abs_13":max(all_fraction_abs_13),
       "original_gate":a103["labels"]["status"],
       "background_crossing":{j:groups[j]["native_z_background_only_threshold_crossings"] for j in groups},
       "base_descriptive_z":{j:groups[j]["descriptive_rawbase_distance_over_7distinct_beta_nodes_sample_SD_NOT_solver_sigma"] for j in groups}},indent=2))

if __name__=="__main__":
    assert len(sys.argv)==2, "usage python3 verifier.py output.json"
    main(sys.argv[1])
