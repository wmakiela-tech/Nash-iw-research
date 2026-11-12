#!/usr/bin/env python3
"""Geeky-S12 ROT010: replay ORIGINAL M13 public source safely in a temp dir.
Needs cloned wmakiela-tech/Nash-iw-research and mpmath==1.3.0.
Do not overwrite the frozen M13 direct_B.json. This wrapper creates a
temporary snapshot and configures the 2026-10-24 PYTHONPATH dependency.

Checks exact ORIGINAL immutable Git blob SHA for all three inputs, runs the
unmodified M13 source_snapshot_ch.py B through subprocess, and tests full
canonical Git blob identity of all 25 directed mpmath.iv coefficient pairs.
"""
import hashlib, json, os, pathlib, shutil, subprocess, sys, tempfile
ROOT=pathlib.Path(__file__).resolve().parents[3]
M13_DIR=ROOT/"research/m13/2026-10-26"
M13_CODE=ROOT/"research/m13/2026-10-24/verify_m13_rot33_interval.py"
M13_SNAPSHOT=M13_DIR/"source_snapshot_ch.py"
M13_FROZEN=M13_DIR/"direct_B.json"
SOURCE_SHA="c6377cfbc9a0070abc34ffedc5871e719f6a4679"
SNAPSHOT_SHA="c8ea76abd77f2186f868d5e16035b5fb0e0f6231"
B_SHA="a6f50fbe5904e580e84c87ee87c5ad043cdec5d0"
def blob(data):
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()
def check(name,file,expected):
    if not file.is_file():raise FileNotFoundError(f"{name}: {file}")
    raw=file.read_bytes();actual=blob(raw)
    if actual!=expected:raise AssertionError(f"{name} Git blob mismatch: {actual} != {expected}")
    return raw
def main():
    check("M13 ROT33 source",M13_CODE,SOURCE_SHA)
    check("M13 original snapshot",M13_SNAPSHOT,SNAPSHOT_SHA)
    expected=check("M13 original direct_B",M13_FROZEN,B_SHA)
    import mpmath
    if mpmath.__version__!="1.3.0":raise RuntimeError("Use mpmath==1.3.0")
    with tempfile.TemporaryDirectory(prefix="geeky_s12_rot010_m13_source_") as temp:
        staged=pathlib.Path(temp)
        shutil.copyfile(M13_SNAPSHOT,staged/"source_snapshot_ch.py")
        env=os.environ.copy()
        env["PYTHONPATH"]=str(M13_CODE.parent)+os.pathsep+env.get("PYTHONPATH","")
        run=subprocess.run([sys.executable,"-u",str(staged/"source_snapshot_ch.py"),"B"],cwd=ROOT,
                           env=env,check=True,text=True,capture_output=True)
        produced=(staged/"direct_B.json").read_bytes()
        # Original snapshot writes a terminal LF; original frozen source
        # Git blob deliberately has NO terminal LF. Preserve exact contents.
        canonical=produced[:-1] if produced.endswith(b"\n") else produced
        if blob(canonical)!=B_SHA:raise AssertionError("Source coefficient Git blob mismatch")
        if canonical!=expected:raise AssertionError("Original canonical coefficient byte mismatch")
        decoded=json.loads(canonical)
        if sorted(decoded)!=list("23456") or any(len(decoded[k])!=5 for k in decoded):
            raise AssertionError("Unexpected source mask/degree structure")
        return {
            "return_id":"IW_GEEKY_S12_ROT010_M13_DIRECT_B_SOURCE_INTERVAL_CANONICAL_REGEN_001_20261112",
            "source_module_blob":SOURCE_SHA,"snapshot_script_blob":SNAPSHOT_SHA,
            "immutable_original_source_blob":B_SHA,"regenerated_source_blob":blob(canonical),
            "all_25_directed_intervals_byte_exact":True,"source_intervals":25,
            "original_snapshot_added_last_newline":produced.endswith(b"\n"),
            "original_byte_count":len(expected),"mpmath_version":mpmath.__version__,
            "original_snapshot_stdout":run.stdout.strip(),
            "claim_ceiling":"M13 auxiliary model only; not byte-identical historical dtc0a runtime or physics"
        }
if __name__=="__main__":
    print(json.dumps(main(),indent=2))
