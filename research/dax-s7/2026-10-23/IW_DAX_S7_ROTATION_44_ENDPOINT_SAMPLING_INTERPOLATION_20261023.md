# DAX-S7 — rotation 44: endpoint sampling interpolation audit

2026-10-23. CONTROLLED SURROGATE / SOURCE-TABLE / NO FULL JULIA / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

Source: Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/main-scan.jl, tool_script-N_relativistic_species.jl, data/ext/N_around_m_e.csv.

Model: no PBH; T0=5 MeV, T_nuc=0.07818527068831995 MeV; original neutron weak rate and decay; H≈0.2066 sqrt(g_rho)*(T/MeV)^2 s^-1. RK4 in lnT over 24000 steps from 5 to 0.0141 MeV, both C_code=-4+r/(3+s) and C_ad=-3(4+r)/(3+s). Reconstructed ln(a) and simulated geometric sampling in a, followed by linear interpolation of X_n in x=Q/T. Sampling a_end multiplied by 1, 2, 10; N=100, 1000, 10000.

Dense reference X_code=0.10903745750, X_ad=0.11025444862. Maximum absolute interpolation errors across both cooling modes and endpoint multipliers: N=100: 5.283e-6; N=1000: 9.607e-8; N=10000: 2.107e-9. N=10000 and endpoint multipliers 1/2/10: code errors +9.09e-10/-1.41e-9/-2.11e-9; ad errors +1.00e-9/-9.12e-10/-1.88e-9.

For an exact IVP, extending integration past target cannot alter prior solution. Endpoint changes sampling spacing, but this is tiny for 10000 samples in this controlled model. Not a proof about adaptive Julia solver, PBH reheating, or possible nonmonotonic T(a). Falsifier: original Julia with endpoint multipliers, tolerance controls, solver status, and monotonicity checks. No physical PBH bound.
