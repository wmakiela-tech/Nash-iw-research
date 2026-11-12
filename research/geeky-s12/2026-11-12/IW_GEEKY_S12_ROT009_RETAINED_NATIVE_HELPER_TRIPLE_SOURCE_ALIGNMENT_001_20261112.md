---
artifact_id: IW_GEEKY_S12_ROT009_RETAINED_NATIVE_HELPER_TRIPLE_SOURCE_ALIGNMENT_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
date: 2026-11-12
exposure: PUBLIC
science_status: AUTHOR_ACTUAL_NATIVE_SOURCE_FUNCTIONAL_REPLAY_PASS / ORIGINAL_INTERVAL_SOURCE_REGEN_NOT_RUN / INDEPENDENT_REFEREE_PENDING / M14_OWNER_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: M13_N41_AUXILIARY_FIVE_MASK_B / NO_HISTORIC_PRODUCER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT009 — trójdrożna kontrola źródła B z uruchomieniem zachowanego DTC0a 3D

## 1. Materialny rezultat

Właściwie URUCHOMIONO zachowany plik pomocniczy DTC0a dostarczony w projekcie, SHA256
23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
Import pliku nie zmienił żadnego bajtu źródła (hash sprawdzony PRZED wykonaniem). Oryginalne metody helpera generate_smooth_fields(41,2pi), compute_K_B na 41x41x41 punktach z centralnym stencil2, E_lin i faktycznym NumPy FFT P_TT zostały wywołane kolejno przy alpha=0,1,-1. Po odtworzeniu tensorów wielomianu K_B(alpha)=U+alpha V+alpha^2 W, wyliczono 25 współczynników quartic g_B,k(alpha)=RMS_mask(K_B(alpha))^2 dla masek k2–k6.

Trzy różne tory wejścia do tych samych 25 danych:
(A) original source M13 outward interval mpmath source quartics, frozen Git blob a6f50fbe5904e580e84c87ee87c5ad043cdec5d0;
(B) Geeky-S12 ROT008 indywidualnie zaimplementowany complex JS sparse Fourier + bezpośrednia skończona suma maski;
(C) NOWY rzeczywiście uruchomiony zachowany NumPy 3D finite-grid FFT TT helper.

**25/25 PASS functional NUMERIC.** Największa względna różnica (C) do źródła (A) = 1.541265343254236e-12; największa (C) do (B) = 9.176398812485076e-13. Maksymalna bezwzględna różnica C–A = 5.169878828456423e-26. Wszystkie są dużo poniżej zadeklarowanej coarse tolerance 1e-10. Największe względne rozbieżności przypadają na niewielkie współczynniki liniowe mask5/6; nie stanowią dowodu fizycznego.

Dodatkowy oryginalny kontrolny historyczny CSV z pakietu projektu, dtc0a_mask_sensitivity_N41_v0_3_1.csv, SHA256 4dc228e1edab9fefc219118b5ba465b817d86a934cfee4d5ae563657e3bd5f91, został osobno odczytany. Kwartyki helpera dają wszystkie **15/15** oryginalnych K_B_RMS dla alpha=0,.05,.2 i k2..k6, max relative RMS discrepancy 8.554885846708229e-16. Nie podstawiono historycznych RMS do helpera.

**Sufit:** To źródłowa zgodność funkcjonalna na poziomie NumPy Float64 z dwiema innymi drogami; nie ścisły certyfikat odtwarzania skierowanych 45-cyfrowych współczynników mpmath.iv. Historyczny oryginalny producent dtc0a_runtime_v0_3_1.py pozostaje niedostępny BYTE-EXACT. Żadnego fizycznego wniosku, nowej K/J3 lub nowości twierdzeń.

## 2. Firstness i odejmowanie dojrzałego hosta

M13 ROT23/32/33 FIRST odtworzył model i 99/99 historycznych RMS, M13 ROT35 geometrię pięciu rozłącznych powłok, ROT39/40 ścisłe wyniki A/C/B źródłowego modelu. Geeky-S12 ROT004–007 pierwsze ograniczone certyfikaty geometrii B najbliższej alternatywy, ROT008 pierwsza własna niezależna numeryczna rekonstrukcja JS źródłowych 25 współczynników i dwie negatywne zmiany modelu. Nowa wartość ROT009 to faktyczny THIRD-PATH 3D NumPy helper source execution and historical B local CSV check; nie przypisuje sobie matematyki M13 ani nie przenosi dowodów przedziałowych na historyczny niedostępny runtime.

Źródło original M13: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json

Źródło niezależne ROT008: https://github.com/wmakiela-tech/Nash-iw-research/blob/23b436252f0d49132d520c8e30b2b67b60fdb7b7/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT008_INDEPENDENT_B_SOURCE_CROSSRUN_25_COEFF_RESULTS_001_20261112.json

## 3. Reprodukcja i rzeczywiście uruchomione programy

Oryginalna metoda helpera wywołana bez zmiany kodu; Python3.13.5, NumPy2.3.5, pełne N41 3D. Pola C1=(.05sin x,.05cos y,0), C2=(.04cos z,0,.04sin x), ambient puretrace h=.1 sin x cos y I; original apply_E, lie_derivative_tensor, lie_bracket, apply_P_TT. Dla mask k użyto operatora średniej energetycznej (1/[6*(41-2k)^3]) SUM_vox SUM_ij Kij^2, czyli tej samej dokładnej definicji co M13 source-family, ale obliczonej na fizycznych tablicach 3D, nie analitycznych modach.

HARNESSES EXACTLY BYTE IDENTICAL to LOCALLY ACTUALLY RUN scripts, verified Git BLOB SHA against locally SHA1-computed blob, then GitHub READBACK full body:
- Native helper 3 alpha N41 run script, Git blob c54377e9ba122c16af0be08e6763faf4cb972b92, SHA256 24863a3c8f971bafc17c620c03ea8737a5d09d52efdb6a7b5c944b10986df504:
https://github.com/wmakiela-tech/Nash-iw-research/blob/14ad1de4ce4dd7303540b8bb5b33fdb16d016b74/research/geeky-s12/2026-11-12/geeky_s12_rot009_helper_native_replay.py
- Historical 15 RMS CSV crosscheck script, Git blob 10e8acdf1a0882f37b462457a0305c88b5a3e34b, SHA256 54f70cc573480e41c1c620580f916d83b9ca98435b6d3113c538180af935e8dc:
https://github.com/wmakiela-tech/Nash-iw-research/blob/f82fd7ede57988f6b922ce3293d0c6d53c92d4da/research/geeky-s12/2026-11-12/geeky_s12_rot009_historical_csv_crosscheck.py

Original local actual executed JSON:
- Native 3D coefficients: /mnt/data/geeky_s12_rot009_helper_native_3d_25_coeff_results.json, SHA256 08e14be14e8c3f2b70dd51061648c7ab82533fbe401ca09521b50f96390d617b;
- Historical 15 row B RMS comparison: /mnt/data/geeky_s12_rot009_historical_csv_results.json, SHA256 ae364cdeb580894b17b633d56a44fa9a0f260b57e746122c96bf7fa845745333.

PUBLIC full triple-source 25 rows, original M13 coefficient mid, ROT008 JS, native helper and discrepancy:
https://github.com/wmakiela-tech/Nash-iw-research/blob/3b59f127a45e24f4c907d7bf32a70d8e2c5ea0a6/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT009_DTC0A_RETAINED_HELPER_NATIVE_3D_TRIPLE_SOURCE_ALIGNMENT_RESULTS_001_20261112.json

The SHA-locked retained HELPER file itself has NOT been uploaded to public GitHub. User must supply the original separate project file locally for independent rerun. GitHub harness and local files together permit independent checks without claiming a standalone self-contained producer. The original high-precision M13 source_snapshot_ch.py from 2026-10-26 is not invoked; its required module verify_m13_rot33_interval.py lives in 2026-10-24 and requires an explicit import path as identified in ROT008. No false SOURCE_45DIGIT_INTERVAL_REGEN_PASS.

## 4. Scientific consequences, negative knowledge and status

The independent original-source replay does NOT change conclusions or firstness:
- ROT004 B universal ALL-delta nearest-only FAIL;
- ROT005 fixed B delta=.01 nearest-only PASS;
- ROT006 B 0<delta<=.020 PASS; delta=.026 FAIL;
- ROT007 B 0<delta<=.025 PASS, delta=.02514 FAIL, global source B 3-candidate reduction beta among legal {0,alpha-delta,alpha+delta};
- M13 A/C universal radial PASS retain firstness.
All these are conditional exact rational source coefficient interval mathematical statements, not yet independent referee accepted nor historic actual runtime identity.

As of 12 Nov evening, KN13 ROT018 explicitly references ROT007 only as SOURCE READ, not independent interval proof; no M14 adoption, independent REC11/AUD1 verifier, or BW custody confirmation for Geeky ROT004–009 identified in bounded Slack scan. BW unique-source event count corrections of KN13 do NOT automatically ingest our new source.

NO new toy-threshold refinement while waiting for independent interval referee; the useful progress here is independent execution against original locally available helper.

FINAL: HELPER_SHA256_PASS / ACTUAL_NATIVE_3D_SOURCE_RUN_PASS /
25_OF_25_TRIPLE_ALIGNMENT_PASS / 15_OF_15_HISTORICAL_RMS_PASS /
PUBLIC_EXECUTED_HARNESSES_BYTE_IDENTICAL_READBACK_PASS /
HISTORIC_PRODUCER_HOLD / SOURCE_45DIGIT_INTERVAL_REGEN_NOT_RUN /
REFEREE_PENDING / OWNER_ADOPTION_PENDING / BW_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
