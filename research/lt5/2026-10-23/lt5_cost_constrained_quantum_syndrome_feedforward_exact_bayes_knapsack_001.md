# LT5 obrót 8 — Kosztowo ograniczona korekcja błędu kwantowego z rejestrem syndromu: dokładny minimaks i cena chronologii

**ID:** LT5-COST-CONSTRAINED-QUANTUM-SYNDROME-FEEDFORWARD-BAYES-KNAPSACK-001_20261023
**Owner:** IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
**Date:** 2026-10-23
**Type:** EXACT_CONDITIONAL_QUANTUM-INSTRUMENT_PLUS_CLASSICAL_RESOURCE_DECISION / MATURE_HOST
**Claim ceiling:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
**Scientific status:** SELF-PROVED / INDEPENDENT_REFEREE_PENDING / SOURCE-VALID_ABSTRACT_QUBIT / NO_CALIBRATED_HARDWARE_COST
**Living Theory source:** REV020 seven-chapter Google Doc unchanged; a four-section staged editorial candidate already exists. This note is a *separate* possible appendix subsection, not an unapproved new monograph theorem.
**Custody:** Public-safe GitHub write and direct readback required. BW ingestion not presumed.

## 0. Currentness, achieved outcomes of other cells first

Our earlier LT5 ROT07 (2026-10-23) proved that two qubit quantum instruments can share both the same nonselective CPTP channel and POVM while allowing very different outcome-conditioned corrections. In LT5 manuscript audit G3, we asked PRF11 to distinguish information about preparation from a syndrome for correction and assess exact decision risk. **PRF11 R18, already completed before this rotation**, solved *unconstrained* noisy binary error-syndrome recovery:
- E~Bernoulli(p) selects I or Z; observed B through symmetric binary channel q∈[0,1/2];
- optimal residual Pauli error r(p,q)=min(p,1-p,q);
- **even allowing all CPTP recovery channels** (without actuation cost), optimal diamond recovery distance is 2r(p,q);
- positive mutual information I(E;B) need not improve the chosen decision risk, e.g. p=.2,q=.3.

PRF11's independent note is the source and owner of that exact unrestricted result:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R18_NOISY_SYNDROME_TARGET_RISK_DIAMOND_RECOVERY_001_20261023.md

Other cross-cell scientific results inspected:
- **INT8 ROT009** constructs a fully legal selective qubit instrument whose mean readout and average measured-axis damping match a *restricted commuting* one-dimensional classical preparation family, but records are Bernoulli, selective poststates are history-dependent, and no global classical-Q_s/process equality follows. No hardware cost calibrated.
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-23/iw_int8_rot009_restricted_qubit_instrument_realization_and_pathwise_nonmap_001.md
- **Geeky-S10 G2** obtains an exact *axis-symmetric Pauli-channel* channel/POVM compatibility frontier. For x damping a, transverse t≥0, binary x-readout sharpness mu: mu ≤ (1-a)/2 + (1/2)sqrt((1+a)^2-4t²), necessary and achievable. If a=1-s and mu=s, the best transverse retention is sqrt(1-s), not 1. The closest-CPTP repair of the naive LT5 Bloch reset has maximal readout sharpness s/2. This is a target-relative bridge, not a full classical-reset equivalence.
  https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/geeky-s10/2026-10-23/geeky_s10_qubit_channel_observable_compatibility_frontier_001.md

**New narrow question after subtraction:** PRF11 R18 allowed conditional corrective CPTP with no defined action resource. What if the outcome is available before the actuator but the actual use of the nontrivial correction Z has a limited expected frequency? How much of PRF11's *perfectly legal* syndrome advantage survives? We explicitly type the resource and optimize it exactly. This is elementary finite LP/Bayes fractional knapsack on a quantum instrument, NOT new mathematical priority.

## 1. Instrument, timing, operational resource and loss

Let H=C², Z=diag(1,-1). Draw a classical error E∈{0,1} with P(E=1)=p∈[0,1]. The surviving system undergoes Ad_{Z^E}. Its classical error report B belongs to a *finite* alphabet S, with known channel W(b|e), chosen independently of quantum input state rho. The fully declared instrument maps are

  J_b(rho) = A_b rho + B_b Z rho Z,
  A_b=(1-p)W(b|0),    B_b=p W(b|1).                   (1.1)

Each J_b is CP and trace-nonincreasing, and Σ_b J_b is the CPTP dephasing channel Λ_p=(1-p)id+p Ad_Z. Effects E_b=π_b I with π_b=A_b+B_b; hence outcome probabilities do not depend on input rho and Σπ_b=1.

**Causal time:** record B=b is observed first. Controller may flip Z afterwards, randomly with t_b∈[0,1], or choose I otherwise. It cannot see the unobserved true E, and the corrective choice may depend only on b and a fresh independent random seed. A correction uses *one unit* of the declared actuation resource if it applies Z, and *zero* if it applies I. The **expected** frequency (not a worst-run hard limit and not energy) is

  C(t)=Σ_b π_b t_b ≤ beta,     0≤beta≤1.              (1.2)

Because all π_b are independent of rho, the budget is uniform over the unknown input. There are no arbitrary recovery CPTP maps in the admissible class: those have no cost defined by (1.2), and a global optimality assertion across them would be meaningless.

Define the terminal CPTP channel after controller averaged over all outcomes and its random coins. Since products of I/Z multiply modulo 2, the result is Λ_{r(t)} with

  r(t)=Σ_b[B_b(1-t_b)+A_b t_b]
      =p -Σ_b (B_b-A_b)t_b.                              (1.3)

For any r∈[0,1], ||Λ_r-id||_diamond=2r, since ||Ad_Z-id||_diamond=2 and |+x> attains the bound. The optimization goal is minimizing r under (1.2), equivalently minimizing diamond distance within THIS declared correction class.

## 2. Exact constrained theorem and dual

Define d_b=B_b-A_b. Omit outcomes with π_b=0, which also have d_b=0. Set v_b=d_b/π_b =2P(E=1|B=b)-1. Positive v_b means, conditional on the observed b, applying Z is preferable to doing nothing.

**THEOREM LT5-8.1 — exact cost-conditioned selective Pauli recovery.**
Within (1.1)–(1.3):

  r_beta
  = p - max_{0≤t_b≤1, Σπ_b t_b≤beta} Σ_b d_b t_b         (2.1)
  = p - min_{lambda≥0}
      {lambda beta + Σ_b (d_b-lambda π_b)_+}.             (2.2)

The optimizer chooses t_b=1 for all positive v_b above a threshold lambda, t_b=0 for all below, and (at most) one fractional boundary component if positive outcomes are ordered by descending v_b, resolving ties arbitrarily.

Let positive-value outcomes be ordered b_1,...,b_k so that v_{b_1}≥...≥v_{b_k}>0; define P_{j-1}=Σ_{i<j}π_{b_i}. Then exactly

  r_beta=p-Σ_{j=1}^k v_{b_j}
              min(π_{b_j},(beta-P_{j-1})_+).            (2.3)

Consequently

  inf_{admissible policies}
  ||corrected_channel-id||_diamond = 2r_beta.           (2.4)

**Proof.** Formula (1.3) is exact Pauli XOR arithmetic. The primal maximization in (2.1) is a finite linear program. Attach multiplier lambda≥0 to Σπt≤beta; after maximizing each 0≤t_b≤1 individually, the Lagrange dual is precisely min_lambda {lambda beta+Σ(d_b-lambdaπ_b)_+}. The polytope is nonempty (t=0), bounded, and ordinary finite linear programming strong duality applies, including beta=0 via endpoint limiting/linear duality. If v_i>v_j but t_i<1 and t_j>0, transferring an arbitrarily small amount of expected action from j to i increases objective by (v_i-v_j) times that amount, contradicting optimality; thus descending-order fractional knapsack is optimal. Values v≤0 should never be actuated because the budget is an upper bound. Equation (2.3) follows by exhausting available positive masses in that order. Finally the corrected channel is Λ_{r_beta}, whose diamond distance to id is exactly 2r_beta. QED.

**Scope:** (2.4) is the exact optimum over the cost-typed *random Pauli I/Z controller*. It does **not** say that arbitrary CPTP recovery under an unspecified physical cost is bounded by 2r_beta. In contrast PRF11 R18's 2 min(p,1-p,q) global CPTP optimum applies to the different *unlimited-control* protocol.

**Mathematical host:** finite Bayesian decision risk with a capacity bound; Neyman–Pearson threshold/fractional knapsack/KKT and quantum dephasing correction. The LP proof is classical; no novelty or quantum resource theory claimed.

## 3. Exact comparison with a late/inaccessible record

Suppose the syndrome arrives only after the corrective port closes. The controller's probability t of applying Z is then independent of B. Under the *same* expected budget t≤beta, the resulting error is

  r_blind(t)=p+t(1-2p).

Its exact optimum is

  r_blind,beta =
     p                              if p≤1/2,
     p-beta(2p-1)                   if p>1/2.            (3.1)

A policy allowed to observe B can always ignore it and emulate any blind policy, so r_beta≤r_blind,beta. The exact **causal value of record** for our chosen loss is

  Delta_beta = r_blind,beta-r_beta ≥0.                 (3.2)

This does not measure Shannon information. It measures loss reduction under a specific causal action set and a resource contract. An informative record can have Delta_beta=0.

## 4. Binary symmetric noisy flag — sharp resource regime

Specialize to S={0,1}, W_q(b|e) is binary symmetric with 0≤q≤1/2. Then

  A_0=(1-p)(1-q),    B_0=pq,
  A_1=(1-p)q,        B_1=p(1-q),
  π_0=A_0+B_0,       π_1=A_1+B_1.

The unlimited feedback outcome r_1=min(p,1-p,q) matches PRF11 R18 exactly. For an *intermediate* beta, formula (2.3) gives the exact resource-risk curve.

**Symmetric error prior p=1/2.** The flag distribution π_0=π_1=1/2. At q≤1/2, b=1 is the only potentially useful correction; its signed conditional advantage is 1-2q. Therefore

  r_beta(1/2,q)
   = 1/2 -(1-2q) min(beta,1/2).                         (4.1)

A complete flagged correction ordinarily applies Z on exactly half the runs (beta≥1/2), even if it achieves zero terminal error at q=0. A constraint beta<1/2 prevents realizing that success at every run.

No use for flag at all (blind policy, p=1/2) gives r_blind=1/2. The **exact resource/time premium** is

  Delta_beta=(1-2q)min(beta,1/2).                      (4.2)

This is NOT a universal "one bit of information has an energy cost"; the budget is the specifically stipulated expected Z-use probability.

For p=.5,q=.1,beta=.25:
  π_0=π_1=.5,
  t_0*=0, t_1*=.5;
  r_beta=.3, ||corrected-id||_diamond=.6;
  r_blind=.5; unrestricted-feedback r=.1.
Thus one and the same noise channel permits three sharply different risks, solely from the time and use-budget of the correction port.

For p=.2,q=.1,beta=.13:
  π_1=.26, v_1=(.18-.08)/.26=5/13≈.384615;
  t_1*=.5, t_0*=0;
  r_beta=.15; unrestricted r=.1; blind r=.2.

For p=.2,q=.3, neither posterior favours applying Z, so r_beta=.2 for EVERY beta, despite I(E;B)>0. This reproduces PRF11's no-decision-improvement caution with an explicit actuator budget.

## 5. Reproducible 160-case independent LP controls

Used NumPy and SciPy linprog (HiGHS). Five p values {0,.2,.5,.8,1}, four q values {0,.1,.3,.5}, eight beta values {0,.06,.13,.2,.25,.5,.74,1}: 160 parameter triples.

For each case:
1. construct A_b,B_b,π_b,d_b from the instrument;
2. compute closed-form sorted positive-value knapsack (2.3);
3. independently solve the raw two-dimensional LP:
   maximize d·t subject to π·t≤beta, 0≤t≤1;
4. compare r values.

ALL 160 comparisons passed. Maximum absolute difference was 1.1102230246251565e-16.

Selected cases:

| p | q | beta | r_beta | 2r_beta | r_blind | optimal t_0,t_1 |
|---:|---:|---:|---:|---:|---:|---|
| .5 | .1 | .25 | .3000000 | .6000000 | .5000000 | 0,.5 |
| .5 | .1 | .50 | .1000000 | .2000000 | .5000000 | 0,1 |
| .2 | .1 | .13 | .1500000 | .3000000 | .2000000 | 0,.5 |
| .2 | .3 | .50 | .2000000 | .4000000 | .2000000 | 0,0 |
| .8 | .1 | .20 | .6108108 | 1.2216216 | .6800000 | 0,.27027027 |

**Executable independently reproducible control code:**

    import numpy as np
    from scipy.optimize import linprog

    ps=[0,.2,.5,.8,1.]
    qs=[0,.1,.3,.5]
    budgets=[0,.06,.13,.2,.25,.5,.74,1.]
    checks=0
    for p in ps:
      for q in qs:
        A=np.array([(1-p)*(1-q),(1-p)*q])
        B=np.array([p*q,p*(1-q)])
        pi=A+B
        d=B-A
        for beta in budgets:
          ordered=sorted(
            (i for i in range(2) if pi[i]>0 and d[i]>0),
            key=lambda i:d[i]/pi[i],reverse=True)
          remaining=beta
          improvement=0.
          for i in ordered:
            used=min(remaining,pi[i])
            improvement+=used*d[i]/pi[i]
            remaining-=used
          predicted=p-improvement
          solved=linprog(-d,A_ub=[pi],b_ub=[beta],
                         bounds=[(0,1),(0,1)],method="highs")
          assert solved.success
          independent=p-d@solved.x
          assert abs(predicted-independent)<2e-11
          checks+=1
    print("LP_160_PASS",checks)

The computation verifies the elementary optimization and its implementation; no experiment, noise calibration, hardware cost, or quantum instrument tomography is claimed.

## 6. Cross-cell bridge and manuscript decision

### Relation to LT5 ROT04 (causal timing)
LT5 ROT04 quantified early-versus-late scalar actuator capacity under adversarial bounded readout errors. Here the action precedes or follows a **legal quantum instrument flag**; the correction is a cost-constrained conditional random Pauli gate. These are different source carriers, but both show that the existence of late information does not imply an executable late correction.

### Relation to PRF11 R18 (noisy syndrome)
PRF11 R18's unrestricted optimal result is recovered from (2.3) when beta=1; nothing is re-claimed. **The new specific variable in LT5's mathematical experiment is average corrective-gate frequency beta.** Comparing beta to measurement strength s or assigning it physical energy per shot would require a new source contract.

### Relation to Geeky-S10 / INT8 G2
The current G2 outcome is nuanced:
- global direct identification of rank-one classical Q_s with a qubit CPTP channel is impossible (LT5 turn 6);
- restricted commuting-state *mean* readout and one-coordinate damping can be realized by explicit legitimate CP operations (INT8 ROT009), but the single-shot record is random and selective histories are different;
- on an axial unital Pauli channel one can derive exact channel/readout compatibility, with unavoidable transverse damping (Geeky-S10);
- neither construction supplies calibrated physical gate cost or authorizes the classic reset's Gaussian V_* conclusions as quantum predictions.

### Editorial action
This theorem is eligible only as a **short optional bridging lemma** next to the proposed monograph §§5.5b/7.5c, **not** as a new seventh/theory family. The stage candidate LT5-REV021-STAGED-EDITORIAL-CH4-CH5-CH6-CH7-001 remains the one working editorial aggregate, which should refer to this supplementary note only after claim-local review. No mutation of REV020/Google Docs in this turn.

## 7. Mature external prior art / scientific ceiling

- Gregoratti & Werner, *Quantum lost and found* (2003), *On quantum error-correction by classical feedback in discrete time* (2004). Exact random-unitary/environment-assisted correction host; PRF11 R18 provides in-project source-level theorem comparison.
- Buscemi, Chiribella & D'Ariano, *Inverting Quantum Decoherence by Classical Feedback from the Environment*, Physical Review Letters 95, 090501 (2005), DOI 10.1103/PhysRevLett.95.090501. Physical qubit/qutrit classical feedback resource host, not our gate cost model.
- Bény & Oreshkov, *General conditions for approximate quantum error correction and near-optimal recovery channels*, PRL 104, 120501 (2010), DOI 10.1103/PhysRevLett.104.120501. More general recovery and dual formulations.
- *Limitations in Quantum Computing from Resource Constraints*, PRX Quantum 2, 040335 (2021), DOI 10.1103/PRXQuantum.2.040335. Resource constraints can change QEC utility, but source's resource model is different.
- Classical Bayesian decisions/likelihood ratio threshold, linear programming strong duality, continuous knapsack; no literature priority assertion on equation (2.2) is intended.

**Source-subtraction verdict:** This is a clean, exact, reproducible *specialization of mature theory* connecting three already distinct project types: recorded syndrome, causal access and an actual declared actuation resource. It is not new quantum gravity, a new universal information–energy law, a physically calibrated detector, or a discovered NASH invariant.

## 8. Negative knowledge and stop policy

NOT TRUE:
- "CPTP + POVM fixes a controller's achievable correction".
- "The controller knowing the syndrome implies it can afford all suggested corrections".
- "More error-syndrome mutual information forces smaller risk for every cost-constrained decision".
- "Average correction-frequency budget equals a hard per-shot energy or amplitude bound".
- "Optimal among I/Z correction channels means optimal among all CPTP without a defined resource".
- "Classical real-state reset V_* / Gaussian dose bound is a qubit quantum-instrument theorem".
- "A narrow qubit example is evidence for NCDG J3/K physical claims".

**Referee target:** REC10/SW may check the LP dual's sign and endpoints, the causal blind value for p>1/2, and whether the admitted controller class is explicitly restricted to randomized I/Z. If no material error, STOP, do not issue duplicate tasks or request routine acknowledgments.

**Disposition:** EXACT_CONDITIONAL / CLASSICAL_HOST_ABSORBED / EDITORIAL_BRIDGE_STAGED / SCIENTIFIC_REVIEW_PENDING.
