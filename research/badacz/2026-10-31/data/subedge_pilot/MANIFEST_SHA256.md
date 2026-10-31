---
artifact_id: IW_BADACZ_WUXU_SUBEDGE_PILOT_MANIFEST_SHA256_20261031
exposure: PUBLIC
claim_ceiling: PROVENANCE_MANIFEST / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-31
origin_cell: BADACZ (wątek Claude)
document_type: MANIFEST
---

# MANIFEST SHA-256: PREREG_041 / REVIEW_042 (Badacz, 31 X 2026)

Ścieżki są względem `research/badacz/2026-10-31/`. Dane wejściowe z wcześniejszych przebiegów
(`data/native_audit/e2_native.csv`, `e2_ols8.csv`) są ujęte w `data/native_audit/MANIFEST_SHA256.md`.
Sterownik v1 (`code/wuxu_subedge_variant_boundary.jl`) pozostaje bez zmian; v2 dodaje warianty `p13` i `pyt`
oraz unikalne nazwy plików tymczasowych.

Sprawdzenie: skopiuj blok do pliku i uruchom `sha256sum -c <plik>` w `research/badacz/2026-10-31/`.

```text
db1eaf8c30e812a39b6aaf85020df1140f84841fbfdfe9d0069fda2c61c81853  code/wuxu_subedge_variant_boundary_v2.jl
78360b6eb95ab204498914a98c14d351cbc6a15b2d28fb66df920ade7ab7be84  code/wuxu_pythia_multiplicity_pilot.py
66230a570d630c9bc2bce0e2530d1a3e488988c24e45e8361673670448fc5b3f  code/wuxu_table_edge_slope_posthoc.py
e52cd96dec8844bfd0da21e81849db152b5f5c02aee475adf4bf9481d7519239  code/wuxu_prereg041_analysis.py
e8354e53faaa5a23ea82dc695e9b7bc041c2333f7b0396a006e208d313a2abaf  data/subedge_pilot/RUNLOG.md
85487b34d4dcb58b9a4d58dd44b08c9b477beb88e41868f7354631aa1b6e2667  data/subedge_pilot/e2_p13.csv
f2e3b542c27e9f0267ac61cb20777b875ba7aa881917b126b0c1024371141888  data/subedge_pilot/prereg041_analysis.json
092eee9ef202d0369e7e6fe12eb5ca416f16965f651cc80e054b237eaf411604  data/subedge_pilot/pythia_multiplicities.csv
3a611c80f27f21cbaa0d6199d60589a91d3be534f9e8445f54a643f476565a7d  data/subedge_pilot/pythia_pilot.json
3d99b9e8ad34278f6132d39c6bcc1300cdc567f2bbfb89b43e93e3e6b43f7868  data/subedge_pilot/pythia_rate_table.csv
4b60b9d2bdebdc78775b7e89e9d31d420881dc7e88ba1be1be43b5c6ce4acfbe  data/subedge_pilot/table_edge_posthoc.json
22f1fc329e33c07e390823306d923c4e860a45a3b7a197a11f1dc63a5057129a  data/subedge_pilot/v2check2_native.csv
a1a5c881047da45003be11868897a295af5724664247f620566d8d0e442b14ab  data/subedge_pilot/v2check2_p13.csv
```

Źródła zewnętrzne: `hadrons_from_PBH.dat` (blob `06d0883a27b108692720422294ba2baacd381a64`) przy commicie autorów
`d395183674cace6c9906a8911bdeb7234ba4040d`; PYTHIA 8.318.3 (`pythia8mc`, PyPI).
