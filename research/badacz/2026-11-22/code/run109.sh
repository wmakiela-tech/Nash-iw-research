#!/bin/bash
# PREREG_109 runner: (1) Herwig 7.1.5 at sqrt(s) = 2E for 10 hadronic primaries at E = 5e4, 7.0711e4, 1e5 GeV (2000 events);
# (2) seam check is in analysis_109.py; (3) table Sc (+ Sa rebuild, bitwise vs 099); (4) native Wu-Xu + PRyMordial for arm c
# (Sc) at the 099 nodes and driver control k (Sa table, node 22 -17.20 vs 099 s22_1720). Hard-gated; fresh dir.
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code; C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D90=/home/claude/nash-iw-research/research/badacz/2026-11-21/data; D99=/home/claude/nash-iw-research/research/badacz/2026-11-22/data
HT=/home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618; PRYM_SRC=/home/claude/bbn077/src/PRyMordial
W=${1:-/home/claude/run109}; O=$W/out; M=$W/mc109; T=$W/tables
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $M $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat" | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
sha256sum $D99/hadrons_099_Sa.dat $HT/herwig_tables/*.txt $HT/pythia_tables/*.txt $D90/primary_spectra_090.tsv.gz /home/claude/h71/inst/bin/Herwig /home/claude/h71/inst/share/Herwig/HerwigDefaults.rpo >> $O/inputs_sha.log
SPEC="50000.0:2000,70710.67811865475:2000,100000.0:2000"; echo "$SPEC" > $O/spec.txt
(  E=/home/claude/gen090/mamba/envs/h71dep; P=/home/claude/h71/inst
   export PATH=$P/bin:$E/bin:$PATH LD_LIBRARY_PATH=$E/lib:$P/lib:$P/lib/ThePEG:$P/lib/Herwig LHAPDF_DATA_PATH=/home/claude/h71/pdf/sets:$E/share/LHAPDF
   log "MC_START"
   mc() { for c in "$@"; do python3 -I $C/mult_herwig_097.py $P/bin/Herwig 7.1.5 $c $M/herwig71_$c.json 9709 $W/w_$c "$SPEC" 2 > $O/mc_$c.log 2>&1 || exit 4; done; }
   mc up down strange charm bottom & a=$!; mc top gluon Wpm Z0 tau & b=$!
   wait $a || exit 4; wait $b || exit 4 ) || stop "MC" 4
log "MC_END"; rm -rf $W/w_*
zcat $D90/primary_spectra_090.tsv.gz > $W/prim.tsv || stop "prim" 9
python3 -I $C/build_tables_109.py $HT $W/prim.tsv $D90/mc090 $D90/hadrons_085_R2.dat $M $T > $O/tables.log 2>&1 || stop "table gates" 7
cmp -s $T/Sa.dat $D99/hadrons_099_Sa.dat || stop "G_REBUILD Sa" 7
cp $T/Sc.dat $T/c.dat; cp $D99/hadrons_099_Sa.dat $T/k.dat
for x in k c; do cp -a $SRC $W/src_$x && cp $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat && cmp -s $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat || stop "copy src_$x" 9; done
sha256sum $T/*.dat > $O/tables_sha256.log
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
awk '/^#/ || /^c22/' $C/cfg109_c.dat > $W/cfg_c22.dat; awk '/^#/ || /^c62/' $C/cfg109_c.dat > $W/cfg_c62.dat
run_j() { x=$1; cfg=$2; out=$3; log "JL_START $out"
  timeout 14400 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $W/src_$x orig $cfg $W/$out > $O/jl_$out.log 2>&1
  echo $? > $O/jl_$out.rc; log "JL_END $out rc=$(cat $O/jl_$out.rc)"; }
side_1() { run_j c $W/cfg_c22.dat dump_c22; }
side_2() { run_j k $C/cfg109_k.dat dump_k; run_j c $W/cfg_c62.dat dump_c62; }
side_1 & side_2 & wait
for x in dump_k dump_c22 dump_c62; do [ "$(cat $O/jl_$x.rc)" = "0" ] || stop "julia $x" 4; done
mkdir -p $W/dd_c $W/dd_k
python3 -I $C81/dedupe_rates_081.py $W/dump_k $W/dd_k >> $O/dedupe.log 2>&1 || stop "dedupe k" 5
python3 -I $C81/dedupe_rates_081.py $W/dump_c22 $W/dd_c22 >> $O/dedupe.log 2>&1 || stop "dedupe c22" 5
python3 -I $C81/dedupe_rates_081.py $W/dump_c62 $W/dd_c62 >> $O/dedupe.log 2>&1 || stop "dedupe c62" 5
cp $W/dd_c22/rates_*.csv $W/dd_c62/rates_*.csv $W/dd_c/ && { head -2 $W/dd_c22/summary_orig.csv; tail -n +3 $W/dd_c22/summary_orig.csv; tail -n +3 $W/dd_c62/summary_orig.csv; } > $W/dd_c/summary_orig.csv || stop "merge c" 5
python3 -I $C81/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_109.py $W/prym079 $W $C > $O/net.log 2>&1 || stop "net" 6
log "ALL_DONE"
