#!/bin/bash
# PREREG_085 / GAP-005 runner, hard-gated: fresh run dir required; every stage stops the pipeline with a nonzero exit
# and NO "ALL_DONE" on failure (BlackHawk/Julia rc, table gate G1, rule gate G2, injection gates, Julia rc, dedupe, NET).
set -u
export JULIA_DEPOT_PATH=/home/claude/julia066/depot JULIA_PKG_OFFLINE=true
J=/home/claude/julia066/julia-1.12.3/bin/julia; ENV=/home/claude/julia066/wuxu_env
SRC=/home/claude/fenyutanchan/primordial-black-hole/arXiv-2509.05618
BH=/home/claude/bh085/BlackHawk_v2.3; BH_TAR=/home/claude/bh085/dl/blackhawk_v2.3.tar.bz2
G0_IN=/home/claude/work085/G0_pythia_5_1e5_100.dat
PRYM_SRC=/home/claude/bbn077/src/PRyMordial
C=/home/claude/nash-iw-research/research/badacz/2026-11-21/code
D83=/home/claude/nash-iw-research/research/badacz/2026-11-21/data
W=/home/claude/run085; O=$W/out; T=$W/tables
[ -e $W ] && { echo "REFUSE: $W exists (fresh run required)"; exit 3; }
mkdir -p $O $T
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
# 0. provenance of inputs
echo "dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7  $BH_TAR" | sha256sum -c >> $O/inputs_sha.log 2>&1 || stop "BlackHawk tarball sha" 10
echo "629ad085ea59d84908dde54de2a9554f68847ce922bd857337bed2ebae3fd942  $G0_IN" | sha256sum -c >> $O/inputs_sha.log 2>&1 || stop "G0 sha" 10
cp $G0_IN $T/G0.dat
sha256sum $SRC/data/out/hadrons_from_PBH.dat $BH/BlackHawk_inst.x $SRC/main-scan.jl >> $O/inputs_sha.log
# 1. BlackHawk tables (2 at a time; distinct result names per tag)
gen() { tag=$1; log "BH_START $tag"
  timeout 3600 $J --startup-file=no --project=$ENV $C/gen_hadron_table_085.jl $SRC $BH $T/$tag.dat $2 $3 $4 $5 $tag > $O/bh_$tag.log 2>&1
  echo $? > $O/bh_$tag.rc; log "BH_END $tag rc=$(cat $O/bh_$tag.rc)"; }
gen P_lo 0 5 25 17 & gen P_hi 0 25 1e5 85 & wait
gen H_hi 1 25 1e5 85 & gen H_R0 1 5 1e5 100 & wait
for t in P_lo P_hi H_hi H_R0; do [ "$(cat $O/bh_$t.rc)" = "0" ] || stop "BlackHawk table $t rc=$(cat $O/bh_$t.rc)" 4; done
python3 -I $C/combine_tables_085.py $T/G0.dat $T/P_lo.dat $T/P_hi.dat $T/H_hi.dat $T/H_R0.dat $T/R2.dat $O/table_gates085.json > $O/combine.log 2>&1 || stop "G1 split additivity (or combine error)" 7
python3 -I -c "import json,sys; sys.exit(0 if json.load(open('$O/table_gates085.json'))['G2_RULE_IRRELEVANCE']['pass'] else 1)" || stop "G2 rule irrelevance FAIL (declared: stop, DEV required)" 7
python3 -I $C/table_scale_085.py $T/G0.dat 2 $T/G0x2.dat >> $O/combine.log 2>&1 || stop "x2 table" 7
sha256sum $T/*.dat > $O/tables_sha256.log
# 2. source copies carrying the injected tables
for v in inj:G0 x2:G0x2 her:R2; do n=${v%%:*}; t=${v##*:}
  cp -a $SRC $W/src_$n && cp $T/$t.dat $W/src_$n/data/out/hadrons_from_PBH.dat || stop "copy src_$n" 9
  cmp -s $T/$t.dat $W/src_$n/data/out/hadrons_from_PBH.dat || stop "table not in src_$n" 9
done
# 3. injection controls (negative: G0 at 4 nodes; positive: G0x2 at o22_1720)
run_j() { tree=$1; arm=$2; cfg=$3; out=$4; tag=$5; log "JL_START $tag"
  timeout 14400 $J --startup-file=no --project=$ENV $C/rate_dump_081.jl $W/src_$tree $arm $C/$cfg $out > $O/jl_$tag.log 2>&1
  echo $? > $O/jl_$tag.rc; log "JL_END $tag rc=$(cat $O/jl_$tag.rc)"; }
run_j inj orig cfg085_inj_orig.dat $W/dump_inj inj_orig & run_j inj e5 cfg085_inj_e5.dat $W/dump_inj inj_e5 & wait
run_j x2 orig cfg085_x2_orig.dat $W/dump_x2 x2_orig
for t in inj_orig inj_e5 x2_orig; do [ "$(cat $O/jl_$t.rc)" = "0" ] || stop "julia $t rc=$(cat $O/jl_$t.rc)" 4; done
python3 -I $C/check_inj_085.py $D83 $W/dump_inj $W/dump_x2 $O/inj085.json > $O/inj.log 2>&1 || stop "injection gates" 8
# 4. HERWIG (R2) native grids, both arms
run_j her orig cfg085_her_orig.dat $W/dump_her her_orig & run_j her e5 cfg085_her_e5.dat $W/dump_her her_e5 & wait
for t in her_orig her_e5; do [ "$(cat $O/jl_$t.rc)" = "0" ] || stop "julia $t rc=$(cat $O/jl_$t.rc)" 4; done
python3 -I $C/dedupe_rates_081.py $W/dump_her $W/dump_her_dedup > $O/dedupe.log 2>&1 || stop "dedupe" 5
# 5. network transfer
python3 -I $C/prym_rate_patch_079.py $PRYM_SRC $W/prym079 > $O/patch.log 2>&1 || stop "prym patch" 2
log "NET_START"
python3 -I $C/run_net_085.py $W/prym079 $W/dump_her_dedup $O $C > $O/net.log 2>&1; rc=$?
[ $rc = 0 ] || stop "net rc=$rc" 6
log "ALL_DONE"
