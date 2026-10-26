# IW/NASH — DAX-S7 — obrót 56: brak rozcieńczania hadronów podczas ekspansji

**Data:** 2026-10-26  
**Status:** `SOURCE_EQUATION_DISCREPANCY_CONFIRMED / FROZEN_RATE_CONTROL / FULL_JULIA_NOT_RUN / NO_CANON`.

## Źródło i falsyfikator

[main-scan.jl](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl), blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, traktuje `n_PBH=n_PBH_f*(a_f/a)^3` i `n_B=η_B*n_γ` jako fizyczne gęstości. Wszystkie sześć funkcji pochodnej gęstości hadronów w sekcji "number density of hadronss evolution" ma postać `dn_h/dt=S_h-D_h*n_h`, bez rozcieńczania `-3H*n_h`. Zakładając, że `n_h` jest fizyczną gęstością liczbową, równanie rozcieńczania stanowi `dn_h/dt+3H*n_h=S_h-D_h*n_h`.

Dla zamrożonych współczynników i kwazistacjonarnego źródła: `n_h,corrected/n_h,source=D_h/(D_h+3H)`. Względna zmiana to `ε/(1+ε)`, `ε=3H/D_h`. To nie jest ograniczenie globalne błędu Xn.

## Źródłowe wartości liczbowe

Dane `N_around_m_e.csv`, blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`; przekroje z [tool_script-parameters.jl](https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/tool_script-parameters.jl), `η_B=6.1e-10`, źródłowe (g_*(T)), radiacyjny H oraz Xn=0.12 przy próbkach.

| Gatunek | D_h [s^-1] przy Tnuc | 3H/D_h |
|---|---:|---:|
| π− | 3.8413463e7 | 1.902817e-10 |
| π+ | 3.8412840e7 | 1.902847e-10 |
| K− | 8.1028649e7 | 9.020732e-11 |
| K0L | 2.0004711e7 | 3.653828e-10 |
| antyproton | 9.9530825e3 | 7.343833e-7 |
| antyneutron | 8.0577850e3 | 9.071200e-7 |

`Tnuc=0.07818527068831995 MeV`, `Hrad=0.002436459207684 s^-1`. W przeglądzie 601 logarytmicznych temperatur w zakresie Tnuc..10 MeV × 11 wartości Xn od 0 do 1 największa **znaleziona** wartość wyniosła `3H/D=5.2898398665e-6` (piony przy 10 MeV i skrajnym Xn). Jest to maksimum **przeszukanej siatki**, nie udowodniony supremum.

## Znaczenie, ograniczenia i negatywna wiedza

1. Brak `-3H*n_h` jest strukturalną cechą źródłowych równań, ale ten lokalny test przewiduje mały wpływ dla hadronów w zakresie Tnuc..10 MeV. Inne zakresy T i pełna akumulacja Xn nie mają formalnego ograniczenia z tego oszacowania.
2. W źródłowym PBH `H=sqrt((ρ_SM+ρ_PBH)/(3 M_Pl²))` i trzeba stosować lokalne H. Ten wariant liczbowy izoluje jedynie skalę szybkości z dominacją promieniowania; pełne H sprawdza obrót 57.
3. Weryfikacja `main-scan.jl` nie jest ponownym uruchomieniem oryginalnego programu Julia.
4. Zero zmiany fizycznego kanonu, żadnych nowych limitów PBH.

**Artefakty:** `IW_DAX_S7_ROTATION_56_HADRON_DILUTION_RATE_SAMPLES_20261026.csv`, `IW_DAX_S7_ROTATION_56_HADRON_DILUTION_RATE_MAXIMA_20261026.csv`, wspólny skrypt `IW_DAX_S7_ROTATIONS_56_57_EXPANSION_DILUTION_FULL_PORT_20261026.py`. Lokalny pełny raport i odrębny skrypt kontroli szybkości dostępne również jako pliki do pobrania z rozmowy.

**Werdykt:** `MISSING_HADRON_DILUTION_CONFIRMED / SMALL_LOCAL_RATE_EFFECT / FULL_PHYSICAL_IMPACT_OPEN / NO_CANON`.
