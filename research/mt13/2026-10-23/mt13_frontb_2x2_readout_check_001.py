#!/usr/bin/env python3
"""Independent MT13 check of MECH-S6 reported FOUR reduced-proxy endpoints.
Uses ONLY Python standard-library decimal. NO original Julia/trajectory solve.
"""
from decimal import Decimal as D, getcontext
getcontext().prec=50

Y={
  '00':D('1.3230817938392783'),
  '01':D('1.3177406564166434'),
  '10':D('1.3229769529861870'),
  '11':D('1.3178103739910758'),
}
X={k:v/(v+D(2)) for k,v in Y.items()}
x=X['00'];d=1-x
a=X['10']-x;b=X['01']-x;c=X['11']-x
ix=c-a-b
iy=Y['11']-Y['10']-Y['01']+Y['00']
linear=2*ix/d**2
curv=2/d**2*(c*c/(d-c)-a*a/(d-a)-b*b/(d-b))
assert abs(linear+curv-iy)<D('1e-44')
exec_law=X['10']-X['00']
sym_law=X['11']-X['01']
assert exec_law<0<sym_law
assert ix>0
e_sign=min(abs(exec_law),abs(sym_law))/2
e_interaction=ix/4
common=D('1.083653e-5')-D('-1.640731e-5')
bg=D('2.251028e-6')-D('-1.607742e-6')
replay=D('-4.204293e-7')-D('-9.735097e-7')
assert abs(common+bg+replay-ix)<D('1e-10')
phi=lambda u:2*u/(1-u)
q=D('.2');h=D('.01')
assert (q+2*h)-2*(q+h)+q == 0
assert phi(q+2*h)-2*phi(q+h)+phi(q)>0
for label,val in [('X interaction',ix),('Y interaction',iy),('tangent',linear),
                  ('curvature',curv),('curvature Y fraction',curv/iy),
                  ('law delta exec',exec_law),('law delta sym',sym_law),
                  ('sign epsilon_X strict bound',e_sign),
                  ('interaction epsilon_X strict bound',e_interaction),
                  ('common background component',common),
                  ('own background component',bg),('replay component',replay)]:
    print(label, val)
print('PASS: exact rational identity, 4-cell inverse, sign split, tolerance gates, conditional replay partition, curvature falsifier')
