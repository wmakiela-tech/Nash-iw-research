"""PREREG_090 folding: hadron yield tables (authors' format) from per-primary multiplicities and BlackHawk primary spectra.

S_h(M) = sum_i  int dE  Phi_i(E; M) * n_{i->h}(E)      [1/s];  table value = S_h * hbar [GeV s]  (authors' units)
Phi_i: BlackHawk v2.3 instantaneous primary spectra (authors' settings, 100 energies 5-1e5 GeV, trapezoid in E).
n_{i->h}: mean number of hadron h per PRIMARY i (BlackHawk convention: per e+e- event / 2, except higgs: per event).
Sources of n:  'BH'   = BlackHawk BBN table (sum over final-energy bins), linear in E between its initial energies;
               'MC'   = PREREG_090 multiplicity JSON (PYTHIA 8.3 or Herwig 7.3), log-log linear between generated
                        energies, used for hadronic primaries at E >= E_lo(i); below E_lo(i) and for photon/e/mu the
                        BH PYTHIA table is used in every variant (common, declared).
               'BHc'  = BH PYTHIA table sampled at the MC energies and interpolated exactly like 'MC' (coarse-grid control).
"""
import json, math, os
import numpy as np

HBAR = 6.582119569e-25  # GeV s (CODATA 2018)
SPEC = ["pipm", "Kpm", "K0L", "proton", "neutron"]
PDG = {"pipm": 211, "Kpm": 321, "K0L": 130, "proton": 2212, "neutron": 2112}
TCOL = ["photon", "gluons", "higgs", "Wpm", "Z0", "electron", "muon", "tau", "up", "down", "charm", "strange", "top", "bottom"]
PCOL = {"photon": "photon", "gluons": "gluons", "higgs": "higgs", "Wpm": "W+-", "Z0": "Z0", "electron": "electron", "muon": "muon",
        "tau": "tau", "up": "up", "down": "down", "charm": "charm", "strange": "strange", "top": "top", "bottom": "bottom"}
MCNAME = {"gluons": "gluon", "higgs": "higgs", "Wpm": "Wpm", "Z0": "Z0", "tau": "tau", "up": "up", "down": "down",
          "charm": "charm", "strange": "strange", "top": "top", "bottom": "bottom"}
PAIR = {k: (0.5 if k != "higgs" else 1.0) for k in TCOL}


def load_bh(table_dir):
    """n[s][col] = (E_init array, multiplicity per primary array)."""
    out = {}
    for s in SPEC:
        a = np.loadtxt(os.path.join(table_dir, s + ".txt"), skiprows=1)
        Ei = np.unique(a[:, 0])
        out[s] = {}
        for ci, c in enumerate(TCOL):
            out[s][c] = (Ei, np.array([a[a[:, 0] == e, 2 + ci].sum() for e in Ei]))
    return out


def load_primary(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path)]
    hdr = rows[0]; data = np.array([[float(x) for x in r] for r in rows[1:]])
    k = data[:, 0].astype(int); ks = np.unique(k)
    m = np.array([data[k == q, 1][0] for q in ks])
    E = data[k == ks[0], hdr.index("energy")]
    Phi = {c: np.array([data[k == q, hdr.index(PCOL[c])] for q in ks]) for c in TCOL}
    return m, E, Phi


def load_mc(path):
    d = json.load(open(path))
    good = [e for e in d["energies"] if e.get("events", 0) > 0]
    E = np.array([e["E"] for e in good])
    return {s: (E, np.array([e[str(PDG[s])] for e in good]) * PAIR_MC(d["primary"]),
                np.array([e[f"se_{PDG[s]}"] for e in good]) * PAIR_MC(d["primary"])) for s in SPEC}


def PAIR_MC(name):
    return 1.0 if name == "higgs" else 0.5


def interp_lin(Ei, n, E):
    return np.interp(E, Ei, n, left=0.0, right=n[-1])


def interp_loglog(Ei, n, E):
    """log-log linear between nodes (zeros handled linearly); constant-slope extrapolation not allowed (clip)."""
    E = np.clip(E, Ei[0], Ei[-1])
    pos = n > 0
    if pos.all():
        return np.exp(np.interp(np.log(E), np.log(Ei), np.log(n)))
    return np.interp(np.log(E), np.log(Ei), n)


def nvec(src, s, c, E, bh, mc=None, elo=None):
    """multiplicity per primary on the folding grid E for species s and table column c."""
    base = interp_lin(*bh[s][c], E)
    if src == "BH" or c not in MCNAME:
        return base
    if src == "BHc":
        Em = mc[MCNAME[c]][s][0]
        nm = interp_lin(*bh[s][c], Em)
    else:
        Em, nm, _ = mc[MCNAME[c]][s]
    lo = max(elo[c], Em[0])
    v = interp_loglog(Em, nm, E)
    return np.where(E >= lo, v, base)


def fold(src, bh, m, E, Phi, mc=None, elo=None):
    Y = np.zeros((len(m), len(SPEC)))
    for si, s in enumerate(SPEC):
        for c in TCOL:
            n = nvec(src, s, c, E, bh, mc, elo)
            Y[:, si] += np.trapezoid(Phi[c] * n[None, :], E, axis=1)
    return Y


def stat_err(bh, m, E, Phi, mc, elo):
    """1-sigma statistical error of the MC part of the folded yield (errors of different primaries/energies
    combined in quadrature; within one primary the nodes' errors are propagated through the same interpolation)."""
    V = np.zeros((len(m), len(SPEC)))
    for si, s in enumerate(SPEC):
        for c in MCNAME:
            Em, nm, se = mc[MCNAME[c]][s]
            lo = max(elo[c], Em[0])
            for q in range(len(Em)):
                bump = nm.copy(); bump[q] += se[q]
                d = np.where(E >= lo, interp_loglog(Em, bump, E) - interp_loglog(Em, nm, E), 0.0)
                V[:, si] += np.trapezoid(Phi[c] * d[None, :], E, axis=1) ** 2
    return np.sqrt(V)


def write_table(path, m_g, Y):
    G = 5.609588603804452e23
    H = ("m_PBH [GeV]\tcharged_pion_dN_over_dt [GeV]\tcharged_kaon_dN_over_dt [GeV]\t"
         "kaon_zero_long_dN_over_dt [GeV]\tproton_dN_over_dt [GeV]\tneutron_dN_over_dt [GeV]")
    with open(path, "x") as f:
        f.write(H + "\n")
        for mg, y in zip(m_g, Y):
            f.write("\t".join(repr(float(x)) for x in [mg * G] + list(y * HBAR)) + "\n")
