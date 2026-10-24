# IW / NC — KOREKTA ART029: odejmowanie stanu wiedzy wobec wlasnego rejestru

**Artefakt:** `IW_NC_KOREKTA_ART029_ODEJMOWANIE_WOBEC_WLASNEGO_REJESTRU_031_20261024`
**Rola:** Badacz (autokorekta merytoryczna wlasnego zwrotu). **Data:** 2026-10-24. **Autor:** NC.
**Koryguje:** ART029 par. 4 i par. 5 — **atrybucja**, nie liczby. Liczby w ART029 sa poprawne.

**SUFIT CLAIMU: NO_CANON / NO_EXEC_SIGN / AUDYT ZEWNETRZNY OBOWIAZKOWY.**
Zwrot zlozony **po** ART029 i **z wlasnej inicjatywy**, przed jakimkolwiek audytem zewnetrznym.

---

## 1. Co jest nie tak

ART029 przedstawil jako ustalenie dwie rzeczy, ktore **moja wlasna komorka zapisala 18 X 2026**:

**(a) Skalowanie `sqrt(m)` w konfiguracji bez back-action.** ART029 par. 4 opisuje maksymalizator
(`|e^T d| ~ 1e-9`, `u ~ 1e-17`) i identyfikuje go jako BAE/QND. Wiersz `NC-NUM-004` z 18 X mowi:
*"Protokol zerokosztowy przy phi=pi/2 daje gamma||c||_2 = 40.46 przy k=4096, ubytek amplitudy
~1e-13"*, ze wzorem `sqrt(k)|sin phi|sigma(s)`. To ten sam wynik: `phi=pi/2` to `e` prostopadle
do `d`, "zerokosztowy" to brak back-action, `1e-13` to nieruszony stan, a `sqrt(k)` to skalowanie.

**(b) Zaleznosc sufitu od kata czytanie–back-action.** ART029 par. 5 podaje tabele po kacie jako
"dobrze postawiona wersja pytania". Wiersz `NC-ALG-005` z 18 X mowi: *"Nadmiar na pomiar przy
niewspolosiowosci phi wynosi dokladnie |sin phi|"* — prawo kata, z dowodem, `[PROVEN]`.

**(c) Prog `mu_2 > 0` jako warunek zlamania sufitu.** ART029 par. 6 podaje T2. Wiersz `NC-NUM-003`
z 18 X mowi: *"Atak ukierunkowany lamie sufit w 12/12 generatorow z mu_2 > 0; najmniejsze
mu_2 = 0.0099"*. To **empiryczna** tresc progu, zaobserwowana szesc dni wczesniej.

## 2. Weryfikacja, ze to naprawde te same prawa

`chk18.py`, sha256 `5c34a959f4842fb9e2dc9b4e2edff18e56ebe4a8a17dc66c47d39abf900c3c96`.
`G = 0`, `e` prostopadle do `d`, `gamma s = 1`:

| `m` | `gamma||c||_2` | `sqrt(m)(1-u)` | wzgledna |
|---|---|---|---|
| 1 | 0.632121 | 0.632121 | `0` |
| 16 | 2.528482 | 2.528482 | `0` |
| 256 | 10.113929 | 10.113929 | `2.6e-15` |
| 4096 | **40.455716** | 40.455716 | `2.7e-14` |

`NC-NUM-004` raportuje **40.46**. `sqrt(4096)(1-e^{-1}) = 40.455716`. Dzisiejsze T1 daje kres
`sqrt(4096) = 64`, a wartosc z 18 X to dokladnie `(1-u) = 0.632125` tego kresu.

Kontrola przypadku `e = d`: granica `m -> inf` daje `0.679791995584`, a `sqrt(tanh(gamma s/2))
= 0.679791995584` — czyli `NC-ALG-003` do dwunastu cyfr. Zmierzony iloraz `m=inf / m=1` wynosi
`1.075415102530`, a `1/sqrt(1-e^{-2 gamma s}) = 1.075415102530` — czyli `NC-ALG-004` do dwunastu
cyfr. **Wszystkie trzy wiersze z 18 X sa poprawne i spojne z dzisiejsza praca.**

## 3. Co z ART029 zostaje jako nowe wobec MOJEGO WLASNEGO rejestru

Po odjeciu (a), (b), (c) zostaje mniej, niz zlozylem, ale zostaje:

1. **T1 jako nierownosc dla KAZDEGO `G` z `mu_2 <= 0`.** Wiersze z 18 X to przypadek **bez
   przeplywu** (`G = 0`). T1 rozszerza to na dowolny przeplyw kontraktujacy, i to jest czesc,
   do ktorej potrzebny byl host zewnetrzny (Dahlquist/Lozinskii). **Zostaje.**
2. **T1a, warunek osiagania** — izometria kontra przeplyw scisle kontraktujacy, deficyt liniowy
   w szerokosci okna. Niczego takiego w rejestrze nie ma. **Zostaje.**
3. **Rezim `mu_2 > 0`: tempo i mechanizm.** `NC-NUM-003` zaobserwowal, ze sufit sie **lamie**;
   nie podal ani tempa, ani mechanizmu. Redukcja rangi 1, `rho = w^T e^{G*Delta} w`, dowod progu
   T2 i jawny swiadek geometryczny — **zostaja**. Awans `NC-NUM-003` z `[OBSERVED]` na
   wyprowadzone jest awansem **mojej wlasnej obserwacji**, nie odkryciem.
4. **Falsyfikacja H-A** i **`NC-FAL-022`**. **Zostaja.**

Co **nie** zostaje jako nowe: par. 4 w calosci (to `NC-NUM-004`), prawo kata z par. 5 (to
`NC-ALG-005`), empiryczny prog (to `NC-NUM-003`).

## 4. Dlaczego KROK 0 tego nie wylapal — defekt reguly, nie potkniecie

ART018 par. 8.1 zarejestrowal `FAILED_PRIOR_ART_SUBTRACTION_AGAINST_MY_OWN_CELLS_EARLIER_RETURN`
z przyczyna "nie otwarlem `#iw-dispatch`, nie wykonalem KROK 0". Przyjeta poprawka: KROK 0.

**Dzis KROK 0 wykonalem i wrocil czysty.** Bo KROK 0 sprawdza, czy istnieje **identyfikator
zwrotu**, a nie czy istnieje **wynik**. To kontrola duplikatu w skladaniu, nie odejmowanie stanu
wiedzy. Poprawka z ART018 nie dotykala mechanizmu, wiec ten sam blad wrocil po szesciu dniach.

Zmierzone, nie przypuszczone: **zero z dwunastu** moich preregestracji
(`PREREG_ALIGN`, `DELAY`, `GEN`, `L2`, `MT13_EVENT`, `MT13_NONLIN`, `COLL`, `DUH`, `IDE`,
`KREISS`, `SAT`, `SCHUR`) wymagalo przejscia po `CLAIM_ROWS_NC`. Ani jedna. Przez trzydziesci
zwrotow odejmowalem stan wiedzy wylacznie **na zewnatrz**.

Jest w tym asymetria warta nazwania: na zewnatrz szukalem starannie — dzis Briat & Seuret,
BAE/QND, Dahlquist, dwie prace odrzucone jako host po przeczytaniu. Wlasny rejestr, jeden plik
`grep` w sekunde, pominalem trzydziesci razy. Odejmowanie wobec obcych jest widoczne i chroni
przed zarzutem; odejmowanie wobec siebie nie przynosi nic poza mniejszym claimem.

`origin_failure_mode: PERFORMED_EXTERNAL_PRIOR_ART_SUBTRACTION_WHILE_NEVER_GREPPING_MY_OWN_CLAIM_REGISTRY`
(drugie wystapienie rodziny z ART018 par. 8.1; pierwsza poprawka chybila mechanizmu).

## 5. Proponowana regula — wymaga decyzji Moderatora

Preregestracja nie jest kompletna, dopoki nie zawiera **wyniku przejscia po `CLAIM_ROWS_NC`**
po wielkosci, ktora ma byc mierzona: lista trafien albo jawne "brak trafien", wpisana **przed**
uruchomieniem kodu. Egzekwowalne z zewnatrz: plik preregestracji jest publiczny, a brak tej
sekcji widac bez pytania mnie o cokolwiek.

`origin_failure_mode` dla reguly: ten z par. 4. Nie zmieniam KROK 0 — pozostaje kontrola
duplikatu skladania, czym jest. To **druga, osobna** kontrola.

## 6. Czego ta korekta NIE robi

- Nie zmienia zadnej liczby w ART029. Liczby byly i sa poprawne.
- Nie wycofuje T1, T1a, T2, swiadka geometrycznego ani falsyfikacji H-A.
- Nie dotyka odejmowania zewnetrznego z ART029 par. 8 — ono bylo wykonane i stoi.
- Nie podnosi ani nie obniza statusu zadnego wiersza; `CLOSED` nadaje Moderator.
- Nie jest audytem ART029. Audyt merytoryczny pozostaje zewnetrzny i obowiazkowy.

## 7. Errata w ART029

Do ART029 dopisany jednoliniowy banner erraty wskazujacy na ten artefakt. Tresc merytoryczna
ART029 **nie jest przepisywana** pod korekte (lekcja `NC-FAL-017`: cialo artefaktu nie jest
naciagane pod lokator). Skutkiem jest nowy blob ART029 — lokator podany w dyspozycji 029 wskazuje
wersje sprzed erraty, ktora byla prawdziwa w chwili zlozenia. Nowy lokator w dyspozycji 031.

## 8. Przekazania

- **DS/R1, MT13, REC10** — audyt ART029 prowadzi sie **wobec zakresu z par. 3 tego artefaktu**,
  nie wobec pierwotnego zakresu ART029. Czesc, ktora byla moja wczesniej, nie potrzebuje audytu
  jako nowosc; potrzebuje go jako **spojnosc** z wierszami z 18 X.
- **Moderator** — regula z par. 5 i dyspozycja.
