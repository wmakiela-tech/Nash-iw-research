"""POST HOC to PREREG_109 (answer to Mech-S10 ROT018; table level only, no native run): sensitivity of table Sc to the missing
Herwig 7.1.5 top endpoint at E = 1e5 GeV (DEV-2). In Sc the top multiplicity above E_last = 7.07e4 GeV is held at n(E_last)
(fold_090.interp_loglog clip). Here only that top segment (E > E_last) is replaced by n(E_last) x k for k in {0, 0.5, 2, 3}
(brackets far wider than any physical multiplicity growth over a factor 1.41 in energy) and by the log-log continuation of
the 5e4 -> 7.07e4 top slope. Reported: max |log10(Sc_alt / Sc)| over rows 0-28 and the 5 species, and the share of the top
segment E > E_last in each yield. Same fold as build_tables_109.py (Sc reproduced first and compared with the run's Sc.dat).
Usage: python3 -I posthoc_109b.py <hadronization_tables_dir> <primary.tsv> <mc109_dir> <Sc.dat of the run> <out.json>"""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "2026-11-21", "code"))
import fold_090 as F

hdir, prim, mc109, scdat, dst = sys.argv[1:6]
DL_PY = np.log(1e11) / 499; BIN_PY = (np.exp(DL_PY) - 1) / DL_PY
DL_HW = np.log(1e11) / 99; BIN_HW = (np.exp(DL_HW) - 1) / DL_HW
bhP = F.load_bh(os.path.join(hdir, "pythia_tables")); bhH = F.load_bh(os.path.join(hdir, "herwig_tables"))
m, E, Phi = F.load_primary(prim)
K = slice(0, 29)


def load_mc_ok(path):
    d = json.load(open(path))
    good = [e for e in d["energies"] if e.get("rc_run") == 0 and (e.get("events") or 0) > 0]
    Em = np.array([e["E"] for e in good])
    return {s: (Em, np.array([e[str(F.PDG[s])] for e in good]) * F.PAIR_MC(d["primary"])) for s in F.SPEC}


H71 = {c: load_mc_ok(os.path.join(mc109, f"herwig71_{name}.json")) for c, name in F.MCNAME.items() if c != "higgs"}
TOPC = [c for c in H71 if F.MCNAME[c] == "top"][0]
E_last = H71[TOPC][F.SPEC[0]][0].max()


def n_py(s, c):
    return F.interp_lin(*bhP[s][c], E)


def n_hc(s, c, mode=None):
    Ei, n = bhH[s][c]
    Er = Ei if c == "higgs" else Ei / 2
    v = np.where(E >= Er[0], np.interp(E, Er, n), 0.0)
    top = Er[-1]; above = E > top
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


def fold(mode=None, only_top_seg=False):
    Y = np.zeros((len(m), len(F.SPEC)))
    lo = E < 12.5
    for si, s in enumerate(F.SPEC):
        for c in F.TCOL:
            if only_top_seg:
                if c != TOPC:
                    continue
                Y[:, si] += np.trapezoid(Phi[c] * np.where(E > E_last, n_hc(s, c), 0.0)[None, :], E, axis=1) / BIN_HW
                continue
            Y[:, si] += np.trapezoid(Phi[c] * np.where(lo, n_py(s, c), 0.0)[None, :], E, axis=1) / BIN_PY
            Y[:, si] += np.trapezoid(Phi[c] * np.where(~lo, n_hc(s, c, mode), 0.0)[None, :], E, axis=1) / BIN_HW
    return Y


Sc = fold()
ref = np.loadtxt(scdat, skiprows=1)[:, 1:] / F.HBAR
out = {"E_last_top": float(E_last), "reproduce_Sc_max_rel": float(np.max(np.abs(Sc[K] / ref[K] - 1))), "scenarios": {}}
for mode in ["0", "0.5", "2", "3", "slope"]:
    A = fold(mode)
    out["scenarios"][mode] = float(np.max(np.abs(np.log10(A[K] / Sc[K]))))
seg = fold(only_top_seg=True)
out["top_segment_share_max_rows0_28"] = float(np.max(seg[K] / Sc[K]))
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps(out))
