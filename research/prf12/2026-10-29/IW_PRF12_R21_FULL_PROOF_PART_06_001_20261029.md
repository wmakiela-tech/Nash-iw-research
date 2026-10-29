## 5. Independent validation and falsification gates

Full standalone NumPy/SciPy code reimplements all branches and provides:
- 3×3 exact Bloch expm and fully independent 2×2/4×4 Hamiltonian/Lindblad density-matrix checks for A and B under source-on finite preparation/readout, across source frequencies and bounded drives;
- specific finite detuning counterexample ξ*=23.496399... at Ωmax/γ=10,q=.5, B probability .5681154068;
- Pauli X/Y/Z two-copy operator identity and exact pure-state 3-axis invariance, including source-active preparation and positive B mixedness;
- 5 gate budgets Ω/γ=5,10,20,50,100 and source-gated exact finite-sample counts/physical-clock costs; numerical Chernoff/time maximizer;
- sample-size audit for source-ON finite prep + ideal XYZ projectors;
- no stochastic Monte Carlo or fitted hidden-phase parameters in final reproduction.

**Research limits and next falsifiers:** independent reviewer must audit whether three different terminal projective axes are physically accessible with Ωmax and an **always-on** source, or whether only S2's finite basis switching is possible; consider shaped/composite robust pulses and exact diamond-error bounds if so. Audit finite QND detector backaction, reset-induced source changes WITHIN pair, correlated B increments, finite SPAM errors and stable shared orientation across shots. Estimate time spent choosing measurement basis and any inter-shot phase drift. Compare R19 and R21 ONLY with the same source-active gate/readout and reset contract; the current results instead map the logical boundary. Do not revive R07's withdrawn unrestricted single-copy LOCC closure gap claim.

RETURN: PRF12_R21 / THREE_EXPLICIT_SOURCE_GATE_BRANCHES / FIXED_DRIVE_SOURCE_GATED_CLOCK_CHERNOFF_FRONTIER / ALWAYS_ON_FINITE_XY_DETUNING_COUNTEREXAMPLE / PURITY_XYZ_SOURCE_ON_FINITE_PREP_RESET_INVARIANT / DIRECT_TWO_METHOD_NUMERIC_CHECK_PASS / NO_FULL_HARDWARE_EQUATION / NO_CANON / NO_EXEC / REFEREE_PENDING / BW_INGEST_PENDING.
