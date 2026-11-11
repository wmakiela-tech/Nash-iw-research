#!/usr/bin/env python3
"""Mech-S8 ROT019: source-locked standalone REVIEW061 root-extraction audit.
Requires Python >=3.8 with HTTPS. No native Julia run or PBH physical bound.
For offline, use --p1 PATH --p2 PATH with original unmodified BADACZ CSVs.
GitHub pinned owner commit 47a8b457b90dd24886d2a5a96667aaf659dcccfd.
"""
import argparse, csv, hashlib, itertools, json
from pathlib import Path
from urllib.request import urlopen

COMMIT="47a8b457b90dd24886d2a5a96667aaf659dcccfd"
ROOT=("https://raw.githubusercontent.com/wmakiela-tech/Nash-iw-research/"
      +COMMIT+"/research/badacz/2026-11-11/data/")
BLOBS={"subedge060_p1.csv":"e8dc7702a4a4764fa8b3bffea64199b3258ffe0d",
       "subedge060_p2.csv":"99d5efca315e34ad77e2cfc602bff88785df548a"}
WINDOWS={22:(-0.07513393682254521,-0.009736483991748484),
         28:(-0.06231583371703794,0.0022229058910954586)}

def read(name, local):
    data=Path(local).read_bytes() if local else urlopen(ROOT+name,timeout=45).read()
    blob=hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
    assert blob==BLOBS[name], (name,blob,BLOBS[name])
    lines=(l for l in data.decode("utf-8").splitlines() if l and not l.startswith("#"))
    return list(csv.DictReader(lines))

def ols(pts):
    n=len(pts);xm=sum(x for x,y in pts)/n;ym=sum(y for x,y in pts)/n
    slope=sum((x-xm)*(y-ym) for x,y in pts)/sum((x-xm)**2 for x,y in pts)
    return xm+(0.251-ym)/slope

def secant(pts):
    for (x0,y0),(x1,y1) in zip(pts,pts[1:]):
        if y0<=0.251<=y1:
            return x0+(0.251-y0)*(x1-x0)/(y1-y0)
    raise AssertionError("No threshold crossing")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--p1");p.add_argument("--p2")
    args=p.parse_args()
    curves={}
    for name,source in [("subedge060_p1.csv",args.p1),
                        ("subedge060_p2.csv",args.p2)]:
        for row in read(name,source):
            if row["phase"]=="fit":
                curves.setdefault(row["id"],[]).append(
                    (float(row["log10beta"]),float(row["Yc"])))
    result={}
    for j in (22,28):
        base=sorted(curves["base"+str(j)+"u"])
        ramp=sorted(curves["ramp"+str(j)])
        assert len(base)==len(ramp)==7
        fits={}
        for n in (3,5,7):
            t=(7-n)//2
            fits["OLS"+str(n)]=ols(ramp[t:t+n])-ols(base[t:t+n])
        fits["secant"]=secant(ramp)-secant(base)
        loo=[ols([v for k,v in enumerate(ramp) if k!=i])-
             ols([v for k,v in enumerate(base) if k!=l])
             for i,l in itertools.product(range(7),repeat=2)]
        lo,hi=WINDOWS[j]
        assert len(loo)==49
        assert all(lo<=v<=hi and v<0 for v in list(fits.values())+loo)
        result[str(j)]={"fits":fits,"leave_one_out_pairs":49,
           "loo_range":[min(loo),max(loo)],
           "max_method_shift_from_OLS7":max(abs(v-fits["OLS7"]) for v in fits.values()),
           "preregistered_window":[lo,hi],"verdict":"PASS_ALL"}
    print(json.dumps({"return_id":"Mech-S8 ROT019","source_git_commit":COMMIT,
         "total_fit_rows":sum(len(v) for v in curves.values()),
         "method_check_count":8,"LOO_pair_count":98,"j":result,
         "claim_ceiling":"CSV_FIT_EXTRACTION_ONLY/NO_JULIA/NO_PBH_BOUND/NO_CANON/NO_EXEC_SIGN"},
         indent=2,sort_keys=True,allow_nan=False))

if __name__=="__main__":
    main()
