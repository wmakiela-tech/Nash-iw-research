# IW_NC_LT4_PRIOR_ART_SUBTRACTION_FULL_MANUSCRIPT_004_20261018

> **ERRATA 2026-10-19 (II):** rachunek kosztu ramy i licznik kandydatów B skorygowane po audycie REC9 — patrz `IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019.md`. REC9: strict B = 0, kandydat B = 1; surowy licznik non-mapów nie jest miarą jakości.

ARTIFACT_ID: IW_NC_LT4_PRIOR_ART_SUBTRACTION_FULL_MANUSCRIPT_004_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude, rola: audytor / prior-art subtraction
OBIEKT: monografia, DRIVE 1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ, 161 432 znaków, rozdziały 1–7, odczyt 2026-10-18
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / SUBTRACTION_FIRST / SOURCE_FIRST
AUTORSTWO I DECYZJA: LT4. Dokument jest audytem, nie propozycją redakcyjną.
POPRZEDZAJĄ: 001 (audyt), 002 (zaostrzenia, §B WYCOFANY), 003 (§A i §B WYCOFANE jako rekonstrukcja)

---

## 0. Dlaczego ten dokument i dlaczego ja

Plan naukowy monografii stawia to wprost w hierarchii wkładu, punkt B: „wyraźnie wskazać
dokładnie, która hipoteza, konkluzja, ostrość lub kontrprzykład nie jest jedynie cytowanym
wynikiem gospodarza. Trzeba wykonać prior-art subtraction i niezależny dowodowy readback."
I w diagnozie: „Większość zapisanych twierdzeń należy jednak do dojrzałego korpusu matematyki
albo jest elementarną dedukcją ze standardowych wyników."

W tabeli własności MT13 z 13 X stoi: LT4 — tekst i architektura; SW — kontrole dowodów;
INT7 — kontrole mostów; MT13 — spójność programowa, **„not independent referee"**.
Subtraction nie należy do nikogo. Robię ją.

**Metoda, podana tak, by claimy o BRAKU były falsyfikowalne** (reguła, którą sam zaproponowałem
dzisiaj po trzech własnych błędach wnioskowania z pośrednika):
pełny tekst pobrany lokalnie; ekstraktor obiektów numerowanych zwalidowany na elementach znanych
jako obecne (`5.5a`, `Twierdzenie 7.4`, `Twierdzenie 7.5`, `Kontrprzykład 7.2`, `7.8.1` — wszystkie
trafione); **pierwsza wersja ekstraktora dawała dla rozdziału 1 zero obiektów, bo wymagała kropki
w numerze, a rozdział 1 numeruje `Twierdzenie 1`..`Twierdzenie 8` bez prefiksu** — złapane, bo
zwrot MT13 z 13 X wymienia twierdzenia rozdziału 1 i zero było niemożliwe. Po poprawce: 68
unikalnych obiektów numerowanych. Każdy claim o nieobecności cytowania poniżej to liczba trafień
wyszukiwania nazwiska w pełnym tekście, do sprawdzenia w jednej linii.

---

## 1. Wynik zbiorczy

**68 obiektów numerowanych. Po odjęciu gospodarzy w hierarchii A pozostaje OSIEM kandydatów do
hierarchii B.** To potwierdza diagnozę planu i ją uściśla: nie „większość", lecz około 88%.

Monografia **nie jest** niedbała w cytowaniu. Cytuje i nazywa: Schur (9), Feshbach (4),
Zwanzig (3), Mori (3), Choi (10), Kraus (2), Blackwell (4), Brüning–Lesch (2+2),
Arnold–Falk–Winther (3+2+2), Grönwall (2), Engel–Nagel (3+3), Tikhonov (1), Pollock (1),
Modi (1), Chiribella (3), Kalman (3), Micchelli (1), Foucart (2). Architektoniczny wymóg planu
— skonfrontować Mori–Zwanzig/Schur–Feshbach, ilorazy i teorię operatorów, kompleksy
Hilberta/Hodge'a, quantum combs, kinetykę i analitykę celu — **jest spełniony, wszystkie pięć
osi obecne i zaopatrzone w gospodarzy.** Wiele twierdzeń nosi własne zastrzeżenie
w tekście („Jest to standardowa równoważność reprezentacji, nie nowa fizyka”; „Równość (3.3)
wynika z łączności złożenia operatorów. Nie dowodzi istnienia niezerowej klasy kohomologicznej”;
„Jest to dominacja całego eksperymentu P nad Q w sensie Blackwella”). Autoocena w tekście jest
rzetelna i to należy zapisać, zanim wyliczę luki.

---

## 2. Subtraction po rozdziałach

### Rozdział 1 — 11 obiektów, 2 kandydaci B

| obiekt | treść | gospodarz | klasa |
|---|---|---|---|
| Tw. 1 | `C(ST)−C(S)C(T)=PSQTJ` | wstawienie `I=JP+Q`; identyczność nośna dla §3.4 | A |
| Tw. 2 | równanie pamięci, `K(t)=Be^{tD}C` | Mori–Zwanzig / Nakajima–Zwanzig, wariacja stałych — CYTOWANE | A |
| Tw. 3 | postać Schura `Σ(z)=B(zI−D)^{-1}C` | dopełnienie Schura / projekcja Feshbacha — CYTOWANE | A |
| Tw. 4 | równoważność 5 warunków (półgrupa ⟺ `K≡0` ⟺ `BD^kC=0` ⟺ `Σ≡0`) | teoria układów liniowych, parametry Markowa | A (zebranie pięciu z jawną klasą ograniczoną to wkład prezentacyjny) |
| Kontrprz. 1 | `BC=0` lecz `BDC=1`; łańcuch nilpotentny | ranga macierzy Hankela, Kalman — CYTOWANY | A |
| Kontrprz. 2 | autonomia całego `x` ⟺ `B=0` | elementarne | A |
| **Tw. 5** | **kryterium celu `τ(zI−A)^{-1}B(zI−D)^{-1}C=0`** | **functional observability** | **KANDYDAT B** |
| **Kontrprz. 3** | **wszystkie `τBD^kC=0`, lecz `τABC≠0`; konieczność `τA=A_Zτ`** | kontrola ostrości dla Tw. 5 | **KANDYDAT B (w parze)** |
| Tw. 6 | `dim Y_min = rank[BD^{i+j}C]` | twierdzenie Ho–Kalmana o randze Hankela — Kalman CYTOWANY | A |
| Tw. 7 | `V(g)=J*U(g)J` jest reprezentacją ⟺ `EU(g)=U(g)E` | elementarna teoria reprezentacji | A |
| Tw. 8 | falsyfikator momentowy, `BD^kC=0`, `K(2)=1` | nilpotentna półgrupa przesunięć, Engel–Nagel — CYTOWANY; plan przypisuje SW | A |

### Rozdział 2 — 10 obiektów, 1 kandydat B

| obiekt | treść | gospodarz | klasa |
|---|---|---|---|
| Tw. 2.1 | faktoryzacja ⟺ stałość na włóknach | własność uniwersalna ilorazu | A |
| Tw. 2.2 | ciągłość na ilorazie | własność uniwersalna topologii ilorazowej | A |
| Tw. 2.3 | autonomia ⟺ włókna we włókna | rzutowalność układu na iloraz | A |
| Tw. 2.4 | `T=SP` ⟺ `‖Tx‖≤C‖Px‖` | **lemat Douglasa o majoryzacji i faktoryzacji (1966)** | A — **NIECYTOWANY, `Douglas` 0 trafień** |
| Kontrprz. 2.1 | `Pe_n=n^{-1}e_n`, `Te_n=n^{-1/2}e_n` | standardowy obraz niedomknięty | A |
| Tw. 2.5 | `diam I_τ(y;ε) ≤ ω(2ε)` | optimal recovery, moduł ciągłości | A (gospodarz cytowany dopiero w rozdz. 7) |
| **Przykł. 2.4a** | **`ω_{K_R}(δ) ≤ min{2R,√(2Rδ)}`, równość osiągana, wykładnik Höldera 1/2 ostry** | stabilność warunkowa źle postawionych zadań, Tikhonov — CYTOWANY | **KANDYDAT B (ostrość, nie teza)** |
| Tw. 2.6 | zwartość ⟹ `ω(δ)→0` | standardowy argument zwartościowy | A |
| Przykł. 2.4 | `ω(δ)=(4δ)^{1/3}` dla `r(x)=x³` | dokładny rachunek elementarny | A |
| Tw. 2.7 | iloczyn włóknisty a dodatkowe prawo `R` | elementarna teoria mnogości | A |

### Rozdział 3 — 10 obiektów, 0 kandydatów B

Wszystkie A. Tw. 3.1 (koniugacja), 3.2 (kompresja jest reprezentacją — **powtórzenie Tw. 7
z rozdz. 1**), 3.3 (tożsamość trzech złożeń = warunek kocyklu Hochschilda, i tekst sam mówi,
że klasy nie dowodzi), 3.4 (transport na iloraz), 3.5 (podobieństwo realizacji), 3.6 (graf
a iloczyn włóknisty), 3.7 (kowariancja Heisenberga), 3.8 (podobieństwo półgrup — Engel–Nagel),
3.9 (randomizacja = dominacja Blackwella, tekst to nazywa). Rozdział jest w całości
porządkowaniem gospodarzy, i sam to o sobie mówi.

### Rozdział 4 — 9 obiektów, 3 kandydaci B

| obiekt | treść | gospodarz | klasa |
|---|---|---|---|
| Tw. 4.1 | `d^f d^f=0`, `ker d^f=ker d`, z zastrzeżeniem niedomkniętości | elementarne; wartością jest zastrzeżenie | A |
| Tw. 4.2 | zachowanie ilorazu zredukowanego | Brüning–Lesch, kompleksy Hilberta — CYTOWANE | A |
| Tw. 4.3 | równoważność norm grafowych z dwustronnych oszacowań | elementarne z hipotezy | A |
| **Tw. 4.4** | **`H̃¹_red(d^f)=0=H¹_red(d)` ale `H¹_alg(d^f)≠0=H¹_alg(d)`, `d^f` niedomknięty** | rozróżnienie zredukowana/algebraiczna klasyczne (Brüning–Lesch); **świadek, w którym ograniczony iniektywny mnożnik zmienia jedną, zachowując drugą** | **KANDYDAT B — najmocniejszy w rozdziale** |
| **Tw. 4.5** | **homotopia spektralna z kontrolą dziedziny, `K:=domknięcie[d*q(Δ)]`, `h=j/√λ`** | konstrukcja homotopii łańcuchowej standardowa; **normalizacja `√λ` czyniąca `K` ograniczonym i naprawa dziedziny** | **KANDYDAT B (techniczny)** |
| Tw. 4.6 | addytywność homotopii | elementarne | A |
| Tw. 4.7 | `T_f(B)=T_g(B)` ⟺ `R(B)=B` | elementarne po sformułowaniu | A |
| **Przykł. 4.1** | **`T_s(B) ⊊ T_t(B)` przy równych domknięciach, na `S¹`** | kontrola ostrości rozróżnienia obraz/domknięcie | **KANDYDAT B (ostrość)** |
| Tw. 4.8 | brak jednostajnej odwracalności `exp(−tΔ_N)` | elementarne; pułapka FEM, Arnold–Falk–Winther CYTOWANI | A |

### Rozdział 5 — 9 obiektów, 0 kandydatów B

Wszystkie A, wszystkie z gospodarzami obecnymi w tekście. Tw. 5.1 (Kraus z redukcji fizycznej —
**`Stinespring` 0 trafień**, cytowani Kraus i Choi), 5.2 (brak półgrupowości), 5.3 (ten sam kanał,
różny proces — quantum combs, Pollock/Modi/Chiribella CYTOWANI), 5.4 (Choi ⟺ CPTP), 5.5 (test
relacji liniowych), 5.6 (transpozycja: dodatnia, nie CP — podręcznikowe), 5.7 (tomografia),
Lemat 5.1 (**trzecie powtórzenie własności uniwersalnej ilorazu**), Przykł. 5.1.

### Rozdział 6 — 8 obiektów, 1 kandydat B, 1 pozycja D

| obiekt | treść | gospodarz | klasa |
|---|---|---|---|
| Tw. 6.1 | dokładne rozwiązanie `n'=S−Dn` | wariacja stałych | A |
| Tw. 6.2 | tożsamość błędu ważonego | całkowanie przez części | A |
| Tw. 6.3 | `∫φ'n=0` dla każdego `n` ⟹ `φ` stała | lemat podstawowy rachunku wariacyjnego | A |
| Tw. 6.4 | niezmienniczość `[0,1]` | wariacja stałych | A |
| Tw. 6.5 | `x_late/x_early = e^{r(T−h)}`, czynnik >54 przy identycznych całkach | dokładny rachunek elementarny; **mocny falsyfikator fizyczny** | A (teza), nośny redakcyjnie |
| Tw. 6.6 | dokładna tożsamość `Δx(T)` | wariacja stałych | A |
| Tw. 6.7 | pierwsza wariacja celu, równanie sprzężone | **dual-weighted residual, Becker–Rannacher, Acta Numerica 10 (2001)** | A — **NIECYTOWANY, `Rannacher`/`Becker`/`Giles`/`Süli` 0 trafień** |
| **Tw. 6.8** | **dokładna postać sieczna dla skończonej zmiany modelu, `p̄(T)=ḡ` ze średnim gradientem** | chwyt wartości średniej jest w literaturze DWR; **bezperturbacyjność w amplitudzie wymaga sprawdzenia u gospodarza** | **KANDYDAT B WARUNKOWY — do odjęcia po lekturze Beckera–Rannachera** |
| §6.10 | hadronowe źródło kosmologiczne, ~1000 znaków | — | **D — plan żąda „pełnego równania źródłowego, zmiennych, dziedzin, danych i ilościowej kontroli dokładności celu"; tekstu nie ma** |

### Rozdział 7 — 21 obiektów, 1 kandydat B (mój, więc nie moja ocena)

Tw. 7.1 (rodzina rozdzielająca — czwarte wystąpienie faktoryzacji), 7.2 + Wn. 7.2 (złożenie
defektów, elementarne), 7.3 (Grönwall, CYTOWANY), 7.4 + Kontrprz. 7.2 + 7.5 (MT13/Rec9/INT7,
treść twierdzenia spektralnego — MT13 sam to nazwał „standard spectral theorem content"),
7.6 + 7.7 (Duhamel + optimal recovery; tekst sam mówi „Dotychczasowe twierdzenia są znanym
rachunkiem optimal recovery"), 7.8 (próbkowanie, elementarne z `‖M'‖≤L*`, lecz nośne: to
ilościowa wersja „skończony zestaw próbek nie kontroluje historii bez modułu ciągłości"),
7.9–7.11 + Wn. 7.3, 7.4 (optimal recovery, Micchelli–Rivlin i Foucart CYTOWANI),
**Tw. 7.12 + Kontrprz. 7.4** (operator kolizji; tożsamość (7.14) jednolinijkowa — A; równoważność
(7.18) i oszacowanie (7.17) z osiąganiem — kandydat B).

**Tw. 7.12 pochodzi częściowo ode mnie i jego ilościowa wersja w mojej postaci była FAŁSZYWA
(wycofana dzisiaj; Kontrprz. 7.4 LT4 ją obala, a jego `‖J_col‖` jest poprawny i ostry — 0 naruszeń
w ~11 900 losowych układach, maksymalny iloraz dokładnie 1.000000). NIE OCENIAM TEGO OBIEKTU.
ANTI-SELF-SEALING: klasyfikacja Tw. 7.12 należy do DS albo MT13.** Dla ich potrzeb zapisuję
niecytowanego gospodarza: `Fuglede` 0 trafień, `Putnam` 0, `Rosenblum` 0 — przypadek `h=id` jest
klasycznym twierdzeniem Fuglede–Putnama, a rozłączne widma to twierdzenie Rosenbluma; Tw. 7.12
leży dokładnie między tymi skrajnościami i ta gałąź musi wejść do bibliografii.

---

## 3. Osiem kandydatów B po odjęciu

1. **Tw. 5 + Kontrprz. 3 (rozdz. 1)** — kryterium celu i konieczność `τA=A_Zτ`.
2. **Przykł. 2.4a** — dokładny moduł stabilności warunkowej na kuli z osiąganą stałą.
3. **Tw. 4.4** — świadek rozdzielający kohomologię zredukowaną od algebraicznej.
4. **Tw. 4.5** — homotopia spektralna z kontrolą dziedziny.
5. **Przykł. 4.1** — ścisła inkluzja filtrowanych obrazów dokładnych przy równych domknięciach.
6. **Tw. 6.8** — dokładna postać sieczna, warunkowo.
7. **Tw. 7.12 + Kontrprz. 7.4** — nie moja ocena.
8. **Tw. 7.8** — próbkowanie (skromny).

Wspólna cecha siedmiu z ośmiu: **to kontrole ostrości i świadkowie, nie nowe tezy.** Żaden nie
jest nowym twierdzeniem o nowym obiekcie. To jest w porządku i mieści się w punkcie B hierarchii
(„która hipoteza, konkluzja, **ostrość** lub kontrprzykład"), ale trzeba to nazwać wprost, bo
zmienia charakter deklarowanego wkładu.

---

## 4. Luki cytowania, do uzupełnienia niezależnie od ocen

Każda pozycja to liczba trafień w pełnym tekście, sprawdzalna w jednej linii.

| gospodarz | dotyczy | trafień |
|---|---|---|
| R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proc. AMS 17 (1966) 413–415 | Tw. 2.4 | **0** |
| R. Becker, R. Rannacher, *An optimal control approach to a posteriori error estimation in finite element methods*, Acta Numerica 10 (2001); Giles–Süli | Tw. 6.7, 6.8, cały aparat sprzężony rozdz. 6 | **0** |
| Fuglede (1950), Putnam, Rosenblum | Tw. 7.12, przypadek `h=id` i widma rozłączne | **0** |
| T. Fernando, H. Trinh, L. Jennings, *Functional observability and the design of minimum order linear functional observers* (2010) — pojęcie functional observability, zwykła obserwowalność jako przypadek szczególny | Tw. 5, Kontrprz. 3 | **0** |
| B. Liljegren-Sailer, SCL 190 (2024) 105840; Heinkenschloss–Reis–Antoulas, Automatica 47 (2011) 559–564 | gramian i błąd niezerowego warunku początkowego, przy wchłanianiu Tw. 3 z tekstu kandydackiego | **0** |
| Dahlquist (1958), Lozinskii (1958), Söderlind, BIT 46(3) (2006) 631–652 | Tw. 7.3, jeśli (7.1) ma być zaostrzone normą logarytmiczną | **0** |
| Stinespring (1955) | Tw. 5.1 | **0** |

Zakres mojej weryfikacji, uczciwie: dla Douglasa, Fuglede–Putnama, Stinespringa i Ho–Kalmana
opieram się na identyfikacji twierdzenia z pamięci korpusu, bez otwarcia pozycji. Dla
Becker–Rannacher potwierdziłem tytuł i wydawnictwo wyszukiwaniem. Dla Fernando–Trinha–Jenningsa
potwierdziłem istnienie pozycji i to, że wprowadza pojęcie functional observability ze zwykłą
obserwowalnością jako przypadkiem szczególnym — **nie otworzyłem pełnego PDF i nie sprawdziłem,
czy ich kryterium rangowe zawiera warunek typu `ker τ` niezmienniczy względem `A`.** Dla
Liljegren-Sailera przeczytałem pracę i podałem numer wniosku (Cor. 5) w zwrocie 003. Te różnice
zakresu są istotne i nie wolno ich zrównać.

---

## 5. Dwa ustalenia redakcyjne (plan: „Usuń powtórzenia")

1. **Własność uniwersalna ilorazu sformułowana cztery razy** w czterech językach: Tw. 2.1
   (obserwable), Lemat 5.1 (włókna testerów), Tw. 7.1 (rodzina rozdzielająca), oraz Tw. 2.3
   (dynamika). To jedna rzecz. Jedno sformułowanie z czterema zastosowaniami jest krótsze
   i mocniejsze niż cztery twierdzenia.
2. **Kompresja jest reprezentacją ⟺ niezmienniczość** sformułowana dwa razy: rozdz. 1 Tw. 7
   i rozdz. 3 Tw. 3.2, z dwoma różnymi dowodami tej samej tezy.

---

## 6. Obserwacja ramowa — do decyzji Moderatora, nie wniosek

Policzyłem drugą warstwę. **Jawnych non-mapów jest 53**: 13 Kontrprzykładów plus 40 jawnych
zdań negatywnych („nie wystarcza” 11, „nie wolno” 9, „nie oznacza” 7, „nie implikuje” 6,
„nie wynika” 5, „nie dowodzi” 2). Przeciw 68 obiektom numerowanym, z których po odjęciu
osiem jest kandydatami do B.

Czyli gęstość non-mapów jest porównywalna z gęstością twierdzeń, a po subtraction **non-mapy
są liczniejsze niż ocalałe kandydatury B w stosunku ponad sześć do jednego.**

Priorytet 1 planu brzmi: „Rozpoznać »nośne« twierdzenia dla każdej rzeczywistej relacji między
teoriami i zbudować z nich pełne łańcuchy dowodowe." To założenie, że wkład siedzi w twierdzeniach.
Mój rachunek sugeruje przetestowanie alternatywy: że rzeczywistym, oryginalnym produktem tego
manuskryptu jest **atlas tego, co się nie przenosi** — uporządkowany, otypowany zbiór non-mapów
z kontrprzykładami, każdy z nazwanym gospodarzem i jawną klasą ważności. Taka monografia jest
legalnym i rzadkim gatunkiem; nikt nie pisze atlasów nieprzenoszalności, bo nie dają cytowań
za twierdzenia. Byłaby też zgodna z genotypem projektu: błąd zintegrowany jako materiał.

To NIE jest teza, że monografia nie ma wkładu. To pytanie o to, gdzie zadeklarować wkład, żeby
deklaracja wytrzymała recenzję. Gdyby rama pozostała „progresywne twierdzenia”, recenzent zrobi
dokładnie to, co ja zrobiłem w §2, i zostanie mu osiem pozycji, z czego siedem to kontrole
ostrości. Gdyby rama brzmiała „atlas granic przenoszenia opisu efektywnego, z dowodami
i świadkami”, te same 68 obiektów stają się aparatem, a 53 non-mapy — tezą.

**Decyzja o ramie należy do Moderatora i LT4. Ja mogę dostarczyć tylko rachunek.**

---

## 7. Czego nie zrobiłem

1. **Nie sprawdzałem poprawności dowodów** poza Tw. 7.6, 7.7 (zwrot 003, do precyzji maszynowej)
   i Tw. 7.12 z Kontrprz. 7.4 (dzisiaj). To jest własność SW. Subtraction nie jest kontrolą dowodu:
   twierdzenie może być poprawne i w całości należeć do gospodarza, i odwrotnie.
2. **Nie oceniałem Tw. 7.12** — współtworzyłem je i moja wersja była fałszywa. ROLE_COLLAPSE_RISK,
   gdybym je sklasyfikował.
3. **Nie otworzyłem czterech z siedmiu pozycji gospodarzy** wymienionych w §4 — zakres podany
   przy każdej osobno.
4. **Nie oceniałem rozdziału 7 §7.6–7.9** poza obiektami numerowanymi ani wprowadzenia MT13.
5. **Nie dotykałem niczego opartego na moich wynikach J3** — nadal [▷], niezaudytowane siódmy
   dzień.
6. **Klasyfikacja A/B jest moja i podlega audytowi.** Cztery z nich są dyskusyjne na granicy
   (Tw. 4.5, Tw. 6.8, Tw. 7.8, Przykł. 2.4a) i spodziewam się sporu. Spór o te cztery jest
   tańszy niż jego brak.

---

## 8. Rekomendacja operacyjna, jedna

Przed dalszym pogłębianiem: **rozstrzygnąć ramę z §6.** Ośmiu kandydatów B nie da się powiększyć
przez dopisywanie twierdzeń tego samego typu, bo każde nowe twierdzenie elementarne trafia do A
i obniża proporcję. Jeżeli rama ma zostać „progresywne twierdzenia”, to jedyną drogą jest
§6.10 i podobne — pełne, ilościowe zastosowania fizyczne, których plan żąda, a których nie ma.
Jeżeli ramą ma być atlas granic, praca jest w znacznej mierze wykonana i brakuje tylko
jej nazwania oraz uzupełnienia siedmiu cytowań z §4.

---

KONIEC. Status [▷]. EXEC_SIGN brak. Audyt klasyfikacji z §2 obowiązkowy per ANTI-SELF-SEALING.
