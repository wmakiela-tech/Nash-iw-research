# Mech-S7 — Front B: terminal kinetic-memory / frozen-impulse falsifier (rotation 005)

```yaml
CELL: IW_MECH_LINEAGE_001_SUCCESSOR_06 / Mech-S7
DATE: 2026-10-23
RETURN_ID: MECH-S7-FRONTB-TERMINAL-KINETIC-MEMORY-AND-FROZEN-IMPULSE-GATE-005
PROBLEM_ID: FRONTB_PBH_HADRON_BBN_SOURCE_VALIDATION
TYPE: EXACT_FROZEN_LINEAR_POPULATION_IDENTITIES / EXECUTED_SPECIES_QUADRATURE / NEGATIVE_MECHANISM_CONTROL
SOURCE: Wu-Xu pinned d395183674cace6c9906a8911bdeb7234ba4040d; NaturalUnits pinned 4a9f007ff1df416c9fef28c4d83d8fe8846099cf
EXPOSURE: PUBLIC
JULIA_10D_RERUN: NOT_EXECUTED
SOURCE_VALID_E2B: OPEN
MODERN_Yp_DH: NOT_EXECUTED
CANON: NO
EXEC_SIGN: NO
NOVELTY: NO_CLAIM
BW_INGEST: NOT_VERIFIED
```

## 1. Main question and distinct result

In Mech-S7 ROT003 the archived Wu–Xu diagnostic exhibited extreme cancellation between signed anti-proton and anti-neutron contributions to neutron forcing. ROT004 derived the exact source-native mass-cube relation and showed that the paper-vs-public subedge source law changes the *unweighted emitted particle counts* by approximately 5.6–6.1%. The missing mechanism question is whether total emitted count, number of hadrons *surviving at source cutoff*, and integrated neutron-conversion impulse are interchangeable.

**They are not.** Under an explicitly frozen-coefficient version of the original species loss equations, the relative paper-law increase in populations still present at the PBH source cutoff is +42.3–42.6% (antinucleons), +79.5% (pions), and +88.3% (charged kaons), even though emitted counts increase by only +5.6–6.1%. In contrast, the signed time-integrated hadronic neutron forcing changes by +1.14% (`B_exec`) or +3.70% (`B_sym`) in this frozen approximation: BOTH positive. The historical full 2×2 fixed-T executor Xn source-law effects had opposite signs (negative exec, positive sym). Thus a *constant T, constant X, fixed density, linear population response* is insufficient to explain the source-law sign reversal. Actual X(t), reaction competition, source cutoff, numerical background and weak terms must be propagated dynamically before a mechanism is claimed.

Important limits: every subedge-source calculation here extrapolates from below the public table edge M0=10^9g down to nominal cutoff M_cut≈12.3669g. THIS IS NOT independently source-valid E2b emission physics, a modern BBN calculation, or a corrected PBH bound. A model-internal analytic result is not a physical validation.

## 2. Exact frozen kinetic mathematics

The pinned source implements the species form n'_h=S_h-D_h n_h, with D_h including source-native decay and baryonic collision channels (depending on frozen background T, X and n_B). With a shared source edge at M0, mass-cube gamma Γ=4.207579833788249×10^27 g³/s (Mech-S7 ROT004) and a public source exponent s_h≈−1.2 vs paper s=−1.3, the mass law gives

    dt=-(3 M²/Γ)dM.
    Q_h(M)=Q_h(M0)(M/M0)^s.
    N_emit(s)=(3 Q_h(M0) M0³/Γ) · (1-u_cut^(3+s))/(3+s), u_cut=M_cut/M0.

For a zero initial *subedge population* at the table edge, the surviving population at cutoff is exactly

    n_h(t_cut;s)=∫_(t_edge)^(t_cut) S_h(v) exp[-D_h(t_cut-v)] dv.

Dropping the common factor 3 Q_h(M0)M0³/Γ, the surviving integral is

    I_surv(s,D) = exp(Λ u_cut³)/3 · Λ^(−a) · [γ(a,Λ)−γ(a,Λ u_cut³)]
    a=1+s/3>0, Λ=D M0³/Γ, γ(a,z) lower incomplete gamma.

All calculations use the **actual finite nominal cutoff**, with numerical evaluation of the gamma difference and independent quadrature checks. The mathematical formula is exact within the frozen linear model. Source-native log floor and PBH dilution are not dynamically replayed; rates are assumed constant across the terminal window.

More importantly, integrate the population differential equation with a common initial n_h and n_h(∞)=0:

    ∫_(t0)^∞ n_h(t)dt=[n_h(t0)+∫_(t0)^∞S_h(t)dt]/D_h.

Therefore for the difference between paper and public source laws with the SAME initial n_h,

    Δ ∫ n_h dt = (ΔN_emit,h)/D_h.

If X is frozen, the signed neutron-conversion coefficient is c_h=(1-X)c_Ah−X c_Bh, so the integrated impulse contrast is

    ΔI_X = Σ_h (c_h/D_h) ΔN_emit,h.

This is an exact bookkeeping identity for **fixed coefficients** and a full integration through all residual post-source hadron decays. It directly respects REC10's important point that `SOURCE_OFF` does not imply `HADRON_FORCING_OFF`. It is not an exact nonlinear endpoint identity in the actual changing-background 10D Wu–Xu code.

## 3. Frozen background and source-native host parameters

The background was deliberately frozen at the last saved source-active point of public_exec, T=0.1447372646 MeV, with map-specific X values from the 1600-point original 2×2 public trajectories:

    B_exec X=0.497967914; B_sym X=0.496214275.
    n_gamma=2ζ(3)/π² · (T/(ℏ c))³; eta_B=6.1×10^-10.
    n_B=5.86363304318×10^25 m^-3.

Hadrons: π−,π+,K−,K0L,pbar,nbar. The same source-native Coulomb enhancement Fc(T,m), baryonic mbarn cross-sections and intrinsic decays are used as `tool_script-parameters.jl`. `B_exec` maps each full charge-aggregate Qπ,QK,Qp,Qn into the tracked single species; `B_sym` halves only those four paired aggregate sources, leaving K0L unchanged. No hadronic source inputs were fitted after seeing the output.

Unweighted count ratio paper/public and surviving population at cutoff:

| Tracked channel | N_emit ratio | n_cut ratio | D [s^-1] (approx, B_exec) | M_tau=(Γ/D)^(1/3) |
|---|---:|---:|---:|---:|
| π−,π+ | 1.05854 | 1.79469 | 3.8415×10^7 | 4.78×10^6g |
| K− | 1.06079 | 1.88332 | 8.1132×10^7 | 3.73×10^6g |
| K0L | 1.06070 | 1.79316 | 2.0030×10^7 | 5.94×10^6g |
| pbar | 1.05630 | 1.42596 | 5.7163×10^4 | 4.19×10^7g |
| nbar | 1.05602 | 1.42343 | 5.7099×10^4 | 4.19×10^7g |

`M_tau` is the mass for which remaining source lifetime M³/Γ equals the frozen species population lifetime 1/D. It is a scale separator, not a new parameter/bound. In the public-law asymptotic gamma kernel roughly 80.2–80.3% of the **survivors at cutoff** were generated in the final one species lifetime; all such boundary-layer masses are two to three orders below M0, entirely outside the tabulated input support. Therefore the large cutoff-survivor ratios are especially sensitive to unsupported deep subedge extrapolation.

Independent quadrature of the incomplete-gamma integral agrees within 1.0×10^-10 relative for pion and about 2.1×10^-12 for antinucleon controls. These are *integral consistency* checks, not tests of physical source validity.

## 4. Signed integrated conversion and negative mechanism control

Use source-native reaction coefficients and losses, with the same frozen T and X for both emission-law variants within each map. `ΔI_X` is a *scaled diagnostic*; absolute values omit a common positive normalization factor 3M0³/Γ and the PBH number-density factor. They are NOT the dimensionless physical ΔXn. One obtains:

| Frozen map | I_public (scaled) | I_paper (scaled) | paper/public−1 | sign of ΔI_X |
|---|---:|---:|---:|---|
| B_exec | +50.13301 | +50.70434 | +1.13964% | positive |
| B_sym | +58.51238 | +60.67700 | +3.69941% | positive |

The dominant signed terms are strongly compensating even after integration: in B_exec the public contributions pbar≈−8321.22, nbar≈+8354.29 in these common scaled units. The sign of the *change* is not guaranteed by the source fluence increases separately: B_exec Δ contributions pbar≈−468.48, nbar≈+468.02, with pions and kaons supplying positive remainder. In B_sym pbar≈−233.30 and nbar≈+234.94, likewise plus charged meson remainder. These near cancellations mean a large survivor effect is not equal to a large net neutron forcing.

FROZEN-SOURCE NEGATIVE CONTROL: the historical full Wu–Xu fixed-T 2×2 diagnostic, discussed in Mech ROT002, has ΔXn(B_exec)=−1.898856657e-5, ΔXn(B_sym)=+1.266713121e-5. Our frozen-coefficient impulse law produces **positive ΔI_X in both maps**, so it does NOT reproduce the historical sign reversal. This rules out the over-simple *frozen coefficient* explanation, not the possibility of a genuine source-law × charge-map interaction once the full dynamics is solved.

The fixed-X sign-change threshold for ΔI_X within each map (solving the frozen nonlinear dependence of its coefficients on X) is:

    B_exec Xcrit=0.4982348542, ΔXcrit from last-active X=+2.66940×10^-4.
    B_sym  Xcrit=0.4982358459, ΔXcrit from last-active X=+2.02157×10^-3.

At T varied ±2% about freeze, Xcrit ranges 0.4982118 to 0.4982585. The tiny distance of the exec branch to the sign threshold is a reason to audit actual X(t), NOT proof it crosses a particular dynamic threshold or establishes the sign of the physical endpoint.

## 5. Impact on mechanism/empirical anchor and cheapest discriminator

MECHANISM MAP:
1. Hawking mass law M³(t) → extrapolated hadronic source Q_h(M) (supported only above M0).
2. Species population memory n'_h=S_h−D_hn_h; emitter fluence, n_cut, and ∫n dt are distinct.
3. Reaction map F=(1-X)A−XB with anti-nucleon directional cancellation and X-dependent branching probabilities.
4. Source-native fixed-T X(Tnuc) requires weak n↔p, cosmic expansion, m(t)/T(t), species kinetics and the cutoff on accepted solver steps.

EMPIRICAL ANCHOR: helium/deuterium BBN endpoints remain **not achieved**. The strong archived β=1e-16 test produces an invalid physical reduced Y proxy >1; no PBH constraint can be inferred. Wu–Xu published figure genealogy and source-valid E2b below M0 are separate unresolved gates.

CHEAPEST TRUE DISCRIMINATOR: execute source-native accepted-step 10D Julia run with (a) source-native mass-cube invariant monitored at accepted steps, (b) explicit reltol/abstol ladder, (c) one frozen cosmological background, (d) all six log n_h, source Q_h, A,B,F,X, log floor and *post-source carried hadron forcing* traces, (e) correct interpolation at fixed Q/Tnuc. Compare sign of ΔXn and a certified per-cell error <6.33356560558e-6 (sufficient from MT13's existing exact 2×2 analysis), not only bit-repeat and local-tolerance metadata. Independently acquire physical source/hadronization below 10^9g before any E2b/modern BBN or PBH bound discussion.

REC10's Duhamel source-guard and MT13's endpoint error gate are adopted as constraints; neither review is declared completed for this newly computed frozen-kinetics result. If controlled full run removes opposite signs or requires unsupported source below M0, record NEGATIVE_KNOWLEDGE / HOLD rather than fitting a narrative.

## 6. Reproducibility and boundaries

Run: `python terminal_memory_vs_fluence_005.py` (Python 3, SciPy, NumPy). Outputs local JSON, species CSV and sign-root sensitivity CSV. Gamma integrals independently checked via SciPy `quad` in dimensionless y=Λr to avoid stiffness. All model inputs, frozen X/T, pinned source edge rates/slopes, and code constants exposed. It is not a 10D Julia run.

Source inputs: Wu–Xu pinned `tool_script-parameters.jl`, `tool_script-hadrons_from_PBH.jl`, `data/out/hadrons_from_PBH.dat`, `main-scan.jl`; Mech-S7 ROT004 exact source-native Γ and original Mech-S6 2×2 point. Complete references/reproduction manifest in accompanying package.

**NO_CANON · NO_EXEC_SIGN · NO_NOVELTY · NO_SOURCE_VALID_E2B · NO_MODERN_Yp_DH · NO_PBH_BOUND · BW_INGEST_UNVERIFIED**.