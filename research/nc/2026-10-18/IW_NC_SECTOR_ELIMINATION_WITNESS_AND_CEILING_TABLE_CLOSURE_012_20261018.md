# IW_NC_SECTOR_ELIMINATION_WITNESS_AND_CEILING_TABLE_CLOSURE_012_20261018

> **ERRATA 2026-10-19:** część ustaleń tego zwrotu skorygowana po audytach INT7 i REC9 — patrz `IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019.md`. Treść poniżej pozostaje w wersji oryginalnej.

ARTIFACT_ID: IW_NC_SECTOR_ELIMINATION_WITNESS_AND_CEILING_TABLE_CLOSURE_012_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
POPRZEDZA: 007 (dziura §2.8), 010, 011 (GitHub 34bedce)
KOD: `garble.py` 5924cdbcd6d077f699d1841b5274b43f4870081cedf194b612a1337c20b9e2c5 **(odrzucony)**,
`garble2.py` fefb47e8236358ef173624805697bebb646528430d5687cfa240e2a65ca5a154 **(pusty wynik)**,
`garble3.py` 35da3d0918e0cb76b703c293b71b6d016201cc08c96848479b5dcb2fa945a47c,
`cross.py` 83a18bbdd64797ae12e7fdd0bf28a3d5cde31db45c93041ece87893fd576a961,
`cross3.py` ebdad567d8ceedd71b329efc7edc18e1e3dd455ec9f1f00efc81b71ffe129aa6

**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY.**

---

## 1. Domknięcie dziury §2.8 — świadek rozdzielający garbling od eliminacji sektora

W 007 §4 zostawiłem tę pozycję otwartą, pisząc, że potrzebny jest *„świadek rozdzielający
garbling od eliminacji sektora dla konkretnej obserwabli"*, i odrzuciłem uwagę z rozdz. 1 §8
(`ρ ↦ VρV*` zmniejsza ślad) jako **nie ten obiekt**.

### Definicje — bez nich cały non-map nie ma treści

- **Garbling (Blackwell).** Ustalony pomiar `M`; rozkład wyników przepuszczony przez macierz
  stochastyczną `L`. Działa na **rozkładzie wyników**, zachowuje masę.
- **Eliminacja sektora.** Rzut `P` na podprzestrzeń, `ρ ↦ PρP`, potem pomiar `M`. Działa
  na **stanie**, nie zachowuje śladu.

### Dlaczego trywialna separacja nie wystarcza

Garbling zachowuje masę, eliminacja nie — i to jest dokładnie obserwacja rozdz. 1 §8.
Separacja na tym oparta jest jej przepisaniem, nie nowym świadkiem. Mocniejsze i właściwe
pytanie brzmi: **modulo normalizację** — przy postselekcji na przeżyciu, gdzie utrata śladu
jest nieobserwowalna — czy eliminacja sektora jest garblingiem?

### Świadek

Rzut rzędu 1 daje `|θ⟩⟨θ|` niezależnie od `ρ`, więc po postselekcji nie rozróżnia niczego;
świadek wymaga rzutu rzędu ≥ 2, czyli wymiaru ≥ 3. Dla `P = I − nnᵀ`, `n = (1,1,1)/√3`:

    (PρP)_kk = ρ_kk − (2/3)·Re r_k + S/9,      tr(PρP) = 1 − S/3

gdzie `r_k` to suma k-tego wiersza, `S` suma wszystkich wyrazów. **Przeżycie zależy wyłącznie
od `S`**, a diagonala po postselekcji od poszczególnych `Re r_k`. Wystarczy więc para o tej
samej diagonali i tym samym `S`, lecz innym rozkładzie koherencji:

    ρ₁ = [[1/2, 1/5,  0 ],      ρ₂ = [[1/2,  0,   0 ],
          [1/5, 3/10, 0 ],            [ 0,  3/10, 1/5],
          [ 0,   0,  1/5]]            [ 0,   1/5, 1/5]]

Obie dodatnio określone (`λ_min = 0.176393` i `0.043845`), obie o śladzie 1.

| warunek | `ρ₁` | `ρ₂` | |
|---|---|---|---|
| diagonala w bazie `M` | (1/2, 3/10, 1/5) | (1/2, 3/10, 1/5) | **identyczna** |
| `tr(PρP)` | 8/15 | 8/15 | **identyczne** |
| diagonala po postselekcji | (17/48, 11/48, 20/48) | (29/48, 11/48, 8/48) | **różna o 1/4** |

Identyczna diagonala oznacza, że **żaden** garbling ich nie rozróżni — `L` działa na rozkładzie,
a rozkłady są równe. Zweryfikowane skanem po pełnej klasie macierzy stochastycznych 3×3
(300 000 próbek z pełnego sympleksu kolumnowego): największa różnica wyjść `0.000e+00`.
Identyczne przeżycie oznacza, że **ślad nie wykonuje tu żadnej pracy** — separacja jest
wyłącznie o koherencji niewidocznej dla `M`. To odróżnia świadka od rozdz. 1 §8.

### Trzy kontrole

1. **Rzut komutujący z `M`** (`diag(1,1,0)`): różnica `0.000e+00`. Świadek musi tam zawodzić
   i zawodzi — sektor współosiowy z pomiarem **da się** odtworzyć garblingiem.
2. **Rzut rzędu 1**: różnica `5.6·10⁻¹⁷`. Potwierdza konieczność rzędu ≥ 2.
3. **Kontrola czułości skanu garblingów**: ta sama pętla na parze o *różnych* diagonalach
   daje `0.0897`, więc skan potrafi wykryć różnicę, gdy ta istnieje.

**Rekomendacja dla LT4.** §2.8 ma świadka; zdanie można zostawić, dopisując, że separacja
zachodzi także po postselekcji i wymaga sektora niewspółosiowego z pomiarem oraz
współwymiaru ≥ 1 w przestrzeni wymiaru ≥ 3. Druga z otwartych pozycji 007 (**§3.6**,
przybliżona minimalność w nieskończonym wymiarze) **pozostaje otwarta** — to pytanie
o literaturę nieskończeniewymiarowej teorii realizacji, którego nie podjąłem.

---

## 2. Korekta do ART011 §6.4 i domknięcie tabeli 2×2

W 011 §6.4 zapisałem jako otwarte pytanie, czy `μ₂ ≤ 0` ratuje sufit przy `φ ≠ 0`.
**To nie było otwarte** — sam to rozstrzygnąłem w 010 §3: oscylator `x' = y, y' = −x` ma
`G` skośnie symetryczne, więc `μ₂ = 0 ≤ 0`, a sufit tam znika (40.46 przy `k = 4096`).
Nie połączyłem dwóch własnych wyników.
`origin_failure_mode: DECLARED_OPEN_A_QUESTION_ALREADY_ANSWERED_BY_AN_EARLIER_OWN_ARTIFACT`.

Sprawdziłem, czy `μ₂ = 0` nie było przypadkiem brzegowym. Dla `G = [[−a, 1], [−1, −a]]`
(`μ₂ = −a`), atak ukierunkowany po `(czasy, siły, stan)` przy `φ = π/2`, `k = 8`:

| `a` | 0.0 | 0.05 | 0.2 | 0.5 | 0.8 | 1.2 | 2.0 |
|---|---|---|---|---|---|---|---|
| sup `γ‖c‖₂` | 2.83 | 2.31 | 1.61 | 1.99 | 1.83 | 1.72 | 1.73 |

**Progu tłumienia nie ma.** Sufit łamie się przy każdym `a` aż do 2.0; bisekcja po `a` dla
siedmiu wartości `φ` dobija do górnego ogranicznika przedziału (3.0) zamiast znaleźć próg.
Kontrola czułości: ten sam atak przy `φ = 0` daje **równo 1.000000000** dla każdego `a`.

**Tabela domknięta:**

| `φ` | `μ₂` | sufit `γ‖c‖₂ ≤ 1` | źródło |
|---|---|---|---|
| `= 0` | `≤ 0` | **TAK** (dowód) | 011 §1; `gen4` S1: 26 gen., maks. 1.000000000 |
| `= 0` | `> 0` | NIE | 011 §2; `gen4` S2: 12/12 złamań |
| `≠ 0` | `≤ 0` | NIE | 010 §3 + `cross3` T1 powyżej |
| `≠ 0` | `> 0` | NIE (a fortiori) | zawiera się w obu powyższych |

Czyli: **sufit wymaga obu warunków naraz** — współosiowości reakcji zwrotnej z odczytem
**oraz** niedodatniej normy logarytmicznej. Każdy z osobna nie wystarcza.

---

## 3. Błędy własne w tym zwrocie

1. **Pierwszy świadek dla §2.8 odrzucony — przez mój własny test.** `garble.py` konstruował
   parę `|+⟩⟨+|` wobec `I/2`, nierozróżnialną przez garbling i rozróżnianą przez eliminację.
   Tabela Q4 pokazała, że po renormalizacji oba stany dają to samo `|+⟩⟨+|`, więc rozróżniało
   je **wyłącznie prawdopodobieństwo przeżycia**, czyli ślad — a to jest obserwacja rozdz. 1
   §8, którą w 007 sam odrzuciłem jako *nie ten obiekt*. Byłbym popełnił dokładnie tę
   konflację, przed którą ten non-map ostrzega.
   `origin_failure_mode: WITNESS_REPRODUCED_THE_VERY_IDENTIFICATION_THE_NONMAP_FORBIDS`.
   Wykryte przez kontrolę, którą dopisałem, bo pamiętałem własne zastrzeżenie z 007 — czyli
   przez bibliotekę, nie przez intuicję.
2. **`garble2.py` — szukanie numeryczne zwróciło pustkę.** Nie dlatego, że świadka nie ma,
   lecz dlatego, że kara w funkcji celu była źle uwarunkowana. Dwie linijki algebry dały
   konstrukcję jawną i wymierną. `origin_failure_mode: OPTIMIZED_BEFORE_DOING_THE_ALGEBRA`.
3. **Odczyt tabeli C1 jako własności układu.** Przy `a = 0.2` protokół regularny dawał
   0.8206 < 1 i odczytałem to jako możliwy próg tłumienia. To była własność **ustalonego
   protokołu**, nie układu — atak ukierunkowany daje tam 1.61.
   `origin_failure_mode: FIXED_PROTOCOL_SCAN_READ_AS_A_PROPERTY_OF_THE_SYSTEM`.
   Piąte wystąpienie rodziny, dla której w 011 §5 zaproponowałem regułę; tu reguła
   **zadziałała** — wstrzymałem zapis komórki tabeli i uruchomiłem atak, zamiast zapisać C1.
4. **Operacyjny, nie naukowy:** `pkill -f cross2.py` dopasował treść polecenia, które samo
   zawierało ten ciąg w komentarzu, i zabiło własną powłokę przed zapisem pliku.

---

## 4. Sygnał proaktywny — gravity well

**Zgłaszam zgodnie z regułą o kontroli fokusu.** Zwroty 008, 009, 010, 011 i część 012 to
pięć kolejnych artefaktów na jednym wątku (sufit pomiarowy przy reakcji zwrotnej), każdy
atakujący poprzedni, wszystkie w ciągu jednej doby i **wszystkie `[▷]`, żaden nieaudytowany**.

Wątek jest produktywny — dał tożsamość dokładną, kryterium `μ₂ ≤ 0` i domkniętą tabelę 2×2 —
ale test użyteczności z instrukcji brzmi: *czy zostało użyte, zmniejszyło obciążenie
Moderatora albo zwiększyło odporność epistemiczną*. Szósty artefakt na nieaudytowanym stosie
**zwiększa** obciążenie Moderatora, zamiast je zmniejszać.

Dlatego §1 tego zwrotu jest celowo z innego wątku: to dług z 007, praca audytowa nad tekstem
LT4, użyteczna dla kogoś innego niż ja. Proponuję, żeby kolejne moje tury szły w tę stronę
(§3.6, świadek ciągłości dla §7.2, karta J3 005 czekająca ósmy dzień), a wątek sufitu wrócił
dopiero po audycie zewnętrznym. **Decyzja o fokusie należy do Ciebie, nie do mnie** —
zgłaszam, nie rozstrzygam.

---

## 5. Czego nie twierdzę

1. **Nowości — nigdzie.** Rozróżnienie garbling/eliminacja sektora to w istocie różnica
   między kanałem klasycznym na wynikach a operacją na stanie; porządek Blackwella,
   degradowalność kanałów i niemożność symulacji operacji kwantowej klasycznym
   postprzetwarzaniem to motywy znane. Spodziewam się gospodarzy dla §1.
   **NIE szukałem literatury.** `SEARCH FAILURE != NOVELTY`.
2. **Świadek z §1 jest konstrukcją w `C³`.** Nie twierdzę, że separacja zachodzi w każdej
   konfiguracji — przeciwnie, dwie kontrole pokazują, kiedy **nie** zachodzi (sektor
   współosiowy z pomiarem; rzut rzędu 1).
3. **§3.6 pozostaje otwarte.** Nie przypisuję nikomu wyniku, którego nie sprawdziłem.
4. **Brak progu tłumienia (§2) zmierzony do `a = 2.0`** i przy `k ≤ 16`. Dla bardzo silnego
   tłumienia albo bardzo wielu pomiarów nie sprawdzałem.
5. **EXEC_SIGN brak** dla całości.

---

KONIEC. Status [▷]. EXEC_SIGN brak. Audyt zewnętrzny obowiązkowy.
