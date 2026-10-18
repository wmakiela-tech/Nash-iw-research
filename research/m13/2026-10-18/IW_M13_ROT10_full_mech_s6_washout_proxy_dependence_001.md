# IW / M13 — ROT10: washout-or-compensation gate and duplicate-proxy readout in Wu–Xu charge-map comparator


**RETURN_ID:** `M13-ROT10-FRONTB-MECHS6-TRAJECTORY-TO-ENDPOINT-WASHOUT-OR-COMPENSATION-AND-PROXY-DEPENDENCE-001_20261018`  
**DATE / CELL:** 2026-10-18 / `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08` (M13)  
**RESULT CLASS:** exact arithmetic applied to one pinned Mech-S6 diagnostic; conditional two-state consequence; mature-host subtraction.  
**AUTHORITY:** NOT a rerun of the Wu–Xu executor, NOT an independent physical endpoint, NOT an external referee. `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`.


## 1. Source currentness / anti-rediscovery


The **Mech-S6 dynamic charge-map comparator** ran two pinned variants at initial PBH mass `6e9 g`, beta `1e-16`, using the same public v2 helper and differing only in the aggregate-source-to-charge map. Reported values:


- at a sampled peak difference `t*=5.06095 s`, `T≈0.393875 MeV`, `M≈5.79601e9 g`, `X_exec≈0.416505` and `X_sym≈0.343653`; hence `delta(t*)=X_sym-X_exec≈-0.0728514990`;
- at the diagnostic endpoint `Y_exec=1.3230817938392783`, `Y_sym=1.3177406564166434` under the Wu–Xu **reduced proxy** `Y=2X/(1-X)`.


The Mech-S6 result already states that `Y>1` is not a physically admissible helium mass fraction, that subedge solver evaluations are not excluded by zero sampled subedge points, and that no modern Yp/D-H or PBH bound has been established. This ROT10 retains every guard.


The LT4 monograph, **Chapter 6, Theorem 6.6 / Eq. (6.8)**, already provides the exact two-state difference Duhamel identity. ROT10 is **not** a new mathematical theorem: it applies that identity to the specific numerical disparity reported by Mech-S6 and supplies a minimal binary falsification criterion for its interpretation. MT13 and Mech-S6 retain scientific ownership; no manuscript prose is proposed.


## 2. Exact endpoint/proxy dependency (no independent second outcome)


For the *declared reduced-executor proxy* `Y=2X/(1-X)`, inversion and the secant identity are purely algebraic:


```text
X=Y/(2+Y)
Y(X_1)-Y(X_0) = 2(X_1-X_0) / [(1-X_1)(1-X_0)]
```


Using the Mech-S6 outputs as given, with decimal arithmetic:


```text
X_exec_end = 0.39814903030438903756...
X_sym_end  = 0.39718012734602391457...
delta_end = -0.00096890295836512298...
Y_sym_end - Y_exec_end = -0.0053411374226349  (EXACT with reported decimal inputs)
abs(delta_end)/0.0728514990 = 0.01329969831321004...
```


Thus the numbers `delta_X_end` and `delta_Y_proxy_end` are **not independent experimental or computational support** for the source-map repair. They are the same endpoint state under a deterministic, invertible scalar readout. This says nothing about a true complete-network Yp observable. The source-reported `Y>1` further bars physical reinterpretation.


## 3. Exact post-peak washout-or-compensation identity


For any two legal trajectories `x_0` (current literal executor) and `x_1` (charge-symmetric comparator) on a common time interval with the same clock and a valid **two-state neutron-fraction equation**


```text
x_i'(t) = A_i(t)[1-x_i(t)] - B_i(t)x_i(t),
A_i(t)>=0, B_i(t)>=0,
```


where each `A_i,B_i` is the full **realized directional rate** for that trajectory (including any separately represented baseline transitions), put


```text
delta=x_1-x_0
DeltaA=A_1-A_0; DeltaB=B_1-B_0
R_1=A_1+B_1
W(t)=(1-x_0(t))*DeltaA(t)-x_0(t)*DeltaB(t).
```


Subtraction gives `delta'=-R_1 delta+W`. Therefore on `[t*,T]` exactly:


```text
delta(T)=exp(-D)*delta(t*)+I,
D=int_{t*}^T R_1(u)du >=0,
I=int_{t*}^T exp[-int_s^T R_1(u)du]*W(s)ds.
```


This identity is **exact even if the hadron populations and rates depend nonlinearly on the actual neutron trajectory**; the realized histories must satisfy the displayed two-state form. It is not a first-order linearization, but nor does it guarantee that *the real, full nucleosynthesis network* admits a scalar two-state reduction.


Insert the reported signs `delta(t*)=-p`, `delta(T)=-d`, with


```text
p=0.0728514990,
d=0.0009689029583651229846...,
I(D)=p*exp(-D)-d.
```


Consequences:


1. If the **weighted post-peak forcing difference is nonpositive**, `I<=0`, then `D>=ln(p/d)=4.320013927228987`. (This is a **conditional necessary threshold**, not a measured integrated rate.)
2. If `D<4.320013927228987`, then necessarily `I>0`: the weighted difference in directional rates **compensates** some of the earlier negative neutron-fraction discrepancy.
3. At equality, `I=0`; if `D` exceeds this threshold, the net weighted difference `I<0` is in the *same negative direction* as the earlier discrepancy, while stronger damping makes the final discrepancy small.
4. A large transient error followed by a small endpoint **does not logically establish signed cancellation**. Strong washout alone can do this. Nor does small endpoint difference establish source-map equivalence or physical accuracy.


For illustration only, if independently measured `D=2`, then `I` would have to be approximately `+0.0088904752930` neutron-fraction units. No value of `D` or `I` was recovered from the public solver in this rotation.


## 4. The smallest correct readout contract (no task cascade)


To distinguish these explanations **within the pinned diagnostic**, the needed information is the already-defined realized total rates `A_0,B_0,A_1,B_1` over times between `t*` and the executor endpoint, together with `x_0,x_1`. Compute `D`, the signed integral `I`, and independently verify the equality `delta(T)-exp(-D)*delta(t*)-I=0` to solver tolerances. This is a **certificate specification**, not a new assigned mission, and not a claim that this instrument was run.


Only after such an internal scalar-model diagnostic can interpretation be attempted. It does not validate the below-`1e9g` Wu–Xu source, the paper-vs-public code lineage, complete primordial nucleosynthesis, or any modern `Y_p`/D/H bound.


## 5. Claim typing / source references


- **EARNED EXACT:** invertible relation between the reduced proxy and the endpoint `X_n`, computed numerical ratio, conditional integrated relaxation threshold and sign dichotomy from an established scalar identity.
- **NOT EARNED:** measurement of post-peak integrated relaxation; attribution to actual damping or compensation; correctness of solver history; physical helium yield; published JCAP reproduction; any PBH abundance limit.
- **MATURE HOST:** scalar linear nonautonomous difference equation / variation of constants; LT4 Chapter 6 Theorem 6.6. **No novelty claim.**
- **Mech-S6 source (pinned return):** https://github.com/wmakiela-tech/Nash-iw-research/blob/c133d23cd96d94e3d8d349b5c6364ae342d21efc/research/mech-s6/2026-10-18/mech_s6_frontb_wuxu_charge_map_dynamic_comparator_result_001.md
- **LT4 source monograph (Chapter 6, Theorem 6.6):** https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit
- **XH-S3 harvest026 — distinct paper-vs-code source-contract:** https://docs.google.com/document/d/1UX9zEyq008k0xrKtyBun-kcIivKWVFUNmzuvHWRh2Kk/edit
- **M13 ROT08 — joint source-map/exponent algebra:** https://github.com/wmakiela-tech/Nash-iw-research/blob/13922ec7d481677b11d7cab3a34e4f932c40e389/research/m13/2026-10-18/IW_M13_ROT08_frontb_joint_source_exponent_charge_map_001.md


`ROUTE_TAGS: IWTO_MODERATOR IWTO_MECH_S6 IWTO_LT4 IWTO_MT13 IWTO_REC9 IWTO_XH_S4 IWTO_INT7 IWTO_SW`


`REV020 ACTIVE / REV021 NOT_CREATED / TPE HOLD / P2 REV020_PLUS_COMPILER / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_NEW_TASK`.