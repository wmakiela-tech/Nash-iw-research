---
artifact_id: IW_PRF13_ROT002_SOURCE_B_SHARED_LATCH_SHARP_MIXTURE_THRESHOLD_001_20261111
created_at: 2026-11-11
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
source_type: SOURCE_TYPED_EXACT_CLASSICAL_COUPLING_WITH_HIGH_PRECISION_QUANTUM_B_EVALUATION
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: SOURCE_B_CORRELATED_DETECTOR_COUNTERMODEL / CONDITIONAL_MIXTURE_THRESHOLD / 70_DPS_INDEPENDENT_LINDBLAD_RECHECK / REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_HARDWARE / NO_GLOBAL_QUANTUM_OPTIMALITY / NO_ORIGINAL_3Q_LOCC_CLOSURE / NO_CLAIM_R34_FALSE_WITHIN_ASSUMPTIONS
---

# PRF13 ROT002 — Source B, shared-latch readout and sharp mixture threshold

## 0. Scientific result and provenance

ROT001 demonstrated that one-shot detector marginals cannot fix the non-additive paired signed score, but its explicit input was an ideal detector vertex. ROT002 tests **the actual source-B ideal two-shot distribution from PRF12 R31/R34**. The quantum source is unchanged: independent Cauchy-Lévy increments, finite source-on controls and two fresh ideal shots with one shared private axis per pair. Only the terminal classical paired readout is extended from independent errors to a source-independent fresh shared-uniform latch. The marginal detector calibration p0*=0.99, p1*=3705/69000 remains exactly unchanged, and time drift is zero.

**Result:** nominal model-B source score with independent readout is 0.2706830837549804812431409270108094474346492689. The same actual quantum source B measured by the shared-latch detector has score **0.2829257326676373768993068657668096872430126868**, above the R33/R34 conservative conditional-B upper bound 0.2828 by **0.00012573266763737689930686577**. Thus the R33/R34 source-B conditional inequality is NOT transportable to arbitrary correlated classical readout from marginal calibration alone. PRF12 R34 remains valid UNDER ITS EXPLICIT conditional-independence assumption; there is no counterexample inside that narrower theorem.

Primary research sources:
- R31: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R31_NINE_CLASS_COMPOSITE_E_OPTIMALITY_BRACKET_AND_FIXED_N_1666_001_20261103.md
- R33: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-08/IW_PRF12_R33_DRIFT_INTERLEAVED_LOCAL_REFERENCES_AND_NONIID_SOURCE_GUARD_001_20261108.md
- R34: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-10/IW_PRF12_R34_VARIANCE_ADAPTIVE_NONSTATIONARY_REFERENCE_ANYTIME_CERTIFICATE_001_20261110.md
- Independent parent source-B 4x4 checker: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-10/IW_PRF12_R34_INDEPENDENT_EVALUE_AND_QUANTUM_FALSIFIERS_001_20261110.py
- PRF13 ROT001: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf13/2026-11-11/IW_PRF13_ROT001_PAIR_READOUT_COPULA_SCORE_RESPONSE_GATE_001_20261111.md

Mature theorem hosts include elementary Frechet-Hoeffding bivariate Bernoulli couplings, Bravyi et al., Phys. Rev. A 103, 042605 (2021), DOI 10.1103/PhysRevA.103.042605 on product versus correlated Markovian readout, and Howard et al., Ann. Statist. 49 (2021), DOI 10.1214/20-AOS1991, on time-uniform CS. No novelty is inferred.

## 1. Exact coupling calculation

Let w=(.18,.20,.62) be the private X,Y,Z axis probabilities; score coefficients on ++ and -- are a=(.943,.907,.347), b=(1,1,.018), and mixed scores are zero. The source-B quantum means m_{B,j} computed from its Lindblad generator are:

m_B=(0.521973443495413435543930779327,
 0.002313357852128669138375189507,
 0.048097378848838209203928789030).

They come from the R31/R34 source-B source-on driven generator in column vectorisation:

L_H=-i(I tensor H - H^T tensor I) + (1/2)(Z tensor Z - I4).

Preparation H=5Y lasts pi/20, free evolution lasts 1/2, and X/Y analyses have H=-5Y and H=5X respectively for pi/20. This reconstructs the baseline independent R34 checker at about 1e-14, using a separate mpmath 70-dps implementation. No R31 source-A all-real-Xi proof was rerun or claimed here.

Put p_j=(1+m_{B,j})/2, p0=.99, p1=247/4600 and d=p0-p1. Each registered shot has plus marginal q_j=p1+d p_j in BOTH detector models. In the independent detector the joint registered ++ probability is t_ind,j=q_j^2.

In the shared-latch detector, for each ideal z1,z2, a fresh common U uniform on [0,1] registers a plus in shot i precisely when U<=p_{zi}, with p_+=p0 and p_-=p1. Source B has two independent ideal shots of plus probability p_j; since p0>=p1,

t_latch,j=E[min(p_{z1},p_{z2})]=p1+d p_j^2.

The signed score for any joint ++ probability t at these fixed marginals is

g_j(t)=a_j t+b_j(1-2q_j+t).

Its global change is

Delta_B=sum_j w_j(a_j+b_j)(t_latch,j-q_j^2)
       =0.01224264891265689565616593875600023980836.

Both detector models match the full one-shot conditional assignment probabilities for EVERY ideal outcome. Their paired score differs because the copula is not identified by the marginals. This is a source-B model witness rather than an artificially chosen ideal (--)-vertex.

## 2. Sharp one-parameter detector-family conditional repair

Define Q_theta=(1-theta)Q_ind+theta Q_latch with a common theta in [0,1] across all axes. The mixer is selected predictably before each pair, independently of its current ideal outcomes, source label, private axis and hidden source noise. Then

p_B(theta)=0.2706830837549804812431409270108
          +theta*(0.0122426489126568956561659387560).

The exact B-side ceiling b=0.2828 is satisfied **if and only if**, within this fixed nominal and common-theta family,

theta<=theta_critical
=0.989729945820190114643421556758072281384853652.

The source-A lower bound is not weakened by any theta in [0,1]: for each axis and each ideal pair z, t_latch(z)=min(p_z1,p_z2)>=p_z1*p_z2=t_ind(z), while a_j+b_j>=0. Consequently the conditional score is monotone increasing when replacing independent readout by shared-U readout, for ANY ideal-pair law, including R31 source A with history-dependent Xi and admissible resets. Hence the prior R31 A lower certificate can be reused in this restricted enlarged detector family. This does not newly prove R31's all-real-Xi quantum theorem.

**Guard:** only a genuine uniform conditional bound on theta, together with the unchanged source model and exact known nominal p0,p1, licenses the B side. Axis-specific theta_j, state-dependent source-readout correlation, post-outcome theta, or drifting detector marginals invalidate the single scalar threshold until reanalysed. An empirical time-uniform estimate of theta would need matched paired reference observations, not just singleton p0/p1 calibration. No such observations were supplied.

## 3. Exact source-B binomial tail and correct interpretation

For R33/R34 fixed science decision N=9500 and declaring A when K>=2765, the exact integer-binomial upper tail at the hypothetical B comparator b=.2828 is

P(Bin(9500,.2828)>=2765)=0.03826512503260072223987358473685562792054.

For the fresh-latch source-B detector at the computed true B success mean, its actual iid pairwise science tail is

P(Bin(9500,.282925732667637... )>=2765)
=0.04058871382617338148607093442707674316167.

The latter exceeds the former. Its arithmetic sum with R34 reference-confidence budget .01 is .050588713826173..., exceeding .05, so the OLD union-bound <=5% **certificate** cannot simply be transferred. This is **not a demonstration of >5% actual error probability**: the science-only error in this fixture is approximately 4.0589%, and union bounds need not be tight.

## 4. Falsifiers, limitations and owner boundary

F1: Quantum B mean/evolution or ideal-shot independence not as specified by R31/R34 => source-B numbers must be recalculated.
F2: Physical readout is not source-independent, post-projective and classical, or the common U is not fresh and source independent => the restricted mixture lemma does not apply.
F3: Unknown drift in p0,p1 or axis-specific theta invalidates theta_critical as a global safety bound.
F4: Marginal reference calibration does not measure theta; independent paired calibration has to be designed, externally anchored, and uncertainty controlled before any device claim.
F5: The failure occurs only near the fully shared latch (theta>98.97%) in this one-parameter family. The result does not establish generic physical instability or an observed failure.

No physical quantum device data, no R35 experimental calibration, no R31 original 3Q single-copy LOCC closure, no full quantum detector optimality, and no novelty. Referee PENDING.

## 5. Reproducibility and storage

A standalone 70-decimal mpmath script, IW_PRF13_ROT002_SHARED_LATCH_B_SOURCE_GATE_REPRO_001_20261111.py, reproduces Lindblad m_B, both registered scores, theta_critical and the binomial regularized incomplete beta tail. An independently written 2x2/4x4 NumPy/SciPy checker from R34 agrees with the m_B fixture. The new high-precision test ran locally with its PASS assertions; arbitrary high precision is NOT formal directed interval error certification. Classical coupling and monotonicity claims are exact algebraic proofs.

All author-written source belongs to public research/prf13/2026-11-11 and remains NO_CANON / NO_EXEC_SIGN. Direct GitHub readback and BW ingestion are distinct events; no BW or Living Theory write by PRF13.

**Return:** PRF13_ROT002 / ACTUAL_R31_SOURCE_B_SHARED_LATCH_FALSIFIER / THETA_CRITICAL_0P9897299458 / EXACT_N9500_TAIL_0P0405887138 / NARROW_FAMILY_A_MONOTONICITY / HIGH_PRECISION_REPRO / SCIENTIFIC_REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_NOVELTY / NO_PHYSICAL_UPGRADE / ORIGINAL_3Q_LOCC_OPEN.
