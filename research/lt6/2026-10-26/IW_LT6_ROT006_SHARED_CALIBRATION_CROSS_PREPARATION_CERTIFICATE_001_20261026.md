---
artifact_id: IW_LT6_ROT006_SHARED_CALIBRATION_CROSS_PREPARATION_CERTIFICATE_001_20261026
created_at: 2026-10-26
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_04 / LT6
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_MATURE_CONVEX_DUALITY / THREE_EXACT_WITNESSES / REPRO_100_LP_PASS / REFEREE_PENDING
claim_ceiling: NO_MATHEMATICAL_NOVELTY / NO_PHYSICAL_PBH_BBN / NO_ORIGINAL_WUXU_JULIA_10D / NO_CANON / NO_EXEC_SIGN
---

# ROT006 — shared calibration is not independent calibration per preparation

**Scientific question.** LT6 ROT005 assumes one source and independent rowwise error sets. Several known source preparations may share ONE unknown error of the same instrument. Checking each preparation against a separately chosen error can wrongly retain inconsistent models.

For a single operator row a, known C=[c1,...,ck] in R^(d×k), residual b=y−C^T a, one common error ||e||1≤eta and observation errors |n_j|≤delta_j, all measurements are jointly consistent iff

    for every lambda in R^k:
      |lambda^T b| <= eta ||C lambda||infinity + sum_j delta_j |lambda_j|.

Proof: exact support function of the compact centrally symmetric convex set C^T B1(eta)+[-delta,delta] plus separation. If C lambda=0, calibration error cancels identically.

The sharp common fitting residual is classical LP minimax duality:

    min_{||e||1<=eta} ||C^T e-b||infinity
      = max_{||lambda||1<=1}(lambda^T b - eta||C lambda||infinity).

**Two exact falsifiers**:
- C=[1,-1], b=(1,1), eta=1: separate calibrations fit, a shared one does not; min common error 1.
- C=I2, b=(.75,.75), eta=1: both scalar fits succeed, shared l1 budget is exceeded; min common error .25.
- Positive control C=[[1,-1],[0,1]], b=(.25,-.65): one shared e=(.25,-.4) fits, min error 0.

**Reproduction**: 100 seeded random problems (d up to 4,k up to 5) solved primal and dual with scipy linprog, maximum gap 1.754e-14. Independent exact examples prevent conflation of a small solver residual with a general mathematical proof.

**Claim ceiling and sources**: Ben-Tal et al. 2004 DOI 10.1007/s10107-003-0454-y; Bertsimas et al. 2025 DOI 10.1287/ijoo.2023.0007; Bontemps–Magnac 2017 DOI 10.1146/annurev-economics-063016-103658. Internal earlier owners MT14 ROT004, Mech-S7 ROT028–029, LT6 ROT002–005. Badacz REVIEW_005 checked ROT003, not ROT006. No novelty claim; no source-validated common calibration for real BlackHawk/Wu–Xu, physical event target or PBH bound.

**Private full theorem and replicator**: https://github.com/wmakiela-tech/Nash-Priv/tree/main/living-theory/2026-10-26/ROT006
**Native working book**: https://docs.google.com/document/d/18lr3zZ6eBNuYn_ZwGhvd3PWP77AxZaSkAV3xqSqiY2s/edit
**Verified composite GitHub REV025**: https://github.com/wmakiela-tech/Nash-Priv/blob/main/living-theory/2026-10-26/REV025/README.md
**Status**: WRITE_AND_READBACK_MUST_BE_VERIFIED / BW_INGEST_PENDING / NO_REFEREE_ACCEPTANCE / NO_EXEC.
