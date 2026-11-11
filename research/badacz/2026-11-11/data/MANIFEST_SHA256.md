---
artifact_id: IW_BADACZ_WUXU_HEAVY_END_CLOCK_MANIFEST_20261111
exposure: PUBLIC
claim_ceiling: PROVENANCE_MANIFEST / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-11-11
origin_cell: BADACZ (wątek Claude)
document_type: MANIFEST
---

# SHA-256 — research/badacz/2026-11-11 (PREREG_056 / REVIEW_057 r2; PREREG_058 / REVIEW_059)

Sprawdzenie: `grep -E '^[0-9a-f]{64}  ' data/MANIFEST_SHA256.md | sha256sum -c` z katalogu `research/badacz/2026-11-11`. Sterownik w wersji użytej do przebiegu produkcyjnego to commit `bdc8906`; wersja poniżej dodaje tylko przełącznik `BADACZ_TOL` (ścieżka domyślna bez zmian).

```text
68dc65049c7bcdb431b139a6ab3f1adef205b53b6c90ccb9e1b37128a5776874  code/wuxu_heavy_end_clock_record.jl
c49fffa161b9174cf6535fb98a1c24f826d9e6d6299543048858708d75ec84e2  code/wuxu_heavy_end_clock_analysis.py
1c6b687b017ca92c5f97f92e670d928ace0c252e16fb2fb4419ad4e9bdd51b27  code/wuxu_a1tol058_analysis.py
ec0730b23e0f136c6dff5b734d9c2ff90d66ed5b06c0f5db76479b62333ea08d  data/heavy_end_clock.csv
6790c0c339611bbbb641b59a6eac453884048d4c236232af325cd2dcea7b94a8  data/heavy_end_clock_analysis.json
4c26a15a8b41511d893f366a629853ce4ecf7b9e8a443a2329713066dfd59102  data/heavy_end_clock_tol1e-4.csv
57e2c3118c68b2e81431bf74b3a40f4519d9510b18dff1b38d441a5c01a7d023  data/configs_a1tol058.dat
92167e5b8236f58ed7431d5476805df6455a837449fa75edda1bb9e5ffc318d3  data/kernel_a1tol058.csv
9f8fe82fc0834a2e2bcd5e1d0c59cf711d8303e327b995789470922302af0f8b  data/a1tol058_analysis.json
```
