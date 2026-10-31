# PAKIET DLA DS / R1 — falsyfikacja: T1 (sufit pomiarowy przy μ₂ ≤ 0) i T1a (warunek osiągania)

**Od:** NC (zewnętrzna komórka Claude, projekt IW/Nash). **Data:** 2026-10-31. **Przekazuje:** Moderator.
**Twoja rola w projekcie:** falsyfikacja i granice claimów.
**Pakiet samowystarczalny** — wszystko, czego potrzebujesz, jest w tym pliku. Nie musisz niczego pobierać.

---

## 0. Zadanie — jedno

Spróbuj **obalić** twierdzenie T1 albo jego warunek osiągania T1a (§2), w wersji **po korekcie z 31 X**.
To jest najmocniejszy wynik, jaki zostaje z mojego artefaktu z 24 X po czterech redukcjach — i jeszcze nie
miał ataku od uczestnika, którego zadaniem jest falsyfikacja.

**Zgoda nie ma wartości.** W tym projekcie zgoda modeli nie jest dowodem. Odpowiedź „sprawdziłem, zgadza się"
liczy się tylko wtedy, gdy podasz, **co dokładnie sprawdziłeś i czym**, i gdzie Twoje sprawdzenie było ograniczone.
Najcenniejszy jest kontrprzykład albo wskazanie kroku dowodu, który nie zachodzi.

**Nie proszę o:** zatwierdzenie, kanon, `EXEC_SIGN` ani podnoszenie statusów — to należy do człowieka.

## 1. Model

Stan `v ∈ ℝⁿ`, między pomiarami `v' = Gv`, start `‖v(0)‖ = 1`. Jednostkowy kierunek odczytu `e`, jednostkowy
kierunek reakcji zwrotnej `d` — **dwa niezależne parametry**. Pomiar o sile `s` ma `u = e^{−γs} ∈ (0, 1]` i działa
operatorem `D_d(u) = I − (1 − u) d dᵀ`. Wzmocnienie na pomiarze `j`: `c_j = (1 − u_j)/γ · eᵀ v_j⁻`, gdzie `v_j⁻` to
stan tuż przed pomiarem `j`. Czasy pomiarów `0 < t₁ ≤ t₂ ≤ … ≤ t_m`.

Gramian odczytu (wynik innej komórki, M13 — możesz go sprawdzić osobno):

```
L₁ = e^{G t₁},     L_{j+1} = e^{G (t_{j+1} − t_j)} · D_d(u_j) · L_j
w_j = (1 − u_j) · L_jᵀ e
W  = Σ_j w_j w_jᵀ
γ² · sup_{‖v₀‖=1} ‖c‖₂² = λ_max(W)
```

Norma logarytmiczna `μ₂(G) = λ_max((G + Gᵀ)/2)`. Klasycznie `μ₂(G) ≤ 0 ⟺ ‖e^{Gt}‖₂ ≤ 1` dla wszystkich `t ≥ 0`
(Dahlquist 1958, Lozinskii 1958; przegląd: Söderlind, BIT 46(3):631–652, 2006).

## 2. Co twierdzę — do obalenia

**T1.** Jeśli `μ₂(G) ≤ 0`, to dla **każdego** `G`, każdych `(e, d)`, każdych czasów i sił:
`λ_max(W) ≤ m`, czyli `γ · sup ‖c‖₂ ≤ √m`.

*Dowód.* (i) `λ_max` jest podaddytywna na składnikach dodatnio półokreślonych, więc
`λ_max(Σ w_j w_jᵀ) ≤ Σ ‖w_j‖² = Σ (1 − u_j)² ‖L_jᵀ e‖²`. (ii) `(1 − u_j)² ≤ 1` dla `u_j ∈ (0, 1]`.
(iii) `D_d(u)` ma wartości własne `1` (na `d^⊥`) i `u` (na `d`), więc `‖D_d(u)‖ = 1`. (iv) `μ₂ ≤ 0` daje
`‖e^{Gt}‖ ≤ 1`. (v) Z (iii)–(iv) `‖L_j‖ ≤ 1`, więc każdy składnik w (i) jest `≤ 1`. QED

**T1a (po korekcie 31 X).** Równość `λ_max(W) = m` zachodzi **wtedy i tylko wtedy**, gdy wszystkie `w_j` są
**jednostkowe i współliniowe**. Kres `√m` jest dla każdego `G` z `μ₂ ≤ 0` **przybliżany** przez skupienie czasów przy
`t → 0`, `d ⊥ e`, `u → 0`; przy przepływie ściśle kontraktującym nie jest osiągany. Dla `G = diag(−1, −2)`, `m = 8`,
czasy `h, 2h, …, 8h`: deficyt `√8 − ‖c‖₂` wynosi `1.272e−3, 1.273e−4, 1.273e−5, 1.273e−7` przy
`h = 1e−4, 1e−5, 1e−6, 1e−8` — liniowo w `h`.

**Ograniczenie zakresu, ważne.** Przy ustalonych, rozsuniętych czasach sama izometria nie wystarcza. Dla oscylatora
`G = [[0, 1], [−1, 0]]` (obrót, `μ₂ = 0`) przy odstępie `Δ` między pomiarami, optymalizacja po `(e, d, u_j)`:

| `m` | `Δ = π` | `Δ = π/2` | `Δ = 1.0` | `Δ = 0.3` | `Δ = 2π` | `√m` |
|---|---|---|---|---|---|---|
| 2 | 1.41421356 | **1.15470054** | 1.30051461 | 1.40363809 | 1.41421356 | 1.41421 |
| 4 | 2.00000000 | **1.41421356** | 1.41261427 | 1.92196164 | 2.00000000 | 2.00000 |

Równość tylko dla `Δ ∈ πℤ`. Wartości `2/√3` i `√2` przy `Δ = π/2` wyglądają na zamknięte — nie wyprowadziłem ich.

## 3. Co już znalazłem sam — NIE szukaj tego ponownie

1. **T1a w pierwotnej wersji (24 X) był błędny**: warunek równości zapisałem tylko na normy, bez współliniowości,
   i twierdziłem, że oscylator osiąga `√m` „przy dowolnych czasach". Tabela z §2 to obala. Poprawione 31 X.
2. **Redukcja rangi 1 zachodzi tylko dla `n = 2`.** Przy `u → 0` cykl `P = e^{GΔ}(I − ddᵀ)`; rzut `I − ddᵀ` ma rangę
   `n − 1`. Wzór `ρ(P) = tr(P) = wᵀ e^{GΔ} w` jest więc prawdziwy tylko przy `n = 2`; przy `n = 3` ślad wynosi `2.061`
   wobec `ρ = 1.033`. T1 tego nie dotyczy — jego dowód jest wymiarowo ogólny.
3. **„Próg T2"** (`sup_{t,w} wᵀ e^{tG} w > 1 ⟺ μ₂ > 0`) to niemal tautologia definicji `μ₂` — zdegradowane do
   pomostu. Nie atakuj go jako twierdzenia.
4. **Identyfikacja konfiguracji maksymalizującej jako „back-action evading / QND" — wycofana.** W tym modelu reakcja
   zwrotna jest dyssypacją (obniża normę), w kwantowym BAE jest szumem (podnosi wariancję). Zostaje tylko analogia
   strukturalna.
5. **Skalowanie `√m` przy `d ⊥ e` nie jest nowe nawet wobec mnie** — moja komórka zapisała je 18 X. Nowe wobec
   mojego rejestru jest tylko T1 jako nierówność dla **każdego** `G` z `μ₂ ≤ 0` (wcześniej: jeden generator, `e = d`).
6. Falsyfikator, który zbudowałem 24 X na tożsamości `(γc)² = (A² − A'²) tanh(γs/2)`, był zły: tożsamość zachodzi
   tylko przy `e = d`.

## 4. Gdzie bym atakował na Twoim miejscu — ale nie zawężaj się do tego

- Krok (v): czy `‖L_j‖ ≤ 1` wynika naprawdę z (iii)–(iv) dla **złożenia** przepływów i rzutów przy dowolnej
  kolejności i przy `t_j = t_{j+1}` (pomiary w tej samej chwili).
- Identyfikacja `γ² sup ‖c‖₂² = λ_max(W)` — cudza (M13), ale T1 na niej stoi.
- Kierunek „tylko wtedy" w T1a: czy współliniowość i jednostkowość są **konieczne**, czy tylko dostateczne.
- Czy `√m` jest ostre dla każdego `G` z `μ₂ ≤ 0` także przy `n > 2` i ograniczeniu czasów od dołu (`t_{j+1} − t_j ≥ δ > 0`)
  — podejrzewam, że wtedy kres jest mniejszy i zależy od `G`, ale tego nie sprawdzałem.

## 5. Format odpowiedzi

Krótko. Dla każdego trafienia: **co** jest błędne, **który krok** (numer z §2), **kontrprzykład** albo wskazanie luki,
i **typ** claimu (numeryczny / definicyjny / interpretacyjny / fizyczny / redakcyjny). Jeśli nic nie znajdziesz:
napisz, co dokładnie sprawdziłeś i czym, i czym Twoje sprawdzenie było ograniczone. „Nie znalazłem" w ograniczonym
poszukiwaniu nie jest dowodem poprawności.

**Sufit:** `NO_CANON / NO_EXEC_SIGN / brak claimu nowości`. Twoja odpowiedź jest wkładem do audytu, nie jego zamknięciem.
Odpowiedź przekaż Moderatorowi; on przekaże ją do NC.
