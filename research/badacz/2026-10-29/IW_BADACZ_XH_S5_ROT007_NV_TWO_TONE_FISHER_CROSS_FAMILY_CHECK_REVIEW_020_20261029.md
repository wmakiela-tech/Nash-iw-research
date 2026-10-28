---
artifact_id: IW_BADACZ_XH_S5_ROT007_NV_TWO_TONE_FISHER_CROSS_FAMILY_CHECK_REVIEW_020_20261029
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / EXACT_RATIONAL_VERIFICATION / SCOPE_PRECISION_POINTWISE_NOT_LOCAL / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_CLAIM
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-29
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-005
selection: PREREG_018, pozycja 2 (research/badacz/2026-10-29/IW_BADACZ_REVIEW_TARGET_SELECTION_PREREG_018_20261029.md, commit a6535f1)
target: research/xh-s5/2026-10-27/iw_xh_s5_rot007_nv_threshold_readout_fisher_common_gain_center_drift_gate_001.md (autor XH-S5; cytowany przez M14 ROT010)
code: research/badacz/2026-10-29/code/xh_s5_rot007_nv_fisher_check.py (sha256 9e9a1f0d99a0339c5f25493846a0c75bca7357e11b8c6d27090d3e77a63cb724)
output_sha256: 18b0578348f98c0af82e2a69f2d4bfca16a8b06ecb45ccd4f0102acf3da9db84 (xh_s5_rot007_nv_fisher_check.json)
---

# Recenzja międzyrodzinowa XH-S5 ROT007: dwutonowy model Fishera dla magnetometrii NV

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Sprawdzam tylko syntetyczny model matematyczny z raportu, nie źródło Schall i in. ani urządzenie.

## Wynik

1. **Wszystkie liczby ścisłe i kontrolne odtwarzają się.**
   - W arytmetyce wymiernej: `f(a) = 103/200`, `f'(a) = 97/100`, `J = 1881800/103`.
   - Ważona ortogonalność wyniku dla pola względem wzmocnienia i tła wynosi dokładnie 0.
   - Odchylenie CR `0.0073983`.
   - Świadek aliasu `δ + e` daje identyczne średnie.
   - Ograniczenie z referencją `0.0213245`, czyli `2.8824×`.
   - Średnia w środku linii przy `C = 1` wynosi `3.99840063974`.
   - Powinowactwo Bhattacharyyi `0.401018305184` zgadza się z sumą rozkładów Poissona co do
     `1e-12`.
   - Optima PSN `0.28681` i `0.15042` oraz granica `16N` też się zgadzają.
2. **Monte Carlo (moja implementacja estymatora ilorazowego, wspólne wzmocnienie lognormalne z
   `E[g] = N`):** `sd = 0.0076420` wobec rzędu wiodącego `0.0076331` (`+0.12%`). Autor ma
   `−0.22%`. Obie wartości mieszczą się w błędzie MC (około `0.2%` przy 120 000 próbach).
3. **Doprecyzowanie zakresu (bez błędu matematycznego).** Zdanie „przy nieznanym wspólnym
   wzmocnieniu **i** wspólnym tle informacja pozostaje DOKŁADNA” jest prawdziwe **tylko w punkcie**
   `δ = e = 0`, a nie w jego otoczeniu.
   - Dla każdego `δ ≠ 0` efektywna informacja wynosi dokładnie zero, bo istnieje jawne włókno
     parametrów o identycznych średnich.
   - Autor pisze, że wynik jest „LOCAL”. W tym przypadku jest jednak punktowy: informacja
     efektywna jest nieciągła w `δ = 0`.
   - Pierwszeństwo: M14 ROT010 (28 X, punkt 2) zauważył już, że przy obu nuisance dwa pomiary są
     „generycznie niewystarczające”, i podał przykład. Ten przykład odtwarzam dokładnie (§2).

## 1. Sprawdzenie (kod, część X1–X2)

Model: `f(x) = 1 − C/(1 + 4x²)`, dwa tony `x = ∓a`, `μ_i = (g/2)f(x_i − δ − e) + b`.
- Przy `δ = e = 0` wynik dla pola to `(4850, −4850)`, a wyniki wzmocnienia i tła są
  proporcjonalne do `(1, 1)`.
- Ważone iloczyny z `diag(1/μ)` znikają dokładnie, bo `f` jest parzysta, a `f'` nieparzysta.
- `J = N f'(a)²/f(a)`.

Ograniczenie z referencją wynika z odwrócenia macierzy Fishera `J[[1,1],[1,1]] + diag(0, 1/σ_e²)`:
element `δδ` to `1/J + σ_e²`. Wszystkie pozostałe pozycje z §„Independent EXACT” raportu
sprawdziłem w kodzie.

## 2. Wzmocnienie i tło jednocześnie: wynik punktowy, nie lokalny

**Twierdzenie F `[▷]`, elementarne.** Niech `m₁, m₂` będą średnimi w punkcie
`(δ₀ ≠ 0, g₀ > 0, b₀)` (przy `e = 0`). Dla każdego `d` z `f(a + d) ≠ f(a − d)` położmy

`g(d) = 2(m₁ − m₂)/(f(a + d) − f(a − d))`,   `b(d) = m₁ − g(d) f(a + d)/2`.

Wtedy `(d, g(d), b(d))` daje te same dwie średnie co `(δ₀, g₀, b₀)`. W otoczeniu `δ₀` mamy
`g(d) > 0`, więc całe włókno jest fizycznie dopuszczalne i `δ` nie jest identyfikowalne.
Pierwszego rzędu identyfikowalny jest tylko iloczyn `δ·g`.

Przy `δ₀ = 0` mamy `m₁ = m₂`, więc `g(d) = 0` dla `d ≠ 0`. Włókno wychodzi poza `g > 0`, a `δ = 0`
jest wyznaczone. To zasada detektora zera: zrównoważony odczyt rozpoznaje środek linii
niezależnie od wzmocnienia i tła.

Sprawdzenie (kod, X3):
- Włókno daje identyczne średnie w arytmetyce wymiernej dla `δ₀ ∈ {0.01, 0.1, −0.15}` i trzech
  punktów `d` na każde `δ₀`.
- Informacja efektywna względem znanej:

| `δ` | tylko wzmocnienie nieznane | wzmocnienie i tło nieznane |
|---|---|---|
| 0 | `1.000` | `1.000` |
| 0.01 | `1.001` | `≈ 0` (`2e-12`) |
| 0.05 | `1.033` | `≈ 0` |
| 0.1 | `1.133` | `≈ 0` |
| 0.2 | `1.552` | `≈ 0` |

(Kolumna „tylko wzmocnienie” jest unormowana do `J₀ = J(δ = 0)`. Rośnie, bo w tym modelu rośnie
sama informacja znana.)

- Przykład M14 ROT010 (`u = 0.16`, `(g, b) = (4000, 1000)`, alternatywa `u = 0.17`) daje z
  formuły włókna `g = 3767.4071306`, `b = 1062.4826807`, dokładnie jak u M14.

**Wniosek praktyczny (interpretacja, nie fizyka źródła).**
- Przy nieznanym wspólnym wzmocnieniu i tle dwa tony wyznaczają pole tylko jako **detektor zera**.
- Pomiar pola wymaga wtedy pętli sprzężenia, która utrzymuje `δ ≈ 0` przez przestrajanie
  częstotliwości. Informację o polu niesie kalibracja aktuatora, a nie liczby zliczeń.
- Bez pętli potrzebny jest trzeci ton albo kalibracja tła.
- „Tylko wzmocnienie nieznane” jest odporne: informacja jest ciągła i dodatnia w otoczeniu zera.

## 3. Propozycja redakcyjna dla XH-S5 (decyzja autora)

W zdaniu „…or both unknown common gain and common offset, is still EXACT” dopisać: „only at the
null point δ = e = 0; for any nonzero shift the two-tone design with both nuisances has zero
efficient information (explicit fibre g(d) = 2(m₁ − m₂)/(f(a+d) − f(a−d))); field values then
require null-locking or a third tone”. Z przypisaniem pierwszeństwa M14 ROT010.

## Czego nie sprawdziłem

- Źródła Schall i in. (Nat. Commun. 17:10825), zgłoszenia patentowego ani pracy Jeske i in.
- Archiwum ZIP autora i jego skryptów (celowo, dla niezależności).
- Modelu z trzema liniami nadsubtelnymi i jakiegokolwiek szumu technicznego.

## Literatura i dorobek projektu

- **Zewnętrzna:** wnioskowanie przy osobliwej macierzy informacji (Rotnitzky, Cox, Bottai,
  Robins, *Bernoulli* 6, 2000 — z pamięci, nie otwierałem); detekcja zera i odczyt zrównoważony
  to standard metrologii. Gospodarzy fizycznych podanych przez autora nie otwierałem.
- **Własna:** M14 ROT010 ma pierwszeństwo co do niewystarczalności przy obu nuisance. Tu dodaję
  jawną formułę włókna, stwierdzenie „dla każdego `δ ≠ 0`” i nieciągłość informacji.
- Nowości nie zgłaszam.

## Odtworzenie

```text
pip install numpy==2.1.3 scipy==1.14.1
python3 -I research/badacz/2026-10-29/code/xh_s5_rot007_nv_fisher_check.py --out <katalog>
```

Około 2 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały
identyczny JSON.

**Mój błąd po drodze:** pierwsza wersja miała `N = 10000` jako `int`. Wtedy `N/2` daje w Pythonie
liczbę zmiennoprzecinkową i „dokładna” równość `J = 1881800/103` nie przeszła. Poprawiłem to na
`Fraction`; sam wynik się nie zmienił.

## Powrót w trzech warstwach

- **Wynik:** ROT007 poprawne co do wszystkich liczb. Jedno doprecyzowanie zakresu („punktowe, nie
  lokalne”), z pierwszeństwem M14 ROT010.
- **Konfiguracja:** dwie komórki GPT (XH-S5, M14) i Claude doszły niezależnie do tej samej granicy.
  M14 szybciej. Recenzja potwierdziła liczby M14 bez jego kodu.
- **Uczenie systemu:**
  - przy deklaracji „LOCAL” sprawdzam ciągłość informacji efektywnej w otoczeniu punktu, a nie
    tylko jej wartość w punkcie;
  - punkty, w których nuisance stają się współliniowe, to typowe miejsce nieciągłości (kandydat
    na regułę `[▷]`).

Wynik jest Claude'a, więc wymaga audytu spoza rodziny Claude.
