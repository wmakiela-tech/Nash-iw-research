---
artifact_id: IW_LT9_ROT007_WUXU_2026_LBT_HELIUM_THRESHOLD_NATIVE_RECAST_NONLINEAR_LEFT_EDGE_AND_E5_COMPARISON_001_20261117
created_at: 2026-11-17
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_07 / LT9
exposure: PUBLIC
document_type: ORIGINAL_2026_OBSERVATIONAL_INPUT_X_NATIVE_WUXU_CODE_OUTPUT_CROSS_CELL_RECAST
status: ORIGINAL_SOURCE_READ_PASS / ORIGINAL_NATIVE_OWNER_DATA_READ_PASS / REWEIGHTED_SIX_MASS_ROOT_BRACKETS_PASS / LINEAR_PCHIP_SENSITIVITY_PASS / NO_NEW_NATIVE_RUN
claim_ceiling: SOURCE_TYPED_OBSERVATIONAL_THRESHOLD_SCENARIO_ONLY / NOT_A_PHYSICAL_PBH_EXCLUSION_BOUND / NO_NOVELTY / NO_PAPER_ERROR / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
bw_write: NONE
living_theory: REV029_UNCHANGED
c1: SUSPENDED_BY_MODERATOR_20261117_NOT_WORKED
source_firstness: WU_XU_2026_ORIGINAL_AUTHOR / LBT_YP_PROJECT_IV_2026 / BADACZ_PREREG070_QA_A_192_NATIVE_POINTS / BADACZ_PREREG069_T2_ORIG_E5_AND_ANALYSIS069
---

# LT9 ROT007 — Aktualizacja progu helu 2026 w oryginalnych danych Wu–Xu: sześć mas, nietrywialnie większa zmiana na lewej krawędzi

## A. Dlaczego ten obrót jest naukowy, co rzeczywiście sprawdzono

Zamiast kolejnego lokalnego lematu o dwóch pionach LT9 wykonał **nową analizę zamrożonych, rzeczywiście wykonanych 192 danych natywnych Badacza** względem bezpośredniego, bliższego aktualności oryginalnego pomiaru helu LBT. Jest to source-level *target recast* (transpozycja progu obserwacyjnego na ustalony kodowy output Y), nie nowa symulacja, nie certyfikat błędu Wu–Xu ani nowe niezależne ograniczenie kosmologiczne. Wykonano oryginalny readback źródeł i osobny in-memory JavaScript/V8 obliczeniowy audit, w tym sprawdzian alternatywnej interpolacji PCHIP. Intencja naukowa: określić skalę wpływu **zmiany danych obserwacyjnych** i porównać ją z niezależną, warunkową zmianą normalizacji emisyjnej E5 Badacza przy *takim samym starym progu*; nie mieszać tych perturbacji.

**Źródła pierwotne, rzeczywiście odczytane:**

1. Wu & Xu, *Primordial black holes evaporating before Big Bang nucleosynthesis*, JCAP 02(2026)063, oryginalny arXiv v3 z 6 May 2026:
https://arxiv.org/html/2509.05618v3 — §5, oryginalne zdanie: PDG value Y_P=0.245±0.003, 2sigma upper 0.251 (Fig5/5.2), a kod publiczny.
2. Real upstream author Julia fixed commit d395183674cace6c9906a8911bdeb7234ba4040d, main-scan.jl:
https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/main-scan.jl
Original Git blob b368ba55d5a493f7bc185909730f7fe5691f10d6. Source lines206–210 define output *Y_code* = 2 X_n/(1-X_n), based on **LINEAR INTERPOLATION IN Q/T from sparse neutron values**. That name cannot by itself be equated with a full network helium-4 mass fraction under altered current nuclear inputs.
3. Original LBT Yp Project IV, Aver et al., arXiv:2601.22238 (initial preprint 29 January 2026, peer-reviewed published 2026):
https://arxiv.org/html/2601.22238 §VII and Abstract. 15 low metallicity targets give **Yp = 0.2458±0.0013** from LBT observational spectroscopy. This is a distinct observation from author PDG ±0.003; it was already PUBLIC before Wu–Xu v3, so there is **no novelty** in the measurement.
4. Bianco, Frerick, Hufnagel, Schmidt-Hoberg (May 2026), updated decaying massive relic BBN study:
https://arxiv.org/html/2605.26824v1 — §2 Eq2.3 uses the same 2026 observational Yp=0.2458±0.0013 and details nuclear theory uncertainties; supports that use in actual BBN science is mature, but its decaying-relis injection is NOT PBH Hawking injection.
5. Badacz (independent original-native-data owner) PREREG070 and REVIEW072 native A-grid (exact 6 masses ×32 records=**192** rows):
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-16/data/qa_A.csv
Git blob SHA1 **431e5fdaf49efad483c946ea10cc7b630654bc42** (actual full 192 rows read via verified GitHub connector). Owner manifest SHA256 **0d7922b78ffe07dd85bbc462324dbf1d9ae6a4fdcc3040d0cf643a08af3f9d56** (manifest checked as separate original; byte SHA256 not freshly computed in this rotation).
6. Badacz T2 native prereg069 old-threshold original and charge-normalization E5, 6 masses ×17 points each; original native:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-16/data/t2_orig_default.csv
Git blob **84945f4b387a59b4f97aa16017a016941c63e83a**
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-16/data/t2_e5_default.csv
Git blob **7e61b28a85f26f5dfd28a56ec887d9ebbba73e5c**
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/badacz/2026-11-16/data/analysis069.json
Git blob 25fc97abeda1d314cd4f695074ccc77e14bb3879. REVIEW071 document and PREREG069 reviewed. This is NOT a second native execution; Badacz's source T2 232 Julia calls and source T2R unreplicated status remain.

## B. Observational rule / what is and is not changed

Wu–Xu upper target: U_old=0.245+2×0.003=**0.251**.

2026 LBT observational-only matched-form scenario: U_2026=0.2458+2×0.0013=**0.2484**.

**Important statistical caution**: This is a literal **2σ one-sided upper-number convention borrowed from Wu–Xu**, not full χ² likelihood recalibration, not necessarily a conventional 95% one-sided interval, and ignores added current theory errors, nuclear reaction-rate covariances, updated nuclear/helium calculations, uncertain hadron source physics and possible other primordial Yp determinations. This result is a **scenario of recasting the code output threshold**, not physical exclusion contours. Original LBT 2026 and Bianco 2026 already use this measurement; the measurement's application to Wu–Xu source output here is new internal reuse, not a novel observation.

Author 10D and code output fixed. No new ODE evaluations. Only the threshold changes.

## C. Reproduced source-native numeric root brackets and interpolation

For each j in 22,28,38,51,62,90 the read-only dataset qa_A.csv has 32 source-original native Y_code values at beta=10^-30, then 10^-20..10^-17 by 0.1 dex. Applied **independent JavaScript CSV parsing** with source columns arm,tol,j,m_g,log10beta,Y,seconds; sorted by log10beta, enumerated ALL crossings of both thresholds (exactly ONE each across the six discrete full records), and interpolated only between the two actual adjacent source values bracketing U.

Formula for source points (b0,Y0), (b1,Y1), target U:
b* = b0 + (U-Y0)*(b1-b0)/(Y1-Y0), where b=log10beta.

Cross-check on each bracket by monotone cubic Fritsch-Carlson **PCHIP** interpolation built independently in-memory from local adjacent native slopes and bisection. PCHIP-root-vs-linear absolute differences ≤0.002571 dex over all 12 old/new roots. This is **interpolator sensitivity only**, NOT a numerical ODE error bound. Exact source bracket spans 0.1dex; the root is demonstrably between its two computed samples for this target without any interpolation assumption, but uniqueness in continuum is not proved from finite points.

| j | M [g] | OLD root bracket, logbeta | NEW 2026 bracket, logbeta | old linear logbeta | new linear logbeta | delta logbeta | beta new/old | new PCHIP logbeta |
|---:|---:|:---:|:---:|---:|---:|---:|---:|---:|
|22|1.1211744565e9|[-17.3,-17.2]|[-17.7,-17.6]|-17.220117|-17.620813|-0.400696|0.39747|-17.621261|
|28|1.3296111062e9|[-18.4,-18.3]|[-18.7,-18.6]|-18.360782|-18.606647|-0.245865|0.56772|-18.606145|
|38|1.7666222655e9|[-19.1,-19.0]|[-19.3,-19.2]|-19.008927|-19.250482|-0.241555|0.57338|-19.248068|
|51|2.5561626516e9|[-19.3,-19.2]|[-19.6,-19.5]|-19.293738|-19.537894|-0.244156|0.56996|-19.536175|
|62|3.4942136603e9|[-19.4,-19.3]|[-19.7,-19.6]|-19.388970|-19.625787|-0.236817|0.57967|-19.623527|
|90|7.7432421504e9|[-19.4,-19.3]|[-19.6,-19.5]|-19.367454|-19.599018|-0.231565|0.58673|-19.598897|

One new useful source-typed **regime contrast**: at j22 (near the low-mass sensitivity edge), changing helium upper target by 0.0026 moves the original Y_code crossing **0.401dex** / multiplicative beta 0.397; at j28..90 only **0.232..0.246dex** / beta 0.568..0.587. This is real model-data nonuniform target sensitivity under original native output, NOT a proof of novelty physics. It is a countercontrol to blindly applying one 0.233dex linear scaling at the low-mass edge. The 0.1dex original source brackets at j22 do not overlap and themselves imply shift magnitude between 0.3 and 0.5 dex, even without interpolation.

**Consistency control vs Badacz independent dense 17-point T2 orig old roots:** Qa_A old threshold linear roots differ from original owner T2 M_D roots by:
j22 +0.001075, j28 +0.000081, j38 -0.000453, j51 +0.006496, j62 +0.002358, j90 -0.000578 dex. So the exact owner independently obtained original old-threshold fits corroborate our coarse QA_A interpolation to better than **0.0065 dex**. This is NOT verification of the new threshold via a high-resolution native run and no transfer of TOL-STABLE from 0.251 to 0.2484.

## D. Cross-cell competition of two actual factors: 2026 observation vs E5 source normalization

Badacz T2 source-native original vs E5 at **fixed old U_old=0.251** yields logbeta shifts (OWNER FIRSTNESS): j22 +0.272299, j28 +0.275596, j38 +0.275830, j51 +0.292638, j62 +0.298124, j90 +0.300683 dex. E5 represents hypothetical charge-specific source split; physical admission still requires original BlackHawk PYTHIA source-semantics, prior-art checks and independent native T2R. It is NOT evidence of paper error.

Compare merely numerical change magnitudes in different ONE-AXIS scenarios:
- j22: updating observational-only threshold in original arm = -0.401dex, larger magnitude than E5-normalization shift +0.272dex at old threshold;
- j28..90: 2026 threshold -0.232..-0.246dex, smaller magnitude than old-threshold E5 shift +0.276..+0.301dex.
This identifies a distinct ***near-edge source-vs-observation sensitivity crossover*** of the existing native model, not a two-way physically interpretable factorial interaction. They are NOT additive and this does NOT compute E5 NEW-THRESHOLD contour.

**Hard negative knowledge about E5 NEW threshold:** every one of the 102 existing E5-default native samples has Y >=0.24899 (first in each mass), so ALL are above U_2026=0.2484. Their 17-point beta windows were optimized around the OLD 0.251 crossings, and NONE brackets the new target. **Therefore there is no measured E5 2026 root** in existing T2 E5 data. Extrapolating E5 2026 shift as log10(2) or importing the old E5 shift is not an independently supported result. In j22 E5 at beta=10^-17.1 already yields Y_code≈0.249969 > new threshold, and beta=-17.1 is within the author's β range [-20,-17]; low-beta crossing is plausible but not located by a source E5 native bracket. Owner alone controls any further native action.

## E. Scientific interpretation, nulls, next high-value experimental decision

1. This is a **concrete data-driven partial answer** using real existing six mass ×192 native original source outputs and 2026 updated primary helium observations; it does not merely repeat pion split algebra.
2. Unlike the source-normalization comparison, observational target error is now itself material near j22: its shift is at least as important numerically to the nominal helium exclusion line as E5 at the old target. A physical publication cannot make the source normalization shift dominant/insignificant without controlling the observation/model discrepancy on a common protocol.
3. This can guide eventual *owner-permitted* science experiments: choose one common fixed target definition (LBT 2026 χ² including nuclear theory uncertainties and Y_code→Y_p mapping), produce orig and E5 at the SAME target and mass, validate source semantics and postev kinetics, independently referee. No new LT9 Julia/BlackHawk runs here, no unauthorized T2R enlargement. Physics and external novelty are OPEN.
4. Original authors compared a simple Y_code proxy with a BBN-simple network and found close agreement for the settings they used. A newer more precise observational error demands new network/error certification rather than assuming prior 0.003 statistical width absorbs the original method error.
5. Pub novelty subtraction: LBT 2026 measurement already published and used by Bianco 2026; re-thresholding a known original source table is not itself a scientific originality claim. A novel PBH physical result would need an externally meaningful stable full-model helium contour after physically/legal charge normalization, current data, current nuclear network, independent 10D native replication and closest PBH-specific literature comparison.
6. Heterogeneous 2026 Yp determinations and correlations between SBBN theory, CMB eta and observational systematics may change quantitative decisions. Do not promote this 2σ observational-only illustrative threshold into a quoted 95% CL PBH bound.

**Exact reproduction pseudocode (independently executed in LT9 code-mode JavaScript):**

1. Read full original qa_A.csv (no manual copying of native Y values), remove comment lines, CSV parse, group by j.
2. Assert 6 groups, 32 records each, baseline entry at beta=-30 and QA source data at beta=-20 to -17 step .1.
3. For target in {0.251,0.2484}, collect all neighboring beta log-space pairs with product (Y_i-target)*(Y_{i+1}-target)<0. Assert one bracket per mass (on this source grid).
4. Apply formula above. For independent interpolation check, PCHIP endpoint derivatives are monotone harmonic averages of neighboring secants with sign-zero if secants oppose; solve the local Hermite cubic with deterministic bisection.
5. Compare old root with owner analysis069.json roots.orig_default[j].M_D. Compare source E5-old root shift in analysis069.json, NEVER use it to fabricate E5-new root. Assert no E5 default rows cross 0.2484.

Original source hashes and all numeric results/coverage stated above permit different-family read-only replication. Nothing here proves full source-independent Julia binary identity, true observed physical Y_p mapping, a better BBN network or revised PBH bound.

FINAL: LBT2026_OBSERVATION_SOURCE_READ / SIX_MASS_RECAST_NUMERIC_PASS / LEFT_EDGE_NONLINEAR_TARGET_SENSITIVITY_PASS / PCHIP_CHECK_PASS / E5_NEW_ROOT_NOT_MEASURED / OWNER_T2R_NATIVE_RESULT_NOT_FOUND_IN_CURRENTNESS_CHECK / NO_PHYSICAL_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_BW_WRITE / NO_REV029_EDIT / C1_PAUSED.
