#!/usr/bin/env python3
"""N31 off-grid direct test of unchanged legacy DTC helper vs ROT32 A/C quartics."""
import json, math,importlib.util,contextlib,io
import numpy as np
from pathlib import Path
ROOT=Path(__file__).resolve().parent
info=json.loads((ROOT/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').read_text())
record=next(t for t in info['cases'] if t['N']==31 and t['mask_k']==3)
a=.113
spec=importlib.util.spec_from_file_location('old_rot32',ROOT/'deepseek_python_20260627_a87249.py')
h=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(h)
N=31;dx=2*math.pi/N
C1,C2,H=h.generate_smooth_fields(N,2*math.pi)
Kc=h.compute_K_C(C1,C2,H,'E_lin',dx,2,a)
Ka=h.compute_K_A_out(C1,C2,H,'E_lin',dx,2,a)
for ch,K in [('A',Ka),('C',Kc)]:
 p=record['G_quartic_squared_RMS'][ch]
 predicted=math.sqrt(np.polynomial.polynomial.polyval(a,p))
 # check native rms_norm signature in the original source before calling:
 actual=float(h.rms_norm(K,slice(3,N-3)))
 error=abs(actual/predicted-1)
 assert error<5e-11,(ch,error,actual,predicted)
 print('UNMODIFIED_SOURCE_OFFGRID_PASS',ch,a,actual,predicted,error)