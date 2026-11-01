All numbers below include exactly TWO fresh sensor shots per pair, free Delta=.5 per shot, source ON during prep and X/Y analysis; detector and sensor reset time explicitly EXCLUDED in both. Since selecting Z needs no analysis pulse, pair duration depends on the random axis. Use worst-case deterministic and expectation over fair independent pair axis coins separately.

| Source-on control | P_X/P_Y/P_Z | N pairs at certified errors | Worst time per pair gamma*T | Expected time per pair gamma*T | Worst total gamma*T | Expected total gamma*T |
|---|---|---:|---:|---:|---:|---:|
| Rectangular pi/2 | .18/.20/.62 | 1075 | 1.628318531 | 1.433539786 | **1750.4424** | **1541.0553** |
| Composite CORPSE pi/2 | .18/.20/.62 | 1134 | 6.076679378 | 4.502908771 | **6890.9544** | **5106.2985** |
| R22 baseline rectangular, equal XYZ | 1/3 each | 3300 | 1.628318531 | 1.523598776 | **5373.4512** | **5027.8759** |

The weighted rectangular protocol is **3.07 times** more economical in CERTIFIED worst-case total duration than R22's equal-weight protocol. The weighted CORPSE protocol consumes **3.94 times** as much certified worst-case time as weighted rectangle. These are source/control/estimator-SPECIFIC comparisons, not universal bounds on quantum detection cost.

Physical time and gate budget subtlety: each pair's actual duration varies with basis; a guarantee on static xi holding across both shots must cover the LONGEST actual pair. A fixed source persistence time shorter than this breaks the source-A contract. Readout and reset deadtimes, SPAM, hidden-dependent drift, finite detector and nonideal Z detection are not included. Any additional positive per-pair deadtime costs `N*t_dead` and cannot be silently omitted when assessing hardware. A randomized total observation clock is not a uniform hard deadline; the worst-case total is the deterministic upper bound.

## 6. Independent reproducibility, falsifiers, and authority

