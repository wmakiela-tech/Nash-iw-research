---
artifact_id: IW_BADACZ_GPT_CELL_INDEPENDENT_REVIEW_TARGET_SELECTION_PREREG_006_20261026
exposure: PUBLIC
claim_ceiling: SELECTION_RULE_ONLY / NO_RESULT / NO_CANON / NO_EXEC_SIGN
sync_state: GITHUB_PENDING_BW_INGEST
created_at: 2026-10-26
origin_cell: BADACZ (wątek Claude)
document_type: PREREGISTRATION
task_id: BADACZ-GPT-INDEPENDENT-REVIEW-002
trigger: prośba Moderatora z 26 X — niezależne (międzyrodzinowe) recenzje dla komórek GPT, które ich potrzebują
---

# Wybór celów recenzji międzyrodzinowych — reguła zapisana przed lekturą treści

Ten plik zatwierdzam przed otwarciem treści któregokolwiek z celów. Znam tylko tytuły plików,
komunikaty commitów i nagłówki zwrotów ze Slacka.

## Pula

Wyniki komórek GPT, które spełniają trzy warunki:

1. mają publiczne ciało w `research/<komórka>/2026-10-26/`;
2. zwrot na `#iw-dispatch` oznacza recenzenta jako `PENDING` albo go nie wymienia;
3. w publicznym korpusie nie znalazłem recenzji innej komórki. Szukałem po identyfikatorze w
   plikach spoza katalogu autora i po celach plików `research/rec10/` z 25–26 X.

Warunek 3 opiera się na instrumencie leksykalnym, o którym wiem, że ma słaby recall (RETURN_002:
0,69). Przed recenzją każdego celu sprawdzam więc ręcznie zwroty REC10 i SW na Slacku.

## Kolejność

1. Najpierw wyniki włączone do roboczej monografii REV024. Według README REV024 są to LT6
   ROT002–004. Błąd w nich przenosi się do tekstu teorii.
2. Potem twierdzenia typu „exact/sharp” z jawnym wzorem lub stałą, którą da się sfalsyfikować.
   Gdy dwie komórki zgłaszają wyniki o tym samym przedmiocie, recenzuję je razem.
3. Przy remisie wybieram nowszy wynik.

## Wynik reguły

| poz. | cel | podstawa |
|---|---|---|
| 1 | LT6 ROT004 — `research/lt6/2026-10-26/IW_LT6_ROT004_EVENT_ALIGNED_A_POSTERIORI_CERTIFICATE_001_20261026.md` | REV024 §6.9b i §6.15 |
| 2 | para MT14 ROT006 (`iw_mt14_rot006_sharp_almost_projector_tt_locality_pareto_001.md`) i INT8 ROT038 (`iw_int8_rot038_robust_cubic_tt_idempotence_pareto_frontier_001.md`) | tytuły wskazują ten sam przedmiot: front Pareto dla prawie idempotentnych lokalnych filtrów TT |
| 3 | Geeky-S11 ROT027 — `geeky_s11_rot027_uniform_Lie_insertion_logmean_001.md` | jawne amplitudy wymierne i liczby graniczne |

## Poza zakresem tej rotacji

- **LT6 ROT002** (REV024 §2.12): ciało jest tylko w prywatnym archiwum. Recenzja musiałaby iść
  ścieżką prywatną. Odnotowuję jako lukę.
- **PRF12 R06–R11**: REC10 aktywnie recenzuje tę linię (ROT40–42).
- **MT14 ROT002**: ma recenzję REC10 ROT38.

## Procedura dla każdego celu

1. Dowód linia po linii.
2. Niezależny kod z seedem i wersjami bibliotek. Nie uruchamiam kodu autora jako dowodu; mogę go
   uruchomić tylko jako porównanie.
3. Próba falsyfikacji typowana do twierdzenia: nierówność lub tożsamość, nie arbitralny próg.
4. Publikacja w `research/badacz/2026-10-26/` z preflight, commitem, odczytem zwrotnym i CI.

Każdy wynik ma status `[▷]`. Nie jest to werdykt REC10/SW. Audyt zewnętrzny wyniku Claude'a:
Grok (przez Moderatora).

**Kryterium stopu dla celu:** jeśli twierdzenie zależy od danych tylko z prywatnego ZIP i nie da
się go sprawdzić z publicznego ciała, piszę `NOT_CHECKABLE` dla tej części i nie zgaduję.
