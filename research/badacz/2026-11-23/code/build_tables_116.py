"""PREREG_116: tables probing the Wu-Xu sub-1e9 g extrapolation channel, plus the exposure-weighted prediction proxy D.
Tables (authors' format, base = Sc of PREREG_109, rebuilt bitwise first: G_REBUILD_SC):
  x0, x3 : Sc with the top segment E > E_last = 7.07e4 GeV multiplied by 0 / 3 (posthoc_109b variants; Mech-S10 ROT022);
  p13    : Sc plus 20 rows prepended below 1e9 g (M0 * 10^(-k/2), k = 1..20) with rate_h = rate_h(M0) (M/M0)^(-1.3): the paper's
           prescription below 1e9 g (arXiv:2509.05618 eqs. 4.4-4.5, T^1.3 calibrated at 1e9 g) instead of the code's log-log
           continuation of rows 0-1; rows >= 1e9 g untouched;
  s15    : as p13 with exponent -1.5 (calibration arm: strong, known change of the extrapolated slope only).
D (prediction proxy, dex): change of the time-integrated hadron-induced n<->p conversion of a native dump (w arm of 112 at a
  node near the roots), weighting each species by its dump terms; M(t) = max(M_init (1 - t/tau)^(1/3), M_init e^-20); rate ratio
  in-table by linear interpolation of log ratio in log M, below 1e9 g by the code's log-log linear extrapolation of each table.
Usage: python3 -I build_tables_116.py <hadronization_tables_dir> <primary.tsv> <mc109_dir> <Sc_109.dat> <rates_j22.csv>
                                       <rates_j62.csv> <out_dir>"""
import csv, hashlib, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "2026-11-21", "code"))
import fold_090 as F

hdir, prim, mc109, scref, rj22, rj62, out = sys.argv[1:8]
os.makedirs(out, exist_ok=True)
DL_PY = np.log(1e11) / 499; BIN_PY = (np.exp(DL_PY) - 1) / DL_PY
DL_HW = np.log(1e11) / 99; BIN_HW = (np.exp(DL_HW) - 1) / DL_HW
bhP = F.load_bh(os.path.join(hdir, "pythia_tables")); bhH = F.load_bh(os.path.join(hdir, "herwig_tables"))
m, E, Phi = F.load_primary(prim)


def load_mc_ok(path):
    d = json.load(open(path))
    good = [e for e in d["energies"] if e.get("rc_run") == 0 and (e.get("events") or 0) > 0]
    Em = np.array([e["E"] for e in good])
    return {s: (Em, np.array([e[str(F.PDG[s])] for e in good]) * F.PAIR_MC(d["primary"])) for s in F.SPEC}


H71 = {c: load_mc_ok(os.path.join(mc109, f"herwig71_{name}.json")) for c, name in F.MCNAME.items() if c != "higgs"}
TOPC = [c for c in H71 if F.MCNAME[c] == "top"][0]
E_last = H71[TOPC][F.SPEC[0]][0].max()


def n_hc(s, c, k=None):
    Ei, n = bhH[s][c]
    Er = Ei if c == "higgs" else Ei / 2
    v = np.where(E >= Er[0], np.interp(E, Er, n), 0.0)
    above = E > Er[-1]
    if c in H71:
        Em, nm = H71[c][s]
        v = np.where(above, F.interp_loglog(Em, nm, E), v)
        if c == TOPC and k is not None:
            nl = F.interp_loglog(Em, nm, np.array([E_last]))[0]
            v = np.where(E > E_last, nl * k, v)
    else:
        v = np.where(above, n[-1], v)
    return v


def fold(k=None):
    Y = np.zeros((len(m), len(F.SPEC))); lo = E < 12.5
    for si, s in enumerate(F.SPEC):
        for c in F.TCOL:
            Y[:, si] += np.trapezoid(Phi[c] * np.where(lo, F.interp_lin(*bhP[s][c], E), 0.0)[None, :], E, axis=1) / BIN_PY
            Y[:, si] += np.trapezoid(Phi[c] * np.where(~lo, n_hc(s, c, k), 0.0)[None, :], E, axis=1) / BIN_HW
    return Y


res = {"gates": {}, "D": {}, "inputs_sha256": {}}
Sc = fold()
F.write_table(os.path.join(out, "Sc.dat"), m, Sc)
res["gates"]["G_REBUILD_SC"] = {"pass": open(os.path.join(out, "Sc.dat"), "rb").read() == open(scref, "rb").read()}
mg = m / m[0] * 1e9
T = {"x0": (m, fold(0.0)), "x3": (m, fold(3.0))}
for name, p in (("p13", -1.3), ("s15", -1.5)):
    Mp = m[0] * 10.0 ** (-np.arange(20, 0, -1) / 2.0)
    T[name] = (np.concatenate([Mp, m]), np.vstack([Sc[0][None, :] * (Mp[:, None] / mg[0]) ** p, Sc]))
for name, (mm, Y) in T.items():
    F.write_table(os.path.join(out, f"{name}.dat"), mm, Y)
res["gates"]["G_FINITE"] = {"pass": bool(all(np.all(np.isfinite(Y)) and np.all(Y > 0) and np.all(np.diff(mm) > 0) for mm, Y in T.values()))}


def log_rate(mm, Y, si, M):
    """code interpolation of log rate in log mass with linear extrapolation on both ends (DataInterpolations Linear)."""
    x = np.log(mm); y = np.log(Y[:, si]); X = np.log(M)
    v = np.interp(X, x, y)
    lo = X < x[0]; hi = X > x[-1]
    v = np.where(lo, y[0] + (X - x[0]) * (y[1] - y[0]) / (x[1] - x[0]), v)
    return np.where(hi, y[-1] + (X - x[-1]) * (y[-1] - y[-2]) / (x[-1] - x[-2]), v)


grid = np.geomspace(6e8, 1e10, 100)
TERMS = {"pipm": ("r_p2n_pi", "r_n2p_pi"), "Kpm": ("r_p2n_K", "r_n2p_K"), "K0L": ("r_p2n_K0L", "r_n2p_K0L"),
         "neutron": ("r_p2n_nbar",), "proton": ("r_n2p_pbar",)}
for j, path in ((22, rj22), (62, rj62)):
    res["inputs_sha256"][os.path.basename(path)] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    rows = list(csv.DictReader(open(path))); a = {k: np.array([float(x[k]) for x in rows]) for k in rows[0]}
    o = np.argsort(a["t_s"]); a = {k: v[o] for k, v in a.items()}
    alive = a["n_PBH_alive"] > 0.5; t = a["t_s"]; tau = t[alive].max(); Mi = grid[j]
    M = np.maximum(Mi * np.clip(1 - t / tau, 0, None) ** (1 / 3), Mi * np.exp(-20.0))
    H = {s: sum(a[c] for c in TERMS[s]) for s in F.SPEC}
    tot = sum(np.trapezoid(np.where(alive, H[s], 0), t) for s in F.SPEC)
    for name, (mm, Y) in T.items():
        num = sum(np.trapezoid(np.where(alive, H[s] * np.exp(log_rate(mm, Y, si, M * m[0] / 1e9) - log_rate(m, Sc, si, M * m[0] / 1e9)), 0), t)
                  for si, s in enumerate(F.SPEC))
        res["D"][f"j{j}|{name}"] = float(np.log10(num / tot))
json.dump(res, open(os.path.join(out, "tables116.json"), "x"), indent=1)
print(json.dumps(res["gates"])); print(json.dumps(res["D"]))
sys.exit(0 if all(g["pass"] for g in res["gates"].values()) else 7)
