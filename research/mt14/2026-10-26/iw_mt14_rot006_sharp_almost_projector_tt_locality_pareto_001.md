---
artifact_id: IW_MT14_ROT006_SHARP_ALMOST_PROJECTOR_TT_LOCALITY_PARETO_001_20261026
created_at: 2026-10-26
origin_cell: IW_MT_SUCCESSOR_13 / MT14
problem_id: P3_DTC0A_SOURCE_TYPED_RAW_TT_PROJECTOR_LOCALITY_AND_APPROXIMATE_IDEMPOTENCY
exposure: PUBLIC
sync_state: GITHUB_PENDING_BW_INGEST
status: EXACT_SOURCE_TYPED_SHARP_PARETO_THEOREM / TWO_INDEPENDENT_ALGEBRA_AND_NUMERIC_CONTROLS_PASS / REFEREE_PENDING
claim_ceiling: NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_J3_K / NO_MASKED_KA / NO_EVEN_N / NO_NONSELFADJOINT_EXTENSION
---

# MT14 ROT006 — dokładne optimum przybliżenia TT dla lokalnych prawie-projektorów

## Właściciele źródeł FIRST / brak roszczenia do nowości

INT8 ROT034 FIRST dowiódł dla tej samej nieparzystej przestrzeni źródłowego surowego TT: każdy nawet niesamosprzężony translacyjny DOKŁADNY idempotent F o błędzie ||F-P||<1 wymaga pełnego podparcia N^3 przesunięć; przy dowolnym właściwym podparciu optimum projektorowe wynosi 1. Również INT8 ROT034 FIRST wykazał dla NIEIDEMPOTENTNEJ ogólnej klasy translacyjnej z promieniem R_N=o(N) asymptotyczne optimum 1/2, osiągane przez F=I/2. Matematyczny i źródłowy raport właściciela:
https://github.com/wmakiela-tech/Nash-iw-research/blob/93e0be3d74cc63aa7d39572818dafdb38ceb143f/research/int8/2026-10-26/iw_int8_rot034_sharp_full_kernel_tt_locality_projector_minimax_001.md

INT8 ROT033 FIRST ma źródłowo odrębną metrycznie indeksowaną transportowaną rodzinę P_g; MT13 FIRST bada interfejs płaskiego E_g i alias surowego k, Geeky-S11 even-grid rawcast, M13 historycznie maskowane K_A. Tutaj żadnych tych granic nośnika nie przekraczamy.

Zewnętrzny dojrzały matematyczny host: luka spektralna samosprzężonego prawie-idempotentu, nierówność Weyla, klasyczna nierówność Bernsteina ||t'||∞<=R||t||∞ dla wielomianów trygonometrycznych stopnia R. Przykład naukowego omówienia tej ostatniej: https://link.springer.com/article/10.1007/s00041-024-10080-4 . Brak wyczerpującego zewnętrznego prior-art search, NO NOVELTY CLAIM.

## Zamrożony legalny eksperyment

N=2m+1 >=3 NIEPARZYSTE. G_N=(Z/NZ)^3. V_N to WSZYSTKIE symetryczne 3x3 pola na siatce z płaskim iloczynem Frobeniusa/L2. P=P_N jest ORTOGONALNYM dokładnym źródłowym projektorem Fourier TT o rangach symbolu: rank Phat(0)=5 (zero-mode tracefree), rank Phat(k)=2 dla KAŻDEGO niezerowego k. Zatem P=P*=P² i ||P||=1.

Aproksymant F jest realny, translacyjnie niezmienniczy i SAMOSPRZĘŻONY (zatem każdy jego symbol hermitowski). Jego jądro splotowe ma zakres tylko w kierunku x ograniczony do |d_x|<=R<m; w pozostałych kierunkach może być nielokalne. To słabszy warunek od kostki lokalnego stempla. Wszystkie błędy w pełnej operatorowej normie L2, nie maskowany RMS i nie tylko wejścia TT.

Kontrolujemy defekt idempotentności ||F²-F|| <= delta przy 0<=delta<1/4.

## T006 — OSTRE DOKŁADNE OPTIMUM

Niech tau=(1-sqrt(1-4delta))/2. Jeżeli dla całkowitego R>=0 zachodzi

   R/N < (1-2tau)/[pi*(5-4tau)]
       = sqrt(1-4delta)/[pi*(3+2sqrt(1-4delta))],        (1)

to

   min ||F-P|| = 1-tau = (1+sqrt(1-4delta))/2            (2)

w dokładnie wskazanej klasie. Osiąga je punktowo lokalny operator F=tau I (R=0), ponieważ ||F²-F||=tau(1-tau)=delta i ||tau I-P||=max(tau,1-tau)=1-tau. Nie jest to tylko asymptotyczny dolny kres.

### Dowód, część I: nieusuwalny skok spektralny

Załóżmy e=||F-P||<1-tau. Ponieważ F jest samosprzężony i ||F²-F||<=delta<1/4, jego wszystkie rzeczywiste wartości własne na KAŻDYM trybie należą do dwóch rozdzielonych pasm lambda<=tau lub lambda>=1-tau. Różnica pomiędzy pasmami wynosi 1-2tau.

Przez porządek Weyla i e<1-tau, liczba wartości własnych w wysokim paśmie dla Fhat(0) MUSI być 5 (jak rank P0), zaś dla Fhat((1,0,0)) MUSI być 2. W szczególności trzecie wartości własne (malejąco) spełniają

   lambda_3(Fhat(0))>=1-tau,
   lambda_3(Fhat(e_x))<=tau.

Zatem Weyl daje

   ||Fhat(0)-Fhat(e_x)||>=1-2tau.                       (3)

To jest dokładna przyczyna potrzeby samosprzężoności. NIE uzyskaliśmy takiej granicy dla ogólnych oblique F.

### Dowód, część II: lokalność wygładza symbol

Dla k_y=k_z=0 symbol A(theta)=Fhat(theta,0,0) jest hermitowskim wielomianem trygonometrycznym stopnia <=R. Dla każdej jednostkowej wektorowej polaryzacji v skalar v*A(theta)v spełnia klasyczną nierówność Bernsteina. Ponieważ każdy theta leży od najbliższej siatkowej theta_j w odległości <=pi/N,

   M_cont<=M_grid+(pi*R/N)M_cont,

gdzie M_grid=max_j||A(2pi j/N)||<=||F||<=1+e. Dla pi R/N<1 mamy

   M_cont<=M_grid/(1-pi R/N).

Na łuku 0->2pi/N otrzymujemy

   ||Fhat(0)-Fhat(e_x)||
      <= b_N*(1+e),
   b_N=(2pi R/N)/(1-pi R/N).                           (4)

Ale e<1-tau implikuje 1+e<2-tau, natomiast warunek (1) jest równoważny b_N*(2-tau)<1-2tau. To daje ścisłą sprzeczność (3) z (4). Zatem e>=1-tau, zaś świadek tau I osiąga równość. QED.

Warunek (1) jest DOSTATECZNY, nie dowodem optymalnego progu promienia; poza nim wynik nie orzeka, czy lepsza aproksymacja istnieje.

## Ilościowe konsekwencje

Przy każdym stałym delta<1/4 i R_N=o(N) warunek (1) zachodzi od pewnego N; optimum jest wówczas dokładnie 1-tau na wszystkich dostatecznie dużych nieparzystych siatkach.

Aby pokonać tę wartość błędu, lokalny operator tej klasy POTRZEBUJE co najmniej liniowego z N zasięgu pierwszej współrzędnej R/N >= sqrt(1-4delta)/[pi*(3+2sqrt(1-4delta))]. To konieczne, lecz nie wystarczające.

| delta | tau | ostry minimalny błąd | wystarczające R/N mniejsze niż |
|---:|---:|---:|---:|
| 0 | 0 | 1.000000000000 | 0.063661977 |
| 0.01 | 0.010102051443 | 0.989897948557 | 0.062883950 |
| 0.09 | 0.1 | 0.900000000000 | 0.055358241 |
| 0.16 | 0.2 | 0.800000000000 | 0.045472841 |
| 0.24 | 0.4 | 0.600000000000 | 0.018724111 |

delta=1/4 jest WYŁĄCZONE: luka spektralna znika, zaś punktowy I/2 osiąga wtedy defekt1/4 i błąd1/2, zgodnie z oryginalnym host INT8. Przy delta=0 jego EXACT full-support theorem pozostaje mocniejszy niż niniejszy wystarczający promień.

## Kontrole i reprodukcja

Samowystarczalny Moderatorski ZIP zawiera pełny 10KB raport po polsku, dwa niezależne programy, deterministyczny JSON, README i manifest SHA256SUMS. Nazwa MT14_ROT006_Almost_Projector_TT_Pareto_20261026.zip; SHA256 0d124086a15309b3955a6027b559d1f37bc27b277b8beb279a867334b3b23788.

- SymPy z dokładnymi liczbami wymiernymi niezależnie wylicza source-free P0 oraz Pe1, sprawdza rangę5/rangę2, idempotencję oraz polaryzację diag(2,-1,-1). 100 prób parametrycznych dla pięciu delta, pięciu nieparzystych N i czterech R; w 75 spełniony dostateczny warunek; żaden z pozostałych 25 nie jest fałszywie oznaczony jako dowiedzione optimum. Wszystkie 100 sprawdzają lokalną konstrukcję tau I. Pięć dodatkowych testów macierzowych polinomów trig kontroluje sampling/Bernstein.
- Niezależny drugi kod Python standard library fractions.Fraction, nieimportujący pierwszego, sprawdza dokładne projektory 6x6, rank5/2 i cztery wymierne pary defekt/świadek.
- Czysty katalog: ZIP CRC PASS, 5/5 sum SHA256 PASS, oba kody świeżo wykonane PASS, ponowny wynikowy JSON bajtowo identyczny PASS.
- Pierwszy test pomocniczy omyłkowo postulował, że macierze w wybranych nieortonormalnych współrzędnych muszą być niesymetryczne. Zbędny assert był fałszywy, usunięto; prawdziwe testy i dowód pozostały niezmienione. Błąd testu odnotowany.
- Oryginalnego produkcyjnego helpera DTC0a w tym obrocie NIE uruchamiano. Source-native oryginalne rangowe i FFT kontrole należą do INT8 ROT034. Dowód posługuje się zamrożonym dokładnym symbolem tego źródła.

## Falsyfikator / STOP

Obaliłby to LEGALNY samosprzężony translacyjnie niezmienniczy operator F, ze źródłowym N nieparzystym, delta<1/4, promieniem R/N spełniającym (1), a jednak ||F-P||<1-tau; albo błędna ranga5/2, luka spektralna, stała Bernsteina. Klasy even-N, niesamosprzężone F, historyczne maskowane K_A, inne metryki, mean-zero-only lub ograniczone wejścia TT, nieliniowe algorytmy i fizyczne J3/K są WYŁĄCZONE, nie obalone.

Jedna opcjonalna niezależna recenzja INT8/REC10 nad krokami Weyl/Bernstein/warunek promienia; autorstwo INT8 i dawnej matematyki zachowane. NO NEW TASK CASCADE. Nie domniemywać BW ingestion, kanonu, novelty ani EXEC.

STATUS: SHARP_SOURCE_TYPED_ALMOST_PROJECTOR_PARETO / TWO_INDEPENDENT_MATH_CHECKS_AND_CLEAN_REPLAY_PASS / REFEREE_PENDING / GITHUB_PENDING_BW_INGEST / NO_CANON / NO_NOVELTY / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
