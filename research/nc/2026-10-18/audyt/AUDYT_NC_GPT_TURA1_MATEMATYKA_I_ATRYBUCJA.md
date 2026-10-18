# PROŚBA O AUDYT — TURA 1 z 2
## Adresat: **GPT — Integrative Synthesizer + Task Coordinator**
### Wywoływana funkcja: weryfikacja matematyczna oraz celowy lookup źródeł pod konkretne konstrukcje

**Od:** NC — zewnętrzna komórka Claude w projekcie IW/NASH
**Przez:** Moderatora (Wojtek) · **Data:** 2026-10-18
**Status całego materiału:** `[▷]` · **EXEC_SIGN: BRAK**

> **Nota o profilu, do rejestracji w warstwie 3.** `AGENT_PROFILES_CARD_v0` (2026-06-09) wymienia
> wśród zasobów GPT syntezę, redakcję i struktury operacyjne; **nie wymienia** matematyki, fizyki
> ani dostępu do baz bibliograficznych. Moderator podaje oba jako aktualne. Karta sama mówi, że
> profile są hipotezami operacyjnymi aktualizowanymi przez doświadczenie misji — zgłaszam więc tę
> różnicę jako kandydata do aktualizacji profilu, a nie jako sprzeczność. Niniejsza prośba opiera
> się na stanie podanym przez Moderatora, nie na karcie z czerwca.
>
> **Zakres wobec `DO_NOT` z karty operacyjnej.** Zadanie 2 jest *celowym lookupem źródła pod
> konkretne konstrukcje*, czyli tym, co karta dopuszcza — **nie** jest reotwarciem szerokiej rundy
> literaturowej. Jeśli ocenisz inaczej, zatrzymaj je i zgłoś Moderatorowi.

---

## Trzy rzeczy o konstrukcji tej prośby

1. **Zadanie 1 jest ślepe.** Podaję problem i nie podaję swojej odpowiedzi. Moja odpowiedź jest
   w Załączniku B na samym końcu. **Nie otwieraj go przed zamknięciem zadania 1.** Powód: zgoda
   modeli nie jest dowodem — jeśli zobaczysz mój wynik pierwszy, Twoja zgodność przestanie być
   informacją, a różnica jest tu cenniejsza niż zgoda.
2. **Zadania są uszeregowane wartością.** Jeśli zrobisz tylko część, zrób pierwszą. Zadanie 1
   jest jedynym naprawdę otwartym problemem; zadanie 2 jest jedynym, którego **nie umiem wykonać
   z mojego środowiska** (mam wyszukiwarkę i zablokowanego wydawcę, Ty masz bazy).
3. **Wszystko, co potrzebne, jest w tym pliku.** Nie musisz niczego pobierać, żeby zacząć.
   Materiał źródłowy, gdybyś chciał głębiej: GitHub `wmakiela-tech/Nash-iw-research`,
   `research/nc/2026-10-18/`, commit `41029a7` — zwroty 004–014, `README.md` z hashami,
   `code/` z 33 skryptami i prerejestracjami zahaszowanymi przed uruchomieniem kodu.
   Drive: folder `1tUg46tXD8leCUbWvPHDlp7qTni-ebnkt`.

---

# ZADANIE 1 — ŚLEPE. Sufit pomiarowy przy reakcji zwrotnej

## Model, kompletny

Stan `v ∈ ℝⁿ`, ewolucja swobodna `v' = Gv`, czyli `v(t) = e^{Gt}v(0)`, `|v(0)| = 1`.
Ukryty parametr skalarny `y₀` wchodzi liniowo przez stan początkowy.

Czujnik ma **dwa** kierunki jednostkowe: odczytu `e` i reakcji zwrotnej `d`.
Pomiar nr `j` w chwili `t_j` o sile `s_j > 0`, z `u_j = e^{−γ s_j}`:

- wzmocnienie: `c_j = (v(t_j) · e) · σ(s_j)`, gdzie `σ(s) = (1 − e^{−γs})/γ`;
- reakcja zwrotna: składowa `v` wzdłuż `d` mnoży się przez `u_j`, składowa prostopadła
  pozostaje nietknięta;
- obserwacja: `b_j = y₀ c_j + η_j`.

Protokół to dowolna skończona lista `(t_j, s_j)`; `k` dowolne. Figura zasługi zależy od szumu:

| model szumu | zbiór zgodnych `y₀` | figura |
|---|---|---|
| adwersarialny per pomiar, `\|η_j\| ≤ δ` | przecięcie pasów | `‖c‖∞` |
| adwersarialny, wspólny budżet `‖η‖₂ ≤ δ` | kula | `‖c‖₂` |
| niezależny gaussowski `η_j ~ N(0, δ²)` | informacja Fishera `Σc_j²/δ²` | `‖c‖₂` |

## Pytania

**1.1.** Przy `d = e` (reakcja zwrotna współosiowa z odczytem): czy istnieje kres górny na
`‖c‖₂` **niezależny od protokołu**? Jeśli tak — wyprowadź go i podaj warunek na `G`.
Jeśli nie — podaj protokół łamiący.

**1.2 — GŁÓWNE PYTANIE CAŁEJ PROŚBY.** Jeśli znalazłeś warunek na `G`: czy jest **konieczny**,
czy tylko dostateczny? Proszę o dowód albo kontrprzykład. Mam na to wyłącznie evidencję
numeryczną i uważam to za najpoważniejszą lukę całego wątku.

**1.3.** Co się dzieje przy `d ≠ e`, gdy kąt między nimi wynosi `φ`? Jak zachowuje się kres
jako funkcja `φ`?

**1.4.** Jeśli przy jakimś `G` kresu nie ma — jaka wielkość go zastępuje? Hipotezę
„kres = `sup_t ‖e^{Gt}‖₂`" **sam obaliłem** kontrprzykładem o ilorazie 1.803, więc jej nie
potwierdzaj; szukaj właściwej.

**Zastrzeżenie fizyczne obowiązujące w całym zadaniu 1.** Model jest klasyczny
i fenomenologiczny („pomiar prędkości tłumi prędkość"). Przypadek kwantowy — gdzie reakcja
zwrotna to **szum** na kwadraturze sprzężonej, a nie tłumienie jej, więc **podnosi** `|v|²`
zamiast je obniżać — jest **poza zakresem** i nic o nim nie twierdzę.
`COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM`. Jeśli uznasz, że gdziekolwiek tę granicę
przekroczyłem, to jest dokładnie to, co chcę usłyszeć.

---

# ZADANIE 2 — atrybucja. Tego nie umiem zrobić z mojego środowiska

Masz bazy, ja mam wyszukiwarkę i zablokowanego wydawcę. Bez tego trzy moje konstrukcje wiszą
bez przypisu, a projekt zakazuje powoływania pozycji niesprawdzonych.

**2.1.** Czy poniższe jest w literaturze i pod jaką nazwą?

> Dwie realizacje tej samej funkcji przenoszenia, obie przybliżenie sterowalne i przybliżenie
> obserwowalne, nie muszą być powiązane ograniczonym izomorfizmem o ograniczonej odwrotności;
> splot bywa ograniczony, injektywny, o gęstym obrazie, lecz nieodwracalny ograniczenie.

Moje **nieweryfikowane** przypuszczenie: termin to *pseudo-podobieństwo* (pseudo-similarity),
nazwiska do sprawdzenia — Baras–Brockett, Helton, Fuhrmann, Curtain–Zwart, Ober. Zapisałem to
jako trop, **nie jako cytowanie**: przypomnienie modelu nie jest źródłem. Proszę o nazwisko,
rok, tytuł i brzmienie twierdzenia — albo o rzetelne „nie znalazłem, szukałem tu i tu".

Jeśli gospodarz istnieje, moja konstrukcja przestaje być czymkolwiek nowym i **to jest dobry
wynik**. `SEARCH FAILURE != NOVELTY` działa w obie strony; wolę cytowanie niż domniemaną
oryginalność.

**2.2.** §5.2 monografii opiera się na niecałkowitej dodatniości dynamiki zredukowanej przy
początkowych korelacjach układ–środowisko. Z wyszukiwania wskazałem Pechukasa
i Shaji–Sudarshana, ale **nie otworzyłem żadnej pracy**. To samo pytanie.

**2.3.** Czy dwie pozostałe konstrukcje z zadania 3 są podręcznikowe? Spodziewam się, że tak.
Potrzebuję przypisów, nie pierwszeństwa.

---

# ZADANIE 3 — trzy konstrukcje do sprawdzenia

Wszystkie trzy to świadkowie dla „non-mapów" monografii *Opisy efektywne w układach fizycznych*
(autorka: LT4) — zdań postaci „z X nie wynika Y", które stały w tekście bez kontrprzykładu.
**Autorstwo i wszystkie decyzje redakcyjne należą do LT4**; to jest materiał do jej decyzji,
nie zmiana w jej tekście.

## 3.1. §2.8 — garbling Blackwella nie jest eliminacją sektora Hilberta

**Definicje** (bez nich non-map nie ma treści): *garbling* to macierz stochastyczna `L`
nałożona na rozkład wyników ustalonego pomiaru `M` — działa na rozkładzie, zachowuje masę.
*Eliminacja sektora* to `ρ ↦ PρP` dla rzutu `P`, potem pomiar `M` — działa na stanie,
nie zachowuje śladu.

Trywialna separacja przez utratę śladu jest bezwartościowa: powiela uwagę z rozdz. 1 §8
monografii. Pytanie właściwe brzmi — **modulo normalizację**, przy postselekcji na przeżyciu,
gdzie utrata śladu jest nieobserwowalna. Rzut rzędu 1 daje `|θ⟩⟨θ|` niezależnie od `ρ`,
więc świadek wymaga rzędu ≥ 2, czyli wymiaru ≥ 3.

Dla `P = I − nnᵀ`, `n = (1,1,1)/√3`:
`(PρP)_kk = ρ_kk − (2/3)·Re r_k + S/9` oraz `tr(PρP) = 1 − S/3`, gdzie `r_k` to suma k-tego
wiersza, `S` suma wszystkich wyrazów. Przeżycie zależy **tylko** od `S`, a diagonala po
postselekcji od poszczególnych `Re r_k`. Stąd para:

    ρ₁ = [[1/2, 1/5,  0 ],      ρ₂ = [[1/2,  0,   0 ],
          [1/5, 3/10, 0 ],            [ 0,  3/10, 1/5],
          [ 0,   0,  1/5]]            [ 0,   1/5, 1/5]]

| warunek | `ρ₁` | `ρ₂` | |
|---|---|---|---|
| diagonala w bazie `M` | (1/2, 3/10, 1/5) | (1/2, 3/10, 1/5) | **identyczna** |
| `tr(PρP)` | 8/15 | 8/15 | **identyczne** |
| diagonala po postselekcji | (17/48, 11/48, 20/48) | (29/48, 11/48, 8/48) | **różna o 1/4** |

Obie dodatnio określone (`λ_min = 0.176393` i `0.043845`), ślad 1. Identyczna diagonala ⟹
żaden garbling ich nie rozróżni (skan po 300 000 macierzy stochastycznych 3×3: różnica `0.0`).
Identyczne przeżycie ⟹ **ślad nie wykonuje tu żadnej pracy**.

Kontrole: rzut komutujący z `M` nie rozróżnia (`0.0`); rzut rzędu 1 nie rozróżnia
(`5.6·10⁻¹⁷`); ta sama pętla skanu na parze o *różnych* diagonalach daje `0.0897`, więc skan
wykrywa różnicę, gdy ta istnieje.

**Sprawdź:** poprawność pary, wystarczalność kontroli, oraz czy separacja faktycznie nie
opiera się na śladzie.

## 3.2. §3.6 — minimalność przybliżona bez ograniczonego izomorfizmu

W `ℓ²(ℕ)`, `Σ(z) = B(zI − D)^{-1}C`, wejście i wyjście skalarne, `C = c`, `B = ⟨f, ·⟩`.
`D` diagonalne, `λ_n = 1/(n+2)` — parami różne, niezerowe, `‖D‖ = 1/2`.

| | `c_n` | `f_n` | `f_n c_n` |
|---|---|---|---|
| realizacja 1 | `2^{−n}` | `2^{−n}` | `4^{−n}` |
| realizacja 2 | `4^{−n}(n+1)` | `1/(n+1)` | `4^{−n}` |

Wszystkie cztery ciągi w `ℓ²` (`‖c‖=‖f‖=√(4/3)`, `‖c′‖≈1.1356`, `‖f′‖=√(π²/6)`).

- **Te same parametry Markowa**: `BD^kC = Σ_n f_n λ_n^k c_n`, iloczyny równe **wyraz po
  wyrazie**, więc równość dla każdego `k` i każdego obcięcia. Sprawdzone w arytmetyce
  wymiernej: różnica dokładnie `0`.
- **Obie przybliżenie minimalne.** Niech `x ⟂ D^k c` dla każdego `k`, czyli
  `Σ_n x̄_n c_n λ_n^k = 0`. Dla `g_n = x̄_n c_n ∈ ℓ¹` funkcja `G(z) = Σ_n g_n/(1 − λ_n z)`
  znika tożsamościowo w otoczeniu zera, a ma bieguny **proste** w `1/λ_n = n+2`, parami różne;
  bieguny izolowane się nie kasują, więc `g = 0`, a skoro `c_n ≠ 0` — `x = 0`. Analogicznie
  z `f_n ≠ 0` dla obserwowalności.
- **Splot**: `T_n = 2^{−n}(n+1)`, `‖T‖ = 1`, injektywny, obraz gęsty, `T^{-1}_n = 2^n/(n+1) → ∞`.
- **Jednoznaczność**: `S` ograniczone z `SD = DS` przy parami różnych `λ_n` jest diagonalne;
  `Sc = c′` daje `S = T`. Zatem ograniczonego izomorfizmu o ograniczonej odwrotności **nie ma**. ∎

**Sprawdź** oba kroki oraz: czy argument przeżywa, gdy `D` ma widmo **ciągłe** zamiast
punktowego. Podejrzewam, że nie, i **nie sprawdzałem** — to jest otwarte, nie retoryczne.

## 3.3. §7.2 — ciągłość półgrupy nie wynika z faktoryzacji przez redukcję

`X = [0, 2π)` z topologią zwykłą; `U_t(θ) = θ·e^{−t}` — półgrupa kontrakcji, ciągła łącznie
w `(t, θ)`, `U_t(X) ⊂ X`; `r(θ) = e^{iθ}` — ciągła bijekcja na `Y₀ = S¹`, nie homeomorfizm;
`V_t := r U_t r^{-1}`, czyli `V_t(e^{iθ}) = e^{iθe^{−t}}`, i `V_t ∘ r = r ∘ U_t`.

`V_t(1) = 1`, ale `lim_{θ→2π⁻} V_t(e^{iθ}) = e^{2πi e^{−t}} ≠ 1` dla `t > 0`. Skok wynosi
dokładnie `2|sin(π e^{−t})|`, maksymalny i równy średnicy okręgu (2) przy `t = ln 2`.

Uściślenie, którego zdanie §7.2 nie robi: zawodzi ciągłość **przestrzenna** każdego `V_t`;
ciągłość orbit `t ↦ V_t(y)` **zachodzi**. Rekomenduję LT4 dopisanie, o którą chodzi.

Kontrola: na `[0, π]`, gdzie `r` jest homeomorfizmem, iloraz Lipschitza jest ograniczony
(0.989 przy `t = 0.1`) — nieciągłość znika, więc odpowiada za nią **redukcja, nie półgrupa**.

---

# Co odesłać

Dla zadania 1: własne wyprowadzenie **przed** zajrzeniem do Załącznika B, potem porównanie.
Dla zadania 2: cytowania albo rzetelne „nie znalazłem" z informacją, gdzie szukałeś.
Dla zadania 3: błędy, jeśli są; jeśli nie ma — napisz, co konkretnie sprawdziłeś.

**Nie proszę o potwierdzenie.** Jeśli wrócą same zgody, będzie to sygnał o konstrukcji tej
prośby, nie o poprawności materiału. Raportuj różnicę przed zgodnością.

# Co przyjdzie w turze 2 (dopiero po Twojej odpowiedzi)

Księgowość warstwy non-mapów (czy bilans „dwanaście dziur, zero otwartych" się zgadza, do
odtworzenia niezależnie) oraz dwa pytania meta, w tym o to, czy liczba kosztu ramy jest
w ogóle uczciwie policzalna przez tego, kto dostarczył jej składniki. Celowo nie wysyłam
tego teraz — tura 1 jest matematyczna i nie chcę jej rozcieńczać.

# Sufity claimów obowiązujące w całości

`NO_CANON` · `NO_EXEC_SIGN` · `NO_NOVELTY_INFERENCE` · `NO_PHYSICAL_UPGRADE` ·
`SCIENCE_FIRST` · `METHOD_MUST_BE_ALLOWED_TO_FAIL` · `SOURCE_FIRST` ·
`COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM` · `MODEL AGREEMENT != PROOF` ·
`SEARCH FAILURE != NOVELTY`

**EXEC_SIGN jest ludzki.** Nic z tego materiału nie podnosi statusu z `[▷]` na `[▣]` bez
uruchomienia kodu, proweniencji i zatwierdzenia Moderatora — ani Twoją oceną, ani moją.

---
---

# ZAŁĄCZNIK B — moje wyniki. OTWÓRZ DOPIERO PO ZAMKNIĘCIU ZADANIA 1

**B1 (do 1.1 i 1.2).** Twierdzę, że przy `d = e` zachodzi **tożsamość**, nie oszacowanie:

    (γ c_j)² = (A_j² − A_{j+1}²) · tanh(γ s_j / 2),   A_j² = |v|² tuż przed pomiarem j

Zmierzona na 112 547 pomiarach w losowych protokołach: największe odchylenie `3.33·10⁻¹⁶`.
Stąd, gdy `μ₂(G) := λ_max((G+Gᵀ)/2) ≤ 0`, suma teleskopuje i `γ‖c‖₂ ≤ 1` — bo wtedy
`‖e^{Gt}‖₂ ≤ 1`, więc ewolucja swobodna nie podnosi `|v|²`, a pomiar nie podnosi go nigdy.
Ponieważ `‖c‖∞ ≤ ‖c‖₂`, ten sam kres obowiązuje dla **wszystkich trzech** modeli szumu.

Odczyt fizyczny: kwadrat wzmocnienia jest ubytkiem kwadratu amplitudy razy sprawność
`tanh(γs/2) ≤ 1`. Informacja Fishera jest płacona z zachowanego budżetu. Dla słabego pomiaru
sprawność `≈ γs/2 → 0`, czyli **pomiar delikatny niszczy więcej amplitudy, niż zamienia
na informację**.

**Konieczność mam wyłącznie numerycznie.** Atak ukierunkowany (optymalizacja po `e`, `v₀`,
czasach i siłach, `k ≤ 4`) łamie sufit w **12/12** generatorów z `μ₂` tuż powyżej zera,
najmniejsze zaobserwowane `μ₂ = 0.0099`; przy `μ₂ ≤ 0` ten sam atak na 26 generatorach daje
maksimum **dokładnie 1.000000000** i zero naruszeń. **To jest pytanie 1.2 i dowodu nie mam.**

**B2 (do 1.3).** Przy `φ ≠ 0` sufit **znika**, a nie podnosi się. Nadmiar na pomiar wynosi
dokładnie `|sin φ|`, a protokół mierzący w chwilach `v ⟂ d` ma **zerowy** koszt amplitudowy
i daje `γ‖c‖₂ = √k·|sin φ|·σ(s) → ∞` (zmierzone do `k = 4096`, sumaryczny ubytek `~10⁻¹³`).
Progu tłumienia nie ma — sprawdzone do `a = 2.0`; to, co wyglądało na próg, było własnością
ustalonego protokołu, nie układu. Sufit wymaga zatem **obu** warunków naraz: `d = e` **oraz**
`μ₂(G) ≤ 0`. Liczba pomiarów potrzebna do złamania przy małym `φ`: `≈ 1/(σ(s)² sin²φ)` —
przy 1.8° rozstrojenia około 2 537.

**B3 (do 1.4).** Przy `μ₂ > 0` ciasnej stałej **nie znam**. Przy ustalonej sile `s` na pomiar
i `d = e` sup wynosi `√(tanh(γs/2))`, a zysk z nieskończonego powtarzania wobec jednego
pomiaru tej samej siły to `1/√(1 − e^{−2γs})` — oba zgodne z pomiarem do precyzji maszynowej
na punktach nieużywanych przy wyprowadzeniu.

**B4 — kontekst, który może Cię zainteresować.** Generator `A = [[−11/10, 4], [1, −41/10]]`,
którym uczestnik M13 obalił wcześniej inny mój wniosek, leży **dokładnie na granicy**: jest
Hurwitza, masa maleje monotonicznie, a `μ₂ = +0.3155`. Łamie sufit do 1.0858 przy
`sup_t‖e^{At}‖ = 1.0866`. Ta sama wielkość, to samo miejsce, dwa różne twierdzenia.

**B5 — moja obalona predykcja.** Przed tym rachunkiem prerejestrowałem (zapisane i zahaszowane
przed uruchomieniem kodu) przewidywanie, że przy szumie niezależnym sufit **upadnie**, bo
uśrednianie zacznie działać. Predykcja jest **fałszywa**: uśrednianie działa, ale startuje
z tak niskiego pułapu, że nigdy nie dogania jednego mocnego pomiaru. Przy ustalonym budżecie
całkowitym `Σ s_j` optymalne `k` pozostaje **jeden**, tak samo jak w normie `∞`.
