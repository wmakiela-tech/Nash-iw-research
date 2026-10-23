# IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018


<!-- IW_CONFORMANCE_BLOCK v1 (docs/IW_DOCUMENT_WRITE_AND_RETRIEVAL_ROUTING.md §2.7) -->
```text
artifact_id          : IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018
exposure             : PUBLIC_SAFE
canonical_body_path  : research/nc/2026-10-18/IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018.md
source_revision      : rozwiazywane przez `git log -- <canonical_body_path>`
bw_event_or_pending  : GITHUB_PENDING_BW_INGEST
claim_ceiling        : NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_INFERENCE / NO_PHYSICAL_UPGRADE / MODEL_AGREEMENT_IS_NOT_PROOF / SEARCH_FAILURE_IS_NOT_NOVELTY
hold                 : BRAK
```

ARTIFACT_ID: IW_NC_BACKACTION_LEDGER_AND_ALIGNMENT_KNIFE_EDGE_010_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
POPRZEDZA: 008, 009 (commit 2058fd3)
PREREJESTRACJE (zahaszowane przed kodem):
`PREREG_L2.md` 5399acbcf0c908009dbb6cfadca2df82ce42902fca2ce4f843f622ae619fb591
`PREREG_ALIGN.md` 1c075b7afe970e4b3e246b63f655608c4a522348761359b72ad4cc3a755491ad
KOD: `l2.py` 205d51c30e47ae036f30290b374202f62fb94443e9f8b21b7309b7585a051464,
`l2b.py` 74e27c701491dc8bd76f44c51db7960cca5760553b92c4729b7add3b8619ced3,
`l2c.py` c677751a318fb2ed409991172cc56ffc53b0b9522102344ea07912e065a2b43a,
`l2d.py` 33f72ae9c36100692c041493ceda5da84a1fe51e1bcdc88c4e75454a8d1e19fa

**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY.** Całość jest moja, łącznie z obaloną predykcją, którą
atakuję. Nie mogę zamknąć tego sam — ANTI-SELF-SEALING.

---

## 0. Co było atakowane i czym się skończyło

Zamykając ART009 zapisałem, że najpoważniejszym ograniczeniem Twierdzenia 1 jest model
szumu, i że przy szumie niezależnym **całe Twierdzenie 1 mogłoby upaść**, bo uśrednianie
zaczęłoby działać. To była prerejestrowana predykcja i jest **fałszywa**.

Ale atak nie skończył się na jej obaleniu. Wyszła z niego tożsamość dokładna, trzy
wnioski ilościowe i — najważniejsze — **obalenie zakresu mojego własnego Twierdzenia 1**.
Jest ono poprawne, lecz nazwane za szeroko: to nie jest twierdzenie o reakcji zwrotnej,
tylko o reakcji zwrotnej **współosiowej z odczytem**. Przy dowolnej niewspółosiowości
sufit nie podnosi się — **znika**.

---

## 1. Dlaczego figura zasługi miała się zmienić

Model obserwacji jest liniowy w ukrytym `y₀`: `b_j = y₀ c_j + η_j`, gdzie
`c_j = y(t_j)·σ(s_j)` i `σ(s) = (1−e^{−γs})/γ`.

| model szumu | zbiór zgodnych `y₀` | figura zasługi |
|---|---|---|
| adwersarialny per pomiar, `\|η_j\| ≤ δ` (Tw. 7.10 monografii) | przecięcie pasów | `‖c‖∞` |
| adwersarialny ze wspólnym budżetem, `‖η‖₂ ≤ δ` | kula | `‖c‖₂` |
| niezależny gaussowski `η_j ~ N(0,δ²)` | informacja Fishera `Σc_j²/δ²` | `‖c‖₂` |

Dla `k` pomiarów o równym wzmocnieniu `‖c‖₂ = √k·‖c‖∞`. Czynnik `√k` jest realny
i to on miał złamać sufit.

---

## 2. Twierdzenie — księgowanie reakcji zwrotnej (tożsamość, nie oszacowanie)

Niech `A_j²` będzie kwadratem amplitudy tuż przed pomiarem `j`, `u_j = e^{−γs_j}`.
Czujnik czyta kwadraturę `e` i tłumi kwadraturę `d`. **Przy `d = e` (współosiowość),
dla dowolnego kierunku odczytu, dowolnych czasów i dowolnych sił:**

    (γ c_j)²  =  (A_j² − A_{j+1}²) · tanh(γ s_j / 2)

Wyprowadzenie zajmuje dwie linijki: `A_j² − A_{j+1}² = y_j²(1−u_j²)`,
`(γc_j)² = y_j²(1−u_j)²`, iloraz to `(1−u_j)/(1+u_j) = tanh(γs_j/2)`.

Zmierzone na 112 547 pomiarach w losowych protokołach: największe odchylenie
`3.33·10⁻¹⁶`, czyli precyzja maszynowa. Zmierzone dla sześciu kierunków odczytu
`θ ∈ {0, 0.3, π/4, 1.2, π/2, 2.5}`: sufit zachodzi dla każdego, 120 000 protokołów,
**0 naruszeń**.

Odczyt fizyczny: **kwadrat wzmocnienia jest ubytkiem kwadratu amplitudy pomnożonym
przez sprawność `tanh(γs/2) ≤ 1`.** Informacja Fishera jest dosłownie płacona
z zachowanego budżetu amplitudy, po kursie zależnym od siły pomiaru. Dla słabego
pomiaru sprawność wynosi `≈ γs/2 → 0`: **pomiar delikatny niszczy więcej amplitudy,
niż zamienia na informację.** To ta sama inwersja, którą w ART009 §3 znalazłem dla
pomiaru ofiarnego — teraz z mechanizmem, a nie tylko ze skanu.

### Wniosek 1 — sufit przeżywa zmianę modelu szumu

`γ²‖c‖₂² = Σ_j ΔA_j²·tanh(γs_j/2) ≤ A_1² − A_końc² ≤ 1`, czyli `‖c‖₂ ≤ 1/γ`.

Skan: 280 000 losowych protokołów, `k ∈ {1,…,12}`, czasy `[0,20]`, siły `[10⁻³, 60]` —
**0 naruszeń**, maksimum `1.000000000`. Podłoga błędu znormalizowanego jest więc
`γδ/R` dla **wszystkich trzech** modeli szumu z §1. Ponieważ `‖c‖∞ ≤ ‖c‖₂`, to
wyprowadzenie zawiera Twierdzenie 1 z ART009 i zastępuje jego dowód lepszym: tamten
mnożył dwa luźne oszacowania (`|y| ≤ 1` oraz `σ < 1/γ`), ten jest prawem zachowania.

### Wniosek 2 — przy ustalonej sile na pomiar sufit jest niższy i ma postać zamkniętą

    sup γ‖c‖₂ = √( tanh(γ s / 2) )      przy ustalonym s na pomiar

Zgodność do precyzji maszynowej na 20 punktach `(γ, s)` **nieużywanych** przy
wyprowadzeniu (`γ ∈ {0.25, 0.5, 1, 2, 4}`, `s ∈ {0.13, 0.37, 1.7, 3.3}`). Optymalizacja
po czasach przy ustalonym `s` daje dokładnie wartość protokołu antywęzłowego — antywęzły
prędkości są optymalne.

Zysk z nieskończonego powtarzania wobec jednego pomiaru tej samej siły:

    √(tanh(γs/2)) / (1−e^{−γs})  =  1 / √(1 − e^{−2γs})

Zmierzone wobec wzoru: zgodność do `10⁻¹⁶` dla `s ≥ 0.05`. Dla `s = 0.02` zysk wynosi
`5.05×`. **Uśrednianie zatem DZIAŁA** — tyle że startuje z tak niskiego pułapu, że nigdy
nie dogania pojedynczego mocnego pomiaru.

### Wniosek 3 — „optymalne k = 1" przeżywa

Przy ustalonym budżecie całkowitym `S = Σs_j` maksimum `‖c‖₂` wypada na `k = 1` dla
`S ∈ {0.1, 0.5, 1, 2, 5, 20}`, dokładnie jak w normie `∞`. Dwa czynniki znoszą się
z nawiązką: dzielenie budżetu obniża każde `σ(s_j)` szybciej, niż `√k` je odbudowuje.

**Moja predykcja z ART009 §5.4 jest więc fałszywa w każdym punkcie, który miał znaczenie:**
sufit nie upada, podłoga `γδ/R` jest ta sama, optymalne `k` pozostaje jeden.
`origin_failure_mode: AGGREGATION_GAIN_COUNTED_WITHOUT_THE_RESOURCE_IT_CONSUMES`.

---

## 3. Twierdzenie — sufit jest o WSPÓŁOSIOWOŚCI, nie o reakcji zwrotnej

Tożsamość z §2 trzyma się dlatego, że czujnik tłumi **tę samą** kwadraturę, którą czyta;
wtedy `y_j²` skraca się w liczniku i mianowniku. To założenie było w ART008/009 ukryte
i nigdy go nie testowałem.

Uogólnienie: odczyt wzdłuż `e`, tłumienie wzdłuż `d`, kąt między nimi `φ`.

**Nadmiar na pomiar.** `max [(γc)² − ΔA²] = |sin φ|`, dokładnie. Zmierzone dla ośmiu
wartości `φ`, zgodność do `2·10⁻¹⁶`. Przy `φ = 0` nadmiar jest **tożsamościowo zerowy** —
stąd sufit.

**Protokół zerokosztowy.** Dla `φ ≠ 0` istnieją chwile, w których `v ⟂ d`: ubytek
amplitudy jest wtedy **zerowy**, a sygnał wynosi `A|sin φ|`. Ewolucja swobodna zeruje
`v·d` dwa razy na okres, więc protokół powtarza się w nieskończoność:

    γ‖c‖₂ = √k · |sin φ| · σ(s)    →    ∞

Zmierzone do `k = 4096`: zgodność ze wzorem do pełnej precyzji, sumaryczny ubytek
amplitudy rzędu `10⁻¹³` (zero numeryczne). Przy `φ = π/2`, `s = 1`: `γ‖c‖₂ = 40.46`
zamiast sufitu `1`.

**Kontrola negatywna.** Ten sam protokół przy `φ = 0` daje `γ‖c‖₂ = 1.8·10⁻¹¹` przy
`k = 4096` — bo tam `v ⟂ d` znaczy `v ⟂ e`, więc sygnał też znika. Zerowy koszt kupuje
się zerowym sygnałem. Dokładnie to jest treścią sufitu.

### Jak ostre jest to ostrze

Sufit nie jest łamany natychmiast. Potrzeba

    k_kryt  ≈  1 / ( σ(s)² sin²φ )

pomiarów, żeby `γ‖c‖₂` przekroczyło `1`. Zmierzone przy `s = 1`:

| niewspółosiowość | `k` potrzebne |
|---|---|
| 90° | 3 |
| 45° | 6 |
| 18° | 27 |
| 5.4° | 283 |
| 1.8° | 2 537 |
| 0.54° | 28 176 |
| 0.18° | 253 573 |

Czyli: sufit `1/γ` jest **matematycznie** ostrzem noża, ale **praktycznie** chroniony
budżetem liczby pomiarów. Przy niewspółosiowości rzędu stopnia trzeba kilku tysięcy
pomiarów, żeby cokolwiek ugrać. To jest wielkość, którą eksperyment może kontrolować,
i to jest właściwa forma tego wyniku dla kogoś, kto projektuje układ.

---

## 4. Konsekwencja dla ART009 — zwężam własne twierdzenie

Twierdzenie 1 z ART009 brzmiało: „przy reakcji zwrotnej o sile `γ` żaden protokół nie
osiąga `M ≥ 1/γ`". Dowód był poprawny, ale **sformułowanie jest za szerokie**: milcząco
zakładało `φ = 0`. Poprawne brzmienie:

> Przy reakcji zwrotnej **współosiowej z odczytem** o sile `γ` żaden protokół nie osiąga
> `‖c‖₂ ≥ 1/γ` — a tym bardziej `‖c‖∞ ≥ 1/γ`. Przy niewspółosiowości `φ ≠ 0` sufit nie
> istnieje; nadmiar na pomiar wynosi `|sin φ|`, a liczba pomiarów potrzebna do jego
> złamania to `≈ 1/(σ(s)² sin²φ)`.

To jest obalenie zakresu, nie treści. Rekomenduję wpisać to jako korektę do ART009,
a nie jako nowy claim obok niego. Decyzja należy do Moderatora.

---

## 5. Obalone predykcje własne (wszystkie prerejestrowane przed kodem)

1. **ART009 §5.4** (commit 2058fd3): „przy szumie niezależnym całe Twierdzenie 1 mogłoby
   upaść" — **FAŁSZ**. Sufit, podłoga i optymalne `k` są niezmienione.
   `origin_failure_mode: AGGREGATION_GAIN_COUNTED_WITHOUT_THE_RESOURCE_IT_CONSUMES`.
2. **PREREG_ALIGN A3**: „niewspółosiowość podnosi sufit do `1/|cos φ|`, skończonego" —
   **FAŁSZ i to w rodzaju, nie w wartości**. Nie ma podniesionego sufitu; nie ma żadnego.
   Zgadywałem skalowanie zamiast policzyć koszt amplitudowy, który przy `v ⟂ d` jest zerem.
   `origin_failure_mode: GUESSED_A_SCALING_LAW_INSTEAD_OF_COMPUTING_THE_CONSTRAINT`.
3. **Błąd w pierwszym przebiegu `l2.py`**: jako „antywęzeł prędkości" wziąłem `t = π/2`,
   które jest **węzłem** — w ART009 sam nazwałem tę chwilę „czasem ślepym". Dwie tabele
   wyszły tożsamościowo zerowe i to je ujawniło. Poprawione na `t = jπ`, do skryptu
   dopisana kontrola drukująca `|y(0)|, |y(π/2)|, |y(π)|`.
   `origin_failure_mode: REUSED_A_LANDMARK_CONSTANT_WITH_ITS_ROLE_INVERTED`.
   Wykryte przez degenerację wyjścia, nie przez przegląd kodu — ta sama rodzina co błąd
   ze świadkiem Bella z 2026-10-17.

Predykcje potwierdzone: P1, P2, P4, P5, P6, A1, A2, A4. Potwierdzona także P6:
zysk z pomiaru ofiarnego **rośnie** przy przejściu z `‖c‖∞` na `‖c‖₂`, z `1.89×` na
`2.12×`, a w szerokim oknie `[0.80, 2.35]` dwa pomiary osiągają `γ‖c‖₂ = 0.99989`,
praktycznie wysycając sufit.

---

## 6. Czego nie twierdzę

1. **Przypadek kwantowy nie jest objęty i nie wnoszę o nim niczego.** Kwantowa reakcja
   zwrotna przy pomiarze jednej kwadratury to **szum** na sprzężonej, nie **tłumienie**
   jej. Szum **podnosi** `A²`, zamiast je obniżać, więc całe księgowanie z §2 trzeba by
   napisać od nowa z innym znakiem. `φ = π/2` z tłumieniem **nie jest** modelem
   kwantowym. `COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`.
2. **Model pozostaje fenomenologiczny**: oscylator harmoniczny, skalarny stan ukryty,
   pomiar impulsowy w granicy `τ → 0` przy ustalonej sile `s = aτ`. Dla ogólnego
   generatora sufit zależałby od istnienia wielkości nierosnącej pełniącej rolę `A²`;
   **nie zbadałem, kiedy taka istnieje** — i to jest właściwe pytanie uogólniające.
3. **Nie szukałem literatury.** Kompromis informacja–zaburzenie, pomiar kwadraturowy
   i back-action evasion to motywy znane; spodziewam się gospodarzy, zwłaszcza dla §3,
   gdzie „mierz kwadraturę, której nie zaburzasz" jest z grubsza ideą pomiaru QND.
   **NIE twierdzę nowości.** `SEARCH FAILURE != NOVELTY`.
4. Tożsamość z §2 zweryfikowałem numerycznie i wyprowadziłem na dwóch linijkach; nie
   przeszła audytu zewnętrznego. **EXEC_SIGN brak.**

---

## 7. Co proponuję dalej

- **Dla DS/R1:** zaatakować §3 od strony, której nie sprawdziłem — czy `k_kryt ≈ 1/(σ²sin²φ)`
  przeżywa, gdy niewspółosiowość **dryfuje** między pomiarami zamiast być stała. Protokół
  zerokosztowy wymaga trafiania w `v ⟂ d`; przy dryfie `φ(t)` może się rozstroić.
- **Dla Gemini:** runtime na uogólnionym generatorze — kiedy istnieje wielkość nierosnąca
  grająca rolę `A²` (§6.2). To jest pytanie o normę logarytmiczną i wraca do M13.
- **Dla Moderatora:** decyzja, czy §4 wchodzi jako korekta ART009, czy jako osobny claim.

---

KONIEC. Status [▷]. EXEC_SIGN brak. Audyt zewnętrzny obowiązkowy.
