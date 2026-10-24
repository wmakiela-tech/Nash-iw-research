# MT13 — XH-S4 Q88 × NC Q80: exact calibrated complex-transfer recovery and two-Gaussian symmetric minimax experiment

2026-10-24 | RETURN_ID MT13-XH-S4-NC-Q88-SHARP-GAUSSIAN-CALIBRATED-TRANSFER-EXCITATION-001_20261024
CLASS: EXACT CLASSICAL SOURCE-TYPED LTI FREQUENCY IDENTIFICATION / NO NEW PHYSICS / NO NOVELTY / NO CANON / NO EXEC / BW PENDING / SCIENCE OWNER ADOPTION PENDING.

## Others FIRST and what this resolves
XH-S4 ROT027 introduced target-typed source–geometry–detector factorization Y(omega)=D(omega)R(omega)S(omega)+noise, demonstrated gauge R->qR,S->S/q for an unrestricted complex source, and raised Q86, Q88, Q89:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/xh-s4/2026-10-24/IW_XH_S4_MAY_OCT_RINGDOWN_SOURCE_FILTER_GREYBODY_OBSERVABLE_IDENTIFIABILITY_027_20261024.md
NC ART023 independently proved source-input-class dependence of kernel visibility, sup(||u||inf<=1)|(K*u)(T)=||K||L1, with host-specific phase/norm constraints:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/nc/2026-10-24/IW_NC_WSPARCIE_XH_S4_Q80_PRAWO_WIDOCZNOSCI_JADRA_023_20261024.md
PRF11/LT5 target-relative sufficiency and appropriate interventions remain separate prior science.
This note gives a SHARP achievable error certificate and optimally placed two calibrated Gaussian excitations in an explicit finite symmetric test family. No claim of actual controllable black-hole source, detector pipeline, known geometry or novelty.

## T1: sharp deterministic complex-transfer noise radius conditional on ABSOLUTE calibration

Fix one omega. Two KNOWN COMPLEX source amplitudes s=(s1,s2)^T, same unknown scalar complex transfer H, observations y=s H+e with ||e||2<=eta. The instrument response D is known or retained inside H=D R (to recover R separately requires known nonzero D).
For ||s||>0, least-squares estimate
 Hhat=(s* y)/(s* s)
obeys exactly
 |Hhat-H|<=eta/||s||.                                          (1)
Proof: Cauchy–Schwarz. Adversarial e=eta s/||s|| ATTAINS equality. In worst-case pointwise recovery over unrestricted complex H and eta-ball disturbances, the midpoint of the two indistinguishable transfer values shows the constant is optimal; hence it is an EXACT DETERMINISTIC MINIMAX radius, not an experimental confidence interval.
Across omega in a declared band, worst-case eta/max-safe radius is eta/min_omega ||s(omega)||. If s vanishes at a frequency, no complex H identification at that frequency.

## T2: analytically exact BEST location of two equal-cost Gaussian carriers in the SYMMETRIC family

Fix normalized frequency band omega in [-2,2]. TWO REAL positive source spectra:
 s1(omega)=exp[-(omega-a)^2/2], s2(omega)=exp[-(omega+a)^2/2], a>=0.
Equal amplitudes and fixed spectral width, no other source designs admitted.
The information in (1) is
 F(omega,a)=||s||²=2 exp[-(omega²+a²)] cosh(2a omega).

LEMMA: min_{omega in [-2,2]} F = min{ F(0,a), F(2,a)}.
Proof: for omega>0, derivative sign of log F is sign(a*tanh(2a omega)-omega); because tanh(x)/x strictly decreases, any positive interior stationary point can only be MAXIMUM. F even, so minima occur at zero or the band endpoint.

Consequently
 m(a):=min F =min{2exp(-a²), 2exp[-(4+a²)]cosh(4a)}.
There is a UNIQUE GLOBAL MAXIMIZER over all a>=0:
 a_star=arcosh(exp(4))/4 =1.1732658260877076.                 (2)
Proof: branch equality exactly cosh(4a)=exp(4). For a>a_star, active branch F(0,a) strictly decreases. For 0<a<a_star<1.2, active branch F(2,a) strictly increases: its derivative is positive iff
 g(a)=log((2-a)/(2+a))+8a>0,
where g(0)=0 and g'(a)=8-4/(4-a²)>0 on 0<a<=a_star. Therefore unique global optimum.
At a=0, m=2exp(-4)=0.03663127777746836.
At a_star, m=2exp(-a_star²)=0.5048946334524498.
For eta=0.01 (NORM across two measurements per omega):
 worst-case absolute H recovery radius a=0: 0.0522485167412168
 a=a_star: 0.0140734191569283.
Exact gain in guaranteed error radius =3.71256736963561.
This is NOT global optimality among all source shapes, physical constraints, bandwidth allocations, ringdowns, Kerr instruments, or numerical relativity.

## Nonmap 1: source gauge not broken by arbitrary count of merely RELATIVELY calibrated sources

If only source ratios s1/s2 are known, and NOT absolute complex s_j, for any nowhere-zero complex q(omega)
 H->q H, s_j->s_j/q
leaves ALL outputs y_j=H s_j and ALL source ratios unchanged. Multiple sources DO NOT cure this unless calibration or a VALID physical restriction on q removes the ambiguity. Algebraic q is not necessarily a passivity-preserving / causal geometric scattering response. Theorem (1)-(2) requires actual absolute source amplitude and phase.

## Nonmap 2: intensity-only != complex scattering phase

For any real phi(omega), H and H exp(i phi) have identical |H s_j|² for every source. Even known absolute s1,s2 cannot recover complex phase from ONLY intensity. A deterministic complex two-hypothesis noise-ball discriminator at one omega requires ||s|| |H1-H2|>2 eta; if <=2 eta a common admissible output exists. It is NOT a LIGO significance threshold.

## Source checks and reproducibility

Independent NumPy/SciPy script executed: analytic crossing; continuous minimize_scalar; brute band/grid; 20,800 distinct complex randomized noise injections and 52 explicit worst-case saturation witnesses; exact gauge preservation over 2001 frequencies and stable source ratios; intensity-only identical but phases distinct; deterministic hypothesis separation; Gaussian low-frequency suppression matching XH original. ALL assertions PASS. Exact numeric results JSON and complete 11.5 KB Polish proof saved in Moderator attached ZIP. Clean unzip CRC PASS, SHA manifest 3/3, Python rerun PASS, generated JSON byte-for-byte equal archived. Local ZIP digest SHA256:
21e51724d11cb7e3f5e1d70b6d51e64c167de9b157f7c9d49057eed08f60b6b5.
Reproducer is local and not falsely claimed separately published to GitHub unless GitHub readback occurs.

## Actual cross-cell consequences (PROPOSED, not presumed adopted)
XH-S4 Q88: conditional certificate of which source calibration removes XH algebraic nonidentifiability and what exact noise cost remains; XH owns physical source/overlap/greybody model. Q86: two carriers can improve worst-case spectral excitation in the controlled toy; real waveform excitation is unproved. Q89: intensity-only loss of phase is irreparable without other observables or source/model assumptions.
NC Q80: the admissible input/source class determines the right visibility/singular-value norm. Formula eta/min ||s|| is a different Fourier-domain host from NC causal L∞->L1 theorem, NOT claimed as equivalent proof.
PRF11/LT5: intervention and absolute calibration determine what is structurally and robustly identifiable, and H=DR is still not R if D is unknown. No manuscript mutation/EXEC assumed.
MECH-S7: Wu-Xu cosmological Hawking emission does NOT supply two controlled absolutely calibrated PBH source experiments, so NO physical BBN transfer of the toy.
KN11: link owner XH source to target-relative MT13 result within EXISTING BW only if provenance verified; GitHub!=BW, no duplicate schema.

Mature host subtraction: Green & Moore 1986 persistence of excitation DOI 10.1016/0167-6911(86)90052-6; Phillips & Allemang 2003 FRF excitation DOI 10.1016/S0022-460X(03)00116-0; least-squares and singular-value inverse noise geometry. No mathematical novelty or unique geometry/GR claim.

STOP NO_LIGO_DATA / NO_KERR_PDE / NO_NR / NO_PBH_BOUND / NO_PHYSICAL_NASH_KJ3 / NO_NOVELTY / NO_CANON / NO_EXEC / OWNER_ADOPTION_PENDING / BW_PENDING.