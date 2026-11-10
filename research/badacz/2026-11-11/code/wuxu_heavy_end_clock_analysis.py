#!/usr/bin/env python3
"""Badacz (Claude): evaluation of PREREG_056 (native heavy-end clock vs MT14 ROT026 reduced clock).
E (descriptive): fraction of the hadron NUMBER (five channels summed, authors' table, mass clock dM/dt = -K/M^2) emitted
after T1, i.e. while M < M(T1): N(0, M_T1)/N(0, M0), with the same table interpolation/extrapolation as
research/badacz/2026-11-08/code/wuxu_band_number_shares.py.
Usage: python3 -I wuxu_heavy_end_clock_analysis.py --csv data/heavy_end_clock.csv --table hadrons_from_PBH.dat --out out.json
"""
import argparse, csv, json, math
ap = argparse.ArgumentParser(); ap.add_argument("--csv", required=True); ap.add_argument("--table", required=True); ap.add_argument("--out", required=True)
a = ap.parse_args()
T_MT14 = 214.96750232179298; TAU1 = 0.2376664163901
G_GEV = 5.60958860380445e23
rows_t = [list(map(float, l.split())) for l in open(a.table) if l.strip() and not l.startswith("m_PBH")]
lm = [math.log(r[0]/G_GEV) for r in rows_t]; lr = [[math.log(r[c]) for r in rows_t] for c in range(1, 6)]
def lnrate(c, x):
    if x <= lm[1]:
        s = (lr[c][1] - lr[c][0])/(lm[1] - lm[0]); return lr[c][0] + s*(x - lm[0])
    i = max(k for k in range(len(lm) - 1) if lm[k] <= x)
    s = (lr[c][i + 1] - lr[c][i])/(lm[i + 1] - lm[i]); return lr[c][i] + s*(x - lm[i])
def number(c, hi, n=4000):            # int_0^hi R(M) M^2 dM
    s = (lr[c][1] - lr[c][0])/(lm[1] - lm[0]); top = min(hi, math.exp(lm[0]))
    out = math.exp(lnrate(c, math.log(top)) + 3*math.log(top))/(3 + s)
    if hi <= top:
        return out
    x0, x1 = math.log(top), math.log(hi); h = (x1 - x0)/n; f = lambda x: math.exp(lnrate(c, x) + 3*x)
    return out + h/3*(f(x0) + f(x1) + sum((4 if k % 2 else 2)*f(x0 + k*h) for k in range(1, n)))
rows = list(csv.DictReader(l for l in open(a.csv) if not l.startswith("#")))
res = {"rows": [], "verdicts": {}, "note_t_evap": "t_evap_s is the first SAVED point with M <= 1e-3 M0; magic() saves 10000 points geometric in a, so dln a ~ 0.0045 and the resolution of t_evap is ~0.9% (biased high); t(T0), t(T1), M(T0), M(T1) are interpolated in log T and are not affected at this level"}
P1 = P2 = P3 = P4 = True; base = {}
for r in rows:
    j, m0, lb = int(r["j"]), float(r["m0_g"]), float(r["log10beta"]); tT0 = float(r["t_T0_s"]); MT0 = float(r["M_T0_g"]); MT1 = float(r["M_T1_g"])
    tau = TAU1*(m0/1e9)**3; f_nat = 1 - tT0/tau; f_mt = 1 - T_MT14/tau
    pred_nat = m0*f_nat**(1/3) if f_nat > 0 else 0.0; pred_mt = m0*f_mt**(1/3) if f_mt > 0 else 0.0
    evap = MT0 <= 1e-3*m0 or not math.isfinite(MT0)
    d = {"j": j, "m0_g": m0, "log10beta": lb, "t_T0_s": tT0, "t_T1_s": float(r["t_T1_s"]), "M_T0_g": MT0, "M_T1_g": MT1,
         "t_evap_s": float(r["t_evap_s"]), "tau_formula_s": tau, "M_T0_pred_native_t": pred_nat, "M_T0_pred_MT14": pred_mt, "evaporated_at_T0": evap}
    if pred_nat > 0 and not evap:
        d["rel_dev_native_t"] = (MT0 - pred_nat)/pred_nat; d["rel_dev_MT14"] = (MT0 - pred_mt)/pred_mt
        d["tau_eff_s"] = tT0/(1 - (MT0/m0)**3); d["tau_eff_rel_dev"] = d["tau_eff_s"]/tau - 1      # lifetime implied by the native point
        d["amplification_dM_over_dtau"] = (tT0/tau)/(3*(1 - tT0/tau))                               # |dM/M| = this * |dtau/tau|
        if j in (98, 99): P2 &= abs(d["rel_dev_native_t"]) <= 0.02
    if j in (98, 99) and evap: P3 = False
    if j in (62, 97) and not evap: P3 = False
    if lb <= -29: P1 &= abs(tT0 - T_MT14) <= 1.0; base[j] = tT0
    tot = sum(number(c, m0) for c in range(5))
    d["hadron_fraction_after_T1"] = (sum(number(c, MT1) for c in range(5))/tot) if (math.isfinite(MT1) and MT1 > 1e-3*m0) else 0.0
    d["hadron_fraction_after_T0"] = (sum(number(c, MT0) for c in range(5))/tot) if (math.isfinite(MT0) and MT0 > 1e-3*m0) else 0.0
    res["rows"].append(d)
for d in res["rows"]:
    if d["log10beta"] > -29 and d["j"] in base:
        d["dt_T0_feedback_s"] = d["t_T0_s"] - base[d["j"]]; P4 &= abs(d["dt_T0_feedback_s"]) <= 0.1
res["verdicts"] = {"P1_clock": P1, "P2_mass_law": P2, "P3_classification": P3, "P4_feedback": P4}
import os
tolf = a.csv.replace(".csv", "_tol1e-6.csv")
if os.path.exists(tolf):          # POST HOC diagnostic (not in PREREG_056): same records at reltol 1e-6, abstol 1e-9
    tr = list(csv.DictReader(l for l in open(tolf) if not l.startswith("#"))); res["posthoc_tol1e-6"] = []
    for r in tr:
        j, m0, lb = int(r["j"]), float(r["m0_g"]), float(r["log10beta"]); tT0 = float(r["t_T0_s"]); MT0 = float(r["M_T0_g"])
        tau = TAU1*(m0/1e9)**3; f_nat = 1 - tT0/tau; pred = m0*f_nat**(1/3) if f_nat > 0 else 0.0
        e = {"tau_eff_rel_dev": ((tT0/(1 - (MT0/m0)**3))/tau - 1) if (pred > 0 and MT0 > 1e-3*m0) else None, "j": j, "log10beta": lb, "t_T0_s": tT0, "dt_vs_MT14_s": tT0 - T_MT14, "M_T0_g": MT0, "t_evap_s": float(r["t_evap_s"]), "tau_formula_s": tau,
             "rel_dev_native_t": ((MT0 - pred)/pred) if (pred > 0 and MT0 > 1e-3*m0) else None, "Yc": float(r["Yc"])}
        res["posthoc_tol1e-6"].append(e)
json.dump(res, open(a.out, "w"), indent=1, allow_nan=False, default=str)
print(json.dumps(res["verdicts"]))
for d in res["rows"]:
    print("j%d lb%+.1f t_T0=%.3f t_T1=%.3f M_T0=%.4e (pred nat %.4e, MT14 %.4e) dev %s evap=%s t_ev=%.2f tau=%.2f fracN_after_T1=%.4f dt_fb=%s" % (
        d["j"], d["log10beta"], d["t_T0_s"], d["t_T1_s"], d["M_T0_g"], d["M_T0_pred_native_t"], d["M_T0_pred_MT14"],
        ("%+.4f" % d["rel_dev_native_t"]) if "rel_dev_native_t" in d else "-", d["evaporated_at_T0"], d["t_evap_s"], d["tau_formula_s"],
        d["hadron_fraction_after_T1"], ("%+.4f" % d["dt_T0_feedback_s"]) if "dt_T0_feedback_s" in d else "-"), "fracN_after_T0=%.4f" % d["hadron_fraction_after_T0"], ("tau_eff %+.5f amp %.2f" % (d["tau_eff_rel_dev"], d["amplification_dM_over_dtau"])) if "tau_eff_rel_dev" in d else "")
for e in res.get("posthoc_tol1e-6", []):
    print("TOL1e-6 j%d lb%+.1f t_T0=%.4f (dMT14 %+.4f) M_T0=%.4e dev %s tau_eff %s t_ev=%.2f Yc=%.6f" % (e["j"], e["log10beta"], e["t_T0_s"], e["dt_vs_MT14_s"], e["M_T0_g"],
          ("%+.4f" % e["rel_dev_native_t"]) if e["rel_dev_native_t"] is not None else "-", ("%+.5f" % e["tau_eff_rel_dev"]) if e["tau_eff_rel_dev"] is not None else "-", e["t_evap_s"], e["Yc"]))
