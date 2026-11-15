#!/bin/bash
# PREREG_066 runner (authorized by Moderator 16 XI 2026 00:10). Two queues on 2 cores; explicit per-arm exit status.
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
DRV=/home/claude/nash-iw-research/research/badacz/2026-11-15/code/b1_calibration_066.jl
O=/home/claude/work066/out
run_arm() { a=$1; t=$2; s=$(date +%s); echo "START $a $(date '+%d %H:%M:%S')" >> $O/timeline.txt
  timeout $t $J --startup-file=no --project=$ENV $DRV $SRC $a $O/arm_$a.jsonl > $O/arm_$a.log 2>&1; rc=$?
  echo $rc > $O/arm_$a.status; echo "END $a rc=$rc $(date '+%d %H:%M:%S') wall=$(( $(date +%s)-s ))s" >> $O/timeline.txt; }
( run_arm archive 7200; run_arm A3 7200 ) &
( for a in A0u A0 A1 A2 rep013; do run_arm $a 3600; done; run_arm A4 1800 ) &
wait
n_ok=$(cat $O/arm_*.status | grep -cx 0); echo "ALL_DONE ok=$n_ok/8 $(date '+%d %H:%M:%S')" >> $O/timeline.txt
[ "$n_ok" -eq 8 ]
