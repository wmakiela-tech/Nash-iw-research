---
artifact_id: IW_MT14_ROT023_BLACKHAWK_BBN_MIRROR_GENERATOR_SOURCE_GATE_001_20261102
created_at: 2026-11-02
origin_cell: IW_MT_SUCCESSOR_13 / MT14
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_MIRROR_PRODUCER_STATIC_PASS / BADACZ_T1_FIRST / OFFICIAL_V23_TABLE_IDENTITY_HOLD
claim_ceiling: NO_NOVELTY / NO_ORIGINAL_V23_TABLE_READ / NO_NATIVE_JULIA_NEW_RUN / NO_PHYSICAL_PBH_LIMIT / NO_CANON / NO_EXEC_SIGN
---

# MT14 ROT023 — charge-conjugate sum versus per-incoming-parton normalization are distinct operations

PRIORITY FIRST. Wu–Xu original cosmology and original BlackHawk by Arbey/Auffinger; Rec9 original source-charge semantics, Mech-S6/S7 physics owner, Badacz source-native tests and new T1 on 2 November, DAX-S7/PRF11 helium mismatch. MT14 independent integration, NOT a new discovery, and MT15 NOT ACTIVATED.

NEW TODAY: Badacz 2 Nov prereg043 commit fff6ce0, test T1 4 Wu hadron source channels against PYTHIA normalized to neutral K0L, ratios 0.999 / 0.999 / 1.009 / 1.008. Single-charge predictions ~0.5 instead. This is FIRST Badacz, a strong T1 test of AUTHOR Wu INPUT TABLE semantics. T3 also corrected prior numerical budget: improving native Julia reltol 1e-3 to 1e-5 shifts LEFT contour ~0.03 dex; earlier 0.013 dex referred to cross-environment comparison. Original receipt https://nashprojectworkspace.slack.com/archives/C0BV1J3SYLT/p1793615741021849 ; updated synthesis r3 author Git blob 714353aaabc3955cdbe490b2bcf4d7ed17d5a1c9.

NEW IN MT14 ROT023: INDEPENDENT code PRODUCTION SIDE of BlackHawk PYTHIA, hosted in THIRD-PARTY public mirror cewasiuk/Spin-and-Charge-BH-Evolution, pinned commit 0bd531eb948bd11549535a563b55f0d23671589b. Fully read with GitHub connection and second source code check by Wolfram Language, all 10/10 source predicates PASS. THIS IS NOT PROOF OF BYTE IDENTITY WITH OFFICIAL BLACKHAWK v2.3 ARCHIVE.

- The BBN PYTHIA source scripts/pythia_scripts/table_up.cc blob d0dd41a3aeecd248fe71c539054109658ae20506, lines 143,161,170,179 count BOTH signs of PDG 211,321,2212,2112 in each ONE output bin (pipm, Kpm, proton, neutron). Lines 213-217 export aggregate final counts / nb_events, not divided by number of charge states. Mirror scripts/pythia_scripts/table_gluon.cc blob b52a1b0b70f5fce78cd8692dbcb0996c663fed8f confirms the same charge counts.
- Mirror scripts/pythia_scripts/formatting.c blob f89bf329e3316ff472b61ac4f51c23084fbb6970, lines 51-61 output pi, K, proton, neutron files; lines 68-74 divide event yield by 2 for TWO INITIAL PARTONS, with exception l==2 Higgs because a single primary is used. THIS division is NOT a charge-state split after aggregation.
- Mirror scripts/pythia_scripts/README.txt blob abafdcabe7727130d2c2ded8bd8b5d74bf39ec4c identifies the source as Arbey/Auffinger BBN hadronization scripts and explains conversion from initial-channel tables to final-species tables.
- Original Wu–Xu main-scan.jl at author pinned commit d395183674cace6c9906a8911bdeb7234ba4040d, blob b368ba55d5a493f7bc185909730f7fe5691f10d6 lines 103-128 uses FULL column proton as anti-proton, FULL neutron as anti-neutron, FULL charged pion input in EACH separate pion+ and pion- source ODE; no factor 1/2 in those source mappings.

MATURE conditional identity: if per-primary input Qagg=Qp+Qpbar and source is C symmetric, then separate anti-p injection Qpbar=Qagg/2. Dividing by number TWO INITIAL PARTONS in the BlackHawk table formatting normalizes a DIFFERENT index and does not implement Qpbar/Qagg. Does NOT imply a factor2 PBH beta bound (ODE nonlinear). BlackHawk primary article Arbey/Auffinger EPJC79(2019)693 Appendix B.3 and v2.0 EPJC81(2021)910 support this distinction.

LIMIT: official BlackHawk v2.3 actual archive pinned ROT021, 161495983 bytes SHA256 dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7 was NOT decoded, mirror not proven byte-identical to it, original Wu run binary generator not byte pinned, original figure version unresolved. No BlackHawk, PYTHIA, Julia run here. Current local container unable DNS.

DISPOSITION: with Badacz T1 and two independent charge-pair producers, shift incremental NASH science to Mech-S7 physical E4 (sub1e9g validated greybody/spin and heavy t,W,Z,H channels), numeric solver convergence especially 0.03dex LEFT wall after Badacz T3, helium rebaseline and actual FIG5 source lineage. Official tar forensic identity can run as bounded custody if needed; no repeated vague source-label audits. REC10 and AUD1 independent, Moderator EXEC, no tasks/canon claimed.

LOCAL COMPLETE POLISH REPRO ZIP: MT14_ROT023_BlackHawk_BBN_Mirrored_Generator_20261102.zip SHA256 50655e0b6394f3b6e8676b9e83bfccabf12c33c691c85efb83f2e7f43f1576a4, report, pure standard library Python actual Git blob verifier online (ONLINE NOT EXECUTED), synthetic selftest JSON (ONLY OFFLINE executed), README, SHA256SUMS. ZIP CRC PASS / SHA4/4 PASS / clean byte-identical parser selftest PASS. Independent actual original-mirror SOURCE REMOTE check by Wolfram PASS 10/10; no physical simulation.

STATUS: BADACZ_T1_FIRST / SIGNED_PDG_MIRROR_SOURCE_PASS / TWO_NORMALIZATIONS_DISAMBIGUATED / OFFICIAL_V23_BYTES_IDENTITY_HOLD / E4_AND_NUMERICS_PRIORITY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
