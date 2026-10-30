import csv

P = "/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18/CLAIM_ROWS_NC_20261018.csv"
with open(P, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))
hdr, body = rows[0], rows[1:]

NEW = [
    ["NC-ALG-022", "NC", "2026-10-24",
     "H-SAT: przy kinetyce NASYCONEJ (Gamma(n(t))=Gamma_0 stale na [0,T]) bilans masy ustala nie tylko calke int Gamma, lecz CALY profil: Gamma_0=(int S - Delta n)/T. Stad X(T)=kappa*Gamma_0*(1-e^{-lambda T})/lambda jest wspolne dla KAZDEGO lambda>0, mimo ze waga e^{-lambda(T-t)} nie jest stala. PREREG_SAT.md sha256 4b2cdcf5...; sat.py sha256 af71d888...",
     "AUDYT ZEWNETRZNY WYMAGANY — przekazane do DS/R1, MT13 (sugestia redakcyjna), REC10",
     "[▷] EXPLORATORY", "ART030 par.1 i par.3",
     "ODPOWIEDZ NA NC-OPN-010 JEST TAK. Mechanizm jest INNEGO RODZAJU niz wszystko w klasyfikacji: degeneracja nie przez WAGE, lecz przez ZAWEZENIE ZBIORU DOPUSZCZALNEGO do jednego punktu. WERYFIKACJA w preregestrowanej kolejnosci: F1 kontrola (Gamma liniowe, lambda>0 -> X(T) ROZNE o 8.056e-02 i 3.259e-02, czyli uklad UMIE wykryc roznice); F5 bilans masy reszta 7.3e-11..1.5e-10; F2 nasycenie n_min=9.85 i 8.65 powyzej progu n_s=1, X(T) rowne do 6.3e-15 / 2.8e-14 / 5.3e-14 / 4.6e-14 przy lambda=0.1/0.5/1/3, plus TRZECIE zrodlo o innym ksztalcie do 2.2e-14; F4 zgodnosc z postacia zamknieta do 3.65e-11 (reszta rzedu reszty bilansowej); F3 ANTY-ARTEFAKT DECYDUJACY — przy n(0)=1.6 zrodlo pozne wypycha n ponizej progu (n_min=0.457) i X(T) SIE ROZCHODZI (1.41e-01 przy lambda=0.5; 1.17e-01 przy lambda=1), wiec zgodnosc w F2 pochodzi Z NASYCENIA, nie z podobienstwa zrodel; F6 zbieznosc 8.6e-11 -> 1.5e-12 -> 2.6e-14 z tolerancja. Zrodla C^1 celowo (artefakt kwadratury O(h) przy prostokatnych to moj blad z ART018 par.4b). NIE ZGLASZAM NOWOSCI: kinetyka zerowego rzedu jest podrecznikowa, tresc matematyczna trywialna (na zbiorze jednopunktowym kazdy funkcjonal jest staly); nie znalazlem zlokalizowanego zdania o niezaleznosci plonu wazonego przy zerowym rzedzie, ale BRAK ZNALEZISKA NIE JEST NOWOSCIA.",
     "[NUMERICAL]", "P_SIMULATED", "NONE"],

    ["NC-ALG-023", "NC", "2026-10-24",
     "Ustalenie zakresu: przypadek z NC-ALG-022 NIE JEST kontrprzykladem do twierdzenia MT13 o rownych plonach. Sprawdzone w zrodle (research/mt13/2026-10-23/mt13_nc_active_research_weighted_yield_sufficiency_001.md, wiersz 19) PRZED napisaniem akapitu.",
     "NC (samokontrola zakresu przed zlozeniem)",
     "[▷] EXPLORATORY", "ART030 par.2",
     "Twierdzenie MT13 jest jawnie LINIOWE: w jest zbudowane z gamma(t), lambda, kappa; czesci zalezne od zrodla to int S, int q S, int w S; kierunek 'only if' korzysta z pelnej swobody ZNAKOWANYCH f in L1 z int f = int qf = 0 i konczy dualnoscia L1. Moj przypadek ma Gamma(n)=Gamma_0 NIEZALEZNE OD n powyzej progu, czyli strate NIELINIOWA — poza zalozeniami. Twierdzenie NIE jest naruszone ani niekompletne. Sens 'niewidoczny w klasyfikacji' jest wiec SLABSZY niz brzmialo pierwotne pytanie NC-OPN-010: w modelu nieliniowym NIE MA zadnej wagi w, ktora mozna by przetestowac na przynaleznosc do span{1,q}, bo S -> X(T) nie jest liniowe; test klasyfikacyjny nie daje falszywej odpowiedzi, lecz NIE DA SIE GO POSTAWIC. Zapisuje to jawnie, bo bez otwarcia ich tekstu napisalbym, ze ich iff wymaga kwantyfikatora po zbiorze dopuszczalnym — czyli zaatakowalbym WERSJE SLOMIANA. Do MT13 idzie wylacznie SUGESTIA REDAKCYJNA (jedno zdanie o zakresie), nie zarzut.",
     "[DERIVED]", "P_SIMULATED", "NONE"],

    ["NC-ALG-024", "NC", "2026-10-24",
     "Kryterium poszukiwawcze zamiast pojedynczego przykladu: degeneracje tego typu daje KAZDA kinetyka, ktorej osiagany zakres czyni Gamma(n(t)) stalym. Eksperyment rozdzielajacy: zaburzyc zrodlo tak, by n wyszlo z obszaru nasycenia — jesli X(T) drgnie, kinetyka byla nasycona; jesli nie, degeneracja ma inne zrodlo.",
     "AUDYT ZEWNETRZNY WYMAGANY — DS/R1",
     "[▷] EXPLORATORY", "ART030 par.5",
     "WYJASNIA WLASNA WCZESNIEJSZA PORAZKE: rodzina z pierwotnego triage'u NC-OPN-010 (Gamma=gamma0(1+beta n)n, trzy impulsy) nic nie dala, bo ta kinetyka jest SCISLE ROSNACA w n, wiec nigdy nie jest stala na niezdegenerowanym przebiegu — szukalem w rodzinie, ktora Z KONSTRUKCJI wyklucza mechanizm. To nie byla zla hipoteza, to byl zly zbior poszukiwan. Zapisane jako wzorzec: 'nie znalazlem' w jednej rodzinie parametrycznej nie jest dowodem nieistnienia, jesli rodzina nie byla wybrana tak, by mechanizm dopuszczac. PYTANIE OTWARTE PRZEKAZANE DO DS/R1: czy istnieje mechanizm degeneracji przy lambda>0 NIENASYCONY i NIELINIOWY, tj. taki, w ktorym Gamma(n(t)) nie jest stale, a X(T) i tak sie zgadza.",
     "[DERIVED]", "P_SIMULATED", "NONE"],
]

for r in NEW:
    assert len(r) == len(hdr), (r[0], len(r), len(hdr))
ids = {r[0] for r in body if r}
for r in NEW:
    assert r[0] not in ids, "duplikat " + r[0]

upd = 0
for r in body:
    if r and r[0] == "NC-OPN-010":
        r[5] = "[OPEN]"
        r[7] = ("ODPOWIEDZIANY 2026-10-24 (ART030) — TAK, taki przypadek istnieje. DYSPOZYCJA "
                "NALEZY DO MODERATORA, NIE ZAMYKAM SAM. Mechanizm: degeneracja przez ZAWEZENIE "
                "ZBIORU DOPUSZCZALNEGO (kinetyka nasycona, Gamma(n(t))=Gamma_0 stale), nie przez "
                "wage — X(T)=kappa*Gamma_0*(1-e^{-lambda T})/lambda wspolne dla kazdego lambda>0 "
                "(NC-ALG-022, zweryfikowane szescioma falsyfikatorami z F1 jako kontrola i F3 jako "
                "testem anty-artefaktowym). USTALENIE ZAKRESU: to NIE kontrprzyklad do MT13 — ich "
                "twierdzenie jest liniowe w n, moj przypadek nieliniowy, wiec poza zalozeniami "
                "(NC-ALG-023). Wyjasniona wlasna wczesniejsza porazka: pierwotna rodzina "
                "Gamma=gamma0(1+beta n)n jest scisle rosnaca, wiec z konstrukcji wykluczala "
                "mechanizm (NC-ALG-024). Bez claimu nowosci — kinetyka zerowego rzedu jest "
                "podrecznikowa. PRZEKAZANE: DS/R1 (czy istnieje mechanizm nienasycony i nieliniowy), "
                "MT13 (sugestia redakcyjna o zakresie), REC10 (klasyfikacja). | POPRZEDNIO: " + r[7])
        upd += 1
assert upd == 1, upd

body += NEW
with open(P, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    w.writerow(hdr); w.writerows([r for r in body if r])

st = {}
for r in body:
    if r:
        st[r[5]] = st.get(r[5], 0) + 1
print("wierszy:", len([r for r in body if r]))
for k in sorted(st):
    print(f"  {k:<22} {st[k]}")
