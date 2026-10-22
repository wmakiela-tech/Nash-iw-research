# LT5 — robocza redakcja wybranych uzupełnień Living Theory REV020 (KANDYDAT, nie REV021)

Data: 2026-10-23
Owner: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5
ID: LT5-REV021-STAGED-EDITORIAL-CH4-CH5-CH6-CH7-001
Class: AUTHORIAL SCIENTIFIC SYNTHESIS / PRIOR-ART-ABSORBED / MANUSCRIPT-STAGING
Basis: working monograph "Opisy efektywne w układach fizycznych", 7 chapters, 159536 characters, Google Docs modified 2026-10-19T13:40:36Z.
Authority: NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE.
Crucial: This is an editorial STAGING file. The authoritative Google Docs monograph was NOT edited; REV021 has not been created or approved. Reviews of one LT theorem do not imply reviews of all later results.
Parent impact audit: research/lt5/2026-10-23/lt5_rev020_manuscript_impact_gap_audit_001.md

## Autor: decyzja ogólna

Dotychczasowa konstrukcja matematyczna rozdziałów 1–7 nie wymaga obalenia ani masowej przebudowy. W nowych pracach występuje wiele nieimplikacji istotnych dla prawidłowego rozumienia dzieła, ale wszystkie omówione wzory mieszczą się w dojrzałej literaturze: matematyce półgrup, teorii decyzji, optymalnego odtwarzania, eksperymentów statystycznych, kanałów oraz instrumentów kwantowych, numerycznej analizy operatorów i teorii ODE. Rola autorska LT5 polega na starannym wpisaniu ich w JEDEN rygor pojęciowy, bez fałszywych syntez fizycznych.

Cztery docelowe wstawki redakcyjne:
A. §4.11b zgodność symbolu dywergencji i projektora na dyskretnej siatce;
B. §5.5b zgodność nieselektywnego kanału i POVM NIE determinuje selektywnych operacji i warunkowej korekty;
C. §6.10a datowany audyt źródłowego błędu PBH/BBN, bez promowania proxy do fizycznych obfitości;
D. §7.5c informacja i odtwarzanie celu versus rzeczywista zdolność sterowania w czasie.

Wstawki zawierają etykiety statusu. Ostateczna publikacja wymaga scalonego, jednokrotnego uporządkowania numeracji i referencji. Obecny rozdział 7 ma m.in. numer 7.4 w dalszej części niż 7.11; doraźna renumeracja jednego fragmentu byłaby niebezpieczna.

---

## Projekt §4.11b — Zgodność dyskretnego operatora i projektora spektralnego

Na siatce periodycznej z krokiem h=L/N rzutnik transwersalno-bezśladowy TT bazuje na wektorze Fouriera k oraz P_k=I-kkᵀ/|k|² i spełnia kᵀTT_k(H)=0. Jednak różnica centralna drugiego rzędu ma symbol delta_h(k)_j=sin(k_jh)/h. Jej dywergencja zrzutowanego tensora jest równa i delta_h(k)ᵀ TT_k(H), co w ogólności NIE znika, ponieważ delta_h(k) i k mogą nie być równoległe.

Jedno-modowy dowód: niech k=(p,q,0), p,q dodatnie i różne, obie składowe poniżej Nyquista. Weźmy u=(q,-p,0)/sqrt(p²+q²), v=(0,0,1), H0=uuᵀ-vvᵀ, H(x)=cos(px+qy)H0 na domenie L=2pi. H0 jest k-poprzeczny, bezśladowy i stały względem TT_k. Wtedy dokładna norm RMS centralnej dywergencji wynosi
  RMS(D_h · H) = |q sin(ph) - p sin(qh)| / [h sqrt(2(p²+q²))].
Dla p=1,q=2: N=31 daje 0.0128579428834, N=41 daje 0.0073831325275 mimo braku błędu w samej geometrii projekcji Fouriera. Dla ustalonego p,q norma jest O(h²), ale nie istnieje taka jednostajna gwarancja w całym paśmie, gdy p/N i q/N pozostają niezerowymi różnymi ułamkami.

W historycznych diagnostykach DTC0a stały interior_k=3 oznacza fizyczną szerokość wykluczenia 3L/N, zmieniającą się wraz z N. Niezbędne są trzy osobne certyfikaty: FOURIER_TT, FINITE_DIFFERENCE_TT i PHYSICAL_CONTINUUM_TARGET. Nie należy utożsamiać tego przykładu z twierdzeniem o nowych kohomologiach, fizycznym J3/K ani zakończoną repliką oryginalnego DTC0a. Osobny helper v0.3.2 ma szkic stencila rzędu 4, ale źródłowy helper v0.3.1 zgłasza NotImplementedError dla order4.

Źródła: INT8 ROT008 (2026-10-23), M13 ROT18/19; standardowa analiza Fouriera i różnic centralnych.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/int8/2026-10-23/iw_int8_rot008_dtc0a_fourier_tt_vs_finite_difference_divergence_symbol_gap_001.md
Status: źródłowo ograniczona algebra i kontrola syntetyczna PASS; oryginalny runtime nieodtworzony, niezależna recenzja pełnego modelu niepotwierdzona.

---

## Projekt §5.5b — Kanał, POVM i instrument są różnymi danymi

Niech Z=diag(1,-1), 0≤p≤1 i Lambda_p=(1-p)id+p Ad_Z. Dwa legalne instrumenty CP o dwóch wynikach to:
  F0=(1-p)id, F1=p Ad_Z;
  C0=(1-p)Lambda_p, C1=p Lambda_p.
W każdym przypadku suma operacji jest tym samym CPTP Lambda_p, a obie pary mają dokładnie te same efekty POVM:
  E0=(1-p)I, E1=pI.
Zatem samo wejściowe prawo etykiet jest identyczne i niezależne od stanu dla wszystkich przygotowań.

Różne są jednak warunkowe transformacje. Rejestr F ujawnia rzeczywiście wykonany błąd Z; po odczycie wybór R0=id i R1=Ad_Z daje sum_a R_a ∘ F_a = id na wszystkich stanach, również splątanych z układem odniesienia. W C etykieta jest niezależną monetą. Dla dwóch ortogonalnych stanów własnych sigma_x zachowany kubit ma po Lambda_p odległość śladową |1-2p|<1 (0<p<1), której żadna późniejsza reguła CPTP warunkowana monetą nie może zwiększyć do 1. Dokładna korekta wszystkich stanów jest więc niemożliwa.

Dla kanałów zachowujących klasyczny rejestr a otrzymujemy
  || Fhat_p - Chat_p ||_diamond = 4p(1-p).
Dowód: różnica to p(1-p) razy tensor z klasyczną różnicą |0><0|-|1><1| i superoperatorem id-Ad_Z; norma diamentowa id-Ad_Z wynosi 2, zaś rozłączne bloki etykiet podwajają normę. Przy p=1/2 daje to 1, mimo zerowej odległości obu kanałów nieselektywnych i identycznych POVM.

Wniosek: poprawny kontrakt operacyjny wymaga wyniku a oraz konkretnych operacji CP instrumentu, nie tylko Lambda i efektów E_a. Rekord może być całkiem nieinformatywny o wejściowym parametrze, a zarazem doskonale identyfikować losowo wykonaną transformację i umożliwiać jej odwrócenie. Jest to przypadek znanej environment-assisted quantum error correction (Gregoratti–Werner), NIE nowe prawo fizyczne.

Wzmocnienie PRF11 R17, ODDZIELNY eksperyment o innym POVM: ten sam kanał qubit Lambda_s tłumiący składowe y,z przez k=sqrt(1-s²) może powstać przez nieostry instrument Lüdersa sigma_x, którego etykieta ma Fishera I_1=s²/(1-s²theta²), albo przez losowo-unitarny instrument z etykietą niezależną od theta, I_1=0. Na jednej kopii powtarzane komutujące odczyty Lüdersa są klasycznym garblingiem jednego ostrego wyniku sigma_x; zatem I_N≤1/(1-theta²), chociaż pełna QFI rodziny rho_theta=(I+theta sigma_x+theta sigma_y)/2 wynosi 2/(1-2theta²). Nie utożsamiać I rekordu z informacją w dostępnej po nim próbce kwantowej ani z informacją z wielu niezależnych kopii.

Dodatkowa granica: klasyczny realny reset Q_s=I-seeᵀ z LT5/INT8/Geeky NIE może być automatycznie globalnym kanałem kubitu Blocha. Diagonalna mapa (1-s,1,1) ma minimalną znormalizowaną wartość własną Choi -s/4 przy s>0. Wielkość jej minimalnej odległości diamentowej do CPTP wynosi s/2. Legalny pomiar kwantowy wymaga jawnego instrumentu oraz prawa Bornowskiego, a nie podstawienia deterministycznego b=s eᵀx+eta.

Źródła:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-23/lt5_same_channel_same_povm_distinct_instrument_exact_causal_recovery_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/prf11/2026-10-23/IW_PRF11_R17_SAME_CHANNEL_DIFFERENT_INSTRUMENT_FISHER_MINIMAX_001_20261023.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/lt5/2026-10-22/lt5_bloch_reset_noncp_exact_diamond_distance_and_instrument_nonmap_001.md
Status: własna algebra i kontrole numeryczne PASS; nie ma jeszcze niezależnego werdyktu REC10/SW dla obrotów LT5 6 i 7. Poprzednia recenzja rozdziału 5 nie obejmowała tego późniejszego przykładu.

---

## Projekt §6.10a — Status źródłowy PBH/BBN na 23 X 2026

Równania w obecnym rozdziale 6 są tożsamościami dla zadanych układów ODE, a nie zrekonstruowanymi obfitościami pełnej nukleosyntezy. Ostatni audyt Wu–Xu porównuje prawo źródłowe tekstu z zachowaniem publicznego helpera oraz dwie mapy ładunkowe B_exec/B_sym; istotny jest porównywalny fizyczny background i odczyt w stałej temperaturze T_nuc≈0.07818527 MeV, nie automatycznie stała wartość czynnika skali.

Źródłowe cztery warianty dały na drukowanych danych proxy Y=2X/(1-X) pojedyncze kontrasty odpowiadające neutronowym X:
  Delta_X_exec ≈ -1.89885665743e-5;
  Delta_X_sym ≈ +1.26671312111e-5.
Aby matematycznie CERTYFIKOWAĆ oba znaki na podstawie czterech końcowych wartości X, wystarczy, lecz konieczne do zweryfikowania jest niezależne ograniczenie błędu globalnego każdej obliczonej wartości:
  epsilon_X < 6.33356560556e-6.
To jest PRÓG WYMAGANY, a nie błąd globalny już dowiedziony. W szczególności samo nominalne reltol/abstol Julia, odtworzenie źródłowego helpera i kontrola źródło-off nie są certyfikatem globalnym. Trzeba związać błąd stanu, błędy temperatury i interpolacji fixed-T, oryginalny adaptacyjny 10D runner oraz brakujące aktywne źródło hadronowe poniżej M=1e9g z rzeczywistym celem. Wyjątkowo duże diagnostyczne proxy Y>1 nie są fizycznymi obfitościami helu.

W tym stanie nie ma uprawnionego wniosku o Y_p/D/H, nowym bound PBH ani kanonizacji mechanizmu. Rozdział 6 zachowuje poprawne tożsamości czułości i quasi-stacjonarnego błędu; należy tylko zaktualizować stan brakujących źródeł i certyfikacji.

Źródła: MT13 FrontB 2x2 i Mech-S7 ROT002.
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mt13/2026-10-23/mt13_frontb_2x2_state_readout_precision_gate_001.md
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/mech-s7/2026-10-22/mech_s7_frontb_common_background_target_gate_002.md
Status: wyłącznie datowany audyt, nie obliczenie endpointu fizycznego.

---

## Projekt §7.5c — Odtwarzanie, korekta i zasób czasu

(A) Już istniejące twierdzenie 7.9: na niezależnych kulach y,eta, dla biernego b=Cy+eta, bez oddziaływania czujnika z układem, dokładny minimaks skalarny to
 E=min_w [ R||m-Cᵀw||+delta||w|| ].
Nie ma tu aktuatora. Jego dodanie wymaga nowych, jawnych portów.

(B) Dla statycznego sprzężenia liniowego o ||F||_op≤kappa i skalarnym terminalnym porcie o czułości a!=0, z=mᵀy-aᵀF(Cy+eta), zachodzi
 J_gain=min_{||w||≤kappa||a||} [R||m-Cᵀw||+delta||w||].
Dowód: w=Fᵀa; każde w w tej kuli jest realizowalne przez operator F rzędu 1. REC10 ROT03: PASS_WITH_GUARDS. Warunek ograniczenia F NIE jest twardą granicą amplitudy u(b) we wszystkich realizacjach pomiaru.

(C) W oddzielnym modelu jednego pomiaru z niezależnym centralnie symetrycznym zwartym wypukłym K i N, oraz arbitralną regułą korekty skalarną |u(b)|≤B:
 A=max_K |mᵀy|, E=max_{v∈K,Cv∈N}|mᵀv|,
 J_amp=max{E,A-B}.
Dowód opiera się na dwóch nierozróżnialnych stanach ±v oraz nasyconym środku warunkowego przedziału. Jest to klasyczna geometria minimaksowej estymacji; status szczegółowego matematycznego referee LT5 obrotu 2 nadal oczekuje.

(D) Dla celu WEKTOROWEGO i zbioru dopuszczalnych korekt D faktyczny problem to
 J*=sup_b min_{d∈D} max_{t∈T_b}||t-d||.
W kwadratowej euklidesowej geometrii dual to
 r_D(T)^2=max_mu [Var_mu(t)+dist(E_mu t,D)^2].
REC10 ROT05: PASS_WITH_SHARPENING; wystarcza certyfikat na najwyżej d+1 aktywnych najdalszych punktach celu w R^d, nie d+2 z pierwszej noty LT5. Naiwne wektorowe max(E,A-B) zawodzi: dla K=[-1,1]^2, idealnego b=y1 i korekt D równych kuli promienia B otrzymujemy sqrt(1+(1-B)_+²).

(E) Dla dwuetapowej chronologii y∈[ell,h], wczesnej nieodwołalnej korekty |u0|≤B0, późniejszego b=s(y-u0)+eta z |eta|≤delta, s>0, oraz późnej |u1|≤B1: w=(h-ell)/2, c=(h+ell)/2, e=min(w,delta/s), zatem
 J_two=max(e,w+(|c|-B0)_+-B1).
Porównując z INNYM protokołem trzymającym sumę B0+B1 wyłącznie na późny czas otrzymujemy dokładną nadwyżkę
 J_two-J_late=min((B0-|c|)_+,(w-B1-e)_+).
REC10 ROT07: PASS_WITH_EXACT_SHARPENING. Pełna identyfikacja na końcu nie oznacza, że dawny, już zamknięty port interwencji mógł tę informację wykorzystać.

(F) Pomiar zmieniający dynamikę wymaga źródłowo zgodnego terminalnego celu m_s, a nie m z układu nieperturbowanego. Dla deklarowanego KLASYCZNEGO resetu Q_s=I-s eeᵀ i ellᵀF x=0 na K mamy ellᵀFQ_sx=-s(ellᵀFe)eᵀx. To nie jest ogólne twierdzenie o kwantowej mierzalności lub CP, a pomiar z indywidualnymi ograniczonymi szumami nie jest automatycznie eksperymentem Gaussian/Le Cam.

(G) Jeżeli sygnał pomiaru może również wejść do fizycznej zmiennej resetu, ograniczenie informacji o oryginalnym parametrze nie kontroluje wielkości faktycznego zaburzenia stanu. REC10 ROT09 potwierdził w źródłowym CLASSICAL Gaussian modelu przy s→0, N≈B/s, ustalonym alpha>0 jednocześnie Fisher=O(s) i Var(x_N)~const/s. Nie importować tej asymptotyki jako pomiarowej fizyki kubitu.

(H) PRF11 R17 pokazuje na jednej kopii rho_theta=(I+theta X+theta Y)/2, że pełny rejestr N powtórzeń komutującego instrumentu Lüdersa sigma_x jest garblingiem pojedynczego ostrego odczytu sigma_x, a więc I_N≤1/(1-theta²), mniej niż QFI=2/(1-2theta²). Dla |theta|≤R<1/sqrt2 pojedynczy ostry sigma_x ma dokładny minimaks kwadratowy R²(1-R²), co daje dolną granicę każdej takiej powtarzanej sekwencji. Nie rozszerzać na pomiary w innych bazach ani na N kopii. Status niezależnego referee R17: PENDING.

Odrębne nośniki należy wypisać przy twierdzeniach: deterministyczny adwersarialny zbiór błędów, niezależne Gaussian innowacje, korelacje kowariancyjne, Bornowskie prawa CP instrumentów oraz ograniczenia fizycznego aktuatora i jego terminu. Żaden wspólny symbol epsilon nie identyfikuje tych klas.

Źródła REC10 ROT03/05/07/09, LT5 obroty 1–7, PRF11 R17, INT8/Geeky oraz literatura optimal recovery, set-membership output feedback, Blackwell i quantum instruments.

---

## Kontrole niezależne bieżącego obrotu

1. Dla s=0.2,0.6,0.9 i theta=-.5,-.2,0,.3,.5 bezpośrednie obliczenia macierzy 2x2 potwierdzają identyczność nieselektywnego instrumentu Lüdersa i odpowiedniej mieszanki id/Ad_X z PRF11; największy błąd Frobeniusa 5.55e-16. Równanie klasycznego FI Bernoulliego również sprawdzone.
2. Dla mody k=(1,2,0) symbol dywergencji z §4.11b odtworzono liczbowo: N31=0.012857942883432427, N41=0.007383132527489159.
3. Cztery źródłowo wydrukowane proxy MT13 odwrócone przez X=Y/(2+Y) potwierdziły kontrasty -1.898856657434e-5 i +1.266713121112e-5, a przez to wymagany epsilon_X<6.33356560556e-6.

Kontrole nie zastępują pierwotnego runtime Wu–Xu, DTC0a ani niezależnego przeglądu nie-recenzowanych fragmentów matematycznych.

## Decyzja autorska o integracji

JEDEN zestaw wstawek, bez deklaracji osobnej teorii. Wewnętrznie gotowe do redagowania po zwykłej kontroli: §7.5c (B,D,E) objęte REC10 ROT03/05/07; §4 ograniczony jako świadectwo metodologiczne, §6 jako datowany stan źródłowy. §5 główny przykład oraz §7.5c (C,F,H) wymagają odrębnego twierdzenie-po-twierdzeniu REFEREE lub bardzo wyraźnej etykiety „kontrprzykład roboczy” przed publikacją. Brak odpowiedzi w wątku zgłoszonych luk nie jest przyjęciem.

Nie edytować automatycznie autorytatywnego Google Docs ani nie oznaczać REV021 jako istniejącej. BW może przyjąć zapis tej noty jako wydarzenie DERIVED, bez naukowej akceptacji lub EXEC. Żadna z dodanych ilustracji nie dowodzi fizycznego J3/K, rzeczywistego nowego kanału kwantowego lub PBH bound. STOP na repakietowanie tych samych klasycznych gospodarzy jako nowość.
