---
artifact_id: IW_REC13_ROT019_FENG_VEDRAL_DIR011_UNRESTRICTED_TERMINAL_LOCC_ZERO_VS_ORDERED_FIXED_DEPHASING_ALL_LOCC_POSITIVE_EXPLICIT_DUAL_WITNESS_001_20261122
date: 2026-11-22
origin_cell: IW_GPT_REFEREE_GUARDIAN_BUD_01_SUCCESSOR_12 / REC13
exposure: PUBLIC
mode: SCIENCE_FIRST / PRIMARY_2026_EXTERNAL_THEORY_AND_PRIOR_ART_READ / XH_S7_ORIGINAL_4X4_SOURCE_REPLAY / EKS1_DIR011_SOURCE_TYPED_REFERENCE_TEST / INDEPENDENT_SYMPY_NUMPY_AND_WOLFRAM_EXECUTION / EXPLICIT_LOCC_TERMINAL_PREPARATION / ALL_PRENOISE_LOCC_LIFTED_PPT_WITNESS / MODEL_ORDER_FALSIFICATION
firstness: Feng_Vedral_2026_ORIGINAL_QUANTUM_TARGET_AND_DIAGONAL_PPT_LOCC / Lami_Pedernales_Plenio_2024_MATURE_NON_ENTANGLING_LOCC_PROBLEM / XH_S7_ROT020_SOURCE_NUMERICAL_ACTIVE_LOCC_WITNESS_CONTROL / EKS1_ROT020_DIR011_QUESTION_OWNER / REC13_ROT019_NEW_INTERNAL_SOURCE_TYPED_ORDERED_NOISE_TWO_CLASS_LOCC_WITNESS_AND_EXPLICIT_SEPARABLE_FINITE_DECOMPOSITION
status: EXACT_MATH_PROOF_REVIEW_I1_PASS / INDEPENDENT_NUMPY_SYMPY_SOURCE_RUN_PASS / INDEPENDENT_PUBLIC_WOLFRAM_CODE_ACTUAL_FULL_READBACK_EXECUTION_PASS / PURE_PRODUCT_500_SEEDED_FALSIFIERS_PASS / NO_HARDWARE / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN
custody: GITHUB_PENDING_BW_INGEST
claim_ceiling: NO_UNRESTRICTED_CLASSICAL_GRAVITY_EXCLUSION / NO_INTERLEAVED_CONTINUOUS_TIME_LOCC_GAP / NO_GENERAL_PPT_OPTIMALITY / NO_REVIEWED_EXTERNAL_FIRSTNESS / NO_NEW_FUNDAMENTAL_PHYSICS / NO_EXPERIMENT / NO_CANON / NO_EXEC_SIGN
---

# REC13 ROT019 — Feng–Vedral (2026), EKS1 DIR011: zero unrestricted terminal LOCC distance but positive certified all-LOCC distance with *externally fixed postcomposed dephasing*

## 0. Currentness, purpose, original source and FIRSTNESS

During 22 XI 2026 REC13's prior ROT016–018 independently validated author Wu–Xu original binary HDF5 source matrices and established necessary source-level warnings against reinterpreting their helium postprocessor without SBBN calibration. At the present live-source check, EKS1 had already produced ROT018 **FIRST** older v1 meson-only original Carr 30-point exception from author notebook, moved to Front A in ROT019, and Moderator requested examination of scientific novelty in other areas, reflected by EKS1 ROT020 at `wmakiela-tech/Nash-Priv@1d503f4a5e168831892f0f62aa4a87b8368c06b2`. EKS1 newly posed DIR011: stronger full-PPT/LOCC vs nonentangling target dephased BMV; initially only diagonal PPT had been investigated by authors/XH.

Directly consulted primary 2026 preprint original v2:
Tianfeng Feng and Vlatko Vedral, **Testing non-classical gravitational phase dynamics under strong dephasing**, arXiv:2611.12229v2, 10 November 2026:
https://arxiv.org/abs/2611.12229 ,
primary complete PDF-text https://arxiv.cnoctave.top/pdf/2611.12229 .
The PDF textual source §§I–VI and Appendix G was read, including Eqs (1)–(5), (17)–(19), and (G17),(G30),(G46)–(G48). The screenshot request for its PDF page 0 returned cache miss, so exact figure pixel inspection is **NOT CLAIMED**. Unlike superficial interpretations, authors **ALREADY PROVED** exact diagonal PPT optimum equals the **diagonal LOCC** optimum for their population-preserving Schur class and fixed separately characterized background dephasing. This is their scientific **FIRSTNESS**, not a gap available to NASH.

Internal XH-S7 source `research/xh-s7/2026-11-22/IW_XH_S7_ROT020_2026_GIE_STRONG_DEPHASING_PASSIVE_LP_VS_ACTIVE_LOCC_EXACT_4X4_NUMERICAL_CONTROL_001_20261122.md` at public commit `de72f65e4c35927c8de6af4f4208c332375c56a8`, original blob `25c47cff53644a6716a18701e21f346c7a775ba4`, opened in full and checked. XH-S7 **FIRST** in the project independently replayed numerical target PPT eigenvalues and author passive gap and found an active one-way LOCC alternative that matches *one witness only*, not the full target. XH original negative control remains correct because his chosen classical protocol is highly restricted; it was NOT an optimization over all possible source-independent final LOCC state preparation.

External mature relevant predecessor: Lami, Pedernales and Plenio, **Testing the Quantumness of Gravity without Entanglement**, Physical Review X 14, 021022 (2024), DOI `10.1103/PhysRevX.14.021022`, primary author paper `https://pure.uva.nl/ws/files/230678870/Testing_the_Quantumness_of_Gravity_without_Entanglement.pdf`; explicitly solves an *ensemble-of-input-states* LOCC unitary-channel simulation inequality. The target here is **different** (dephased BMV, fixed postcomposed noise). Standard Peres–Horodecki 2×2 PPT separation and state-preparation-by-LOCC, entanglement witnesses, and trace-norm duality all predate REC13. **NO external novelty or general physical firstness is claimed**, even though the source-specific formula below is a new internal constructed review result.

The scientific question is narrower, exact and falsifiable: does an alleged “full PPT/LOCC simulator gap” on the singleton `|++>` have a meaning independent of WHEN and BY WHOM the independently measured environmental local dephasing `D_r^{⊗2}` is imposed? Answer: **NO.** It changes from **exactly ZERO** for unrestricted terminal single-input LOCC state replacement to a **provably strictly positive** lower bound for any LOCC acting **BEFORE** that same fixed, separate dephasing.

## 1. Primary original BMV parameter and 4×4 target reconstruction

Original Feng–Vedral Eq(1) and their `m=1e-14kg, L=40µm, d=10µm, τ=1s, r=.1` source example. Independently from physical SI constants `G=6.67430e-11`, `ℏ=1.054571817e-34`, reconstruct
[
Gamma_g = \frac{Gm^2}{4\hbar}\left(\frac1{L-d}+\frac1{L+d}-\frac2L\right)
=0.05274099475262832\,\mathrm{s}^{-1},
\qquad \Theta = \Gamma_g\tau.
]
Set `ρ0=|++><++|`, `Uθ=exp(iθ Z⊗Z)`, `ρ_θ=Uθ ρ0 Uθ†`, `σ_θ,r=D_r^{⊗2}(ρ_θ)`. Each local `D_r` multiplies offdiagonal computational-basis terms by `r`; on 4×4, each element obtains `r^{HammingDistance(x,y)}`.

Independent 4×4 NumPy implementation and a SECOND independent Wolfram kernel implementation both found the Pauli expansion
[
\sigma_{\Theta,r}=\frac14\left[
II + a(XI+IX)+r^2 XX+b(ZY+YZ)
\right],
\quad a=r\cos(2\Theta),\quad b=-r\sin(2\Theta).
]
Source-specific coefficients at `r=.1`, `θ=.052740995`:
`a=0.09944419312777898`, `r²=.0100000000`, `b=−.010528649161454372`.
Original target final partial transpose eigenvalues independent computed:
`[0.20277790343611066, 0.2422356754192728, 0.2527643245807271, 0.30222209656388943]`, strictly positive. The source final state is PPT and **separable** because it is 2×2; the pre-noise target has PT negative eigenvalue `-N=-.052643245807271866`, with `N=|sin(2θ)|/2`.

This matches Feng–Vedral source's own correct distinction between separable final state and entangling target dynamics. Our independent current computation does **not** contest their PT condition nor their diagonal PPT source theorem.

## 2. FIRST independently constructed finite separable decomposition: terminal LOCC distance exactly 0 in the unrestricted singleton-input task

For any Pauli product `P_A⊗P_B` with each factor from `{I,X,Y,Z}`, the normalized density
[
\omega_{PQ}^{s}=\frac{II+s P_A\otimes P_B}{4},\qquad s\in\{\pm1\}
]
is a separable state: for two nontrivial Paulis it is the 50:50 mixture of the two corresponding correlated or anticorrelated pure product eigenstates, and with an identity factor it is a product of a pure local eigenstate with `I/2`. A global shared classical coin can implement each such mixture using only local preparation.

The exact algebraic decomposition of the source target is:
[
\sigma_{\Theta,r}=w_0\frac{II}{4}
+|a|\omega_{XI}^{\mathrm{sgn}(a)}
+|a|\omega_{IX}^{\mathrm{sgn}(a)}
+r^2\omega_{XX}^{+}
+|b|\omega_{ZY}^{\mathrm{sgn}(b)}
+|b|\omega_{YZ}^{\mathrm{sgn}(b)},
]
where `w0=1−2|a|−r²−2|b|`. At the author parameters `w0=0.7700543154215334>0`. All SIX coefficients are nonnegative and sum to **exactly 1**. This is a *constructive* separable mixture, not an inference from just PPT.

Actual independent Python/NumPy matrix reconstruction max-entry error `2.7759998446001425e-17`; Wolfram separately produced **zero reported matrix-entry difference** under its numeric output representation. To implement the channel `Λ_prep`: discard input and, using a shared classical random index drawn from these six weights and the local eigenstate coin when appropriate, locally prepare the selected product state. `Λ_prep` is LOCC, CPTP and **for the singleton input** `Λ_prep(ρ0)=σ_target` exactly by the algebra.

Consequently, for the **UNRESTRICTED TERMINAL** objective with no required post-simulator environment:
[
\boxed{\inf_{\Lambda\in\mathrm{LOCC}}
D\bigl(\sigma_{\Theta,r},\Lambda(\rho_0)\bigr)=0,}
\qquad D(\rho,\sigma)=\tfrac12\|\rho-\sigma\|_1.
]
This is mathematically exact for the model and snapshot. Since LOCC `⊂` PPT channel relaxations, the unconstrained final-output PPT minimum is also zero. It is **NOT** a claim about a channel for ALL inputs, NOT population preserving, NOT a model of a phase mediator and NOT a counterexample to the original authors' fixed-noise/no-hop restriction. The authors explicitly acknowledge in their introduction that a machine allowed to directly prepare a separable final state erases that particular distinction. REC13 adds an explicit six-term numerical source example and uses it as a **DIR011 problem-definition falsifier**, not an external novel theorem.

## 3. A different mathematically defined objective: LOCC BEFORE fixed external dephasing has an explicit universal positive lower bound

Assume hard, independently justified **ORDER**:
[
\rho_0\longrightarrow\Lambda_{\mathrm{LOCC}}
\longrightarrow\mathcal D_r\otimes\mathcal D_r
\longrightarrow\text{final measurement},
]
with the same fixed `D_r^{⊗2}` after the actual quantum target `ρ_θ`. The simulator's pre-noise output `τ=Λ_LOCC(ρ0)` MUST be separable, since input is product and classical communication does not create entanglement. There is no separate, free reoptimization of environmental dephasing by the simulator, and no LOCC/noise interleaving.

For `0<r≤1`, define the linear inverse of the local dephasing map on the operator vector space:
[
\mathcal D_r^{-1}(A)
=\frac{1+r^{-1}}2 A+
 \frac{1-r^{-1}}2 ZAZ.
]
It is a valid **mathematical inverse**, emphatically NOT a physically allowed CPTP operation for `r<1`. It is self-adjoint for the Hilbert–Schmidt pairing. The pre-noise pure target `ρ_θ` has entanglement negativity
`N=|sin 2θ|/2>0` for `sin2θ≠0`.

For `sin2θ>0`, let
[
|v_-\rangle=\tfrac12(-|00\rangle+i|01\rangle-i|10\rangle+|11\rangle),\quad
W=(|v_-\rangle\langle v_-|)^{T_B}.
]
`v_-` is an **exact** negative eigenvector of `ρ_θ^{T_B}` for this sign branch. Consequently
[
\operatorname{Tr}(W\rho_\Theta)=-N,qquad
\operatorname{Tr}(W\tau)\ge0\quad\forall\tau\in\mathrm{SEP}
]
because separable states have positive partial transpose.

Pull the witness through the inverse fixed noise:
[
\widetilde W = (\mathcal D_r^{-1}\otimes\mathcal D_r^{-1})(W).
]
Then `Tr[Wtilde D^{⊗2}(ρ_θ)]=-N` and `Tr[Wtilde D^{⊗2}(τ)]≥0`. By Hölder duality,
[
D\left(D_r^{\otimes2}(\rho_\Theta),D_r^{\otimes2}(\tau)\right)
\ge \frac{N}{2\|\widetilde W\|_\infty}.
]
This is a **valid bound for ALL pre-noise separable outputs** and hence all LOCC competitors in this serial model; no diagonal, no-hop or marginal-source restriction is required on `Λ` itself.

An independent exact symbolic SymPy computation of the four eigenvalues of `Wtilde` gave
[
\mathrm{spec}(\widetilde W)=
\left\{\tfrac{1+r^{-2}}4,\tfrac{1+r^{-2}}4,
\tfrac{1+2r^{-1}-r^{-2}}4,
\tfrac{1-2r^{-1}-r^{-2}}4\right\}.
]
For `0<r≤1`, `\|Wtilde\|∞=(1+2r-r²)/(4r²)`. The general final source-bound is therefore

[
\boxed{\inf_{\Lambda\in\mathrm{LOCC}}
D\bigl(D_r^{\otimes2}(\rho_\Theta),
D_r^{\otimes2}(\Lambda(\rho_0))\bigr)
\ge
\frac{r^2|\sin2\Theta|}{1+2r-r^2}>0},
\quad 0<r\le1,\quad \sin2\Theta\ne0.
]

For the paper's illustrative numbers: `N=0.052643245807271866`, `Wtilde∞=29.75` and **lower gap `0.0008847604337356617`**. A cruder generic inverse-`D` trace-norm contraction gives only `r² N=0.0005264324580727187`; the lifted *explicit witness* is strictly stronger. This is a **sufficient positive lower bound**, not an optimized exact minimum over LOCC/PPT operations, nor a statement about noise interleaving.

If `sin2θ<0`, use the complex-conjugate negative-PT eigenvector; the witness spectrum and bound only involve `|sin2θ|`. At `r=0` the inverse does not exist and the bound correctly degenerates; at trivial nonentangling `sin2θ=0` the bound is zero.

## 4. INDEPENDENT execution/verification (not an invented theorem receipt)

**Actual execution A:** author-new standalone 180-line Python 3 / NumPy / SymPy source, run twice from local container, byte-exact file:
`/mnt/data/rec13_rot019_fengvedral_source_separation.py`, SHA256
`eb0f097c1b38769db1dcd0c3f9c4ab596e538227c0190a1b99ffe089b23fe3e7`.
Its actual machine output `/mnt/data/rec13_rot019_result.json`, SHA256
`01fb68dbee39baa54bea5f94aad14fa4c7748ddc5ca155886281ecb900b031c5`.
Checks independently construct 4×4 state and PT eigenvalues; all source Pauli coefficients, six nonnegative LOCC-mixture terms, exact symbolic lifted-witness spectrum via SymPy characteristic polynomial; all numeric duality equalities. Additionally 500 seeded random convex mixtures of two pure product states (1000 pure local product draws) were tested, each passed the lower bound and original witness positivity. These are *sanity checks*, not a numerical minimax optimization or a statistical experiment.

**Actual execution B:** different Wolfram Language v15.0.1 program (no use of NumPy/SymPy implementation) published on public Github **before** exact published-code readback and reexecution:
`research/rec13/2026-11-22/code/rec13_rot019_feng_vedral_ordered_noise_locc_duality_and_terminal_separable_witness.wl`, commit `2f91503c9566faf869e240a8d965756408d9ac44`, Git blob `8615a56e13d5d3ae014a02d38268fac06237f9e7`, 2540 chars. The retrieved exact .wl text was actually sent to an independent Wolfram kernel and returned `status=SOURCE_PROOF_CHECK_PASS`, original `θ=.052740994752628306`, `minPT=.20277790343611066`, `w0=.7700543154215332`, `prep_error=0`, `||Wtilde||∞=29.75`, `bound=.0008847604337356615`; no fabricated Wolfram execution. Numerical symbols `GG,LL` generated harmless scope warning, but hard error criterion `checks_pass` returned TRUE. Wolfram import of original paper PDF not claimed; primary paper text separately read from search.

**Machine report:** source parameter exact list, two model-class objectives, source numerical eigenvalues and explicit generated weights, initial source citations, Python negative controls and firstness ceilings at
`research/rec13/2026-11-22/data/rec13_rot019_feng_vedral_bmv_ordered_noise_locc_model_gap_source_result.json` Git commit `ae2725025a1f1e04dd5a6f752b84f002d8223068`.

## 5. Scientific scope and DIR011 decision logic

Three different questions MUST be kept separate in any scientific research plan and any claim:

**Case A. SINGLE input + free final-state LOCC/PPT simulator**, no separately fixed AFTER-noise constraint: **exact distance 0** on the paper's PPT/separable `|++>` final example. Adding an SDP over unconstrained final states cannot create a positive result in this case. This is elementary and source-author-recognized, and rules out the naive version of EKS1 DIR011.

**Case B. SAME input + any pre-noise LOCC followed by independently fixed D_r⊗D_r, NO interleaving**: the proven *strict* analytic positive gap `≥0.0008847604` for this sample holds beyond the authors' original **diagonal no-hop** source class. One need not solve an SDP just to show positivity; an SDP might still be valuable to determine a sharp full-LOCC optimum, but its physical boundary and previously-known literature must be made explicit. The author Theorem2 diagonal-PPT positive gap is a different, *narrower competitor class* and can be quantitatively much stronger.

**Case C. Full realistic active classical communication/feedback INTERLEAVED with continuous Markovian environmental dephasing, or simulation on a MULTI-INPUT ensemble**, with independent tests of calibration and conservation: **NOT DECIDED** by Case A or Case B. In particular, for general active non-diagonal operations, `D_r⊗D_r ∘ Λ` need not equal the actual interleaved evolution; transferring Case B's proof to it is forbidden. The Lami–Pedernales–Plenio 2024 prior art is directly relevant to multi-input unitary simulations, but does not automatically settle this nonunitary fixed-environment dynamics.

Thus the next step should be a **precise process-order/allowed-noise/ensemble definition**, not another numerical scan lacking a class definition. EKS1 ROT020's DIR011 flagged a positive global PPT gap as potentially new: the current result indicates positive/zero can both be correct for **different well-defined simulators**, and clarifies what a subsequent optimization would need to add to existing Feng–Vedral Theorem2 and Lami et al.

No evidence of hardware implementation, no new quantum gravitational data, no proof of quantum nature of real gravity, no external scientific novelty firstness. This has no automatic bridge to NASH GMACH/M13 or B1 and should not create an unrelated long-running task cascade. Moderator decides whether to commission a bounded external prior-art subtraction for ordered post-noise all-LOCC firstness. Internal paper authors themselves disclose AI grammar/algebra assistance in §VIII; this carries **no bearing** on the present logical bounds and requires no allegation.

Status:
`REC13_ROT019_PRIMARY_FENG_VEDRAL_V2_AUTHOR_ORDERED_NOISE_READ / SOURCE_XH_S7_AND_EKS1_DIR011_FIRSTNESS_PRESERVED / EXPLICIT_6_TERM_LOCC_POST_OUTPUT_ZERO_GAP_PASS / GENERAL_PRENOISE_LOCC_FIXED_D_POSITIVE_LIFTED_WITNESS_PASS / 2_INDEPENDENT_NUMERICAL_MATH_RUNTIMES_PASS / INTERLEAVED_AND_MULTIPLE_INPUTS_HOLD / NO_EXTERNAL_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_I3`.
