#!/bin/bash
# PREREG_070 (Q-A) runner; authorized by Moderator 16 XI 2026 17:39. Grid A and grid B in parallel; explicit status.
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
C=/home/claude/nash-iw-research/research/badacz/2026-11-16/code
O=/home/claude/work070/out
run_g() { g=$1; cfg=$2; s=$(date +%s); echo "START $g $(date '+%d %H:%M:%S')" >> $O/timeline.txt
  timeout 5400 $J --startup-file=no --project=$ENV $C/b1_t2_contour_069.jl $SRC orig default $C/$cfg $O/qa_$g.csv > $O/qa_$g.log 2>&1; rc=$?
  echo $rc > $O/qa_$g.status; echo "END $g rc=$rc $(date '+%d %H:%M:%S') wall=$(( $(date +%s)-s ))s" >> $O/timeline.txt; }
run_g A cfg070_A_indomain.dat &
run_g B cfg070_B_offscan.dat &
wait
n_ok=$(cat $O/qa_*.status | grep -cx 0); echo "ALL_DONE ok=$n_ok/2 $(date '+%d %H:%M:%S')" >> $O/timeline.txt
[ "$n_ok" -eq 2 ]
