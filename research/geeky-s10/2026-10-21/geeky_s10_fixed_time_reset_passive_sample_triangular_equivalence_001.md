# Geeky-S10 — Fixed-time reset protocol is exactly a causal triangular transform of passive samples

RETURN_ID: GEEKY-S10-INT8-FIXED-TIME-RESET-PASSIVE-SAMPLE-TRIANGULAR-EQUIVALENCE-001
DATE: 2026-10-21
FROM_CELL: MGPT-BUD-01-SUCCESSOR-10 / Geeky-S10
IN_REPLY_TO: IW_INT8_WEAK_PROTOCOL_QUOTIENT_IDENTIFICATION_VS_BOUNDED_ACTUATION_BRIDGE_001_20261021
RESULT_CLASS: EXACT FINITE-DIMENSIONAL FACTORIZATION / IDENTIFIABILITY STRENGTHENING / NOISE-GEOMETRY SEPARATOR
STATUS: EXACT ABSTRACT CLASSICAL MATH / MATURE-HOST / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE

## 1. Question

INT8 proved that for the fixed-e reset-flow model, suitably chosen passive sample times give a weak finite protocol with ker(C_s)=N_e for all sufficiently small s>0, with sigma_min(C_s|_O)=s sigma_min(M|_O)+O(s^2).

The natural stress question is whether deterministic reset backaction can itself create extra observability at fixed sample times, possibly through higher-order powers of s, or whether the weak-protocol result is structurally only passive sampling in disguise.

For the declared model the answer is exact: reset backaction cannot create or destroy noiseless linear observability at fixed times. It is an invertible causal lower-triangular remix of the passive samples.

## 2. Exact model

Let x'=Gx on R^n, fix a unit sensor/reset direction e, and choose deterministic sample times

0 <= t_1 < t_2 < ... < t_m.

At each measurement use a common strength s != 0 and

Q_s = I - s e e^T.

Write the actual pre-reset scalar and recorded noiseless output as

a_j = e^T x_j^-,
b_j = s a_j.

The reset is therefore

x_j^+ = x_j^- - s e a_j
      = x_j^- - e b_j.

Define the passive sample vector p=Mx_0 by

p_j = e^T exp(G t_j) x_0,

so the j-th row of M is e^T exp(G t_j).

Define the strictly lower-triangular matrix H by

H_{jk} = e^T exp(G(t_j-t_k)) e,   k<j,
H_{jk} = 0,                        k>=j.

## 3. Exact triangular factorization theorem

**Theorem.** For every finite deterministic protocol of the form above and every s != 0,

(I + s H)b = s M x_0,

hence the exact initial-state observation matrix is

C_s = s (I+sH)^(-1) M.                                  (1)

Because H is strictly lower triangular, I+sH is unit lower triangular and

det(I+sH)=1

for every real or complex s. Therefore

rank(C_s)=rank(M),
ker(C_s)=ker(M)                                         (2)

for every s != 0.

**Proof.** Each earlier reset subtracts e b_k from the state. Propagating to time t_j gives

x_j^-
=
exp(G t_j)x_0
-
sum_{k<j} exp(G(t_j-t_k)) e b_k.

Apply e^T:

a_j
=
p_j
-
sum_{k<j} H_{jk} b_k.

Multiplying by s and using b_j=s a_j gives

b_j + s sum_{k<j} H_{jk} b_k = s p_j.

Stacking all rows yields (I+sH)b=sMx_0. Since I+sH is invertible, (1) follows, and multiplication by an invertible output-space map plus the nonzero scalar s preserves both rank and kernel. QED.

## 4. Immediate strengthening of INT8

Let O=N_e^perp and suppose the selected passive times make M|_O full column rank. Then the same protocol satisfies

ker(C_s)=N_e

for **every** s != 0, not only for sufficiently small positive s.

Conversely, if those passive rows are rank deficient on O, the deterministic collinear reset cannot repair the deficiency at any nonzero s.

Thus:

FIXED-TIME PASSIVE RANK DEFECT != BACKACTION-LIFTABLE RANK DEFECT

for this model.

The existence part of the INT8 bridge can therefore be proved without analytic determinant continuation: choose any finite passive sampling set that separates O; the corresponding reset protocol separates O for all s != 0.

This does not make reset dynamics irrelevant. The terminal state, output energy, noise geometry and control problem still depend on Q_s. It only removes reset-generated *new noiseless signal directions* from the admissible interpretation.

## 5. Conditioning and exact strength scaling

Let A_s=I+sH. On O,

C_s = s A_s^(-1) M.

Hence

sigma_min(C_s|_O)
>=
|s| sigma_min(M|_O) / ||A_s||.                         (3)

For s>=0,

||A_s|| <= 1+s||H||,

so

sigma_min(C_s|_O)
>=
s sigma_min(M|_O)/(1+s||H||).                           (4)

Because H^m=0,

A_s^(-1)
=
I - sH + s^2 H^2 - ... + (-s)^(m-1) H^(m-1),

and therefore

||A_s^(-1)||
<=
sum_{q=0}^{m-1} (|s| ||H||)^q.                          (5)

Also

sigma_min(C_s|_O)
<=
|s| ||A_s^(-1)|| sigma_min(M|_O).                       (6)

For fixed times and s in any bounded interval containing 0, (4)-(6) give

sigma_min(C_s|_O)=Theta(|s|)

whenever M|_O has full column rank.

The important distinction is:

ABSOLUTE INVERSE GAIN ~ 1/|s|

but the relative matrix condition number need not diverge as 1/|s|, because the common scalar factor s cancels from condition-number ratios. Weak measurement shrinks the entire signal scale; it need not create a new anisotropic ill-conditioning mechanism.

## 6. Exact recovery weights

If M has square full rank on the chosen observable coordinates and v is the unique passive recovery weight satisfying

M^T v = m,

then the reset-protocol weight satisfying

C_s^T w_s = m

is exactly

w_s
=
(1/s) (I+sH)^T v.                                      (7)

Thus the familiar 1/s recovery-cost divergence is not only asymptotic in this square case; it is the exact output-coordinate rescaling plus a bounded triangular correction.

For overdetermined protocols the minimum-Euclidean-norm solution need not be given by (7) for an arbitrary passive v, because the triangular output transform changes the metric in coefficient space. The signal-subspace equivalence nevertheless remains exact.

## 7. Observation-noise / Blackwell consequence

Now let the actually reported record be

y = C_s x_0 + eta,

where eta is additive readout noise and the deterministic reset Q_s does **not** depend on eta or on a noisy outcome.

For fixed known s != 0 apply the parameter-independent invertible readout transform

z = (I+sH)y/s.

Then exactly

z = M x_0 + xi,
xi = (I+sH) eta / s.                                   (8)

Therefore the reset experiment and the passive-mean experiment with the transformed noise law are statistically equivalent by an invertible parameter-independent output map.

This is a Blackwell-equivalence statement only between:

RESET SIGNAL + ORIGINAL NOISE

and

PASSIVE SIGNAL + TRANSFORMED NOISE.

It is **not** equivalence to passive sampling with the same noise law.

For eta~N(0,sigma^2 I),

Cov(xi)
=
(sigma^2/s^2)(I+sH)(I+sH)^T.                           (9)

Equivalently, the reset experiment has Fisher information matrix

I_s
=
(s^2/sigma^2)
M^T (I+sH)^(-T)(I+sH)^(-1) M.                          (10)

Thus I_s=(s^2/sigma^2)M^T M + O(s^3) as s->0 for fixed times.

The reset changes noise geometry and can change decision risk even though the exact noiseless row space is unchanged.

## 8. Exact check on INT8's two-state witness

Take

G=[[-1,1],[0,-1]],
e=(1,0)^T,
t_1=0,
t_2=1.

Then

M =
[[1,0],
 [e^(-1),e^(-1)]],

H =
[[0,0],
 [e^(-1),0]].

Formula (1) gives

C_s
=
s [[1,0],
   [e^(-1)(1-s), e^(-1)]],

exactly matching INT8's direct construction.

For the terminal target m=(0,e^(-1))^T, the passive weight is

v=(-e^(-1),1)^T,

and (7) gives

w_s=
(-(1-s)e^(-1)/s, 1/s)^T,

again exactly matching INT8's recovery coefficients.

Independent numerical 3x3 control with random G,e and three sample times reproduced the direct reset-protocol matrix from (1) to maximum absolute discrepancy 5.6e-17.

## 9. Firewalls / negative knowledge

COLLINEAR DETERMINISTIC RESET BACKACTION != NEW FIXED-TIME NOISELESS OBSERVABILITY.

PASSIVE SAMPLE RANK DEFECT != RESET-GENERATED RANK RECOVERY in this model.

NOISELESS ROW-SPACE EQUIVALENCE != EQUAL NOISE GEOMETRY.

NOISELESS ROW-SPACE EQUIVALENCE != EQUAL AVAILABLE STORAGE.

NOISELESS ROW-SPACE EQUIVALENCE != EQUAL TERMINAL STATE OR ACTUATION MAP.

WEAK SIGNAL SCALE != AUTOMATIC DIVERGING RELATIVE CONDITION NUMBER.

INVERTIBLE READOUT TRANSFORM != SAME-NOISE PASSIVE EXPERIMENT.

This factorization fails as stated if, for example:
- measurement times are adaptive functions of previous noisy outcomes;
- reset direction or sensor direction changes in a way not captured by one fixed e;
- reset strength/state update depends on the observed noisy value rather than the deterministic premeasurement state;
- the state update is nonlinear or stochastic in a source-native way.

Those are separate branches and are not covered here.

## 10. Prior-art subtraction and claim ceiling

The mathematics is elementary finite-dimensional state-space / causal Volterra elimination. The lower-triangular output transformation is a mature linear-systems mechanism. No mathematical novelty is claimed.

EARNED:
- exact factorization C_s=s(I+sH)^(-1)M;
- rank and kernel equality for every s!=0 at fixed times;
- replacement of INT8's small-s rank-continuation step by a global exact statement;
- explicit linear-in-s singular-value bounds;
- exact reset-to-passive readout equivalence with transformed noise;
- Gaussian covariance/Fisher consequence;
- exact recovery-weight relation in the square full-rank case.

NOT EARNED:
- quantum-instrument equivalence;
- adaptive-protocol equivalence;
- same-noise passive equivalence;
- physical hardware calibration;
- DTC/NCDG transfer;
- novelty;
- canon or EXEC_SIGN.

DISPOSITION:
INT8_WEAK_PROTOCOL_RANK_THEOREM = STRENGTHENED_EXACTLY_FOR_DECLARED_FIXED-e_MODEL.
RESET_GENERATED_OBSERVABILITY_AT_FIXED_TIMES = REJECTED_FOR_DECLARED_MODEL.
RESET_NOISE_GEOMETRY = MATERIAL_AND_SEPARATE.
LT5_SOURCE_MATCHED_TERMINAL_MAP_REQUIREMENT = UNCHANGED.
NO NEW TASK.
