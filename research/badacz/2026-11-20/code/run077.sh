#!/bin/bash
# PREREG_077 runner. MUST NOT be executed before the Moderator authorizes the run (RUNLOG entry).
# Phase 1: NET arm (PRyMordial, patched copy, 2 workers). Phase 2: CODE arm (authors' Julia, 2 tol queues).
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-20/code
W=/home/claude/work077; O=$W/out; mkdir -p $O
[ -d $W/prym077 ] || python3 -I $C/prym_kick_patch_077.py $PRYM_SRC $W/prym077 > $O/patch.log 2>&1 || { echo PATCH_FAIL; exit 2; }
echo "NET_START $(date '+%d %H:%M:%S')" >> $O/timeline.txt
python3 -I $C/run_net_077.py $W/prym077 $O > $O/net.log 2>&1; echo $? > $O/net.rc
echo "NET_END rc=$(cat $O/net.rc) $(date '+%d %H:%M:%S')" >> $O/timeline.txt
run_c() { tol=$1; echo "CODE_START $tol $(date '+%d %H:%M:%S')" >> $O/timeline.txt
  timeout 5400 $J --startup-file=no --project=$ENV $C/code_gain_077.jl $SRC $tol $C/cfg077_code_${tol}.dat $O/code_${tol}.csv > $O/code_${tol}.log 2>&1; rc=$?
  echo $rc > $O/code_${tol}.rc; echo "CODE_END $tol rc=$rc $(date '+%d %H:%M:%S')" >> $O/timeline.txt; }
run_c default & run_c 1e-4 & wait
echo "ALL_DONE net=$(cat $O/net.rc) code_default=$(cat $O/code_default.rc) code_1e-4=$(cat $O/code_1e-4.rc) $(date '+%d %H:%M:%S')" >> $O/timeline.txt
