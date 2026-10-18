import numpy as np
from scipy.linalg import expm

# SWIADEK dla blizniaczej pary §2.9 / §3.5:
# "Rownowaznosc realizacji minimalnych z dokladnoscia do podobienstwa
#  NIE JEST tozsamoscia wewnetrznej zmiennej fizycznej."
#
# Dwie minimalne realizacje TEJ SAMEJ funkcji przenoszenia, zwiazane podobienstwem T.
# Obserwabla ukryta zadana TYM SAMYM WZOREM w obu ukladach wspolrzednych ("pierwsza
# wspolrzedna ukryta") ma ROZNE trajektorie, mimo ze cale dane wejscie-wyjscie sa rowne.
# Dodatkowo: dla realizacji minimalnych podobienstwo jest JEDNOZNACZNE, wiec nie da sie
# tego naprawic innym wyborem T.

D1 = np.diag([-1.0,-2.0])
C1 = np.array([[1.0],[1.0]])        # wejscie  (skalarne) -> Y
B1 = np.array([[1.0, 1.0]])         # Y -> wyjscie (skalarne)

T  = np.array([[1.0, 1.0],[0.0, 1.0]])      # odwracalne, nietrywialne
Ti = np.linalg.inv(T)
D2 = T@D1@Ti;  C2 = T@C1;  B2 = B1@Ti

def K(B,D,C,t): return float((B@expm(t*D)@C).item())

print("TABELA T1  ta sama funkcja przenoszenia: K(t) = B e^{tD} C")
print("  t      K_1(t)               K_2(t)               |roznica|")
for t in [0.0,0.25,0.5,1.0,2.0,4.0]:
    k1,k2=K(B1,D1,C1,t),K(B2,D2,C2,t)
    print(f"  {t:<6.2f} {k1:<20.15f} {k2:<20.15f} {abs(k1-k2):.3e}")

print()
print("TABELA T2  minimalnosc obu realizacji (rangi Kalmana)")
def ctrb(D,C): return np.hstack([np.linalg.matrix_power(D,k)@C for k in range(2)])
def obsv(B,D): return np.vstack([B@np.linalg.matrix_power(D,k) for k in range(2)])
for nm,(B,D,C) in [('realizacja 1',(B1,D1,C1)),('realizacja 2',(B2,D2,C2))]:
    print(f"  {nm}: rank osiagalnosci = {np.linalg.matrix_rank(ctrb(D,C))}, "
          f"rank obserwowalnosci = {np.linalg.matrix_rank(obsv(B,D))}")

print()
print("TABELA T3  obserwabla ukryta zadana TYM SAMYM wzorem s(y) = y_1")
print("  stan poczatkowy y(0) = C (odpowiedz na impuls jednostkowy)")
print("  t      s(y_1(t)) real.1     s(y_2(t)) real.2     |roznica|")
for t in [0.0,0.25,0.5,1.0,2.0,4.0]:
    y1=expm(t*D1)@C1; y2=expm(t*D2)@C2
    print(f"  {t:<6.2f} {y1[0,0]:<20.15f} {y2[0,0]:<20.15f} {abs(y1[0,0]-y2[0,0]):.6f}")

print()
print("TABELA T4  jednoznacznosc podobienstwa miedzy realizacjami minimalnymi")
# S musi spelniac S D1 = D2 S, S C1 = C2, B1 = B2 S. Rozwiazuje uklad liniowy.
import itertools
A_eq=[];b_eq=[]
for i in range(2):
    for j in range(2):
        row=np.zeros(4)
        for a in range(2):
            row[2*i+a]+=D1[a,j]
            row[2*a+j]-=D2[i,a]
        A_eq.append(row); b_eq.append(0.0)
for i in range(2):
    row=np.zeros(4)
    for a in range(2): row[2*i+a]+=C1[a,0]
    A_eq.append(row); b_eq.append(C2[i,0])
for j in range(2):
    row=np.zeros(4)
    for a in range(2): row[2*a+j]+=B2[0,a]
    A_eq.append(row); b_eq.append(B1[0,j])
A_eq=np.array(A_eq); b_eq=np.array(b_eq)
sol,res,rk,sv=np.linalg.lstsq(A_eq,b_eq,rcond=None)
S=sol.reshape(2,2)
print(f"  rank ukladu = {rk} z 4 niewiadomych  ->  rozwiazanie {'JEDNOZNACZNE' if rk==4 else 'NIEJEDNOZNACZNE'}")
print(f"  S = {np.round(S,12).tolist()}   T = {T.tolist()}   ||S-T|| = {np.linalg.norm(S-T):.3e}")
print(f"  residuum ukladu: {np.linalg.norm(A_eq@sol-b_eq):.3e}")

print()
print("TABELA T5  czy jakiekolwiek podobienstwo przenosi obserwable s(y)=y_1 ?")
s1=np.array([[1.0,0.0]]); s2=np.array([[1.0,0.0]])
print(f"  warunek zgodnosci to s_2 o S = s_1")
print(f"  s_2 S = {np.round(s2@S,12).tolist()}    s_1 = {s1.tolist()}")
print(f"  ||s_2 S - s_1|| = {np.linalg.norm(s2@S-s1):.6f}")
