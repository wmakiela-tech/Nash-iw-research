# XH-S4 / Wu–Xu public version history — first rotation 001 (2026-10-18)

STATUS: SOURCE_PROVENANCE_PARTIAL / NO_EXEC_SIGN / NO_CANON / NO_PBH_BOUND
CELL: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_03 / XH-S4
AUTHORITY: Moderator activation explicitly approved in XH-S4 conversation 2026-10-18.
CONTROLLING PREDECESSOR: XH-S3 HARVEST-026 (Drive 1UX9zEyq008k0xrKtyBun-kcIivKWVFUNmzuvHWRh2Kk).

## Verified primary code-history facts
- Public repository: https://github.com/Fenyutanchan/Primordial-Black-Hole
- Repo commits API returned HEAD d395183674cace6c9906a8911bdeb7234ba4040d, dated 2025-12-30, message "2509.05618: update to v2".
- Its predecessor 3613b5452dd103f521b9aaae2e6e912ef6b9c611, 2025-09-09, was a citation-information update.
- In v2 commit, tracked changes include README and Julia Project.toml updates: advertised Julia 1.11.6 -> 1.12.3, changed dependency list; archived subtree arXiv-2509.05618v1 added to repo.
- Current README names main.ipynb as reproduction notebook for Figs. 1, 3, 4, 5; main-scan.jl as scan runner.
- Current public helper arXiv-2509.05618/tool_script-hadrons_from_PBH.jl SHA cc73432910f872d526113ce59b6204f38d0766a9 reads hadrons_from_PBH.dat and uses species-wise LinearInterpolation(log(rate),log(mass); extrapolation=Linear). No explicit sub-1e9 g M^-1.3 branch in this inspected helper.
- Public releases API returned [] (no releases).

## Interpretation (limited)
Public v1 archive plus v2 commit give an additional route for historical comparison. They do NOT demonstrate which source rule produced published numerical Y_P / PBH results. This remains PUBLISHED_RUN_PROVENANCE = UNRESOLVED.
Do not equate code release timing or repository README reproduction instructions with verified figure-level provenance.
Predecessor HARVEST-026 establishes PAPER_DECLARED_SUBEDGE_M^-1.3 != CURRENT_PUBLIC_HELPER_LOGLOG_EDGE, and distinguishes aggregate generator Q from reaction source R. No normalization, Yp, D/H or PBH-bound error is concluded.

## Source pointers
- https://github.com/Fenyutanchan/Primordial-Black-Hole/commit/d395183674cace6c9906a8911bdeb7234ba4040d
- https://github.com/Fenyutanchan/Primordial-Black-Hole/tree/master/arXiv-2509.05618/arXiv-2509.05618v1
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl
- https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/master/arXiv-2509.05618/README.md

## Open source-native questions
1. Inspect historical v1 source helper and main-scan path against v2; avoid interpreting absence of a same-named file as absence of source logic.
2. Whether scanning.jld2 output (or figure notebook metadata) binds author figures to an exact source branch / commit.
3. Identify BlackHawk secondary species columns from generator-native documentation before B_exec vs B_split physical normalization conclusions.

CUSTODY: GitHub archival report only; no BW ingestion, referee receipt or scientific acceptance inferred.
