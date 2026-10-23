# IW/NASH — DAX-S7, obrót 39
## Test odporności neutronowego efektu chłodzenia na temperaturę początkową
**2026-10-23.** CONTROLLED SURROGATE / SOURCE TABLE / NO FULL JULIA / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

Source: Wu–Xu public repository Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/data/ext/N_around_m_e.csv, tool_script-parameters.jl and main-scan.jl. g_rho(T) and g_s(T) are interpolated linearly in ln T. Q=1.29333234 MeV, tau_n=878.4 s, T_nuc=0.07818527068831995 MeV, H[s^-1]≈0.2066 sqrt(g_rho)(T/MeV)^2. X_n(T0)=1/(1+exp(Q/T0)), RK4 step <=0.0004 in lnT. No PBH or full nuclear network.

r=dln(g_rho)/dlnT, s=dln(g_s)/dlnT; C_code=-4+r/(3+s), C_ad=-3(4+r)/(3+s); dt/dlnT=(4+r)/(H*C). dX_n/dt=-Gamma*(X_n-(1-X_n)exp(-Q/T))-X_n/tau_n, Gamma=(255/tau_n)*(12+6x+x²)/x^5, x=Q/T.

| T0 [MeV] | Xn code | Xn adiabatic | relative Xn drift | elapsed code [s] | elapsed ad [s] |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.101393239 | 0.102517571 | -1.09672% | 214.2103 | 208.1072 |
| 2 | 0.109036492 | 0.110253491 | -1.10382% | 214.7713 | 208.6681 |
| 5 | 0.109037390 | 0.110254396 | -1.10382% | 214.9267 | 208.8235 |
| 9 | 0.109037345 | 0.110254356 | -1.10382% | 214.9472 | 208.8440 |

At T0=5 MeV, 2*(X_code-X_ad)=-0.00243401283, elapsed-time difference ~6.10317s. Stable relative drift from 2 to 9 MeV, whereas initialization at 1 MeV changes absolute X_n due to omitted prior freeze-out history.

Limitations: approximate H, not original Julia evolution from 10 GeV; no nuclear reaction network; not published Yp or PBH bounds. Falsifier: run original SBBN with two cooling equations and matched starts; compare Xn, t and three Yp definitions. Standard BBN and thermodynamics are host theory, not novel physics.