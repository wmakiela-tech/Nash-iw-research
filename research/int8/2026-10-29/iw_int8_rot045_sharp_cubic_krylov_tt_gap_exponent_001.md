---
artifact_id: IW_INT8_ROT045_CUBIC_KRYLOV_SHARP_TT_GAP_001_20261029
origin_cell: IW_MGPT_SCIENTIFIC_INTEGRATOR_SUCCESSOR_08 / INT8
problem_id: P3_DTC0A_FLAT_AFFINE_METRIC_NUMERICAL_COORDINATE_VS_GEOMETRIC_NORM_001
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: EXACT_MATCHED_CUBIC_ARITHMETIC_TT_NORM_GAP_EXPONENT / SOURCE_TYPED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE
---

# INT8 ROT045 — sharp cubic arithmetic gap for integer-flat metric source TT

Date: 2026-10-29. Scientific class: EXACT finite odd RAW-k auxiliary DTC0a operator mathematical result, independent Python/SymPy audit, TWO clean byte-identical reproductions. No physics. BW actual ingestion, external referee, science owner and Moderator EXEC remain unverified.

## Predecessors FIRST / unrelated source owners
MT13 FIRST proved correct affine metric E_g and naive target RAW-k alias fault; INT8 ROT033 FIRST source-matched natural metric P_g via the cubic stabilizer; INT8 ROT034–039 FIRST different TT locality and arithmetic stencil results; ROT040/041 exact pointwise and whole TT xy-shear norms; ROT042 FIRST general A Wielandt norm and exact finite-grid attainment criterion; ROT043 FIRST O_A(N^-2) uniform upper and infinitely many O_A(N^-3) Dirichlet subsequence upper; ROT044 FIRST exact positive angular curvature and strictly positive global angular constant c_A with an OMEGA_A(N^-4) integer CROSS-product lower bound. **ROT045 improves ONLY this last lower exponent to 3, matching ROT043 on an infinite subsequence.** M14 h=fI historical masked K_A, Geeky even-N RAW real-cast, PRF different Lie and XH curved York remain distinctly owned.

Classical mathematical hosts: irreducible integer matrix has every nonzero rational vector cyclic; integer determinant >=1; Vandermonde determinant; simultaneous 2D Dirichlet rational approximation; Wielandt inequality on transported orthogonal projectors. Lin/Sinnamon generalized Wielandt (2012) https://www.math.uwo.ca/faculty/sinnamon/pdf/wielandt.pdf ; classic Dirichlet in two dimensions https://pmc.ncbi.nlm.nih.gov/articles/PMC7114982/ . NO general mathematical novelty or original number-theory priority claimed.

## Carrier — nonzero SOURCE RAW-k and two different operator norms
Fix odd N=2m+1>=3. Carrier: full REAL Sym²(R³)-valued grid tensor fields; TT operator approximation norm on MEANZERO fields ONLY, k !=0 but all six symmetric tensor polarizations allowed. Literal auxiliary original source apply_P_TT, original retained user deepseek_python_20260627_a87249.py SHA256 23b0ec865263c5688682425af9d4c1f9cdb9f1d582a0f2f33d99c642c176f801, is an orthogonal rank2 Fourier TT projector on each nonzero signed wavevector k∈[-m,m]^3. Historical dtc0a_runtime_v0_3_1.py BYTE-UNAVAILABLE; masked original K_A and historic h=fI NOT RUN. The original unusual rank5 P(0) is not used anywhere in the result.

For A∈SL3(Z), D=A A^T and g=A^T A, source-to-target properly NATURAL operator P_g=U_A P_I U_A^-1, U_A H(x)=A^T H(Ax mod N) A. This remains orthogonal with norm 1 in correct tensor metric L²(g); the gap below is measured in a FIXED-coordinate Frobenius L²_0, not g. Let D have ordered eigenvalues a>b>c>0, abc=1, and eigenvectors v_plus,v_mid,v_minus. On a nonzero source k, M_A(k)=||C_A P_k C_A^-1|| with C_A(H)=A^T H A; M_N^0(A)=max_(k≠0 in signed cube) M_A(k), W(A)=(a/c+c/a)/2 and V_A=(a-b)(a-c)(b-c)=sqrt(disc(p_D)).

## T045.1 — exact irreducibility/cyclic-vector gate
D is an integer positive definite symmetric determinant1 matrix. For NONORTHOGONAL A its cubic characteristic polynomial p_D∈Z[t] has three DISTINCT positive roots (INT8 ROT042). By rational-root theorem, p_D is reducible over Q iff it has a rational root. A rational root of monic integer polynomial is an INTEGER; positive integer divides abs constant coefficient1, hence MUST be1. Therefore:

det(D−I)!=0 iff p_D is IRREDUCIBLE over Q.

For ANY k∈Z³ nonzero define the 3-step Krylov matrix and determinant
  K_D(k)=[k, Dk, D²k],  Delta_D(k)=det K_D(k).
If the matrix were singular, there would exist rational nonzero polynomial f of degree<=2 with f(D)k=0. But the irreducible degree3 p_D is the minimal polynomial of D and remains the minimal polynomial for every nonzero vector over Q (the Q[D]-module is simple); no polynomial of degree<3 can annihilate k. Hence K_D(k) is nonsingular. Its entries are integers, so:
  Delta_D(k)∈Z\{0}, |Delta_D(k)|>=1.          (T045.1)
This is a universal theorem for ALL nonzero integer k, not a consequence of scanning finitely many modes.

## T045.2 — sharp cubic lower exponent

Write k=k_plus v_plus + k_mid v_mid + k_minus v_minus and theta the acute angle with the middle eigen-axis. Vandermonde identity gives EXACTLY:
  |Delta_D(k)| = V_A |k_plus k_mid k_minus|.
The elementary bounds |k_plus k_minus|<=(k_plus²+k_minus²)/2=||k||² sin²(theta)/2 and |k_mid|<=||k|| imply
  1 <= |Delta_D(k)| <= (V_A/2)||k||³ sin²(theta).
Therefore for EVERY nonzero integer k:
  sin²(theta)>=2/[V_A ||k||³].                (T045.2)

On signed grid ||k||<=sqrt(3)m. ROT044 ALREADY proved an implicitly defined but strictly positive fixed-A constant
  c_A=inf_(||n||=1,n!=±v_mid) [W(A)−M_A(n)]/[1−(n·v_mid)²] >0,
by exact positive Hessian at unique maximizing middle eigendirection and compactness elsewhere. Thus
  W(A)−M_A(k) >= c_A sin²(theta)
               >= 2 c_A/[3 sqrt(3) V_A m³].
Taking minimum over nonzero k yields for EVERY odd N and ALL A with det(D-I)!=0:
  **2 c_A/[3 sqrt(3) V_A m³] <= W(A)-M_N^0(A) <= 8(a/c)/m².**       (T045.3)
The right inequality was FIRST established in ROT043. If c_A has not been globally numerically certified, this remains a rigorous POSITIVE but implicit constant. Do not invent a decimal c_A.

### Sharpness in the exponent — exactly typed
ROT043 used classical simultaneous Dirichlet approximation for TWO real ratios of v_mid. For nonrational v_mid, there are infinitely many signed grids N_j→infinity with
  W(A)−M_(N_j)^0(A) <= C_A N_j^-3
for some positive fixed-A constant C_A. Combine with T045.3 for ALL N:
  **W(A)-M_(N_j)^0(A) = Theta_A(N_j^-3)** on an INFINITE subsequence.
This establishes exponent 3 is optimal for a uniform POSITIVE lower bound, in the standard sense that a hypothetical lower ≥C_A N^-p with p<3 for all large N contradicts that subsequence. There is NO claim that all N satisfy an O(N^-3) upper bound, NO optimal global coefficient, and NO new number theoretic discovery. If det(D-I)=0, a rational middle eigendirection eventually appears as an exact finite Fourier mode and gap becomes ZERO — no positive bound allowed then. Orthogonal A gives W=1 and all gaps0.

## Example A_mix and EXACT discriminant
A_mix=[[1,1,0],[0,1,1],[0,0,1]],
D=[[2,1,0],[1,2,1],[0,1,1]],
p_D(t)=t³−5t²+6t−1, irreducible over Q because neither +1 nor −1 is a root.
disc(p_D)=49 EXACT; V_A=7.
Thus
  W(A_mix)−M_N^0(A_mix) >= 2 c_A_mix/(21 sqrt(3) m³).
Its integer Krylov determinant polynomial for k=(x,y,z) is
  x³−x²y+2x²z−2xy²+xyz−xz²+y³+y²z−2yz²−z³.
It takes ±1 e.g. on k=(1,0,0) and k=(0,0,1).
For two other irreducible test matrices [1 2 0;0 1 1;0 0 1] and [1 1 2;0 1 1;0 0 1] the exact discriminants are 1957 and 81. The rational middle-eigendirection control [1 0 -1;0 1 2;0 0 1] has det(D-I)=0 and correctly permits zero Krylov determinant on k=(2,1,0).

## Executed independent reproducibility, actual source, failure mode
Route A standalone NumPy+stdlib: EXACT Python integer Krylov determinant arithmetic over **225128** nonzero half-grid vectors, eight m=1,2,3,4,7,10,15,20 times four matrices; 168846 separate irreducible-angle lower bound controls. Three original unchanged SHA-verified auxiliary source apply_P_TT real mean-zero cosine N3/N5/N7 checks PASS. Matrix tests use exact integer determinant, while angle tests rely on floating eigenvectors, not source production numerical accuracy. Full historical masked K_A not run.

Route B separate wholly source-free SymPy/stdlib, NO NumPy and no Route A import: exact spectral Vandermonde formula for diagonal a,b,c and arbitrary symbolic k, four exact integer cubic charpolys and discriminants, exact 3-step Krylov cubic for each D, 27708 separate integer k checks and rational control with 219 legal zero determinants PASS.

**Negative knowledge:** preliminary Route B FAILED after SymPy internal charpoly returned a bare symbol named t while the external discriminant variable was t(real=True): same printing but different exact symbol, spuriously returning zero discriminant. Fixed symbolic variable identity, then reran COMPLETE exact audit. Both independent programs now PASS. The failure concerned test plumbing, not a theorem counterexample; initial attempt not passed off as a PASS.

Complete user/Moderator-local 8-file ZIP:
  iw_int8_rot045_sharp_cubic_krylov_gap_bundle.zip
SHA256 **ef31a04fb2a9c0a4478afa857e9881fa53dfc929c46120bfc58f17413947eecf**.
ZIP CRC PASS and SHA256 **7/7 member PASS**. CLEAN extractions A and B with literal SHA-verified original helper: both frozen JSON BYTE IDENTICAL. CLEAN C helper ABSENT: independent exact JSON byte-identical and all mathematical main fields exactly equal, source correctly SOURCE_SKIPPED_NO_HELPER. Original helper code not included in bundle. Full original Polish report, two complete stand-alone Python, two frozen JSON, README, RUNLOG and SHA256SUMS all in ZIP. The full scripts/JSON are not yet separately asserted to be present in public GitHub.

## STOP, custody, source limitations
Mathematical SOURCE-TYPED odd finite RAW-k TT, constant integer flat metric, mean-zero Frobenius L² only. NOT even-grid RAW Nyquist cast, not original historical masked h=fI K_A, original production runtime, curved York, GR gauge, Noether, J3/K, GW physical energies or experiment. No new scientific physical admission, no canon or EXEC, no general math novelty priority. BW actual ingestion, independent referee and original source owner all PENDING. No new task cascade.