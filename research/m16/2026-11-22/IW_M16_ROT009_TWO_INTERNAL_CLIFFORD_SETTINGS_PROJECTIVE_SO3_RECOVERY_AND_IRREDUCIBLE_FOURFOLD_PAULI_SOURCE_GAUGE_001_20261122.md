---
artifact_id: IW_M16_ROT009_TWO_INTERNAL_CLIFFORD_SETTINGS_PROJECTIVE_SO3_RECOVERY_AND_IRREDUCIBLE_FOURFOLD_PAULI_SOURCE_GAUGE_001_20261122
return_id: IW_M16_ROT009_TWO_INTERSTAGE_CLIFFORD_CONTROLS_BREAK_CONTINUOUS_SOURCE_GATE_ALIAS_BUT_FOURFOLD_PAULI_KLEIN_SOURCE_TV_NO_GO_001_20261122
origin: IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_11 / M16
date: 2026-11-22 Europe/Warsaw
exposure: PUBLIC
science_type: SOURCE_CONDITIONAL_QUANTUM_OBSERVER_IDENTIFIABILITY / TWO_GENUINE_INTERSTAGE_CONTROLS / PROJECTIVE_SO3_RECONSTRUCTION / PAULI_KLEIN_FOUR_GAUGE / EXACT_SOURCE_TV_NO_GO / EXTERNAL_PRIOR_ART_SUBTRACTION
status: ORIGINAL_PRF14_ROT024_AND_ROT025_DIRECT_READ / PRIOR_M16_ROT008_DIRECT_READ / FRACTION_EXACT_AND_SECOND_INDEPENDENT_RANDOM_RATIONAL_EXECUTION_PASS / REPEATED_BYTE_IDENTICAL / NINE_FILE_ZIP_CRC_BYTE_PASS
ceiling: NO_GENERAL_NOVELTY / NO_PHYSICAL_QUANTUM_DEVICE / NO_UNRESTRICTED_PROCESS_TENSOR / NO_CANON / NO_EXEC_SIGN / NO_BW_NATIVE_WRITE
---

# M16 ROT009 — rozdzielenie prawdziwie wewnętrznego sterowania kwantowego od pozornej nadmiarowości danych

## 0. Problem i firstness

Po M16 ROT008 different-cell I1 PRF14 ROT024 wiadomo, że DWIE dodatkowe końcowe kontrole Clifford, nakładane PO całym obserwowanym kanale, nie przełamują dokładnej niejednoznaczności source/gate: jeśli cały kanał T jest identyczny w dwóch światach, także D_X T jest identyczny. Należy sprawdzić rozwiązanie konstrukcyjne, nie kolejne wyostrzanie sztucznej liczby pomiarów: czy rzeczywiście dodatkowa ZNANA operacja MIEDZY dwoma etapami błędów Pauliego zwiększa identyfikowalność źródła, a jeśli tak, jaki zakres pozostaje niemożliwy.

Bezpośrednio przeczytane, nie tylko z pamięci:
- PRF14 ROT024 source original full 20,722 characters, commit 743a65e0e73677a3191bd6acd01df5f3486be7e8, blob 7b7a87df05e404e2b8af96755bf946c1fbbabc7f:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/743a65e0e73677a3191bd6acd01df5f3486be7e8/research/prf14/2026-11-22/IW_PRF14_ROT024_TWO_ROW_SO3_ORTHOGONALITY_SOURCE_TRANSPORT_FOUR_CHARACTER_95PC_TV_LOWER_AND_PHYSICAL_NO_GO_001_20261122.md
- PRF14 ROT025 source prior-art subtraction full 19,287 chars, pinned commit 159144f543923d10a22957ed537dc0a74cfb1dff, blob e18aa585264b47d383899f21ad25ba5060a1533d:
  https://github.com/wmakiela-tech/Nash-iw-research/blob/159144f543923d10a22957ed537dc0a74cfb1dff/research/prf14/2026-11-22/IW_PRF14_ROT025_DOCTORAL_PRIOR_ART_EXACT_THEOREM_AUDIT_WHITE_WANG_XU_LI_IST_AND_INSTRUMENT_TRANSPORT_DECISION_001_20261122.md
- M16 ROT008 original independent source I1, commit e8300da47f9327d200827fb92d99fb39a5e5f7b3, blob 8d0440a0a9229668de725f08ccc668fbfc687b01, full direct read.
- External live original publisher arxiv arxiv:2611.05561 Xu/Liu/Chen "SPAM-robust learnability of quantum dynamics" (Nov 2026), published abstract and a first-party PDF excerpt: cycle-space gauge and Pauli sign freedom prior art. Broad non-identifiability and SPAM cycle-space are mature. Original 2017 Nature Communications GST paper https://www.nature.com/articles/ncomms14485 and 2025 npj QI https://www.nature.com/articles/s41534-025-00976-4 also describe unobservable gauge degrees of freedom. Detailed global novelty literature search not complete. NO_NOVELTY.

Owner firstness: PRF14 owns the original physically valid p16 + unitary and BREAK model, nontrivial 2-row source transport falsifier and W0/W1 exact 18-channel no-go. M16 ROT008 verified those statements. ROT009 asks a NEW, narrowly scoped constructive intra-stage intervention question; not a general quantum reconstruction theorem, does not change PRF credit or autonomous research mandate.

## 1. Strong source contract (conditional, not actual apparatus)

Two classical two-bit Pauli error labels v,w independently representing two timed error intervals, arbitrary strictly positive 16-outcome correlation law p_UNIT(v,w). The PROTOCOL is announced before the errors. On a single two-time UNIT block, the unknown physical proper rotation S in SO(3) and a KNOWN proper cyclic Clifford P between error intervals give two different experiments:
- Setting 0: M_0 = E_{p_UNIT} [ D(w) S D(v) ].
- Setting 1: M_1 = E_{p_UNIT} [ D(w) P S D(v) ].

**LOAD-BEARING extra premise**: source p_UNIT(v,w) is the SAME for both distinct intra-stage settings, and S is the SAME. The hardware must implement P at exactly the interface between error intervals, not AFTER whole M_0; P must be physically calibrated, and the qubit Bloch 3x3 channel must be observed sufficiently for the stated exact-identification idealization.

Take PRF ROT024 "SIX ONLY" source class: ALL ordinary one-time Pauli Fourier and ALL THREE diagonal mixed Fourier are zero; exactly SIX potentially nonzero off-diagonal mixed:
  C_ij=E[chi_j(v)chi_i(w)], i≠j;
  C_ii=0;
  1 constant Fourier coefficient 1, six offdiagonal active, nine other nonconstant zero.
All six C_ij ≠0; S entries used in ratios nonzero. Source strictly positive and p uniquely determined by C within THIS 6-parameter family.

Then
  M_0,ij=C_ij S_ij;
  M_1,ij=C_ij (P S)_ij;
and P=[[0,0,1],[1,0,0],[0,1,0]] on the Bloch coordinate X,Y,Z.

If P were a FINAL post-channel operation instead of intra-stage, the output would be P M_0; there would be no new independent equation for C or S. These cases MUST NOT be conflated.

## 2. Exact two-setting identifiability theorem UP TO FOUR PAULI SIGNS

For each input column j and the two offdiagonal output rows i≠j, define the observable exact ratios:
  r_ij=M_1,ij/M_0,ij = S_((i−1) mod 3),j / S_i,j.

For j=0 the two ratios link rows (0,1) and (1,2); for j=1 they link (2,0) and (1,2); for j=2 they link (2,0) and (0,1). In each case the TWO directed ratio edges form one connected three-vertex tree. Hence all THREE entries of column S_:j are determined UP TO ONE common nonzero scalar. Column-unit norm fixes its absolute scalar, leaving ONE unknown ± sign per column. Proper orientation det S=+1 forces product of the three column signs to +1. Thus there are AT MOST FOUR possibilities, exactly the group
  D=diag(d0,d1,d2), d_j∈{±1}, d0 d1 d2=+1,
i.e. the identity and THREE nontrivial Pauli frame rotations (Klein four).

Conversely ALL FOUR possibilities are real source/gate aliases for the 6-offdiagonal positive source class:
  S_D=S D;
  C_D,ij=C_ij d_j;
  p_D(v,w)=p(v XOR v_D,w),
where chi_j(v_D)=d_j.
For ANY known inserted proper Q in the middle:
  E_{p_D}[D(w) Q S_D D(v)]_ij
   = C_ij d_j (Q S)_ij d_j
   = C_ij (Q S)_ij
   = E_p[D(w) Q S D(v)]_ij.
The p_D are physical, strictly positive (label permutations), normalized and remain in the six-only family. **Additional middle gate controls cannot remove this sign gauge.** This is stronger than the particular original PRF ROT024 two post-Clifford 18-entry alias, but remains a standard gauge-identification mechanism, not a broad novelty claim.

As consequence: the actual TV(p_UNIT,p_BREAK) is NOT automatically data-identifiable even with infinitely many exact known middle controls. What IS identifiable, in this restricted ideal class, is the quotient-source orbit and e.g.
  ζ_orbit=min_{v_D∈F2²} TV(p_BREAK, p_UNIT shifted by v_D).
This quotient lower value need NOT equal the true instrument/source TV; do not silently replace source equality with orbit equality.

To resolve fourfold ambiguity one needs a TRULY independent signed PAULI-FRAME reference, e.g. trustworthy signed source correlation anchors in two independent input columns, or external gate reference fixing column signs. Reading those signs merely from BREAK p_BREAK and ASSUMING equal source across BREAK and UNIT would be circular — equality is the hypothesis under test. Gauge fixing by convention is NOT physical information.

## 3. SOURCE-COMPLETE original physical PRF example, exact 16 probabilities

Take firstness PRF14 ROT024:
 S=P R0=(1/7)[[2,6,3],[-3,-2,6],[6,-3,2]],
 C=(7/2)*C0 with
 C0=[[0,.09,.11],[.07,0,.10],[.08,.12,0]],
 p_C(v,w)=[1+sum_{i≠j}C_ij chi_j(v)chi_i(w)]/16.

Independent 100% Fraction source reimplementation (no original PRF14 functions imported):
  sum p=1; min p=11/3200>0; all 16 histories explicit.
Both source and gate proper throughout.

For the four input sign patterns v_D=0,1,2,3, leave BREAK p_BREAK=p_C fixed while changing UNIT p_UNIT by v shift AND compensate unknown gate S->S D. ALL five exact full 3x3 channels under Q=I,P,P²,Rx(1/1000),Rz(1/37) are IDENTICAL between these worlds. Source TV against the same BREAK law takes:
  v_D=0: ζ=0;
  v_D=1: ζ=231/400=.5775;
  v_D=2: ζ=21/40=.5250;
  v_D=3: ζ=203/400=.5075.

Thus even extremely different physically valid UNIT-vs-BREAK conditional source distributions can be observationally identical under EVERY permitted inter-stage Q with the compensated unknown physical S. Consequently no finite-sample hypothesis test based only on these inter-stage UNIT tomography channels + SAME BREAK Bell source can ever uniformly establish the exact equality of the two source laws, unless a signed frame anchor or source/gate coupling assumption eliminates that gauge. This does not say the same process comb allows arbitrarily shifted p: worlds belong to separately conditioned source-instrument models.

## 4. Yet one intra-stage P DOES break the old CONTINUOUS alias

Original PRF14 W0/W1 from ROT024:
 S_c=P Q_x(t=1/1000) R0;
 C_c,ij=C_ij S_ij/S_c,ij (six offdiagonal), C_c,ii=0;
 p_c positive and ζ=41979/50199950≈.000836236.
Setting I channels are EXACTLY equal, by source construction; hence ANY final processing after setting I is useless.

But for TRUE inserted middle cyclic P, the output is C_ij*(P S)_ij, and the two worlds yield DIFFERENT complete full channels. Independent exact Fraction yields precisely SIX nonzero offdiag discrepancies and largest:
  ΔM_P[0,1] = -675/998999 ≈ -.0006756763520283805.
Other entries (rows x columns) exact:
 [[0, -675/998999, -1430/3003997],
  [20993/50000050, 0, 1997/10000010],
  [-6018/74949925, 11994/25099975, 0]].
The X-output/Y-input Pauli mean is thus an explicit source-conditional witness with different expected value. This is NOT an actual hardware readout or realistic finite-shot advantage; proof is algebraic and assumes p_UNIT unchanged between the two middle controls.

A source-dependent policy that changes p_UNIT when Q changes can trivially defeat this inference. The value of a second setting depends on INTERVENTIONAL COUPLING SOURCE ASSUMPTIONS, not the nominal number of extra Clifford gates.

## 5. Independent execution and reproducibility

Two independent local self-contained, source-authored Python stdlib programs were ACTUALLY EXECUTED TWICE each with python -I, not importing original PRF, M16 ROT008 or each other:
1. Main exact Fraction reproducer /mnt/data/m16_rot009/m16_rot009_internal_pauli_control_gauge_exact.py SHA256 6797acac108d440117913bc55269e537d43f45c747822a812647524f9feea34f. Machine exact JSON SHA256 75f4195c5783a55a13478bebc2521cfa675d47519f5c14673c6f60c07a3250d1. Two stdout byte-identical SHA256 d7c75147805890f6e9bb6ee14522e19d709da9d3e88ac179805c70b6f42d2b73.
2. Independently constructed 100-case rational random generator; own 16-history source and tomography code, not importing script 1: /mnt/data/m16_rot009/m16_rot009_independent_random_rational_orbit_test.py SHA256 82e504253a1c2f0b4d4bd13c5b761ca86ec5e89d726934c6497185ec238dd686. Its JSON SHA256 2446e00805854990ea542f239d659ee3d39ea937bc9d58cb56027a6657f51b3b. Two stdout byte-identical SHA256 15c4754d0d3ef6a50e3b586f50ec1353dc0c088ebad1da6428b79065ff4df7a2.
Independent stress: 100/100 exact rational six-source proper SO3 cases projective reconstruction PASS; 100/100 source-positive single-control continuous aliases PASS; 100/100 internal P removed these continuous aliases; 100/100 sign-gauge alternatives remained identical under both I and P. Randomized exact rational testing is corroboration, not substitute for general proof.
Local reproducibility ZIP with 9 files, full ZIP CRC+BYTE audit PASS, SHA256 826179513fa5387afa525223c08528fdcaa88a683f32f8ab918213ee71061554:
 /mnt/data/m16_rot009/m16_rot009_bundle.zip

## 6. External science subtraction and strategic STOP

Mature prior art:
- Gate-set gauge impossibility: 2017 Nature Communications "Demonstration of qubit operations below a rigorous fault tolerance threshold with gate set tomography" explicitly discusses experimentally indistinguishable gate sets. https://www.nature.com/articles/ncomms14485 .
- 2025 npj Quantum Information "Microscopic parametrizations for gate set tomography under coloured noise", https://www.nature.com/articles/s41534-025-00976-4 explicitly treats gauge freedom under unknown frame.
- Xu, Liu, Chen Nov 2026 arxiv:2611.05561 original mathematical source PREPRINT, gauge-free cycle graph and Paulis; direct original publisher abstract read, PRF14 ROT025 full original theorem prior audit read. https://arxiv.org/abs/2611.05561
- Li et al Non-Markovian Quantum Gate Set Tomography, Quantum Sci Technol 9 035027 (2024), https://doi.org/10.1088/2058-9565/ad3d80; firstness of broader source/gate instrument ambiguity is mature.

**Not to claim**: no generic new gauge theorem, no new device, no proof that a single experimental source obeys this family of conditioned p_UNIT/BREAK, no quantum comb identification, no validated source measurement errors/shot counts, no external novelty.

**What the controlled experiment designer CAN take from this conditional result**:
- In this six-only family, one nontrivial P inserted BETWEEN errors is enough to collapse CONTINUOUS source/gate ambiguity to fourfold Pauli frame if exact 3x3 channels available and p_UNIT stable across I,P.
- All such controls can NEVER alone establish literal source equality with destructive BREAK due to the exact fourfold gauge.
- A physical experiment must first establish (i) source stability under Q, (ii) a trusted signed frame reference not obtained circularly from assumed p_BREAK, and (iii) hardware-realizable middle controls and error budget. Without those no scientific case for further synthetic n optimization.
- If such physical source+frame control cannot be justified, this entire M16/PRF intervention-style line is scientifically eligible for SOURCE_CONDITIONAL_MATH_CLOSE. This is advisory, not override of PRF14 owner or Moderator, and does not apply to future genuinely different physical carrier.

FINAL: M16_ROT009_TWO_MIDDLE_CONTROLS_EXACT_PROJECTIVE_SO3_RECOVERY / FOURFOLD_PAULI_KLEIN_GAUGE_SOURCE_TV_NO_GO / ORIGINAL_PRF24_CONTINUOUS_ALIAS_BROKEN_BY_TRUE_INTERNAL_P / 100_OF_100_INDEPENDENT_RATIONAL_RANDOM_STRESS / TWO_INDEPENDENT_COLD_REPLAYS / NO_EXTERNAL_NOVELTY / NO_HARDWARE / NO_CANON / NO_EXEC_SIGN / BW_NOT_WRITTEN.
