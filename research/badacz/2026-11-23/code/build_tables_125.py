#!/usr/bin/env python3
"""PREREG_125 (STOP A control for STD_A): authors' hadron table hadrons_from_PBH.dat (d395183) with 20 rows prepended below
M0 = 1e9 g at M0 * 10^(-k/2), k = 20..1, rate_h(M) = rate_h(M0) (M/M0)^s, for s in {-1.0, -1.3, -1.5}; the authors' header and
100 rows are kept byte-identical (gate G_TAB). Physical reading: q_h = P_BH * n_E with P_BH ~ M^-2 (f_BH constant below 1e10 g,
REVIEW_120) and hadrons per GeV n_E ~ E^(alpha - 1) ~ M^(1 - alpha), i.e. s = -(1 + alpha): alpha = mean-multiplicity growth
exponent N(E) ~ E^alpha at constant hadron energy fraction. s = -1.0 (alpha 0), code continuation ~ -1.20 (alpha 0.2),
paper prescription -1.3 (alpha 0.3), -1.5 (alpha 0.5).
Also reported (no threshold): alpha_PY, the local exponent d ln nu_had / d ln E' of the BlackHawk v2.3 PYTHIA BBN tables for
u, d, s, c, b and gluons at E' in [1e4, 1e5] GeV (total count of the 5 BBN hadron species per primary).
Usage: python3 -I build_tables_125.py <hadrons_from_PBH.dat> <pythia_tables> <out_dir>"""
import hashlib, json, os, sys
import numpy as np

AUTH, PY, OUT = sys.argv[1:4]
os.makedirs(OUT, exist_ok=True)
lines = open(AUTH).read().split("\n")
hdr, rows = lines[0], [l for l in lines[1:] if l.strip()]
A = np.array([[float(x) for x in l.split("\t")] for l in rows])
M0, q0 = A[0, 0], A[0, 1:]
res = {"auth_sha256": hashlib.sha256(open(AUTH, "rb").read()).hexdigest(), "tables": {}, "gates": {}}
code_slope = (np.log(A[1, 1:]) - np.log(A[0, 1:])) / (np.log(A[1, 0]) - np.log(A[0, 0]))
res["code_slope_rows01"] = code_slope.tolist()
ok = True
for name, s in (("m10", -1.0), ("m13", -1.3), ("m15", -1.5)):
    Mp = M0 * 10.0 ** (-np.arange(20, 0, -1) / 2.0)
    new = [hdr] + ["\t".join(repr(float(x)) for x in [mm] + list(q0 * (mm / M0) ** s)) for mm in Mp] + rows
    p = os.path.join(OUT, f"hadrons_from_PBH_{name}.dat")
    open(p, "x").write("\n".join(new) + "\n")
    back = open(p).read().split("\n")
    ok &= back[0] == hdr and back[21:121] == rows and all(np.isfinite([float(x) for x in l.split("\t")]).all() for l in back[1:21])
    res["tables"][name] = {"slope": s, "sha256": hashlib.sha256(open(p, "rb").read()).hexdigest(), "rows": len(back) - 2}
res["gates"]["G_TAB"] = bool(ok and open(AUTH).read().endswith("\n"))
FIN = ["pipm", "Kpm", "K0L", "proton", "neutron"]
N = {}
for j in FIN:
    h = open(f"{PY}/{j}.txt").readline().split(); a = np.loadtxt(f"{PY}/{j}.txt", skiprows=1)
    Ei = np.unique(a[:, 0]); Ef = np.unique(a[:, 1]); N[j] = np.abs(a[:, 2:]).reshape(len(Ei), len(Ef), len(h) - 2)
pr = h[2:]; nu = sum(N[j].sum(axis=1) for j in FIN)
sel = (Ei >= 1e4) & (Ei <= 1e5)
res["alpha_PY"] = {p: float(np.polyfit(np.log(Ei[sel]), np.log(nu[sel, pr.index(p)]), 1)[0]) for p in ("up", "down", "strange", "charm", "bottom", "gluons")}
json.dump(res, open(os.path.join(OUT, "tables125.json"), "x"), indent=1, sort_keys=True)
print(json.dumps({"G_TAB": res["gates"]["G_TAB"], "code_slope": [round(x, 4) for x in code_slope]}))
sys.exit(0 if res["gates"]["G_TAB"] else 7)
