---
artifact_id: IW_BADACZ_B1_MODERN_GENERATOR_REPLICA_TRANSFER_PREREG_094_20261122
exposure: PUBLIC
origin_cell: BADACZ (wątek Claude), właściciel 090/091
created_at: 2026-11-22
document_type: PREREGISTRATION (zamrożona przed przebiegiem natywnym)
authorization: Moderator 22 XI 08:57 („Akceptuję”, propozycja z odpowiedzi po REVIEW_093); stała autoryzacja przebiegów 21 XI 16:05
claim_ceiling: NUMERYCZNY w modelach [▷] / NO_PBH_BOUND / NO_NOVELTY / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
---

# PREREG_094: czy etykieta MOD_INTERMEDIATE przeżywa repliki MC przepuszczone przez solver natywny i ile wynosi czysty szum solwera na pierwiastkach

## 1. Pytanie

REVIEW_091 r3 zostawił HOLD na odporności łącznej (MC + solver). Źródła HOLD:

- AUD3 ROT007 i KN15 ROT007: najgorszy przypadek > 0.27;
- REC13 ROT010: j22/net/LBT ma 3.8× zamiast 5×;
- INT10 ROT013: przeniesienie rozrzutu MC na próg przez elastyczność nie jest zweryfikowane.

Zamiast składać najgorsze przypadki, mierzę bezpośrednio, w dwóch krokach:

1. Repliki tablic R1 i R2 (REVIEW_091 r2) przepuszczam przez natywny Wu–Xu i PRyMordial. Każda replika daje dmod z własnym szumem MC i własnym szumem solwera.
2. Szum samego solwera mierzę na ramieniu J: tablica nominalna ×1.001. Fizycznie odpowiada to przesunięciu pierwiastka o −log₁₀1.001 = −4.3e−4 dex, czyli praktycznie niczemu. Wszystko ponad to jest szumem solwera.

## 2. Przebiegi (`run094.sh`, kod natywny i sieciowy bez zmian)

| ramię | tablica | rola |
|---|---|---|
| a / b | P83 R1 / H73 R1 (SHA afb4dddc…, 041b0bb6…) | realizacja R1 |
| c / d | P83 R2 / H73 R2 (536d0546…, 5708993c…) | realizacja R2 |
| e / f | P83 / H73 nominalne × 1.001 (`table_scale_085.py`) | J: czysty szum solwera |
| k | P83 nominalne (67dad44e…), węzeł j22 −17.20 | kontrola tożsamości sterownika wobec 090 |

- **Węzły:** wszystkie węzły siatki 090 (co 0.05 dex) w odległości ±0.15 dex od któregokolwiek z 4 nominalnych pierwiastków 090 danego generatora i masy, plus węzeł bazowy (`gen_cfg_094.py`).
- **Liczba przebiegów:** 39 dla P83 i 38 dla H73 na ramię, plus 1 kontrolny. Razem 232 przebiegi Julii (dwa procesy równolegle) oraz 233 + 1 przebiegów PRyMordial.
- **Szacowany czas:** ~65 min. Mój szacunek dla Moderatora („~30 przebiegów, kilkanaście minut”) był za niski. Pominąłem, że 4 pierwiastki na krzywą i 2 masy na 4 tablice wymagają własnych przedziałów, a do tego dochodzi kontrola J.

## 3. Bramki (wszystkie muszą przejść, inaczej brak etykiet)

- **G_COMPLETE:** komplet identyfikatorów natywnych i sieciowych; każdy przebieg sieciowy ma rc = 0.
- **G_V2:** v2_max_rel ≤ 1e−6, n_points ≥ 20000 (jak w 090).
- **G_TABLES:** SHA tablic a–d i k jak w manifeście 090; e i f równe nominalnym ×1.001 z dokładnością 1e−12.
- **G_DRIVER:** k22_1720 bitowo równe 090 p22_1720 w kodzie i w sieci; net_base bitowo równe 090.
- **G_WINDOW:** pierwiastki nominalne przeliczone na węzłach okna równe pierwiastkom 090 z dokładnością 1e−12. Atrapa z danych 090 przechodzi wszystkie bramki.
- **G_BASE:** |Y_base − Y_base_090| ≤ 5e−4.

## 4. Estymaty (`analysis_094.py`)

- **Pierwiastek:** przecięcie liniowe, dokładnie jeden przedział.
- **Komórki:** 8, czyli j ∈ {22, 62} × {code, net} × Y* ∈ {0.251, 0.2484}.
- **Dla realizacji X ∈ {J, R1, R2}:**
  - δroot = root_X − root_nom;
  - dmod_X = root_H73,X − root_P83,X;
  - Δdmod_X = dmod_X − dmod_nom.
- **Szum J:** ε = δroot_J + log₁₀1.001, podany także w jednostkach noise_dex z 090 (N_Y/|nachylenie|).
- **Poziom węzłów:** dY = Y_ramię − Y_nom w identycznych węzłach (kod i sieć). Porównanie z N_Y = 6.13e−5.
- **Etykieta LM_X:** reguła 090 zamrożona bez zmian, liczona na 8 wartościach dmod_X.

## 5. Predykcje (moje, zamrożone)

- **Pr1:** LM = MOD_INTERMEDIATE w J, R1 i R2.
- **Pr2:** max |Δdmod_R| po 16 parach (komórka, R) ≤ 0.04.
- **Pr3:** po 16 pierwiastkach J mediana |ε|/noise_dex ≤ 1, a maksimum ≤ 3. To sprawdza, czy heurystyka N_Y nie jest antykonserwatywna.

## 6. Reguła statusu

| status | warunek |
|---|---|
| `LM_STABLE_IN_3_REALIZATIONS` | LM_X = INTERMEDIATE we wszystkich trzech realizacjach i wszystkie 24 wartości dmod_X w [0.10, 0.27) |
| `LM_STABLE_CELLWISE_EXCURSIONS` | etykiety stabilne, ale część komórek poza tym przedziałem |
| `LM_FLIPS` | w przeciwnym razie |

Trzy realizacje to nie przedział ufności. Status sam nie zdejmuje HOLD z REVIEW_091 r3; decyzja należy do audytu zewnętrznego i Moderatora.

## 7. Granice z góry

- Jedna para strojeń generatorów; dwie repliki MC.
- Ramię J próbkuje szum solwera jednym zaburzeniem.
- Bez nowych przebiegów MC i bez zmian kodu natywnego i sieciowego.
- Wynik dotyczy wyłącznie progów w modelach. Nie jest granicą fizyczną PBH.
