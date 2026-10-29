#!/usr/bin/env python3
"""Source-typed stress diagnostic, not a complete TPP energy-loss operator.

Uses asymptotic q_TPP and q_ICS in an isotropic MONOENERGETIC photon bath
from Mastichiadis-style approximate q energy-loss functions as quoted in
'On the numerical analysis of triplet pair production cross-sections and
the mean energy of produced particles for modelling electron-photon cascade
in a soft photon field' (1999). q=k is fixed to epsilon=2.701*T,
a=1 ONLY. Actual Planck+angle integrated LOSS must be calculated separately.
"""
from __future__ import annotations
import math, csv, argparse, pathlib
import sys
import numpy as np
from scipy.optimize import brentq
P=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(P))
from IW_DAX_S7_ROTATION_68_BOUNDED_CHANNEL_OPERATOR_20261029 import PhotonicRates, ME, ALPHA, TNUC, r67

def qratio(k):
    L=math.log(2*k)
    q_tpp=.386*ALPHA*(L*L)*(L-218/84)
    q_ics=math.log(4*k)-11/6
    return q_tpp/q_ics

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--out',type=pathlib.Path,default=P)
    ar=ap.parse_args();ar.out.mkdir(parents=True,exist_ok=True)
    bg=r67.BG(nx=125,nq=140)
    rates=PhotonicRates(132)
    rows=[]
    for E in [1e2,1e3,1e4,1e5,1e6,1e8,1e9,1e12]:
        k=E*1e3*(2.701*TNUC)/ME**2
        ic,_=bg.calc(E)
        tr=rates.tpp_asymptotic_event(E)
        rows.append({'E_electron_GeV':E,'T_MeV':TNUC,'k_monochromatic_2p701T_a1':k,
         'TPP_event_rate_asymptotic_Planck_angular_s_inv':tr,
         'IC_event_rate_BG_Planck_s_inv':ic,'TPP_to_IC_event_rate_ratio':tr/ic,
         'q_TPP_over_q_ICS_monoenergetic_loss_proxy':qratio(k),
         'TPP_loss_would_dominate_in_monoenergetic_proxy':int(qratio(k)>1)})
    with (ar.out/'IW_DAX_S7_R68_TPP_EVENT_VS_LOSS_PROXY_20261029.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    root=brentq(lambda x:qratio(x)-1,1e7,1e10)
    egev=root*ME**2/(1e3*2.701*TNUC)
    print('critical k*=',root,'E* GeV mono 2.701T:',egev)
    for row in rows:print(row['E_electron_GeV'],row['TPP_to_IC_event_rate_ratio'],row['q_TPP_over_q_ICS_monoenergetic_loss_proxy'])
if __name__=='__main__':main()
