# IW / M13 — ROT14: pełnorankowy aktuator nie przywraca skalarnej dekompozycji błędu informacji i działania

**RETURN_ID:** `M13-ROT14-LT5-FULL-PORT-VECTOR-TARGET-POSTERIOR-GEOMETRY-001_20261021`  
**Komórka:** `IW_MGPT_BUD_02_BUD_01_BUD_01_BUD_01_SUCCESSOR_08 / M13`  
**Data:** 2026-10-21  
**Klasa:** ścisły skończeniewymiarowy kontrprzykład i rozwiązanie minimaksowe; host: klasyczne set-membership optimal recovery / robust output feedback / geometria Chebysheva.  
**Status:** `[▷] EXACT_ABSTRACT / HOST_ABSORBED / INDEPENDENT_REVIEW_NOT_ASSERTED / NO_CANON / NO_EXEC_SIGN / NO_NOVELTY / NO_PHYSICAL_UPGRADE / NO_NEW_TASK`.

## 0. Aktualność, właściciele i odjęcie istniejącego wyniku

Stan odczytany 2026-10-21: M13 ROT13 z 2026-10-19 zakończył analizę dokładnego progu stabilności okresowego sensora oraz podziału norm szumu l2/linfty. Nie powielamy ROT07–ROT13. LT5, jako właściciel Living Theory, opublikował `LT5-SCALAR-AMPLITUDE-LIMITED-OUTPUT-FEEDBACK-001_20261021`, którego twierdzenie mówi dla skalarnego celu, centralnie symetrycznych wypukłych zbiorów i scalar corrective interval [-B,B]:

    J_scalar*(B) = max{E, A-B}.

LT5 sam wykazał, że wektorowy cel z jednowymiarowym portem nie podlega tej formule. ROT14 *nie* poprawia twierdzenia skalarnego. Wzmacnia granicę transferu: porażka wzoru utrzymuje się nawet z pełnym, dwuwymiarowym, izotropowym portem sterowania, czyli nie może być przypisana samej niepełnej przestrzeni kierunków aktuatora.

Główne źródło: https://github.com/wmakiela-tech/Nash-iw-research/blob/b8bd36a4b2224b4f560eb14d1172634cb14b74f5/research/lt5/2026-10-21/lt5_scalar_target_amplitude_limited_output_feedback_minimax_decomposition_001.md

## 1. Nośnik i dokładny eksperyment

Niech K=[-1,1]^2 w R² będzie zwarty, wypukły i centralnie symetryczny. Niech pomiar będzie dokładny:

    y=(s,t) in K;  b=C y=s,  C=[1 0],  N={0}.

Cel to **cały wektor** M y=y w normie euklidesowej. Polityka sprzężenia zwrotnego może być dowolną mierzalną mapą u:[-1,1]->R², z twardym ograniczeniem ||u(s)||_2 <= B, B>=0. Terminalnie z=y+u(s). Port jest PEŁNYM rzędu 2: każdą składową można poprawiać, jedynie łączna długość korekty jest ograniczona.

    J*(B) = inf_{u, ||u(s)||<=B} sup_{s,t in [-1,1]} ||(s,t)+u(s)||_2.

Definiujemy naturalne, ale odrębne dolne granice wektorowe:

    E_vec=max_{v in K, C v=0} ||v||_2=1;
    A_vec=max_{y in K} ||y||_2=sqrt(2);
    D_act=max_{y in K} dist(-y, closed_ball(0,B))=max(sqrt(2)-B,0).

`E_vec` jest pasywnym promieniem informacji przy symetrycznych włóknach, zaś `D_act` to dolna granica niedoboru sterowania dla doskonale znanego stanu. Nie zakładamy, że ich maksimum jest osiągalne dla pojedynczej polityki przy częściowej obserwacji.

## 2. Dokładne twierdzenie i dowód

**Twierdzenie ROT14.1.** Dla każdego B>=0:

    J*(B) = sqrt(1 + max(1-B,0)^2).

**Dowód.** Ustalmy wynik pomiaru s. Zbiór możliwych celów jest pionowym odcinkiem P_s={(s,t): -1<=t<=1}. Dla dowolnej korekty u=(u_1,u_2):

    max_{|t|<=1} ||(s,t)+u||_2²
      = (s+u_1)² + max_{|t|<=1}(t+u_2)²
      = (s+u_1)² + (1+|u_2|)².

Dla każdej dopuszczalnej pary (u_1,u_2) para (u_1,0) również jest dopuszczalna i słabo zmniejsza powyższy błąd, zatem optimum warunkowe ma u_2=0. Minimalizacja po |u_1|<=B wybiera u_1=-clip(s,-B,B); dokładna wartość warunkowa to

    j_B(s) = sqrt(1 + max(|s|-B,0)^2).

Największą wartość dla |s|<=1 otrzymujemy przy |s|=1, więc

    J*(B) = max_s j_B(s) = sqrt(1+max(1-B,0)^2).

Zawarta w dowodzie jawna polityka

    u*(s)=(-clip(s,-B,B),0)

jest ciągła i spełnia ograniczenie normy. Kwantyfikatory `inf_policy sup_state` zostały zachowane: korekta zależy od s, nie od niewidocznego t. QED.

## 3. Silniejszy brak dekompozycji niż świadek LT5

Dla 0<B<1:

    J*(B) = sqrt(1+(1-B)^2) > 1 = E_vec,

oraz

    J*(B)^2 - (sqrt(2)-B)^2 = 2B(sqrt(2)-1) > 0.

Zatem J*(B)>max(E_vec,D_act). `max(E_vec,A_vec-B)` daje to samo słabsze ograniczenie dla 0<B<1, ale nie wartość minimaksu.

Przy B=1/2:

    E_vec=1;
    A_vec=sqrt(2);
    D_act=sqrt(2)-1/2 = 0.914213562373...;
    naive max(E_vec,A_vec-B)=1;
    actual J*(1/2)=sqrt(5)/2=1.11803398875... .

Różnica nie jest artefaktem rank-deficient port: V=closed_ball_R²(0,B) ma pełny wymiar i wszystkie kierunki. Włókno P_s jest niezerowo rozległe w kierunku ortogonalnym do s; symetria t↔-t wymusza optymalne u_2=0, więc cały użyteczny budżet może redukować tylko zaobserwowane s. Informacyjny promień i punktowy niedobór aktuacji stają się sprzężone przez normę euklidesową, zamiast układać się w skalarne maksimum dwóch stałych.

Dla B>=1 optymalny wybór u=(-s,0) daje dokładnie J*=E_vec=1. Odrębna skalarna formuła LT5 pozostaje nienaruszona na swoim legalnym typie.

## 4. Falsyfikatory, host i kwalifikacja

- Kontrprzykład pozostaje prawdziwy przy zero noise i bez back-action: nie opiera się na korelacjach szumu, nielegalnym porcie, ograniczeniu wzmocnienia liniowego ani złym timingu.
- Wektorowa geometra celu jest istotna; zastąpienie normy euklidesowej normą maksimum może zmienić funkcję optimum. Wynik nie jest uniwersalny po wszystkich normach.
- Kontrola B=0: J*=sqrt(2)=A_vec. Kontrola B=1: J*=1=E_vec. Zachowanie 0<B<1 dowiedzione nierównością kwadratów, nie wnioskiem z siatki.
- Bliski host: klasyczna geometria Chebysheva posterior uncertainty sets, deterministic optimal recovery i output-feedback set membership (takie same rodziny jak wskazane przez LT5). Nie przypisujemy matematycznej nowości ani prawa fizycznego.
- Dla ogólnego wektorowego celu jawny poprawny punkt wyjścia to `sup_b inf_{v in V} sup_{z in M K_b} ||z+v||`, z rozdzieleniem legalnego obrazu aktuatora V od posterior target set. Nie zastępujemy go formułą max(E,A-B) bez dodatkowych hipotez.
- Dla równości z estymatorem przy nieskończonych zbiorach i dla wersji kwantowych konieczne są nowe, typowane warunki; tu ich nie postulujemy.

## 5. Źródła wewnętrzne i dyscyplina statusu

- LT5, 2026-10-21, tytuł i GitHub powyżej, szczególnie twierdzenie LT5-2.1 i jego wektorowy kontrprzykład o **jednowymiarowym** porcie.
- LT5, 2026-10-20, `LT5-TARGET-INFORMATION-VS-ACTUATION-EXACT-GATE-001`, limit wzmocnienia liniowego: https://github.com/wmakiela-tech/Nash-iw-research/blob/ee4a54651106ca2e150e6795f5d258b3842e9d2c/research/lt5/2026-10-20/lt5_target_information_vs_actuation_bounded_feedback_exact_gate_001.md
- M13 ROT13, 2026-10-19, inna figura i normy szumu: https://github.com/wmakiela-tech/Nash-iw-research/blob/123b3e811dc2a90aed917d85e82b3326a617805f/research/m13/2026-10-19/IW_M13_ROT13_fixed_cycle_schur_threshold_noise_norm_split_001.md

**DO NOT INFER:** J3/K physical observables; alpha_Nash; PBH/BBN endpoint; experimental prediction; novelty; theory promotion.

**ROUTE_TAGS:** IWTO_LT5 IWTO_MT13 IWTO_INT8 IWTO_SW IWTO_REC10 IWTO_MODERATOR.

**STATUS:** `EXACT_CLASSICAL_FINITE_DIMENSIONAL / VECTOR_FULL_PORT_COUNTEREXAMPLE / LT5_SCALAR_THEOREM_UNCHANGED / HOST_ABSORBED / NO_CANON / NO_EXEC_SIGN / NO_NEW_TASK / TPE_HOLD`.
