from fractions import Fraction as F
from itertools import product
from math import comb, exp
import numpy as np

# WERYFIKACJA PRF11 R28 par.2 — twierdza, ze TV -> 1 i podaja wzor binomialny.
# MODEL AGREEMENT IS NOT PROOF dziala tez wtedy, gdy ktos poprawia moj wynik na plus.
# Droga NIEZALEZNA: pelna enumeracja sciezek w arytmetyce DOKLADNEJ (Fraction),
# bez korzystania z ich redukcji do Bin(n,p).

P1 = [[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
P2 = [[F(2,3),F(1,3)],[F(1,3),F(2,3)]]

def tv_enum(n):
    """TV praw na sciezkach dlugosci n, pelna enumeracja, arytmetyka dokladna"""
    s = F(0)
    for path in product([0,1], repeat=n+1):
        p = F(1,2); q = F(1,2)
        for a,b in zip(path, path[1:]):
            p *= P1[a][b]; q *= P2[a][b]
        s += abs(p-q)
    return s/2

def tv_binom(n):
    """ich wzor R28.1, tez dokladnie"""
    s = F(0)
    for k in range(n+1):
        s += comb(n,k)*abs(F(1,2)**n - F(1,3)**k * F(2,3)**(n-k))
    return s/2

print("TABELA W1  czy ich wzor binomialny = TV z pelnej enumeracji sciezek (arytmetyka DOKLADNA)")
print("  n    TV enumeracja (dokladnie)      TV wzor R28.1 (dokladnie)      rowne?   wartosc")
for n in [1,2,3,4,6,8,10]:
    a, b = tv_enum(n), tv_binom(n)
    print(f"  {n:<4} {str(a)[:28]:<30} {str(b)[:28]:<30} {'TAK' if a==b else 'NIE':<8} {float(a):.10f}")

print()
print("TABELA W2  moje opublikowane wartosci z ART006 wobec ich wzoru")
moje = {1:0.166667, 2:0.194444, 4:0.280093, 6:0.336634, 10:0.409919, 14:0.477832, 18:0.536399}
print("  n    ART006 (moje)   wzor R28.1      roznica")
for n in sorted(moje):
    print(f"  {n:<4} {moje[n]:<15.6f} {float(tv_binom(n)):<15.6f} {abs(moje[n]-float(tv_binom(n))):.2e}")

print()
print("TABELA W3  ich wartosci dla duzych n — czy odtwarzam")
ich = {18:0.5363986518, 100:0.9123154696, 300:0.9968515105, 1000:0.9999999278}
print("  n      PRF11 podaje     moj wzor (float)   roznica      granica Hoeffdinga 1-2exp(-n/72)")
for n in sorted(ich):
    v = float(tv_binom(n)) if n <= 300 else None
    if v is None:
        # dla n=1000 licz w float, zeby nie meczyc Fraction
        s = 0.0
        for k in range(n+1):
            s += comb(n,k)*abs(0.5**n - (1/3)**k*(2/3)**(n-k))
        v = s/2
    h = 1-2*exp(-n/72)
    print(f"  {n:<6} {ich[n]:<16.10f} {v:<18.10f} {abs(ich[n]-v):<12.2e} {h:.10f}  {'<= TV' if h <= v else 'NARUSZONA'}")

print()
print("TABELA W4  kontrola ich KROKU wyprowadzenia: czy wskazniki przelaczen sa IID Bernoulli")
print("  Twierdza: dla P1 p=1/2, dla P2 p=1/3, niezaleznie od stanu biezacego")
for nm,P in [("P1",P1),("P2",P2)]:
    print(f"  {nm}: P(przelacz | stan 0) = {P[0][1]}   P(przelacz | stan 1) = {P[1][0]}   "
          f"stale: {'TAK' if P[0][1]==P[1][0] else 'NIE'}")
print("  -> wiec F_j IID Bern(p); bijekcja (X0,F_1..F_n) <-> sciezka; X0 jednostajne pod OBOMA")
print("  -> TV sciezek = TV ciagow Bernoulliego, a wiarogodnosc zalezy tylko od K = suma F_j")
print("  Kontrola dostatecznosci K: czy TV po K = TV po pelnym ciagu?")
def tv_bern_full(n):
    s = F(0)
    for f in product([0,1], repeat=n):
        k = sum(f)
        s += abs(F(1,2)**n - F(1,3)**k*F(2,3)**(n-k))
    return s/2
for n in [4,8,10]:
    a,b = tv_bern_full(n), tv_binom(n)
    print(f"  n={n}: TV po pelnym ciagu = {float(a):.12f}   TV po K = {float(b):.12f}   rowne: {'TAK' if a==b else 'NIE'}")
