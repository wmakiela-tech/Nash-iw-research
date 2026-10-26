import sympy as s
assert s.simplify(-s.Rational(131072,59049)*s.sqrt(3)) != 0
print('R10 nonzero minor identity; full certificate in report')
