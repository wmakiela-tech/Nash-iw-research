"""PREREG_090: frozen MC request (energies per primary, events per energy). Writes requested.json and prints
'<primary> <seed> <E1:N1,...>' lines for the runner.  Usage: python3 -I mc_spec_090.py <out_dir>"""
import json, os, sys
EN = [25, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 100000]
NEV = lambda E: 2000 if E <= 800 else (1000 if E <= 6400 else 500)
START = {"Wpm": 100, "Z0": 100, "top": 200, "gluon": 100, "higgs": 100, "tau": 100}  # H-mediated PYTHIA processes need sqrt(s) >= 200 GeV with PDF:lepton off
PRIM = ["gluon", "higgs", "Wpm", "Z0", "tau", "up", "down", "strange", "charm", "bottom", "top"]
req = {}; lines = []
for k, p in enumerate(PRIM):
    Es = [E for E in EN if E >= START.get(p, 25)]
    req[p] = {f"{E:g}": NEV(E) for E in Es}
    lines.append(f"{p} {90001 + k} " + ",".join(f"{E}:{NEV(E)}" for E in Es))
json.dump(req, open(os.path.join(sys.argv[1], "requested.json"), "x"), indent=1)
print("\n".join(lines))
