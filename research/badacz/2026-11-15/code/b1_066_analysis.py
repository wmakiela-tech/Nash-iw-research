#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_066 (written before any run; the native run itself awaits Moderator authorization).
Inputs: JSONL outputs of code/b1_calibration_066.jl (one file per arm) and the authors' scanning.jld2.
A: Float64(Y) of arm 'archive' versus Y_P_mat[22, k] (k = 86..99): A-BIT / A-NEAR / A-STAT / A-MISMATCH.
B: C0a (A0u == A0 bitwise), C0b (A1 == A0 bitwise), C0c |Y(A2) - Y(A1)| classes; gate S on X_T0 = Y/(2+Y):
   RELEASE if |X(A4)-X(A3)| <= 1e-5 and |X(A4)-X(A3)| <= 0.5 |X(A3)-X(A0)|, else HOLD.
C: rep013 versus Mech-S9 ROT013 published values.
Usage: python3 -I b1_066_analysis.py <dir with arm_*.jsonl> <scanning.jld2> <out.json>
"""
import json, os, sys, zlib, numpy as np

D, jld, outp = sys.argv[1], sys.argv[2], sys.argv[3]
def arm(name):
    p = os.path.join(D, "arm_%s.jsonl" % name)
    if not os.path.exists(p):
        return None
    rows = [json.loads(l) for l in open(p) if l.strip()]
    return {"header": rows[0], "rows": rows[1:]}
b = open(jld, "rb").read(); streams = []; i = 0
while i < len(b) - 2:
    if b[i] == 0x78 and b[i + 1] in (0x01, 0x5e, 0x9c, 0xda):
        try:
            d = zlib.decompressobj(); o = d.decompress(b[i:]); used = len(b[i:]) - len(d.unused_data)
            if len(o) >= 64:
                streams.append(np.frombuffer(o, "<f8")); i += used; continue
        except Exception:
            pass
    i += 1
Y_mat = [s for s in streams[2:] if s.max() < 2][0].reshape((100, 100), order="F")
res = {}
# ---- A ----
a = arm("archive")
if a:
    d = [{"k": r["k"], "Y_native": r["Y"], "Y_archive": float(Y_mat[22, r["k"]]), "diff": r["Y"] - float(Y_mat[22, r["k"]]),
          "bit_equal": r["Y"] == float(Y_mat[22, r["k"]])} for r in a["rows"]]
    diffs = np.array([x["diff"] for x in d]); n = len(d)
    if n == 14 and all(x["bit_equal"] for x in d): v = "A-BIT"
    elif n == 14 and np.all(np.abs(diffs) <= 1e-12): v = "A-NEAR"
    elif n == 14 and np.all(np.abs(diffs) <= 3e-4) and abs(diffs.mean()) <= 3e-5: v = "A-STAT"
    else: v = "A-MISMATCH" if n == 14 else "A-INCOMPLETE_%d" % n
    res["A"] = {"points": d, "n_bit_equal": int(sum(x["bit_equal"] for x in d)), "mean_diff": float(diffs.mean()) if n else None,
                "max_abs_diff": float(np.max(np.abs(diffs))) if n else None, "verdict": v, "header": a["header"]}
# ---- B ----
B = {k: arm(k) for k in ("A0u", "A0", "A1", "A2", "A3", "A4")}
r = {k: (v["rows"][0] if v and v["rows"] else None) for k, v in B.items()}
if r["A0u"] and r["A0"]:
    res["C0a"] = {"bit_equal": r["A0u"]["Y_big"] == r["A0"]["Y_big"], "diff": r["A0u"]["Y"] - r["A0"]["Y"]}
if r["A1"] and r["A0"]:
    res["C0b"] = {"bit_equal": r["A1"]["Y_big"] == r["A0"]["Y_big"], "diff": r["A1"]["Y"] - r["A0"]["Y"]}
if r["A2"] and r["A1"]:
    dd = abs(r["A2"]["Y"] - r["A1"]["Y"])
    res["C0c"] = {"abs_diff": dd, "class": "NO_CONFOUND" if dd <= 1e-12 else ("NEGLIGIBLE_CONFOUND" if dd <= 1e-6 else "MATERIAL_CONFOUND_ERRATA")}
if r["A0"] and r["A3"]:
    d03 = r["A3"]["X_T0"] - r["A0"]["X_T0"]
    S = {"dX_A3_minus_A0": d03}
    if r["A4"]:
        d34 = r["A4"]["X_T0"] - r["A3"]["X_T0"]; S["dX_A4_minus_A3"] = d34
        S["gate"] = "RELEASE" if (abs(d34) <= 1e-5 and abs(d34) <= 0.5 * abs(d03)) else "HOLD_SOLVER_CALIBRATION"
    else:
        S["gate"] = "HOLD_SOLVER_CALIBRATION_A4_MISSING"
    res["S"] = S
res["B_records"] = {k: v for k, v in r.items() if v}
# ---- C ----
c = arm("rep013")
if c and c["rows"]:
    x = c["rows"][0]
    res["C"] = {"Y": x["Y"], "Y_ref": 0.25239220435845267, "Y_equal_17digits": "%.17g" % x["Y"] == "0.25239220435845267",
                "first_zero_index": x.get("first_nPBH_zero_index_1based"), "index_ref": 8545,
                "t_last_live_s": x.get("t_s_at_last_live"), "t_ref": 0.33492735181}
json.dump(res, open(outp, "w"), indent=1)
print(json.dumps({k: v for k, v in res.items() if k != "B_records"}, indent=1, default=str)[:4000])
