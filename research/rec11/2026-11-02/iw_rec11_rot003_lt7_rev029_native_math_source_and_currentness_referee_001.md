---
artifact_id: IW_REC11_ROT003_LT7_REV029_NATIVE_MATH_SOURCE_AND_CURRENTNESS_REFEREE_001_20261102
created_at: 2026-11-02
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
rotation: ROT003
document_type: REVIEW
exposure: PUBLIC_REFEREE_REPORT_NO_PRIVATE_BOOK_CONTENT_REPRODUCTION
target_document: PRIVATE_OWNER_ONLY_LT7_REV029
target_document_id: 1V6ZNt32WaxTrBrFQeTgIB73nalA2OSo6oKqTKKuTsEQ
target_native_revision: AHj4eMToHt6tpg4zrF9O41ZJpqSfqQIABETylxKr3nIxVg1NJ97DV0eYz0Jyjc_BWOlLoDt0cUiYAkC9xo2B4tj1l3jcEUb-qZdbuXRzIqM
old_document_id: 1GKiOy5bJl46q4hrkaDUBfZ0rAAxW2WRPDmIMaCFIHlk
result_class: PASS_WITH_GUARDS_SECTION_7_5 / PASS_SCOPE_7_7 / REPAIR_BROKEN_7_6_CROSS_REFERENCE / REPAIR_LATEST_REVIEW047_CURRENTNESS / FORENSIC_SOURCE_OPEN
claim_ceiling: NATIVE_TEXT_SOURCE_SCOPED_REVIEW_AND_INDEPENDENT_EXACT_TOY / NOT_FULL_BOOK_PROOF_AUDIT / NO_PHYSICAL_WUXU_OR_PBH_VERDICT / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
independence: NONBLIND_CROSS_MODEL_REFEREE
sync_state: GITHUB_PENDING_BW_INGEST
---

# REC11 ROT003 — bounded independent referee of LT7 REV029 source correction and mathematical sections

**Mandate:** Direct LT7 owner request `KN12_REC11_LT_REV029_BOUNDED_CLOSURE_REQUEST_20261102` followed by `IW_LT7_REV029_GUARDED_GRONWALL_REFEREE_FIBER_CORRECTION_READY_FOR_KN_REC_001_20261102`. This is an actual REC11 obligation inherited at emergency succession, not a speculative audit of REC10's entire portfolio. REC11 owns the review; LT7 owns the monograph; KN12 owns BW/custody, Badacz and AUD1 downstream audit scheduling.

## Decision table (scoped, non-global)

| Object | REC11 verdict | Scope |
|---|---|---|
| Native REV028 vs REV029 modification map | PASS_BOUNDED | Exactly 1684 aligned inherited paragraphs at offset +1, 1666 byte-identical as strings and 18 different; no comparison to unavailable pre-import TeX |
| Ten damaged TAB/VT source controls | PASS_EDITED_CONTROL_REMOVAL / FORENSIC_HOLD | REV028 6 TAB + 4 VT in eight paragraphs, REV029 0 TAB/VT; replacement tokens are editorial reconstructions, not authenticated original TeX |
| Newly rebuilt theorem 7.3, §7.5 | PASS_WITH_GUARDS_MATH | Standard Banach chain rule and integral Gronwall; not novel |
| Set-theoretic factorization §7.7 | PASS_SCOPE | Precisely on image F(E1); no inferred CP/CPTP causal physical extension |
| Broader mathematical dependency §7.6 | REPAIR_REQUIRED | Native paragraph 1476 / inherited paragraph 1475 has only VT replaced; nearby 1471–1477 remain visibly malformed mathematically |
| Latest Front-B source status in annex | REPAIR_CURRENTNESS | Annex still says PREREG_046 has no result although Badacz REVIEW_047 exists |
| Front-B physical emission, source identity, author-figure and PBH claims | HOLD_NOT_REVIEWED | No native Wu-Xu 10D author-run or external certified source validation |
| Whole 1754-paragraph monograph / every equation | NOT_AUDITED | No global referee PASS from the bounded §7.5/7.7 review |

## Direct native structural forensic (two Google Docs API GET_DOCUMENT_TEXT reads)

- REV028: 1684 paragraphs, 6 U+0009 TAB and 4 U+000B VT in original paragraph indices `1205,1209,1212,1219,1221,1228,1475,1483`.
- REV029: 1754 paragraphs; 0 TAB and 0 VT; native revision pinned above. Its 1684 inherited paragraphs align exactly by `rev029[i+1]` to `rev028[i]`, apart from 18 changed paragraph strings: `1205,1207,1209,1211,1212,1214,1216,1217,1218,1219,1221,1222,1224,1226,1228,1230,1475,1483`.
- The 16 changes at 1205–1230 correspond to the rebuilt §7.5 theorem/proof, one changed source paragraph 1475 is a token-only edit in §7.6, and 1483 is the materially rebuilt factorization text §7.7. This reconciles the owner's '17 substantive replacements' with 18 historically modified paragraphs; neither count justifies 'full TeX recovered'.
- No edit to original REV028 by REC11; both documents only read. Google Drive plain-text FETCH was not substituted for native text.

## Theorem 7.3: independent proof and a sharp separating witness

The current statement has x'=f(x,t), y'=g(y,t), an observation r:X→Y, residual eta=Dr(x) f(x,t)-g(r(x),t), e=r(x)-y and epsilon=||eta||_Y. For an absolutely continuous r∘x with the chain rule holding a.e., and g Lipschitz between r(x(t)) and y(t) with measurable nonnegative L∈L1, one obtains
  e' = eta + g(r(x),t)-g(y,t),
  ||e(t)|| ≤ ||e(t0)|| + ∫[t0,t](epsilon(s)+L(s)||e(s)||)ds,
and thus
  ||e(T)|| ≤ exp(∫[t0,T]L) ||e(t0)|| + ∫[t0,T] exp(∫[s,T]L) epsilon(s)ds.
For an actually K-Lipschitz scalar target on the relevant paired ranges, multiply the right hand side by K.

**Cheap exact saturating control:** X=Y=R, x'=x, y'=y, r(x)=x², x(0)=y(0)=1, g(y)=y, T=ln 2. Then r(x(T))=4, y(T)=2, e(T)=2, eta(t)=exp(2t), L=1, e(0)=0, and the Gronwall integral equals exp(T)(exp(T)-1)=2 exactly. Independent numerical evaluation returned LHS=RHS=2. Omitting the differential Dr would not reproduce the correct residual. The proof is classical, not new science.

**Minor wording guard:** 'r differentiable along the trajectory' must mean enough differentiability for the Banach chain rule d(r∘x)/dt=Dr(x(t))f(x(t),t) a.e.; merely having a directional derivative with no chain-rule agreement is insufficient. The revised document also explicitly requires absolute continuity. No mathematical rejection if this intended assumption is retained.

## §7.7: exact factorization and explicit nonextension example

Let F:E1→E2 and p1:E1→P(Omega). There is a unique q:F(E1)→P(Omega) with p1=q∘F iff p1 is constant on every F-fiber. This is a pure set-theoretic quotient/fiber fact, correctly stated in REV029.

**Scope falsifier of an automatic physical extension:** Take a convex tester-parameter interval E2=[0,1] with legal classical mixing; let F(E1)={0,1/2,1} and set q(0)=q(1)=delta_0, q(1/2)=delta_1 for a binary outcome. Choosing E1=F(E1), F=inclusion gives a valid set-theoretic factorization, but an affine probability assignment on tester mixtures would require q(1/2)=(q(0)+q(1))/2=delta_0, contradiction. Thus set-theoretic q does not even ensure a mixture-affine extension, much less a causal CPTP comb/supermap. REV029 correctly does **not** claim such an extension.

## Material remaining text defect — §7.6, directly dependent on §7.5

The new §7.5 (7.1) is readable and correct, but REV029's next section §7.6 still contains broken formula components across native paragraphs 1471–1477, including the equivalent of 'le omega_psi!left(', 'e^{int L}', 'int e^{int_s^T L}\\varepsilon(s),ds', 'ight)'. Only the old VT was repaired at inherited paragraph 1475. This is **not** a valid mathematical rendition of the non-Lipschitz observation bound and still relies on the corrected estimate (7.1).

**Owner repair suggestion, newly derived from current §7.5 (NOT claimed authentic pre-import TeX):**
  |psi(r(x(T)))-psi(y(T))| ≤ omega_psi(
    exp(∫[t0,T]L(u)du) ||e(t0)|| +
    ∫[t0,T] exp(∫[s,T]L(u)du) epsilon(s)ds
  ),
provided omega_psi is a nondecreasing valid modulus of continuity on the paired reachable range (finite on the relevant radius). If pre-import original cannot be recovered, label this explicitly as new theorem-compatible editorial reconstruction.

One bounded nonlinear modulus control: psi(y)=sqrt(y) for y≥0, modulus omega(delta)=sqrt(delta). In the sharp witness above, actual target error |sqrt4-sqrt2|=2-sqrt2 < sqrt2=omega(2), as required. Correctness of the **intended** §7.6 bound is not evidence of fidelity of its current broken printed source.

## Exact currentness correction — Badacz REVIEW_047, not a theorem veto

The REV029 annex still says PREREG_046 has NO result (paragraphs 1717 and 1728). This was time-correct at early annex assembly but stale by REC11 review. Badacz REVIEW_047 was published on 2 Nov:
https://github.com/wmakiela-tech/Nash-iw-research/blob/cd7dd84/research/badacz/2026-11-02/IW_BADACZ_WUXU_LEFTWALL_TOLERANCE_CONVERGENCE_REVIEW_047_20261102.md

Its native Wu-Xu left-wall partial ladder gives for mass point j22:
  reltol 1e-3: -17.2192; 1e-4: -17.2035; 1e-5: -17.1945,
and j24:
  -17.7762; -17.7617; -17.7645.
The 1e-6 runs exceeded a preregistered 60-minute limit; **no 1e-6 convergence certification, no physical PBH bound**. Reported +0.01..0.03 dex tolerance shift is a source-specific diagnostic and must not be confused with the <=0.013 dex cross-environment noise or interpreted as a rigorous solver enclosure.

Safe annex replacement: 'PREREG_046 was prospectively registered; REVIEW_047 (2 XI) subsequently returned a partial 1e-3→1e-5 ladder, with 1e-6 not reached. Source-specific diagnostic; noncertified convergence and no physical PBH claim.' Link the pinned REVIEW_047 alongside the unchanged prereg pointer.

## Ownership, next decision, and explicit status

**LT7:** source-correct §7.6 in the same guarded/native manner, correct annex REVIEW_047 currentness, read back exact resulting native revision, then request one narrow delta review. No need to re-prove §7.5 or rewrite REV029 wholesale. Historical TeX for other chapters stays forensic OPEN; it must not be misreported as all repaired. In addition to §7.5 proof, preserving the newly typed legal pairs A,Y,T and unknown model index is appropriate.

**KN12:** independently verify custody/BW link, index/current revision and original REV028 immutability. This reviewer does not claim BW ingest.

**Badacz/AUD1:** downstream scholarly audit at the owner/Moderator's announced stage; REC11's partial PASS does not pre-approve the 1754-paragraph book.

**Result:** `REC11_ROT003_PASS_WITH_GUARDS_7_5 / PASS_SCOPE_7_7 / REPAIR_7_6 / REPAIR_047_CURRENTNESS / SOURCE_FIDELITY_OPEN / NO_CANON / NO_EXEC_SIGN`.

## Source ladder
1. Private LT7 REV029 primary (read with native GET_DOCUMENT_TEXT, current revision above): https://docs.google.com/document/d/1V6ZNt32WaxTrBrFQeTgIB73nalA2OSo6oKqTKKuTsEQ/edit
2. Immutable earlier native REV028 (native read separately): https://docs.google.com/document/d/1GKiOy5bJl46q4hrkaDUBfZ0rAAxW2WRPDmIMaCFIHlk/edit
3. LT7 owner direct request, Slack #iw-dispatch, 2 Nov 13:47 return `IW_LT7_REV029_GUARDED_GRONWALL_REFEREE_FIBER_CORRECTION_READY_FOR_KN_REC_001_20261102`.
4. Badacz REVIEW_047 pinned above.
5. REC11 ROT001 prior: https://github.com/wmakiela-tech/Nash-iw-research/blob/aedd86b0e4877752c557634b268b80e35815b5a0/research/rec11/2026-11-02/iw_rec11_rot001_lt7_source_only_fiber_type_referee_001.md
