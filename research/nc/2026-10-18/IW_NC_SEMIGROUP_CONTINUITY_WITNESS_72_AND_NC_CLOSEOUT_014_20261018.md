# IW_NC_SEMIGROUP_CONTINUITY_WITNESS_72_AND_NC_CLOSEOUT_014_20261018

> **ERRATA 2026-10-19 (II):** rachunek kosztu ramy i licznik kandydatów B skorygowane po audycie REC9 — patrz `IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019.md`. REC9: strict B = 0, kandydat B = 1; surowy licznik non-mapów nie jest miarą jakości.

> **ERRATA 2026-10-19:** część ustaleń tego zwrotu skorygowana po audytach INT7 i REC9 — patrz `IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019.md`. Treść poniżej pozostaje w wersji oryginalnej.

ARTIFACT_ID: IW_NC_SEMIGROUP_CONTINUITY_WITNESS_72_AND_NC_CLOSEOUT_014_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
POPRZEDZA: 005, 007 (§7.2), 012, 013 (GitHub f88b71b)
KOD: `sg72.py` 6b91d3c75116880ea3aa2fb75aa6cc3d23ce1d634e48c872e36e0f7e1e14be8c

**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY.**

---

## 1. Świadek dla §7.2, człon „ciągłość"

W 007 §2 zgłosiłem ten świadek jako **konstruowalny, ale nieskonstruowany**, pisząc, że
przykład `[0,2π) → S¹` z §2.3 „dotyczy `τ̄`, nie `V_t`, więc nie przenosi się wprost".

**Blokada była pozorna.** Szukałem półgrupy **obrotu** na `[0,2π)`, która faktycznie nie jest
ciągła, bo się zawija. Nic jednak nie wymaga obrotu — wystarczy kontrakcja.

### Konstrukcja

    X   = [0, 2π) z topologią zwykłą
    U_t(θ) = θ·e^{−t}                     półgrupa kontrakcji, ciągła ŁĄCZNIE w (t, θ)
    r(θ)   = e^{iθ},   Y₀ = r(X) = S¹      ciągła BIJEKCJA, nie homeomorfizm
    V_t := r U_t r^{-1},  czyli V_t(e^{iθ}) = e^{iθe^{−t}}

Sprawdzone: `U_s U_t = U_{s+t}` (błąd `8.9·10⁻¹⁶`), `U_0 = id`, `U_t([0,2π)) ⊂ [0,2π)`,
`U_t` lipschitzowska łącznie (0 naruszeń na 20 000). `V_t ∘ r = r ∘ U_t` z definicji.

**Nieciągłość.** `V_t(1) = 1`, natomiast `lim_{θ→2π⁻} V_t(e^{iθ}) = e^{2πi e^{−t}} ≠ 1`
dla każdego `t > 0`. Skok na `S¹` wynosi dokładnie

    |e^{2πi e^{−t}} − 1| = 2·|sin(π e^{−t})|

Zmierzone wobec wzoru dla siedmiu wartości `t`: zgodność na wszystkich wyświetlonych cyfrach.
Maksimum skoku to **2 — średnica okręgu, punkty antypodyczne — osiągane przy `t = ln 2`**
(bo `e^{−ln2} = 1/2`, więc `e^{2πi/2} = −1`). Zmierzone maksimum `1.999999999967`
przy `t = 0.6931508` wobec `ln 2 = 0.6931472`.

### Uściślenie, którego zdanie monografii nie robi

Rozdzieliłem dwie ciągłości, bo zdanie §7.2 ich nie rozróżnia, a zachowują się odwrotnie:

- **ciągłość przestrzenna każdego `V_t`** jako odwzorowania `Y₀ → Y₀`: **zawodzi** dla każdego `t > 0`;
- **ciągłość orbit** `t ↦ V_t(y)` przy ustalonym `y`: **zachodzi** (moduł ciągłości zmierzony
  na siatce, maks. przyrost `9.4·10⁻⁴` przy kroku `1.5·10⁻⁴`).

Rekomendacja dla LT4: dopisać w §7.2, o którą ciągłość chodzi. Bez tego zdanie jest prawdziwe,
ale niesprawdzalne, bo czytelnik nie wie, czego ma szukać.

### Dwie kontrole

1. **Kontrola czułości.** Na `X′ = [0, π]`, gdzie `r′` jest homeomorfizmem na obraz,
   iloraz `|V_t(e^{ia}) − V_t(e^{ib})| / |e^{ia} − e^{ib}|` jest **ograniczony**
   (0.989 przy `t = 0.1`, 0.211 przy `t = 2`) — `V_t` jest wtedy lipschitzowska, więc ciągła.
   Świadek musi tam zawodzić i zawodzi: **odpowiada za niego redukcja, nie półgrupa.**
2. **Kontrola dopełniająca.** Ta sama wielkość na `[0,2π)` jest nieograniczona:
   68.4 / 74.8 / 200.9 dla `t = 0.1 / ln2 / 1.0`, i rośnie z zagęszczeniem próbek przy
   punkcie sklejenia.

---

## 2. Bilans komórki NC — stan na zamknięcie dnia

Warstwa non-mapów z 005 (dwanaście dziur) jest **domknięta w całości**. Poniżej rozliczenie
pozycja po pozycji, bo zbiorcza tabela, którą napisałem najpierw, sumowała się do **14** —
myliłem dziury ze świadkami (§2.9 i §3.5 dzielą jednego) i liczyłem §7.2 trzy razy, raz za
każdą z jej trzech podtez. Właściwe rozliczenie:

| # | sekcja | rozstrzygnięcie | gdzie |
|---|---|---|---|
| 1 | §5.2 | cytowanie literatury (Pechukas, Shaji–Sudarshan) | 005/006 |
| 2 | §3.6 | **świadek** | 013 |
| 3 | §3.10 | **świadek** | 006 |
| 4 | §7.8 | **świadek** | 006 |
| 5 | §1.7 | **świadek** | 006 |
| 6 | §1.10 | **świadek** (nieoznaczoność Stieltjesa) | 006 |
| 7 | §2.8 | **świadek** | 012 |
| 8 | §2.9 | **świadek** (wspólny z 9) | 007 |
| 9 | §3.5 | **świadek** (wspólny z 8) | 007 |
| 10 | §4.7 | przeredagowanie (uwaga o typowaniu) | 007 |
| 11 | §5.10 | odsyłacz do Tw. 5.3 | 007 |
| 12 | §7.2 | **świadek** (ciągłość) + odsyłacz (równoważność) + przeredagowanie (CP) | 014 + 007 |

**Dziewięć z dwunastu dziur ma skonstruowanego świadka** — przy ośmiu odrębnych świadkach,
bo pozycje 8 i 9 dzielą jednego. Jedno cytowanie, jeden odsyłacz, jedno przeredagowanie.
Pozycja 12 jako jedyna wymaga wszystkich trzech rodzajów pracy naraz. **Otwartych: zero.**

Koszt ramy atlasowej: **zero otwartych pozycji matematycznych**, sama redakcja. To trzecia
i ostatnia liczba obiecana w 007 §5. Liczę ją sam, dostarczywszy sam te świadki — zastrzeżenie
o biasie z 013 §3 obowiązuje tu tak samo i jest jednym z zadań audytowych.

Równolegle wątek problemu otwartego §7.5b.5 (008–011) dał: minimaks w postaci zamkniętej,
tożsamość księgową `(γc)² = ΔA²·tanh(γs/2)`, kryterium `μ₂(G) ≤ 0` i domkniętą tabelę 2×2.

**Wszystko to jest `[▷]` i nic z tego nie przeszło audytu zewnętrznego.** Dlatego ten zwrot
zamyka produkcję NC, a następnym krokiem są pakiety audytowe — nie kolejny wynik.

---

## 3. Błąd własny

**Zgłosiłem przeszkodę, której nie było.** W 007 napisałem, że przykład z §2.3 „nie przenosi
się wprost" — i to zdanie było prawdziwe tylko dla półgrupy obrotu, której nikt nie wymagał.
Zawęziłem przestrzeń poszukiwań do jednej rodziny, a potem zaraportowałem wynik tego
zawężenia jako własność problemu. Świadek jest dwulinijkowy.

`origin_failure_mode: REPORTED_A_SELF_IMPOSED_SEARCH_RESTRICTION_AS_A_PROPERTY_OF_THE_PROBLEM`.

**Drugi błąd, złapany przy pisaniu §2.** Pierwsza wersja tabeli bilansowej sumowała się do 14
przy dwunastu dziurach: policzyłem świadków zamiast dziur i rozbiłem §7.2 na trzy pozycje,
choć to jedna dziura o trzech podtezach. Liczba „zero otwartych" była poprawna, ale rozkład
na kategorie nie. Złapane przez sprawdzenie sumy wobec listy z 005, a nie przez przegląd
tabeli — czyli znów przez bibliotekę, nie przez intuicję.
`origin_failure_mode: COUNTED_DISPOSITIONS_INSTEAD_OF_ITEMS_IN_A_BALANCE_TABLE`.

Ta sama rodzina co błąd z 013 §4 (kontrola czułości zamiast wymówki) i jak cztery wcześniejsze:
**zakres, który wygląda na wymuszony przez problem, a jest wyborem.** Reguła z 011 §5 wymaga
kontroli pokrycia — tu brakowało jej nie w skanie numerycznym, lecz w przestrzeni konstrukcji.
Proponuję rozszerzyć regułę: *zgłaszając coś jako niekonstruowalne lub trudne, podaj rodzinę,
w której szukałeś, i uzasadnij, dlaczego akurat ta.*

---

## 4. Czego nie twierdzę

1. **Nowości — nigdzie.** Ciągła bijekcja bez ciągłej odwrotności i sprzężenie półgrupy przez
   nią to materiał podręcznikowy. `SEARCH FAILURE != NOVELTY`.
2. **Świadek dotyczy jednej konkretnej redukcji.** Nie twierdzę, że redukcja z §7.2 monografii
   jest tego typu — twierdzę tylko, że z ciągłości `U_t` i z samej faktoryzacji przez redukcję
   ciągłość `V_t` **nie wynika**, bo oto kontrprzykład. To jest dokładnie treść non-mapa.
3. **Nie orzekam o dwóch pozostałych członach §7.2** poza tym, co ustaliłem w 007: całkowita
   dodatniość to uwaga o typowaniu, równoważność procesów to odsyłacz do Tw. 5.3.
4. **EXEC_SIGN brak**, audyt zewnętrzny obowiązkowy, całość moja.

---

KONIEC. Status [▷]. EXEC_SIGN brak.
