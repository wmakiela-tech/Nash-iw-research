# LT5 ROT18 — ciągłe półgrupy a procesy, warunek globalnego ilorazu i nieidentyfikowalność zdarzeń z próbek

**Date:** 2026-10-24  
**Return ID:** LT5-REV021-ROT18-GLOBAL-QUOTIENT-INTERVENTION-PROCESS-ARITY-SOURCE-EVENT-001_20261024  
**Function:** LT5 independent living-theory author, science-first source-typed chapter integration.  
**Actual edited 7-chapter native working document:** https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit  
**Original REV020 preserved unchanged:** https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit  
**Status:** SOURCE_NATIVE_AUTHORIAL_INTEGRATION / 4_NEW_SECTION_TEXTS / INDEPENDENT_QUANTUM_AND_CLASSICAL_SPOT_CHECK_PASS / FULL_REFEREE_PENDING.  
**Ceilings:** NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_QUBIT_HARDWARE / NO_PHYSICAL_PBH_LIMIT / NO_NEW_BW_INGEST_ASSUMPTION.

## 0. Currentness and allocation of credit

Read up-to-date Slack dispatch and exact full GitHub source reports, especially:
- **PRF11 R29**, sole author of continuous all-time semigroup-vs-process witness and universal compatible quotient positive theorem. Familiar scientific host Milz & Modi PRX Quantum 2, 030201 (2021) Sec VI.A.2, Milz, Kim, Pollock & Modi PRL 123, 040401 (2019), and Kropf, Gneiting & Buchleitner PRX 6 031023 (2016); no NASH priority for the underlying phenomenon. Exact source blob 5d58bcda978b99f30c0edb017cf5f99347caf7e1.
https://github.com/wmakiela-tech/Nash-iw-research/blob/3199a28e2fff9f6f4a1a262f0d0708d81ba97145/research/prf11/2026-10-24/IW_PRF11_R29_CONTINUOUS_SEMIGROUP_PROCESS_ECHO_AND_QUOTIENT_CONTRACT_001_20261024.md
- **Mech-S7 ROT016**, original archived saved sample event coverage and generic exact-knot/dense interpolation negative counterexample, GitHub source:
https://github.com/wmakiela-tech/Nash-iw-research/blob/206c93cc21b6a78cf214772bc9f38c1b2b9020bf/research/mech-s7/2026-10-24/mech_s7_rot016_event_aliasing_exact_knot_interpolation_negative_control_self_contained.md
- **M13 ROT032**, source-generator *restricted* model identification of α and common amplitude s via A/C channel ratio, proof for published decimal polynomial coefficients and condition number Θ(N²) under fixed ABSOLUTE noise:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6e1e21649f134f7e4635f73138dc4eec38ee5fff/research/m13/2026-10-24/IW_M13_ROT32_source_model_alpha_amplitude_identifiability_001.md
- **INT8 ROT024**, exact filtered metric-raw-k affine alias H^s-to-L² operator norm, attained over real TT cross polarisations and sharp Θ(N^(-s)) with FIXED α for s>0:
https://github.com/wmakiela-tech/Nash-iw-research/blob/71d548f3406089be41030b3ba6394cba9df632d8/research/int8/2026-10-24/iw_int8_rot024_exact_filtered_affine_tt_alias_sobolev_operator_norm_001.md

These results are original to their source cell or older literature, not LT5's original discovery. LT5's incremental effort is to disambiguate logically distinct science in native working REV021 and independently verify a small well-defined set of witness computations.

## 1. Material Chapter 7 typed correction: two notions of "autonomous"

The source REV020 Chapter 7 §7.2 Thm 7.1 has a GLOBAL factorization condition r U_t = V_t r for EVERY full state and t, and closes: "Nie wynika stąd jej ciągłość, całkowita dodatniość ani równoważność procesów z interwencjami". This statement is sensible ONLY without a separately established instrument contract. It must NOT be used as a negative result against a stronger **global compatible quotient**.

New native §7.2a states and proves the positive transfer result:

If for every allowed full state x, rU_t=V_t r for all t≥0; for every allowed, possibly adaptive outcome instrument there exists an admissible outcome map i_a with r I_a = i_a r; and r preserves the normalization/mass of unnormalized outcome branches, then for ANY finite history
r U(Δ_m) I(a_(m−1)) ... I(a_1) U(Δ_1) x
 = V(Δ_m) i(a_(m−1)) ... i(a_1) V(Δ_1) r x.
Proof: repeatedly insert the intertwining identities from right to left; branch probabilities follow from mass preservation. This requires a genuine positive/CP structure and source-legal reduced instruments; bare set maps don't automatically acquire physical legitimacy. The instrument condition is NOT implied by dynamical factorization alone.

Independent classical verification: take X=R⁴ with two 2-vector flag sectors, Y=R², r=(I₂,I₂), V_t=e^(−.2t)I₂, U_t=diag(V_t,V_t), and I=diag(M,M), i=M, M=diag(.6,.8). One hundred random full initial states and four time/measurement stages satisfy the equality with maximum error ~1.67e−16. A deliberately NONFACTORING I_bad=diag(.1,.5,.9,.5) maps full states (1,0,0,0) and (0,0,1,0), which have the SAME reduced state, to reduced outputs separated by .8. These are textbook algebraic checks and NOT legal quantum hardware.

## 2. Complementary Chapter 7 process NONMAP: identical ALL-T CPTP semigroups

New native §7.7a gives the strongly continuous-time counterexample under a WEAKER observation contract, also independently recounted:
A: one static, per-run ξ~Cauchy(0,γ), qubit U_(ξt)=e^(−iξt Z/2).
B: independent symmetric Cauchy Lévy increments with scale γΔt.
Both give for every initial uncorrelated qubit ρ, every t>=0:
Φ_t(ρ)= [(1+e^(−γt))/2]ρ+[(1−e^(−γt))/2]ZρZ;
Φ_(t+s)=Φ_t Φ_s, L=γ/2(Ad_Z−id).
A legal deterministic intermediate X in the middle of T=2s, a known final X correction and a final |+> test give
P_A(+)=1, P_B(+)=[1+e^(−γT)]/2,
TV=[1−e^(−γT)]/2.
At γ=.7 and T=2, TV=0.37670151802919677.

A whole ideal X-pulse train with signed exposure E=Σ(-1)^(j−1) Δ_j yields
TV = [e^(−γ|E|)−e^(−γT)]/2,
exact within THIS input/pulse family and maximized when E=0. Static Cauchy noise is a mature dephasing/echo host, not new hardware or a universal optimum over all instruments.

**CRITICAL TYPE REMEDY:** The static model does NOT satisfy rU_t=V_t r on all joint system+environment states: with the same system ρ, distinct ξ values can produce different outputs after tracing/forgetting ξ. Thus a channel family averaged at one fixed initial independent environment law is NOT a global quotient. PRF R29 directly makes this distinction; our §7.2a/§7.7a pair prevents an incorrect conflation of it with §7.2 Thm 7.1.

Independent LT5 NumPy 2x2 unitary control:
- U(a) X U(a)=X and echo path identity tested numerically; max 1.5701e−16.
- γ=.7, T=2, terminal test P_B=.6232984819708031; TV=.37670151802919694.
- seeded 250000 pairs of independent Cauchy increments show mean cos(a−b)=.24831657536798535 versus e^(−1.4)=.2465969639416065, MC deviation .0017196114263788587. This Monte Carlo check is limited sampling verification, not proof of Cauchy characteristic function.

Source PRF11 R29 also independently states uniqueness of static Cauchy/Dirac for exact all-time semigroup; our native integration does NOT promote it to a claim about all microscopic dephasing noise.

## 3. Chapter 6 §6.10c: archive sampling does not identify accepted-step errors

The earlier LT5 conditional source §6.10b distinguishes translation of the entire autonomous time coordinate from a physical change in mass-cube rate and states that current global endpoint accuracy is not certified. New Mech-S7 ROT015–016 supplies the missing negative control for ERROR ATTRIBUTION.

Four original public/paper × exec/sym archives contain last source-on saved sample at M≈1.8366e9 g and t≈49.9619 s; first source-off at M≈8–11 g, t≈52.2591 s. Approx sample gap=2.2972034211 s. Exact pinned source mass cube gives t_table=51.0982580232, t_cut=51.3359243396, duration=.2376663164 s, so gap/subtable lifetime=9.66566678885 and no saved sample in the active below-table interval.

Three reasonable 2-point interpolation laws give very DIFFERENT edge times relative to the EXACT SOURCE mass cube: linearly in M: −.089925 s; in M³: +.790050 s; in log M: −1.063613 s. These are illustrative transformations of TWO archived samples, **NOT** SciML's actual dense interpolant.

Most importantly the Mech source exact-knot negative witness uses source-law-EXACT ODE states at BOTH accepted knot endpoints, but a generic linear interpolation of log M between those knots yields <.0431% mass deviation and effective sampled Γ secant ratios 0.95049...1.05118; a ±5% sampled secant error alone CANNOT prove the solver's accepted steps wrong. It also cannot prove actual SciML dense interpolation is the culprit. Genuine original Julia accepted state mesh and dense sample output need separate logs and callback/source events; Mech's Julia instrumenter is prepared, NOT run. Full physical 10D/E2b/BBN endpoint remains on HOLD.

This is consequential for §6.9a event-time adjoints: mathematical event identities can be exact while the material required to evaluate their residual/error terms (solver step history, interpolation, transversality) is unavailable. It is incorrect to turn a time-secants anomaly into a physical PBH rate uncertainty.

Direct independent LT5 arithmetic computes original reported gap/subtable life ratio=9.66566678885; NOT independent archival reprocessing or original Julia integration.

## 4. Chapter 4 §4.11e: source-restricted positive identifiability and H^s alias rates

M13 ROT31's general full 3D TT five-mask RMS non-identifiability remains valid. M13 ROT32 carefully restricts to one FIXED known source generator, known masks/grid and stencil E_lin, α∈[0,.2], and ONE shared positive scale s for diagnostic A and C. Then K_j(α)=U_j+αV_j+α²W_j, squared RMS g_j quartic and ratio R=y_A/y_C=√(g_A/g_C) cancels s. The source certifies strict monotonic R in 10 cases via exact rational sign check on the PUBLISHED DECIMAL coefficients, not directed interval rigor for the original trigonometric source. Then α and scale s can be recovered. A/B instead has a tiny turn near α=.000712669 (N41 k3) and a second parameter point giving the same A/B with a different common scale; so experimental channel design matters. Stability with absolute RMS noise degrades as O(N²) condition number, C is of order N^−2 while A stays nonzero. This is NOT generic TT inverse and not physical J3/K.

INT8 ROT024 further states EXACT source H^s -> target L² metric raw-k TT alias+filter operator norm as a max over folded modes. For FIXED α and s>0 the rate is SHARP Θ(N^−s), whereas high-band L² near-total TT projection loss from ROT023 also remains true. Uniform O(N^−s) for a GRID-DEPENDENT α_N needs a bounded α_N family; arbitrary α_N tuning has an independent two-mode positive lower certificate. Distinct source and target norms MUST be typed.

The manuscript's §4.11e gives both source-typed positive/negative results and asks for simultaneous structural identifiability, stability under physically credible observation error, and regularity-conditioned alias bounds.

## 5. Source-proof and readback status

Edited the existing native WORKING REV021, without changing authoritative REV020, inserting exactly four scoped HEADING_2 sections inside Chapters 4, 6, 7:
- §4.11e restricted parametric inverse vs alias H^s (M13/INT8).
- §6.10c archive dense-output sampling vs integrator accepted steps (Mech-S7).
- §7.2a positive global quotient plus instrument factor contract (PRF11).
- §7.7a same-all-time CPTP semigroup vs multitime echo NONMAP (PRF11).
Frontnote adjusted for these sections; a Polish α interval punctuation correction was made and verified via replace count 1.

Google Docs direct readback at this turn:
- original REV020 1763 paragraphs (156790 concatenated UTF16 text chars), untouched.
- working REV021 2027 paragraphs (206823 concatenated UTF16 text chars).
- ALL 1763 original paragraphs **literally preserved in the same order**, 7 chapter HEADING_1 entries.
- Each new §4.11e / §6.10c / §7.2a / §7.7a occurs ONCE with HEADING_2 and a nonempty NORMAL_TEXT source-linked question body.
- Typographic/PDF page rendering and independent full theorem review NOT claimed.

### Independent reproducer

Self-contained LT5 Python using NumPy, deterministic seed 20261024, wrote and executed full script successfully:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-24/reproduce_lt5_rot18_process_quotient.py

Terminal result:
- echo matrix maximum 1.57009245868e−16
- Γ=.7, T=2 TV .37670151802919694
- independent Cauchy Monte Carlo 0.24831657536798535, deviation .0017196114263788587
- 100 full compatible classical quotient branch histories max 1.66533453694e−16
- source event sampled-gap/lifetime 9.665666788850368
- LT5_ROT18_SCOPED_CONTROLS_PASS.

None of these local controls verify the complete other-cell paper, physical lab system or full Julia solver.

## 6. Research questions / stopping

- CH7: Characterize minimal admissible intervention algebras closed under a given exact quotient; can a target-relative approximate quotient have an explicit finite-horizon history probability error without assuming incompatible instruments?
- CH7: Which source and environment preparations preserve process distinctions if all unperturbed one-time CPTP channels are known? Experimental distinguishability requires actual legal pulse/readout calibration.
- CH6: Disentangle accepted mesh, dense readouts, physical mass source events and global event-aligned error budget in original Julia, without inferring mechanism from archival secants or declaring synthetic interpolation the historical one.
- CH4: Which small set of source generator diagnostic channels yields good condition number under a realistic ABSOLUTE error budget, preserving continuous operator realization?

Stop boundaries: no physical PBH helium inference, no gravitational TT covariant invariant, no new quantum instrument realization, no novelty claim, no new metascience trial, and no automatic BW ingest/referee/Moderator EXEC. Preserve owner credits and negative knowledge.

**Disposition:** R29_GLOBAL_QUOTIENT_SCOPE_REPAIRED / ALL_TIME_ECHO_NONMAP_CONFIRMED / MECH16_ACCEPTED_DENSE_OBSERVATION_NONMAP_INTEGRATED / M13_32_SOURCE_RESTRICTED_IDENTIFIABILITY_AND_INT8_24_HS_RATE_INTEGRATED / NATIVE_REV021_DIRECT_READBACK_PASS / INDEPENDENT_FULL_REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
