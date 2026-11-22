#!/bin/bash
# Build ThePEG 2.1.5 + Herwig 7.1.5 (sources from herwig.hepforge.org / thepeg.hepforge.org downloads) with conda-forge
# GCC 9.5, boost-cpp 1.74, GSL 2.8, FastJet 3.5.3, LHAPDF 6.5.6, HepMC 2.06.11 (env h71dep). For the DIR-009 vintage
# fingerprint (PREREG_105). Each step exits nonzero on failure (fix after a false STAGE_OK on a failed configure). Usage: bash build_herwig71_104.sh <stage: thepeg|herwig|repo> ; logs in /home/claude/h71/log_*.txt
set -eu
E=/home/claude/gen090/mamba/envs/h71dep; S=/home/claude/h71/src; P=/home/claude/h71/inst
export PATH=$E/bin:$PATH CC=$E/bin/x86_64-conda-linux-gnu-gcc CXX=$E/bin/x86_64-conda-linux-gnu-g++ FC=$E/bin/x86_64-conda-linux-gnu-gfortran F77=$E/bin/x86_64-conda-linux-gnu-gfortran
export CPPFLAGS="-I$E/include" LDFLAGS="-L$E/lib -Wl,-rpath,$E/lib -Wl,-rpath,$P/lib -Wl,-rpath,$P/lib/ThePEG -Wl,-rpath,$P/lib/Herwig" LD_LIBRARY_PATH=$E/lib:$P/lib:$P/lib/ThePEG
export LHAPDF_DATA_PATH=/home/claude/gen090/mamba/envs/hw/share/LHAPDF
case "$1" in
 thepeg) cd $S/ThePEG-2.1.5 && ./configure --prefix=$P --with-gsl=$E --with-boost=$E --with-fastjet=$E --with-hepmc=$E --with-lhapdf=$E --with-zlib=$E --without-rivet > /home/claude/h71/log_thepeg_conf.txt 2>&1 || exit 11; make -j2 > /home/claude/h71/log_thepeg_make.txt 2>&1 || exit 12; make install > /home/claude/h71/log_thepeg_inst.txt 2>&1 || exit 13 ;;
 herwig) cd $S/Herwig-7.1.5 && ./configure --prefix=$P --with-thepeg=$P --with-gsl=$E --with-boost=$E --with-fastjet=$E --without-madgraph --without-openloops --without-vbfnlo --without-gosam --without-njet > /home/claude/h71/log_herwig_conf.txt 2>&1 || exit 21; make -j2 > /home/claude/h71/log_herwig_make.txt 2>&1 || exit 22; make install > /home/claude/h71/log_herwig_inst.txt 2>&1 || exit 23 ;;
 *) echo "stage?"; exit 2 ;;
esac
echo "STAGE_OK $1"
