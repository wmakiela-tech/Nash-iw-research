#!/bin/bash
# PREREG_099 runner: native Wu-Xu + PRyMordial for tables L (control), Sa and Sb (sqrt(s) fix, two extrapolations above 5e4 GeV),
# Ua (sqrt(s) + binning fix) and the
# driver control k (R2 table). Hard-gated; fresh dir; no ALL_DONE on failure.  Usage: bash run099.sh [run_dir]
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
HT=/home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code
C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D90=/home/claude/nash-iw-research/research/badacz/2026-11-21/data
W=${1:-/home/claude/run099}; O=$W/out; T=$W/tables
[ -e $W ] && { echo "REFUSE: $W exists"; exit 3; }
mkdir -p $O $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
{ echo "590c7eb6553a0d55801e6dcacec5cc651b82369c7618735b1142bec9902da78c  $D90/hadrons_085_R2.dat"
  echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat"; } | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
sha256sum $HT/herwig_tables/*.txt $HT/pythia_tables/*.txt $D90/primary_spectra_090.tsv.gz $D90/mc090/herwig_*.json >> $O/inputs_sha.log
zcat $D90/primary_spectra_090.tsv.gz > $W/prim.tsv || stop "prim" 9
python3 -I $C/build_tables_099.py $HT $W/prim.tsv $D90/mc090 $D90/hadrons_085_R2.dat $T > $O/tables.log 2>&1 || stop "table gates (tables099.json)" 7
cp $D90/hadrons_085_R2.dat $T/k.dat; cp $T/L.dat $T/l.dat; cp $T/Sa.dat $T/s.dat; cp $T/Ua.dat $T/u.dat; cp $T/Sb.dat $T/b.dat
for x in k l s u b; do
  cp -a $SRC $W/src_$x && cp $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat && cmp -s $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat || stop "copy src_$x" 9
done
sha256sum $T/*.dat > $O/tables_sha256.log
run_j() { x=$1; log "JL_START $x"
  timeout 14400 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $W/src_$x orig $C/cfg099_$x.dat $W/dump_$x > $O/jl_$x.log 2>&1
  echo $? > $O/jl_$x.rc; log "JL_END $x rc=$(cat $O/jl_$x.rc)"; }
side_1() { for x in k l s; do run_j $x; done; }
side_2() { for x in u b; do run_j $x; done; }
side_1 & side_2 & wait
for x in k l s u b; do [ "$(cat $O/jl_$x.rc)" = "0" ] || stop "julia $x rc=$(cat $O/jl_$x.rc)" 4; done
for x in k l s u b; do python3 -I $C81/dedupe_rates_081.py $W/dump_$x $W/dd_$x >> $O/dedupe.log 2>&1 || stop "dedupe $x" 5; done
python3 -I $C81/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_099.py $W/prym079 $W $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || stop "net rc=$rc" 6
log "ALL_DONE"
