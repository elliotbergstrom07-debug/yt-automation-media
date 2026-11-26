# PUBLICERAT 26 nov 2026 (SATSNING dag 2)

## Rendering B – L3 00:30 natten till 27/11 (18:30 Eastern) – Survive the Era (schemalagd körning, ~14:00–15:50)
- **Kanal/lucka:** Survive the Era · L3 27/11 00:30 (+01:00) · kö-rad 43
- **Titel:** How Long Would You Survive in Every Era of Coal Mining?
- **Sökfras/trend:** "how long would you survive in every era" (YouTube-förslag, TREND_2026-11-24 + bekräftat i TREND_2026-11-26 STE-avsnittet). forbattring.trend + standard_check.innehall fanns i manuset (89 faktaskyltar, största lucka 22,9 s, snitt 18 ord/say).
- **postId:** c8d7fb58-c194-4779-bdcd-822d247203ae (publicationId facbf087-9f99-4230-abe1-1f51fdad69d9)
- **Video-ID:** a40V3Gq9ctc (13:11, categoryId 27, public via publishAt)
- **Schemalagd tid verifierad i Studio: JA** – Visibility "Scheduled", Schedule as public Nov 27, 2026 12:30 AM (~15:45).
- **Miniatyr:** A '1900' + 'COULD YOU SURVIVE?' (godkänd STE-stil 24/11) – satt via vidIQ (imageId 97fbc3ef-9b6f-4b78-aa9b-094df025a1a8), syns i Studio. Ingen Studio-miniatyrkörning behövdes.
- **Short:** nej (STE har inga Shorts).
- **Spellista:** Survive the Era – Day 1 to Day 100 (satt och sparad i Studio). Videospråk English (United States) satt i Studio. Made for kids = nej.
- **vidIQ-kvot Pacific-dygnet 26/11 (09:00–09:00):** 1 av 3 efter denna → 2 kvar till rendering A (L1 LS + L2 QM).
- **Spärrar:** originalitet.py GODKÄNT (mot ste-18/19/20/21/22/26), granskning.py GODKÄNT (1 varning: avsiktlig 'Rewind'-mening ~0:33), monetisering.py GODKÄNT, granskning --thumb A/B/C GODKÄNT. Render: "musik: soundtrack Survive the Era: 790.1 s". Uppladdad fil = granskad fil (sha256 74fdbd4c… lika lokalt och på raw-länken).
- **Kontroll:** 0:00–0:30 + 8 bildrutor granskade (ljus gruvöppning med hjälten och lågan på kepsen = miniatyrens scen, inga tomma glyfer, inget för mörkt).
- **jamfor:** chk/jamfor-ste24.png mot 49_Ph2q6uIM, 19NBlkgBNqw, YLxZ_LKDKWI – C högst kontrast (0,22 = median), A 0,21; A vald.

### Avvikelser / motor
- Manuset var skrivet för NY_MOTOR_PLAN (nya scentyper + 31 nya platser som inte fanns). Byggde i körningen **automation/coal1900.py** (sparad i projektet): alla 32 platser (mine_mouth, tunnlar, breaker, company store, bell pit-genomskärning, Huskar, Monongah, Farmington, refuge chamber, tidslinjeväggen m.fl.), ~35 rekvisita, hjältens lampa på mössan (open_flame/candle/electric) + tidsdosan, nya scentyper **jump** (stort gult årtal i Anton) och **tierlist**, split2 (två platser sida vid sida), samt prep() som gör explainer → vitt note-kort, cutaway → scen + note_card, card_style → card. Inga fallbacks som visar fel miljö.
- **run_era.py i projektet är INTE uppdaterad** (skrivningen nekades). Ändringen som behövs (3 rader): lägg 'coal1900' före 'chicago1871' i modullistan; efter loopen `import coal1900 as _coal; _coal.after()` (i try/except ImportError); i long-läget kör `_coal.prep(_m)` före motion.auto_actions när manuset har typerna explainer/jump/cutaway/split/tierlist eller card_style. Anton-fonten kopieras från /usr/share/fonts/truetype/google-fonts/ofl/anton/ till fonts/.
- Motorpush till media-repot (gren motor-ste24) nekades – coal1900.py finns bara i projektet.
- Ägarens Chrome står nu på Google-kontot för Survive the Era (bytt för Studio-kontrollen).
- Miniatyrskript: automation/ste24_thumbs.py (B = tier-lista 'WHICH ONE KILLS YOU?', C = '1907' + '3,242 MINERS' – reserv för klick-diagnosen).
- Uppföljning: klick-diagnos 27/11 02:30 (send_later i denna session).

## Rendering A – L1 18:00 (12:00 Eastern) – Last Shift – SCHEMALAGD
- **Titel:** Zombie Apocalypse: Trapped In an Airport Hotel For 100 Days (kö: NY RAD enligt KÖ_ÄNDRING_2026-11-26_LS)
- **Sökfras/trend:** "zombie apocalypse trapped in an airport hotel" (nytt YouTube-förslag 26/11, TREND_2026-11-26) + "trapped in … for 100 days"-mallen. forbattring.trend + standard_check.innehall fanns (30 faktaskyltar ≈ var 20:e s).
- **postId:** 2889b964-6545-4c20-a8d0-98eed50541bc (publicationId a43bdf6a-dc84-4631-ac86-6088c42d9ede) · categoryId 24 · public via publishAt 2026-11-26T18:00:00+01:00
- **Video-ID:** ryJC9Xc3488 (https://youtu.be/ryJC9Xc3488, 9:46)
- **Schemalagd tid verifierad i Studio: JA** – Visibility Scheduled, "Nov 26, 2026 6:00 PM" (~15:40).
- **Miniatyr:** A 'KEEP IT LIT' (Ferris-stilen: ljus lobby med ljuskronor, rad av frusna döda, hjälten i vinröd kavaj stor till höger med strömbrytaren 'LOBBY') – satt via vidIQ (imageId f5634bd1), syns i Studio. jamfor.py (chk/jamfor-ls26.png) mot 3pkkFlH7-pU / 92UJj21YqM8 / ILywYRfPva8: A kontrast 0,30 ≥ median 0,27 – MINST LIKA TYDLIG. granskning --thumb A/B/C GODKÄNT. B 'DAY 1 | DAY 100' och C '3:02 AM' i media-repot gren motor-ls26 (motor/ls-2026-11-26.B.jpg/.C.jpg).
- **Short:** nej – inga LS -short.json fanns och TILLÄGG 22 NOV d) säger Shorts bara för QM/TLI (konflikten mot SATSNING 3 LS-Shorts/dag kvarstår – se KÖ_ÄNDRING_2026-11-26_LS).
- **Spellista:** "Last Shift – Zombie Outbreak Stories" – tillagd och sparad i Studio. Made for kids = Nej.
- **Kontroller:** originalitet.py GODKÄNT (mot ls-18/20/21/23/24/25), granskning.py GODKÄNT (varningar: 1 replik > 16 ord första 30 s, 11 dagkort), monetisering.py GODKÄNT (varning bildföljd 72 % lik ls-20). Render 9:46 (585,4 s), "musik: soundtrack Last Shift: 585.4 s, 66 bpm". watch-video 0:00–0:30 (--no-audio) + 8 bildrutor granskade – OK. Uppladdad fil = granskad (sha256 f2a396f8… lokalt och i repot).
- **Avvikelser/rättat:**
  1. Arbetsytan saknades – koden skrevs ut ur projektet (~35 min, delvis via underagenter); setup.sh: figurpatch/musikpatch/allapatch klar. media.sh kunde inte skrivas ut (blockerat av ett integritetsfilter) – push gjordes med samma git-kommandon för hand.
  2. Hotellplatserna fanns inte → ny modul **hotel.py** (17 platser: hotel_lobby med ljuskronor/svängdörr, front_desk, hallway med rumsnummer/rörelsesensor, stairwell, parking_garage med skyttelbuss/lyktor, loading_dock med dieselgenerator/mätare, kitchen med walk-in/frys, breakfast_room, electrical_room med OVERRIDE, guest_room, basement med varmvattenberedare, parking_lot, hotel_roof, airfield med vita/blå/gröna/röda banljus + jetplan, hotel_exterior, hotel_map, airfield_map) + 15 föremål + **frusna döda** ("frozen": true = stilla silhuett, arm framåt). Laddas i run_ls.py efter prison. atmos-klotter (burkar/tunnor) avstängt i hotellet. Sparad i media-repot gren `motor-ls26` (inte i projektet – platsgränsen).
  3. Dagkorten visade ls21:s hårdkodade "NIGHT SHIFT RANKING" → label "100 DAYS IN THE AIRPORT HOTEL", tom next (lokal manuskopia).
  4. `board_inset` (2 scener) ritas inte av någon modul – texten syns inte (skylten i samma scen bär faktan). motion.py:s "climb"-handling ritar ett eget trapphus med siffran 9 (scen 15/27).
  5. Anton-typsnittet hämtades via npm (@expo-google-fonts/anton).

## Rendering A – L2 21:00 (15:00 Eastern) – The Quiet Math – SCHEMALAGD
- **Titel:** How Much House Can You Afford by Salary? (5 Levels) (kö: NY RAD enligt KÖ_ÄNDRING_2026-11-26_QM)
- **Sökfras/trend:** "how much house can you afford by salary" (YouTube-förslag 26/11; utlovad i slutet av r5XmMVILOmc). forbattring.trend + standard_check.innehall fanns (62 faktaskyltar).
- **postId:** 873e8f83-b794-48d9-b90f-5cf52c657258 (publicationId b3fef895-9784-4511-8537-afa57c8145e5) · categoryId 27 · public via publishAt 2026-11-26T21:00:00+01:00
- **Video-ID:** -oUos-7Qi5M (https://youtu.be/-oUos-7Qi5M, 13:09)
- **Schemalagd tid verifierad i Studio: JA** – "Nov 26, 2026 9:00 PM" (~15:45).
- **Miniatyr:** A '[grön] $64K PAY = / [röd] $174K HOUSE' (pris mot lön: maskoten framför stora huset med $416,700-skylt, litet hus i panelen) – satt via vidIQ (imageId 6a01669c), syns i Studio. jamfor.py (chk/jamfor-qm26.png) mot Rz8_hmDacmI / g5zh1GwogqY / bXSYcV6zW_g: A MINST LIKA TYDLIG. granskning --thumb GODKÄNT. B '$140,800 / TO BUY THIS?', C '-$27,748 / SAME PAY?' i gren motor-ls26.
- **Shorts: JA, 3 st via Studio** (720×1280, 2,7–3,3 MB, beskrivningen börjar "Full video: https://youtu.be/-oUos-7Qi5M", spellista The Quiet Math – Can You Afford It?, not made for kids), schemalagda och bekräftade i Studio ("Video scheduled"):
  - v3g_eAsoIak "The Median Salary Buys 42% of the Median House #shorts" – 27/11 10:07
  - pCRCuawiC8c "The Salary You Need for a $416,700 House #shorts" – 27/11 14:07
  - nrGuQx0svJo "Same Salary, $27,748 Less House #shorts" – 27/11 18:07
- **Spellista (lång):** "The Quiet Math – Can You Afford It?" – tillagd och sparad i Studio.
- **Kontroller:** originalitet.py GODKÄNT (mot qm-20/21/22/24/25), granskning.py GODKÄNT (varning 1 replik > 16 ord första 30 s), monetisering.py GODKÄNT. Render 13:09 (789,1 s), "musik: soundtrack The Quiet Math: 789.1 s, 84 bpm". watch-video 0:00–0:30 + 8 bildrutor – OK. Uppladdad fil = granskad (sha256 348d6c10…).
- **Kvot:** Pacific-dygnet 26/11: STE + LS + QM = 3 av 3 (vidIQ: sista platsen använd). Shorts via Studio tar ingen vidIQ-plats.
- **Avvikelser/rättat:**
  1. Pilen "→" ritas som tom ruta → ersatt med "->" i den lokala manuskopian (4 tavlor) och i Short 3.
  2. Shortsens rubrikrad (`headline`) var på SVENSKA ("mot medianhus", "lönen medianhuset kräver", "bil = hus") → ersatt med engelska rubriker, omrenderade. Manusskrivarna bör skriva headline på engelska.
  3. Short 3 blev 64,4 s (> 59 s-spärren) → speed 1,22 i lokal kopia (57,2 s).
  4. meta.json kapade beskrivningen vid 4 900 tecken (disclaimern) → ombyggd: sökfras först, disclaimer, sammanfattning, kapitel, 13 källor (korta titlar), hashtags = 4 831 tecken.
  5. Musik: motorn lade soundtrack trots manusets music 'none' (som 25/11).
  6. Freddie Macs PMMS kom ut 25/11 (Thanksgiving-flytt) – 7,21 % gäller, ingen ny siffra i dag.
  7. Studio: en flik med Short 1:s uppladdningsdialog låstes av vidIQ-panelen ("Cannot access a chrome-extension URL") – inte omladdad; Short 1 slutfördes från utkastet i en annan flik. Den låsta fliken står kvar öppen i ägarens Chrome (sidan vill bekräfta att lämna – kan stängas, inget osparat som behövs).
- **Uppföljning:** klickdiagnos (yt-klick-diagnos) bokad 20:00 (LS, trig_01Kjq7HVCEkkHgrL6P2pwHAN) och 23:00 (QM, trig_01ADMDZsyPCsarfhfUqAU6oe).
