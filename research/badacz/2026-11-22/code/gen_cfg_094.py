"""PREREG_094: generate native run configs for the replica/jitter threshold-transfer test.
Usage: python3 -I gen_cfg_094.py <analysis090.json (2026-11-21/data)> <out_dir>
Window: every node of the frozen 090 grid (0.05 dex) within +-0.15 dex of any of the 4 nominal 090 roots
({code, net} x {0.251, 0.2484}) of that generator and mass; plus the base node (log10 beta = -30).
Arms: a = P83_R1, b = H73_R1, c = P83_R2, d = H73_R2, e = P83_J, f = H73_J (nominal x 1.001); k = driver control
(nominal P83, node j22 -17.20, must reproduce 090 p22_1720 bitwise)."""
import json, os, sys

A = json.load(open(sys.argv[1])); out = sys.argv[2]
ARMS = {"a": "P83", "b": "H73", "c": "P83", "d": "H73", "e": "P83", "f": "H73"}
W = 0.15
for arm, g in ARMS.items():
    lines = [f"# PREREG_094 arm {arm} ({g}): run_id j log10beta; window +-{W} dex around the 4 nominal 090 roots"]
    for j in (22, 62):
        lbs = A["series"][f"{g}_{j}"]["lb"]
        roots = [A["roots"][f"{g}_{j}|{m}|{t}"]["lb"] for m in ("code", "net") for t in ("0.251", "0.2484")]
        nodes = sorted({x for x in lbs for r in roots if abs(x - r) <= W + 1e-9})
        lines.append(f"{arm}{j}_base {j} -30")
        lines += [f"{arm}{j}_{int(round(-x * 100))} {j} {x:.2f}" for x in nodes]
    open(os.path.join(out, f"cfg094_{arm}.dat"), "x").write("\n".join(lines) + "\n")
open(os.path.join(out, "cfg094_k.dat"), "x").write("# PREREG_094 driver control: nominal P83 table, same node as 090 p22_1720\nk22_1720 22 -17.20\n")
print("CFG094", {a: sum(1 for l in open(os.path.join(out, f"cfg094_{a}.dat")) if l.strip() and not l.startswith("#")) for a in list(ARMS) + ["k"]})
