#!/bin/bash
# PREREG_092 runner (EKS1 DIR-008 native test): fresh run dir; any rc != 0 or table mismatch stops; no ALL_DONE on failure.
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code
C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
R2=/home/claude/nash-iw-research/research/badacz/2026-11-21/data/hadrons_085_R2.dat
W=${1:-/home/claude/run092}; O=$W/out
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
{ echo "590c7eb6553a0d55801e6dcacec5cc651b82369c7618735b1142bec9902da78c  $R2"
  echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat"; } | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
cp -a $SRC $W/src_h && cp $R2 $W/src_h/data/out/hadrons_from_PBH.dat && cmp -s $R2 $W/src_h/data/out/hadrons_from_PBH.dat || stop "copy src_h" 9
run_j() { tree=$1; cfg=$2; tag=$3; log "JL_START $tag"
  timeout 7200 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $tree orig $C/$cfg $W/dump_$tag > $O/jl_$tag.log 2>&1
  echo $? > $O/jl_$tag.rc; log "JL_END $tag rc=$(cat $O/jl_$tag.rc)"; }
run_j $W/src_h cfg092_her_orig.dat h & run_j $SRC cfg092_py_orig.dat p & wait
for t in h p; do [ "$(cat $O/jl_$t.rc)" = "0" ] || stop "julia $t" 4; done
log "ALL_DONE"
