# M12 DRAFT009 faithful-reduction composition gate

RETURN_ID: M12-DRAFT009-FAITHFUL-REDUCTION-COMPOSITION-GATE-001

Let r:X->Y and s:Y->Z be legal reductions.

TARGET:
If tau=tau_Y o r and tau_Y=tau_Z o s, then tau=tau_Z o s o r.
So target faithfulness composes forward.

Converse guard:
tau=tau_Z o s o r only proves faithfulness for that final target. It does not prove that an independently declared intermediate target sigma:Y->S descends through s.

Control: take s constant, sigma(y)=y, final tau constant. Composite target faithfulness passes while sigma descent fails.

PROCESS:
If r Phi=G r and s G=H s, then sr Phi=H sr. Process projectability composes forward.
Converse fails: if sr is constant, the composite is trivially projectable even when r itself is not.

REALIZATION:
With declared redundancy ~X, r is realization-faithful iff r(x)=r(x') implies x~Xx'.
Second-stage faithfulness must be tested on reachable image r(X), with the induced redundancy there.
Global noninjectivity of s outside r(X) is irrelevant.

Compiler rule:
record at each reduction stage
- faithfulness level,
- declared target,
- induced target,
- reachable image,
- process projectability,
- redundancy relation,
- stagewise certificate,
- composite certificate.

Firewalls:
COMPOSITE TARGET FAITHFULNESS != ALL INTERMEDIATE TARGETS FAITHFUL.
COMPOSITE PROCESS CLOSURE != STAGEWISE PROCESS CLOSURE.
TARGET FAITHFULNESS != REALIZATION FAITHFULNESS.
UNQUALIFIED "FAITHFUL REDUCTION" IS UNDER-TYPED.

HOST_RELATION=EXACT_INSTANCE of factorization/projectability/quotient mathematics.
PROJECT_ROLE=CROSS_HOST_COMPILER_RULE.
No novelty; TPE remains thin compiler; REV020 active; REV021 not created.
