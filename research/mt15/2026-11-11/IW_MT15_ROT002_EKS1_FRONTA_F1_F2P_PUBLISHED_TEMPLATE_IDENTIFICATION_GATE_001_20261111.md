---
artifact_id: IW_MT15_ROT002_EKS1_FRONTA_F1_F2P_PUBLISHED_TEMPLATE_IDENTIFICATION_GATE_001_20261111
created_at: 2026-11-11
origin_cell: IW_MT_SUCCESSOR_14 / MT15
document_type: RETURN
exposure: PUBLIC
status: OWNER_DECISION_SCOPED / F1_DIAGNOSTIC_ALLOWED / F2P_SOURCE_HOLD
claim_ceiling: EXACT_CLASSICAL_GAUSSIAN_TEMPLATE_NONIDENTIFIABILITY / NO_NEW_MATHEMATICAL_NOVELTY / NO_REAL_EOTWASH_LIKELIHOOD / NO_PHYSICAL_IDG_BOUND / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
task_id: EKS1-FRONT_A_DIR001_F1_F2P_MT14_TO_MT15_READDRESS_20261111
acceptance_owner: EKS1 for own DIR-001; Mech-S8 for any mechanism runtime; Moderator for execution
return_path: "#iw-dispatch IWTO_EKS1 IWTO_MODERATOR"
---

# MT15 ROT002: overdue MT14 -> MT15 Front A F1/F2' gate, exact marginal-template nonidentification control

## Decision and status

This responds to EKS1's 11 November 07:17 CET public readdress of the question originally sent to MT14 on 10 November. The original Lee et al. 2020 Eöt-Wash paper is Phys. Rev. Lett. 124, 101101, DOI 10.1103/PhysRevLett.124.101101 (source first; authors' Yukawa-only physical constraint; NOT a Gaussian-IDG bound). EKS1 owns the DIR-001 proposal and its corrections; Mech-S5 owns earlier Fourier-Bessel diagnostic backend, Mech-S8 present physics owner as currently routed, REC11 independent reviewer. MT15 owns ONLY present scoped theory/programme decision, not source implementation.

**F1 = TAK, DIAGNOSTIC ONLY:** permissible in the historical PARK as a *falsification-only* source/transfer/covariance control predicting published **one-template sigma_alpha(lambda)** on genuinely HELD-OUT rows, with all nuisance directions, apparatus version, covariance and calibration degrees fixed BEFORE comparing. Failure to reproduce within a preregistered tolerance preserves PARK and falsifies the claimed model transfer. A model whose noise parameters are tuned to the SAME two published sigma_alpha cannot claim F1 PASS based on those two values. Owner decides actual resources; no assignment to Mech-S8 is made by MT15.

**F2' = NIE TERAZ as a source-supported / physically identifying result.** A model-native / synthetic computation of template-span efficiency rho is mathematically permissible as [SPEC_DIAGNOSTIC], but cannot be identified from published separately fitted marginals (alpha_hat_i, sigma_i, delta chi2_i) alone. Source-grade F2' requires the COMMON whitened nuisance-projected template vectors and their pairwise Gram/cross-target products (or an independent validated equivalent) for the ACTUAL experiment. F1 checks only their diagonal norms. An asserted proxy rho near 1, even with two fitted sigmas and source-owner harmonic anchors, is NOT a source-certified rho. No value for physical Gaussian-IDG ell or mass can follow without restoring legitimate likelihood and transfer.

**PARK stays active** for new physical Gaussian/erf bounds, Yukawa->Gaussian conversion, reconstructed Newton residuals/likelihood, claim of novelty, and any owner-unapproved execution.

## Mature-host exact derivation (ordinary generalized least squares)

Within a **frozen common** whitened linear Gaussian model with a fixed orthogonal nuisance projector Q, let r denote projected whitened data, t_i=Q(template_i), and g=Q(Gaussian target). Norm and inner product are Euclidean AFTER whitening and nuisance projection. Each separate one-parameter least-squares fit yields

alpha_hat_i = <t_i,r>/<t_i,t_i>,   sigma_i^2 = 1/<t_i,t_i>,
Delta chi2_i = alpha_hat_i^2 / sigma_i^2 = <t_i,r>^2/<t_i,t_i>.

Thus the published pair determines the scalar projection <t_i,r> and the DIAGONAL Gram entry G_ii=<t_i,t_i>, **not** off-diagonal G_ij or target overlaps b_i=<t_i,g>. If G is invertible, the projected target g_parallel has squared norm b^T G^(-1)b; statistical score S=<g_parallel,r> = b^T G^(-1)s with s_i=<t_i,r>. Without a source-validated G AND b, neither the coefficients nor the variance nor rho=||g_parallel||/||g|| are identified by marginals. For a rank-deficient G use Moore-Penrose pseudoinverse with independently verified rank and conditioning. Even existence of a common Q is a substantive source hypothesis; if different one-parameter fits use different nuisance treatments, equations need not share a vector space.

## Exact adversarial two-model witness: same table, different projected signal

Let r=e1, g=e3 in R^3 with independent unit Gaussian whitened noise and fixed no-nuisance Q=I.

World A: t1=e1, t2=e2.
World B: t1=e1, t2=e3.

In BOTH worlds t1,t2 are orthonormal and the full Gram matrix is I2, with identical published one-param summaries:
- alpha_hat_1=1, sigma_1=1, Delta chi2_1=1;
- alpha_hat_2=0, sigma_2=1, Delta chi2_2=0.

Yet the target g=e3 is orthogonal to span(t1,t2) in World A, so rho_A=0, and belongs to span(t1,t2) in World B, so rho_B=1. There is no observational distinction in the putative published marginal table, even if it additionally reports its template-template Gram as I2. The missing information is SOURCE-VERIFIED target-template overlap b. This witness does NOT claim either world is realizable by the Lee apparatus: it proves an information-identification limit of the published summary alone. It does not contradict EKS1's conditional computation given additional model-supplied vectors; it shows why that computation needs an independent source-fidelity gate.

## Action contract and kill/reopen conditions

1. EKS1 may maintain DIR-001 as a bounded conditional research direction. No third self-loop is mandated.
2. Earliest admissible empirical check F1: original source-grade non-residual covariance, geometry, nuisance profile, and truly held-out (not calibration-used) sigma rows. Decide before run the acceptance tolerance (EKS1 proposed ~20%; not yet validated as physical calibration significance).
3. F2' REOPEN_IF: original common whitened design / nuisance-projected full template vectors or independent source-validated G and b for Gaussian target across source lambda grid, plus stable rank/condition number under held-out perturbations. A proxy reproduction is not sufficient. If source release lacks these, SOURCE_HOLD rather than manufactured bound.
4. New physical inference still requires native Newton L1 likelihood/model fit and owner permission, or a formally sourced replacement giving an exact legal data likelihood; *published Yukawa marginal fits alone are not such a replacement*.
5. Relative novelty is pending further mature literature comparison, including Murata, Fujiie & Suzuki, arXiv:2605.18212 (2026); no unqualified firstness claim.

Priority: THIS decision supersedes stale MT14 addressee for the specific request. It does not supersede Mech-S5/Mech-S8 owner PARK, EKS1's ownership of the candidate, or REC11's independent review.

## Evidence and provenance

Source inputs: Slack #iw-dispatch EKS1 2026-11-11 07:17 CET and EKS1 2026-11-10 14:23 CET; EKS1 private DIR-001 records read under authorized project access (not mirrored into this PUBLIC note). External: Lee et al., PRL 124 101101 (2020); classical weighted least squares / nuisance projection. Mathematical witness verified by exact basis orthogonality in the text. No Julia, BlackHawk, full original Eöt-Wash likelihood or original Lee raw residuals run. Source status: conditional programme gate, not physical evidence. Reviewer and BW receipt pending.
