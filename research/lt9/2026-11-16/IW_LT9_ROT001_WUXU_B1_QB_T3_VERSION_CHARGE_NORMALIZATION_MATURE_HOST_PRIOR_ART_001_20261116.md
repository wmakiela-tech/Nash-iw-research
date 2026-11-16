---
artifact_id: IW_LT9_ROT001_WUXU_B1_QB_T3_VERSION_CHARGE_NORMALIZATION_MATURE_HOST_PRIOR_ART_001_20261116
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_07 / LT9
created_at: 2026-11-16
as_of: 2026-11-16 Europe/Warsaw
document_type: LITERATURE_RECORD / BOUNDED_REVIEW
task_id: IW_BADACZ_B1_QB_T3_REQUEST_TO_LT8_001_20261116
exposure: PUBLIC
status: COMPLETE_BOUNDED_SOURCE_T3 / OWNER_INTERPRETATION_PENDING
claim_ceiling: NO_PAPER_ERROR_CLAIM / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
source_mode: DIRECT_PRIMARY_PUBLISHED_JCAP_AND_ARXIV_HTML_V2_V3 / AUTHOR_GITHUB_REST / CLASSICAL_PRIMARY_PRIOR_ART
execution: NO_NATIVE_JULIA / NO_BLACKHAWK_RUN / NO_NEW_NUMERIC_PHYSICS / NO_OWNER_CODE_EDIT
primary_evidence:
  - https://arxiv.org/html/2509.05618v2
  - https://arxiv.org/html/2509.05618v3
  - https://doi.org/10.1088/1475-7516/2026/02/063
  - https://inspirehep.net/files/9adbfbb35c345cc510bed18e66a36b55
  - https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole/issues?state=all
  - https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole/commits?per_page=20
---

# LT9 ROT001 — B1 Q-B / T3: independent charge-state prior-art and paper-version gate

## 0. Mandate and bounded verdict

This is the overdue T3 specifically requested of LT8 (or fallback XH) by Badacz on 2026-11-16, recovered and completed by its activated successor LT9. Responds to public `research/badacz/2026-11-16/IW_BADACZ_B1_G1_FREEZE_PROPOSAL_068_20261116.md` §3, `IW_BADACZ_B1_QB_T3_SOURCE_VERSION_COMPARISON_INPUT_073_20261116.md` and `IW_BADACZ_B1_STATE_AT_G1_SYNTH_074_20261116.md`. Badacz is hypothesis proposer, not the independent T3 judge. No new physical solver run or claim promotion.

**T3 result: PASS_WITH_GUARDS / PRIOR_ART_PER_SPECIES_CONVENTION_KNOWN / NO_EXPLICIT_PUBLIC_QB_CHARGE_CORRECTION_FOUND_IN_CHECKED_SURFACES / AUTHOR_INTENT_AND_PUBLISHED_PHYSICAL_EFFECT_UNRESOLVED.**

`T3-NOT-FOUND_BOUNDED` refers ONLY to an explicit public correction of the specific grouped-source-to-individual-reaction-state map in the checked journal/arXiv and author-repository surfaces. It is NOT `T3-PAPER_ERROR_PASS`, NOT proof of absence, NOT novelty clearance, and NOT proof that the authors' convention is unintended. The May v3 correction of a neutron-proton rate is independently real and not to be conflated with the Q-B claim.

## 1. Primary author-version results (independently opened; not inherited from INPUT_073)

**Published journal / JCAP 02(2026)063**, DOI https://doi.org/10.1088/1475-7516/2026/02/063 (published 2026-02-17): paper section 4.1, Eq. (4.4) enumerates N* for pi±, K±, K0L, p, n and explicitly says "these numbers include contributions of both particles and antiparticles" (publisher PDF around journal pp. 9-10; directly indexed full-text lines 563-573). Eq. (4.6) uses `n_j(Γ_j^dec+Γ_j^scat) ≈ n_BH dN_j/dt` with j in pi±, K±, K0L, and later anti-p/anti-n; Eqs. (4.7)-(4.8) use `n_j <σ_{n->p,p->n}^j v>`. Eqs. (4.9)-(4.12) give charge-selected meson cross-sections pi+, pi-, K-, not an explicitly declared grouped-charge-averaged cross-section. No explicit 1/2 split at that transition found.

**arXiv v2**, direct full HTML https://arxiv.org/html/2509.05618v2 (30 December 2025): independently checked section 4.1 Eq. (4.4) and the same explicit both-particles-and-antiparticles sentence; Eq. (4.6) grouped source; Eqs. (4.7)-(4.12) charge-specific listed cross-sections. No per-state split factor or explicit charge-group reweighting in those parts.

**arXiv v3**, direct full HTML https://arxiv.org/html/2509.05618v3 (6 May 2026): exact same substantive group-source and charge-specific formal definitions in §4.1-4.3. It newly acknowledges Boting Zhou for help correcting a minor mistake in neutron-proton conversion-rate calculation. The independently checked difference in Appendix B is material in the *weak-interaction matrix element derivation*: v2 Eq. (B.6) uses `32 G_F^2(g_V^2+3g_A^2) m_p^2 (p_nu · p_e)` times spin factor, whereas v3 Eq. (B.6) gives a distinct expanded vector/axial decomposition followed by rest-frame reductions (v3 B.7-B.9; v2 direct original HTML B.6-B.8). This substantiates a changed standard neutron-decay/weak-rate derivation. It does not establish that the group-to-charge mapping was corrected, or that figure 5 was unchanged numerically. No independently pixel-verified v2/v3 Fig. 5 parity claim here.

**arXiv v1**, https://arxiv.org/pdf/2509.05618v1: older text has the early grouped j notation in Eq. (4.6), but no later explicit 2025-12 addition's "both particles and antiparticles" phrase; later updated paper versions control Q-B paper interpretation.

## 2. Exact mathematical distinction

Let `S_G` be the total source for a conjugate pair `G={h_+,h_-}`. If the generator's output is group-total, the physical state sources obey `S_+ + S_- = S_G`. Under charge symmetry one obtains `S_+=S_-=S_G/2`. For a state-specific conversion process, the kinetic contribution is `Γ_{n->p}^{h_+}=n_{h_+}<σ^{h_+}v>`, not automatically `n_G<σ^{h_+}v>`. Applying full `n_G` to each of two distinct charge channels is a factor-two counting discrepancy *if* `n_G` is the group-total and the listed cross-sections are physical per-state cross-sections without group normalization.

This is a precise CONDITIONAL algebraic implication, not a proof of an error in the Wu-Xu published output. Charge symmetry/equal 1/2 allocation must itself be source verified for each channel; p/anti-p, n/anti-n, K± and pion state populations need not be numerically exchangeable without conditions. K0L is not to be divided by two merely because other columns are grouped. A deliberately group-averaged effective cross-section or an explicit change in the definition of `n_j` could remove apparent inconsistency, but was not stated at the inspected Eq. (4.6)->(4.7) interface.

**Semantic diagnostic**:
- `GROUP_TOTAL_SOURCE` is established at the author generator level by Mech-S9 T1 original BlackHawk v2.3 25/25 source match (T1 firstness belongs to Mech-S9, Moderator admitted technical retry).
- `INDIVIDUAL_STATE_REACTION` is the convention of the physical reaction cross-section labels at Eqs. (4.9)-(4.12).
- `TRANSFER_GAP` remains: no directly located statement that this source has already been divided per charge state, or that `σ^j` is averaged over group state probabilities, at that boundary.
- `PHYSICAL_EFFECT` not established by this literature review: needs authorized T2R, source-matched production semantics, independent referee and direct paper version/observable comparison.

T2 is AUTHOR/BADACZ native result, NOT LT9 execution: `IW_BADACZ_B1_QB_T2_NATIVE_CHARGE_NORMALIZATION_CONTOUR_REVIEW_071_20261116.md` (16 Nov): source-native `D_j` +0.2723 to +0.3007 dex (six masses), under E5 and specific solver convention; T1 T2 results are not automatically accepted published PBH limits.

## 3. Mature prior-art subtraction

(a) K. Kohri and J. Yokoyama (2000; preprint astro-ph/9908160), *Primordial Black Holes and Primordial Nucleosynthesis I: Effects of Hadron Injection from Low Mass Holes*, Phys Rev D 61, 023501, DOI 10.1103/PhysRevD.61.023501: meson/antinucleon-induced n↔p conversion under PBH hadron injection is established mature physics. This absorbs any novelty claim for the generic mechanism.

(b) M. Kawasaki, K. Kohri, T. Moroi (2005), *Big-bang nucleosynthesis and hadronic decay of long-lived massive particles*, Phys Rev D 71, 083502, DOI 10.1103/PhysRevD.71.083502; original source https://www2.yukawa.kyoto-u.ac.jp/~kazunori.kohri/allmypapers/kawasaki_kohri_moroi_2005.pdf, §VI.B Eqs. (6.8)-(6.10): `K_{N->N'} = Σ_{H_i} N^{H_i} P_{N->N'}^{H_i}` over explicitly enumerated `H_i=π+, π-, n nbar, p pbar`; `N^{H_i}` is species-associated averaged number per decay. This is a direct mature per-reaction-state construction and is a substantive prior-art counterexample to treating species-specific counting as a new methodological discovery.

(c) Carr, Kohri, Sendouda, Yokoyama (2010), *New cosmological constraints on primordial black holes*, Phys Rev D 81,104019, DOI 10.1103/PhysRevD.81.104019; original https://www2.yukawa.kyoto-u.ac.jp/~kazunori.kohri/allmypapers/CarrKohriSendoudaYokoyamaPRD81_2010_104019.pdf, interconversion section: charged pions and anti-nucleons are treated as distinct physical species. It supports maturity of the mechanism, not an exact Wu–Xu code audit.

None of these by itself establishes whether the exact author Wu–Xu v2.3 source-to-state map was already publicly diagnosed and corrected. The narrow source-specific empirical/code inconsistency would be a source-validated corrective claim only after separate original-code, author-interpretation, independent review and published-observable gates, not a new fundamental physics theorem.

## 4. Repository and correction search — executed bounded checks

On 16 Nov 2026 the original public author repo GitHub REST:
- `GET https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole`: default branch `master`, `open_issues_count=0`, latest `pushed_at=2025-12-30T15:30:13Z`.
- `GET https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole/issues?state=all&per_page=100`: `[]`, no public recorded issues in this queried endpoint.
- `GET https://api.github.com/repos/Fenyutanchan/Primordial-Black-Hole/commits?per_page=20`: head `d395183674cace6c9906a8911bdeb7234ba4040d`, 2025-12-30, subject "2509.05618: update to v2"; no later commit in this repository as inspected.
- Published DOI landing (17 Feb 2026), arXiv versions v2/v3, full journal PDF and targeted public queries for corrigendum/erratum did NOT return an explicit correction of the charge-group mapping. The v3 new acknowledgement is a concrete, real later change, not evidence that no other unpublished correction exists.

Search queries (public web, 2026-11-16; not exhaustive):
- `Wu Xu 2026 JCAP 02 063 primordial black holes BBN erratum correction neutron proton conversion pion kaon hadrons 2509.05618`
- `Fenyutanchan Primordial-Black-Hole github issues hadrons_from_PBH.dat charge normalization pipm pion multiplicities correction`
- `Kohri Yokoyama astro-ph/9908160 hadron injection meson neutron proton conversion pion kaon multiplicity`
- `site:iopscience.iop.org 10.1088/1475-7516/2026/02/063 corrigendum erratum`
- `"Primordial black holes evaporating before Big Bang nucleosynthesis" corrigendum erratum error`
- `site:github.com/Fenyutanchan/Primordial-Black-Hole/issues normalization hadrons`

Coverage limitation: publisher correction index not globally audited; authors' private correspondence/closed unpublished issues unavailable; exact v2/v3 Fig5 pixel comparison not done; no independent rerun of BlackHawk/Julia or T2. The attempted web PDF screenshots returned cache-miss, so PDF typography was not visually verified by the web screenshot utility; relevant mathematical text was independently corroborated by author arXiv HTML v2/v3 and publisher PDF text extraction.

## 5. Adjudication matrix and first action

| Question | Current answer | Caveat |
|---|---|---|
| Public source explicitly groups particles+antiparticles? | PASS, v2/v3/JCAP | Direct author text |
| Charge-selected cross sections in §4? | PASS | π+, π−, K− |
| Explicit 1/2 split at grouped-source-to-charge-state interface in §4? | NOT FOUND in inspected section | Not global absence |
| Mature hadron species-by-species n↔p reaction formalism? | KNOWN | Kohri / Kawasaki et al. |
| v3 materially changes Appendix B weak-rate derivation? | PASS | Does not directly resolve group normalization |
| Public Wu–Xu specific group-charge corrigendum or author GitHub issue? | NOT FOUND_BOUNDED | No novelty proof |
| Author intended a grouped effective cross-section? | UNRESOLVED | Require direct definition or owner/source decision |
| Physical +0.272...+0.301 dex shift as published-limit correction? | HOLD | T2R, REC/AUD, author version/observable |
| Contact author? | MODERATOR_DECISION_ONLY | No unilateral correspondence |

**Recommendation to Badacz + Mech-S9/Moderator**: treat T3 as `T3-NOT-FOUND_BOUNDED_WITH_DEFINITIONAL_TRANSFER_GAP` NOT `T3-KNOWN_CORRECTION` and NOT `T3-INTENDED`. Preserve 30-day B1 source gate and avoid premature journal-error language. Next pre-approved route: Mech-S9 T2R and independent REC12/AUD2 once returned; for source correctness, request one bounded explicit definition from author/source if available. Do not initiate new native experiments or mass-scan. `REOPEN_IF`: an actual post-v2/v3 correction, author intent evidence, charge-tagged source rates, T2R failure, or refereed source-level alternative.

## 6. Custody and status

Origin LT9 after Moderator activation; former LT8 direct inbound T3 discharged in limited source-verification scope. This PUBLIC document is not a canon claim, BW scientific ingestion, scientific acceptance, or publication of a physical corrected PBH bound. Reviewer and Moderator control all downstream adoption. Source URLs are public; no private cross-surface fallback. No change to seven-chapter Living Theory REV029.
