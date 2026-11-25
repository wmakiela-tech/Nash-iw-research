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

## 129 (PREREG, zamrożony przed przebiegiem)
```
f5ee66390f29c6b0ee0e95d8f7195dbcac5bfaae8f659a8684aa92326a85c7f1  IW_BADACZ_B1_STOPA_GENERATOR_EXTENSION_PREREG_129_20261125.md
```

## 130 (delta §F + poprawka A1 do PREREG_129, przed wynikiem)
```
8ac212c3464bc5682062795dde990f29ff2e8e95196b21a45cc947630346bd7c  IW_BADACZ_B1_SECTION_F_UPDATE_AND_PREREG129_AMENDMENT_130_20261125.md
```

## 131 (brief B1 v0)
```
9e0533bf380b3162f656339bcb68e86c2043f1f33169cf507bc50bc4b6395fa2  IW_BADACZ_B1_RESULT_BRIEF_STD_A_V0_131_20261125.md
```

## 132–133 (REVIEW_132, brief v1, rysunek)
```
7e4bcbe0d4ea1088a83c6ff74813399f6e6aae509ce0e34e4e79a827c6b2f06e  IW_BADACZ_B1_STOPA_GENERATOR_EXTENSION_REVIEW_132_20261125.md
9ce228bc724208ed7777e68521a1101c32779b1cbfb9f60b7ad80fe73da489df  IW_BADACZ_B1_RESULT_BRIEF_STD_A_V1_133_20261125.md
22566984f2dd6ee125fe6f589f77f19343c61a2cc01ad160262dc753244c00d1  code/figure_brief_133.py
8f75081e98121939c45883f6cc35d81cda98d5bace80066964704db3d7bb3441  data/fig_brief_133.json
66d5442fd2ec82dea99e1365813a9023d66e263b9290ed7f7accbc54a1d6ec3c  data/fig_brief_133.png
```
Odtworzenie rysunku: `python3 -I code/figure_brief_133.py <research/badacz> data/fig_brief_133.png data/fig_brief_133.json` (PNG zależy od wersji matplotlib; kontrolny jest JSON).

## 134 (PREREG, zamrożony przed obliczeniem)
```
826db6ae5db2a156580668e0de52aeb74d62d72f7361ec326870b14fbd745097  IW_BADACZ_PEV_GENERATOR_DIAGNOSTIC_SIGN_SPLIT_PREREG_134_20261125.md
```

## 135 (REVIEW_135 + kod i wynik PREREG_134)
```
17c301e4290228f05974e694c795b6f6ec18dca41398d6ac59ec49b31ee67af4  IW_BADACZ_PEV_GENERATOR_DIAGNOSTIC_SIGN_SPLIT_REVIEW_135_20261125.md
c0e4f5de0c04252a1184945164ff8726a38fbeef00a32aac527de917128a2995  code/pev_sign_split_134.py
c009895a70737ecf4a9407680c5b7831ab9903e04b29061fb0d4074a5633a0f0  data/pev_sign_split_134.json
```
Odtworzenie: pobrać 8 artefaktów (ID w REVIEW_135), rozpakować każdy do katalogu <id>/, `python3 -I code/pev_sign_split_134.py <katalog> data/pev_sign_split_134.json`.
