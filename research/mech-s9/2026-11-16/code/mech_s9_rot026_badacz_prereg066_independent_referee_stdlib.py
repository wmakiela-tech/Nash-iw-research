#!/usr/bin/env python3
"""Mech-S9 ROT026: independent stdlib audit of authorized Badacz B1 PREREG_066.
Native Julia runs are not performed. Reproduces archived observations and
pre-registered gates on the exact owner raw and original Wu-Xu archive.
Usage: python3 -I mech_s9_rot026_b1_066_independent_referee.py <badacz_dir> <author_scanning.jld2> <result.json>
"""
import json,sys,hashlib,struct,zlib,statistics,math
from pathlib import Path
from decimal import Decimal,localcontext

D=Path(sys.argv[1]); original=Path(sys.argv[2]); outfile=Path(sys.argv[3])
INPUT_SHAS={
 "data/b1_066_raw_outputs.json":"db4261be59d9f796094c10e57761608b1c0247f98d925ee1294970eb10e96ae",
 "data/analysis066.json":"b59a0a06bd3c13305bcb58e1676da0a5a780c5477d03cfc05928f8d1b236013c",
 "code/b1_066_analysis.py":"4bc59f6382bf0271fda78df5f47096415d13a8325d3b5659a10e5b41cee6e5d9",
 "code/b1_calibration_066.jl":"6382b7e4dc809fd512f259073c772c21cf0cdec11342b2ccab0a96eaba6fab76"
}
SCAN_SHA="51844a46ca904f57f941e0d0ebc3b5920c38bace76eea9e1d89cb5fd1f2c5786"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name,expect in INPUT_SHAS.items():
 assert sha(D/name)==expect,(name,"OWNER_BYTES_MISMATCH")
assert sha(original)==SCAN_SHA,"ORIGINAL_AUTHOR_JLD2_MISMATCH"
raw=json.loads((D/"data/b1_066_raw_outputs.json").read_text())
owner=json.loads((D/"data/analysis066.json").read_text())
names=("archive","A0u","A0","A1","A2","A3","A4","rep013")
assert set(raw["arms"])==set(names)
records={};integrity={}
for arm in names:
 v=raw["arms"][arm]
 assert v["status"]==0,(arm,"NATIVE_OWNER_RUN_NONZERO")
 b=("\n".join(v["jsonl_lines"])+"\n").encode()
 assert hashlib.sha256(b).hexdigest()==v["jsonl_sha256"],(arm,"JSONL_SOURCE_DIGEST")
 l=[json.loads(line) for line in v["jsonl_lines"]]
 assert len(l)==(15 if arm=="archive" else 2)
 assert l[0]["arm"]=="header" and l[0]["BITS"]==100
 assert l[0]["line_changed"]==(arm in ("A0","A1","A2","A3","A4"))
 records[arm]=l[1:]
 integrity[arm]={"line_count":len(l),"jsonl_sha256":v["jsonl_sha256"],
                  "native_exit_code":v["status"]}
b=original.read_bytes()
streams=[];i=0
while i<len(b)-2:
 if b[i]==120 and b[i+1] in (0x01,0x5e,0x9c,0xda):
  try:
   dz=zlib.decompressobj()
   expanded=dz.decompress(b[i:])
   used=len(b[i:])-len(dz.unused_data)
   if len(expanded)>=64 and len(expanded)%8==0:
    s=struct.unpack("<%dd"%(len(expanded)//8),expanded)
    streams.append(s);i+=used;continue
  except (zlib.error,ValueError,struct.error):pass
 i+=1
 candidates=[s for s in streams[2:] if s and max(s)<2]
assert len(candidates)>=1,"AUTHOR_ARCHIVE_Y_NOT_FOUND"
Y=candidates[0]
assert len(Y)==10000,"ARCHIVE_100X100"
archive=[]
for q in records["archive"]:
 assert q["j"]==22 and 86<=q["k"]<=99
 yarc=Y[100*q["k"]+22]
 archive.append({"k":q["k"],"original_archive_Y":yarc,
                 "native_Y":q["Y"],"native_minus_archive":q["Y"]-yarc})
assert [r["k"] for r in archive]==list(range(86,100))
ad=[r["native_minus_archive"] for r in archive]
A={"n":len(ad),"n_bit_equal":sum(z["native_Y"]==z["original_archive_Y"] for z in archive),
   "mean_native_minus_archive":statistics.fmean(ad),
   "sd_sample_native_minus_archive":statistics.stdev(ad),
   "max_abs_diff":max(map(abs,ad))}
A["verdict"]="A-BIT" if A["n_bit_equal"]==14 else (
 "A-NEAR" if all(abs(v)<=1e-12 for v in ad) else (
 "A-STAT" if max(map(abs,ad))<=3e-4 and abs(A["mean_native_minus_archive"])<=3e-5 else "A-MISMATCH"))
assert A["verdict"]==owner["A"]["verdict"]
assert A["n_bit_equal"]==owner["A"]["n_bit_equal"]
assert abs(A["mean_native_minus_archive"]-owner["A"]["mean_diff"])<2e-17
for n in ("A0u","A0","A1","A2","A3","A4","rep013"):
 assert len(records[n])==1
 v=records[n][0]
 assert v["Y"]>0 and 0<v["X_T0"]<1
 assert abs(v["Y"]/(2+v["Y"])-v["X_T0"])<1e-15
assert records["A0u"][0]["Y_big"]==records["A0"][0]["Y_big"]
assert records["A1"][0]["Y_big"]==records["A2"][0]["Y_big"]
C0b=records["A1"][0]["Y_big"]==records["A0"][0]["Y_big"]
assert C0b is False
A1=records["A1"][0];A0=records["A0"][0];A2=records["A2"][0]
assert A1["naccept"]==A2["naccept"]==1284 and A1["nreject"]==A2["nreject"]==82
assert A1["Y_big"]==A2["Y_big"]
assert A1["stop_bracket_M_g"]!=A2["stop_bracket_M_g"],"A2_SAMPLED_STEP_STATS_EXPECTED_TO_DIFFER"
assert records["A0"][0]["naccept"]==1290
assert records["A3"][0]["naccept"]==11395
assert records["A4"][0]["naccept"]==111836
x={n:records[n][0]["X_T0"] for n in ("A0","A1","A2","A3","A4")}
d34=x["A4"]-x["A3"]
def gate(ref):
 d03=x["A3"]-x[ref]
 return {"reference":ref,"dX_A3_minus_reference":d03,
   "dX_A4_minus_A3":d34,"abs_tightened_change":abs(d34),
   "half_reference_change":0.5*abs(d03),
   "condition_1":abs(d34)<=1e-5,
   "condition_2":abs(d34)<=0.5*abs(d03),
   "verdict":"RELEASE" if (abs(d34)<=1e-5 and abs(d34)<=0.5*abs(d03)) else "HOLD"}
g0=gate("A0");g1=gate("A1")
assert g0["verdict"]=="RELEASE" and g1["verdict"]=="HOLD"
assert abs(g0["dX_A3_minus_reference"]-owner["S"]["dX_A3_minus_A0"])<1e-17
assert abs(g0["dX_A4_minus_A3"]-owner["S"]["dX_A4_minus_A3"])<1e-17
Yrep=records["rep013"][0]
assert "%.17g"%Yrep["Y"]=="0.25239220435845267"
assert Yrep["first_nPBH_zero_index_1based"]==8545
with localcontext() as ctx:
 ctx.prec=70
 x70={n:Decimal(records[n][0]["X_T0_big"]) for n in ("A0","A1","A2","A3","A4")}
 exact_diff=x70["A1"]-x70["A0"]
 d34_exact=x70["A4"]-x70["A3"]
 margin0=abs(x70["A3"]-x70["A0"])/2-abs(d34_exact)
 margin1=abs(x70["A3"]-x70["A1"])/2-abs(d34_exact)
 decimal_stats={"X_A1_minus_A0":str(exact_diff),
                "X_A4_minus_A3":str(d34_exact),
                "prereg_A0_gate_margin_half_ref_minus_abs_change":str(margin0),
                "posthoc_A1_gate_margin_half_ref_minus_abs_change":str(margin1)}
 assert margin0>0>margin1
output={
 "identity":"IW_MECH_S9_ROT026_OWNER_PREREG066_INDEPENDENT_SOURCE_I1",
 "author_original_scanning_sha256":SCAN_SHA,
 "owner_file_sha256":INPUT_SHAS,"raw_jsonl_integrity":integrity,
 "original_14pt_archive_check":A,
 "source_gate_S_pre_registered_A0":g0,
 "source_gate_S_alternate_posthoc_A1":g1,
 "independent_decimal70":decimal_stats,
 "C0a_original_bit_identical":True,
 "C0b_original_bit_identical":C0b,
 "C0b_abs_X_delta":abs(x["A1"]-x["A0"]),
 "C0c_original_Y_and_step_stats_A1_A2_equal":True,
 "C0c_A2_saved_point_stats_do_not_equal_step_stats":True,
 "rep013_Y_code":Yrep["Y"],"rep013_first_zero_index":8545,
 "single_point_noise_window_X_max_minus_min":max(x[n] for n in ("A0","A1","A3","A4"))-min(x[n] for n in ("A0","A1","A3","A4")),
 "scientific_limits":["NOT A SECOND NATIVE JULIA RUN","NO CERTIFIED NOISE DISTRIBUTION",
 "C0b REPRESENTATION MECHANISM NOT ISOLATED BY RATIONAL_RELTOL_RUN",
 "GATE_S_PREREG_PASS_IS_REFERENCE_SENSITIVE","NO_PHYSICAL_PBH_BOUND",
 "NO_NOVELTY","NO_CANON","NO_EXEC_SIGN"]
}
outfile.write_text(json.dumps(output,ensure_ascii=False,indent=2,sort_keys=True)+"\n")
print(json.dumps({"A":A,"C0b":C0b,"S_A0":g0,"S_A1":g1,"decimal70":decimal_stats},indent=2))
