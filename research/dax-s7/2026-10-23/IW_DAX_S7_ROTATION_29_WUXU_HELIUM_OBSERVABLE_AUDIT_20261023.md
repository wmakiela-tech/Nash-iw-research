# DAX-S7 Rotation 29: Wu-Xu helium observable audit

Date 2026-10-23. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_BOUND.

Public main-scan.jl initializes X_n=1/(1+exp(Q/T)) and evolves it by dX_n/dt_SM=-Gamma*(X_n-(1-X_n)*exp(-Q/T)) and hadronic (1-X_n)*A-X_n*B. Hence X_n is neutron fraction n_n/(n_n+n_p). Yet its Yp is calculated as 2*X_n/(1-X_n), compared with observed 0.245 and sigma 0.003. For standard helium-4 mass fraction assuming all neutrons enter helium, Yp≈2*X_n, not 2*X_n/(1-X_n). At X_n=.12 these yield .24 vs .272727, a 13.636% difference. Target Yp=.245 corresponds to X_n=.1225 under standard convention but X_n=.245/2.245 under code formula.

Source-code mismatch verified, physical paper impact NOT verified. Cheap test: recompute Yp and chi-square from same saved X_n trajectory using both maps, check article definition, code revision and possible independent corrections. No solver rerun or bound release.
