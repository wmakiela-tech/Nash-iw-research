---
artifact_id: IW_GEEKY_S12_ROT006_M13_B_UNIFORM_SMALL_DELTA_AND_SHARPENED_FAILURE_GATE_001_20261112
origin_cell: MGPT-BUD-01-SUCCESSOR-12 / Geeky-S12
created_at: 2026-11-12
exposure: PUBLIC
type: SOURCE_TYPED_NEW_QUANTIFIER_THEOREM_AND_FALSIFIER / INDEPENDENT_AUTHOR_RECHECK
science_status: EXACT_SOURCE_DIRECTED_RATIONAL_INTERVAL_CERTIFICATE_PASS / INDEPENDENT_REFEREE_PENDING / M14_OWNER_ADOPTION_PENDING
sync_state: GITHUB_PENDING_BW_INGEST
claim_ceiling: N41_M13_FUNCTIONALLY_MATCHED_AUXILIARY_FIVE_MASK_B_ONLY / NO_HISTORIC_PRODUCER / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE
---

# Geeky-S12 ROT006 — kanał B: ścisły bezpieczny zakres separacji (0,0,02] i bliższa falsyfikacja przy 0,026

## 0. Nowy wynik, bez mieszania kwantyfikatorów

Na DOKŁADNYM źródłowo dopasowanym pięciomaskowym profilu B z M13 N=41, przy jednym wspólnym dodatnim wzmocnieniu energii oraz ustalonych wagach pięciu rozłącznych powłok, udowodniono:

**Twierdzenie ROT006-A (przedział całkowicie bezpieczny):** DLA KAŻDEGO alpha∈[0,1/5] i DLA KAŻDEJ rzeczywistej delta spełniającej 0<delta<=1/50=0,02, pełne minimum globalne profilowanej odległości kwadratowej D_B²(alpha,beta), beta∈[0,1/5], |beta-alpha|>=delta, jest osiągane w JEDNEJ Z NAJBLIŻSZYCH DOPUSZCZALNYCH alternatyw beta=alpha±delta.

**Twierdzenie ROT006-B (ściśle bliższy falsyfikator ogólnego twierdzenia):** Dla exact rational alpha=4/125=0,032 i delta=13/500=0,026, oba najbliższe punkty beta_L=3/500=0,006 i beta_R=29/500=0,058 są ściśle GORSZE od dalszego **wewnętrznego** punktu beta_*=1/2000=0,0005, o odległości |beta_*-alpha|=63/2000=0,0315>0,026. Istnieje również negatywna kontrola beta=0.

Te twierdzenia nie są sprzeczne: wynik dodatni dotyczy ALL alpha i ALL delta≤0,02; wynik ujemny tylko przykładowej delta=0,026, co dowodzi, że **maksymalny bezpieczny promień** (jeśli definiować jako kres przedziału bezpiecznych delta od zera) jest nie mniejszy niż 0,02 i nie większy niż 0,026, bez dowodzenia dokładnej granicy ani monotoniczności własności w delta >0,02. Nie twierdzimy, że każde delta>0,026 jest złe. Zakres nieprzebadany leży pomiędzy dwoma rozstrzygniętymi punktami.

Wartość względem ROT005: twierdzenie dla FIXED delta=.01 zostaje rozszerzone do CAŁEGO rzeczywistego przedziału delta≤.02 — nie jest to skończona lista testów delta. Wartość względem ROT004: źródłowy kontrprzykład ogólnego ALL-delta twierdzenia przy delta=.035 zostaje zastąpiony bliższym przy .026, z dala od końca domeny także dla świadka beta=.0005.

## 1. Pierwszeństwo i źródło

M13 ROT32–40 pierwszy wyprowadził źródłowy profil pięciu masek N41, geometrię wspólnego dodatniego wzmocnienia, wagi rozłącznych powłok i certyfikaty A/C. M13 ROT40 pierwszy stwierdził FAKTYCZNĄ niemonotoniczność radialną B i pozostawił jego globalny nearest-endpoint problem OPEN. M13 ROT39 pierwszy certyfikował dokładnie delta=.01, dwupunktowe przełączenie stron w B przy alpha_B≈.03265254963589545. Geeky-S12 ROT004 pierwszy dostarczył B ALL-DELTA falsyfikator przy (.039,.035); ROT005 pierwszy domknął B FIXED delta=.01 całym dokładnym źródłowym certyfikatem. ROT006 rozszerza poprawne kwantyfikatory, nie przypisuje sobie prac M13/MT13.

Źródłowe prace:
- M13 ROT39: https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-25/IW_M13_ROT39_full5_nearest_alternative_side_switch_001.md
- M13 ROT40: https://github.com/wmakiela-tech/Nash-iw-research/blob/27188018c1dbbcee81d391ceb8ba5c55237cff7e/research/m13/2026-10-26/IW_M13_ROT40_universal_AC_radial_mask_global_argmin_001.md
- S12 ROT004: https://github.com/wmakiela-tech/Nash-iw-research/blob/a8f0497a8bff36d4d63b1cd8fa90f326e0673380/research/geeky-s12/2026-11-11/IW_GEEKY_S12_ROT004_M13_SOURCE_B_NON_NEAREST_GLOBAL_MINIMIZER_FALSIFIER_001_20261111.md
- S12 ROT005: https://github.com/wmakiela-tech/Nash-iw-research/blob/60d00bbf497c2384800588a85547920ca039ae16/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT005_M13_B_FIXED_DELTA001_GLOBAL_NEAREST_ENDPOINT_BERNSTEIN_CERTIFICATE_001_20261112.md

ORIGINAL IMMUTABLE SOURCE M13, 25 skierowanych przedziałowych współczynników kwartycznych g_{B,k}(alpha) dla k=2..6:
https://github.com/wmakiela-tech/Nash-iw-research/blob/main/research/m13/2026-10-26/direct_B.json
Git blob SHA-1: a6f50fbe5904e580e84c87ee87c5ad043cdec5d0.

Historia: oryginalny historyczny producent dtc0a_runtime_v0_3_1.py NIE został odzyskany byte-exact. M13 wskazał FUNKCJONALNIE DOPASOWANE źródło generatora pomocniczego: N41, C1=(.05sin x,.05cos y,0), C2=(.04cos z,0,.04sin x), h=.1sin x cos y I AMBIENT pure trace, drugi centralny stencil i płaski Fourier-TT. Source coefficients themselves are inherited and are NOT independently regenerated from the original trigonometric stencil in ROT006. All downstream interval inequalities ARE recomputed from this immutable public source body. No transfer to historic masked producer, measured noise, source physical tensor space or K/J3/TPE.

## 2. Matematyka profilowanej odległości

Niech maska k ma n_k=(41-2k)^3 voxeli, a pięć rozłącznych powłok ma wagi W=(7778,6938,6146,5402,24389). Niech s_i(alpha) oznacza średnią energię powłoki, wyznaczoną liniowo z oryginalnych quartic g_k. Wszystkie s_i mają dokładnie certyfikowane dodatnie dolne współczynniki Bernsteina na alpha∈[0,.2].

Dla a=s(alpha), b=s(beta), p=<a,b>_W, q=||b||_W², N=sum_(i<j) w_i*w_j*(a_i*b_j-a_j*b_i)²:
D_B²(alpha,beta)=||a||_W²-p²/q=N/q.
Dodatniość s_i daje p,q>0, więc optymalny wspólny gain t=p/q>0 jest legalny.

Dla H=2p_beta*q-p*q_beta, zachodzi d_beta D²=-pH/q².
Algebraicznie H=(alpha-beta)*P(alpha,beta), gdzie P jest wielomianem obliczonym ZAMIAST numerycznego dzielenia przez alpha-beta:
P=2*sum_(i<j) w_i*w_j Q_ij(alpha,beta)R_ij(beta),
Q_ij=[s_i(alpha)s_j(beta)-s_j(alpha)s_i(beta)]/(alpha-beta) — formalny podzielny wielomian,
R_ij=s_i'(beta)s_j(beta)-s_i(beta)s_j'(beta).
Tożsamość wynika z wyznaczników Gram; P ma stopień najwyżej (3,9) w (alpha,beta).
Wszystkie współczynniki liczone są ze skierowanych końców oryginalnych wielomianów przez dokładną arytmetykę wymiernych przedziałów.

Gdy P>0, znak pochodnej D² jest znakiem beta-alpha. To wystarcza do radialnego wniosku, ale ROT004 pokazał, że dla B P nie jest globalnie dodatni.

## 3. Ośmioczęściowy dokładny certyfikat ROT006-A

Używamy podziału beta według b_c=1/125=0,008 oraz alpha według a_c=7/250=0,028. Oryginalne końce skierowanych współczynników odczytano jako DOKŁADNE ułamki BigInt z dziesiętnych ciągów znaków (nie float). Potem formalna algebra wielomianów, przedziałowe mnożenie kwadratów, Horner i exact Bernstein transform.

**Trzy typy faktów, łącznie OSIEM ścisłych dodatnich testów:**

**(I) P>0 na beta∈[0,008,0,2] dla WSZYSTKICH alpha∈[0,0,2].** Pięć domkniętych prostokątów Bernsteina dokładnie pokrywa tę dziedzinę. Ich dodatnie dolne granice (przybliżenia tylko do prezentacji):
1. alpha∈[0,.1], beta∈[.008,.02]: +6817.992147847181.
2. alpha∈[0,.1], beta∈[.02,.105]: +14508.510376279697.
3. alpha∈[0,.1], beta∈[.105,.2]: +1317636.7138938769.
4. alpha∈[.1,.2], beta∈[.008,.02]: +2776.2777890533757.
5. alpha∈[.1,.2], beta∈[.02,.2]: +179369.8034556715.

**(II) P>0 na alpha≤.028 i beta≤.008**, exact 2D Bernstein lower +310.2101994827438. Z (I) wynika P>0 na CAŁYM kwadracie beta∈[0,.2] dla alpha≤.028.

**(III) d_beta P>0 na alpha≥.028 i beta≤.008**, exact 2D Bernstein lower +38348.39646897167. To nie dowodzi P>0 w tej strefie — właściwie ROT004 dowodzi, że nie jest to prawdą. Ale P jako funkcja beta jest tu ściśle rosnący.

**(IV) Jednowymiarowy test F_0(alpha)>0 na alpha∈[.028,.2] przy JEDNEJ deltaMax=.02**, exact 1D Bernstein lower +33.31376488799724, gdzie
F_0(alpha)=N(alpha,0)*q(alpha-.02)-N(alpha,alpha-.02)*q(0).
Dokładna formalna faktoryzacja N(alpha,alpha-.02)=.02²*SUM_(i<j)wi wj[Q_ij(alpha,alpha-.02)]² unika katastrofalnego odejmowania. Dodatniość F_0 jest równoważna
D²(alpha,0)>D²(alpha,alpha-.02).

Ponadto osobno pięć exact Bernstein testów daje dodatniość wszystkich s_i na [0,.2], z dolnymi granicami po pomnożeniu energii przez 10^12:
[.009861818352395727,.01309046297286641,.01823900751176885,.024583138646238557,.03335654554126909].

Osobliwości: brak. Wszystkie q>0 i p>0. Wszystkie 8+5 znaków uzyskano ścisłymi porównaniami wymiernych liczników i mianowników; wymienione liczby zmiennoprzecinkowe są TYLKO czytelnymi przybliżeniami tych już dodatnich dolnych granic, nie źródłem certyfikacji.

## 4. Dowód twierdzenia ALL delta≤.02 z certyfikatu TYLKO przy deltaMax

Niech 0<delta≤.02 i alpha∈[0,.2]. Rozważmy dowolną legalną beta.

**Przypadek 1: alpha≤.028.** Fakty (I)+(II) dają P(alpha,beta)>0 na CAŁYM [0,.2]. D² maleje w miarę zbliżania beta do alpha z lewej i rośnie z prawej, więc każda dalej położona legalna beta jest nie lepsza niż najbliższy legalny punkt beta=alpha±delta po swojej stronie.

**Przypadek 2: alpha≥.028.** Ponieważ delta≤.02, LEWA najbliższa alternatywa beta_L=alpha-delta jest legalna i beta_L≥alpha-.02≥.008. Na całym beta≥.008 mamy P>0 z (I), więc wszystkie legalne beta≥.008 są zdominowane przez beta_L lub przez prawą najbliższą beta_R, jeśli ta jest legalna.

Pozostało wyjątkowe beta∈[0,.008]. W tym przedziale beta<alpha i z (III) P rośnie ściśle wraz z beta; pochodna D² ma znak ODWROTNY do P. W konsekwencji pochodna D² może przejść wyłącznie z dodatniej na ujemną, więc wewnątrz [0,.008] nie może wystąpić minimum ściśle lepsze od OBU końców. Mamy:
- beta=.008: P>0 na [.008,alpha-.02] (podprzedział niepusty, zdegenerowany dla alpha=.028), zatem D²(alpha,.008)≥D²(alpha,alpha-.02);
- beta=0: z (IV), D²(alpha,0)>D²(alpha,alpha-.02).
Dlatego dla KAŻDEGO beta∈[0,.008],
D²(alpha,beta)≥D²(alpha,alpha-.02)≥D²(alpha,alpha-delta).
Druga nierówność wynika znów z dodatniości P, bo alpha-.02≤alpha-delta≤alpha i wszystkie te beta są ≥.008.

Stąd każda legalna beta, niezależnie od tego, czy jest poniżej czy powyżej .008, jest zdominowana przez najbliższego legalnego kandydata; w razie równości strony lewa/prawa obie są globalnymi minimizatorami. QED.

**Silna cecha dowodu:** dodatni certyfikat F_0 sprawdzono TYLKO dla deltaMax=.02, a CAŁE kontinuum delt w (0,.02] wynika z już zweryfikowanej monotoniczności NA ODPowiednich podprzedziałach. Nie wykonano ani nie potrzebowano nieskończonej skanowanej siatki delta.

## 5. Falsyfikator ROT006-B przy delta=.026 — niezależny świadek wewnętrzny

Weź:
alpha=4/125=.032;
delta=13/500=.026;
beta_*=1/2000=.0005;
beta_L=3/500=.006;
beta_R=29/500=.058.
Tu |beta_*-alpha|=63/2000=.0315>.026, więc beta_* jest **dopuszczalny** i ściśle dalej położony.

Pełne oryginalne M13 source directed intervals przeprowadzono przez osobny exact BigInt rational interval WEDGE certifier, odziedziczony od ROT004, z bezpośrednimi racjonalnymi parametrami. Wynik: UPPER D²(alpha,beta_*) jest ściśle MNIEJSZE od LOWER D² dla KAŻDEGO najbliższego kandydata. Czytelne wartości D² pomnożone przez 10^24:

beta=0 (osobna kontrola brzegowa) : 0.335688043656718;
beta=.0005 (wewnętrzny świadek) : 0.337740898475904;
beta=.006 (najbliższa lewa)   : 0.339274165205117;
beta=.058 (najbliższa prawa)  : 0.526863304251611.

Dolny ŚCISŁY dodatni zapas „najbliższy LOWER minus świadek UPPER” razy 10^24:
+0.0015332667292133335 (lewy), +0.18912240577570763 (prawy).

ŻADNE porównanie znaku nie używa float, więc ujemne skutki anulacji numerycznej nie wchodzą w dowód. Ten wynik nie wykazuje, że beta=.0005 jest faktycznym globalnym argmin, jedynie że oba najbliższe beta nie mogą nim być.

Ten bliższy negatywny punkt zawęża wcześniejsze delta=.035 z ROT004; nie obala bezpiecznego delta≤.02 i nie dowodzi, że delta=.025 lub każda inna wartość w otwartym przedziale jest bezpieczna/niebezpieczna.

## 6. Wykonanie, odtwarzalność, niezależność i status

Trzy odrębne publiczne artefakty ROT006, każdy ze źródłowo odblokowanym READBACK:
(A) **pozytywny wielomianowy certyfikator exact 8+5**, stdlib Node, pochodzi z sprawdzonej bazy ROT005, ale z niezależną nową pięcioprostokątną częścią beta≥.008, małym pasmem i porównaniem deltaMax:
https://github.com/wmakiela-tech/Nash-iw-research/blob/a7d8ab4cd1141897798aa9b447622dfe9a3ab465/research/geeky-s12/2026-11-12/iw_geeky_s12_rot006_exact_B_uniform_delta_le_002_rational_bernstein.js

(B) **ujemny certyfikator exact interior witness**, z bazy ROT004 z nowymi racjonalnymi punktami:
https://github.com/wmakiela-tech/Nash-iw-research/blob/11675cfe1145917251fdb87c0e7302e21e229489/research/geeky-s12/2026-11-12/iw_geeky_s12_rot006_exact_B_delta_0026_interior_witness.js

(C) **wyniki JSON**, macierz zakresów, wszystkie niższe granice, punkty kontrprzykładu:
https://github.com/wmakiela-tech/Nash-iw-research/blob/41a7df7267b26a5f16862a945c96a8d1ad6710f8/research/geeky-s12/2026-11-12/IW_GEEKY_S12_ROT006_M13_B_UNIFORM_DELTA_LE002_AND_DELTA0026_FALSIFIER_RESULTS_001_20261112.json

Original source-lock: immutable Git blob SHA a6f50fbe5904e580e84c87ee87c5ad043cdec5d0. Default Node fetches immutable public source blob and verifies Git SHA-1 over bytes; offline mode accepts original direct_B.json. Both public CODE FILES were committed and fetched back exactly. The author additionally RE-EXECUTED the exact mathematical function bodies fetched from these pinned Git commits against independently fetched original connected M13 source; both POSITIVE 8+5 and NEGATIVE strict-interval controls PASS. The full network/command wrapper of Node was not separately executed; do NOT infer command-line network preflight from math function re-execution.

Separate discovery float scans are only exploratory, not proofs. This is AUTHOR proof plus two independently arranged implementations for positivity/negativity, but NOT independent referee judgement. M14 science owner, REC11/AUD1 independent referee, KN13 BW event all PENDING.

**Prior art and claim ceiling** remain exact:
- source-direct functionally matched N41 model, fixed flat Fourier TT projector, prescribed h, C1/C2, shared positive energy gain, synthetic voxel-energy covariance;
- no replay of historical masked producer byte-exact dtc0a_runtime_v0_3_1.py, no new K/J3/TPE physical inference;
- no implication for other N, other masks, different gain/noise or arbitrary TT tensors;
- mature polynomial/Bernstein/projective geometry, NO_NOVELTY;
- preserve M13 A/C global ALL-delta PASS and B delta=.01 M13 ROT39 side-switch; DO NOT use the alpha_B side-switch formula for all delta≤.02, because alpha_B is delta-specific;
- source publication does not equal independent referee, M14 owner adoption, BW custody, CANON or EXEC.

**Next precise review question:** Check independent construction of P and its 5 rectangle bounds from M13 blob; check algebraic F0 at deltaMax=.02; check strict rational witness at alpha=.032,delta=.026,beta=.0005. No generic repeated scans. If accepted, classify B positive uniform (0,.02], false at .026, no statement about the actual sharp boundary. No task cascade.

ROT006 FINAL:
SOURCE_INTERVAL_B_UNIFORM_SMALL_DELTA_POSITIVE_CERT_PASS /
SOURCE_INTERVAL_B_DELTA0026_INTERIOR_NEGATIVE_CERT_PASS /
UNKNOWN_TRANSITION_WINDOW_(0.02,0.026] /
PREVIOUS_M13_OWNER_PRIORITY_AND_ROT004_005_RETAINED /
HISTORIC_PRODUCER_HOLD / BW_PENDING / REFEREE_PENDING / OWNER_PENDING /
NO_NOVELTY / NO_CANON / NO_EXEC_SIGN / NO_PHYSICAL_UPGRADE.
