---
artifact_id: IW_MECH_S11_ROT022_STOPA_GENEALOGICAL_CUT_PREDECAY_LOCALIZATION_AND_PARTIAL_FRAGMENTATION_INPUT_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
status: EXISTING_RECORD_DIAGNOSTIC / PREDECAY_LOCALIZATION / FRAGMENTATION_INPUT_PARTIAL
claim_ceiling: NO_CAUSAL_SUBROUTINE_IDENTIFICATION / NO_GATE_CHANGE / NO_STOPA_CLOSURE / NO_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Source and method
Reopened actual four ZIPs from run 45705655584, with source identities and verified provider hashes in ROT021 c895835c385bc99b76286898a6ee2e2f357b125d. Used all 800 gzipped event records. PYTHIA public status documentation https://pythia.org/latest-manual/ParticleProperties.html indexed description, and https://pythia.org/pdfdoc/worksheet8312.pdf indexed status table (not exact 8.318.3 source, direct latest manual fetch 403). abs status 81..89 primary hadron entries, 91..99 late decay or Bose-Einstein entries, 71..79 preparation. Do not assume all record links are physical vertices. Reconstruct cut by tracing final entries back across 91..99 to first non-late mother, require one mother (mother2=0 or same), strict backwards index, full late entry coverage, exact reciprocal contiguous daughter endpoints for all nonfinal late-tree roots/nodes, no final node with children. Deduplicate roots. Use math.fsum four-vectors normalized by nominal 2E. Posthoc diagnostic, not new scientific gate. No new simulations.
# Results
|cell|valid decay cut|final E fails among valid|predecay E fails|valid fragmentation input proxy|final E fails among proxy valid|input E fails among these|
|---|---:|---:|---:|---:|---:|---:|
|u off 100TeV|200|0|0|126|0|0|
|u off 2PeV|200|70|70|64|21|19|
|u on 2PeV|200|82|82|70|32|32|
|g off 2PeV|199|18|18|19|1|1|
799/800 cut valid, all 170 original energy-fail events included, all 170 have same threshold failure before late decays; max component change across this cut 1.4551915228366853e-16 normalized. The invalid case g off success127 has late coverage and daughter mismatch, original final E residual -1.7142743256408723e-7 (pass). No inference about this case's predecay vector. Thus late recorded decay trees do not explain the large residuals on validated subset.
# Partial input proxy
Replace primary hadron roots by deduplicated union of their recorded inclusive mother ranges, retain other predecay roots. Require all mothers 71..79, no overlap with retained other roots, each prep entry either in union or has daughter1 in prep status group, ranges strictly before hadron. These checks are necessary diagnostic restrictions, NOT proof of complete physical cut or independent incoming strings; shared ranges and copy/recoil semantics require exact source. Only 279/800 pass these proxy checks. 54 final E fails in valid proxy subset, 52 already input E fail, two u-off events 134 and 174 input E residual +3.518327751662582e-7 and -5.554669947596267e-7, predecay +1.2497050339588896e-6 and -1.0764867659891023e-6, respectively; proxy transition differences +8.978722587926314e-7 and -5.210197712294757e-7. Maximum normalized component delta between proxy and predecay 1.8183131956029682e-5 (u on). Cannot attribute this to fragmentation itself: proxy incomplete, not a causal vertex cut. 521 excluded by proxy rules, no extrapolation of 52/54 to all 170. 
# Reproducibility
Actual Python execution on archived records produced local mech-s11-rot022-cut-certificate.json SHA256 feb567107f07f1d4b78278a2aa89744a3d58e64620c81b8e50e448402c7cf744 (899021 bytes), script mech_rot022_cut.py SHA256 25c3dfe6ba4c887ca603b2390f5aa38473c32ed97a865eb777ad494b9863158f. Local deliverables, not represented as repo-stored. No new generator execution, no gate relaxation, no folding or BW write. Next: exact source of motherList and parton preparation/copy semantics before further localization. Original G_E/P3 FAIL unchanged; no physical nonconservation or author-error claim.
