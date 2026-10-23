# IW/NASH — DAX-S7, obrót 45

## Próg ponownego ogrzewania i wielowartościowość Xn(T)
2026-10-23. SOURCE-NATIVE CONDITIONAL CRITERION / PBH SCAN NOT RUN / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

Sources: Wu–Xu, Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/main-scan.jl, tool_script-N_relativistic_species.jl, data/ext/N_around_m_e.csv.

Source Yp reads Xn via sortperm(Q ./ T_SM_list), LinearInterpolation(Xn_list[tmp_perm], Q ./ T_SM_list[tmp_perm]) and evaluation at Q/T_nuc, not via a specified temporal crossing.

Source cooling equation dln(rho_SM)/dln(a)=-4+r/(3+s)+I where r=dln(g_rho)/dlnT, s=dln(g_s)/dlnT, I=-dot(M_PBH)*n_PBH/(H*rho_SM)>=0 during evaporation. Since dln(rho_SM)/dlnT=4+r, dlnT/dlna=[-4+r/(3+s)+I]/(4+r). Assuming 4+r>0, reheating iff I>Icrit=4-r/(3+s). At equality derivative is zero, not necessarily multiple T_nuc crossings.

Source-table thresholds: T=1 MeV Icrit=3.988084711; .5:3.955167747; .3:3.894429645; .1:3.800898831; T_nuc=.0781852706883:3.868975850.

If T(a) is nonmonotone and T_nuc is crossed multiple times, Xn(T_nuc) can be multivalued. Sorting Q/T loses temporal branch information; duplicate x-values may violate interpolation node assumptions. Reheating alone does NOT prove multiple T_nuc crossings. No PBH scan or full Julia executor run. Falsifier: source-native compute I/Icrit, count crossings T=T_nuc, compare first/last Xn and sorted-interpolator Xn, check numerical monotonicity and interpolation validity. No physical bound or novelty inference.
