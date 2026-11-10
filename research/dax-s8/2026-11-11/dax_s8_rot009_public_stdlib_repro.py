#!/usr/bin/env python3
"""DAX-S8 ROT009: standalone stdlib proof of frame-typed 4e cut transfer.
Exact on-shell identities use Fraction; displayed angles use math float.
NO QED amplitudes/rates, transport, PBH or BBN.
"""
from fractions import Fraction as Q
from math import sqrt, degrees, atan, acos, tan, radians
import json
E=Q('1436554')            # gamma lab energy, MeV
u=Q('0.07818527068831995') # bath photon lab energy, MeV
m=Q('0.51099895')         # electron rest mass energy, MeV
W2=4*E*u
assert W2>16*m*m
# Four outgoing COM leptons with pT vectors +x,-x,+y,-y; pz*=0.
# All energy W/4 and pT^2=W^2/16-m^2.
pT2=E*u/4-m*m
L=(E+u)/4
Z=(E-u)/4
assert pT2>0
assert pT2==W2/16-m*m
assert L*L-Z*Z-pT2==m*m
assert 4*L==E+u and 4*Z==E-u
W=sqrt(float(W2))
theta_deg=degrees(atan(sqrt(float(pT2))/float(Z)))
max_min_theta_deg=degrees(acos(float((E-u)/(E+u))))
# 4x1GeV cut in COM needs W>=4GeV. Same LAB energy cut is passed.
assert W/4<1000<float(L)
# 7-degree LAB all-track cut requires u>=E*tan^2(3.5deg), regardless of QED.
min_u_lab7=float(E)*tan(radians(3.5))**2
min_u_com4=4000**2/(4*float(E))
assert float(u)<min_u_com4<min_u_lab7
assert theta_deg<max_min_theta_deg<7
print(json.dumps({
 'status':'PASS_EXACT_4MOMENTUM_AND_LAB_ANGLE_CUT_NONMAP',
 'COM_sqrt_s_MeV':W,
 'COM_each_lepton_MeV':W/4,
 'LAB_each_lepton_MeV':float(L),
 'LAB_each_polar_angle_degrees':theta_deg,
 'LAB_max_possible_min_polar_angle_degrees':max_min_theta_deg,
 'COM_cut_1GeV_each_passes':False,
 'LAB_cut_1GeV_each_passes_for_witness':True,
 'LAB_7deg_all_tracks_possible_at_epsilon_T':False,
 'epsilon_min_COM_1GeV_each_MeV':min_u_com4,
 'epsilon_min_LAB_7deg_all_tracks_MeV':min_u_lab7,
 'source':'Sotsky 2006 arxiv:hep-ph/0604020, COM collider cuts',
 'claim_ceiling':'NO_QED_MATRIX_ELEMENT / NO_RATE / NO_PHYSICAL_DEPOSITION / NO_CANON'
},indent=2,sort_keys=True))
