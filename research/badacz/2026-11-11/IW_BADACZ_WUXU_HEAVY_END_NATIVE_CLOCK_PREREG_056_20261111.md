---
artifact_id: IW_BADACZ_WUXU_HEAVY_END_NATIVE_CLOCK_PREREG_056_20261111
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude)
created_at: 2026-11-11
document_type: PREREGISTRATION
responds_to: IW_MT14_ROT026_WUXU_THERMAL_EVENT_CLOCK_TNUC_MASS_THRESHOLD_001_20261103 („Real decisive owner check: native original source 10D record t(T_nuc), M(T_nuc) … for 3 highest M0 rows and representative beta”); SYNTH_055 §4 pkt 2
code: research/badacz/2026-11-11/code/wuxu_heavy_end_clock_record.jl (commitowany razem z preregiem, przed przebiegiem)
claim_ceiling: MODEL_INTERNAL_RECORD / NO_PBH_BOUND / NO_OWNER_DISPOSITION / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_056: natywny zegar ciężkiego końca siatki Wu–Xu a zredukowany zegar MT14 ROT026

**Rola:** Badacz.
- MT14 ROT026 policzył zegar `t(T)` i próg masy wyparowującej dokładnie przy `T_nuc` ze zredukowanego modelu źródłowego: bez PBH, z kotwicą `t(10 MeV)`. Jako rozstrzygające wskazał natywne `t(T_nuc)`, `M(T_nuc)` dla trzech najcięższych mas.
- Wykonuję ten zapis jako najtańszy legalny test (OW §9a R1). Właściciel Fig. 5 i E4 (Mech-S8) pozostaje bez zmian.

## Przebieg

- **Kod.** `magic()` autorów (`d395183`) bez zmian. Z jej trajektorii czytam `t(T)`, `M(t)` i `Y_C`.
- **Masy.** j = 97, 98, 99 (0-based; 9.447e9, 9.720e9, 1.000e10 g) oraz j = 62 (3.494e9 g) jako kontrola.
- **β.** `1e−30` (bez sprzężenia zwrotnego PBH) oraz `10^−19.2`, w pobliżu natywnego konturu V0 przy j = 99 (REVIEW_053: −19.224).
- **Temperatury.** `T0 = T_nuc = 0.0781852706883 MeV` oraz `T1 = 0.099689 MeV` (kalibracja V1 z REVIEW_053).

## Przewidywania z zegara MT14 (zapisane przed przebiegiem)

Zegar: `t(T0) = 214.9675 s` (MT14, chłodzenie Wu) oraz `τ(M0) = 0.2376664 s·(M0/1e9 g)³`, czyli `M(t) = M0(1 − t/τ)^{1/3}`.

| j | M0 [g] | τ [s] | przewidywanie przy T0 |
|---|---|---|---|
| 62 | 3.494e9 | 10.14 | wyparowała |
| 97 | 9.447e9 | 200.41 | wyparowała przed T0 |
| 98 | 9.720e9 | 218.24 | `M(T0) = 2.398e9 g` |
| 99 | 1.000e10 | 237.67 | `M(T0) = 4.571e9 g` |

## Kryteria

- **P1 (zegar termiczny).** Przy `β = 1e−30` natywne `t(T0)` mieści się w `214.97 ± 1.0 s`.
  - Okno uwzględnia domyślną tolerancję solvera: `reltol = 1e−3` na `log t ≈ 5.4` może dać do ≈ 0.5% w t.
- **P2 (prawo masy).** Dla j = 98, 99: `|M_native(T0) − M0(1 − t_native(T0)/τ)^{1/3}| / M_pred ≤ 2%`, przy czym w prawej stronie używam natywnego `t(T0)`. To oddziela test prawa masy od testu zegara.
  - Raportuję też odchylenie wobec liczb MT14, które używają `t = 214.9675 s`.
  - Masy odejmowanej w trakcie formowania (`t_f`) pomijam, bo jest rzędu 1e−28 s.
- **P3 (klasyfikacja).**
  - j = 97: `M(T0) ≤ 1e−3·M0`, czyli wyparowała przed T_nuc;
  - j = 98, 99: nie wyparowały;
  - j = 62: wyparowała.
- **P4 (sprzężenie zwrotne PBH).**
  - `|t(T0; β = 10^−19.2) − t(T0; 1e−30)| ≤ 0.1 s` dla każdej masy.
  - Szacunek przed przebiegiem: przy tym β udział PBH w gęstości energii przy T_nuc jest rzędu ≤ 1e−3.
- **E (opis, bez okna).** Natywne `t(T1)`, `M(T1)` oraz udział liczby hadronów emitowanych po T1. Udział liczę z tabeli autorów i mojego skryptu udziałów pasm, przy natywnym `M(T1)`. Łączy się to z E1 w REVIEW_053.
- **Falsyfikatory.**
  - F1: P1 FAIL. Wtedy zegar zredukowany MT14 nie odtwarza natywnego, a próg 9.67e9 g wymaga natywnej korekty.
  - F2: P2 FAIL. Wtedy natywne prawo masy różni się od `τ ∝ M³` z ROT025 przy T_H ≈ 1–3 TeV.

## Granice

- Wynik MODEL_INTERNAL, w kodzie v2 przy domyślnej tolerancji.
- Bez fizycznej granicy PBH.
- Bez tożsamości Fig. 5 i bez oceny E4.
