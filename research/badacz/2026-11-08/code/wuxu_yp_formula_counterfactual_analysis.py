#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_051 (Wu-Xu Y_P formula counterfactual) from the native-driver CSV files.
Usage: python3 -I wuxu_yp_formula_counterfactual_analysis.py <data/yp051 dir> <data/kernel_analysis.json> <out.json>
Roots: least-squares quadratic through the 4 points around the first sign change (log10 beta increasing); numerical
uncertainty = |quadratic root - linear-interpolation root|.
"""
import csv, glob, json, math, re, sys
import numpy as np

ddir, kpath, out = sys.argv[1], sys.argv[2], sys.argv[3]
cal, rows = {}, []
for f in sorted(glob.glob(ddir + "/yp_*.csv")):
    lines = open(f).read().splitlines()
    for l in lines:
        m = re.match(r"# SBBN j=(\d+) m_g=\S+: X0s=(\S+) Ycode_native=(\S+) Ycode_recomp=(\S+) T1_MeV=(\S+) X1s=(\S+)", l)
        if m:
            cal[int(m.group(1)) if f.endswith("_a.csv") else 1000 + int(m.group(1))] = dict(
                X0s=float(m.group(2)), Yc=float(m.group(3)), Yc_re=float(m.group(4)), T1=float(m.group(5)), X1s=float(m.group(6)), file=f)
    rows += list(csv.DictReader(l for l in lines if not l.startswith("#")))
T0 = float(re.search(r"T0_MeV=(\S+)", open(sorted(glob.glob(ddir + "/yp_*.csv"))[0]).readline()).group(1))
c22 = [v for k, v in cal.items() if k % 1000 == 22][0]
X0s, X1s, T1 = c22["X0s"], c22["X1s"], c22["T1"]
xstar = 0.1255*X0s/X1s
crit = {"V0": lambda r: float(r["Yc_native"]) - 0.251,
        "V1": lambda r: 2*float(r["X_T1"]) - 0.251,
        "V2": lambda r: 2*float(r["X_T0"]) - 2*X0s - 0.006,
        "V1p": lambda r: float(r["X_T0"]) - xstar}
def root(pts, fn):
    lb = np.array([float(p["log10beta"]) for p in pts]); y = np.array([fn(p) for p in pts])
    idx = np.where((y[:-1] < 0) & (y[1:] >= 0))[0]
    if len(idx) == 0:
        return None
    i = int(idx[0]); lin = lb[i] - y[i]*(lb[i + 1] - lb[i])/(y[i + 1] - y[i])
    sel = list(range(max(0, i - 1), min(len(lb), i + 3)))
    if len(sel) >= 3:
        c = np.polyfit(lb[sel] - lin, y[sel], 2); rr = np.roots(c); rr = rr[np.isreal(rr)].real + lin
        rr = rr[(rr >= lb[i] - 1e-9) & (rr <= lb[i + 1] + 1e-9)]
        q = float(rr[0]) if len(rr) else lin
    else:
        q = lin
    # post hoc addition (not in PREREG_051): noise scale from residuals of a cubic over all points of the id
    noise = None
    if len(lb) >= 6:
        cc = np.polyfit(lb - lb.mean(), y, 3); sd = float(np.std(y - np.polyval(cc, lb - lb.mean()), ddof=4))
        sl = float(np.polyval(np.polyder(cc), q - lb.mean())); noise = sd/abs(sl) if sl != 0 else None
    return {"root": q, "num_unc": abs(q - lin), "noise_se_posthoc": noise, "bracket": [float(lb[i]), float(lb[i + 1])]}
kan = json.load(open(kpath))["configs"]
res = {"T0_MeV": T0, "calibration": cal, "xstar_V1p": xstar, "ids": {}}
ident = 0.0
for r in rows:
    ident = max(ident, abs(float(r["Yc_native"]) - float(r["Yc_recomp"]))/float(r["Yc_native"]))
for gid in sorted({r["id"] for r in rows}):
    pts = sorted([r for r in rows if r["id"] == gid], key=lambda r: float(r["log10beta"]))
    j = int(pts[0]["j"]); d = {"j": j, "m_g": float(pts[0]["m_g"]), "n_points": len(pts)}
    for k, fn in crit.items():
        d[k] = root(pts, fn)
    if all(d[k] for k in ("V0", "V1", "V2", "V1p")):
        d["shift_V1"] = d["V1"]["root"] - d["V0"]["root"]; d["shift_V2"] = d["V2"]["root"] - d["V0"]["root"]
        d["P1_dev"] = d["V1"]["root"] - d["V1p"]["root"]
    b = kan.get("base_%d" % j)
    if b and d["V0"]:
        d["V0_minus_REVIEW050"] = d["V0"]["root"] - b["root"]
    res["ids"][gid] = d
main = [res["ids"][g] for g in ("g22", "g28", "g34", "g62") if g in res["ids"]]
win_V1 = {22: (0.08, 0.15)}; win_V2 = {22: (0.20, 0.30)}
v = {}
v["I0_identity"] = ident <= 1e-12 and all(abs(d.get("V0_minus_REVIEW050", 1)) <= 0.01 for d in main)
c_all = list(cal.values())
v["C1_calibration"] = all(0.244 <= c["Yc"] <= 0.246 for c in c_all) and T1 > T0 and max(c["X0s"] for c in c_all) - min(c["X0s"] for c in c_all) < 1e-6
v["P1_decay_only_scaling"] = len(main) == 4 and all(abs(d["P1_dev"]) <= 0.02 for d in main)
v["P2_V1_windows"] = len(main) == 4 and all(win_V1.get(d["j"], (0.03, 0.07))[0] <= d["shift_V1"] <= win_V1.get(d["j"], (0.03, 0.07))[1] for d in main)
v["P2_V2_windows"] = len(main) == 4 and all(win_V2.get(d["j"], (0.07, 0.13))[0] <= d["shift_V2"] <= win_V2.get(d["j"], (0.07, 0.13))[1] for d in main)
res["identity_max_rel"] = ident; res["verdicts"] = v
json.dump(res, open(out, "w"), indent=1)
print(json.dumps(v)); print("X0s=%.9f X1s=%.9f T0=%.9f T1=%.9f MeV" % (X0s, X1s, T0, T1))
for g, d in res["ids"].items():
    f = lambda k: ("%.4f" % d[k]["root"]) if d.get(k) else "  -  "
    print(g, d["j"], "%.3e" % d["m_g"], "V0", f("V0"), "V1", f("V1"), "V1p", f("V1p"), "V2", f("V2"),
          "sV1 %+.4f sV2 %+.4f P1dev %+.4f dV0 %+.4f" % (d.get("shift_V1", float("nan")), d.get("shift_V2", float("nan")), d.get("P1_dev", float("nan")), d.get("V0_minus_REVIEW050", float("nan"))))
