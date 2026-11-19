---
artifact_id: IW_XH_S7_ROT006_KY1999_EFFECTIVE_YIELD_STAGE_AND_SINGLE_SCALAR_FALSIFIER_001_20261119
exposure: PUBLIC
origin_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
created_at: 2026-11-19
responds_to: XH-S7 ROT005; Badacz INPUT_075; LT9 ROT006
document_type: PRIMARY_SOURCE_BOUND_SOURCE_SEMANTICS_CLARIFICATION_WITH_NEW_NEGATIVE_CONTROL
status: KY1999_EFFECTIVE_YIELD_STAGE_EXPLICIT_PASS / PDG1998_TABLE_ORIGINAL_READ_PASS / NO_UNIFORM_PDG_TO_KY_FACTOR_PASS / KY14P1_FULL_TRANSFORMATION_HOLD / T3_SEMANTICS_OPEN
claim_ceiling: NO_ORIGINAL_AUTHOR_ERROR / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT006 — KY(1999) 14.1 is an effective yield, NOT a raw PDG entry; no universal normalization scalar

## 0. Science priority and scope

Human Moderator has paused NASH C1 until independently meaningful scientific achievements (LT9 ROT006 Slack dispatch 17 Nov 19:33 CET). XH-S7 therefore performs only this narrow source-native historical review, without C1 design, ownership transfer or execution of any PBH numerical physics.

Parent source reviewer: XH-S7 ROT005 public Git commit 20f5c38cf0ff9da13c4efc2e703a371b0eece8e3. Primary T3 owner LT9 later confirms SEMANTICS_OPEN and accepts the bounded ROT005 finding in issue #16 comment 6957486816; independent LT9 ROT006 and its 2026 Bianco et al. mature source host remain separate. Original hypothesis from BADACZ INPUT_075 retains firstness.

## 1. Direct original primary textual sources (not secondary paraphrase)

**Kohri & Yokoyama 1999**, *Primordial Black Holes and Primordial Nucleosynthesis I: Effects of Hadron Injection from Low Mass Holes*, arXiv astro-ph/9908160v1, https://arxiv.org/pdf/astro-ph/9908160. Original primary PDF text retrieved directly in this rotation. Relevant Eq10,11,13,14 and text in section II pp5–7. PDF page **screenshot was attempted through web and failed CACHE MISS**, and container direct PDF download also failed; therefore source text was read but original PDF pages were not visual/byte authenticated.

**Particle Data Group 1998**, Caso et al., *Review of Particle Physics*, exact PDG Table38.1, https://pdg.lbl.gov/1998/hadronicrpp_page7.pdf ; direct original primary PDF text retrieved. Table states charged conjugates INCLUDED in grouped π+, K+, p entries, rates for hadronic e+e− events with short-resonance decay products included. PDF page screenshot attempted, returned CACHE MISS. No visual-page or archive byte assertion.

**Wu & Xu** original source prior pinned GitHub d395183 retains literal same-group-source-to-two-pion-charge equations. This is accepted prior source fact, NOT rerun here.

## 2. Important explicit original-author text requiring clarification to ROT005

In KY section II, immediately BEFORE Eq13:
- Eq10: per-JET `N_Hi=f_Hi <Nch>/2`, with `<Nch>` per TWO jets.
- Their text expressly says they must ESTIMATE **EFFECTIVE f_Hi**, accounting for decay products of particles whose lifetime is too short to affect BBN; they determine which species survive on the nucleon conversion timescale, about O(10^-8 seconds).
- Directly preceding Eq13 they explain they **CALCULATED final yield** `n_Hi` of those species per two jets **OUT OF** PDG Table38.1. This is NOT a claim that KY Eq13 repeats the literal PDG table values.
- Eq13 then gives n_pi+=n_pi−=14.1, n_K+=n_K−=1.67, n_p=n_pbar=0.772, etc.
- Eq14 sets f_Hi=n_Hi/<Nch>(91.2GeV).

**Dated correction to ROT005 wording:** The statement `PDG 1998 π group 17.1 ≠ KY 14.1` remains a DIRECT numerical fact. However this cannot be characterized as an unexplained citation discrepancy or indication of a typo: KY's own source text EXPLICITLY announces a post-PDG effective-yield calculation. ROT005 itself recognized a possible effective-decay transformation; this addendum upgrades that from hypothetical to directly supported original-author stated method, while preserving the unknown *exact transformation*. There is no authenticated numerical derivation of each 14.1,1.67,.772 from Table38.1.

## 3. New exact negative control: no common one-parameter rescaling of PDG grouped values produces KY effective Eq13

Original PDG Table38.1 at √s≈91GeV, conjugates included:
`π+ column 17.1±.4`, `K+ column 2.39±.12`, `p column .964±.102`.

Original KY Eq13 effective n labels:
`π+ / π− each labeled 14.1`; `K+ / K− each labeled 1.67`; `p / pbar each labeled .772`.

For each **printed charge-conjugate/group comparable source row**, the numerical ratios KY/PDG are:
- π: 14.1/17.1 = 0.8245614035087718;
- K: 1.67/2.39 = 0.6987447698744769;
- p: 0.772/0.964 = 0.8008298755186722.

These are unequal; therefore NO single `c` satisfies `KY_i = c·PDG_i` for all three species. This falsifies ONLY the simplest **ONE_UNIVERSAL_POST_PDG_SCALAR** hypothesis. Species-dependent effective lifetimes/decay branching, differing state inclusion, generator conventions or other steps can produce unequal ratios. Their true exact formula remains unresolved. This is not evidence that the author made an error and not a 2×-factor proof.

Additional denominator logic: Original KY Eq11 yields `<Nch>(91.2GeV)=20.82461855454813`. For simultaneous LITERAL independent charge-state final multiplicities Eq13 would imply 28.2 charged pion counts>Nch, so such interpretation cannot describe a common disjoint same-stage partition of charged final-state tracks. But because original KY explicitly creates BBN-effective yields from another stage, the *strong claim of a raw final-track contradiction* is CONDITIONAL on both stages and count domains being identical. It cannot by itself adjudicate author's physics. Under a one-group reading 14.1/<Nch>=0.67708 whereas PDG 17.1/<Nch>=0.82114, not a physical probability attribution without full mapping.

## 4. Ownership, source-quality and conclusion

LT9 retains B1/T3 reviewer ownership, Badacz original T2 / hypothesis and Mech-S10 native T2R lease. Do not rerun T2R or launch Julia/BlackHawk or contact authors. No new external gravity SI/raw torsion data source obtained; XH-S6/ROT003–004 HOLD remains unchanged.

Machine-repro source-only arithmetic ACTUALLY executed on 19 Nov under /mnt/data/xh_s7_rot006/rot006_kohri_effective_factors.py and output JSON. Independently published GitHub reproducible code in same ROT006:
https://github.com/wmakiela-tech/Nash-iw-research/blob/2f36ffd6d43501ca56373874200940176674bcbc/research/xh-s7/2026-11-19/code/xh_s7_rot006_ky1999_effective_yield_scalar_falsifier.py .
Do not confuse the two implementations' byte SHA with each other; compare numeric invariants.

FINAL: XH_S7_ROT006_ORIGINAL_KY_EFFECTIVE_POST_PDG_YIELD_TEXT_PASS / PDG_TABLE38P1_CONJUGATES_PASS / SINGLE_SCALAR_RESCALING_FAIL_EXACT / KY_14P1_FULL_DERIVATION_HOLD / ROT005_SOURCE_STAGE_CLARIFICATION / T3_SEMANTICS_OPEN / C1_PAUSED / NO_ORIGINAL_AUTHOR_ERROR_NO_PBH_BOUND_NO_NOVELTY_NO_CANON_NO_EXEC_SIGN.
