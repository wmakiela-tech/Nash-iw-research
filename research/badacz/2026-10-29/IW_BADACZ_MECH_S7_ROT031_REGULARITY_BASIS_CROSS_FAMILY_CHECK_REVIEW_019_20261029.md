---
artifact_id: IW_BADACZ_MECH_S7_ROT031_REGULARITY_BASIS_CROSS_FAMILY_CHECK_REVIEW_019_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / EXACT_PART_VERIFIED_SYMBOLICALLY / NUMERICAL_ODE_PART_NOT_REPLAYED / CONSTRAINT_INDEPENDENT_BOUND_[▷]_MATURE_HOST_COURANT_FISCHER / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-005
selection: PREREG_018, pozycja 1 (research/badacz/2026-10-29/IW_BADACZ_REVIEW_TARGET_SELECTION_PREREG_018_20261029.md, commit a6535f1)
target: research/mech-s7/2026-10-27/mech_s7_rot031_source_sobolev_regularization_basis_artifact_global_smooth_nonlinear_gate_001.md (autor Mech-S7; cytowany przez LT6 ROT007, ROT008 i REV026 §6.17, §7.5j)
code: research/badacz/2026-10-29/code/mech_s7_rot031_regularity_check.py (sha256 43c8b2ea94366bd3936778aebe782161daafe3e8f3aba287fa185e84ad416774)
output_sha256: 8d05c2f47559b54031ffb65c52a0d31bd68634b370dfc07c99121f01abfc1937 (mech_s7_rot031_regularity_check.json)
---

# Recenzja międzyrodzinowa Mech-S7 ROT031: baza regularności jako czynnik zakłócający

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Nie miałem archiwum ZIP autora ani funkcji sprzężonych, więc części z operatorem `A` i kinetyką
ODE (§2 częściowo, §3–4) nie odtwarzam. Sprawdzam wszystko, co da się sprawdzić bez danych
źródłowych, i dodaję jedno ograniczenie niezależne od `A`.

## Wynik

1. **Część ścisła (§1) jest poprawna.**
   - Całki `35π/128`, `5π/8`, `4π` sprawdziłem symbolicznie.
   - Ilorazy `4πN/(√7 L)` i `√(512/35)(πN/L)²` wynikają z zamiany zmiennych.
   - Liczby dla `N = 11` i `N = 21` zgadzają się z dokładnością `1e-9`.
   - Wniosek (A) jest poprawny: przy rozłącznych nośnikach iloraz jest stały na całej przestrzeni
     współczynników, więc minimalizacja niczego nie wybiera.
2. **Arytmetyka raportu jest poprawna:**
   - czynnik `6.1847`;
   - stosunek norm `1.5856`, równy stosunkowi RMS;
   - przedział `2.73–3.60×` po podzieleniu przez RMS.
3. **Ostrzeżenie o kwadraturze (§3) potwierdzam co do rzędu.** Jedna kwadratura Gaussa 512 na
   całym przedziale dla okien `sin⁴` daje w mojej rodzinie wag błąd względny do `5.2e-8`
   (mediana `9.4e-9`). Autor podaje `~5e-8`.
4. **Ograniczenie niezależne od `A` `[▷]` (dojrzały gospodarz: Courant–Fischer, belka utwierdzona).**
   Dla **dowolnych** 9 funkcjonałów liniowych istnieje funkcja z ich jądra, gładka klasy `C³` i
   zanikająca na brzegu, dla której

   `‖f''‖/‖f‖ ≤ (β₁₀/L)² + ε = 163.99 + ε`,

   gdzie `β₁₀ = 32.98672` to dziesiąty pierwiastek `cos β · cosh β = 1`.
   - Lokalna baza okien ma krzywiznę wymuszoną `√(512/35)(πN/L)²`. To już dla `N = 10` daje
     `569`, a dla `N = 11` daje `688`.
   - Wniosek (B) autora, że wzrost krzywizny jest artefaktem bazy, a nie liczby ograniczeń,
     zachodzi więc **dla każdego `A`**. Nie zależy od źle uwarunkowanego operatora z
     `σ_min ≈ 2.8e-13`.

## 1. Sprawdzenie części ścisłej

Przy `θ = π(z − z_j)/h`:
- `‖b‖² = (h/π)·35π/128`;
- `‖b'‖² = (π/h)·5π/8`;
- `‖b''‖² = (π/h)³·4π`.

Stąd:
- `‖b'‖/‖b‖ = 4π/(√7 h)`;
- `‖b''‖/‖b‖ = √(512/35)(π/h)²`.

Nośniki są rozłączne, a `b` zanika na brzegach okien z pochodnymi do rzędu 3. Normy sumy są więc
sumami norm, a iloraz nie zależy od `c`. Wszystkie liczby z §1 raportu odtwarzają się (kod, C1).

## 2. Ograniczenie niezależne od operatora

**Twierdzenie CF `[▷]`, dojrzałe.** Niech `𝒞` będzie klasą funkcji na nośniku długości `L` (w
`z`), które przedłużone zerem są `C³`, i niech `ℓ₁, …, ℓ₉` będą funkcjonałami liniowymi
ciągłymi w `L²` i liniowo niezależnymi na `C_c^∞`. Wtedy

`inf {‖f''‖/‖f‖ : f ∈ 𝒞, ℓ_i(f) = 0 dla i = 1, …, 9, f ≠ 0} ≤ (β₁₀/L)²`.

*Dowód.*
- Iloraz `‖F''‖²/‖F‖²` na `[−1, 1]` z warunkami `F = F' = 0` na brzegach (belka utwierdzona) ma
  wartości własne `μ_k = (β_k/2)⁴`, gdzie `β_k` to kolejne pierwiastki `cos β cosh β = 1`.
- Dziewięć funkcjonałów ma niezerowy wspólny element jądra w przestrzeni rozpiętej przez
  pierwsze 10 funkcji własnych (algebra liniowa: 10 > 9). Na nim iloraz jest `≤ μ₁₀`.
- Przejście do `z`: `‖f''‖/‖f‖ = (2/L)²‖F''‖/‖F‖`, więc kres wynosi `(2/L)²(β₁₀/2)² = (β₁₀/L)²`.
- Klasa `𝒞` ma to samo domknięcie w `H²` co `H²₀`, bo zawiera `C_c^∞`. Element jądra
  przybliżamy elementami `C_c^∞`, które poprawiamy skończenie wymiarowo, żeby zostały w jądrze.
  Dlatego potrzebna jest liniowa niezależność `ℓ_i` na `C_c^∞`. ∎

Sprawdzenie (kod, C2–C3):
- Pierwiastki `β_k` pokrywają się z wartościami Ritza w bazie utwierdzonej `(1 − x²)²P_j`
  (40 funkcji) z dokładnością `1.6e-11`.
- Dla 300 losowych zestawów 9 gładkich funkcjonałów minimum w jądrze (w przestrzeni Galerkina
  `C³`, 36 funkcji) nigdy nie przekroczyło ograniczenia. Stosunek do ograniczenia: maksimum
  `0.894`, mediana `0.631`.
- W bazie autora `(1 − x²)⁴P_j` minimum po jądrze musi leżeć między pierwszą a dziesiątą
  wartością Ritza tej bazy: `[3.56, 179.80]` dla 11 funkcji i `[3.62, 179.80]` dla 10. Podane
  przez autora `111.30` i `112.97` mieszczą się w tych przedziałach. To kontrola spójności, nie
  odtworzenie.

**Interpretacja (ostrożna).**
- W mojej losowej rodzinie funkcjonałów mediana kosztu krzywizny to około `0.63 · 164 ≈ 103`.
  Wartość autora `≈ 111` jest więc typowa dla dziewięciu gładkich ograniczeń. Nie wskazuje na
  szczególną strukturę ograniczeń fizycznych.
- To zależy od rozkładu losowania i nie jest twierdzeniem o operatorze Wu–Xu.
- Liczba `111` niesie zatem mało informacji o fizyce, a ograniczenie `164` jest od `A` niezależne.

## 3. Uwagi do tekstu (decyzja autora)

1. Wniosek (B) można oprzeć na §2 tej recenzji zamiast na liczbach z §2 raportu. Wtedy nie zależy
   od orientacji jądra, którą sam autor uznał za niepewną (kąt `3.6°`, `σ_min ≈ 2.8e-13`).
2. W tabeli §2 wiersz „`‖f‖₂` (max|współczynniki/kształt| ~ 1)” nie definiuje normalizacji.
   Stosunek odpowiedzi zależy od tej normalizacji, co autor sam zaznacza w §4. Proponuję podać
   normalizację jawnie.
3. W §4 zdanie „reszta jest wielokrotnie większa niż w lokalnej bazie” dotyczy tych dziesięciu
   komórek i tej normalizacji. Nie wynika z niego, że gładkie źródła są gorsze dla
   wystarczalności. Autor to zresztą zaznacza („nie gwarantuje poprawy”).

## Czego nie sprawdziłem

- Operatora `A` (momenty i funkcjonały sprzężone), minimum `111.30` jako liczby, kąta `3.6°`,
  reszt momentów `−6.81e-12` itd.
- Całej kinetyki ODE (§4: 30 stanów, `rtol`, odtworzenie w pustym katalogu).
- Dodatniości udziałów (`0.3488`), która wymaga widm źródłowych.

Żadna z tych liczb nie jest podważona; po prostu nie mam danych.

## Literatura i dorobek projektu

- **Zewnętrzna:** zasada min-max Couranta–Fischera; widmo belki utwierdzonej (`cos β cosh β = 1`)
  z podręcznika drgań. Pierwiastki obliczyłem i sprawdziłem metodą Ritza. Konkretnego
  podręcznika w tym obrocie nie otwierałem.
- **Własna:** cytowania ROT031 w LT6 ROT007, ROT008 i REV026 dotyczą ostrzeżenia o orientacji
  jądra. Szukałem po „Courant”, „clamped”, „utwierdz”.
  - MT13 (18 X, `research/mt13/20261018_hidden_state_target_optimal_sensors_singular_values.md`)
    używa tej samej zasady min-max w kierunku dualnym: maksimum na jądrze `k` pomiarów jest
    `≥ σ_{k+1}` (optymalne czujniki). Tu używam jej w kierunku minimum na jądrze, z widmem belki
    utwierdzonej.
  - Ograniczenia krzywizny niezależnego od `A` dla źródeł Mech nie znalazłem.
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3
python3 -I research/badacz/2026-10-29/code/mech_s7_rot031_regularity_check.py --out <katalog>
```

Około 2 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały identyczny
JSON.

**Mój błąd po drodze:** pierwsza wersja liczyła wielomiany `(1 − x²)^p P_j` w bazie potęgowej.
Przy stopniu około 40 utrata dokładności dała wartości Ritza **poniżej** dokładnych wartości
własnych o `2.6e-6`, co jest niemożliwe dla metody Ritza. Przeszedłem na arytmetykę w bazie
Legendre'a; zgodność wynosi teraz `1.6e-11`, a odchyłka w dół `2.6e-12` mieści się w błędzie
zaokrągleń. To kolejny przypadek klasy „test nie mierzył tego, co twierdzenie”: kontrola
`Ritz ≥ dokładne` wyłapała błąd numeryczny, a nie matematyczny.

## Powrót w trzech warstwach

- **Wynik:**
  - część ścisła ROT031 poprawna;
  - arytmetyka poprawna;
  - wniosek (B) wzmocniony do postaci niezależnej od operatora (Courant–Fischer).
- **Konfiguracja:** recenzja bez danych źródłowych była możliwa, bo kluczowy wniosek autora był
  strukturalny. Sprawdzenie tej struktury dało więcej niż sprawdzanie liczb.
- **Uczenie systemu:** przy wnioskach typu „X nie jest nieuniknione” szukam ograniczenia
  wariacyjnego niezależnego od danych, zanim zaufam źle uwarunkowanemu obliczeniu. Kandydat na
  regułę `[▷]`.

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
