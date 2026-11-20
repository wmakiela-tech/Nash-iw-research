#!/usr/bin/env python3
"""Mech-S10 standalone T2R 68-call native-output referee; written BEFORE execution.
Input: two fresh 34-row Julia source CSVs, two frozen owner CSVs.
No Badacz analyzer import, no reading Badacz derived roots, no SciPy/Numpy required.
Strict fail-closed native record validation; primary R-SHIFT <=0.010 dex each.
"""
import csv
import hashlib
import json
import math
import pathlib
import sys

TARGET=0.251
OWNER={22:0.2722992609128987,62:0.29812358518660886}
GRID={
    ("orig",22):(-17.38,-17.06),
    ("orig",62):(-19.54,-19.22),
    ("e5",22):(-17.10,-16.78),
    ("e5",62):(-19.26,-18.94),
}

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def read_csv(path):
    with path.open(encoding="utf-8",newline="") as f:
        return list(csv.DictReader(line for line in f if line.strip() and not line.startswith("#")))

def parse_native(arm,path):
    rows=read_csv(path)
    assert len(rows)==34,(arm,len(rows))
    obs={}
    for row in rows:
        assert row["arm"]==arm and row["tol"]=="default",row
        j=int(row["j"])
        assert j in (22,62)
        x=float(row["log10beta"])
        y=float(row["Y"])
        mass=float(row["m_g"])
        assert math.isfinite(x) and math.isfinite(y) and math.isfinite(mass)
        assert mass>0 and 0<y<1
        obs.setdefault(j,[]).append((x,y,row["Y"],row["m_g"]))
    assert set(obs)=={22,62}
    for j,s in obs.items():
        assert len(s)==17
        lo,hi=GRID[(arm,j)]
        expected=[round(lo+k*.02,6) for k in range(17)]
        assert abs(expected[-1]-hi)<1e-9
        assert [v[0] for v in s]==expected,(arm,j,s,expected)
        assert len(set(v[0] for v in s))==17
        assert len({v[3] for v in s})==1
    return obs

def seven_nearest_ols(arm,j,series):
    xx=[row[0] for row in series]
    yy=[row[1]-TARGET for row in series]
    crossings=[i for i in range(16) if yy[i]<0<=yy[i+1]]
    assert len(crossings)==1,(arm,j,"CROSSINGS",crossings,yy)
    i=crossings[0]
    x_lin=xx[i]-yy[i]*(xx[i+1]-xx[i])/(yy[i+1]-yy[i])
    chosen=sorted(range(17),key=lambda idx:(abs(xx[idx]-x_lin),idx))[:7]
    xx7=[xx[k] for k in chosen]
    yy7=[yy[k] for k in chosen]
    mx=sum(xx7)/7
    my=sum(yy7)/7
    sxx=sum((x-mx)**2 for x in xx7)
    sxy=sum((x-mx)*(y-my) for x,y in zip(xx7,yy7))
    assert sxx>0
    slope=sxy/sxx
    assert slope>0,(arm,j,slope)
    root=mx-my/slope
    assert min(xx)<root<max(xx)
    return dict(j=j,arm=arm,root_M_D=root,root_M_C=x_lin,
                ols7_indices_zero_based=sorted(chosen),
                slope=slope,crossing_left_index_zero_based=i,
                n=17,source_startY=series[0][1],source_endY=series[-1][1])

def owner_text_map(owner_path,arm):
    rows=read_csv(owner_path)
    out={}
    for row in rows:
        if int(row["j"]) in (22,62):
            assert row["arm"]==arm and row["tol"]=="default"
            key=(int(row["j"]),float(row["log10beta"]))
            assert key not in out
            out[key]=row["Y"]
    assert len(out)==34
    return out

def analyze(fresh_orig,fresh_e5,owner_orig,owner_e5):
    fresh={}
    owner={}
    byarm={}
    for arm,p,op in [("orig",fresh_orig,owner_orig),("e5",fresh_e5,owner_e5)]:
        byarm[arm]=parse_native(arm,p)
        owner[arm]=owner_text_map(op,arm)
        for j in (22,62):
            fresh[(arm,j)]=seven_nearest_ols(arm,j,byarm[arm][j])
    shifts={}
    matches={"exact_Y_text":0,"out_of_68":68,"by_arm_mass":{}}
    for arm in ("orig","e5"):
        for j in (22,62):
            count=0
            for x,y,yt,_ in byarm[arm][j]:
                assert (j,x) in owner[arm]
                if yt==owner[arm][(j,x)]:
                    count+=1
            matches["by_arm_mass"][arm+"_"+str(j)]=count
            matches["exact_Y_text"]+=count
    for j in (22,62):
        shift=fresh[("e5",j)]["root_M_D"]-fresh[("orig",j)]["root_M_D"]
        diff=shift-OWNER[j]
        shifts[str(j)]={
          "D_mech_s10_dex":shift,
          "D_badacz_owner_native_dex":OWNER[j],
          "abs_delta_dex":abs(diff),
          "R_SHIFT_gate":abs(diff)<=0.010,
          "beta_factor":10**shift,
          "orig_root":fresh[("orig",j)]["root_M_D"],
          "e5_root":fresh[("e5",j)]["root_M_D"],
        }
    verdict=all(v["R_SHIFT_gate"] for v in shifts.values())
    return {
      "artifact":"IW_MECH_S10_NATIVE68_T2R_INDEPENDENT_OUTPUT_AUDIT",
      "source":"ACTUAL_ORIGINAL_AUTHOR_JULIA_NATIVE_OUTPUT_ONLY",
      "new_native_calls_expected":68,
      "target":TARGET,
      "native_arms":{a:{str(j):fresh[(a,j)] for j in (22,62)} for a in ("orig","e5")},
      "shifts":shifts,
      "R_BIT_descriptive":matches,
      "R_SHIFT_TWO_MASSES_PASS":verdict,
      "result_state":"T2R_NATIVE68_PASS" if verdict else "T2R_NATIVE68_FAIL",
      "sha256_inputs":{p.name:digest(p) for p in (fresh_orig,fresh_e5,owner_orig,owner_e5)},
      "no_paper_error":True,
      "no_physical_pbh_bound":True,
      "no_canon":True,
      "no_exec_sign":True,
    }

def main():
    assert len(sys.argv)==6, "USAGE: new_orig new_e5 owner_orig owner_e5 output_json"
    inputs=[pathlib.Path(k) for k in sys.argv[1:]]
    out=analyze(*inputs[:4])
    inputs[4].write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"R_SHIFT":out["R_SHIFT_TWO_MASSES_PASS"],"shifts":out["shifts"],"R_BIT":out["R_BIT_descriptive"]},indent=2))
    if not out["R_SHIFT_TWO_MASSES_PASS"]:
        raise SystemExit(2)

if __name__=="__main__":
    main()
