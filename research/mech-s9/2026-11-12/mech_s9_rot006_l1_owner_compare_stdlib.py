#!/usr/bin/env python3
"""Mech-S9 ROT006: independently inspect native L1 source CSV. Python stdlib.
Comparison to ORIGINAL Badacz REVIEW053 source CSVs; numeric solver is unchanged.
The root estimator here is independent linear bracketing, not Badacz's quadratic.
Never assert native Julia physical Yp/PBH bound from this diagnostics script.
"""
import argparse, csv, hashlib, io, json, math, pathlib, re, sys

NUMCOLS = ("m_g", "log10beta", "X_T0", "X_T1", "Yc_native", "Yc_recomp")
CAL = re.compile(r"^# SBBN j=(\d+) m_g=(\S+): X0s=(\S+) Ycode_native=(\S+) Ycode_recomp=(\S+) T1_MeV=(\S+) X1s=(\S+) seconds=(\S+)")
def parse_csv(p):
    s = pathlib.Path(p).read_text()
    comments = [x for x in s.splitlines() if x.startswith("#")]
    data = list(csv.DictReader(x for x in s.splitlines() if x.strip() and not x.startswith("#")))
    if any(not all(k in x for k in ("id", "j", *NUMCOLS, "seconds")) for x in data):
        raise ValueError(f"wrong CSV header {p}")
    calibrations = {}
    for x in comments:
        m = CAL.match(x)
        if m:
            calibrations[int(m.group(1))] = {k: float(v) for k, v in zip(("m_g", "X0s", "Ycode_native", "Ycode_recomp", "T1_MeV", "X1s", "seconds"), m.groups()[1:])}
    return comments, data, calibrations
def compare_rows(actual, baseline):
    ka = {(r["id"], int(r["j"]), r["log10beta"]):r for r in actual}
    kb = {(r["id"], int(r["j"]), r["log10beta"]):r for r in baseline}
    if len(ka) != len(actual) or len(kb) != len(baseline):
        raise ValueError("duplicate beta row key")
    if set(ka) != set(kb):
        raise ValueError(f"row identity differs missing={sorted(set(kb)-set(ka))}, unexpected={sorted(set(ka)-set(kb))}")
    out = {c: {"max_abs":0.,"max_rel":0.,"exact_decimal_matches":0,"n":len(ka)} for c in NUMCOLS}
    for key in sorted(ka):
        for c in NUMCOLS:
            va, vb = float(ka[key][c]),float(kb[key][c])
            if not (math.isfinite(va) and math.isfinite(vb)):
                raise ValueError(f"not finite {key} {c}")
            d=abs(va-vb); denom=max(abs(vb),1e-99)
            out[c]["max_abs"]=max(out[c]["max_abs"],d)
            out[c]["max_rel"]=max(out[c]["max_rel"],d/denom)
            out[c]["exact_decimal_matches"]+=int(ka[key][c]==kb[key][c])
    return out
def first_linear_root(points, field, zero):
    pairs=sorted(((float(r["log10beta"]),field(r)-zero) for r in points))
    for (x,y),(X,Y) in zip(pairs,pairs[1:]):
        if y<=0 and Y>=0 and Y!=y:
            return {"root_log10beta":x-y*(X-x)/(Y-y),"bracket":[x,X],"method":"first negative_to_positive crossing / linear interpolation"}
    return None
def root_groups(rows, X0s):
    gs={g:[r for r in rows if r["id"]==g] for g in sorted({r["id"] for r in rows})}
    res={}
    for gid,pt in gs.items():
        v0=first_linear_root(pt,lambda r:float(r["Yc_native"]),.251)
        v1=first_linear_root(pt,lambda r:2*float(r["X_T1"]),.251)
        v2=first_linear_root(pt,lambda r:2*float(r["X_T0"])-2*X0s,.006)
        res[gid]={"j":int(pt[0]["j"]),"n":len(pt),"V0":v0,"V1":v1,"V2":v2}
        if all((v0,v1,v2)):
            res[gid]["V1_minus_V0_dex"]=v1["root_log10beta"]-v0["root_log10beta"]
            res[gid]["V2_minus_V0_dex"]=v2["root_log10beta"]-v0["root_log10beta"]
    return res
def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
def main():
    a=argparse.ArgumentParser()
    a.add_argument("--actual",required=True)
    a.add_argument("--owner-a",required=True)
    a.add_argument("--owner-b",required=True)
    a.add_argument("--out-dir",required=True)
    args=a.parse_args()
    out=pathlib.Path(args.out_dir); out.mkdir(parents=True, exist_ok=True)
    ac,ar,acal=parse_csv(args.actual)
    ac1,oa,oca=parse_csv(args.owner_a)
    ac2,ob,ocb=parse_csv(args.owner_b)
    if len(ar)!=53 or len(oa)!=18 or len(ob)!=35:
        raise ValueError(f"expected 53 native points, 18 owner A,35 owner B; got {len(ar)}, {len(oa)},{len(ob)}")
    if set(acal)!={22,62} or set(oca)!={22,62} or set(ocb)!={22,62}:
        raise ValueError("SBBN calibration comments missing")
    cmax={k:max(abs(acal[j][k]-oca[j][k]),abs(acal[j][k]-ocb[j][k])) for j in [] for k in []}
    for j in (22,62):
        for k in ("X0s","Ycode_native","Ycode_recomp","T1_MeV","X1s"):
            cmax[f"j{j}_{k}"]=max(abs(acal[j][k]-oca[j][k]),abs(acal[j][k]-ocb[j][k]))
    keyA={r["id"] for r in oa}
    A=[r for r in ar if r["id"] in keyA]
    B=[r for r in ar if r["id"] not in keyA]
    if len(A)!=18 or len(B)!=35:
        raise ValueError("split original config not a 18+35 partition")
    a_stats=compare_rows(A,oa);b_stats=compare_rows(B,ob)
    columns=list(ar[0])
    for name,subset in (("replica_yp_a.csv",A),("replica_yp_b.csv",B)):
        with (out/name).open("w",newline="") as f:
            for comment in ac: f.write(comment+"\n")
            w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(subset)
    root_results=root_groups(ar,acal[22]["X0s"])
    max_numeric_rel=max(v["max_rel"] for d in (a_stats,b_stats) for k,v in d.items() if k not in ("m_g","log10beta"))
    report={
       "status":"FULL_L1_ORIGINAL_JULIA_DRIVER_NATIVE_REPLICATION_COMPARISON",
       "source_driver":"research/badacz/2026-11-08/code/wuxu_yp_formula_counterfactual.jl",
       "classification":"NONBLIND; owner values known, compared on separate source inputs",
       "source_ids": {"owner_yp_a_git_blob":"df78f479277d85c7a558e132428d8846c64f9512",
                      "owner_yp_b_git_blob":"a8f3fea64b46d5c42c69e155a3690b99581cc1aa"},
       "data_counts":{"actual":len(ar),"owner_a":len(oa),"owner_b":len(ob)},
       "source_file_sha256":{"actual":sha(args.actual),"owner_a":sha(args.owner_a),"owner_b":sha(args.owner_b)},
       "calibration_actual":acal,
       "calibration_max_abs_vs_owners":cmax,
       "row_comparison":{"a":a_stats,"b":b_stats},
       "root_method":"independent first monotone crossing linear interpolation, not owner 4-point quadratic",
       "roots":root_results,
       "max_numeric_relative_vs_owner":max_numeric_rel,
       "full_L1_all_reported_numeric_digits_match":max_numeric_rel==0 and max(cmax.values())==0,
       "nonclaims":["No independent L2 operator","No physics bound","No journal Fig5 source identity","No E4 spectra validation","No scientific referee signoff"]
    }
    (out/"L1_COMPARISON_AND_LINEAR_ROOTS.json").write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"counts":report["data_counts"],
       "numeric_max_relative":max_numeric_rel,
       "calibration_max_abs":max(cmax.values()),
       "exact":report["full_L1_all_reported_numeric_digits_match"],
       "linear_roots":root_results},indent=2))
    return 0
if __name__=="__main__":
    raise SystemExit(main())
