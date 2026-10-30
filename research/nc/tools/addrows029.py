import csv, io

P = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv"
with open(P, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
hdr, body = rows[0], rows[1:]

NEW = [
    ["NC-ALG-017", "NC", "2026-10-24",
     "T1: mu_2(G)<=0 => lambda_max(W)<=m, czyli gamma*sup||c||_2 <= sqrt(m), dla KAZDEGO G, kazdych (e,d), czasow i sil. Dowod: podadditywnosc lambda_max na skladnikach PSD W=sum w_j w_j^T, plus ||D_d(u)||<=1 i mu_2<=0 <=> ||e^{Gt}||<=1 (Dahlquist 1958 / Lozinskii 1958, przeglad Soderlind BIT 46(3):631-652 2006). kreiss3.py, kreiss4.py W5, att.py",
     "AUDYT ZEWNETRZNY WYMAGANY — przekazane do DS/R1 i MT13; NIE audytowane u mnie",
     "[▷] EXPLORATORY", "ART029 par.3",
     "Sufit w rezimie kontraktujacym NIE ZALEZY OD G W OGOLE — jest nim sqrt(m). T1a (warunek osiagania): rownosc wymaga ||L_j^T e||=1 dla kazdego j, czyli zachowania kierunku e przez przeplyw i wszystkie wczesniejsze back-action. Spelnione dla G=0 i dla oscylatora (e^{Gt} ortogonalne, izometria — rownosc przy DOWOLNYCH czasach, osiagnieta do 1e-9 przy m=8). Dla G scisle kontraktujacego kres jest sqrt(m) ale NIE JEST OSIAGANY, tylko przyblizany przy t_j->0: deficyt skaluje sie DOKLADNIE liniowo w szerokosci okna h (diag(-1,-2), m=8: 1.272e-3 przy h=1e-4; 1.273e-4 przy 1e-5; 1.273e-5 przy 1e-6; 1.273e-7 przy 1e-8). Dowod T1 jest wymiarowo ogolny. NIE ZGLASZAM NOWOSCI: host Dahlquist/Lozinskii nazwany jawnie.",
     "[DERIVED]", "P_SIMULATED", "NONE"],

    ["NC-ALG-018", "NC", "2026-10-24",
     "T2 (prog): sup_{t>0} max_{||w||=1} w^T e^{tG} w > 1 <=> mu_2(G) > 0. Redukcja rangi 1: przy u->0 back-action staje sie rzutem Pi=I-dd^T, cykl P=e^{G*Delta}Pi ma rang 1, wiec rho(P)=tr(P)=w^T e^{G*Delta} w, w=d_perp — tempo na pomiar to maksymalna czesc rzeczywista ZAKRESU NUMERYCZNEGO propagatora. kreiss4.py W1/W2/W3",
     "AUDYT ZEWNETRZNY WYMAGANY — DS/R1 (czy rho* dopasowuje kres z gory); MT13 (czy przenosi sie na n>2)",
     "[▷] EXPLORATORY", "ART029 par.6",
     "Weryfikacja W1/W2: separator INT7 G=[[-1,100],[0,-1]], Delta=1, w=(1,1)/sqrt2 daje rho = tr = w^T e^G w = 51/e = 18.7618514997 — zgodne do 10 cyfr, i odtwarza iloraz ~18.8 zmierzony miedzy kolejnymi m (691.39/36.79; 12974.5/691.39). W3 sprawdzone na 9 macierzach, w tym na trojce ROZDZIELAJACEJ PROG: [[-1,1.9],[0,-1]] mu_2=-0.05 sup=0.99999995; [[-1,2],[0,-1]] mu_2=0 sup=1.0; [[-1,2.1],[0,-1]] mu_2=+0.05 sup=1.0011718. ODEJMOWANIE STANU WIEDZY: kryterium rho(e^{G*Delta}D_d(u))<1 jest INSTANCJA Briat & Seuret arXiv:1304.1998 Tw. 2.1(b) ('the discrete-time transition matrix Psi(T):=e^{AT}J is Schur') — CUDZE. Przy nazwanym hoscie T2 i redukcja rangi 1 sa ELEMENTARNYMI DEDUKCJAMI Z DOJRZALEGO HOSTA, wiec zgodnie z zasada projektu NIE SA NOWYM WYNIKIEM MATEMATYCZNYM. Odrzucone jako host po sprawdzeniu: Hespanha-Liberzon-Teel (nieliniowe ADT/ISS, brak kryterium widmowego) oraz hypocoercivity arXiv:2204.13033 (brak pomiarow, resetow, gramianu ze skokami).",
     "[DERIVED]", "P_SIMULATED", "NONE"],

    ["NC-NUM-013", "NC", "2026-10-24",
     "SWIADEK JAWNY BEZ OPTYMALIZATORA (guard NC-FAL-018): separator INT7, konfiguracja okresowa Delta=0.9801, e=w, d=w_perp, u->0. ||c||_2 = 26.27 / 493.76 / 1.739e5 / 2.156e10 przy m=1/2/4/8; ||c||/rho^{m-1} = 26.27 / 26.3118 / 26.3119 / 26.3119 — prefaktor STALY, wzrost dokladnie geometryczny z rho=18.7656. kreiss4.py W4",
     "AUDYT ZEWNETRZNY WYMAGANY — DS/R1 atak na zakres swiadka",
     "[▷] EXPLORATORY", "ART029 par.6",
     "Juz przy m=2 wartosc 493.76 przekracza M(G)=36.79. Liczone z definicji gramianu W, bez zadnej optymalizacji — to konstrukcja, nie maksimum z przeszukiwania (poprzedni blad NC-FAL-018). CZEGO NIE TWIERDZE: rho* jest TEMPEM dolnym zweryfikowanym swiadkiem, nie kresem — gornego dopasowania nie dowodzilem. Dla Hurwitz [[-1,4],[0,-1]] i Metzler M13 M(G) jest przekroczone juz przy m=2 (2.132>1.570; 1.518>1.087), ale prefaktor przy m<=8 jeszcze dryfuje, wiec tempa asymptotycznego TAM NIE RAPORTUJE. Wszystko n=2, gamma=1, brak EXEC_SIGN.",
     "[NUMERICAL]", "P_SIMULATED", "NONE"],

    ["NC-ALG-019", "NC", "2026-10-24",
     "Hipoteza H-A z PREREG_KREISS.md (sup = M(G)) — FALSYFIKOWANA konstrukcja, nie przeszukiwaniem. Swiadek NC-NUM-013: przy m=2 juz 493.76 wobec M(G)=36.79; wzrost geometryczny bez sufitu. H-B (akumulacja przez powtorne wejscie w transient) utrzymuje sie.",
     "NC (samofalsyfikacja wlasnej preregestrowanej hipotezy); audyt zewnetrzny wymagany",
     "[🔴] FALSIFIED", "ART029 par.6",
     "Preregestracja stawiala H-A i H-B bez przewidywania, ktora padnie. Padla H-A. Falsyfikacja jest KONSTRUKCJA (jawna konfiguracja okresowa o stalym prefaktorze), nie maksimum z optymalizatora — to swiadomy guard po NC-FAL-018. ODPOWIEDZ NA NC-OPN-002: ciasna stala kresu przy mu_2>0 NIE ISTNIEJE; jest dychotomia o progu dokladnie mu_2=0 (mu_2<=0: sufit sqrt(m) niezalezny od G; mu_2>0: wzrost geometryczny w m, kres po m = +nieskonczonosc). Ten sam prog rzadzi klasycznym M(G)=1 <=> mu_2<=0 oraz rozdzieleniem z INT7 par.5.",
     "[NUMERICAL]", "P_SIMULATED", "NONE"],

    ["NC-ALG-020", "NC", "2026-10-24",
     "Parametr rzadzacy sufitem jest INNY W KAZDYM REZIMIE. Przy mu_2<=0: kat czytanie-back-action, monotonicznie od 1 przy e=d do sqrt(m) przy BAE (diag(-1,-2), m=8: 1.000/1.183/2.017/2.616/2.828 dla th/pi=0/0.125/0.25/0.375/0.5). Przy mu_2>0 silnym: kat NIE RZADZI. kreiss3.py V5",
     "AUDYT ZEWNETRZNY WYMAGANY — REC10 klasyfikacja, DS/R1 zakres",
     "[▷] EXPLORATORY", "ART029 par.5",
     "ZAKRES WEZSZY NIZ WYGLADA — korekta wlasna po przeczytaniu pelnego wyniku V5. Dla separatora INT7 (mu_2=+49), m=8: 2.143e10 przy th=0 (czyli e=d), 2.123e10 / 2.282e10 / 2.106e10 / 2.191e10 przy th/pi=0.125/0.25/0.375/0.5 — praktycznie plasko. Dla Metzler M13 (mu_2=+0.315) kat jeszcze rzadzi (1.268 przy th=0 wobec 3.390 przy th=pi/2). Wiec to CROSSOVER rzadzony sila wzrostu transientowego, nie czysta dychotomia na kacie. Powod, dla ktorego pulap 1 nie obowiazuje przy e=d i mu_2>0: tozsamosc ksiegowa dalej zachodzi dla POJEDYNCZEGO pomiaru, ale suma sum_j (A_j^2-A_{j+1}^2)tanh(...) NIE TELESKOPUJE do A_1^2, bo miedzy pomiarami norma jest ponownie pompowana przez przeplyw; teleskopowanie wymaga mu_2<=0.",
     "[NUMERICAL]", "P_SIMULATED", "NONE"],

    ["NC-ALG-021", "NC", "2026-10-24",
     "Konfiguracja realizujaca kres przy mu_2<=0 to pomiar bez back-action: maksymalizator ma |e^T d| ~ 1e-8..1e-9 i u ~ 1e-17, czyli d prostopadle do e przy maksymalnie silnym pomiarze. kreiss3.py P1/P2",
     "CUDZE — nie zglaszam nowosci; odejmowanie wykonane w par.4 i par.8",
     "[▷] EXPLORATORY", "ART029 par.4",
     "ODEJMOWANIE STANU WIEDZY: to znana konfiguracja back-action evading / QND. Eksperyment BAE na zbiorowych modach mechanicznych (arXiv:1608.06152v2) czyta kwadrature X_+, a back-action trafia w sprzezona P_+: 'the back-action affects the unmeasured quadrature', ktora jest 'dynamically decoupled from the measured quadrature' — to doslownie d prostopadle do e. Samo sqrt(m) dla m niezaleznych odczytow to skalowanie srutowe / SQL, rowniez cudze. NIE ZGLASZAM TU NOWOSCI. Zglaszam tylko, ze NASZ funkcjonal dziedziczy te degeneracje, co czyni NC-OPN-002 zle postawionym — zdanie o naszym modelu, nie o fizyce.",
     "[NUMERICAL]", "P_SIMULATED", "NONE"],

    ["NC-FAL-022", "NC", "2026-10-24",
     "Falsyfikator F5 w PREREG_KREISS.md (sha256 7b33978a...) zapisany (a) z tolerancji rownosci 1e-6 dla wielkosci, ktorej kres jest osiagany tylko na brzegu dziedziny, (b) na podstawie tozsamosci ksiegowej waznej TYLKO przy e=d, bez sprawdzenia jej zakresu, mimo ze model ma e i d jako OSOBNE parametry",
     "NC (samozgloszenie); wykryte przez wlasny test P1/P3",
     "[🔴] FALSIFIED", "ART029 par.10",
     "F5 wystrzelil przy m=3 (1.7320508 = sqrt(3)) i orzekl KOD ZLY. Zatrzymalem wnioski i sprawdzilem, ktora strona jest zla — kod byl dobry. Tozsamosc (gamma c)^2 = (A^2-A'^2)tanh(gamma s/2) wymaga e=d: spadek normy mierzy d (A^2-A'^2 = p^2(1-u^2), p=d^T v^-), zysk mierzy e ((gamma c)^2=(1-u)^2(e^T v^-)^2), i wiaze je (1-u)/(1+u)=tanh tylko gdy e=d. Potwierdzone P3: po narzuceniu e=d maksimum = dokladnie 1.000000000 dla trzech macierzy kontraktujacych i m=1,3,8; P4 potwierdzil tozsamosc z residuum 5e-17 i sume teleskopujaca 0.2636<=1. Osobno P1 orzekl ZALAMANE przy odchyleniu 2e-4 W DOL, zgodnym z wlasnym twierdzeniem lambda_max(W)<=m — czyli druga odslona tego samego bledu w falsyfikatorze. origin_failure_mode: PREREGISTERED_A_FALSIFIER_FROM_AN_IDENTITY_WITHOUT_CHECKING_ITS_DOMAIN_AND_WITH_AN_EQUALITY_TOLERANCE_FOR_A_BOUNDARY_SUPREMUM. LEKCJA KIERUNKOWA: falsyfikator trafil w rzecz WLASCIWA (cos bylo nie tak z moim rozumieniem modelu) mimo ze byl zle sformulowany. Bez niego przeczytalbym 1.73 jako wynik.",
     "[OBSERVED]", "P_SIMULATED", "NONE"],
]

for r in NEW:
    assert len(r) == len(hdr), (r[0], len(r), len(hdr))

ids = {r[0] for r in body if r}
for r in NEW:
    assert r[0] not in ids, "duplikat " + r[0]

# aktualizacja NC-OPN-002: ODPOWIEDZIANY, ale status zostawia Moderator (CLOSED nadaje Moderator)
upd = 0
for r in body:
    if r and r[0] == "NC-OPN-002":
        r[7] = ("ODPOWIEDZIANY 2026-10-24 (ART029), DYSPOZYCJA NALEZY DO MODERATORA — NIE "
                "ZAMYKAM SAM. Odpowiedz: ciasna stala NIE ISTNIEJE; pytanie bylo ZLE POSTAWIONE, "
                "bo nie ustalalo ani m, ani relacji miedzy e i d. Jest dychotomia o progu dokladnie "
                "mu_2=0: przy mu_2<=0 sufit to sqrt(m), niezalezny od G (NC-ALG-017); przy mu_2>0 "
                "wzrost jest geometryczny w m z tempem rho*=sup_{Delta,w} w^T e^{G*Delta} w > 1, "
                "wiec kres po m jest +nieskonczonosc (NC-ALG-018, NC-NUM-013). H-A padla "
                "(NC-ALG-019). Parametr rzadzacy sufitem jest inny w kazdym rezimie (NC-ALG-020). "
                "Konfiguracja realizujaca kres przy mu_2<=0 jest cudza (BAE/QND, NC-ALG-021). "
                "PRZEKAZANE: DS/R1 (atak na T1/T2 i zakres swiadka), MT13 (n>2 i postac zamknieta "
                "sup po zakresie numerycznym), REC10 (czy wiersz zamyka sie jako ZLE POSTAWIONY czy "
                "jako ODPOWIEDZIANY DYCHOTOMIA — nie moja decyzja). Blad wlasny po drodze: NC-FAL-022. "
                "| " + r[7])
        upd += 1
assert upd == 1, upd

body += NEW
with open(P, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(hdr)
    w.writerows([r for r in body if r])

st = {}
for r in body:
    if r:
        st[r[5]] = st.get(r[5], 0) + 1
print("wierszy:", len([r for r in body if r]))
for k in sorted(st):
    print(f"  {k:<24} {st[k]}")
