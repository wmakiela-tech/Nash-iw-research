---
artifact_id: IW_BADACZ_WUXU_SUBEDGE_EXTRAPOLATION_NATIVE_ROOT_PREREG_060_20261111
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-11
document_type: PREREGISTRATION
responds_to: Mech-S8 ROT017 (p2 vs p12 extrapolation below 1e9 g, smooth flat extension); REVIEW_050 (band kernel); REVIEW_054/059 (A1); INT9 ROT012; MT15 ROT001
code: code/wuxu_subedge_ramp.jl (derived from 2026-11-08/code/wuxu_band_kernel.jl); code/wuxu_subedge_ramp_prediction.py
data: data/subedge_ramp060_prediction.json (prediction, computed before the run); data/configs_subedge060.dat
claim_ceiling: MODEL_INTERNAL / BRIDGE_TEST / NO_PBH_BOUND / NO_E4_UNBLOCK / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_060: o ile przesuwa się korzeń Fig. 5 przy innej ekstrapolacji poniżej 1e9 g i czy jądro pasm to przewiduje

**Rola:** Badacz. Most między Mech-S8 ROT017 a natywnym korzeniem β.

## Pytanie

- **Co robi kod autorów.** Kod autorów (`tool_script-hadrons_from_PBH.jl`) interpoluje `ln R_h` liniowo w `ln M` i poniżej pierwszego wiersza tabeli (1e9 g) przedłuża pierwszy odcinek. To wykładnik `p2_h`.
- **Co pokazał Mech-S8 ROT017.**
  - Wykładnik OLS z 12 pierwszych wierszy (`p12_h`), zakotwiczony w wierszu 1, daje stopę wyższą o 10.5–10.9% przy 3e8 g i o 21.1–21.8% przy 1e8 g.
  - Gładkie rozszerzenie płaskie w krawędzi zgadza się ze wszystkimi 100 wierszami przy dowolnym mnożniku `c`.
  - Tabela nie wyznacza więc stóp poniżej 1e9 g.
- **Pytanie natywne.** O ile przesuwa się korzeń `Y_C = 0.251` w log10 β przy wariancie p12? Oraz czy jądro pasm z REVIEW_050, zmierzone przy jednorodnym mnożniku w pasmie, przewiduje odpowiedź na mnożnik gładki i różny dla gatunków?

## Niezależne odtworzenie wykładników (z tabeli autorów)

- Źródło: blob `06d0883a`, SHA-256 `25411c26…199df`.
- Wartości:

| gatunek | p2 | p12 | dp |
|---|---|---|---|
| π± | 1.20049 | 1.28478 | 0.08429 |
| K± | 1.19665 | 1.27974 | 0.08309 |
| K⁰L | 1.19680 | 1.28011 | 0.08331 |
| p p̄ | 1.20429 | 1.28982 | 0.08553 |
| n n̄ | 1.20476 | 1.29040 | 0.08564 |

- Zgodne z zakresami w Mech-S8 ROT017. To sprawdzenie tej samej tabeli, nie audyt zewnętrzny.

## Wariant

- **Mnożnik.** Poniżej `m1 = 1e9 g` natywna stopa gatunku h jest mnożona przez `(M/m1)^(−λ·dp_h)`.
  - λ = 1 to wariant p12; λ = 0 to kod autorów.
  - Ruszane jest tylko pięć stóp hadronów. Prawo masy i wstrzykiwanie energii zostają bez zmian, tak jak w jądrze pasm.
- **Kontrola tożsamości (przed preregiem, wynik znany, efektu nie mówi).** Punkt j = 22, log10 β = −17.828, λ = 0, `BADACZ_TOL = 1e−4:1e−7`.
  - Nowy sterownik, stary sterownik i powtórzenie w jednym procesie dają ten sam `Y_C = 0.24718420969015406`, bit w bit.
  - Ten sam punkt w przebiegu 058 (inna maszyna, przed odzyskaniem kontenera) dał `0.24715182815744363`.
  - Kod jest więc deterministyczny na jednej maszynie, a nie między maszynami. Różnica `3.2e−5` w `Y_C` odpowiada ok. 0.005 dex korzenia.
  - To wyjaśnia dryf bazy między przebiegami (0.008 dex, REVIEW_054). Dlatego baza i wariant idą w jednej sesji.

## Przebieg

- **Konfiguracje.** `BADACZ_TOL = 1e−4:1e−7`, dwa procesy równolegle, ta sama maszyna (`data/configs_subedge060.dat`):
  - proces 1: `base22u` (λ = 0) i `ramp22` (λ = 1);
  - proces 2: `base28u` (λ = 0) i `ramp28` (λ = 1).
- **Pomiar.** Bracket, bisekcja do 0.02 dex, 7 punktów dopasowania, korzeń dopasowania, jak w REVIEW_050/054/059. Δ = korzeń(ramp) − korzeń(base) przy tym samym j.

## Przewidywanie (policzone przed przebiegiem; `data/subedge_ramp060_prediction.json`)

- **Formuła.** Jądro pasm REVIEW_050 (s_eff przy k = 2) i A1: `Δ = −log10(1 + Σ_b (k_b − 1) s_b)` dla pasm B (3e8–1e9 g), C (M_grid–3e8 g) i D (< M_grid).
- **Skąd przedział.** Mnożnik rośnie monotonicznie ku małym masom, więc efektywne `k_b` leży między wartościami na brzegach pasma. Zakładam, że korzeń reaguje monotonicznie na wzrost stopy.
- **Pasmo D.** Ważę liczbą hadronów, bo całe pasmo D jest emitowane w ostatnich ~3e−4 s.
- **Koniec słaby:** brzeg górny, `s − SE`, najmniejsze dp. **Koniec silny:** brzeg dolny, `s + SE`, największe dp.

| j | Δ słaby | Δ silny | Δ centralny (diagnostyka) | okno preregu (± 0.010 dex) |
|---|---|---|---|---|
| 22 | −0.0197 | −0.0651 | −0.0422 | [−0.0751, −0.0097] |
| 28 | −0.0078 | −0.0523 | −0.0295 | [−0.0623, +0.0022] |

- **Zapas 0.010 dex.** To największa zmiana Δ między tolerancjami w REVIEW_059. Okno dla j = 28 obejmuje zero, więc j = 28 nie odróżnia efektu od braku efektu; służy tylko do testu jądra.

## Kryteria (zapisane przed przebiegiem)

- **P1 (j = 22):** natywne Δ w [−0.0751, −0.0097] → PASS, czyli przedział z brzegów pasm wystarcza dla mnożników gładkich. Poza oknem → FAIL: jądra pasm nie wolno używać do mnożników niejednorodnych w pasmie, o czym powiadamiam komórki, które go używały (KN13, INT9, Mech-S8, REC11, AUD1, MT15).
- **P2 (j = 28):** natywne Δ w [−0.0623, +0.0022], z tą samą interpretacją.
- **Bez okna (wynik główny):**
  - natywne Δ przy j = 22 i 28 jako przesunięcie korzenia dla wariantu p12;
  - położenie `ℓ = (Δ − Δ_słaby)/(Δ_silny − Δ_słaby)` w przedziale, czyli gdzie w pasmach B i C leży odpowiedź;
  - SE dopasowania każdego korzenia, osobno od zapasu solvera (łatka `FIT_SE_AS_TOTAL_UNCERTAINTY`).
- **Uczciwość.** Nie znam żadnego punktu z λ = 1. Kontrola tożsamości dotyczy tylko λ = 0.

## Granice

- Wariant p12 to jedna z nieskończenie wielu krzywych zgodnych z tabelą (Mech-S8 ROT017, rozszerzenie płaskie z dowolnym `c`). Wynik nie jest więc granicą niepewności stóp i nie odblokowuje E4 (właściciel: Mech-S8).
- Wynik MODEL_INTERNAL, przy dwóch masach i tolerancji `1e−4`. Bez fizycznej granicy PBH.
