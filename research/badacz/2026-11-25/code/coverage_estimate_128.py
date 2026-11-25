# Coverage estimate for LT11_REQ_BADACZ_001 (geometric-optics thermal spectra; NOT BlackHawk greybody).
# T_BH[GeV] = 1.058e13 / M[g]. Energy-flux fraction of primaries above E'max, fermions x^3/(e^x+1), bosons x^3/(e^x-1).
# Count fraction of j22 hadrons emitted below M for code source q ~ m^-1.2 (cumulative ~ M^1.8).
import json
from scipy.integrate import quad
import numpy as np
fd = lambda x: x**3/(np.exp(x)+1); be = lambda x: x**3/np.expm1(x)
tot_f = quad(fd, 0, np.inf)[0]; tot_b = quad(be, 0, np.inf)[0]
M22 = 6e8*(1e10/6e8)**(22/99)
out = {"M22_g": M22, "rows": []}
for Emax in (1e5, 2e6):
    for M in (1.12e9, 1e9, 5e8, 2e8, 1e8, 8e7, 5e7):
        T = 1.058e13/M; x = Emax/T
        out["rows"].append({"Emax_GeV": Emax, "M_g": M, "T_GeV": T, "x": x,
            "flux_frac_above_fermion": quad(fd, x, np.inf)[0]/tot_f,
            "flux_frac_above_boson": quad(be, x, np.inf)[0]/tot_b,
            "j22_count_frac_below_M": min(1.0, (M/M22)**1.8)})
for r in out["rows"]:
    print(f"Emax={r['Emax_GeV']:.0e} M={r['M_g']:.2e} T={r['T_GeV']:.3e} x={r['x']:.2f} fF={r['flux_frac_above_fermion']:.2e} fB={r['flux_frac_above_boson']:.2e} cnt<M={r['j22_count_frac_below_M']:.4f}")
json.dump(out, open(__import__('sys').argv[1], "w"), indent=1, allow_nan=False)
