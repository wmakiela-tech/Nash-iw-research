"""PREREG_085 injection gates (run before the HERWIG grid; the runner stops on FAIL).
Usage: python3 -I check_inj_085.py <data_083_dir> <dump_inj> <dump_x2> <out_json>
V_INJ_NEG: source copy carrying the regenerated PYTHIA table G0 (max rel diff to the authors' table 1.2e-15) reproduces
           the 083 native Y at the 4 nearest-root nodes: |Y_inj - Y_083| / |Y_083 - Y0_083(j)| <= 1e-3.
V_INJ_POS: source copy carrying G0 x 2 changes dY at o22_1720 by >= 20 %: |dY_x2 / dY_083 - 1| >= 0.2
           (proves the copy reads its own table, so V_INJ_NEG is not passing vacuously).
"""
import csv, json, os, sys


def rd(p):
    return {r["run_id"]: r for r in csv.DictReader(l for l in open(p) if not l.startswith("#"))}


d83, dinj, dx2, dst = sys.argv[1:5]
s83 = {}
for arm in ("orig", "e5"):
    s83.update(rd(os.path.join(d83, f"summary_{arm}_083.csv")))
inj = {}
for arm in ("orig", "e5"):
    inj.update(rd(os.path.join(dinj, f"summary_{arm}.csv")))
x2 = rd(os.path.join(dx2, "summary_orig.csv"))
Y0 = {j: float(s83[f"o{j}_base"]["Y"]) for j in (22, 62)}
neg = {}
for rid, r in inj.items():
    ref = s83[rid[1:]]; j = int(r["j"])
    dy = float(ref["Y"]) - Y0[j]
    neg[rid] = {"Y_inj": float(r["Y"]), "Y_083": float(ref["Y"]), "rel_to_dY": abs(float(r["Y"]) - float(ref["Y"])) / abs(dy),
                "bitwise": float(r["Y"]) == float(ref["Y"])}
ok_neg = len(neg) == 4 and all(x["rel_to_dY"] <= 1e-3 for x in neg.values())
dy83 = float(s83["o22_1720"]["Y"]) - Y0[22]; dyx2 = float(x2["xo22_1720"]["Y"]) - Y0[22]
pos = {"dY_083": dy83, "dY_x2": dyx2, "ratio": dyx2 / dy83}
ok_pos = abs(dyx2 / dy83 - 1) >= 0.2
out = {"V_INJ_NEG": {"cases": neg, "pass": ok_neg}, "V_INJ_POS": dict(pos, threshold=0.2, pass_=ok_pos)}
json.dump(out, open(dst, "x"), indent=1)
print(json.dumps({"V_INJ_NEG": ok_neg, "V_INJ_POS": ok_pos, "x2_ratio": pos["ratio"]}))
sys.exit(0 if (ok_neg and ok_pos) else 8)
