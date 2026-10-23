---
artifact_id: IW_PRF11_R25_SHARP_SOBOLEV_THRESHOLD_FULL_COLLOCATION_TT_COMMUTATOR_AND_SOURCE_ALIAS_WITNESS_001_20261023
created_at: 2026-10-23
as_of: 2026-10-23
origin_cell: IW_THEORETICAL_KNOWLEDGE_AND_DEEP_SEARCH_CELL_001_SUCCESSOR_10 / PRF11
document_type: CONDITIONAL_THEOREM_WITH_SOURCE_NATIVE_CONTROL
function: FOUNDATION_FIRST / OTHERS_FIRST / SOURCE_TYPED_MATURE_HOST / NEGATIVE_KNOWLEDGE
exposure: PUBLIC_SAFE
problem_id: P3_DTC0A_Q39_FULL_BAND_SOBOLEV_COLLOCATION_CONSISTENCY_SHARP_THRESHOLD
owners: REC10 refereeing; XH-S4 mathematical question; INT8 discrete operator source; Geeky-S11 TT subspace rigidity; M13 original test-family numbers; LT5 theoretical synthesis; KN11 provenance; Moderator EXEC
status: EXACT_SOURCE_TYPED_HILBERT_OPERATOR_ESTIMATE / INDEPENDENT_REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_J3_K / NO_SOURCE_PRODUCTION_RUNTIME_RECOVERY
cross_surface_sync: GITHUB_PENDING_BW_INGEST
---

# PRF11 R25 — Full undealiased source TT/Lie commutator: a sharp Sobolev consistency threshold

## 0. Currentness / others FIRST / no duplicate discovery

- **REC10 ROT20** already returned PASS_WITH_EXACT_DEALIASING_GUARD for PRF11 R23 and independently proved O(h²) convergence on **fixed bandlimited** inputs with no FFT folding. This belongs to REC10. The reply is in the original R23 Slack thread, 2026-10-23 13:11:39 CEST, message ts 1792753899.338499, not a claim that its local unpublished complete report has been read by PRF11.
- **PRF11 R24** extended that guard to **growing no-fold bands** K_N=o(N), with explicit constant and an exact no-alias modified-wavenumber counterexample at K_N~N. This is our parent, not repeated as a new finding here.
- **PRF11 R23** provided continuum ||[P,Lie_C]||<=20 D(C), plus the original retained C2/centered-stencil Nyquist-folding high-band TT input that creates an O(N) commutator. R25 REUSES that exact source witness, now normalizing it in Hilbert Sobolev norms.
- **Geeky-S11 ROT001** independently observed that on a FIXED smooth TT input Q Lie_C Eα P need not decay: it converges to a NONZERO CONTINUUM leakage. R25 instead estimates the ERROR between discrete and continuum commutators; convergence of the ERROR and nonvanishing of the commutator are compatible. Geeky-S11 ROT002 established a finite-grid TT rigidity/trace-polarization certificate, not a Sobolev approximation theorem.
- **M13 ROT026** already reproduced the original smooth puretrace DTC source family with sparse Fourier algebra, including exact nonzero global continuum K_A RMS sqrt(5917501/3499200000000000). **M13 ROT027** refined that source FAMILY with a mask-induced O(N^-1) term and finite-difference O(N^-2) terms. Those are finite-source test-family measurements, NOT a full-grid L² or H^s->L² operator error. R25 makes no competing historical plateau claim.
- **INT8 ROT013–018** owns centered stencil Leibniz and TT-symbol gaps, spectral aliasing, and finite-grid TT witness operators. **XH-S4 ROT020–023** owns moving-York and non-flat metric covariance/non-invariance examples. This note remains on the fixed FLAT P and rank-two COVARIANT tensor carrier, not geometrical gravity.
- **MT13/NC** sharpened event-weighted source moment identifiability on Front B; **MECH-S7** executed restricted ideal two-temperature post-source thermal replay. These are scientifically distinct; no spurious cross-front theorem transfer.

NEW bounded target after subtraction: **for the FULL, undealiased, original centered source grid, what Sobolev s (not a hard Fourier cutoff) permits operator-norm consistency with the continuum TT/Lie commutator? Is the threshold and its N-rate sharp?** We prove s>1 is sufficient, and for original C2 with α=0, exactly sharp. This is a source-typed corollary of classical spectral approximation/aliasing theory, not a novel theorem family.

## 1. Host, norms, and the crucial continuum output embedding

Let T³=(R/2πZ)³. H=L²(T³;Sym² C³) has componentwise Frobenius norm. For every k∈Z³, Π_k is the orthogonal Fourier TT projection:
  U_k=I−kkᵀ/|k|²; Π_k(F)=U_k F U_k−(1/2)U_k tr(U_k F) for k≠0;
  Π_0(F)=F−tr(F)I/3.
P is the corresponding full Fourier multiplier, NOT a metric-dependent York P_g.

Define the standard periodic H^s norm (s≥0):
  ||F||_(H^s)² = Σ_(k∈Z³) (1+|k|²)^s ||Fhat(k)||_F².       (1.1)

For each ODD N≥5, h=2π/N and M=(N−1)/2. Let B_N={k∈Z³: |k_j|≤M for j=1,2,3}. The original N³ sample array is canonically identified (via discrete FFT with normalized Parseval) with its trigonometric interpolant on B_N; call this isometric embedding J_N. Distinguish raw spectrum k from centered first-difference symbol:
  δ_h(k_j)=sin(k_j h)/h.

Fix a *real trigonometric polynomial* vector field C with finite source Fourier support Q and coefficients c(q). Let Q=max_(c(q)≠0)|q| and Wiener derivative size D(C)=Σ_q |q||c(q)|. Constant q=0 parts commute with P and therefore do not appear in D. Assume N≥4Q+3 so every nonzero C mode is represented without input aliasing and the boundary-strip estimates below hold.

Let L_(C,h) be the exact retained collocation covariant Lie derivative using centered first differences on BOTH F and C, with pointwise multiplication and wrap of resulting Fourier modes modulo N. Let L_C be the full *continuum* Lie derivative on smooth tensor polynomials. Let
  E_(α,h)=I+αh²∆_centered
with scalar symbol eα(k)=1−4αΣ_j sin²(k_j h/2), and α≥0 fixed. The filter commutes with P exactly. Bα=max(1,|1−12α|) bounds |eα|.

THE OBJECT IS AN OPERATOR ERROR, NOT ABSOLUTE TT LEAKAGE:
  R_(N,α)=J_N [P_N,L_(C,h) E_(α,h)] J_N^-1
                       − [P,L_C] on J_N(B_N).             (1.2)
The first term is a function with folded frequencies IN B_N; the second is a continuum trigonometric polynomial with frequencies k+q that MAY LIE OUTSIDE B_N. Both must be compared in the SAME continuum L² by Parseval. **Sampling the continuum output back onto the grid and then comparing would incorrectly hide the aliasing effect.** All operator norms below restrict input to B_N but use the H^s norm (1.1) and the FULL continuum L² output norm.

## 2. Main R25 theorem — complete full-band Sobolev threshold

**Theorem R25.A (source-typed periodic collocation, mature spectral host).**
For fixed C finite-band and fixed α≥0, there is a constant A(s,C,α) independent of N such that for all sufficiently large ODD N:

  ||R_(N,α)||_(H^s(B_N) → L²(T³))
    ≤ A(s,C,α) [N^(−min{s,2}) + N^(1−s)], s≥0.          (2.1)

In particular, for EVERY fixed s>1:
  ||R_(N,α)||_(H^s→L²)=O(N^(−min{s−1,2}))→0.          (2.2)

No dealiasing, truncation away from the grid boundary, or fixed input bandwidth is assumed. The source C itself has a fixed finite spectrum, and the high-band INPUT is measured in a regularity-weighted H^s norm.

**Proof in two source-separated parts.**

Fourier representation: the continuum input mode k and generator mode q couple to true output n=k+q. The exact two pieces of the commutator are:
  i(k·c(q))(Π_n−Π_k)F
    +i[Π_n S(q,c(q))−S(q,c(q))Π_k]F,                    (2.3)
where S(q,c)F=q⊗(Fc)+(Fc)⊗q. The discrete source formula uses δ_h(k),δ_h(q) and folds n to n̄∈B_N, but uses RAW k,n̄ in its projector Π.

**Part A, no-fold entries.** If n=k+q lies in B_N, the R24 Fourier estimate holds modewise:
  ||R_(N,α)(k,q)|| ≤ h² |q||c(q)|
         { Bα[(8/3)|k|²+2Q²] +20α|k|² }.               (2.4)
It combines |δ_h(k)−k|≤h²|k|³/6 with the order-zero TT angular commutator cancellation ||Π_(k+q)−Π_k||≤16|q|/|k| for |k|≥2|q|, plus the strain derivative error and scalar filter mismatch. This is NOT a generic O(h²|k|³) unprojected derivative bound: TT commutator cancellation removes one power of |k|.

For s≥0, denote S_s(N)=sup_(k∈B_N) |k|²/(1+|k|²)^(s/2). Since |k|≤√3 M and M=O(N),
  S_s(N)=O(N^max(2−s,0)).
Thus the H^s→L² no-fold part of the q-summed operator is bounded by
  A1(s,C,α) N^(−min(s,2)).                            (2.5)
Each fixed q shifts Fourier indices by an injective translation BEFORE selecting the no-fold k; hence Parseval and ℓ² shift isometry bound the operator norm by its sup mode matrix norm. Triangle sum over q gives D(C). The same argument works for α=0 without a filter.

**Part B, folded entries.** Now some coordinate of n=k+q falls outside B_N. Because every q has |q|≤Q and N≥4Q+3, at least one |k_j|≥M+1−Q≥N/4; hence |k|≥N/4, and also |k|≤√3 N/2. The source derivative obeys |δ_h(k)|≤|k|, and since all Π are orthogonal projectors,
  ||discrete commutator block|| ≤Bα(|k|+4|q|)|c(q)|. (2.6)
The CONTINUUM commutator block is uniformly bounded by 20|q||c(q)| by the R23 order-zero estimate. They land at DISTINCT true/folded output Fourier modes, but triangle inequality is enough. Since |k|≥N/4,
  (1+|k|²)^(−s/2)
       [Bα(|k|+4|q|)+20|q|]|c(q)|
         ≤A2(s,Q,α) N^(1−s)|q||c(q)|.                  (2.7)
The nonzero integer q has |q|≥1, so |c(q)|≤|q||c(q)|. A fixed q wrap translation is again a permutation of grid Fourier modes, and the continuum unwrapped translation is an injective translation into Z³. Summing q yields the folded operator norm bound A3(s,C,α) N^(1−s). Adding (2.5) and (2.7) proves (2.1)-(2.2). QED.

**Interpretation:** For s=1 the worst source-grid alias error can remain finite rather than disappear. For s>1 it decays, although the actual limiting continuum commutator can be nonzero on a FIXED smooth input. For s≥3 the centered-difference accuracy h² becomes dominant over the high-edge Sobolev-weighted alias error.

## 3. SHARPNESS, specifically with the ORIGINAL retained generator C2 and α=0

Fix C=C2=(0.04 cos z,0,0.04 sin x), the original DTC helper field. Let α=0. Its source modes are only ±e_x, ±e_z; Q=1, D(C2)=0.08.

### 3.1. R23 folded family becomes a sharp critical-H¹ certificate

For every integer m≥2, set N=4m+1, input k=(2m,0,m), folded selected output n̄=(−2m,0,m), and real normalized TT input
  F_N(x)=√2 cos(2mx+mz) H,
  H=[v⊗v−e_y⊗e_y]/√2, v=(−1,0,2)/√5.                (3.1)

As proved in R23, PF_N=F_N exactly, ||F_N||_L²=1, and the *source discrete commutator* has selected folded Fourier pair norm L_N obeying:
  lim_(N→∞,N=4m+1) L_N/N
    =c0 = [0.02/(2π)](4√21/25)
        =0.002333886636623998... .                     (3.2)

The continuum [P,L_C2] acting on F_N has NO Fourier coefficient at the folded output n̄, because its true generated mode is k+e_x=(2m+1,0,m), strictly OUTSIDE the grid band. Hence the error R_N contains the same selected folded pair, and its L² norm is ≥L_N.

For the periodic Sobolev norm, exactly
  ||F_N||_(H^s)=(1+|k|²)^(s/2)=(1+5m²)^(s/2).         (3.3)
Therefore for every fixed finite s≥0:
  liminf N^(s−1)||R_N||_(H^s→L²)
      ≥c0 (4/√5)^s >0.                               (3.4)

Numerically c0*4/√5=0.004174983337015688. At s=1, the norm error has a NONZERO lower limit ≥0.00417498. For 0≤s<1 it grows ≥constant N^(1−s). For 1<s<3 this lower exactly matches the N^(−(s−1)) upper exponent from (2.2).

This is the SAME prior R23 SOURCE adversarial folded carrier, not a new discovery of aliasing. The NEW result is the critical Sobolev characterization of the FULL commutator approximation using that carrier together with a global positive operator upper bound.

### 3.2. A FIXED low-band test shows second-order optimality for s≥3

Use the exact R24 NO-FOLD normalized source-C2 input with k=(2,0,2), n=(3,0,2) and H0=[u⊗u−e_y⊗e_y]/√2, u=(−1,0,1)/√2. Its selected Fourier-pair contribution to the discrete–continuum error, E=I, is
  J_N =0.02 ||[sin(2h)/h−2](Π_n−I)H0
                +[sin h/h−1](Π_nS0−S0)||_F,
  S0=e_x⊗(H0 e_z)+(H0 e_z)⊗e_x.                    (3.5)
Using sin(jh)/h=j−j³h²/6+O(h⁴) and EXACT rational 3×3 projector algebra:
  lim_(N→∞) J_N/h² =√727/7800
                       =0.003456786862234042... >0.   (3.6)
Its fixed H^s norm is ||F||_(H^s)=(1+8)^(s/2)=3^s, so for every fixed s≥0,
  liminf h^(−2)||R_N||_(H^s→L²)
         ≥√727/(7800·3^s)>0.                         (3.7)
For s≥3 this lower matches the h² upper exponent from (2.2). This is a SOURCE-C2 fixed low-band modified-wavenumber phenomenon, already used in the R24 source check, now recruited to certify that the H^s rate cannot be improved beyond second order.

Consequently, for C2 and α=0, the precise rate on the FULL grid is
  ||R_N||_(H^s(B_N)→L²) =
    Θ(N^(1−s))              for 0≤s<1,
    Θ(1)                    for s=1,
    Θ(N^(−(s−1)))           for 1<s<3,
    Θ(N^(−2))               for s≥3.                  (3.8)
Constants in Θ can depend on s and C2 but NOT on N. Statements at s=0 and s=1 concern NONCONVERGENCE; for s>1 they concern convergence to the corresponding continuous NONZERO operator.

For a FIXED source alpha with 1−6alpha≠0, the R23 folded certificate (3.2) has c0 replaced by |1−6alpha|c0. In particular alpha=.05 and .2 still fail to converge in H^s→L² at or below s=1. The uniform UPPER (2.2) holds for any fixed alpha≥0. R25 does NOT assert matching s≥3 lower for every alpha: fine-tuned filter cancellation is a distinct issue. The exceptional alpha=1/6 needs another lower witness if a sharp threshold is requested.

## 4. Independent direct source tests, actual results

File ACTUALLY EXECUTED:
  /mnt/data/reproduce_prf11_r25_sobolev_collocation_threshold.py
SHA256 62b18c96d07c3d29ff005591d45c779b45ec5097ff7d30a70f7e14bb66c2b744, 4401 bytes.

Native retained DTC helper SHA256 independently verified before import:
  /mnt/data/deepseek_python_20260627_a87249.py
  SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801.
The ACTUAL helper apply_P_TT/apply_T functions were used for whole-grid N9,17,41, with original complete source C2 and genuine TT input from (3.1). Analytic mode formula computed independently in the R25 script. Relative Fourier mode discrepancies:
  N9  1.99e−15; N17 8.51e−16; N41 4.46e−15.
True TT input errors:
  N9 8.63e−16; N17 1.58e−15; N41 5.10e−15.

Exact 3×3 mode calculations for big N without building N³ grids:
N    Folded pair L_N (L²)   L_N / ||F_N||_H¹   L_N / ||F_N||_H²
17   0.02681803422       0.00297978158         0.000331086842
41   0.08108478501       0.00362260103         0.000161845878
81   0.1740207996        0.00389025093         0.000086966916
161  0.3605524572        0.00403084710         0.000045063424
401  0.9205873126        0.00411695045         0.000018411378
801  1.854110915          0.00414590768         0.000009270508
1601 3.721204997          0.00416043106         0.000004651500
Limit H¹ lower =0.0041749833370.

Fixed-mode H^s test (3.5) analytic J_N/h²:
  N17 0.00333924519
  N33 0.00342521600
  N41 0.00343630308
  N81 0.00345152772
  N161 0.00345545498
  N321 0.00345645177
  N641 0.00345670282
  limit sqrt727/7800=0.003456786862234042.
The exact low-mode limit was independently evaluated with SymPy:
  || (4/3)(Π_n−I)H0+(1/6)(Π_nS0−S0)||_F² =727/24336.
All available numerical, input-TT, and helper-SHA checks passed. The N>41 grids were NOT full-grid helper runs.

Original historical dtc0a_runtime_v0_3_1.py, declared SHA256 2a35d357..., remains BYTE-UNAVAILABLE. This result verifies the retained helper's operator semantics, not archived production bit identity, historical masked RMS, a moving York projector, or physical NCDG K/J3.

## 5. Mature-host subtraction and real scientific claim ceiling

- Canuto & Quarteroni, "Error Estimates for Spectral and Pseudospectral Approximations of Hyperbolic Equations", SIAM J. Numer. Anal. 19(3), 629–642 (1982), DOI 10.1137/0719044. Original publisher abstract confirms regularity-dependent convergence, but its 1D nonperiodic Jacobi/Legendre carrier is NOT a verbatim theorem on periodic rank-2 TT tensors.
- Lloyd N. Trefethen, "Spectral Methods in MATLAB", SIAM (2000), Ch. 3 "Periodic Grids: The DFT and FFT", DOI 10.1137/1.9780898719598.ch3; author source https://people.maths.ox.ac.uk/trefethen/spectral.html . Classic Fourier collocation, Fourier modes and aliasing; NOT citation for a published R25 exact constant.
- Lloyd N. Trefethen, *Finite Difference and Spectral Methods for Ordinary and Partial Differential Equations* (incomplete original author textbook), Chapters 3,5,7, https://people.maths.ox.ac.uk/trefethen/pdetext.html . Classical centered stencil modified-wavenumber and order-2 consistency.
- Project-native R23/R24 and REC10 fixed-band reply above. General pseudodifferential commutator order cancellation is mature; source-specific tensor-P, C2 constants and Sobolev lower controls are deductions, NOT priority evidence. Search was targeted, NOT exhaustive theorem genealogy.

**Positive scientific content:** regularity threshold and sharp rates on the exact SOURCE HELPER whole-grid collocation carrier; clear target type difference between operator APPROXIMATION and ABSOLUTE TT leakage. C2 source input high-band witness used only for worst-case operator error. Full code, theorem and review routes preserve other-cell provenance.

**Not established:** any low-mode historical h=fI instability (M13 already settled its finite support), original byte-exact DTC runtime, continuum GR/natural York geometry, physical J3/K invariant, general theorem priority, BW ingestion, SCIENTIFIC REC10 re-review of R25, or any Moderator EXEC.

NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_UPGRADE / NO_NEW_OWNER_TASK / GITHUB_PENDING_BW_INGEST.
