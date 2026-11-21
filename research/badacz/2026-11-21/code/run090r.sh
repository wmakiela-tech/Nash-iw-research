#!/bin/bash
# PREREG_090 r2 (post-run robustness, AUD3 ROT006 F1/F2): two independent MC replicates with a DISTINCT seed per
# (primary, energy) = base + 100*k + i (base 91000 / 92000), one energy per generator call; eventwise energy residual.
# Physics, energies and event counts identical to mc_spec_090.py. Folding with the frozen make_tables_090.py.
# Usage: bash run090r.sh <replicate_base> <out_dir>
set -u
PYV=/home/claude/gen090/venv/bin/python; HW=/home/claude/gen090/mamba/envs/hw/bin/Herwig
C=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
BASE=$1; W=$2; [ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $W/mc $W/parts $W/log
python3 -I $C/mc_spec_090.py $W/mc > $W/log/spec.txt
gen() { g=$1; k=0
  while read p s spec; do i=0
    for es in $(echo $spec | tr ',' ' '); do seed=$((BASE + 100*k + i))
      if [ $g = pythia ]; then $PYV $C/mult_pythia_090r.py $p $W/parts/${g}_${p}_$i.json $seed $es > /dev/null 2>&1 || echo "$g $p $es" >> $W/log/failed.txt
      else python3 -I $C/mult_herwig_090r.py $HW $p $W/parts/${g}_${p}_$i.json $seed $W/hwwork $es > /dev/null 2>&1 || echo "$g $p $es" >> $W/log/failed.txt; fi
      i=$((i+1)); done; k=$((k+1)); done < $W/log/spec.txt; }
gen pythia & gen herwig & wait
[ -e $W/log/failed.txt ] && { echo "FAILED"; cat $W/log/failed.txt; exit 4; }
python3 -I - <<PY
import json, glob, os
W = "$W"
for g in ("pythia", "herwig"):
    for p in json.load(open(os.path.join(W, "mc", "requested.json"))):
        parts = sorted(glob.glob(os.path.join(W, "parts", f"{g}_{p}_*.json")), key=lambda f: int(f.rsplit("_", 1)[1][:-5]))
        en = [json.load(open(f))["energies"][0] for f in parts]
        json.dump({"generator": g, "primary": p, "energies": en}, open(os.path.join(W, "mc", f"{g}_{p}.json"), "x"), indent=1)
PY
echo REPLICATE_DONE
