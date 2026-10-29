# IW/NASH — DAX-S7 — Obrót 66: energetycznie ważona gałąź kaskady γγ/IC

**Data:** 2026-10-29. **Funkcja:** niezależna falsyfikacja dotychczasowych przybliżeń transportu energii po PBH.  
**Status:** `CONDITIONAL_BRANCHING_TRANSPORT_PROXY / SOURCE_TYPED / NO_EXEC / NO_CANON / NO_PHYSICAL_PBH_BOUND`.

## 1. Problem
Obrót 64 wykazał szybkie pierwsze zderzenia przy energiach TeV–PeV. Obrót 65 wykrył błąd ×2 normalizacji kątowej, poprawił go i podkreślił, że zderzenie nie jest depozycją energii. Nie istniała weryfikacja szybkości **wielokrotnego przenoszenia energii do nośników o niższej energii**. Obrót 66 zamyka tylko ten wąski test, nie termalizację.

## 2. Równania i provenance
- γγ→e⁺e⁻: pełny całkowity Breit–Wheeler, Planck Tγ=0.078185270688319944 MeV, poprawna izotropowa średnia `1/2 integral[-1,+1] (1-mu)*sigma dmu`, bez modyfikacji fizyki tła.
- e±+γ→e±+γ: różniczkowy ultrarelatywistyczny Jones/Blumenthal–Gould, całkowanie po fotonach Plancka i energii fotonu wyjściowego, włącznie z jądrem `2q lnq + (1+2q)(1-q) + (Γq)²(1-q)/(2(1+Γq))`.
- Każdy foton uczestniczący w BW jest zastępowany parą; dla **podziału energii pary brak tu pełnego różniczkowego rozkładu**. Zamiast niego trzy świadomie nieźródłowe kontrole: dokładnie 1/2–1/2; `Beta(2,2)`; dokładnie 0.1–0.9. Nie użyto prawa Bethe–Heitlera dla jąder atomowych, bo nie opisuje ono bezpośrednio procesu foton–foton.
- Rozpraszanie IC: przy energii E elektronu wybierana jest losowa frakcja fotonu wyjściowego `f` z rozkładu różniczkowego; energia jest rozdzielana na foton `fE` i elektron `(1-f)E`.
- Metoda **energy packet lineage**: śledzimy losową jednostkę energii, wybierając gałąź i z prawdopodobieństwem E_i/E. Indukcyjnie empiryczna dystrybuanta czasu przekroczenia progu jest estymatą oczekiwanego **ułamka energii** w nośnikach poniżej progu, a nie rozkładu losowo wybranej cząstki.
- Losowany jest również czas każdego oddziaływania z rozkładu wykładniczego o tempie otrzymanym przez interpolację tablic przekrojów. Tło jest stałe; nie przeprowadzono transportu kosmologicznego ani sprzężenia energii zwrotnej.
- **STOP: E ≤ 0.1 GeV.** To próg obliczeniowy gwarantujący γ≥100 dla użytego jądra IC. To NIE termalizacja, nie depozycja i nie osiągnięcie równowagi plazmy. Przy 100 MeV fotony nadal są nietermiczne i szybko produkują pary.
- Fizyczne źródło: Wu–Xu, https://github.com/Fenyutanchan/Primordial-Black-Hole ; kontrolny kod DAX R65: `IW_DAX_S7_R65_ANGULAR_NORMALIZATION_IC_ENERGY_KERNEL_20261029.py` (jego oryginalne wartości stanowią test regresji), Jones/BG: https://doi.org/10.1103/RevModPhys.42.237 ; https://doi.org/10.1093/mnras/stac2712 .

## 3. Test główny — 48 000 trajektorii
4 energie × 2 początkowe gatunki × 3 podziały energii par × 2000 powtórzeń. Dla początkowego **fotonu** z podziałem Beta(2,2):

| E początkowa | Mediana zejścia poniżej 0.1 GeV | p90 | p99 | Średnia liczba zdarzeń |
|---:|---:|---:|---:|---:|
| 1e+03 GeV | 7.6652354e-10 s | 1.3723303e-09 s | 2.1255376e-09 s | 24.87 |
| 1e+06 GeV | 4.7362997e-07 s | 8.9985597e-07 s | 1.3675927e-06 s | 45.15 |
| 1e+09 GeV | 0.00036573684 s | 0.00067977729 s | 0.0010222876 s | 66.06 |
| 1e+12 GeV | 0.28453173 s | 0.52152411 s | 0.85487312 s | 87.79 |

Zależność od proxy podziału par jest materialna: dla 10⁹ GeV mediany początkowego fotonu to 0.277 ms (równy podział), 0.366 ms (Beta(2,2)) i 0.866 ms (0.1/0.9). To nie jest błąd kwadratury ani zidentyfikowana fizyczna niepewność — jest to zakres trzech arbitralnie wybranych operatorów transferu energii.

## 4. Warunkowy test masy PBH i progu 3 ms
Podstawiono tylko proxy **E_foton=T_H(M)=1.06×10¹³ GeV·g / M(g)**, M₀=9.58288×10⁹ g, bez widma Hawkinga i bez czasowej funkcji depozycji. Przy `P(t_pass>0.003s)=0.5`:

| Podział pary | E początkowa | M pozostała | M/M₀ |
|---|---:|---:|---:|
| equal | 1.19952e+10 GeV | 883.688 g | 9.22153e-08 |
| beta22 | 8.8703e+09 GeV | 1195 g | 1.24701e-07 |
| asymmetric | 3.63687e+09 GeV | 2914.6 g | 3.04146e-07 |

Udział energii emitowanej z opóźnieniem śledzonej gałęzi powyżej 3 ms, otrzymany przez **dodatkową, wyraźnie modelową** kwadraturę po pozostałej masie μ=M/M₀, jest rzędu 10⁻⁷ (tabela `R66_MONOCHROMATIC...csv`). W tym etapie użyto dodatkowych założeń: stały współczynnik konwersji utraty masy na energię, monochromatyczne E=T_H, interpolację po logE i ekstrapolację P=0 poniżej i P=1 powyżej zakresu siatki. Jest to wskaźnik ilustracyjny, NIE oszacowanie depozycji ani ścisłe ograniczenie fizyczne.

## 5. Kontrole numeryczne
- `nquad=75,110,160` (bez niezależnego użycia poprawki z R65); maksymalny relatywny rozstęp bezpośrednich szybkości BW/IC w kontrolach 1e3/1e6/1e9 GeV: 0.00022114.
- Dla `E₀=10⁹ GeV`, początkowego fotonu, Beta(2,2), porównano po 1500 trajektorii z dwoma ziarnami losowymi i progami E_stop=0.1/1/10 GeV. Zakres median:
  - E_stop=0.1 GeV: 0.00035761884–0.00036493818 s.
  - E_stop=1 GeV: 0.00034439264–0.00037052951 s.
  - E_stop=10 GeV: 0.00035387588–0.00036673446 s.
- 48 000 trajektorii głównych i 18×1500 kontrolnych przeszło limit 700 zdarzeń bez nierozwiązanych przypadków.
- Skwantylowany rozkład IC (`1024` kwantyle) reprodukuje bezpośredni moment energii fotonu z różniczkowego jądra z względnym błędem poniżej 4×10⁻⁴ w sprawdzonych energiach 0.1–10¹² GeV.
- Porównano wprost poprawione zderzenia BW i IC z liczbami R65 dla 1 TeV i 1 PeV.
- Dla wyniku `P=0` na N=2000 próbach nie ma dowodu zerowego prawdopodobieństwa; granica statystyczna jest niezerowa i wymaga ostrożności.

## 6. Rozstrzygnięcie i brakujące elementy
**Nowe ustalenie warunkowe:** już w modelu z energią przenoszoną przez gałęzie BW↔IC czas wielokrotnego przenoszenia może być większy od czasu pierwszego zderzenia o kilka razy. W przypadku ekstremalnych E>~10¹⁰ GeV może osiągać milisekundy i więcej, ale przy proxy E=T_H odpowiada to zaledwie około 10⁻⁷ pozostałej początkowej masy PBH.

**Nie ma prawa wnioskować**, że pełna energia w tym czasie *deponuje się* w termicznej plazmie. Nie ma też bezpośredniej granicy na rzeczywisty czas jej depozycji; potrzebny jest operator transferu dla rozpraszania na fotonach i jądrach, pełny różniczkowy BW, synchrotron, pozostałe kanały, zmieniające się tło, dystrybucja widm BlackHawk i sprzężenie z BBN.

**Werdykt:** `ENERGY_WEIGHTED_BRANCHING_PROXY_RUN / ANGULAR_X2_FIXED / BG_DIFFERENTIAL_USED / PARTIAL_TRANSFER_NOT_DEPOSITION / SOURCE_BW_SPLIT_UNIDENTIFIED / BLACKHAWK_NOT_RUN / JULIA_NOT_RUN / NO_EXEC / NO_CANON / NO_PBH_BOUND`.