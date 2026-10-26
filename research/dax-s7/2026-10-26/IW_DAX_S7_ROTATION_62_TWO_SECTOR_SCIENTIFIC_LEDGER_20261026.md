# DAX-S7 rotation 62 — Two-sector PBH energy-deposition conditional falsifier

Date: 2026-10-26. Status: CONDITIONAL_TWO_SECTOR_TRIPLE_CROSSING_SUPPORTED / FOLD_SCALING_3_OVER_2 / NO_FULL_JULIA / NO_EXEC / NO_CANON / NO_PBH_BOUND.

## Source and method
Wu & Xu, arXiv:2509.05618v3, section 3: https://arxiv.org/html/2509.05618v3; GitHub source main-scan.jl blob b368ba55d5a493f7bc185909730f7fe5691f10d6. The authors do NOT determine the physical EM vs neutrino Hawking deposition fraction. Independent moment-closure test, NOT full source Julia or BBN:
dot(rho_EM)+3H(rho_EM+p_EM)=f_EM Q_PBH;
dot(rho_nu)+4H rho_nu=(1-f_EM)Q_PBH;
dot(rho_PBH)+3H rho_PBH=-Q_PBH.
Photons plus e± pressure and energy from independent Fermi–Dirac quadratures (PCHIP EOS). rho_nu=(pi²/30)*5.25*Tnu_eff^4; effective neutrino T is an ENERGY MOMENT ONLY, NOT a thermalized Hawking-neutrino distribution. Fixed test T_dec=2 MeV, beta=1e-17, T_nuc=0.07818527068831995 MeV; early pre-decoupling PBH injection neglected, instantaneous decoupling assumed. Mass lifetime uses the high-temperature Hawking source coefficient. These are conditional modelling assumptions, not physical calibration.

Use y=M_PBH/M_initial as integration variable to regularize the evaporation endpoint:
dR_EM/dy=9*tau*y²*H*(R_EM+P_EM)-f_EM*D;
dR_nu/dy=12*tau*y²*H*R_nu-(1-f_EM)*D;
dln(a)/dy=-3*tau*y²*H.
Here D=D_dec exp(-3 ln(a/a_dec)) is the initial-PBH-mass-weighted comoving density.

## Primary findings
A broad initial 10-mass × 5-fraction scan produced ONE T_nuc crossing per case. It missed an extremely narrow region: after bracketing the local EM-temperature minimum and the EM-temperature at evaporation, FIVE positive fractions yield THREE crossings:
| f_EM | lower mass g | upper mass g | width g |
|:--|--:|--:|--:|
| 0.10 | 9569954777 | 9569970113 | 15336 |
| 0.25 | 9572105539 | 9572166080 | 60541 |
| 0.50 | 9575651483 | 9575822350 | 170866 |
| 0.75 | 9579160808 | 9579474036 | 313228 |
| 1.00 | 9582639930 | 9583121149 | 481219 |

At f_EM=0 the EM sector has no direct PBH heating and is monotone (no triple crossing). Mid-window for f=1: M=9582880539 g, crossings at t=209.092571, 209.148492 and 209.164884 s.

Measured width: Delta(M) proportional to f_EM^(1.496753874), log-log fit R²=0.999999548. Near end-of-evaporation dR_EM/dy≈A y²-fD (A>0), which implies y_min=sqrt(fD/A) and R_EM(0)-R_EM(y_min)≈(2/3)(fD)^(3/2)/sqrt(A). Smooth mass dependence implies window width proportional to f_EM^(3/2). This is a standard local asymptotic mechanism, NOT a novelty claim or new physical discovery.

## Controls
Nine resolution tests at f_EM=.1,.5,1 retain three crossings. Finite-difference total-energy continuity residual ≤6.1e-8 (normalized), direct ODE-substitution residual ≤2.2e-14. At f_EM=0, comoving EM entropy conserved to ~1.6e-7; at f_EM=1, Tnu_eff*a conserved to ~4e-12. Physical mass-window location depends on assumed instant neutrino decoupling temperature: for f=1 middle mass is ~9.57084e9 (1 MeV), 9.58288e9 (2 MeV) and 9.58512e9 g (3 MeV).

The independently calculated gamma scale-factor spans for triple crossings are much narrower than original source-output sampling (particularly for small f_EM), so X_n(T) aliasing requires direct chronological source-solver testing.

## Forbidden inference
No true f_EM(M,t), no spectral neutrino transport, no n↔p nonthermal rates, no 6-hadron/full BBN integration, no original Julia execution, no revised PBH bounds, no EXEC and no canon upgrade. Source paper's section 3 states the actual fraction going to neutrinos is complicated by secondary production. Do not convert these toy mass windows into published constraints or evidence of new PBH physics.

FULL self-contained original source files, local Python scripts, 50-row sweep, 5 windows, convergence/residual controls, output JSON, and SHA manifest were archived as IW_DAX_S7_ROTATION_62_REPRODUCIBLE_PACKET_20261026.zip in the DAX-S7 conversation workspace. The linked GitHub entry is a scientific readback ledger, not a full binary copy of the ZIP.
