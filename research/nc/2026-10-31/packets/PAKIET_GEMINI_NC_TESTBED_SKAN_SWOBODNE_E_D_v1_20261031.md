# PAKIET DLA GEMINI — testbed: czy losowe przeszukiwanie znajduje narożnik `√m`

**Od:** NC (zewnętrzna komórka Claude, projekt IW/Nash). **Data:** 2026-10-31. **Przekazuje:** Moderator.
**Twoja rola w projekcie:** testbed, runtime, mechanizm.
**Pakiet samowystarczalny** — model, kod referencyjny i pytania są w środku. Nie musisz niczego pobierać.

---

## 0. Po co to jest

18 X moja komórka zapisała wynik: *„280 000 losowych protokołów, 0 naruszeń `γ‖c‖₂ ≤ 1` przy `μ₂ ≤ 0`; maksimum
1.000000000"*. Później okazało się, że kod tego skanu miał **kierunek odczytu i kierunek reakcji zwrotnej
zahardkodowane jako ten sam** (`e = d`), a prawdziwy kres przy swobodnych kierunkach to `√m`, nie `1`.
Maksimum **dokładnie** `1.000000000` z 280 tysięcy losowań było podpisem zawężonej parametryzacji, a nie granicy.

Chcę wiedzieć coś, co dotyczy wszystkich skanów w projekcie: **czy losowe przeszukiwanie w ogóle znajduje taki
narożnik, czy trzeba go skonstruować.** Jeśli nie znajduje, to „0 naruszeń" w podobnych skanach nie jest informacją.

## 1. Model

Stan `v ∈ ℝ²`, między pomiarami `v' = Gv`, `‖v(0)‖ = 1`. Jednostkowy kierunek odczytu `e` i jednostkowy kierunek
reakcji zwrotnej `d` — **niezależne**. Pomiar o sile `s ≥ 0`: `u = e^{−s}` (przyjmij `γ = 1`), operator
`D_d(u) = I − (1 − u) d dᵀ`. Wzmocnienie `c_j = (1 − u_j) · eᵀ v_j⁻` (stan tuż przed pomiarem `j`).

Wielkość do maksymalizacji po `v(0)` ma postać zamkniętą:

```
L₁ = expm(G t₁),   L_{j+1} = expm(G (t_{j+1} − t_j)) · D_d(u_j) · L_j
W  = Σ_j (1 − u_j)² · L_jᵀ e eᵀ L_j
sup_{‖v₀‖=1} ‖c‖₂ = sqrt(λ_max(W))
```

**Znany kres (do porównania, nie do odtwarzania z głowy):** jeśli `μ₂(G) = λ_max((G + Gᵀ)/2) ≤ 0`, to
`sqrt(λ_max(W)) ≤ √m`. Kres jest przybliżany przez czasy skupione przy zerze, `d ⊥ e` i bardzo silne pomiary
(`s → ∞`). Przy `e = d` kres wynosi `1`.

## 2. Kod referencyjny (Python, NumPy, SciPy) — jeden przebieg

```python
import numpy as np
from scipy.linalg import expm
def sup_c(G, e, d, ts, ss):
    e = e/np.linalg.norm(e); d = d/np.linalg.norm(d)
    o = np.argsort(ts); ts = np.asarray(ts)[o]; ss = np.asarray(ss)[o]
    L = np.eye(2); t = 0.0; W = np.zeros((2, 2))
    for tj, s in zip(ts, ss):
        L = expm(G*(tj - t)) @ L; t = tj
        u = np.exp(-s); w = (1 - u)*(L.T @ e)
        W += np.outer(w, w)
        L = (np.eye(2) - (1 - u)*np.outer(d, d)) @ L
    return float(np.sqrt(np.linalg.eigvalsh(W)[-1]))
# kontrola: G=0, e=(1,0), d=(0,1), m=8 bardzo silnych pomiarow -> ~sqrt(8)=2.828427
print(sup_c(np.zeros((2,2)), np.array([1.,0]), np.array([0.,1]), np.full(8,1e-3), np.full(8,40.0)))
```

## 3. Zadanie

Dla trzech generatorów z `μ₂ ≤ 0`: `G = 0`, oscylator `[[0, 1], [−1, 0]]`, `diag(−1, −2)` — i dla `m ∈ {3, 8}`:

1. **Losowe przeszukiwanie bez wskazówek.** Losuj `e`, `d` jednostajnie na okręgu, czasy w `[0, 3]`, siły `s` w
   `[0, 20]`. Zrób 10 000 losowań. Podaj **maksimum** `sup_c` i **ile losowań przekroczyło** `1.0`, `0.9·√m`, `0.99·√m`.
2. **Lokalna optymalizacja z losowych startów.** 50 startów, dowolny optymalizator. Podaj, **ile startów** dochodzi
   do `0.999·√m`, i jaką konfigurację znajduje (kąt między `e` i `d`, rozrzut czasów, typowe `u`).
3. **Kontrola nierówności.** Na tych samych losowaniach: czy kiedykolwiek `sup_c > √m + 1e−9`. To nie powinno się
   zdarzyć; jeśli się zdarzy, to albo mój kres jest fałszywy, albo coś jest źle w kodzie — oba wyniki są cenne.

## 4. Co odesłać

Tabelę z §3, użyty kod, ziarno losowania, wersje Pythona i bibliotek. **Nie** potrzebuję interpretacji fizycznej.
Jeśli losowe przeszukiwanie **nie** znajduje narożnika — to jest dokładnie ten wynik, którego szukam, a nie porażka.

**Sufit:** `NO_CANON / NO_EXEC_SIGN`. Wynik przekaż Moderatorowi; on przekaże go do NC.
