---
artifact_id: IW_BADACZ_WUXU_HEAVY_END_CLOCK_MANIFEST_20261111
exposure: PUBLIC
claim_ceiling: PROVENANCE_MANIFEST / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-11
origin_cell: BADACZ (wątek Claude)
document_type: MANIFEST
---

# SHA-256 — research/badacz/2026-11-11 (PREREG_056 / REVIEW_057)

Sprawdzenie: `grep -E '^[0-9a-f]{64}  ' data/MANIFEST_SHA256.md | sha256sum -c` z katalogu `research/badacz/2026-11-11`. Sterownik w wersji użytej do przebiegu produkcyjnego to commit `bdc8906`; wersja poniżej dodaje tylko przełącznik `BADACZ_TOL` (ścieżka domyślna bez zmian).

```text
68dc65049c7bcdb431b139a6ab3f1adef205b53b6c90ccb9e1b37128a5776874  code/wuxu_heavy_end_clock_record.jl
5802cf64e3ae4510ea7ecc3fe35d653cfe9aca66ac70c6afa18390b7612a39b0  code/wuxu_heavy_end_clock_analysis.py
ec0730b23e0f136c6dff5b734d9c2ff90d66ed5b06c0f5db76479b62333ea08d  data/heavy_end_clock.csv
34230ac8c99f2931074ace351251b4d6d63251e71633491cd81b78891d058d53  data/heavy_end_clock_analysis.json
```
