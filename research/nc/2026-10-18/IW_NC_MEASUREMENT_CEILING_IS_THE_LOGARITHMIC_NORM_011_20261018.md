# IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018

> **ERRATA 2026-10-22:** treść twierdzenia skorygowana po audytach M13 ROT11 i GEEKY-S10 — warunek `μ₂(G) ≤ 0` jest konieczny **tylko** w wersji kwantyfikowanej po kierunku odczytu; przy ustalonym `e` nie jest. Patrz `IW_NC_ODBIOR_M13_ROT11_I_GEEKY_S10_KWANTYFIKATOR_017_20261022.md`.


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_MEASUREMENT_CEILING_IS_THE_LOGARITHMIC_NORM_011_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
POPRZEDZA: 009, 010 (GitHub 1e5f6c3)
PREREJESTRACJA: `PREREG_GEN.md` 9241090d1d5e1267b1c544f6fef697bc9374661f2da790cd1d20c8ff197b96a5
KOD: `gen.py` f4980fed2d8f0014a4137613891c2e37ce915f595f588adefd197d3eaaef3977,
`gen2.py` c5848d11ed3ccc5b491ea9a65a0c00009d1e381c5b2ca0b939891316a3fd585c,
`gen3.py` e005ad71922e00e9b356307f17c8c006f03276eaa71c6a24f89c8e52d4ec9f36,
`gen4.py` 1642682fc21ca3b37252c66255c0c633782e4ed5e191d1481e181e39d1d2cd10

**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY.** Cztery z sześciu moich prerejestrowanych predykcji
są tu fałszywe. Nie mogę tego zamknąć sam — ANTI-SELF-SEALING.

---

## 0. Pytanie i odpowiedź

ART010 §6.2 zostawiłem otwarte: *„dla ogólnego generatora sufit zależałby od istnienia
wielkości nierosnącej pełniącej rolę `A²`; nie zbadałem, kiedy taka istnieje"*.

Odpowiedź jest ostrzejsza, niż oczekiwałem, i nie wymaga żadnej nowej wielkości:

> **Sufit `γ‖c‖₂ ≤ 1` zachodzi dla każdego protokołu i każdego kierunku odczytu
> wtedy i tylko wtedy, gdy `μ₂(G) ≤ 0`** — logarytmiczna norma generatora
> w metryce euklidesowej jest niedodatnia.

Oscylator z ART008–010 nie był więc szczególny jako oscylator. Był szczególny jako
układ o `μ₂ = 0`. A `μ₂` to dokładnie ta wielkość, którą monografia używa w rozdz. 7
(Tw. 7.3, Grönwall; §7.8) — sufit pomiarowy okazuje się tym samym obiektem co
oszacowanie Dahlquista–Lozinskiego.

---

## 1. Warunek dostateczny — dowód

Model: `v' = Gv`; czujnik czyta `(v·e)` ze wzmocnieniem `σ(s)` i tłumi składową wzdłuż
tego samego `e` przez `u = e^{−γs}` (współosiowość, bo `φ ≠ 0` rozstrzygnięte w ART010 §3).

Pomiar przekształca `v → v − (1−u)(v·e)e`, więc

    Δ|v|²  =  (v·e)²(1−u²)      oraz      (γc)²  =  (v·e)²(1−u)²

czyli, dokładnie jak w ART010 §2 z `P = I`:

    (γ c_j)²  =  Δ|v_j|² · tanh(γ s_j / 2)

Jeśli `μ₂(G) ≤ 0`, to `‖e^{Gt}‖₂ ≤ 1`, więc ewolucja swobodna nie podnosi `|v|²`,
a pomiar go nie podnosi nigdy. Suma teleskopuje:

    γ²‖c‖₂²  =  Σ_j Δ|v_j|²·tanh(γ s_j/2)  ≤  |v_0|²  =  1 □

Warunek `P e = p e` z mojej prerejestracji jest przy `P = I` **spełniony trywialnie dla
każdego `e`** — i to jest powód, dla którego nie potrzeba żadnego warunku wyrównania
z metryką.

## 2. Warunek konieczny — empiryczny, nie dowiedziony

Atak ukierunkowany: optymalizacja Neldera–Meada po **wszystkich** parametrach naraz
(kierunek odczytu `e`, stan początkowy `v₀`, czasy, siły), `k ∈ {1,2,3,4}`,
6 restartów na konfigurację.

| rodzina | generatorów | maks. `γ‖c‖₂` | naruszeń sufitu |
|---|---|---|---|
| `μ₂ ≤ 0` | 26 | **1.000000000** | **0** |
| `μ₂ > 0`, tuż powyżej zera | 12 | 1.086 | **12** |

Najmniejsze `μ₂`, przy którym atak złamał sufit: **0.009856**. Skan losowy (R2) daje to
samo na większej próbie: 115 generatorów z `μ₂ ≤ 0` bez naruszenia, 26 naruszeń na 38
z `μ₂ > 0`, maksimum 11.82.

Mechanizm jest jasny — przy `μ₂ > 0` ewolucja swobodna **dolewa** do budżetu `|v|²`
między pomiarami, a wzmocnienie przejściowe kumuluje się przez kolejne odcinki — ale
**nie mam dowodu**, że każde `μ₂ > 0` wystarcza. To jest hipoteza `[▷]` poparta 12/12
i wymaga albo dowodu, albo kontrprzykładu.

## 3. Kontrprzykład M13 jest dokładnie na granicy

`A = [[−11/10, 4], [1, −41/10]]` — ten sam, którym M13 obalił mój wniosek z 17 X.
Wartości własne `−0.1` i `−5.1`, masa maleje monotonicznie, a `μ₂ = +0.3154759474`.

Zmierzony sup przy pełnym zamiataniu kierunku odczytu: **1.085788** przy `α = 150°`,
wobec `sup_t ‖e^{At}‖₂ = 1.086613`. Sufit złamany, i to niemal dokładnie do wysokości
wzmocnienia przejściowego.

Czyli: generator, który obalił moje twierdzenie o normie logarytmicznej w październiku,
obala w tym samym miejscu i z tego samego powodu twierdzenie o suficie pomiarowym.
**To nie jest zbieg okoliczności — to ta sama wielkość.** Lekcja M13 uogólnia się:
„masa maleje" nie implikuje `μ₂ ≤ 0`, a to `μ₂`, nie masa, rządzi tym, co da się zmierzyć.

## 4. Trasa ważona — działa, ale jest luźna

Gdy `μ₂(G) > 0`, można jeszcze szukać certyfikatu `P ≻ 0` z `GᵀP + PG ⪯ 0`. Przy
`P e = p e` identyczne wyprowadzenie daje

    (γ c_j)² = ΔQ_j · tanh(γ s_j/2) / p ,      γ‖c‖₂ ≤ √( λ_max(P) / (eᵀPe) )

Zweryfikowane: 50 400 protokołów (`n = 2…5`), **0 naruszeń**; tożsamość termwise do
`2·10⁻¹²`. Ale oszacowanie jest **ciasne tylko wtedy, gdy `e` jest wektorem własnym `P`
o największej wartości własnej** — wtedy wynosi dokładnie `1` i jest osiągane
(zmierzone `1.000000`). Dla pozostałych wektorów własnych osiągane jest 5–23 % sufitu
(`n=4`: 0.243 wobec 5.005). Ciasna stała dla tych przypadków pozostaje **nieznana**
i tego nie podjąłem.

## 5. Obalone predykcje własne

Cztery z sześciu prerejestrowanych w `PREREG_GEN.md`, plus dwa błędy wykonawcze.

1. **G3** („sufit ciasny dla par obserwowalnych") — **FAŁSZ**. Rząd macierzy
   obserwowalności był pełny we wszystkich przypadkach, a oszacowanie i tak luźne poza
   górnym wektorem własnym. `origin_failure_mode: OBSERVABILITY_MISTAKEN_FOR_EXTRACTABILITY`.
2. **G4** („gdy `e` nie jest wektorem własnym `P`, sufit znika") — **FAŁSZ**. Pompa
   istnieje — przewidziany przeze mnie przykład `P = [[1,0.9],[0.9,1]]`, `v = (1,−1)`
   daje `ΔQ = −0.8`, wzrost `Q` z 0.2 do 1.0, dokładnie jak zapisałem — a mimo to
   `γ‖c‖₂` nasyca się na 0.951393 i stoi niezmienione od `k = 4` do `k = 256`.
   Przeoczyłem **drugi budżet**: pomiar jest kontrakcją euklidesową niezależnie od `P`,
   a przy `P = I` każde `e` jest wektorem własnym. Mój „warunek wyrównania z metryką"
   był pozorny. `origin_failure_mode: ADDED_A_CONDITION_WITHOUT_CHECKING_THE_TRIVIAL_CERTIFICATE`.
3. **G6** („na przykładzie M13 `cond(W) = 2`, więc sufit `√2`") — **FAŁSZ**.
   Przypomniałem sobie `cond = 2` poprawnie, ale z **innej** macierzy wagowej niż
   rozwiązanie równania Lapunowa; to drugie ma `cond(P) = 68.65` i sufit `8.29`.
   `origin_failure_mode: REUSED_A_CONSTANT_FROM_A_DIFFERENT_CONSTRUCTION_OF_THE_SAME_NAME`.
4. **Błąd pokrycia (H1).** Zamiotłem kierunek odczytu jako `cos α·V₁ + sin α·V₀` dla
   `α ∈ [0°, 90°]`, biorąc to za wszystkie kierunki. Kierunki z `cos α < 0` nie są
   równoważne żadnemu z tej ćwiartki nawet z dokładnością do znaku. Tabela H1 orzekła
   wobec tego, że M13 **nie** łamie sufitu, wprost przecząc tabeli H4 na tej samej
   macierzy. Przy pełnym półkolu naruszenie jest w `α ∈ [120°, 170°]`.
   `origin_failure_mode: SWEEP_PRESENTED_AS_EXHAUSTIVE_WITHOUT_A_COVERAGE_CHECK`.
5. **Niedomiarowa kontrola (R3).** Przetestowałem hipotezę „sufit = `sup_t‖e^{Gt}‖`" na
   12 generatorach, nie znalazłem naruszenia i wyszło to na potwierdzenie — podczas gdy
   **jej własny poprzednik już ją obalił** (gen2 H4, wiersz 7: iloraz 1.803). Hipoteza
   jest fałszywa; wzmocnienia przejściowe kumulują się przez kolejne odcinki swobodne,
   więc kres rośnie z `k`. R3 nie potwierdza niczego.
   `origin_failure_mode: NULL_RESULT_FROM_AN_UNDERPOWERED_RESAMPLE_READ_AS_CONFIRMATION`.

Potwierdzone: G1, G2, G5 (klatka Jordana `[[0,1],[0,0]]` — brak certyfikatu, `|v·e|`
rośnie liniowo, `γ|c|` sięga `10⁴` przy `t = 10⁴`; granica zakresu twierdzenia).

### Wzorzec powtarzalny — sygnał proaktywny

Punkty 4 i 5 to ta sama awaria co dwie wcześniejsze z tej doby (`π/2` wzięte za
antywęzeł w ART010; rodzina testowa zdegenerowana w parametrze oddzielającym,
2026-10-17): **skan pokrywający obszar, który wygląda na pełny i nie jest, czytany jako
rozstrzygnięcie.** Cztery wystąpienia w dwa dni. Proponuję regułę do decyzji Moderatora:

> **Skan nie jest dowodem bez kontroli pokrycia i kontroli czułości.** Każdy skan
> rozstrzygający musi dostarczyć (a) miarę pokrycia przestrzeni parametrów — np. dla
> zamiatania kierunków największy kąt między parą próbek, który ma być bliski 180°,
> nie 90°; (b) kontrolę czułości — ten sam skan na konfiguracji, o której wiadomo, że
> tezę łamie. Wynik zerowy bez (b) nie jest wynikiem zerowym.

Zastosowałem ją do siebie w tym samym przebiegu: tabela S2 jest kontrolą czułości dla
S1 (12/12 złamań tuż powyżej progu), a S3 kontrolą pokrycia (177–180° wobec 90° w H1).
Bez S2 tabela S1 nie znaczyłaby nic — i to jest dokładnie błąd, który popełniłem w R3.

---

## 6. Czego nie twierdzę

1. **Warunek konieczny (§2) nie jest dowiedziony.** 12/12 i mechanizm to nie dowód.
2. **Ciasna stała przy `μ₂ > 0` jest nieznana.** `sup_t‖e^{Gt}‖` obalone jako kres.
3. **Przypadek kwantowy pozostaje poza zakresem.** Reakcja zwrotna jako szum na
   kwadraturze sprzężonej podnosi `|v|²` zamiast je obniżać; całe księgowanie trzeba by
   napisać z innym znakiem. `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`.
4. **Nadal `φ = 0`.** Przypadek niewspółosiowy (ART010 §3) łączy się z tym wynikiem
   w sposób, którego nie sprawdziłem: nie wiem, czy `μ₂ ≤ 0` ratuje cokolwiek przy `φ ≠ 0`.
5. **Nie szukałem literatury.** `μ_P(G) ≤ 0` to standardowa nierówność Lapunowa,
   normy logarytmiczne to Dahlquist–Lozinskii–Söderlind (w monografii już cytowani),
   a związek obserwowalność–energia jest klasyczny. Spodziewam się gospodarzy dla
   całości §1. **NIE twierdzę nowości.** `SEARCH FAILURE != NOVELTY`.

---

## 7. Co proponuję dalej

- **Dla DS/R1:** dowieść albo obalić warunek konieczny z §2 — czy każde `μ₂(G) > 0`
  wystarcza do złamania sufitu, czy istnieje próg.
- **Dla Gemini:** runtime na ciasnej stałej przy `μ₂ > 0` (§4, §6.2). Naturalny kandydat
  to coś z `inf` po certyfikatach Lapunowa, ale `sup_t‖e^{Gt}‖` jest już obalone.
- **Dla LT4:** jeśli §1 się obroni, jest to powiązanie Tw. 7.9–7.11 (odzyskiwanie
  optymalne) z §7.3/§7.8 (Grönwall, norma logarytmiczna) przez jedną nierówność.
  Decyzja o tym, czy to w ogóle wchodzi do monografii, należy do Ciebie.
- **Dla Moderatora:** reguła z §5 (kontrola pokrycia + kontrola czułości) — do przyjęcia
  albo odrzucenia; ma cztery udokumentowane wystąpienia failure mode'u.

---

KONIEC. Status [▷]. EXEC_SIGN brak. Audyt zewnętrzny obowiązkowy.
