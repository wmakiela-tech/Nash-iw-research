# PRF11 rotation 007 — Target error bounds
Status: conditional mathematical derivation, not PBH numerical validation; NO_CANON / NO_EXEC_SIGN / NO_NOVELTY.
Consider x'=f(t,x,u), Y=Phi(x(tf)), two inputs u_F,u_D, common initial state. Assume f is Lipschitz in state and input on a region containing both trajectories with integrable bounds L_x(t),L_u(t); Phi is Lipschitz with constant L_Phi. Standard Gronwall gives:
|Y_D-Y_F| <= L_Phi integral_{t0}^{tf} L_u(s) ||u_D(s)-u_F(s)|| exp(integral_s^{tf} L_x(r)dr) ds.
This is a conditional finite-perturbation bound, often conservative in stiff networks; constants are not validated for PBH/BBN.
If differentiable, adjoint -p'=D_x f(t,x_F,u_F)^T p, p(tf)=grad Phi(x_F(tf)); first-order delta Y = integral p(t)^T D_u f(t,x_F,u_F) delta u(t) dt. Linear sensitivity, rigorous global error bounds, and direct full-versus-reduced receiver simulations are different evidence levels. No universal model-independent hadron error threshold ensures accuracy of all final BBN observables.
