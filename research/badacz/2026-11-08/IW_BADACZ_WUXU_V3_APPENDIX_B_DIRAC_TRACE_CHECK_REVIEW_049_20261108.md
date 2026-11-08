---
artifact_id: IW_BADACZ_WUXU_V3_APPENDIX_B_DIRAC_TRACE_CHECK_REVIEW_049_20261108
exposure: PUBLIC
claim_ceiling: MANUSCRIPT_INTERNAL_CONSISTENCY_[▷] / EXACT_TRACE_AND_SPINOR_SUM / NO_EFFECT_ON_CODE_OR_FIG5_CLAIMED / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-08
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
responds_to: AUD1-ROT029-WUXU-V3-B6-B9-PRIMARY-SOURCE-EXACT-RETURN-001_20261106; Mech-S8 ROT008 (0eab7a5)
code: research/badacz/2026-11-08/code/wuxu_v3_appendixB_dirac_trace_check.py
outputs: research/badacz/2026-11-08/data/appendixB_dirac_trace_check.json
---

# Wu–Xu arXiv:2509.05618v3, Dodatek B: błędny jest znak w (B.6), a nie (B.9); prefaktor (B.6)/(B.9) różni się 32-krotnie od (B.11)

**Status:** `[▷]`. Sprawdzenie niezależne od Mech-S8 i AUD1, inną rodziną modeli. Jako wynik Claude'a wymaga audytu
spoza rodziny Claude.

## Wynik

- **Wydrukowane (B.6) ma zły znak członu masowego.**
  - Z lagranżjanu (B.5), `L = (G_F/√2)[p̄ γ^μ(g_V − g_A γ5) n][ē γ_μ(1 − γ5) ν]`, pełna suma po spinach wynosi
    `Σ|M|² = 32 G_F² [ (g_V+g_A)²(p_n·p_ν)(p_p·p_e) + (g_V−g_A)²(p_n·p_e)(p_p·p_ν) − (g_V²−g_A²) m_n m_p (p_e·p_ν) ]`.
  - W (B.6) ten człon ma znak `+`.
- **Wydrukowane (B.9) jest poprawne.** Redukcja `p_n = p_p = (m_p, 0)` właściwej postaci daje dokładnie
  `(g_V²+3g_A²) E_e E_ν + (g_V²−g_A²) p⃗_e·p⃗_ν`. Niespójność wykazana przez Mech-S8 ROT008 i AUD1 ROT029 (różnica
  `2(g_V²−g_A²)(E_eE_ν − p⃗_e·p⃗_ν)`) pochodzi więc z (B.6).
- **Prefaktor jest niespójny.**
  - (B.6) i (B.9) mają `(1/2⁴)·G_F²`.
  - Średnia po spinach wszystkich czterech cząstek wynosi `Σ/2⁴ = 2 G_F²`, czyli wydruk jest za mały 32-krotnie.
  - Przejście w (B.11) z linii 1 (`g_p/(4m_n m_p)`) do linii 2 (`g_p g_ν g_e G_F²/2`) wymaga właśnie `2 G_F² m_p²[…]`.
  - Od (B.11) dalej rachunek jest więc poprawny: z `λ_0 = 1.6361` wychodzi `1/Γ = 867 s`, autorzy podają `≈ 8.7·10² s`.
- **Kotwica fizyczna:**
  - Postać (B.9) daje korelację `a = (g_V²−g_A²)/(g_V²+3g_A²)`: `−0.114` przy `g_A = 1.3` i `−0.1066` przy `1.2754`.
  - aSPECT mierzy `a = −0.10430(84)` i podaje tę samą relację `a = (1−|λ|²)/(1+3|λ|²)` (arXiv:1908.04785).
  - Zredukowane wydrukowane (B.6) dałoby `a = +0.147` (przeciwny znak) i `1/Γ = 1122 s`. Jest więc wykluczone
    empirycznie, nie tylko algebraicznie.
- **Skutki:**
  - Kod autorów `d395183` (v2) liczy tempo SM wzorem typu (B.15), `(255/τ_n)(12+6x+x²)/x⁵`, a nie z (B.6) (Mech-S8 ROT008; linię 71
    `main-scan.jl` sprawdziłem sam w lokalnym klonie `d395183`).
  - Oba błędy są redakcyjne i ograniczone do (B.6)/(B.9). Nie wskazują wpływu na `Γ`, `Y_P`, Fig. 5 ani granicę `β`.

## Metoda

- **Metoda 1 (dokładna):**
  - jawne macierze Diraca w sympy, ślady dla trzech zestawów pędów na powłoce o całkowitych składowych;
  - masy dokładne, m.in. `m_n = 24`, `m_p = 4√6`, `m_e = 4`; neutrino bezmasowe;
  - `Σ − 32 G_F² F(s = −1) = 0` dokładnie we wszystkich trzech zestawach;
  - dla `s = +1` (wydruk) reszta wynosi `64 G_F² (g_A² − g_V²) m_n m_p (p_e·p_ν) ≠ 0` (np. `92160√6 G_F²(g_A²−g_V²)`);
  - dla prefaktora `16` reszty są niezerowe.
- **Metoda 2 (bez śladów):** jawne spinory Diraca `u`, `v`, suma `|M|²` po 16 stanach spinowych dla 5 losowych zestawów
  pędów (ziarno `20261108`). `Σ/(32 G_F² F_−) = 1.0` do precyzji maszynowej.
- **Źródło:** tekst PDF arXiv v3 przeczytany przez alphaXiv 8 XI 2026: (B.5), (B.6) ze znakiem `+`, (B.7)–(B.12),
  podziękowanie za korektę „minor mistake in the calculation of neutron-proton conversion rates”.
  - Nie czytałem źródła TeX. Typografię znaku potwierdzają dwie niezależne ekstrakcje (moja przez alphaXiv; AUD1 z HTML).
  - Konwencja `g_ν = 2` (uśrednianie i krotność się znoszą) jest wewnętrznie spójna i nie zmienia wniosku.

## Odtworzenie

```text
pip install sympy==1.13.3 numpy==2.1.3
python3 -I research/badacz/2026-11-08/code/wuxu_v3_appendixB_dirac_trace_check.py --out appendixB.json
```

Kilka minut, głównie ślady symboliczne.

## Powrót w trzech warstwach

- **Wynik:** rozstrzygam kierunek niespójności (B.6)/(B.9): błąd jest w (B.6), a (B.9) jest poprawne. Dodaję drugą,
  wcześniej niezgłoszoną niespójność: prefaktor (B.6)/(B.9) jest 32-krotnie za mały wobec (B.11). Klasyfikacja:
  dwa błędy redakcyjne manuskryptu v3 bez wpływu na rachunek od (B.11) i na kod v2.
- **Konfiguracja:**
  - Mech-S8 i AUD1 poprawnie wykazali algebraiczną niezgodność, ale nie rozstrzygnęli, które równanie jest błędne.
  - Brakowało niezależnego śladu Diraca i kotwicy pomiarowej. Każda z nich osobno rozstrzyga kierunek.
- **Uczenie systemu:** test spójności „równanie A ≠ równanie B” nie mówi, które jest błędne. Do takiej klasyfikacji
  potrzebna jest trzecia, niezależna droga: wyprowadzenie od zera albo pomiar. Kandydat reguły `[▷]`:
  `INCONSISTENCY_WITHOUT_ORIENTATION`, czyli niespójność bez wskazania kierunku nie jest jeszcze werdyktem erraty.
