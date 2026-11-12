---
artifact_id: IW_PRF13_ROT010_CLIFFORD_ECHO_OPTIMAL_TESTER_TV_PUBLIC_RETURN_001_20261112
created_at: 2026-11-12
origin_cell: PRF13
source_type: SOURCE_TYPED_EXACT_THEOREM
exposure: PUBLIC
sync_state: GITHUB_SOURCE_READBACK_PENDING_BW_INGEST_PENDING
status: AUTHOR_EXACT_REPRODUCED / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_PHYSICAL_DEVICE / NO_NASH_CROSS_FIELD_BRIDGE / NO_ORIGINAL_3Q_LOCC / NO_CANON / NO_EXEC_SIGN
---

# PRF13 ROT010 — Clifford echo and exact two-time Pauli-comb discrimination

**Result.** Within the two-step classical-label qubit Pauli-comb example independently constructed in PRF13 LT8-THEORY-010-PRF (ROT009), one single deterministic intermediate Clifford gate separates the two sources with outcome TV=1/2, even without recording an intermediate measurement. Allowing arbitrary time-ordered tester-local ancillary resources, the optimal single-use process discrimination TV is exactly 3/4; equal-prior success is 7/8. These are source-specific examples of mature process-tensor and quantum-control theory, not original theoretical novelty.

## Frozen source and three matching channels

Set G=F_2² and U_(a,b)=X^a Z^b, modulo irrelevant phase. Under C, draw v uniformly from G and set w=F(v), F(a,b)=(b,a xor b). Under I, draw v,w independently uniformly from G. Because F and id+F are both bijective, v,w,v+w are uniform under both. Thus their **unconditional** first-stage, second-stage, and unperturbed endpoint CPTP channels are IDENTICAL, all D(rho)=I*Tr(rho)/2. The environment label pair is chosen exogenously and is unaffected by interventions.

Each channel is a lawful random-unitary CPTP map. Both two-time process combs are convex mixtures W_p=sum p(v,w) J(U_v) tensor J(U_w), with J unnormalized Choi, so W>=0. The causal identities are Tr_(second output) W=J(D) tensor I and Tr_(first output) J(D)=I, as checked in parent ROT009.

## Theorem A: one deterministic legal control suffices

Let H=(X+Z)/sqrt(2), S=diag(1,i), V=SH. Conjugation gives V X V†=Z and V Z V†=Y, implying V U_v V†=phase(v)*U_F(v). Hence for EVERY C branch U_F(v) V U_v=phase'(v)*V, and the correlated two-stage channel WITH intermediate Ad_V is exactly Ad_V. For independent I, the second uniform Pauli twirl depolarizes everything and the resulting intervened channel is D.

Prepare |0><0|; V|0> is |Y+>. At the final Pauli-Y measurement, C has probabilities (+1,-1)=(1,0) and I has (1/2,1/2). Exactly TV=1/2; equal-prior success=3/4. Without insertion, both endpoint channels were the same depolarizing D. A deterministic intermediate CPTP gate, NOT only an intermediate selective CP instrument, is thus a valid exact falsifier for endpoint-only reduction.

## Theorem B: global quantum tester optimum is exactly 3/4

For any admissible adaptive tester, once the exogenous classical label pair L=(v,w) is fixed, the law of its declared outcome o is a common stochastic kernel K(o|L). By classical data processing for total variation, TV(output_C,output_I)<=TV(p_C,p_I). Since C puts 1/4 on four graph pairs and zero elsewhere, while I puts 1/16 on all sixteen, the exact upper bound is (1/2)*(4*3/16+12*1/16)=3/4.

Achieve equality by preparing a Bell pair between the system and a tester-local ancilla at stage 1, measuring the orthogonal states (U_v tensor I)|Phi+> to read v exactly, repreparing a fresh Bell pair at the intermediate slot, and measuring the second Bell outcome to read w exactly. The tester thereby produces exactly the classical joint p(v,w), saturating the upper bound. This uses legal time-ordered instrument-and-ancilla resources, not a physically accessible environment-register measurement. With equal prior source probabilities P_success^*=(1+TV)/2=7/8.

**Scope guard:** TV=3/4 is optimal for THIS exogenous classical Pauli-label source family and liberal tester resource class. No universal comb discrimination theorem, original LOCC gap, or physical NCDG field bridge is inferred. The nonselective one-gate no-ancilla construction is proven to achieve TV=1/2, not claimed globally optimal among all ancilla-free tests.

## Prior-art subtraction

Chiribella, D'Ariano, Perinotti, *Theoretical Framework for Quantum Networks*, PRA 80 022339 (2009), DOI 10.1103/PhysRevA.80.022339 (quantum combs); Pollock et al., *Non-Markovian quantum processes: Complete framework and efficient characterization*, PRA 97 012127 (2018), DOI 10.1103/PhysRevA.97.012127; Pollock et al., *Operational Markov Condition for Quantum Processes*, PRL 120 040405 (2018), DOI 10.1103/PhysRevLett.120.040405. Echo/active noise recovery is mature: *Experimental on-demand recovery of entanglement by local operations within non-Markovian dynamics*, Sci Rep 5 8575 (2015), DOI 10.1038/srep08575. No novelty or hardware claim.

## Reproduction and negative knowledge

Author exact SymPy: F bijective and id+F bijective, four Clifford identities checked up to global phase, both no-gate outputs I/2, Y-readout TV=1/2, Bell orbit orthonormal and complete, classical upper bound attained TV=3/4, P_success=7/8: PASS. Full original standalone reproducibility script, stdout, manifest and expanded proof are archived in the separate downloadable ROT010 ZIP. Independent external referee PENDING; BW and Living Theory not edited.

Source parent: https://github.com/wmakiela-tech/Nash-iw-research/blob/4d8041e24962978d0aeba05029dae8a2f96abaf4/research/prf13/2026-11-12/IW_PRF13_LT8_THEORY_010_PRF_TWO_TIME_CAUSAL_COMB_INTERVENTION_FALSIFIER_001_20261112.md

RETURN: ROT010 / EXACT_CLIFFORD_ECHO_TV_1_2 / OPTIMAL_TESTER_TV_3_4 / SOURCE_TYPED / AUTHOR_EXACT_REPRODUCED / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
