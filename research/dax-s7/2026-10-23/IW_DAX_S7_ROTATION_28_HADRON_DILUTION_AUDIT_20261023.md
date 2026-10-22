# IW/NASH DAX-S7 rotation 28: hadron cosmological dilution audit
Date 2026-10-23. SOURCE-CODE RESIDUAL VERIFIED / PHYSICAL SIGNIFICANCE OPEN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_BOUND.

Source: Fenyutanchan/Primordial-Black-Hole arXiv-2509.05618/main-scan.jl and tool_script-parameters.jl, inspected 2026-10-23.

The public executor uses n_PBH=n_PBH_ini*(a_ini/a)^3, sources S_h=(dN_h/dt)(M)*n_PBH and baryon physical density n_B=eta_B*n_gamma(T). Its six hadron RHS have dn_h/dt=S_h-D_h*n_h, without -3H*n_h. For physical hadron number densities, the FLRW balance is dn_h/dt+3H*n_h=S_h-D_h*n_h. Thus omission of the explicit dilution term is source-code verifiable, but impact on Yp is untested.

For locally frozen coefficients, n_code=S/D and n_diluted=S/(D+3H); fractional overestimate relative to corrected state is 3H/D. Illustrative estimate using eta_B=6.1e-10, sigma*v ~ 30mb*c, n_gamma(T)=410.7*(T/T_CMB)^3 cm^-3 and H~0.68*(T/MeV)^2 /s yields 3H/D~1.17e-7 at 1 MeV, ~1.17e-6 at 0.1 MeV, ~1.17e-5 at 0.01 MeV. These are order-of-magnitude examples, not executor-native numerical bounds. Meson decay further increases D.

Cheapest falsifier: extract source-native H(t), D_h(t), n_h(t), A(t), B(t), check 3H/D_h and rerun six hadron ODE with -3H*n_h under same background and floor logic, then compare X_n and Yp. Julia/full rerun NOT RUN. Mature host: standard FLRW Boltzmann dilution. No PBH endpoint claim.
