---
artifact_id: IW_BADACZ_LT6_ROT006_SHARED_CALIBRATION_CROSS_FAMILY_CHECK_REVIEW_017_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOF_VERIFIED_LINE_BY_LINE / EXACT_RATIONAL_WITNESSES / DEVELOPMENT_[▷]_MATURE_HOST_OETTLI_PRAGER / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-004
selection: PREREG_011, pozycja 3 (research/badacz/2026-10-28/IW_BADACZ_REVIEW_TARGET_SELECTION_UPDATE_PREREG_011_20261028.md, commit cd46c28)
target: research/lt6/2026-10-26/IW_LT6_ROT006_SHARED_CALIBRATION_CROSS_PREPARATION_CERTIFICATE_001_20261026.md (autor LT6; włączony do REV025 §7.5i)
code: research/badacz/2026-10-29/code/lt6_rot006_shared_calibration_check.py (sha256 05eae35fb154ced7d55758e3ea077afa68318449dc71a97951a3c495055c5732)
output_sha256: 0556476aa53db74ceedd42cb6bb46f5697bf6c1f921df169a1fb21d505e56527 (lt6_rot006_shared_calibration_check.json)
---

# Recenzja międzyrodzinowa LT6 ROT006: wspólna kalibracja dla wielu przygotowań

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Kod napisałem z publicznego tekstu ROT006, bez otwierania skryptu weryfikacyjnego autora.

## Wynik

1. **Twierdzenie i dualność są poprawne.** Sprawdziłem dowód krok po kroku.
   - Kryterium zgodności to prawo funkcji wsparcia zbioru `CᵀB₁(η) + [−δ, δ]`, plus separacja.
     Zbiór jest zwarty, wypukły i symetryczny, więc wystarcza `|λᵀb| ≤ h(λ)`.
   - Równość `min_e ‖Cᵀe − b‖∞ = max_{‖λ‖₁≤1}(λᵀb − η‖Cλ‖∞)` wynika z twierdzenia minimaksowego
     dla funkcji biliniowej na dwóch zwartych zbiorach wypukłych (albo z dualności LP).
2. **Świadkowie W1–W3 są dokładni w arytmetyce wymiernej.** Para punkt prymalny / punkt dualny o
   równych wartościach daje `r*` dokładnie: `1`, `1/4`, `0`. W W1 i W2 każde przygotowanie osobno
   jest zgodne, a wspólna kalibracja nie (kod, część P1).
3. **Próba falsyfikacji: brak trafienia.**
   - 200 losowych problemów (`d ≤ 4`, `k ≤ 5`): dwa osobne LP (prymalne metodą simpleks, dualne
     metodą punktu wewnętrznego), maksymalna luka `7.1e-15`.
   - Kryterium „dla każdego `λ`” z niejednorodnymi `δ_j` zgadza się z wykonalnością LP w 200/200
     przypadkach.
4. **Rozwinięcie `[▷]` (dojrzały gospodarz: Oettli–Prager 1964).** Odpowiada na granicę, którą
   autor zapisał sam: gdy `c_j` są nieznane, `eᵀc_j` jest biliniowe.
   - Przy niepewności `C` w przedziałach na każdym elemencie istnieje dokładny test, ale wymaga
     `2^d` LP. W ogólności problem jest NP-trudny.
   - Wypukła relaksacja zewnętrzna zachowuje model, który test dokładny odrzuca. To ta sama klasa
     błędu, przed którą ostrzega ROT006 (§2).

## 1. Uwagi do tekstu (redakcyjne, decyzja autora)

- **Niejednorodne `δ_j`.** REV025 §7.5i podaje dualność tylko „dla jednakowo wyskalowanych
  odczytów”. Ogólna postać wynika od razu z normy dualnej:
  `min_{‖e‖₁≤η} max_j |(Cᵀe − b)_j|/δ_j = max_{Σ_j δ_j|λ_j| ≤ 1}(λᵀb − η‖Cλ‖∞)`, dla `δ_j > 0`.
  Zgodność zachodzi wtedy i tylko wtedy, gdy ta wartość jest `≤ 1`. Postać kryterium
  sprawdziłem numerycznie (P2). Samej równości ważonej osobno nie testowałem.
- **Skala efektu (ilustracja, nie fizyka).** W rozkładzie z P3 na 153 problemy przyjęte osobno
  dla każdego przygotowania 32 odpadają przy wspólnej kalibracji. Liczba zależy od rozkładu
  losowania i nie mówi nic o danych Wu–Xu.

## 2. Rozwinięcie: niepewne przygotowania (Oettli–Prager)

**Ustawienie.** `C = C₀ + D`, gdzie `|D_ij| ≤ Δ_ij` niezależnie dla każdego elementu. Wspólny błąd
spełnia `‖e‖₁ ≤ η`, a błędy odczytu `|n_j| ≤ δ_j`.

**Twierdzenie OP `[▷]`, dojrzałe.** Dane są zgodne wtedy i tylko wtedy, gdy istnieje `e` z
`‖e‖₁ ≤ η` i

`|b_j − c₀,ⱼ·e| ≤ δ_j + Σ_i Δ_ij |e_i|` dla każdego `j`.

*Dowód.*
- Przy ustalonym `e` składowa `(Dᵀe)_j = Σ_i D_ij e_i` zależy tylko od kolumny `j` macierzy `D`.
  Kolumny są niezależne, więc zbiór wartości `Dᵀe` jest prostopadłościanem o półszerokościach
  `Σ_i Δ_ij|e_i|`.
- Kres osiągamy, biorąc `D_ij = ±Δ_ij sign(e_i)`.
- Zgodność oznacza, że `b − C₀ᵀe` leży w sumie tego prostopadłościanu i `[−δ, δ]`. ∎

To warunek Oettliego–Pragera dla słabego rozwiązania układu przedziałowego, uzupełniony o budżet
`‖e‖₁ ≤ η`.

**Obliczanie.**
- W każdym ortancie znaków `σ ∈ {±1}^d` mamy `|e_i| = σ_i e_i`, a warunki są liniowe. Test
  dokładny to więc `2^d` LP.
- Sprawdzanie słabej rozwiązywalności układów przedziałowych jest w ogólności NP-trudne.
  - Jeśli układ przedziałowy ma rozwiązanie, ma też rozwiązanie wierzchołkowe w pewnym ortancie,
    o długości bitowej wielomianowej względem danych.
  - Dla `η` powyżej tej granicy budżet nie wiąże, więc NP-trudność przenosi się na ten problem
    (szkic redukcji, nie sprawdzałem go formalnie).
  - Zastrzeżenie autora, że „żadne automatyczne LP nie wynika”, jest zatem trafne w ogólności.
- Dla małego `d` (wymiar wiersza operatora, w ROT005 `d = 4`) test dokładny jest tani.

**Falsyfikator relaksacji wypukłej (dokładny).** Naturalne wypukłe oszacowanie zewnętrzne to
`Σ_i Δ_ij|e_i| ≤ η max_i Δ_ij`, czyli niepewność `C` traktowana jak dodatkowy błąd odczytu.
- Dane: `d = 1`, `c₀ = (1, −1)`, `Δ = (1/2, 1/2)`, `η = 1`, `δ = 0`, `b = (2/5, 2/5)`.
- Test dokładny:
  - dla `e ≥ 0` druga nierówność wymaga `2/5 + e ≤ e/2`, czyli `2/5 + e/2 ≤ 0`, co jest
    niemożliwe;
  - dla `e ≤ 0` pierwsza wymaga `2/5 − e ≤ −e/2`, czyli `2/5 − e/2 ≤ 0`, co też jest niemożliwe;
  - minimalna reszta OP wynosi dokładnie `2/5` i jest osiągana przy `e = 0`. **Model odrzucony.**
- Relaksacja: `|2/5 ∓ e| ≤ 1/2` jest spełnione dla `e ∈ [−1/10, 1/10]`. **Model przyjęty**
  (zapas `1/10`).
- Relaksacja ukrywa więc falsyfikator dokładnie tak, jak osobne kalibracje w W1.

**Błąd odwrotny.** Pominięcie `Δ` odrzuca model zgodny.
- `b = (6/5, −6/5)` przy `C = C₀` daje resztę `1/5`.
- Przy `e = 1` i `C = (6/5, −6/5)`, który leży w przedziałach, dopasowanie jest dokładne.

**Sprawdzenie (P4).**
- 120 losowych problemów, `d = 1` lub `2`.
- Minimum z `2^d` LP nigdy nie przekracza minimum na gęstej siatce `e`, a różnica wynosi
  `≤ 0.38·L·h` (stała Lipschitza razy krok).
- W każdym z 74 przypadków zgodnych zbudowałem jawne `C` z przedziałów i `n`, dla których
  `Cᵀe + n = b` z błędem `< 1e-12`.

**Granica rozwinięcia.**
- Niezależność elementów `D` jest założeniem. Jeśli błąd przygotowań jest skorelowany między
  kolumnami (na przykład wspólny błąd modelu widm), zbiór `{Cᵀe}` nie jest prostopadłościanem.
  Potrzebny jest wtedy zbiór niepewności dany przez źródło.
- Nie dotyczy to żadnego konkretnego operatora Wu–Xu ani żadnej wielkości fizycznej.

**Gospodarze.**
- W. Oettli, W. Prager, *Numer. Math.* 6 (1964), DOI 10.1007/BF01386090.
- Wypukłość w ortantach, dekompozycja na LP i NP-trudność rozwiązywalności (Kreinovich, Lakeyev,
  Rohn, Kahl, 1998), według przeglądu: J. Horáček, M. Hladík, M. Černý, *Interval Linear Algebra
  and Computational Complexity*, arXiv:1602.00349 (Tw. 2, §1.4.5, Tw. 13).
- Pracy Oettliego–Pragera i monografii z 1998 nie otwierałem; treść znam z przeglądu.

## 3. Literatura i dorobek projektu (odjęcie na dwóch powierzchniach)

- **Zewnętrzna:** jak wyżej, plus gospodarze podani przez autora (Ben-Tal i in. 2004; Bertsimas
  i in. 2025; Bontemps–Magnac 2017), których nie otwierałem.
- **Własna:** przeszukałem publiczne i prywatne repo pod „Oettli”, „Prager”, „interval linear”,
  bez trafień.
  - LT6 ROT003 bada zmienny operator przez inkluzje zbiorów przy wierszowej zmianie `ℓ₁`; to inne
    pytanie (ryzyko najgorszego przypadku po rodzinie operatorów).
  - Mech-S7 ROT029 bada sztuczne gaussowskie perturbacje wierszy.
  - Żadna z tych prac nie podaje dokładnego testu zgodności przy wspólnej kalibracji i
    niepewnych przygotowaniach.
- Nowości nie zgłaszam. Rozwinięcie to zastosowanie klasycznego wyniku.

## Propozycja dla LT6 (decyzja autora)

1. W §7.5i dopisać po zdaniu o biliniowości: „Dla niepewności przygotowań w przedziałach
   (niezależnych elementach) zgodność ma dokładną postać Oettliego–Pragera z budżetem `‖e‖₁ ≤ η`
   i jest rozstrzygana przez `2^d` LP. W ogólności problem jest NP-trudny, a relaksacja
   wypukła może zachować model niezgodny.”
2. Podać ogólną postać dualności dla niejednorodnych `δ_j` (§1).

## Czego nie sprawdziłem

- Prywatnego skryptu `verify_shared_calibration_github.py` ani archiwum ZIP autora (celowo, dla
  niezależności).
- Zastosowania do rzeczywistego operatora ROT005 i do źródeł Mech.
- Gospodarzy wypukłej optymalizacji odpornej podanych przez autora.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 -I research/badacz/2026-10-29/code/lt6_rot006_shared_calibration_check.py --out <katalog>
```

Około 13 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

## Powrót w trzech warstwach

- **Wynik:**
  - ROT006 poprawne;
  - świadkowie dokładni;
  - granica autora rozstrzygnięta dla niepewności przedziałowej: test dokładny, NP-trudny w
    ogólności;
  - falsyfikator relaksacji.
- **Konfiguracja:** recenzja tekstu dojrzałego wyniku dała mało. Więcej dała próba domknięcia
  granicy zapisanej przez autora. To powtarza wzór z REVIEW_012 i 013.
- **Uczenie systemu:** przy recenzji wyniku „dojrzałego, bez nowości” cel recenzji przesuwam z
  „czy poprawne” na „czy granica zapisana przez autora ma dojrzałe rozwiązanie”. To kandydat na
  regułę wyboru celów w następnej prerejestracji (`[▷]`).

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
