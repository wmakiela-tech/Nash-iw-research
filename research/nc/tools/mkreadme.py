import hashlib, glob, os
os.chdir('/home/claude/wmakiela-tech/nash-iw-research/research/nc/2026-10-18')

def h(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

desc = {
 '004': 'prior-art subtraction calej monografii: 68 obiektow numerowanych; po odjeciu gospodarzy i dwoch demotacjach zostaje 5 kandydatow do hierarchii B; 7 niecytowanych gospodarzy',
 '005': 'audyt warstwy non-mapow jako klasy: 96 zdan negatywnych, 44 ze swiadkiem, probka 10 swiadkow zweryfikowana 10/10, 12 dziur ze wzorcem na granicach rezimu',
 '006': 'cztery skonstruowane swiadki, w tym jadro analityczne na (0,inf) o WSZYSTKICH momentach zerowych (nieoznaczonosc Stieltjesa)',
 '007': 'domkniecie dwunastki: 6 swiadkow, 3 odsylacze wewnatrz manuskryptu, 1 przeredagowanie, 1 cytowanie, 2 otwarte',
 '008': 'minimaks dla czujnika oddzialujacego zwrotnie (problem otwarty par. 7.5b.5): postac zamknieta, prog dopuszczalnosci, nieciaglosc optymalnego wzmocnienia',
 '009': 'sufit niezalezny od protokolu M < 1/gamma (dowod elementarny) oraz pomiar OFIARNY: zysk 1.9x przy ograniczonych czasach pomiaru',
 '010': 'atak na wlasne Tw.1 z 009: tozsamosc ksiegowa (gamma c)^2 = dA^2 * tanh(gamma s/2); sufit przezywa trzy modele szumu, ale OBALONY zostaje jego ZAKRES — jest o wspolosiowosci reakcji zwrotnej z odczytem, nie o reakcji zwrotnej',
 '011': 'uogolnienie na dowolny generator: sufit zachodzi wtedy i tylko wtedy, gdy mu_2(G) <= 0 (norma logarytmiczna). Oscylator nie byl szczegolny jako oscylator. Kontrprzykad M13 lezy dokladnie na granicy i lamie sufit tak samo jak zlamal twierdzenie o normie logarytmicznej',
 '012': 'domkniecie dziury par.2.8 z 007: jawny wymierny swiadek rozdzielajacy garbling od eliminacji sektora PO POSTSELEKCJI, wiec nie przez slad; plus korekta 011 par.6.4 i domknieta tabela 2x2 (sufit wymaga wspolosiowosci ORAZ mu_2 <= 0); plus zgloszenie gravity well',
 '013': 'domkniecie dziury par.3.6: dwie przyblizenie minimalne realizacje tej samej funkcji przenoszenia w l^2, splecione operatorem ograniczonym o NIEograniczonej odwrotnosci, dowod elementarny; literatura NIE domknieta i zapisana jako trop, nie cytowanie',
 '015': 'ERRATA po audytach INT7 i REC9: odsylacz dla par.7.2 (czlon procesowy) byl za szeroki, bilans NIE wynosi zero otwartych; odsylacz dla par.5.10 przezywa, bo teza jest dwuczasowa; claim o braku progu tlumienia potwierdzony do a=50 z plateau przy sqrt(2) i z kontrola czulosci',
 '014': 'swiadek dla par.7.2 (ciaglosc): polgrupa kontrakcji na [0,2pi) sprzezona przez r(theta)=e^{i theta} daje V_t nieciagla ze skokiem 2|sin(pi e^{-t})|, maksymalnym (srednica okregu) przy t = ln 2; plus rozliczenie calej dwunastki non-mapow pozycja po pozycji i zamkniecie produkcji NC',
}

L = []
L.append('# NC — zwroty z 2026-10-18')
L.append('')
L.append('Zewnętrzna, niezależna komórka Claude (NC). Rola: audyt, prior-art subtraction, wkład matematyczny.')
L.append('')
L.append('**STATUS CAŁOŚCI: `[▷]` — nierecenzowane.** `NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE`')
L.append('')
L.append('EXEC_SIGN jest ludzki; żaden wynik stąd nie wchodzi do claimu ani artykułu bez uruchomienia kodu,')
L.append('proweniencji i zatwierdzenia Moderatora. **Audyt zewnętrzny obowiązkowy** per ANTI-SELF-SEALING —')
L.append('nie mogę wystawić go sobie sam.')
L.append('')
L.append('Autorstwo monografii i wszelkie decyzje redakcyjne należą do LT4. Zwroty 004–007 audytują jej tekst;')
L.append('008–011 nie są audytem, tylko próbą rozwiązania problemu, który monografia stawia jako otwarty')
L.append('(§7.5b.5 — czujnik oddziałujący zwrotnie na układ). 010 atakuje 009 i zwęża jego zakres,')
L.append('011 atakuje 010 i uogólnia go na dowolny generator. 012 wraca do audytu: domyka dziurę')
L.append('§2.8 z 007, koryguje 011 i zgłasza **gravity well** — pięć kolejnych zwrotów na jednym')
L.append('wątku, wszystkie nieaudytowane. Decyzja o fokusie należy do Moderatora.')
L.append('')
L.append('013 domyka §3.6, a 014 §7.2. **015 jest erratą** po audytach INT7 i REC9 i koryguje')
L.append('bilans: odsyłacz dla §7.2 w członie procesowym okazał się za szeroki, więc **nie jest to')
L.append('„zero otwartych"** — jedna pozycja pozostaje częściowo otwarta. Dziewięć dziur ma')
L.append('świadka, jedno cytowanie, jeden zweryfikowany odsyłacz, jedno przeredagowanie.')
L.append('')
L.append('Zastrzeżenie z 013 §3 — że liczę koszt własnego dorobku — potwierdziło się w praktyce:')
L.append('jedyne zawyżenie w tym bilansie wykrył audytor zewnętrzny, nie ja. Zwroty 007 i 012–014')
L.append('noszą baner erraty i zachowują oryginalną treść; datowanych zwrotów nie przepisuję.')
L.append('')
L.append('`audyt/` zawiera sześć pakietów do rozesłania przez Moderatora: nota przewodnia oraz')
L.append('po jednym zadaniu dla GPT, DS/R1 (część A **ślepa**), Gemini (reimplementacja bez')
L.append('zaglądania do mojego kodu), Groka i Bielika. Nic z 004–014 nie jest gotowe do')
L.append('podniesienia statusu — wszystko czeka na te audyty.')
L.append('')
L.append('Prerejestracje (`PREREG_*.md`) są zapisywane i haszowane **przed** uruchomieniem kodu,')
L.append('który opisują, razem z predykcjami. Trzy z nich okazały się fałszywe i są wymienione niżej.')
L.append('')
L.append('## Zwroty')
L.append('')
L.append('| plik | treść | sha256 |')
L.append('|---|---|---|')
for a in sorted(glob.glob('IW_NC_*.md')):
    k = [x for x in desc if '_' + x + '_' in a]
    d = desc[k[0]] if k else ''
    L.append('| `' + a + '` | ' + d + ' | `' + h(a) + '` |')
L.append('')
L.append('## Kod')
L.append('')
L.append('Reguła przyjęta po własnym błędzie z 11–12 X: **bez tekstu interpretacyjnego w `print`** —')
L.append('skrypty drukują wyłącznie tabele, odczyty dopisywane są po fakcie. `PREREG_DELAY.md` to')
L.append('prerejestracja zapisana i zahaszowana PRZED uruchomieniem kodu, który opisuje.')
L.append('')
L.append('| plik | sha256 |')
L.append('|---|---|')
for c in sorted(glob.glob('code/*')):
    L.append('| `' + c + '` | `' + h(c) + '` |')
L.append('')
L.append('## Błędy własne zapisane w tych zwrotach')
L.append('')
L.append('Zapisane celowo. Są materiałem (error-as-data), a bez bazowej stopy błędu audytor kalibruje się źle:')
L.append('')
L.append('- oszacowanie transportu spektralnego przez **supremum** bloków kolizyjnych — **FAŁSZYWE**,')
L.append('  obalone kontrprzykładem LT4 (poprawna wielkość to norma **sumy**), wycofane; jego wersję')
L.append('  potwierdziłem potem na ~11 900 układach, 0 naruszeń;')
L.append('- wniosek, że kinetyka dyssypatywna pociąga ujemną normę logarytmiczną — **ODRZUCONY**')
L.append('  kontrprzykładem M13 (generator Metzlera, masa maleje, a `mu2 = +0.3155`);')
L.append('- falsyfikator momentowy zgłoszony jako nowy — okazał się **REKONSTRUKCJĄ** Tw. 8 rozdz. 1;')
L.append('- **trzy claimy o tym, czego manuskrypt NIE MA**, postawione z pośrednika (regex, plan')
L.append('  redakcyjny, liczba znaków) zamiast z tekstu;')
L.append('- predykcja `a* = 2/(gamma t_s)` — **FAŁSZYWA**; pominięty człon współrządzi optimum;')
L.append('- przewidywanie optymalnej liczby pomiarów `k > 1` — **FAŁSZYWE**, optimum to `k = 1`')
L.append('  przy swobodnych czasach;')
L.append('- prerejestrowana predykcja z 009 §5.4, że przy szumie niezależnym sufit `1/gamma`')
L.append('  **upadnie** — **FAŁSZYWA**: sufit, podłoga i optymalne `k` są niezmienione (010);')
L.append('- prerejestrowana predykcja A3, że niewspółosiowość **podnosi** sufit do `1/|cos φ|` —')
L.append('  **FAŁSZYWA w rodzaju, nie w wartości**: podniesionego sufitu nie ma, nie ma żadnego;')
L.append('- `π/2` użyte jako antywęzeł prędkości, gdy jest **węzłem** — tę samą chwilę nazwałem')
L.append('  „czasem ślepym" w 009; wykryte przez tożsamościowo zerowe wyjście, nie przez przegląd;')
L.append('- cztery z sześciu predykcji prerejestrowanych w `PREREG_GEN.md` — **FAŁSZYWE** (011 §5),')
L.append('  w tym warunek wyrównania z metryką, który okazał się pozorny: przy `P = I` spełnia go')
L.append('  każdy kierunek odczytu;')
L.append('- zamiatanie kierunku po **ćwiartce** wziętej za wszystkie kierunki — dwie tabele')
L.append('  orzekły wtedy przeciwnie na tej samej macierzy;')
L.append('- wynik zerowy z niedomiarowej próby odczytany jako potwierdzenie hipotezy, którą')
L.append('  jej własny poprzednik już obalił;')
L.append('- pierwszy świadek dla §2.8 **odrzucony przez własną kontrolę** — rozróżniał stany')
L.append('  wyłącznie przez ślad, czyli powielał uwagę, którą w 007 sam odrzuciłem jako nie tę;')
L.append('- `nan` z niedomiaru zmiennoprzecinkowego w trzech tabelach, skwitowane **zastrzeżeniem')
L.append('  w wydruku zamiast poprawienia rachunku** — wymówka udająca kontrolę (013 §4).')
L.append('')
L.append('Cztery z tych błędów to jedna awaria: **skan pokrywający obszar, który wygląda na pełny')
L.append('i nie jest, czytany jako rozstrzygnięcie.** Reguła zaproponowana w 011 §5 (kontrola')
L.append('pokrycia + kontrola czułości) jest odpowiedzią i została zastosowana do samej siebie')
L.append('w tym samym przebiegu.')
L.append('')
L.append('Dwie reguły proceduralne zaproponowane po tych błędach, do decyzji Moderatora:')
L.append('')
L.append('1. **Claim o BRAKU jest claimem numerycznym** i wymaga podania miejsca, narzędzia oraz')
L.append('   walidacji narzędzia na elemencie znanym jako obecny. Streszczenie manuskryptu nie jest')
L.append('   dopuszczalnym źródłem dla claimu o braku.')
L.append('2. **Przed wysłaniem OSZACOWANIA** trzeba skonstruować konfigurację oddzielającą je od')
L.append('   najbliższego fałszywego wariantu i podać parametr oddzielający. Rodzina testowa')
L.append('   zdegenerowana w tym parametrze nie dowodzi niczego, choćby przechodziła w 100%.')
open('README.md', 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('napisano README.md,', len('\n'.join(L).encode()), 'bajtow')
