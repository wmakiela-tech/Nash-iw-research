#!/usr/bin/env python3
"""ROT008: independent ORIGINAL RAW source 32-root linear vs shape-preserving PCHIP audit.

Run in clean git checkout of wmakiela-tech/Nash-iw-research:
  python3 research/mech-s10/2026-11-22/code/mech_s10_rot008_modern_generator_pchip_raw_referee.py output.json

Requires only Python3 standard library + git for exact source blob SHA checks.
Reimplements Fritsch-Carlson/PCHIP harmonic nodal slopes, Hermite root bisection.
Does not import owner analysis_090.py or use owner analysis090.json as input.
No Julia, no PYTHIA, no Herwig, no PRyMordial runs.
"""
import csv
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

BASE = Path("research/badacz/2026-11-21/data")
SOURCES = {
    "summary_orig_083.csv": "f7ea90eb3202933e9f52336315c1f36b3d40b019",
    "net083_raw.jsonl": "05f6f93eb4f53a95f5ad6fbe38609557bae04465",
    "summary_her_orig_085.csv": "347d928c2e75e6a2348c1304d3bc51109239386b",
    "net085_raw.jsonl": "4797209d5efec4bbc05f8799fcc5460df17f283b",
    "summary_p_orig_090.csv": "737eaccea9e8152d4f39bdfeb026577dc1744c6f",
    "summary_h_orig_090.csv": "c98450860cfb81484ff5cfb8dc120d00e29cc108",
    "net090_raw.jsonl": "3fbc134fd63cc6aa181e908d640d7482b56af46a",
}
ARMS = [
    ("PYBH", "summary_orig_083.csv", "net083_raw.jsonl", "o"),
    ("HERBH", "summary_her_orig_085.csv", "net085_raw.jsonl", "ho"),
    ("P83", "summary_p_orig_090.csv", "net090_raw.jsonl", "p"),
    ("H73", "summary_h_orig_090.csv", "net090_raw.jsonl", "h"),
]
TARGETS = (0.251, 0.2484)
MASSES = (22, 62)
MODELS = ("code", "net")
MODERATOR_MC_DMOD_ENVELOPE = 0.0224  # conditional ~2*0.0112 MC table-spread dex, not a confidence bound.

def verify_sources():
    for filename, sha in SOURCES.items():
        p = BASE / filename
        assert p.is_file(), ("SOURCE_MISSING", str(p))
        seen = subprocess.check_output(["git", "hash-object", str(p)], text=True).strip()
        assert seen == sha, ("SOURCE_BLOB_MISMATCH", filename, seen, sha)

def csv_records(filename):
    with (BASE / filename).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(line for line in f if line.strip() and not line.startswith("#")))

def net_records(filename):
    with (BASE / filename).open(encoding="utf-8") as f:
        values = [json.loads(line) for line in f if line.strip()]
    out = {}
    for row in values:
        assert row["run_id"] not in out, ("DUPLICATE_NET_ROW", row["run_id"])
        assert row["rc"] == 0 and math.isfinite(float(row["YP_BBN"]))
        out[row["run_id"]] = row
    return out

def sign(x):
    return (x > 0) - (x < 0)

def slopes(xs, ys):
    n = len(xs)
    h = [xs[i+1]-xs[i] for i in range(n-1)]
    s = [(ys[i+1]-ys[i])/h[i] for i in range(n-1)]
    assert all(x > 0 for x in h)
    out = [0.0]*n
    for i in range(1,n-1):
        if s[i-1] and s[i] and sign(s[i-1]) == sign(s[i]):
            w1, w2 = 2*h[i]+h[i-1], h[i]+2*h[i-1]
            out[i] = (w1+w2)/(w1/s[i-1]+w2/s[i])
    def end(h0,h1,s0,s1):
        v = ((2*h0+h1)*s0-h0*s1)/(h0+h1)
        if sign(v) != sign(s0):
            return 0.0
        if sign(s0) != sign(s1) and abs(v) > 3*abs(s0):
            return 3*s0
        return v
    out[0] = end(h[0],h[1],s[0],s[1])
    out[-1] = end(h[-1],h[-2],s[-1],s[-2])
    return out

def crossing(xs,ys,target):
    js=[i for i in range(len(xs)-1) if (ys[i]-target)*(ys[i+1]-target)<=0 and ys[i]!=ys[i+1]]
    assert len(js)==1, ("NONUNIQUE_BRACKET",target,js)
    i=js[0]
    dx=xs[i+1]-xs[i]
    linear=xs[i]+(target-ys[i])*dx/(ys[i+1]-ys[i])
    der=slopes(xs,ys)
    def cub(t):
        return ((2*t**3-3*t*t+1)*ys[i] + (t**3-2*t*t+t)*dx*der[i]
                + (-2*t**3+3*t*t)*ys[i+1] + (t**3-t*t)*dx*der[i+1])
    a,b=0.0,1.0
    leftsign=sign(ys[i]-target)
    for _ in range(72):
        mid=(a+b)/2
        if sign(cub(mid)-target)==leftsign:
            a=mid
        else:
            b=mid
    pchip=xs[i]+(a+b)*dx/2
    assert xs[i]<=pchip<=xs[i+1]
    return {"linear":linear, "pchip":pchip, "pchip_minus_linear":pchip-linear,
            "bracket":i,"bracket_width":dx}

def main(dst):
    verify_sources()
    assembled={}
    for label,src,nrc,prefix in ARMS:
        n=net_records(nrc)
        rows=csv_records(src)
        for j in MASSES:
            subset=sorted((r for r in rows if int(r["j"])==j and float(r["log10beta"])>-29),
                          key=lambda r: float(r["log10beta"]))
            assert len(subset)>=40
            x=[float(r["log10beta"]) for r in subset]
            ycode=[float(r["Y"]) for r in subset]
            ynet=[]
            for r in subset:
                assert r["run_id"].startswith(prefix+str(j)+"_")
                key="net_"+r["run_id"]
                assert key in n,("MISSING_NET_RATE",key)
                ynet.append(float(n[key]["YP_BBN"]))
            assembled[f"{label}_{j}"]=(x,ycode,ynet)
    roots={}
    for name,(xs,code,net) in assembled.items():
        for mod,ys in (("code",code),("net",net)):
            for target in TARGETS:
                roots[f"{name}|{mod}|{target}"]=crossing(xs,ys,target)
    assert len(roots)==32
    estimands={}
    for j in MASSES:
        for mod in MODELS:
            for target in TARGETS:
                key=f"{mod}|{target}"
                def r(name,interp):
                    return roots[f"{name}_{j}|{key}"][interp]
                values={}
                for interp in ("linear","pchip"):
                    values[interp]={
                        "dmod":r("H73",interp)-r("P83",interp),
                        "drepro":r("P83",interp)-r("PYBH",interp),
                        "dhold":r("HERBH",interp)-r("H73",interp),
                        "dgenBH":r("HERBH",interp)-r("PYBH",interp)
                    }
                    q=values[interp]
                    assert abs(q["dmod"]+q["drepro"]+q["dhold"]-q["dgenBH"])<1e-12
                values["dmod_pchip_minus_linear"]=values["pchip"]["dmod"]-values["linear"]["dmod"]
                estimands[f"{j}|{mod}|{target}"]=values
    root_max=max(abs(x["pchip_minus_linear"]) for x in roots.values())
    dmax=max(abs(x["dmod_pchip_minus_linear"]) for x in estimands.values())
    linear_values=[v["linear"]["dmod"] for v in estimands.values()]
    lower=min(linear_values)-dmax-MODERATOR_MC_DMOD_ENVELOPE
    upper=max(linear_values)+dmax+MODERATOR_MC_DMOD_ENVELOPE
    assert 0.10<lower<upper<0.27
    result={
        "artifact":"IW_MECH_S10_ROT008_GENERATOR090_INDEPENDENT_RAW_32_ROOTS_PCHIP_REFEREE",
        "source_git_blobs":SOURCES,"root_count":len(roots),"model_generator_cases":len(estimands),
        "roots":roots,"estimands":estimands,
        "max_abs_pchip_minus_linear_single_root":root_max,
        "max_abs_pchip_minus_linear_dmod":dmax,
        "dmod_all_cells_conservative_mc_plus_interp_envelope":[lower,upper],
        "classification_robust_for_declared_envelope":"MOD_INTERMEDIATE",
        "physical_claim":False,"network_executed":False,"julia_executed":False,
        "note":"MC ±0.0224 dex is illustrative owner empirical table-spread transfer, NOT a statistical confidence interval."
    }
    Path(dst).write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in
        ("root_count","model_generator_cases","max_abs_pchip_minus_linear_single_root",
         "max_abs_pchip_minus_linear_dmod","dmod_all_cells_conservative_mc_plus_interp_envelope")},indent=2))

if __name__ == "__main__":
    assert len(sys.argv)==2,"USAGE: python3 script.py OUTPUT.json"
    main(sys.argv[1])
