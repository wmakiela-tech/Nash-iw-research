#!/usr/bin/env python3
"""MT13 ROT038: exact rational Bernstein source-cone certificates.
Execute from Nash-iw-research clone: M13 ROT32 JSON must be at sibling path.
Or use the local Moderator ZIP pinned 15-quartic source JSON beside this file.
This is NOT a physical DTC runtime or measured noise test.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, sqrt
import json

HERE=Path(__file__).resolve().parent
REPO_M13=HERE.parents[1]/'m13/2026-10-24/IW_M13_ROT32_alpha_amplitude_identifiability_001.json'
PINNED=HERE/'M13_ROT32_N41_15_decimal_quartics_source_pinned.json'
if REPO_M13.exists():
    doc=json.loads(REPO_M13.read_text())
    cases=sorted((c for c in doc['cases'] if c['N']==41),key=lambda c:c['mask_k'])
    assert [c['mask_k'] for c in cases]==[2,3,4,5,6]
    coeff={ch:[[str(x) for x in c['G_quartic_squared_RMS'][ch]] for c in cases] for ch in 'ABC'}
else:
    assert PINNED.exists(),'M13 source JSON or pinned source required'
    coeff=json.loads(PINNED.read_text())['G_quartic_squared_RMS']
n=[50653,42875,35937,29791,24389]
v=[7778,6938,6146,5402,24389]
ells={'A':['1','0','0','0','-1.273'],
      'B':['1','-1.47','0','.72','-.28'],
      'C':['1','-1.361','0','0','0']}
assert [n[i]-n[i+1] for i in range(4)]+[n[-1]]==v

def build(ch):
    g=[[F(s) for s in row] for row in coeff[ch]]
    m=[[(n[i]*g[i][k]-n[i+1]*g[i+1][k])/v[i] for k in range(5)] for i in range(4)]
    m.append(g[-1])
    return g,m

def val(poly,a):
    return sum(c*a**k for k,c in enumerate(poly))

for ch in 'ABC':
    g,m=build(ch)
    ell=[F(s) for s in ells[ch]]
    p=[sum(ell[i]*m[i][k] for i in range(5)) for k in range(5)]
    # Bernstein degree 4 on alpha=[0,1/5], with x=5alpha.
    b=[sum(p[k]/5**k*F(comb(j,k),comb(4,k)) for k in range(j+1)) for j in range(5)]
    assert max(b)<0,('source-Bernstein sign fail',ch)
    alpha0=F(1,20)
    # Synthetic 5% increase of outermost disjoint shell ONLY.
    obs=[val(x,alpha0) for x in m]
    obs[0]*=F(21,20)
    tau=F(1,100)*val(g[0],alpha0)
    z=float(sum(ell[i]*obs[i] for i in range(5)))/(float(tau)*sqrt(sum(float(ell[i]**2/v[i]) for i in range(5))))
    assert z>1.6448536269514722 and z*z>10.371033903003577
    print(ch,'exact Bernstein all negative',
          [format(float(x),'.8e') for x in b],
          'z',format(z,'.12f'),'GLOBAL Q* >=',format(z*z,'.8f'))
print('PASS all three exact rational source-cone certificates')
