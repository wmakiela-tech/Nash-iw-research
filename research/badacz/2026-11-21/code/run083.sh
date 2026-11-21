#!/bin/bash
# PREREG_083 runner, hard-gated (REC13 ROT007 / Mech-S10 ROT007): fresh work dir required; any Julia rc!=0, missing
# summary rows, dedupe failure or NET failure stops the pipeline with a nonzero exit and NO "ALL_DONE".
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
W=/home/claude/work083; O=$W/out; DUMP=$W/dump
[ -e $W ] && { echo "REFUSE: $W exists (fresh run required)"; exit 3; }
mkdir -p $O $DUMP
python3 -I $C/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || { echo PATCH_FAIL | tee -a $O/timeline.log; exit 2; }
run_j() { arm=$1; echo "JL_START $arm $(date '+%d %H:%M:%S')" >> $O/timeline.log
  timeout 14400 $J --startup-file=no --project=$ENV $C/rate_dump_081.jl $SRC $arm $C/cfg083_${arm}.dat $DUMP > $O/jl_${arm}.log 2>&1
  echo $? > $O/jl_${arm}.rc; echo "JL_END $arm rc=$(cat $O/jl_${arm}.rc) $(date '+%d %H:%M:%S')" >> $O/timeline.log; }
run_j orig & run_j e5 & wait
for a in orig e5; do [ "$(cat $O/jl_$a.rc)" = "0" ] || { echo "STOP: julia $a rc=$(cat $O/jl_$a.rc)" | tee -a $O/timeline.log; exit 4; }; done
python3 -I $C/dedupe_rates_081.py $DUMP $W/dump_dedup > $O/dedupe.log 2>&1 || { echo "STOP: dedupe" | tee -a $O/timeline.log; exit 5; }
echo "NET_START $(date '+%d %H:%M:%S')" >> $O/timeline.log
python3 -I $C/run_net_083.py $W/prym079 $W/dump_dedup $O $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || { echo "STOP: net rc=$rc" | tee -a $O/timeline.log; exit 6; }
echo "ALL_DONE $(date '+%d %H:%M:%S')" >> $O/timeline.log
