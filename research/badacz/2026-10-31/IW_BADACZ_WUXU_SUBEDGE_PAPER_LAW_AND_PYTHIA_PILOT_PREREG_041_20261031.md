---
artifact_id: IW_BADACZ_WUXU_SUBEDGE_PAPER_LAW_AND_PYTHIA_PILOT_PREREG_041_20261031
exposure: PUBLIC
claim_ceiling: PREREGISTRATION / TESTS_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: PREREG
task_id: BADACZ-FRONTB-SUBEDGE-STRESS-002
owner_of_physics: Mech-S7 (E4 zaproponowane właścicielowi 31 X); to jest pilotaż wspierający jego decyzję, nie przejęcie E4
---

# Preregistracja: prawo z tekstu autorów poniżej `1e9 g` (V3) i pilotaż PYTHIA dla krotności hadronów (E4-lite)

## Kontekst (stan przed przebiegami)

- **Tekst autorów (arXiv:2509.05618, Eq. 4.4–4.5, czytany 31 X):**
  - poniżej `1e9 g` używają wzoru analitycznego `dN/dt ∝ T_BH^{1.3}`, przeskalowanego tak, by zgadzał się
    z BlackHawk przy `1e9 g`;
  - wykładnik pochodzi z `N(E) ∝ E^{0.3}`, uzyskanego „running PYTHIA (v8) independently of BlackHawk”;
  - BlackHawk nie jest używany poniżej `1e9 g` z powodu limitu energii partonu `1e5 GeV`.
- **Kod autorów** ekstrapoluje natomiast z dwóch pierwszych wierszy tabeli (`s ≈ −1.20`). Rozbieżność
  tekstu i kodu opisał Rec9, 18 X. Jej skutku na konturze nikt jeszcze nie zmierzył.
- **Moje E2 (REVIEW_038):** nachylenie OLS-8 (`≈ −1.27`) przesuwa granicę o `−0.02…−0.04 dex` przy
  `m ≤ 1.58e9 g`. Wyzerowanie emisji poniżej krawędzi usuwa lewą ścianę.
- **Test dymny PYTHIA** (5 zdarzeń, para `uū` po `1e4 GeV`): sprawdzona tylko mechanika i czas
  (`~3 ms`/zdarzenie). Krotności nie analizowałem.

## A. V3: prawo z tekstu autorów

- **Wariant `p13`:** `Q_i(m) = Q_i(m₁)·(m/m₁)^{−1.3}` dla `m < m₁ = 1e9 g`, dla wszystkich pięciu kolumn. Ten
  sam sterownik i bisekcja co E2, 12 mas.
- **Przewidywanie:** wzmocnienie ograniczenia o `0.02–0.06 dex` przy `m ≤ 1.58e9 g`; `|przesunięcie| ≤ 0.01`
  dla `m ≥ 2.0e9 g`.
- **Falsyfikatory:** przesunięcie dodatnie `> 0.03` w którejkolwiek masie `≤ 1.58e9 g` albo
  `|przesunięcie| > 0.1` gdziekolwiek.

## B. Pilotaż PYTHIA (E4-lite, tylko fragmentacja SM)

### Procedura

- **Generator:** PYTHIA 8.318 (`pythia8mc` z PyPI), `ProcessLevel:all = off`.
- **Pary partonów:** `qq̄` i `gg` wstawione w rekord zdarzenia jako para tyłem do siebie, kaskada
  `forceTimeShower`, potem hadronizacja.
  - Kwarki: `u, d, s, c, b`, po 80 zdarzeń na zapach (razem 400).
  - Gluony: 400 zdarzeń.
  - Ziarno ustalone.
- **Energia na parton:** `E = 1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000 TeV`.
- **Liczenie:** w stanie końcowym `π±`, `K±`, `K⁰_L`, `p + p̄`, `n + n̄`, na parton. Stabilne: `π±`, `K±`,
  `K⁰_L`, `n`, `μ`; reszta rozpada się domyślnie.
- **`δ(E)`:** lokalny wykładnik `d ln n/d ln E` z sąsiednich energii.
- **Splot z widmem Hawkinga:**
  - `⟨n⟩_T = ∫x² f(x) n(xT) dx / ∫x² f(x) dx`, gdzie `f = 1/(eˣ ± 1)` (fermiony/bozony). Przybliżenie
    optyki geometrycznej: bez współczynników szarości zależnych od spinu.
  - `n(E)`: interpolacja log-log; poza siatką ekstrapolacja ostatnim nachyleniem.
  - Tempo: `R_i(T) ∝ T·[w_q⟨n_{i,q}⟩_T + w_g⟨n_{i,g}⟩_T]`, gdzie `w_q = 72·1.5ζ(3)` i `w_g = 16·2ζ(3)`.
  - Nachylenie: `s_i(T) = d ln R_i/d ln m = −d ln R_i/d ln T`.
  - `T_BH = 1.058e13 GeV·(1 g/m)`, czyli `T₁ = 10.58 TeV` przy `1e9 g`.
- **Pominięte:** pierwotne `t`, `W`, `Z`, `H`; współczynniki szarości; stopnie swobody spoza SM.

### Bramka walidacyjna (warunek uruchomienia C)

- **B1:** `δ` dżetu kwarkowego między 10 a 100 TeV mieści się w `[0.15, 0.45]` (autorzy: `0.3`).
- **B2:** `s_π(T₁)` z modelu mieści się w `±0.10` od nachylenia tabeli przy krawędzi (`−1.20`).
- Jeśli B1 albo B2 nie przejdzie, pilotaż nie jest dość wierny. C nie uruchamiam; raportuję B.

### Przewidywanie B

- `δ` maleje z energią (krotność QCD rośnie wolniej niż potęgowo): `δ(10–30 PeV) < δ(10–30 TeV)`;
- `|s_π(1 PeV)| < |s_π(10 TeV)|`.

**Falsyfikatory:** `δ` rosnące z energią albo poza `[0.1, 0.5]` w którymkolwiek przedziale.

## C. Wariant natywny `pyt` (tylko jeśli B1 i B2 przejdą)

- `Q_i(m) = Q_i(m₁)·R_i(T(m))/R_i(T₁)` dla `m < m₁`, z `R_i` z punktu B (tabela w CSV, interpolacja
  log-log). Ten sam sterownik i bisekcja, 12 mas.
- **Przewidywanie:** `|przesunięcie| ≤ 0.05 dex` wszędzie; na lewej ścianie słabsze ograniczenie
  (`0…+0.04`), jeśli `|s|` poniżej krawędzi jest mniejsze niż `1.2`.
- **Falsyfikator:** `|przesunięcie| > 0.1` w którejkolwiek masie.

## Granice wniosku

- To nie jest walidacja fizycznego widma (E4 pozostaje u Mech-S7): brak współczynników szarości,
  pierwotnych bozonów ciężkich i fizyki spoza SM.
- Szum metody na granicy to około `0.01 dex` (REVIEW_035/038).
- Werdykt każdego testu ogłaszam niezależnie od kierunku. Wynik jest Claude'a i wymaga audytu spoza rodziny
  Claude.
