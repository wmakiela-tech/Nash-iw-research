#!/usr/bin/env python3
"""Recheck 2-epoch stopped detector radii with 70-digit arithmetic from logs.
This is an INDEPENDENT endpoint check, not formal rounding proof for the
underlying float-generated synthetic sample path.
"""
import json
import mpmath as mp
mp.mp.dps=70
r=json.load(open(__file__.replace('IW_PRF12_R34_HIGH_PRECISION_ENDPOINT_RECHECK_001_20261110.py','R34_main_stdout.json')))
LAMS=['0.06','0.085','0.12','0.17','0.24','0.34','0.48','0.68']
A=mp.mpf('0.3106993896688963');B=mp.mpf('0.27161358975207756')
S=mp.mpf('0.59514')
limit=min((A-mp.mpf('.2995'))/(2*S),(mp.mpf('.2828')-B)/(2*S))
for e in r['reference_epochs']:
 j=e['epoch']
 for i in (0,1):
  n=e['ref_counts'][i];k=e['ref_positive_counts'][i]
  V=mp.mpf(str(e['observed_quadratic_V'][i]))
  C=mp.log(mp.mpf(4*8*j*(j+1))/mp.mpf('.01'))
  radius=min((C+(-mp.log(1-mp.mpf(x))-mp.mpf(x))*V)/(mp.mpf(x)*n) for x in LAMS)
  nominal=mp.mpf('.99') if i==0 else mp.mpf(3705)/69000
  bias=abs(mp.mpf(k)/n-nominal)
  gap=mp.mpf(str(e['Lipschitz_time_budget'][i]))
  delta=radius+bias+gap
  assert delta<limit
  print('epoch',j,'reference arm',i,'radius',mp.nstr(radius,28),'delta',mp.nstr(delta,28), 'slack',mp.nstr(limit-delta,24))
print('R34 MULTIPRECISION STOP RULE PASS')
