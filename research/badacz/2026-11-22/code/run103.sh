#!/bin/bash
# PREREG_103 runner (EKS1-DIR-010, one predeclared native switch): Wu-Xu native code-model with the authors' hadron table
# scaled by 1e-12 (hadronic n<->p injection off, PBH background/evaporation kept), j22 and j62, log10 beta -20..-13 step 0.25,
# plus driver control k (authors' table, node 22 -17.20, must equal 083 o22_1720 bitwise). Code model only (the NET arm
# transfers hadronic rates only and is uninformative here). Hard-gated; fresh dir.  Usage: bash run103.sh [run_dir]
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code
C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
W=${1:-/home/claude/run103}; O=$W/out; T=$W/tables
[ -e $W ] && { echo "REFUSE: $W exists"; exit 3; }
mkdir -p $O $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat" | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
python3 -I $C81/table_scale_085.py $SRC/data/out/hadrons_from_PBH.dat 1e-12 $T/z.dat > $O/tables.log 2>&1 || stop "scale" 9
cp $SRC/data/out/hadrons_from_PBH.dat $T/k.dat
for x in k z; do
  cp -a $SRC $W/src_$x && cp $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat && cmp -s $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat || stop "copy src_$x" 9
done
sha256sum $T/*.dat > $O/tables_sha256.log
awk 'NR==1 || /^#/ || /^z22/' $C/cfg103_z.dat > $W/cfg_z22.dat; awk 'NR==1 || /^#/ || /^z62/' $C/cfg103_z.dat > $W/cfg_z62.dat
run_j() { x=$1; cfg=$2; out=$3; log "JL_START $out"
  timeout 14400 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $W/src_$x orig $cfg $W/$out > $O/jl_$out.log 2>&1
  echo $? > $O/jl_$out.rc; log "JL_END $out rc=$(cat $O/jl_$out.rc)"; }
side_1() { run_j k $C/cfg103_k.dat dump_k; run_j z $W/cfg_z22.dat dump_z22; }
side_2() { run_j z $W/cfg_z62.dat dump_z62; }
side_1 & side_2 & wait
for x in dump_k dump_z22 dump_z62; do [ "$(cat $O/jl_$x.rc)" = "0" ] || stop "julia $x rc=$(cat $O/jl_$x.rc)" 4; done
log "ALL_DONE"
