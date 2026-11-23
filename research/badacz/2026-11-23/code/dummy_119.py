#!/usr/bin/env python3
"""PREREG_119: synthetic inputs (arbitrary numbers, file formats only) to exercise analysis_119.py before the run.
Usage: python3 -I dummy_119.py <dir>"""
import gzip, os, sys
import numpy as np

D = sys.argv[1]; os.makedirs(f"{D}/run", exist_ok=True)
rng = np.random.default_rng(119)
for a in ("code", "ad"):
    for s in ("def", "r8", "r9"):
        for j in (22, 62):
            tag = f"{a}_{s}_j{j}"
            with open(f"{D}/run/summary_{tag}.csv", "w") as f:
                f.write("tag,arm,solver,j,m_init_g,Y,wall_s,nsteps,retcode,T_nuc_MeV\n")
                f.write(f"{tag},{a},{s},{j},1e9,{0.2 + rng.random() * 0.1},1.0,10,Success,0.07818527068831995\n")
            with open(f"{D}/run/bg_{tag}.csv", "w") as f:
                f.write("T_target_MeV,eta,t_s,rho_GeV4,T_MeV,X_n,N_s,N_rho,Q_a3NsT3_GeV3\n")
                for k, T in enumerate([10.0, 1.0, 0.5, 0.25, 0.1, 0.07818527068831995]):
                    f.write(f"{T},{30 + k},{0.01 * 10 ** k},1e-12,{T},0.1,10,10,{1 + rng.random() * 0.2}\n")
M = np.array([float(f"{x:.5e}") for x in np.geomspace(1.221e19, 1e46, 1000)])
with open(f"{D}/fcode.csv", "w") as f:
    f.write("M_GeV,M_g,T_BH_GeV,N_rho_TBH,N_BH,f_code_GeV4,m_Pl_GeV,M_Pl_GeV\n")
    for m in M:
        f.write(f"{float(m)!r},{float(m) / 5.6095886e23!r},1,1,1,{1.6e74 * (1 + 0.01 * rng.random())!r},1.22e19,2.4e18\n")
with open(f"{D}/fM.txt", "w") as f:
    f.write("   mass/a   0.00000e+000   1.00000e-003\n")
    for m in M:
        f.write(f"   {m:.5e}   {9.5e73 * (1 + 0.01 * rng.random()):.5e}   1.0\n")
E = np.geomspace(5, 1e5, 100)
with gzip.open(f"{D}/prim.tsv.gz", "wt") as f:
    f.write("k\tm_g\tA\tenergy\tB\n")
    for k, mg in enumerate([3e9, 5e10]):
        for e in E:
            f.write(f"{k}\t{mg}\t{1e20 / e ** 2}\t{e}\t{1e19 / e ** 2}\n")
for j, tau in ((22, 0.3), (62, 10.0)):
    with open(f"{D}/rates_{j}.csv", "w") as f:
        f.write("i,T_MeV,t_s,n_PBH_alive\n")
        for i, t in enumerate(np.linspace(0, 2 * tau, 50)):
            f.write(f"{i},1,{t},{int(t <= tau)}\n")
print("DUMMY_OK")
