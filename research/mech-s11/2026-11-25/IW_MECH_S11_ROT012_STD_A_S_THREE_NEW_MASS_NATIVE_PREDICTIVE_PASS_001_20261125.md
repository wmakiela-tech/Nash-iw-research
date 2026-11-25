---
artifact_id: IW_MECH_S11_ROT012_STD_A_S_THREE_NEW_MASS_NATIVE_PREDICTIVE_PASS_001_20261125
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_10 / Mech-S11
date: 2026-11-25
result: H2_POINT_3_OF_3_PASS / BRACKET_FULL_CONTAINMENT_2_OF_3
class: NATIVE_PROSPECTIVE_NONBLIND_MODEL_CONDITIONAL
claim_ceiling: NO_PHYSICAL_PBH_BOUND / NO_AUTHOR_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---
# Decision delta §F: H2 supported at three frozen new mass points
Badacz DRAFT127 firstness, commit 74d04e081b69a4856bdb481933f80f21339c9aed; REC14 ROT016 H1/H2 split; Badacz errata 128 commit 7d6a15b7bdda6a3c7b50e85d9800c1ca0e224619 explicitly accepts split and nonblind status. H1 already independently replicated in Mech-S11 ROT009, bounded referee PASS AUD4 ROT007. H2 is a separate test. No claim of global law, exact symmetry, independent physics implementation, or novelty.

# Actual native experiment
Prereg commit beb4553750c9147dc5b415d772713a8967cfa88e blob baa4cc7f65d13da0a83b0bf174c5281ad4a7bb0b. Workflow commit 9ea19f1b6fc6c457051f93461e11b69e1a410d3b blob ef7e2da6746f345a05c330c9364f085da77147b9. GHA run 45620537732 job 139227167830 all steps success. Three fresh std-only arms, 10 native calls each, no retry. UTC timeline 13:08:49 to 13:27:17. Same original author code and hadron table, R=.5817518, target Y_code=.251, default solver. Explicit decimal masses, not original scan indices. Exact owner driver one-line mass input change verified by reversing patch and Git blob hash fcbcaed4ba4f84f29a4030201a1dfae746e763ed. Same Julia 1.12.3, Project.toml and Manifest.toml byte-identical to actual ROT009 artifact independently compared locally.
Run https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45620537732
Artifact https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45620537732/artifacts/15028500895
Downloaded ZIP 44405 bytes, SHA256 86a928c051fdaa338c9a290e21fc295cf55582d3b038e2a32ece322ce9ef4626 matches provider; CRC PASS; 19/19 SHA256 manifest entries exact, coverage all 19 nonmanifest files, RUN_ID/NASH_COMMIT correct. Resolved Manifest SHA256 95c23d60afaa7bc9fcba71ed1a2b412500102dc89d450cfbd0d4f37925b26564; Project 21d47a9f1b942fd387877db8624780f52005fb5d79367a255cf828c8d5d59cca.

# Results
Independent local Python replay on actual downloaded three CSVs, all 30 rows Success, correct mass identity, one sampled upward crossing each, all roots exactly match CSV and workflow JSON.
| mass g | frozen interval | root | final bracket | relation |
|---|---|---|---|---|
|1474765000|[-19.274,-19.190]|-19.221910866204908|[-19.25,-19.1875]|overlap|
|2133869000|[-19.566,-19.482]|-19.52216040167406|[-19.5625,-19.5]|inside|
|6464011000|[-19.632,-19.549]|-19.587029783120567|[-19.625,-19.5625]|inside|
Frozen primary point criterion 3/3 PASS; secondary full bracket 2/3 inside, first overlaps and extends .0025 dex beyond upper prediction edge. Minimum point margins .0319108662,.0401604017,.0380297831 dex. Endpoint Y margins .0004466843,.0003024182,.0003405815; these are not certified ODE errors. No refinement or changed gates.
CSV SHA256 j38 b55ae7aa97bde941c74eed4be39475f0cf2a0a3828ff836a6a376deeacefa2ff; j51 99e43813aa29f7b25fda854da22ef72d507b49c4b9e5c176af9407c02b9f0a3d; j90 9f0763120aa4abac917762c76adc81ac284778f95a247511ce2ff8e97458c599.
Posthoc inferred effective exponent using rounded frozen base anchors -19.0085,-19.3002,-19.3669: c=.907119,.943459,.935678. Diagnostic, NOT a new fitted common exponent or proof of exact scaling. LT11 source energy nonmatch remains valid: approximate target-law success does not require exact joint source similarity.

# Limits and disposition
H1/H2 both supported at specified points, primary test nonblind. No new solver tolerance test, no full continuous root certification, no physical helium network, STOP A/B/G_DEP remain. Badacz 128 corrects left-wall claim to map-dependent, and requests distinct high-energy generator feasibility test. Do not conflate with this test. EKS1 ROT029 r2 mature-application ceiling not overturned by this result; novelty would require separate prior-art/referee assessment. Request bounded referee of actual fresh data and decision update only, no task cascade. NO_BW_WRITE.
