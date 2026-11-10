---
artifact_id: IW_PRF13_ROT001_PAIR_READOUT_COPULA_SCORE_RESPONSE_GATE_001_20261111
created_at: 2026-11-11
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_12 / PRF13
source_type: ORIGINAL_SOURCE_TYPED_MATHEMATICAL_COUNTEREXAMPLE_AND_CONDITIONAL_CALIBRATION_GATE
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_FRECHET_COUNTERMODEL_AND_SCORE_RESPONSE_TRANSFER_LEMMA / LOCAL_STD_PYTHON_FRACTION_REPRO_PASS / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_HARDWARE / NO_3Q_LOCC_CLOSURE / NO_R34_CORRELATED_DEVICE_VALIDATION
---

# PRF13 ROT001 — Paired-readout copula obstruction and a score-response calibration gate

**Scientific result:** exact non-identifiability of the non-additive two-shot signed score from calibrated one-shot marginals, together with a *conditional* repair that calibrates only the four scalar score responses of a source-independent classical paired readout channel for each axis. No physical demonstration, priority claim or scientific owner adoption.

## 1. Original source and mature theorem hosts

The source-native parents are [PRF12 R34](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-10/IW_PRF12_R34_VARIANCE_ADAPTIVE_NONSTATIONARY_REFERENCE_ANYTIME_CERTIFICATE_001_20261110.md), [R33](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-08/IW_PRF12_R33_DRIFT_INTERLEAVED_LOCAL_REFERENCES_AND_NONIID_SOURCE_GUARD_001_20261108.md) and [R31](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-03/IW_PRF12_R31_NINE_CLASS_COMPOSITE_E_OPTIMALITY_BRACKET_AND_FIXED_N_1666_001_20261103.md). R31's source A (static hidden Xi within each intact two-shot pair), source B (nonanticipating independent Cauchy–Lévy increments), conditional source hazard, source-ON pulses and all-real-Xi numerical/interval certification are **inherited, not re-proved**. R34's independent conditional shot-readout assumption is **not weakened silently**; the present result studies a different, larger detector class and a possible new conditional repair.

The nominal one-shot detector comparator is p0*=99/100 and p1*=3705/69000=247/4600. R31's source bounds within its original independent-readout model are A0=0.3106993896688963 and B0=0.27161358975207756. The private axes (X,Y,Z) have weights (.18,.20,.62) and the signed score has (++/--) coefficients alpha=(.943,.907,.347), beta=(1,1,.018), with mixed outcomes assigned score zero.

Mature hosts: classical Fréchet–Hoeffding coupling bounds; [Bravyi et al., correlated versus product readout error mitigation, PRA 103 (2021)](https://doi.org/10.1103/PhysRevA.103.042605); [Qiskit full correlated assignment calibration](https://qiskit-community.github.io/qiskit-experiments/stable/0.8/stubs/qiskit_experiments.library.characterization.CorrelatedReadoutError.html); [Howard et al., time-uniform confidence sequences (2021)](https://doi.org/10.1214/20-AOS1991); [Chugg and Ramdas, empirical Bernstein CS for changing conditional means (2025)](https://arxiv.org/abs/2512.21300). No novelty is inferred by recombining mature constructions.

## 2. Exact theorem: one-shot calibration does not identify a paired signed score

Let u=P(R1=+) and v=P(R2=+) be the *conditional* registered-plus marginals given a fixed ideal two-shot input. Write t=P(R1=+,R2=+). Any joint law with those marginals is

\[
Q=(t,\ u-t,\ v-t,\ 1-u-v+t),\qquad
\max(0,u+v-1)\le t\le\min(u,v).
\]

For a private Bernoulli scoring coin with probabilities a on ++, b on --, zero on mixed, where a,b are nonnegative, its mean is

\[
g(u,v,t)=b(1-u-v)+(a+b)t.
\]

Consequently the exactly attainable width at fixed marginals is

\[
(a+b)\{\min(u,v)-\max(0,u+v-1)\}.
\]

**Proof:** the four coordinates of Q are nonnegative exactly on the displayed Fréchet interval. The score is affine increasing in t, so its sharp extrema occur at both endpoints. Both endpoints are probability couplings with the same u,v. This is elementary, established mathematics rather than novel theory.

**Concrete R34 nominal-aligned detector countermodel.** For fixed ideal input pair (--), let u=v=p1*=247/4600 and use the Z score a=347/1000,b=18/1000. Model I uses independent conditional readout, t=p1* squared. Model II uses one hidden Uniform(0,1) latch U shared within the two recorded shots: each registered sign is + when U<=p1*, so t=p1*. Both models have *identical one-shot calibration marginals*. Across all four ideal input pairs, extend both channels by using conditional registered-plus probabilities p0* or p1* on each position and either independent uniforms or the common U. Thus the entire single-shot conditional calibration map remains identical.

Exact rational results:

| Statistic on ideal (--) Z input | Value |
|---|---:|
| Model I score | 72449017/4232000000 = 0.017119332939508507 |
| Model II score | 164063/4600000 = 0.03566586956521739 |
| Difference | 78488943/4232000000 = **0.018546536625708886** |
| Full Fréchet score width | 18031/920000 = **0.01959891304347826** |
| Difference times Z-axis weight .62 | **0.011498852707939508** |

The R33/R34 inherited conservative science targets (a_s=0.2995,b_s=0.2828) permit a maximum common *per-source* change of score

\[
\varepsilon_*=\min(A_0-a_s,\ b_s-B_0)
=0.01118641024792244.
\]

The input-conditional weighted Z discrepancy above is larger than this amount. Hence marginal calibration alone cannot **uniformly certify** the required joint-score response over all ideal-pair inputs. This does **not** establish that the actual R31 source pair law reaches the input (--) vertex or that R34's conclusions are false *inside its explicitly independent-readout contract*. The witness falsifies an unsupported extension of that contract.

## 3. Conditional repair lemma: four score responses, not necessarily sixteen channel entries

**Additional hypothesis (requires independent empirical justification).** For each axis j and time t, the registered pair is generated by a **source-independent classical channel AFTER ideal projective Z results** Q_{j,t}(r|z). The same conditional channel must govern forced ideal-pair reference preparation and source-on science, including relevant memory/hazard history. General coherent POVM cross-talk or source-dependent readout is NOT covered.

For the predetermined score probability w_j(r) in [0,1], define for each of the four ideal two-bit inputs z:

\[
g_{j,z}(t)=\sum_r w_j(r)Q_{j,t}(r|z).
\]

Let g* be the nominal independent-readout score response. Suppose, uniformly for every scientific time and every relevant past,

\[
\max_z|g_{j,z}(t)-g^*_{j,z}|\le\varepsilon_j.
\]

For ANY probability distribution \mu_{s,j,\mathcal H}(z) over the four ideal outcomes—including correlations between ideal shots and permitted history-dependence of Xi—the change in score at axis j is bounded by eps_j, since

\[
\left|\sum_z\mu_{s,j,\mathcal H}(z)
(g_{j,z}-g^*_{j,z})\right|
\le \sum_z\mu_{s,j,\mathcal H}(z)\varepsilon_j=\varepsilon_j.
\]

With source-independent private axis sampling, define eps_score=sum_j omega_j eps_j. Under the unchanged R31 quantum source law, the transported conditional inequalities are

\[
P_A(Y=1|\mathcal H)\ge A_0-\varepsilon_{\rm score},\qquad
P_B(Y=1|\mathcal H)\le B_0+\varepsilon_{\rm score}.
\]

In particular eps_score<=0.01118641024792244 suffices to restore the *predeclared* R33 conditional score bounds. With a separately paid calibration failure probability, the **inherited** non-iid exact rational N=9500,K>=2765 binomial test can then be used. This is only a conditional sufficiency lemma: no experimental calibration certificate is produced here.

For one fixed score functional, only four scalar responses g_{j,z} per axis enter this proof; the whole 4×4 channel need not be reconstructed. When arbitrary ideal-outcome mixtures are allowed, leaving one of those four response values uncontrolled permits a simplex vertex with unknown score. This is a *worst-case source class* argument, not a minimality claim for R31's narrower ideal-source family.

## 4. Prospect for nonstationary anytime reference calibration and its blockers

A candidate method would use forced sequential reference pairs for four ideal inputs per private axis (12 cells), generate a private Bernoulli score coin for each registered pair, and apply R34's **predictable nonstationary empirical-Bernstein e-supermartingale** separately to the twelve streams. For epochs k=1,2,... with total reference failure budget alpha, finite Lambda subset (0,1), and alpha/[k(k+1)] split across 12 streams, two signs and |Lambda| choices, the R34 construction yields the simultaneous anytime radius

\[
r_{j,z,k,n}=\min_{\lambda\in\Lambda}
\frac{\log(24|\Lambda|k(k+1)/\alpha)
+\psi(\lambda)\sum_{\ell\le n}(X_\ell-q_\ell)^2}{\lambda n},
\quad\psi(\lambda)=-\log(1-\lambda)-\lambda.
\]

This step requires every predictor q_l and reference choice to be pre-outcome predictable, correct conditional Bernoulli means, and independently justified pathwise score-response drift bounds for relocating the stopped reference average to the science window. Stopping must ABSTAIN when the needed score-response envelope is not certified. No reference sample-size efficiency, true drift-rate estimate, actual hardware or experimental realization is claimed.

**Open cheap falsifiers:** (F1) forced-pair reference preparation and source-ON science do not share the same conditional channel; (F2) ideal Z-projective postprocessing does not describe the actual POVM; (F3) hidden memory dependence cannot be bounded from reference times; (F4) accessible reference preparations cannot force four known two-shot ideal outcomes with source timing preserved. If any is established, stop this proposed gate and retain R34's narrower valid model. Competing hosts: full correlated 4×4 assignment tomography, a bounded correlation parameter model, or physical characterization establishing conditional shot independence.

## 5. Exact reproducibility, status and return

[Public standalone Python exact-rational checker](IW_PRF13_ROT001_EXACT_SCORE_RESPONSE_COPULA_CHECK_001_20261111.py), using only Python standard-library Fraction, verifies positivity, normalisation and the marginals for both models across all four ideal pairs, the extremal Fréchet score width, exact values in Section 2 and a finite exact mixture check supporting the convexity lemma. Local Python execution and py_compile PASS. Independent local SHA-256: be5bb317fd86933ee4f17ddcb869d382f66048a8b9bf7927393c4b4e92ba3ddf. The published script Git blob SHA-1 39e724bab81e8a5be3c21635b9062f35923d37f6 matched the local Git hash-object byte-for-byte on readback.

**NO CLAIM:** that the current physical device implements the correlated countermodel; that the actual source attains the detector input witness; that the proposed twelve-cell calibration is experimentally valid or efficient; that original single-copy 3-qubit LOCC closure is solved; that the mathematical result is novel; that an external referee accepted it; that BW or Living Theory adopted it.

**PRF13 ROT001 RETURN:** EXACT_COPULA_NONIDENTIFICATION / SOURCE_INDEPENDENT_SCORE_ONLY_CALIBRATION_SUFFICIENCY_CONDITIONAL / EXACT_FRACTION_REPRO_PASS / R31_R33_R34_ASSUMPTIONS_PRESERVED / JOINT_READOUT_EMPIRICAL_GATE_OPEN / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
