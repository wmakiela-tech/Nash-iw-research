"""PREREG_085: frozen native configs for the HERWIG (rule R2) cells and the injection control.

Usage: python3 -I gen_cfg_085.py <grid083.json> <outdir>
HER grid per (mass j in {22, 62}, arm): multiples of 0.05 dex from floor((r - 1.50)/0.05) to ceil((r + 0.70)/0.05),
r = PREREG_083 T2 code root (M_D) of the PYTHIA cell (grid083.json). Run ids h<a><j>_<|lb|*100>; bases h o<j>_base at
log10 beta = -30 (orig arm only, as in 083).
Injection control (V_INJ): the 083 nearest-root node of each of the 4 PYTHIA cells, run on the source copy that carries
the regenerated PYTHIA table G0; ids i<a><j>_<...>.
"""
import json, math, os, sys

MASSES = [22, 62]
g = json.load(open(sys.argv[1])); out = sys.argv[2]
v = {}
for arm, a in (("orig", "o"), ("e5", "e")):
    lines = [f"# PREREG_085 HER arm={arm}: run_id j log10beta; grid 0.05 dex from floor((r-1.50)/0.05) to ceil((r+0.70)/0.05); r = 083 T2 M_D root (PYTHIA)"]
    inj = [f"# PREREG_085 injection control arm={arm}: 083 nearest-root nodes on the G0-table source copy"]
    if arm == "orig":
        lines += [f"ho{j}_base {j} -30" for j in MASSES]
    for j in MASSES:
        r = g[f"{arm}_{j}"]["root_M_D"]
        k0 = math.floor(round((r - 1.50) / 0.05, 9)); k1 = math.ceil(round((r + 0.70) / 0.05, 9))
        for k in range(k0, k1 + 1):
            lb = round(k * 0.05, 2)
            lines.append(f"h{a}{j}_{abs(int(round(lb * 100))):04d} {j} {lb:.2f}")
        node = g[f"{arm}_{j}"]["nearest_root_node"]
        lb_node = -int(node.split("_")[1]) / 100.0
        inj.append(f"i{node} {j} {lb_node:.2f}")
        v[f"{arm}_{j}"] = {"root_M_D_PY": r, "n_nodes": k1 - k0 + 1, "lb_min": round(k0 * 0.05, 2), "lb_max": round(k1 * 0.05, 2),
                           "inj_node": "i" + node, "py_node_083": node}
    open(os.path.join(out, f"cfg085_her_{arm}.dat"), "w").write("\n".join(lines) + "\n")
    open(os.path.join(out, f"cfg085_inj_{arm}.dat"), "w").write("\n".join(inj) + "\n")
open(os.path.join(out, "cfg085_x2_orig.dat"), "w").write(
    "# PREREG_085 positive injection control: G0 table with all five yield columns x2, orig arm, 083 node o22_1720\nxo22_1720 22 -17.20\n")
v["V45_cases"] = ["ho22_1720", "ho62_1940"]
v["x2_case"] = "xo22_1720"
json.dump(v, open(os.path.join(out, "grid085.json"), "w"), indent=1)
print(json.dumps(v))
