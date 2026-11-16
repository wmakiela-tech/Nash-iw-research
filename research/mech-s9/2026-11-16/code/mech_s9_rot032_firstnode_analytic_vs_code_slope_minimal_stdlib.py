#!/usr/bin/env python3
"""ROT032 original Wu-Xu source-only analytic-vs-DataInterpolations slope.
No Julia, BlackHawk, BBN integration. Exact first 2 tabulated source nodes,
source frozen d395183674cace6c9906a8911bdeb7234ba4040d,
rate table Git blob 06d0883a27b108692720422294ba2baacd381a64,
original interpolation Git blob cc73432910f872d526113ce59b6204f38d0766a9.
DOI 10.1088/1475-7516/2026/02/063, section 4.1 equation 4.5.
"""
import math
from decimal import Decimal,localcontext
M0=Decimal("5.609588603804452e32")
M1=Decimal("6.099798045788406e32")
R0=tuple(map(Decimal,("489105.5126008581","59105.93631247951",
 "29086.774913348447","34849.08026691193","34656.17773724596")))
R1=tuple(map(Decimal,("442306.73787501804","53467.712852971126",
 "26311.795859614824","31504.591028094237","31328.963561830213")))
CHANNELS=("pipm","Kpm","K0L","proton","neutron")
with localcontext() as ctx:
 ctx.prec=75
 slopes=[float(ctx.ln(b/a)/ctx.ln(M1/M0)) for a,b in zip(R0,R1)]
for ch,s,a,b in zip(CHANNELS,slopes,R0,R1):
 assert math.isclose(float(a)*(float(M1/M0)**s),float(b),rel_tol=5e-14)
 print(f"{ch}: original low-end slope k={s:.15f}; code/paper at M=1e8g: "
       f"{(0.1**(s+1.3)):.13f}; at last recorded live M=1.44891220526512e8g: "
       f"{((1.44891220526512e8/1e9)**(s+1.3)):.13f}")
 assert -1.21<s<-1.19
print("SOURCE_FIRST_TWO_NODES_M_MINUS_1_3_CONTRAST_PASS; no native solver.")
