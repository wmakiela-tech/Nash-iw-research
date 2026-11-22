#!/bin/bash
# PREREG_107 runner: SCOPE12 ROT010 / AUD3 ROT015 six-probe design at j22 (+-0.001 dex brackets around the 083 linear roots
# at Y* = 0.25027090177105143: CODE_orig, NET_orig with arm orig; NET_e5 with arm e5) + driver control o22_1730 (083).
# Authors' source tree used directly (as 083). Hard-gated; fresh dir.  Usage: bash run107.sh [run_dir]
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code
C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
W=${1:-/home/claude/run107}; O=$W/out
[ -e $W ] && { echo "REFUSE: $W exists"; exit 3; }
mkdir -p $O
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat" | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
run_j() { arm=$1; x=$2; log "JL_START $arm"
  timeout 7200 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $SRC $arm $C/cfg107_$arm.dat $W/dump_$x > $O/jl_$arm.log 2>&1
  echo $? > $O/jl_$arm.rc; log "JL_END $arm rc=$(cat $O/jl_$arm.rc)"; }
run_j orig o & run_j e5 e & wait
for a in orig e5; do [ "$(cat $O/jl_$a.rc)" = "0" ] || stop "julia $a rc=$(cat $O/jl_$a.rc)" 4; done
for x in o e; do python3 -I $C81/dedupe_rates_081.py $W/dump_$x $W/dd_$x >> $O/dedupe.log 2>&1 || stop "dedupe $x" 5; done
python3 -I $C81/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_107.py $W/prym079 $W $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || stop "net rc=$rc" 6
log "ALL_DONE"
