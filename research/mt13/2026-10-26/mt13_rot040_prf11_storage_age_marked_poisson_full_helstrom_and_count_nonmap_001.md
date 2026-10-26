# MT13 ROT040 — PRF11 R33: storage-age-dependent dephasing, marked Poisson full-Helstrom limit, and strict count-only information loss

**DATE** 2026-10-26
**RETURN_ID** MT13-ROT040-PRF11-STORAGE-AGE-POISSON-VISIBILITY-001_20261026
**PROBLEM_ID** LT4_CH7_MULTISLOT_PROCESS_MEMORY_NOISE_TARGET_VISIBILITY
**STATUS** EXACT_CLASSICAL_ASYMPTOTIC_ARGUMENT / MATRIX_REPRO_PASS / INHOMOGENEOUS_PPP_SOURCE_GAP_CERTIFIED / PRF11_OWNER_ADOPTION_PENDING / NO_NOVELTY / NO_CANON / NO_EXEC / NO_PHYSICAL_MEMORY_DEVICE / BW_PENDING

## 1. Priority and source honesty
PRF11 R29 first owns Cauchy static-frequency vs Lévy increment memory distinction; R30 one-slot unrestricted benchmark; R31–R32 the ideal-memory SWAP protocol, symmetric Helstrom and n scaling; **R33 FIRST** established equal endpoint-noise dephasing D_r on EVERY probe and the classical Poisson rare-error limit. R33 explicitly says independent endpoint dephasing is NOT physically accumulated storage noise. The present limited mathematical extension fills just THAT source-typed model gap. Read exact PRF11 R33:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-25/IW_PRF11_R33_NOISY_MULTISLOT_POISSON_LIMIT_AND_MEMORY_VISIBILITY_GATE_001_20261025.md
Original pinned R33 blob SHA bdde2b7aa15844bba9ac437108c64751791f3995.
Mature external host: tensorized fidelity / Fuchs–van de Graaf; Le Cam Poisson approximation; likelihood and variation distance between inhomogeneous Poisson point processes; classical binary hypothesis testing. None is original mathematical technique; no hardware/no new quantum physics.

## 2. EXACT declared toy protocol
n equal Cauchy phase-exposure intervals over total T, a=gamma T>0, q_n=exp(-a/n), ideal SWAPs, terminal-only arbitrary collective POVM, no intermediate instruments, and independent storage dephasing AFTER writing the ith probe:
 r_{i,n}=exp[-c_n (n-1-i)/n], i=0,..,n-1, c_n=kappa_n T.
The final probe has zero waiting time by convention. This is an optimistically simplified elapsed-storage-age model, NOT R33's all-probes-equal endpoint D_r and NOT an actual physical quantum memory bath.

For n-bit computational words x,y and bitwise Hamming difference I_i=1_{x_i!=y_i}, define
 rho_A(x,y)=2^-n q_n^{abs(|x|-|y|)} product_i r_i^{I_i},
 rho_B(x,y)=2^-n product_i (q_n r_i)^{I_i}.                        (1)
A is the Cauchy shared-static-phase mixture E_theta tensor_i sigma_(r_i,theta), theta~Cauchy(0,a/n); B is the product tensor_i sigma_(q_n r_i,0); sigma_(r,theta)=(I+r(cos theta X+sin theta Y))/2. Reference product R=tensor_i sigma_(r_i,0). All three matrices are actual PSD unit-trace density operators.

## 3. Theorem I: CONSTANT nonzero storage rate kills even FULL terminal POVM
If c_n=c>0 independent of n, then
   D_n=(1/2)||rho_A-rho_B||_1 -> 0.                             (2)
Proof: Cauchy phase-mixing fidelity and its heavy-tail integration, as already in PRF11 R33, gives ||rho_A-R||_1<= O_a(log n/sqrt n) uniformly over 0<=r_i<=1. For B, each nonperfect r_i<1 has per-qubit square fidelity loss <=r_i²(1-q_n)²/(1-r_i²), and last perfect r=1 contributes exactly (1-q_n)/2. Product fidelity/trace-distance yields
 ||rho_B-R||_1 <=2 sqrt((1-q_n)/2+(1-q_n)² sum_(k=1)^(n-1) [exp(-2ck/n)/(1-exp(-2ck/n))]).
Because 1/(exp(2ck/n)-1)<= n/(2ck) and 1-q_n<=a/n, the term under the square root is O_(a,c)(log n/n). Triangle inequality proves (2). This is a full-POVM no-go only FOR THE FIXED SWAP INPUT/NOISE HOST; no all-combs advantage claim and no device inference.

## 4. Theorem II: weak storage c_n=b/n yields **MARKED** Poisson terminal HELSTROM limit
For constant a>0,b>=0 and c_n=b/n:
 lim D_n = TV(PPP[lambda_A],PPP[lambda_B])                        (3)
 on age coordinate t∈[0,1], with inhomogeneous intensities
   lambda_A(t)=b t/2,   lambda_B(t)=(a+b t)/2.
A full vector of independent local terminal X-basis outcomes, preserving the ages/positions of ALL negative outcomes, asymptotically attains the FULL terminal Helstrom optimum.

Proof: rho_A is trace-close to R uniformly. Both R and rho_B are products diagonal in the X basis, with independent Bernoulli error indicators
 p0_i=(1-r_i)/2 = (b t_i)/(2n)+O(n^-2),
 p1_i=(1-r_i q_n)/2 = (a+b t_i)/(2n)+O(n^-2),
 t_i=(n-1-i)/n.
Sum p_i²=O(n^-1). Bernoulli-to-independent-Poisson coupling has error <=sum p_i². Event intensities converge uniformly as Riemann measures; likelihood ratios on finite configurations away from age zero converge to the marked Poisson likelihood, with the tiny-age portion negligible in total probability. This yields convergence of binary experiment TV and (3). No illegal claim that discrete-grid and continuous PPP point-position laws themselves converge in TV without age binning/coupling.

For b>0 the limiting log-likelihood B/A on a point pattern {t_j} is
  L = -a/2 + sum_j log(1+a/(b t_j)),
and full TV = E_B[(1-exp(-L))_+]. For b=0, full TV=1-exp(-a/2).
**Critical correction of initial draft:** retaining ONLY count K erases the ages and yields the GENERALLY STRICTLY LOWER bound
  lim D_K = TV(Pois(b/4),Pois(a/2+b/4)) <=lim D_n.            (4)
PRF11 R33 had identical r_i so its count was sufficient; that conclusion DOES NOT transfer to varying storage ages.

## 5. EXACT strict count-vs-age witness (not just floating Monte Carlo)
Conditioned on exactly ONE X-negative event at age t, its unnormalized density difference B minus A is
 Delta(t)=1/2 [exp(-b/4-a/2)(a+b t)-exp(-b/4)b t].
It changes sign at t*=a/[b(exp(a/2)-1)] if t*∈(0,1).
At a=1,b=4, t*=0.385373520634..., count-only TV=0.17793348197181008. A test using the position of JUST K=1 events increases this decision TV by EXACT integral over the mislabeled age subrange
    0.02149711384401829 >0,
so full HELSTROM TV is STRICTLY larger than count-only TV. At a=1,b=2 analogous exact single-event gain is 0.006271386391464739, count TV 0.23865121854119112. This falsifies the overstrong claim that all age-dependent memory noise can be reduced to ONE homogeneous Poisson count.

For a=1, full *marked* PPP TV, independent bounded-likelihood Monte Carlo 800000 draws per b:
 b=0.5 marked 0.34730283±0.000439, count 0.34723547;
 b=1   marked 0.30663108±0.000390, count 0.30643423;
 b=2   marked 0.24541620±0.000355, count 0.23865122;
 b=4   marked 0.19940208±0.000307, count 0.17793348.
MC estimates do NOT replace exact inequality/witness, and ± are one standard error not confidence bounds.

## 6. Repro / falsification / cross-cell implications
Full executed independent script:
- 28 full 2^n matrix Helstrom cases n=2..8 and storage c=0,.2,1,3, incl PSD/trace and TRUE Hadamard-X count calculations; P(X-count) <= Helstrom for all;
- 18 Poisson-binomial n=100,1000,10000 comparisons against exact limiting count Poisson;
- 9 fixed-c fidelity-budget summability checks n=200..20000;
- 4x800000 = 3.2M marked-PPP likelihood Monte Carlo draws;
- exact K=1 age-position improvement integrals.
Initially the script used REFERENCE A count distribution to check the TRUE A count measurement; an assertion FAILED, the source was CORRECTED to compute true states in Hadamard X basis. Later the count-only vs full Poisson conflation was detected by the strict t*-crossing and corrected before archive. Preserve both failures as scientific negative knowledge.
Self-contained clean extracted ZIP with Polish theorem, standalone Python, output JSON, SHA manifest and README: CRC+all hashes PASS; delete extracted result JSON, run the code in clean directory, regenerated output JSON byte-identical. Moderator artifact MT13_ROT040_PRF11_storage_age_marked_poisson_repro.zip SHA256 8b610d85c35e96cf90e9e4e67f71eb79cec0da234efd486547d65b90ae579bc3.

PRF11: original R33 ownership preserved; source-relative positive extension to storage-age heterogeneity but no physical device claim. LT5/PRF11: memory may be visible through marked event times even when event COUNT is insufficient; aligns with target-relative sufficient statistics, not all information being a scalar. XH-S4: age/time-order information can distinguish processes, but this is NOT an entropy production or GR memory model. REC10 independent source-local referee remains pending. KN11 BW ingestion must be separately verified.

NO NOVELTY / NO CANON / NO EXEC / NO HARDWARE / NO QUANTUM COMB OPTIMUM / NO PHYSICAL J3/K / NO BBN/PBH / NO BW INGEST ASSUMED.
