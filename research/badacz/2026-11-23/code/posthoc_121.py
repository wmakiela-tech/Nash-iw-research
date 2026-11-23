#!/usr/bin/env python3
"""POST HOC to PREREG_121 (not preregistered; labelled as such in REVIEW_122).
(1) HERWIG coarse-bin estimator calibration: PYTHIA counts re-binned into the HERWIG final-energy bins, same Ebar estimator;
    bias b = eps_coarse / eps_fine, evaluated at PYTHIA E'_PY = E'_HW / 2 (same jet energy as HERWIG at sqrt(s) = E').
(2) Per-channel mass-level ledger at selected masses (power share, energy excess, hadron-count share), and the ledger as
    BlackHawk assembles it (primary photons and electrons also added directly, secondary.c l.724-736).
(3) Higgs column: formatting.c l.70 does not divide by 2 while table_higgs.cc sets eCM = 2E'. Energy-consistent variant
    within the same generator setup: nu_H(E') -> nu_H(E'/2) (event at eCM = E'). Effect on the authors' hadron counts.
(4) Gluon (and other) columns are zero for E' <= 61.26 GeV: share of primary power below that energy.
Usage: python3 -I posthoc_121.py <pythia_tables> <herwig_tables> <primary_spectra_090.tsv.gz> <fcode_119.csv> <fM.txt> <out.json>
"""
import csv, gzip, json, sys
import numpy as np

PY, HW, PRIM, FCODE, FM, OUT = sys.argv[1:7]
FIN = ["photon", "electron", "muon", "nue", "numu", "nutau", "pipm", "Kpm", "K0L", "proton", "neutron"]
HAD = FIN[6:]; QG = ["up", "down", "charm", "strange", "bottom", "gluons"]; HBAR = 6.582119569e-25


def load(d):
    N = {}
    for j in FIN:
        h = open(f"{d}/{j}.txt").readline().split(); a = np.loadtxt(f"{d}/{j}.txt", skiprows=1)
        Ei = np.unique(a[:, 0]); Ef = np.unique(a[:, 1]); N[j] = np.abs(a[:, 2:]).reshape(len(Ei), len(Ef), len(h) - 2)
    return h[2:], Ei, Ef, N


def ebar(Ef):
    r = Ef[1:] / Ef[:-1]
    return np.append((Ef[1:] - Ef[:-1]) / np.log(r), Ef[-1] * (r[-1] - 1) / np.log(r[-1]))


pr, Ei, Ef, N = load(PY); prh, Eih, Efh, Nh = load(HW)
Eb, Ebh = ebar(Ef), ebar(Efh)
out = {"post_hoc": True}
# (1) coarse-bin calibration
idx = np.clip(np.searchsorted(Efh, Eb, side="right") - 1, 0, len(Efh) - 1)       # HW bin containing each PY bin centre
cal = {}
for p in QG:
    ip, iph = pr.index(p), prh.index(p); rows = []
    for e in range(len(Eih)):
        if Eih[e] < 100.0:
            continue
        ePY = np.argmin(np.abs(np.log(Ei / (Eih[e] / 2))))                     # PYTHIA at jet energy E'_HW / 2
        fine = sum(N[j][ePY][:, ip] @ Eb for j in FIN) / Ei[ePY]
        coarse = sum(np.bincount(idx, weights=N[j][ePY][:, ip], minlength=len(Efh)) @ Ebh for j in FIN) / Ei[ePY]
        hw = sum(Nh[j][e][:, iph] @ Ebh for j in FIN) / Eih[e]
        rows.append((float(Eih[e]), float(fine), float(coarse / fine), float(hw), float(hw / (coarse / fine))))
    a = np.array(rows)
    cal[p] = {"bias_minmax": [float(a[:, 2].min()), float(a[:, 2].max())], "eps_hw_mid_minmax": [float(a[:, 3].min()), float(a[:, 3].max())],
              "eps_hw_corrected_minmax": [float(a[:, 4].min()), float(a[:, 4].max())]}
out["herwig_coarse_bin_calibration"] = cal
# (2)-(4) mass level
fc = list(csv.DictReader(open(FCODE))); GpG = float(np.median([float(r["M_GeV"]) / float(r["M_g"]) for r in fc]))
fm = [l.split() for l in open(FM) if l.strip()]; fmM = np.array([float(x[0]) for x in fm[1:]]); fBH = np.array([float(x[1]) for x in fm[1:]])
rows = [l.rstrip("\n").split("\t") for l in gzip.open(PRIM, "rt")]; h = rows[0]; dat = np.array([[float(x) for x in r] for r in rows[1:]])
chan = [c for c in h if c not in ("k", "m_g", "energy")]; cmap = {c: ("Wpm" if c == "W+-" else c) for c in chan}
lE = np.log(Ei)
eall = np.stack([sum(N[j][e].T @ Eb for j in FIN) / Ei[e] for e in range(len(Ei))])
nu = {hh: np.stack([N[hh][e].sum(axis=0) for e in range(len(Ei))]) for hh in HAD}
ms = np.unique(dat[:, 1]); res = []
for mg in ms:
    s = dat[dat[:, 1] == mg]; s = s[np.argsort(s[:, h.index("energy")])]; E = s[:, h.index("energy")]; x = np.log(E)
    P = {c: float(np.trapezoid(E * E * s[:, h.index(c)], x)) for c in chan}; Ptot = sum(P.values())
    Nch = {}; exc = {}
    for c in chan:
        Phi = s[:, h.index(c)]
        if cmap[c] not in pr:
            continue
        ip = pr.index(cmap[c])
        exc[c] = float(np.trapezoid(E * E * Phi * (np.interp(x, lE, eall[:, ip], left=0.0) - 1), x)) / Ptot
        Nch[c] = np.array([float(np.trapezoid(E * Phi * np.interp(x, lE, nu[hh][:, ip], left=0.0), x)) for hh in HAD])
    Ntot = sum(Nch.values())
    ipH = pr.index("higgs"); PhiH = s[:, h.index("higgs")]
    NH_half = np.array([float(np.trapezoid(E * PhiH * np.interp(np.log(E / 2), lE, nu[hh][:, ipH], left=0.0), x)) for hh in HAD])
    PfM = float(np.exp(np.interp(np.log(mg * GpG), np.log(fmM), np.log(fBH)))) / (mg * GpG) ** 2 / HBAR
    below61 = {c: float(np.trapezoid((E * E * s[:, h.index(c)])[E <= 61.27], x[E <= 61.27])) / Ptot if (E <= 61.27).sum() > 1 else 0.0 for c in ("gluons",)}
    res.append({"M_g": float(mg), "power_share": {c: P[c] / Ptot for c in chan}, "energy_excess_over_Ptot": exc,
                "r_all_as_prereg": 1 + sum(exc.values()),
                "r_blackhawk_assembly": 1 + sum(exc.values()) + P["photon"] / Ptot + P["electron"] / Ptot,
                "hadron_share_higgs": (Nch["higgs"] / Ntot).tolist(), "hadron_share_Z0": (Nch["Z0"] / Ntot).tolist(),
                "higgs_energy_consistent_dN_over_N": ((NH_half - Nch["higgs"]) / Ntot).tolist(),
                "gluon_power_share_below_61GeV": below61["gluons"], "P_spec_over_P_fM": Ptot / PfM})
out["mass_level"] = res
json.dump(out, open(OUT, "w"), indent=1, sort_keys=True)
pick = [r for r in res if any(abs(r["M_g"] / m - 1) < 0.05 for m in (1e9, 3.5e9, 1e10, 1e11, 1e12))]
print(json.dumps({"cal": cal, "pick": [{k: (v if not isinstance(v, dict) else {kk: round(vv, 4) for kk, vv in v.items()}) for k, v in r.items()} for r in pick]}, indent=0)[:6000])
