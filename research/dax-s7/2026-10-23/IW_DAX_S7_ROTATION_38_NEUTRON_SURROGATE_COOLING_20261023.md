# DAX-S7 — obrót 38: kontrolowany test neutronowego skutku równania chłodzenia

**2026-10-23.** Status: SOURCE-TABLE CONTROLLED SURROGATE / NOT FULL SOURCE-NATIVE JULIA / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.

## Dane i model

Wu–Xu public repo `Fenyutanchan/Primordial-Black-Hole`, `arXiv-2509.05618/data/ext/N_around_m_e.csv`, `tool_script-parameters.jl`, `main-scan.jl`. Oryginalne `g_rho(T),g_s(T)` interpolowane liniowo w ln(T). Parametry: Q=939.5654205-938.27208816 MeV, tau_n=878.4 s, T_nuc=0.07818527068831995 MeV. Model bez PBH, od T0=1 MeV z X_n(T0)=1/(1+exp(Q/T0)); standardowe H[s^-1]~0.2066 sqrt(g_rho)*(T/MeV)^2. Wcześniejsza historia 10 GeV->1 MeV nie została rozwiązana.

Równanie neutronów zgodne z formą źródła: dX/dt=-Gamma*(X-(1-X)exp(-Q/T))-X/tau_n, Gamma=(255/tau_n)*(12+6x+x^2)/x^5, x=Q/T. Równanie czasu dt/dlnT=(4+r)/(H*C), gdzie r=dln(g_rho)/dlnT, s=dln(g_s)/dlnT, C_code=-4+r/(3+s), C_ad=-3(4+r)/(3+s). RK4 po lnT z krokiem <=0.0005, kontrola krokiem <=0.00025.

## Wyniki

| Wynik | code cooling | adiabatic cooling |
|---|---:|---:|
| elapsed time from 1 MeV | 214.2109 s | 208.1077 s |
| X_n(T_nuc) | 0.10139320 | 0.10251754 |
| 2X_n | 0.20278639 | 0.20503508 |
| 2X_n/(1-X_n) | 0.22566755 | 0.22845580 |

Kontrola podwojonej rozdzielczości: X_code=0.10139333, X_ad=0.10251764; różnice ~1e-7. Wartości bezwzględne są **surrogatem**, nie wynikami publikacji i nie służą do wyznaczania ograniczeń PBH. Względna różnica X_n ~ -1.10%, a różnica 2X_n ~ -0.002249. Nie wolno interpretować tego jako potwierdzonego błędu opublikowanego Yp.

## Ograniczenia, host theory i falsyfikator

Użyto przybliżonego współczynnika H, nie pełnego pakietu NaturalUnits; początek 1 MeV w równowadze, nie źródłowe 10 GeV; brak pełnego rozwiązania Julia, neutrinowej termodynamiki i sieci jądrowej. Równania są standardowym modelem BBN (host-theory subtraction), bez roszczenia do nowej teorii. Falsyfikator: uruchomić źródłowy SBBN z dwoma wariantami chłodzenia i wspólnymi warunkami początkowymi, porównać X_n(T_nuc) oraz t(T), a następnie osobno porównać trzy definicje Yp. Bez EXEC nie zmieniać kanonu.
