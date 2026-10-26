---
artifact_id: IW_MT14_ROT004_FRONTB_SEVEN_BIN_MOMENT_RANK_AND_EXACT_TARGET_DUAL_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P1_FRONTB_SOURCE_MOMENT_TARGET_SUFFICIENCY_SEVEN_BIN
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_TYPED_EXACT_CONDITIONAL_RANK_AND_SHARP_TARGET_LP_DUAL / ABSTRACT_NUMERIC_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_PBH_BBN / NO_ORIGINAL_JULIA_10D / NO_UNCONDITIONAL_NONLINEAR_ERROR
---

# MT14 ROT004 — seven-window moment identifiability and exact target-sensitivity dual

Date 2026-10-26. Mathematical source-typed return; Polish long report (12,637 bytes), self-contained script and JSON, SHA256 manifest and replay-tested ZIP are held in the Moderator conversation.

## Source and mature theory FIRST

**Mech-S7 ROT024** owns the original seven logarithmic source intervals, sin^4 compact bumps, pointwise pbar+nbar preservation, moment tests j=0..5, sensitivity kernel and conditional 7D ODE. Original scientific report: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-26/mech_s7_rot024_six_log_moment_target_nonsufficiency_and_approximate_closure_001.md ; original Python https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-26/reproduce_high_order_moment_gate_024.py. Prior Mech ROT020–023 own earlier pair-sum, adjoint and target-moment controls. MT13/NC/LT own broader prior mathematical themes.

**External classical host:** Karlin–Studden, Tchebycheff Systems (1966), https://books.google.com/books?id=pAmVzwEACAAJ (ordered positive systems and Vandermonde); classical finite LP duality and Hahn–Banach, https://doi.org/10.33993/jnaat311-706 ; Chebyshev/Bernstein approximation, https://github.com/chebfun/ATAP/blob/development/chap12.m. No literature novelty or independent physics claim.

## The seven-source-window experiment

Set u=M/(10^9 gram), z=ln(u). Seven ordered intervals I_i=(z_i,z_{i+1}), z_i=ln(.07)+i*(ln(.92)-ln(.07))/7, i=0,...,7. Inside I_i, b_i(z)=sin^4(pi*(z-z_i)/(z_{i+1}-z_i)), zero elsewhere; each strictly positive on its open support. Source Qp,Qn are strictly positive there; S=Qp+Qn; the ACTUAL source moment weight is W(z)=exp(3z)*S(z)>0.

For coefficients c_i and amplitude epsilon, set f=sum_i c_i*b_i and perturb Qp->Qp+epsilon*S*f, Qn->Qn-epsilon*S*f. The pair sum is pointwise unchanged. Differences in comoving logarithmic moments of either channel are plus/minus epsilon*M_k*c, where

M_(j,i)=integral_(I_i) W(z)*b_i(z)*P_j(z) dz, 0<=j<=k,

and P_j forms ANY polynomial basis of degree j, including scaled powers or Chebyshev.

## Theorem R1 (exact, no numerical approximation)

For EVERY k=0,1,2,3,4,5,6, rank(M_k)=k+1 and nullity(M_k)=6-k.

PROOF. Select any ordered k+1 columns and the polynomial rows 0..k. Multilinearity of determinants and Fubini express the minor determinant as an integral over the product of selected disjoint intervals. Its integrand equals the strictly positive product of W(z_l)*b_(i_l)(z_l) multiplied by the polynomial evaluation determinant. The latter is a nonzero constant times Vandermonde product over pairs l<m of (z_m-z_l). Selected interval order makes every difference positive throughout the interiors; the sign never changes and the integral is nonzero. All selected k+1 columns are independent. Therefore rank=k+1.

Thus within this SPECIFIC seven-parameter family: retaining moments degree 0..5 leaves EXACTLY one unobserved coefficient; retaining degree 0..6 forces identical coefficient vectors and hence identical source profiles and downstream targets. This is a finite-family system-identifiability statement, NOT sufficient statistics for arbitrary physical source spectra; infinite-dimensional moment nonuniqueness persists.

## Theorem R2 (sharp linearized target bound)

Let g_i be the derivative of the declared conditional downstream target Y in the pair-preserving direction (+S*b_i,-S*b_i), at epsilon=0. The original Mech ROT021/024 adjoint is the appropriate source-specific way to calculate g; that sensitivity CSV and nonlinear 7D model were NOT independently executed in this MT14 turn.

Constrain moment conservation M_k*c=0 and |c_i|<=1. Then the exactly largest absolute FIRST-ORDER target variation is

B_k := max_(M_k*c=0, norm_infty(c)<=1) abs(g dot c)
     = min_(lambda in R^(k+1)) norm_1(g - transpose(M_k)*lambda).

PROOF: symmetry of the feasible box and subspace reduces the maximum absolute to maximum g dot c. For each lambda and feasible c, g dot c=(g-M^T lambda) dot c <= ||g-M^T lambda||_1. Strong finite-dimensional linear-programming duality for moment equalities and box constraints gives equality and attainment.

CONSEQUENCES. For SAME seven bumps, SAME W and SAME g, B_(k+1)<=B_k, B_6=0. For any v spanning the one-dimensional kernel of M_5, B_5=abs(g dot v)/||v||infinity. Further, B_k=0 iff g belongs to row(M_k). Mech ROT024 has a nonzero numerically measured k=5 target derivative for its selected conditional host, an original-author-owned witness of nonzero B_5; this turn did NOT recompute it.

The strict source positivity sufficient amplitude restriction for any ||c||infinity<=1 is abs(epsilon)<inf_z min(Qp(z),Qn(z))/(Qp(z)+Qn(z)). For a known uniform nonlinear second-derivative bound C, the target satisfies abs(Y(epsilon,c)-Y(0))<=abs(epsilon)*B_k+C*epsilon^2/2. Here NO valid numeric C was obtained. Therefore do NOT use B_k as a certified nonlinear neutron target or physical BBN/PBH error bar.

## Infinite-dimensional counterguard and theoretical pathway

For all measurable signed f with ||f||infinity<=1 and moment annihilation up to k, classical L1-Linfinity duality gives

sup abs(integral phi*f*dmu) = inf_(p polynomial degree<=k) integral abs(phi-p)*dmu,

where dmu=W dz, phi is a target sensitivity density when it exists. This distinguishes finite-dimensional identifiability from arbitrarily shaped spectrum recovery. For analytic phi on a Bernstein ellipse the best approximation has geometric-degree bounds, but analyticity of Mech ROT021 tabulated target kernel was NOT verified; the four original numerical k=2..5 sensitivities do not establish any universal approximation rate.

## Independently executed *synthetic-weight* check

The source seven mass windows and sin^4 shapes are preserved, but the test sets artificial positive W(z)=exp(z) and artificial phi(z)=cos(5*pi*x(z)), with x scaled to [-1,1]. This control is NOT a replay of the real Mech Qp/Qn or ODE.

A 160-node Gauss-Legendre quadrature and separate SciPy adaptive integral evaluator using a different Chebyshev-basis expression agreed at max |M-Mref| 3.61e-16, max |g-gref| 2.08e-16. Seven tested numerical ranks [1,2,3,4,5,6,7]. Separate primal and dual HiGHS LP checks passed with max gap <3e-17. The synthetic sharp values are:

k :  0            1            2            3            4            5            6
B : .163898694914 .140518369763 .113085253371 .107659015564 .020755084217 .019274341705 0

One standalone script, JSON, long Polish report and README are packaged with SHA256SUMS; ZIP CRC, 4 of 4 SHA verifications, isolated clean-room rerun, and byte-exact regenerated JSON all PASS. Synthetic numbers are method controls, NOT values for the author's target sensitivity.

## Decision and falsifier

Falsifiers: exhibit strictly positive source W and seven ordered disjoint positive-interior b_i with any rank defect; find differing seven-window coefficient vectors matching degrees 0..6; or source-valid g,M violating primal/dual equality. Additional source-level falsifiers: Qp/Qn nonpositive on window support or invalid assumed smooth target derivative. PRF/SW/REC/MECH review separate. MECH retains first ownership of model and clinical/physical domain gates; MT14 owns this bounded exact conditional rank/duality computation.

STATUS: SOURCE_TYPED_EXACT_RANK_AND_LP_DUAL / ABSTRACT_NUMERIC_PASS / ORIGINAL_MECH_TARGET_NOT_RERUN / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PBH_BBN_PHYSICAL_CLAIM / GITHUB_PENDING_BW_INGEST.
