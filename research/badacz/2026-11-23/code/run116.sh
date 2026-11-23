#!/bin/bash
# PREREG_116 runner: tables x0, x3, p13, s15 (+ bitwise Sc rebuild, prediction proxy D) by build_tables_116.py; native Wu-Xu
# for arms x0, x3 (j22), p13, s15 (j22, j62) and driver control k (Sa, node 22 -17.20 vs 099 s22_1720); after each Julia run the
# raw dump is hashed, deduplicated and deleted (disk; Moderator consent 22 XI); PRyMordial; analysis. Hard-gated; fresh dir.
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-23/code; C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D99=/home/claude/nash-iw-research/research/badacz/2026-11-22/data; D90=/home/claude/nash-iw-research/research/badacz/2026-11-21/data
HT=/home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables; K115=/home/claude/keep115
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618; PRYM_SRC=/home/claude/bbn077/src/PRyMordial
W=${1:-/home/claude/run116}; O=$W/out; T=$W/tables
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat" | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
sha256sum $D99/hadrons_099_Sa.dat $D99/hadrons_109_Sc.dat $D99/mc109/*.json $HT/herwig_tables/*.txt $HT/pythia_tables/*.txt $D90/primary_spectra_090.tsv.gz $K115/*.csv $SRC/tool_script-hadrons_from_PBH.jl $SRC/main-scan.jl >> $O/inputs_sha.log
zcat $D90/primary_spectra_090.tsv.gz > $W/prim.tsv || stop "prim" 9
log "TABLES_START"
python3 -I $C/build_tables_116.py $HT $W/prim.tsv $D99/mc109 $D99/hadrons_109_Sc.dat $K115/rates_w22_1740.csv $K115/rates_w62_1940.csv $T > $O/tables.log 2>&1 || stop "table gates" 7
cp $D99/hadrons_099_Sa.dat $T/k.dat
for x in k x0 x3 p13 s15; do cp -a $SRC $W/src_$x && cp $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat && cmp -s $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat || stop "copy src_$x" 9; done
sha256sum $T/*.dat > $O/tables_sha256.log
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
for a in x0 x3 p13 s15; do awk "/^#/ || /^${a}22_/" $C/cfg116_$a.dat > $W/cfg_${a}22.dat; awk "/^#/ || /^${a}62_/" $C/cfg116_$a.dat > $W/cfg_${a}62.dat; done
run_j() { x=$1; cfg=$2; out=$3; log "JL_START $out"
  timeout 14400 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $W/src_$x orig $cfg $W/$out > $O/jl_$out.log 2>&1
  rc=$?; echo $rc > $O/jl_$out.rc; log "JL_END $out rc=$rc"
  if [ $rc = 0 ]; then ( cd $W && find $out -type f | sort | xargs sha256sum ) > $O/rawsha_$out.log && \
     python3 -I $C81/dedupe_rates_081.py $W/$out $W/dd_${out#dump_} > $O/dedupe_$out.log 2>&1 && rm -rf $W/$out && log "DEDUPED $out"; fi; }
side_1() { run_j s15 $W/cfg_s1522.dat dump_s1522; run_j x3 $W/cfg_x322.dat dump_x322; run_j p13 $W/cfg_p1362.dat dump_p1362; }
side_2() { run_j k $C/cfg116_k.dat dump_k; run_j x0 $W/cfg_x022.dat dump_x022; run_j p13 $W/cfg_p1322.dat dump_p1322; run_j s15 $W/cfg_s1562.dat dump_s1562; }
side_1 & side_2 & wait
for x in dump_k dump_s1522 dump_x322 dump_p1362 dump_x022 dump_p1322 dump_s1562; do [ "$(cat $O/jl_$x.rc)" = "0" ] && [ -d $W/dd_${x#dump_} ] && [ ! -e $W/$x ] || stop "julia/dedupe $x" 4; done
for a in x0 x3 p13 s15; do mkdir -p $W/dd_$a; parts=""; for j in 22 62; do [ -d $W/dd_$a$j ] && parts="$parts $W/dd_$a$j"; done
  set -- $parts; first=$1
  { head -2 $first/summary_orig.csv; for p in $parts; do tail -n +3 $p/summary_orig.csv; done; } > $W/dd_$a/summary_orig.csv || stop "merge $a" 5
  for p in $parts; do for f in $p/rates_*.csv; do ln $f $W/dd_$a/$(basename $f) || stop "link $a" 5; done; done; done
python3 -I $C81/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_116.py $W/prym079 $W $C > $O/net.log 2>&1 || stop "net" 6
python3 -I $C/analysis_116.py $D99 $W $C $O/analysis116.json > $O/analysis116.stdout 2>&1 || stop "analysis" 8
log "ALL_DONE"
