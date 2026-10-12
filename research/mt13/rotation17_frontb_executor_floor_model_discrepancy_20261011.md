# MT13 / temporary Living Theory — Rotation 17
2026-10-11. Noncanon, no EXEC, no PBH/BBN bound, no novelty.

CURRENTNESS: LT3 DRAFT018 remains active. Mech-S6 floor semantics report: (private Drive source; original locator retained in BW) ; XH-S3 Wu-Xu monotonicity: (private Drive source; original locator retained in BW) .

THREE DISTINCT OBJECTS:
(1) intended source-sink physical population n_phys'=S-D n_phys;
(2) executor population n_exec'=alpha(n_exec)S-D n_exec with alpha=min(1,n_exec/epsilon) and epsilon=exp(-100) in internal density units, for the reported log-floor executor;
(3) algebraic DE n_DE=S/D. Agreement between (2) and (3) is not sufficient to validate (1).

EXACT EXECUTOR-TO-INTENDED ERROR (prescribed common S,D and same initial population):
Let e=n_exec-n_phys. Then e'=-D e -(1-alpha(n_exec))S. With e(t0)=0, variation of constants yields
e(t)=-integral_{t0}^t exp(-integral_s^t D(u)du) (1-alpha(n_exec(s)))S(s)ds <=0.
Thus the floor-active executor systematically underestimates the intended population for the same prescribed source and loss rate, and the bias persists after the floor becomes inactive until depletion erases it. The sign conclusion does NOT automatically hold for fully coupled histories with different X_n/background and D.

SOURCE DEFICIT BUDGET:
delta_S(t)=(1-alpha(n_exec(t)))S(t)>=0.
For prescribed branching b(t), compare the two exact physical/executor equations and integrate the error:
int b D (n_exec-n_phys) dt = -[b e]_{t0}^T + int b' e dt - int b delta_S dt.
For weighted q=w b:
int q D (n_exec-n_phys) dt = -[q e]_{t0}^T + int q' e dt - int q delta_S dt.
This is a distinct executor-model error and must not be collapsed into the DE-closure error. Total intended-vs-DE error can be decomposed as (intended-executor)+(executor-DE), using one typed common comparison contract.

BOUND:
If D>=d>0 and common initial population, |e(t)| <= integral_{t0}^t exp(-d(t-s))delta_S(s)ds. In particular integral |e| dt <= (1/d)integral delta_S dt. If q is bounded, the rate-weighted discrepancy can be bounded using D upper bounds or the exact identity with endpoint and q' terms plus integral |q|delta_S. This is an a posteriori residual certificate requiring the actual floor-active trajectory.

LIMITS:
- For the public Wu-Xu code the floor's actual activation in relevant parameter scans is not established; no numerical severity is inferred.
- n_exec=exp(y) versus n_eval=max(n_exec,epsilon) must be kept distinct.
- When S=0, delta_S=0 and the executor equation equals intended depletion; previously accumulated e may still persist.
- Frozen DE root existence/uniqueness from XH-S3 does not validate time-dependent closure or source matching.
- Multispecies feedback changes D and X across trajectories; comparison needs a coupled residual tube, e.g. SW/M12, not this scalar sign argument.
- PBH_B2 transfer, target-weighted Yp/DH, and numerical constraints remain OPEN.

PLACEMENT: P2 REV020_PLUS_COMPILER retained, P3 HOST_ATLAS_ONLY strong fallback, TPE HOLD, DRAFT018 active. No promotion. The meaningful source-native advance is the typed executor-model discrepancy and exact residual propagation, mature ODE host.
