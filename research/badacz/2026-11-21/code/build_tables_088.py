"""PREREG_088 (E4, table domain below 1e9 g): build two hadron tables for the j22 native test.
Usage: python3 -I build_tables_088.py <authors_table> <direct_rows_1e8_1e9> <out_A> <out_C> <out_json>
A (lower bracket, artifact of the 1e5 GeV primary ceiling): the 10 direct BlackHawk PYTHIA-BBN rows 1e8..7.94e8 g
  (authors' settings; data/hadrons_087_PY_rows_1e8_1e9.dat without its 1e9 g row) prepended to the authors' 100 rows.
C (untruncated trend): rows 0-4 of the authors' table replaced, and 10 rows 1e8..7.94e8 g prepended, by a per-species
  power law anchored at authors' row 5 with the mean local log-log slope of rows 5-10 (rows not visibly affected by the
  ceiling, SYNTH_087 sec. 3). Rows 5-99 are copied verbatim.
Both: header and format of the authors' file; masses strictly increasing (asserted)."""
import json, sys
import numpy as np

H = ("m_PBH [GeV]\tcharged_pion_dN_over_dt [GeV]\tcharged_kaon_dN_over_dt [GeV]\t"
     "kaon_zero_long_dN_over_dt [GeV]\tproton_dN_over_dt [GeV]\tneutron_dN_over_dt [GeV]")
auth, rows, oa, oc, oj = sys.argv[1:6]
assert open(auth).readline().rstrip("\n") == H
A = np.loadtxt(auth, skiprows=1); R = np.loadtxt(rows, skiprows=1)
assert A.shape == (100, 6) and R.shape == (11, 6) and abs(R[-1, 0] / A[0, 0] - 1) < 1e-12
low = R[:-1]
TA = np.vstack([low, A])
lm = np.log(A[:, 0])
sl = np.array([np.mean([(np.log(A[i + 1, k]) - np.log(A[i, k])) / (lm[i + 1] - lm[i]) for i in range(5, 11)]) for k in range(1, 6)])
def cont(m):
    return np.exp(np.log(A[5, 1:]) + sl * (np.log(m) - lm[5]))
TC = A.copy()
for i in range(5):
    TC[i, 1:] = cont(A[i, 0])
TC = np.vstack([np.c_[low[:, 0], np.array([cont(m) for m in low[:, 0]])], TC])
for T in (TA, TC):
    assert T.shape == (110, 6) and np.all(np.diff(T[:, 0]) > 0) and np.all(T[:, 1:] > 0)
for T, o in ((TA, oa), (TC, oc)):
    with open(o, "x") as f:
        f.write(H + "\n")
        for r in T:
            f.write("\t".join(repr(float(x)) for x in r) + "\n")
info = {"slopes_rows5_10": sl.tolist(),
        "C_over_authors_log10_rows0_4": np.log10(TC[10:15, 1:] / A[0:5, 1:]).tolist(),
        "C_over_A_log10_prepended_rows": np.log10(TC[:10, 1:] / TA[:10, 1:]).tolist(),
        "rows_5_99_verbatim": bool(np.array_equal(TC[15:], A[5:])) and bool(np.array_equal(TA[10:], A))}
json.dump(info, open(oj, "x"), indent=1)
print(json.dumps({"rows_verbatim": info["rows_5_99_verbatim"], "C_row0_log10": info["C_over_authors_log10_rows0_4"][0]}))
sys.exit(0 if info["rows_5_99_verbatim"] else 9)
