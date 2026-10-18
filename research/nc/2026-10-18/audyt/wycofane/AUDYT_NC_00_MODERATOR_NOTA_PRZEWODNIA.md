# NOTA PRZEWODNIA DLA MODERATORA — rozesłanie audytów NC

**Od:** NC (zewnętrzna komórka Claude) · **Data:** 2026-10-18

---

## Co wysyłasz i do kogo

| plik | adresat | zadanie w jednym zdaniu | zależności |
|---|---|---|---|
| `AUDYT_NC_01_GPT_SPOJNOSC_I_KSIEGOWOSC.md` | GPT | czy jedenaście moich zwrotów nie przeczy sobie i czy bilans „zero otwartych" się zgadza | niezależny |
| `AUDYT_NC_02_DS-R1_FALSYFIKACJA_SLEPA.md` | DS / R1 | wyprowadzić sufit pomiarowy **na ślepo**, potem porównać; dowieść albo obalić konieczność `μ₂ ≤ 0` | **część A ślepa** |
| `AUDYT_NC_03_GEMINI_RUNTIME_REIMPLEMENTACJA.md` | Gemini | zaimplementować od zera ze specyfikacji i odtworzyć siedem tabel | **nie czytać mojego kodu przed przebiegiem** |
| `AUDYT_NC_04_GROK_RED_TEAM_LATERALNY.md` | Grok | zaatakować ramę i sposób pracy, nie rachunki | niezależny |
| `AUDYT_NC_05_BIELIK_WEZEL_ROZNORODNOSCI.md` | Bielik | atrybucja (czego nie znalazłem) + czy non-mapów naprawdę jest dwanaście | niezależny |

## Jak je wysłać

**Sekwencyjnie, nie równolegle** — zgodnie z regułą projektu, że dla precyzyjnych misji
sekwencja modeli jest tańsza i czystsza niż wysyłka równoległa. Proponowana kolejność
i uzasadnienie:

1. **Bielik (Z2)** — pierwszy, bo jeśli non-mapów jest trzynaście, bilans jest fałszywy
   i część zadania GPT traci sens. To jest najtańsze pytanie o najwyższej dźwigni.
2. **DS/R1** — drugi, bo jego część A jest ślepa i nie wolno jej kontaminować niczym,
   co wróci od innych.
3. **Gemini** — trzeci, po DS, żeby móc porównać trzy niezależne tory: mój, DS i runtime.
4. **GPT** — czwarty, bo księgowość ma sens dopiero, gdy wiadomo, co zostało obalone.
5. **Grok** — ostatni, bo red team ramy jest najmocniejszy, gdy widzi wyniki pozostałych.

Jeśli wolisz szybciej: Bielik i DS można puścić równolegle, reszta po nich.

## Dwie rzeczy, które wymagają Twojej decyzji, nie audytu

1. **Zakres Twierdzenia 1 z 009.** W 010 §4 zwęziłem je sam (sufit dotyczy reakcji zwrotnej
   współosiowej z odczytem, nie reakcji zwrotnej w ogóle). Rekomendowałem wpisać to jako
   **korektę do 009**, nie jako osobny claim obok. Decyzja o formie należy do Ciebie.
2. **Decyzja ramowa** (atlas wobec ramy twierdzeniowej). Dostarczyłem trzecią i ostatnią liczbę:
   zero otwartych pozycji matematycznych po stronie atlasu. **Z zastrzeżeniem, które powtarzam,
   bo jest istotne: sam dostarczyłem te świadki i sam policzyłem, ilu brakuje.** To konfiguracja,
   w której moja ocena kosztu jest systematycznie zbyt niska. Zadanie C3 u Groka i zadanie Z2
   u Bielika są w to wymierzone — proszę, nie podejmuj decyzji ramowej przed ich odpowiedziami.

## Czego w tych pakietach celowo nie ma

- **Żadnego EXEC_SIGN i żadnej prośby o niego.** Nic z 004–014 nie jest gotowe do podniesienia
  statusu, a sufity claimów są wpisane w każdy pakiet.
- **Żadnej prośby o potwierdzenie.** Każdy pakiet mówi wprost, że zgoda nie jest wynikiem.
  Jeśli wrócą same potwierdzenia, to będzie sygnał o konstrukcji pakietów, nie o poprawności
  zwrotów, i warto wtedy przepisać pakiety, a nie przyjąć wyniki.
- **Żadnej rekomendacji ramowej.** Dostarczam liczbę, nie zdanie o tym, która rama jest lepsza
  dla czytelnika.

## Stan materiału

GitHub `wmakiela-tech/Nash-iw-research`, `research/nc/2026-10-18/`: zwroty 004–014, `README.md`
z tabelą hashy wszystkich plików, `code/` z 33 skryptami, w tym prerejestracje zapisane
i zahaszowane **przed** uruchomieniem opisywanego kodu.
Drive, folder `1tUg46tXD8leCUbWvPHDlp7qTni-ebnkt`: zwroty 004–014.

W `README.md` jest też pełna lista moich własnych błędów z tej doby — siedem, w tym jeden
obalony przez LT4, dwa obalone przez moje własne prerejestracje i jeden świadek, który
odrzuciłem sam, bo powielał uwagę, którą wcześniej odrzuciłem jako nie tę. Lista jest tam
celowo: bez bazowej stopy błędu audytor kalibruje się źle.

## Jedna rzecz, którą zgłaszam poza kolejką

Zwroty 008–011 to cztery artefakty na jednym wątku w ciągu doby, każdy atakujący poprzedni.
Zgłosiłem to jako **gravity well** w 012 §4 i przeniosłem się z powrotem na dług audytowy
(012, 013, 014). Uważam, że przeniesienie było słuszne, ale nie mnie to oceniać — stąd
zadanie C1 u Groka. Jeśli jego werdykt będzie ostry, warto, żeby wpłynął na to, co NC robi
dalej, a nie tylko na to, jak opisuje to, co zrobiła.
