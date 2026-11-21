"""PREREG_085 / GAP-005: build the primary HERWIG hadron table (rule R2) and the table-level gates G1, G2.

Usage: python3 -I combine_tables_085.py <G0> <P_lo> <P_hi> <H_hi> <H_R0> <out_R2_table> <out_json>
  G0   : PYTHIA (BBN) Emin 5 GeV, Emax 1e5 GeV, 100 primary energies (authors' setting, regenerated)
  P_lo : PYTHIA (BBN) [5, 25] GeV, 17 energies          P_hi : PYTHIA (BBN) [25, 1e5] GeV, 85 energies
  H_hi : HERWIG (BBN) [25, 1e5] GeV, 85 energies         H_R0 : HERWIG (BBN) [5, 1e5] GeV, 100 energies
         (H_R0 = BlackHawk's own below-table-Emin shift extrapolation for 5-25 GeV primaries)
Rules for primaries below the HERWIG table minimum (25 GeV):
  R2 (primary) = P_lo + H_hi  (PYTHIA where only PYTHIA has tables, HERWIG above 25 GeV; no silent extrapolation)
  R1 = H_hi (primaries below 25 GeV dropped)              R0 = H_R0 (BlackHawk native extrapolation)
Gates on rows k <= 28 (table masses <= 1.08e10 g, i.e. all rows the scan masses 6e8-1e10 g can touch, incl. the
two rows that define the authors' log-log extrapolation below 1e9 g):
  G1 split additivity : max |(P_lo + P_hi)/G0 - 1| <= 0.02 over 5 species        (stop if FAIL)
  G2 rule irrelevance : max |R0/R2 - 1| and max |R1/R2 - 1| <= 0.01 over 5 species (FAIL -> R1 sensitivity runs)
Writes R2 in the authors' format (same header; tab-separated; m column copied from the inputs, asserted identical).
"""
import json, sys
import numpy as np

HEADER = ("m_PBH [GeV]\tcharged_pion_dN_over_dt [GeV]\tcharged_kaon_dN_over_dt [GeV]\t"
          "kaon_zero_long_dN_over_dt [GeV]\tproton_dN_over_dt [GeV]\tneutron_dN_over_dt [GeV]")
SPECIES = ["pipm", "Kpm", "K0L", "proton", "neutron"]
KMAX = 28
GEV_PER_GRAM = 5.609588603804452e23  # only for reporting masses in grams (first G0 row / 1e9 g)


def load(p):
    with open(p) as f:
        assert f.readline().rstrip("\n") == HEADER, f"header {p}"
    a = np.loadtxt(p, skiprows=1)
    assert a.shape == (100, 6) and np.all(np.isfinite(a)) and np.all(a[:, 1:] >= 0), p
    return a


def main(g0, plo, phi, hhi, hr0, out_tab, out_json):
    G0, PL, PH, HH, H0 = (load(p) for p in (g0, plo, phi, hhi, hr0))
    for a in (PL, PH, HH, H0):
        assert np.array_equal(a[:, 0], G0[:, 0]), "mass column mismatch"
    R2 = G0.copy(); R2[:, 1:] = PL[:, 1:] + HH[:, 1:]
    R1 = HH; R0 = H0
    k = slice(0, KMAX + 1)
    rel = lambda a, b: np.abs(a[k, 1:] / b[k, 1:] - 1.0)
    SPLIT = np.c_[G0[:, 0], PL[:, 1:] + PH[:, 1:]]
    g1 = rel(SPLIT, G0)
    g2a = rel(R0, R2); g2b = rel(R1, R2)
    out = {
        "rows_checked": [0, KMAX],
        "m_gram_rows": [float(G0[0, 0] / GEV_PER_GRAM), float(G0[KMAX, 0] / GEV_PER_GRAM)],
        "G1_SPLIT_ADDITIVITY": {"max_rel_per_species": dict(zip(SPECIES, g1.max(axis=0).tolist())),
                                "max": float(g1.max()), "threshold": 0.02, "pass": bool(g1.max() <= 0.02)},
        "G2_RULE_IRRELEVANCE": {"R0_vs_R2_max_rel_per_species": dict(zip(SPECIES, g2a.max(axis=0).tolist())),
                                "R1_vs_R2_max_rel_per_species": dict(zip(SPECIES, g2b.max(axis=0).tolist())),
                                "max": float(max(g2a.max(), g2b.max())), "threshold": 0.01,
                                "pass": bool(max(g2a.max(), g2b.max()) <= 0.01)},
        "descriptive": {
            "log10_R2_over_G0_rows_0_28": {s: np.log10(R2[k, i + 1] / G0[k, i + 1]).tolist() for i, s in enumerate(SPECIES)},
            "sub25GeV_fraction_P_lo_over_P_lo_plus_P_hi_rows_0_28": {
                s: (PL[k, i + 1] / (PL[k, i + 1] + PH[k, i + 1])).tolist() for i, s in enumerate(SPECIES)},
            "loglog_extrapolation_slope_rows01": {
                "G0": {s: float(np.log(G0[1, i + 1] / G0[0, i + 1]) / np.log(G0[1, 0] / G0[0, 0])) for i, s in enumerate(SPECIES)},
                "R2": {s: float(np.log(R2[1, i + 1] / R2[0, i + 1]) / np.log(R2[1, 0] / R2[0, 0])) for i, s in enumerate(SPECIES)}},
        },
    }
    with open(out_tab, "x") as f:
        f.write(HEADER + "\n")
        for row in R2:
            f.write("\t".join(repr(float(x)) for x in row) + "\n")
    json.dump(out, open(out_json, "x"), indent=1)
    print(json.dumps({"G1": out["G1_SPLIT_ADDITIVITY"]["pass"], "G1_max": out["G1_SPLIT_ADDITIVITY"]["max"],
                      "G2": out["G2_RULE_IRRELEVANCE"]["pass"], "G2_max": out["G2_RULE_IRRELEVANCE"]["max"]}))
    sys.exit(0 if out["G1_SPLIT_ADDITIVITY"]["pass"] else 7)


if __name__ == "__main__":
    main(*sys.argv[1:8])
