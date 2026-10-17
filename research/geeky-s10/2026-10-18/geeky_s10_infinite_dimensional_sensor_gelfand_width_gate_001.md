# Geeky-S10 — Infinite-dimensional hidden-state sensor Gelfand-width gate

RETURN_ID: GEEKY-S10-MT13-INFINITE-DIMENSIONAL-SENSOR-GELFAND-WIDTH-GATE-001  
DATE: 2026-10-18  
STATUS: PASS_EXACT_MATURE-HOST / MT13_FINITE_DIMENSIONAL_CAVEAT_RESOLVED_AT_ABSTRACT_HILBERT_LEVEL / NO_SENSOR_ADMISSION / NO_PHYSICAL_UPGRADE / NO_CANON / NO_EXEC_SIGN  
BW_INGESTION_STATUS: PENDING

Private Drive durable copy exists; private locator intentionally omitted from this public scientific body.

## Fixed finite-rank measurement theorem

Let Y,Z be Hilbert spaces, M in B(Y,Z), ||y||<=R, and let L:Y->F^k be any bounded finite-rank exact noiseless measurement.

Define

E_R(L;M)
=
inf_a sup_{||y||<=R} ||My-a(Ly)||.

Then exactly

E_R(L;M)
=
R ||M|_{ker L}||.

The lower bound comes from indistinguishable opposite states ±v in ker L. The upper bound uses the orthogonal minimal-norm lift from (ker L)^perp.

## Free rank-k optimum

With Gelfand-number convention

c_n(M)
=
inf {
||M|_V|| :
V closed,
codim V < n
},

one has exactly

inf_{rank L<=k} E_R(L;M)
=
R c_{k+1}(M).

No compactness is required.

## Finite-dimensional and compact recovery

In finite dimensions:

c_{k+1}(M)=sigma_{k+1}(M),

recovering MT13.

For compact operators between Hilbert spaces:

c_{k+1}(M)=s_{k+1}(M),

so

inf E_R
=
R s_{k+1}(M),

attained by measuring the first k right singular directions.

## Noncompact obstruction

For M=I on an infinite-dimensional Hilbert space,

c_{k+1}(I)=1

for every finite k.

Hence

inf_{rank L<=k} E_R(L;I)=R.

So a finite number of exact noiseless sensors can buy literally no minimax improvement.

FINITE SENSOR RANK != NONTRIVIAL WORST-CASE IMPROVEMENT AUTOMATICALLY.

## Exact zero-risk attainability

A rank-k measurement achieves zero risk iff

ker L subseteq ker M.

Such an L exists with rank <=k iff

codim ker M <= k,

equivalently M has finite rank <=k.

Thus infinite-rank target maps cannot be made exactly known by one fixed finite sensor budget.

## Target effective sensor dimension

For tolerance tau define

d_tau(M;R)
=
inf {
k>=0 :
c_{k+1}(M) <= tau/R
}.

This is a target-relative width count, not an ambient hidden-state dimension.

For compact M it is controlled by singular-value decay.

For the infinite-dimensional identity and tau<R, it is infinite.

## Legal access remains a constrained-width problem

If admissible sensors have form

L=HC

for fixed accessible channel C:Y->W, then

ker C subseteq ker(HC)

and therefore

E_R(HC;M)
>=
R ||M|_{ker C}||.

The exact constrained optimum is

inf_{rank H<=k}
R||M|_{ker(HC)}||,

which need not equal the free Gelfand number.

FREE-SENSOR WIDTH != LEGAL-ACCESS WIDTH.

## LT4 endpoint target

For

M_T=GP S(T)J_Y,

the free k-sensor endpoint optimum is

R c_{k+1}(M_T).

Only if M_T is compact may this be written as

R s_{k+1}(M_T).

BOUNDED ENDPOINT MAP != DISCRETE SINGULAR-VALUE LADDER AUTOMATICALLY.

## LT4 history target

Define

mathcal M_T:Y->L^2([0,T];Z),

(mathcal M_T y)(t)=M(t)y.

Then

mathcal M_T^* mathcal M_T
=
W_T
=
integral_0^T M(t)^*M(t) dt.

Thus

no-sensor history risk
=
R||W_T||^{1/2},

and with k unrestricted exact sensors,

inf E_hist,k
=
R c_{k+1}(mathcal M_T).

If mathcal M_T is compact, equivalently W_T compact positive,

inf E_hist,k
=
R sqrt(lambda_{k+1}(W_T)).

Optimal history sensors are the leading Gramian eigenvectors in this compact setting.

ENDPOINT-OPTIMAL SENSOR DIRECTIONS != HISTORY-OPTIMAL SENSOR DIRECTIONS AUTOMATICALLY.

## Disposition

MT13_FINITE_DIMENSIONAL_SENSOR_THEOREM = EXTENDED_EXACTLY_TO_HILBERT_GELFAND_WIDTH_FORM.  
COMPACT_CASE = SINGULAR_VALUE_RECOVERY.  
NONCOMPACT_CASE = WIDTH_FORM_REQUIRED.  
FINITE_SENSOR_RANK_MAY_BUY_NOTHING = EXACT_IDENTITY_WITNESS.  
HISTORY_SENSOR_DESIGN = GRAMIAN_WIDTH / EIGENVALUE_FORM_IF_COMPACT.  
LEGAL_ACCESS = SEPARATE_CONSTRAINED_WIDTH.

Mature host: optimal recovery / Gelfand numbers / compact-operator singular values / observability Gramians.

NO novelty / NO canon / NO EXEC_SIGN / NO NEW TASK.
