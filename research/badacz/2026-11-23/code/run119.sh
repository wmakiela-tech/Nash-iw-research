#!/bin/bash
# PREREG_119 runner: native no-PBH background export (arms code/ad x solver def/r8/r9 x start j22/j62, beta = 0) and
# f_code(M) on the BlackHawk fM.txt mass grid; then analysis_119.py (G_EC+(a), predictions frozen in PREREG_119).
# Hard-gated; fresh dir; two parallel lanes (2 CPUs).
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-23/code; D90=/home/claude/nash-iw-research/research/badacz/2026-11-21/data
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618; K115=/home/claude/keep115
FM=/home/claude/bh085/src/blackhawk_v2.3/src/tables/fM_tables/fM.txt
W=${1:-/home/claude/run119}; O=$W/out
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "b368ba55d5a493f7bc185909730f7fe5691f10d6  main-scan.jl" > $O/expected_blob.txt
[ "$(git -C $SRC/.. rev-parse HEAD:arXiv-2509.05618/main-scan.jl)" = "b368ba55d5a493f7bc185909730f7fe5691f10d6" ] || stop "author blob" 10
git -C $SRC/.. diff --quiet HEAD -- arXiv-2509.05618 || stop "author tree modified" 10
sha256sum $SRC/main-scan.jl $SRC/tool_script-parameters.jl $SRC/tool_script-N_relativistic_species.jl $FM $D90/primary_spectra_090.tsv.gz $K115/*.csv $C/bg_export_119.jl $C/analysis_119.py > $O/inputs_sha.log
cp -a $SRC $W/src && cmp -s $SRC/main-scan.jl $W/src/main-scan.jl || stop "copy src" 9
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
run_j() { tag=$1; shift; log "JL_START $tag"
  timeout 7200 $J --startup-file=no --project=$ENV $C/bg_export_119.jl $W/src "$@" $W/exp > $O/jl_$tag.log 2>&1
  rc=$?; echo $rc > $O/jl_$tag.rc; log "JL_END $tag rc=$rc"; }
lane_1() { for a in code ad; do for s in def r8 r9; do run_j ${a}_${s}_j22 $a $s 22; done; done; }
lane_2() { run_j fcode fcode $FM; mv $W/exp/fcode_119.csv $W/fcode_119.csv 2>/dev/null
           for a in code ad; do for s in def r8 r9; do run_j ${a}_${s}_j62 $a $s 62; done; done; }
mkdir -p $W/exp; lane_1 & lane_2 & wait
for f in $O/jl_*.rc; do [ "$(cat $f)" = "0" ] || stop "julia $(basename $f)" 4; done
[ -s $W/fcode_119.csv ] || stop "fcode" 4
( cd $W && sha256sum exp/* fcode_119.csv ) > $O/outputs_sha256.log
python3 -I $C/analysis_119.py $W/exp $W/fcode_119.csv $FM $D90/primary_spectra_090.tsv.gz $K115/rates_w22_1740.csv \
  $K115/rates_w62_1940.csv $O/analysis119.json > $O/analysis119.stdout 2>&1 || stop "analysis" 8
log "ALL_DONE"
