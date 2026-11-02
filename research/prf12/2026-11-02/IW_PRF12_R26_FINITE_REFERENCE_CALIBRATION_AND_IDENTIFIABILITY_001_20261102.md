---
artifact_id: IW_PRF12_R26_FINITE_REFERENCE_CALIBRATION_AND_IDENTIFIABILITY_001_20261102
created_at: 2026-11-02
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R25_FINITE_CALIBRATION_DATA_UNCERTAINTY_AND_SHOT_OVERHEAD
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_BINOMIAL_REFERENCE_CALIBRATION_CI / UNCONDITIONAL_WRONG_DECISION_RISK_GATE / STRUCTURAL_T1_ASSIGNMENT_NONIDENTIFIABILITY / SOURCE_TYPED_RESOURCE_GRID / INDEPENDENT_KRAUS_CP_INVERSION_PASS / REFEREE_PENDING
claim_ceiling: NO_OBSERVED_HARDWARE_CALIBRATION / NO_CONCLUSIVE_OUTPUT_PROBABILITY_GUARANTEE / NO_GLOBAL_SHOT_OR_CLOCK_OPTIMALITY / NO_EXPERIMENTAL_PREP_FIDELITY / NO_CANON / NO_EXEC / NO_NOVELTY / ORIGINAL_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R26 — Finite-sample calibration of the affine detector, end-to-end risk and resource allocation

**Data:** 2 listopada 2026. **Funkcja:** PRF12. **Wynik główny:** zamiana arbitralnie zadanych granic błędów kalibracji R25 na dokładne dwumianowe przedziały ufności ze skończonego zbioru pomiarów dwóch stanów odniesienia; kompozycja z nie-iid, martyngałowym testem źródła; ujawnienie *strukturalnej nieidentyfikowalności* T1 i eta_minus przy pojedynczej długości opóźnienia detektora; jawna, jednak tylko numeryczna i NOMINALNA analiza kosztów kalibracji względem kosztów właściwych par Ramsey'ego. Weryfikacja dotyczy ściśle zadeklarowanego modelu, a nie fizycznego urządzenia.

## 0. Genealogia i dojrzałe metody

- First-owner: PRF11 R35, Cauchy quasi-static A kontra niezależny Cauchy–Lévy B. Nie redefiniujemy tego modelu.
- Bezpośredni model: PRF12 R23 (wagi osi w=(.18,.20,.62), skończone source-ON prostokątne przygotowanie i analizowanie, idealna końcowa projekcja Z), R24 (długość pary, conditional hazard), R25 (T1 podczas oczekiwania Z, niesymetryczny assignment, korelowany w czasie ukryty ξ, score Y i ograniczenie martyngałowe). Źródło R25: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R25_AFFINE_T1_AND_FAST_RESET_IDENTIFIABILITY_LIMIT_001_20261102.md .
- Zewnętrzny gospodarz: dwumianowe przedziały Clopper–Pearson, C. J. Clopper i E. S. Pearson, *Biometrika* **26**, 404 (1934), DOI https://doi.org/10.1093/biomet/26.4.404 ; SAS exact CP reference https://support.sas.com/documentation/cdl/en/procstat/66703/HTML/default/procstat_freq_details37.htm ; IBM Quantum measurement assignment calibration https://quantum.cloud.ibm.com/learning/en/courses/tools-for-quantum-advantage/error-mitigation . Dokładna kalibracja dwumianowa, union bounds i korekcja macierzy assignment są dojrzałe. Nie ma roszczenia do odkrycia tych metod ani pierwszeństwa nowych twierdzeń.

**Freeze of non-calibration source contracts:** gamma=1 units; Omega_max/gamma=10; two fresh sequential qubit shots per pair, private weighted axis choice; A keeps one ξ during an intact pair, with conditional exogenous reset clock allowed; B independent symmetric Cauchy–Lévy increments during all source-active controls. Prior conservative pre-detector bounds: a0=.576, b0=.526. Gamma*L_pair=1.7783185307179588; gamma*T_pair,worst=1.8283185307179588. At lambda/gamma=.02 allowing mid-shot resets, conditional survival s=exp(−.02*L_pair), floor=0, hence a=s*a0=.5558738000065122, b=.526, contrast D0=.0298738000065122. This is not a new proof of R23's all-real-ξ gap, R24's hazard clock, or R25's fast-reset indistinguishability.

**Critical source quantifier:** survival s is independent of or lower-bounded conditionally on the *actual hidden ξ, private axis, prior observation history and relevant hazard variables*. A bound conditional only on observed outcomes is insufficient, as corrected in the R25 owner report. The current R26 confidence test inherits this guard without relaxation.

## 1. Theorem R26.1 — two physical reference states identify the effective detector exactly, but not all its microscopic parameters

Let the mean registered sign R∈{±1} conditional on ideal pre-detector Z expectation m∈[−1,1] be E[R|m]=cm+d. The source R25 detector model has g=exp(−t_d/T1), eta_+=Pr(+ true -> − registered), eta_−=Pr(− true -> + registered), alpha=1−eta_+−eta_−, beta=eta_−−eta_+, and

    c=g alpha,        d=(1−g)alpha+beta.                         (R26.1)

Prepare known computational eigenstates |0> (m=+1) and |1> (m=−1), independently of the scientific source, with the same detector wait and assignment channel used during the experiment. Let p0=Pr(R=+1||0>), p1=Pr(R=+1||1>). Then

    p0=(1+c+d)/2=1−eta_+,
    p1=(1−c+d)/2=1−eta_+−g(1−eta_+−eta_−),
    c=p0−p1,         d=p0+p1−1.                          (R26.2)

The two reference populations suffice for the entire *effective* affine detector map, if the reference states are truly known Z eigenstates and the instrument remains stationary. Static unknown Z phases/dephasing between preparation and final measurement do not change populations of the Z eigenstates. Unknown imperfect reference preparation, detector drift, correlated label errors or additional T1 during source-active pulses are OUTSIDE this proof.

**Structural negative knowledge, not a sampling error:** p0 fixes eta_+, but p1 constrains only the product g(1−eta_+−eta_−)=c. Hence a continuum of physically distinct (T1,eta_−) produces identical calibrated (p0,p1). For the R25 nominal detector c=.9362975155471993, d=.043702484452800686, eta_+=.01, t_d=.05/gamma, alternatives are:

| eta_minus | inferred Gamma1/gamma | same effective c,d? |
|---:|---:|---|
| .02 | .707255740711 | YES |
| .03 | .500000000000 | YES |
| .04 | .290574002654 | YES |

No amount of additional calibration shots at JUST ONE detector delay identifies the true T1 separately from eta_−. A second known nonzero detector dwell (or independent measurement of one microscopic parameter) can remove this degeneracy, but requires stable eta and a valid same-channel dynamical model. For instance, c(t)=alpha exp(−Gamma1*t), so two calibrated dwell times t1≠t2 with c(ti)>0 give Gamma1=−log[c(t2)/c(t1)]/(t2−t1) and alpha=c(t1)exp(Gamma1*t1), then eta_−=1−eta_+−alpha.

## 2. Theorem R26.2 — finite CP intervals propagate to detector scores without iid source assumptions

Take independent *calibration* populations n0 and n1, with observed plus counts K0,K1. Within each population, measurements must be iid Bernoulli with fixed unknown p0,p1. For X~Binomial(n,p), let the two-sided Clopper–Pearson interval at error alpha be

    L(k,n,alpha)=0 if k=0, else BetaQuantile(alpha/2;k,n−k+1),
    U(k,n,alpha)=1 if k=n, else BetaQuantile(1−alpha/2;k+1,n−k).

Use alpha0=alpha1=delta_cal/2, yielding joint event C={p0∈[L0,U0],p1∈[L1,U1]} with Pr(C)≥1−delta_cal by Bonferroni. The calibration samples MUST be independent of all later scientific source trials; adaptivity of the later test to observed calibration counts is permitted, provided no optional-stopping invalidates the fixed-n CP coverage.

The raw point estimates and exact induced confidence rectangle are

    chat=K0/n0−K1/n1,    dhat=K0/n0+K1/n1−1,
    c∈[L0−U1,U0−L1],   d∈[L0+L1−1,U0+U1−1].            (R26.3)

If chat≤0 OR the interval for c reaches 0, output **ABSTAIN / CALIBRATION NONINVERTIBLE**. Otherwise set uc=max(|chat−cL|,|cU−chat|), ud=max(|dhat−dL|,|dU−dhat|). Under event C,

    eps=(uc+ud)/|chat|,
    |E[Yhat|m1,m2]−(1+m1*m2)/2|≤b_cal=eps+eps²/2,     (R26.4)

where Yhat=[1+(R1−dhat)(R2−dhat)/chat²]/2. This uses independent readout channels conditional on their two ideal pre-detector means and the frozen calibrated affine map. Proof: each corrected conditional first moment differs from m by at most eps, and expanding the product gives 2eps+eps² before the prefactor 1/2. Bounds remain valid for arbitrary non-iid hidden phase histories and source-reset correlations satisfying R25's conditional hazard contract.

Let a=s a0+(1−s)f and b=b0 be the science contract bounds. Compute D_cert=a−b−2*b_cal; if D_cert≤0 output **ABSTAIN / GAP NOT CERTIFIED**. Otherwise the score range width is exactly W_hat=(1+|dhat|)/chat², provided chat>0 and |dhat|<1. Choose a midpoint decision threshold θ=(a+b)/2 and after N science pairs declare A iff average Yhat≥θ; else B. Conditional on C the source hypotheses' mean scores lie respectively above a−b_cal and below b+b_cal. For δ_test∈(0,1), the bounded-increment martingale Hoeffding–Azuma bound shows that BOTH conditional wrong-decision probabilities are ≤δ_test if

    N=ceil[2 W_hat² log(1/delta_test) / D_cert²].          (R26.5)

If a calibration dataset yields D_cert>0 but N above an a priori permitted resource ceiling, ABSTAIN, not forced declaration. The test may adapt N and θ to calibration results because calibration and science trials are disjoint. *End-to-end* for either hypothesis,

    Pr(WRONG scientific conclusion) ≤delta_cal+delta_test.         (R26.6)

**Quantifier caveat:** the bound (R26.6) includes failures of the true calibration coverage event and therefore is unconditional over calibration data. However the chance of output **ABSTAIN** can be arbitrarily large for poor or drifted detectors. We do NOT claim guaranteed conclusiveness on every dataset or a fixed error probability conditional only on the postselected event of getting a conclusion. For the reported “both errors ≤5%” set delta_cal=.01, delta_test=.04. No exact binomial model should be applied to Yhat because it is not Bernoulli and xi may be arbitrarily dependent across pairs.

## 3. Actual finite-count calculation: synthetically generated, NOT experimental data

Retain R25's nominal *physical* detector eta_+=.01, eta_−=.03, Gamma1/gamma=.5, gamma*t_d=.05. Its reference probabilities are p0=.99, p1=.05370248445280068. For a declared **SYNTHETIC AS-EXPECTED** calibration record set

    n0=46000, K0=45540, n1=69000, K1=3705.

With delta_cal=.01, individual exact two-sided CP confidence alpha_i=.005, the computed point and interval-related parameters are:

| value | checked output |
|---|---:|
| chat | .936304347826 |
| dhat | .043695652174 |
| uc | .003826418162 |
| ud | .003753849930 |
| b_cal | .008128716720 |
| certified D | .013616366567 |
| W_hat | 1.190528493715 |
| required N scientific pairs | **49215** |
| calibration reads n0+n1 | 115000 |
| total individual qubit preparations/readouts n0+n1+2N | **213430** |

The science mean bounds under the calibration event are A≥.547745083287 and B≤.534128716720. The actual two-hypothesis error target is delta_cal+delta_test=.05, not .04; it includes the possibility that the CP confidence rectangle missed the true detector. The counts are NOMINAL, not observed and not automatically achieved with high probability; an actual experiment must insert its observed counts and may return ABSTAIN. Do not transfer the finite sample to drifted detectors or inaccurate reference preparation.

## 4. Resource tradeoffs: synthetic grid, not a universal optimum

The full reproducer evaluates **exact CP beta quantiles** for integer synthetic counts Ki=round(ni*pi) while varying the split between n0 and n1. No unknown physical truth is inferred from these synthetic data, and the source of the count ratio is only an example. Contrasting allocations:

| synthetic n0 | synthetic n1 | calibrated science pairs N | total individual qubit reads |
|---:|---:|---:|---:|
| 32000 | 48000 | 86327 | 252654 |
| 44850 | 70150 | 49147 | **213294** |
| 46000 | 69000 | 49215 | 213430 |
| 57500 | 57500 | 51795 | 218590 |
| 98800 | 161200 | 24855 | 309710 |

The source-model nominal detector makes calibration of p1 more expensive: p1≈.0537 has a larger Bernoulli variance than p0=.99. Consequently, a slightly larger sample devoted to |1> is efficient; naive 50:50 calibration is not generally optimal.

A numerical coarse grid ncal=60000,...,400000 in steps of 5000, allocation percentage n0/ncal=.25,...,.50 in 0.01 increments gave two *different* minima among the grid points:

- **Count objective** ncal+2N: 213294 total sensor measurements at ncal=115000, n0=44850, n1=70150, N=49147.
- **Illustrative clock objective**, assume EVERY reference calibration shot independently costs exactly gamma*t_cal=.1 (a strictly ADDITIONAL, potentially unrealistic assumption), and science pair worst gamma*T_pair=1.8283185307: grid minimum gamma*T_total≈71442.8571 at ncal=260000, n0=98800, n1=161200, N=24855.

This second clock computation does **not** include an independently calibrated physical |1>-state preparation pulse, nor additional reference switching overhead; if the actual reference times t_cal,0 and t_cal,1 differ, the correct physical formula is

    gamma*T_total = gamma*(n0*t_cal,0+n1*t_cal,1)+N*(gamma*T_pair,worst).

No claim that either coarse-grid minimum is a *global* mathematical optimum over all calibration allocations, interval constructions, decision scores or source-control strategies. Calibration uncertainty dominates the R25 ideal-known-calibration count N=9516 in this conservative approach, but a sharper likelihood/martingale test may significantly reduce the overhead.

## 5. Independent audit, falsifiers and custody

A full standalone NumPy/SciPy program produces the CP intervals, score extrema, worst-case cal-bias bounds, per-hypothesis martingale exponents, synthetic count fixtures and the coarse resource grid. A second independent program derives the detector via physical 2×2 zero-temperature Kraus amplitude-damping and asymmetric classical assignment and independently checks CP limits by **inversion of binomial tails** using root finding for all k at n=3,5,8,12. The independent program also enumerates physical distinct (Gamma1,eta_minus) parameter sets with EXACT identical c,d.

**Critical falsifiers/negative knowledge:**
1. If reference |0> or |1> state preparation is imperfect or source-ON finite reference prep introduces unmodeled mixing, the simple p0,p1 calibration no longer identifies the science detector response. Calibration is only as valid as its reference states.
2. If detector parameters drift between reference and science, CP coverage of the historical calibration no longer guarantees current c,d. Interleaved or sequential confidence methods are a new contract, not proved by fixed-n CP.
3. If the two recorded errors share common memory/crosstalk conditional on ideal outcomes, product-score unbiasedness can fail.
4. If hidden source resets preferentially at a specific xi or axis, a marginally bounded hazard does NOT imply the preserved R25 a=s a0; the conditional hidden-state guard is mandatory.
5. If calibration N is selected via optional stopping, the fixed-N CP intervals need replacement by time-uniform confidence sequences.
6. For fast-Cauchy refreshed A_h the R25 channel-distance no-identifiability obstruction persists unchanged; this additional data-only refinement CANNOT recover information absent from the physical output process.
7. The open original single-copy unrestricted asymptotic LOCC closure problem is NOT resolved by any of the controlled-source calibration results.

**Status:** LOCAL_THEORY_AND_NUMERIC_REPRO_PASS / INDEPENDENT_REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / GITHUB_PENDING_BW_INGEST. Next: R27 compare raw full-pair multinomial likelihood vs corrected bounded score with certified calibration nuisance intervals, and investigate time-uniform calibration sequences under drift without assuming iid unknown xi.
