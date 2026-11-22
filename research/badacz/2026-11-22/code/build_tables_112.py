"""PREREG_112: tables for splitting the j22 residual r_H73 - r_U into generator vintage and table processing.
Usage: python3 -I build_tables_112.py <hadronization_tables_dir> <primary.tsv> <mc090_dir> <mc112_dir> <mc109_dir>
                                       <H73_090.dat> <Sc_109.dat> <requested112.json> <out_dir>
Tables (authors' format):
  W   = PREREG_090 construction (fold_090 'MC', same ELO, PY BH table below ELO and for photon/e/mu, / BIN_PY) with
        Herwig 7.1.5 multiplicities (mc112/herwig71_<prim>.json, sqrt(s) = 2E, same energies/events as 090; top up to
        51200 GeV only: E = 1e5 fails in 7.1.5, REVIEW_110 DEV-2; declared before the run).
  V   = Uc: table Sc of PREREG_109 (PY below 12.5 GeV, relabelled HERWIG rows, Herwig 7.1.5 above 5e4 GeV) with the PY
        binning convention on both parts (as Ua of 099, but from Sc).
  H73 = rebuilt exactly as make_tables_090.py (must equal data/hadrons_090_H73.dat bitwise: G_REBUILD_H73);
  Sc  = rebuilt exactly as build_tables_109.py (must equal data/hadrons_109_Sc.dat bitwise: G_REBUILD_SC);
  H73t = H73 with its top node at 1e5 GeV dropped (descriptive: effect of the declared top clip on the 7.3 side).
Gates: G_MC (every requested energy: rc 0, events = requested, |<E_final/sqrt(s)> - 1| <= 1e-3, K0S and hyperons absent),
  G_STAT (1-sigma MC stat error of W <= 1 % on rows 0-28), G_REBUILD_H73, G_REBUILD_SC, G_FINITE.  Exit 7 on any gate fail."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "2026-11-21", "code"))
import fold_090 as F

hdir, prim, mc090, mc112, mc109, h73ref, scref, reqp, out = sys.argv[1:10]
os.makedirs(out, exist_ok=True)
DL_PY = np.log(1e11) / 499; BIN_PY = (np.exp(DL_PY) - 1) / DL_PY
DL_HW = np.log(1e11) / 99; BIN_HW = (np.exp(DL_HW) - 1) / DL_HW
ELO = {c: 25.0 for c in F.MCNAME}; ELO.update({"Wpm": 100.0, "Z0": 100.0, "top": 200.0, "gluons": 100.0, "higgs": 100.0, "tau": 100.0})
bh = F.load_bh(os.path.join(hdir, "pythia_tables")); bhH = F.load_bh(os.path.join(hdir, "herwig_tables"))
m, E, Phi = F.load_primary(prim)
K = slice(0, 29)
res = {"gates": {}, "descriptive": {}, "constants": {"BIN_PY": BIN_PY, "BIN_HW": BIN_HW, "ELO": ELO}}

# --- G_MC on the new Herwig 7.1.5 runs
req = json.load(open(reqp)); gm = []
for name, ens in req.items():
    d = json.load(open(os.path.join(mc112, f"herwig71_{name}.json")))
    got = {f"{e['E']:g}": e for e in d["energies"]}
    for Es, N in ens.items():
        e = got.get(Es, {})
        ok = (e.get("rc_read") == 0 and e.get("rc_run") == 0 and e.get("events") == N and abs(e.get("Efinal_over_sqrts", 0) - 1) <= 1e-3
              and all(e.get(str(i), 0.0) == 0.0 for i in (310, 3122, 3222, 3112, 3312, 3322, 3334)))
        gm.append({"prim": name, "E": Es, "events": e.get("events"), "ok": bool(ok)})
    if len(got) != len(ens):
        gm.append({"prim": name, "E": "count", "ok": False})
res["gates"]["G_MC"] = {"n": len(gm), "failed": [x for x in gm if not x["ok"]], "pass": all(x["ok"] for x in gm)}

mc71 = {name: F.load_mc(os.path.join(mc112, f"herwig71_{name}.json")) for name in F.MCNAME.values()}
mc73 = {name: F.load_mc(os.path.join(mc090, f"herwig_{name}.json")) for name in F.MCNAME.values()}
mc73t = {k: dict(v) for k, v in mc73.items()}
keep = mc73["top"]["pipm"][0] < 9.9e4
mc73t["top"] = {s: tuple(a[keep] for a in mc73["top"][s]) for s in F.SPEC}

Y = {"W": F.fold("MC", bh, m, E, Phi, mc71, ELO) / BIN_PY,
     "H73": F.fold("MC", bh, m, E, Phi, mc73, ELO) / BIN_PY,
     "H73t": F.fold("MC", bh, m, E, Phi, mc73t, ELO) / BIN_PY}
stW = F.stat_err(bh, m, E, Phi, mc71, ELO) / BIN_PY / Y["W"]
res["gates"]["G_STAT"] = {"max_rel": float(stW[K].max()), "pass": bool(stW[K].max() <= 0.01)}


# --- Sc / V: same functions as build_tables_109.py (copied; that script runs at import)
def load_mc_ok(path):
    d = json.load(open(path))
    good = [e for e in d["energies"] if e.get("rc_run") == 0 and (e.get("events") or 0) > 0]
    Em = np.array([e["E"] for e in good])
    return {s: (Em, np.array([e[str(F.PDG[s])] for e in good]) * F.PAIR_MC(d["primary"]),
                np.array([e[f"se_{F.PDG[s]}"] for e in good]) * F.PAIR_MC(d["primary"])) for s in F.SPEC}


H71 = {c: load_mc_ok(os.path.join(mc109, f"herwig71_{name}.json")) for c, name in F.MCNAME.items() if c != "higgs"}


def n_py(s, c):
    return F.interp_lin(*bh[s][c], E)


def n_hc(s, c):
    Ei, n = bhH[s][c]
    Er = Ei if c == "higgs" else Ei / 2
    v = np.where(E >= Er[0], np.interp(E, Er, n), 0.0)
    top = Er[-1]; above = E > top
    if c in H71:
        Em, nm, _ = H71[c][s]
        v = np.where(above, F.interp_loglog(Em, nm, E), v)
    else:
        v = np.where(above, n[-1], v)
    return v


def fold_parts(n_lo, n_hi, split, b_lo, b_hi):
    YY = np.zeros((len(m), len(F.SPEC)))
    lo = E < split
    for si, s in enumerate(F.SPEC):
        for c in F.TCOL:
            YY[:, si] += np.trapezoid(Phi[c] * np.where(lo, n_lo(s, c), 0.0)[None, :], E, axis=1) / b_lo
            YY[:, si] += np.trapezoid(Phi[c] * np.where(~lo, n_hi(s, c), 0.0)[None, :], E, axis=1) / b_hi
    return YY


Y["Sc"] = fold_parts(n_py, n_hc, 12.5, BIN_PY, BIN_HW)
Y["V"] = fold_parts(n_py, n_hc, 12.5, BIN_PY, BIN_PY)
for k, v in Y.items():
    F.write_table(os.path.join(out, f"{k}.dat"), m, v)
res["gates"]["G_REBUILD_H73"] = {"pass": open(os.path.join(out, "H73.dat"), "rb").read() == open(h73ref, "rb").read()}
res["gates"]["G_REBUILD_SC"] = {"pass": open(os.path.join(out, "Sc.dat"), "rb").read() == open(scref, "rb").read()}
res["gates"]["G_FINITE"] = {"pass": bool(all(np.all(np.isfinite(v)) and np.all(v[K] > 0) for v in Y.values()))}
for a, b in (("W", "H73"), ("V", "W"), ("V", "Sc"), ("H73t", "H73")):
    r = np.log10(Y[a][K] / Y[b][K])
    res["descriptive"][f"log10_{a}_over_{b}_rows0_28_min_max"] = {s: [float(r[:, i].min()), float(r[:, i].max())] for i, s in enumerate(F.SPEC)}
json.dump(res, open(os.path.join(out, "tables112.json"), "x"), indent=1, default=float)
print(json.dumps({k: v["pass"] for k, v in res["gates"].items()}))
sys.exit(0 if all(v["pass"] for v in res["gates"].values()) else 7)
