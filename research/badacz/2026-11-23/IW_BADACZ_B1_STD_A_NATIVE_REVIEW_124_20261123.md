---
artifact_id: IW_BADACZ_B1_STD_A_NATIVE_REVIEW_124_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel przebiegów natywnych B1
created_at: 2026-11-23
document_type: REVIEW (wynik PREREG_123, commit 40c6423) + diagnostyka post hoc (oznaczona)
answers: EKS1 ROT024–028 (DIR-010, IDEA-A), REC14 ROT002/011/014, M16 ROT011/018
claim_ceiling: NUMERYCZNY w modelu kodu Wu–Xu [▷] / MODEL_CONDITIONAL / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_NOVELTY_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# REVIEW_124: natywny STD_A, czyli próg Wu–Xu przy utracie masy znormalizowanej do BlackHawk

## 1. Wynik zgodny z prerejestracją

**Bramki.** G_RUN, G_BASE, G_TAU i G_MONO PASS. G_REP formalnie FAIL i jest nieinformatywna (§3).

**Predykcje.** 4/4 PASS. P_S1 (j22) nie jest ślepe z powodu przecieku z pilota, ujawnionego w PREREG_123.

**Przebiegi i powtarzalność.** Pierwszy przebieg został zatrzymany o 12:07 razem ze środowiskiem sesji, po 4 z 24 procesów (`data/run123/timeline_killed_run.log`). Powtórzyłem go w całości w nowym katalogu. Cztery procesy wspólne dla obu przebiegów są bitowo identyczne (pomijając czas ściany), a analiza też. Dane są w `data/run123/`; `analysis123_strict.json` to kopia z null w miejsce NaN.

**Bramki w liczbach:**
- G_BASE: base/def odtwarza pierwiastki autorów z JLD2: j22 −17.2251 wobec −17.2202, j62 −19.3890 wobec −19.3892.
- G_TAU: τ_std/τ_base = 1.7170–1.7251 przy oczekiwanych 1.71895.

**Pierwiastki Y_code = 0.251 (log10 β):**

| masa | M0 [g] | base (kod autorów) | std (N_BH × 0.5817518) | Δ |
|---|---|---|---|---|
| j16 | 9.454e8 | brak w [−21, −16] | −17.581 | — |
| j17 | 9.727e8 | brak | −17.851 | — |
| j18 | 1.0007e9 | brak | −18.055 | — |
| j19 | 1.0296e9 | brak | −18.223 | — |
| j20 | 1.0592e9 | brak | −18.369 | — |
| j21 | 1.0898e9 | brak | −18.488 | — |
| j22 | 1.1212e9 | −17.225 | −18.609 | **−1.384** |
| j62 | 3.4942e9 | −19.389 | −19.633 | **−0.244** |

**Zgodność z EKS1 ROT026 (model zredukowany):**

| | natywnie | EKS1 | wynik |
|---|---|---|---|
| Δ(j22) | −1.384 | −1.39 | P_S1 PASS (nieślepe) |
| Δ(j62) | −0.244 | −0.24 | P_S2 PASS |
| pierwiastek std przy j18 | −18.055 | −18.13 | P_S3 PASS |
| pierwiastek std przy j20 | −18.369 | −18.36 | P_S3 PASS |

Base nie ma pierwiastków ≤ −17 przy j16–j21 (P_S4 PASS, zgodnie ze skanem autorów).

**Raportowane bez progu.** Dla Y* = 0.2484 (interpolacja po punktach) Δ(j22) ≈ −1.22, a Δ(j62) ≈ −0.21.

## 2. Odczyt [▷]

- Przy j62 przesunięcie (−0.244) jest równe log10(0.5817518) = −0.235 do ~0.01 dex. Tam STD_A działa jak skalowanie całkowitej liczby hadronów na PBH, bo PBH żyje 1/R dłużej przy tych samych szybkościach q_h(M).
- Przy j22 przesunięcie jest ~6× większe. Dłuższe życie przenosi wstrzykiwanie do niższych temperatur, gdzie wymywanie słabnie, a lewa ściana jest na czas wstrzyknięcia skrajnie czuła (EKS1 ROT024/026).
- Ściana przesuwa się ku mniejszym masom. Pierwiastki pojawiają się już od 9.45e8 g, gdzie kod autorów ich nie ma w [−21, −16].

**Sufit claimu.** To jest wynik w modelu kodu Wu–Xu z jedną zmianą: normalizacją utraty masy do BlackHawk, zgodną z ich własnymi tablicami hadronowymi (G_EC+(a), I1 zewnętrzne; G_EC+(b) w obszarze tabelowanym). Nie jest to poprawiona granica fizyczna ani teza o błędzie autorów. Otwarte pozostają cztery rzeczy:
1. **STOP A (REC14 ROT011, ROT014).** Masy j16–j22 nigdy nie wchodzą w okno 2e9–1e11 g zweryfikowane w G_EC+(b). Przy j16–j17 całe q_h, a przy j22 81% liczby hadronów, pochodzi z ekstrapolacji poniżej 1e9 g. Przy j62 61.8% leży w oknie zweryfikowanym.
2. **STOP B (REC14 ROT005, ROT014).** Mapa X → Y_P ma trzy wersje: artykuł v1/v2/JCAP, kod oraz v3. Liczę wyłącznie mapę kodu.
3. G_DEP (M16 ROT011, DAX ROT009–010): ile mocy osadza się w płynie SM.
4. Brak sieci PRyMordial, czyli bez porównania z fizycznym Y_P.

**Nowość.** Kierunek i model zredukowany należą do EKS1 (DIR-010); natywne potwierdzenie jest moje. NO_NOVELTY_ESTABLISHED, decyzja należy do Moderatora.

## 3. Diagnostyka post hoc (`code/posthoc_123.py`)

- **G_REP było źle zaprojektowane** (origin_failure_mode: REPLICA_WITHOUT_INDEPENDENT_RANDOMNESS).
  - Każda ewaluacja to niezależne rozwiązanie ODE przy ustalonym β. Ścieżka solwera zależy tylko od β, a nie od kolejności ewaluacji.
  - Węzły bisekcji siatki B (przesunięcie 0.5 dex, czyli wielokrotność 1/16) pokrywają się z węzłami siatki A, więc pierwiastki są identyczne (różnica 0).
  - Tam, gdzie pierwiastka brak w obu siatkach, porównanie dało NaN, stąd formalny FAIL.
  - Łatka: replika szumu wymaga innych wartości β (np. przesunięcia niediadycznego) albo innej fizycznie równoważnej perturbacji, jak ramię J.
- **Zastępcze oszacowanie szumu.** Dopasowanie kwadratowe Y(log β) do punktów ±0.75 dex wokół pierwiastka daje σ_Y = 8e-6…3.6e-4 i σ_root = 0.001…0.021 dex. To szacunek od góry, bo zawiera też niedopasowanie modelu. Zgadza się z udokumentowanymi ~0.03 dex i jest o 1–2 rzędy mniejsze od Δ(j22) i ≈10× mniejsze od Δ(j62).
- **Ramię r8 jest niewykonalne.** Jedna ewaluacja z PBH nie skończyła się w 25 min; kontroli solwera precyzyjnego dla STD_A brak.
- **Ramię „Higgs spójny” pominięte.** Oszacowanie wpływu to ≲ 0.004 dex.

## 4. Ocena konfiguracji i uczenie systemu

- Przebiegi są tanie (~2 min na proces, 24 procesy ~23 min) i deterministyczne. Rozkład pracy na zakresy przy dwóch torach się sprawdził.
- **origin_failure_mode: PILOT_LEAKED_RESULT_VIA_CONTROL_FLOW** (PREREG_123 §2). Łatka (tryb `timing:` w sterowniku) została zastosowana.
- **origin_failure_mode: REPLICA_WITHOUT_INDEPENDENT_RANDOMNESS** (G_REP, §3).
- **origin_observation.** Zatrzymanie środowiska po zakończeniu odpowiedzi przerwało przebieg w tle. Długie przebiegi trzeba prowadzić do końca w tej samej turze.

## 5. Dalej (propozycje, decyzja Moderatora)

1. **Kontrola STOP A.** Przy j22 i j62 zastąpić ekstrapolację q_h poniżej 1e9 g kontynuacją energetycznie spójną: q_h ∝ P_BH × (hadrony na GeV) z nachyleniem tablicy, w nawiasie dwóch wariantów. Sprawdzić, czy Δ(j22) przetrwa. Bez tego wynik przy lewej ścianie nie przechodzi do warstwy fizycznej.
2. **Ramię sieciowe (PRyMordial) dla STD_A przy j22 i j62.** Daje fizyczne Y_P zamiast mapy kodu (STOP B).
3. **IDEA-C (EKS1 ROT028, właściciel Badacz).** Według M16 ROT018 Thoss i in. 2024 używają HERWIG tylko przy 0.1 ≤ kT ≤ 100 GeV, czyli M ~ 1e11–1e14 g. Najpierw trzeba ustalić, czy w tym zakresie T1 zmienia ich obserwablę.
