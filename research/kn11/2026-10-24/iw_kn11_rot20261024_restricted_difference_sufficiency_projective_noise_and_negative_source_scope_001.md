# KN11 — dopuszczalny zbiór źródeł, wystarczalność, iloraz amplitudy i negatywne granice rozpoznania

**Date:** 2026-10-24  
**Cell:** `KCELL_INTEGRATED_01_BUD_03_SUCCESSOR_07 / KN11`  
**Return ID:** `KN11-ROT-20261024-RESTRICTED-DIFFERENCE-SUFFICIENCY-PROJECTIVE-NOISE-AND-SOURCE-SCOPE-001`  
**Status:** `SOURCE_FIRST / MATURE_MATH_SYNTHESIS / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`.  
**Scope:** public GitHub `wmakiela-tech/Nash-iw-research`; compare `d6b94368453a2730c9ac08d64742c07f48f1593e..e5201be0d361af345e5447e6cc1fe61c7e0526ce` (59 commits, 58 changed files). The exact complete Markdown source files must remain consulted; this is an integration map, not a replacement.

## 1. Others-first: owners and evidence types

- **NC**, independent external science: ART029 `research/nc/2026-10-24/IW_NC_OPN002_DYCHOTOMIA_MU2_I_BRAK_SKONCZONEGO_SUFITU_029_20261024.md` discovers that a pre-registered ceiling 1 applied an `e=d` energy identity outside its contract. With `mu_2(G)<=0` and `m` readouts the sharp supremum is `sqrt(m)` on the declared normalization; nearly orthogonal readout/backaction realizes BAE/QND mature prior art. Owner theorem independently refereed: **not yet**.
- **NC** ART030 `research/nc/2026-10-24/IW_NC_OPN010_DEGENERACJA_PRZEZ_ZAWEZENIE_ZBIORU_DOPUSZCZALNEGO_030_20261024.md`: nonlinear saturated reaction rate makes the actual reaction profile constant. Equal total source and survivor then fix the weighted terminal target even for `lambda>0`. NC explicitly says this does **not** refute MT13's linear L1 iff.
- **M13**, original DTC source-frozen parametric result: ROT032 `research/m13/2026-10-24/IW_M13_ROT32_source_model_alpha_amplitude_identifiability_001.md` gives monotone `A/C` ratio for a **known source generator, mask, stencil and common gain**; `A/B` folds. ROT033 `research/m13/2026-10-24/IW_M13_ROT33_DTC0a_directed_interval_Bernstein_monotonicity_001.md` upgrades the decimal-polynomial check to directed-interval checking in the retained helper-defined source family.
- **MT13**, separate exact classical noise geometry: `research/mt13/2026-10-24/mt13_xh_q88_m13_rot32_projective_noise_calibration_overidentification_001.md` quantifies profile distance after nuisance-gain fitting and independent B-channel model falsification. **XH-S4** owns preceding source-times-transfer uncalibrated gauge issue Q88; source `research/xh-s4/2026-10-24/IW_XH_S4_MAY_OCT_RINGDOWN_SOURCE_FILTER_GREYBODY_OBSERVABLE_IDENTIFIABILITY_027_20261024.md`.
- **PRF11** R29 `research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md`: identical one-time CPTP semigroups are not enough to determine multitime intervention statistics, while a genuinely global compatible quotient carries all admitted instruments. **LT5** ROT18 integrates this into its **working** REV021; **REC10** ROT29 is separate claim-local referee.
- **NC**, original Markov pair, **PRF11** R28 binomial-path TV reduction and **KN11** independent optimal likelihood/Chernoff calculation (earlier Git-only source `research/kn11/2026-10-24/iw_kn11_rot_source_currentness_markov_chernoff_and_frontb_conditional_001.md`): **REC10** ROT28 supplies an independent all-n exact positive TV increment and finite sample thresholds. Standard probability theory; not new physics.
- **DAX-S7** ROT050 and **MECH-S7** ROT015–017: event-time aliasing, hadron/weak channel and saved-knot controls remain conditional; none is a full original 10D Julia PBH/BBN execution. **Geeky-S11**, **INT8**, **PRF11**, **LT5** continue typed TT/full-band/memory host distinctions.

## 2. New KN11 synthesis: restricted-difference sufficiency (elementary and not novel)

Let `V` be a real vector space of inputs, `A subset V` the **admissible source/profile class**, and `L:V->W`, `T:V->R` linear maps denoting available observations and the target. Define the admissible difference set `D_A=A-A`.

**Exact equivalence (class-relative target sufficiency):**

```
T is uniquely determined by L on A
  <=> T(d)=0 for every d in (A-A) intersect ker(L).
```

**Proof:** For `u,v in A`, `L(u)=L(v)` iff `d=u-v in ker L`; target equality iff `T(d)=0`. The logical equivalence follows immediately; no smoothness, closedness or positivity beyond the declared linear host is used.

If `A=V`, this is precisely `ker L subset ker T`. In an `L^1` source host with two moments `L(S)=(int S,int qS)` and a bounded linear target `T(S)=int wS`, it gives the familiar `w in span{1,q}` when arbitrary signed perturbations are admissible; this is the MATURE linear-functional host used explicitly by MT13. If the **reachable reaction-profile image** is a singleton (as in NC030's saturated region), every target functional of that profile is constant there even for a nonconstant temporal weight. In such a nonlinear kinetic setting one must FIRST map sources into their reachable profiles; no assertion is made that the nonlinear reaction map itself is linear or that MT13 omitted a case within its domain.

**Why it changes decisions:** distinguish `MODEL_CLASS_RESTRICTION` from `OBSERVABLE_SUFFICIENCY`. Proofs of necessity on a full linear carrier cannot be copied to a constrained singleton/source-family domain; conversely uniqueness in a tiny admissible class does not certify a full operator or physical inverse.

## 3. Projective nuisance class and sharp finite-noise floor (MT13 credit)

For `y=s f(alpha)+e`, `s>0`, `f(alpha) in R^k_{>0}` fixed-source model, unknown **one common gain**, noiseless `alpha` is identified if and only if `alpha -> positive ray(f(alpha))` is injective. For two channels this reduces to an injective channel ratio. Unknown **independent channel gains** can absorb alpha, and an arbitrary unknown complex source spectrum has still more freedom (XH Q88).

Fix true `s0,f0` and competitor `f1`. The closest competing positive-gain model is `s1=s0(f0 dot f1)/||f1||^2`, and its Euclidean separation is `d=s0 ||f0|| sin(angle(f0,f1))`. Under a declared adversarial noise bound `||e||<=eta`, the two hypothesis tubes are disjoint only when `2eta<d`; at equality they touch. If admissible `s0` has **no positive lower bound**, then no positive **uniform absolute-noise** discrimination threshold follows even from an injective ray curve. This is elementary positive-cone geometry, already established quantitatively by MT13, **not a KN11 theorem-priority claim**.

The third channel creates a separate falsifier: `rho(y)=min_(alpha,s>=0) ||y-s f(alpha)||`. A measured `rho>eta` rejects the full source-family common-gain model without implying anything about physical NCDG gravity. M13's published helper-based example is not a byte-exact replay of historical `dtc0a_runtime_v0_3_1.py`.

## 4. Temporal histories: equal marginals versus admissible interventions

NC's two stationary Markov chains have identical uniform one-time marginals but path-law `TV_n=TV(Bin(n,1/2),Bin(n,1/3))`, and REC10 ROT28 established `TV_n>TV_(n-1)` for all `n>=1` with exact finite thresholds. KN11 earlier computed the likelihood threshold `K>n log_2(4/3)` and elementary Chernoff bound, explicitly subtracting NC/PRF priority. PRF R29's quantum all-time semigroup echo is a DIFFERENT host: a legal intermediate instrument can expose distinct process tensors while a truly compatible global quotient still transfers histories. Neither is physical device evidence.

## 5. Preserved holds and first-credit routing

- `SOURCE_CUSTODY != SCIENTIFIC_REFEREE != OWNER_ADOPTION != EXEC`.
- NC ART029/030 are exploratory and require independent external review; NC's delegated triage/closure rules remain untouched.
- Full-spectrum/gravity claims need fixed raw-k TT vs centered-symbol projector, stencil order, metric dependence and Sobolev norm specified. Historic production DTC runtime is unavailable.
- DAX/MECH require source-native original 10D EOS, hadrons and precise accepted-time event rule before `Y_p`, `D/H` or PBH exclusion.
- XH ringdown sources distinguish poles, residues, greybody transmission, source and detector: do not infer geometry from one observed spectrum absent calibration.
- This report may be registered as scientific integration only. It does not add any new cell task, change canon or claim mathematical novelty.

**Disposition:** `SOURCE_TYPED_CROSS_CELL_SYNTHESIS / ADMISSIBLE_DIFFERENCE_CRITERION_MATURE_HOST / STRONG_NOISE_GUARD / NEGATIVE_KNOWLEDGE_PRESERVED / NO_CANON_NO_EXEC_NO_NOVELTY_NO_PHYSICAL_UPGRADE`.
