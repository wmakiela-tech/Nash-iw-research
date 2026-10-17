# XH-S4 — Wu–Xu v1/v2 source and scan artifact provenance (002, 2026-10-18)

STATUS: SOURCE_HISTORY_AND_DISTINCT_SCAN_BLOBS_VERIFIED / FIGURE_LINEAGE_OPEN / NO_EXEC_SIGN / NO_CANON / NO_PBH_BOUND
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4

## Verified source facts from primary GitHub repository
Repo: https://github.com/Fenyutanchan/Primordial-Black-Hole
The archived arXiv-2509.05618v1 subtree is preserved alongside the top-level current arXiv-2509.05618 files, in v2 commit d395183674cace6c9906a8911bdeb7234ba4040d (2025-12-30).

V1 main-scan.jl blob SHA 1855db41e67dddbcc4380daf904829833c082d19 explicitly includes tool_script-mesons_from_PBH.jl and calls dN_over_dt_pion, dN_over_dt_kaon, dN_over_dt_kaon_zero_long.
V1 helper tool_script-mesons_from_PBH.jl blob SHA d9b9b15adaf8e500c67f1d1f1f531ccf26002b35 loads mesons_from_PBH.dat, with three species-wise LinearInterpolation(log(rate),log(mass); extrapolation=Linear).
V2 main-scan.jl blob SHA b368ba55d5a493f7bc185909730f7fe5691f10d6 includes tool_script-hadrons_from_PBH.jl and calls five source functions for charged pion, charged kaon, long neutral kaon, proton, neutron. V2 helper blob SHA cc73432910f872d526113ce59b6204f38d0766a9 uses the same log-log linear extrapolation type across five columns.

## Binary output evidence
V1 tracked arXiv-2509.05618/arXiv-2509.05618v1/data/out/scanning.jld2: blob ff08072449c4ef46144cb800778224acd9669a8f, 149272 bytes.
V2 tracked arXiv-2509.05618/data/out/scanning.jld2: blob 10cc9b3f078fcadb91b5e520e75845859ca00b74, 151089 bytes.
Two different tracked blobs exist. Binary JLD2 metadata and numerical payload were NOT parsed. No proof yet binds either file to final printed JCAP plots. The README labels main.ipynb as a reproduction notebook for figures 1,3,4,5, but this is not a file-level figure genealogy.

## Interpretation
V1->v2 entails a material SOURCE-MODEL EXPANSION (mesons three columns -> hadrons five columns), not merely Julia dependency changes. Both inspected source helpers use log-log linear edge extrapolation, neither examined helper implements the paper-declared below-1e9g M^-1.3 branch. This reinforces a source-contract mismatch but does NOT establish the implementation of the actual published numerical run, its Yp/DH sensitivity, or a PBH bound revision.

## Source URLs
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/arXiv-2509.05618v1/tool_script-mesons_from_PBH.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/arXiv-2509.05618v1/main-scan.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/main-scan.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/README.md

PENDING: read figure-notebook lineage and JLD2 data metadata, primary generator table semantics, separately verify post-handoff owner/referee currentness. STORAGE != RECEIPT != SCIENTIFIC ACCEPTANCE.
