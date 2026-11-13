#!/usr/bin/env python3
"""Mech-S9 ROT016: posthoc, source-native Wu-Xu six-hadron signed RHS exposure.
Reuses one authentic original 10D Julia source artifact, never calls Julia.
This is an on-path forcing integral, not a causal delta X or physical PBH bound.
Usage: python3 -I mech_s9_rot016_hadron_rhs_exposure_stdlib.py <source.zip> <out.json>
"""
import csv
import hashlib
import io
import json
import math
import sys
import zipfile
from pathlib import Path

EXPECTED_ZIP_SHA = "71db406d971a7ca19416b19766f32c312df2e1f6c96668b544b6efb1fd47f486"
EXPECTED_CSV_SHA = "45a65a1a079abed48102907b09ac8dc90f0fb731f1c2aaf6e7b55e199b5549f1"
HAD_NAMES = ("pi_minus", "pi_plus", "K_minus", "K0_L", "pbar", "nbar")
TABLE_NODE_G = 1e9

def integrate(method, t, y):
    assert len(t) == len(y) and len(t) >= 3
    h = [b-a for a,b in zip(t[:-1],t[1:])]
    assert all(v > 0 for v in h), "non-increasing original source times"
    if method == "left":
        return math.fsum(v*dt for v,dt in zip(y[:-1],h))
    if method == "right":
        return math.fsum(v*dt for v,dt in zip(y[1:],h))
    if method == "trapezoid":
        return math.fsum((a+b)*dt/2 for a,b,dt in zip(y[:-1],y[1:],h))
    if method != "pchip":
        raise ValueError(method)
    # Standard Fritsch–Butland shape-preserving cubic Hermite derivatives.
    sec = [(b-a)/dt for a,b,dt in zip(y[:-1],y[1:],h)]
    def end_slope(h0,h1,s0,s1):
        v = ((2*h0+h1)*s0-h0*s1)/(h0+h1)
        if s0==0 or math.copysign(1,v)!=math.copysign(1,s0):
            return 0.0
        if s0*s1 < 0 and abs(v)>abs(3*s0):
            return 3*s0
        return v
    d = [0.0]*len(y)
    d[0] = end_slope(h[0],h[1],sec[0],sec[1])
    d[-1] = end_slope(h[-1],h[-2],sec[-1],sec[-2])
    for k in range(1,len(y)-1):
        a,b=sec[k-1],sec[k]
        if a*b <= 0:
            d[k]=0.0
        else:
            w1=2*h[k]+h[k-1]
            w2=h[k]+2*h[k-1]
            d[k]=(w1+w2)/(w1/a+w2/b)
    return math.fsum(dt*((a+b)/2+dt*(da-db)/12)
                     for dt,a,b,da,db in zip(h,y[:-1],y[1:],d[:-1],d[1:]))

def run(zip_path):
    zipbytes=Path(zip_path).read_bytes()
    assert hashlib.sha256(zipbytes).hexdigest()==EXPECTED_ZIP_SHA, "original GitHub source ZIP tampered"
    with zipfile.ZipFile(io.BytesIO(zipbytes)) as z:
        assert z.testzip() is None, "GitHub original ZIP CRC failure"
        members=set(z.namelist())
        manifest=z.read("ARTIFACT_SHA256SUMS").decode().splitlines()
        assert len(manifest)==16, "expected 16 source digests"
        for line in manifest:
            digest, fname=line.split(maxsplit=1)
            base=fname.split("/")[-1]
            assert base in members
            assert hashlib.sha256(z.read(base)).hexdigest()==digest, base+" source SHA mismatch"
        raw=z.read("author_native_raw_hadron_history_10000.csv")
        assert hashlib.sha256(raw).hexdigest()==EXPECTED_CSV_SHA
        metadata=z.read("native_source_summary.txt").decode()
        assert "AUTHOR_NATIVE_MAGIC_CALL_COUNT=1" in metadata
        assert "ORIGINAL_FROZEN_COMMIT=d395183674cace6c9906a8911bdeb7234ba4040d" in metadata
    data=list(csv.DictReader(io.StringIO(raw.decode())))
    assert len(data)==10000
    T=[float(row["T_MeV"]) for row in data]
    t=[float(row["t_seconds"]) for row in data]
    M=[float(row["PBH_mass_g"]) for row in data]
    X=[float(row["Xn"]) for row in data]
    pbh=[int(row["nPBH_zero"]) for row in data]
    logs=[[float(row["lograw_"+s]) for s in HAD_NAMES] for row in data]
    flags=[[int(row["floor_active_"+s]) for s in HAD_NAMES] for row in data]
    assert all(a<b for a,b in zip(t[:-1],t[1:]))
    assert all(0<=x<=1 for x in X)
    for ls,fs in zip(logs,flags):
        assert all(f == int(v< -100) for v,f in zip(ls,fs))
    ev=next(i for i,f in enumerate(pbh) if f==1)
    assert all(v==0 for v in pbh[:ev]) and all(v==1 for v in pbh[ev:])
    assert ev==8544
    assert all(sum(fl)==0 for fl in flags[:ev])
    assert all(sum(fl)==6 for fl in flags[ev:])
    k=next(i for i in range(1,ev) if M[i]<TABLE_NODE_G)
    assert k==8383 and M[k-1]>TABLE_NODE_G and M[k]<TABLE_NODE_G

    # Derive units from exact SI definitions (not Mech-S9 original force output).
    h=6.62607015e-34
    c=299792458.0
    electric=1.602176634e-19
    hbar=h/(2*math.pi)
    gev_j=1e9*electric
    gev_inverse_meter=hbar*c/gev_j
    one_mb_in_gevm2=1e-31/(gev_inverse_meter**2)
    rate_const=one_mb_in_gevm2*gev_j/hbar
    ref=1.45148683724038e-19/math.exp(-100)
    assert abs(rate_const/ref)/ref<4e-9
    alpha_em=1/137.035999084
    def Fc(temp,mass):
        u=2*math.pi*alpha_em/(math.sqrt(temp/mass)+math.sqrt(temp/938.27208816))
        return u/(-math.expm1(-u))

    rates=[]
    weak=[]
    signed_components=[]
    for temp,x,raw in zip(T,X,logs):
        cp=Fc(temp,139.57039)
        ck=Fc(temp,493.677)
        coeff=((1-x)*1.5*cp,-x*1.7,
               (1-x)*31*ck-x*26,(1-2*x)*7,
               -x*28,(1-x)*28)
        components=[rate_const*math.exp(max(v,-100))*kval for v,kval in zip(raw,coeff)]
        signed_components.append(components)
        rates.append(math.fsum(components))
        q=(939.5654205-938.27208816)/temp
        gamma=(255/878.4)*(12+6*q+q*q)/(q**5)
        weak.append(-gamma*(x-(1-x)*math.exp(-q))-x/878.4)

    # Never integrate over the original PBH evaporation state discontinuity.
    # The mass-table crossing is estimated solely by LINEAR interpolation
    # of the two actual source output samples; it is not an exact ODE event.
    lam=(M[k-1]-TABLE_NODE_G)/(M[k-1]-M[k])
    tx=t[k-1]+lam*(t[k]-t[k-1])
    Tx=T[k-1]+lam*(T[k]-T[k-1])
    Xx=X[k-1]+lam*(X[k]-X[k-1])
    fx=rates[k-1]+lam*(rates[k]-rates[k-1])
    wx=weak[k-1]+lam*(weak[k]-weak[k-1])
    ta=t[:k]+[tx]
    fa=rates[:k]+[fx]
    tb=[tx]+t[k:ev]
    fb=[fx]+rates[k:ev]
    wa=weak[:k]+[wx]
    wb=[wx]+weak[k:ev]
    assert ta[-1]==tb[0] and tb[-1]==t[ev-1]
    methods={}
    for method in ("left","right","trapezoid","pchip"):
        a=integrate(method,ta,fa)
        b=integrate(method,tb,fb)
        methods[method]={"above_node_exposure":a,"below_node_exposure":b,
                         "fraction_below_node":b/(a+b),"sum":a+b}
    species={}
    for j,name in enumerate(HAD_NAMES):
        allc=[row[j] for row in signed_components]
        cross=allc[k-1]+lam*(allc[k]-allc[k-1])
        species[name]={
            "above_trapezoid":integrate("trapezoid",ta,allc[:k]+[cross]),
            "below_trapezoid":integrate("trapezoid",tb,[cross]+allc[k:ev]),
        }
    iu=integrate("trapezoid",tb,wb)
    ih=methods["trapezoid"]["below_node_exposure"]
    true_change=X[ev-1]-Xx
    result={
        "kind":"POSTHOC_SOURCE_NATIVE_SIGNED_HADRON_RHS_EXPOSURE_NOT_CAUSAL_ENDPOINT",
        "source_authors":"Wu and Xu",
        "author_original_commit":"d395183674cace6c9906a8911bdeb7234ba4040d",
        "source_original_GitHub_action":43436800793,
        "source_archive_sha256":EXPECTED_ZIP_SHA,
        "source_CSV_sha256":EXPECTED_CSV_SHA,
        "original_source_rows":10000,
        "six_hadron_rate_unit":"dXn/dt s^-1",
        "source_log_floor_minus_100_verified":True,
        "no_new_Julia_call":True,
        "scanned_betas_original_max_1e_17":True,
        "sample_is_out_of_original_beta_grid":True,
        "source_mass_table_first_node_g":TABLE_NODE_G,
        "crossing_bracket_1based":[k,k+1],
        "crossing_linear_estimate":{"t_sec":tx,"T_MeV":Tx,"Xn":Xx},
        "last_active_PBH_1based":ev,
        "first_zero_PBH_1based":ev+1,
        "last_active_t_sec":t[ev-1],
        "end_PBH_jump_not_integrated":True,
        "rate_conversion_per_mbarn_GeV3_to_s_inv":rate_const,
        "methods":methods,
        "per_species":species,
        "below_node_weak_integral_trapezoid":iu,
        "below_node_source_state_change":true_change,
        "below_node_rhs_trapezoid_minus_native_state_change":(ih+iu)-true_change,
        "above_below_hadron_forcing_positive_at_all_saved_live_samples":min(rates[:ev])>0,
        "scientific_ceilings":["NO_PHYSICAL_PBH_BOUND","NO_FULL_10D_COUNTERFACTUAL",
         "NO_HADRONIZATION_SOURCE_ERROR_CERTIFICATE","NO_CERTIFIED_NATIVE_ODE_ERROR",
         "NO_FIG5_EXECUTABLE_BUILD_ID","NO_NOVELTY","NO_CANON","NO_EXEC_SIGN"],
    }
    assert 0.70 < methods["trapezoid"]["fraction_below_node"] < 0.75
    assert abs(methods["trapezoid"]["fraction_below_node"] -
               methods["pchip"]["fraction_below_node"]) < 0.001
    return result

if __name__=="__main__":
    if len(sys.argv)!=3: raise SystemExit(__doc__)
    res=run(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(res,indent=2,sort_keys=True,ensure_ascii=False)+"\n")
    print(json.dumps({"trapezoid":res["methods"]["trapezoid"],"pchip":res["methods"]["pchip"],
      "below_node_rhs_state_residual":res["below_node_rhs_trapezoid_minus_native_state_change"]},indent=2))
