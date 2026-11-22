---
artifact_id: IW_XH_S7_ROT019_2026_QUANTUM_CLOCK_MASS_GIE_PARTIAL_TRACE_N_SCALING_INDEPENDENT_FALSIFIER_001_20261122
date: 2026-11-22
cell: IW_EXTERNAL_SCIENCE_HARVEST_CELL_001_SUCCESSOR_06 / XH-S7
exposure: PUBLIC
mode: ORIGINAL_OUTWARD_SCIENCE_HARVEST / ORIGINAL_SPECIALIST_THEORY_SOURCE / MATHEMATICAL_FALSIFIER / EXECUTED_FINITE_N_TEST / TWO_SURFACE_PRIOR_ART / NEGATIVE_KNOWLEDGE
study_status: ARXIV_V1_PREPRINT_NOT_REPORTED_EXPERIMENT
model_status: ORIGINAL_ARXIV_HTML_FULL_EQUATIONS_READ / INDEPENDENT_EXACT_PARTIAL_TRACE_DERIVED / NUMPY_N1_N2_N3_N4_N6_N8_EXECUTED_PASS / AUTHOR_FINITE_SLAB_SCALE_REPRODUCED
primary_boundary: UNCONDITIONED_SINGLE_CLOCK_N_INDEPENDENT_IN_SOURCE_PURE_STATE_MODEL / MASS_INTERFERENCE_N_DEPENDENT / CONDITIONAL_CLOCK_MEASUREMENT_DISTINCT / AUTHOR_FULL_NONIDEAL_MASTER_EQ_NOT_INDEPENDENTLY_VERIFIED
claim_ceiling: SOURCE_MODEL_INTERNAL_OBSERVABLE_SEMANTICS_FLAG_ONLY / NOT_EXTERNAL_AUTHOR_REBUTTAL / NO_EXPERIMENT / NO_UNIVERSAL_GRAVITATIONAL_NO_GO / NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# XH-S7 ROT019 — Original 2026 quantum-gravity clock-array proposal: exact finite-N reduced-state falsifier, observables and prior art

**22 November 2026.** The one-letter O instructs an independent external research rotation of XH-S7. Responding to standing Moderator direction "Sprawdź aktualności w literaturze. Trzymaj się mocniej funkcji" and deliberately leaving ROT015–016 materials science and ROT017–018 mass-only static gravity.

## 0. Original primary literature read — novelty boundary

Germain Tobar, Markus Aspelmeyer and Magdalena Zych, **"Testing Gravitationally-Induced-Entanglement with Massive Particles and Quantum Clocks"**, preprint arXiv:2611.08313v1, first submitted **5 November 2026**.
Original source: https://arxiv.org/abs/2611.08313 ; primary browser-readable original full text via that source. The actual ORIGINAL arXiv text including Eqs (18)–(24), Appendix A Eqs (32)–(35), Appendix B (39)–(58) and Appendix C Eq (59)–(61) was READ. This was NOT inferred merely from third-party science summaries. Status **theoretical PREPRINT**, not peer reviewed in the checked evidence and not an observed successful entanglement experiment.

Authors propose delocalized source mass (Planck-mass order 2.18e-8 kg) gravitationally coupled to nuclear Sc-45 clocks with energy-dependent passive/active mass-energy corrections, and eventually a crystal slab of N~1e23 clocks. Their clock energy couples as -GM*H_clock/(c² separation), a relativistic correction compared with treating the clock as a fixed c-number rest mass. A long physical dephasing time, ~5e6 s in the proposed finite slab, is presented as potentially observable in future experiments, not measured. They use Eq(21) collective overlap s^N and derive N-enhanced decoherence rate of the MASS wavefunction, which is a valid property of the specified factorized controlled-unitary branch model.

Foundation FIRSTNESS subtraction:
- 2017 Castro-Ruiz, Giacomini and Brukner, "Entanglement of quantum clocks through gravity," PNAS 114, 12, DOI https://doi.org/10.1073/pnas.1616427114 ; theoretical clock-clock gravitational time dilation entanglement. No XH or Tobar novelty in the general principle of gravitational time-dilation-induced clock correlations.
- 2015 Pikovski, Zych, Costa and Brukner, "Universal decoherence due to gravitational time dilation," Nature Physics DOI https://doi.org/10.1038/nphys3366. Standard quantum clock interferometric visibility/decoherence with internal time.
- Closest contemporary Beyer, Önne, Kolkowitz, Bluvstein, Lukin, Ye and Pikovski, "Gravitational Interactions in Nuclear Clocks," preprint 28 October 2026 arXiv:2610.38832, https://arxiv.org/abs/2610.38832, describes mutual gravitational shifts in clock nuclear arrays and distinct geometry scaling; do NOT portray massive clock-array enhancement as invented November 2026.
- Nearest Tobar/et al proposal's distinctive target is a DEL0CALIZED LEVITATED MACROSCOPIC SOURCE mass entangling with internal nuclear clocks. The original paper is a proposal of a geometry and witness, not current evidence of quantized active gravitational mass.

## 1. Specific source claim selected for bounded falsification

Primary original source Eqs:
(18) starts with particle cat |L>+|R> and N initially independent |+> clock superpositions.
(20) defines single-clock overlap s = |<tau_L|tau_R>| = |cos(Delta phi/2)|.
(21) correctly gives particle's branch coherence s^N and decoherence on sqrt(N) shorter time scale under weak identical phase coupling.
(22) is specifically master-equation decoherence of levitated PARTICLE, with its larger N.
(23)–(24) explicitly describe **single-clock reduced density matrix**, "tracing out the motional degree of freedom of the levitated particle and the N−1 clocks", yet attach N to the dephasing kernel and sqrt(N) to the individual clock's off-diagonal.
Appendix A Eq (33) calls s^(N−1) "visibility loss for each individual clock" after tracing other N−1 clocks; Appendix B similarly uses s^(N−1) in a visibility integral (41); Appendix C Eq (59)–(61) labels N-dependent local single-clock kernel.
Central question: is s^(N−1) a scalar of UNCONDITIONED clock-only reduced rho, or instead a coherence of joint mass+selected clock after tracing the OTHER clocks? These are different systems.

## 2. Exact symbolic derivation from authors' OWN explicit state (model boundary, not a general gravity theorem)

Let source mass branches |L> and |R> orthonormal, all N clocks start factorized and evolve under controlled position-dependent gravitational phases to normalized one-clock states |a>=|tau_L> and |b>=|tau_R>. Their Eq (32)/(39) after interaction is:

|Psi_N> = ( |L>|a>^{otimes N} + |R>|b>^{otimes N} )/sqrt(2).
Let s = |<a|b>| and complex omega_ab = <b|a>.

TRACING ALL N clocks yields MASS reduced state:
rho_P = 1/2 ( |L><L|+|R><R| + omega_ab^N |L><R| + conj(omega_ab)^N |R><L| ),
and its normalized interferometric coherence is **s^N**. This mathematically supports the authors' collective speedup for a particle interferometer in their idealized model.

TRACING mass P AND other N−1 clocks to isolate one SPECIFIC CLOCK yields:
rho_C1 = 1/2( |a><a| + |b><b| ).
There is NO N in this expression under the stated initial product clocks and conditional-local evolution. Its purity and local computational-basis offdiagonal are N-independent for fixed local coupling and one-clock phase:
Tr rho_C1² = (1+s²)/2. The one-clock relative contrast for the symmetric phase gauge chosen below is s.
In particular N=1 and N=1e23 have exactly the same unconditional single-clock density matrix IF its local physical coupling/environment is held fixed and interactions via a moving quantum source back-action and clock-clock terms beyond the authors' specified ideal conditional branch state are ignored.

TRACING ONLY the OTHER N−1 clocks while retaining P + clock1 gives:
rho_{P,C1} = 1/2 sum_{i,j in {L,R}} |i><j| tensor |tau_i><tau_j| ( <tau_j|tau_i> )^(N−1).
Thus its offdiagonal P block has trace norm **(1/2)s^(N−1)**. This is exactly where the authors' source Eq (33) factor naturally belongs. It is **not** the clock-only local offdiagonal rho_{01}, because an additional trace over P kills that block.

Conditioning on a SUCCESSFUL mass measurement P=|+> can yield N-dependent reduced state of clock1 through the coherent cross term with s^(N−1), and also an N-dependent probability of postselection. A conditional readout protocol may therefore remain viable; a genuine inferential comparison must distinguish:
A) particle interference / particle+array entanglement;
B) unconditional single-clock Ramsey visibility;
C) particle+clock1 JOINT coherence, not directly measured by clock alone;
D) clock1 statistics CONDITIONAL on measured mass and success probability.
Source proposed protocol DOES discuss recombining and measuring the particle. It cannot be assumed fully refuted by this local observable counterexample. Still, Eqs (23)/(24) explicitly claim a single-clock REDUCED RHO after tracing P and all other clocks, so the inconsistency merits independent specialist mathematical review.

This is a statement about exact state reductions in the explicitly given model. We did NOT reproduce original realistic trap mass-energy motion, non-Markovian coupling, Born approximations, crystal many-body interactions, noise PSD or final lab observables.

## 3. Independent exact local computation ACTUALLY executed: NumPy tensor states and partial traces

Created and EXECUTED locally:
- SCRIPT /mnt/data/xh_s7_rot019_clock_partial_trace_test.py, SHA256 **185bbfe4676ee38dd9ae8090ee33b887b0249a4f6b4572a59d5d20f2230f2c68**
- JSON RECEIPT /mnt/data/xh_s7_rot019_clock_partial_trace_receipt.json, SHA256 **84e80c47a738b2157953f54b539a1016f9611313b6665bebd83d7ff89479edb3**

Concretely define phi=1.1 rad and a=(e^-i phi/4|0>+e^+i phi/4|1>)/sqrt2, b=(e^+i phi/4|0>+e^-i phi/4|1>)/sqrt2; overlap s=cos(phi/2)=**0.8525245220595057**.

Explicitly form normalized full 2^(N+1) state tensor for N=1,2,3,4,6,8 (no source code merely cited; local NumPy executed). Compute rho_P, rho_C1, rho_(P,C1) through actual multidimensional einsum traces; calculate original mass visibility, clock computational coherence, clock purity, joint-P+C1 offdiagonal 2x2 block nuclear norm and POSTSELECTED P=|+> single clock contrast/probability. Assertions compare with analytic independent s^N,s,s^(N−1) to <4e−13.

Observed for N=1: particle contrast .8525245, unconditional clock contrast .8525245, joint offdiag scaled 1.
N=2: particle .7267981, unconditional clock .8525245, joint .8525245.
N=3: particle .6196132, unconditional clock .8525245, joint .7267981.
N=4: particle .5282354, unconditional clock .8525245, joint .6196132.
N=6: particle .3839205, unconditional clock .8525245, joint .4503336.
N=8: particle .2790327, unconditional clock .8525245, joint .3273016.
For all N, clock purity is 0.863399030356394 within roundoff. Selected single-clock postselected contrast varies (1, .9874, .9751, .9633, .9414, .9224), illustrating measurement-conditioning difference. Full receipt contains all 2x2 reduced clock matrices.

Result is **EXACT FINITE-N MATHEMATICAL FLAG / SOURCE OBSERVABLE TARGET SEMANTICS**, NOT "paper disproved" and not a graviton observation. The global mass decoherence claim remains true within these specified Hamiltonian assumptions.

## 4. Independently computed physical example, exact numeric source formula

Original source finite-density crystal formula Eq(8)/Eq(63):
t_finite ≈ [2 c²/(G M_p omega_c Delta x)] sqrt[2 D/(pi n)].
Source parameters: M_p=2.18e-8 kg, D=450e-6m, angular omega_c=1.82e19 /s, Delta x=1e-7m, n=4e28/m³, Newton G=6.67430e-11, c=299792458.
Independent Python source formula result **5,744,524.936059602 seconds = 66.48755713 days**. Authors state order ~5×10^6 s / ~64 days. Agreement at rounding/order level, NOT independent engineering feasibility verification. SOURCE single-clock (for near-face same d) characteristic t~1.3745572e16 seconds (hundreds of millions years) in two-branch small superposition formula. Thus the collective N effect is in mass mode/conditional joint phenomenon, not automatically a local Ramsey-rate enhancement.

Separate minor algebra note: Appendix A source Eq(28) prints cos(x) approximately 1−x², whereas exact Taylor is cos(x)=1−x²/2+O(x^4). Our numeric check (1−cos(0.001))/0.001² = **0.4999999583**. This is an independently confirmed isolated equation-level factor-of-two flag, NOT by itself a full error correction of all model times (definitions/approximations need source matching).

## 5. Direct competing prior art and epistemic ceiling

Already-established source foundations of gravitational internal-energy-clock dynamics and quantum interferometry are in Castro-Ruiz, Giacomini & Brukner PNAS 2017 and Pikovski et al Nature Physics 2015. Beyer et al Oct2026 nuclear clock arrays covers related enhancement but with distinct mutual internal clock gravity/geometry; do not invent same observable/claim. Cross-literature possible issue with extracting local clock dephasing vs collective particle visibility is a STANDARD partial-trace/marginal distinction; NOVELTY for NASH not asserted.

No publicly observed gravitation-mediated particle-nuclear-clock entanglement was found or rerun, no noise/clock control device operated, no future predictions adopted as empirical fact, no user-appointed contact with authors. This bounded flag is supported by exact primary source Eqs18–24 and independent explicit partial trace, and could be a technically appropriate **question to authors / independent mathematical referee** if Moderator chooses, not unilaterally declare journal misconduct/falsification of all conclusions.

One unambiguous question for a future independent referee:
"Starting from Eqs (18)/(32), explicitly evaluate Tr_{P,C_2...C_N} |Psi_N><Psi_N| for a selected clock. If this yields the N-independent 1/2(|tau_L><tau_L|+|tau_R><tau_R|), what precise conditional, joint, or different state does Eq(23)/(24) describe, and how exactly is its sqrtN enhancement accessed by the proposed observable, with or without particle postselection?"

Keep scientific state:
PRIMARY_SOURCE_READ_PASS /
EXACT_REDUCED_MASS_SPOWER_N_PASS /
EXACT_UNCONDITIONED_SINGLE_CLOCK_NO_N_PASS /
EXACT_RETAIN_P_C1_CROSS_BLOCK_SPOWER_N_MINUS1_PASS /
CONDITIONAL_CLOCK_N_DEPENDENCE_POSSIBLE /
AUTHOR_EQ23_24_LOCAL_RHO_SEMANTICS_REVIEW_FLAG /
FINITE_SLAB_5P7445E6_SOURCE_FORMULA_REPRO_PASS /
NO_AUTHOR_COMMUNICATION / NO_NEW_NASH_PHYSICS /
NO_NASH_NOVELTY / NO_CANON / NO_EXEC_SIGN.

End of ROT019 source report. Public Github readback not equal BW/independent peer acceptance.
