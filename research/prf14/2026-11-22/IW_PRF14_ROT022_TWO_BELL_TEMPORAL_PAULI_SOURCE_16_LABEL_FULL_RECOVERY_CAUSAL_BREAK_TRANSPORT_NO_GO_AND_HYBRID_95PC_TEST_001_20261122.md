---
artifact_id: IW_PRF14_ROT022_TWO_BELL_TEMPORAL_PAULI_SOURCE_16_LABEL_FULL_RECOVERY_CAUSAL_BREAK_TRANSPORT_NO_GO_AND_HYBRID_95PC_TEST_001_20261122
date: 2026-11-22 Europe/Warsaw
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_13 / PRF14
exposure: PUBLIC
science_class: TWO_TIME_CLASSICAL_PAULI_LABEL_SOURCE / TEMPORALLY_RESOLVED_TWO_BELL_MEASURE_RESET_PROBE / TESTER_DEPENDENT_CAUSAL_SOURCE / EXPLICIT_NO_GO / HYBRID_UNITARY_VS_BELL_TRANSPORT_FALSIFIER
status: FOUR_ORIGINAL_ACTUALLY_EXECUTED_PROGRAMS / DIRECT_INDEPENDENT_WITHIN_OWNER_BELL_BORN_AND_PAULI_KRAUS_CHECK / ORIGINAL_SIX_FOURIER_PHYSICAL_ALIAS_EXACT / 95PC_ANALYTIC_MULTINOMIAL_AND_BINARY_CONFIDENCE / 2700_SYNTHETIC_EXPERIMENTS / 14_FILE_ZIP_CRC_SHA256_PASS / DIFFERENT_CELL_EXTERNAL_AUDIT_PENDING
firstness: PRF13_ROT011_SIX_HIDDEN_FOURIER_SOURCE / PRF14_ROT021_NINE_TRANSFER_AND_SIX_MARGINAL_BLINDNESS / PRF14_ROT022_RESTRICTED_TESTER_CONTEXT_TRIANGULATION_INTERNAL_ONLY
ceiling: NO_GENERAL_QUANTUM_PROCESS_TENSOR / NO_NONINVASIVE_BELL_PROBE / NO_TRANSPORT_CAP_FROM_BREAKER_OUTPUT / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# PRF14 ROT022 — Temporal Bell labels recover the complete breaker-source distribution, while measurement-induced source changes can defeat its interpretation for uninterrupted experiments

## 0. Summary of newly executed results

The original ROT021 two-time classical Pauli source has sixteen joint histories (v,w) in F2²×F2². Its full terminal qubit channel provides only nine mixed Fourier correlations and is blind to three first-error plus three second-error marginal coordinates. ROT022 constructs two *temporally placed Bell-pair measurement-and-repreparation instruments* such that, conditional on a fixed pre-sampled classical source law during that exact diagnostic protocol, the sixteen possible pairs of observed Bell labels reproduce the FULL sixteen-element source distribution. Four Bell states yield a 4×4 identity measurement channel; two error time slices yield I_16, checked from both exact symbolic orthogonality and an independently written complex Born/POVM computation.

This does NOT prove the diagnostic source matches the original uninterrupted unitary-experiment source. The bell-break tester changes the system trajectory and may change the noise generator's conditional law. Two explicitly legal physical source worlds with exactly the SAME full terminal channels and the SAME breaker Bell label data have unitary-context source TV respectively 0 and .99 in the unrestricted sixteen-way classical Pauli model. A second source-specific physical no-go PRESERVES all ten ordinary Fourier coordinates at ZERO, i.e. the original PRF13 six-only source family: reference world's two contexts have unitary source TV=0, but a different physical target gate and two adjusted positive six-only source laws yield unitary source TV exactly 56909401620057847415776307603455327/132351817902681306874347204262889866800 ≈ .000429985794844945; both full terminal channels and both breaker Bell laws remain identical between worlds.

On the POSITIVE side, an *externally supplied* total-variation transport cap between unitary-source and breaker-source contexts supports a two-source, 16-outcome, 95% confidence interval with 122,144 two-Bell-label protocol runs. More originally, separate unitary matched-Clifford source-TV LOWER measurements and breaker-label source-TV UPPER measurements can be TRIANGULATED to put a positive LOWER bound on tester-induced source change without presupposing transport. A specified legal source alternative gives a 95%-sufficient one-sided detection resource of 872,386 experimental-model runs. The new statement is source-specific and a falsifier, not an invariant-source proof.

General Bell measurements, causal breaks, process tensor tomography, and categorical L1 concentration are mature. NO external novelty, no real quantum hardware, no full quantum process tensor claim.

## 1. Firstness and current original literature

Original science files ACTUALLY inspected: PRF14 ROT021 complete executed Python and machine JSON under /mnt/data/prf14_rot021/, and original public report immutable Git commit ed2240254be6a60d97627ef42ea5b60fc2e7f88e:
https://github.com/wmakiela-tech/Nash-iw-research/blob/ed2240254be6a60d97627ef42ea5b60fc2e7f88e/research/prf14/2026-11-22/IW_PRF14_ROT021_FULL_MATCHED_CLIFFORD_NINE_CHANNEL_SOURCE_TV_SHARP_2SQRT2_RELATIVE_CALIBRATION_TWO_SIDED_CONFIDENCE_AND_SIX_MARGINAL_BLINDNESS_001_20261122.md
PRF13 ROT011 is original owner of six hidden offdiagonal Fourier memory coordinates. PRF14 ROT020/021 owns matched unitary Clifford source-TV lower bounds. INT10 ROT020 owns earlier independent sharp 9/8 inverse six-Fourier norm; not rediscovered here.

Direct external publisher/search abstract/excerpt sources examined, full manuscripts NOT claimed read:
- Taranto, Milz, Murao, Quintino, Modi, A Guide to Higher-Order Quantum Operations, PRX Quantum 7 042001, published 13 November 2026, DOI https://doi.org/10.1103/92c4-g7qs. Mature treatment of operational instruments, measurement-and-repreparation and higher-order causality.
- Non-Markovian Quantum Process Tomography, PRX Quantum 3 020344 (2022), https://doi.org/10.1103/PRXQuantum.3.020344. Restricted/complete multi-time testers and causal-break motivation are mature.
- Demonstration of Non-Markovian Process Characterisation and Control on a Quantum Processor, Nature Communications (2020), https://doi.org/10.1038/s41467-020-20113-3.
- Weissman, Ordentlich, Seroussi, Verdu, Weinberger, Inequalities for the L1 Deviation of the Empirical Distribution (2003). Original PDF locator only found, NOT analyzed; the exact elementary subset-union finite-alphabet inequality below was derived independently and is not claimed new.

## 2. The two physically distinct source domains

A complete joint classical source p(v,w), v,w∈F2², has fifteen independent nonconstant Walsh-Fourier coefficients: three from v alone, three from w alone, nine cross terms chi_j(v)chi_i(w). For any unknown stable physical middle R∈SO3 and any fixed middle control S_q(R), the terminal unital Pauli-mixture Bloch channel depends only on C_ij=E[chi_j(v)chi_i(w)] through T_ij=C_ij[S_q(R)]_ij. The normalization plus nine cross-character map has exact rank10 on sixteen joint probabilities, leaving SIX invisible marginal directions. These are NOT the original six hidden offdiagonal mixed coordinates from PRF13 when marginal/diagonal source Fourier coefficients are separately fixed.

Use proper original target R=[[-3,-2,6],[6,-3,2],[2,6,3]]/7 and cyclic Clifford P=[[0,0,1],[1,0,0],[0,1,0]]. For a=.99 the STRICTLY POSITIVE laws
 p_plus(v,w)=[1+a chi_X(v)]/16, p_minus(v,w)=[1-a chi_X(v)]/16
have each minimum probability 1/1600, normalization1 and TV(p_plus,p_minus)=.99. Every mixed C_ij is exactly zero because w is uniform, so every full terminal transfer matrix is zero for ANY physical middle gate. Independent Born-and-Kraus code verifies this physically, not just by an asserted formal Fourier shortcut.

Source law MUST be indexed by complete preannounced experiment (control q, tester e). In particular p^(q,UNIT)(v,w) for uninterrupted original experiment need not equal p^(q,BREAK)(v,w) for the Bell measuring/resetting experiment, even when every law separately describes a lawful causal CPTP experiment. If the entire tester choice is known BEFORE the first noise label is sampled, this context effect needs no retrocausal mechanism. These context laws are NOT automatically a single intervention-independent quantum comb.

## 3. Exactly what the two-Bell tester measures

The protocol assumes experimental access IMMEDIATELY AFTER the first U_v and before R, and again IMMEDIATELY AFTER R and before the second U_w. Before U_v prepare a maximally entangled system-ancilla Bell state |Phi+>=(|00>+|11>)/sqrt(2). Immediately after U_v Bell-measure the pair; this reveals v. Destroy/reset/reprepare a sacrificial system input into R, apply R and any designated control according to q, then discard/reset its output and prepare a FRESH system-ancilla Bell pair immediately before U_w; Bell-measure after U_w; this reveals w. Thus the two noise intervals probe DIFFERENT physical system qubits and the circuit is NOT the original uninterrupted quantum trajectory.

For Pauli U_v=X^x Z^z, the four pure Bell states |Phi_v>=(U_v tensor I)|Phi+> form an orthonormal basis, and a perfect projective Bell measurement produces
 Pr(a,b|v,w;BREAK)=delta_(a,v)delta_(b,w).
Thus its sixteen outcome probabilities are EXACTLY p^(q,BREAK)(v,w), provided the two classical error labels were chosen as a fixed joint classical pair for THAT tester and are not affected subsequently by its readouts/resets. For a source that depends on tester, this conclusion STILL correctly identifies p^(q,BREAK), but does NOT identify p^(q,UNIT).

Exact SymPy Bell Gram I4, 16-label Kronecker Bell likelihood I16 PASS. A second independently written NumPy complex Born trace of physical Bell projectors checks the complete POVM and I16. The second test additionally explicitly exhausts ALL 65,536 subsets of sixteen source categories and reproduces categorical TV duality. These are two within-author methods, not an independent outside laboratory.

## 4. Two rigorous physical transport no-go examples

**Unrestricted sixteen-way source:** Compare W0 p_A^UNIT=p_B^UNIT=uniform16, with W1 p_A^UNIT=p_plus and p_B^UNIT=p_minus. In BOTH worlds set p_A^BREAK=p_B^BREAK=uniform16. All terminal unitary contexts are completely depolarizing for both worlds. All breaker Bell outcomes are uniformly sixteen-way in both worlds. Yet TV between the two unitary source laws is respectively 0 and .99. All source distributions strictly positive; the physical operation choice UNIT versus BREAK is announced beforehand. Thus infinite-sample joint unitary-terminal-and-breaker-label observations still do not identify the unitary source contrast.

**Stronger original six-Fourier-only source:** At q0=R and q1=LR with original R0 and six-offdiagonal matrix C0=[[0,.09,.11],[.07,0,.10],[.08,.12,0]], reference W0 uses same C0 both contexts. Alternative W1 uses a different proper target R'=U_X(1/1000)R0, where U_X is an exact rational SO3 Cayley rotation, and alternative SIX coefficients C'^q_ij=C0_ij[S_q(R0)]_ij/[S_q(R')]_ij for all i≠j, all TEN ordinary Fourier moments zero. Exact sixteen-Pauli-history Kraus calculations verify BOTH complete 3×3 terminal channels identical to W0, all 16 conditional source probabilities strictly positive, all ten ordinary moments zero. Yet TV(p'^q0,p'^q1)≈.000429985794844945>0. Independently assign the SAME breaker distribution p0 at both contexts in both worlds: all 16-label Bell outcomes coincide, although unitary source contrasts differ. This is a no-go IN THE FROZEN PRF13 SOURCE CLASS and avoids reliance on nonzero first/second marginals.

No claim of a single global fixed process tensor for these context-conditioned worlds. Such a global comb, if separately established with quantum interventions, carries additional cross-instrument constraints beyond this model.

## 5. Conditional direct TV confidence with 122,144 Bell-label trials

Let q_obs^A,q_obs^B be actual categorical sixteen-label recorded output laws of two Bell-break experiments. Their calibrated TV distance to their latent breaker sources p_A^BREAK,p_B^BREAK is bounded by beta_A,beta_B. Separately let zeta_A=TV(p_A^UNIT,p_A^BREAK), zeta_B analogously; these cross-tester quantities are unknown unless an EXTERNAL premise bounds them.

For a 16-category i.i.d empirical distribution p_hat from n samples and any r>0, TV(p_hat,q)=max over nonempty proper label subsets S of the Bernoulli frequency deviation. By two-sided Hoeffding for one S, union over complementary subsets gives
 Pr(||p_hat-q||_1>r) ≤ (2^16−2) exp(−n r²/2).
For TWO breaker contexts the joint union tail ≤2(2^16−2) exp(−n r²/2), with each empirical TV error≤r/2 on the event.

Write d_hat=TV(p_hat_A,p_hat_B). Then with the joint coverage:
 [d_hat−r−beta_A−beta_B]_+ ≤ TV(p_A^BREAK,p_B^BREAK) ≤ min(1,d_hat+r+beta_A+beta_B).
Only IF independently supplied zeta_A,zeta_B caps are valid may we extend that interval to actual uninterrupted sources by adding zeta_A+zeta_B to both error radii:
 TV(p_A^UNIT,p_B^UNIT) in [[d_hat−r−beta_A−beta_B−zeta_A−zeta_B]_+, min(1,d_hat+r+beta_A+beta_B+zeta_A+zeta_B)].

Specific two-context 95% demonstration:
 r=.022, beta_A=beta_B=.001, externally promised zeta_A,zeta_B≤.0004, alpha=.05.
 n=ceil[2ln(2(65534)/.05)/(.022)^2]=61,072 paired-source-label trials EACH context;
 N=**122,144 trials**, TWO Bell measurements/trial, hence 244,288 Bell readouts.
Actual mathematical tail .0499889924633<.05.
Nominal observed-based unit-source TV CI:
 [max(0,d_hat−.0248),min(1,d_hat+.0248)].
When the TRUE breaker sources equal, d_hat≤r+2beta=.024 on the event, hence U_unit≤2r+4beta+2zeta=.0488<.05 with confidence≥95%. Conversely, if true unit-source pair TV=.05, then lower CI≥.05−2r−4beta−4zeta=.0004>0 on the event. This is a source- and calibration-conditional sample-SUFFICIENT certificate, not an unconditional report of source invariance or a hardware experiment. Without independent zeta, the interval is valid ONLY for BREAK sources.

Actual original synthetic multinomial source tests n61,072/setting with physical valid classical confusion K=(1−.0008)I+.0008 uniform: 1,000 null paired experiments, zero lower-CI false declarations and 1,000 upper certs <.05; 1,000 .05-TV source alternative experiments, all 1,000 detected. Model-only, no hardware, analytic bound is proof.

## 6. New hybrid falsifier of TESTER TRANSPORT, WITHOUT ASSUMING a zeta cap

One can sometimes empirically find evidence that instrument choice changes source behavior. Under the known matched full-frame two-Clifford controls from ROT021, context A uses P R, context B uses D_X P R. For any arbitrary classical Pauli joint sources the aligned output X/input Y source channel contrast E_XY equals (C_B^UNIT−C_A^UNIT) S_XY; since a character is ±1 and |S_XY|≤1:
 TV(p_A^UNIT,p_B^UNIT)≥|E_XY|/2.
Separately two Bell-label sources provide TV(p_A^BREAK,p_B^BREAK) UPPER confidence. The triangle inequality, without any transport premise, gives
 **zeta_A+zeta_B≥[ L_unit−U_break ]_+**,
where L_unit is a unitary-data lower bound on source TV and U_break a breaker-data upper bound on source TV. Hence positivity of their difference REFUTES zeta_A=zeta_B=0 for this class of physical devices. Zero cannot confirm the absence of source reaction.

Detailed calibrated sample certificate using two statistically separate data streams:
 * Each unitary Pauli binary mean has independent statistical error eta_u=.0075, two-readout Hoeffding union ≤4exp(−n_u eta_u²/2).
 * Relative physical known Clifford error delta_rel=.0002; physical Bloch state prep, POVM axis and bias errors each .00005, sum g=.00015 per mean. For arbitrary p, cmax=1 and per contrast systematic ≤2g+delta_rel=.0005.
 * Therefore unitary aligned mean contrast error ≤2eta_u+.0005=.0155; choose L_unit=[|Ehat_XY|−.0155]_+/2. Allocate alpha_unit=.025, n_unit=180,451 samples EACH of the two unitary contexts; actual tail≈.024999736.
 * Bell source categorical deviation r=.011, beta=.001 each context; breaker confidence U_break=min(1,d_hat+.011+.002). Allocate alpha_break=.025, n_break=255,742 two-Bell-label samples EACH context; tail≈.024999000.
 * By union, joint confidence ≥95%. Total physically separate runs **2*(180451+255742)=872,386**, of which 360,902 are two unitary Pauli readout settings and 511,484 are Bell-break trials (TWO Bell measurements EACH).
 * Declared lower CI: [ (|Ehat_XY|−.0155)_+/2 − (d_hat+.013) ]_+.

For the specified PHYSICAL source alternative: UNIT source A=C0, UNIT B=C0 with only C_(output X,input Y) increased by .1 (TV=.05), BREAK source both C0 (TV=0); actual zeta_A=0,zeta_B=.05. All 16 latent distributions are legal/strictly positive. At original R0 the exact source-only unitary measured contrast is 3/35=.0857142857.
For SOURCE-SPECIFIC POWER ONLY, independently assume the common unknown A physical gate is within operator norm .001 of P R0, so contrast ≥.1(6/7−.001)=.0856142857. On the joint sampling/calibration event L_unit≥(.0856142857−2*.0155)/2=.0273071429, and since breaker p_A=p_B, U_break≤2r+4beta=.026. Thus transport lower CI≥**.001307142857>0 with ≥95% probability**. This is a one-sided 95%-sufficient falsification of tester-invariance for that exact model alternative. A smaller/different actual effect could escape detection. This does NOT assume any zeta threshold to establish the lower confidence interval.

Actual seeded aggregate independent physical classical multinomial/Bernoulli model tests at n_unit180451 and n_break255742: 350 transport-stable null runs ->0 false transport reports; 350 instrument-affected alternative ->350 detections, observed minimal transport lower≈.011902. No physical qubit measurements actually executed.

## 7. Exact source execution/provenance

Four independent ORIGINAL local Python programs ACTUALLY EXECUTED:
1. Main SymPy/NumPy full Bell 16-label and finite-n program, local /mnt/data/prf14_rot022/prf14_rot022_two_bell_source_tomography_transport.py, SHA256 dff7341d601f60bc304ba52e6eaafffb9ca4b1b514765483628129b2e6b753a4; original JSON SHA256 c77d2c041704862e5af7a3be86b0f6cc969a0b329eedd9969a269a1fbc35de51. Cold rerun stdout SHA256 c7e12073bb2abeab9ba682aec293e835c7f26a10951ff745897de78bfdbe8b3a exactly reproduced.
2. Independent within-owner direct complex-Born 4x4 Bell POVM and ALL 65,536 categorical subsets, local /mnt/data/prf14_rot022/prf14_rot022_independent_bell_born_and_transport_referee.py, SHA256 366665321e4abcb5fd87cdfd0e41aff42b514ce101f1d39dece3429e3438d066. No imports from main.
3. Independent original six-Fourier-only physical R' and 2x9 Kraus transfer source, local /mnt/data/prf14_rot022/prf14_rot022_six_fourier_unknown_gate_break_transport_alias.py, SHA256 651bce110a4fdd3e82efeebda157cf7b91e159234f0bcea7e40aab53fd0c29f3; native JSON SHA256 a9fda40e28ae18587e364ef9a8e2e8517ac9eb5471c25dff7ebd42028cfa579a.
4. Separate unitary+Bell hybrid statistical source, /mnt/data/prf14_rot022/prf14_rot022_hybrid_tester_transport_95pc.py, SHA256 9c2544dc178701e11bf25e33944db16161d414b4a950c9806392b9933d0ad427; native JSON SHA256 f950b63ad188d6a3e2140573ba46db1af7ddd857c5425bc41856889e90a1d8ab. Second cold execution exactly repeated stdout.

All four Python programs compiled. 2,700 synthetic complete model-trial experiments in total (2,000 paired-Bell multinomial, 700 combined unitary-Bell multinomial/Bernoulli), all synthetic, not hardware. Local ZIP with FOUR original sources, THREE original JSON certs, original stdout and SHA256 manifest contains 14 entries; CRC plus every entry exact byte-wise readback PASS. ZIP SHA256 f85ab0ec218e5136b6ff1ab4f25d738f44da606726199a1b37fd87438c84b672, path /mnt/data/prf14_rot022/prf14_rot022_reproducibility_bundle.zip.

The public GitHub report/certificate code receipts are separate immutable artifacts; preparation of source files does not constitute independent different-cell I1/I2 review.

## 8. Referee falsifiers and explicit limits

AUD3/REC13 should independently check (a) the two Bell Born maps with actual post-first-noise/pre-R and post-R/pre-second-noise ACCESS and destructive reset, (b) p± unrestricted 0 vs .99 TV world and its completely depolarizing full terminal channels, (c) stricter original SIX-only alternate R' physical/source laws all ten ordinary Fourier moments ZERO with exact 0 vs .0004299858 TV worlds, (d) categorical paired 16-source bound factor 2(2^16−2), doubled beta and zeta terms in .0248, .0488, .0004, (e) two-data-stream source transport lower CI and unitary relative-control error, (f) alpha split .025+.025 and 872,386 source-specific 95% power, (g) verify this is NOT an unrestricted process tensor or a nondisturbing observation, and (h) subtract mature 2022 and 13 Nov 2026 causal-break/ancilla theory before any novelty promotion.

Scientific conclusion: a fully informative INSTRUMENT does not imply full information about the corresponding UNINTERRUPTED PROCESS without an independent instrument-transport premise. Combining differing observations can sometimes FALSIFY that premise but can never generally prove it by passing a finite family of tests.

RETURN: PRF14_ROT022 / DIRECT_ROT021_SOURCE_READ / TWO_BELL_BORN_I16_SOURCE_RECOVERY_IN_BREAKER_CONTEXT / GENERAL_SOURCE_TV0P99_CROSS_TESTER_NO_GO / SIX_FOURIER_ONLY_TV0P000429986_CROSS_TESTER_NO_GO / 95PC_CONDITIONAL_SOURCE_TV_122144_BELL_RUNS / 95PC_HYBRID_INSTRUMENT_TRANSPORT_FALSIFIER_872386_RUNS / 2700_SYNTHETIC_MODEL_TRIALS / FOUR_ORIGINAL_EXECUTED_PROGRAMS / ZIP_14_ENTRY_CRC_SHA256_PASS / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN.
