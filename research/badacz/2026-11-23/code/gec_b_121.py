#!/usr/bin/env python3
"""PREREG_121: G_EC+(b), energy ledger of the BlackHawk v2.3 BBN hadronization tables and of the Wu-Xu hadron table.
Part T (tables): per primary particle i and primary energy E', energy fraction carried by the 11 tabulated secondaries
  eps_all_i(E') = sum_j sum_k Ebar_k N_jki(E') / E',   Ebar_k = (E_{k+1} - E_k) / ln(E_{k+1}/E_k)
  (N = tabulated count per primary in final bin [E_k, E_{k+1}], BlackHawk secondary.c l.138 convention; final energies are
  total energies: lowest nonzero proton bin contains m_p). Brackets: Ebar -> E_k (lo), E_{k+1} (hi). Also eps_had (5 BBN
  hadron species) and nu_had (counts per primary).
Part M (masses): 090 primary spectra (BlackHawk v2.3, 16 channels, E' = 5..1e5 GeV x 100) folded with the PYTHIA tables:
  N_h(M) = sum_i int Phi_i nu_ih dE',  P_sec(M) = sum_i int Phi_i E' eps_all_i dE' (+ neutrinos + graviton passed as is),
  vs the authors' table hadrons_from_PBH.dat (d395183) and the full BlackHawk power f_BH(M)/M^2 (fM.txt, a = 0).
Thresholds frozen in PREREG_121.
Usage: python3 -I gec_b_121.py <pythia_tables> <herwig_tables> <primary_spectra_090.tsv.gz> <hadrons_from_PBH.dat>
       <fM.txt> <fcode_119.csv> <out.json>
"""
import csv, gzip, hashlib, json, sys
import numpy as np

PY, HW, PRIM, AUTH, FM, FCODE, OUT = sys.argv[1:8]
HBAR = 6.582119569e-25
FIN = ["photon", "electron", "muon", "nue", "numu", "nutau", "pipm", "Kpm", "K0L", "proton", "neutron"]
HAD = ["pipm", "Kpm", "K0L", "proton", "neutron"]
QG = ["up", "down", "charm", "strange", "bottom", "gluons"]
TOL = {"T1": (0.90, 1.05), "T2": (0.45, 0.55), "NUM": 0.03, "M1": (0.90, 1.05)}


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def load_tab(d):
    N = {}; hdr = None
    for j in FIN:
        h = open(f"{d}/{j}.txt").readline().split()
        a = np.loadtxt(f"{d}/{j}.txt", skiprows=1)
        if hdr is None:
            hdr = h; Ei = np.unique(a[:, 0]); Ef = np.unique(a[:, 1])
        assert h == hdr
        N[j] = np.abs(a[:, 2:]).reshape(len(Ei), len(Ef), len(hdr) - 2)   # [E', E_k, primary]; BlackHawk takes fabs
        assert np.allclose(a[:, 0].reshape(len(Ei), len(Ef))[:, 0], Ei) and np.allclose(a[:, 1].reshape(len(Ei), len(Ef))[0], Ef)
    return hdr[2:], Ei, Ef, N


def ledger(prims, Ei, Ef, N):
    r = Ef[1:] / Ef[:-1]
    Ebar = np.append((Ef[1:] - Ef[:-1]) / np.log(r), Ef[-1] * (r[-1] - 1) / np.log(r[-1]))
    Elo = Ef.copy(); Ehi = np.append(Ef[1:], Ef[-1] * r[-1])
    out = {}
    for name, E in (("mid", Ebar), ("lo", Elo), ("hi", Ehi)):
        out[f"eps_all_{name}"] = np.stack([sum(N[j][e].T @ E for j in FIN) / Ei[e] for e in range(len(Ei))])  # [E', primary]
        out[f"eps_had_{name}"] = np.stack([sum(N[j][e].T @ E for j in HAD) / Ei[e] for e in range(len(Ei))])
    out["nu"] = {h: np.stack([N[h][e].sum(axis=0) for e in range(len(Ei))]) for h in HAD}   # counts per primary
    return out


res = {"inputs_sha256": {}, "tol": TOL, "T": {}, "M": {}, "predictions": {}, "gates": {}}
for p in (PRIM, AUTH, FM, FCODE):
    res["inputs_sha256"][p.split("/")[-1]] = sha(p)
for d in (PY, HW):
    for j in FIN:
        res["inputs_sha256"][f"{d.rstrip('/').split('/')[-1]}/{j}.txt"] = sha(f"{d}/{j}.txt")

tabs = {}
for tag, d in (("pythia", PY), ("herwig", HW)):
    prims, Ei, Ef, N = load_tab(d)
    L = ledger(prims, Ei, Ef, N); tabs[tag] = (prims, Ei, Ef, N, L)
    T = res["T"][tag] = {"n_Eprim": len(Ei), "n_Efin": len(Ef), "Eprim_range": [float(Ei[0]), float(Ei[-1])],
                         "dln_Efin": float(np.log(Ef[1] / Ef[0])), "per_primary": {}}
    for ip, p in enumerate(prims):
        lo = 400.0 if p == "top" else (200.0 if p in ("Wpm", "Z0", "higgs") else 50.0)
        sel = Ei >= lo
        T["per_primary"][p] = {"Eprim_min_used": lo,
            **{f"{k}_minmax": [float(L[k][sel, ip].min()), float(L[k][sel, ip].max())] for k in ("eps_all_mid", "eps_all_lo", "eps_all_hi", "eps_had_mid")},
            "eps_all_mid_at": {f"{e:g}": float(np.interp(np.log(e), np.log(Ei), L["eps_all_mid"][:, ip])) for e in (50.0, 1e3, 1e4, 1e5) if e >= Ei[0]},
            "eps_had_mid_at": {f"{e:g}": float(np.interp(np.log(e), np.log(Ei), L["eps_had_mid"][:, ip])) for e in (50.0, 1e3, 1e4, 1e5) if e >= Ei[0]}}

pp = res["T"]["pythia"]["per_primary"]
res["predictions"]["P_T1_pythia_energy_conservation"] = {"band": TOL["T1"], "PASS": all(
    TOL["T1"][0] <= v["eps_all_mid_minmax"][0] and v["eps_all_mid_minmax"][1] <= TOL["T1"][1] for v in pp.values())}
prims_h, Ei_h = tabs["herwig"][0], tabs["herwig"][1]; Lh = tabs["herwig"][4]; sel = Ei_h >= 100.0
hv = {p: [float(Lh["eps_all_mid"][sel, prims_h.index(p)].min()), float(Lh["eps_all_mid"][sel, prims_h.index(p)].max())] for p in QG}
res["predictions"]["P_T2_herwig_half_energy"] = {"band": TOL["T2"], "values_minmax": hv,
    "PASS": all(TOL["T2"][0] <= v[0] and v[1] <= TOL["T2"][1] for v in hv.values())}

# ---------------- Part M ----------------
fc = list(csv.DictReader(open(FCODE)))
GeV_per_g = float(np.median([float(r["M_GeV"]) / float(r["M_g"]) for r in fc]))
fm = [l.split() for l in open(FM) if l.strip()]
fmM = np.array([float(x[0]) for x in fm[1:]]); fBH = np.array([float(x[1]) for x in fm[1:]])
op = gzip.open if PRIM.endswith(".gz") else open
rows = [l.rstrip("\n").split("\t") for l in op(PRIM, "rt")]
h = rows[0]; dat = np.array([[float(x) for x in r] for r in rows[1:]])
chan = [c for c in h if c not in ("k", "m_g", "energy")]
cmap = {c: ("Wpm" if c == "W+-" else c) for c in chan}
prims, Ei, Ef, N, L = tabs["pythia"]
assert set(cmap[c] for c in chan if c not in ("neutrinos", "graviton")) == set(prims)
BIN = float((np.exp(np.log(Ef[1] / Ef[0])) - 1) / np.log(Ef[1] / Ef[0]))
auth = np.loadtxt(AUTH, comments="#") if not open(AUTH).readline()[0].isalpha() else np.loadtxt(AUTH, skiprows=1)
auth_Mg = auth[:, 0] / GeV_per_g; auth_q = auth[:, 1:6] / HBAR      # authors' units: GeV (natural) -> s^-1
ms = np.unique(dat[:, 1]); rowsM = []
for mg in ms:
    s = dat[dat[:, 1] == mg]; s = s[np.argsort(s[:, h.index("energy")])]; E = s[:, h.index("energy")]; x = np.log(E)
    Pspec = float(np.trapezoid(E * E * sum(s[:, h.index(c)] for c in chan), x))
    Psec = 0.0; Phad = 0.0; Nh = np.zeros(5)
    for c in chan:
        Phi = s[:, h.index(c)]
        if cmap[c] in prims:
            ip = prims.index(cmap[c])
            ea = np.interp(x, np.log(Ei), L["eps_all_mid"][:, ip], left=0.0)
            eh = np.interp(x, np.log(Ei), L["eps_had_mid"][:, ip], left=0.0)
            Psec += float(np.trapezoid(E * E * Phi * ea, x)); Phad += float(np.trapezoid(E * E * Phi * eh, x))
            for k, hh in enumerate(HAD):
                Nh[k] += float(np.trapezoid(E * Phi * np.interp(x, np.log(Ei), L["nu"][hh][:, ip], left=0.0), x))
        else:   # neutrinos, graviton: not hadronized, energy passed as is
            Psec += float(np.trapezoid(E * E * Phi, x))
    PfM = float(np.exp(np.interp(np.log(mg * GeV_per_g), np.log(fmM), np.log(fBH)))) / (mg * GeV_per_g) ** 2 / HBAR
    ia = int(np.argmin(np.abs(auth_Mg / mg - 1)))
    rowsM.append({"M_g": float(mg), "r_all": Psec / Pspec, "r_had_of_P_fM": Phad / PfM, "P_spec_over_P_fM": Pspec / PfM,
                  "auth_M_rel": float(auth_Mg[ia] / mg - 1), "auth_times_BIN_over_mine": (auth_q[ia] * BIN / Nh).tolist(),
                  "n_E_per_GeV_of_P_fM": (Nh / PfM).tolist(), "auth_n_E_per_GeV_of_P_fM": (auth_q[ia] / PfM).tolist()})
res["M"] = {"rows": rowsM, "BIN_pythia": BIN, "GeV_per_g": GeV_per_g, "channels": chan}
selM = [r for r in rowsM if 2e9 <= r["M_g"] <= 1e11]
res["gates"]["G_NUM_authors_table_reproduced"] = {"n": len(selM), "tol": TOL["NUM"],
    "max_abs_dev": float(max(abs(v - 1) for r in selM for v in r["auth_times_BIN_over_mine"])),
    "max_mass_mismatch": float(max(abs(r["auth_M_rel"]) for r in selM))}
res["gates"]["G_NUM_authors_table_reproduced"]["PASS"] = bool(res["gates"]["G_NUM_authors_table_reproduced"]["max_abs_dev"] <= TOL["NUM"]
                                                              and res["gates"]["G_NUM_authors_table_reproduced"]["max_mass_mismatch"] < 1e-4)
res["predictions"]["P_M1_mass_level_ledger"] = {"band": TOL["M1"], "minmax": [min(r["r_all"] for r in selM), max(r["r_all"] for r in selM)],
    "PASS": all(TOL["M1"][0] <= r["r_all"] <= TOL["M1"][1] for r in selM)}
lnM = np.log(auth_Mg[:2]); res["M"]["authors_rows01_slope_dlnq_dlnM"] = ((np.log(auth_q[1]) - np.log(auth_q[0])) / (lnM[1] - lnM[0])).tolist()
json.dump(res, open(OUT, "w"), indent=1, sort_keys=True)
print(json.dumps({"gates": {k: v["PASS"] for k, v in res["gates"].items()}, "predictions": {k: v["PASS"] for k, v in res["predictions"].items()}}, indent=1))
