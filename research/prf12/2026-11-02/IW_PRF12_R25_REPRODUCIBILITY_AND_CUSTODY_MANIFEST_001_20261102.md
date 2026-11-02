---
artifact_id: IW_PRF12_R25_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: FULL_REPORT_BYTEWISE_GIT_READBACK_PASS / FULL_LOCAL_REPRO_PASS / INDEPENDENT_2X2_4X4_PASS / ZIP_CRC_PASS / MEMBER_SHA256_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_HARDWARE / NO_CANON / NO_EXEC / NO_NOVELTY / NO_ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE
---

# R25 — manifest źródeł, granice twierdzeń i odtwarzalność

**[Pełny raport naukowy R25](IW_PRF12_R25_AFFINE_T1_AND_FAST_RESET_IDENTIFIABILITY_LIMIT_001_20261102.md).**
Git blob SHA zweryfikowany wobec bajtów oryginału: \`89d9d4c60c5c353a0d5d6b666b020d5ea8bd8047\`.
Commit pierwotnego zapisu: \`8929f0faea82dc7e76326cf54bc4db2c44b3e5b6\`.

**[GitHub — samodzielny skrócony program NumPy/SciPy](IW_PRF12_R25_GITHUB_AFFINE_T1_AND_FAST_RESET_CORE_001_20261102.py)**, blob \`dbba2859234a884c87003827bc8d9bfe620bf261\`. Pełna lokalna wersja obejmuje wszystkie testy macierzowe i koncentracyjne; skrócony program ogranicza się do głównych równań i granic.

**Pełny archiwalny pakiet:** \`PRF12_R25_reproducibility_bundle_20261102.zip\`, 15871 bytes, SHA-256:
\`032911ba61e0b6e5d945626bab5264ddeb08ac8a24526acc3964afe87f617dd3\`.
Zawiera sześć plików (pełny raport, główny Python, niezależny Python, dwa logi i JSON manifest). CRC \`zipfile.testzip()\`: PASS. Porównanie bajtowe pełnej zawartości każdego elementu i SHA-256: PASS.

SHA-256 pełnych elementów:
- raport: \`1a4a52316275f511d259b79dc3db248a85fa1ab8cd2b55822bb5d8f4369ee16b\`;
- pełny Python: \`3e4480168efdff8ee9932a654b6e4a7d9f031c4d28060783c0430752fff8a1e0\`;
- niezależny Python: \`20f33ccc85ea8b9fbcc3b9fb7569c99fa56e72005bf8c204fa0b30936de0d2be\`;
- log główny: \`7db728f5658bf5a2e242d483eb2dbe7c47039b4965331b4fffe36453ce6c2868\`;
- log niezależny: \`360058d63cbb9392d8db3e46a0cda3434824bc41a884bfccd1ed060b6e87d17a\`;
- JSON manifest: \`7ab346232d0861202bfe650e790748ce59f9d3462f1e09f17363a55eb7f2af92\`.

Weryfikacja:
1. 101 niezależnych wartości m∈[-1,1] dla kanałów T1 Krausa i asymetrycznej macierzy assignment.
2. Siedem źródłowo różnorodnych ξ, wszystkie cztery kombinacje dwóch zapisanych znaków oraz niezależny pomiar B; identyczność kalibrowanego korelatora.
3. N par i nie-iid warunkowa granica Hoeffdinga, f=0 lub f=.31; szczególnie N=9516 dla lambda/gamma=.02, oraz N=11039 przy błędach kalibracji .0005.
4. Stabilność Cauchy'ego i dokładna równość fazowych przyrostów przy stroboskopowych resetach; obliczeniowa kontrola wzoru \`J4\` także przez niezależną kwadraturę.
5. Analityczna granica diamond dla źródła A_h przy ustalonym, ograniczonym niekomutującym sterowaniu; **nie** twierdzenie dla adaptacyjnych sterowań z nieograniczoną szybkością.

**Źródłowość:** R23 i R24 dostarczają poprzednio certyfikowane (a0,b0)=(.576,.526), geometrię sensora i no-reset contract; R25 wyprowadza affine readout inversion i nową kontrolę szybkich resetów. Wariant A_h *nie* spełnia założenia jednej ξ przez pełną parę. Brak pełnego kontraktu fizycznej detekcji. Brak niezależnego referee, rozstrzygnięcia nowości i BW readback. NO_CANON / NO_EXEC.

**Następny falsyfikator R26:** kalibracja c,d z ograniczonym skończonym zbiorem danych, dwustronne przedziały ufności nieoparte na deklarowanym δ, skuteczność alternatywnych funkcji wyniku przy tej samej liczbie shotów; sprawdzenie procesu A_h pod wybranymi ograniczonymi kształtami impulsów bez dopuszczania nowych źródeł informacji.
