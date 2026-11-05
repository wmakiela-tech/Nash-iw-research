---
artifact_id: IW_MECH_S8_ROT008_WUXU_V3_APPENDIX_B6_B9_INTERNAL_ALGEBRA_FALSIFIER_001_20261105
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
created_at: 2026-11-05
exposure: PUBLIC_SAFE
result_class: DIRECT_ORIGINAL_MANUSCRIPT_EQUATION_CHECK / INDEPENDENT_EXACT_RATIONAL_AND_SYMBOLIC_REPLAY
source_class: ARXIV_V3_MANUSCRIPT_FORMULAS_NOT_PUBLISHED_JCAP_EXECUTION_NOT_PINNED_V2_JULIA_CODE
sync_state: LOCAL_VERIFIED / GITHUB_PENDING_READBACK / BW_PENDING
claim_ceiling: EQ_B6_TO_B9_ALGEBRA_DISAGREEMENT_ONLY / AUTHOR_CLARIFICATION_PENDING / NO_PHYSICAL_BOUND / NO_CANON / NO_EXEC_SIGN
---

# ROT008 — Wu–Xu v3: wewnętrzny falsyfikator równań (B.6)–(B.9), aneks B

## 1. Zakres i proweniencja

Sprawdzenie **oryginalnych równania autorów**, nie fizycznej dokładności programu ani publikowanego ograniczenia kosmologicznego. Prace Wu i Xu, *Primordial Black Holes Evaporating before Big Bang Nucleosynthesis*, arXiv:2509.05618:

- **arXiv v2, 30 grudnia 2025:** https://arxiv.org/html/2509.05618v2; aneks B: (B.6) uproszczony kwadrat amplitudy z czynnikiem `32 G_F²`, (B.12)/(B.14) końcowe przybliżone stopy konwersji.
- **JCAP 02 (2026) 063, opublikowany 17 lutego 2026:** https://doi.org/10.1088/1475-7516/2026/02/063 — nie przypisywać równania wersji v3 historycznie opublikowanej wersji bez kontroli jej PDF.
- **arXiv v3, 6 maja 2026:** https://arxiv.org/html/2509.05618v3; w aneksie B pojawia się rozwinięty wzór (B.6) i nowe kroki (B.7)–(B.9), końcowe wzory (B.15)/(B.17); autorzy dziękują Boting Zhou za pomoc w poprawieniu *minor mistake* w obliczaniu szybkości konwersji neutron–proton. To potwierdza zmianę redakcyjną/teoretyczną, **ale nie podaje tożsamości wykonywanego kodu, zakresu wartości nowej poprawki ani zmiany Fig.5**.
- **Publiczny kod autorów v2:** https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl; Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`. Linia 71: `Γₙ_SM = (255 / τ_n) * (12 + 6 * x + x^2) / x^5`; linia 88: SM `dXₙ_dt_SM`, linia 89: osobny rozpad `dXₙ_dt_decay = -Xₙ / τ_n`. Repozytorium publiczne ma `master` HEAD `d395183` z 30 XII 2025 (v2), nie potwierdzono v3 code commit.

**Metoda materiałowa:** odczyt tekstu matematycznego bezpośrednio z arXiv HTML v2/v3; próby screenshotów arXiv PDF w narzędziu sieciowym zwróciły `cache miss`, zatem nie deklaruję fotograficznego porównania typograficznego PDF. Podane rówania sprawdzić niezależnie w źródłowym PDF/TeX przed publikacją zewnętrznego zarzutu.

## 2. Dokładny falsyfikator (warunkowy na wiernym odczycie wzorów v3)

Po wyłączeniu wspólnego czynnika `G_F² m_p² / 16`, wzór v3 (B.6) to suma

```
B6 = (gV+gA)^2 * (pn·pν)(pp·pe)/mp²
   + (gV-gA)^2 * (pn·pe)(pp·pν)/mp²
   + (gV²-gA²) * (mn/mp) * (pe·pν)
```

W tym samym przybliżeniu v3 (B.7) podaje `pn=pp=(mp,0)` (masses identified to leading order), a v3 (B.8) `pe·pν=Ee Eν - vec_pe·vec_pν`. Stąd redukcja ściśle algebraiczna:

```
B6_NR = (3gV²+gA²)*Ee*Eν - (gV²-gA²)*(vec_pe·vec_pν).
```

Natomiast **wydrukowany** v3 (B.9) przy identycznym czynniku zewnętrznym podaje

```
B9_print = (gV²+3gA²)*Ee*Eν + (gV²-gA²)*(vec_pe·vec_pν).
```

Zatem

```
B6_NR - B9_print
  = 2*(gV²-gA²)*(Ee*Eν - vec_pe·vec_pν).
```

Wzory **nie są identyczne ogólnie**. Pokrywają się jedynie na szczególnych podklasach takich jak `gV²=gA²` lub `pe·pν=0`. Kontrola jawna (we wspólnych jednostkach i z wyłączoną normalizacją): `gV=1`, `gA=13/10`, `Ee=Eν=1`, `vec_pe·vec_pν=0`: `B6_NR=469/100`, `B9=607/100`, różnica `-69/50`. Lokalna różnica normalizowana do (B.9) = `138/607 ≈ 22.735%` (wyłącznie współczynnik algebraiczny; **nie** procent fizycznego błędu Γ, Yp czy β).

Test niezależny: 147 kombinacji exact `fractions.Fraction` plus 5 kontrolnych (w tym dwa warunki szczególnej równości); dodatkowo symboliczne rozwinięcie SymPy `PASS`. Reproduktor jednoplikowy `mech_s8_rot008_wuxu_v3_appendix_b6_b9_algebra_audit.py`, JSON. To wskazuje na **wewnętrzną niezgodność zapisów aneksu v3**, nie na błędne obserwacje lub wyniki autorów.

## 3. Dodatkowa uwaga o normalizacji i implementacji — brak przeniesienia na fizykę

V2 (B.6) zawiera `32 G_F²` przed uproszczonym wyrażeniem, zaś wyświetlony v3 (B.6) zawiera `G_F²` przed rozwiniętym wyrażeniem. Tego problemu normalizacji **nie** zaliczam do niezależnego ilościowego werdyktu fizycznego: wymaga przeglądu definicji sumowania/średniowania spinów i pełnej ścieżki B.4→B.11. Już powyższe **porównanie bez wspólnej normalizacji** jest rozstrzygające dla poprawności samego przejścia B.6→B.9 przy zapisanych podstawieniach.

Oryginalny przypięty `main-scan.jl` v2 stosuje ostateczne przybliżenie `255` (w tekście v2 B.12 i v3 B.15 występuje analityczny współczynnik około `253.9`) oraz niezależnie dodaje rozpad neutronu. **Nie wyprowadza w runtime kwadratu amplitudy z v3 B.6**. Brak v3 zmian w GitHub master nie dowodzi braku prywatnej poprawki. Brak materiałów uzasadniających stwierdzenie „JCAP Fig.5 ma błąd” lub „beta zmienia się o X%”.

## 4. Werdykt / następny test

- `V3_B6_B9_ALGEBRA_CONSISTENCY = FAIL_WITH_EXPLICIT_COUNTEREXAMPLE` **dla dokładnych zapisów HTML w źródle**.
- `SYMBOLIC_REPLAY = PASS`; `EXACT_RATIONAL_152_CASES = PASS`.
- `V2_AUTHOR_MAIN_SCAN_WEAK_RATE = READBACK_VERIFIED`; nie stanowi potwierdzenia nowego wykonania v3.
- `JCAP_PUBLISHED_FIG5_EFFECT = UNDETERMINED`; `V3_UPDATED_RATE_CODE = NOT_FOUND_IN_CHECKED_AUTHOR_MASTER`.
- `E4_HADRON_SPECTRUM_PHYSICS = HOLD/SOURCE_BLOCK`; `MECH_ROT035_ODE_CERT = OPEN`.

**Wniosek dla REC11/AUD1**: jeden audyt formuł rękopisu przez drugą niezależną rodzinę (najpierw potwierdzić źródłowy PDF/TeX, potem arytmetykę spinową i precyzyjny klucz do typograficznego erratum); następnie tylko jeśli źródło na to wskazuje, zwrócić się do autorów z pytaniem o wersję kodu i wpływ na (B.15)/(B.17), wykresy Yp, Fig.5. Nie postulować automatycznej reanalizy fizycznych ograniczeń.

`NO_PHYSICAL_BOUND / NO_CANON / NO_EXEC_SIGN / BW_PENDING / INDEPENDENT_REVIEW_PENDING`