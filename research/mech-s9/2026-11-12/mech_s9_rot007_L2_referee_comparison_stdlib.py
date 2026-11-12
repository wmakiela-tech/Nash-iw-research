#!/usr/bin/env python3
"""Mech-S9 ROT007 referee-neutral independent GPT L2 post-run comparison.
Parses independently written Julia native L2 roots; original Badacz results are
comparison targets only, NEVER passed to native Julia driver. stdlib Python.
"""
import csv, json, pathlib, hashlib, math, sys
if len(sys.argv)!=4:
    raise SystemExit("usage: independent_L2_roots.csv original_BADACZ_yp051_analysis.json out.json")
roots_path, owner_path, out_path = map(pathlib.Path, sys.argv[1:])
own=json.loads(owner_path.read_text())
rows=list(csv.DictReader(roots_path.open(newline="")))
if len(rows)!=6 or len({(r["j"],r["criterion"]) for r in rows})!=6:
    raise ValueError("expected exactly six unique native roots")
obs={}
for r in rows:
    j=int(r["j"])
    q=r["criterion"]
    if j not in (22,62) or q not in ("V0","V1","V2"): raise ValueError("unexpected native root")
    a,b,mid,reslo,reshi=map(float,[r["left_log10beta"],r["right_log10beta"],r["root_log10beta"],r["lo_residual"],r["hi_residual"]])
    if not (math.isfinite(mid) and a<mid<b and reslo<=0 and reshi>=0 and (b-a)<.002): 
        raise ValueError("source-root bracket invariants FAIL "+str(r))
    obs.setdefault(j,{})[q]=mid
result={"kind":"NONBLIND_NATIVE_ORIGINAL_AUTHOR_ODE_INDEPENDENT_GPT_DRIVER_AND_ADAPTIVE_BISECTION",
"scientific_status":"L2_SOURCE_NUMERIC_REPLICATION_ONLY",
"origin_owners":"Wu-Xu original magic() authors; Badacz REVIEW053 native results originally",
"target_windows_predeclared_by_EKS1":"j22 root<=0.02dex; j62 root<=0.01dex; shifts <=0.02dex",
"source_results_sha256":hashlib.sha256(roots_path.read_bytes()).hexdigest(),
"cases":{}, "all_within_predeclared_windows":True, "no_physical_PBH_bound":True}
for j in (22,62):
    expected=own["ids"][f"g{j}"]
    loc=obs[j]
    metrics={}
    for q in ("V0","V1","V2"):
        exp=float(expected[q]["root"])
        delta=loc[q]-exp
        win=.02 if j==22 else .01
        metrics[q]={"native":loc[q],"owner_quadratic":exp,"delta":delta,"abs_delta":abs(delta),"tolerance":win,"PASS":abs(delta)<=win}
    for key,aa,bb in (("shift_V1","V1","V0"),("shift_V2","V2","V0")):
        native=loc[aa]-loc[bb]
        exp=float(expected[key])
        metrics[key]={"native":native,"owner_quadratic":exp,"delta":native-exp,"tolerance":.02,"PASS":abs(native-exp)<=.02}
    result["cases"][str(j)]=metrics
    result["all_within_predeclared_windows"] &= all(x["PASS"] for x in metrics.values())
out_path.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
print(json.dumps(result,indent=2))
