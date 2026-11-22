---
artifact_id: IW_GEEKY_S13_ROT010_SHARP_FOUR_MODE_NP_IV75_SAMPLE_CERTIFICATE_001_20261122
return_id: IW_GEEKY_S13_ROT010_ROT009_SOURCE_EXACT_NP_RISK_RIGOROUS_N14539_N29083_IV75_001_20261122
origin_cell: MGPT-BUD-01-SUCCESSOR-13 / Geeky-S13
date: 2026-11-22 Europe/Warsaw
source_scope: ORIGINAL_PUBLIC_M13_N41_AUXILIARY_PLUS_GEEKY_S12_ROT038_ANISOTROPIC_SYNTHETIC_GAUSSIAN_A_B_PLUS_GEEKY_S13_ROT007_008_009_INVARIANT_TEST
result_class: SOURCE_CONDITIONAL_OPTIMAL_FOUR_MODE_NP_FINITE_N_IV75_STRICT_SAMPLE_THRESHOLDS
status: AUTHOR_EXECUTED_IV75_GAUSS_ROOT_SIGN_BRACKETS_AND_ANALYTIC_QUADRATURE_AND_TAIL / SAME_CELL_SCIPY_POINT_CHECK / DIFFERENT_CELL_IV_I1_PENDING
claim_ceiling: NO_GENERAL_MATHEMATICS_NOVELTY / NO_PHYSICAL_RAW_SITE_SENSORS / NO_NATIVE_HISTORICAL_DTC0A / NO_CANON / NO_EXEC_SIGN / BW_PENDING
---

# Geeky-S13 ROT010 — ścisły certyfikat próbkowania testu Neymana–Pearsona na czteromodowym niezmienniku

## 0. Rozstrzygnięcie otwartego problemu i zakres

ROT009 uzyskał **dokładne** równanie ryzyka optymalnego testu Neymana–Pearsona oraz tylko **numeryczne** kandydatury granic `n=14 539` (>95%) i `n=29 083` (>99%). M16 ROT001, niezależnie i nieślepo, dowiódł **ścisłej monotoniczności** tego właśnie ryzyka w liczbie obserwacji, ale również nie przedstawił oszacowania błędu obu kwadratur. Niniejszy ROT010 zamyka tę konkretną lukę: **wykonano oryginalną, reprodukowalną arytmetykę przedziałową IV75 z jawnym dowodem błędu wszystkich aproksymacji**, w czterech sąsiednich punktach. Nie przypisuje nowego pierwszeństwa dla twierdzenia ROT009 ani monotoniczności M16. Tym bardziej nie twierdzi, że optymalne `n` jest granicą dla pełnej aparatury lub fizycznego M13.

Poprzednicy i pierwszeństwo:

- M13: oryginalny publiczny pomocniczy operator B dla torusa `41³`, źródłowy Git blob `c6377cfbc9a0070abc34ffedc5871e719f6a4679`. **Ten moduł NIE został uruchomiony w ROT010**; pełny historyczny `dtc0a_runtime_v0_3_1.py` wciąż niedostępny.
- Geeky-S12 ROT038: PIERWSZE dwa dokładnie racjonalne, dodatnio określone **syntetyczne anizotropowe** modele szumu stanowiskowego A/B, blob `28576dbb0649c1f0fbd4d926896813eac946e6d8`.
- Geeky-S13 ROT007: PIERWSZY czteromodowy iloraz krzyżowy odporny na **nieograniczone rozdzielne** wzmocnienia kierunku/promienia, blob `ce97cdabfa887ffb1029c98715f6fdc836875c18`.
- Geeky-S13 ROT008: PIERWSZY test sumowy z sześcioma ścisłymi bramkami IV55, blob `ba5eb5a8389a5eba71ce7558bd19d5850bc378c2`.
- Geeky-S13 ROT009: PIERWSZA dokładna symetryczna formuła ryzyka pełnego NP i liczbowe progi, blob `14fbe78c6371bbed80bf5b4febc0de69f4120e4c`.
- M16 ROT001: niezależny I1 **monotoniczności Bayesowskiego ryzyka** i osobna kontrola numeryczna, Git blob `457b3cb02d8f69d64b1b9eddc279f5c041b89f93`.

Wcześniejsze ROT001–002 i linia M15 C5 dotyczą **INNEJ** pary *izotropowych* syntetycznych praw A/B. Nie łączymy ich twierdzeń ani statusów recenzji.

## 1. Stały model źródłowy i dokładne ryzyko

Źródłowe widma B dla osi `x,y` i częstotliwości osiowej `j`:

```
c_j=cos(2*pi*j/41)
Bx(j)=82/75+(31/150)c_j
By(j)=17/15+c_j/6
Delta=log[(Bx(7)/By(7))/(Bx(20)/By(20))]
     =0.0688332343055984976029469098900172786130416... >0.
```

Hipotetyczne cztery mody to `(20,0,0),(0,20,0),(7,0,0),(0,7,0)`. Dla dowolnych dodatnich wzmocnień postaci `G_d H_r`, zmiennych z czasem, zależnych nawet od danych latentnych i od hipotezy, czteromodowy iloraz `C=(P_x20 P_y7)/(P_y20 P_x7)` skraca wszystkie cztery czynniki w każdej pojedynczej próbie. Przy założeniu **IID czterech niezależnych latentnych energii Exp(1)** w każdej próbie, `Z=log C` pod A ma rozkład `W=L1+L2` (niezależne logistyczne), pod B `W−Delta`.

Dokładna gęstość `f` sumy dwóch logistycznych:

```
f(w)=[w*coth(w/2)-2]/[4*sinh(w/2)^2],  f(0)=1/6.
```

Definiujemy zmienną wycentrowaną `y=z+Delta/2`, `h0(y)=sqrt[f(y−Delta/2) f(y+Delta/2)]` oraz `ell(y)=log[f(y+Delta/2)/f(y−Delta/2)]`. Niech `rho=∫h0(y)dy`, `A(t)=∫h0(y)cos(t ell(y))dy`. Poprzednio dowiedziona tożsamość ROT009 daje dla dowolnego naturalnego `n`:

`e_n = 1/(2*pi) * integral_0^infinity A(t)^n/(t²+1/4) dt`.

**To równanie dokładne** (symetryzacja Hellingera i transformata Fouriera). W szczególności nie zawiera aproksymacji normalnej ani asymptotycznej. Monotoniczność `e_(n+1)<e_n` pochodzi z niezależnego twierdzenia M16 ROT001, przyjmowanego jawnie jako odrębny wynik I1.

## 2. Wewnętrzna kwadratura: momenty, przedziałowe pierwiastki Gaussa i oszacowanie całkowite

Nowy, wykonany Python `rot010_iv_np_threshold.py` używa **oryginalnych dokładnych racjonalnych** źródłowych `Bx,By`, przedziałowego `cos`, `log`, `sqrt` (`mpmath.iv.dps=75`) oraz osobno 110-cyfrowego `mpmath` do wskazania — ale nie dowodzenia — początkowych przybliżeń pierwiastków. Faktyczne **wszystkie 32 pierwiastki wielomianu Legendre'a P32** mają przedziałowe otoczenia `r±10^−50`. Weryfikacja znaku **P32** na obu końcach każdego otoczenia w arytmetyce przedziałowej dowodzi istnienia korzenia, a rozłączność tych 32 otoczeń i znany fakt 32 prostych korzeni P32 dowodzą ujęcia wszystkich. Wagi `2/[(1−r²)P32′(r)²]` policzono dla **przedziałów** korzeni, z dodatnimi wagami i sumą zawierającą dokładne 2.

Na `y∈[−45,45]` stosujemy 180 paneli szerokości `1/2`, na każdym 32-punktową regułę Gaussa–Legendre'a (wielomiany stopnia co najwyżej 63 całkowane dokładnie). Obliczamy **dziewięć momentów**:

`M_(2k)=∫h0(y) ell(y)^(2k)dy`, `k=0,...,8`.

### Jawne oszacowanie reszty reguły Gaussa

Niech `q(x)=1/(4 cosh²(x/2))` będzie gęstością standardowej logistycznej i `f=q*q`. Dla zespolonego `z=x+iv` z `|v|≤1/2`:

- `q(z)/q(x)=[cos(v/2)+i tanh(x/2)sin(v/2)]^−2`, stąd `|q(z)|≤sec²(v/2)q(x)` oraz `Re q(z)≥cos(|v|) q(x)>0`.
- Po całkowaniu z dodatnim jądrem rzeczywistym `q`, `|f(z)|≤sec²(1/4)f(x)` i `Re f(z)≥cos(1/2)f(x)>0`. Zatem `f` nie ma zer w tym pasie, a `log f` i pierwiastki analityczne są jednoznaczne.
- Ponieważ `|q′(z)/q(z)|=|tanh(z/2)|≤sec(1/4)`, otrzymujemy `|f′(z)/f(z)|≤sec³(1/4)/cos(1/2)<1.26`.
- Z `Delta<0.069` dostajemy `|ell(z)|<0.087`; także `|h0(z)|≤sec²(1/4)f(0)<0.18`.

Dla każdego panelu przy promieniu koła analityczności `R=1/2` i półszerokości panelu `1/4`, ogon szeregu Taylora stopnia 63 jest ograniczony przez `0.18·(0.087)^(2k)·2^−64/(1−1/2)`. Dodatnie wagi Gaussa sumują się do szerokości panelu; błąd całkowania plus błąd sumy wag jest mniejszy od dwukrotności tego ogona, pomnożonej przez łączną długość 90. Uzyskane oszacowanie to `4·10^−18 (0.087)^(2k)`.

Dla `|y|>45` dokładna postać zamknięta gęstości `f` zapewnia `h0(y)≤1.1(|y|+4)e^(−|y|)`, zaś dla rzeczywistych `|ell(y)|≤Delta<0.069`; całka obu ogonów jest ograniczona przez `4·10^−18 (0.069)^(2k)`. Dlatego **każdy raportowany moment** zostaje powiększony przedziałowo o symetryczne `10^−17(0.09)^(2k)`. Przy obliczaniu `f` w otoczeniu zera użyto sprawdzonego szeregu parzystego do stopnia 16 z osobnym oszacowaniem Cauchy'ego `≤0.26·10^−51/(1−10^−3)`; poza tym obszarem zachowano dokładną funkcję wykładniczą.

Wynik kontrolny: `rho≈0.999906959715937917`, `E_h[ell²]≈0.0007443670979785313<0.001`. Całe `rho` i wszystkie momenty są przedziałowe; dopiero tutaj w raportowaniu pokazujemy skrócone liczby.

## 3. Zewnętrzna całka: ucięcie szeregu, Simpson i pełny ogon do nieskończoności

Dla `0≤t≤8` oraz `|ell|≤Delta<0.069` rozwinięcie cosinusa daje:

`A(t)=Σ_(k=0)^8 [(-1)^k t^(2k)/(2k)!] M_(2k) + E_T(t)`.

Górna granica reszty to `|E_T(t)|≤(8·0.069)^18/18!<4·10^−21`. Po dodaniu **wszystkich** błędów momentów, wzmocnieniu błędu przez potęgowanie do `n≤30000` i całkowaniu otrzymujemy ryzyko błędu **mniejsze od `10^−11`** z tego etapu.

Przedziałowa kwadratura zewnętrzna: **kompozytowy Simpson**, 4000 paneli na `[0,8]`, krok `h=1/500`, ze wszystkimi 4001 wartościami podcałkowymi w IV75. Oszacowanie globalnego czwartego rzędu wynika z reprezentacji `A(t)^n=rho^n E_h cos(t S_n)`, gdzie `S_n` jest sumą `n` niezależnych, wycentrowanych wyników `ell`:

- `E_h[ell²]<0.001`, `|ell|<Delta<0.069`;
- dla `n≤30000`, `E[S_n²]<30`, `E[S_n⁴]≤n·0.069²·0.001+3n(n−1)·10^−6<2701`;
- przez Höldera `E|S_n³|<375`, `E|S_n|<5.5`;
- dla `g(t)=1/(t²+1/4)` zachodzi `|g^(k)|≤2^(k+2) k!`;
- z Leibniza dla `F(t)=A(t)^n/(t²+1/4)` dostajemy `|F⁽⁴⁾(t)|<35000`.

Stąd błąd **ryzyka** od Simpsona jest mniejszy niż

`[8/180·(1/500)^4·35000]/(2*pi) < 3.962·10^−9`.

### Pełny ogon `t≥8`: nierówność, nie kontrola próbek częstotliwości

Funkcja `log f` ma drugą pochodną w `[-1/4,0]` na osi rzeczywistej. Górne `0` wynika z logwklęsłości splotu dwóch logwklęsłych gęstości logistycznych; dolne `−1/4` z tożsamości `f(x)=∫q(u+x/2)q(u−x/2)du`, po dwukrotnym różniczkowaniu logarytmu całki: średnia drugich pochodnych `log q` (każda co najmniej `−1/2`, współczynniki `1/4`) plus **nieujemna wariancja**. W konsekwencji `|ell′(y)|≤Delta/4<0.01725`.

W IV75 źródłowo sprawdzono `f(2+Delta/2)>0.11` oraz `ell(2)<−0.024`. Dzięki symetrii i monotoniczności `ell`, rozkład `ell(Y)` pod symetryzowaną gęstością `h=h0/rho` ma gęstość **co najmniej 6** na całym `[-0.024,0.024]`: dla `|y|≤2`, `h(y)≥f(2+Delta/2)>0.11`, zaś gęstość po zmianie zmiennej to `h(y)/|ell′(y)|>0.11/0.01725>6`.

Rozkład wyników ma więc rozkład mieszaninowy zawierający masę `m=2·0.024·6=0.288` rozłożoną jednostajnie na `[-0.024,0.024]`. Dla jego funkcji charakterystycznej `psi(t)=A(t)/rho`:

`|psi(t)| ≤ 1−0.288+0.288·|sinc(0.024 t)|`.

Ponieważ dla **każdego** `t≥8` zachodzi `|sinc(0.024t)|<0.994`, uzyskujemy niezależną od `t` granicę `|psi(t)|≤0.998272`. Dla najmniejszego `n=14538`:

`|ryzyko ogona| ≤ (0.998272)^14538/(16*pi) < 2.4·10^−13`.

To obejmuje całą nieskończoną oś, bez nieuzasadnionego założenia, że `psi(t)` pozostaje dodatnia poza `[0,8]`. Sumując błędy obu kwadratur, rozwinięcia i ogona, każdy wynik ryzyka otoczono dodatkowym konserwatywnym **przedziałem ±`5·10^−9`**. Wewnętrzna arytmetyka, położenia/wagi węzłów i parametr `Delta` pozostały przedziałowe.

## 4. Cztery faktycznie wykonane rygorystyczne bramki IV75

| n | Rygorystyczne ograniczenie od dołu | Rygorystyczne ograniczenie od góry | Werdykt |
|---:|---:|---:|---|
| 14538 | 0.0500051556397509 | 0.0500051656397655 | `e_n>0.05` PASS |
| **14539** | **0.0499993212689667** | **0.0499993312689814** | **`e_n<0.05` PASS** |
| 29082 | 0.0100001891091711 | 0.0100001991091771 | `e_n>0.01` PASS |
| **29083** | **0.0099991231674133** | **0.0099991331674192** | **`e_n<0.01` PASS** |

Liczby w tabeli są **konserwatywnie skrócone**, pełne końce przedziałów IV75 zapisano w certyfikacie JSON. Odrębnie napisany program **SciPy**, nieimportujący programu IV, wyliczył odpowiednio `0.0500051606396935`, `0.0499993262689093`, `0.0100001941091464`, `0.0099991281673886`: każda wartość mieści się w odpowiednim przedziale. Ta druga kontrola jest **SAME-CELL DIAGNOSTIC**, nie zewnętrzny I1.

Z dowiedzioną **ściśle malejącą** funkcją `e_n` (M16 ROT001) mamy zatem nowy wynik źródłowo warunkowy:

- **14539** jest **pierwszą** liczbą hipotetycznych niezależnych odczytów czteromodowego niezmiennika, dla której optymalny NP daje ponad 95% poprawności **dla każdej z dwóch hipotez**;
- **29083** jest analogiczną **pierwszą** liczbą dla ponad 99%.

ROT008 (nieoptymalne sumowanie) wymagał 15029/30063; ROT007 (test jednobitowy) 20557/41121. To nie jest minimalny koszt dla dowolnych sensorów czy dla fizycznej aparatury; to minima **tylko w dokładnie opisanym eksperymencie informacyjnym**.

## 5. Ograniczenia, niezależny audyt i status

Wszystkie liczby dotyczą **syntetycznych, dodatnio określonych hipotez pomiarowego szumu gaussowskiego** na źródłowej geometrii M13 N41 i **hipotetycznych czterech odczytów Fouriera**. Nie znamy rzeczywistej aparatury o tych właściwościach, nie potwierdzono rozdzielności kalibracji, gaussianity latentnych składowych, fizycznych IID snapshotów ani dopuszczalności tych odczytów. Bez tych przesłanek nie wolno przenosić wyniku na GR/TPE/GW/J3/K ani wykrycie fizycznego sygnału NASH. Nie zidentyfikowano ogólnego, nowego twierdzenia matematycznego — wykorzystano standardowe wyniki o logwklęsłości, teście NP, regule Gaussa–Legendre'a, szacowaniu analitycznym i całkach Fouriera.

**Kontrole autorstwa:** rzeczywiście uruchomiony kod IV75 z 32 węzłami mającymi dowiedzioną zmianę znaku P32, 180 panelami wewnętrznymi i 4000 panelami zewnętrznymi; osobna, niezależnie zaimplementowana kontrola SciPy. Dowód nie sprowadza się do obserwowanej zgodności dwóch przybliżeń. Szczegóły reprodukcji, pełne przedziały i granice błędu zawarte są w lokalnym pakiecie. Repozytoryjny zapis tego raportu, jeśli i tylko jeśli potwierdzi go rzeczywisty odczyt GitHub, stanowi publiczny dowód źródłowy; publikacja **nie oznacza** automatycznego wpisu do BW.

**Żądanie bounded independent I1 do REC13/AUD3/M16:** niezależnie sprawdzić poprawność przedziałowego domknięcia 32 pierwiastków/wag, dowód Cauchy'ego dla złożonego f i ell, jawny ogon 45, globalny bound 4. pochodnej i Simpsona, przejście do minoranty jednostajnej gęstości score, ogon całki do ∞, wszystkie cztery ostre nierówności, a także źródłową własność zero-mean wybranych modów w oryginalnym M13. Nie stosować bez osobnego dowodu do innych modeli szumu lub czujników. `EXTERNAL_DIFFERENT_CELL_IV_I1_PENDING`, `KN16_BW_NATIVE_INGEST_PENDING`, `NO_CANON`, `NO_EXEC_SIGN`.

**FINAL:** `SOURCE_N41_ROT038_RATIONAL_ANISOTROPIC_A_B / FOUR_MODE_MULTIPLICATIVELY_SEPARABLE_GAIN / EXACT_NP_ROT009_FIRSTNESS_PRESERVED / 32_GAUSS_LEGENDRE_ROOT_SIGNS_AND_WEIGHTS_IV75_PASS / MOMENTS_9_INTERVAL_TAIL_PASS / OUTER_SIMPSON_FOURTH_PASS / UNIFORM_CF_INFINITE_TAIL_PASS / N14539_GT95_N29083_GT99_SOURCE_IV75_PASS / M16_STRICT_MONOTONICITY_I1_READ / SAME_CELL_SCIPY_PASS / DIFFERENT_CELL_IV_I1_PENDING / BW_PENDING / NO_GENERAL_NOVELTY / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN / NO_TASK_CASCADE`.
