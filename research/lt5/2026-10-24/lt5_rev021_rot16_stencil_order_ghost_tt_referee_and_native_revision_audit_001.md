# LT5 ROT16 — Audyt rzędu dyskretyzacji TT oraz aktualizacja roboczej REV021

Data: 2026-10-24
Typ: SOURCE-TYPED THEOREM AUDIT / INDEPENDENT_SYMBOL_VERIFICATION / NATIVE_EDITORIAL_INTEGRATION
Status: MATH_SOURCE_SPOT_CHECK_PASS / MANUSCRIPT_READBACK_PASS / REFEREE_PENDING / NO_CANON / NO_EXEC / NO_NOVELTY / NO_PHYSICAL_UPGRADE

Rękopis roboczy: https://docs.google.com/document/d/15b-8uK2DZVScU6k-K6eesL8d8nt777-UmalEUb5U-zE/edit
Oryginalna REV020: https://docs.google.com/document/d/1cn97_kO65BcJRRWQrvrL9fKlEYBT3PHg6BJItn1Q4FQ/edit

## 1. Nowy istotny wynik źródłowy

Oryginalny autor: Geeky-S11 ROT007, własny dowód i 96 niezależnych testów numerycznych:
https://github.com/wmakiela-tech/Nash-iw-research/blob/d348662c085456ed650e8d78d1b189e8673f6eba/research/geeky-s11/2026-10-24/geeky_s11_rot007_fourth_order_checkerboard_tt_falsifier_001.md
Źródłowy blob 1e92e85560c8c8f8183fc9f19bb0602b29467925.

Nowość dla rękopisu: rząd schematu może zniszczyć pewną dyskretną symetrię TT, CHOĆ w obu porównywanych nośnikach projektor jest zbudowany z symbolu odpowiedniej pochodnej. Nie jest to obalenie twierdzeń dotyczących ustalonych gładkich pól lub zbieżności wyższego rzędu.

Dla N podzielnego przez 8, h=2pi/N, definiujemy symbole różnic centralnych:
d2(theta)=sin(theta)/h,
d4(theta)=sin(theta)(4-cos(theta))/(3h).
Oba odpowiednie TT rzutniki są oznaczone P2/P4; Qr=I-Pr. Wspólne E_alpha=I+alpha*h^2*Delta2 jest filtrem z LAPLACJANEM DRUGIEGO RZĘDU, nawet dla D4. Generator szachownicowy C_N(j)=(-1)^(jx+jy+jz)*e_x jest grid-dependent i ma D2 C_N=D4 C_N=0. Mnożenie przez szachownicę przesuwa mod Fouriera o pełny Nyquist.

D2(theta+pi)=-D2(theta), stąd Q2 Lie_C^2 E_alpha P2=0 dla każdego alpha. Dla D4 iloraz d4(theta+pi)/d4(theta)=-(4+cos(theta))/(4-cos(theta)) zależy od współrzędnej; matching P4 nie zachowuje przesunięcia Nyquista.

Jawne dwa matched-P4-TT mody:
kA=(N/8,N/4,0), kB=(N/8,3N/8,0).
Dają normy wycieku:
N*A0*abs(1-(4-sqrt(2))*alpha), N*B0*abs(1-4*alpha),
A0=0.020444737111672044, B0=0.041723057420514936.
Ostrą dolną granicą MINIMAXU DWÓCH WSKAZANYCH ŚWIADKÓW jest c*=0.005489440114557819 przy alpha*=0.28289212520568247. Dlatego NORMA PEŁNEGO OPERATORA jest co najmniej c* N dla wszystkich rzeczywistych alpha, również N-dependent. OSTRY WSPÓŁCZYNNIK CAŁEJ NORMY OPERATORA NIE JEST DOWIEDZIONY.

## 2. Własna kontrola LT5, wyraźnie ograniczona

Niezależnie napisano konstrukcję symboli, tensorów T=vv^T-ez ez^T i rzutników ze znormalizowanym kierunkiem d. Sprawdzono TT przed mnożeniem i po przejściu k -> k+N/2, dokładny e_alpha z drugiego Laplacjanu oraz dwie formuły analityczne. 
N={8,16,24,32,64}, dwa pola A/B, dwa rzędy D2/D4, alpha={0,.05,alpha*,1/(4-sqrt(2)),.25}: 100/100 PASS, błędy podwójnej precyzji <3e-12.
Kontrola potwierdziła A0, B0, alpha*, c* oraz równowagę dwóch świadków przy N=32, 0.1756620836659 dla każdego. To NIE jest osobny pełny symulator 3D ani kontrola oryginalnego runnera DTC0a.

Kod LT5:
https://github.com/wmakiela-tech/Nash-iw-research/blob/6d86d4dcefd3d8a1d81467c3f00d585ac4762ace/research/lt5/2026-10-24/lt5_rev021_rot16_independent_matched_tt_order_crosscheck_v001.py

## 3. Weryfikacja granicy zastosowania M13

W części §4.11b zastąpiono skrócone ujęcie M13 ROT030 wersją z niezbędnymi hipotezami. Wynik pozytywny dotyczy periodycznej 2pi siatki ODD N>=13, pięciu masek k=2,3,4,5,6 i realnych symetrycznych tensorów TT niezależnych od y,z z pasmem |m_x|<=B<=2. Identyfikowalna jest GLOBALNA RMS, nie cały tensor. Dla B=3 istnieje para poprawnych TT, której pięć RMS maskowanych jest identycznych, mimo różnych RMS całego pola. Stabilność odwrotności nie wynika z samej jednoznaczności: raport N41 pokazuje L1 wektora wag odtwarzania około 31.659.
Źródło:
https://github.com/wmakiela-tech/Nash-iw-research/blob/df81d9f27225f70870eb70910085d6cfdb8636e9/research/m13/2026-10-24/IW_M13_ROT30_sharp_TT_bandwidth_mask_identifiability_001.md

## 4. Co faktycznie zmieniono w monografii

(1) Dodano §4.11c z dowodem-świadkiem rzędu 2 vs 4, dokładnymi ograniczeniami N, alpha, klasą operatorów i falsyfikowalnym pytaniem o nieprzypadkowe symetrie. 
(2) Doprecyzowano kwantyfikatory twierdzenia M13 w §4.11b i stabilność odtwarzania normy.
(3) Zaktualizowano notę otwierającą rękopis, odsyłając również do §4.11c.
(4) W istniejącym §7.5b poprawiono dawne style Heading 2 błędnie przypisane prozie, wzorom i lematom. Normalizowano 116 takich akapitów do zwykłego tekstu, a pięć właściwych podsekcji 7.5b.1–7.5b.5 ma nadal Heading 3. Treści dowodów nie zmieniono.

Bezpośredni Google Docs readback:
- źródłowe REV020: 1763 akapity;
- kopia robocza po obrocie: 1910 akapitów, 185542 znaków tekstu UTF-16;
- 1763/1763 akapitów REV020 pozostaje dosłownie i w tej samej kolejności;
- siedem oryginalnych rozdziałów, nowy §4.11c Heading 2;
- w §7.5b zero nadmiarowych Heading 2 i pięć zamierzonych Heading 3;
- notatka nie ustanawia finalnej autoryzacji REV021 ani praw fizycznych.

## 5. Pytania otwarte i stop

P1: scharakteryzować rodzinę różniczkowań i dopasowanych TT, dla której komutacja z checkerboard jest dokładna, a nie przypadkowa.
P2: rozdzielić zbieżność na ustalonych gładkich polach od rosnących norm pełnopasmowych dla C_N zależnego od N.
P3: oddzielnie potwierdzić naturalność metryczną, aliasing raw-k, granice masek i źródłowy runtime; nie przenosić ich na fizyczne J3/K.
P4: pełna niezależna recenzja Geeky i M13 oraz przegląd spójności numeracji i bibliografii wydania roboczego.

Gospodarz matematyczny: standardowa analiza Fouriera różnic centralnych, np. https://tobydriscoll.net/fd-spectral-notes/finite-diffs/fourier.html .
Nie uzyskano pochodnego twierdzenia o fizyce, nowości naukowej ani potwierdzenia historycznego DTC. Pełna matematyczna recenzja nowych fragmentów pozostaje otwarta.
