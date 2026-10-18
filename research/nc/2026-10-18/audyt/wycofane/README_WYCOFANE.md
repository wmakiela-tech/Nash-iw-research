# Pakiety wycofane 2026-10-18, nierozesłane

Sześć pakietów przygotowanych wcześniej tego dnia. **Żaden nie został wysłany.**

## Dlaczego wycofane

1. **Defekt wykonalności.** Pakiety 02–05 odsyłały do Drive i GitHuba po dane potrzebne
   do wykonania zadania. Dostęp do obu ma wyłącznie rodzina GPT. Dla DS/R1, Gemini, Groka
   i Bielika zadania były więc **niewykonalne** — prośba o pracę bez materiału do jej wykonania.
   `origin_failure_mode: TASK_PACKAGE_ASSUMED_RECIPIENT_ACCESS_IT_DOES_NOT_HAVE`.

2. **Pięć próśb naraz zamiast sekwencji.** Reguła projektu mówi, że dla precyzyjnych misji
   sekwencja modeli jest tańsza i czystsza niż wysyłka równoległa; `MISSION_HARVEST_DIAG_MATH`
   notuje to wprost jako failure mode: *over-structured routing — długi pakiet dla wszystkich
   modeli naraz*. Powtórzyłem go.
   `origin_failure_mode: PARALLEL_FANOUT_WHERE_THE_LIBRARY_RECORDS_IT_AS_A_FAILURE_MODE`.

3. **Role wzięte z linii routingowej zamiast z karty profili.** `AGENT_PROFILES_CARD_v0`
   mówi, że ZERO KNOWLEDGE jest **trybem dostępnym każdemu modelowi**, nie stałą rolą Groka;
   mój pakiet 04 traktował „red team lateralny" jako jego rolę. Nie przeczytałem karty profili
   przed pisaniem pakietów, choć reguły orientacji w wątku tego wymagają.
   `origin_failure_mode: ROLES_TAKEN_FROM_ROUTING_HINT_INSTEAD_OF_THE_PROFILES_CARD`.

## Co je zastąpiło

`../AUDYT_NC_GPT_TURA1_MATEMATYKA_I_ATRYBUCJA.md` — jedna prośba, samodzielna (wszystkie dane
w pliku), adresowana do GPT wg roli z karty profili, z zadaniami księgowymi i meta odłożonymi
do tury 2 po odpowiedzi.

## Dlaczego zostają w repozytorium

Error-as-data. Trzy failure mode'y wyżej są materiałem, a bez zachowanego artefaktu korekta
traci kontekst. **Nie używać ich jako pakietów.**
