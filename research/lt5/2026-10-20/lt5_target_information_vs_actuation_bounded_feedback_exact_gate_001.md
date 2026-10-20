# LT5 Research Note 001 — Informacja o celu a możliwość jego zmiany: ścisła bramka sterowania z ograniczonym wzmocnieniem

Data: 2026-10-20.
Linia: IW_LIVING_THEORY_LINEAGE_002_SUCCESSOR_03 / LT5.
Ekspozycja: PUBLIC_SAFE (samodzielne sformułowanie, bez prywatnych danych/modeli i bez prywatnego manuskryptu).
Status naukowy: EXACT_CONDITIONAL_DERIVATION / HOST_ABSORBED_STRUCTURAL_EXAMPLE / INDEPENDENT_REVIEW_PENDING. NO_CANON / NO_EXEC_SIGN / NO_NOVELTY_CLAIM / NO_PHYSICAL_VALIDATION.

## 1. Problem naukowy

Zdolność określenia skalarnego celu końcowego na podstawie pomiarów nie oznacza zdolności doprowadzenia celu do zera przez fizycznie ograniczoną interwencję. Rozważamy najprostszy sprawdzalny most od funkcjonalnej obserwowalności i optimal recovery do sterowania wyjściowego o ograniczonym wzmocnieniu. Nie zakładamy, że obserwacja jest automatycznie fizyczną supermapą lub nieinwazyjnym pomiarem kwantowym.

## 2. Legalny nośnik i definicje

Wszystkie przestrzenie są rzeczywistymi euklidesowymi przestrzeniami skończenie wymiarowymi; używamy normy 2 i jej indukowanej normy operatorowej.

Stan przygotowania ukrytego y należy do R^n, ||y|| <= R, R > 0. Pojedyncza paczka obserwacji przed sterowaniem ma postać

    b = C y + eta,   C : R^n -> R^p,   ||eta|| <= delta,   delta >= 0.

Interesuje nas skalarna *odchyłka od znanego deterministycznego celu* po sterowaniu

    z = m^T y + a^T u,

gdzie m należy do R^n, a do R^q i a oznacza dokładnie znaną czułość terminalną na sterowanie u w chwili podjęcia działania. Zakładamy brak innej zależności od u i brak fizycznego back-action samego odczytu przed zdefiniowaną interwencją. Dopuszczone są wyłącznie statyczne liniowe reguły

    u = -F b,  F : R^p -> R^q,  ||F||_op <= kappa.

kappa >= 0 jest ograniczeniem *wzmocnienia sterownika*, NIE ograniczeniem maksymalnej wartości impulsu ani energii aktuatora. Wynik nie dotyczy bez dodatkowego dowodu ogólnych polityk nieliniowych, aktywnych czujników, nieznanego a, ograniczeń trajektorii ani modeli kwantowych.

Definiujemy gwarantowany błąd fizycznego celu

    J_kappa = min_{||F||<=kappa} max_{||y||<=R,||eta||<=delta} |m^T y - a^T F(Cy+eta)|.

## 3. Twierdzenie: dokładnie ograniczona dostępność korekty

Jeśli a != 0, to

    J_kappa = min_{||w||<=kappa ||a||} [ R ||m-C^T w|| + delta ||w|| ].     (1)

Jeśli a = 0, to J_kappa = R ||m|| dla dowolnego kappa.

Dla porównania, bez ograniczeń aktuatora i przy pełnej swobodzie liniowego estymatora minimalny minimaksowy błąd pasywnej estymacji m^T y z b wynosi

    E_passive = min_{w in R^p} [R ||m-C^T w|| + delta ||w||].               (2)

Zatem zawsze J_kappa >= E_passive. Dla a != 0 równość zachodzi wtedy i tylko wtedy, gdy kula ||w||<=kappa||a|| zawiera przynajmniej jeden minimizer problemu (2). W szczególności informacyjna wystarczalność pomiaru nie implikuje osiągalności zerowego błędu po fizycznym działaniu o ograniczonym wzmocnieniu.

Dowód. Dla danego F wprowadźmy w=F^T a. Wtedy z=(m-C^T w)^T y - w^T eta. Niezależna, centralnie symetryczna niepewność dwóch kul daje dokładnie (nie tylko górne oszacowanie)

    max |z| = R ||m-C^T w|| + delta ||w||,

ponieważ wektory y i eta można wybrać zgodnie z odpowiadającymi funkcjonałami, a znaki można uzgodnić. Z ||F||<=kappa wynika ||w||<=kappa||a||. Odwrotnie dla a != 0 i każdego takiego w operator F=a w^T / ||a||^2 spełnia F^T a=w i ||F||=||w||/||a||<=kappa. Zbiór dopuszczalnych w jest więc dokładnie kulą w (1). Dla a=0 sterowanie nie zmienia z. Równość z (2) przy ograniczeniu wynika z ciągłości i istnienia minimizera funkcji wypukłej; w nieskrępowanym problemie istnieje minimizer także przy delta=0 (odległość od domkniętej przestrzeni ran C^T). QED.

Granica twierdzenia: ten rachunek jest specjalizacją elementarnej wypukłej dualności, klasycznego optimal recovery i output-feedback robust control. Nie jest przedstawiany jako nowa rodzina twierdzeń ani nowe prawo fizyczne.

## 4. Dynamika źródłowa: oscylator z pomiarem i jedną legalnie zadeklarowaną interwencją

Dla t < t_s mamy x'=y, y'=-x, x(0)=0, |y(0)|<=R. W chwili t_s najpierw mierzymy b=x(t_s^-)+eta, |eta|<=delta, a następnie wykonujemy impuls

    x(t_s^+)=x(t_s^-),   y(t_s^+)=y(t_s^-)-k b,   |k|<=kappa.

Po impulsie układ ponownie spełnia x'=y, y'=-x aż do T. Rozwiązanie daje:

    b = sin(t_s) y(0) + eta,
    x(T) = sin(T) y(0) - k sin(T-t_s) [sin(t_s)y(0)+eta].

Jest to przypadek (1) z n=p=q=1, C=sin(t_s), m=sin(T), a=sin(T-t_s), F=k. Minimalny błąd końcowy jest więc dokładnie

    min_{|k|<=kappa} [R |sin(T)-k sin(T-t_s) sin(t_s)| + delta |k sin(T-t_s)|].   (3)

### Świadek A — pełna identyfikacja celu, ale niewystarczająca siła interwencji

Weź T=pi/2, t_s=pi/4, R=1, delta=0, kappa=1. Pomiar b=y(0)/sqrt(2) determinuje y(0), więc pasywna rekonstrukcja skalarnego celu x(T)=y(0) jest dokładna: E_passive=0. Jednak fizycznie dozwolony pojedynczy impuls daje

    J_1=min_{|k|<=1}|1-k/2|=1/2.

Jeśli zwiększyć dopuszczalne wzmocnienie do kappa=2, k=2 daje dokładnie J_2=0. Wniosek nie dotyczy dowolnych aktuatorów, tylko podanego portu i ograniczenia.

### Świadek B — pełna identyfikacja, ale zero terminalnej czułości aktuatora

Weź T=3pi/2, t_s=pi/2, R=1, delta=0. Pomiar jest b=y(0) i odtwarza cel bez błędu. Jednak sin(T-t_s)=sin(pi)=0, więc impuls na y w chwili t_s nie zmienia x(T). Dla każdego kappa: J_kappa=1, E_passive=0. To świadek źle wybranego czasu i portu aktuatora, nie brak informacji.

### Test kontrolny szumu

Dla T=pi/2, t_s=pi/4, R=1 i delta=0.1 z (3):
- kappa=0: J=1;
- kappa=1: optimum k=1, J=0.5+0.1/sqrt(2)=0.5707106781186548;
- kappa=2: optimum k=2, J=sqrt(2)*0.1=0.1414213562373095.
Dla delta=0.8 i kappa=2 optymalny jest k=0, J=1 (szum jest zbyt kosztowny względem użytecznej informacji).

Liczby zweryfikowano niezależnie przez siatkę k w [-3,3] o kroku 10^-4 i porównanie ze wzorem dokładnym; test numeryczny nie zastępuje dowodu.

## 5. Najsilniejsi gospodarze i odejmowanie nowości

(a) Klasyczne optimal recovery funkcjonału z błędnymi obserwacjami i formuła dualna; M. Ettehad, S. Foucart, *Instances of Computational Optimal Recovery: Dealing with Observation Errors*, SIAM/ASA JUQ 9 (2021), 1438–1456, DOI https://doi.org/10.1137/20M1328476.

(b) A.B. Kurzhanski, P. Varaiya, *Optimization of Output Feedback Control Under Set-Membership Uncertainty*, Journal of Optimization Theory and Applications 151 (2011), DOI https://doi.org/10.1007/s10957-011-9861-z. Rodzina właściwych problemów obejmuje ograniczenia sterowania, bounded disturbances i horyzont skończony.

(c) A.N. Montanari, C. Duan, A.E. Motter, *Duality between controllability and observability for target control and estimation in networks*, https://arxiv.org/abs/2401.16372. Badana jest celowa/functional obserwowalność i wyjściowa sterowalność; obecnego przykładu nie wolno przedstawiać jako odkrycia dualności.

(d) Aktualny szerszy kontekst: J. Wehbeh, E.C. Kerrigan, *Robust Output Feedback of Nonlinear Systems through the Efficient Solution of Min-Max Optimization Problems*, https://arxiv.org/abs/2409.08684. Pokazuje, że rzeczywiste ograniczenia i set-membership są już przedmiotem dojrzałych metod optymalizacji.

Po odjęciu gospodarzy: (1) jest ścisłym, użytecznym pedagogicznie i metodologicznie szczególnym przypadkiem, ale NOWOŚĆ MATEMATYCZNA NIEUSTALONA, wstępnie HOST-ABSORBED. Świadkowie A/B pokazują na wspólnym, legalnym nośniku różnicę między przewidzeniem a fizyczną korektą końcowego celu.

## 6. Co pozostaje otwarte i falsyfikator ambicji

Materiał nie dowodzi osiągalności dowolnego celu przy niedostępnym porcie ani optymalności liniowych reguł dla ogólnych interwencji. Rzeczywiste pytanie po subtraction: przy fizycznie określonych kosztach i ograniczeniach impulsu (amplituda, energia, opóźnienie, zaburzenie pomiarowe), kiedy dopuszczalny adaptacyjny protokół ma wynik ściśle inny od biernego optimal recovery, i czy tę różnicę można ograniczyć dla pełnej dynamiki, nie tylko dla liniowej czułości?

Kill-test dla rozbudowy: jeśli nowy claim sprowadza się po zmianie zmiennych do (1), klasycznego robust output-feedback lub standardowej separacji obserwacji/sterowania, należy go oznaczyć KNOWN_HOST i nie rozwijać pod szyldem nowej teorii. Nowa fizyka wymaga jawnego, walidowanego modelu źródłowego i legalnej klasy pomiarów/aktuatorów.

## 7. Status pracy

- Derivation: własny rachunek w skończonym wymiarze, algebraicznie sprawdzony.
- Computational check: tylko syntetyczny test oscylatora, bez fizycznej walidacji.
- Prior art: identyfikacja właściwych rodzin i reprezentatywnych publikacji; NIE pełny globalny survey twierdzenie-po-twierdzeniu.
- Independent mathematical referee: PENDING.
- Scientific claims ceiling: exact conditional specialization, illustrative counterexample; no novelty, no CANON, no EXEC.
- Manuscript decision: NIE wstawiać jako nowego odkrycia; ewentualnie zwięzły pomost w części o kosztach interwencji po odrębnej recenzji i redakcji.
