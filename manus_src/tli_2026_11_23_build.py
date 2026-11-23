"""Bygger manus/tli-2026-11-23.json + -short.json av parts.json (kör tli_2026_11_23.py först)."""
import json

p = json.load(open("parts.json"))
SC, beats, st = p["SC"], p["beats"], p["stats"]
TITLE = "What If Earth Stopped Spinning Because of You?"

SOURCES = [
    "https://www.astronomy.com/science/what-happens-if-earth-stops-rotating/",
    "https://www.space.com/what-would-happen-if-earth-stopped-spinning",
    "https://www.livescience.com/what-if-earth-stopped-spinning.html",
    "https://www.scientificamerican.com/article/if-i-stop-the-world-will-i-melt-with-you/",
    "https://what-if.xkcd.com/26",
    "https://www.jpl.nasa.gov/news/nasa-details-earthquake-effects-on-the-earth/",
    "https://www.nist.gov/pml/time-and-frequency-division/time-realization/leap-seconds",
    "https://en.wikipedia.org/wiki/Leap_second",
    "https://www.timeanddate.com/time/leapseconds.html",
    "https://aps.org/apsnews/2007/02/foucault-earth-rotates",
    "https://www.britannica.com/science/Foucault-pendulum",
    "https://www.nesdis.noaa.gov/about/k-12-education/atmosphere/what-the-coriolis-effect",
    "https://scijinks.gov/coriolis",
    "https://news.agu.org/press-release/ancient-shell-shows-days-were-half-hour-shorter-70-million-years-ago/",
    "https://oceanservice.noaa.gov/facts/earth-round.html",
]

SUMMARY = """What if Earth started spinning slower, and you were the reason? You wash windows on a glass tower in downtown Denver, and one gray afternoon in November you find an old brass watch in a planter box. Turn the crown backward and the whole planet slows down. Level by level, you add a millisecond, then a second that crashes a hospital's computers, then a minute that an 82-year-old museum volunteer catches with a Foucault pendulum and a piece of chalk, then a whole hour. A freight boss offers you a million dollars a year to keep the 25-hour day. On day 30 the crown is jammed, the sun is still up at 9 p.m., and the day is getting longer every hour.

This is a fictional What If story. The watch and every character (Rosa, Priya, Abe, Grant Vole) are made up. The facts on screen are real:
- The ground at the equator moves about 1,037 mph (794 mph in New York City); a sudden stop would mean winds over 1,000 mph and almost all structures collapsing; ocean water would migrate toward the poles; Earth will never actually stop rotating (Astronomy magazine, 2026)
- A gradual stop would stretch day and night to six months each; air and ocean currents follow Earth's rotation (Space.com, 2024)
- One rotation takes 23 h 56 min 4.09 s; no natural force would stop Earth spinning (Live Science, 2021)
- Earth's spin energy is about 2 × 10^29 joules, about a million times the dinosaur-killing asteroid (Scientific American)
- The 2004 Sumatra earthquake shortened the day by 2.68 microseconds; a filled Three Gorges reservoir would lengthen it by 0.06 microseconds (NASA JPL)
- 27 leap seconds since June 30, 1972, the last on December 31, 2016; UTC is kept within 0.9 s of Earth's spin and is 37 s behind TAI (NIST, Wikipedia)
- The June 2012 leap second caused problems at Qantas, Mozilla and many Linux sites; leap seconds are to be dropped in or before 2035 (Wikipedia)
- The shortest day on record was June 29, 2022, 1.59 ms under 24 hours; an average day runs about 0.002 s over (Wikipedia, timeanddate.com)
- Foucault's 1851 pendulum: 28 kg bob, 67 m wire, about 270° a day in Paris (APS News, Britannica)
- Storms spin counterclockwise in the Northern Hemisphere because different parts of Earth move at different speeds (NOAA)
- 70 million years ago a day was about 23.5 hours and a year had 372 days, from a fossil rudist clam; the Moon recedes 3.82 cm a year (AGU, 2020)
- Earth bulges at the equator because of its spin (NOAA Ocean Service)
- Spinning in an office chair changes Earth's rotation, but not enough to matter (xkcd What If?)"""

seo = {
    "title": TITLE,
    "title_b": "What If You Could Slow Down the Earth? (Every Level)",
    "sokfras": "what if earth stopped spinning",
    "sokfras_kalla": "YouTubes sökförslag: 'what would happen if the earth stopped spinning' är förslag nr 2 för prefixet 'what would happen if' (trend/tli.json, GitHub Action niche-trends 23 nov 09:26 UTC) och 'what if earth stopped spinning' finns i TREND_2026-11-22.md (TLI) och ägarens lista 22 nov. Ingen video med exakt vår titel vid webbsök 23 nov.",
    "hook": "It's 9 p.m. in Denver, the sun is still up, and today will last 30 hours. Thousands of people on 16th Street are filming a sunset that never came.",
    "summary": SUMMARY,
    "description": SUMMARY,
    "disclaimer": "This is a fictional What If story. The watch and all characters are made up; the Earth, time and weather facts are real and sourced below.",
    "chapters": "00:00 The sun that won't set · Level 1: One millisecond · Level 2: One second · Level 3: Abe · Level 4: The 25-hour day · Level 5: The weather · Level 6: Grant Vole · Level 7: The longest day · The choice",
    "keywords": ["what if earth stopped spinning", "what would happen if the earth stopped spinning", "what if", "earth rotation",
                 "leap second", "foucault pendulum", "length of day", "what if story", "what if animation", "stickman story",
                 "the long if", "slow down the earth", "coriolis effect", "longest day"],
    "sources": SOURCES,
    "question": "On day 30, would you let the gear snap back in one jump, or hold it all night, one click at a time? A or B.",
    "pinned_comment": "A or B: let the watch snap the planet back to 24 hours in one jump, or hold it all night, one click at a time? Level 8 is coming: what if you were the last man on earth?",
    "hashtags": ["#whatif", "#story", "#animation"],
    "playlist": "What If You Could...? Hypothetical Scenarios",
}

thumb = {
    "kind": "tli",
    "script": "huvudchatten bygger (thumbs_v4_mall.py-stil; nya platserna street_16th + tower_platform, rekvisita sun_stuck med gatuklocka 9:00 PM)",
    "klickfraga": "Klockan är 21 och solen vägrar gå ner – han har saktat ner hela jorden med en armbandsklocka och nu sitter kronan fast. Hur får han tillbaka 24 timmar utan att förstöra planeten?",
    "hot_i_bild": "En jättestor, lågt hängande sol över Denvers skyline som tar ~40 % av bilden (övre högra), och under den en gatuklocka som tydligt visar 9:00 PM – solen som inte går ner är hotet; folkmassan på gatan filmar den med uppspärrade ögon.",
    "skiljer_sig": "Förra TLI (tli-2026-11-22) var en horisontell vintergata med en sladdande lastbil i vänster–mitten och blåaktig frusen ton. Nu: varm guld/orange kvällston, hotet (solen) uppe till höger, hjälten högt uppe på en fönsterputsarplattform till vänster med klockan i handen, gul text nere till vänster. Ingen bil, ingen snö.",
    "jamfor_ark": "chk/jamfor-tli-2026-11-23.png",
    "forsta_scen_matchar": "Scen 1 (0–7 s) är A-miniatyren i rörelse: 16th Street i varm kvällston, solen hänger kvar över skylinen (sun_stuck), gatuklockan visar 9:00 PM, folkmassan filmar, hjälten går framåt och pekar. Repliken säger '9 p.m.' och '30 hours' = miniatyrens text och HUD 'DAY 30 HRS'.",
    "variants": [
        {"id": "A", "layout": "hotet uppe till höger / hjälten vänster på plattformen / text nere till vänster",
         "big": "30 HOURS", "label": "THE SUN WON'T SET",
         "bild": "Jättesol över skylinen kl 21 (gatuklocka 9:00 PM); hjälten (svart stickman, gröna ögon, fönsterputsarsele) lugn på plattformen med mässingsklockan uppsträckt; Rosa och två i folkmassan med uppspärrade ögon. Gult '30 HOURS' + röd etikett 'THE SUN WON'T SET'."},
        {"id": "B", "layout": "fråga, närbild på klockan",
         "big": "WHY WON'T IT SET?", "label": "",
         "bild": "Mässingsklockan stor i förgrunden med sekundvisaren som går bakåt; solen speglad i glaset; liten stad i bakgrunden."},
        {"id": "C", "layout": "HUD-siffra, split",
         "big": "DAY: 30 HRS", "label": "AND GROWING",
         "bild": "Vänster: stort HUD-instrument 'DAY 30:00:00'. Höger: Foucault-pendeln med Abes kritstreck 'LATE' på golvet (gåtan som löser klimax)."},
    ],
}

forbattring = {
    "forra_videon": "tli-2026-11-22 'What If You Could Stop Time While Holding Your Breath?' (MANUS KLART 22/11 i GitHub-grenen manus-tli-2026-11-22; publiceringsstatus saknas) och senast publicerade TLI OOBnQjk7zV0 '1850' – ~0 exponeringar (TITTARTID_REGLER PRIORITET 23 NOV: TLI ~0 på 28 d).",
    "matt_forra": "TLI 28 d: ~0 exponeringar (TITTARTID_ANALYS_2026-11-23 via TITTARTID_REGLER). Ingen tittarkurva ännu.",
    "problem": "Distribution: kanalen får inga exponeringar. Titlarna har varit superkrafter som få söker exakt; 22/11 var första sökfras-titeln. Innehåll: risk för för få nya verkliga fakta per minut.",
    "andring": "TITTARTID_REGLER: TRENDORDER (titeln innehåller 'what if earth stopped spinning', förslag nr 2 under 'what would happen if' 23/11 – och utlovad i slutet av 22/11-videon), INNEHÅLLSORDER (DUI-mallen på What if: 7 numrerade nivåer med dom, 32 THAT'S REAL-kort + 32 faktaremsor, största lucka 29 s, snitt 21 ord/replik, 0 repliker < 6 ord), FORMATORDER/TLI-raden (sökfras-titel) och DISTRIBUTIONSORDER 2 (Short).",
    "forvantat": "Exponeringar via sök ('what if earth stopped spinning' är en evig sökfras) och via Shorten (mål ≥ 300 första veckan), CTR ≥ 3 %, ≥ 55 % kvar vid 0:30 och ≥ 35 % vid 2:00.",
    "referens": "DOOMPERK 'What If You Had Infinite IQ in PRISON?' (X_wiaDTxSho, 894 932 visningar på 8 dagar, läst 17 nov) + trenden 23 nov (trend/tli.json): 'What If You Were Born as Ghost?' 3 658 052 (vecka), What1fy 'What If U Could Pick Your Speed Every Morning?' 576 969 (vecka), Jeremy Bearimy 'What IF You Were HUNTED by The FBI, But Had Infinite IQ?' 448 595 (vecka).",
    "vi_slår_den_med": "Sökfrasen är evig (inte en veckotrend), kraften har en mätare tittaren känner igen (solnedgången, klockan), varje nivå lär ut en verklig sak om jordens rotation med källa, och klimax löses av två planterade saker (Priyas regel 'en sekund i taget' + lappen 86,401 – nivå 2; Abes kritmärken vid Foucault-pendeln – nivå 3) i stället för av kraften.",
    "trend": "Trend 23 nov (GitHub Action niche-trends, trend/tli.json 09:26 UTC): sökförslag för 'what would happen if' → 'what would happen if the earth stopped spinning' (nr 2), 'what would happen if you could freeze time'. Veckans största: 'What If You Were Born as Ghost?' 3 658 052, What1fy 'What If U Could Pick Your Speed Every Morning?' 576 969 (personlig kraft som ändrar fysiken = vår vinkel), Jeremy Bearimy 'Infinite IQ' 448 595. TREND_2026-11-22 (TLI) listar 'what if earth stopped spinning'. TREND_2026-11-23.md finns inte i projektet (projektet fullt) – analysen gjordes ur repots trend-data.",
}

types = [s["visual"]["type"] for s in SC]
standard_check = {
    "miniatyr": "A: '30 HOURS' i stor gul text (kraftens följd som siffra, TLI_STANDARD 6), lugn hjälte med klockan, chockade bifigurer, ljus varm miljö. B = fråga, C = HUD 'DAY: 30 HRS'.",
    "krok": "0 s hotet (solen uppe kl 21, 30 timmar), 6 s vändningen (solnedgången som aldrig kom), 11 s löftet i klartext ('every level of slowing the planet, and the real science behind each one'), 18 s slutlöfte + klocka (kronan fast, +4 min i timmen), 24 s gåta (Vole $2 M), 30 s första faktakortet (1 037 mph), 37 s gåta (Abe och kritan), 45 s titelfrågan. Ingen presentation före första händelsen.",
    "nivåer": "LEVEL 1 One millisecond · 2 One second (Priya) · 3 One minute (Abe) · 4 The 25-hour day · 5 The weather · 6 Grant Vole · 7 The longest day · Level 8: ??? (last man on earth). Dom efter varje nivå.",
    "verkligt_faktum_per_nivå": "1: dygnslängd +0,002 s, rekorddagen 2022, Sumatra 2,68 µs + skridskoåkaren, Three Gorges 0,06 µs · 2: 86 401, 27 skottsekunder 1972–2016, ±0,9 s, 2012-felen, 2035 · 3: Foucault 1851 (28 kg, 67 m, 270°, polerna) · 4: 23,5 h för 70 Ma, 372 dagar, rudistmusslan, Månen 3,82 cm/år, 2,3 ms/sekel · 5: rotation styr strömmar, Coriolis, ekvatorsvällningen, haven mot polerna · 6: 1 000 mph vindar, kollaps, 6 månaders dag, 2×10^29 J, ×1 000 000 asteroiden · 7: 2020 28 korta dagar, negativ skottsekund 2029? · Slut: kontorsstolen (xkcd).",
    "planteringar_som_betalas": "1) Priyas regel 'one second at a time, never one big jump' (nivå 2) → valet i klimax · 2) lappen 86,401 (nivå 2) → 86,400 vid soluppgången · 3) Abes kritmärken varje timme (nivå 3) → han ropar ut varje klick, LATE blir OK · 4) Rosas 'The sun's the boss' (nivå 1) → sista repliken · 5) Volés erbjudande $1 M/år (nivå 4) → $2 M i klimax, du skickar soluppgångsbilden · 6) Sudden stop = 1 000 mph (nivå 6) → därför kan du inte krossa klockan · 7) klockan i blomlådan (nivå 1) → DO NOT WIND i montern.",
    "känsloslag": "Abe skriver LATE och tittar upp på dig, Priyas arga ansikte på lappen, nio timmar med tummen mot kugghjulet, LATE blir OK.",
    "moraliskt_val": "Mitt i: Voles miljon per år för att behålla 25-timmarsdygnet. Klimax: ett snabbt hopp tillbaka (risk för planeten) eller en sekund i taget hela natten; och $2 M mot en vanlig dag. Speglar kroken.",
    "slut": "Fråga A/B till tittaren + fäst kommentar, 'Level 8: ???', ett verkligt fenomen att se i kväll (solnedgången = jorden som snurrar) och fiktionskortet.",
    "HUD": "DAY x / 30 · DAY (24 HRS → +1 S → +1 M → 25 → 27 → 30 → 26 → 24 HRS) · PAY ($0 → $310 → $1 440) på varje bild.",
    "bilder": f"Wide första 30 s (0 medium), {types.count('closeup')} närbilder (första vid ~6:12), {types.count('board')} tavlor, {types.count('plan')} ritning, {types.count('real')} THAT'S REAL-kort, scene-andel {types.count('scene') / len(types):.0%}. Tystnad (silence) vid klicket dag 1, kronan som fastnar och när du håller emot.",
    "innehall": f"Snitt {st['avg']} ord per say; {st['lt6']} say under 6 ord; faktaskyltar på skärmen: {types.count('real')} THAT'S REAL-kort + {sum(1 for s in SC if 'fact_strip' in s['visual'])} faktaremsor = {st['facts']}; största lucka mellan två faktaskyltar {st['maxgap']} s. Löftet i klartext vid 0:11. Högst ett icke-progressivt moment per nivå (Rosas replik, Priyas arga lapp, Abes LATE, taffy-eftermiddagen, –, –, –).",
    "längd": f"{st['words']} ord ≈ {st['min']:.1f} min (TLI_STANDARD 14–18 min; granskning 2 000–2 800 ord).",
}

notes = {
    "påhittat": "Klockan och kraften (kronan saktar ner jorden), alla personer (Rosa Delgado, Priya Shah, Abe Lindqvist, Grant Vole och Vole Freight), museet (ospecificerat 'science museum' i Denver), alla belopp ($3/ruta, $120/dag, $1 M/år, $2 M), klockslag och dygnslängder i berättelsen (25/27/30 timmar, +1/+4 min i timmen) och att väder och hav följer med långsamt (sägs i MADE UP-kortet). 16th Street och Denver är verkliga platser men inget som händer där är verkligt.",
    "verkligt": "Bara THAT'S REAL-korten och faktaremsorna. Verkliga personer (Léon Foucault, Dr. Bruce Warrington, Randall Munroe) nämns bara på faktakort/källrader, aldrig i påhittade scener.",
    "research": "Ingen Chrome i molnkörningen → youtube-transcriber gick inte; vidIQ användes inte (krediter återställs 23 nov 19:29 UTC, efter körningen). Topplistan kommer från GitHub Action niche-trends (trend/tli.json i repot, 23 nov 09:26 UTC). Inget transkript i dag – krokens 0/5/10/20/30 s är från TLI_STANDARD (DOOMPERK, läst 17 nov): 0 s premiss + orättvisa, ~5 s kraften visas, ~10 s vändningen, ~20 s en regel som låter som visdom, ~30 s målet + tidslinjelöften. Källor öppnade 23 nov via web-fetch (verbatimcitat): Astronomy.com (feb 2026), Space.com (2024), Live Science (2021, via space.com-URL), Scientific American, xkcd What If 26, NASA JPL (2005), NIST Leap Seconds (ändrad 28 okt 2026), Wikipedia Leap second, timeanddate.com, APS News 2007, Britannica (delvis), NOAA NESDIS, NOAA SciJinks, AGU 2020, NOAA Ocean Service. Wikipedia-sidorna för Foucault/Coriolis/geostationär bana nekades (behörighet) – inga fakta därifrån. Källorna anger ekvatorhastigheten olika (1 000 / 1 037 / 1 100 mph) – vi använder Astronomy.com:s 1 037 och anger spannet på en remsa.",
    "krokvarianter": [
        "A (VALD – visuell, fungerar utan ljud, matchar miniatyren): 'It's 9 p.m. in Denver, the sun is still up, and today is going to last 30 hours.' + filmande folkmassa.",
        "B (kraften först): 'Every time you turn this watch backward, the whole planet spins a little slower. Tonight the crown is stuck.'",
        "C (tittaren deltar): 'Look at the time on your screen. Now imagine the sun is still up, and it's going to stay up for another 9 hours.'",
    ],
    "hook_writer": "social-media-skills:hook-writer laddades inte (tidsgräns mot render 13:47); tre varianter skrevs enligt TLI_STANDARD 2 och A valdes för att den matchar miniatyren och syns utan ljud.",
    "humanizer": "humanizer:humanizer laddades och tillämpades på alla say-repliker (inga tankstreck, inga 'not X but Y', inga upprepande slutrepliker, inga AI-ord); automatisk sökning efter tankstreck/actually/quietly/crucial/key/Here's gav 0 träffar. Siffror, källor och fakta oförändrade.",
    "jamfor": "monetisering.py kördes mot tli-2026-11-22 (lång + Short, från GitHub-grenen). tli-2026-11-20/-21 lästes ur projektet men skrevs inte ut lokalt; de är andra berättelser med annan bildföljd (många närbilder/daycards) – render-körningen kör spärren igen mot alla.",
    "motor": "Nya platser som huvudchatten MÅSTE bygga (t.ex. tli1123.py, laddas efter dacli2, mönster som tli1850.py): street_16th (Denvers gågata med låga tegelhus och höghus, Klippiga bergen i bakgrunden; sky='stuck_evening' = varm guldorange kvällshimmel med solen kvar högt; sky='sunrise'/'sunset'), tower_platform (fönsterputsarplattform hängande på en glasfasad 31 våningar upp, rep och davit; wind 0..1 = rep som svänger), office_floor (kontorsvåning med blomlåda), apartment_kitchen, apartment_hall (trapphall i flerfamiljshus), hospital_it (serverrum/IT-kontor med skärmar och lapp på väggen), museum_hall (stor sal med Foucault-pendel: mässingskula på lång vajer över en ring av träpinnar; kritmärken på golvet, chalk_lines crooked/text), museum_dome (glaskupol sedd ovanifrån, hjälten i sele), museum_steps, crew_van, vole_office (kontor på 50:e våningen med stadsutsikt), elevator. Rekvisita: sun_stuck (x, y, clock='9:00 PM' = gatuklocka), crowd_phones (n, expr – folk som filmar med telefoner), watch_big (spin backward/stutter/none – stor mässingsklocka i bild), watch_open (grit), phone (screen), planter (watch), squeegee, note (text), server_racks, pendulum (pegs), chalk_lines, tv (screen), chart, glass_case (card). Kläder: hjälten window_washer + sele (ritas ovanpå, figurkoden orörd), hold brass_watch; Rosa crew_boss + gul hjälm; Priya hospital_it + nyckelband + laptop; Abe cardigan, age='old', flat_cap, krita, kneel=True; Grant Vole suit + bakåtkammat hår + telefon. visual.fact_strip {head, text, source} på 32 scener/närbilder MÅSTE ritas (nedre tredjedel, samma stil som 22/11) – annars blir faktaluckan > 30 s. HUD som 22/11 med a=['DAY', 'x HRS'] och b=['PAY', '$x']. Inga fallbacks till city_street för street_16th/tower_platform – miniatyrens scen måste synas i första bilden.",
}

out = {
    "channel": "The Long If", "title": TITLE, "standard": "TLI_STANDARD", "style": "qm", "look": "stickman_day",
    "voice": "am_puck", "speed": 1.05, "lang": "en-us", "music": "calm", "music_level": 0.07,
    "beats": beats, "scenes": SC, "seo": seo, "thumb": thumb, "forbattring": forbattring,
    "standard_check": standard_check,
    "experiment": {"variable": "evig sökfras ('what if earth stopped spinning') i stället för veckotrend-kraft",
                   "metric": "exponeringar från sök/Shorts och 0:30-andel mot tli-2026-11-22", "decide_at": "48 h"},
    "notes": notes,
}
json.dump(out, open("manus/tli-2026-11-23.json", "w"), ensure_ascii=False, indent=1)

# ---------------- SHORT ----------------
H = {"outfit": "window_washer", "harness": True, "hold": "brass_watch"}
def sc(say, loc, extra=None, **kw):
    vis = {"type": "scene", "location": loc, "shot": "wide", "sky": kw.pop("sky", "day"),
           "hero": dict(H, x=kw.pop("x", 0.4), expr=kw.pop("expr", "worried"), arms=kw.pop("arms", "down"))}
    if "walk" in kw: vis["hero"]["walk_to"] = kw.pop("walk")
    vis.update(extra or {})
    d = {"say": say, "visual": vis}; d.update(kw); return d
LSRC = "Wikipedia, 'Leap second'"
short_sc = [
    sc("You turn your watch back one second, and every day on Earth gets one second longer.", "tower_platform",
       {"props": [{"type": "watch_big", "x": 0.3, "spin": "stutter"}], "hud": {"a": ["DAY", "24 HRS +1 S"]}}, x=0.45, expr="shock", walk=0.52, silence=True),
    {"say": "At midnight, every clock in a hospital downtown starts disagreeing with every other clock.",
     "visual": {"type": "scene", "location": "hospital_it", "shot": "wide", "hero": {"name": "Priya", "outfit": "hospital_it", "x": 0.4, "expr": "shock", "arms": "head", "walk_to": 0.5},
                "props": [{"type": "server_racks", "x": 0.8}], "hud": {"a": ["DAY", "86,401 S"]}}},
    {"say": "A day with a leap second really has 86,401 seconds instead of 86,400.",
     "visual": {"type": "real", "head": "THAT'S REAL", "big": "86,401", "text": "seconds in a day with a leap second", "source": "timeanddate.com, 'Leap seconds'"}},
    {"say": "And one extra second has broken real computers. In 2012, Qantas and Mozilla reported problems.",
     "visual": {"type": "real", "head": "THAT'S REAL", "big": "JUNE 30, 2012", "text": "Qantas, Mozilla and Linux sites hit", "source": LSRC}},
    {"say": "So you try to turn the watch forward again, and the crown won't move.",
     "visual": {"type": "closeup", "location": "tower_platform", "expr": "shock", "look": -1, "thought": "JAMMED", "bad": True}},
    sc("The second hand starts turning backward on its own. Full video on the channel.", "street_16th",
       {"props": [{"type": "sun_stuck", "x": 0.7, "y": 0.28, "clock": "9:00 PM"}, {"type": "crowd_phones", "x": 0.5, "n": 30, "expr": "shock"}], "hud": {"a": ["DAY", "30 HRS"]}},
       x=0.4, expr="shock", walk=0.48, sky="stuck_evening"),
]
sw = sum(len(s["say"].split()) for s in short_sc)
sdur = sum(max(len(s["say"].split()) / 2.6 + 0.45, 2.0) for s in short_sc)
SDESC = "Full video: https://youtu.be/<id>\n\nTurn a watch back one second and the whole Earth spins slower. One extra second sounds harmless, but a day with a leap second has 86,401 seconds, and the June 2012 leap second caused software problems at Qantas, Mozilla and many Linux sites. A fictional What If story with real facts (timeanddate.com, Wikipedia 'Leap second')."
short = {
    "channel": "The Long If", "title": "What If Earth Stopped Spinning... Just a Little? #shorts", "style": "qm", "look": "stickman_day",
    "vertical": True, "format": "1080x1920", "voice": "am_puck", "speed": 1.05, "lang": "en-us", "music": "calm", "music_level": 0.06,
    "headline": "One second slower.",
    "long_video": f"automation/manus/tli-2026-11-23.json ({TITLE})",
    "scenes": short_sc,
    "beats": [{"t": "0:00", "typ": "vändning", "text": "ett klick – jorden saktar in"},
              {"t": "0:05", "typ": "hot", "text": "sjukhusets klockor går isär"},
              {"t": "0:11", "typ": "vändning", "text": "verkligt: 86 401 sekunder"},
              {"t": "0:16", "typ": "hot", "text": "verkligt: 2012-felen"},
              {"t": "0:23", "typ": "hot", "text": "kronan sitter fast"},
              {"t": "0:28", "typ": "gåta", "text": "cliffhanger: visaren går bakåt själv"},
              {"t": "0:32", "typ": "callback", "text": "Full video on the channel"}],
    "seo": {
        "title": "What If Earth Stopped Spinning... Just a Little? #shorts",
        "sokfras": "what if earth stopped spinning",
        "sokfras_kalla": "YouTubes sökförslag (trend/tli.json 23 nov: 'what would happen if the earth stopped spinning'; TREND_2026-11-22: 'what if earth stopped spinning')",
        "summary": SDESC, "description": SDESC,
        "hashtags": ["shorts", "whatif", "story"],
        "keywords": ["what if earth stopped spinning", "leap second", "what if", "earth rotation"],
        "sources": ["https://www.timeanddate.com/time/leapseconds.html", "https://en.wikipedia.org/wiki/Leap_second"],
        "disclaimer": "Fictional What If story; the leap-second facts are real.",
        "long_video_url": "https://youtu.be/<id>",
    },
    "thumb": {"kind": "short_cover", "text": "[gul] +1 SECOND|BROKE EVERYTHING",
              "klickfraga": "Hur kan en enda extra sekund få ett sjukhus datorer att krascha – och varför sitter klockan fast?",
              "hot_i_bild": "Den stora mässingsklockan med sekundvisaren som går bakåt, överst i vertikalt format, och solen som hänger kvar över gatan nederst.",
              "skiljer_sig": "Förra TLI-Shorten (22/11) var en lastbil i sladd på is; nu en klocka i närbild + varm kvällsgata.",
              "jamfor_ark": "chk/jamfor-tli-2026-11-23-short.png",
              "forsta_scen_matchar": "Scen 1 visar hjälten på fönsterputsarplattformen med klockan som hackar – samma klocka och plattform som långa videons nivå 1."},
    "forbattring": {
        "forra_videon": "tli-2026-11-22-short 'What If You Could Stop Time? (One Breath Only)' (första TLI-Shorten, i GitHub-grenen; ingen mätning än).",
        "problem": "TLI:s långa videor får ~0 exponeringar; Shorts gav LS/STE/QM nästan all tidig trafik (TITTARTID_REGLER v48).",
        "andring": "DISTRIBUTIONSORDER 2: titel med sökfrasen + #shorts, EN vändning (en extra sekund kraschar datorer, verkligt 2012), länk till långa videon först i beskrivningen, cliffhanger (kronan fast).",
        "forvantat": "≥ 300 visningar i Shorts-flödet på 48 h och klick till den långa videon.",
        "referens": "QM-Shorten 22/11 och TLI-Shorten 22/11 (samma mall: en vändning + 'Full video on the channel').",
        "vi_slår_den_med": "Två verkliga fakta på 30 s (86 401 sekunder, Qantas/Mozilla 2012) och en tydlig cliffhanger som bara långa videon löser.",
    },
    "notes": {
        "moment": "Nivå 2 ur långa videon (en extra sekund, sjukhuset) + slutet av nivå 6 (kronan fastnar).",
        "langd": f"≈ {sw} ord ≈ {sdur:.0f} s med am_puck 1,05 (20–45 s).",
        "uppladdning": "Via Studio i ägarens Chrome (Create → Upload), kodad ≤ 3,7 MB (720×1280, ~550 kbit/s, 64 kbit/s ljud) – inte via vidIQ. Render-körningen ersätter <id> med den långa videons id.",
        "kontroll": "monetisering.py GODKÄNT. granskning.py: se körningens rapport – spärren saknar Shorts-gren (TLI-ordgräns 2 000–2 800 och beats-krav per minut för långform), samma som TLI/QM-Shorten 22/11. Spärren ändrades inte.",
    },
}
json.dump(short, open("manus/tli-2026-11-23-short.json", "w"), ensure_ascii=False, indent=1)
print("long words", st["words"], "short words", sw, "short s", round(sdur, 1))
