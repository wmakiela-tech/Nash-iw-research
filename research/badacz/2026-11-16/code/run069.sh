#!/bin/bash
# PREREG_069 (T2) runner; authorized by Moderator 16 XI 2026 16:47. Two queues on 2 cores; explicit per-series status.
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
C=/home/claude/nash-iw-research/research/badacz/2026-11-16/code
O=/home/claude/work069/out
run_s() { arm=$1; tol=$2; s=$(date +%s); echo "START $arm $tol $(date '+%d %H:%M:%S')" >> $O/timeline.txt
  timeout 5400 $J --startup-file=no --project=$ENV $C/b1_t2_contour_069.jl $SRC $arm $tol $C/cfg069_${arm}_${tol}.dat $O/t2_${arm}_${tol}.csv > $O/t2_${arm}_${tol}.log 2>&1; rc=$?
  echo $rc > $O/t2_${arm}_${tol}.status; echo "END $arm $tol rc=$rc $(date '+%d %H:%M:%S') wall=$(( $(date +%s)-s ))s" >> $O/timeline.txt; }
( run_s orig default; run_s orig 1e-4 ) &
( run_s e5 default; run_s e5 1e-4 ) &
wait
n_ok=$(cat $O/t2_*.status | grep -cx 0); echo "ALL_DONE ok=$n_ok/4 $(date '+%d %H:%M:%S')" >> $O/timeline.txt
[ "$n_ok" -eq 4 ]
