#!/bin/bash
# PREREG_112 runner: (1) Herwig 7.1.5 (sqrt(s) = 2E) for the 11 hadronic primaries at the PREREG_090 energies/events/seeds
# (top without E = 1e5: fails in 7.1.5, REVIEW_110 DEV-2), every Herwig call limited to 1500 s; (2) tables W, V (+ bitwise
# rebuilds of H73 and Sc, H73t descriptive) by build_tables_112.py; (3) native Wu-Xu + PRyMordial for arms w (W) and v (V)
# at the 099/109 nodes and driver control k (Sa, node 22 -17.20 vs 099 s22_1720). Hard-gated; fresh dir.
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code; C81=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D90=/home/claude/nash-iw-research/research/badacz/2026-11-21/data; D99=/home/claude/nash-iw-research/research/badacz/2026-11-22/data
HT=/home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618; PRYM_SRC=/home/claude/bbn077/src/PRyMordial
W=${1:-/home/claude/run112}; O=$W/out; M=$W/mc112; T=$W/tables
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $M $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
echo "25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df  $SRC/data/out/hadrons_from_PBH.dat" | sha256sum -c > $O/inputs_sha.log 2>&1 || stop "input sha" 10
sha256sum $D99/hadrons_099_Sa.dat $D99/hadrons_109_Sc.dat $D90/hadrons_090_H73.dat $D90/mc090/*.json $D99/mc109/*.json $HT/herwig_tables/*.txt $HT/pythia_tables/*.txt $D90/primary_spectra_090.tsv.gz /home/claude/h71/inst/bin/Herwig /home/claude/h71/inst/share/Herwig/HerwigDefaults.rpo >> $O/inputs_sha.log
python3 -I -c "
import json; r=json.load(open('$D90/mc090/requested.json')); r['top'].pop('100000')
json.dump(r, open('$O/requested112.json','x'), indent=1)
P=['gluon','higgs','Wpm','Z0','tau','up','down','strange','charm','bottom','top']
for k,p in enumerate(P): print(p, 90001+k, ','.join(f'{float(E)}:{N}' for E,N in sorted(r[p].items(), key=lambda x: float(x[0]))))
" > $O/spec.txt || stop "spec" 9
(  E=/home/claude/gen090/mamba/envs/h71dep; P=/home/claude/h71/inst
   export PATH=$P/bin:$E/bin:$PATH LD_LIBRARY_PATH=$E/lib:$P/lib:$P/lib/ThePEG:$P/lib/Herwig LHAPDF_DATA_PATH=/home/claude/h71/pdf/sets:$E/share/LHAPDF
   log "MC_START"
   mc() { for c in "$@"; do read -r _ seed spec <<< "$(grep "^$c " $O/spec.txt)"
            python3 -I $C/mult_herwig_097.py $C/herwig71_timeout_wrap.sh 7.1.5 $c $M/herwig71_$c.json $seed $W/w_$c "$spec" 2 > $O/mc_$c.log 2>&1 || exit 4
            if grep -q FAILED $O/mc_$c.log; then exit 4; fi; done; }
   mc gluon up top higgs Z0 tau & a=$!; mc strange down bottom charm Wpm & b=$!
   wait $a || exit 4; wait $b || exit 4 ) || stop "MC" 4
log "MC_END"; rm -rf $W/w_*
zcat $D90/primary_spectra_090.tsv.gz > $W/prim.tsv || stop "prim" 9
python3 -I $C/build_tables_112.py $HT $W/prim.tsv $D90/mc090 $M $D99/mc109 $D90/hadrons_090_H73.dat $D99/hadrons_109_Sc.dat $O/requested112.json $T > $O/tables.log 2>&1 || stop "table gates" 7
cp $T/W.dat $T/w.dat; cp $T/V.dat $T/v.dat; cp $D99/hadrons_099_Sa.dat $T/k.dat
for x in k w v; do cp -a $SRC $W/src_$x && cp $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat && cmp -s $T/$x.dat $W/src_$x/data/out/hadrons_from_PBH.dat || stop "copy src_$x" 9; done
sha256sum $T/*.dat > $O/tables_sha256.log
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
for a in w v; do awk "/^#/ || /^${a}22/" $C/cfg112_$a.dat > $W/cfg_${a}22.dat; awk "/^#/ || /^${a}62/" $C/cfg112_$a.dat > $W/cfg_${a}62.dat; done
run_j() { x=$1; cfg=$2; out=$3; log "JL_START $out"
  timeout 14400 $J --startup-file=no --project=$ENV $C81/rate_dump_081.jl $W/src_$x orig $cfg $W/$out > $O/jl_$out.log 2>&1
  echo $? > $O/jl_$out.rc; log "JL_END $out rc=$(cat $O/jl_$out.rc)"; }
side_1() { run_j w $W/cfg_w22.dat dump_w22; run_j v $W/cfg_v62.dat dump_v62; }
side_2() { run_j k $C/cfg112_k.dat dump_k; run_j v $W/cfg_v22.dat dump_v22; run_j w $W/cfg_w62.dat dump_w62; }
side_1 & side_2 & wait
for x in dump_k dump_w22 dump_w62 dump_v22 dump_v62; do [ "$(cat $O/jl_$x.rc)" = "0" ] || stop "julia $x" 4; done
mkdir -p $W/dd_k $W/dd_w $W/dd_v
python3 -I $C81/dedupe_rates_081.py $W/dump_k $W/dd_k >> $O/dedupe.log 2>&1 || stop "dedupe k" 5
for a in w v; do for j in 22 62; do python3 -I $C81/dedupe_rates_081.py $W/dump_$a$j $W/dd_$a$j >> $O/dedupe.log 2>&1 || stop "dedupe $a$j" 5; done
  cp $W/dd_${a}22/rates_*.csv $W/dd_${a}62/rates_*.csv $W/dd_$a/ && { head -2 $W/dd_${a}22/summary_orig.csv; tail -n +3 $W/dd_${a}22/summary_orig.csv; tail -n +3 $W/dd_${a}62/summary_orig.csv; } > $W/dd_$a/summary_orig.csv || stop "merge $a" 5; done
python3 -I $C81/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_112.py $W/prym079 $W $C > $O/net.log 2>&1 || stop "net" 6
python3 -I $C/analysis_112.py $D99 $W $C $O/analysis112.json > $O/analysis112.stdout 2>&1 || stop "analysis" 8
log "ALL_DONE"
