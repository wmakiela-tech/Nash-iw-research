# LT5 / obrót 6 — Positive Bloch reset is NOT quantum CP: exact diamond distance, legal completions, and source-matched target nonmap

**Date:** 2026-10-22
**Cell:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
**Return ID:** LT5-BLOCH-RESET-NONCP-DIAMOND-AND-INSTRUMENT-NONMAP-001_20261022
**Scientific status:** EXACT_CONDITIONAL_QUBIT_CHANNEL_THEOREM / CLASSICAL_HOST / SOURCE-TYPED_NONMAP / INDEPENDENT_REFEREE_PENDING
**Authority:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NCDG_PHYSICAL_CLAIM
**Exposure:** PUBLIC_SAFE; source-independent algebra and synthetic matrices
**Project source:** LT5 2026-10-21 reset-target note; INT8 and Geeky-S10 fixed-e reset-flow; current LT monograph chapter 5 on Choi and legal quantum instruments
**Storage:** GitHub full body; semantic readback must follow write. No BW or monograph mutation.

## Executive scientific finding

The deterministic classical reset Q_s=I-s ee^T used in the finite-dimensional LT5/INT8/Geeky reset-flow calculations is well-typed on an **ordinary real vector state**. One cannot silently identify that vector with the entire Bloch vector of a qubit and promote the same update to an **unconditional physical quantum channel**.

For 0<s<=1, the unital, trace-preserving linear map \mathcal Q_s acting on qubit density matrices as

  rho=(I+r_x sigma_x+r_y sigma_y+r_z sigma_z)/2
  \mapsto (I+(1-s)r_x sigma_x+r_y sigma_y+r_z sigma_z)/2

is positive (it maps the Bloch ball to itself) but NOT completely positive. Its normalized Choi state has one eigenvalue -s/4. Stronger: the minimum completely bounded trace / diamond norm distance from this linear map to ANY CPTP qubit channel is **exactly s/2**, attained by an explicit three-Pauli Kraus mixture.

This is a sharp but elementary specialization of mature Choi/Fujiwara–Algoet and qubit-channel mathematics (Ruskai–Szarek–Werner); it is not a newly discovered physical principle. The correct project conclusion is a **source-validity barrier**, not “all classical reset effects are impossible quantum mechanically.” A restricted preparation family can admit several distinct CPTP completions with different terminal target effects; a genuine POVM instrument has a different law of observed outcomes and a different unconditional update.

## 1. Distinguish state types before claiming a map

CLASSICAL_X: finite-dimensional real X, nonnegative quadratic storage, deterministic reset Q_s=I-s ee^T and scalar real record b=s e^T x, possibly with an independent numerical error eta.

QUBIT_BLOCH: rho_r=(I+r \cdot sigma)/2, |r|<=1. A real affine Bloch map r\mapsto T r +t corresponds to a linear trace-preserving Hermiticity-preserving map on 2x2 operators, but positivity of the Bloch-ball image is NOT sufficient for complete positivity.

QUBIT_INSTRUMENT: outcome-indexed completely positive operations \mathcal I_a, with \sum_a \mathcal I_a CPTP. Probability of outcome a is Tr \mathcal I_a(rho). A deterministic scalar b with independent adversarial |eta|<=delta is not automatically a POVM outcome law.

We study only the attempt to make the **entire Bloch vector** obey the exact classical reset at e=(1,0,0):

  T_s=diag(1-s,1,1),   0<s<=1.                       (1.1)

We do NOT assume that INT8 or Geeky-S10 actually intended the variables x of their classical carrier as qubit Bloch coordinates. The following no-go concerns this explicit attempted interpretation, not the validity of those original classical proofs.

## 2. Exact non-CP test

**Theorem LT5-6.1 (global qubit no-go).** For each 0<s<=1, the unique unital trace-preserving complex-linear extension of (1.1) on qubit operators is positive but not completely positive. Let J_s be its **normalized** Choi operator, i.e.

  J_s=(\mathcal Q_s\otimes id)(|\Phi^+\rangle\langle\Phi^+|),
  |\Phi^+\rangle=(|00\rangle+|11\rangle)/sqrt2.        (2.1)

Then its eigenvalues (in a Bell basis; order immaterial) are

  {1-s/4, -s/4, s/4, s/4}.                             (2.2)

The operator becomes a valid CPTP channel at s=0 only.

**Proof:** Since r_x is multiplied by 1-s in [0,1] while other Bloch components are unchanged, |T_s r|<=|r|<=1 and the map is positive. It is manifestly trace preserving and unital.

For a Pauli-diagonal trace-preserving unital linear map with multipliers (lambda_x,lambda_y,lambda_z), the normalized Choi eigenvalues in the Bell basis are

  p_0=(1+lambda_x+lambda_y+lambda_z)/4,
  p_x=(1+lambda_x-lambda_y-lambda_z)/4,
  p_y=(1-lambda_x+lambda_y-lambda_z)/4,
  p_z=(1-lambda_x-lambda_y+lambda_z)/4.                (2.3)

Putting (lambda_x,lambda_y,lambda_z)=(1-s,1,1) yields (2.2). p_x=-s/4<0, so J_s is not positive and Choi's theorem rules out CP. QED.

**Alternative one-line test:** The Fujiwara–Algoet inequalities for this ordering require |lambda_y+lambda_z|<=1+lambda_x, i.e. 2<=2-s, false for s>0.

**Instrument corollary:** No qubit instrument defined on the entire qubit state space can have (1.1) as its nonselective channel: a sum of CP instrument operations must itself be CP. This says nothing about whether the same action on a smaller compatible subset can be extended differently.

## 3. Stronger exact quantitative distance to *all* CPTP channels

Let ||.||_diamond be the completely bounded trace norm of linear superoperators (not a physical probability). All maps below act from M_2 to M_2.

**Theorem LT5-6.2 (exact diamond distance).** For 0<s<=1,

  inf_{\Phi CPTP} ||\mathcal Q_s-\Phi||_diamond
      = s/2.                                           (3.1)

This infimum is attained by the explicit CPTP Pauli channel

  \Phi_s
   = (1-s/2) id
     +(s/4) Ad_{sigma_y}
     +(s/4) Ad_{sigma_z},                              (3.2)

where Ad_U(X)=UXU^\dagger. Its Bloch matrix is

  diag(1-s,1-s/2,1-s/2).                               (3.3)

Thus a **global CPTP repair with the same x-coordinate contraction** necessarily disturbs at least one additional Bloch direction, and a symmetric repair can disturb each of the other two by exactly s/2.

**Proof of universal lower bound.** Let \Phi be ANY CPTP channel, not necessarily unital or Pauli diagonal, and set Z=J_\Phi>=0 with Tr Z=1. Let P_- be the rank-one spectral projector onto the negative Bell eigenvector of J_s, so Tr P_- J_s=-s/4.

Put D=J_s-Z, a Hermitian operator with Tr D=0. Its negative expectation satisfies
  Tr P_- D = -s/4 - Tr P_- Z <= -s/4.
For any trace-zero Hermitian D and rank-one projector P, ||D||_1>=2|Tr(PD)| (equivalently, Helstrom's variational trace-norm bound). Consequently

  ||J_s-J_\Phi||_1 >= s/2.

By testing the diamond norm on the input |\Phi^+\rangle\langle\Phi^+|, we obtain
  ||\mathcal Q_s-\Phi||_diamond >= ||J_s-J_\Phi||_1 >=s/2.   (3.4)

**Proof of attainable upper bound.** (3.2) is a nonnegative convex mixture of unitary channels because 0<s<=1. Its Pauli multipliers are precisely (3.3). Direct calculation on the operator basis {I,sigma_x,sigma_y,sigma_z} gives

  \mathcal Q_s-\Phi_s
     = (s/4)(id-Ad_{sigma_x}).                           (3.5)

Both id and Ad_{sigma_x} are CPTP, so each has diamond norm 1. By the triangle inequality,

  ||\mathcal Q_s-\Phi_s||_diamond
     <= (s/4)(1+1)=s/2.

Combine with (3.4), proving (3.1). QED.

**Scope of optimality:** s/2 is minimum **global channel distance** over all CPTP qubit channels under the diamond norm. It is NOT an information–disturbance limit for an instrument required to generate a prescribed x-readout, and not a bound on error for a restricted input K.

### Symmetric compensation threshold

For the two-parameter Pauli-diagonal ansatz

  T_{s,t}=diag(1-s,1-t,1-t), 0<=s<=1, 0<=t<=1,

the Choi Bell weights are

  p0=1-s/4-t/2,
  px=t/2-s/4,
  py=pz=s/4.

Thus this ansatz is CPTP precisely when t>=s/2 (under the declared s,t bounds). At t=s/2 it realizes (3.2). The threshold is specific to equal transverse contractions; it is not a universal statement that each individual transverse coordinate must contract by s/2.

## 4. Restricted preparations admit inequivalent *legal* completions

Take the one-dimensional physical preparation family

  K={rho_theta=[I+theta sigma_x+theta sigma_y]/2 :
                        |theta|<=1/sqrt2}.             (4.1)

These are valid qubit density matrices. Consider the scalar terminal target

  L(r)=r_y-r_x,                                        (4.2)

which is identically zero on K.

The abstract reset (1.1) would create the target
  L(T_s r_theta)=+s theta.                            (4.3)

The map T_s itself is NOT globally CPTP, but legal CPTP channels that have **exactly the same x-coordinate contraction (1-s) theta** yield different terminal target values on this family:

(a) Symmetric diamond-optimal repair (3.2):
  r_out=((1-s)theta,(1-s/2)theta,0),
  L(r_out)=(s/2)theta.

(b) y-axis dephasing
  \Phi_s^{(y)}=(1-s/2)id+(s/2)Ad_{sigma_y},
  T=diag(1-s,1,1-s),
  r_out=((1-s)theta,theta,0),
  L(r_out)=+s theta.

This channel exactly reproduces the **restricted** Q_s output on the states (4.1), because r_z=0, although it has different action on general Bloch vectors.

(c) Isotropic depolarizing channel
  \Delta_s(\rho)=(1-s)\rho+s\,Tr(\rho)I/2,
  T=diag(1-s,1-s,1-s),
  r_out=((1-s)theta,(1-s)theta,0),
  L(r_out)=0.

For every 0<=s<=1 all three maps are legitimate CPTP channels. At fixed s they agree on the output **x-coordinate** for all states and nevertheless disagree on the target (4.2) even for the same admissible family K.

**Conclusion:** A declaration of how one real component of a qubit state is damped does not uniquely specify the physical full channel, let alone an instrument and outcome law. Conversely, the absence of a global CP extension of the naive three-coordinate Q_s does NOT imply that the restricted K witness from LT5 turn 5 is forbidden; (b) is an explicit legal CPTP extension on that K. It is NOT proved that (b) simultaneously supports a specified measurement of sigma_x with a given informativeness/POVM distribution.

This is a precise NONMAP between a **classical reset model**, a **global quantum channel**, and a **restricted-input operational target**, not a claim that one predicts new measurement physics.

## 5. Source-valid instrument with explicit x readout: the Lüders comparison

A legal unsharp two-outcome sigma_x POVM has effects

  E_+ = (I+s sigma_x)/2,
  E_- = (I-s sigma_x)/2,     0<=s<=1.                 (5.1)

For rho_r, outcomes a in {+1,-1} obey

  Pr(a|rho_r)=[1+a s r_x]/2,
  E[a|rho_r]=s r_x.                                    (5.2)

The minimally specified square-root / Lüders instrument has CP operations

  \mathcal I_a(\rho)=sqrt(E_a)\rho sqrt(E_a).            (5.3)

Its nonselective channel \Lambda_s=\sum_a\mathcal I_a is

  (r_x,r_y,r_z) -> (r_x, sqrt(1-s^2) r_y,
                          sqrt(1-s^2) r_z).            (5.4)

**Proof:** In the sigma_x eigenbasis, sqrt(E_\pm) are diagonal with entries sqrt((1±s)/2) in opposite order. Summing both branches leaves diagonal matrix entries invariant while multiplying the offdiagonal entries by
  2 sqrt[(1+s)(1-s)]/2 = sqrt(1-s^2).
In Bloch coordinates this gives (5.4). E_\pm are positive and sum to I, and the Kraus normalization is exact.

For rho_theta from (4.1),

  E[a | theta]=s theta,
  L(\Lambda_s rho_theta)
      = (sqrt(1-s^2)-1)theta
      = -s^2 theta/2+O(s^4).                            (5.5)

This is qualitatively and quantitatively different from the CLASSICAL Q_s pair:
  ideal deterministic record b=s theta (possibly plus bounded eta),
  L(Q_s r_theta)=+s theta.                              (5.6)

Crucially (5.2) and (5.6) are NOT the same measurement experiment. Equation (5.2) is a genuinely stochastic Bernoulli record with outcomes ±1, and (5.6) is a declared deterministic real signal with optional independent bounded error. Their shared mean dependence s theta alone is insufficient to identify their noise/inference theory, and (5.4) cannot be replaced by Q_s.

The contrast is an example of known POVM/Lüders instrument theory, not a universal measurement-disturbance theorem. Selective posterior updates depend on the observed outcome and are NOT described by (5.4); the latter is nonselective.

## 6. Independent finite-matrix stress controls

The following is a compact NumPy-only reference for normalized Choi spectra and the actual unsharp Lüders operations. It constructs the full 4x4 Choi operator from the action of the map on the four matrix units, rather than substituting the analytic Bell-weight formulas, so it can catch a sign or normalization mismatch.

    import numpy as np
    I=np.eye(2,dtype=complex)
    X=np.array([[0,1],[1,0]],complex)
    Y=np.array([[0,-1j],[1j,0]],complex)
    Z=np.diag([1,-1]).astype(complex)
    Pauli=[X,Y,Z]

    def chan(lam,M):
        return (np.trace(M)*I
                +sum(lam[k]*np.trace(Pauli[k]@M)*Pauli[k]
                     for k in range(3)))/2

    def normalized_choi_spectrum(lam):
        J=np.zeros((4,4),complex)
        for i in range(2):
            for j in range(2):
                E=np.zeros((2,2),complex); E[i,j]=1
                J+=np.kron(chan(lam,E),E)/2
        return np.linalg.eigvalsh(J)

    for s in [0.1,0.4,0.8,1.0]:
        ev=normalized_choi_spectrum([1-s,1,1])
        assert np.allclose(ev,sorted([-s/4,s/4,s/4,1-s/4]))
        ev2=normalized_choi_spectrum([1-s,1-s/2,1-s/2])
        assert min(ev2)>-1e-12
        assert np.isclose(np.sum(ev2),1)

        Eplus=(I+s*X)/2; Eminus=(I-s*X)/2
        Ks=[]
        for E in [Eplus,Eminus]:
            vals,V=np.linalg.eigh(E)
            Ks.append(V@np.diag(np.sqrt(vals))@V.conj().T)
        for r in [[0.4,0.4,0],[0.2,-0.4,0.3]]:
            rho=(I+sum(r[k]*Pauli[k] for k in range(3)))/2
            out=sum(K@rho@K for K in Ks)
            actual=np.array([np.trace(out@P).real for P in Pauli])
            goal=np.array([r[0],np.sqrt(1-s*s)*r[1],
                            np.sqrt(1-s*s)*r[2]])
            assert np.allclose(actual,goal,atol=1e-12)
    print("QUBIT_CHOI_AND_LUDERS_CHECKS_PASS")

Private control execution with NumPy on 2026-10-22 gave for s={0.1,0.4,0.8,1.0}: smallest Q_s Choi eigenvalue = {-0.025,-0.1,-0.2,-0.25}, each repaired CPTP map had nonnegative Choi spectrum, and both Lüders state checks passed at each s. These checks do not replace the analytic diamond norm proof.

## 7. Mature literature, prior-art subtraction and monograph relationship

**External primary mature hosts:**
- M. B. Ruskai, S. Szarek, E. Werner, *An Analysis of Completely-Positive Trace-Preserving Maps on M_2*, Linear Algebra and its Applications 347 (2002), 159–187, DOI 10.1016/S0024-3795(01)00547-X; original author arXiv quant-ph/0101003. CP conditions and Bloch channel geometry.
- P. S. Bourdon, H. T. Williams, *Unital quantum operations on the Bloch ball and Bloch region*, Phys. Rev. A 69, 022314 (2004), DOI 10.1103/PhysRevA.69.022314. Fujiwara–Algoet type diagonal CP criteria.
- *Quantum state discrimination via repeated measurements and the rule of three*, Quantum Studies: Mathematics and Foundations (2020), DOI 10.1007/s40509-020-00233-7. Two-outcome unsharp spin-x observable E_\pm=(I±s sigma_x)/2.
- *Entropic Uncertainty Relations for Successive Generalized Measurements*, Mathematics 4(2), 41 (2016), https://www.mdpi.com/2227-7390/4/2/41. Lüders instrument sqrt(E)·sqrt(E) and sequential statistics.

**Project hosts and boundaries:**
- LT working monograph chapter 5 already contains Choi positivity, instrument/comb legality, the quantum transposition no-CP witness and typed process-law bridges. This note adds an explicit **countercheck against the project's particular classical reset Q_s** and quantifies its exact global channel distance s/2. No claim that the quantum formalism itself is new.
- INT8 and Geeky-S10 use fixed-e and sometimes heterogeneous reset models on R^n, with rigorous deterministic record-storage and conditioning bounds. They DO NOT claim to have built CPTP qubit instruments in those source theorems. Their mathematics is left intact.
- LT5 turn 5 established a classical target-generation identity under deterministic reset, and a scalar bounded-noise minimax. Its formula is not invalidated **within that source model**; only automatic quantum/physical promotion is blocked.
- REC10 completed local reviews of LT5 turns 1, 3, 4. For turn 3 d+2 support is sharpened to d+1; for turn 4 exact early/late premium is min((B0-|c|)_+,(w-B1-e)_+). Separate REC10 documentation; neither review is used as approval of this turn.
- PRF11's correlated-Gaussian noise seam additionally warns that matching mean readout is not enough: full conditional distribution/covariance affects inferential power. The POVM readout here has its own Bernoulli law and must not inherit a deterministic bounded-eta or Gaussian noise model from other cells.

**Novelty/prior-art verdict:** All quantum channel tools (Choi's theorem, Pauli-diagonal CP, diamond norm, Lüders POVM), and the explicit arithmetic are standard, known mathematics. The project-specific contribution is a targeted false-inference barrier and legal alternative realizations, not a claim of new quantum physics or new abstract theorem family.

## 8. Falsifiers, possible uses and STOP rules

To propose any physical transport of classical Q_s into a quantum observation protocol, require at least:
1. a declared valid instrument {I_a} with CP operations and \sum_a I_a CPTP;
2. its actual outcome law P(a|rho) and error/cost contract;
3. the full nonselective or selective post-measurement channel;
4. the source-matched terminal observable and any dynamics;
5. the allowed actuator type and causal timing;
6. a direct calculation of the claimed target effect and identifiable quantities.

Without these, do NOT substitute classical Q_s into a quantum Choi/comb channel or use its reset-generated target mismatch as a physical measurement-disturbance bound.

**STOP on novelty:** This is an exact hostile-example audit / source-typing patch, fully surrounded by mature quantum channel theory. It is worthwhile as a concise new subsection near the Choi-to-process legality discussion only after independent referee and editor approval; it should not inflate the theory with another physics “prediction.”

**Independent reviewer:** PENDING.
**Owner acceptance:** UNKNOWN.
**Monograph:** NOT MUTATED.
**BW ingestion:** NOT VERIFIED.
**Current scientific conclusion:** Classical reset Q_s is mathematically legitimate in its original carrier; a global naive Bloch-lift is positive but non-CP at any s>0, with sharp CPTP diamond distance s/2. Restricted and fully operational realizations must be checked separately.
