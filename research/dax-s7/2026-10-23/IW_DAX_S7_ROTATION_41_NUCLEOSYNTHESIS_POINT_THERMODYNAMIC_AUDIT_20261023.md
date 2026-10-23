# DAX-S7 — obrót 41: audyt chłodzenia w punkcie T_nuc

Data: 2026-10-23. Status: SOURCE-TABLE VERIFIED / THERMODYNAMIC INTERPRETATION CONDITIONAL / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

## Źródło
Fenyutanchan/Primordial-Black-Hole: arXiv-2509.05618/data/ext/N_around_m_e.csv, tool_script-N_relativistic_species.jl, tool_script-parameters.jl, main-scan.jl. T_nuc=0.078185270688319950 MeV. Tablica 1000 punktów, kolumny T, g_rho, g_s; interpolacja liniowa w ln T.

## Obliczenie
T=0.07818527068831995 MeV; g_rho=3.722254946361439; g_s=4.242172521488243; r=0.4401177357589263; s=0.3590581309288303. C_code=-4+r/(3+s)=-3.868975850192498; C_ad=-3*(4+r)/(3+s)=-3.965502437909135; Delta=0.09652658771663702; |Delta/C_ad|≈2.434%. Dla adiabatycznego odniesienia reszta dln(S_comoving)/dlna=4*(r-s)/(4+r)=0.07302473461662917.

## Interpretacja i granice
Jeżeli g_s opisuje całkowitą entropię jako funkcję T_gamma, zachowanie S=a³ s_total prowadzi do C_ad również przy T_nu != T_gamma; nie wymaga to niepoprawnej tożsamości T_gamma*s_total=rho_total+p_total. Jeżeli tablice uwzględniają nieadiabatyczność, transfery lub inne efekty, wymagają osobnej kontroli. Obrót 40 odrzucił naiwny test entalpii, nie zaś automatycznie test entropii. Liczby to test pochodnych tablicy, nie pełny Julia SBBN, nie Yp i nie ograniczenia PBH. Falsyfikator: ustalić pochodzenie i definicję g_s, zweryfikować zachowanie S i source-native integrację z C_code/C_ad. Bez EXEC brak kanonizacji.
