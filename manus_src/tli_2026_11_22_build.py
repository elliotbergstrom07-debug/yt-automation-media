"""Bygger automation/manus/tli-2026-11-22.json + -short.json av parts.json (kör tli_2026_11_22.py först)."""
import json

p = json.load(open("parts.json"))
SC, beats = p["SC"], p["beats"]
TITLE = "What If You Could Stop Time While Holding Your Breath?"

SOURCES = [
    "https://www.smithsonianmag.com/smithsonian-institution/ask-smithsonian-whats-longest-you-can-hold-your-breath-180960905/",
    "https://www.mayoclinic.org/diseases-conditions/hiccups/symptoms-causes/syc-20352613",
    "https://health.osu.edu/health/general-health/what-happens-when-you-hold-your-breath",
    "https://www.scientificamerican.com/article/breath-holding-dive-reflex-extends",
    "https://www.guinnessworldrecords.com/news/2021/5/freediver-holds-breath-for-almost-25-minutes-breaking-record-660285",
    "https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6419a3.htm",
    "https://www.cdc.gov/mmwr/preview/mmwrhtml/mm6425a6.htm",
    "https://www.discovery.com/science/What-Would-Happen-If-You-Stopped-Time",
    "https://en.wikipedia.org/wiki/Chronostasis",
    "https://www.astronomy.ohio-state.edu/pogge.1/Ast162/Unit5/gps",
    "https://hyperphysics.gsu.edu/hbase/Relativ/airtim.html",
    "https://www.nationalgeographic.com/science/article/time-doesnt-actually-slow-down-in-a-crisis",
    "https://corpora.tika.apache.org/base/docs/govdocs1/144/144771.html",
    "https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-11/Winter%20Driving%20Tips_2022-2023_tag_0.pdf",
    "https://www.iihs.org/research-areas/fatality-statistics/detail/bicyclists/trends",
    "https://www.nationalgeographic.com/environment/article/black-ice",
    "https://www.weather.gov/safety/winter-ice-frost",
    "https://www.fmcsa.dot.gov/registration/commercial-drivers-license/drivers",
]

SUMMARY = """What if you could stop time, but only for as long as you can hold your breath? Breathe in and every snowflake on the street hangs in the air. Breathe out and the world starts again. You're a bike courier in Chicago in December, and in 30 days you find out the rules, save a rival from a skidding sedan, get paid to freeze time 30 times a day, learn to breathe from a 74-year-old swim coach at a bus stop, and fall down an icy staircase with empty lungs. On day 30 a box truck slides on black ice toward a bus shelter with five people inside, and you have about 41 seconds of air.

This is a fictional What If story. The power and every character (Hal, Marisol, Dex) are made up. The facts on screen are real:
- Most people can hold their breath for 30 seconds to a few minutes; trained free divers 4–8 minutes or more; high carbon dioxide, not low oxygen, drives the burn (Smithsonian Magazine, quoting Mayo Clinic's Dr. Clayton Cowl)
- A hiccup is a diaphragm spasm that snaps the vocal cords shut; see a doctor after 48 hours (Mayo Clinic)
- "One minute is probably the limit"; holding too long can make you pass out (Ohio State Wexner Medical Center, Dr. Jonathan Parsons)
- Diving reflex: cold water on the face can slow a person's heart 10% or more, roughly 90% in some marine mammals; Stéphane Mifsud 11:35 in 2009 (Scientific American)
- Guinness record 24:37.36 by Budimir Šobat, 56, Sisak, Croatia, 27 March 2021, after breathing pure oxygen (Guinness World Records)
- Dangerous underwater breath-holding, New York State 1988–2011: 16 swimmers, 4 deaths; hyperventilating first lowers CO2 and risks blackout (CDC MMWR, 2015)
- If time truly stopped, light, sound and air would stop too (Discovery, quoting physicist Sean Carroll)
- GPS satellite clocks run about 38 microseconds a day fast; uncorrected, positions would drift about 10 km a day (Prof. Richard Pogge, Ohio State)
- Hafele–Keating 1971: atomic clocks lost 59 ns flying east and gained 273 ns flying west (HyperPhysics)
- Volunteers dropped 150 feet guessed their fall lasted 36% longer, but time didn't slow down (National Geographic, on Stetson, Fiesta & Eagleman, PLoS ONE 2007)
- Without ABS, hard braking can lock the wheels and take away steering (NHTSA); slow down and leave more distance on slick roads (NHTSA Winter Driving Tips)
- 1,075 U.S. bicyclists killed in crashes with motor vehicles in 2024, 81% in urban areas (IIHS)
- Black ice is thin, clear ice on dark asphalt; bridges and overpasses freeze first (National Geographic, National Weather Service)
- Stopped-clock illusion (chronostasis): the first second you see can seem up to half a second longer (Wikipedia)

Never practice holding your breath in water, never hyperventilate first, and never do it alone."""

seo = {
    "title": TITLE,
    "title_b": "You Can Stop Time, But Only While You Hold Your Breath",
    "sokfras": "what if you could stop time",
    "sokfras_kalla": "YouTubes sökförslag 22 nov 2026: förslag nr 1 för prefixet 'what if you could' (trend/tli.json i repot, GitHub Action niche-trends) + TREND_2026-11-22.md. Även 'what would happen if you could freeze time' bland förslagen för 'what would happen if'.",
    "hook": "A box truck is sliding on black ice toward a bus shelter with five people inside. You breathe in and hold it. Every snowflake on Halsted Street stops in midair.",
    "summary": SUMMARY,
    "description": SUMMARY,
    "disclaimer": "This is a fictional What If story. The power and all characters are made up; the breathing, safety, physics and traffic facts are real and sourced below. Never practice breath-holding in water or alone.",
    "chapters": "00:00 The truck on Halsted · Level 1: The hiccups · Level 2: The rules · Level 3: Dex · Level 4: The stopwatch · Level 5: Hal · Level 6: The fall · Level 7: The ice · The choice",
    "keywords": ["what if you could stop time", "what would happen if you could freeze time", "stop time", "freeze time", "what if",
                 "holding your breath", "how long can you hold your breath", "diving reflex", "time dilation", "what if story",
                 "what if animation", "stickman story", "the long if", "black ice"],
    "sources": SOURCES,
    "question": "On day 30, would you hold past your limit to save Hal faster, or breathe every 20 seconds like he said? A or B.",
    "pinned_comment": "A or B: hold past your limit to drag Hal out faster, or breathe every 20 seconds like he told you? Level 8 is coming: what if the Earth stopped spinning for one second?",
    "hashtags": ["#whatif", "#story", "#animation"],
    "playlist": "What If You Could...? Hypothetical Scenarios",
}

thumb = {
    "kind": "tli",
    "script": "huvudchatten bygger (thumbs_v3_all.py-stil; ny plats halsted_street + frozen=True)",
    "klickfraga": "Tiden står still bara så länge han håller andan – lastbilen hänger 9 fot från en busskur med fem personer, och han har 41 sekunder luft. Hinner han?",
    "hot_i_bild": "En stor box truck som sladdar snett i bild på blank svart is, fryst mitt i rörelsen med snöflingor som hänger i luften, och hörnet bara en meter från en glasbusskur med fem personer – lastbilen tar ~45 % av bilden (vänster–mitten).",
    "skiljer_sig": "Förra TLI (tli-2026-11-21) var ett vertikalt hotelltorn med röken uppe till vänster och text nere till vänster. Nu: horisontell vintergata i dagsljus, hotet (lastbilen) i vänster–mitten, hjälten lugnt gående i förgrunden till höger med kinderna fulla av luft, gul text uppe till höger. Ny effekt: frusna snöflingor/blåaktig ton = superkraften syns i bild.",
    "jamfor_ark": "chk/jamfor-tli-2026-11-22.png",
    "forsta_scen_matchar": "Scen 1 (0–7 s) är A-miniatyren i rörelse: samma Halsted-gata i ljust vinterdagsljus, box trucken sladdar på svart is mot busskuren med fem personer (threat=truck_skid, drive_to). Scen 2 (7 s) fryser samma bild: snöflingorna stannar (frozen=True, tystnad). HUD 'AIR 0:41' = miniatyrens siffra.",
    "variants": [
        {"id": "A", "layout": "hotet vänster–mitten / hjälten höger förgrund / text uppe till höger",
         "big": "41 SEC", "label": "OF AIR LEFT",
         "bild": "Lastbilen fryst i sladd 9 fot från glaskuren; snöflingor som hänger stilla; fem bifigurer i kuren med uppspärrade ögon (Hal längst fram, ler); hjälten (svart stickman, gröna ögon, cykelbudsjacka och hjälm) går lugnt framåt med kinderna fulla av luft. Gult '41 SEC' + röd etikett 'OF AIR LEFT'."},
        {"id": "B", "layout": "fråga, hjälten centrerad stort",
         "big": "HOW LONG CAN YOU HOLD IT?", "label": "",
         "bild": "Hjälten i mitten med uppblåsta kinder och ett stort frusen-tid-ljus runt sig; bakom honom gatan helt stilla (bil, duva och kaffe i luften). Annan vinkel: själva begränsningen."},
        {"id": "C", "layout": "HUD-siffra, split",
         "big": "AIR 0:41", "label": "TIME: STOPPED",
         "bild": "Vänster: stort HUD-instrument 'AIR 0:41' som en tryckmätare. Höger: lastbilens hjul låsta på isen och förarens fot på bromsen (gåtan som löser klimax)."},
    ],
}

forbattring = {
    "forra_videon": "tli-2026-11-21 'What If You Could Never Forget Anything for 30 Days?' (MANUS KLART 21/11, publiceringsstatus saknas i kö.md) och senast publicerade OOBnQjk7zV0 '1850' – 0 exponeringar (KANALANALYS_2026-11-22).",
    "matt_forra": "TLI: 0–1 exponeringar per lång video; ingen tittarkurva än (TITTARTID_ANALYS_2026-11-22).",
    "problem": "Distribution: titlarna har inte varit exakta sökförslag och kanalen har inga Shorts. Innehåll: tidigare TLI-manus hade verkliga fakta bara på 12 kort (en var ~75:e s) och långa stämningsstretcher – förlorarmönstret i TITTARTID_ANALYS.",
    "andring": "TITTARTID_REGLER: TRENDORDER (titeln innehåller förslag nr 1 'what if you could stop time'), INNEHÅLLSORDER (DUI-mallen på What if: 7 numrerade nivåer med dom, en verklig fakta med källa på skärmen minst var 30:e s – 33 THAT'S REAL-kort + 28 faktaremsor + 2 säkerhetskort, största lucka 29,9 s, snitt 19 ord/replik, 0 repliker < 6 ord), FORMATORDER/TLI-raden (sökfras-titel) och DISTRIBUTIONSORDER 2 (första TLI-Shorten).",
    "forvantat": "Exponeringar via sök på 'what if you could stop time' och via Shorten (mål ≥ 300 första veckan), CTR ≥ 3 %, ≥ 55 % kvar vid 0:30 och ≥ 35 % vid 2:00.",
    "referens": "DOOMPERK 'What If You Had Infinite IQ in PRISON?' (X_wiaDTxSho, 894 932 visningar på 8 dagar, läst 17 nov) + trenden 22 nov: ConChaser 'What If You Could See Everyone's IQ?' 2 898 995 (månad), What If Effect 'What If You Were Born With Infinite IQ?' 890 222 (vecka).",
    "vi_slår_den_med": "Kraften har en fysisk mätare som tittaren känner i sin egen kropp (håll andan medan du tittar), varje nivå lär ut en verklig sak om andning, tid eller is med källa, och klimaxet löses av två planterade fakta (låsta hjul kan inte styra – nivå 3; Hals regel 'never past the edge alone' – nivå 5) i stället för av kraften.",
    "trend": "Ämne/titel ur TREND_2026-11-22 (TLI): 'What If You Could …'-superkraft. Sökförslag: 'what if you could stop time' (förslag nr 1, trend/tli.json). Trendande videor: ConChaser 'What If You Could See Everyone's IQ?' 2 898 995 visningar (månad), 'What If You Could See Everyone's Future Wealth?' 2 388 323 (månad), What If Effect 'What If You Were Born With Infinite IQ?' 890 222 (vecka). Ingen video med exakt vår titel hittad (webbsök 22/11); 'What If You Could Stop Time but Only for 1 Second' finns – vår begränsning (andan) är en annan.",
}

types = [s["visual"]["type"] for s in SC]
says = [len(s["say"].split()) for s in SC]
standard_check = {
    "miniatyr": "A: kraften som siffra '41 SEC' i stor gul text (TLI_STANDARD 6), lugn hjälte på väg framåt, 5 bifigurer i kuren med uppspärrade ögon, ljus vinterdag. B = fråga, C = HUD 'AIR 0:41'.",
    "krok": "0 s hotet (lastbil mot kur, 5 personer), 7 s kraften visas (andas in – snön stannar, tystnad), 12 s löftet i klartext ('every level of stopping time with one breath, and the real science of holding it'), 19 s insatsen med siffror (9 fot, 41 s) = slutlöfte, 26 s första verkliga faktakortet, 34 s gåtan (Hal lärde dig), 49 s titelfrågan. Ingen presentation före första händelsen.",
    "nivåer": "LEVEL 1 The hiccups · 2 The rules · 3 Dex · 4 Marisol (stopwatch/GPS) · 5 Hal · 6 The fall · 7 The ice · Level 8: ??? (what if Earth stopped spinning). Dom efter varje nivå.",
    "verkligt_faktum_per_nivå": "1: Mayo hicka ×2, Smithsonian CO2 · 2: Discovery ljus/ljud/luft · 3: NHTSA låsta hjul, IIHS 1 075 / 81 % · 4: GPS 38 µs/10 km (Pogge), Hafele–Keating 59/273 ns, OSU svimning/1 min · 5: CDC 16/4 + hyperventilation, dykreflex 10 %/90 %, fridykare 4–8 min, Mifsud 11:35, Guinness 24:37 + rent syre · 6: Eagleman 150 ft / 36 % / läste inte snabbare · 7: NHTSA vinter + ABS, CDC blackout, CO2-narkos, svart is (NatGeo/NWS), FMCSA 26 001 lb · Slut: IIHS 3:e högsta, kronostas.",
    "planteringar_som_betalas": "1) Låsta hjul kan inte styra (nivå 3, Dex) → klimax: foten av bromsen + ratten · 2) Mississippi-räkningen (nivå 2) → '33 Mississippi, 34' och '20 Mississippi' · 3) Hals regel 'Breathe, kid. Never past the edge alone' (nivå 5) → valet · 4) Hal i glaslådan kl 4:40 (nivå 5) → busskuren dag 30 · 5) Marisols stoppur (nivå 1) → 4 minuter sen · 6) $500-paketet 4:45 (nivå 6) → valet pengar mot människor · 7) tomma lungor = ingen kraft (nivå 6) → sprinten tar luften dag 30. Återkommande skämt: 'Hiccup' / Hals mint.",
    "känsloslag": "Dex säger ditt namn, Hal ler bakom glaset, 'Breathe, kid.' i snön, Hal sparar platsen längst från vägen.",
    "moraliskt_val": "Mitt i: Marisols rush route ($40/$500) – kraften för pengar. Klimax: hålla förbi gränsen ensam (snabbare, risk för blackout) eller följa Hals regel; och $500-paketet mot fem personer. Speglar kroken.",
    "slut": "Fråga A/B till tittaren + fäst kommentar, 'Level 8: ???', ett verkligt fenomen att prova i kväll (kronostas) och säkerhetskortet.",
    "HUD": "DAY x / 30 · AIR (0:38 → 1:25 → 0:41 efter sprinten) · PAY ($0 → $1 840 → $4 100) på varje bild.",
    "bilder": f"Wide första 30 s (0 medium), {types.count('closeup')} närbilder (ingen före 2:15), {types.count('board')} tavlor, {types.count('plan')} ritningar, {types.count('real')} THAT'S REAL-kort, scene-andel {types.count('scene') / len(types):.0%}. Tystnad (silence) vid varje frysning som är en vändning.",
    "innehall": f"Snitt {sum(says) / len(says):.1f} ord per say; {sum(1 for n in says if n < 6)} say under 6 ord; faktaskyltar på skärmen: {types.count('real')} THAT'S REAL-kort + {sum(1 for s in SC if 'fact_strip' in s['visual'])} faktaremsor (fact_strip) + 2 säkerhetskort = 63; största lucka mellan två faktaskyltar 29,9 s. Löftet i klartext vid 0:12. Högst ett icke-progressivt moment per nivå (hicka/skratt, tystnaden, 'Hiccup', –, Hals tupplur, –, soffan på isen).",
    "längd": f"{sum(says)} ord ≈ {p['total'] / 60:.1f} min (TLI_STANDARD 14–18 min; granskning 2 000–2 800 ord).",
}

notes = {
    "påhittat": "Kraften (tiden stannar medan du håller andan), alla personer (Marisol Vance, Dex Moreau, Hal Benning, föraren, de fem i kuren), budfirman, alla belopp ($40, $500, $1 840, $4 100), klockslag, avstånd (9 fot) och andningstiderna 38 s / 1:25 / 41 s. Halsted, Madison, Jackson, Wacker och busslinje 8 Halsted är verkliga gatunamn i Chicago men inget som händer där är verkligt.",
    "verkligt": "Bara THAT'S REAL-korten, faktaremsorna och säkerhetskorten. Verkliga personer (Budimir Šobat, Stéphane Mifsud, Sean Carroll, Richard Pogge) nämns bara på faktakort, aldrig i påhittade scener.",
    "research": "vidIQ 0 krediter (återställs 23 nov 19:29 UTC). Ingen Chrome i molnkörningen → youtube-transcriber gick inte; TubeAlfred-nyckel saknas. Topplistan kommer från GitHub Action niche-trends (trend/tli.json i repot, 22 nov 03:05): ConChaser 'See Everyone's IQ?' 2 898 995 (mån), 'Future Wealth?' 2 388 323 (mån), What If Effect 'Born With Infinite IQ?' 890 222 (vecka), What1fy 'Pick Your Speed Every Morning?' 486 397 (vecka). Inget transkript i dag – krokens 0/5/10/20/30 s är från TLI_STANDARD (DOOMPERK, läst 17 nov): 0 s premiss + orättvisa, ~5 s kraften visas, ~10 s vändningen, ~20 s en regel som låter som visdom, ~30 s målet + tidslinjelöften. Källor öppnade 22 nov via web-fetch: Smithsonian, Mayo Clinic, OSU Wexner (health.osu.edu), Scientific American, Guinness 2021, CDC MMWR mm6419a3 + erratum mm6425a6, Discovery, Wikipedia Chronostasis, Pogge (Ohio State), HyperPhysics, National Geographic (Eagleman 2007; black ice 2026), NHTSA ABS + Winter Driving Tips, IIHS Fatality Facts 2024, NWS Ice Storms, FMCSA CDL. PLoS ONE-originalet (PMC2110887) blockerades av reCAPTCHA – siffrorna 150 ft/36 % är från National Geographics genomgång. Wikipedia anger kronostas 'upp till en halv sekund' med Yarrow et al. 2006 som källa (inte 2001).",
    "krokvarianter": [
        "A (VALD – visuell, fungerar utan ljud, matchar miniatyren): 'A box truck is sliding on black ice toward a bus shelter with five people inside.' + 'You breathe in and hold it. Every snowflake on Halsted Street stops in midair.'",
        "B (kraften först): 'You can stop time. The catch is that it only lasts as long as you can hold your breath, and you just ran six blocks.'",
        "C (tittaren deltar): 'Take a breath and hold it. Right now. However long you last is how long you'd get to stop the world.'",
    ],
    "hook_writer": "social-media-skills:hook-writer laddades inte i denna körning (tidsgräns mot render 13:47); tre varianter skrevs enligt TLI_STANDARD 2 och A valdes för att den matchar miniatyren och syns utan ljud.",
    "humanizer": "humanizer:humanizer-reglerna tillämpade på alla say-repliker (inga tankstreck, 'truly'/'quietly'/'actually' bort, inga 'not X but Y' utom där källan själv rättar en vanlig missuppfattning (CO2, inte syrebrist)); siffror, källor och fakta oförändrade.",
    "motor": "Nya platser som huvudchatten MÅSTE bygga (t.ex. tli1122.py, laddas efter dacli2, mönster som tli1850.py): halsted_street (ljus vintergata i Chicago, snö, tegelhus, gatuskyltar 'HALSTED', svart is som blank yta; sky='winter_day'), bus_shelter (glaskur med linjeskylt '8 HALSTED' och bänk; props bus_shelter people=0..5, cracked=True), courier_depot (budfirma med cyklar på väggen, radio, dispatchdisk), bathroom, apartment_window (lägenhet med fönster mot staden), intersection (korsning med trafikljus, cykelbana), dispatch_office, train_stairs (isig trappa upp till en tågperrong, räcke med nitar, duva), truck_cab (förarhytt: ratt, pedaler). FLAGGAN frozen=True är kärnan: snöflingor stilla i luften, lätt blå/avmättad ton på allt utom hjälten, figurer (frozen=True) och föremål helt stilla, och 'silence' i ljudet. Rekvisita: box_truck (skid, wheels='locked', steer, drive_to), sedan (skid, wheels, steer, drive_to), bus_shelter, snow_frozen, measure (text '9 FT'/'8 FT'), coffee_frozen/coffee_splash, phone (screen), count_bubble (text), window_city, bike, packages (flying), pigeon, snowpile, pedal (pressed), steering_wheel (turn), people_moved (n), snowbank, sink, street_clock. Kläder: hjälten outfit courier + cykelhjälm + budväska (ritas ovanpå, figurkoden orörd); Marisol dispatch + headset + stoppur; Dex orange_courier + orange cykel; Hal ymca_jacket, age='old', keps, mintpåse. NYTT FÄLT visual.fact_strip {head, text, source}: nedre tredjedel med 'THAT'S REAL' + text + SOURCE-rad (samma stil som real-kortets källrad) på 28 scener – den räknas i INNEHÅLLSORDER 2 och MÅSTE ritas, annars blir faktaluckan > 30 s. HUD som 21/11 (dacli2.hud) med a=['AIR', 'm:ss'] och b=['PAY', '$x']. Inga fallbacks till city_street för halsted_street/bus_shelter – miniatyrens scen måste synas i första bilden.",
}

out = {
    "channel": "The Long If", "title": TITLE, "standard": "TLI_STANDARD", "style": "qm", "look": "stickman_day",
    "voice": "am_puck", "speed": 1.05, "lang": "en-us", "music": "calm", "music_level": 0.07,
    "beats": beats, "scenes": SC, "seo": seo, "thumb": thumb, "forbattring": forbattring,
    "standard_check": standard_check,
    "experiment": {"variable": "titel = exakt sökförslag nr 1 + faktaskylt var 30:e s + första TLI-Shorten",
                   "metric": "exponeringar från sök/Shorts och 0:30-andel mot tli-2026-11-21", "decide_at": "48 h"},
    "notes": notes,
}
json.dump(out, open("manus/tli-2026-11-22.json", "w"), ensure_ascii=False, indent=1)

# ---------------- SHORT ----------------
def sc(say, loc, v=None, **kw):
    vis = {"type": "scene", "location": loc, "shot": "wide", "sky": "winter_day",
           "hero": {"outfit": "courier", "helmet": True, "x": kw.pop("x", 0.4), "expr": kw.pop("expr", "worried"), "arms": kw.pop("arms", "down")}}
    if "walk" in kw: vis["hero"]["walk_to"] = kw.pop("walk")
    vis.update(v or {})
    d = {"say": say, "visual": vis}; d.update(kw); return d

TRUCK = {"type": "box_truck", "x": 0.2, "skid": True, "wheels": "locked"}
SHELTER = {"type": "bus_shelter", "x": 0.72, "people": 5, "route": "8 HALSTED"}
def R2(say, big, text, source):
    return {"say": say, "visual": {"type": "real", "head": "THAT'S REAL", "big": big, "text": text, "source": source}}
short_sc = [
    sc("Time stops while you hold your breath. A truck slides toward 5 people.", "halsted_street",
       {"props": [dict(TRUCK, drive_to=0.3), SHELTER, {"type": "snow_frozen"}], "frozen": True, "threat": "truck_skid", "hud": {"a": ["AIR", "0:41"]}}, x=0.45, expr="shock", walk=0.52, sfx="horn"),
    {"say": "You have 41 seconds of air. The truck is 9 feet away.",
     "visual": {"type": "plan", "title": "ONE BREATH", "items": [{"box": [0.08, 0.2, 0.84, 0.14], "label": "AIR: 0:41", "hot": True}, {"box": [0.08, 0.38, 0.84, 0.14], "label": "TRUCK: 9 FT"}, {"box": [0.08, 0.56, 0.84, 0.14], "label": "PEOPLE: 5"}]}},
    {"say": "You push it with everything you have. It doesn't move an inch.", "silence": True,
     "visual": {"type": "closeup", "location": "halsted_street", "expr": "worried", "look": -1, "thought": "NOTHING", "bad": True, "frozen": True, "hud": {"a": ["AIR", "0:30"]}}},
    R2("Then you see the wheels. Locked wheels can't steer, NHTSA warns.",
       "LOCKED = NO STEERING", "hard braking without ABS can lock the wheels", "NHTSA, 'Antilock Brake Systems (ABS)'"),
    sc("So you climb into the cab and lift the driver's boots off the brake.", "truck_cab",
       {"props": [{"type": "pedal", "x": 0.5, "pressed": False}], "frozen": True, "hud": {"a": ["AIR", "0:24"]}}, arms="reach", walk=0.46),
    {"say": "20 seconds left. You turn the wheel toward the snowbank.",
     "visual": {"type": "label", "big": "AIR 0:20", "text": "a quarter turn toward the snowbank", "bad": True}},
    sc("But the back corner still points at the old man inside. Full video on the channel.", "halsted_street",
       {"props": [dict(TRUCK, steer="left"), SHELTER, {"type": "snow_frozen"}], "frozen": True, "hud": {"a": ["AIR", "0:04"]},
        "friends": [{"name": "Hal", "x": 0.76, "outfit": "ymca_jacket", "age": "old", "frozen": True}]}, x=0.5, expr="shock", walk=0.56),
]
sw = sum(len(s["say"].split()) for s in short_sc)
sdur = sum(max(len(s["say"].split()) / 2.6 + 0.45, 2.0) for s in short_sc)
short = {
    "channel": "The Long If", "title": "What If You Could Stop Time? (One Breath Only) #shorts", "style": "qm", "look": "stickman_day",
    "vertical": True, "format": "1080x1920", "voice": "am_puck", "speed": 1.05, "lang": "en-us", "music": "calm", "music_level": 0.06,
    "headline": "41 seconds of air. One truck.",
    "long_video": f"automation/manus/tli-2026-11-22.json ({TITLE})",
    "scenes": short_sc,
    "beats": [{"t": "0:00", "typ": "hot", "text": "lastbilen glider mot 5 personer"},
              {"t": "0:03", "typ": "vändning", "text": "du håller andan – allt fryser"},
              {"t": "0:05", "typ": "hot", "text": "41 s luft, 9 fot"},
              {"t": "0:10", "typ": "hot", "text": "lastbilen rör sig inte"},
              {"t": "0:15", "typ": "vändning", "text": "låsta hjul = ingen styrning (NHTSA)"},
              {"t": "0:20", "typ": "lösning", "text": "foten av bromsen"},
              {"t": "0:26", "typ": "hot", "text": "20 s luft kvar, ratten"},
              {"t": "0:30", "typ": "gåta", "text": "cliffhanger: hörnet siktar fortfarande på Hal"},
              {"t": "0:35", "typ": "callback", "text": "Full video on the channel"}],
    "seo": {
        "title": "What If You Could Stop Time? (One Breath Only) #shorts",
        "sokfras": "what if you could stop time",
        "sokfras_kalla": "YouTubes sökförslag nr 1 för 'what if you could' (trend/tli.json, 22 nov 2026)",
        "summary": "Full video: https://youtu.be/<id>\n\nTime only stays stopped while you hold your breath, and a box truck is sliding on black ice toward a bus shelter. You can't push it. But its wheels are locked, and NHTSA says that without antilock brakes, hard braking can lock the wheels and take away steering. A fictional What If story with a real fact.\n\nNever practice holding your breath in water or alone.",
        "description": "Full video: https://youtu.be/<id>\n\nTime only stays stopped while you hold your breath, and a box truck is sliding on black ice toward a bus shelter. You can't push it. But its wheels are locked, and NHTSA says that without antilock brakes, hard braking can lock the wheels and take away steering. A fictional What If story with a real fact.\n\nNever practice holding your breath in water or alone.",
        "hashtags": ["shorts", "whatif", "story"],
        "keywords": ["what if you could stop time", "freeze time", "what if", "black ice", "locked wheels"],
        "sources": ["https://corpora.tika.apache.org/base/docs/govdocs1/144/144771.html"],
        "disclaimer": "Fictional What If story; the NHTSA fact is real.",
        "long_video_url": "https://youtu.be/<id>",
    },
    "thumb": {"kind": "short_cover", "text": "[gul] 41 SEC|OF AIR",
              "klickfraga": "Hur stoppar man en lastbil man inte kan rubba – med 41 sekunder luft?",
              "hot_i_bild": "Lastbilen fryst i sladd mot glaskuren, uppifrån-ned i vertikalt format.",
              "skiljer_sig": "Första TLI-Shorten: vertikal, lastbilen överst och kuren nederst, rubrik i mitten.",
              "jamfor_ark": "chk/jamfor-tli-2026-11-22-short.png",
              "forsta_scen_matchar": "Scen 1 visar exakt långa videons öppningsbild (lastbil, kur, frusen snö) i vertikalt format."},
    "forbattring": {
        "forra_videon": "Ingen tidigare TLI-Short (Shorts pausade 16/11; TLI startade 16/11).",
        "problem": "TLI:s långa videor får 0 exponeringar; Shorts gav LS/STE nästan all tidig trafik (KANALANALYS_2026-11-22).",
        "andring": "DISTRIBUTIONSORDER 2: första TLI-Shorten – titel med sökförslag nr 1 + #shorts, EN vändning (låsta hjul), länk till långa videon först i beskrivningen, cliffhanger.",
        "forvantat": "≥ 300 visningar i Shorts-flödet på 48 h och klick till den långa videon.",
        "referens": "QM-Shorten 22/11 (samma mall: en vändning + 'Full video on the channel'); egen billån-short 6,7 % CTR.",
        "vi_slår_den_med": "Ett fysiskt problem som syns i varje bild (lastbilen, klockan AIR i hörnet räknar ned) och en verklig fakta som löser det, men slutet bara i långa videon.",
    },
    "notes": {
        "moment": "Nivå 7 ur långa videon: 41 s luft, 9 fot, lastbilen rör sig inte → låsta hjul (NHTSA) → foten av bromsen → ratten → hörnet siktar fortfarande på Hal.",
        "langd": f"≈ {sw} ord ≈ {sdur:.0f} s med am_puck 1,05 (20–45 s).",
        "uppladdning": "Via Studio i ägarens Chrome (Create → Upload), kodad ≤ 3,7 MB (720×1280, ~550 kbit/s, 64 kbit/s ljud) – inte via vidIQ. Render-körningen ersätter <id> med den långa videons id.",
        "kontroll": "monetisering.py GODKÄNT. granskning.py: allt godkänt utom långformens ordgräns (2 000–2 800 ord för TLI) och thumb.jamfor_ark – spärren saknar Shorts-gren, så en 20–45 s Short kan aldrig nå ordgränsen. Spärren ändrades inte (samma som QM-Shorten 22/11).",
    },
}
json.dump(short, open("manus/tli-2026-11-22-short.json", "w"), ensure_ascii=False, indent=1)
print("long words", sum(says), "short words", sw, "short s", round(sdur, 1))
