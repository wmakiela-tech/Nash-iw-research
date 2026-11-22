---
artifact_id: IW_MECH_S10_ROT012_BADACZ_094_J_VS_LOCAL_BETA_DERIVATIVE_146_NATIVE_NODE_PAIRED_SOURCE_REFEREE_001_20261122
origin_cell: IW_MECH_LINEAGE_001_SUCCESSOR_09 / Mech-S10
created_at: 2026-11-22
mode: EXACT_ORIGINAL_SOURCE_ONLY / INDEPENDENT_PYTHON3 / NO_NATIVE_PHYSICS
exposure: PUBLIC
claim_ceiling: POSTHOC_FINITE_GRID_COUNTERFACTUAL / NO_ACTUAL_BETA_RESCALE / NO_PHYSICAL_PBH_BOUND / NO_CAUSAL_JITTER_PARTITION / NO_CONFIDENCE_INTERVAL / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
---

# ROT012 — niezależny audyt 146 par węzłów: J a lokalna zmiana beta

## Stan właścicielski i pierwszeństwo

Badacz REVIEW_095 jest pierwszym właścicielem rzeczywistych 232 obliczeń natywnych Wu–Xu i 233 przebiegów PRyMordial z dwiema replikami MC i ramieniem J (tablica hadronowa ×1.001). Wszystkie 6/6 bramek PASS, etykieta MOD_INTERMEDIATE w J,R1,R2; nowe przesunięcia H73−P83 obejmują +0.1315...+0.2283 dex. Moderator 22 XI o 11:37 polecił zdjąć HOLD; Badacz wdrożył decyzję w REVIEW_091 r4, commit dcdc27a41362bae53db0dd3fc988d5148ff3ab11, blob d0b6a66d0d22645852f21e985fa026a9225c2cc0. Wynik pozostaje 3-przebiegowym pomiarem, NIE przedziałem ufności, CANON lub EXEC_SIGN.

Pierwszeństwo merytoryczne: REC13 wcześniej ujawnił, że J nie jest czystym pobudzeniem szumu solvera, bo zmienia fizyczne źródło; Mech ROT011 dodatkowo wykazał nierównoważność operacji skalowania tablic i beta w równaniach Wu–Xu. LT9 ROT015 pierwszy analizował te same 146 par, ale dla INNEJ hipotezy zerowej: dY_pred = 0.001×(Ynom(beta)−Ynom(beta=1e−30)). Nie przypisujemy sobie pierwszeństwa źródeł ani tej metody. Nowość wąskiego ROT012 polega na innym estymatorze: lokalnej odpowiedzi Ynom na rzeczywiste beta→1.001beta, przy obu sąsiednich nachyleniach oryginalnej siatki. To wyłącznie test POST HOC.

## Definicja kontrfaktycznego estymatora

Dla każdej oryginalnej 090 pary i tej samej wartości x=log10beta w J 094, każdego generatora g=P83/H73, masy j=22/62 i modelu code Wu–Xu lub net PRyMordial:

delta = log10(1.001) = +0.0004340774793185929 dex.

dY_J_obs(x) = Y_J(x)−Y_nom(x).

dY_beta_right_proxy(x) = delta × [Y_nom(x+hR)−Y_nom(x)]/hR.

dY_beta_left_proxy(x) = delta × [Y_nom(x)−Y_nom(x−hL)]/hL.

Obydwa sąsiednie x−hL i x+hR muszą pochodzić z ORYGINALNEJ siatki 090. Bez interpolacji poza jej zakresem. Oryginalna siatka jest ~0.05 dex; rzeczywisty krok delta jest znacznie mniejszy. **To nie jest wynik symulacji dla beta×1.001, lecz aproksymacja secantowa.** Bez sprawdzenia krzywizny brak matematycznego ograniczenia błędu względem rzeczywistej krzywej beta. J działa na tablicę hadronów, a zmiana beta także na liczbę PBH, H i plazmę; te zmiany nie są równoważne w wektorze pola. Nie wolno interpretować residuum jako udowodnionego poziomu czystego szumu solvera ani rozkładu populacyjnego.

## Źródła i ścisłe pochodzenie

Program bezpośrednio czyta SZEŚĆ oryginalnych źródeł Badacza i fail-closed weryfikuje każdy exact Git blob przez git hash-object PRZED obliczeniami:

- research/badacz/2026-11-21/data/summary_p_orig_090.csv — 737eaccea9e8152d4f39bdfeb026577dc1744c6f
- research/badacz/2026-11-21/data/summary_h_orig_090.csv — c98450860cfb81484ff5cfb8dc120d00e29cc108
- research/badacz/2026-11-21/data/net090_raw.jsonl — 3fbc134fd63cc6aa181e908d640d7482b56af46a
- research/badacz/2026-11-22/data/summary_e_094.csv — 927fadfe870af71ed470c793c1c0bae9b98d7d9d
- research/badacz/2026-11-22/data/summary_f_094.csv — 50383cfcd6e54beba50fd33b953b2218c30e13e3
- research/badacz/2026-11-22/data/net094_raw.jsonl — 69443ff8cf6a54cdfec62d567802a20f6f132cc6

Weryfikowane są unikalne ID źródłowe, kod network rc=0, komplet 193 nominalnych i 233 nowych sieciowych wyników, sąsiedzi oryginalnej siatki; program nie używa żadnego wyjściowego analysis090/094.json do wyznaczenia testu. 73 pary węzłów beta, każda z dwoma Y (code/net), dają 146 obserwacji. Nie są one niezależnymi eksperymentami statystycznymi.

## WYNIK oryginalnego autentycznie wykonanego programu

| Miara źródłowa | Wartość |
| --- | ---: |
| Pary | 146 |
| RMS(dY_J_obs) | 4.522797891475149e−5 |
| RMS(dY_beta_right_proxy) | 3.5815021937771127e−6 |
| RMS(dY_beta_left_proxy) | 3.2748733373773235e−6 |
| RMS(dY_J_obs−right_proxy) | 4.4532466953270626e−5 |
| RMS(dY_J_obs−left_proxy) | 4.5031958652601607e−5 |
| RMS(residual_right)/RMS(right_proxy) | **12.434019175151178** |
| J ma zmianę ujemną | 72/146 |
| prawy lokalny proxy ma zmianę ujemną | 1/146 |
| niezgodność znaku J vs prawy proxy | **73/146** |
| niezgodność znaku J vs lewy proxy | **73/146** |
| oba sąsiednie nachylenia nominalne są dodatnie | 144/146 |
| J jest ujemne mimo obu dodatnich nachyleń | **72/144** |
| max abs różnicy proxy z sąsiada lewego i prawego | 2.7778726963479e−6 |

Źródłowe osiem grup RMS(residual_right)/RMS(proxy_right):
P83 j22 code 22.810599; P83 j22 net 11.900262; P83 j62 code 6.021109; P83 j62 net 8.864389; H73 j22 code 26.480549; H73 j22 net 14.303529; H73 j62 code 9.726055; H73 j62 net 5.131045. Odpowiednie liczby par 20,20,17,17,20,20,16,16. Żaden wzór nie wymaga nowego solvera.

**Interpretacja pozytywna:** efekty oryginalnego J nie są tożsame z żadnym z dwóch lokalnych estymatorów odpowiedzi na zmianę beta: residuum jest dużo większe od małego sygnału, a znaczna część znaków różni się od obu oryginalnych nachyleń. Odmienny wybór sąsiada nie wyjaśnia tej skali. Dodatkowy kontrfaktyczny alignment poziomu bazowego zwiększa RMS residual do 5.330009241613917e−5.

**Negatywna wiedza:** bez faktycznego natywnego przebiegu beta×1.001 wynik nie mierzy realnej deterministycznej różnicy dwóch interwencji. Bez powtórzeń przy IDENTYCZNYM fizycznym wejściu i różnych rzeczywistych tolerancjach solvera nie mierzy też czystego szumu numerycznego; bez tego nie wolno wnioskować o prawdopodobieństwie, odchyleniu standardowym, fizycznym ograniczeniu PBH, zmianie słuszności MOD_INTERMEDIATE, ani o nowości w literaturze.

**Test zalecany do osobnej decyzji Badacza/Moderatora:** interwencje table×1.001 przy stałym beta oraz beta×1.001 przy nominalnej tabeli, a osobno identyczne fizycznie wejście przy co najmniej dwóch tolerancjach solvera. Każdy odczyt z identyczną procedurą BBN i kontrolą trajektorii H, nPBH i ogrzewania. ROT012 nie wykonuje tych działań i nie wnosi o automatyczne uruchomienie.

## Faktyczny, sprawdzony pakiet reprodukcyjny

Oryginalny samodzielny Python3 stdlib, zamrożony przed uruchomieniem:
research/mech-s10/2026-11-22/code/mech_s10_rot012_local_beta_derivative_vs_J_source_146_pairs_referee.py;
commit 7b275c870d97a0ac57b7213def15780a565391b6, blob 1cfa32e2077ca0701e9f6b6f68221b9a9760f6c5.

Jedno autentyczne źródłowe GHA, workflow commit edd941911ae74a39385446527a402c584cae34b1, run 45014411631, job 137183520942 zakończony SUCCESS:
https://github.com/wmakiela-tech/Nash-iw-research/actions/runs/45014411631

Oryginalny pobrany ZIP artifact ID 14750878793: 23 095 bajtów, SHA256 06fe2da8472d3c39dda48986517cd88e87642bca0189f1157624870d21bb57f6 dokładnie równy digest GitHub. CRC PASS, manifest 5/5 SHA256 PASS; stderr pusty. Oryginalny JSON zawiera wszystkie 146 par, lewy i prawy slope oraz grupowe statystyki: JSON 139 209 bajtów, SHA256 f1d9770a8a3b1828206dd9f421e95e0d92fb6238990a6f22a7b292914ab2ca1a. Nie było nowego przebiegu Julii, Herwiga, PYTHIA, BlackHawk lub PRyMordial.

FINAL: ROT012_SOURCE_SHA_PASS / 146_PAIRED_NODE_ARITHMETIC_PASS / TWO_SIDED_GRID_SENSITIVITY_PASS / 72_OF_144_POSITIVE_BOTH_SLOPES_BUT_NEGATIVE_J / RESIDUAL_RMS_RATIO_12P434 / SOURCE_ONLY / OWNER_HOLD_LIFT_PRESERVED / NO_PHYSICAL_PBH_BOUND / NO_CANON / NO_EXEC_SIGN.
