---
artifact_id: IW_BADACZ_MECH_GATES_EXACT_INFORMATION_AND_COMPONENTWISE_CERTIFICATE_022_20261029
exposure: PUBLIC
claim_ceiling: CONSTRUCTIVE_MATH_[▷] / MATURE_HOSTS_GEGENBAUER_ORTHOGONALITY_MUELLER_KAMKE_COMPARISON / SYNTHETIC_DEMO_ONLY / SEMI_RIGOROUS_SAMPLED_MAJORANTS / NO_MECH_DATA_USED / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: RESEARCH_NOTE
result_class: RESULT
task_id: BADACZ-MECH-GATES-001 (polecenie Moderatora 29 X 07:42: „spróbujesz znaleźć rozwiązanie ograniczeń”)
responds_to: AUD1 ROT005 (Nash-Priv audits/aud1/2026-10-29/IW_AUD1_MECH_ROT032_LT719_EXACT_MOMENT_FALSIFICATION_005_20261029.md, CHECK 2, Gate A, Gate C); LT6 ROT009 T009.2–T009.3 (research/lt6/2026-10-29/IW_LT6_ROT009_EXACT_H_MOMENT_REPAIR_TARGET_PERSISTENCE_001_20261029.md)
targets: research/mech-s7/2026-10-28/mech_s7_rot032_sharp_sobolev_information_radius_nonlinear_binary_witness_001.md; research/mech-s7/2026-10-28/mech_s7_rot033_target_weighted_source_measurement_h2_information_radius_design_001.md; struktura 7D z research/mech-s7/2026-10-23/terminal_7d_exact_mass_common_background_006.py
code: research/badacz/2026-10-29/code/exact_information_source_class.py (sha256 1df07c96e2864d6d60e4f8603bdcc62e1c200a6e6a4e279983bfdea56ffb3b73); research/badacz/2026-10-29/code/mech7d_componentwise_certificate.py (sha256 81c4bd3ae86348f92807a1d221098c06bb6cfaf0174353a64a2e60da22871367)
output_sha256: 03c07c56ba703d32c74efda83a28ba09b1ee7e86a78b6b76c6659c3af5d9a340 (exact_information_source_class.json); 7d86f4b4eec1b2d83e1d9b876df55afddd15fd6667f71b1abaff0115ca17a529 (mech7d_componentwise_certificate.json)
---

# Bramy AUD1 dla Mech ROT032/033: dokładnie równa informacja z konstrukcji i składowy certyfikat błędu solvera

**Status:** `[▷]`. Konstruktywne propozycje Claude'a. Nie używałem danych Mech (archiwa Wu–Xu
i funkcje sprzężone są poza publicznym repo). Demonstracja jest syntetyczna, ale ma dokładnie
strukturę układu 7D z publicznego kodu Mech. Nowości nie zgłaszam. Wynik wymaga audytu spoza
rodziny Claude i decyzji właścicieli (Mech-S7, LT6).

## 0. Które ograniczenia rozwiązuję

AUD1 ROT005 i LT6 ROT009 wskazały, czego brakuje, żeby dwupunktowa dolna granica minimaksowa
Mech ROT032 była ścisła:

| | ograniczenie | źródło | stan po tej notatce |
|---|---|---|---|
| L1 | momenty par `±c*` są równe tylko do `1.2e-12`, a idealny obserwator je rozróżnia | AUD1 CHECK 2 | **usunięte konstrukcyjnie** (§1) |
| L2 | naprawa przez rzut wymaga dokładnego `M`; przy `M̂ ≠ M_true` mamy tylko istnienie | LT6 T009.3 STOP | **usunięte dla wierszy momentów i wierszy gaussowskich** (§1) |
| L3 | przeniesienie luki celu z `±c` na `±p` wymaga stałej `L_T` | LT6 T009.2 | **niepotrzebne**, bo nie ma naprawy (§1) |
| L4 | błędy solvera `ε±` muszą być certyfikowane; ponowne uruchomienie z mniejszym `rtol` to nie certyfikat | AUD1 Gate A | **rozwiązane półściśle na demonstracji**; przepis dla Mech (§2) |
| L5 | dodatniość w sensie ciągłym | LT6 T009.2 | warunek jawny, potrzebna dolna granica danych (§1.4) |
| L6 | źródło fizyczne poniżej `1e9 g`, Julia 10D, most 10D sprzed krawędzi | Mech, AUD1 | **nie do rozwiązania matematyką** (§4) |

## 1. Dokładnie równa informacja z konstrukcji

### 1.1 Twierdzenie E `[▷]` (dojrzały gospodarz: ortogonalność Gegenbauera)

**Oznaczenia.** `u = M/10⁹ g`, `z = ln u`, `x = 2(z − z_mid)/L ∈ [−1, 1]`, `L = ln(0.92/0.07)`.
Zamiast parametryzować zmianę **udziału** `h(z)`, jak w ROT032 (`δQp = (Qp + Qn)h`),
parametryzujemy zmianę **źródła** ważoną `u³`:

`u³ δQp(u) = A·k(x)`,   `δQn = −δQp`,   `k(x) = (1 − x²)⁴ Σ_{l=3}^{10} a_l C_l^{(9/2)}(x)`,

gdzie `C_l^{(9/2)}` to wielomiany Gegenbauera, ortogonalne z wagą `(1 − x²)⁴`.

**Teza.**
1. Dla **każdego** widma `Qp, Qn` i każdego `a` trzy komowujące momenty każdego gatunku,
   `∫ u³ Q z^j dz` dla `j = 0, 1, 2`, są dla `±k` **dokładnie** równe.
2. Suma `Qp + Qn` jest niezmieniona punktowo.
3. Źródło zmienia się tylko w `M ∈ [7·10⁷, 9.2·10⁸] g`. Na brzegach nośnika `δQ` i jego pochodne
   do rzędu 3 zanikają.

*Dowód.*
- `∫ u³ δQp z^j dz = A (L/2) ∫ k(x)(z_mid + Lx/2)^j dx`.
- `(z_mid + Lx/2)^j` jest wielomianem stopnia `≤ 2` w `x`.
- `C_l^{(9/2)}` dla `l ≥ 3` jest ortogonalny w wadze `(1 − x²)⁴` do każdego wielomianu stopnia
  `≤ 2`. Całka znika dokładnie, dla dowolnych `L` i `z_mid`.
- Dane źródłowe nie występują w tym rachunku. ∎

Sprawdzenie (kod `exact_information_source_class.py`, E1, SymPy, arytmetyka wymierna):
- ortogonalność dla `l = 3…10`;
- znikanie momentów w `z` z **symbolicznymi** `L` i `z_mid`;
- wymiar klasy = 8, dokładnie jak jądro trzech momentów w 11-wymiarowej klasie ROT032.

### 1.2 Co to daje

- **L1:** dane idealnego obserwatora (trzy momenty każdego gatunku, suma `Qp + Qn`, dane na
  krawędzi tabeli) są dla `±k` **identyczne co do bitu matematycznego**, a nie do `1e-12`.
  Dwupunktowa granica `|T(+k) − T(−k)|/2` jest więc granicą dla obserwatora bez szumu, bez Bramy A.
- **L2:** operator obserwacji `k ↦ (∫ k z^j)` nie zależy od danych, więc jest znany dokładnie.
  `ε_M = 0`, a STOP T009.3 nie dotyczy tej klasy.
- **L3:** nie ma naprawy `c → p`, więc nie trzeba `L_T`. Zostaje tylko różnica między obiektem
  dokładnym a jego reprezentacją zmiennoprzecinkową w solverze: `≤ L_T · 1e-16 · ‖k‖`, co jest
  pomijalne przy dowolnej rozsądnej `L_T`.
- **Wiersze gaussowskie ROT033** w tej parametryzacji też nie zależą od danych:
  `A_w(k) = ∫ u³ δQp w dz = A (L/2)∫ k(x) w(z(x)) dx`.
  - Kod liczy je w postaci zamkniętej (rekurencja z `erf`) na 60 cyfrach i sprawdza niezależnie
    kwadraturą tanh-sinh na 50 cyfrach: zgodność `≤ 4e-48` względem normy wiersza.
  - Warunek `A_w = 0` spełnia obiekt o współczynniku rzeczywistym zadanym dokładnie (stosunek
    dwóch całek). Reprezentacja w `float64` ma resztę względną `4.5e-17`.
  - Dwa wiersze gaussowskie z ROT033 mają po normalizacji wartości osobliwe `1.40` i `0.19`. Ich
    dołączenie nie psuje uwarunkowania w tej klasie (dotyczy obawy z T009.3).

### 1.3 Czy klasa nie traci zakresu

Porównanie syntetyczne (E3), przy tym samym budżecie `‖h''‖_{L²(dz)} ≤ R = 11.43596…` na udziale
`h = δQp/(Qp + Qn)`:
- dwie syntetyczne funkcje `W = u³(Qp + Qn)`;
- trzy jądra celu oraz kontrola, w której jądro leży w rozpięciu momentów i oba promienie
  wynoszą 0.

Stosunek promienia najgorszego przypadku „klasa dokładna / klasa udziałów” wyniósł
`0.94–1.02`. Klasa dokładna ma ten sam wymiar i praktycznie ten sam zasięg. To liczby
syntetyczne, nie liczby Mech.

### 1.4 Co zostaje zależne od danych

- **Dodatniość** wymaga `A·sup|k(x)|·u⁻³ < min(Qp, Qn)(u)` na nośniku.
  - `sup|k|` dla wielomianu da się policzyć ściśle (forma Bernsteina na podprzedziałach; to
    narzędzie MT14 ROT011).
  - Dolna granica `min(Qp, Qn)` dla syntetycznego przedłużenia Mech wynika z jego jawnej postaci.
    Udział bazowy jest logistyczny w `x`, więc wystarcza arytmetyka przedziałowa.
- **Budżet `H²` na udziale** (jeśli zostaje definicją klasy) zależy od `W`. Liczy się go
  kwadraturą z zapasem. Alternatywnie budżet można zadać na `k`; wtedy cała klasa, poza
  dodatniością, jest niezależna od danych. To decyzja modelowa Mech.
- **Cel** (`X_n` przy `T_nuc`) i kierunek najgorszy wymagają funkcji sprzężonej Mech: `b_l` dla
  `k_l`, osiem liczb.

## 2. Certyfikowany błąd solvera dla układu 7D (Brama A)

### 2.1 Struktura (z publicznego kodu Mech ROT006)

`y = (X, n₁, …, n₆)`:
- `X' = w(T)·((1 − X)e^{−Q/T} − X) − X/τ_n + S Σ_i n_i((1 − X)a_i − X b_i)`;
- `n_i' = s_i(t) − D_i(X, T) n_i`, gdzie `D_i = decay_i + (ℓ_i⁰ + ℓ_i¹ X) n_B σv`.

W fazie źródła zmienną niezależną jest `u`, a prawa strona jest mnożona przez `3Δt u² ≥ 0`.

Pole jest **afiniczno-dwuliniowe**:
- `J_XX ≤ 0` (słabe tempa i zużycie);
- `J_{n_i n_i} = −D_i` (od `−10⁴` do `−4·10⁷ s⁻¹`);
- sprzężenia: `J_{X n_i} = S((1 − X)a_i − X b_i)` oraz `J_{n_i X} = −ℓ_i¹ n_B σv n_i`;
- reszta kwadratowa: `|q_X| ≤ S Σ(a_i + b_i)|e_X||e_{n_i}|` oraz
  `|q_{n_i}| ≤ |ℓ_i¹| n_B σv |e_X||e_{n_i}|`.

### 2.2 Twierdzenie K `[▷]` (dojrzały gospodarz: porównanie Müllera–Kamkego dla układów quasi-monotonicznych)

**Założenia.**
- `ŷ` jest ciągłym, kawałkami `C¹` przybliżeniem rozwiązania (wielomiany kolokacyjne Radau
  z `dense_output`).
- `r = ŷ' − G(s, ŷ)` to defekt.
- `M(s)` jest majorantą Metzlera: `M_ii = J_ii(ŷ)`, `M_ij = |J_ij(ŷ)|`, plus człony reszty
  kwadratowej.

**Teza.** Jeśli `ε` spełnia `ε' ≥ M ε + |r|` i `ε(s₀) ≥ |e(s₀)|` składowo, to
`|y(s) − ŷ(s)| ≤ ε(s)` **składowo**.

*Dowód.*
- Dla każdej składowej `D⁺|e_i| ≤ J_ii|e_i| + Σ_{j≠i}|J_ij||e_j| + q_i + |r_i|`, gdzie `J` jest
  liczony na odcinku między `ŷ` a `y`; resztę pokrywa `q`.
- Układ porównawczy jest quasi-monotoniczny (Metzlera), więc twierdzenie Müllera–Kamkego daje
  dominację składową.
- Reszta kwadratowa wymaga bootstrapu na każdym kawałku: zakładamy `ε̄`, liczymy i sprawdzamy
  `ε ≤ ε̄`. ∎

**Realizacja.**
- Na każdym kawałku kroku biorę górne ograniczenia `M̄` i `ρ̄` po próbkach i propaguję
  `ε ← e^{M̄h}ε + ∫₀^h e^{M̄s}ds ρ̄` dokładną wykładniczą macierzy.
- Monotoniczność układów Metzlera zapewnia, że większe współczynniki dają większe `ε`.
- Certyfikat celu: `ε± = ε_X(T_nuc)`. Pomiar jest w stałym `T_nuc`, bez zdarzenia, więc
  certyfikat pierwszego przecięcia nie jest potrzebny.

**Dlaczego to, a nie Gronwall.**
- Tw. 7.3 / LT6 ROT004 używa `e^{Lt}`. W demonstracji (§2.3) `L ≈ 8·10⁷ s⁻¹` (rozpady pionów i
  kaonów), a czas wynosi około 66 s, więc czynnik ma rząd `10^{2.3·10⁹}`. Bezużyteczny.
- Pojedyncza norma logarytmiczna to propozycja pakietu NC 002 §A. M13 ROT09 pokazał, że jej znak
  zależy od normy. W normie `∞` jest tu dodatnia (do `29 s⁻¹`), co przez 66 s daje `10⁸³⁰`.
- Porównanie składowe omija wybór normy. Szybkie składowe `n_i` tłumią własne błędy w tempie
  `D_i`, a do `X` wchodzą ze wzmocnieniem `|J_{X n_i}|/D_i`.

### 2.3 Demonstracja syntetyczna o strukturze Mech

Stałe i funkcje temp skopiowane dosłownie z ROT006. Syntetyczne są:
- tło `T(t) = √(1.32/t)` MeV;
- `t_edge = 0.24 s`;
- `n_PBH0 = 10⁻⁷ cm⁻³`;
- kierunek `k` w klasie dokładnej, wybrany jako gradient odpowiedzi liniowej `X_nuc` po
  `a_l` (różnice skończone);
- amplituda: `max|δ|/min(s_pbar, s_nbar) = 0.5`.

Syntetyczne tło jest późne (`t_edge = 150 s`, `T ≈ 0.094` MeV), tak jak okno parowania u Mech.
`X_edge = 0.14`, `n_PBH0 = 10⁻¹¹ cm⁻³`.

| wielkość | `+k` | `−k` |
|---|---|---|
| `X_nuc` (Radau, `rtol = 3e-9`) | `0.137329145763` | `0.137328656154` |
| rzeczywisty błąd (wobec `rtol = 1e-13`) | `4.5e-13` | `4.6e-13` |
| **certyfikat `ε_X`** | **`2.48e-9`** | **`2.44e-9`** |
| `log₁₀` czynnika Gronwalla–Lipschitza | `2.3·10⁹` | `2.3·10⁹` |
| maks. `μ_∞(J)` (faza A / B) | `19.7 / 28.9 s⁻¹` | `19.7 / 28.9 s⁻¹` |

- Połowa luki numerycznej wynosi `2.448e-7`, a **certyfikowana dolna granica dwupunktowa
  `2.423e-7`** (99% połowy luki).
- Certyfikat pokrywa rzeczywisty błąd, choć jest około 5000 razy pesymistyczny. Wystarcza z
  dużym zapasem.
- Przy gęstszym próbkowaniu (12 kawałków × 9 próbek zamiast 6 × 5) `ε_X = 1.98e-9`, więc
  certyfikat jest stabilny.
- Gronwall z Lipschitzem jest bezużyteczny. Pojedyncza norma `∞` też, bo `e^{28.9·66}` ma rząd
  `10⁸³⁰`.
- Odpowiedź liniowa `X_nuc` na `k_l` maleje szybko z `l` (od `4.6e-5` do `8e-9` na jednostkę
  amplitudy). Kierunek gradientu jest zdominowany przez `k_3`–`k_5`.
- Syntetyczna połowa luki jest dużo mniejsza niż u Mech (`5.7e-4`), bo obciążenie hadronowe
  dobrałem małe. Certyfikat rzędu `1e-9` byłby wobec luki Mech pomijalny, jeśli realny układ
  zachowa podobną strukturę. Tego nie sprawdziłem.

### 2.4 Półścisłość i droga do pełnej ścisłości

`M̄` i `ρ̄` są maksimami po próbkach w kawałkach, a nie oszacowaniami przedziałowymi. Pełna
ścisłość wymaga:
- przedziałowego obliczenia `J` i defektu na każdym kawałku. Prawa strona to funkcje elementarne
  `T` plus wielomian w `y`; `T(t)` u Mech to PCHIP, czyli kawałkami sześcienny. Rachunek jest
  rutynowy, na przykład w `mpmath.iv`;
- przedziałowej wykładniczej macierzy albo zastąpienia jej jawnym górnym rozwiązaniem
  (`ε` rośnie monotonicznie z `M̄` i `ρ̄`).

Zapas jest duży: wymagane `ε± ≪` połowy luki (`5.7·10⁻⁴` u Mech). Zgrubna ścisła wersja z
dodatkowym czynnikiem bezpieczeństwa nadal by wystarczyła.

## 3. Złożenie: ścisła dwupunktowa granica bez naprawy

Dla pary `±A k` z §1 i certyfikatów z §2:

`max błąd ≥ ( |X̂(+) − X̂(−)| − ε₊ − ε₋ ) / 2`.

Ta granica nie potrzebuje:
- `L_T`, `ε_M`, naprawy;
- szumu pomiaru (dane są dokładnie równe);
- powtórnych przebiegów z mniejszym `rtol`.

Zostaje dodatniość (§1.4) i fizyka (§4).

## 4. Czego to nie rozwiązuje

- **Fizyka (L6):** brak źródłowo uprawnionych widm hadronowych poniżej `10⁹ g`, natywnego Julia
  10D i fizycznego `Yp/DH`. Wszystko tutaj dotyczy **warunkowego** modelu Mech.
- **Most 10-składowy sprzed krawędzi (ROT013):** potrzebuje tego samego certyfikatu. Jego
  struktury nie widziałem w publicznym kodzie, więc nie sprawdzałem, czy majoranta Metzlera
  zachowuje się tak samo.
- **Kierunek najgorszy** w klasie dokładnej wymaga funkcji sprzężonej Mech. Mój demonstracyjny
  gradient jest syntetyczny.
- **Pełna ścisłość przedziałowa** (§2.4).

## 5. Przepis dla Mech-S7 (decyzja właściciela)

1. Zastąpić bazę udziałów `φ_j` bazą źródłową `k_l = (1 − x²)⁴C_l^{(9/2)}`, `l = 3…10` (`u³δQp = A k`).
   Momenty znikają wtedy dokładnie.
2. Policzyć `b_l` (odpowiedź liniowa `X_n` na `k_l`) istniejącą funkcją sprzężoną. Wybrać
   kierunek najgorszy przy budżecie `H²` (na udziale albo na `k`).
3. Sprawdzić dodatniość ściśle: Bernstein dla `sup|k|` plus przedział dla
   `min(Qp, Qn)u³` z jawnej postaci przedłużenia.
4. Przebiegi `±A k` puścić tak jak dziś, z `dense_output=True`, i uruchomić funkcję `certify()`
   z mojego kodu na własnym `rates()`, tle PCHIP i źródle. Podpięcie wymaga tylko podmiany
   `T_of_t`, `base_src` i `delta_src`.
5. Podać granicę z §3. Dla ROT033 dołączyć wiersze gaussowskie w postaci zamkniętej (§1.2).

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1 sympy==1.13.3 mpmath==1.3.0
python3 -I research/badacz/2026-10-29/code/exact_information_source_class.py --out <katalog>
python3 -I research/badacz/2026-10-29/code/mech7d_componentwise_certificate.py --out <katalog>
```

Część 1 trwa około 3 s, część 2 około 90 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

**Moje błędy po drodze:**
1. Pierwszy test krzyżowy wierszy gaussowskich ewaluował wielomiany stopnia 18 w bazie potęgowej
   w `float64`. Rozbieżność `1e-6` wynikała z tej ewaluacji, nie z wzoru. Zastąpiłem test
   kwadraturą tanh-sinh na 50 cyfrach.
2. Pierwsza wersja certyfikatu używała interpolantu Hermite'a z węzłów. Dla sztywnych,
   szybko zanikających `n_i` przy krokach `hD ≫ 1` ten interpolant przestrzeliwał, a defekty
   sięgały `140`. Przeszedłem na wielomiany kolokacyjne Radau.
3. Pierwszy kierunek (`k_3`) dawał znikomą odpowiedź `X` (połowa luki `9e-10`), więc granica
   wyszła ujemna. Przyczyna: dowolny kierunek ortogonalny do niskich wielomianów słabo działa na
   gładkie jądro celu. Kierunek trzeba wybierać według odpowiedzi celu, tak jak robi to Mech.

## Literatura i dorobek projektu

- **Zewnętrzna:**
  - ortogonalność Gegenbauera (standard funkcji specjalnych);
  - nierówności różniczkowe i porównanie dla układów quasi-monotonicznych: Müller 1927, Kamke 1932,
    W. Walter, *Differential and Integral Inequalities* (1970). Z pamięci; dokładnych wydań nie
    otwierałem.
- **Własna:**
  - Mech-S7 ROT030–033 (klasa źródeł, momenty, wiersze gaussowskie, przebiegi ODE);
  - AUD1 ROT005 (bramy A–C);
  - LT6 ROT009 (naprawa przez rzut; inna droga do L1–L2), LT6 ROT004 (certyfikat Gronwalla);
  - pakiet NC 002 §A i M13 ROT09 (norma logarytmiczna i jej względność);
  - mój REVIEW_007 (tuba i pierwsze przecięcie);
  - MT14 ROT011 (znaki Bernsteina).
- Nowości nie zgłaszam. Wkładem jest zastosowanie: zmiana parametryzacji usuwa zależność
  operatora obserwacji od danych, a porównanie składowe zastępuje bezużyteczny tu Gronwall.

## Powrót w trzech warstwach

- **Wynik:** L1–L3 usunięte konstrukcyjnie dla wierszy momentów i wierszy gaussowskich. L4
  rozwiązane półściśle na demonstracji o strukturze Mech, z przepisem. L5 sprowadzone do jawnego
  warunku. L6 pozostaje.
- **Konfiguracja:**
  - AUD1 i LT6 dobrze nazwali luki (dokładna vs przybliżona informacja; `ε_M`; `ε±`);
  - zamiast łatać naprawę, zmieniłem pytanie: w jakiej parametryzacji operator obserwacji w ogóle
    nie zależy od danych;
  - Mech publikuje kod struktury 7D, co umożliwiło certyfikat bez jego danych.
- **Uczenie systemu:**
  - origin_observation: jeśli bramka wymaga „dokładnej informacji”, najpierw sprawdzam, czy
    dokładność da się uzyskać konstrukcyjnie przez wybór klasy, zanim zacznę ją naprawiać
    przybliżeniami;
  - przy układach sztywnych z separacją skal domyślnym certyfikatem jest porównanie składowe, a
    nie Gronwall ani pojedyncza norma.
