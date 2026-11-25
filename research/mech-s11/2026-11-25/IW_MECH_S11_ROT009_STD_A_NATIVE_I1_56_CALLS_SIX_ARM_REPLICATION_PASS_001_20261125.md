---
artifact_id: IW_MECH_S11_ROT009_STD_A_NATIVE_I1_56_CALLS_SIX_ARM_REPLICATION_PASS_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
exposure: PUBLIC_SOURCE_REPLICATION
result: STD_A_R_NATIVE_INDEPENDENT_EXECUTION_PASS_NONBLIND
claim_ceiling: MODEL_CONDITIONAL / NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Native source replication STD_A-R: PASS
Moderator confirmed standing computation authorization. Frozen prereg commit 24c5fcb49b27f3eb63bb1049dc9a44adfa451706 blob 21cac9610498a6e060a4168ba786326dd5c0a883. Workflow commit 206be911e7846f1b0ade9d6f1634d3534299b782 blob af5f18883c5deb142133fb4f01b0b1d9e3996d41. Actual GHA run 45616230955, job 139212212682, completed success, all steps success. Public guard and CI for same commit success. Native fresh six arms, owner driver reused, no retry, separate GPT execution and Python scorer, not independent implementation or blinded test. Badacz first native result REVIEW124/126, EKS1 first direction, REC14 ROT016 H1/H2 decision separation retained.

## Primary source and custody
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45616230955
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45616230955/artifacts/15023132612
Artifact ZIP 50865 bytes, id 15023132612, SHA256 5140a3e3f7fef4699f45a9fe27fce260c266d35363b344287b3c1c6f36445342 provider digest and local hash agree. Actual downloaded ZIP CRC PASS, all 30/30 manifest hashes independently verified, 31 entries total. RUN_ID and NASH_COMMIT match. Actual resolved Manifest.toml SHA256 95c23d60afaa7bc9fcba71ed1a2b412500102dc89d450cfbd0d4f37925b26564; package status verified pinned direct dependencies incl Julia 1.12.3 configured, NaturalUnits 4a9f007. No assertion transitive environment identical to Badacz's.
Original Wu-Xu commit d395183674cace6c9906a8911bdeb7234ba4040d, main-scan.jl SHA256 1c78b4012dc3b4357446169b31347e84ade8f4de3420538ef83764937e0a6978; author hadron table SHA256 25411c26cb24b08058be6dffe01e3c6cc668c91de963438a91c4aac0a38199df. Badacz driver SHA256 3e11cf8453aee30783492a7dbcf13c91a6627a67871f3a240d9c1bdd1dd140b6. Timeline actual six arms UTC 12:42:10 to 12:57:47. All 56 evaluations Success.

## Result
j16 base no sampled upward crossing (6 evaluations), std -17.580646487288295 (10).
j22 base -17.225076555908338, std -18.608872941203636, delta -1.3837963852952981.
j62 base -19.388974357352645, std -19.63275456458953, delta -0.24378020723688465.
Each j22/j62 arm 10 evaluations. Five roots independently recalculated from downloaded CSVs in local Python, exact match to recorded roots and owner. All five final brackets width .0625 dex. Six original owner CSVs separately re-fetched from immutable commit 58b276a99264794efc8c1f6bfc6d21019d0fb32e; all 56 Y_code values compare equal after parsing as binary64 in corresponding row order. NOT bytewise CSV equality or full trajectory identity. Owner firstness preserved.
Tau std/base j16 1.718356664149678, j22 1.7251298011104599, j62 1.7190837155299394. Five prereg gates G_RUN G_BASE G_TAU G_MONO G_REPLICA true. Note Y_code >1 in three high-beta j62 rows, since Y_code=2X/(1-X) is not a bounded physical helium mass fraction; no physical helium transfer claimed. No new test of solver tolerance, owner G_REP failure preserved, STOP A/B/G_DEP and T3 semantics open. A PASS cannot establish H2; B untested. Recommend independent REC/AUD referee of this bounded source replication and Moderator §F update; no automatic candidate elimination or promotion. No BW write.

## Negative knowledge / operations
Prior attempts to locate run used PR-only commit workflow connector, no matching Gmail, no inference of execution failure. Direct GitHub GET /repos/wmakiela-tech/Nash-iw-research/actions/runs?head_sha=206be911e7846f1b0ade9d6f1634d3534299b782 returned exact run, job and artifact retrieved. No duplicate computation.
