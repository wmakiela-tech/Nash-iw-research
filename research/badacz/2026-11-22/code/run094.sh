#!/bin/bash
# PREREG_094 runner (MC replica + solver-jitter threshold transfer, modern P83/H73 tables), hard-gated:
# fresh run dir; any input SHA mismatch, table copy mismatch, Julia rc != 0, dedupe or NET failure stops; no ALL_DONE on failure.
# Usage: bash run094.sh [run_dir]
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code
C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D90=/home/claude/nash-iw-research/research/badacz/2026-11-21/data
W=${1:-/home/claude/run094}; O=$W/out; T=$W/tables
[ -e $W ] && { echo "REFUSE: $W exists (fresh run required)"; exit 3; }
mkdir -p $O $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
{ echo "67dad44eeb44004a916f7fa5cfda33f4660c7424524893e5e9c4f715d49d5289  $D90/hadrons_090_P83.dat"
  echo "5e5334ca7c8efdf4ebde8c72583f94f6257355d2d16326b52cfb79a7d6a8ec66  $D90/hadrons_090_H73.dat"
  echo "afb4dddcd3c78088ed21afd5b7609b6f10d8bfcc17fa46e9fd95990b0e4386a1  $D90/hadrons_090r1_P83.dat"
  echo "041b0bb6d09dd3f606f7ac167eb0a718c1e158060c90f775d2548d61cd3bf18b  $D90/hadrons_090r1_H73.dat"
  echo "536d0546259dcb158d6e1dafbdf10299eb3fc2f99b5c4f9f438242bedcc3f499  $D90/hadrons_090r2_P83.dat"
  echo "5708993c33ec81a0c878d58477243f49c08d35d267f25065127c267c991f1e68  $D90/hadrons_090r2_H73.dat"
  echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat"; } | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
cp $D90/hadrons_090r1_P83.dat $T/a.dat; cp $D90/hadrons_090r1_H73.dat $T/b.dat
cp $D90/hadrons_090r2_P83.dat $T/c.dat; cp $D90/hadrons_090r2_H73.dat $T/d.dat
python3 -I $C81/table_scale_085.py $D90/hadrons_090_P83.dat 1.001 $T/e.dat > $O/scale.log 2>&1 || stop "scale e" 9
python3 -I $C81/table_scale_085.py $D90/hadrons_090_H73.dat 1.001 $T/f.dat >> $O/scale.log 2>&1 || stop "scale f" 9
cp $D90/hadrons_090_P83.dat $T/k.dat
for x in a b c d e f k; do
  cp -a $SRC $W/src_$x && cp $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat && cmp -s $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat || stop "copy src_$x" 9
done
sha256sum $T/*.dat > $O/tables_sha256.log
run_j() { x=$1; log "JL_START $x"
  timeout 14400 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $W/src_$x orig $C/cfg094_$x.dat $W/dump_$x > $O/jl_$x.log 2>&1
  echo $? > $O/jl_$x.rc; log "JL_END $x rc=$(cat $O/jl_$x.rc)"; }
side_p() { for x in k a c e; do run_j $x; done; }
side_h() { for x in b d f; do run_j $x; done; }
side_p & side_h & wait
for x in k a b c d e f; do [ "$(cat $O/jl_$x.rc)" = "0" ] || stop "julia $x rc=$(cat $O/jl_$x.rc)" 4; done
for x in k a b c d e f; do python3 -I $C81/dedupe_rates_081.py $W/dump_$x $W/dd_$x >> $O/dedupe.log 2>&1 || stop "dedupe $x" 5; done
python3 -I $C81/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_094.py $W/prym079 $W $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || stop "net rc=$rc" 6
log "ALL_DONE"
