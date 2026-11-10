#!/usr/bin/env python3
"""Mech-S8 ROT016 public compact exact Fraction witness, Python >= 3.8.
The model interface from author v2 main-scan.jl retains five integrated
hadron rates R_h(M), not the secondary energy spectra S_h(M,E).
Original author data/out/hadrons_from_PBH.dat pinned Git d395183674,
blob 06d0883a27b108692720422294ba2baacd381a64, FIRST mass row.
Both spectra below are hypothetical mathematical profiles, NOT PYTHIA
or BlackHawk physical spectra. NO physical PBH/BBN-bound inference.
"""
from fractions import Fraction as F
rates = {
    "charged_pion": "489105.5126008581",
    "charged_kaon": "59105.93631247951",
    "K0L": "29086.774913348447",
    "proton_group": "34849.08026691193",
    "neutron_group": "34656.17773724596",
}
# h_a(E)=4(E-a), a<=E<=a+1/2;
#       =4(a+1-E), a+1/2<=E<=a+1; =0 otherwise.
# Exact integration gives area=1 and E-mean=a+1/2.
def moments(a):
    a = F(a)
    left_number = F(1,2)
    right_number = F(1,2)
    left_energy = a/2 + F(1,6)
    right_energy = a/2 + F(1,3)
    return left_number+right_number, left_energy+right_energy
nl,ml=moments(1)
nh,mh=moments(100)
assert nl == nh == 1 and ml == F(3,2) and mh == F(201,2)
assert mh/ml == 67
for name,rate in rates.items():
    r=F(rate)
    assert r > 0 and r*nl == r*nh
    assert r*mh == 67*(r*ml)
    print(name, "equal number rate", str(r), "moment ratio", mh/ml)
print("PASS 5/5 exact source-rate groups; rate-only ODE spectral nullspace.")
print("NO_PHYSICAL_SOURCE_VALIDATION / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN")
