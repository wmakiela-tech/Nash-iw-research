#!/bin/bash
# PREREG_123 runner: native STD_A (base vs std = N_BH x 0.5817518), authors' solver; grid A for j16..j22, j62; replica grid B
# for j18, j20, j22, j62; then analysis_123.py. Fresh dir; pristine author tree (blob b368ba55 checked); two lanes.
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-23/code
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
W=${1:-/home/claude/run123}; O=$W/out
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $W/res
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
[ "$(git -C $SRC/.. rev-parse HEAD:arXiv-2509.05618/main-scan.jl)" = "b368ba55d5a493f7bc185909730f7fe5691f10d6" ] || stop "author blob" 10
git -C $SRC/.. diff --quiet HEAD -- arXiv-2509.05618 || stop "author tree modified" 10
sha256sum $SRC/main-scan.jl $SRC/data/out/hadrons_from_PBH.dat $C/std_a_123.jl $C/analysis_123.py > $O/inputs_sha.log
cp -a $SRC $W/src && cmp -s $SRC/main-scan.jl $W/src/main-scan.jl || stop "copy src" 9
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
run_j() { a=$1; j=$2; g=$3; m=$4; tag=${a}_j${j}_${g}; log "JL_START $tag"
  timeout 3600 $J --startup-file=no --project=$ENV $C/std_a_123.jl $W/src $a def $j $m $W/res/sa_${tag}.csv > $O/jl_$tag.log 2>&1
  rc=$?; echo $rc > $O/jl_$tag.rc; log "JL_END $tag rc=$rc"; }
lane_1() { for j in 22 62 20 18; do for a in base std; do run_j $a $j A coarse; done; done
           for j in 22 62; do for a in base std; do run_j $a $j B coarseB; done; done; }
lane_2() { for j in 16 17 19 21; do for a in base std; do run_j $a $j A coarse; done; done
           for j in 18 20; do for a in base std; do run_j $a $j B coarseB; done; done; }
lane_1 & lane_2 & wait
for f in $O/jl_*.rc; do [ "$(cat $f)" = "0" ] || stop "julia $(basename $f)" 4; done
( cd $W && sha256sum res/* ) > $O/outputs_sha256.log
python3 -I $C/analysis_123.py $W/res $O/analysis123.json > $O/analysis123.stdout 2>&1 || stop "analysis" 8
log "ALL_DONE"
