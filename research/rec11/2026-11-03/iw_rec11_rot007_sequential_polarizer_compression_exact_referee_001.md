---
artifact_id: IW_REC11_ROT007_SEQUENTIAL_POLARIZER_COMPRESSION_EXACT_REFEREE_001_20261103
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_10 / REC11
date: 2026-11-03
review_type: BOUNDED_NONBLIND_MATH_AND_SOURCE_TYPED_REFEREE
target: Moderator-routed LT7/KN12/REC11/PRF12/AUD1 sequential polarization candidate from #iw-dispatch 2026-11-03 08:38:07 CET
source: Flavio Del Santo, arXiv 2610.20752 (historical paper: abstract verified; complete primary PDF historical identification NOT verified)
class: PASS_EXACT_COMPRESSED_DEFECT / REPAIR_GLOBAL_OPERATOR_DOMAIN / PASS_FIXED_ORIENTATION_NEGATIVE_CONTROL / HOLD_HISTORICAL_FIDELITY
claim_ceiling: AUXILIARY_CLASSICAL_MEASURE_KERNEL / NO_HISTORICAL_AUTHENTICATION / NO_QUANTUM_NOVELTY / NO_CANON / NO_EXEC_SIGN
bw_state: NOT_VERIFIED
---

# REC11 ROT007 — independent sequential polarizer compression audit

## Decision and source precedence

**PASS core math, exact** for the explicitly declared *auxiliary classical model*: the original `-1/4` operator-compression defect is correct, the sequence order is correctly interpreted, and the positive and negative controls separate orientation updates from scalar threshold composition.

**MATERIAL REPAIR** to any unqualified formulation of the operators on *all* finite Borel measures: when `cos²(beta-alpha)=0` and `lambda=1`, the prescribed passing test `lambda>=sin²(beta-alpha)=1` accepts an atomic point but the update `lambda'=(lambda-1)/(1-1)` is undefined `0/0`. Restrict to atom-free (e.g. absolutely continuous in lambda) preparation/signed-measure class with a zero-transmission convention for orthogonal settings, or specify a mathematically consistent endpoint convention for atomic measures. The given uniform initial preparation and its reachable signed combinations are safe; this is a *domain* repair, not a refutation of the `-1/4` result.

**HOLD historical source fidelity**: the original arXiv abstract of Del Santo, *Schrödinger's unpublished hidden-variable model in the 1944–45 debate over the "Collapse of Determinism"* (arXiv:2610.20752, submitted 2026-10-14) was confirmed. Its abstract states a historical model and characterizes it as a proof of principle, not a commitment to determinism. Full author PDF/transcription and the precise historical sequential-map definitions were **not** authenticated in this turn. The user-routed model is explicitly its own auxiliary mathematical construction; this referee does not attribute the complete operator semigroup to the historical manuscript. No physical identification or novelty is authorized.

## Exact mathematical object

Take state space `Omega=(R/piZ)×[0,1]`; angle `alpha` is a polarization orientation and `lambda` is a hidden scalar. A setting `beta` has
`a(alpha,beta)=sin²(beta-alpha)`, `c(alpha,beta)=cos²(beta-alpha)=1-a`.
For `c>0`, accept `lambda>=a` and output `(alpha',lambda')=(beta,(lambda-a)/c)`. Let `M_beta` be the corresponding unnormalized pushforward on legally admitted finite signed measures; `P` be the total mass; and `J(r)=r delta_H tensor U[0,1]` for fixed preparation `H=0`. Then `PJ=Id` and `JP` is an idempotent reset onto the one-dimensional prepared family.

For uniform input lambda, the exact direct integral gives
`M_beta J(1)=cos²(beta-H) delta_beta tensor U[0,1]`
and `C(M_beta)=PM_beta J=cos²(beta-H)`. This is a *mass* compression, not a source-autonomous propagator on all hidden input states. For any two settings `beta,gamma`,
`P M_gamma M_beta J = cos²(beta-H)cos²(gamma-beta)`,
`C(M_gamma)C(M_beta) = cos²(gamma-H)cos²(beta-H)`.
Therefore the **exact orientation-memory defect** is
`Delta(beta,gamma;H)=cos²(beta-H)[cos²(gamma-beta)-cos²(gamma-H)]`.

At `H=0, beta=45deg, gamma=H`:
`P M_H M_45 J=1/4`, whereas `(P M_H J)(P M_45 J)=1/2`. Thus
`P M_H (I-JP) M_45 J = 1/4-1/2 = -1/4`.
Explicitly `nu=(I-JP)M_45J = (1/2)(delta_45-delta_H) tensor U[0,1]` has total signed mass 0, while `P M_H nu=-1/4`. Hence `ker P` is not stable under `M_H`, and `PM_H` does **not** factor through total mass P on the whole reachable signed space. No new physics is claimed: this is a standard failed-factorization witness for a Markov substochastic kernel.

### Sequence, boundary, and input law falsifiers

1. **Operator order matters for the orientation-changing model.** `P M_H M_45 J=1/4`, but `P M_45 M_H J=1/2`. For three events (45°, H, 45°) the actual mass is `1/8`, while the product of individually compressed scalar maps at fixed H is `1/4`. This is *classical context dependence*, not proof of quantum noncommutativity.
2. **Fixed-orientation negative control PASS.** If only a normalized scalar lambda is filtered at thresholds `a,b` with update `lambda'=(lambda-a)/(1-a)`, composing two filters gives effective threshold `a⋆b=a+b-ab` and normalized update `(lambda-(a⋆b))/(1-a⋆b)`; `a⋆b=b⋆a`. For uniform initial lambda, both survive with probability `(1-a)(1-b)`, so this *different* semigroup has zero scalar compression defect.
3. **Nonuniform input falsifier.** If the initial lambda density is `2lambda`, setting `a=1/2` transmits mass `3/4`, not the uniform-source `1/2`. Its post-transmission conditional mean of lambda' is `5/9`, not the uniform mean `1/2`. Uniform reset from filtering is therefore conditional on the input/source distribution.
4. **Orthogonal setting requires a domain guard.** At `a=1,c=0`, for uniform lambda the accepted event is measure zero and the output measure is naturally zero. But for an atomic input `delta_{lambda=1}`, the literal `>=` acceptance rule selects the atom and asks for an undefined `0/0` update. Do not claim an everywhere-defined linear operator on *all* finite signed measures without a zero-branch convention or a suitable atom-free domain.
5. **`I-JP` is not positivity-preserving.** The defect is a signed cancellation between the original sequential experiment and a counterfactual reset-to-H experiment; its numerical value `-1/4` is not a negative transmission probability.
6. **Sufficient autonomy criterion.** A compressed scalar target would be autonomous if `P M_beta(I-JP)=0` for the relevant beta and legally reachable inputs (equivalently `P M_beta=C(M_beta)P` on the chosen linear state space). The witness above violates it. A known initial hidden state or a preparation-aware compressed object could change the target contract.

## Independent exact reproducibility

An independent **Python stdlib-only** one-file verifier was executed with Python `fractions.Fraction`:
- 48 exact integral-moment equalities (thresholds 0,1/4,1/2,3/4; moments k=0..11) prove that the accepted/rescaled uniform measure returns the uniform law, multiplied by acceptance mass;
- 16 exact fixed-orientation threshold pair compositions;
- exhaustive 36 two-stage and 216 three-stage sequences over orientations modulo 180° at 30° spacing; of these, **20/36** two-stage and **142/216** three-stage sequences have nonzero discrepancy between the actual sequential mass and the naïve product of scalar compressions;
- exact main `1/4 - 1/2=-1/4`, reversed `1/2`, three-stage `1/8`, orthogonal and identity boundary probabilities, and `2lambda` distribution counterexample.

One-file verifier SHA256:
`e376974a4be17383b50f9970ca0740ef4114579a34a5049d056ee509a86f665c`.
Exact frozen JSON SHA256:
`c95850c87dba56e216c5d5d472403ea87e1c723f70f6c48f90183b0fb5c146d2`.
Both are local artifacts in the current REC11 conversation. Their hashes identify those artifacts; GitHub hosting is NOT claimed unless separately confirmed.

## Additional owner-requested REV029 delta pin

LT7 asked REC11 to check new forensic register M of native REV029:
`AHj4eMSXmR7pDX_HVgr5S0n9U4eAteQQ_wJniSn9ARzrfCi3N5-maBwfZFIxT0wRSUNiP-UM62FFz9cEXixQCPzqTT-cwae4cAOa-OOHBiA`.
Direct native read returned **1762 paragraphs, zero TAB/VT**. Historical REV028 was reread at unchanged native revision, 1684 paragraphs; lexical old-to-new alignment with offset 1 found **1660/1684 unchanged and 24 changed**, exactly as owner reports, with changes concentrated in §7.5 (16), §7.6 (7), §7.7 (1). The previously passed §7.6 corrected modulus formula and REVIEW047 currentness in annex are unchanged; no new mathematical repair required in this delta. Forensic register M is explicitly a bounded *lexical scan only*, not historical pre-import TeX proof. **PASS_DELTA_REGISTER_M_CURRENTNESS / HOLD_AUTHENTIC_ORIGINAL_TEX / HOLD_KN12_BW**. REC11 ROT005 math approval remains limited to its prior native pin; unchanged body permits carry-forward to this pin for §7.6 only.

## Verdict and downstream scope

**`PASS_EXACT_AUX_MODEL / REPAIR_ORTHOGONAL_ATOM_DOMAIN / PASS_FIXED_ANGLE_CONTROL / PASS_REV029_REGISTER_M_DELTA / HOLD_HISTORICAL_SOURCE / HOLD_BW_CUSTODY / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN`.**

The recommended minimal wording for LT7/PRF12 if this becomes a book example: label the state and preparation injection J, specify signed-measure linearity and a convention for zero-transmission settings, state the ordinary kernel compression identity, and make clear that the negative defect tests a reset-to-H scalar closure. Separate historical text verification and independent acceptance by AUD1/Badacz. No owner-only book edit or automatic BW write undertaken.

## References

- Moderator-routed #iw-dispatch candidate 2026-11-03 08:38:07 CET; mathematical definitions and prior ROT001–004 claims are those of the routed request.
- Del Santo arXiv: https://arxiv.org/abs/2610.20752 (historical-source abstract and bibliographic metadata checked; full transcription unverified).
- LT7 private REV029 native document ID `1V6ZNt32WaxTrBrFQeTgIB73nalA2OSo6oKqTKKuTsEQ`; source material not replicated in public report beyond claim-local types and scope.
- REC11 ROT005 preceding limited review: https://github.com/wmakiela-tech/Nash-iw-research/blob/b761eea52badf4c18ff7eb0ffd48fd362e3ae255/research/rec11/2026-11-03/iw_rec11_rot005_lt7_rev029_section76_review047_owner_delta_referee_001.md
