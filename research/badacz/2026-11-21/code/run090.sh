#!/bin/bash
# PREREG_090 runner (modern PYTHIA 8.3 / Herwig 7.3 BBN multiplicity tables -> Wu-Xu native + network), hard-gated:
# fresh run dir; any rc != 0, table gate, copy check, dedupe or NET failure stops with nonzero exit and NO "ALL_DONE".
# Usage: bash run090.sh [run_dir]
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
BH=/home/claude/bh085/BlackHawk_v2.3; BHT=/home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables
PYV=/home/claude/gen090/venv/bin/python; HW=/home/claude/gen090/mamba/envs/hw/bin/Herwig
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
W=${1:-/home/claude/run090}; O=$W/out; T=$W/tables; M=$W/mc
[ -e $W ] && { echo "REFUSE: $W exists (fresh run required)"; exit 3; }
mkdir -p $O $T $M $W/prim
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
{ echo "dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7  /home/claude/bh085/dl/blackhawk_v2.3.tar.bz2"
  echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat"
  echo "5554b2f66027accc3fe38b55b846d5c7c6d771283868187870bf9c86e5c46678  /home/claude/gen090/dl/CT14lo.tar.gz"
  echo "ad62063067e1d73942b1aadcaff2e50a6b2e2d28ad989e8bd3eee5f48e05f18c  /home/claude/gen090/dl/CT14nlo.tar.gz"; } | sha256sum -c >> $O/inputs_sha.log 2>&1 || stop "input sha" 10
sha256sum $BH/BlackHawk_inst.x $BHT/pythia_tables/*.txt $BHT/herwig_tables/*.txt >> $O/inputs_sha.log
$PYV -c "import importlib.metadata as m; print('pythia8mc', m.version('pythia8mc'))" >> $O/inputs_sha.log 2>&1
$HW --version >> $O/inputs_sha.log 2>&1
MAMBA_ROOT_PREFIX=/home/claude/gen090/mamba /home/claude/gen090/micromamba list -n hw | grep -E "herwig|thepeg|lhapdf|hepmc" >> $O/inputs_sha.log 2>&1
python3 -I $C/mc_spec_090.py $M > $O/mc_spec.txt || stop "mc spec" 9
stream_py() { log "PRIM_START"; timeout 3600 $J --startup-file=no --project=$ENV $C/primary_spectra_090.jl $SRC $BH $W/prim/prim.tsv 0 5 1e5 100 P90 > $O/prim.log 2>&1; echo $? > $O/prim.rc; log "PRIM_END rc=$(cat $O/prim.rc)"
  while read p s spec; do $PYV $C/mult_pythia_090.py $p $M/pythia_$p.json $s $spec > $O/py_$p.log 2>&1 || echo "$p" >> $O/py_failed.txt; done < $O/mc_spec.txt; log "PY_END"; }
stream_hw() { while read p s spec; do python3 -I $C/mult_herwig_090.py $HW $p $M/herwig_$p.json $s $W/hwwork $spec > $O/hw_$p.log 2>&1 || echo "$p" >> $O/hw_failed.txt; done < $O/mc_spec.txt; log "HW_END"; }
log "MC_START"; stream_py & stream_hw & wait
[ "$(cat $O/prim.rc)" = "0" ] || stop "primary spectra rc" 4
[ -e $O/py_failed.txt ] && stop "pythia failed: $(cat $O/py_failed.txt | tr '\n' ' ')" 4
[ -e $O/hw_failed.txt ] && stop "herwig failed: $(cat $O/hw_failed.txt | tr '\n' ' ')" 4
python3 -I $C/make_tables_090.py $BHT $W/prim/prim.tsv $SRC/data/out/hadrons_from_PBH.dat $M $T > $O/tables.log 2>&1 || stop "table gates (see tables/tables090.json)" 7
sha256sum $T/*.dat $M/*.json $W/prim/prim.tsv* > $O/tables_sha256.log
for v in p:P83 h:H73; do n=${v%%:*}; t=${v##*:}
  cp -a $SRC $W/src_$n && cp $T/$t.dat $W/src_$n/data/out/hadrons_from_PBH.dat || stop "copy src_$n" 9
done
python3 -I -c "
import filecmp, json
r = {v: filecmp.cmp('$T/%s.dat' % t, '$W/src_%s/data/out/hadrons_from_PBH.dat' % v, shallow=False) for v, t in (('p', 'P83'), ('h', 'H73'))}
json.dump(dict(r, **{'pass': all(r.values())}), open('$O/v_table.json', 'w'))
import sys; sys.exit(0 if all(r.values()) else 1)" || stop "table not in tree copy" 9
run_j() { v=$1; log "JL_START $v"
  timeout 14400 $J --startup-file=no --project=$ENV $C/rate_dump_081.jl $W/src_$v orig $C/cfg090_${v}_orig.dat $W/dump_$v > $O/jl_$v.log 2>&1
  echo $? > $O/jl_$v.rc; log "JL_END $v rc=$(cat $O/jl_$v.rc)"; }
run_j p & run_j h & wait
for v in p h; do [ "$(cat $O/jl_$v.rc)" = "0" ] || stop "julia $v rc=$(cat $O/jl_$v.rc)" 4; done
for v in p h; do python3 -I $C/dedupe_rates_081.py $W/dump_$v $W/dd_$v >> $O/dedupe.log 2>&1 || stop "dedupe $v" 5; done
python3 -I $C/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_090.py $W/prym079 $W/dd $O $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || stop "net rc=$rc" 6
log "ALL_DONE"
