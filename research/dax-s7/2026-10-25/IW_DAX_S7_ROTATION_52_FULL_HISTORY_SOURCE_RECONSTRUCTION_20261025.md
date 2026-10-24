# IW/NASH — DAX-S7 — obrót 52

**Data raportu:** 2026-10-25  
**Tytuł:** Odtworzenie neutronów od warunków początkowych i ograniczenie wcześniejszej interpretacji potrójnego przejścia temperatury.  
**Status:** `FULL_FORMATION_TO_NUC_SOURCE_EQUATION_RECONSTRUCTION / SIX_HADRON_FINITE_LIFETIME / OFFGRID_SINGLE_POINT / JULIA_NOT_RUN / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE`.

## 1. Kontekst i zmiana względem obrotu 51

Obroty 49–51 wyizolowały w źródłowym podukładzie tła trzy przejścia przez temperaturę nukleosyntezy dla punktu **poza źródłową siatką** `M_f=9.6725×10^9 g, β=10^-17`. W obrocie 51 początkowy stan neutronów przy pierwszym przejściu był narzucony warunkowo: `X_n(t_1)=0.11`. Obrót 52 sprawdza, czy wartość ta jest zgodna z wcześniejszą dynamiką źródłową.

### Źródła programu Wu–Xu

Repozytorium publiczne `Fenyutanchan/Primordial-Black-Hole`, katalog `arXiv-2509.05618`:

| Źródło | Git blob SHA |
|---|---|
| `main-scan.jl` | `b368ba55d5a493f7bc185909730f7fe5691f10d6` |
| `main-scan-parameters.jl` | `53faee65beda383348580c28d0424188da69b660` |
| `tool_script-parameters.jl` | `0d7198ff3557bdbd5753000bb07a7a7405cc24f5` |
| `tool_script-N_relativistic_species.jl` | `0437c032bdc4bafca6cb634c0db4cd2c46fb7efc` |
| `data/ext/N_around_m_e.csv` | `93f2494f026c5d0587ea40fe08bb938dd9d01fa8` |
| `data/ext/N_s_from_PDG2024.csv` | `33aceb876fc36cb2486d36c690e6401d85d76b46` |
| `data/ext/N_rho_OVER_N_s_from_PDG2024.csv` | `28b0c13563d7b3bdeaee191a3a981197345d05b8` |
| `data/out/hadrons_from_PBH.dat` | `06d0883a27b108692720422294ba2baacd381a64` |

Źródła są wejściem modelu; ich analiza nie stanowi niezależnego potwierdzenia praw fizycznych ani publikowanych ograniczeń PBH.

## 2. Źródłowe warunki początkowe i zakres rekonstrukcji

- Początkowe `a_f=1`, `t_f=M_f/(γ_PBH m_Pl²)` z `γ_PBH=1/(3√3)`.
- `H_f=1/(2t_f)`, `ρ_SM,f=3M_Pl²H_f²` i `T_f` z interpolatora `ρ↦T`.
- `ρ_PBH,f=βρ_SM,f`, `n_PBH,f=ρ_PBH,f/M_f`.
- `X_n,f=[1+exp(Q/T_f)]^-1`; wszystkie sześć początkowych gęstości hadronów równa się `10^-60 n_γ,f`.
- PBH traci masę według `dM/dt=-N_BH m_Pl⁴/M²`, z efektywnie stałym `N_BH≈0.007334383` przy temperaturach Hawkinga tej próbki.
- Zmienną tła jest `L=ln(g_ρ T_MeV⁴)` i `A=ln a`. Odtworzono dokładne reguły interpolacji źródłowych tablic, w tym osobną interpolację odwrotną `ρ↦T`.
- Sześć kanałów: `π−`, `π+`, `K−`, `K0L`, `p̄`, `n̄`. Ich źródłowe emisje, zaniki, anihilacje i wkłady do `dX_n/dt` zostały odtworzone; użyto **skończonych** czasów życia populacji, nie tylko równowagi natychmiastowej.
- Tło jest zgodne strukturalnie z kodem Wu–Xu. Podukład tła nie otrzymuje sprzężenia zwrotnego od `X_n` ani od hadronów, zgodnie z oryginalnym kodem.
- Integrator niezależny: RK4 dla tła (najpierw `ln(t/t_f)`, potem `y=M/M_f`), propagacja hadronów wykładnicza z dokładnym rozwiązaniem lokalnym przy stałych współczynnikach, stabilne wykładnicze propagowanie afinicznego równania neutronów, iterowane w punkcie środkowym. Po końcu parowania hadrony nadal ulegają zanikowi/anihilacji, ale brak nowych źródeł PBH.
- **Ważna naprawa względem pierwszej wersji obliczenia:** źródło emisji w ostatnim kroku masowym oceniane jest w środkowym `y`, nie przy `y≈0`. Pozwala to uniknąć sztucznego wzmocnienia przez log-log ekstrapolację `Q_h∝y^p` blisko zera.

## 3. Główny wynik liczbowy

Punkt `M_f=9.6725×10^9 g`, `β=10^-17`. Wartości zaokrąglono; reprezentatywna konfiguracja ma `N_pre=20 000`, `N_evap=30 000`, niezależny solver w JavaScript korzystający z czterech pełnych źródłowych tabel (pobranych przez GitHub). Nie był wykonywany solver Julia.

| Próg | `X_n` z hadronami | `X_n` bez źródeł hadronowych, identyczne tło |
|---|---:|---:|
| około 2 MeV | 0.34903 | 0.34912 (porównanie z biegu 14k/20k) |
| około 1 MeV | 0.25561 | 0.25455 (porównanie z biegu 14k/20k) |
| około 0.5 MeV | 0.19176 | 0.18447 (porównanie z biegu 14k/20k) |
| około 0.3 MeV | 0.18220 | 0.15870 (porównanie z biegu 14k/20k) |
| około 0.15 MeV | 0.23260 | 0.13804 (porównanie z biegu 14k/20k) |
| około 0.1 MeV | 0.30370 | 0.12265 (porównanie z biegu 14k/20k) |
| **pierwsze `T_nuc`** | **0.393202** | **0.109051** |
| **drugie `T_nuc`** | **0.393588** | **0.109049** |
| **trzecie `T_nuc`** | **0.393718** | **0.109047** |

Poszczególne próbki T różnią się nieznacznie od progów tabelarycznych; to kontrole trendu, nie porównanie dwóch trajektorii interpolowanych dokładnie do tych samych temperatur.

Zatem **narzucone `X_n(t_1)=0.11` z obrotów 50–51 nie odpowiada rekonstrukcji od warunków źródłowych przy tej wartości β**. Przed pierwszym przejściem obserwujemy skumulowaną zmianę `X_n` rzędu `+0.284` względem kontrolnego biegu bez hadronów.

**Potrójne przejście:** w przebiegu 20k/30k: `t_1≈215.05798 s`, `t_2≈215.07076 s`, `t_3≈215.08153 s`; `ΔX_n(t_1→t_3)=+0.00051609`. Jest to **około 3.7 razy mniej** od `+0.00192653` w obrocie 51 przy sztucznym `X_n(t_1)=0.11`.

## 4. Kontrola zbieżności i niezależny tryb quasi-stacjonarny

| `N_pre / N_evap` | Podejście | `X_n(t_1)` | `X_n(t_3)` | `ΔX_n` |
|---:|---|---:|---:|---:|
| 8 000 / 12 000 | pełne populacje, skończone życie | 0.39315444 | 0.39370386 | +0.00054942 |
| 14 000 / 20 000 | pełne populacje, skończone życie | 0.39317189 | 0.39371164 | +0.00053976 |
| 20 000 / 30 000 | pełne populacje, skończone życie | 0.39320177 | 0.39371787 | +0.00051609 |
| 12 000 / 18 000 | populacje quasi-stacjonarne `n=S/D` | 0.39318709 | 0.39371735 | +0.00053026 |
| 14 000 / 20 000 | źródła hadronów wyłączone | 0.10905055 | 0.10904731 | −0.00000323 |

**Interpretacja zbieżności:** wynik jakościowy i skala `X_n(t_1)≈0.393` są stabilne; czas precyzyjnego przecięcia i `ΔX_n` na bardzo krótkim epizodzie nadal zmieniają się w zauważalnym stopniu przy zagęszczaniu kroków. **Nie przypisywać dokładności sześciu cyfr do `ΔX_n`; używać rzędu `5×10^-4`.** Zbieżność w Julia i ścisła tolerancja dla przecięć: **NOT RUN**.

## 5. Gdzie zaczyna się zależność od ekstrapolacji hadronowej?

Minimalna masa PBH z tabeli emisji to `10^9 g`; dla `M_f=9.6725×10^9 g` granica odpowiada `y=10^9/M_f≈0.1034` i czasowi około `214.834 s`. Wartości przy `T≈0.1 MeV` (`t≈122.7 s`, `M_PBH≈7.30×10^9 g`) i przy `T≈0.15 MeV` dotyczą **mas PBH wewnątrz tablicy emisji**, a już wtedy `X_n` z hadronami silnie przewyższa kontrolę bez hadronów (`≈0.304` wobec `≈0.123` dla 0.1 MeV).

Zatem dominujący wzrost `X_n` **zaczyna się przed zejściem masy poza zakres tablicowy**. Końcowe wartości i zwłaszcza mikrostruktura potrójnego przejścia nadal korzystają z log-log ekstrapolacji poniżej 10^9 g i wymagają walidacji poza tym modelem.

## 6. Konsekwencja dla wielkości `Y_p` kodu

W źródle `main-scan.jl` użyto `Y_p,code=2X_n/(1-X_n)`, podczas gdy przybliżenie standardowej frakcji masowej przy natychmiastowym wychwycie neutronów to `Y_p≈2X_n`. Dla `X_n(t_1)≈0.393202`:

- `Y_p,code(t_1)≈1.29599`; `Y_p,code(t_3)≈1.29879`;
- `2X_n(t_1)≈0.78640`; `2X_n(t_3)≈0.78744`;
- `ΔY_p,code≈+0.00281`, `Δ(2X_n)≈+0.00103` dla dwóch gałęzi w powyższym przebiegu.

Wartość `Y_p,code>1` **nie może stanowić fizycznej frakcji masowej helu**. Punkt ma olbrzymią niezgodność z obserwacyjną wartością 0.245 wprost w kryterium kodu i nie jest kandydatem na punkt dopuszczalny obserwacyjnie. Nie wolno przekładać `ΔY_p,code` na korektę rzeczywistych granic PBH ani interpretować jako nowego wyniku dla helu.

## 7. Granice poznawcze, falsyfikatory i stan sprawy

1. `SOURCE_RECONSTRUCTION` oznacza niezależny port równań i danych, nie wykonanie i nie pełny readback źródłowego programu Julia.
2. W rekonstrukcji użyto operatorowego rozdzielenia układu i dyskretyzacji; źródłowy solver wykorzystuje `AutoTsit5(Rosenbrock23())`, inne adaptacyjne tolerancje i może odmiennie traktować ekstremalnie szybkie hadrony.
3. Nie badano 10 000 pełnych trajektorii neutronowych; test to jeden świadomie wybrany **punkt spoza skanu** plus kontrole schematów.
4. Otwarta pozostaje zależność od ekstrapolowanej emisji przy masie PBH poniżej `10^9 g`, a także znaczenie brakującego rozcieńczania hadronów i termodynamiki g* w fizycznym modelu.
5. **Falsyfikatorem priorytetowym** jest oryginalny Julia: uruchomienie `magic(M_f,β; dump_flag=true,hadrons_output_flag=true)` z gęstym diagnostycznym rejestrowaniem `T(a), X_n(a), n_h(a)`, bez zmiany źródłowych parametrów. Wymagane jest wykrywanie przecięć na interpolancie rozwiązania ODE, a nie wyłącznie na końcowych 10 000 punktach `a_list`, i kontrola wyboru pierwszego/ostatniego przecięcia.
6. Dodatkowy test: zmienić wyłącznie tablicowy zasięg emisji `M<10^9 g`, w sposób jawnie opisany jako perturbacja modelu, i porównać `X_n(t_1)`, liczbę przejść oraz `Y_p`.

**Werdykt:** `SOURCE_INITIAL_X_RESOLVED_IN_INDEPENDENT_RECONSTRUCTION / PRIOR_CONDITIONAL_X=0.11_NOT_SOURCE_REPRESENTATIVE / EARLY_HADRON_UPLIFT_INSIDE_TABLE / OFFGRID_TRIPLE_CROSSING_PERSISTS / ABSOLUTE_BOUNDS_UNSUPPORTED / JULIA_NOT_RUN / NO_CANON`.

## 8. Odtwarzalność

Dołączono samodzielny skrypt Python `IW_DAX_S7_ROTATION_52_FULL_HISTORY_SOURCE_RECONSTRUCTION_20261025.py`, który weryfikuje cztery źródłowe Git blob SHA i umożliwia pobranie ich opcją `--download`. Sprawdzono jego składnię i wewnętrzny `--selftest` oraz przebieg na syntetycznej tablicy stałego `g*`; **pełen bieg Python na czterech oryginalnych plikach lokalnie nie został uruchomiony**, ponieważ środowisko kontenera nie udostępnia bezpośrednio plików pobranych przez konektor GitHub. Wynik ilościowy pochodzi z niezależnego przebiegu JavaScript na pełnych danych zwróconych przez GitHub.

### Status przekazania

`DAX-S7 rotation 52 / BOUNDED SCIENTIFIC RESULT / cross-lineage ready for REC/SCOPE/KN after review / EXEC authority remains Moderator.`
