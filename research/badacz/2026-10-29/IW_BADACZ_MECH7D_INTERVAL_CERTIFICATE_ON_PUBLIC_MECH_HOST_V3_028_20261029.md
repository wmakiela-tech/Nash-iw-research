---
artifact_id: IW_BADACZ_MECH7D_INTERVAL_CERTIFICATE_ON_PUBLIC_MECH_HOST_V3_028_20261029
exposure: PUBLIC
claim_ceiling: CONSTRUCTIVE_[▷] / RIGOROUS_SOLVER_ERROR_BOUND_ON_PUBLIC_MECH_ROT006_HOST (conditional on mpmath.iv correctness and on the host model as defined) / NOT_MECH_ROT035_TRAJECTORIES / NO_PHYSICAL_PBH_BBN / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: RESULT
result_class: RESULT
task_id: BADACZ-MECH-GATES-003
responds_to: AUD1 ROT010 (warunek awansu 1: wykonanie v2 na hoście zgodnym ze źródłem); Mech-S7 ROT035 (OPEN: ścisły certyfikat błędu ODE)
code: research/badacz/2026-10-29/code/mech7d_interval_certificate_v3_owner_host.py (sha256 655fe01a5da948fed8dcba8866844547caf21c0c406c0fbfec9ad5e153fbe5bb); importuje bez zmian mech7d_interval_certificate_v2.py (sha256 0b324062b79f946f134b0cb25c578b61f7c08cb7dc49c1b75c77722d88448d38)
host_inputs: GitHub Actions artifacts 12116193467 (sha256 75766c5b…, = PUB z Mech ROT006) i 12192535869 (sha256 3b24f50c…, = PAP), repo wmakiela-tech/Nash-iw-research; wygasają 2027-01-15 i 2027-01-17
output_sha256: b8252fbd654d843acf714388e880ccf678b86a84af682c40dd1d2a54bbdcc87d (mech7d_interval_certificate_v3_owner_host.json)
code_r2: research/badacz/2026-10-29/code/mech7d_interval_certificate_v3_1_owner_host.py (sha256 ebad2394e5efd1b9ab99484685d1f22f27b483b03ca172a99b1ec1df3534b1fc), v3.1 po AUD1 ROT014
output_sha256_r2: 84cf3cb097b26250c0c97454f6650852bda9436322915f3ac743855d928f98c6 (mech7d_interval_certificate_v3_1_owner_host.json)
revision: r3 (30 X) — nota o kontrakcie nośnika po AUD1 ROT016 (argument formalny, bez zmiany kodu i wyników); r2 (29 X, commit 675404f) — naprawa po AUD1 ROT014: v3 nie był formalnie ścisłym certyfikatem (wybór segmentu PCHIP i brzeg nośnika decydowane na zaokrąglonym floacie); v3.1 domyka obie luki, dodaje ścisły certyfikat dodatniości i testy regresyjne; liczby bez zmian (identyczne co do bitu); r1 = commit 5b6bf45
---

# Certyfikat błędu solvera v2 na publicznym hoście Mech-S7 ROT006 (v3 → v3.1)

**Status:** `[▷]`. Wynik Claude'a, wymaga audytu spoza rodziny Claude. Kod przedziałowy v2 (doc 025)
jest importowany **bez zmian**. AUD1 ROT010 nadał mu status `CONDITIONAL_ALGORITHMIC_REPAIR_SUPPORTED`.

**ERRATUM r2 (po AUD1 ROT014, 29 X).**
- **Luka 1 (AUD1).** W v3 obwiednia PCHIP wybierała segmenty po zaokrągleniu końców przedziału do
  `float64`. Przedział tuż poniżej węzła mógł wtedy pominąć lewy segment. Kontrprzykład AUD1:
  `PCHIP(t) = t`, `t ∈ [1 − 1e-20, 1 + 1e-20]` daje obwiednię `[1, …]`, która nie zawiera `1 − 1e-20`.
  W r1 przymiotnik „ścisły” nie był więc formalnie uzasadniony.
- **Luka 2 (ta sama klasa, znaleziona przy naprawie).** Człon Gegenbauera był włączany według flagi
  liczonej ze zmiennoprzecinkowego środka kawałka. Kawałek przecinający brzeg nośnika z dokładnością do
  zaokrąglenia mógł dostać obwiednię bez tego członu na wąskim pasku.
- **Naprawa (v3.1).**
  - Segmenty wybieram porównaniami w wysokiej precyzji, z zapasem ±1 segment, i sprawdzam, że
    pokrywają cały przedział.
  - Na kawałku, którego `x` przecina `±1`, człon jest obwiedziony przez hull wartości na części
    wewnętrznej z zerem. To jest poprawne, bo `k` znika na brzegu do rzędu 3.
  - Dodatniość źródeł mam teraz z certyfikatu przedziałowego, a nie z gęstej siatki float.
  - Testy regresyjne uruchamiają się przed obliczeniem i przerywają je przy porażce: oba przykłady
    AUD1, 1500 losowych punktów przy węzłach dla wartości i pochodnej, test brzegu nośnika oraz kontrola
    negatywna (stary selektor pomija lewy segment).
- **Wynik po naprawie.** 25 kawałków przecinało brzeg nośnika i są teraz obsłużone. `ε_X` oraz liczby
  kawałków są **identyczne co do bitu** z r1. Luka była formalna, nie liczbowa, i jest domknięta. Liczby
  w tabelach poniżej obowiązują teraz jako wynik v3.1.

**NOTA r3 (po AUD1 ROT016, 30 X): które ODE jest certyfikowane.**
- **Uwaga AUD1.** Model float (`G_f_host`) włącza perturbację dla `0.07 < u < 0.92`. Model przedziałowy
  (`src_g`) włącza ją dla `|x(u)| < 1`, gdzie `x = (ln u − ZM)·fl(2/Lz)`, a `ZM` i `Lz` są stałymi binary64.
  To różne zbiory: różnią się o pasy szerokości około `4.5e-18` przy `u = 0.07` i `1.2e-16` przy
  `u = 0.92`, w których `|k| ~ 1e-64`.
- **Kontrakt (doprecyzowanie, kod bez zmian).** Certyfikowane jest ODE zdefiniowane przez model
  przedziałowy `G_g`: tło PCHIP i pole Mech ROT006, a perturbacja na `|x(u)| < 1` z dokładnie tymi
  stałymi binary64.
  - Model float służy wyłącznie do wygenerowania przybliżenia `ŷ`, czyli wielomianów kolokacyjnych
    Radau.
  - Certyfikat ogranicza `|y − ŷ|` dla rozwiązania `y` ODE `G_g` przez obwiednię defektu
    `r = ŷ′ − G_g(s, ŷ)` liczoną z `G_g`. Każda niezgodność `G_f` z `G_g`, także w tych pasach, jest
    częścią `r` i jest obwiedziona.
  - Wybór nośnika w `G_f` nie wpływa więc na ważność ograniczenia, tylko ewentualnie na jego wielkość,
    tu niezauważalnie.
- **Dokładna informacja w certyfikowanym modelu.** `x` jest funkcją afiniczną `z = ln u`, a nośnik to
  `|x| < 1`. Ortogonalność Gegenbauera daje więc dokładnie zerowe momenty `∫ u³ δQ z^j dz`, `j = 0, 1, 2`,
  przy dowolnych stałych afinicznych, w tym binary64. Suma par jest zachowana punktowo.
- **Pozostałe elementy dotyczą tego samego modelu.** Certyfikat dodatniości liczony jest na `|x| ≤ 1`.
  Dno dwupunktowe `|ŷ₊ − ŷ₋|/2 − (ε₊ + ε₋)/2` jest ścisłe dla rozwiązań ODE `G_g`.
- **Wniosek.** Bez ponownego przebiegu: liczby r1/r2 obowiązują dla tak zdefiniowanego modelu. Względem
  modelu, w którym nośnik ma dokładnie rzeczywiste końce `0.07` i `0.92`, oba różnią się tylko w pasach
  poniżej ULP o źródło rzędu `1e-60` względnie. Tej różnicy nie zaliczam do certyfikatu.

## Wynik

1. **Host Mech jest publiczny i odtworzony co do bitu na wejściu.**
   - Archiwa, z których Mech ROT006 bierze tło `T(t)`, `a(t)` i stan na krawędzi, to publiczne
     artefakty GitHub Actions tego repozytorium. Ich sha256 są **identyczne** z przypiętymi w kodzie
     Mech (`PUB`, `PAP`).
   - Moja reimplementacja pola 7D daje `X_target = 0.3978013205256`, a publiczna funkcja Mech
     `simulate()`, wywołana na tych samych plikach, `0.3978013205257`. Różnica `1.6e-13`;
     `t_eval = 215.172386 s` jest identyczne.
2. **Ścisłe ograniczenie błędu solvera na prawdziwym tle.**
   - Dla dwóch świadków `±` z klasy dokładnej informacji (Twierdzenie E z doc 022, ta sama klasa co w
     Mech ROT035) przy `rtol = 3e-9`:

     | świadek | `X_target` | ścisłe `ε_X` | błąd diagnostyczny (wobec `rtol = 1e-12`) |
     |---|---:|---:|---:|
     | `+` | 0.39795437081 | `1.360e-7` | `9.8e-11` |
     | `−` | 0.39764825705 | `1.366e-7` | `7.2e-11` |

   - Ograniczenie obejmuje błąd diagnostyczny z zapasem około 1400 razy.
3. **Ścisłe dno dwupunktowe w tym hoście.**
   - Połowa luki `1.5306e-4`; po odjęciu obu `ε` zostaje **`1.5292e-4`, czyli 99,91% połowy luki**.
   - Oba źródła mają **dokładnie** te same momenty komowujące `j = 0, 1, 2` każdego gatunku, tę samą
     sumę par punktowo i te same pozostałe gatunki.
   - Wniosek: każdy estymator `X_target`, który widzi tylko te dane, myli się o co najmniej `1.5292e-4`
     dla jednego z dwóch źródeł. **Liczba ta jest ścisła względem błędu numerycznego ODE**, w obrębie
     warunkowego modelu Mech ROT006.

## 1. Co zostało certyfikowane

- **Równanie.**
  - Pole 7D `y = (X, n_π⁻, n_π⁺, n_K⁻, n_K0L, n_p̄, n_n̄)` jest takie jak w Mech ROT006: kurs słaby,
    konwersje, rozpad i straty. Tło `T(t)` i `ln a(t)` to `PchipInterpolator` na węzłach zarchiwizowanej
    trajektorii `public_exec`; współczynniki PPoly są dokładnie tymi liczbami zmiennoprzecinkowymi,
    których używa model.
  - Faza A: `u = M/10⁹ g` od 1 do `U_cut`, ze źródłem ROT006 (prawo „public”, mapa „exec”). Faza B:
    `t ∈ [t_cut, t_eval]`.
  - Stan początkowy: wiersz 1469 archiwum przeniesiony na krawędź tablicy (wariant `archive` z ROT006).
- **Źródło perturbowane.**

      Q_p̄ → Q_p̄ + amp·Q1[3]·k(x)/u³,
      Q_n̄ → Q_n̄ − amp·Q1[3]·k(x)/u³,
      0.07 < u < 0.92,
      k = (1 − x²)⁴ Σ_{l=3..10} a_l C_l^(9/2)(x).

  - Kierunek `a` to znormalizowany gradient `X_target` po `a_l`, liczony różnicami skończonymi; składowe
    w wyniku JSON. Amplituda `amp = 0.7 ×` maksimum dopuszczone przez dodatniość obu gatunków.
    W r2 dodatniość jest certyfikowana przedziałowo: na 4000 podprzedziałach `x ∈ [−1, 1]`
    `|δ| / min(Q_p̄, Q_n̄) ≤ 0.7067 < 1`.
  - To **nie** są świadkowie Mech ROT035: tam stan na krawędzi pochodzi z naprawionego 10-składnikowego
    mostu ROT013, a kierunki z rzutu Riesza. Te dane są w lokalnym ZIP-ie u Moderatora.
- **Arytmetyka.**
  - Rdzeń jest niezmieniony z v2: obwiednie przedziałowe na całych kawałkach, defekt w postaci centrowanej
    z pochodną z dualnej arytmetyki przedziałowej, bootstrap na całym kawałku ze ścisłą inkluzją, porównanie
    skalarne ze sprzężeniem gwiazdowym.
  - Nowe w v3: obwiednia przedziałowa i dualna dla PCHIP (hull po wszystkich przedziałach węzłowych, które
    przecina argument) oraz cięcie kawałków w każdym węźle PCHIP (faza B: 32 węzły).
  - Liczba kawałków: faza A około 38 tys. (30 tys. podziałów adaptacyjnych), faza B około 20 tys.
- **Dominujący wkład.** `ε_X` po fazie A wynosi `1.38e-7`, a w fazie B nieco maleje. Błąd pochodzi więc
  z krótkiej (0,24 s), bardzo sztywnej fazy źródłowej.

## 2. Co z tego wynika dla AUD1 ROT010 i Mech ROT035

- **AUD1, warunek awansu 1** („execution against a source-legal host”).
  - Kod v2 został wykonany na hoście Mech z publicznym, sprawdzonym sha256 tłem, a nie na tle
    syntetycznym `T = √(1.32/t)`.
  - Wykonanie jest jednak moje, nie niezależne. Wystarczy ponowne uruchomienie przez komórkę spoza
    rodziny Claude (instrukcja w „Odtworzenie”).
  - Pozostałe warunki AUD1 (pełna weryfikacja `mpmath.iv`, most 10D, fizyczne źródło) pozostają otwarte.
- **Mech ROT035, OPEN „strict endpoint ODE solver error certificate”.**
  - Ten sam kod obsłuży trajektorie ROT035, jeśli dostanie ich stan na krawędzi (7 liczb dla
    `χ_EM = 0.5`) oraz współczynniki `a_l` i amplitudy świadków.
  - Przy luce ROT035 `3.86e-4` i spodziewanym `ε` rzędu `1e-7` dno będzie bliskie 100% połowy luki.
  - Uwaga: stan na krawędzi z mostu 10D sam ma błąd numeryczny. v3 przyjmuje go jako `eps0`, ale
    certyfikat mostu 10D wymaga osobnego sprawdzenia, czy ma strukturę gwiazdy.
- **Custody.**
  - Host istnieje publicznie tylko jako artefakty Actions, które wygasają 15 i 17 I 2027.
  - Propozycja dla właściciela (Mech-S7/SYSS5/KN12): utrwalić oba pliki ZIP w repozytorium albo w
    Drive. Decyzja o ekspozycji należy do właściciela i Moderatora.

## Czego nie twierdzę

- Że to są trajektorie ani luki Mech ROT035.
- Że model Mech ROT006 jest fizyczny: źródło poniżej `10⁹ g` jest syntetyczne, oryginalny Julia 10D nie
  był uruchamiany, brak mostu 10D, Yp, D/H i ograniczeń PBH.
- Że `mpmath.iv` jest formalnie zweryfikowane.
- Że gradient daje kierunek optymalny w jakiejkolwiek normie. To tylko kierunek demonstracyjny.

## Literatura i dorobek projektu

- **Zewnętrzna:** porównanie Müllera–Kamkego (Walter, *Differential and Integral Inequalities*, 1970);
  postać centrowana i arytmetyka przedziałowa (Moore, Kearfott, Cloud, *Introduction to Interval
  Analysis*, 2009); kolokacja Radau IIA (Hairer, Wanner, *Solving ODEs II*).
- **Własna:** doc 022 r3, doc 025, AUD1 ROT009/ROT010, Mech-S7 ROT006 (host), ROT035 (zastosowanie
  klasy E), LT6 ROT009.
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3 mpmath==1.3.0 pandas
gh api repos/wmakiela-tech/Nash-iw-research/actions/artifacts/12116193467/zip > pub.zip   # sha256 75766c5b…
gh api repos/wmakiela-tech/Nash-iw-research/actions/artifacts/12192535869/zip > pap.zip   # sha256 3b24f50c…
python3 -I research/badacz/2026-10-29/code/mech7d_interval_certificate_v3_1_owner_host.py \
  --pub pub.zip --pap pap.zip \
  --mech006 research/mech-s7/2026-10-23/terminal_7d_exact_mass_common_background_006.py --out <katalog>
```

Około 35 minut na jednym rdzeniu. Pobranie artefaktów wymaga zalogowania do GitHub. Dwa przebiegi v3.1
(równolegle, na dwóch rdzeniach) dały identyczny JSON (`84cf3cb0…`). Testy regresyjne uruchamiają się
na początku i przerywają przebieg przy porażce. Plik v3 (r1) zostaje w repozytorium jako obiekt audytu
AUD1 ROT014; nie należy go używać.

## Powrót w trzech warstwach

- **Wynik:** pierwsze ścisłe ograniczenie błędu solvera na prawdziwym tle Mech. Dno dwupunktowe
  `1.5292e-4` (99,91% połowy luki) dla świadków z dokładnie równymi momentami.
- **Konfiguracja:** kluczowe dane hosta leżały publicznie jako artefakty Actions, ale żaden raport nie
  wskazywał ich jako takich. Znalazłem je po sha256. Wąskie gardło „dane tylko w lokalnym ZIP-ie”
  bywa pozorne: warto sprawdzać artefakty i wydania repozytorium, zanim poprosi się o przekaz.
- **Uczenie systemu:**
  - `origin_observation: PUBLIC_HOST_INPUTS_HIDDEN_AS_CI_ARTIFACTS_WITH_EXPIRY`. Kandydat na regułę
    `[▷]`: każdy raport korzystający z artefaktów CI podaje ich ID i datę wygaśnięcia, a właściciel
    utrwala je przed wygaśnięciem.
  - **r2:** origin_failure_mode `FLOAT_ROUNDED_DECISION_INSIDE_INTERVAL_CODE`: wybór segmentu i flagę
    nośnika ustalałem na zaokrąglonych floatach, choć arytmetyka była przedziałowa. Łatka: każda
    decyzja dyskretna w kodzie przedziałowym zapada na porównaniach dokładnych albo pokrywa obie
    możliwości (hull). Do tego testy regresyjne z przykładami przeciwnika przed każdym przebiegiem.
    Błąd znalazł zewnętrzny audyt (AUD1, rodzina GPT).
  - Dla mnie: v2 zadziałał na nowym tle po dodaniu tylko obwiedni PCHIP. Rozdzielenie rdzenia
    przedziałowego od modelu hosta się opłaciło.
