#!/usr/bin/env python3
"""POST HOC to PREREG_123 (not preregistered). G_REP was uninformative: every evaluation is an independent ODE solve at
fixed beta, and grid B's bisection nodes coincide with grid A's (dyadic offsets), so A and B gave identical roots.
Substitute local noise estimate: for each mass-arm with a root, take all evaluated points (A and B) within +-0.75 dex of
the root, fit Y quadratically in log10 beta; residual RMS sigma_Y (includes fit misfit, so an upper-side estimate); local
slope s at the root; sigma_root = sigma_Y / s (dex).
Also writes <strict.json>: analysis123.json with NaN ("no root") -> null (strict JSON; REC14 ROT011 data-quality guard).
Usage: python3 -I posthoc_123.py <analysis123.json> <out.json> <strict.json>"""
import json, sys
import numpy as np

d = json.load(open(sys.argv[1])); out = {"post_hoc": True, "cells": {}}
roots = d["roots"]
for key, (st, r) in roots.items():
    a, j, mode = key.split("|")
    if st != "root" or mode != "coarse":
        continue
    pts = d["points"].get(f"{a}|{j}|A", []) + d["points"].get(f"{a}|{j}|B", [])
    u = {}
    for p in pts:
        u[p["lb"]] = p["Y"]
    lb = np.array(sorted(x for x in u if abs(x - r) <= 0.75)); Y = np.array([u[x] for x in lb])
    if len(lb) < 4:
        out["cells"][key] = {"n": int(len(lb)), "note": "too few points"}; continue
    c = np.polyfit(lb - r, Y, 2); res = Y - np.polyval(c, lb - r)
    sY = float(np.sqrt(np.sum(res ** 2) / (len(lb) - 3))); s = float(c[1])
    out["cells"][key] = {"n": int(len(lb)), "lb_range": [float(lb.min()), float(lb.max())], "sigma_Y": sY, "slope_dY_dlb": s,
                         "sigma_root_dex": sY / s if s > 0 else None}
json.dump(out, open(sys.argv[2], "w"), indent=1, sort_keys=True, allow_nan=False)


def _null(o):
    if isinstance(o, float) and o != o:
        return None
    if isinstance(o, dict):
        return {k: _null(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_null(v) for v in o]
    return o


json.dump(_null(d), open(sys.argv[3], "w"), indent=1, sort_keys=True, allow_nan=False)
print(json.dumps(out, indent=1))
