#!/usr/bin/env python3
"""tau_check_118: PBH lifetime in the native Wu-Xu code (d395183, main-scan.jl blob b368ba55) vs the standard
greybody-normalised lifetime t_BH = 407 s * (f/15.35)^-1 * (M/1e10 g)^3 with f = 15.35 (formula as cited by EKS1 ROT025:
Chluba et al., arXiv:1912.10995 Eq. 3.2; the citation itself not re-verified here).

Inputs: two native rate dumps kept from REVIEW_113 / posthoc_115 (W arm, j22 and j62 of the scan grid
geomspace(6e8, 1e10, 100) g). Evaporation in the code does not depend on the hadron table, so the arm is irrelevant.
tau_code = last time with n_PBH_alive > 0.5 in the dump (resolution: local time step, recorded).
Usage: python3 tau_check_118.py <rates_w22.csv> <rates_w62.csv> <out.json>
"""
import csv, hashlib, json, sys
import numpy as np

grid = np.geomspace(6e8, 1e10, 100)
out = {"formula": "tau_std = 407 s * (M/1e10 g)^3 (f = 15.35)", "cells": {}, "inputs_sha256": {}}
for j, path in ((22, sys.argv[1]), (62, sys.argv[2])):
    out["inputs_sha256"][path.split("/")[-1]] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    rows = list(csv.DictReader(open(path)))
    t = np.array([float(r["t_s"]) for r in rows]); alive = np.array([float(r["n_PBH_alive"]) for r in rows]) > 0.5
    o = np.argsort(t); t, alive = t[o], alive[o]
    k = np.nonzero(alive)[0].max()
    tau = float(t[k]); dt = float(t[k + 1] - t[k]) if k + 1 < len(t) else float("nan")
    M = float(grid[j]); tstd = 407.0 * (M / 1e10) ** 3
    out["cells"][f"j{j}"] = {"M_init_g": M, "tau_code_s": tau, "tau_resolution_s": dt, "tau_std_s": tstd,
                             "ratio_std_over_code": tstd / tau}
json.dump(out, open(sys.argv[3], "w"), indent=1, sort_keys=True)
print(json.dumps(out["cells"], indent=1))
