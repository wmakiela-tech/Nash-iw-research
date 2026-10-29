---
artifact_id: IW_PRF12_R17_SOURCE_ACTIVE_SWAP_STORAGE_AND_AXIS_ROBUSTNESS_001_20261029
created_at: 2026-10-29
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_11 / PRF12
problem_id: PRF12_R16_RESET_AGNOSTIC_READOUT_REALISTIC_RESOURCE_PERTURBATION
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_IDLE_STORAGE_FORMULA / FINITE_ACTIVE_SWAP_DUHAMEL_CERTIFICATE / CAUCHY_LOG_TAIL / CONDITIONAL_VS_AVERAGED_RESET_SPLIT / INDEPENDENT_REPRO_PASS / REFEREE_PENDING
claim_ceiling: NO_FULL_SINGLE_RUN_LOCC_GAP / NO_NOVELTY / NO_CANON / NO_EXEC / NO_HARDWARE_VALIDATION / NO_UNRESTRICTED_SOURCE_RESET_UNIFORM_PULSE_CERTIFICATE
---

# PRF12 R17 — Odporność losowanego odczytu X/Y na starzenie pamięci, skończone SWAP, ciężkie ogony i błąd kalibracji

**Owner:** PRF12. **Data:** 29.10.2026. **Scientific status:** source-typed exact propositions and conservative channel-distance bounds. Independently reconstructed matrices and elementary 2-qubit active-pulse simulations PASS; independent referee PENDING. **Main anti-overclaim:** a Cauchy-average one-run pulse perturbation does **not** certify repeated-run iid performance if the same static ξ persists through many runs.

## 0. Dependency and mature external prior art

**Direct IW first owners:** PRF11 R35 — Cauchy static vs independent Lévy phase source, ideal SWAP experiment; PRF12 R01 fixed-clock feasibility; PRF12 R02 source-active finite-duration SWAP Duhamel and heavy-Cauchy-tail penalty; PRF12 R04 n=3 exact endpoint states; PRF12 R09 corrected coarse-graining/LOCC-closure overclaim; PRF12 R15 source reset lifetime; PRF12 R16 randomized fair X/Y all-equal event and exactly 80-run ideal Bayes threshold.

Internal source links:
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R35_NONUNIFORM_SWAP_TIME_GRID_RECOVERS_IDEAL_MEMORY_WITH_CRITICAL_STORAGE_RATE_001_20261025.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-26/IW_PRF12_R02_FINITE_DURATION_SWAP_CAUCHY_ACTIVE_PULSES_AND_RESOURCE_GATE_001_20261026.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-28/IW_PRF12_R15_OPTIMAL_LOCC_HERALD_UNDER_PARTIAL_SOURCE_RESET_001_20261028.md
- https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf12/2026-10-29/IW_PRF12_R16_RESET_AGNOSTIC_SOURCE_TEST_AND_SEPARATE_LIFETIME_CALIBRATION_001_20261029.md

**External mature hosts (no priority claims):** the Cauchy density and nonexistence of E|ξ|, NIST Engineering Statistics Handbook, https://itl.nist.gov/div898/handbook/eda/section3/eda3663.htm ; Cauchy characteristic functions and moments, https://pmc.ncbi.nlm.nih.gov/articles/PMC9955388/ ; unitary-channel diamond norm vs operator difference and Duhamel estimates, quantum Hamiltonian simulation literature https://par.nsf.gov/servlets/purl/10195522 ; time-varying quantum noise and channel-distance cautions, https://www.nature.com/articles/s41534-021-00448-5 . This R17 combines these established bounds with the **specific observable and source** of R16, not a new generic open-system theorem.

## 1. Exact experiment and reference, with physical time gate

Three sequential fresh probe qubits undergo EQUAL free exposure durations Δ to one sensor S, with TWO swaps S↔M1 and S↔M2. Ideal free exposure time T_free=3Δ. In the physical experiment each SWAP is implemented by Hamiltonian H0=(π/2τ)SWAP for duration τ, so T_phys=T_free+2τ, subject to the fixed clock resource T_phys<=T_budget and control Ω=π/(2τ). One must **not** write T_phys=T_free while secretly inserting finite-duration pulses. The numeric example fixes γ T_free=1, so q=γΔ=1/3, and requires T_budget>=1.002 T_free for τ/T_free=.001. Under fixed total T_budget, replace Δ with (T_budget−2τ)/3 and recompute q accordingly.

Hypothesis A: one ξ~Cauchy(0,γ) frozen within ONE run, and possibly frozen between runs by arbitrary reset scheduling. During a physical pulse it contributes H_A,noise=ξ Z_S/2. Hypothesis B: independent Cauchy–Lévy phase increments including during pulses, whose averaged generator is D_γ(ρ)=(γ/2)(Z_S ρ Z_S−ρ). Both have same single-period characteristic function exp(−γΔ). No conjectural averaging of B into a single random phase DURING a noncommuting SWAP is allowed.

**Ideal reference:** same three FREE windows Δ, perfectly executed instantaneous-permutation-equivalent SWAP gates, NO source noise during the two pulses, and memory local dephasing only during free PARKING times. Local memory offdiagonal decay rate κ. For stored probe ages a1=2Δ, a2=Δ, a3=0, set

 d1=exp(−2κΔ), d2=exp(−κΔ), d3=1,
 S=d1*d2+d1*d3+d2*d3,
 x=exp(−γΔ)=exp(−q).

The reference ignores κ during active SWAP pulses; §4 accounts for this separately by a conservative perturbation. No uncontrolled amplitude damping, depolarizing noise, phase reference drift, cross-talk or readout assignment errors are assumed unless quantified explicitly.

## 2. R17.1 — exact reset-history independence survives arbitrary different storage ages

For equatorial qubit state ρ_j(φ_j,d_j)=(I+d_j cosφ_j X+d_j sinφ_j Y)/2, all-3-same-sign effect at a local common axis X_θ is

 E_θ=⊗³(I+X_θ)/2 +⊗³(I−X_θ)/2
     =1/4[I+Σ_{i<j} X_{θ,i}X_{θ,j}].

Randomly choose global X setting θ=0 or orthogonal Y setting θ=π/2, each with fresh fair independent setting coin and local X/Y measurement on each spatially separated qubit; record C=1 iff the THREE signs agree. Its source-independent observable is

 E=(E_0+E_{π/2})/2
   =I/4 +(1/8)Σ_{i<j}(X_iX_j+Y_iY_j).

For a product state with local Bloch lengths d_j and phases φ_j, an EXACT 8×8 trace gives

 p(C=1|φ1,φ2,φ3)=1/4+(1/8)Σ_{i<j} d_i*d_j*cos(φ_i−φ_j).       (R17.1)

If all three probes see the SAME frozen ξ for an EQUAL Δ, then φ1=φ2=φ3=ξΔ conditional on ξ, irrespective of the reset policy BETWEEN runs. Therefore exactly

 p_A^ref(ξ)=1/4+S/8 (independent of ξ).                    (R17.2)

Under B, the individual local dephasing factor is x, so

 p_B^ref=1/4+S*x²/8,
 G_ref=p_A−p_B=S(1−x²)/8>0.                             (R17.3)

The R16 iid Bernoulli argument thus survives local storage dephasing PROVIDED reference weights d_j are fixed and known, all three conditional phases are exactly identical per run, independent fresh preparations and measurement-setting coins are used, and B increments are independent across runs. In particular even arbitrarily correlated A reset history cannot alter the conditional Bernoulli parameter p_A because (R17.2) holds BEFORE averaging. This is a positive operational result beyond R16's κ=0 fixture.

If FREE exposure durations differ, the A conditional probability generally depends on ξ through cos[ξ(Δ_i−Δ_j)], so the reset-history-invariance breaks. After *single-run Cauchy averaging* one obtains p_A^marg=1/4+(1/8)Σ d_i d_j exp(−γ|Δ_i−Δ_j|), whereas B gives 1/4+(1/8)Σ d_i d_j exp(−γ(Δ_i+Δ_j)). Marginal positivity is NOT Bernoulli independence when ξ persists between runs. This is a falsifier for any blanket 'unequal grids are reset-agnostic' claim.

## 3. R17.2 — exact orthogonality-defect response, including worst persistent φ

Assume all THREE labs share the same basis settings, the first at θ0=0 and the second nominal Y at θ1=π/2+ε, with ONE constant orthogonality defect ε (radians). This is **not** an arbitrary independent error on each lab's axes. Let φ be the common within-run phase under A. Direct evaluation of both possible settings gives

 p_A^ref(φ,ε)=1/4+(S/8)[1−sinε*sin(2φ−ε)],            (R17.4)
 p_B^ref(ε)=1/4+(S*x²/8)[1+sin²ε].                  (R17.5)

Thus p_A can now depend on a ξ persisting across runs, with certified WORST-CASE independent-φ envelope

 |p_A^ref(φ,ε)−p_A^ref(0)| ≤ (S/8)|sinε|,
 0≤p_B^ref(ε)−p_B^ref(0)=(S*x²/8)sin²ε.

Hence every phase yields gap at least

 G_angle ≥ G_ref − (S/8)(|sinε|+x² sin²ε).         (R17.6)

The worst-case phase envelope is the correct resource for subsequent conditionally valid concentration bounds; replacing it by a Cauchy-unconditional average and then claiming iid trials would be invalid.

## 4. R17.3 — finite-source-active pulses and non-existent Cauchy absolute first moment

For two active source-free comparator gates of duration τ each (combined L=2τ), ordinary Duhamel/telescoping bounds, **conditional on ξ**, give for the states before the same final measurement:

 T(ρ_A^active(ξ),ρ_A^ref(ξ)) ≤ min(1,|ξ|L/2)=min(1,|ξ|τ).

For B, CP contractivity and ||D_γ||_diamond≤γ give

 T(ρ_B^active,ρ_B^ref) ≤ γ L/2=γτ.

Here T=||ρ−σ||_1/2. Source noncommutation with SWAP is allowed, and the comparison fixes exactly the same free intervals and ideal unitary gates.

Since ξ~Cauchy(0,γ), E|ξ| DOES NOT EXIST. A legitimate source-averaged first-error bound is

 H(z)=E[min(1,z |Cauchy(0,1)|)]
     =(z/π) log(1+z^-2)+(2/π) atan(z), z=γτ.        (R17.7)

Proof: integrate the centered Cauchy density 2/[π(1+u²)] over u>=0, splitting at u=1/z; below that cutoff the integrand is zu, above it is 1. As z→0,

 H(z)=(2z/π)[log(1/z)+1]+O(z³),

so it is **not O(z)** with a uniform constant as z→0. Numerically H(.001)=.005034233472. This exactly matches R02's source-active Duhamel quantity ε(2γτ)/2; R17 is a readout-specific transfer, not discovery of the generic tail bound.

**Memory during active pulses.** Model at most THREE dephasing registers, each with rate κ and generator (κ/2)(ZρZ−ρ) when active during the two gates. Relative to the comparator that turns this memory noise off during the pulses, the worst-case trace-distance penalty PER hypothesis is at most (3 registers)*(κ/2)*(2τ)=3κτ. This count is conservative: real SWAP occupancy may involve fewer live registers. If more registers/noise channels are active, this bound must be revised; amplitude damping is outside this certificate.

Therefore for ONE run's unconditional source-averaged measurement probabilities and common-axis defect ε, the combined A−B contrast is **rigorously bounded** by

 G_active^marg ≥ G_ref−H(γτ)−γτ−6κτ
   −(S/8)(|sinε|+x² sin²ε).                         (R17.8)

A strictly positive right-hand side certifies an A–B difference in the ONE-RUN averaged statistic. It does NOT certify independent Bernoulli samples or a universal finite-N source classification protocol for arbitrary persistent ξ. It does NOT imply an endpoint Helstrom/LOCC-closure inequality.

## 5. R17.4 — phase-uniform high-probability guarantee for a SINGLE shared ξ over N runs

For the persistent-common-ξ contract, the unconditional mean bound (R17.8) cannot be converted into iid classification guarantees. Instead, for any specified tail failure δ in (0,1), the centered Cauchy distribution gives EXACTLY

 Pr[|ξ| > Λ_δ]=δ,  Λ_δ=γ cot(πδ/2).              (R17.9)

On the event |ξ|≤Λ_δ, the active-source A conditional deviation is bounded by min(1,Λ_δτ). Consequently **all** trials conditioned on this same ξ obey a positive probability separation whenever

 G_conf(δ)=G_ref−(S/8)(|sinε|+x² sin²ε)
             −min(1,Λ_δτ)−γτ−6κτ>0.              (R17.10)

A threshold midway between the worst allowed A success probability and B success probability then has conditional false-decision risk ≤exp(−N G_conf(δ)^2/2) for EACH source, using Hoeffding's bound for independent fresh runs, conditional on the hidden static phase. The unconditional A error has at most an additional δ for the rare Cauchy-tail event. **This is a conservative sufficient sample bound, not a minimal N.** If ξ changes across up to m independent OR even arbitrary correlated draws with Cauchy marginals, use the UNION bound δ/m in Λ; the guarantee becomes markedly weaker for large m. Without a restriction on reset count or hidden-frequency range, no uniform small pulse-error guarantee follows from (R17.9).

## 6. Worked normalized example and three distinct confidence levels

Set γ T_free=1, q=1/3, κ T_free=.3, τ/T_free=.001 (so total physical time T_phys=1.002 T_free), common basis orthogonality defect ε=.02. Exact idle d=(exp(−.2),exp(−.1),1) and S=2.464386391796.

| Metric | Value |
|---|---:|
| p_A reference, ε=0 | .558048298974 |
| p_B reference, ε=0 | .408157270182 |
| reference contrast G_ref | .149891028792 |
| maximum contrast penalty from angle defect | .006223809730 |
| A source-averaged finite pulse penalty H(.001) | .005034233472 |
| B source-active pulse penalty γτ | .001000000000 |
| memory active-pulse contribution to contrast, ≤6κτ | .001800000000 |
| **R17.8 guaranteed ONE-RUN marginal contrast** | **.135832985590** |
| **R17.10 guaranteed contrast, δ=.05, one ξ shared** | **.128161014326** |
| **R17.10 guaranteed contrast, δ=.01, one ξ shared** | **.077210477899** |

The average penalty .00503 and the 99%-confidence worst-case pulse penalty .06366 describe DIFFERENT claims and must never be conflated.

For the **reference source with κ aging but no active-pulse/angle imperfections**, the exact iid-binomial Bayes threshold (equal priors) gives minimal N=119 runs for A/B average error <5%, and N=121 for BOTH conditional errors <5%. This is a concrete corrected cost against R16's κ=0 N=80, not a performance claim for active pulses.

For the **source-active physical case with one frozen ξ shared over all N runs**, δ=.01 confidence and G_conf≈.077210 yield the conservative Hoeffding count N≥1006 for each conditional error ≤5% ON THE 99% HIDDEN-FREQUENCY GOOD EVENT. Outside it no bound of that strength is asserted; total A error is bounded by ≤δ+.05=.06. This number is deliberately much larger than exact ideal N and is not an experimentally optimized protocol.

## 7. Independent executable tests and limitations

Complete NumPy/SciPy source (local and mirrored GitHub):
`IW_PRF12_R17_SOURCE_ACTIVE_SWAP_STORAGE_AND_AXIS_ROBUSTNESS_REPRO_001_20261029.py`.

- Exact 8×8 X/Y event matrix constructed from tensor-product local projectors.
- For κ T_free in {0,.1,.3,1.2}, q in {.05,1/3,.7,1.4}, and 30 randomized conditional phases each, p_A(ξ) and p_B compared to (R17.2)-(R17.3) at <1e−13.
- Five basis orthogonality defects and six phase values per parameter pair independently compared to (R17.4)-(R17.5) at <1e−13.
- H(z) independently checked by numerical quadrature over the arctan-transformed centered-Cauchy density, not merely by re-evaluating the same closed expression.
- **Active-source two-qubit pulse check:** direct dense matrix exponentiation of H0τ=(π/2)SWAP and H_A,noise τ=(ξτ/2)Z_sensor at a range of |ξ|τ; separately exponentiated Markovian B Liouvillian on 2 qubits with noncommuting SWAP. Both satisfy the claimed Duhamel trace-distance upper bounds. A local pulse check is a sanity test of the inequality, NOT a full three-probe source-active device simulation.
- Exact finite-binomial enumeration validates minimum N=119,121 under κ reference.
- Cauchy 95%- and 99%-quantile conditional contrasts and 1006-run sufficient Hoeffding count checked.

**Falsifier gates:** independent audit of each factor 1/2 in channel distance; reference free-vs-physical timing; factor # registers=3 during active gates; no passing from a single-run Cauchy average to iid counts when ξ persists; correct ε angle convention and global shared-axis calibration; free stages equal Δ and κ strictly pure dephasing; no source-active noncommutation ignored; no claim of uniform Cauchy amplitude bound; no quantum-capability overclaim. Future R18 should investigate a pulse design with physically valid shared-phase cancellation and quantitative finite-κ source-driven simulations, not assume state-dependent uniformity.

**Return:** PRF12_R17 / SOURCE_TYPED_STORAGE_RESILIENCE_EXACT / ACTIVE_PULSE_CAUCHY_LOG_TAIL / AXIS_ORTHOGONALITY_EXACT_DEFECT / AVERAGE_VS_PERSISTENT_XI_CONFIDENCE_SEPARATED / QUANTIFIED_POSITIVE_CONTRAST / INDEPENDENT_MATRIX_PULSE_INTEGRAL_PASS / REFEREE_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / SINGLE_RUN_LOCC_CLOSURE_OPEN / GITHUB_PENDING_BW_INGEST.
