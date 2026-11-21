#!/bin/bash
# PREREG_079 runner. MUST NOT be executed before the Moderator authorizes the run (RUNLOG entry).
# Phase 1: native rate dumps (authors' Julia; orig and e5 queues in parallel). Phase 2: NET rate transfer (PRyMordial).
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
W=/home/claude/work079; O=$W/out; DUMP=$W/dump; mkdir -p $O $DUMP
[ -d $W/prym079 ] || python3 -I $C/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || { echo PATCH_FAIL; exit 2; }
run_j() { arm=$1; echo "JL_START $arm $(date '+%d %H:%M:%S')" >> $O/timeline.log
  timeout 7200 $J --startup-file=no --project=$ENV $C/rate_dump_079.jl $SRC $arm $C/cfg079_${arm}.dat $DUMP > $O/jl_${arm}.log 2>&1; rc=$?
  echo $rc > $O/jl_${arm}.rc; echo "JL_END $arm rc=$rc $(date '+%d %H:%M:%S')" >> $O/timeline.log; }
run_j orig & run_j e5 & wait
echo "NET_START $(date '+%d %H:%M:%S')" >> $O/timeline.log
python3 -I $C/run_net_079.py $W/prym079 $DUMP $O > $O/net.log 2>&1; echo $? > $O/net.rc
echo "ALL_DONE jl_orig=$(cat $O/jl_orig.rc) jl_e5=$(cat $O/jl_e5.rc) net=$(cat $O/net.rc) $(date '+%d %H:%M:%S')" >> $O/timeline.log
