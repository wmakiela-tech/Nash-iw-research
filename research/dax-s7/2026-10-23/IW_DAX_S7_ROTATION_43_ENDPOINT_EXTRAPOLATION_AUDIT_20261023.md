# DAX-S7 — obrót 43: audyt końca integracji i ekstrapolacji

Data: 2026-10-23. SOURCE-NATIVE FORMULA AUDIT / CONDITIONAL ADIABATIC CONTROL / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

Źródła: Fenyutanchan/Primordial-Black-Hole, arXiv-2509.05618/main-scan.jl, tool_script-N_relativistic_species.jl, data/ext/N_around_m_e.csv. W kodzie a_end=10*cbrt(Nrho(Tf)*a_f³*Tf³/(Nrho(T_nuc)*T_nuc³)). Odwrotna interpolacja rho->T ma siatkę 0.01 MeV–1e6 MeV, N_around_m_e.csv zaczyna się od 0.01400299 MeV. Nrho i Ns mają ekstrapolację stałą, odwrotny interpolator liniową.

Warunkowy test bez PBH przy adiabatycznym S∝g_s T³a³, T_f=5 MeV i T_nuc=0.07818527068831995 MeV: grho_f=10.74353698, gs_f=10.74317950, grho_nuc=3.72225495, gs_nuc=4.24217252. a_end/a_f=910.5255, a_end/a_nuc=10.44557. Przy stałym gs poniżej tabeli (3.912040085) T_end≈0.00768991 MeV, poniżej obu dolnych granic. Dla T_f=1,10 MeV otrzymano ~0.00769045, ~0.00768991 MeV.

Wniosek: wybrany a_end prowadzi w kontrolnym modelu do ekstrapolacji; nie dowodzi to błędu Yp, gdyż Xn(T_nuc) odczytywany jest wcześniej. Potrzebne testy oryginalnego Julia: T_end, monotoniczność, zakres interpolacji Xn(T_nuc), wrażliwość na a_end, tolerancje i solver. Nie jest to pełny PBH executor ani fizyczne ograniczenie.
