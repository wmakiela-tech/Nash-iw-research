#!/usr/bin/env python3
"""PREREG_121: synthetic inputs (arbitrary numbers, formats only) to exercise gec_b_121.py before the real run.
Usage: python3 -I dummy_121.py <dir>"""
import gzip, os, sys
import numpy as np

D = sys.argv[1]; rng = np.random.default_rng(121)
FIN = ["photon", "electron", "muon", "nue", "numu", "nutau", "pipm", "Kpm", "K0L", "proton", "neutron"]
PR = ["photon", "gluons", "higgs", "Wpm", "Z0", "electron", "muon", "tau", "up", "down", "charm", "strange", "top", "bottom"]
for t, ne, nf in (("py", 20, 40), ("hw", 10, 12)):
    os.makedirs(f"{D}/{t}", exist_ok=True)
    Ei = np.geomspace(5 if t == "py" else 25, 1e5, ne); Ef = np.geomspace(1e-6, 1e5, nf)
    for j in FIN:
        with open(f"{D}/{t}/{j}.txt", "w") as f:
            f.write(" initial_energy final_energy " + " ".join(PR) + "\n")
            for e in Ei:
                for ef in Ef:
                    f.write(f"{e:.5e} {ef:.5e} " + " ".join(f"{rng.random() * (ef < e):.5e}" for _ in PR) + "\n")
M = np.array([float(f"{x:.5e}") for x in np.geomspace(1.221e19, 1e46, 1000)])
with open(f"{D}/fcode.csv", "w") as f:
    f.write("M_GeV,M_g,T_BH_GeV,N_rho_TBH,N_BH,f_code_GeV4,m_Pl_GeV,M_Pl_GeV\n")
    for m in M:
        f.write(f"{float(m)!r},{float(m) / 5.6095886e23!r},1,1,1,1.6e74,1.22e19,2.4e18\n")
with open(f"{D}/fM.txt", "w") as f:
    f.write("   mass/a   0.00000e+000   1.00000e-003\n")
    for m in M:
        f.write(f"   {m:.5e}   9.5e73   1.0\n")
ch = ["W+-", "Z0", "bottom", "charm", "down", "electron", "gluons", "graviton", "higgs", "muon", "neutrinos", "photon", "strange", "tau", "top", "up"]
E = np.geomspace(5, 1e5, 30); ms = np.geomspace(1e9, 4e12, 6)
with gzip.open(f"{D}/prim.tsv.gz", "wt") as f:
    f.write("k\tm_g\t" + "\t".join(ch[:8]) + "\tenergy\t" + "\t".join(ch[8:]) + "\n")
    for k, mg in enumerate(ms):
        for e in E:
            v = [f"{1e20 / e ** 2 * rng.random()}" for _ in ch]
            f.write(f"{k}\t{mg}\t" + "\t".join(v[:8]) + f"\t{e}\t" + "\t".join(v[8:]) + "\n")
with open(f"{D}/auth.dat", "w") as f:
    f.write("m_PBH [GeV]\tpi\tK\tK0L\tp\tn\n")
    for mg in np.geomspace(1e9, 4e12, 6):
        f.write(f"{mg * 5.6095886e23}\t" + "\t".join(f"{rng.random() * 1e5}" for _ in range(5)) + "\n")
print("DUMMY_OK")
