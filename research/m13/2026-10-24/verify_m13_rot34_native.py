#!/usr/bin/env python3
"""ROT34 off-grid source-native check N41, masks 2/4 (same physical grid)."""
import contextlib,importlib.util,io,math,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
q=json.loads((ROOT/'IW_M13_ROT32_alpha_amplitude_identifiability_20261024.json').read_text())
s=importlib.util.spec_from_file_location('retained',ROOT/'deepseek_python_20260627_a87249.py')
m=importlib.util.module_from_spec(s)
with contextlib.redirect_stdout(io.StringIO()):s.loader.exec_module(m)
N=41;alpha=.113;dx=2*np.pi/N
C1,C2,h=m.generate_smooth_fields(N,2*np.pi)
KA=m.compute_K_A_out(C1,C2,h,'E_lin',dx,2,alpha)
KC=m.compute_K_C(C1,C2,h,'E_lin',dx,2,alpha)
maxerr=0
for k in (2,4):
    case=next(x for x in q['cases'] if x['N']==N and x['mask_k']==k)
    for ch,t in [('A',KA),('C',KC)]:
        actual=float(m.rms_norm(t,slice(k,N-k)))
        poly=case['G_quartic_squared_RMS'][ch]
        expected=math.sqrt(np.polynomial.polynomial.polyval(alpha,poly))
        err=abs(actual/expected-1)
        maxerr=max(maxerr,err)
        assert err<2e-11,(ch,k,actual,expected,err)
        print('UNMODIFIED_HELPER_OFFGRID_PASS',N,k,ch,alpha,'rms',actual,'relative_error',err)
print('NATIVE_4_OF_4_PASS_MAX_REL',maxerr)