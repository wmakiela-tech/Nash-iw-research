#!/bin/bash
# PREREG_125 runner (STOP A control for STD_A): tables with prepended sub-1e9 g continuation (s = -1.0, -1.3, -1.5);
# arms base/std x masses j22, j62, j20, authors' solver, grid A (std_a_123.jl unchanged); code-slope reference = run123.
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-23/code; D123=/home/claude/nash-iw-research/research/badacz/2026-11-23/data/run123
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618; PY=/home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables/pythia_tables
W=${1:-/home/claude/run125}; O=$W/out
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $W/res
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
[ "$(git -C $SRC/.. rev-parse HEAD:arXiv-2509.05618/main-scan.jl)" = "b368ba55d5a493f7bc185909730f7fe5691f10d6" ] || stop "author blob" 10
git -C $SRC/.. diff --quiet HEAD -- arXiv-2509.05618 || stop "author tree modified" 10
python3 -I $C/build_tables_125.py $SRC/data/out/hadrons_from_PBH.dat $PY $W/tables > $O/build125.stdout 2>&1 || stop "tables" 7
sha256sum $SRC/main-scan.jl $SRC/data/out/hadrons_from_PBH.dat $C/std_a_123.jl $C/build_tables_125.py $C/analysis_125.py $W/tables/* > $O/inputs_sha.log
for s in m10 m13 m15; do
  cp -a $SRC $W/src_$s && cp $W/tables/hadrons_from_PBH_$s.dat $W/src_$s/data/out/hadrons_from_PBH.dat
  cmp -s $SRC/main-scan.jl $W/src_$s/main-scan.jl || stop "copy src $s" 9
  [ "$(diff -rq $SRC $W/src_$s | wc -l)" = "1" ] || stop "src_$s differs beyond the table" 9
done
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
run_j() { a=$1; j=$2; s=$3; tag=${a}_j${j}_${s}; log "JL_START $tag"
  timeout 3600 $J --startup-file=no --project=$ENV $C/std_a_123.jl $W/src_$s $a def $j coarse $W/res/sa_${tag}.csv > $O/jl_$tag.log 2>&1
  rc=$?; echo $rc > $O/jl_$tag.rc; log "JL_END $tag rc=$rc"; }
lane_1() { for s in m10 m13 m15; do for a in base std; do run_j $a 22 $s; done; done; for a in base std; do run_j $a 20 m10; done; run_j std 20 m13; }
lane_2() { for s in m10 m13 m15; do for a in base std; do run_j $a 62 $s; done; done; run_j base 20 m13; for a in base std; do run_j $a 20 m15; done; }
lane_1 & lane_2 & wait
for f in $O/jl_*.rc; do [ "$(cat $f)" = "0" ] || stop "julia $(basename $f)" 4; done
( cd $W && sha256sum res/* ) > $O/outputs_sha256.log
python3 -I $C/analysis_125.py $W/res $D123/analysis123_strict.json $W/tables/tables125.json $O/analysis125.json > $O/analysis125.stdout 2>&1 || stop "analysis" 8
log "ALL_DONE"
