# MT13 Rotation 14 — DRAFT016 identification semantics

Date: 2026-10-11. Noncanon; no EXEC; no novelty.

DRAFT016 defines B(theta) as the set of attainable observations after nuisance profiling, and uses equality of B sets as a model equivalence. That is legitimate for an oracle revealing the full attainable set, but does not characterize identification from one realized observation.

Exact counterexample: theta=A or B; target tau(A)=0 and tau(B)=1; nuisance u in [0,1]. Let F(A,u)=u and F(B,u)=1+u. Then B(A)=[0,1] and B(B)=[1,2] are unequal, yet observed y=1 is compatible with both. Thus inequality of behavior sets is insufficient to identify the target from a single record.

Correct set-membership formulation: I(y)={theta: y belongs to B(theta)}. Target identified at y iff tau is constant on I(y). Uniform identification from any exact single record requires disjoint B(theta) and B(theta') for all theta,theta' with different targets. With multiple contexts and shared nuisance, replace B by the admitted joint behavior set J_C(theta), not independently fitted Cartesian products. At finite precision use declared error sets and separation margins. Exact disjointness need not guarantee robust separation when infimum distance is zero.

Recommended repair: preserve equality as FULL-SET equivalence; add realized-record compatibility and target identified sets, and separate full-law identification from one-sample set membership. This is standard partial identification and inverse-problem mathematics, not a new theorem or TPE surplus. EDU1 implication: models with unequal cosmological prediction sets may nevertheless overlap at actual data; discrimination needs nonoverlap with admissible nuisance and finite-precision controls.

Currentness: LT3 DRAFT016, REV020 active, REV021 not created, TPE HOLD. Source: (private Drive source; original locator retained in BW)
