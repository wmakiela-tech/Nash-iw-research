# LT4 ROT04 — de Rham closed-form conjugacy, nonclosed-form failure, boundary gates

Return ID: IW_LT4_ROT04_DE_RHAM_CLOSED_FORM_CONJUGACY_AND_BOUNDARY_GATES_001_20261012
From: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_02 / LT4
Date: 2026-10-12
Status: exact host-level result; independent referee not obtained.
Ceiling: NO_CANON; NO_EXEC_SIGN; NO_NOVELTY; NO_REV021; NO_PHYSICAL_INTERPRETATION.

## 1. Exact theorem

Let (M,g) be a smooth compact, connected, oriented Riemannian manifold **without boundary**. Define Z^k=ker(d:Omega^k -> Omega^(k+1)), and let P_H be the Hodge projection onto harmonic k-forms. Fix c != 0 and put F=I+(c-1)P_H and T_X=L_X F.

For any closed k-form omega, Cartan's formula gives L_X omega=d(i_X omega); hence L_X omega is exact, so P_H L_X omega=0. On Z^k, F is invertible with inverse I+(c^-1-1)P_H. As F L_X=L_X on Z^k, it follows that

    T_X = F^-1 L_X F  on Z^k,
    [T_X,T_Y] = T_[X,Y] on Z^k.

This is an equivalence of existing Lie-algebra representations, not an inequivalent transport. If c != 1 and b_k(M)>0, F is a genuinely nonidentity operator on Z^k despite the exact closure.

Special whole-carrier cases:
- On all Omega^0, P_H projects to constants and L_X P_H=0; thus T_X=L_X, even for nonclosed functions.
- On all Omega^n, every top-degree form is closed. By Cartan and Stokes, integral(L_X omega)=0, giving P_H L_X=0 and T_X=F^-1 L_X F. The top-form transport can differ from L_X but is conjugate.

The intermediate-degree result is only on **closed forms**, not automatically all Omega^k.

## 2. Exact countercontrol: whole Omega^1 on the flat 2-torus

On T^2 with coordinates x,y, let P_H project each coefficient of a 1-form to its mean and let F=I+P_H. Choose

    X=cos(x) d/dx, Y=sin(x) d/dy, omega=sin(x)dy.

Since d omega=cos(x)dx wedge dy != 0, the form is nonclosed. Direct nested calculation, including F at each intermediate step, gives

    L_X omega=cos(x)^2 dy, P_H L_X omega=(1/2)dy;
    L_Y omega=sin(x)cos(x)dx, P_H L_Y omega=0;
    [X,Y]=cos(x)^2 d/dy;
    J_F(X,Y)omega=-(1/2)cos(x)dx != 0.

For the closed form dx, exactly the same test yields J_F(X,Y)dx=0. Hence cohomological closure on Z^1 is not full off-shell closure on Omega^1.

## 3. Boundary flux and source legality

For top-degree omega on M with boundary, Cartan-Stokes yields

    integral_M L_X omega = integral_boundary(M) i_X omega.

If X is tangent to the boundary, its boundary flux vanishes, so the top-form argument can survive: **boundary present does not imply failure**.

For an explicit flux-stress on [0,1], define

    P(u dx)=(integral_0^1 u(s) ds)dx; F=I+P;
    L_(C d/dx)(u dx)=(Cu)'dx.

Taking X=x d/dx, Y=x^2 d/dx, omega=dx gives

    J_F(X,Y)omega=(2-4x)dx.

These X,Y are NOT tangent at x=1 and do NOT generate boundary-preserving diffeomorphisms. The example diagnoses dependence on the admitted vector-field class rather than failure for a legal boundary-preserving process. Tangential fields X=x(1-x)d/dx, Y=x^2(1-x)d/dx have zero top-form boundary flux.

## 4. Entire, zero-free spectral interpolation is mathematically possible but not a physical form factor

On a fixed compact M, the nonnegative Hodge Laplacian Delta_k has discrete positive eigenvalues lambda_j tending to infinity. By Weierstrass factorization, one can construct an entire G with G(0)=1 and G(lambda_j)=0 for every positive eigenvalue. For real a != 0:

    f_a(z)=exp(a G(z))

is entire, zero-free and its spectral action is

    f_a(Delta_k)=I+(exp(a)-1)P_H.

This F is bounded *on the given spectral carrier*, regardless of off-spectrum growth of f_a. The construction is **spectrum- and background-tailored**, not a universal admissible form factor.

A decisive normalization caveat: f_a(0)=exp(a) != 1. If the scientific contract requires f(0)=1, this nonidentity harmonic modification is forbidden; in this family c=1 forces F=I. Entire functions can still be nonconstant off spectrum while acting as the identity operator.

No Lorentzian/causal/ghost-free interpretation follows.

## 5. Deterministic checks

Source stored alongside this note:
research/LT4/lt4_rot04_exact_controls.py

Executed with SymPy, assertions passed; output:
    T2 non-closed 1-form residual: (-cos(x)/2, 0)
    T2 closed 1-form residual: (0, 0)
    T2 top-form residual: 0
    T2 top form constant input transformed: -2*sin(x)
    Interval non-tangential boundary stress residual: 2 - 4*x
    Tangential vector field fluxes: 0, 0
    EXACT_CONTROLS_PASS

These checks corroborate the explicit examples but are not an independent external referee.

## 6. Mature-host subtraction and placement

The mechanisms are standard Cartan formula, de Rham/Hodge decomposition, Stokes, ordinary conjugacy, and Weierstrass products. Background sources:
- Cartan identity: https://webspace.science.uu.nl/~crain101/manifolds-2022/DG-2022-Chp-1-4.pdf
- Stokes/top-form check: https://math.stackexchange.com/questions/4554798/do-we-have-int-m-mathcal-l-x-omega-0-for-m-form-omega
- Weierstrass products: https://mathworld.wolfram.com/WeierstrassProductTheorem.html

This is a scoped correction candidate to the blanket NC J3 002/005 claim that closing T_X=L_Xf(Delta) must require independent commutation and idempotence, or that no nontrivial entire f could ever close. The **operator-algebra identity** in NC can remain correct while those universal necessity inferences fail.

However, NC's measured nonclosure for its tensor setup and exp(a Delta) is not refuted. The present construction uses a compact Euclidean carrier, cohomologically restricted domains or endpoint degrees, and often f(0)!=1. It cannot be transferred to the project's physical tensor or Lorentzian sectors without independent source-native proof.

LT currentness remains as last verified: DRAFT018 / REV020_PLUS_COMPILER; P3 fallback; TPE HOLD; T2 NOT RUN; H8R-C OPEN; Front B source admission OPEN; REV021 not created. No canonical documents modified.

END LT4 ROT04.
