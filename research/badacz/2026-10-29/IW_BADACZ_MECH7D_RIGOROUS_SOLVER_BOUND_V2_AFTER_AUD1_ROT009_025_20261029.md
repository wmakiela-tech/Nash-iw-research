---
artifact_id: IW_BADACZ_MECH7D_RIGOROUS_SOLVER_BOUND_V2_AFTER_AUD1_ROT009_025_20261029
exposure: PUBLIC
claim_ceiling: OWNER_REPAIR_[▷] / INTERVAL_ENCLOSURES_AND_INTERIOR_BOOTSTRAP / SYNTHETIC_MECH_STRUCTURED_MODEL_ONLY / NO_MECH_DATA / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: RESEARCH_NOTE
result_class: RESULT
task_id: BADACZ-MECH-GATES-002 (naprawa po AUD1 ROT009)
responds_to: AUD1 ROT009 (Nash-Priv audits/aud1/2026-10-29/IW_AUD1_ROT009_BADACZ022_EXACT_SOURCE_AND_SOLVER_BOOTSTRAP_REFUTATION_001.md), punkty B, C, D1–D2
supersedes: §2 doc 022 (research/badacz/2026-10-29/IW_BADACZ_MECH_GATES_EXACT_INFORMATION_AND_COMPONENTWISE_CERTIFICATE_022_20261029.md, r2 c63e126) w części „certyfikat błędu solvera”
code: research/badacz/2026-10-29/code/mech7d_interval_certificate_v2.py (sha256 0b324062b79f946f134b0cb25c578b61f7c08cb7dc49c1b75c77722d88448d38)
output_sha256: 7f2435e8064aa83fab80a13e70eed4ae0a9788ac7fc9de4f7a36266c69fcd8fb (mech7d_interval_certificate_v2.json)
---

# Naprawiony certyfikat błędu solvera dla układu 7D o strukturze Mech (v2, po AUD1 ROT009)

**Status:** `[▷]`. Naprawa mojego wyniku po zewnętrznym audycie AUD1 ROT009. AUD1 wykazał dwa
błędy wersji v1 (doc 022 §2): majoranty z próbek oraz bootstrap reszty kwadratowej sprawdzany
tylko na końcu kawałka. Wersja v2 usuwa oba. Model jest syntetyczny, choć o strukturze Mech. Nowości
nie zgłaszam. Wynik wymaga ponownego audytu spoza rodziny Claude.

## 0. Wynik w skrócie

- Oba kontrprzykłady AUD1 v2 pokrywa poprawnie. Przy zbyt grubym kawałku bootstrap **odmawia**
  wydania ograniczenia, zamiast wydać fałszywe.
- Na syntetycznej demonstracji v1 (te same trajektorie, ta sama para `±k` z klasy dokładnej)
  **ograniczenie v2 wynosi `ε_X = 3.5·10⁻⁸`** przy rzeczywistym błędzie `4.6·10⁻¹³`. Daje to
  dodatnią dwupunktową dolną granicę **`2.10·10⁻⁷`**, czyli 86% połowy luki numerycznej
  `2.45·10⁻⁷`.
- Liczba v1 (`2.5·10⁻⁹`) była około 14 razy mniejsza od v2 i nieważna jako certyfikat. Uczciwa
  cena ścisłości to rząd wielkości.

## 1. Twierdzenie K′ `[▷]` (dojrzali gospodarze: porównanie dla nierówności różniczkowych, arytmetyka przedziałowa)

**Ustawienie.**
- `y' = G(s, y)` na `[s₀, s₁]`. `ŷ` jest ciągłe i kawałkami `C¹`: wielomiany kolokacyjne Radau.
- `e = y − ŷ`, defekt `r = ŷ' − G(s, ŷ)`.
- Pole jest afiniczno-dwuliniowe w `y`, więc `G(s, ŷ + e) = G(s, ŷ) + J(s, ŷ)e + B(s; e, e)`
  **dokładnie**.
- Struktura gwiazdy: wiersze hadronowe `n_j` sprzęgają się tylko z `X`, a `B` ma postać
  `|B_X| ≤ Σ_j qx_j|e_X||e_j|`, `|B_j| ≤ qn_j|e_X||e_j|`.

**Na każdym kawałku `P` długości `h`** dane są ograniczenia przedziałowe (a nie z próbek):
- `ρ_i ≥ sup_P |r_i|`;
- `d_i ≥ sup_P J_ii`;
- `o_{ij} ≥ sup_P |J_ij|`;
- `qx_j`, `qn_j` ograniczają współczynniki `B` na `P`.

**Bootstrap na całym kawałku.** Dla poziomów `Φ` (wektor) definiujemy:
- dla hadronów: `d_j(Φ) = d_j + qn_j Φ_X`, `f_j = ρ_j + o_{jX}Φ_X`,
  `φ_j(t) = e^{d_j(Φ)t}ε_j + f_j ψ(d_j(Φ), t)`, gdzie `ψ(d, t) = (e^{dt} − 1)/d`;
- `I_j = ∫₀^h φ_j ≥ ∫₀^h |e_j|`;
- dla `X`: `φ_X(h) = e^{d_X h}ε_X + ρ_X ψ(d_X, h) + max(1, e^{d_X h}) Σ_j (o_{Xj} + qx_j Φ_X) I_j`;
- supremum: `sup_P φ_X ≤ max(1, e^{d_X h})(ε_X + ρ_X h + Σ_j(o_{Xj} + qx_jΦ_X)I_j)`, oraz
  `sup_P φ_j ≤ max(ε_j, φ_j(h))`.

**Teza.** Jeśli `|e(s_P)| ≤ ε` składowo i **ściśle** `sup_P φ < Φ`, to `|e| ≤ Φ` na całym `P`
oraz `|e(s_P + h)| ≤ φ(h)`.

*Dowód.*
- Niech `τ*` będzie supremum czasów, do których `|e| ≤ Φ`.
- Na `[0, τ*]` reszta `B` jest ograniczona przez `Φ`. Każda składowa spełnia skalarną nierówność
  różniczkową `D⁺|e_i| ≤ d_i|e_i| + (wymuszenie)`. Porównanie skalarne daje `|e_i| ≤ φ_i(t)`
  przy dowolnym znaku `d_i`, a dla `X` z wymuszeniem całkowanym w czasie.
- Stąd `|e| ≤ sup φ < Φ` na `[0, τ*]`. Z ciągłości `τ* = h`. ∎

To naprawia błąd (C) z AUD1. Poziom `Φ` ogranicza błąd na **całym** kawałku i jest sprawdzany
przez supremum, a nie przez wartość końcową.

**Obwiednie (naprawa błędu B).**
- `J`, `B` i źródło liczone są w `mpmath.iv` z zaokrąglaniem na zewnątrz, na całym kawałku.
- Defekt w postaci centrowanej: `r(θ) ∈ r(θ_m) + r'(P)(P − θ_m)`. Pochodną `r'(P)` daje
  arytmetyka liczb dualnych nad przedziałami (klasa `DI`), propagowana przez cały model: czas,
  tło, tempa, źródło i `ŷ`.
- Kawałki są dzielone adaptacyjnie (bisekcja), bo przeszacowanie obwiedni maleje jak `|P|²`.
- Wielomian `k(x)` liczę rekurencją Gegenbauera zamiast w bazie potęgowej, której współczynniki
  rzędu `10⁸` rozdmuchiwały przedziały.
- Wykładnicze tylko skalarne i przedziałowe. Wykładnicza macierzy z v1 zniknęła.

## 2. Testy na kontrprzykładach AUD1 (najpierw)

| model AUD1 | wartość prawdziwa | v2 |
|---|---|---|
| bootstrap: `x' = −10x + 100n + 10xn`, `n' = −10n`, `ŷ = 0`, `ε₀ = (0, 1)` | `x(1) = 0.0051381` | 1 kawałek: **odmowa** (bootstrap się nie domyka); 10: `0.01354`; 100: `0.005548`; 1000: `0.005177` |
| defekt zerowy w węzłach: `y' = −y + g`, `ŷ = 0`, `g = p²/∫p²` (`g = 0` w węzłach 5- i 9-punktowych) | `y(1) = 0.66898` | 16 kawałków: `14.7`; 64: `1.63`; 256: `0.842`; 1024: `0.709` |

- W pierwszym modelu v1 zwracała `0.0045441`, czyli mniej niż prawda. v2 zawsze daje wartość
  powyżej prawdy albo odmawia.
- W drugim modelu v1 widziała defekt zerowy. v2 obwiednią przedziałową znajduje dodatni defekt
  na każdym kawałku, a ograniczenie zbiega do prawdy przy zagęszczaniu.

## 3. Demonstracja (to samo syntetyczne ustawienie co v1)

| wielkość | `+k` | `−k` |
|---|---|---|
| `X_nuc` (Radau, `rtol = 3e-9`) | `0.137329145763` | `0.137328656154` |
| błąd diagnostyczny (wobec `rtol = 1e-13`) | `4.55e-13` | `4.58e-13` |
| **ograniczenie v2 `ε_X`** | **`3.51e-8`** | **`3.49e-8`** |
| w tym po fazie źródła (A) | `3.47e-8` | `3.44e-8` |
| kawałki A / B (w tym bisekcje) | `11601 / 6246` (`4993 / 798`) | `11756 / 6231` (`5156 / 791`) |

- **Dwupunktowa dolna granica:** `(|X₊ − X₋| − ε₊ − ε₋)/2 = 2.098·10⁻⁷ > 0`.
- Prawie całe ograniczenie powstaje w fazie źródła. Dominuje obwiednia defektu dla `p̄`/`n̄`,
  przenoszona do `X` przez sprzężenie `S·28·X`.
- Faza po źródle niemal go nie powiększa, bo słabe tempa tłumią `X`, a hadrony szybko zanikają.
- Zapas wobec połowy luki z Mech (`5.7·10⁻⁴`) wyniósłby cztery rzędy, gdyby realny model zachował
  podobną strukturę. Tego nie sprawdziłem.

## 4. Co pozostaje nieścisłe albo poza zakresem

- **Model jest syntetyczny:** tło `T(t) = √(1.32/t)`, `t_edge = 150 s`, `n_PBH0 = 10⁻¹¹`. Stałe i
  wzory na tempa pochodzą z publicznego kodu Mech ROT006. Wynik dotyczy rozwiązania **tego**
  modelu, nie modelu Mech i nie fizyki.
- **Biblioteka:** zakładam poprawność arytmetyki przedziałowej `mpmath.iv`. Stałe modelu to
  liczby binarne z kodu.
- **Dla Mech:**
  - tło PCHIP jest kawałkami sześcienne, więc obwiednie są proste;
  - most 10-składowy sprzed krawędzi ma inną strukturę i wymaga sprawdzenia, czy zachodzi
    sprzężenie typu gwiazdy (jeśli nie, potrzebny jest ogólny wariant porównania wektorowego);
  - przebiegi z `dense_output=True` i funkcja `certify()` z podmianą `G_g`.
- **Koszt:** około 4 minut na przebieg. To rząd minut, więc da się to robić rutynowo.

## 5. Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3 mpmath==1.3.0
python3 -I research/badacz/2026-10-29/code/mech7d_interval_certificate_v2.py --out <katalog> \
  --v1json research/badacz/2026-10-29/code/mech7d_componentwise_certificate.json
```

Plik v1 JSON służy tylko do odczytu kierunku `a_l` i amplitudy, żeby porównanie było na tych
samych trajektoriach. Dwa czyste uruchomienia dały identyczny JSON.

## Powrót w trzech warstwach

- **Wynik:** oba błędy z AUD1 ROT009 usunięte; kontrprzykłady AUD1 pokryte lub odrzucone;
  na demonstracji ścisła (modulo `mpmath.iv`) dodatnia granica `2.10·10⁻⁷`. L4 dla modelu
  syntetycznego o strukturze Mech jest rozwiązane. Dla modelu Mech wymaga ich przebiegów.
- **Konfiguracja:** audyt zewnętrzny AUD1 znalazł w ciągu kilku godzin błąd logiczny, którego
  moje własne kontrole nie wykryły. Moje testy sprawdzały pokrycie rzeczywistego błędu
  (`4.5e-13`) przez ograniczenie, więc z konstrukcji nie mogły ujawnić, że ograniczenie jest
  nieważne jako certyfikat.
- **Uczenie systemu:**
  - origin_failure_mode `TEST_BY_COVERAGE_CANNOT_FALSIFY_CERTIFICATE_LOGIC`: test „ograniczenie ≥
    błąd rzeczywisty” nie sprawdza ważności certyfikatu. Łatka: każdy nowy certyfikat najpierw
    przepuszczam przez kontrprzykłady skonstruowane przeciw jego logice (jak oba modele AUD1);
  - etykieta „certified” wymaga obwiedni i bootstrapu na całym kawałku. Inaczej piszę
    „diagnostic”.
