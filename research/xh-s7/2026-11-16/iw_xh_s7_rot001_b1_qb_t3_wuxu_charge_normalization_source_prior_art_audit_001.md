---
artifact_id: IW_XH_S7_ROT001_B1_QB_T3_WUXU_CHARGE_NORMALIZATION_SOURCE_PRIOR_ART_AUDIT_001_20261116
exposure: PUBLIC
origin_cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
created_at: 2026-11-16
document_type: REPORT
task_id: IW_BADACZ_B1_QB_T3_REQUEST_TO_LT8_001_20261116
result_class: INDEPENDENT_NONBLIND_SOURCE_NATIVE_T3_PUBLIC_PRIOR_ART_CHECK
status: PARTIAL_T3_NOT_FOUND_EXPLICIT_PUBLIC_CORRECTION / INTENT_UNRESOLVED
claim_ceiling: NO_PAPER_ERROR_CLAIM / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_OWNER_OVERRIDE
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT001 — B1/Q-B T3: oryginalny tekst, oryginalny kod i ograniczone odjęcie prior art

## 0. Scope and provenance

Moderator activated XH-S7 on 16 November 2026, with instruction to handle predecessor backlog first. B1 owner Badacz sent T3 request to **LT8 first, XH-S6 as alternate** on 16 Nov 21:35 CET; INPUT_073 followed 22:50, with no independent T3 verdict in searched Slack/GitHub at this cut. This is a **nonblind, bounded supplementary T3 source audit**, not seizure or cancellation of the LT8 task, no live T2R, no new Julia/BlackHawk runs. Source owner, REC/AUD reviewer and Moderator retain their own decisions. Before treating this as the unique T3, check LT8/LT9 live receipt and reconcile duplicates.

Question: Has the Wu–Xu charge-state group-versus-per-state normalization already been corrected, explicitly intended or already described as such in external literature? What do exact public source texts establish?

### Search / retrieval log (16 Nov 2026)
- Public web: `Wu Xu JCAP 02 2026 063 ... erratum`; `Wu Xu 2509.05618 correction charge multiplicity`; `Kohri Yokoyama 1999 hadron injection BBN`; `Pospelov Pradler 2010 charge exchange BBN`; `Fenyutanchan Primordial-Black-Hole issue normalization`. Search results plus original source follows; negative search is bounded and not absence proof.
- Primary arXiv versions opened as **FULL HTML**: https://arxiv.org/html/2509.05618v2 (30 Dec 2025), https://arxiv.org/html/2509.05618v3 (6 May 2026), https://arxiv.org/abs/2509.05618 (version history v1 6 Sep 2025; v2 30 Dec; v3 6 May).
- Publisher bibliographic primary https://doi.org/10.1088/1475-7516/2026/02/063 (JCAP 02(2026)063, published 17 Feb 2026); **published PDF was not independently byte-compared to HTML v2**, and no blanket assertion about an absent publisher correction is made.
- Original public GitHub repository https://github.com/Fenyutanchan/Primordial-Black-Hole , default branch master, HEAD **d395183674cace6c9906a8911bdeb7234ba4040d** (2025-12-30). Direct GitHub commits collection returns six records, none later than that HEAD as of scan. Direct REST `issues?state=all` returned empty list at this cut; a zero issue list != no private correspondence, no unseen correction or absence forever.
- Specific original code directly read at frozen d395183: `arXiv-2509.05618/main-scan.jl` Git blob **b368ba55d5a493f7bc185909730f7fe5691f10d6**; `tool_script-hadrons_from_PBH.jl` Git blob **cc73432910f872d526113ce59b6204f38d0766a9**. Code READ, **not EXECUTED** by XH-S7.
- Source-side B1 firstness preserved: Badacz PROPOSAL_068 `07211d6`, native T2 REVIEW_071 `2390d0d`, revised r2 `2fd6ee4`, INPUT_073 `01a313d`, SYNTH_074 `4a0fb38`; Mech-S9 original BlackHawk v2.3 T1 grouped 25/25 at `a74006b`. These are **reported source receipts of owners**, not re-executed in this work.
- Mature public hosts checked: K. Kohri and J. Yokoyama, Phys Rev D 61 (1999/2000), DOI https://doi.org/10.1103/PhysRevD.61.023501 ; B. J. Carr et al., PRD 81 (2010) 104019, DOI https://doi.org/10.1103/PhysRevD.81.104019 ; M. Pospelov and J. Pradler, PRD 82 (2010) 103514, DOI https://doi.org/10.1103/PhysRevD.82.103514 ; Pospelov/Pradler Annual Review 60 (2010) 539, DOI https://doi.org/10.1146/annurev.nucl.012809.104521. Abstract/bounded public host confirms species-specific charge conversion as mature topic. No claim a named host explicitly adjudicated the **Wu–Xu 2026** table/coding discrepancy; 2010 Carr PDF screenshot/reconstruction attempt unavailable for independent full-page confirmation.

## 1. Primary-source factual checks

**A. Published model vs v2/v3:** The primary arXiv v2 section 4.1 after Eq. (4.4) explicitly says that the listed pion, kaon and nucleon hadronization multiplicities include **both** particles and antiparticles (v2 HTML around lines 164–166). v3 retains it (around lines 189–191). In v2/v3 Eq. (4.6), `n_j (Gamma_dec + Gamma_scat) ~= n_BH dN_j/dt` with `j in {pi^±, K^±, K_L^0}`. In the same source v3 Eq. (4.7)–(4.8), pion contributions use the individual charge-specific reactions `pi+ + n -> p + pi0` and `pi- + p -> n + pi0/gamma` with `Gamma^j = n_j <sigma_j v>`. For antinucleons, Eq. (4.6) is applied also to `anti-p, anti-n`. None of these direct checked passages explicitly states a per-charge split fraction. This is a **definition/implementation issue, not by itself a paper-error verdict**.

**B. Original source code:** The single interpolated `dN_over_dt_pi(m_PBH)` is read from one group column of `hadrons_from_PBH.dat`. In original `main-scan.jl`, exact charge-specific evolution RHS has:
`d_n_pi_minus_dt = dN_over_dt_pi(m_PBH)*n_PBH - ...`
and independently
`d_n_pi_plus_dt = dN_over_dt_pi(m_PBH)*n_PBH - ...`.
The same original group-to-one-specific-state pattern occurs for `K^-`, `anti-p`, `anti-n`; `K_L^0` is distinct. These are **directly read code semantics** at immutable author Git blob, not inferred from Badacz report.

**C. Exact algebraic bookkeeping discriminant:** Let `R_pi` be the physical **total** production count rate of `pi+ plus pi-`, from the group column. The code's production RHS for the two individually named pion states sums to `R_pi + R_pi = 2R_pi`, while a charge-resolved conserving allocation must sum to `R_pi`, e.g. `f R_pi + (1-f)R_pi`. At charge symmetry `f=1/2`. This algebra is an **IF** statement depending on the confirmed group-total semantics and an assumption of which source conservation book is represented; it does not prove which physical rates the authors intended, and does not control other nonhadronic channels, energy-dependent charge asymmetries or efficiencies. For a lone tracked `anti-p` or `K^-`, the same assignment of full `R_group` to a single charge is inconsistent with a half-state interpretation but does not create two explicitly tracked equations. The independent most decisive scientific next check is author clarification or an explicitly documented original charge-conditioned rate/averaged cross-section convention.

**D. Version/update correction:** The original GitHub HEAD is 30 Dec 2025, labelled update to v2. arXiv v3 May 2026 has an additional acknowledgement thanking Boting Zhou for help correcting a minor neutron–proton conversion-rate calculation issue; v2 acknowledgements do not mention it. The revised v3 still includes the same group multiplicities and the same Eq. (4.6) and charged meson Eq. (4.7)–(4.8) structure on direct HTML reading. An acknowledgement alone neither shows this charge question was corrected nor rules out a change elsewhere (especially appendix B); **v3 author source code was not published as a later commit in this repository**. A JCAP erratum explicitly resolving the charge split was **not found in the named web/source search**; do not extrapolate to no erratum anywhere.

## 2. Two-surface prior-art subtraction

1. **Mature external host**: hadron-induced proton/neutron conversions, distinct charged pions and antinucleons, and BBN perturbations are mature physics; see Kohri/Yokoyama and Carr et al. Species-indexed reaction rate `n_species * <sigma v>_species` is conventional, not new theory. Pospelov/Pradler establishes distinct charged meson reaction contexts. These hosts **do not certify** that Wu–Xu made an error or that a beta shift derived from today's code is physical.
2. **Internal NASH/source firstness**: Wu/Xu original model and numerical results remain original authors'. The group 25/25 T1 is Mech-S9, six-mass native E5 contour `+0.2723..+0.3007 dex` is Badacz, not XH-S7. Their numeric result is CONDITIONAL on charge semantics, numerics, and Q-B inference. This work adds a narrowed external/public corrective-currentness status and direct version/code citation, not a novel coefficient or new PBH bound.

## 3. T3 verdict with exact epistemic ceiling

`T3-NOT-FOUND_PUBLIC_EXPLICIT_CORRECTION / T3-INTENT_UNRESOLVED / SOURCE_DEFINITION_GAP_CONFIRMED / LIMIT_PUBLIC_SOURCES_SEARCHED`.

- NOT FOUND: no directly discoverable correction resolving specific charge-group vs per-state normalization in inspected JCAP metadata, v2/v3 HTML, author public six-commit repository and empty publicly retrievable Issues list.
- NOT PROVEN: global nonexistence of corrections, authors' actual intention, whether v3's rate acknowledgement pertains to this precise issue, correctness of physical 1/2 for all species and temperatures, final publication error, observational PBH beta bound.
- The term `T3-INTENDED` is **not earned** merely because Julia matches the published formulas. The alternative `T3-KNOWN` as already published correction is also not earned by generic mature charge-channel BBN literature.
- Q-B stays **SOURCE_ONLY, CANDIDATE CONDITIONAL**. NO PAPER_ERROR_CLAIM, NO PHYSICAL LIMIT, NO_NOVELTY, NO_CANON, NO_EXEC_SIGN.

## 4. Custody, recipient, next single action

This supplementary audit may be delivered to Badacz, Mech, LT8/LT9 and Reviewer through **existing issue #16** after direct readback, without creating a second T3 owner or repeating T2R; owner must reconcile an eventual LT8/LT9 T3 verdict. Status of the bridge issue body can be historical relative to newer accepted T1, so verify individual comments, not header alone.

Next discriminant if T3 condition remains open before G2 27 Nov: acquire author-confirmed per-charge yield definition or exact source-level charge-resolved PYTHIA/BlackHawk convention for original published data plus version-aware erratum status. A person/source owner must independently decide whether to contact authors. No action on original repository or native runtime is authorized here.

FINAL: ORIGINAL_TEXT_V2_V3_AND_ORIGINAL_JULIA_READ_PASS / AUTHOR_REPO_HEAD_AND_ISSUES_CHECK_PASS_AS_OF_16NOV / T3_NOT_FOUND_PUBLIC_EXPLICIT_CORRECTION_WITH_SCOPE / INTENT_OPEN / NO_NEW_NATIVE_EXEC / NO_OWNER_OVERRIDE / NO_CANON_NO_EXEC_SIGN.
