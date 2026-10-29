# DAX-S7 — obrót 66: energetycznie ważony transport w kaskadzie gamma-gamma / IC
**Data:** 2026-10-29
**Status:** `CONDITIONAL_TRANSPORT_PROXY / NO_EXEC / NO_CANON / NO_PBH_BOUND / BLACKHAWK_NOT_RUN / JULIA_NOT_RUN`

## Zakres audytu
Kontynuacja erraty R65: po poprawieniu czynnika izotropowej średniej kątowej x1/2 trzeba oddzielić pierwszy kontakt z kąpielą termiczną od transportu energii przez wiele rozgałęzień gamma-gamma -> e+e- oraz e+gamma -> e+gamma.

Użyto:
- całkowitego przekroju Breit-Wheelera z poprawną średnią po energii i kątach fotonów Plancka przy `Tgamma=0.07818527068831995 MeV`;
- ultrarelatywistycznego różniczkowego jądra Jones/Blumenthal-Gould, z losowanym rozdziałem energii w zdarzeniu IC;
- trzech **nieźródłowych** modeli podziału energii w produkcji par: 50/50, Beta(2,2), 10/90;
- śledzenia losowo wybranej jednostki energii po rozgałęzieniach, gdzie prawdopodobieństwo wyboru potomka jest proporcjonalne do jego energii. Zatem dystrybuanta czasu przekroczenia progu estymuje ułamek energii transportowanej poniżej progu; nie jest rozkładem liczby cząstek.

**Próg obliczeniowy E<0.1 GeV to NIE depozycja ani termalizacja**. Jądro IC poniżej gamma=100 nie zostało użyte, dlatego 100 MeV to sztuczny próg zatrzymania obliczeń.

## Test główny
48 000 trajektorii: 4 energie × foton/elektron × 3 podziały par × 2000.
Mediany w sekundach dla początkowego fotonu i podziału Beta(2,2):
- 1e3 GeV: `7.665235373e-10`
- 1e6 GeV: `4.736299746e-7`
- 1e9 GeV: `3.657368444e-4`
- 1e12 GeV: `0.2845317253`.

W przypadku 1e9 GeV mediana jest zależna od BW podziału: 50/50=`2.77240132e-4s`, Beta(2,2)=`3.65736844e-4s`, 10/90=`8.66289290e-4s`. To materialna niepewność operatora transferu, nie rozrzut samej kwadratury.

## Test proxy E=T_H(M), Mf=9.58288e9g
Masę, przy której `Pr(t_przejscia_ponizej_100MeV > 0.003s)=0.5`, oszacowano **wyłącznie przy monochromatycznym proxy** `E=T_H=1.06e13 GeV*g/M`:
- 50/50: `M=883.688g`, `M/Mf=9.22153e-8`;
- Beta(2,2): `M=1194.999g`, `M/Mf=1.24701e-7`;
- 10/90: `M=2914.598g`, `M/Mf=3.04146e-7`.

Dodatkowa kwadratura względem pozostałej masy (a nie faktycznego widma emisji) daje przykładowy udział energii o opóźnieniu >3ms w tym **monochromatycznym** modelu: `1.02e-7, 1.38e-7, 3.37e-7` odpowiednio. Dla pozaobszarowych energii narzucono `P=0` poniżej siatki, `P=1` powyżej siatki. **Liczby nie są ścisłym ani fizycznym ograniczeniem depozycji.**

## Kontrola
W trzech rozdzielczościach kwadratury `N=75,110,160` względny rozstęp bezpośrednich szybkości BW i BG w energiach 1e3/1e6/1e9 GeV wynosi najwyżej `2.212e-4`.
18 niezależnych kontroli × 1500 trajektorii zmieniało N, seed i zatrzymanie E=0.1/1/10 GeV; przy E0=1e9 GeV mediana w zakresie `0.344e-3..0.371e-3s`.
Nie znaleziono trajektorii przekraczających cap 700 zdarzeń w 75 tys. przebiegów testowych. Przy P=0 w skończonej próbie nie wolno twierdzić P dokładnie równe zero.

## Granice naukowe
Brak dokładnego różniczkowego BW dla rozdziału energii par; brak pełnej ciągłej kaskady, synchrotronu, innych kanałów, wpływu ekspansji, zmiennego tła, nieliniowego sprzężenia i pełnego widma BlackHawk. **Wyniki mogą opisywać transport do niskiej energii, NIE czas ogrzania termicznej kąpieli.** Nie wyznaczono nowej fizycznej granicy PBH.

**Provenance:** Wu–Xu public repository https://github.com/Fenyutanchan/Primordial-Black-Hole ; BG doi:10.1103/RevModPhys.42.237 ; Jones/BG differential kernel https://doi.org/10.1093/mnras/stac2712 .
**Weryfikowalna baza lokalna:** `IW_DAX_S7_ROTATION_66_REPRODUCIBLE_PACKET_20261029.zip` (14 plików: reproducer, skan, testy, CSV, pełny raport, manifest SHA256).
**Werdykt:** `ENERGY_WEIGHTED_BRANCHING_PROXY_PASS / NO_THERMAL_DEPOSITION_CLAIM / NO_EXEC / NO_CANON`.
