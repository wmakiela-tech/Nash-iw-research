# DAX-S7 Rotation 27 — Wu–Xu initial Hubble consistency, closed by source scan

Date 2026-10-23. SOURCE-NATIVE EXACT ALGEBRA / NEGATIVE KNOWLEDGE / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_BOUND.

Source: Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/main-scan.jl: initial H_f=1/(2*t_f), rho_SM,f=3*M_Pl^2*H_f^2, rho_PBH,f=beta*rho_SM,f. Evolution uses H=sqrt((rho_SM+rho_PBH)/(3*M_Pl^2)). Therefore H_ODE,f/H_init,f=sqrt(1+beta), exactly. The difference is the radiation-dominance approximation at formation, not automatically a physical inconsistency.

CRITICAL SOURCE-MATCHED SUBTRACTION: main-scan-parameters.jl sets beta_PBH_min=1e-20, beta_PBH_max=1e-17 (100 points), M_f=6e8..1e10 g. Thus maximum initial relative H discrepancy is approximately 5e-18, negligible for this scan. Initial H anomaly alarm CLOSED; no Yp bias claimed, no numerical validation run. Large-beta examples are not relevant to the source-native scan. Future work should focus on real trajectory comparison rather than this negligible initialization residual.
