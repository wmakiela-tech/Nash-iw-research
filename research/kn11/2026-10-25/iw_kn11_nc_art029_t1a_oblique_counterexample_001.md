# KN11 — NC ART029 T1a: conditional-attainment counterexample
RETURN_ID: KN11-NC029-T1A-OBLIQUE-ATTAINMENT-FALSIFIER-001_20261025
DATE: 2026-10-25
CLASS: EXACT_2D_MATURE_LINEAR_ALGEBRA / NONBLIND_CLAIM_LOCAL_AUDIT
CEILING: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE / NC_FIRST_CREDIT / INDEPENDENT_REFEREE_PENDING

## Source
NC's source packet: https://github.com/wmakiela-tech/Nash-iw-research/blob/b1ee5b2c4377811789e5f8c4c39613a5b240c134/research/nc/2026-10-25/PAKIET_GROK_NC_029_032_v1.md .
NC ART029 correctly gives the upper bound gamma sup ||c||_2 <= sqrt(m) if mu_2(G)<=0. Its T1a also says equality is achieved for G=0 or an orthogonal oscillator, wording which needs geometry qualifications. NC previously acknowledged an e=d restriction and BAE physical analogy error; this audit does not relabel those prior discoveries.

## Exact new claim-local 45-degree witness
Set m=2, gamma=1, G=0, e=(1,0), d=(1,1)/sqrt(2), strong pulses u_1=u_2=0. The free flow is I for ANY shot times. Then w_1=e and w_2=(I-dd^T)e=(1/2,-1/2), so
W=w_1 w_1^T+w_2 w_2^T=[[5/4,-1/4],[-1/4,1/4]].
Thus lambda_max(W)=(3+sqrt(5))/4=1.3090169943749475, and gamma sup ||c||_2=1.1441228056353685 < sqrt(2). In particular ||L_2^T e||=1/sqrt(2). The strict gap persists for sufficiently strong FINITE pulses by continuity. This is oblique, not NC's previously known co-aligned e=d test.

For G=0, ||D_d(u)e||^2=1-(1-u^2)(e.d)^2; any e.d !=0 and u<1 prevents unit-norm second-shot saturation. A corrected sufficiency statement for ideal strong pulses also needs common alignment of every vector L_j^T e (to saturate the PSD eigenvalue sum). With e perpendicular d, the original existential G=0 attainment is valid; the universal interpretation is false.

## Scope
This is a T1a wording/quantifier falsifier only, NOT a counterexample to NC's T1 inequality. Candidate NC fourth-error item remains NOT independently adjudicated and may overlap NC's old alignment correction. No quantum BAE/QND, original source runner, or physical claim.