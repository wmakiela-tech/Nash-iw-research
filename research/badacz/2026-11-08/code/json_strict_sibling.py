#!/usr/bin/env python3
"""Badacz (Claude): write a strict-JSON sibling of a JSON file that contains the non-standard tokens Infinity/-Infinity/NaN
(Python json default). The original file is left untouched (raw custody). Non-finite numbers become null; the list of their
JSON paths is printed (and should be recorded in the RUNLOG).
Usage: python3 -I json_strict_sibling.py <in.json> <out.strict.json>
"""
import json, math, sys
src, dst = sys.argv[1], sys.argv[2]
paths = []
def conv(x, p):
    if isinstance(x, float) and not math.isfinite(x):
        paths.append(p + " = " + repr(x)); return None
    if isinstance(x, dict):
        return {k: conv(v, p + "/" + str(k)) for k, v in x.items()}
    if isinstance(x, list):
        return [conv(v, p + "/" + str(i)) for i, v in enumerate(x)]
    return x
obj = conv(json.load(open(src)), "")
json.dump(obj, open(dst, "w"), indent=1, allow_nan=False)
print(len(paths), "non-finite values ->", dst); print("\n".join(paths))
