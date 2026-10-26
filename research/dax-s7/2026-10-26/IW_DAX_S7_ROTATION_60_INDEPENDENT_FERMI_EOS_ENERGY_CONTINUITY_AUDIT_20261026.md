# IW/NASH — DAX-S7 — obrót 60

**Tytuł:** Niezależny test równania stanu Fermiego–Diraca i bilansu energii przy β=0 w publicznym kodzie Wu–Xu  
**Data:** 2026-10-26  
**Werdykt:** `BETA0_SOURCE_ENERGY_CONTINUITY_RESIDUAL_VERIFIED / FERMION_EOS_INDEPENDENT_CROSSCHECK_PASS / PAPER_EOS_MATCH_WITHIN_TABLE_INTERPOLATION / FULL_JULIA_NOT_AVAILABLE / NO_EXEC / NO_CANON`  
**Granica twierdzenia:** wykryto niespójność lokalnych równań źródłowych z zachowaniem energii przy β=0 w konkretnym modelu idealnego gazu z dodatku A; bez ustalania nowej granicy PBH, bez pełnego solvera Julia.

## 1. Pytanie falsyfikacyjne i realizacja

Obrót 59 ujawnił, że `main-scan.jl` przy β=0 nie zachowuje współporuszającej entropii z równania (2.7) publikacji. Potencjalnym kontrargumentem było to, że tablice `g_rho(T_gamma)` i `g_s(T_gamma)` zawierają neutrina o osobnej temperaturze; równość entropii pojedynczego płynu może wówczas wymagać dodatkowego uzasadnienia. Obrót 60 **nie zakłada** relacji entropijnej w głównym teście: wyprowadza ciśnienie i energię **niezależnie** z całek Fermiego–Diraca dla elektronów/pozytonów oraz fotonów i masywnych termicznie (lecz traktowanych jako bezmasowe kinematycznie) neutrin rozsprzęgniętych, jak w dodatku A autorów. Dopiero po tej rekonstrukcji kontroluje równanie zachowania `dot(rho)+3H(rho+p)=0` bez PBH.

**Ograniczenie środowiska:** na wykonawczym serwerze nie zainstalowano `julia`, a publicznych zależności solvera nie pobrano. Wykonano realny test Python+SciPy na **13 źródłowo wyznaczonych w obrocie 59 punktach**, a nie ponowne uruchomienie oryginalnego `magic(m,0)` ani ponowny odczyt pełnych 1000 punktów tabeli do procesu Pythona. Pełny 1000-punktowy wektor interpolacji i kwadraturę sprawdzono odrębnie w obrocie 59 przez podłączone źródło. Przygotowano ponadto **niewykonany jeszcze** samodzielny mikrotest Julia, nie wymagający innych pakietów niż standardowe biblioteki.

## 2. Ściśle określone źródła

1. **Tekst autorów:** Quan-feng Wu, Xun-Jie Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, `arXiv:2509.05618v3`, https://arxiv.org/html/2509.05618v3 — (2.7), (A.1)–(A.4), z osobnymi temperaturami fotonów i neutrin.
2. **Główne równanie w publicznym kodzie:** `arXiv-2509.05618/main-scan.jl`, https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl , Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, równanie `d_log_ρ_SM_dη = -4 + r/(3+s) - dotM*nPBH/(H*rho_SM)`.
3. **Definicja tablic:** `tool_script-N_relativistic_species.jl`, Git blob `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc`.
4. **Oryginalna tabela:** `data/ext/N_around_m_e.csv`, Git blob `93f2494f026c5d0587ea40fe08bb938dd9d01fa8`, 1000 wierszy. Dla Pythona tego obrotu wejściem jest wynikowy CSV z obrotu 59 `IW_DAX_S7_ROTATION_59_PAPER_CODE_NEUTRINO_ENTROPY_COMPARISON_20261026.csv` (13 temperatur) — blob tej lokalnej migawki `a1934e09b02d797a7b759510da99b10e1facfa97`.

## 3. Niezależny bilans energii — bez założenia zachowania entropii

Dla `g_{e±}=4` i `y=m_e/T_gamma` obliczono całki:

\[
I_\rho(y)=\int_0^\infty\frac{x^2\sqrt{x^2+y^2}}{e^{\sqrt{x^2+y^2}}+1}\,dx,
\qquad I_p(y)=\int_0^\infty\frac{x^4}{\sqrt{x^2+y^2}(e^{\sqrt{x^2+y^2}}+1)}\,dx.
\]

Wkłady par elektron–pozyton do współczynników wynoszą:

\[
g_{\rho,e}=\frac{15g_e}{\pi^4}I_\rho,\quad
 g_{p,e}=\frac{5g_e}{\pi^4}I_p,\quad
 g_{s,e}=\frac{45g_e}{4\pi^4}\left(I_\rho+\frac{I_p}{3}\right).
\]

Z tablicowego `g_rho` i `g_s` otrzymuje się **dwa niezależne estymatory** `q=T_nu/T_gamma` przy `g_nu=5.25`:

\[
q_\rho=\left(\frac{g_\rho-2-g_{\rho,e}}{5.25}\right)^{1/4},\qquad
q_s=\left(\frac{g_s-2-g_{s,e}}{5.25}\right)^{1/3}.
\]

Ich zgodność testuje spójność fizyczną tablicy, a nie samą dynamikę czasową. Następnie:

\[
g_p=\frac{2+5.25q_\rho^4}{3}+g_{p,e},\quad
C_{\rm EOS}=-3\left(1+\frac{g_p}{g_\rho}\right).
\]

Równanie ciągłości FLRW przy β=0 ma postać `dln(rho)/dln(a)=C_EOS`. Jego **bezwymiarowa reszta**:

\[
\mathcal R_E=\frac{\dot\rho+3H(\rho+p)}{H\rho}
=C_{\rm badany}+3\left(1+\frac{g_p}{g_\rho}\right)
=C_{\rm badany}-C_{\rm EOS}.
\]

Oceniono ją dla `C_code=-4+r/(3+s)` i niezależnie `C_paper=-3(4+r)/(3+s)`, korzystając z tablicowych pochodnych `r,s` obliczonych w obrocie 59.

## 4. Główne wyniki liczbowe

W temperaturze nukleosyntezy `T_nuc=0.07818527068831995 MeV`:

| Wielkość | Wartość |
|---|---:|
| `g_rho` / `g_s` | `3.722254946361439` / `4.242172521488243` |
| `g_rho,e±` / `g_s,e±` | `0.20219764183587` / `0.16996009837017` |
| `g_pressure,e±` | `0.02441582265768` |
| `q_rho` | `0.73354230280409` |
| `q_s` | `0.73354200814787` |
| **`q_rho-q_s`** | **`2.947e−7`** |
| `C_EOS` z ciśnienia | **`−3.96535697427`** |
| `C_paper` z (2.7) | `−3.96550243791` |
| `C_code` z `main-scan.jl` | `−3.86897585019` |
| **`R_E(code)`** | **`+0.09638112408`** |
| `R_E(paper)` | `−0.00014546363` |
| **`R_E(code)/4`** | **`2.4095281%`** |

Na 13 źródłowych temperaturach maksimum `|q_rho-q_s|` wynosi `2.947e−7`, a maksimum `|R_E(paper)|=1.5334e−4` — zgodne z dokładnością tablic/interpolacji i modelu zerowej korekty elektromagnetycznej. **Równanie kodu daje natomiast resztę +0.13086606457 przy 0.1 MeV**, czyli około `3.27165%` skali `4Hrho`. Brakujący człon energetyczny występuje *bez PBH* i ma lokalnie dodatni znak w okresie anihilacji elektron–pozyton. Nie utożsamiać go z fizycznym strumieniem promieniowania PBH.

## 5. Odniesienie do obrotu 59 i ostrożna interpretacja

W obrocie 59, całkując źródłowe `C_code` między 10 MeV a `T_nuc`, uzyskano `S_com(T_nuc)/S_com(10MeV)=1.1467816334`, podczas gdy relacja (2.7) wymaga 1. Ta wcześniejsza analiza może być obecnie skonfrontowana z **niezależną zasadą zachowania energii**, niewymagającą bezpośredniego założenia o całkowitej entropii. Na tym samym zestawie tablic `C_paper` ma resztę w bilansie energii ≤`1.54e−4`; `C_code` osiąga `~0.13`. To wzmacnia diagnozę o błędnym kontrakcie równania chłodzenia względem modelu opisanego w tekście autorów.

**Uściślenie:** `q_rho` oraz `q_s` są parametrami *zakodowanymi przez tablice*, nie temperaturami dynamicznie obliczanymi przez `main-scan.jl`. `q_source` z obrotu 59 był tylko hipotetyczną konsekwencją dołączenia osobno warunku `T_nu a=const` do trajektorii źródłowej. Nie należy nazywać go bezpośrednią prognozą neutrin z Julii.

Istotny negatywny wynik: na tej podstawie **nie wolno** wyznaczać poprawki do `Y_p` ani nowych ograniczeń PBH, bo kod wymaga pełnej integracji dla rzeczywistych warunków początkowych i emisji, a dwusektorowy wtrysk energii PBH pozostaje nieodtworzony. Nie zakładamy, że prosta jednopłynowa poprawka zachowania entropii automatycznie przenosi się na `β>0`.

## 6. Testy, odtwarzalność i kolejny falsyfikator

**Wykonano naprawdę:**
- Python/SciPy z całkami dla e±, 13 punktów źródłowo wyznaczonych w R59;
- sprawdzenie `g_rho,e→3.5`, `g_p,e→3.5/3`, `g_s,e→3.5` przy wysokiej temperaturze i zaniku e± przy niskiej;
- testy `q_rho≈q_s`, papierowy bilans energii `|R_E|<2e−4` oraz istotna reszta źródłowa przy `T_nuc`;
- zapis tabeli wynikowej i JSON z provenance.

**Nie wykonano:** oryginalnej Julii (`julia` nieobecna w środowisku), nie załadowano 1000 oryginalnych wierszy CSV do lokalnego programu Python w tym obrocie, nie rozwiązywano równania PBH dla `β>0`.

**Dostarczony test Julia:** samodzielny `IW_DAX_S7_ROTATION_60_JULIA_BETA0_ENTROPY_MICROHARNESS_20261026.jl` potrafi, w środowisku z Julia, odczytać oryginalne 1000 wierszy ze sprawdzonym Git blob SHA i odtworzyć całkę źródłową `ln a` oraz `S_com` **bez zależności solvera**. To przygotowany falsyfikator, ale **nie uruchomiono go w tej sesji**. Najsilniejszy dalszy test: oryginalne `magic(m,β=0)` z jawnym zapisem `rho`, `T_gamma`, `a`, `g_s`, następnie test bilansu `R_E` w trakcie anihilacji e± z ciśnieniem wyliczonym w obrocie 60.

**Werdykt:** `PAPER_CODE_AND_PHYSICAL_EOS_MISMATCH_CONFIRMED_FOR_BETA0 / INDEPENDENT_PRESSURE_INTEGRALS_PASS / NUMERICALLY_LOCAL / FULL_JULIA_PENDING / NO_EXEC / NO_CANON`.
