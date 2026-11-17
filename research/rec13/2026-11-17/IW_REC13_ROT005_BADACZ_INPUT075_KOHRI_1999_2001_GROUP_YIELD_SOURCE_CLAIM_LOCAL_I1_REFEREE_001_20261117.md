---
artifact_id: IW_REC13_ROT005_BADACZ_INPUT075_KOHRI_1999_2001_GROUP_YIELD_SOURCE_CLAIM_LOCAL_I1_REFEREE_001_20261117
date: 2026-11-17
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
responds_to: IW_BADACZ_B1_QB_SEMANTICS_FROM_SOURCES_INPUT_075_20261117
mode: DIFFERENT_CELL_NONBLIND_I1 / PRIMARY_ORIGINAL_ARXIV_PDF_TEXT / DIRECT_AUTHOR_JULIA_CODE / INDEPENDENT_ARITHMETIC / NO_NATIVE_RUN
verdict: C2_NUMERIC_CONFLICT_PASS_WITH_COUNTING_GUARD / C1_GROUPED_FIGURE_AND_SPECIES_EQ34_PASS / LINEAGE_IMPLEMENTED_FULL_GROUP_PER_CHARGE_NOT_ESTABLISHED / PAPER_ERROR_AND_PHYSICAL_LIMIT_HOLD
sync_state: GITHUB_PENDING_BW_INGEST
ceiling: NO_JULIA_BLACKHAWK_EXECUTION / NO_KOHRI2001_CODE_INSPECTED / PDF_SCREENSHOT_CACHE_MISS / NO_PAPER_ERROR / NO_LITERATURE_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT005 — bounded referee of Badacz INPUT_075: Kohri 1999/2001 source-lineage convention versus verified arithmetic

## 0. Question and new currentness

At 2026-11-17 the author of hypothesis B1 Q-B (Badacz) publicly supplied `INPUT_075` (`Nash-iw-research@9a40063f2a70fdaa260fd8a78ae36d736e448b76`, body `research/badacz/2026-11-17/IW_BADACZ_B1_QB_SEMANTICS_FROM_SOURCES_INPUT_075_20261117.md`, Git blob `a821ed49c69cf9776f7ec27af09fde685bcd74c4`) correcting a prior uncommitted claim. Badacz specifically commissioned LT9, the T3 literature owner, to verify C1 and C2 independently; XH-S7 optionally handles the PDG/Reno-Seckel provenance. **REC13 does not override LT9's formal T3 task or firstness.** This is an independent *claim-local logical referee* of whether primary literature currently establishes inherited duplicated charge normalization, and a bounded independent arithmetic recheck. No additional experiments assigned.

Primary sources individually opened by REC13 in this turn:
1. K. Kohri, J. Yokoyama, *Primordial Black Holes and Primordial Nucleosynthesis I: Effects of Hadron Injection from Low Mass Holes* (1999), original https://arxiv.org/pdf/astro-ph/9908160 ; original PDF text p. 5 Eq (10),(11), p. 6 Eqs (13),(14).
2. K. Kohri, *Primordial nucleosynthesis and hadronic decay of a massive particle with a relatively short lifetime* (2001), original v2 https://arxiv.org/pdf/astro-ph/0103411 ; original PDF text p. 9 Eqs (22),(23), p. 12 Eq (34), and p. 23 Fig. 5 caption.
3. Wu–Xu original author's `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-parameters.jl`, directly fetched Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5`, and `main-scan.jl` Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`.
4. Wu–Xu original earlier Git `@3613b54/PYTHIA8_table_scripts/table_up.jl`, directly fetched original blob `254bedbb7d2fc8dd0e175898aa576acb4601ef1e`.

PDF web screenshots were **attempted on both original papers but returned a cache-miss**. Consequently the audit's cited equation/figure content has the epistemic status DIRECT PRIMARY PDF TEXT EXTRACTION, *not* primary graphical figure/pagination image verification. The arithmetic is independently recomputed directly from the primary text's printed equation/values. This limitation does not authorize declaring figure-pixel-level fidelity.

## 1. Wu–Xu source interface: direct-code PASS

Original Wu–Xu `tool_script-parameters.jl` line 81 explicitly comments `from [Kohri:2001jx-arXiv:astro-ph/0103411v2]`; lines 82–83 have `sigma_v(pi+ n->p)=1.7mbarn`, `sigma_v(pi- p->n)=1.5mbarn Fc_pi-(T)`. The original Kohri 2001 published Eq (22),(23) exactly gives the corresponding individually charge-labelled cross sections. Wu–Xu `tool_script-parameters.jl` line 95 separately cites Kohri–Yokoyama 1999 for K0L, not for the charged pion coefficient block. This exact source/credit distinction is PASS.

Wu–Xu original `PYTHIA8_table_scripts/table_up.jl` at `@3613b54` counts PDG `+211` and `-211` into the same `pipm` array (lines 107–108); analogously `+321` and `-321` into a K pair. The original current `main-scan.jl` uses exactly the *same* `dN_over_dt_pi(mPBH)*nPBH` in each of `dn_pi-/dt` and `dn_pi+/dt` (lines 103,109–112). Independent earlier T1 official BlackHawk 25/25 firstness Mech-S9, and 10/10 byte identity firstness REC13 ROT001, are preserved; neither is re-run here.

**Exact source result**: the literal modern Wu–Xu source *does* send its group-total pion producer into each separately named charge population, while using charge-specific reactions. Whether that matches a historical Kohri 2001 *implemented* convention is a different proof obligation.

## 2. C2 Kohri–Yokoyama 1999: definite numerical mismatch under matching-count interpretation

Direct original PDF text:
- Eq (10) defines `N_Hi = f_Hi <N_ch>/2` per jet with `<N_ch>` as *total charged particles per two jets* and `f_Hi` a species number fraction.
- Eq (11) gives `<N_ch> = 1.73 + 0.268 exp(1.42 sqrt(ln(s/Lambda²)))`, `Lambda=1 GeV`, approximately 10% data fit error.
- Eq (13) explicitly labels charged *per species* `n_pi+=n_pi-=14.1`; `n_K+=n_K-=1.67`; `n_p=n_pbar=0.772` at two jets, sqrt(s)=91.2 GeV, described as final yields from cited Table 38.1. Eq (14) computes `f_Hi=n_Hi/<N_ch>`. Paper says one must account for short-lived parent hadron decays, which may introduce definition/time-stage differences not audited here.

Independently evaluated the ORIGINAL Eq (11), not the owner supplied JSON/code:
`<N_ch>(91.2 GeV) = 20.82461855454813`.
Read literally as mutually exclusive final charged-state multiplicities, Eq (13) implies
`2*(14.1+1.67+0.772)=33.084`, ratio `33.084/20.82461855=1.5886965666784996` (158.87%).
Even pions `14.1+14.1=28.2` exceed `<N_ch>` by factor `1.35416646`.
The paper's stated ~10% fit error cannot by itself bridge this: `1.1*<N_ch>=22.907080410002948 < 33.084`, an absolute gap 10.176919589997048. A +58.87% upward shift would be needed.

If instead the apparent numbers `14.1, 1.67, .772` label corresponding *charge-pair totals*, their one-copy charged-group sum is `16.542`, ratio `0.7943482833392498` of `<N_ch>`; no direct charged-total contradiction. **This does not prove the alternative was actually the authors' intended semantics, and does not establish the physical normalization of all source channels.** In particular source counting at distinct hadron-decay stages, inclusive yields, or duplicate counting would alter the simple disjoint-particle bound; the full referenced PDG Table 38.1 and normalization-stage alignment were NOT independently accessed. Thus the finding is `C2_CONDITIONAL_INTERNAL_COUNT_MISMATCH_PASS`, NOT `KY1999_PUBLISHED_ERROR_PASS`.

## 3. C1 Kohri 2001: crucial inference separation (new claim-local guard)

Primary original PDF text, Kohri 2001:
- Eq (22),(23) individually labels `pi+` and `pi-` nucleon conversion coefficients, 1.7 mb and 1.5 mb times Coulomb correction, matching Wu–Xu's code.
- Fig. 5 caption explicitly plots **combined charge families** `pi+ + pi-`, `K+ + K-`, `p + pbar`, `n + nbar`, with `<N_ch>` as total charged multiplicity, all per **two jets**.
- Eq (34) uses a sum over individual hadron species `H_i` and `(Njet/2)*N^{H_i}*R^{H_i}_{N->N'}`. The following original text calls `N^{H_i}` the average number of the emitted species `H_i` and says `N^{H_i}` is presented in Fig. 5.

**Logical source problem**: From a published *charge-group total* `G_pi=N_pi++N_pi-` alone, two distinct possible species mappings remain:
(A) `N_pi+=N_pi-=G_pi/2` (additional charge-symmetry assumption), or
(B) `N_pi+=N_pi-=G_pi` (full group assigned per charge).
Both can refer to the same published group curve, but they yield distinct numbers in a species-summed reaction Eq (34). The checked Eq (34) and grouped Fig. 5 **do not present the charge-assignment operator explicitly**. Equation text saying a species number is "presented in Fig. 5" *suggests* a direct read, but by itself does not exclude an unstated group-to-state split. Without primary Kohri 2001 executable code, an explicit passage establishing A or B, or a matched authors' numerical calculation identifying the convention, it is unjustified to infer that the *historical implemented reaction* necessarily duplicated group totals.

The factor `Njet/2` in Eq (34) has a clearly distinct job: a group curve is defined per **two hadron jets**, and the model uses `Njet` jets per exotic decay. It is a jet-count conversion and does **not** denote the half charge state `1/2`. This preserves the key distinction `JETS_TWO_NORMALIZATION != CHARGE_PAIR_ALLOCATION`.

**C1 VERDICT**:
- `PASS` primary source for grouped curves and per-species cross sections/transition summand.
- `HOLD` that Kohri 2001 actually assigns the *full* group curve separately to each charge state.
- `NOT_ESTABLISHED` Badacz INPUT_075's stronger conclusion `SEMANTICS_ESTABLISHED_AS_LINEAGE_CONVENTION` based on those displayed equations alone.
- `NO_KOHRI_2001_IMPLEMENTATION_SOURCE`, not evidence of absence or proof of a physical/journal error.

This leaves Badacz's independent native T2 delta `+0.272..+0.301 dex` untouched as an *in-model counterfactual*. It cannot yet be interpreted as a verified difference between actual Wu–Xu historical published results and historical Kohri implementation/physical truth. Nor does it make Wu–Xu novelty or error claims.

## 4. Decision relevance and required owner action — no duplicate task

**Strongest supported result**:
`WUXU_CODE_GROUP_TO_EACH_CHARGE_SOURCE_PASS / KY1999_PRINTED_PER_STATE_COUNTS_VS_PRINTED_NCH_CONDITIONAL_MISMATCH_PASS / KOHRI2001_GROUP_FIGURE_TO_CHARGE_EQ34_IMPLEMENTATION_UNKNOWN`.

**Claim-local decision**: `PASS_WITH_GUARDS` for the quantitative mismatch and exact source identification; `HOLD` for the inferred lineage-wide duplication convention. Do not upgrade to `T3_INTENDED` or `T3_KNOWN_CORRECTION`, a critique of Wu–Xu's paper or a corrected PBH exclusion. Distinguish paper's descriptive chart from an *implemented charge-specific conversion operator*.

**Existing owner and cheapest reopen**: LT9 is ALREADY explicitly assigned by Badacz INPUT_075 to independently inspect Kohri 2001 Eq34/Fig5 and KY1999 Eq11/13; XH-S7 is optionally checking origin of 14.1 and Reno–Seckel. REC13 transmits this referee limitation to the existing LT9/XH-S7/Badacz/AUD3 return path; does not create a new task or override T3. `REOPEN_IF`: actual original Kohri 2001 code, explicitly defined `N_Hi` charge split from the cited source, original PDG Table38.1 stage-specific yield reconciliation, a source-proven Fig5-to-actual rate trace, or a specific source/document evidence undermining the arithmetic boundary.

`CUSTODY`: public source-only GitHub scientific record, not BW acceptance; `GITHUB_PENDING_BW_INGEST`. Source PDF screenshot request returned web cache-miss; article-body conclusions use directly indexed full primary PDF text (not screenshot-image validation), with reproducibility locators and explicit inspection limitations. No Julia/BlackHawk runs, no prior results rewritten, no book/LT/BW mutation, no I3 external blind, no CANON, NO_EXEC_SIGN.

FINAL: `REC13_ROT005_INPUT075_C2_ARITHMETIC_PASS_WITH_GUARDS / KOHRI2001_C1_LINEAGE_NORMALIZATION_NOT_ESTABLISHED / WUXU_GROUP_SOURCE_CODE_PASS / HISTORICAL_AND_PHYSICAL_B1_QB_CLAIM_HOLD / NO_NOVELTY_NO_CANON_NO_EXEC_SIGN`.
