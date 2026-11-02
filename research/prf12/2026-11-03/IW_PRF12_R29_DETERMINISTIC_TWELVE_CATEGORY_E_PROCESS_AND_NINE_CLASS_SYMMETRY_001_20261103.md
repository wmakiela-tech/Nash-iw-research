---
artifact_id: IW_PRF12_R29_DETERMINISTIC_TWELVE_CATEGORY_E_PROCESS_AND_NINE_CLASS_SYMMETRY_001_20261103
created_at: 2026-11-03
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
source_type: PUBLIC_INDEPENDENT_OWNER_DERIVATION_DEPENDENT_ON_R28_CERTIFICATE
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_RAO_BLACKWELL_E_PROCESSES / GLOBAL_POSITIVE_LOG_DRIFT_UPLIFT / EXACT_12_TO_9_MINIMAX_AFFINE_SYMMETRIZATION / INDEPENDENT_2X2_4X4_MATRIX_PASS / DESIGN_ONLY_701_GRID_LP_PASS / REFEREE_PENDING
claim_ceiling: NO_NEW_FIXED_N_2251_IMPROVEMENT / NO_ALL_MULTINOMIAL_MINIMAX_SOLUTION / NO_SOURCE_ACTIVE_HARDWARE_PROOF / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_3Q_LOCC_CLOSURE_OPEN
---

# PRF12 R29 — Remove the final classical coin: deterministic full-category e-processes and a 12→9 symmetry reduction

**Data:** 2026-11-03. **Funkcja:** PRF12. **Wynik:** formalnie poprawny test sekwencyjny wykorzystujący bezpośrednio obserwowaną kategorię (X/Y/Z, dwa znaki) jest co najmniej tak skuteczny jak R28 w oczekiwanym logarytmicznym przyroście dowodu, bez dodatkowego losowania bitu. Udowodniono ściśle dodatnią, *globalną* dolną granicę przyrostu log-dowodu dla obu hipotez, dziedzicząc certyfikat wszystkich realnych Xi z R28. Niezależnie zamknięto dokładną redukcję 12→9 kategorii dla **jednoparowych liniowych reguł maksymalizacji najgorszego kontrastu** w kontrakcie wymiennych dwóch odczytów. Nie twierdzimy, że dowolne wieloetapowe testy 12-kategorialne są równoważne 9-kategorialnym.

## 0. Źródła, obiekt, nieprzenoszalne kontrakty

**First owner:** PRF11 R35, źródło A stała Cauchy Xi podczas eksperymentu i źródło B przyrosty Cauchy–Lévy. Najbliższy bezpośredni owner: PRF12 R28, kompletne źródłowo warunkowane twierdzenie:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R28_SIGNED_QUARTET_GLOBAL_XI_AND_NONIID_CERTIFICATE_001_20261102.md
R28 pełna odtwarzalność:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-11-02/IW_PRF12_R28_REPRODUCIBILITY_AND_CUSTODY_MANIFEST_001_20261102.md
CP calibration + exact latent Xi hazard: PRF12 R25/R26. R27 raw parity controls.

Zachowujemy R28 sprzęt: jeden sensor; każdy blok zawiera **dwa kolejno przygotowywane i mierzone** niezależne kubity w sensie dwóch odrębnych użyć sensora; stała Xi podczas obu przebiegów pary, jeśli brak resetu; w przeciwnym razie arbitralne m_1,m_2∈[-1,1]. Źródło A może mieć dowolną zależność Xi pomiędzy parami. Losowanie prywatnej osi J∈{X,Y,Z} z wagami (.18,.20,.62) jest niezależne od źródła. Przygotowanie i skończona analiza X/Y (Ωmax/γ=10), swobodny czas γΔ=.5 i terminalny projektor Z pozostają identyczne z R28; źródło jest aktywne podczas impulsów, a źródło B korzysta z ciągłego generatora Lindblada również w impulsach. Detektor stabilny i opisany efektywnymi c,d. KALIBRACJA pozostaje ustaloną liczebnością 46000 + 69000 **syntetycznych** odczytów wzorcowych, z równoczesnym regionem CP o pokryciu co najmniej .99. Reset przy λ/γ=.02 ma przeżycie s=exp(-λL) WARUNKOWO na bieżącej Xi, wylosowanej osi i każdym ukrytym czynniku hazardu (lub niezależny zegar Poissona). Jedna konkretna zmiana R29: przy odczytach **nie losujemy kolejnego bitu** jak w R28, lecz zachowujemy kategorię i obliczamy czynnik dowodowy.

Dziedziczone certyfikowane granice warunkowe R28, po kalibracji i hazardzie:
  E_A[f(Z_n)|F_(n-1)] ≥ a = .3055,
  E_B[f(Z_n)|F_(n-1)] ≤ b = .2720,
dla **każdej** zgodnej z kontraktem zależności Xi między parami. Są to dane wejściowe R29, **nie** nowe obliczenie pełnej kwantowej arytmetyki przedziałowej. Zakładają udaną kalibrację. Nie przesuwamy stanu naukowego pierwotnego 3-kubitowego problemu LOCC; luka dla domknięcia pojedynczego przebiegu pozostaje OTWARTA.

**Zewnętrzni dojrzali gospodarze:** Grünwald et al., *Safe testing*, JRSS B 86, 1091–1128 (2024), DOI 10.1093/jrsssb/qkae011; Saha & Ramdas (2024), *Robust likelihood ratio tests for composite nulls and alternatives*, https://arxiv.org/abs/2408.14015; randomized Pauli measurements review, *Physics Reports* 1095 (2024), https://doi.org/10.1016/j.physrep.2024.09.009. Rao–Blackwell conditioning, Jensen, Ville, martingale Hoeffding are standard and carry NO priority claim.

## 1. Exact twelve-category law inherited from R27/R28

Let z=(j,r_1,r_2), j∈{X,Y,Z}, r_i∈{+1,-1}. Let c,d denote stable detector parameters, u_j=c m_j+d. Under A with intact pair, m_j=m_j(Xi) and both shots have the same conditional mean u_j. Under B the two shots are independent and have identical mean u_{B,j}. Then

 P(z | Xi,intact, c,d)=w_j (1+r_1 u_j)(1+r_2 u_j)/4.           (R29.1)

For a broken pair, use generally distinct u_1,u_2 in [-c+d,c+d] and the obvious product formula; conditional independence of shots given the complete source and detector trajectory is REQUIRED.

Keep the R28 rational signed scoring rule f(z)∈[0,1]:
- for J=X: f(++):.94; f(--):1.00; f(+-)=f(-+)=0;
- for J=Y: f(++):.88; f(--):.96; f(+-)=f(-+)=0;
- for J=Z: f(++):.36; f(--):.02; f(+-)=f(-+)=0.

R28 actually generated an extra coin Y_n~Bernoulli(f(z_n)); R29 does **not** generate this Y_n.

## 2. Theorem R29.1 — exact composite-null full-category e-factors, optional stopping

Let 0<b<a<1 be the inherited conditional mean bounds, set

 r_1=a/b = 1.123161764705882,
 r_0=(1-a)/(1-b) = .9539835164835165,
 s_1=b/a = .8903436988543373,
 s_0=(1-b)/(1-a) = 1.0482361411087113.

Given the actual observed raw category z, define positive factors

 G_A(z)=r_0+(r_1-r_0)f(z),                                   (R29.2)
 G_B(z)=s_0+(s_1-s_0)f(z).                                   (R29.3)

Under the ENTIRE source-B composite conditional family,
 E_B[G_A(Z_n)|F_(n-1)] = r_0+(r_1-r_0) E_B[f(Z_n)|F_(n-1)]
                        ≤r_0+(r_1-r_0)b = 1.
Under the ENTIRE source-A composite conditional family,
 E_A[G_B(Z_n)|F_(n-1)] = s_0+(s_1-s_0) E_A[f(Z_n)|F_(n-1)]
                        ≤s_0+(s_1-s_0)a = 1.
The second inequality uses s_1<s_0. No iid assumption on Xi is used.

Hence M_n^A=∏_{i=1}^n G_A(z_i) is a nonnegative test supermartingale under B, and M_n^B=∏ G_B(z_i) is one under A. Starting from 1, Ville's inequality bounds the false crossing of threshold 1/.04=25 by .04, respectively. If the fixed-size calibration fails with probability at most .01, the familywise probability of a WRONG declaration is at most .05 per true hypothesis. **Calibration itself is NOT optionally stopped.** When calibration fails to certify a positive margin, report ABSTAIN. Because we have conditioned two opposite factors separately, M_n^A*M_n^B need NOT be 1 (unlike R28's binary LR pair).

An anytime-valid decision policy can declare A if M_n^A≥25, B if M_n^B≥25, and otherwise continue. If both ever cross in one trajectory, the first crossing policy is prespecified. This is a test for *this declared measurement* only; not any unrestricted measurement or optimality theorem.

## 3. Theorem R29.2 — strict, globally quantified expected-log uplift

Under the old random coin Y|z~Bernoulli(f(z)), the R28 one-step log evidence for A is log(r_1) if Y=1 and log(r_0) if Y=0. The new log evidence given the SAME raw z is

 log G_A(z) = log(E[r_Y|z])
            ≥ E[log r_Y|z]
            = f(z)log r_1+[1-f(z)]log r_0.                   (R29.4)

By strict Jensen, the inequality is strict at any category with 0<f(z)<1 and positive conditional probability. The analogue with s_1,s_0 holds for evidence B. Thus removal of the coin is a **Rao–Blackwell improvement in conditional expected LOG growth**. It is NOT a pathwise dominance statement, NOT a blanket improved fixed-n tail inequality, and NOT a guarantee of lower stopping time for EVERY realized sequence.

For quantitative global uplift, use that the logarithm of an affine positive function has curvature bounded away from zero. For r_0,r_1>0,

 log[(1-f)r_0+fr_1] −[(1-f)log r_0+f log r_1]
 ≥ κ_r f(1-f)/2, κ_r=(r_1-r_0)^2/[max(r_0,r_1)]².       (R29.5)

Under source A with intact pair, the pre-detector **Z** Bloch mean obeys m_{A,Z}(Xi)≥0 for every real Xi (R24's exact finite-rectangular-preparation identity). To check analytically, for u=Xi/Ω,

 m_Z=[u²+cos((π/2)sqrt(1+u²))]/(1+u²)≥0:
 when u²≤1, cos(π/2 sqrt(1+u²))≥−πu²/4, and for u²≥1 cos≥−1.

On Z with observed ++, f=.36, so f(1-f)=.2304; its probability under A, conditional on Xi and successful calibration, is ≥[(1+d_min)/2]² with d_min=.039941802242004, since c>0 and m_Z≥0. Include the conditional no-reset survival s=.9650586805668616 and w_Z=.62. Therefore for **all allowed non-iid Xi histories**,

 h_A := inf E_A[f(1-f)|F_(n-1)]
    ≥ s*.62*.36*.64*[(1+d_min)/2]²
    = .0372722805116.                                    (R29.6)

For source B, use m_{B,Z}=.0480973788488, c_min=.9324779296622 and the same detector region. Then

 h_B ≥.62*.36*.64*[(1+d_min+c_min*m_{B,Z})/2]²
     =.0420249066389.                                     (R29.7)

Both are globally positive lower bounds; ignoring fractional X/Y categories makes them deliberately conservative. Broken A pairs contribute nonnegative f(1-f), so the survival factor suffices.

Combining (R29.4–R29.7) with μ_A=E_A[f]≥a and μ_B=E_B[f]≤b gives respectively

 inf E_A[log G_A | past] ≥ D(Bern(a)||Bern(b)) + .0004228247459
                         = .0031888295298,                 (R29.8)
 inf E_B[log G_B | past] ≥ D(Bern(b)||Bern(a)) + .0004767395563
                         = .0031798308161.                 (R29.9)

The baseline Kullback–Leibler terms are .0027660047838 and .0027030912598. The proven positive uplift of these CONSERVATIVE LOWER BOUNDS is at least 15.286% and 17.637%, respectively. We do NOT claim the actual experimental gain equals these percentages, nor that full expected stopping time is reduced by those exact factors. They are conditional-source-uniform guaranteed *per-pair drift bounds*.

Because the log factors are bounded, standard martingale Hoeffding plus (R29.8–9) also yields **loose**, reproducible sufficient n=6070 under A or n=6099 under B for the CORRECT e-process to cross 25 with probability at least .96 conditional on valid calibration, if the science stream is allowed to continue. Early WRONG cross may occur with probability ≤.04; these numbers are NOT a replacement of R28's superior exact fixed-n 2251-pair guarantee and are NOT claimed as minimax sample complexity.

## 4. Theorem R29.3 — exact 12→9 for ONE-PAIR affine worst-case contrasts

For each axis j, denote the four category coefficients f_{j,++}, f_{j,+-}, f_{j,-+}, f_{j,--}, each in [0,1]. Under intact A and B, shots are exchangeable and their two mixed-sign probabilities are equal:

 P_j(+-)=P_j(-+).

For source-A reset, R28 permits ALL ordered (m_1,m_2)∈[-1,1]², with a conditional lower bound on intact survival independent of the orientation. The reset uncertainty set is therefore closed under exchanging the two shots, and

 P_j(+-|m_1,m_2)=P_j(-+|m_2,m_1).                            (R29.10)

Define f_sym by replacing f_{j,+-} and f_{j,-+} by their arithmetic average for each axis. The intact-A expectation and B expectation are UNCHANGED. For a broken pair whose source means are (m_1,m_2),

 E[f_sym|m_1,m_2]
 = .5 E[f|m_1,m_2]+.5 E[f|m_2,m_1]
 ≥ inf_{u,v} E[f|u,v].                                   (R29.11)

Taking the worst reset case and no-reset phase mixture shows the robust *affine contrast* does not decrease. Thus maximizing the guaranteed mean separation over **single-pair linear pointwise rules** needs only 9 independent coefficients: {++, mixed, --} for each of the three axes. The reduction is EXACT at the specified level of robustness, not merely nominal numerical evidence.

**Limits:** if shot order is intentionally asymmetric in the experimental contract, if the reset set is not closed under swapping the two shots, or if one uses a more general multi-pair nonlinear/adaptive likelihood, the 12→9 statement need not hold. In particular, the time-ordered difference P(+-)−P(-+)=(u_1−u_2)/2 may help diagnose SOURCE RESET or detector drift under a structured alternative. It is merely irrelevant for this *symmetric maximin affine discrimination task*, not scientifically meaningless.

### Independent design-only LP comparison

For the NOMINAL calibrated (c,d) and 701 equally spaced Xi∈[-35,35], solve a 16-variable LP: twelve category scores, three lower-reset-floor variables and one guaranteed gap. Separately solve a 13-variable LP using only 9 symmetrized category scores. Results:

 gap_LP12=.0414230323471; gap_LP9=.0414230247896.

The 7.56e−9 discrepancy is within the numerical tolerance of the HiGHS solver and is consistent with the exact symmetrization proof. Both LPs produce zero coefficients for mixed sign outcomes in this finite-grid fixture, while ++/-- coefficients are nontrivial; the R28 rational scoring table remains the certified source choice.

**IMPORTANT:** the 701-node LP is only a DESIGN/DIAGNOSTIC check, **NOT** a proof of the all-real-Xi optimum, CP-detector-rectangle optimum, or unrestricted all-outcome test optimum. The scientific uniformity claim of (R29.2–9) is already certified by R28's separate 7001-node interval+tail calculation and exact R29 algebra.

## 5. Reproduction, negative knowledge and custody

A complete independent one-file Python3/NumPy/SciPy reproducer recalculates the R28 effective detector CP rectangle, 12-category Bloch probabilities, the two exact e-null inequalities, explicit h_A/h_B drift certificates, 701-point numerical LPs and conservative Azuma horizons. A SEPARATE independent program uses **2×2 conditional static source-A density matrices and the correct 4×4 Lévy Lindblad superoperator** to recompute 12-outcome laws for nine phase controls and B, and independently checks strict Jensen and shot-swap symmetry. Neither independent checker claims to re-prove the source-A ALL-Xi compact interval theorem from R28; it is a properly attributed source dependency.

**New negative knowledge, do not erase:**
- R29 did NOT obtain a smaller *certified fixed-length* number than R28's 2251 pairs, and Rao–Blackwell log improvement alone cannot justify transplanting R28's exact binomial tails to a fractional deterministic score;
- no complete twelve-alphabet composite-likelihood minimax optimum is established. Fixed detector nuisance and hidden phase/correlated reset mixtures require proper worst-case handling;
- no arbitrary non-iid likelihood-product model or phase-averaged false iid assumption;
- the calibration counts are SYNTHETIC, source hazard must satisfy its latent-state/axis conditional requirement, and CP interval inversion from SciPy has previously noted numerical rounding limitations;
- no new real device, no physical-source proof, no original one-shot three-party LOCC closure result, no CANON/EXEC or publication-priority claim.

**Next R30:** construct all-outcome robust likelihood **e-factors optimized by a convex composite-null expectation constraint**, with separate A/B e-processes; extend to detector calibration via a fixed-size confidence set, derive a real ALL-Xi guarantee rather than a nominal grid optimization, and compare validated stopping times or fixed-sample resources with the coin-free R29 baseline.

RETURN: PRF12_R29 / RAO_BLACKWELL_DETERMINISTIC_12_CATEGORY_E_PROCESS / SOURCE_UNIFORM_STRICT_LOG_UPLIFT / AFFINE_12_TO_9_EXACT_SYMMETRY / NOMINAL_LP_701_DESIGN_ONLY / INDEPENDENT_2X2_4X4_REPRO_PASS / R28_2251_FIXED_N_UNCHANGED / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / ORIGINAL_SINGLE_COPY_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.
