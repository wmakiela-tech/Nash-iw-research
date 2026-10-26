#!/usr/bin/env python3
"""DAX-S7 rotation 59: independent paper/code entropy contract check, beta=0.

Input: unchanged N_around_m_e.csv (1000 rows), from
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/data/ext/N_around_m_e.csv
Run: python IW_DAX_S7_ROTATION_59_SOURCE_ENTROPY_RECHECK_20261026.py N_around_m_e.csv
No Julia solver or PBH bounds; does not model neutrino injection by PBHs.
"""
import bisect
import csv
import hashlib
import math
import sys
from pathlib import Path

SHA='93f2494f026c5d0587ea40fe08bb938dd9d01fa8'
TNUC=0.07818527068831995
TBASE=10.0
if len(sys.argv)!=2:
    sys.exit('Usage: python audit.py path/to/N_around_m_e.csv')
raw=Path(sys.argv[1]).read_bytes()
git_sha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
if git_sha!=SHA:
    sys.exit('SOURCE_IDENTITY_FAIL: '+git_sha)
rows=[list(map(float,row)) for row in csv.reader(raw.decode().splitlines())]
assert len(rows)==1000
grid=[math.log(row[0]) for row in rows]
def values(k,z):
    z0,z1=grid[k:k+2]
    r0,r1=rows[k:k+2]
    g=r0[1]+(r1[1]-r0[1])*(z-z0)/(z1-z0)
    s=r0[2]+(r1[2]-r0[2])*(z-z0)/(z1-z0)
    return g,s,(r1[1]-r0[1])/(z1-z0)/g,(r1[2]-r0[2])/(z1-z0)/s
def thermo(T):
    z=math.log(T)
    k=max(0,min(len(grid)-2,bisect.bisect_right(grid,z)-1))
    return values(k,z)
def log_a(T,n=8):
    z0,z1=math.log(T),math.log(TBASE)
    knots=[z1]+[v for v in reversed(grid) if z0<v<z1]+[z0]
    total=0.0
    for hi,lo in zip(knots,knots[1:]):
        k=max(0,min(len(grid)-2,bisect.bisect_right(grid,(hi+lo)/2)-1))
        step=(lo-hi)/n
        for j in range(n):
            a=hi+j*step
            b=a+step
            def fun(z):
                _,_,r,s=values(k,z)
                C=-4+r/(3+s) # actual main-scan.jl beta=0
                return (4+r)/C
            total+=step*(fun(a)+4*fun((a+b)/2)+fun(b))/6
    return total
g0,s0,_,_=thermo(TBASE)
for T in [1,0.5,0.2,0.1,TNUC,rows[0][0]]:
    gr,gs,r,s=thermo(T)
    A=log_a(T)
    A_paper=math.log(TBASE/T)+math.log(s0/gs)/3
    S=math.exp(3*(A-A_paper))
    nu_src=TBASE/T*math.exp(-A) # infer by paper's T_nu*a=constant
    nu_paper=(gs/s0)**(1/3) # paper Eq (A.1)
    print(f'T={T:.12g}  entropy_ratio={S:.12g}  Tnu/Tg_src={nu_src:.12g}  Tnu/Tg_paper={nu_paper:.12g}')
    if abs(T-TNUC)<1e-10:
        assert abs(S-1.14678163340782)<2e-9
        assert abs(nu_src-0.70077683358859)<2e-9
        assert abs(nu_paper-0.73351102521884)<2e-9
print('PASS: source-table paper/code mismatch under beta=0')
