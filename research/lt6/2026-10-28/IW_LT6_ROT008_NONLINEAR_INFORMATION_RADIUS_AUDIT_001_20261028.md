---
artifact_id: IW_LT6_ROT008_NONLINEAR_INFORMATION_RADIUS_AUDIT_001_20261028
created_at: 2026-10-28
origin_cell: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_04 / LT6
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: MATURE_OPTIMAL_RECOVERY_PLUS_SYMMETRIC_TAYLOR / EXACT_TOY_AND_250_RANDOM_CHECKS_PASS / NONLINEAR_SOURCE_DATA_STOP
claim_ceiling: NO_MATHEMATICAL_NOVELTY / NO_PHYSICAL_PBH_BBN / NO_SOURCE_NATIVE_JULIA10D / NO_EXEC / NO_CANON / INDEPENDENT_REFEREE_PENDING
---

# LT6 ROT008 — Conditional nonlinear radius of information and legality of numerical two-point witnesses

## Prior work / original scientific owner

**FIRST OWNER:** [Mech-S7 ROT032](https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-28/mech_s7_rot032_sharp_sobolev_information_radius_nonlinear_binary_witness_001.md) computed the **sharp linear** radius of an adjoint target on the 11-function global C3 finite source family with conserved moments and an H2 second-derivative budget R=11.435960696834389. Mech FIRST executed full-amplitude opposite-source conditional 7D kinetic solves at χ_EM=.5: B_exec numerical targets (0.401532078747270, 0.400386812623339), B_sym (0.400301539601712, 0.399868355214440). Linear radii respectively 5.72547461749e−4 and 2.16589567135e−4. The source’s independently integrated **relative** moment residuals were at most 1.171e−12 and 8.701e−14 (exec, sym); ODE tolerance-variation differences in the reported contrasts 5.680e−13 and 1.074e−13 are **not rigorous solver error bounds**.

Earlier source owners: Mech ROT031 global basis, MT14 ROT009 Borsuk–Ulam exact six-target alias (a different statement), LT6 ROT004 with Badacz REVIEW007 event-error clarification, LT6 ROT007 target-specific exact nonlinear fibers. Do not silently upgrade any conditional original model to physical Wu–Xu PBH spectra.

## T008.1 — nonlinear two-point risk from an H2 linear radius (classical mathematics)

Let V=ker C, H>0 restricted to V, ||v||_H=(v^THv)^{1/2}. Let ℓ=DT(0)|_V and r=||ℓ||_(H*,V). Choose u∈V with ||u||_H=1 and ℓ(u)=r>0; for a budget R>0 suppose **both** ±Ru are admissible and induce at least one *common feasible observation*. Suppose T is C3 on a neighborhood of the segment [−Ru,Ru], with |D3T(x)[h,h,h]|≤M3 ||h||_H^3 there for all h∈V. Then

    |T(Ru)−T(−Ru)−2Rr| ≤ (M3/3)R³,
    minimax absolute target error ≥ max(0, Rr − M3 R³/6).

**Proof:** second-order Taylor at zero for both opposite endpoints; identical even quadratic terms cancel, and two signed third-order remainders each have absolute value ≤M3 R³/6. Any one prediction for a common observation has maximum absolute error at least half the endpoint target gap by the triangle inequality. The premise about common feasible observation is essential, not just convenient.

If only ||D²T(x)[h,h]||≤M2||h||_H², the weaker risk floor is max(0,Rr−M2 R²/2). For computed gradient ℓhat and certified **source-valid** dual-norm error εℓ, the maximizing ℓhat-direction yields the floor max(0,R(||ℓhat||*−εℓ)−M3 R³/6). These are familiar optimal recovery and symmetric Taylor facts, **not mathematical novelty**.

## T008.2 — extremely close source moments are not exactly identical data

For available information vectors N+ and N−, and a deterministic observation model y=N±+ξ with coordinate-wise |ξ_j|≤δ_j, both hypotheses have a *common feasible y* iff

    |N+_j−N−_j| ≤ 2δ_j    for every j.

Proof: the two closed intervals around each coordinate overlap precisely under that condition. Their midpoint gives a common y. If source-information error is correlated or otherwise constrained, use actual uncertainty-set intersection instead of intervals.

**Critical falsifier:** if the observer measures the exact noiseless N (δ=0), ANY nonzero moment difference, even 1e−12, distinguishes this specific source pair. Mech’s independent quadrature residual is numerical near-equality, **not** a proof of equality for an ideal-information experiment. A mathematical two-point minimax floor for exact moments must either construct sources with exactly equal true moments or justify observational tolerances large enough for overlap. Moment discrepancies expressed as relative quadrature residuals are not automatically physical measurement δ.

If certified solver errors of the two target outputs satisfy |Ttrue±−Tnum±|≤ε±, then conditional on common feasible data:

    minimax error ≥ max(0, (|Tnum+−Tnum−|−ε+−ε−)/2).

Convergence under smaller solver rtol is not itself an ε± certificate; event-aligned targets require source-valid residual/tube/transversality/first-crossing controls (Badacz REVIEW007).

## Strict exact example and negative controls

Let C=(1,0,0), H=diag(1,4,9), R=1, ℓ(c)=2c_2, maximizing u=(0,1/2,0). For

    T(c)=2c_2+5c_2²−2c_2³

we have T(u)=2, T(−u)=1/2, pair gap 3/2, half-gap 3/4. The H-operator norm M3=3/2, so the lower bound 1−M3/6=3/4 is **exactly sharp**. The large even quadratic term cancels. Replacing −2c_2³ by −8c_2³ gives T(u)=T(−u) despite ℓ(u)=1: a linear radius by itself cannot guarantee finite-amplitude target separation.

The toy exact moment N±=±10^(−12) is distinguishable at noiseless resolution, but observationally compatible with the *same* y=0 when δ≥10^(−12). Standard-library Fraction arithmetic and 250 independently seeded cubic-polynomial checks PASS. No original Julia or source-native physical target was run.

## Source-specific diagnostic, **not** an H3 certificate

| Map | Mech nonlinear target gap | 2×linear radius | odd residual (nonlinear minus linear) | relative odd residual |
|---|---:|---:|---:|---:|
| B_exec | 1.145266123931e−3 | 1.145094923498e−3 | +1.71200433e−7 | 1.4951e−4 |
| B_sym | 4.33184387272e−4 | 4.33179134270e−4 | +5.25300202e−9 | 1.2126e−5 |

These two numerical differences do NOT bound M3 uniformly across the source ball. Under the above H-metric, a positive theorem-based floor would require M3<6r/R²=6a/R³: <2.29691424804e−6 (exec), <8.68902049115e−7 (sym). No such source-valid bound exists in the reviewed outputs.

**Mature external hosts:** radius of information in Novak–Woźniakowski (information-based complexity); centered difference Taylor remainder (e.g. [finite-difference theory](https://diffprog.github.io/finite_diff.html)); two-point worst-case lower bound by triangle inequality; optimal recovery of ellipsoidal source classes (e.g. [Juditsky–Nemirovski 2018](https://doi.org/10.4171/MSL/1-2-2)). No novelty claim.

**Scientific stop:** no physical hadronic spectra below 10^9 g, no author-native Julia10D, no certified true source moments or observational δ, no certified ODE output ε±, no uniform M3; therefore **no physical PBH/BBN/Yp/DH conclusions**. Scientific next step is to define the actual observation interface and verify the pair through it, not to claim a physical bound from a near-exact numerical match.

**Archive:** native [Żywa Teoria REV027](https://docs.google.com/document/d/1hiEkt3cXYJZyMv51pPIfFV5MEvMZl2ah2OCAdSUSyDQ/edit), [fully reconstructed private GitHub REV027](https://github.com/wmakiela-tech/Nash-Priv/blob/main/living-theory/2026-10-28/REV027/README.md). Local complete Polish proof, self-contained Python, JSON and SHA256 ZIP in Moderator conversation. No BW ingestion, independent referee or Moderator EXEC.
