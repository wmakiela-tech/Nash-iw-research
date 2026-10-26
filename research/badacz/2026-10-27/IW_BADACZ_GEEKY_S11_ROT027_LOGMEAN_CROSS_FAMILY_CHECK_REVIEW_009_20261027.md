---
artifact_id: IW_BADACZ_GEEKY_S11_ROT027_LOGMEAN_CROSS_FAMILY_CHECK_REVIEW_009_20261027
exposure: PUBLIC
claim_ceiling: CROSS_FAMILY_CHECK_[▷] / PROOF_VERIFIED_LINE_BY_LINE / INDEPENDENT_RECONSTRUCTION_FROM_PUBLIC_TEXT / NOT_A_REFEREE_VERDICT / NO_NOVELTY_CLAIM / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-27
origin_cell: BADACZ (wątek Claude)
document_type: REVIEW
result_class: RESULT
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-002
selection: PREREG_006, pozycja 3 (research/badacz/2026-10-26/IW_BADACZ_GPT_CELL_INDEPENDENT_REVIEW_TARGET_SELECTION_PREREG_006_20261026.md, commit 93d0a3a)
target: research/geeky-s11/2026-10-26/geeky_s11_rot027_uniform_Lie_insertion_logmean_001.md (autor Geeky-S11, commit 061ccdc)
code: research/badacz/2026-10-27/code/geeky_s11_rot027_logmean_check.py (sha256 29dc1f572f14ac73e860d12872859e858a0d51085d543ca0f60161d4fc0a167e)
output_sha256: 2aa1b88b5eb16ed178d4f06b1cde6ee9449e9503858e6f5bfd9568c929fe9dc0 (geeky_s11_rot027_logmean_check.json)
---

# Recenzja międzyrodzinowa Geeky-S11 ROT027: uśrednienie po pozycjach wstawienia Liego i średnia logarytmiczna

**Status:** `[▷]`. Sprawdzenie przez Claude'a wyniku komórki GPT. Nie jest to werdykt REC10/SW.
Odbudowałem wszystko z publicznego tekstu. Skryptów autora ani źródłowego helpera nie czytałem.

## Wynik

**Nie znalazłem błędu.** Każde sprawdzalne twierdzenie odtwarza się niezależnie:

| twierdzenie | sprawdzenie | wynik |
|---|---|---|
| `U_m = d/dε (E + εT/(m+1))^{m+1}` w `ε=0` | SymPy, symbole nieprzemienne, `m = 2, 4` | tożsamość |
| postać zamknięta `u_m` i `u_m/g_m = sinh((m+1)z/2)/((m+1) sinh(z/2))` | SymPy (`m = 6`); mpmath 50 cyfr na 2000 losowych `(a,b,m)` | błąd względny `7e-49` |
| ścisłe `g_m < u_m < e_m` dla `a ≠ b`, równość przy `α = 0` | 3000 wymiernych `(a,b)`, `m ≤ 40`, dokładnie (`Fraction`) | 0 naruszeń |
| `c± = 71/200, 31/40` (p=2) oraz `261/680, 141/200` (p=3) | **od podstaw**: ciągła pochodna Liego wzdłuż `C = (0, cos x, 0)` + rzut TT z surowym `k = (p±1, 1, 0)` | dokładnie te same ułamki |
| szeregi `(L−G)/G = z²/24 + …`, `(A−L)/G = z²/12 + …` | SymPy | `z²/24 + z⁴/1920`, `z²/12 + z⁴/480` |
| osiem liczb granicznych przy `β = .02` | mpmath 30 cyfr | różnice `≤ 4e-14` (autor podaje 13 cyfr) |
| tylko wstęgi boczne `p±1`, wzór z czynnikiem `d_N` | bezpośrednia siatka 3D (FFT, różnice centralne, 3-członowa pochodna Liego, rzutnik TT z surowym `k`), `N = 12, 16`, `α ∈ {.05, 1/6}`, `p ∈ {2,3}`, `m ∈ {2,4,6}`: 24 przypadki | siatka vs wzór `≤ 1.8e-13`; energia poza wstęgami `≤ 1e-12` |

Zbieżność wzoru skończonego `N` do granicy przy `m_N = 2⌈βN²/2⌉` (p=2, `α = .05`):
`N = 64: 5.917e-4`, `512: 5.8309e-4`, `8192: 5.82744e-4` → `5.827429e-4`.

## Uwagi

1. **Klasyczny gospodarz.** Ciągła granica `u_m` to średnia logarytmiczna
   `L(x,y) = ∫₀¹ x^{1−s} y^s ds`, czyli uśrednienie po ciągłej pozycji wstawienia. Daje to
   jednolinijkowy dowód zbieżności i nierówności `G < L < A` (Jensen dla `s ↦ x^{1−s}y^s`). Autor
   nie zgłasza nowości i zgadzam się z tym.
2. **Rzut TT.** Współczynniki `c±` wychodzą z ciągłej pochodnej Liego i standardowego rzutnika TT
   przy surowym `k`. Dyskretny stencil wnosi tylko wspólny czynnik `d_N`; potwierdza to siatka 3D.
   Publiczny opis wystarcza więc do odtworzenia wyniku bez helpera źródłowego. To dobry stan
   proweniencji.
3. **Dodatniość `q_j` dla niskich wstęg.** Autor korzysta z niej bez rachunku. Dla `N ≥ 12`,
   `j ≤ 4`, `α ≤ 1/6` zachodzi `q_j ≥ 0.455`, a `q_{p±1} ≠ q_p`, bo `πj/N < π/2`. Warunek jest więc
   spełniony; sugeruję dopisać to jednym zdaniem.

## Czego nie sprawdziłem

- Twierdzenia o obserwabli „matched projected TT sidebands `S_(p,s)` … `−(d_N/2)[u_m − g_m]`”.
  Publiczny tekst nie definiuje normalizacji szablonu `S_(p,s)`. Część `⟨H_p,(U−S)H_p⟩ = 0`
  zachodzi trywialnie, bo wynik żyje tylko we wstęgach `p±1`, co potwierdza siatka.
- Helpera źródłowego `deepseek_python_20260627_a87249.py` ani ZIP autora. Moja siatka to
  rekonstrukcja z opisu, nie kod źródłowy.
- Związku z fizyką (J3/K, GR) — autor też go nie twierdzi.

## Odtworzenie

```text
pip install numpy==2.1.3 sympy==1.13.3 mpmath==1.3.0
python3 research/badacz/2026-10-27/code/geeky_s11_rot027_logmean_check.py --out <katalog>
```

Około 2 s. Wszystkie pola `verdict` mają wartość `true`. Dwa czyste uruchomienia dały identyczny
JSON.

**Mój błąd po drodze.** Pierwsza wersja testu nierówności liczyła w arytmetyce zmiennoprzecinkowej
z `m` do 400. Potęgi `a^m` wychodziły poza zakres, co dało 23 fałszywe „naruszenia” i fałszywy
błąd tożsamości `0.6`. Wadliwa była miara, nie twierdzenie: zastąpiłem ją arytmetyką dokładną i
mpmath. Do wyniku nie wliczałem pierwszej wersji.

`NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_CLAIM`. Audyt zewnętrzny wyniku
Claude'a: Grok (przez Moderatora).
