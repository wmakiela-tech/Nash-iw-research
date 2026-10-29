## 4. Theorem R21.3 — 3-axis randomized local PURITY witness repairs finite-prep dependence under TRUE orthogonal projective readout

For two identically prepared independent single-qubit outputs ρ=(I+r·σ)/2, choose one common axis j∈{X,Y,Z} uniformly and measure both qubits along j. Define Zsame=1 if outcomes agree. For the fixed output state,

 p(same|ρ)=1/2+(r_x²+r_y²+r_z²)/6=1/2+||r||²/6.    (R21.5)

An exact operator identity follows:

 E_same=I_4/2+(XX+YY+ZZ)/6=(I_4+SWAP)/3.          (R21.6)

Consequently this is a standard two-copy **purity witness**, not a new unambiguous source detector. Under static A, all source-on finite preparation/free/axis-INDEPENDENT idle operations are coherent single-qubit unitaries conditional on the same ξ; both outputs are the SAME pure state, so ||r_A(ξ)||=1 for EVERY ξ and

 p_A(same|ξ)=2/3.                                   (R21.7)

No averaging or even a Cauchy marginal law is needed for this identity; any arbitrary history of static xi between pairs is allowed. Conditional independent fresh preparations and private basis randomness yield iid Bernoulli 2/3.

Under Lévy B all single-shot output states are the same mixed ρ_B. The 3×3 dynamics includes **finite source-active Y preparation**, exactly:

 r_B = diag(e^(−γ(Δ+t_d)),e^(−γ(Δ+t_d)),1)
       exp{[Ω [e_y]×−γdiag(1,1,0)] π/(2Ω)} e_z,

 p_B=1/2+||r_B||²/6.                              (R21.8)

For Ω>0, γ>0, Δ>0, the Bloch radius is strictly less than 1 because d||r||²/dt=−2γ(r_x²+r_y²) during any time source B is active, and Y drive creates a nonzero x component. Thus p_B<2/3, giving a globally phase-independent strictly positive gap in the S3 contract at FIXED Ω>0.

**Fixture:** γ=1, Ωmax/γ=10, Δ=.5, source-active finite preparation t_g=π/20, common source-active readout idle t_d=.05 and reinitialize/reset deadtime t_reset=.05. Direct 3×3 matrix exponentials yield p_A=2/3, p_B=0.5479181432777969. Exact binomial equal-prior test requires N=182 to get mean error <5% and N=185 to get EACH conditional error <5%. Physical-clock accounting under S3: γT_total =2N(.5+π/20+.05+.05)≈280.119464 at N=185. This time budget counts a calibrated ideal three-axis terminal projective instrument but NOT a finite-duration axis-dependent basis setting operation, and therefore is NOT a fully demonstrated Ωmax-limited implementation of those X/Y/Z projectors.

**Do NOT transfer** (R21.7) to S2 where axis-dependent source-active analysis pulses deform three measurement axes in different ways. Even a common source-on waiting period is harmless only because it is an identical coherent unitary under A before the three genuine projectors. A possible practical resource is a measurement apparatus directly calibrated in three orthogonal Pauli bases; such availability has not been established for the NASH hardware.

