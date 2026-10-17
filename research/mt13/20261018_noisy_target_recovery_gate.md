# MT13 bounded-noise target recovery

2026-10-18 | Standard optimal recovery, no novelty or EXEC.

For real Euclidean y with norm <=R, target m^T y, measurement z=Cy+eta with norm eta<=delta, the exact minimax scalar error is sup{abs(m^T v): norm(v)<=R, norm(Cv)<=delta}. It also equals inf_w [R norm(m-C^T w)+delta norm(w)], achieved by a linear estimator w^T z. The equality follows from symmetric indistinguishable preparations and convex minimax duality. Normalization of sensor C and noise delta is required for meaningful instrument comparison.

For R=1, m=(1,1), C=(1,0), delta=.2, risk is .2+sqrt(.96)=1.179795897. Numerical primal and dual checks passed locally.

Mature hosts: Micchelli-Rivlin optimal recovery, Donoho Statistical Estimation and Optimal Recovery (1994), Instances of computational optimal recovery (2020, doi 10.1016/j.jco.2020.101503). Scope: deterministic, no sample-law or physical measurement claim. LT4 book integration remains with LT4.