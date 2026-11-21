#!/bin/bash
# PREREG_088 (E4) runner, hard-gated: fresh run dir; any rc != 0, table check, dedupe or NET failure stops with nonzero
# exit and NO "ALL_DONE".  Usage: bash run088.sh [run_dir]
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D=/home/claude/nash-iw-research/research/badacz/2026-11-21/data
W=${1:-/home/claude/run088}; O=$W/out; T=$W/tables
[ -e $W ] && { echo "REFUSE: $W exists (fresh run required)"; exit 3; }
mkdir -p $O $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "5f36d45b85fe3ba5815ea4c322169a7583e52f2c7d9b1c56c52bdaef99b0b3f6  $D/hadrons_087_PY_rows_1e8_1e9.dat" | sha256sum -c >> $O/inputs_sha.log 2>&1 || stop "rows sha" 10
echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat" | sha256sum -c >> $O/inputs_sha.log 2>&1 || stop "authors table sha" 10
python3 -I $C/build_tables_088.py $SRC/data/out/hadrons_from_PBH.dat $D/hadrons_087_PY_rows_1e8_1e9.dat $T/A.dat $T/C.dat $O/tables088.json > $O/tables.log 2>&1 || stop "table build/check" 9
sha256sum $T/*.dat > $O/tables_sha256.log
for v in a:A c:C; do n=${v%%:*}; t=${v##*:}
  cp -a $SRC $W/src_$n && cp $T/$t.dat $W/src_$n/data/out/hadrons_from_PBH.dat || stop "copy src_$n" 9
  cmp -s $T/$t.dat $W/src_$n/data/out/hadrons_from_PBH.dat || stop "table not in src_$n" 9
done
run_j() { v=$1; log "JL_START $v"
  timeout 14400 $J --startup-file=no --project=$ENV $C/rate_dump_081.jl $W/src_$v orig $C/cfg088_${v}_orig.dat $W/dump_$v > $O/jl_$v.log 2>&1
  echo $? > $O/jl_$v.rc; log "JL_END $v rc=$(cat $O/jl_$v.rc)"; }
run_j a & run_j c & wait
for v in a c; do [ "$(cat $O/jl_$v.rc)" = "0" ] || stop "julia $v rc=$(cat $O/jl_$v.rc)" 4; done
for v in a c; do python3 -I $C/dedupe_rates_081.py $W/dump_$v $W/dd_$v >> $O/dedupe.log 2>&1 || stop "dedupe $v" 5; done
python3 -I $C/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_088.py $W/prym079 $W/dd $O $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || stop "net rc=$rc" 6
log "ALL_DONE"
