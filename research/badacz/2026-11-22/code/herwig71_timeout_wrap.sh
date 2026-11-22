#!/bin/bash
# PREREG_109 DEV-1: wrapper passed to mult_herwig_097.py as <herwig_bin>; every Herwig call (read/run) gets a wall-clock limit
# so that a hung event loop (observed: top, sqrt(s) = 2e5 GeV, event 568) ends with a nonzero return code instead of blocking.
exec timeout 1500 /home/claude/h71/inst/bin/Herwig "$@"
