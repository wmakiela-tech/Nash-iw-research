# M13 rotation 02 — Front B finite-point vs interval source certificate

﻿IW / M13 ROTATION 02 — Front B source agreement
RETURN_ID: M13-ROT02-FRONTB-FINITE-POINT-VS-INTERVAL-CERTIFICATE-001
DATE: 2026-10-12
STATUS: EXACT LOCAL MATHEMATICAL CONTROL / NO EXEC_SIGN / NO CANON / NO PBH BOUND
FROM: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13


CURRENT INPUT: XH-S3 source-harvest 023 introduced a QCD-curved stress prior and warned the E0 fixed edge power is not an exact terminal law. Mech-S6 proposed point checks near 6e8, 3e8, and 1e8 grams. MT13 ROT19 derives weighted bounds for declared power stress. The gap: success at a finite collection of regenerated masses cannot alone certify the entire interval.


THEOREM A — NEGATIVE FINITE SAMPLE RESULT.
On finite I=[M_low,M_edge] with M_low>0, let q0>0 smooth and samples M_i finite. Pick a smooth nonnegative bump phi(t) supported between samples, max phi=1, where t=ln(M/M_edge). For any A>0 set qA(M)=q0(M)*exp(A*phi(t)). Then qA(M_i)=q0(M_i), but max_I(qA/q0)=exp(A), arbitrarily high. Thus POINTWISE_SOURCE_PASS != INTERVAL_SOURCE_PASS. If the fixed positive weight overlaps bump support, even its weighted yield can change arbitrarily. This is an interpolation counterexample, not a claim about physically legal PBH spectra.


THEOREM B — CONDITIONAL INTERVAL CERTIFICATE.
For positive admitted species source qreg, q0 define f(t)=ln(qreg/q0), t=ln(M/M_edge). Assume on the WHOLE admitted interval |f(t)-f(s)|<=L|t-s| and sampled |f(t_i)|<=eps_i. Then triangle inequality yields:
|f(t)|<= min_i[eps_i+L|t-t_i|] = B(t).
If eps_i<=eps and rho=max_t min_i |t-t_i|, then |f(t)|<=eps+L*rho, so:
exp(-eps-L*rho) <= qreg/q0 <= exp(eps+L*rho).
If sampling includes both interval endpoints and maximal log-mass gap is Delta, rho<=Delta/2; otherwise include the uncovered boundary gaps.


FIXED-KERNEL TRANSPORT.
If fixed weight K(M)>=0 uses the SAME mass clock and is nonzero in the integrated interval, then the corresponding positive weighted integral ratio lies between exp(-eps-L*rho) and exp(eps+L*rho). For signed fixed K, only absolute bound:
|Ireg-I0| <= [exp(eps+L*rho)-1]*integral |K| q0 dM.
These results fail as a ready-made certificate if source changes clock, state response, nuisance or target kernel.


LEGALITY / SCIENTIFIC LIMITS.
L must be independently justified for each species pi/K/p/n and the same source/units/hadronization contract. Total jet multiplicity asymptotics do not establish a source-matched finite L for individual species. E1b QCD-curved prior is stress only; neither sample data nor valid L were generated here. No target-specific Yp/DH result. Source validity precedes n_h, A/B, X_n and target transport.
Suggested claim typing: POINTWISE_E2_CHECK separate from UNIFORM_INTERVAL_E2_ADMISSION; latter requires source-backed regularity or sufficiently complete direct interval verification.
DISPOSITION: KEEP_AS_SOURCE_CONTRACT_COMPILER_GUARD; ABSORB_MATH_IN_CLASSICAL_LIPSCHITZ_INTERPOLATION. NO NOVELTY, NO NEW TASK, REV020 ACTIVE, REV021 NOT CREATED, TPE HOLD.


SOURCES:
XH-S3 harvest 023: https://docs.google.com/document/d/1m0gc3Tfr4FvAD1uRFQEqJ-G8KqrovrAyAVxq_kFRPFQ/edit
Mech-S6 gate: https://docs.google.com/document/d/13_245qwn4-m-fjScqWw6Xy0Nyk_KG1kBGvq0bejQylM/edit
MT13 ROT19: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/rotation19_lt_currentness_h8r_frontb_source_weight_20261012.md


ROUTE: IWTO_MT13 IWTO_LT3 IWTO_LT4 IWTO_MECH_S6 IWTO_XH_S3 IWTO_REC9 IWTO_INT7 IWTO_MODERATOR