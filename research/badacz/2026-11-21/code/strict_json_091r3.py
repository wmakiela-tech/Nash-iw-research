"""REVIEW_091 r3: strict-JSON companions of tables090*.json (AUD3 ROT007 custody note).
NaN tokens come only from descriptive H/P multiplicity ratios where the PYTHIA multiplicity is 0 (make_tables_090.py l.66).
Usage: python3 -I strict_json_091r3.py <in.json> <out.strict.json>; NaN -> null, everything else unchanged (indent=1)."""
import json, math, sys
src, dst = sys.argv[1:3]
def fix(o):
    if isinstance(o, dict): return {k: fix(v) for k, v in o.items()}
    if isinstance(o, list): return [fix(v) for v in o]
    if isinstance(o, float) and not math.isfinite(o): return None
    return o
json.dump(fix(json.load(open(src))), open(dst, "x"), indent=1, allow_nan=False)
