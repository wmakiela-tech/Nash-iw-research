# IW/NASH — REC10 ROT06
## Niezależna recenzja PRF11 R14: słaby pomiar i skorelowany szum

**Data:** 2026-10-21  
**Komórka:** IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_09 / REC10  
**Werdykt:** PASS_WITH_STRENGTHENING / EXACT_CLASSICAL_GAUSSIAN / NO_NOVELTY  
**Status przekazania:** raport lokalny; zapis do GitHub i przekazanie do Slack zablokowane przez zabezpieczenia połączeń. Brak potwierdzenia BW ingestion lub owner acceptance.

**Źródło pierwotne:** [PRF11 R14](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-21/IW_PRF11_R14_CORRELATED_NOISE_COVARIANCE_SEAM_WEAK_STORAGE_STATISTICAL_COUNTEREXAMPLE_001_20261021.md). Odczytany blob: `1651db6337a2fdedc2ca96c0ee706b93624c90ab`.

### Model i weryfikacja twierdzenia źródłowego

Dla parametru theta w [-R,R] i 0<s<1 model PRF11 R14 opisuje dwa odczyty o średniej `theta * (s, s(1-s))` oraz wspólnej kowariancji

    Sigma_s = sigma² [[1, -1+s²],
                      [-1+s², 1]].

Macierz jest dodatnio określona dla każdego s>0, przy stałych wariancjach brzegowych sigma². Energia bezszumowego sygnału maleje, ale informacja Fishera wynosi dokładnie

    I_s = (2-s)²/(2sigma²) + s⁴/[2sigma²(2-s²)] -> 2/sigma².

Wzór i liczby źródłowe przechodzą niezależną kontrolę algebraiczną.

### Nowe wzmocnienie: granica całego eksperymentu statystycznego

Zdefiniujmy odwracalnie

    T_s = (Z1+Z2)/(s(2-s)),
    D_s = (Z1-Z2)/sqrt(2).

Przy zadanej wartości theta są to **niezależne** zmienne gaussowskie:

    T_s ~ N(theta, 2sigma²/(2-s)²),
    D_s ~ N(theta*s²/sqrt(2), sigma²(2-s²)).

Samo T_s jest dokładnym eksperymentem gaussowskiego przesunięcia. Odrzucenie D_s jest dopuszczalnym przetworzeniem odczytu. Odtworzenie pełnych danych z T_s przez dołączenie symulowanego D_s o zerowej średniej powoduje błąd KL równy

    KL = theta²*s⁴/[4sigma²(2-s²)].

Z nierówności Pins­kera wynika jednostajnie na theta w [-R,R]:

    TV <= R*s²/[sqrt(8)*sigma*sqrt(2-s²)].

Zatem odległość Le Cama pełnego eksperymentu dwóch odczytów od eksperymentu T_s jest O(s²).

Ponadto wariancja T_s zbiega do sigma²/2. Dla r_s=4/(2-s)² nierówność Gaussa KL/Pinsker daje

    TV(N(theta, v_s), N(theta, sigma²/2))
      <= (1/2)*sqrt(r_s-1-ln(r_s)) = O(s).

Stąd **pełny eksperyment**, a nie tylko jego informacja Fishera, zbiega w odległości Le Cama w tempie O(s) do nietrywialnego eksperymentu `N(theta, sigma²/2)`. Nie jest asymptotycznie równoważny eksperymentowi bez informacji.

Dla straty kwadratowej i theta ograniczonego do [-R,R] estymator można przyciąć do [-R,R] bez pogarszania ryzyka, dzięki czemu strata jest ograniczona przez 4R². Standardowe porównanie eksperymentów daje zbieżność ryzyk minimaksowych do ryzyka granicznego eksperymentu. Nie twierdzimy, że liniowy estymator kurczący z PRF11 osiąga dokładne minimaksowe optimum.

### Test niezależny

Przy sigma²=1/4:

| s | Pełna informacja Fishera | Var(T_s) | Górne ograniczenie TV przy R=1 dla dołączonego D_s |
| ---: | ---: | ---: | ---: |
| 0.1 | 7.2201005025 | 0.1385041551 | 0.00501255 |
| 0.01 | 7.9202000100 | 0.1262594379 | 0.00005000125 |
| 0.001 | ok. 7.9920020 | 0.1251250938 | 0.0000005000001 |

### Granice i dyspozycja

- Jest to klasyczny model o *zależnej od s* prawie osobliwej **wspólnej kowariancji**. Stałe wariancje pojedynczych pomiarów nie zapewniają dolnej granicy na najmniejszą wartość własną całej kowariancji.
- Ustalona klasyczna dynamika resetu i osobno przyjęty gaussowski szum nie dowodzą istnienia fizycznego instrumentu pomiarowego o tych parametrach.
- Wniosek PRF11 R13 o zaniku informacji przy niezależnych innowacjach gaussowskich pozostaje poprawny **w jego własnym modelu**.
- Nie przenosimy tego wyniku automatycznie na adaptacyjne pomiary ze skorelowanymi innowacjami, modele kwantowe, DTC/NCDG ani PBH.
- Otrzymany rachunek jest zastosowaniem dojrzałej teorii gaussowskich eksperymentów statystycznych i porównania Le Cama; **brak twierdzenia o nowości**.

**Disposition:** PASS_WITH_STRENGTHENING. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK. STABLE STOP przy niezmienionym modelu.

**Custody:** plik utworzony jako załącznik do rozmowy. GitHub_write: BLOCKED. Slack_delivery: BLOCKED. Owner_receipt / BW_ingestion: NOT_VERIFIED.

---

### Aktualizacja custody / recovery — 2026-10-22

Historyczne oznaczenia `GitHub_write: BLOCKED` i `Slack_delivery: BLOCKED` w oryginalnym raporcie dotyczą nieudanych prób z 21.10.2026 i pozostają zachowane jako ślad audytowy. **Ponowiony zapis: GitHub WRITE+EXACT READBACK PASS**, commit: `efc43814c7f2ec33373e421ad4a74b7708aa6d97`. **Ponowione doręczenie: Slack SENT+SEARCH READBACK PASS**, wiadomość: https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1792655162182689. Nie stwierdzono BW ingestion, niezależnej akceptacji właściciela, CANON ani EXEC_SIGN.
