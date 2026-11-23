"""POST HOC (answer to Mech-S10 ROT021/ROT022; arithmetic on existing tables and native dumps, no new native run).
(1) Native exposure: share of the time-integrated hadron-induced n<->p conversion (sum of the pi, K+-, K0L, nbar, pbar terms of
    the native dumps) delivered while the PBH mass is below M_c, M_c in {1e9 (lowest table row), 5e8, 1e8, 1e6} g.
    M(t) = max(M_init (1 - t/tau)^(1/3), M_init e^-20) (approximation: constant emitted-species factor; floor = author evaporation
    stop, main-scan.jl blob b368ba55), tau = last alive time of the dump;
    M_init from the native scan grid (main-scan-parameters.jl: geomspace(6e8, 1e10, 100) g; j22 -> 1.1212e9, j62 -> 3.4942e9).
(2) Effective change of that integrated conversion for the top-endpoint variants of posthoc_109b (segment E > 7.07e4 GeV of
    the top channel x0, x3, slope continuation), including the code's log-log linear extrapolation below the lowest table row:
    log R_k/R = (1 - lam) D0 + lam D1, lam = ln(M/M0)/ln(M1/M0) (Wu-Xu tool_script-hadrons_from_PBH.jl, blob cc734329, local =
    public pinned d395183); in-table: linear interpolation of log ratio in log M. Per species weighting by its dump terms.
Usage: python3 -I posthoc_115.py <hadronization_tables_dir> <primary.tsv> <mc109_dir> <Sc.dat> <rates_j22.csv> <rates_j62.csv> <out.json>"""
import csv, hashlib, json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "2026-11-21", "code"))
import fold_090 as F

hdir, prim, mc109, scdat, rj22, rj62, dst = sys.argv[1:8]
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


def n_hc(s, c, mode=None):
    Ei, n = bhH[s][c]
    Er = Ei if c == "higgs" else Ei / 2
    v = np.where(E >= Er[0], np.interp(E, Er, n), 0.0)
    above = E > Er[-1]
    if c in H71:
        Em, nm = H71[c][s]
        v = np.where(above, F.interp_loglog(Em, nm, E), v)
        if c == TOPC and mode is not None:
            seg = E > E_last; nl = F.interp_loglog(Em, nm, np.array([E_last]))[0]
            if mode == "slope":
                i = np.argsort(Em)[-2:]; b = np.log(nm[i[1]] / nm[i[0]]) / np.log(Em[i[1]] / Em[i[0]])
                v = np.where(seg, nl * (E / E_last) ** b, v)
            else:
                v = np.where(seg, nl * float(mode), v)
    else:
        v = np.where(above, n[-1], v)
    return v


def fold(mode=None):
    Y = np.zeros((len(m), len(F.SPEC))); lo = E < 12.5
    for si, s in enumerate(F.SPEC):
        for c in F.TCOL:
            Y[:, si] += np.trapezoid(Phi[c] * np.where(lo, F.interp_lin(*bhP[s][c], E), 0.0)[None, :], E, axis=1) / BIN_PY
            Y[:, si] += np.trapezoid(Phi[c] * np.where(~lo, n_hc(s, c, mode), 0.0)[None, :], E, axis=1) / BIN_HW
    return Y


Sc = fold(); ref = np.loadtxt(scdat, skiprows=1)[:, 1:] / F.HBAR
out = {"reproduce_Sc_max_rel": float(np.max(np.abs(Sc / ref - 1))), "M_init_g": {}, "inputs_sha256": {}, "exposure": {}, "variants": {}}
mg = m / m[0] * 1e9                                       # table masses in gram (row 0 = 1e9 g)
lnr = {k: np.log(fold(k) / Sc) for k in ("0", "3", "slope")}  # per row, per species
grid = np.geomspace(6e8, 1e10, 100)
TERMS = {"pipm": ("r_p2n_pi", "r_n2p_pi"), "Kpm": ("r_p2n_K", "r_n2p_K"), "K0L": ("r_p2n_K0L", "r_n2p_K0L"),
         "neutron": ("r_p2n_nbar",), "proton": ("r_n2p_pbar",)}


def lnratio(k, si, M):
    x = np.log(M); x0, x1 = np.log(mg[0]), np.log(mg[1]); r = lnr[k][:, si]
    lam = (x - x0) / (x1 - x0)
    ext = (1 - lam) * r[0] + lam * r[1]
    return np.where(M < mg[0], ext, np.interp(x, np.log(mg), r))


for j, path in ((22, rj22), (62, rj62)):
    out["inputs_sha256"][os.path.basename(path)] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    rows = list(csv.DictReader(open(path))); a = {k: np.array([float(x[k]) for x in rows]) for k in rows[0]}
    o = np.argsort(a["t_s"]); a = {k: v[o] for k, v in a.items()}
    alive = a["n_PBH_alive"] > 0.5; t = a["t_s"]; tau = t[alive].max(); Mi = grid[j]; out["M_init_g"][f"j{j}"] = float(Mi)
    M = np.maximum(Mi * np.clip(1 - t / tau, 0, None) ** (1 / 3), Mi * np.exp(-20.0))  # author stop: log(M_init/M) = 20 (main-scan.jl l.146, 167)
    H = {s: sum(a[c] for c in TERMS[s]) for s in F.SPEC}
    tot = sum(np.trapezoid(np.where(alive, H[s], 0), t) for s in F.SPEC)
    out["exposure"][f"j{j}"] = {f"M<{Mc:.0e}": float(sum(np.trapezoid(np.where(alive & (M < Mc), H[s], 0), t) for s in F.SPEC) / tot)
                                for Mc in (1e9, 5e8, 1e8, 1e6)}
    for k in lnr:
        num = sum(np.trapezoid(np.where(alive, H[s] * np.exp(lnratio(k, si, M)), 0), t) for si, s in enumerate(F.SPEC))
        intab = sum(np.trapezoid(np.where(alive & (M >= mg[0]), H[s] * np.exp(lnratio(k, si, M)), 0), t) for si, s in enumerate(F.SPEC))
        intab0 = sum(np.trapezoid(np.where(alive & (M >= mg[0]), H[s], 0), t) for s in F.SPEC)
        out["variants"][f"j{j}|x{k}"] = {"dex_total_conversion": float(np.log10(num / tot)),
                                         "dex_in_table_part": float(np.log10(intab / intab0)) if intab0 > 0 else None}
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps(out["exposure"])); print(json.dumps(out["variants"]))
