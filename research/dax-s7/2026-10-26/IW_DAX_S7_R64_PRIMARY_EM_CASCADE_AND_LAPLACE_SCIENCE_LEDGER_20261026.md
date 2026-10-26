# IW/NASH — DAX-S7 — Obrót 64: pierwotne EM, pierwsze zderzenia, opóźnienie depozycji

Data 2026-10-26. Tryb: BOUNDED_FALSIFIER / SOURCE_TYPED / NONCANONICAL / NO_EXEC.

## Źródła i identyfikowalność
Publiczny kod Wu–Xu/BlackHawk, ścieżka arXiv-2509.05618/external_code/BlackHawk_v2.3-hack/BlackHawk_inst.c, zawiera pierwotne fotony (2 stany), elektrony i pozytony (4 stany), neutrina (6 stanów). Blob f517b0a71a3c994e396600ce73cb9658e440d646. Temperatura Hawkinga dla 9.58e9 g wynosi ~1.106 TeV, po utracie 90% masy ~11.06 TeV. W ustalonym SM i dla mas cząstek zaniedbywalnych wobec T_H pierwotne udziały gamma i e± nie zanikają wymuszenie do zera przy M_PBH→0; pojedyncza moc gatunku ma postać c_i / M². Rzeczywiste c_i nie zostały obliczone.

Uwaga: udział energii pierwotnej EM, udział EM produktów wtórnych i efektywna depozycja EM są trzema różnymi wielkościami. Publiczne źródłowe liczby hadronów nie wystarczają do pełnego bilansu ∫E d²N/dEdt.

## Niezależne testy pierwszych kontaktów w plazmie
Przy T_gamma=0.07818527068831995 MeV otrzymano n_gamma=1.51520e28 cm^-3. Całki po rozkładzie Plancka i kątach z pełnym przekrojem Breita-Wheelera oraz pierwszym rozproszeniem IC (Klein-Nishina) dają:

| E | t_first_gamma_gamma [s] | t_first_electron_IC [s] |
|---:|---:|---:|
| 1 TeV | 8.1473e-11 | 1.4465e-10 |
| 10 TeV | 6.8220e-10 | 1.2337e-9 |
| 100 TeV | 5.8674e-9 | 1.0754e-8 |
| 1 PeV | 5.1471e-8 | 9.5320e-8 |

N=210 vs N=330: maksymalna względna różnica 1.749e-5; test progu BW i limitu Thomson PASS. Są to czasy PIERWSZEGO ZDERZENIA, nie pełnej kaskady ani pełnej termalizacji. Nie wyznaczono funkcji f_EM_deposited.

## Model opóźnionej depozycji z zachowaniem energii
Dodano nietermiczny rezerwuar energii U_EM:
- d(rho_EM)/dt + 3H(rho_EM+p_EM) = U_EM/t_dep;
- dU_EM/dt + 4H U_EM = f_EM(y) Q_H - U_EM/t_dep;
- d(rho_nu)/dt + 4H rho_nu = [1-f_EM(y)] Q_H.
H obejmuje rho_EM, rho_nu, U_EM i rho_PBH.

Przy stałej masie ze środka okna obrotu 62 trzy przejścia przez T_nuc wystąpiły dla t_dep=.005s, ale znikły przy .006s. To NIE był dowód zaniku rodziny. Po ponownej optymalizacji masy potrójne przejścia powróciły:

| t_dep [s] | szerokość okna masowego [g] |
|---:|---:|
| 0 (R62) | 481219 |
| .005 | 341110 |
| .010 | 262641 |
| .050 | 19202 |
| .055 | 10182 |
| .060 | 4120 |

Przy .065s uzyskano 3 przejścia w przykładowej masie, ale nie ustalono pełnego okna; przy .075s nie wykryto lokalnego okna w sprawdzonym sąsiedztwie.

## Splot Laplace'a i warunkowe progi
Niech y=[(tau-t)/tau]^(1/3), źródło Q_H proporcjonalne y^(-2), profil końcowy f_EM(y)~f0 y^p. Relaksacja wykładnicza rezerwuaru daje [U_EM/t_dep]_evap proporcjonalne f0 Gamma((p+1)/3) t_dep^((p-2)/3). To zwykła całka Laplace'a, bez claimu nowości.

| p | wykładnik teoria | fit numeryczny (7 opóźnień) |
|---:|---:|---:|
| 0 | -.6666667 | -.6665726 |
| .5 | -.5 | -.4999523 |
| 1 | -.3333333 | -.3333121 |

R² dla każdego fitu >0.9999999998. Maksymalny względny błąd wartości wobec teorii z Gamma: 3.274e-5. Kryterium lokalnego dodatniego ogrzewania po parowaniu: U_EM/t_dep > 3H(rho_EM+p_EM). Progi w odpowiednio dostrojonych punktach: p=0: .0690254s, p=.5: .0208740s, p=1: .00294053s. Nie są to fizyczne czasy depozycji.

## Kontrole falsyfikacyjne i granice
Wewnętrzna reszta energetyczna RHS: max 6.42e-13. Niezależna reszta różnic skończonych interpolowanych stanów ODE: mediana ~9.7e-8, max 3.49e-6 (względny krok 1e-4). Brak pełnego przebiegu Julia, brak integracji widm BlackHawk, brak kaskady EM, brak nie-termicznych słabych reakcji neutronowych i ograniczeń PBH. NO_CANON / NO_EXEC / NO_NOVELTY_INFERENCE / NO_PBH_BOUND.

## Custody i cross-cell
Lokalny pełny pakiet reprodukcyjny: IW_DAX_S7_ROTATION_64_COMPLETE_REPRODUCIBLE_PACKET_20261026.zip; raport: IW_DAX_S7_ROTATION_64_PRIMARY_EM_FIRST_INTERACTION_LAPLACE_DELAY_FALSIFICATION_AUDIT_20261026.md; manifest SHA256: IW_DAX_S7_ROTATION_64_SHA256_CUSTODY_MANIFEST_20261026.json. Wewnątrz ZIP 31 plików, zweryfikowanych bajtowo. Pakiet jest lokalny, nie twierdzimy że ZIP zapisano w repozytorium.

Zamówienie do XH/MECH/INT/PRF/BW: uzyskać masowo zależne widma pierwotne i wtórne BlackHawk; podać konfiguracje grav/add_DM, energię/zakres widm, bilansować moc względem -dM/dt bez podwójnego liczenia; wyliczyć rzeczywistą czasową depozycję w EM i neutrino oraz wtórne widma; dopiero następnie ponownie sprawdzić tzw. potrójne przejścia i X_n.