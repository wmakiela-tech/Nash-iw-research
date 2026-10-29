# IW/NASH — DAX-S7 — obrót 68: konkurencyjne kanały kaskady i identyfikowalność neutrin

**Data:** 2026-10-29. **Status:** `BOUNDED_COMPETING_CHANNEL_AUDIT / NO_EXEC / NO_CANON / NO_PBH_BOUND`.

## 1. Teza i istotna korekta perspektywy

Włączenie całkowitego przekroju produkcji dwóch par elektronowych (`DPP`):
`gamma gamma -> e+ e- e+ e-` bez wiarygodnego rozkładu różniczkowego **nie** tworzy pełnego fizycznego operatora kaskady. Zależność wyników od czterech ułamków energii jest duża, a kanały mionowe i potrójna produkcja par w zderzeniach e-gamma muszą być rozdzielone na *liczbę reakcji*, *stratę energii*, *opóźniony rozpad* i *depozycję termiczną*.

Wszystkie liczby używają **stałej** temperatury fotonów `Tgamma=0.07818527068831995 MeV` ze starszych kontroli DAX, nie rzeczywistej ewolucji Tgamma w czasie PBH.

## 2. Status źródeł i operatorów

| Kanał | Operator w R68 | Status i ograniczenie |
|---|---|---|
| `gamma gamma -> e+e-` (BW) | Przekrój i rozkład różniczkowy QED ze zamrożonego R67 | Traktowanie pierwotnych fotonów tła Plancka; poprawka R65 czynnika kątowego 1/2 zachowana |
| `gamma gamma -> 2(e+e-)` (DPP) | Opublikowana **wysokoenergetyczna asymptota przekroju całkowitego**, konkurujące ryzyko zdarzeń | Brak zidentyfikowanego różniczkowego rozkładu czterech leptonów w danych Wu–Xu; pięć jawnych profili *sztucznych* |
| `gamma gamma -> mu+mu-` | Pełny przekrój Breit–Wheelera z masą miona; całka po Plancku i kątach | Zdarzenie oznaczono jako `muon_opportunity`, **nie** natychmiastowe neutrina i nie depozycja |
| `e gamma -> e gamma` (IC) | Z zamrożonego R67 jądro Blumenthala–Goulda | Elektron nie ma w R68 innych strat energii |
| `e gamma -> e e+e-` (TPP) | Tylko wysokoenergetyczny **całkowity** przekrój Haug/Borsellino, oraz literaturowe przybliżenie strat | **Nie dołączono** jako zdarzenia do symulacji, ponieważ brak właściwego różniczkowego transferu energii; częstość zdarzeń ≠ tempo chłodzenia elektronu |

Ważny negatywny filtr: przekroje `gamma+atom -> muons` i `gamma+electron -> muons` z Geant4 **nie są** przekrojami `gamma+gamma -> mu+mu-` i nie wolno używać ich zamiast niego.

## 3. Szybkości pierwszego zdarzenia, wspólna kąpiel termiczna

Wszystkie liczby pochodzą z niezależnego całkowania przekrojów z właściwą średnią kątową (1/2); `DPP` jest tylko wysokonergetyczną asymptotą:

| E_gamma [GeV] | P(DPP) | P(muons) | Gamma(BW) [s^-1] | Gamma(DPP) [s^-1] | Gamma(mu) [s^-1] |
|---:|---:|---:|---:|---:|---:|
| 100 | 5.507% | 1.433% | 4.946e+10 | 2.927e+09 | 7.617e+08 |
| 1,000 | 29.565% | 8.451% | 6.137e+09 | 2.927e+09 | 8.367e+08 |
| 10,000 | 76.036% | 4.927% | 7.329e+08 | 2.927e+09 | 1.897e+08 |
| 1,000,000 | 99.527% | 0.143% | 9.714e+06 | 2.927e+09 | 4.198e+06 |

Przy 1 TeV: `P_mu=0.08450699` i `P_DPP=0.29565499`, **warunkowo na trzech kanałach**. Nie ma tu procesów hadronowych, plazmowych ani TPP (TPP dotyczy elektronu, nie fotonu); procenty NIE są frakcjami energii do neutrin.

## 4. Sztuczne profile energii czterech produktów DPP

W każdym zdarzeniu DPP cztery ułamki `f_i>=0` sumują się dokładnie do 1. W modelu jednej losowo wybranej porcji energii kolejny lepton jest wybierany proporcjonalnie do `f_i`. To próbka *energy-biased lineage*, nie cztery rozgałęzienia i nie pełna kaskada.

- `equal4` — 25% na cząstkę, efektywny zachowany udział drugiego momentu `sum f_i²=0.25`.
- `Dirichlet(alpha=4)` — skoncentrowany wokół równego podziału, `E[sum f_i²]=5/17`.
- `Dirichlet(alpha=1)` — jednorodny simpleks, `E[sum f_i²]=0.4`.
- `Dirichlet(alpha=0.15)` — rozkład silnie asymetryczny, `E[sum f_i²]=0.71875`.
- `leading95` — jeden produkt ma 95%, trzy pozostałe po 1.667%, `sum f_i²=0.903333...`.

**Żaden z nich nie został utożsamiony z różniczkowym przekrojem QED czterech leptonów.** Dla 20 000 prób na profil maksymalna różnica średniej drugiego momentu względem wzoru analitycznego wyniosła `0.00142576`.

## 5. Uwarunkowane trajektorie w modelu jednej porcji energii

Symulacja: 32 konfiguracje, po 750 prób każda = 24 000 trajektorii głównych. Zdarzenie mionowe oznacza zatrzymanie jako `UNRESOLVED_MUON_OPPORTUNITY`; zejście poniżej 0.1 GeV oznacza `BELOW_CUT_NOT_DEPOSITION`. Kolumna `p_mu` to odsetek wybranych porcji energii, które napotkały kanał mionowy przed przejściem poniżej odcięcia; **nie** jest to utracona na neutrina część energii.

| E_initial [GeV] | Profil DPP | Mediana czasu wyjścia [s] | p90 [s] | p_mu | Średnia liczba DPP |
|---:|---|---:|---:|---:|---:|
| 1e+03 | `equal4` | 8.324e-10 | 1.995e-09 | 0.273 | 1.05 |
| 1e+03 | `dirichlet_a1` | 1.028e-09 | 2.406e-09 | 0.279 | 1.19 |
| 1e+03 | `dirichlet_a0p15` | 1.308e-09 | 3.012e-09 | 0.411 | 1.41 |
| 1e+03 | `leading95` | 1.637e-09 | 3.714e-09 | 0.456 | 1.66 |
| 1e+06 | `equal4` | 5.895e-08 | 1.4e-07 | 0.383 | 5.18 |
| 1e+06 | `dirichlet_a1` | 9.555e-08 | 3.16e-07 | 0.432 | 6.21 |
| 1e+06 | `dirichlet_a0p15` | 3.901e-07 | 9.632e-07 | 0.555 | 11.09 |
| 1e+06 | `leading95` | 1.094e-06 | 2.23e-06 | 0.583 | 17.50 |
| 1e+09 | `equal4` | 4.254e-05 | 0.0001045 | 0.391 | 9.84 |
| 1e+09 | `dirichlet_a1` | 7.026e-05 | 0.0002182 | 0.427 | 12.21 |
| 1e+09 | `dirichlet_a0p15` | 0.000276 | 0.0007 | 0.549 | 23.13 |
| 1e+09 | `leading95` | 0.0008876 | 0.001837 | 0.581 | 37.61 |
| 1e+12 | `equal4` | 0.03187 | 0.08015 | 0.408 | 14.54 |
| 1e+12 | `dirichlet_a1` | 0.05848 | 0.1706 | 0.461 | 18.08 |
| 1e+12 | `dirichlet_a0p15` | 0.2224 | 0.5923 | 0.536 | 36.09 |
| 1e+12 | `leading95` | 0.7497 | 1.536 | 0.572 | 59.80 |

W punkcie `E=1e12 GeV` mediany czasu wyjścia z **tego ograniczonego modelu** obejmują `0.0319–0.75 s`, zależnie od przyjętego sztucznego podziału energii. Nie można wyznaczyć fizycznego czasu termalizacji z tych liczb, a pominięte TPP mogą zasadniczo zmienić elektronową część trajektorii.

Kontrole: zero niedokończonych trajektorii (`maxevents=1200`) w głównej macierzy; 24 dodatkowe kontrole przy Nquad=54/84/105, grid=85/130/155, dwóch niezależnych ziarnach MC i 500 próbach na wariant. Zależność jakościowa i porządek wyników są stabilne; **numeryczna mediana przy E=1e12 nadal wykazuje losowy rozrzut na poziomie ~8% CV**, więc nie ma podstaw do interpretacji kilku cyfr znaczących.

## 6. TPP: zdarzenie vs utrata energii

Asymptota całkowitego przekroju TPP:

`sigma_TPP ~ alpha * r_e² * [(28/9)ln(2k) - 218/27]`, `k=E_e epsilon (1-cos theta)/m_e²`, dla wysokich k (tu w praktyce `k>1e4`).

| E_electron [GeV] | Gamma_TPP / Gamma_IC (Planck, całkowite zdarzenia) | q_TPP / q_ICS (MONO 2.701T, reprezentatywny kąt) |
|---:|---:|---:|
| 1e+03 | 2,761.1 | 0.512 |
| 1e+05 | 286,458.9 | 0.924 |
| 1e+06 | 2,898,443.4 | 1.175 |
| 1e+09 | 2,965,574,293.6 | 2.106 |

Trzeba ściśle oddzielić te wielkości. Drugie przybliżenie wykorzystuje `q_TPP=0.386 alpha [ln(2k)]²[ln(2k)-218/84]`, `q_ICS=ln(4k)-11/6`. Próg równości w tym **tylko** monochromatycznym przybliżeniu: `k*=1.6757185691e8`, `E_e*=207201 GeV` przy `epsilon=2.701T, a=1`. Wartości q nie są wynikiem wykonania pełnej całki strat nad Planckiem.

Oznacza to, że pomijanie TPP w **stratach energii** przy ekstremalnych energiach nie jest małą perturbacją udowodnioną przez model. Bez różniczkowego operatora TPP nie ma wiarygodnego czasu kaskady.

## 7. Miony: opóźniony kanał neutrinowy

Przy pierwotnym `gamma gamma -> mu+mu-` neutralna część energii pojawia się wskutek dalszych reakcji i rozpadów, a nie w punkcie produkcji pary. Prostą kontrolą jest średni czas rozpadu przy założeniu `E_mu≈E_gamma/2` bez strat mionu:

`tau_lab = tau_mu * (E_gamma/2m_mu)`, `tau_mu=2.1969811e-6 s`, `m_mu=0.1056583755 GeV`.

Przy 1 TeV `tau_lab=0.01039663 s`, dłużej niż 3 ms analizowane w R64; przy 10 TeV `tau_lab≈0.104 s`. **To kontrola latencji rozpadu, nie model fizycznego przeżycia mionu**, który może wcześniej tracić energię i oddziaływać z tłem.

Wniosek: utożsamianie `P(muon event)` z `f_neutrino` albo z natychmiastowym zniknięciem energii z układu jest niedopuszczalne.

## 8. Werdykt i plan falsyfikacji

**Zamknięte lokalnie:** QED muon pair total rates w Plancku, asymptota DPP jako competing hazard, matematyczna normalizacja czterech ułamków, analityczny drugi moment Dirichleta, kontrola całkowitych zdarzeń TPP i wyraźne oznaczenie granicy modelu.

**Otwarte i blokujące:** (i) pełny różniczkowy operator DPP dla 4 leptonów (QED / zweryfikowany generator); (ii) energetyczny operator TPP, nie tylko całkowity przekrój; (iii) los mionów, ich straty i kanały neutrinowe, przy wtrysku zmiennym w czasie; (iv) inne procesy, hadrony i przejścia między sektorami; (v) pełne widma BlackHawk i oryginalny solver Julia; (vi) sprzężenie z plazmą BBN.

**Nie wolno stwierdzać:** fizycznego czasu depozycji, rzeczywistego `f_EM(M,t)`, nowej granicy PBH, odkrycia nowego prawa fizycznego ani wykonania oryginalnej Julii/BlackHawk.

**Proponowane testy następne:**
1. `DPP differential`: uzyskać niezależną macierz elementów / kod 4-leptonowy, walidować całkę po fazie przestrzennej do stałej asymptotycznej, zachowanie energii i sprawdzać profile podziału.
2. `TPP differential`: użyć Anguelov et al 1999/2000; porównać moment strat i całkowity przekrój przy k=1e4,1e6,1e8,1e10; obliczyć Planck+angle full loss.
3. `Muon transfer`: porównać rozpad, IC i produkcję wtórną dla propagujących mionów, z bilansem energii EM/neutrino/nonthermal.
4. `Real spectra`: dopiero po operatorze transportu wstrzyknąć widmo Hawkinga z kontrolą pełnej mocy i depozycji.

## 9. Źródła, provenance

- Public source Wu–Xu: https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/main/arXiv-2509.05618 (nie uruchomiono solvera).
- Frozen R67 kernel: `R67_FROZEN_EXACT_DIFFERENTIAL_BW_CASCADE_20261029.py` — oryginalny kod w zestawie lokalnym, niezmieniony.
- C. Carimalo, W. da Silva, F. Kapusta, *Towards a complete gamma gamma -> 4 leptons Monte Carlo* (1999), https://arxiv.org/abs/hep-ph/9909339 — materialny problem różniczkowego rozkładu wielociałowego.
- A. F. Esmaeili et al., *Ultrahigh energy neutrinos from high-redshift electromagnetic cascades*, Phys. Rev. D 106, 123016 (2022), https://doi.org/10.1103/PhysRevD.106.123016 — DPP i miony w kaskadzie.
- V. Anguelov et al., *On the numerical analysis of triplet pair production ...*, J. Phys. G 25, 1733–1747 (1999), https://arxiv.org/abs/astro-ph/0001252 — TPP z rozdzieleniem przekroju i momentu strat.
- A. Mastichiadis, *Relativistic electrons in photon fields: effects of triplet pair production ...*, MNRAS 253, 235–244 (1991), https://doi.org/10.1093/mnras/253.2.235 .

**Werdykt:** `DPP_TOTAL_HAZARD_PASS_CONDITIONALLY / FOUR_LEPTON_ENERGY_KERNEL_NOT_IDENTIFIED / DIRECT_MUON_CHANNEL_QUANTIFIED / MUON_DECAY_LATENCY_OPEN / TPP_EVENTS_NOT_LOSSES / TPP_LOSS_IMPORTANCE_SUPPORTED_BY_LITERATURE / NO_EXEC / NO_CANON / NO_PBH_BOUND`.