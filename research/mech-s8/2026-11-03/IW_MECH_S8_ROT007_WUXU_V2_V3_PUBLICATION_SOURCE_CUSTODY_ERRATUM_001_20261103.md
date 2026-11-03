---
artifact_id: IW_MECH_S8_ROT007_WUXU_V2_V3_PUBLICATION_SOURCE_CUSTODY_ERRATUM_001_20261103
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_07 / Mech-S8
created_at: 2026-11-03
exposure: PUBLIC_SAFE
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: ORIGINAL_VERSION_CUSTODY_CORRECTION_ONLY / NO_FIG5_HISTORICAL_RUN_PROOF / NO_V3_CODE_REPLAY / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN
---

# ROT007 — Critical owner correction: author's pinned Wu–Xu commit is **v2**, NOT v3

**Status:** SOURCE_VERSION_IDENTITY_PASS / ROT004_VERSION_LABEL_ERRATUM_REQUIRED / HISTORICAL_JCAP_FIG5_EXECUTION_OPEN / POSTPUBLICATION_V3_CODE_OPEN.

The Mech-S8 ROT004 report correctly read the original code dependencies, author JLD2, the 10-dimensional top-level scan and distinct 8-dimensional legacy overlay. Its repeated label `v3` for the pinned **top-level** `main.ipynb`, `main-scan.jl`, `scanning.jld2`, `Y_P.png` was WRONG. Owner correction: **all top-level files at author Git commit `d395183674cace6c9906a8911bdeb7234ba4040d` belong to the author's publicly pinned v2 branch state**. The `arXiv-2509.05618v1/` subdirectory is the archived v1 code, with 8D dynamics and separate JLD2. This correction does not change ROT003's subedge first-interval arithmetic, ROT004's static file graph or ROT006's conditional number integrals, but does change their version/provenance interpretation.

## Independent primary source chronology and exact identities

| Source | Pinned identity/date | What is established |
|---|---|---|
| arXiv v1 | https://arxiv.org/pdf/2509.05618v1 ; deposited 2025-09-06, 23 pages | v1 manuscript |
| arXiv v2 | https://arxiv.org/pdf/2509.05618v2 ; deposited 2025-12-30, 27 pages | v2 prepublication manuscript |
| Author Git | https://github.com/Fenyutanchan/Primordial-Black-Hole/commit/d395183674cace6c9906a8911bdeb7234ba4040d ; commit created_at 2025-12-30T15:29:31Z, exact message `2509.05618: update to v2` | TOP-LEVEL 10D original source files are v2; the commit is **before** JCAP publication |
| Published JCAP | DOI https://doi.org/10.1088/1475-7516/2026/02/063 , published 2026-02-17 | peer reviewed version of record; its full runtime provenance remains unproven |
| arXiv v3 | https://arxiv.org/pdf/2509.05618v3 ; 2026-05-06, 28 pages | postpublication revision; acknowledgments add thanks to Boting Zhou for helping correct **a minor error in n–p conversion-rate calculation**; magnitude, exact changed code and downstream Fig5 effects remain unverified |
| PUBLIC AUTHOR REPO | GitHub API https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole/branches/master ; `master.commit.sha=d395183674cace6c9906a8911bdeb7234ba4040d`, repo `pushed_at=2025-12-30T15:30:13Z`; all six accessible author commits ending Dec 2025 | **No v3 implementation commit in checked original public master as of 2026-11-03** |

Original top-level `main.ipynb` blob `171c4a29e414860d724c817641896628f35982b0`; 10D scan `main-scan.jl` blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`; `scanning.jld2` blob `10cc9b3f078fcadb91b5e520e75845859ca00b74`; five-hadron source module blob `cc73432910f872d526113ce59b6204f38d0766a9`. Archived v1 8D notebook blob `89a69d1ac23f3024893db51da29c9f573ecf0c5f`; separate v1 `scanning.jld2` blob `ff08072449c4ef46144cb800778224acd9669a8f`. v2 Fig5 public plotting has a v1 symlink overlay, as found ROT004. **Do not rename physical files to v3 by inference from present-day default arXiv URL.**

Source texts: arXiv v3 includes the new Boting Zhou acknowledgment; neither arXiv v2 nor inspected published JCAP PDF text contains this acknowledgment. Figure 5 captions and the nominal YP, beta target range in retrieved v2/v3/JCAP text are similar; **NO pixel plot, exact contour or data-file identity was verified across versions.** Attempts to screenshot paper PDFs through the web PDF screenshot service yielded cache-miss errors, so no visual comparison is claimed.

## Consequences and no-overclaim guard

(1) ROT003's precise code-vs-manuscript below-edge exponent issue is already **within v2**, before publication; it is not an artifact of comparing v3 prose with v2 code. ROT003's law issue remains a SOURCE-METHOD DIVERGENCE, **not** an observed published bound error.

(2) The public pinned author main is v2 even after the later arXiv v3 May 2026 change. Therefore **reproduction of v2 Git code is not automatically reproduction of v3 model or updated manuscript Fig5**. Distinguish `WUXU_CODE_V2_PINNED`, `WUXU_JCAP_2026_PUBLISHED`, `WUXU_ARXIV_V3_POSTPUB` in all future reviews.

(3) The paper v3 acknowledgment does not independently prove actual code change to a particular cross section, nor numeric YP/DBB/β sensitivity. Never assert v3's output contours changed unless version-specific native data/code and controlled results are obtained.

**Next owner gate:** obtain author-confirmed exact JCAP figure run provenance (source SHA, original scanning.jld2 hash, plotted image), and, separately, author v3 source/rate correction diff plus v3 scan. The original E4 below-table physics, BlackHawk energy/hadronization support, charge-state map and full numerical strict error gates remain OPEN. 

`ROT007 PASS / ROT004 OWNER_ERRATUM / HISTORICAL_FIG5_EXECUTION_OPEN / ARXIV_V3_CODE_NOT_IN_CHECKED_MASTER / E4_SOURCE_BLOCK / NO_PBH_BOUND / NO_CANON / NO_EXEC_SIGN`
