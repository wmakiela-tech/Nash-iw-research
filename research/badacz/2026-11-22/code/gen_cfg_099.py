"""PREREG_099: native configs. Usage: python3 -I gen_cfg_099.py <analysis090.json> <out_dir>
Arms l (table L, control of R2), s (Sa, sqrt(s) fix), b (Sb, other extrapolation above 5e4), u (Ua, sqrt(s) fix + PY
binning convention); nodes on the 0.05-dex
grid inside the union over the 4 cells (code/net x 0.251/0.2484) of [root_H73 - 0.15, root_HERBH + 0.15] (090 roots),
plus the base node; k = driver control (R2 table, node 22 -17.20 = 085 ho22_1720)."""
import json, os, sys
A = json.load(open(sys.argv[1])); out = sys.argv[2]
grid = [round(-21 + 0.05 * i, 2) for i in range(int(5 / 0.05) + 1)]
for arm in "lsub":
    L = [f"# PREREG_099 arm {arm}: run_id j log10beta; union over cells of [root_H73-0.15, root_HERBH+0.15]"]
    for j in (22, 62):
        iv = [(A["roots"][f"H73_{j}|{m}|{t}"]["lb"] - 0.15, A["roots"][f"HERBH_{j}|{m}|{t}"]["lb"] + 0.15) for m in ("code", "net") for t in ("0.251", "0.2484")]
        nodes = sorted({x for x in grid for a, b in iv if a - 1e-9 <= x <= b + 1e-9})
        L.append(f"{arm}{j}_base {j} -30")
        L += [f"{arm}{j}_{int(round(-x * 100))} {j} {x:.2f}" for x in nodes]
    open(os.path.join(out, f"cfg099_{arm}.dat"), "x").write("\n".join(L) + "\n")
open(os.path.join(out, "cfg099_k.dat"), "x").write("# PREREG_099 driver control: R2 table, node of 085 ho22_1720\nk22_1720 22 -17.20\n")
print({a: sum(1 for l in open(os.path.join(out, f"cfg099_{a}.dat")) if l.strip() and not l.startswith("#")) for a in "lsubk"})
