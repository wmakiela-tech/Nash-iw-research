"""PREREG_109: table Sc = sqrt(s)-label-corrected BlackHawk HERWIG table with the missing primary range 5e4-1e5 GeV filled by
Herwig 7.1.5 (the vintage matched in REVIEW_106) at the correct sqrt(s) = 2E, plus a bitwise rebuild check of Sa.
Usage: python3 -I build_tables_109.py <hadronization_tables_dir> <primary.tsv> <mc090_dir> <R2_table> <mc109_dir> <out_dir>
  Sc = PY(E<12.5)/BIN_PY + HS_c(E>=12.5)/BIN_HW, HS_c = relabelled HERWIG rows (E'->E'/2; higgs not relabelled) up to 5e4 GeV;
  above 5e4 GeV: Herwig 7.1.5 multiplicities per primary (mc109/herwig71_<channel>.json, sqrt(s) = 2E, E in {5e4, 7.07e4, 1e5},
  log-log in E) for the 10 hadronic MC channels; constant n(5e4) (as Sa) for photon/electron/muon; higgs uses its own rows.
  Sa is rebuilt identically to PREREG_099 (must equal data/hadrons_099_Sa.dat bitwise: G_REBUILD in run109.sh).
--- docstring of build_tables_099.py follows ---
PREREG_099: hadron-yield tables (authors' format) for the native test of the sqrt(s)-label correction of the BlackHawk
v2.3 HERWIG BBN tables (REVIEW_098). Folding as PREREG_090 (fold_090.py: S_h(M) = sum_c int dE Phi_c(E;M) n_c->h(E)).
Usage: python3 -I build_tables_099.py <hadronization_tables_dir> <primary.tsv> <mc090_dir> <R2_table> <out_dir>
Multiplicities per primary n_c(E) on the primary grid E (5..1e5 GeV):
  PY : BlackHawk PYTHIA BBN table (E' = E, correct label), linear in E between nodes (as fold_090 'BH').
  HL : BlackHawk HERWIG table as labelled (row E' used for primary E = E'), E in [25, 1e5].
  HS : HERWIG table relabelled: row E' used for primary E = E'/2 (tables were generated at sqrt(s) = E'), E in [12.5, 5e4];
       the 'higgs' column is NOT relabelled (single primary of energy sqrt(s) = E').
       Above 5e4 GeV (no HERWIG data):  (a) constant n_HS(5e4);  (b) n_HS(5e4) x n_H73(E)/n_H73(5e4) with Herwig 7.3
       multiplicities of PREREG_090 (mc090, sqrt(s) = 2E, log-log) for hadronic channels; constant for photon/e/mu.
Tables (part below the split energy uses PY, above uses HERWIG; each part divided by its BlackHawk binning factor to mimic
  BlackHawk + the authors' ln E trapezoid, as the 085 R2 table):
  L  = PY(E<25)/BIN_PY + HL(E>=25)/BIN_HW                    -- control, must reproduce R2 (G_CTRL)
  Sa = PY(E<12.5)/BIN_PY + HS_a(E>=12.5)/BIN_HW               -- sqrt(s) fix, HERWIG binning convention kept
  Sb = PY(E<12.5)/BIN_PY + HS_b(E>=12.5)/BIN_HW               -- same, other extrapolation above 5e4
  Ua = PY(E<12.5)/BIN_PY + HS_a(E>=12.5)/BIN_PY               -- sqrt(s) fix + binning convention of the PY/H73 tables
Gates: G_CTRL max |L/R2 - 1| <= 0.01 on rows 0-28, all 5 species; G_FINITE all yields finite and > 0."""
import json, os, sys
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "2026-11-21", "code"))
import fold_090 as F

hdir, prim, mcdir, r2, mc109, out = sys.argv[1:7]
os.makedirs(out, exist_ok=True)
DL_PY = np.log(1e11) / 499; BIN_PY = (np.exp(DL_PY) - 1) / DL_PY
DL_HW = np.log(1e11) / 99; BIN_HW = (np.exp(DL_HW) - 1) / DL_HW
bhP = F.load_bh(os.path.join(hdir, "pythia_tables")); bhH = F.load_bh(os.path.join(hdir, "herwig_tables"))
m, E, Phi = F.load_primary(prim)
K = slice(0, 29)
H73 = {}
for c, name in F.MCNAME.items():
    d = json.load(open(os.path.join(mcdir, f"herwig_{name}.json")))
    good = [e for e in d["energies"] if e.get("events", 0) > 0]
    H73[c] = {s: (np.array([e["E"] for e in good]), np.array([e[str(F.PDG[s])] for e in good])) for s in F.SPEC}


def n_py(s, c):
    return F.interp_lin(*bhP[s][c], E)


def n_hl(s, c):
    Ei, n = bhH[s][c]
    return np.where(E >= Ei[0], np.interp(E, Ei, n), 0.0)


def n_hs(s, c, ext):
    Ei, n = bhH[s][c]
    Er = Ei if c == "higgs" else Ei / 2
    v = np.where(E >= Er[0], np.interp(E, Er, n), 0.0)
    top = Er[-1]; above = E > top
    if ext == "b" and c in H73 and c != "higgs":
        Em, nm = H73[c][s]
        g = F.interp_loglog(Em, nm, E) / F.interp_loglog(Em, nm, np.array([top]))[0]
        v = np.where(above, n[-1] * g, v)
    else:
        v = np.where(above, n[-1], v)
    return v


def load_mc_ok(path):
    """as fold_090.load_mc, but energies with a failed run (rc_run != 0 or events null) are dropped (DEV-2: top at 1e5 GeV)."""
    d = json.load(open(path))
    good = [e for e in d["energies"] if e.get("rc_run") == 0 and (e.get("events") or 0) > 0]
    Em = np.array([e["E"] for e in good])
    return {s: (Em, np.array([e[str(F.PDG[s])] for e in good]) * F.PAIR_MC(d["primary"]),
                np.array([e[f"se_{F.PDG[s]}"] for e in good]) * F.PAIR_MC(d["primary"])) for s in F.SPEC}


H71 = {c: load_mc_ok(os.path.join(mc109, f"herwig71_{name}.json")) for c, name in F.MCNAME.items() if c != "higgs"}


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
    Y = np.zeros((len(m), len(F.SPEC)))
    lo = E < split
    for si, s in enumerate(F.SPEC):
        for c in F.TCOL:
            Y[:, si] += np.trapezoid(Phi[c] * np.where(lo, n_lo(s, c), 0.0)[None, :], E, axis=1) / b_lo
            Y[:, si] += np.trapezoid(Phi[c] * np.where(~lo, n_hi(s, c), 0.0)[None, :], E, axis=1) / b_hi
    return Y


Y = {"L": fold_parts(n_py, n_hl, 25.0, BIN_PY, BIN_HW),
     "Sa": fold_parts(n_py, lambda s, c: n_hs(s, c, "a"), 12.5, BIN_PY, BIN_HW),
     "Sc": fold_parts(n_py, n_hc, 12.5, BIN_PY, BIN_HW)}
R = np.loadtxt(r2, skiprows=1)[:, 1:] / F.HBAR
rc = Y["L"][K] / R[K]
res = {"gates": {}, "descriptive": {}, "constants": {"BIN_PY": BIN_PY, "BIN_HW": BIN_HW}}
res["gates"]["G_CTRL"] = {"ratio_min": float(rc.min()), "ratio_max": float(rc.max()), "pass": bool(np.max(np.abs(rc - 1)) <= 0.01)}
res["gates"]["G_FINITE"] = {"pass": bool(all(np.all(np.isfinite(v)) and np.all(v[K] > 0) for v in Y.values()))}
for k in ("Sa", "Sc"):
    res["descriptive"][f"log10_{k}_over_L_rows0_28_min_max"] = {s: [float(np.log10(Y[k][K, i] / Y["L"][K, i]).min()), float(np.log10(Y[k][K, i] / Y["L"][K, i]).max())] for i, s in enumerate(F.SPEC)}
for k, v in Y.items():
    F.write_table(os.path.join(out, f"{k}.dat"), m, v)
json.dump(res, open(os.path.join(out, "tables109.json"), "x"), indent=1)
print(json.dumps(res["gates"])); print(json.dumps(res["descriptive"]))
sys.exit(0 if all(g["pass"] for g in res["gates"].values()) else 7)
