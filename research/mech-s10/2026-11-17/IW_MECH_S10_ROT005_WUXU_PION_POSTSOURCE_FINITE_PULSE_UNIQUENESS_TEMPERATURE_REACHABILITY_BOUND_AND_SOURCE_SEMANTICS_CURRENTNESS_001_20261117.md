---
artifact_id: IW_MECH_S10_ROT005_WUXU_PION_POSTSOURCE_FINITE_PULSE_UNIQUENESS_TEMPERATURE_REACHABILITY_BOUND_AND_SOURCE_SEMANTICS_CURRENTNESS_001_20261117
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
date: 2026-11-17 Europe/Warsaw
type: SOURCE_FIRST_CLASSICAL_KINETIC_DISCRIMINANT_WITH_ACTUALLY_EXECUTED_INDEPENDENT_PYTHON_REPRODUCTION
exposure: PUBLIC
status: EXACT_UNIQUENESS_PASS / TEMPERATURE_NECESSITY_PASS / SCIPY_SYMPY_EXEC_PASS / NATIVE_10D_HOLD
science_ceiling: NO_PBH_BOUND / NO_ORIGINAL_WUXU_TRAJECTORY / NO_PAPER_OR_LINEAGE_ERROR / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# Mech-S10 ROT005 — sharp finite-pulse source-off pion sign reachability and temperature threshold

## 0. Distinctness, primary-source identity and currentness

ROT003 established a constant-positive equal charged-pion source local response; ROT004 established the *steady-before-stop* source-off sign flip and one synthetic source duration case (a=2,b=1). LT9 ROT003 independently established exact nonautonomous charge-imbalance dynamics in the original ten-dimensional author ODE. This ROT005 proves a **general necessary-and-sufficient existence and uniqueness theorem for any positive unequal capture rates** and derives an original-constant temperature reachability threshold which strongly constrains the earlier idealized post-stop mechanism.

Original Wu–Xu source, author commit `Fenyutanchan/Primordial-Black-Hole@d395183674cace6c9906a8911bdeb7234ba4040d`: directly reopened `arXiv-2509.05618/main-scan.jl`, original Git blob `b368ba55d5a493f7bc185909730f7fe5691f10d6` (nPBH flag line60, pion source line103, pion dX line90 and separate density lines109-112), and `tool_script-parameters.jl`, Git blob `0d7198ff3557bdbd5753000bb07a7a7405cc24f5` (tau_pi=2.6033e-8s, eta_B=6.1e-10, cross sections 1.5mbarn Fc and 1.7mbarn, m_pi, m_p, alpha_EM, n_gamma and Coulomb Fc). Upstream source rate and kinetic firstness Wu and Xu; BlackHawk origin Arbey and Auffinger. No prior original physical numerical result reattributed.

Late scientific currentness: Badacz `INPUT_075` (Git blob a821ed49c69cf9776f7ec27af09fde685bcd74c4) suggested the Wu–Xu full-group-per-charge source convention follows Kohri 2001 and Kohri–Yokoyama 1999. REC13 ROT005 original-source referee (Git blob e26dabb093103b9362dbece23924ce2df4b7e20f) independently confirmed the **printed KY1999 charge-count inconsistency under literal exclusive yields**, but held the stronger claim that Kohri 2001 *implemented* a full-group yield in each charge-state reaction. Original Kohri 2001 primary PDF Eq34 and Fig5 were also examined here in text: the plot is charge-GROUPED while Eq34 sums species, and does not explicitly select the charge-split operator. PDF screenshot retrieval failed, so no primary figure-pixel-level claim. This is **NOT** a new T3 review, not a lineage error or Wu–Xu paper error; LT9 and XH-S7 already own the relevant independent source tasks. Do not silently adopt Badacz INPUT075's stronger interpretation.

T2R: Badacz SYNTH_074 r2 confirmed no native 68-call run started and consented to transfer one session to Mech-S10, but explicit **human Moderator acceptance of Mech-S10 as executor remains unverified** in inspected issue#16, relevant commits and Slack. No native run initiated.

## 1. Exactly specified local problem

Let a positive common pion injection S run for duration L>0 from zero initial pi-minus and pi-plus populations. Assume T>0, neutron fraction X in (0,1), nB>0, and S all constant over that finite pulse and after source-off (S=0 after the pulse), with constant original source collision coefficients. Define

  gamma = 1/tau_pi >0,
  A=(1-X)*nB*(1.5mbarn*Fc(T)) >0,
  B=X*nB*(1.7mbarn) >0,
  a=A/gamma, b=B/gamma.

The pion ODEs are nminus'=S-(gamma+A)nminus; nplus'=S-(gamma+B)nplus during injection, followed by respective exponential losses with S=0. Original pion contribution to the *physical-time* neutron-fraction derivative is (A*nminus-B*nplus)/nB.

The dimensionless signed entire post-shutdown response, with u=gamma L, is:

  j(u) := gamma*nB*Jtail(L)/S
  = a/(1+a)^2*[1-exp(-(1+a)u)] - b/(1+b)^2*[1-exp(-(1+b)u)].

For u>0, a!=b, this is well defined. It is a **frozen-background classical ODE convolution**, NOT a physical PBH cosmic trajectory or author 10D numerical result.

## 2. New sharp global theorem and proof

For a>b>0, j(0)=0 and

  j'(u) = a/(1+a)*exp(-(1+a)u) - b/(1+b)*exp(-(1+b)u).

At u=0, j'(0)>0 because z/(1+z) strictly increases in z. The derivative crosses zero exactly once at

  u_peak = ln{a*(1+b)/[b*(1+a)]}/(a-b) >0,

and j' is strictly negative for every u>u_peak. Therefore j first rises, then falls monotonically to

  j(infinity)=(a-b)*(1-a*b)/[(1+a)^2*(1+b)^2].

This proves the exact **necessary and sufficient** finite-pulse inversion condition:

- a*b>1 (equivalently AB>gamma^2): j has exactly ONE positive nontrivial root ucrit>u_peak, positive before ucrit and negative after it.
- a*b=1: j remains positive at every FINITE u>0 and approaches zero from above.
- a*b<1: j remains strictly positive at all u>0.
- For 0<a<b, interchange the species to obtain the sign-reversed statements; a=b gives identically zero response.

Thus for A!=B an opposite signed entire poststop tail is reachable by a sufficiently long preceding constant source pulse **iff AB>gamma^2**, with one unique finite critical duration. ROT004 proved this only in the special a=2,b=1 witness; ROT005 establishes the general uniqueness/existence condition.

Additional exact temporal reciprocity:

  dJtail(L)/dL = Psteady_poststop(t=L),

where Psteady_poststop is the already-derived decay tail starting from the infinite pre-stop local steady populations. This follows directly by differentiating the finite-pulse expression, and explains why u_peak equals the previously obtained steady-tail source-off sign-crossing time in units of tau_pi. It is standard linear-response calculus; NO novelty asserted.

## 3. New source-constant reachability bound in T and X

For original author parameter values and natural-unit-to-SI conversion, use

  nB(T)=eta_B*[2*zeta(3)/pi^2]*[kB*T/(hbar*c)]^3
  (when T is specified as energy in MeV, kB*T = T_MeV * MeV_J).

With sigma-v cross sections from natural units, area times c gives per-volume kinetic rate in SI. Then

  AB/gamma^2 =
  X*(1-X)*[nB(T)^2*(1.5mbarn*Fc(T))*(1.7mbarn)]/gamma^2.

For any T, X*(1-X)<=1/4, with equality uniquely at X=1/2. Therefore AB/gamma^2>1 is possible for ANY neutron fraction exactly when

  nB(T)*sqrt[(1.5mbarn*Fc(T))*(1.7mbarn)] > 2 gamma.

Here Fc=x/[1-exp(-x)], x=C0/sqrt(T), C0>0; its logarithmic slope obeys

  dln Fc / dln T = -(1/2)*[1 - x/(exp(x)-1)] in (-1/2,0).

Since nB^2 scales T^6, the maximum AB/gamma^2 grows strictly monotonically with T, with log slope between 5.5 and 6. There is exactly one crossing:

  **Tcrit = 4.294807511761714 MeV** [original author parameters, source-only freeze].

For every T<=Tcrit and every physically admissible 0<X<1, AB<=gamma^2: the finite-pulse *integrated* source-off pion tail CANNOT invert its initial sign within this model. For T>Tcrit there exists a nonempty interval in X allowing inversion for some sufficiently long source pulse. This is NOT a statement about the instantaneous tail sign (which can reverse formally late at low T) or the author's actual time-varying PBH/BBN system.

At T=5MeV, explicit original-constant values:

  max_X AB/gamma² = 2.4731494409685433,
  AB>gamma² iff X in (0.114105821289965, 0.885894178710035).

Local pre-stop pion neutron effect is initially positive iff X<Xstar(T)=1.5Fc/(1.5Fc+1.7)=0.4902447448232642. Therefore **initially positive then entire signed posttail negative** is possible exactly for

  X in (0.114105821289965, 0.4902447448232642)

with a sufficiently long constant pulse. The opposite initial sign/integral inversion holds for X in (0.4902447448232642,0.885894178710035). Boundaries excluded.

For the illustrative frozen T=5MeV, X=.30 specifically: a=2.159130205471652, b=0.9621677864303547, ab=2.077445530413576. The unique critical preceding source duration is

  ucrit=0.8246719015406858 pion lifetimes,
  Lcrit=2.1468683612808674e-8 seconds =21.4686836128ns,

whereas the steady post-stop instant sign reversal is at u_peak=0.2773896818209495. At L=.7 Lcrit, the normalized signed tail is +0.012022193720952451; at L=1.5 Lcrit it is -0.01584613731533316. These are not measured PBH durations or observational times.

At T=1MeV, X=.15, ab=8.947775474654037e-5 and the integrated poststop response retains its original sign for all L>0, despite the late mathematical instantaneous sign change in ROT004. Distinguish sign of the pointwise tail from sign of its integral.

## 4. ACTUAL independent execution and negative controls (not a script-presence claim)

In the current ROT005 container, an independent Python3 script was **ACTUALLY EXECUTED**. It uses SciPy DOP853 ODE numerical integration of nminus,nplus and their cumulative neutron response, separate analytic closed forms, exact SymPy1.14 factorization, derivative reciprocity, and source-constant root search; it does NOT import any prior Mech-S10 script and performs NO Julia/BlackHawk. It verifies:

1. SymPy exact factor j(infinity) and finite-pulse special a=2,b=1 polynomial; exact duration-derivative/steady-tail reciprocity.
2. Analytic vs independently integrated ODE responses for steady, short pulse (u=.4) and long pulse (u=1.3): signed areas (-0.02777777777777779, +0.017622416159927157, -0.013707585767706393); direct solver agrees within <=2e-13 absolute in these controls.
3. The full T5,X.30 steady signed area -0.03356359748128068 matches numerical integrated ODE -0.03356359748128104.
4. Unique duration root and two opposite-sign negative controls (0.7 Lcrit vs 1.5 Lcrit), plus T1MeV no-reversal controls for six pulse durations.
5. Tcrit 4.294807511761714 MeV and the T5 exact X interval.

The ACTUALLY EXECUTED independent script SHA256 is `edd2f075ac64313cdc11877a68a5cad7fcbb642d47646799ea3dbce096c44043`, and output JSON SHA256 `6d07e8d8c7a9fdee9c820a0794bf415a9049d19dafdb8b78c01ed78fc7f207fa` (both SHA256 of local bytes). The local conversation contains both exact files available for download. This proves an independent Python mathematical replay, **NOT** the previously absent original-two-Julia-file end-to-end execution of ROT003/ROT004 uploaded scripts; neither is retroactively marked executed. The original Julia source was read and authenticated via the connected GitHub API, not mounted inside the Python execution.

## 5. Admissibility, custody, and next owner boundary

These classical frozen-source formulas are relevant primarily as **negative knowledge**: the local postevaporation mechanism is not sign-definite without explicitly declaring temperature, neutron fraction, source history and an outcome integrand. The actual original 10D trajectory evolves X,T,nB and PBH mass, includes log floor/evaporation stop and competing hadrons, and has not been rerun here. No Yp beta root, physical 10D bound or author paper error is proved. At actual BBN temperatures at or below 1MeV the present local frozen coefficient condition is firmly below threshold, but no claim about actual Wu–Xu cosmic history is made.

Badacz INPUT075 source-lineage interpretation remains under external LT9/XH-S7 and REC13 C1 HOLD; do not promote lineage convention or physical factor-two correction automatically. The original T2R one-session 68-call (j22,j62 orig/E5) remains **HOLD pending explicit Moderator confirmation of transfer to Mech-S10**, despite Badacz consent in SYNTH074 r2. NO additional execution lease or native run requested, no automatic tasks issued, no BW/Living Theory/CANON/EXEC_SIGN.

FINAL:
ROT005_FINITE_PULSE_UNIQUENESS_THEOREM_EXACT / TEMP_SOURCE_GATE_4P2948075118_MEV / T5_X_INTERVAL_AND_21P4687_NS_ROOT / INDEPENDENT_SYMPY_SCIPY_LOCAL_EXEC_PASS / ORIGINAL_TWO_SOURCE_FILE_SCRIPT_EXEC_NOT_CLAIMED / KOHRI_LINEAGE_MAPPING_HOLD / T2R_LEASE_HOLD / E4_PHYSICS_HOLD / NO_PAPER_ERROR / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN.
