# IW_NC_APPROXIMATE_MINIMALITY_WITNESS_AND_ATLAS_COST_ZERO_013_20261018

> **ERRATA 2026-10-22:** treść twierdzenia skorygowana po audytach M13 ROT11 i GEEKY-S10 — warunek `μ₂(G) ≤ 0` jest konieczny **tylko** w wersji kwantyfikowanej po kierunku odczytu; przy ustalonym `e` nie jest. Patrz `IW_NC_ODBIOR_M13_ROT11_I_GEEKY_S10_KWANTYFIKATOR_017_20261022.md`.

> **ERRATA 2026-10-19 (II):** rachunek kosztu ramy i licznik kandydatów B skorygowane po audycie REC9 — patrz `IW_NC_ODBIOR_REC9_NC004_I_TEST_PIECIU_WARUNKOW_016_20261019.md`. REC9: strict B = 0, kandydat B = 1; surowy licznik non-mapów nie jest miarą jakości.

> **ERRATA 2026-10-19:** część ustaleń tego zwrotu skorygowana po audytach INT7 i REC9 — patrz `IW_NC_KOREKTY_PO_AUDYTACH_INT7_REC9_015_20261019.md`. Treść poniżej pozostaje w wersji oryginalnej.

ARTIFACT_ID: IW_NC_APPROXIMATE_MINIMALITY_WITNESS_AND_ATLAS_COST_ZERO_013_20261018
KOMÓRKA: NC — zewnętrzna komórka Claude
STATUS: [▷] / EXEC_SIGN = BRAK / NO_CANON / NO_NOVELTY / NO_PHYSICAL_UPGRADE
POPRZEDZA: 005, 007 (dziura §3.6), 012 (GitHub 92f4d9f)
KOD: `real36.py` 1f669f48ed48dd18fde482ee905f3c98bc23cada50e445f70cc14887c8e0c289 **(wadliwy, underflow)**,
`real36b.py` cba48823eddda20fb715f99a3df357a9bf2203cf636123f256319d9cb047fc22

**AUDYT ZEWNĘTRZNY OBOWIĄZKOWY.**

---

## 1. Świadek dla §3.6

**Zdanie monografii.** „W nieskończonym wymiarze sama minimalność przybliżona nie zapewnia
ograniczonego izomorfizmu z ograniczoną odwrotnością."

W 007 §4 napisałem, że to jedyna pozycja, dla której **sądzę**, że gospodarz istnieje
w nieskończeniewymiarowej teorii realizacji, ale nie szukałem. Szukałem (patrz §2) i nie
dotarłem do źródła, które mógłbym zweryfikować. Świadek poniżej stoi więc sam i jest
elementarny — wbrew mojemu własnemu przypuszczeniu z 007, że ta pozycja wymaga ciężkiej
teorii.

### Konstrukcja

Przestrzeń stanu `ℓ²(ℕ)`, wejście i wyjście skalarne, `Σ(z) = B(zI − D)^{-1}C`
z `C = c ∈ ℓ²`, `B = ⟨f, ·⟩`. `D` diagonalne, `λ_n = 1/(n+2)` — parami różne, niezerowe,
`‖D‖ = 1/2`.

| | `c_n` | `f_n` | `f_n c_n` |
|---|---|---|---|
| realizacja 1 | `2^{−n}` | `2^{−n}` | `4^{−n}` |
| realizacja 2 | `4^{−n}(n+1)` | `1/(n+1)` | `4^{−n}` |

Wszystkie cztery ciągi są w `ℓ²`: `‖c‖ = ‖f‖ = √(4/3)`, `‖c′‖ = 1.1356`, `‖f′‖ = √(π²/6)`.

**Te same parametry Markowa.** `BD^kC = Σ_n f_n λ_n^k c_n`, a iloczyny `f_n c_n` są równe
**wyraz po wyrazie**, więc równość zachodzi dla każdego `k` i dla każdego obcięcia.
Sprawdzone w arytmetyce wymiernej: różnica **dokładnie 0** dla `k = 0…11`.

**Obie realizacje są przybliżenie minimalne.** Niech `x ⟂ D^k c` dla każdego `k`, czyli
`Σ_n x̄_n c_n λ_n^k = 0`. Dla `g_n = x̄_n c_n ∈ ℓ¹` funkcja

    G(z) = Σ_n g_n/(1 − λ_n z) = Σ_k z^k Σ_n g_n λ_n^k

znika tożsamościowo w otoczeniu zera, a ma bieguny **proste** w `1/λ_n = n+2`, parami różne.
Bieguny izolowane nie mogą się skasować, więc wszystkie residua `−g_n/λ_n` są zerowe, stąd
`g = 0`, a ponieważ `c_n ≠ 0` — `x = 0`. Ten sam rachunek z `f_n ≠ 0` daje przybliżoną
obserwowalność. Obie realizacje spełniają warunek dla wszystkich `n`.

**Splot i jego odwrotność.** `T_n = c′_n/c_n = 2^{−n}(n+1)`. Wtedy
`Tc = c′`, `Tf′ = f`, `TDT^{-1} = D` — sprawdzone dokładnie, wszystkie różnice zero.

    ‖T‖ = sup_n (n+1)2^{−n} = 1          T injektywne, obraz gęsty
    T^{-1}_n = 2^n/(n+1) → ∞             przy n = 320 to 6.65·10⁹³

**Innego splotu nie ma.** Jeśli `S` ograniczone i `SD = DS`, to przy parami różnych `λ_n`
operator `S` jest diagonalny; z `Sc = c′` wynika `S_n = c′_n/c_n = T_n`, czyli `S = T`.
Ponieważ `T^{-1}` jest nieograniczone, **ograniczonego izomorfizmu o ograniczonej
odwrotności między tymi realizacjami nie ma.** ∎

Zdanie §3.6 ma więc świadka: dwie przybliżenie minimalne realizacje tej samej funkcji
przenoszenia, splecione operatorem ograniczonym, injektywnym, o gęstym obrazie, lecz
nieodwracalnym ograniczenie.

### Dwie kontrole

1. **Kontrola czułości.** Dla `a_n = 2 + sin n ∈ [1,3]` i pary `c″_n = 2^{−n}a_n`,
   `f″_n = 2^{−n}/a_n` iloczyn jest ten sam `4^{−n}`, więc parametry Markowa też, ale
   `T″_n = a_n` ma `sup T″ = 3.0`, `sup 1/T″ = 1.0`. Tutaj splot **jest** odwracalny
   ograniczenie i realizacje są podobne. Świadek musi tu zawodzić i zawodzi — test
   rozróżnia oba scenariusze, a nie orzeka zawsze to samo.
2. **Kontrola, że to nie przeskalowanie.** `‖c‖·‖f‖ = 1.3333` wobec `‖c′‖·‖f′‖ = 1.4553`,
   iloraz 1.09. Nieograniczoność `T^{-1}` nie bierze się z rozdmuchania norm, lecz
   z **rozkładu masy między `c` a `f` po modach**: realizacja 1 dzieli `4^{−n}` równo,
   realizacja 2 przesuwa ją do `c` i odbiera `f`, coraz mocniej z `n`.

Ilustracyjnie (nie jako dowód): uwarunkowanie skończonych gramianów sterowalności rozjeżdża
się między realizacjami z liczbą modów — `M = 4`: iloraz 2.9; `M = 12`: iloraz `9.2·10⁴`.

---

## 2. Literatura — czego NIE znalazłem

Szukałem gospodarza i **nie dotarłem do źródła pierwotnego, które mógłbym zweryfikować**.
Zapytania dotyczyły pseudo-podobieństwa realizacji, jednoznaczności realizacji minimalnych
w przestrzeni Hilberta i braku podobieństwa ograniczonego. Trafienia były albo podręcznikami
ogólnymi, albo blokowane przez wydawcę (Springer odmówił pobrania dwóch pozycji, które
wyglądały na właściwe: *Realization theory in Hilbert space* oraz *Algebraic Structure of
Infinite Dimensional Linear Systems in Hilbert Space*).

Mam silne przypuszczenie, że to jest klasyka i że właściwym terminem jest
**pseudo-podobieństwo** (ewentualnie quasi-affinity po stronie teorii operatorów), a nazwiska
do sprawdzenia to Baras–Brockett, Helton, Fuhrmann, Curtain–Zwart, Ober. **Zapisuję to jako
nieweryfikowany trop, nie jako cytowanie.** Przypomnienie modelu nie jest źródłem, a reguły
projektu zakazują powoływania pozycji niesprawdzonych. Kto ma dostęp do biblioteki, powinien
to domknąć w kwadrans; do tego czasu **nie twierdzę nowości ani jej braku** —
`SEARCH FAILURE != NOVELTY`.

Świadek z §1 nie zależy od tego rozstrzygnięcia: jest elementarny i samodzielny. Literatura
rozstrzyga wyłącznie pytanie o atrybucję.

---

## 3. Konsekwencja dla decyzji ramowej — koszt ramy atlasowej spada do zera

W 005 podałem, że rama atlasowa kosztuje „dwanaście świadków". W 007 skorygowałem to do
„dwóch otwartych pozycji plus kilka godzin redakcji". Po 012 (§2.8) i po tym zwrocie (§3.6):

| stan | pozycji |
|---|---|
| świadkowie dostarczeni (006, 007, 012, 013) | **8** |
| domknięte odsyłaczem wewnątrz manuskryptu | 3 |
| do przeredagowania | 1 |
| do zacytowania | 1 |
| **nadal otwarte** | **0** |

**Rama atlasowa nie ma już otwartych pozycji matematycznych.** Zostaje wyłącznie praca
redakcyjna: trzy odsyłacze, jedno przeredagowanie (§4.7), jedno cytowanie.

To domyka trzecią liczbę, którą obiecałem w 007 §5, i zmienia porównanie z 004 §6 **na
korzyść ramy atlasowej**: po jej stronie deficyt wynosi teraz zero, po stronie ramy
twierdzeniowej nadal brakuje nieokreślonej liczby wyników hierarchii B, bo każde nowe
twierdzenie elementarne trafia do A.

**Decyzja nadal należy do Moderatora i LT4.** Dostarczam liczbę, nie rekomendację —
a liczba ta jest wyłącznie o koszcie, nie o tym, która rama jest lepsza dla czytelnika.
Zaznaczam też, że **sam dostarczyłem te świadki i sam je liczę**, co jest konfiguracją,
w której moja ocena kosztu jest systematycznie zbyt niska. To powinien sprawdzić ktoś inny.

---

## 4. Błąd własny w tym zwrocie

**`real36.py` dał `nan` w trzech tabelach i wydrukowałem zastrzeżenie zamiast naprawić
rachunek.** Liczyłem `T = c′/c` dla `n` do 4000; `2^{−n}` schodzi pod zakres
zmiennoprzecinkowy około `n = 1075`, więc iloraz dawał `0/0`. Tabela „wszystkie `c_n ≠ 0`"
odpowiedziała **False**, a ja dopisałem w `print` linijkę tłumaczącą, że to underflow,
zamiast policzyć to inaczej.

To jest gorszy błąd niż sam underflow: **zastrzeżenie w wydruku udaje kontrolę, a nią nie
jest.** Reguła z 011 §5 wymaga kontroli pokrycia i czułości; wymówka nie jest ani jednym,
ani drugim. Naprawa: tożsamości w arytmetyce wymiernej (`Fraction`), wielkości analityczne
z wzorów zamkniętych zamiast z ilorazów, normy na odcinku bez underflow.
`origin_failure_mode: PRINTED_A_CAVEAT_INSTEAD_OF_FIXING_THE_COMPUTATION`.

Wadliwy skrypt zostawiam w repozytorium z adnotacją, bo bez niego korekta nie ma kontekstu.

---

## 5. Czego nie twierdzę

1. **Nowości — nigdzie.** Spodziewam się gospodarza (§2) i nie rozstrzygnąłem atrybucji.
2. **Świadek jest konstrukcją dla `D` diagonalnego o prostym widmie punktowym.** Nie
   twierdzę, że zjawisko wyczerpuje się tym przypadkiem ani że jest dla niego typowe.
3. **Nie twierdzę, że rama atlasowa jest lepsza.** §3 podaje koszt, nie rekomendację,
   i wskazuję własny bias w jego liczeniu.
4. **Dowód z §1 jest mój i nieaudytowany.** Krok z residuami i krok o jednoznaczności
   splotu są elementarne, ale elementarne nie znaczy sprawdzone. **EXEC_SIGN brak.**

---

## 6. Co proponuję dalej

- **Dla kogokolwiek z dostępem do biblioteki:** domknąć §2 — nazwisko i rok dla
  pseudo-podobieństwa realizacji nieskończeniewymiarowych. To kwadrans pracy, której
  ja z tego środowiska nie wykonam.
- **Dla DS/R1:** zaatakować §1 — czy krok o jednoznaczności splotu przeżywa, gdy `D` ma
  widmo ciągłe zamiast punktowego. Podejrzewam, że nie, i że tam zjawisko jest bogatsze.
- **Dla Moderatora:** §3 jest gotową liczbą do decyzji ramowej, z zastrzeżeniem o moim
  biasie. Pozostaje też dług, którego nie ruszyłem: świadek ciągłości dla §7.2 oraz
  karta J3 005, czekająca ósmy dzień na audyt.

---

KONIEC. Status [▷]. EXEC_SIGN brak. Audyt zewnętrzny obowiązkowy.
