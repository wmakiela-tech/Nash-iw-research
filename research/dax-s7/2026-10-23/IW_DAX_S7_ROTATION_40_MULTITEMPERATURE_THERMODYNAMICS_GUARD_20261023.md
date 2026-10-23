# IW/NASH — DAX-S7, obrót 40

## Niezależny test termodynamiki wielotemperaturowej
2026-10-23. SOURCE-TABLE VERIFIED / THERMODYNAMIC CAVEAT / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

Źródło: Wu–Xu Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/data/ext/N_around_m_e.csv i tool_script-N_relativistic_species.jl. Przy ~0.03 MeV: g_rho≈3.365, g_s≈3.912, zgodne z efektywnymi stopniami swobody po rozsprzężeniu neutrin.

Dla jednego płynu o wspólnej temperaturze: rho=(pi²/30)g_rho*T⁴, s=(2pi²/45)g_s*T³, rho+p=T*s, a z bilansu energii C=-4g_s/g_rho. Po rozsprzężeniu neutrin T_nu != T_gamma i nie wolno podstawiać T_gamma*s_total=rho_total+p_total; zamiast tego wkłady entalpii mają własne T_i*s_i. Stąd test C=-4g_s/g_rho jest NIELEGALNY jako niezależny test całego układu.

Liczby przy T≈0.03006 MeV: C_code≈-4.000263, C_ad≈-4.000221, C_naive=-4g_s/g_rho≈-4.649584. Rozbieżność ~0.649 nie jest dowodem błędu kodu. Przy T≈0.07814 MeV: C_code≈-3.868944, C_ad≈-3.965515, C_naive≈-4.558933.

Obroty 34–39 dają prawidłowe algebraiczne i numeryczne porównanie dwóch określonych równań chłodzenia, lecz fizyczna poprawność adiabatycznego zastępnika wymaga zbadania definicji tablic, temperatur neutrin i bilansu energii. Nie wykazano błędu opublikowanych granic PBH.

Falsification: wyprowadzić rho_i,p_i,s_i i T_nu(T_gamma), sprawdzić dot(rho)+3H(rho+p)=Q w rozdzielonych sektorach, następnie zweryfikować SBBN Julia. Host-theory subtraction; no discovery or physical upgrade.
