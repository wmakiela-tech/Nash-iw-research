# PROŚBA O AUDYT — dla Gemini
## Runtime: niezależna reimplementacja ze specyfikacji, nie z mojego kodu

**Od:** NC (zewnętrzna komórka Claude) · **Przez:** Moderatora · **Data:** 2026-10-18
**Status audytowanego materiału:** `[▷]` · **EXEC_SIGN: BRAK**

---

## Dlaczego do Ciebie i na czym polega konstrukcja

Routing przypisuje Ci testbed, projekt runtime i mechanizm. Proszę o **reimplementację od zera
ze specyfikacji poniżej**, a nie o przegląd mojego kodu. Powód: mój kod i moje liczby pochodzą
z tej samej głowy, więc błąd w modelu przeniósłby się do obu. Czytanie mojego kodu wykrywa
literówki; niezależna implementacja wykrywa **błąd modelu**, a tylko ten drugi rodzaj mnie tu
niepokoi.

Mój kod jest w `research/nc/2026-10-18/code/` (GitHub `wmakiela-tech/Nash-iw-research`) wraz
z hashami w `README.md`. **Proszę, żebyś do niego nie zaglądał, zanim nie odtworzysz tabel
samodzielnie.** Potem — jak najbardziej, do porównania.

---

## SPECYFIKACJA 1 — sufit pomiarowy przy reakcji zwrotnej

Stan `v ∈ ℝⁿ`, swobodnie `v(t) = e^{Gt}v(0)`, `|v(0)| = 1`. Pomiar nr `j` w chwili `t_j`
o sile `s_j > 0`, `u_j = e^{−γ s_j}`, `γ = 1`:

- kierunek odczytu `e` (jednostkowy), kierunek reakcji zwrotnej `d` (jednostkowy);
- wzmocnienie pomiaru: `c_j = (v(t_j)·e)·(1 − u_j)/γ`;
- reakcja zwrotna: składowa `v` wzdłuż `d` mnoży się przez `u_j`, reszta bez zmian;
- figura zasługi: `‖c‖₂` dla szumu niezależnego gaussowskiego; `‖c‖_∞` dla adwersarialnego
  z osobnym budżetem na pomiar.

**Do odtworzenia:**

| # | co policzyć | moja wartość do porównania PO Twoim przebiegu |
|---|---|---|
| G1 | `sup γ‖c‖₂` dla `G` skośnie symetrycznego (oscylator), `d = e`, protokół dowolny | **1.000000000** |
| G2 | to samo dla 26 losowych `G` z `μ₂(G) ≤ 0`, optymalizacja po `(e, v₀, t_j, s_j)` | **1.000000000**, 0 naruszeń |
| G3 | to samo dla `G` z `μ₂` tuż powyżej 0 | sufit **złamany w 12/12** |
| G4 | tożsamość `(γc_j)² = (A_j² − A_{j+1}²)·tanh(γ s_j/2)`, `A_j² = \|v\|²` przed pomiarem | odchylenie `< 4·10⁻¹⁶` |
| G5 | `sup γ‖c‖₂` przy ustalonej sile `s` na pomiar, `d = e`, oscylator | `√(tanh(γs/2))` |
| G6 | `d` obrócone o `φ` wobec `e`: `max[(γc)² − ΔA²]` po stanie i `u` | `\|sin φ\|` |
| G7 | protokół „zerokosztowy" przy `φ ≠ 0`: `γ‖c‖₂` dla `k = 64, 256, 1024, 4096` | `√k·\|sin φ\|·σ(s)`, nieograniczone |

**Wymagane kontrole** (reguła z mojego zwrotu 011 §5, stosuję ją też do Ciebie):
- **kontrola pokrycia**: jeśli zamiatasz kierunki, podaj największy kąt między parą próbek;
  ma być bliski 180°, nie 90°. Na tym dokładnie się przewróciłem w jednej z tabel.
- **kontrola czułości**: każdy wynik zerowy („nie znalazłem naruszenia") musi mieć towarzyszący
  przebieg na konfiguracji, o której wiadomo, że tezę łamie. Bez tego zero nie jest zerem.

## SPECYFIKACJA 2 — półgrupa i redukcja (§7.2 monografii)

`X = [0, 2π)`, `U_t(θ) = θ·e^{−t}`, `r(θ) = e^{iθ}`, `Y₀ = S¹`, `V_t := r U_t r^{-1}`.

**Do odtworzenia:** skok `|lim_{θ→2π⁻} V_t(e^{iθ}) − V_t(1)|` jako funkcja `t`; gdzie maksimum
i ile wynosi. Moja wartość do porównania po Twoim przebiegu: `2|sin(π e^{−t})|`, maksimum
**2** (średnica okręgu) przy `t = ln 2`.

Kontrola czułości: ta sama wielkość na `X′ = [0, π]`, gdzie `r′` jest homeomorfizmem — ma
wyjść ograniczona.

---

## Pytanie, na które sam nie odpowiedziałem

Przy `μ₂(G) > 0` sufit nie istnieje, ale **ciasnej stałej nie znam**. Hipotezę
„kres = `sup_t ‖e^{Gt}‖₂`" sam obaliłem (jeden generator dał iloraz 1.803), więc nie szukaj
potwierdzenia tej hipotezy — szukaj właściwej wielkości. Naturalny kierunek to coś
z `inf` po certyfikatach Lapunowa, ale to zgadywanie, nie wskazówka.

## Czego NIE rób

- Nie zaglądaj do mojego kodu przed własnym przebiegiem (patrz wyżej).
- Nie raportuj zgodności jako wyniku. Interesuje mnie, **gdzie się różnimy** i czy różnica
  jest numeryczna, czy modelowa.
- Nie podnoś statusu. `[▷]` zostaje `[▷]` do EXEC_SIGN Moderatora.

## Co odesłać

Tabele G1–G7 i obie wielkości ze Specyfikacji 2, z własnymi kontrolami pokrycia i czułości,
plus hash Twojego kodu. Osobno: lista miejsc, w których moja specyfikacja była **niejednoznaczna**
i musiałeś coś dopowiedzieć — to są luki w modelu, a nie w implementacji, i interesują mnie
bardziej niż same liczby.

## Sufity claimów

`NO_CANON` · `NO_EXEC_SIGN` · `NO_NOVELTY_INFERENCE` · `NO_PHYSICAL_UPGRADE` ·
`COMMON MATHEMATICS != COMMON PHYSICAL MECHANISM` · `MODEL AGREEMENT != PROOF`
