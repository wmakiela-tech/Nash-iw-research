---
artifact_id: IW_BADACZ_MANIFEST_SHA256_128_20261125
exposure: PUBLIC
document_type: MANIFEST
claim_ceiling: CUSTODY_ONLY
sync_state: GITHUB_PENDING_BW_INGEST
---

# MANIFEST SHA-256 (Badacz, 2026-11-25)

## 128 (triage STOP A + errata; jedyne obliczenie: oszacowanie pokrycia w Pythonie, bez Julii)

Pliki: raport 128, kod `code/coverage_estimate_128.py` (python3 -I, argument: ścieżka wyjścia JSON), wynik `data/coverage_estimate_128.json`. Odtworzenie: `python3 -I code/coverage_estimate_128.py data/coverage_estimate_128.json`, następnie porównanie skrótów poniżej.
```
bd0d0840c7d04544c327eba87f1da9a9d4379192cbf30d21eaacc7068f0706da  IW_BADACZ_B1_STOPA_SOURCE_FEASIBILITY_AND_ERRATA_128_20261125.md
ce7b8f320f719c45488323b382325c910d7645cfa4d2a095ef79c64a7e986357  code/coverage_estimate_128.py
eb7975351b8a4baa8105f9bda46d3d2dac9627b2c9b6ed848e551dbc7e043e63  data/coverage_estimate_128.json
```
