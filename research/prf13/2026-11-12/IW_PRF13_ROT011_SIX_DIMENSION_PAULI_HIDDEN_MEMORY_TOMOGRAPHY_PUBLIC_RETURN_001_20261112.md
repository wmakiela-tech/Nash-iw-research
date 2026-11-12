---
artifact_id: IW_PRF13_ROT011_SIX_DIMENSION_PAULI_HIDDEN_MEMORY_TOMOGRAPHY_PUBLIC_RETURN_001_20261112
created_at: 2026-11-12
origin_cell: PRF13
source_type: EXACT_FINITE_FOURIER_KERNEL_AND_SOURCE_RESTRICTED_CP_INTERVENTION_TOMOGRAPHY
exposure: PUBLIC
sync_state: GITHUB_SOURCE_READBACK_PASS_BW_INGEST_PENDING
status: AUTHOR_EXACT_REPRODUCED / REFEREE_PENDING
claim_ceiling: NO_GENERAL_QUANTUM_PROCESS_TOMOGRAPHY / NO_NOVELTY / NO_HARDWARE / NO_ORIGINAL_3Q_LOCC / NO_CANON / NO_EXEC_SIGN
---

# PRF13 ROT011 — six-dimensional Pauli correlation kernel and single-gate intervention tomography

**Result.** For every pair of two-stage qubit *classical Pauli noise* process combs with equal separately averaged first-stage channel, second-stage channel and idle endpoint channel, the still-invisible differences form an EXACT six-dimensional real linear space. One fixed generic intermediate CPTP unitary plus six input-Pauli/final-Pauli expectation configurations identifies all six degrees. This is source-restricted elementary group Fourier analysis and a mature process-tensor application, NOT original general theory.

## Source and the ten ordinary-channel constraints

Let G=F_2² and U_(a,b)=X^a Z^b. Joint Pauli-label distribution p(v,w) has sixteen entries. Define characters chi_0=1, chi_X(a,b)=(-1)^b, chi_Y(a,b)=(-1)^(a+b), chi_Z(a,b)=(-1)^a. These are precisely the Pauli conjugation signs. For d=p-p' define its 16 Fourier coefficients C_ab(d)=sum_(v,w) d(v,w) chi_a(v)chi_b(w).

First-stage unconditional CPTP equality is equivalent to C_a0=0 for all a. Second-stage equality is C_0b=0 for all b. With no gate inserted, U_w U_v is phase times U_(v+w), so endpoint CPTP equality is C_cc=0 for all c. Pauli mixing labels are identifiable from the diagonal quantum channel on Bloch space, so these implications are biconditional in this model. The union of coefficient constraints has size 4+4+4−2=10 (index 00 counted three times). The remaining ordered off-diagonal pairs (a,b) with a,b in {X,Y,Z} and a!=b number exactly SIX.

Using Fourier inversion, precisely:
d(v,w)=(1/16) sum_(a,b !=0, a!=b) C_ab(d) chi_a(v)chi_b(w).

Thus ordinary reduction R=(channel_1,channel_2,channel_idle) has a six-dimensional fiber about any strictly positive joint p. Construct all six independent legal examples
p_epsilon(v,w)=[1+epsilon chi_a(v)chi_b(w)]/16, -1<=epsilon<=1,
where a!=b and p0 is independent uniform. All three ordinary channels remain exactly completely depolarizing for every epsilon. The linear 12×16 marginal/convolution constraint matrix has rank exactly 10 over Q, hence nullity 6; code checks all six basis vectors and positivity.

## One fixed unitary recovers the entire missing fiber

Choose V=[I−i(X+Y+2Z)]/sqrt(7). This is unitary. Its Bloch SO(3) matrix in ordered Pauli basis (X,Y,Z) is
R(V)=(1/7)*[[-3,-2,6],[6,-3,2],[2,6,3]],
with all six off-diagonal entries nonzero.

When V is inserted, first Pauli U_v gives input sign chi_j(v), V gives rotation R_ij and last U_w gives output sign chi_i(w). Therefore the complete Bloch transfer matrix equals
T_ij(p;V)=R_ij(V)*C_(j,i)(p).
If p,p' are equivalent under the three ordinary channels, their only possible differences lie in the six i!=j entries. Hence prepare the eigenstate + of sigma_j, insert the SAME V, and measure sigma_i at output for each i!=j. Then
Delta C_(j,i)=Delta E[sigma_i | prep +j,V]/R_ij(V).
All six signed coefficients are exactly identifiable with one fixed intermediate unitary and six scalar input/output Pauli expectation settings. Six linearly independent scalar coordinates are necessary to recover a generic six-dimensional linear fiber within this restricted measurement-coordinate paradigm. No general quantum-query minimality claim is made.

For each basis p_epsilon with epsilon=1, the correct Pauli terminal binary test has TV=|R_ij|/2, either 1/7 or 3/7, against independent p0. A distinct tailored Clifford rotating input j into output i could achieve TV=|epsilon|/2 for that single direction. The generic V does not need retuning and accesses all six directions.

## Explicit existing LT8/ROT010 parent and subgroup no-go

For correlated F(a,b)=(b,a xor b), p_C(v,w)=1/4 if w=F(v), the nonzero off-diagonal Fourier coefficients are exactly C_XZ=C_YX=C_ZY=1. Thus the parent LT8 two-time counterexample occupies a boundary point of this exact six-dimensional hidden fiber.

For a qubit **Pauli subgroup with only two projective labels**, the row/column/xor-sum constraint matrix for its 4 joint entries has rank 4. There is NO hidden direction when those three ordinary channels are jointly fixed within that restricted two-label Pauli noise class. This does not apply to other kinds of two-state classical or quantum memory or unrestricted process combs.

## Scope and prior-art subtraction

Fourier inversion on finite groups, quantum process tomography and memory are mature. The physical legal interposition follows quantum comb causal constraints as established by Chiribella, D'Ariano, Perinotti, PRA 80 022339 (2009), DOI 10.1103/PhysRevA.80.022339; and process tensors of Pollock et al., PRA 97 012127 (2018), DOI 10.1103/PhysRevA.97.012127; operational Markov memory, Pollock et al. PRL 120 040405 (2018), DOI 10.1103/PhysRevLett.120.040405. No novelty/priority/new physics; no NCDG field mapping. A successful source-typed intervention discriminator here is NOT a general CIPIR or multitheory unification proof.

Author SymPy checks: 12×16 rank=10, six Fourier bases rank=6, exact V unitary and R orthogonal determinant 1, six physical 2×2 input-output tomography identities, subgroup rank=4, parent source coefficients: PASS. Full expanded report, standalone code, exact stdout and manifest in ROT011 ZIP. Independent referee and BW ingestion PENDING.

RETURN: ROT011 / SIX_DIMENSION_INVISIBLE_PAULI_PROCESS_KERNEL / ONE_FIXED_GATE_SIX_PAULI_TESTER_COORDINATES / PARENT_CORR_SOURCE_EXACT_EMBEDDING / PRIOR_ART_ABSORBED / NO_CANON / NO_EXEC_SIGN.
