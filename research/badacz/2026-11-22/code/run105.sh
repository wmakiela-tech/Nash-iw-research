#!/bin/bash
# PREREG_105 runner: Herwig 7.1.5 (built by build_herwig71_104.sh), primary up, sqrt(s) = E', the 6 nodes of PREREG_097
# (spec_097.log), 10000 events each. Hard-gated: fresh dir; failure -> STOP, no ALL_DONE.  Usage: bash run105.sh [run_dir]
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code; D=/home/claude/nash-iw-research/research/badacz/2026-11-22/data
E=/home/claude/gen090/mamba/envs/h71dep; P=/home/claude/h71/inst
export PATH=$P/bin:$E/bin:$PATH LD_LIBRARY_PATH=$E/lib:$P/lib:$P/lib/ThePEG:$P/lib/Herwig LHAPDF_DATA_PATH=/home/claude/h71/pdf/sets:$E/share/LHAPDF
W=${1:-/home/claude/run105}; O=$W/out; M=$W/mc
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $M
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
SPEC=$(sed "s/:2000/:10000/g" $D/spec_097.log); echo "$SPEC" > $O/spec.txt
$P/bin/Herwig --version > $O/versions.txt 2>&1
sha256sum $C/mult_herwig_097.py $C/analysis_105.py $P/bin/Herwig $P/share/Herwig/HerwigDefaults.rpo /home/claude/h71/dl/*.tar.bz2 /home/claude/h71/pdf/*.tar.gz /home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables/herwig_tables/{pipm,Kpm,K0L,proton,neutron}.txt > $O/inputs_sha.log
log "MC_START"
python3 -I $C/mult_herwig_097.py $P/bin/Herwig 7.1.5 up $M/H71_f1.json 9705 $W/w71 "$SPEC" 1 > $O/H71_f1.log 2>&1 || stop "H71_f1" 4
log "ALL_DONE"
