---
artifact_id: SW-FRONTB-WUXU-ENERGY-SUPPORT-AND-SLOPE-CONFOUNDING-001
title: Front B — generator energy support and mass-slope confounding
created_at: 2026-10-12
as_of: 2026-10-12
origin_cell: IW_SCIENCE_WORK_01 / SW
document_type: RETURN
exposure: PUBLIC
archive_mode: PUBLIC_ARTIFACT
bw_ingestion_event_id: ING-20261012-0063
bw_qualification_state: SOURCE_ENERGY_SUPPORT_SLOPE_CONFOUNDING_NARROW
bw_lifecycle_state: CURRENT_REPRESENTED
scientific_claim_ceiling: SOURCE_DIAGNOSTIC_NO_OWNER_AUTHORITY
source_revision: PRIVATE_ORIGINAL_BW_ROW_1390
no_canon: true
no_exec_sign: true
---

> Public scientific source body (not merely a custody pointer). Original scientific return reproduced below without intentional change. The private source locator remains in BW; the result is NARROW, not physical endpoint validation, canon or EXEC_SIGN.

# Front B: zakres energii generatora i niejednoznaczność nachylenia źródła

**RETURN_ID:** SW-FRONTB-WUXU-ENERGY-SUPPORT-AND-SLOPE-CONFOUNDING-001  
**FROM_CELL:** IW_SCIENCE_WORK_01 / SW  
**Data:** 2026-10-12  
**Werdykt:** **NARROW** — bezpośrednie przeliczenie E2 wymaga najpierw kontroli zakresu energii i hadronizacji.  
**Wynik wykonany:** audyt rzeczywistego generatora, rachunek obciętej całki i numeryczny kontrprzykład dla jednoznacznego przypisywania krzywizny źródła fizyce.  
**BlackHawk/PYTHIA:** NOT_RUN. **Walidacja fizycznych źródeł i celu BBN:** OPEN.

## 1. Co zmienia ten obrót

XH022/023 i Mech-S6 poprawnie przenieśli priorytet z podłogi logarytmicznej na źródło hadronów. Podczas tego obrotu XH024 i Mech opublikowali już rekonstrukcję generatora oraz rozdział E2a (obcięty test wykonawcy) od E2b (walidacja pełnego źródła). Te ustalenia są tutaj potwierdzeniem i wejściem. Własne uzupełnienie SW to dokładny rachunek niejednoznaczności nachylenia, diagnostyka ważona liczebnością E^0.3 oraz jawna mapa kolumn źródła do nominalnego wstrzykiwania populacji.

Odtworzony notebook generujący tabelę faktycznie ustawia **energię pierwotną 5–100000 GeV na 100 punktach**, a następnie wybiera tryb BBN. Jest to potwierdzone w miejscu wywołania, nie wywnioskowane z wartości domyślnych wrappera. Wzrost temperatury Hawkinga przy zmniejszaniu masy przesuwa wagę całki poza ten zakres. Zwiększenie liczby punktów w niezmienionym przedziale nie odtwarza pominiętego ogona.

W zadanym modelu kontrolnym wykazano ponadto, że ograniczenie energii **samo zmienia lokalne nachylenie względem masy**. Zmienność nachyleń przy brzegu tabeli może zatem zawierać efekt obcięcia. Nie ustalono, jaka część rzeczywistego nachylenia Wu–Xu pochodzi z tego efektu.

Praktyczna korekta: E2 powinno kontrolować osobno zakres energii pierwotnej, zakres i konwencję hadronizacji oraz całkowanie liczebności wtórnych. Najoszczędniejszą reprezentacją wejścia do obecnego modelu populacji są **momenty zerowe, rozdzielone według gatunków**. Nie wymagają przechowywania pełnego dwuwymiarowego widma fragmentacji, jeśli nie wprowadza się zależności reakcji od energii.

## 2. Stan projektu i zachowane wyniki

Sprawdzono Slack, Drive i rezerwowy GitHub. Początkowy stan zamrożono około 17:23 CEST; przed publikacją włączono XH024/025, Mech E2 pipeline oraz zwroty Rec9 do 2026-10-12 18:16 CEST. Późniejsze wejścia i ich adresy zapisano w source_ledger.json.

- LT4 pojawiła się i przejęła autorstwo LT; MT13 zakończył tymczasowe pokrycie i wrócił do programu badań. DRAFT018 ma późniejszy overlay H8R-C: SOURCE_INTERFACE_UNRESOLVED; wcześniejszy stan oczekiwania na werdykt jest nieaktualny.
- REV020 pozostaje aktywne, REV021 nie utworzono, TPE HOLD, użyteczność kompilatora niezmierzona.
- Samą gotowość pakietu M12→M13 odróżniono od aktywacji. Dla LT4 uwzględniono późniejsze potwierdzenie MT13 z 18:02 CEST.
- Poprzedni SW coupled residual tube pozostaje poprawnym wynikiem warunkowym dla zadanych źródeł. Nie wycofuje się ani nie modyfikuje poprzednich raportów i archiwów.
- Wyniki Mech dotyczące monotoniczności, jednoznaczności chwilowego DE oraz masowo ważonej liczebności E0 nie są tu ponownie zgłaszane jako nowe.

## 3. Łańcuch rzeczywistego generatora

Repozytorium: `Fenyutanchan/Primordial-Black-Hole`, obserwowany commit `d395183674cace6c9906a8911bdeb7234ba4040d`. Dokładne blob SHA i lokalne SHA256 znajdują się w `source_ledger.json` oraz `audit_results.json`.

| Etap | Zaobserwowana implementacja | Wniosek |
|---|---|---|
| Generator | `valid_hadrons_from_BlackHawk.ipynb`, komórka 12 | 100 mas od 1e9 do 4e12 g |
| Energia pierwotna | `set_BlackHawk_energy_spectrum!(...,5,1e5,100)` | Skończony, stały zakres dla każdej masy |
| Tryb | `set_BlackHawk_BBN!` ustawia `hadronization_choice=0` | Nie wolno zastąpić go widmami dzisiejszych stabilnych produktów |
| Liczebność | Trapezy w logarytmie energii wtórnej dla `E*dN/(dt*dE)` | Generator potrzebuje całki po widmie, osobno dla pięciu kolumn |
| Eksport | `hadrons_from_PBH.dat`, jednostki GeV | 100 × 6 dodatnich wartości, pierwsza kolumna to masa |
| Wykonawca ODE | liniowa interpolacja log–log z liniową ekstrapolacją | Poniżej brzegu używa pierwszego nachylenia tabeli |
| Archiwalne PYTHIA | `table_up.jl`: `Emax_initial=1e5`, `Emax_final=1e5` | Dodatkowy ślad zakresu; nie dowód, że ten skrypt wygenerował zainstalowane tabele BlackHawk |

Wrapper wskazuje artefakt BlackHawk v2.3 z SHA256 `dd148349304c158ed3509ea6935f2fd3d60ebe7cda4c34598aa99ea329c129a7`. Nie pobrano i nie zbadano jego pełnej zawartości w tym obrocie. Julia nie jest zainstalowana w środowisku wykonawczym. Nie wykonywano kosztownej przebudowy środowiska.

README zawiera starszy odsyłacz do `valid_mesons_from_BlackHawk.ipynb`. W aktualnym katalogu znajduje się `valid_hadrons_from_BlackHawk.ipynb`; jego treść odczytano po blob SHA, bo zwykły odczyt dużego notebooka nie zwracał treści. Analiza dotyczy poprawnego, aktualnego pliku.

Odtworzone nachylenia pierwszego przedziału: pion −1.200486, K± −1.196651, K0L −1.196805, proton −1.204291, neutron −1.204763. To reprodukcja XH/Mech, nie nowy wynik.

## 4. Dokładne ograniczenie informacyjne

Niech P_i(E;M)≥0 będzie widmem pierwotnym, a N_ih(E)≥0 oczekiwaną liczebnością gatunku h z jednego pierwotnego obiektu i, przy ustalonej konwencji cząstka/para i rozpadów. Wtedy

\[
q_h(M)=\sum_i\int_0^\infty P_i(E;M)N_{ih}(E)\,dE.
\]

Rozdzielenie przedziałów jest dokładne:

\[
q_h=q_h^{<E_{\min}}+q_h^{[E_{\min},E_c]}+q_h^{>E_c}.
\]

Siatka na środkowym przedziale, nawet dowolnie gęsta, nie identyfikuje ostatniego składnika bez dodatkowej informacji o N_ih. Jeżeli kernel na tym przedziale jest dokładny i całkowanie dodatnie, obcięta całka jest dolnym ograniczeniem dla **tego samego pełnego kernela**. Nie ustala to znaku błędu E0: E0 jest odrębną ekstrapolacją po masie, a nie tą obciętą całką.

Najtańszy kontrprzykład: dwie funkcje liczebności są identyczne dla E≤E_c. Powyżej E_c pierwsza ma N_h=0, a druga N_h=E/(2m_h) na skończonym paśmie (E_c,2E_c), zero poza nim. Obie spełniają dodatniość oraz ograniczenie energii m_h N_h≤E, lecz ich źródła różnią się o dodatnią całkę, gdy P>0. Jest to kontrprzykład dla wystarczalności **dodatniości i budżetu energii**, a nie konstrukcja dwóch fizycznie dopuszczalnych modeli QCD.

Jeśli niezależnie dopuszczono górne ograniczenie N_ih(E)≤B_ih(E), otrzymuje się brakujący certyfikat

\[
0\le q_h^{>E_c}\le\sum_i\int_{E_c}^{\infty}P_i(E;M)B_{ih}(E)\,dE.
\]

Taki bound może zastąpić część kosztownego generowania. Jego założenia muszą dotyczyć właściwego gatunku, konwencji rozpadu i zakresu energii. Nie ustanowiono go tutaj dla rzeczywistych źródeł Wu–Xu.

## 5. Wykonany rachunek spektralny — jawny model kontrolny

Przyjmujemy wyłącznie do diagnostyki: bezmasowe widmo w przybliżeniu optyki geometrycznej oraz liczebność proporcjonalną do E^δ. Daje to całkę w zmiennej x=E/T_BH:

\[
f_{\sigma,\delta}(x)=\frac{x^{2+\delta}}{e^x+\sigma},\qquad
I_{\sigma,\delta}=\int_0^\infty f_{\sigma,\delta}(x)\,dx,
\]

gdzie σ=−1 oznacza statystykę Bosego, σ=+1 Fermiego. Dla s=3+δ:

\[
I_{-1,\delta}=\Gamma(s)\zeta(s),\qquad
I_{+1,\delta}=(1-2^{1-s})\Gamma(s)\zeta(s).
\]

Wyniki poniżej dotyczą δ=0.3. Temperatura została policzona z T_BH=ℏc³/(8πGM), z jednostkami GeV i gramami. Otrzymano w przybliżeniu T_BH M=1.0572612×10¹³ GeV·g; nie jest to deklaracja takiej dokładności fizycznej.

| Masa [g] | E_c/T_BH dla E_c=1e5 GeV | Pominięta część całki kontrolnej: Bose | Fermi |
|---:|---:|---:|---:|
| 1e9 | 9.458 | 0.566% | 0.710% |
| 6e8 | 5.675 | 9.05% | 11.33% |
| 3e8 | 2.838 | 47.15% | 56.86% |
| 1.06e8 | 1.003 | 90.17% | 96.06% |
| 1e8 | 0.946 | 91.22% | 96.65% |

**Te liczby nie są błędami rzeczywistych źródeł π/K/p/n, przedziałami ufności ani ograniczeniami BBN.** Nie użyto właściwych spinowych greybody factors, gatunkowej fragmentacji i ich niepewności. Model kontrolny pokazuje skalę wymaganej kontroli zakresu; nie dostarcza E2.

W tym samym modelu, dla pominiętego górnego ogona poniżej 1%, potrzeba E_c/T_BH≈8.72–9.02. Przy 1e8 g odpowiada to około **0.92–0.95 miliona GeV**. Dla 0.1% jest to około **1.23–1.26 miliona GeV**. To wartości projektujące test, nie gwarancje dla BlackHawk. Samo zwiększenie Emax wrappera bez właściwego kernela hadronizacji nie wystarcza.

## 6. Dlaczego nachylenie przy brzegu jest niejednoznaczne

Nieobcięty model kontrolny ma dokładnie q∞(M)∝M^(−1−δ). Przy stałych energiach E_min,E_c:

\[
q_{\rm box}(M)\propto M^{-1-\delta}
\int_{\ell(M)}^{\eta(M)} f_{\sigma,\delta}(x)\,dx,
\qquad \ell=E_{\min}/T,\quad\eta=E_c/T.
\]

Ponieważ ℓ i η są proporcjonalne do M,

\[
\frac{d\log q_{\rm box}}{d\log M}
=-1-\delta+
\frac{\eta f(\eta)-\ell f(\ell)}{\int_\ell^\eta f(x)\,dx}.
\]

To dokładna tożsamość dla zadanej rodziny kontrolnej. Na pierwszym rzeczywistym przedziale mas tabeli, dla δ=0.3, pełne źródło ma nachylenie −1.3, lecz obcięte daje **−1.26744 (Bose) lub −1.25910 (Fermi)**. Dla większych mas efekt górnego obcięcia maleje i nachylenie zbliża się do −1.3.

Rzeczywisty pionowy wykładnik tabeli wynosi −1.20049. Model kontrolny go **nie reprodukuje**: różnica wynosi około 0.059–0.067. Nie ma podstaw do przypisania całego obserwowanego odchylenia obcięciu. Wynik usuwa jednak jednoznaczną interpretację zmienności nachyleń jako samej krzywizny fizycznej.

Konsekwencja dla E1a: lokalne nachylenia pozostają legalnym testem wrażliwości. Ich rozrzut nie staje się przez to fizycznym przedziałem niepewności. W E2 trzeba zmieniać zakres energii przy ustalonej masie i konwencji źródła; zmiana samej masy miesza oba efekty.

## 7. Najmniejsza naprawa drogi E2

Nie zlecam nowej kampanii. Dla istniejącego kierunku XH/Mech trzy punkty mas pozostają sensowne, ale wejście do E2 musi zawierać:

1. **Kontrolę energii przy ustalonej masie:** osobno zagęszczenie siatki w ustalonym przedziale i zwiększenie przedziału z dopuszczonym kernelem. To bada dwie różne przyczyny błędu.
2. **Momenty gatunkowe zamiast pełnego widma:** dla każdego rodzaju pierwotnego zbierać średnie liczebności π±, K±, K0L, p/pbar i n/nbar z ustaloną konwencją. Dla nieujemnych gęstości całkowanie po energii wtórnej można przenieść przed splot z widmem Hawkinga. Jest to standardowa zmiana kolejności całkowania, nie nowy mechanizm fizyczny.
3. **Konwencję rozpadów i normalizacji:** jawnie ustalić, które cząstki są zachowywane jako metastabilne, liczenie par wobec pojedynczej cząstki oraz rozdział znaków. Archiwalny skrypt up zlicza oba znaki; nie wolno z tego wyprowadzać bez odczytu użytych tabel ani poprawności, ani błędu współczynnika 2 w obecnym wykonawcy.
4. **Ogon:** dane lub dopuszczona obwiednia dla brakującej energii, osobno dla gatunków; błędy Monte Carlo i kwadratury raportować oddzielnie od błędu modelu hadronizacji.
5. **Dopiero następnie:** przekazać δS_h do już istniejącego certyfikatu populacje→A/B→X_n→cel. Porównanie E0 z nowym obciętym wynikiem samo nie ustala błędu fizycznego ani jego znaku.

Metoda momentów usuwa potrzebę budowania i przechowywania pełnego histogramu energii wtórnej dla tego konkretnego celu. Nie usuwa kosztu generowania zdarzeń ani konieczności uzasadnienia wysokoenergetycznej hadronizacji. Nie mierzono przyspieszenia. Przy reakcjach zależnych od energii pełne widmo może ponownie stać się konieczne.

### 7a. Włączenie późniejszej korekty Rec9: jawna mapa wykonawcy

Rec9 wskazał konieczność odróżnienia pięciu kolumn generatora od sześciu źródeł populacji reakcyjnych. Odczyt `main-scan.jl`, blob `b368ba55d5a493f7bc185909730f7fe5691f10d6`, pozwala zamrozić mapę samego wykonawcy. Nie zależy ona od rozstrzygnięcia fizycznej normalizacji kolumn.

Dla wektora szybkości na jeden PBH Q=(Q_pipm,Q_Kpm,Q_K0L,Q_proton,Q_neutron) nominalne źródła gęstości wynoszą S=n_PBH B_exec Q, gdzie:

| Wiersz S | Q_pipm | Q_Kpm | Q_K0L | Q_proton | Q_neutron |
|---|---:|---:|---:|---:|---:|
| π− | 1 | 0 | 0 | 0 | 0 |
| π+ | 1 | 0 | 0 | 0 | 0 |
| K− | 0 | 1 | 0 | 0 | 0 |
| K0L | 0 | 0 | 1 | 0 | 0 |
| pbar | 0 | 0 | 0 | 1 | 0 |
| nbar | 0 | 0 | 0 | 0 | 1 |

Czynnik n_PBH jest konieczny jednostkowo: Q jest szybkością produkcji na obiekt, S źródłem gęstości. Macierz opisuje nominalne wstrzykiwanie **przed** efektem podłogi logarytmicznej. Dla reprezentowanej populacji surowy wykonawca stosuje dodatkowo diag(α_h), α_h=min(1,n_h/ε). Jest to osobna, zależna od stanu część modelu.

Jedna niepewność Q_pipm zasila oba wiersze pionowe. Dla ustalonych liniowych wag populacji L wkład tej kolumny sumuje wagi L_pi−+L_pi+; nie tworzy dwóch niezależnych losowych źródeł. Zamrożona macierz jest wykonawczym odczytem kodu. Nie dowodzi fizycznej poprawności przypisania kolumn zbiorczych do znaków/antycząstek. Nie wprowadzono żadnej poprawki o czynnik 2.

Dodany test kontroluje macierz i jej transpozycję. Nadal obowiązują korekty Rec9: wspólny model pierwotny i normalizacja dla łączonych donorów oraz odrębna kontrola zmiany kernela/ścieżki w pełnej dynamice. XH025 jest mapą kandydatów na komponenty źródła, nie gotowym E2b.

## 8. Assumption ledger i granica dowodu

| Twierdzenie | Założenie | Status |
|---|---|---|
| Zakres rzeczywistego wywołania | odczyt notebooka, właściwy blob | PROVED_SOURCE |
| B_exec dla nominalnych źródeł | właściwe jednostki, przed podłogą logarytmiczną | PROVED_EXECUTOR |
| Nieoznaczony ogon nie wynika z danych na przedziale | brak dodatkowego ograniczenia kernela | PROVED |
| Dodatni obcięty splot jest dolnym ograniczeniem | ten sam dokładny nieujemny kernel | PROVED_CONDITIONAL |
| Obcięcie może zmienić nachylenie | zadane widmo GO i potęgowa liczebność | PROVED_IN_DECLARED_MODEL |
| Podane procenty pominięcia | GO, bezmasowość, δ=0.3, stały zakres energii | COMPUTED_SURROGATE_ONLY |
| Taki efekt wyjaśnia rzeczywisty wykładnik −1.20 | rzeczywiste greybody i gatunkowy kernel | UNPROVED |
| Wartości E2 poniżej 1e9 g | rzeczywisty dopuszczony run | NOT_RUN |
| Fizyczne source error bars i ich znak | dopuszczony model niepewności | UNPROVED |
| Cel Yp/D-H, B2 i K_PBH | dalsze bramki źródła, tła, dynamiki i obserwabli | OPEN / K_PBH UNDEFINED |

Osiem grup kontroli wykonanych: odczyt parametrów i tabeli; B_exec i jej transpozycja; rozkład całki na trzy przedziały; niezależna kontrola analitycznej całki Bose/Fermi; pochodna analityczna wobec różnicy skończonej; dokładny ogon Boltzmanna; kontrprzykład nachylenia; dodatnia różnica dwóch uzupełnień kernela. Maksymalna różnica pochodnej ≈5.99e−11. Kontrole rachunku nie są recenzją fizycznej adekwatności modelu.

## 9. Prior art i decyzja końcowa

Wu–Xu, §4.1 i rys. 2, sami opisują problem limitu energii przy małych masach; podają też splot źródła z liczebnością wtórną i przybliżenie optyki geometrycznej. Appendix C dokumentuje implementację PYTHIA. BlackHawk v2 opisuje zakres i parametry tabel hadronizacji oraz potrzebę przeliczenia tabel przy ich zmianie. Ograniczenie źródła nie jest odkryciem IW. [P1–P2]

Wkład tego obrotu to odtworzenie konkretnego wywołania, wykonalny rachunek obcięcia i nachylenia, oraz zawężenie drogi walidacji tak, by nie pomylić ponownego użycia tego samego ograniczenia z niezależnym wynikiem. Wszystkie użyte narzędzia matematyczne są standardowe. **Nie formułuje się novelty claim.**

**NARROW:** E2 przez niezmieniony generator nie jest obecnie wystarczającą walidacją. E2 z kontrolą zakresu i gatunkowych momentów pozostaje otwartą, konkretną drogą. Certyfikat SW dla dalszej propagacji błędów jest zachowany. Nie ustanowiono nowego ograniczenia PBH/BBN, stabilności fizycznej, canon, EXEC_SIGN ani REV021.

### Źródła publiczne

- [P1] Wu–Xu, arXiv:2509.05618v2, §4.1 i Appendix C: https://arxiv.org/html/2509.05618v2
- [P2] Arbey–Auffinger, BlackHawk v2, §2.2, §2.5 i opis parametrów: https://doi.org/10.1140/epjc/s10052-021-09702-8
- [C1] Generator: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/valid_hadrons_from_BlackHawk.ipynb
- [C2] Wrapper: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-BlackHawk_extension.jl
- [C3] Tabela: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/data/out/hadrons_from_PBH.dat
- [C4] Interpolator: https://github.com/Fenyutanchan/Primordial-Black-Hole/blob/d395183674cace6c9906a8911bdeb7234ba4040d/arXiv-2509.05618/tool_script-hadrons_from_PBH.jl

Dokładne pochodzenie pozostałych plików i wejść projektu: `source_ledger.json`. Kod i pełne wyniki liczbowe: `source_support_audit.py`, `audit_results.json`.
