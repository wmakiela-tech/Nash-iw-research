#!/bin/bash
# PREREG_097 runner: Herwig 7.2.0 and 7.3.0 (conda-forge), primary 'up', 6 BlackHawk HERWIG table nodes, 2000 events each.
# Arms: H72_f1 (sqrt s = E', as the archived BlackHawk main.cpp), H73_f1, H73_f2 (sqrt s = 2E', manual convention / our 090).
# Hard-gated: fresh dir; any failure -> STOP, no ALL_DONE.  Usage: bash run097.sh [run_dir]
set -u
C=/home/claude/nash-iw-research/research/badacz/2026-11-22/code
H72=/home/claude/gen090/mamba/envs/hw72/bin/Herwig; H73=/home/claude/gen090/mamba/envs/hw/bin/Herwig
export LHAPDF_DATA_PATH=/home/claude/gen090/mamba/envs/hw/share/LHAPDF
W=${1:-/home/claude/run097}; O=$W/out; M=$W/mc
[ -e $W ] && { echo "REFUSE"; exit 3; }; mkdir -p $O $M
log() { echo "$1 $(date '+%d %H:%M:%S')" | tee -a $O/timeline.log; }
stop() { log "STOP: $1"; exit $2; }
SPEC=$(python3 -I -c "
import math
E=[10**(math.log10(25.)+(math.log10(1e5)-math.log10(25.))/99*i) for i in (0,20,40,60,80,99)]
print(','.join('%r:2000'%e for e in E))")
echo "$SPEC" > $O/spec.txt
{ $H72 --version; $H73 --version; } > $O/versions.txt 2>&1
sha256sum $C/mult_herwig_097.py $C/analysis_097.py /home/claude/bh085/src/blackhawk_v2.3/src/tables/hadronization_tables/herwig_tables/{pipm,Kpm,K0L,proton,neutron}.txt > $O/inputs_sha.log
log "MC_START"
python3 -I $C/mult_herwig_097.py $H72 7.2.0 up $M/H72_f1.json 9701 $W/w72 "$SPEC" 1 > $O/H72_f1.log 2>&1 & p1=$!
python3 -I $C/mult_herwig_097.py $H73 7.3.0 up $M/H73_f1.json 9702 $W/w73a "$SPEC" 1 > $O/H73_f1.log 2>&1 & p2=$!
wait $p1 || stop "H72_f1" 4; wait $p2 || stop "H73_f1" 4
python3 -I $C/mult_herwig_097.py $H73 7.3.0 up $M/H73_f2.json 9703 $W/w73b "$SPEC" 2 > $O/H73_f2.log 2>&1 || stop "H73_f2" 4
log "ALL_DONE"
