"""PREREG_083: generate frozen native configs from T2 code roots (analysis069.json, M_D).
Grid per (mass, arm): multiples of 0.05 dex from floor((root-1.20)/0.05)*0.05 to ceil((root+0.10)/0.05)*0.05.
Usage: python3 -I gen_cfg_083.py <analysis069.json> <outdir>"""
import json, math, os, sys
A = json.load(open(sys.argv[1])); out = sys.argv[2]
MASSES = [22, 38, 62, 90]
v = {}
for arm, key, a in (("orig", "orig_default", "o"), ("e5", "e5_default", "e")):
    lines = [f"# PREREG_083 arm={arm}: run_id j log10beta; grid 0.05 dex from floor((root-1.20)/0.05) to ceil((root+0.10)/0.05); root = T2 M_D"]
    if arm == "orig":
        lines += [f"o{j}_base {j} -30" for j in MASSES]
    for j in MASSES:
        r = A["roots"][key][str(j)]["M_D"]
        k0 = math.floor(round((r - 1.20) / 0.05, 9)); k1 = math.ceil(round((r + 0.10) / 0.05, 9))
        best = None
        for k in range(k0, k1 + 1):
            lb = round(k * 0.05, 2)
            rid = f"{a}{j}_{abs(int(round(lb*100))):04d}"
            lines.append(f"{rid} {j} {lb:.2f}")
            if best is None or abs(lb - r) < abs(best[1] - r):
                best = (rid, lb)
        v[f"{arm}_{j}"] = {"root_M_D": r, "n_nodes": k1 - k0 + 1, "nearest_root_node": best[0]}
    open(os.path.join(out, f"cfg083_{arm}.dat"), "w").write("\n".join(lines) + "\n")
json.dump(v, open(os.path.join(out, "grid083.json"), "w"), indent=1)
print(json.dumps(v))
