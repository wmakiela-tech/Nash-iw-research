Mature published foundation: randomized qubit Pauli-axis purity detection and two-copy SWAP identity (Physics Reports, *Analysing quantum systems with randomised measurements*, 2024, DOI https://doi.org/10.1016/j.physrep.2024.09.009); finite off-resonance composite pulse control (Kukita, Kiya, Kondo, *General off-resonance-error-robust symmetric composite pulses with three elementary operations*, PRA 106, 042613, 2022, DOI https://doi.org/10.1103/PhysRevA.106.042613); detuning-compensating controls (Berkheim and Tannor, *The robustness of composite pulses elucidated by classical mechanics: stability around the globe*, PCCP 28, 764–775, DOI https://doi.org/10.1039/D5CP03162A). Do not claim first discovery of Pauli twirling, bounded-detuning pulses, interval numerics or source discrimination.

**Scope exclusions:** no SWAP, no second quantum memory, no finite detector duration, no device imperfections beyond stated on-source square-pulse detuning and Lévy noise, no assertion about arbitrary composite pulses being inferior, no global LOCC discrimination closure gap on the original passive three-probe output.

## 1. Exact physical sequence and two source contracts

Each PAIR consists of two independent preparations of the SAME single sensor, each starting in |0>. An independent fair trit J∈{X,Y,Z} is sampled ONCE per pair and kept the same for its two shots. The two resulting classical Z outcomes are tested for EQUALITY. Peak transverse drive amplitude is Ωmax=Ω=10γ and the total FREE interval per shot is Δ=1/(2γ). Work in units γ=1, so Ω=10, q=γΔ=.5, t=π/(2Ω)=π/20.

The following source-ON stages occur in each shot:

1. Prepare the sensor by a **finite square +Y π/2 pulse** of duration t, with Hamiltonian H=(ξZ+ΩY)/2 under A, or with the **driven Lindblad** generator −i[ΩY/2,ρ]+γ/2(ZρZ−ρ) under B.
2. Free evolve for Δ under ξZ/2 (A) or dephase under γ/2(Ad_Z−Id) (B).
3. If J=X, perform a source-ON **−Y π/2** analysis pulse of duration t. If J=Y, perform a source-ON **+X π/2** analysis pulse of duration t. If J=Z, perform NO analysis pulse. Then directly perform an ideal projective Z readout. The X and Y analysis pulse generators contain exactly the same unknown static ξ under A or continuously active Lévy dephasing under B. A Z shot is shorter than an X/Y shot.
4. Reset the sensor to |0> and repeat the same J for the other shot. **A retains the SAME ξ across both shots of the pair**, including the reset gap. It can take ANY real value and may change arbitrarily BETWEEN pairs, provided it is chosen exogenously independently of the fresh private axis trit. Source B has independent increments across every free, pulse, and successive-shot interval.

