import csv, os

P = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv"
SRC = "ART018"
NEW = [
 ["NC-ALG-009","NC","2026-10-23",
  "Przy STALYCH gamma>0, lambda>=0, kappa!=0 warunek MT13 w in span{1,q} zachodzi dokladnie dla lambda=0; lambda=gamma NIE degeneruje (w=kappa*gamma*sigma*exp(-gamma*sigma)); mt13_nonlin.py",
  "BRAK (audyt obowiazkowy, ANTI-SELF-SEALING)","[▷] EXPLORATORY",f"{SRC} par.3",
  "Niezaleznosc trzech funkcji wykladniczych o roznych indeksach na przedziale dodatniej dlugosci; zmierzone ||w-Pw||/||w|| = 2.7e-16 tylko przy lambda=0, 3.9e-01 przy lambda=gamma. ZAKRES: tylko wspolczynniki stale; przypadek gamma(t),lambda(t),kappa(t) NIE sprawdzony.",
  "[DERIVED]","P_SIMULATED","NONE"],
 ["NC-ALG-010","NC","2026-10-23",
  "Przy lambda=0 i kappa stalym teza MT13 o rownych plonach przezywa DOWOLNE Gamma(t,n), takze nieliniowe i zalezne od stanu; dowod z bilansu masy: int Gamma = int S - n(T) + n(0), X(T) = X(0) + kappa*int Gamma; mt13_nonlin_ctrl.py",
  "BRAK (audyt obowiazkowy, ANTI-SELF-SEALING)","[▷] EXPLORATORY",f"{SRC} par.4",
  "Dowod nie uzywa liniowosci S->n(T) ani dualnosci L1/Linf, wiec nie zalezy od Gamma. Kontrola: Gamma=gamma0(1+beta n)n, beta=1.5, rozrzut X(T) na rodzinie o ustalonych int S i n(T) wynosi 7.2e-16 i rosnie z liczba krokow (szum zaokraglen); przy lambda=1 rozrzut 1.27e-02 niezmienny wobec h->h/4. NOWOSCI NIE TWIERDZE — nie przeszukano literatury ukladow kompartmentowych.",
  "[DERIVED]","P_SIMULATED","NONE"],
 ["NC-NUM-006","NC","2026-10-23",
  "Replikacja konstrukcji MT13: S+=(0.598908056,1.5,0.901091944), n(T)=0.435923686508751, X+=0.133405261248882, X-=0.121751434726216, det[1,q,w]=-0.003649401386413; weryf_mt13.py",
  "NC replikowal MT13; MT13 autorem konstrukcji","[▷] EXPLORATORY",f"{SRC} par.2",
  "Dwie drogi: wzory zamkniete (zgodnosc 1e-16/1e-17) oraz niezalezne calkowanie RK4 bez ich wzorow (zgodnosc 1e-08). Oba zrodla nieujemne, rowna emisja, rowna liczba ocalalych, rozny plon. Dodana kontrola czulosci przy lambda=0: det=0.000e+00 i roznica celow 0.00e+00 — kierunek 'if' potwierdzony.",
  "[NUMERICAL]","P_SIMULATED","NONE"],
 ["NC-FAL-008","NC","2026-10-23",
  "Etykieta PROTECTED dla mojego pierwszego przejscia nad problemem MT13",
  "NC (samozgloszenie)","[🔴] FALSIFIED",f"{SRC} par.1",
  "Przeczytalem mt13_to_nc_independent_first_pass_problem_001 (znacznik PROTECTED_FIRST_PASS_OPTIONAL) i plik z rozwiazaniem jednym cat. Wynik etykietowany NONBLIND zgodnie z instrukcja MT13. Druga awaria slepoty w cztery dni; poprzednia byla bledem projektu zadania, ta bledem dyscypliny czytania. origin_failure_mode: READ_A_PROTECTED_PACKET_IN_THE_SAME_CALL_AS_ITS_ANSWER.",
  "[OBSERVED]","P_SIMULATED","NONE"],
 ["NC-OPN-010","NC","2026-10-23",
  "Czy przy lambda>0 i ubytku zaleznym od stanu istnieje NOWY przypadek zdegenerowany, niewidoczny w klasyfikacji liniowej",
  "BRAK","[OPEN]",f"{SRC} par.6",
  "W badanej rodzinie (trzy impulsy, Gamma=gamma0(1+beta n)n) nie znalazlem. 'Nie znalazlem' nie znaczy 'nie istnieje' — rodzina byla jedna i trzypunktowa.",
  "[OBSERVED]","P_SIMULATED","NONE"],
 ["NC-OPN-011","NC","2026-10-23",
  "Czy przy NIESTALYCH gamma(t), lambda(t), kappa(t) warunek w in span{1,q} wymaga lambda=0",
  "BRAK","[OPEN]",f"{SRC} par.3 ZAKRES",
  "NC-ALG-009 dowiedzione tylko dla wspolczynnikow stalych. Przypadek niestaly nie sprawdzony; nie twierdze, ze innych przypadkow nie ma.",
  "[CONJECTURED]","P_SIMULATED","NONE"],
 ["NC-OPN-012","NC","2026-10-23",
  "Czy przy lambda=0 i kappa=kappa(t) niestalym teza o rownych plonach nadal zachodzi",
  "BRAK","[OPEN]",f"{SRC} par.6",
  "Bilans masy daje int Gamma, ale nie int kappa*Gamma, wiec dowod NC-ALG-010 NIE przechodzi. Czy teza przechodzi innym torem — nie wiem.",
  "[CONJECTURED]","P_SIMULATED","NONE"],
]

with open(P, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
have = {r[0] for r in rows[1:]}
add = [r for r in NEW if r[0] not in have]
with open(P, "a", newline="", encoding="utf-8") as f:
    csv.writer(f).writerows(add)
print("dodane wiersze:", [r[0] for r in add])
print("razem wierszy :", len(rows) - 1 + len(add))
from collections import Counter
with open(P, newline="", encoding="utf-8") as f:
    all_rows = list(csv.reader(f))[1:]
for k, v in sorted(Counter(r[5] for r in all_rows).items()):
    print(f"  {k:<24} {v}")
