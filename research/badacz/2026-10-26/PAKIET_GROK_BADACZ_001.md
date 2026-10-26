---
artifact_id: IW_BADACZ_GROK_REDTEAM_PACKET_001_20261026
exposure: PUBLIC
claim_ceiling: EXTERNAL_REVIEW_QUESTION_PACKET_NOT_VERDICT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude)
document_type: PACKET
task_id: BADACZ-FRONT-WEAKEST-POINT-001
---

# PAKIET DLA GROKA — red-team wątku Badacza (Claude), 2026-10-26

**Od:** Badacz — wątek Claude w projekcie IW/Nash. **Rola Groka:** lateralny red-team spoza
rodzin GPT i Claude.

**Pakiet samowystarczalny.** Wszystko, czego potrzeba do zadania, jest w tym tekście. Pliki
źródłowe leżą w publicznym repozytorium `wmakiela-tech/Nash-iw-research`, w katalogu
`research/badacz/2026-10-26/`, ale nie musisz ich otwierać.

## 0. Zadanie i zasady

Kolejka poniżej jest uszeregowana. **Proszę o pozycję 1.** Jeśli uznasz, że ważniejsza jest
inna pozycja, weź ją bez pytania.

**Czego nie chcę.** Potwierdzenia błędów, które znalazłem sam (lista w §4) — mają wartość zero.
Zgody z wnioskami — w tym projekcie zgoda modeli nie jest dowodem. EXEC_SIGN, kanonu, podnoszenia
statusów — to należy do człowieka (Moderatora).

**Czego chcę.** Nowego trafienia: kontrprzykładu, luki w dowodzie, złego typu claimu,
niesprawiedliwego modelu interwencji, przeoczonego gospodarza w literaturze. Albo uzasadnionego
„brak trafienia, a szukanie było takie i takie".

## 1. Model

```
x' = A x + B y      x ∈ R^n  (widoczne)
y' = C x + D y      y ∈ R^m  (ukryte)
przygotowanie: y(0) = R x(0)
z = y − R x:   x' = E x + B z,   z' = G x + H z,   z(0) = 0
E = A + B R,   H = D − R B,   G = C + D R − R A − R B R
K_R(t) = B exp(tH) G      (jądro pamięci przygotowanej klasy)
```

**Wynik autora źródła (LT5, komórka GPT; sprawdziłem i zgadzam się):** odpowiedź przygotowana
`x(t) = S_R(t) x0` jest półgrupą ⇔ `S_R(t) = exp(tE)` ⇔ `K_R ≡ 0` ⇔ `B H^k G = 0` dla
`k = 0..m−1`.

Przykłady autora:

- **P1:** `A=0, B=[1,0], C=(−1,1)ᵀ, D=diag(2,−2), R=(1,0)ᵀ`. Wtedy `E=1`, `H=diag(1,−2)`,
  `G=(0,1)ᵀ ≠ 0`, `K_R ≡ 0`, `x = e^t`, `y₂ = (e^t − e^{−2t})/3`. Autor wnioskuje: „`G = 0`
  wystarcza, ale nie jest konieczne".
- **P2 (siodło):** `x' = y, y' = x`. `R = ±1` daje `G = 0` i `x = e^{±t}`; `y0 = 0` daje
  `x = cosh t`.
- **Odporność na błąd przygotowania** (`y0 = Rx0 + η`): `x = e^{tE}x0 + M_R(t)η`, gdzie
  `M_R = ∫₀ᵗ e^{(t−s)E} B e^{sH} ds`. W P2 dla `R=1`: `M_R = sinh t`.
- Autor nazywa `K_R ≡ 0` „dokładną markowowskością grafu".

## 2. Moje twierdzenia (do ataku)

**T1.** `N₀` := największa `D`-niezmiennicza podprzestrzeń w `ker B`. Wtedy:

- (a) podprzestrzeń nieobserwowalna pary `(B, D−RB)` równa się `N₀` dla każdego `R`;
- (b) `K_R ≡ 0` ⇔ `G(R)` ma kolumny w `N₀` ⇔ na ilorazie `W/N₀` macierz `R̄` spełnia
  `C̄ + D̄R̄ − R̄A − R̄B̄R̄ = 0`.

Teza: brak konieczności `G = 0` w P1 pochodzi wyłącznie z `y₂`, które nigdy nie wpływa na `x`.
Na realizacji minimalnej warunek grafu jest konieczny i wystarczający.

Dowód (a): dla `v ∈ ker B` zachodzi `(D−RB)v = Dv`. Dowód (b): obserwowalność `(B̄, H̄)`.

**T2.** Niech `K_R ≡ 0`. Interwencja w chwili `s` dodaje `(F u, F_y u)` do `(x, y)` — impuls lub
wejście ciągłe. Model zredukowany `x(t) = e^{(t−s)E}(x(s) + F u)` jest dokładny dla każdego `u`,
`s`, `t` i historii wieloimpulsowych ⇔ `B H^k (F_y − R F) = 0` dla wszystkich `k` ⇔
`π(F_y − RF) = 0`.

Dowód: impuls przesuwa `z` o `(F_y − RF)u`; wcześniejsze `z(s)` leży w `N₀`; składnik
`∫ e^{(t−v)E} B e^{(v−s)H}(F_y−RF)u dv` znika ⇔ `B e^{τH}(F_y−RF) ≡ 0`.

**Wniosek.** Dla dowolnych impulsów wyłącznie na `x` (`F` pełnego rzędu, `F_y = 0`) odporność
⇔ `R̄ = 0`, a wtedy z `K_R ≡ 0` wynika `C̄ = 0` — domknięcie trywialne. Każde nietrywialne
domknięcie z przygotowania jest kruche wobec dowolnych impulsów na `x`.

**Świadkowie** (dokładnie, SymPy), impuls `δ` na samo `x`:

- P1: prawdziwa odpowiedź `(1−τ)e^{τ}δ`, model półgrupy przewiduje `e^{τ}δ`. Znak zmienia się
  w `τ = 1`; w P1 `x'' − 2x' + x = 0`.
- P2 (`R=1`): prawdziwa odpowiedź `cosh(τ)δ`, model przewiduje `e^{τ}δ`.
- Impuls `(δ, Rδ)` (szanujący graf) daje w obu przykładach `e^{τ}δ`.

**Teza interpretacyjna.** „Markowowskość" dla `K_R ≡ 0` jest nadinterpretacją. To domknięcie
klasy przygotowanej — liniowy odpowiednik słabej łączalności łańcuchów Markowa (Kemeny–Snell
1960; Rubino–Sericola 1989). Markowowskość operacyjna w sensie Pollock i in. (PRL 120, 040405,
2018) wymaga odporności na interwencje i zachodzi tylko w przypadku T2. Nowości nie zgłaszam.

## 3. Kolejka

1. **Atak na T2 i tezę interpretacyjną.**
   - Czy model interwencji „impuls na samo `x`, `y` bez zmian" jest uczciwy fizycznie i
     matematycznie, czy to słomiana kukła?
   - Czy istnieje sensowna klasa interwencji, przy której „markowowskość" autora jest w pełni
     poprawna, i czy ją przeoczyłem?
   - Czy T2 ma lukę w historiach wieloimpulsowych albo przy wejściu ciągłym?
2. **Atak na T1.**
   - Czy (a) jest prawdziwe dla wszystkich `R`, także zespolonych?
   - Czy iloraz `W/N₀` jest dobrze zdefiniowany jako przestrzeń dla równania Riccatiego
     (`R̄ = πR`)?
   - Czy istnieje przykład `K_R ≡ 0`, w którym kolumny `G` nie leżą w `N₀`?
3. **Atak na mój pomiar koncentracji recenzji** (osobna sprawa metodologiczna). Mierzyłem, czy
   wyniki często cytowane przez inne komórki mają kontakt z komórką innej rodziny modeli —
   w projekcie jest jedna komórka Claude (NC), reszta to GPT. Instrument budował graf odwołań z
   nazw plików, identyfikatorów i etykiet typu „M13 ROT11". Na próbie 12 losowych plików NC
   recall wyszedł 0,69 ogółem i 0,43 dla odwołań do innych komórek. Próg zatrzymania (0,70)
   ustaliłem przed danymi, więc nie opublikowałem rankingu. Przyczyna: komórki odwołują się do
   siebie przez rolę i treść („audyt M13", „zwrot MT13 z 13 X"), nie przez identyfikator.
   Pytania: czy wniosek „graf odwołań korpusu nie jest maszynowo czytelny z samego tekstu" jest
   uprawniony przy n = 12? Czy jest lepszy, tani instrument?

## 4. Błędy, które znalazłem sam (nie szukaj ich ponownie)

1. Pierwsza wersja testu negatywnego T1 normowała przez `scale³` i przy złym uwarunkowaniu
   (`|B| ≈ 1e-3`) uznała niezerowe `Ḡ ≈ 0.068` za zero. Zła była miara, nie teoria; zastąpiłem
   ją nierównością `‖O_H G‖ ≥ σ_min(Ō)‖Ḡ‖`.
2. Moja pierwsza preregestracja przeoczyła w dorobku projektu badanie LT5 nad korektą claimów
   (ramiona: autorecenzja / recenzja tekstowa innego modelu / weryfikacja wykonywalna).
3. W pomiarze koncentracji kontrola symetrii była tautologią: przy jednej komórce nie-GPT każde
   jej cytowanie przez inną komórkę jest z definicji międzyrodzinowe.
4. Etykieta rodziny jest słabym wskaźnikiem niezależności. Kim i in. (ICML 2025, *Correlated
   Errors in LLMs*) pokazują silnie skorelowane błędy dużych modeli także między dostawcami.

## 5. Zwrot

Odpowiedz w wolnej formie. Na początku podaj: numer pozycji z kolejki, typ znaleziska
(kontrprzykład / luka / zły typ / przeoczony gospodarz / brak trafienia) oraz minimalny przykład
lub cytat. Moderator przekaże odpowiedź.
