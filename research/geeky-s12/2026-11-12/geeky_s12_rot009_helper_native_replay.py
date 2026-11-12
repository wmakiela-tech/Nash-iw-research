#!/usr/bin/env python3
"""ROT009: execute uploaded retained DTC0a helper as-is (no source modification),
compute original 3D tensor K_B values at alpha -1,0,+1 and mask quartics.
SHA256 LOCKED helper. Float64 functional replay only, not historical producer.
"""
import hashlib,importlib.util,json,time
import numpy as np
from pathlib import Path
SRC=Path('/mnt/data/deepseek_python_20260627_a87249.py')
EXPECTED='23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==EXPECTED
spec=importlib.util.spec_from_file_location('dtc0a_retained_helper',str(SRC)); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
N=41; L=2*np.pi;dx=L/N;C1,C2,h=mod.generate_smooth_fields(N,L)
print('ROT009 LOCAL UPLOADED HELPER SHA PASS',EXPECTED, 'numpy',np.__version__,flush=True)
tensors={};t0=time.monotonic()
for alpha in (0.,1.,-1.):
    t=time.monotonic()
    tensors[alpha]=mod.compute_K_B(C1,C2,h,'E_lin',dx,2,alpha)
    print('ALPHA',alpha,'seconds',round(time.monotonic()-t,2),'elapsed',round(time.monotonic()-t0,2),flush=True)
U=tensors[0.];V=(tensors[1.]-tensors[-1.])/2;W=(tensors[1.]+tensors[-1.])/2-U
out={}
for k in range(2,7):
    sl=np.s_[k:N-k,k:N-k,k:N-k,:,:]
    u,v,w=U[sl],V[sl],W[sl]
    avg=lambda a,b:float(np.sum(a*b)/((N-2*k)**3*6))
    out[str(k)]=[avg(u,u),2*avg(u,v),avg(v,v)+2*avg(u,w),2*avg(v,w),avg(w,w)]
    print('MASK',k,'quartic',out[str(k)],flush=True)
result={'return_id':'IW_GEEKY_S12_ROT009_UPLOADED_DTC0A_HELPER_NATIVE_3D_B_25_COEFFICIENT_CHECK_001_20261112',
'helper_sha256':EXPECTED,'helper_kind':'user-uploaded retained helper (NOT historic original runtime)',
'helper_executed':'3 alpha runs at N41, original finite grid FFT TT and original centered stencil/fields',
'alpha_values':[0,1,-1],'output':'K_B quartics 5 masks k2..6','quartics':out,
'elapsed_seconds':time.monotonic()-t0,'numpy_version':np.__version__,'claims':['FLOAT64_NONINTERVAL','NOT_HISTORICAL_BYTE_EXACT_RUNTIME','NO_PHYSICAL_UPGRADE','NO_NOVELTY','NO_CANON','NO_EXEC_SIGN']}
path=Path('/mnt/data/geeky_s12_rot009_helper_native_3d_25_coeff_results.json')
path.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('WROTE',path,flush=True)
