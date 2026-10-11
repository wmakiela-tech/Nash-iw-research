# MT13 Rotation 16 — Front B weighted yield error bound

Date: 2026-10-11. NONCANON / NO EXEC / NO NOVELTY.

Correction to rotation 15: LT3 DRAFT017 section 92 explicitly says that endpoint terms are tracked in the general channel identity. The issue is the unqualified abbreviated total-count equality, not absence of endpoints throughout the document.

Let n'=S-Rn on [a,T], S>=0, n(a)>=0 and R(t)>=r>0. Let n_DE=S/R. For a prescribed channel fraction b(t) and response weight w(t), put q(t)=w(t)b(t). Then exact-minus-DE weighted yield is

Delta = integral q(Rn-S) dt = -[qn]_a^T + integral q' n dt.

Positivity and integrated balance imply

integral n dt <= (n(a)+integral S dt)/r.

Hence the rigorous a priori estimate

|Delta| <= |q(T)n(T)| + |q(a)n(a)| + ||q'||_infinity (n(a)+integral S dt)/r.

This estimate does not require a slowly varying source. It does require a strictly positive lower bound on the total loss rate and a prescribed, differentiable q. It is sufficient, not necessary, and can be loose for impulsive sources or small r. For q constant, only endpoints contribute. A better source-specific certificate can retain the exact propagator exp(-integral R) rather than replacing it with r.

Exact solution: n(t)=n(a)exp(-integral_a^t R)+integral_a^t S(s)exp(-integral_s^t R)ds. This gives an exact memory-kernel representation for the weighted error, valid for any integrable nonnegative source and positive rate.

No physical PBH/BBN inference: in state-dependent multi-species channels, q is not prescribed; the effective BBN target may be nonlinear and its response weight is not yet validated. This is mature linear ODE and integration-by-parts mathematics, not new theory.

Source: LT3 DRAFT017 https://docs.google.com/document/d/13j--r76yvVKcwvR2_TvQHGbRLiE2zjuosZ5HJBgqXOc/edit
