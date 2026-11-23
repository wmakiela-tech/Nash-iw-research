---
artifact_id: IW_BADACZ_B1_STD_A_NATIVE_PREREG_123_20261123
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel przebiegów natywnych B1
created_at: 2026-11-23
document_type: PREREGISTRATION (zamrożona przed przebiegami; ujawniony przeciek z pilota, §2)
authorization: Moderator 23 XI 09:22 („Najpierw A”: tło + G_EC+, potem STD_A), rotacja „O” 11:29; stała autoryzacja 21 XI 16:05
answers: EKS1 ROT024–027 (DIR-010, STD_A), REC14 ROT002, M16 ROT011
claim_ceiling: NUMERYCZNY w modelu kodu Wu–Xu [▷] / NO_PBH_BOUND / NO_AUTHOR_ERROR_ESTABLISHED / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_123: natywny STD_A, czyli kod Wu–Xu z utratą masy znormalizowaną do BlackHawk

## 1. Cel

G_EC+(a) (REVIEW_120; I1: DAX ROT007, M16 ROT011) ustaliło, że kod traci masę 1/0.5817518 = 1.719× szybciej niż BlackHawk v2.3. G_EC+(b) (REVIEW_122) ustaliło, że w obszarze tabelowanym tablica hadronowa jest spójna z emisją BlackHawk do ~1%.

STD_A zmienia w kodzie autorów tylko linię 80:
`d_m_PBH_dt = -N_PBH * NU.m_Pl^4 / m_PBH^2` → `d_m_PBH_dt = -0.5817518 * N_PBH * NU.m_Pl^4 / m_PBH^2`.
- Źródło hadronowe q_h(M) zostaje bez zmian (M16 ROT011).
- Ogrzewanie korzysta z tego samego d_m_PBH_dt, więc energia zdeponowana na jedną PBH się nie zmienia, zmienia się tylko jej rozkład w czasie.

Pytanie: o ile przesuwa się próg β autorów, liczony jako Y_code = 0.251, czyli górny brzeg χ² = 4 przy mapie Y kodu. Odniesieniem są przewidywania EKS1 ROT026 z modelu zredukowanego.

## 2. Ujawnienie wiedzy przed zamrożeniem

- **Przeciek z pilota (origin_failure_mode: PILOT_LEAKED_RESULT_VIA_CONTROL_FLOW).** Pilot czasowy std/def/j22 wyciął kolumnę Y, ale wypisał ciąg punktów bisekcji (−18.5, −18.75, −18.625, −18.5625). Ten ciąg koduje wynik: pierwiastek std przy j22 leży w (−18.625, −18.5). P_S1 (j22) nie jest więc ślepe i oznaczam je NONBLIND. Pozostałe predykcje są ślepe.
  - Łatka: piloty wyłącznie w trybie `timing:<lb>`, czyli jedna ewaluacja, bez punktów i bez Y (dodany do sterownika).
- **Pilot r8 (`timing:-19`, std, j62)** nie skończył jednej ewaluacji w 25 min. Ramię r8 z PBH jest niewykonalne w tej sesji.
  - Zamiast niego kontrola szumu solwera przez replikę ścieżki: druga siatka zgrubna przesunięta o +0.5 dex daje inną ścieżkę solwera i bisekcji.
  - Udokumentowany szum progu solwera autorów wynosi ~0.03 dex. Spodziewane efekty to 0.2–1.4 dex.
- Znane wcześniej: pierwiastki autorów z JLD2 (j22 −17.2202, j62 −19.3892; EKS1 ROT016, REC13 ROT017) oraz brak przecięć w [−20, −17] dla mas poniżej j22 w skanie autorów.

## 3. Ramiona i siatka (`code/std_a_123.jl`, `code/run123.sh`)

| | |
|---|---|
| ramiona | base (kod autorów), std (N_BH × 0.5817518); solwer autorów (def) |
| masy | j16–j22 (9.45e8–1.121e9 g, lewa ściana) i j62 (3.494e9 g) |
| siatka A | log10 β ∈ {−21, −20, −19, −18, −17, −16}; najniższe przecięcie w górę; 4 bisekcje; interpolacja liniowa w końcowym przedziale (1/16 dex) |
| siatka B (replika) | {−20.5, …, −15.5}, ta sama procedura; dla j18, j20, j22, j62 |
| tablica | `hadrons_from_PBH.dat` autorów (d395183), T_nuc ustalone, mapa Y kodu |

Bez sieci PRyMordial: obserwablą jest Y kodu autorów. Ramienia „Higgs spójny” nie liczę: jego oczekiwany efekt, 0.4–0.9% liczby hadronów, czyli ≲ 0.004 dex, leży poniżej szumu 0.03 dex. Podaję go tylko jako oszacowanie.

## 4. Bramki i predykcje (`code/analysis_123.py`)

**Bramki:**
- G_RUN: wszystkie ewaluacje z retcode Success.
- G_BASE: pierwiastek base/def przy j22 i j62 zgodny z JLD2 autorów do ±0.05 dex.
- G_TAU: τ_std/τ_base = 1/0.5817518 = 1.71895 z dokładnością do 1% przy każdej masie. Czas zatrzymania mierzony bisekcją na rozwiązaniu gęstym.
- G_MONO: Y na siatce zgrubnej niemalejące z tolerancją 3e-4.
- G_REP: |pierwiastek_A − pierwiastek_B| ≤ 0.05 dex dla 8 par masa–ramię.

**Predykcje:** odniesienie to EKS1 ROT026 (model zredukowany, τ = 407 s, tablica bez zmian, próg 0.251, przesunięcia względem bazy Wu–Xu).

| id | wielkość | odniesienie | tolerancja | ślepa? |
|---|---|---|---|---|
| P_S1 | Δ(j22) = r_std − r_base | −1.39 | ±0.20 | NIE (przeciek) |
| P_S2 | Δ(j62) | −0.24 | ±0.10 | tak |
| P_S3 | pierwiastki std przy j18 i j20 istnieją | −18.13 i −18.36 | ±0.25 | tak |
| P_S4 | base przy j16–j21 bez pierwiastka ≤ −17 | skan autorów | — | spójność |

Raportowane bez progu:
- pierwiastki i przesunięcia dla wszystkich 8 mas;
- pierwiastki dla Y* = 0.2484 (interpolacja liniowa po wszystkich punktach);
- czasy życia.

## 5. Interpretacja (ustalona przed przebiegiem)

- **P_S2 i P_S3 PASS.** Natywny kod potwierdza model zredukowany EKS1. Przy energetycznie spójnej utracie masy próg Wu–Xu przy lewej ścianie przesuwa się o rząd 1 dex, a ściana przesuwa się ku mniejszym masom. To byłby największy efekt w B1, ale zależny od modelu:
  - poniżej 1e9 g q_h jest ekstrapolowane i nieskontrolowane energetycznie;
  - G_DEP pozostaje otwarta;
  - bez sieci PRyMordial;
  - to jedna zmiana w kodzie, a nie poprawiona granica.
- **FAIL.** Model zredukowany źle przenosi zmianę czasu życia; raportuję natywne wartości.
- Nic tutaj nie jest tezą o błędzie autorów. Normalizacja geometryczno-optyczna (N_BH = 27N_ρ/(4·30720π)) to ich przybliżenie modelowe; mierzę jego wpływ.
