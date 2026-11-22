"""Generator: The Long If 22 nov 2026 – What If You Could Stop Time While Holding Your Breath?
python3 tli_2026_11_22.py  ->  parts.json (scenes + beats) som tli_2026_11_22_build.py gör manus av."""
import json

WPS = 2.6
SC = []
HUD = {"day": "30 / 30", "a": ["AIR", "0:41"], "b": ["PAY", "$4,100"]}

def hud(day, air, pay):
    global HUD
    HUD = {"day": f"{day} / 30", "a": ["AIR", air], "b": ["PAY", pay]}

def add(say, v, beat=None, chapter=None, fact=False, **kw):
    v = dict(v); v["hud"] = dict(HUD)
    s = {"say": say, "visual": v}
    if chapter: s["chapter"] = chapter
    s.update(kw)
    s["_beat"] = beat; s["_fact"] = fact
    SC.append(s)

HERO = {"outfit": "courier", "helmet": True, "bag": "courier"}
MARISOL = {"name": "Marisol", "outfit": "dispatch", "hair": "bun", "headset": True, "hold": "stopwatch"}
DEX = {"name": "Dex", "outfit": "orange_courier", "helmet": True, "bike": "orange"}
HAL = {"name": "Hal", "outfit": "ymca_jacket", "age": "old", "hat": "cap", "hold": "mints"}

def S(say, loc, x=0.3, expr="neutral", arms="down", walk=None, shot="wide", friends=None, props=None, beat=None, chapter=None, frozen=False, **kw):
    h = dict(HERO, x=x, expr=expr, arms=arms)
    if walk is not None: h["walk_to"] = walk
    v = {"type": "scene", "location": loc, "hero": h, "shot": shot, "sky": "winter_day"}
    if friends: v["friends"] = friends
    if props: v["props"] = props
    if frozen: v["frozen"] = True
    extra = {k: kw.pop(k) for k in list(kw) if k in ("silence", "sfx")}
    v.update(kw)
    add(say, v, beat, chapter, **extra)

def R(say, big, text, source, beat=None, chapter=None):
    add(say, {"type": "real", "head": "THAT'S REAL", "big": big, "text": text, "source": source}, beat, chapter, fact=True)

def L(say, big, text, bad=True, beat=None, chapter=None, fact=False):
    add(say, {"type": "label", "big": big, "text": text, "bad": bad}, beat, chapter, fact=fact)

def P(say, title, labels, hot=None, beat=None):
    items = []
    for i, lab in enumerate(labels):
        col, row = divmod(i, 4)
        it = {"box": [0.08 + 0.46 * col, 0.2 + 0.18 * row, 0.38, 0.14], "label": lab}
        if hot is not None and i == hot: it["hot"] = True
        items.append(it)
    add(say, {"type": "plan", "title": title, "items": items}, beat)

def B(say, title, lines, result, beat=None):
    add(say, {"type": "board", "title": title, "lines": lines, "result": result}, beat)

def C(say, loc, expr, thought, bad=True, beat=None, frozen=False):
    v = {"type": "closeup", "location": loc, "expr": expr, "look": -1, "thought": thought, "bad": bad}
    if frozen: v["frozen"] = True
    add(say, v, beat)

def D(say, day, sub, chapter=None, beat=None):
    add(say, {"type": "daycard", "day": day, "sub": sub}, beat, chapter)

TRUCK = {"type": "box_truck", "x": 0.18, "skid": True, "wheels": "locked"}
SHELTER = {"type": "bus_shelter", "x": 0.72, "people": 5, "route": "8 HALSTED"}
SNOW = {"type": "snow_frozen"}

# ================= KROK (dag 30, miniatyrens scen) =================
S("A box truck slides on black ice toward a bus shelter with five people inside.",
  "halsted_street", 0.42, "shock", "point", 0.48, props=[dict(TRUCK, drive_to=0.3), SHELTER], threat="truck_skid",
  beat=("hot", "box truck glider mot busskuren, 5 inne"), chapter="The truck on Halsted", sfx="horn")
S("You breathe in and hold it. Every snowflake on Halsted Street stops in midair.",
  "halsted_street", 0.48, "neutral", "down", 0.54, props=[TRUCK, SHELTER, SNOW], frozen=True, threat="truck_skid",
  beat=("vändning", "du håller andan – allt fryser"), silence=True)
S("This is every level of stopping time with one breath, and the science behind it.",
  "halsted_street", 0.54, "smirk", "down", 0.62, props=[TRUCK, SHELTER, SNOW], frozen=True,
  beat=("gåta", "löftet: varje nivå + verklig vetenskap"))
S("The truck is frozen 9 feet from the glass. Your lungs give you about 41 seconds.",
  "halsted_street", 0.3, "worried", "point", 0.36, props=[TRUCK, SHELTER, SNOW, {"type": "measure", "text": "9 FT"}], frozen=True,
  beat=("hot", "9 fot, 41 sekunder luft (slutlöfte)"))
R("That isn't much. Most people manage 30 seconds to a few minutes.",
  "30 SECONDS", "to a few minutes, for most people", "Smithsonian Magazine, 'Ask Smithsonian: What's the longest you can hold your breath?'")
S("Behind the glass, an old man named Hal is still smiling at you, because he taught you this.",
  "halsted_street", 0.4, "worried", "down", 0.5, friends=[dict(HAL, x=0.74, expr="smirk")], props=[SHELTER, SNOW], frozen=True,
  beat=("gåta", "Hal ler bakom glaset – han lärde dig"))
S("On day 1 you couldn't hold it for 40 seconds. Today, five people need you to go longer.",
  "halsted_street", 0.5, "worried", "down", 0.58, props=[TRUCK, SHELTER, SNOW], frozen=True,
  beat=("hot", "5 personer behöver mer än du klarar"))
L("So, what if you could stop time, but only for as long as you hold your breath?",
  "HOLD = STOP", "breathe out, and the world starts again", bad=False)

# ================= NIVÅ 1 =================
hud(1, "0:38", "$0")
D("Day 1 is a Monday in December, at a bike courier depot in Chicago.", 1, "the hiccups", chapter="Level 1: The hiccups")
L("Level one is the hiccups, which is how you find out about any of this.", "LEVEL 1", "THE HICCUPS: 38 seconds of nothing")
S("You've had the hiccups since breakfast, loud ones, and dispatch keeps laughing at you over the radio.",
  "courier_depot", 0.3, "doubt", "head", 0.36, friends=[{"name": "Couriers", "x": 0.75, "outfit": "courier", "expr": "smirk"}],
  beat=("humor", "hicka, alla skrattar"))
S("Marisol Vance runs dispatch. She times every delivery with a silver stopwatch and says every second is a dollar.",
  "courier_depot", 0.3, "neutral", "down", friends=[dict(MARISOL, x=0.68, say="Every second is a dollar")],
  beat=("människor", "Marisol och stoppuret (planterat)"))
R("Here's what a hiccup is. A spasm in your diaphragm makes your vocal cords snap shut, and that makes the sound.",
  "HIC", "diaphragm spasm, vocal cords snap shut", "Mayo Clinic, 'Hiccups: Symptoms and causes'")
S("So you do what everyone's grandmother tells you to do. You take a big breath, and you hold it.",
  "courier_depot", 0.34, "neutral", "head", 0.4, friends=[dict(MARISOL, x=0.7)])
S("The radio goes quiet mid-word. Marisol's stopwatch hangs at 14 seconds, and the hiccups are gone.",
  "courier_depot", 0.4, "shock", "down", 0.46, friends=[dict(MARISOL, x=0.7, frozen=True)], frozen=True,
  beat=("vändning", "tiden stannar – stoppuret på 14"), silence=True)
S("Nobody in the depot is moving. A coffee is pouring out of a cup and has stopped halfway to the floor.",
  "courier_depot", 0.46, "shock", "reach", 0.58, props=[{"type": "coffee_frozen", "x": 0.62}], frozen=True,
  beat=("hot", "kaffet hänger i luften"))
R("For most people, hiccups only last a few minutes. Mayo Clinic says to see a doctor if they last more than 48 hours.",
  "48 HOURS", "hiccups longer than that: see a doctor", "Mayo Clinic, 'Hiccups: Symptoms and causes'")
S("Your chest starts to burn at about 38 seconds. You gasp, and the coffee hits the floor all at once.",
  "courier_depot", 0.5, "worried", "head", 0.52, props=[{"type": "coffee_splash", "x": 0.62}], friends=[dict(MARISOL, x=0.75, expr="shock")],
  beat=("vändning", "38 sekunder – du andas, kaffet faller"), sfx="splash")
R("That burn has a real cause. High carbon dioxide, not low oxygen, is what makes a long breath-hold hurt.",
  "CO2", "high carbon dioxide drives the burn, not low oxygen", "Smithsonian Magazine, quoting Mayo Clinic's Dr. Clayton Cowl")
C("Marisol stares at the puddle, then at her stopwatch, then at you, as if the numbers just skipped.",
  "courier_depot", "doubt", "0:14?", beat=("gåta", "Marisol märker hoppet i sekunderna"))
S("Level one verdict: you can stop the whole world for 38 seconds, and the only price is a burning chest.",
  "courier_depot", 0.3, "smirk", "down", 0.36, beat=("hot", "dom nivå 1: 38 s"))

# ================= NIVÅ 2 =================
hud(3, "0:38", "$0")
D("Day 3, at home, with the bathroom door locked and a phone stopwatch running.", 3, "the rules", chapter="Level 2: The rules")
L("Level two is the rules, because a power with no rules is going to get somebody hurt.", "LEVEL 2", "THE RULES: 3 of them")
S("You start the stopwatch on your phone and hold your breath. The stopwatch freezes along with everything else.",
  "bathroom", 0.35, "doubt", "hold", 0.4, props=[{"type": "phone", "x": 0.42, "screen": "0:00.00"}], frozen=True,
  beat=("vändning", "telefonens stoppur fryser också"))
S("So you count in your head instead, one Mississippi at a time, like a kid playing hide and seek.",
  "bathroom", 0.4, "neutral", "head", props=[{"type": "count_bubble", "text": "1 MISSISSIPPI"}], frozen=True,
  beat=("humor", "Mississippi-räkningen (planterad)"))
P("Rule one: breathe in, and time stops. Rule two: breathe out, and it starts again exactly where it was.",
  "THE RULES", ["1. BREATHE IN: TIME STOPS", "2. BREATHE OUT: IT STARTS", "3. ???"], hot=2)
R("Real physics is much harsher. If time really stopped, physicists point out, all light and sound would stop too.",
  "NO LIGHT, NO SOUND", "if time stopped, both would stop with it", "Discovery, 'What Would Happen If You Stopped Time?'",
  beat=("vändning", "verklig fysik: ljus och ljud stannar"))
R("Even the air would freeze in place, with every molecule stuck where it is. You couldn't take a single step.",
  "FROZEN AIR", "every molecule held in place, so you couldn't move", "Discovery, quoting physicist Sean Carroll")
L("In our story, light and air still work for you. That part is made up. Everything on a card like this is real.",
  "MADE UP", "the power is fiction. the cards are real.", bad=False)
S("What does feel real is the silence. No traffic, no wind, no radiator, only your own heartbeat.",
  "apartment_window", 0.4, "neutral", "down", 0.46, props=[{"type": "window_city", "frozen": True}], frozen=True, silence=True)
P("Rule three you learn by accident. You can move things while time is stopped, but only what you can carry.",
  "RULE 3", ["YOU CAN MOVE THINGS", "ONLY WHAT YOU CAN CARRY", "A CAR: NO", "A BIKE: YES"], hot=0,
  beat=("vändning", "regel 3: du kan flytta det du orkar bära"))
S("Your limit is still 38 seconds, and on days when you're tired it drops to about 30.",
  "bathroom", 0.4, "worried", "head", 0.42, beat=("hot", "trött = 30 s"))
S("Level two verdict: the power is real, it has rules, and the only clock still running is the one in your lungs.",
  "apartment_window", 0.35, "smirk", "down", 0.42, beat=("hot", "dom nivå 2"))

# ================= NIVÅ 3 =================
hud(6, "0:38", "$310")
D("Day 6, rush hour at Halsted and Madison, and you're racing another courier.", 6, "the red light", chapter="Level 3: Dex")
L("Level three is Dex Moreau, the fastest courier in the depot, and he wants every one of your routes.", "LEVEL 3", "DEX MOREAU: never brakes")
S("Dex rides an orange bike, never stops at red lights, and has called you Hiccup since Monday.",
  "intersection", 0.2, "doubt", "down", 0.32, friends=[dict(DEX, x=0.5, walk_to=0.7, say="Later, Hiccup!")],
  beat=("humor", "Dex kallar dig Hiccup"))
S("He blows straight through a red light. A sedan is braking hard from the left, and it isn't going to stop in time.",
  "intersection", 0.25, "shock", "point", 0.3, friends=[dict(DEX, x=0.55)], props=[{"type": "sedan", "x": 0.15, "drive_to": 0.4, "skid": True}],
  beat=("hot", "Dex kör mot rött, sedanen glider"), sfx="horn")
S("You breathe in and hold it. The sedan stops two feet from Dex, its tires locked on the wet road.",
  "intersection", 0.3, "worried", "down", 0.42, friends=[dict(DEX, x=0.55, frozen=True)], props=[{"type": "sedan", "x": 0.4, "skid": True, "wheels": "locked"}],
  frozen=True, beat=("vändning", "du fryser tiden – 2 fot kvar"), silence=True)
S("Then you notice something strange. The driver has the steering wheel turned hard right, and the car is sliding dead straight.",
  "intersection", 0.42, "doubt", "point", props=[{"type": "sedan", "x": 0.4, "skid": True, "wheels": "locked", "steer": "right"}], frozen=True,
  beat=("gåta", "ratten vriden – bilen glider rakt (planterat)"))
R("That's real. Without antilock brakes, NHTSA says a hard stop can lock the wheels and take away your steering.",
  "LOCKED = NO STEERING", "hard braking without ABS can lock the wheels", "NHTSA, 'Antilock Brake Systems (ABS)'")
S("You can't move a car, but you can move a bike. You drag Dex and his bike two feet to the right.",
  "intersection", 0.5, "neutral", "reach", 0.58, friends=[dict(DEX, x=0.6, walk_to=0.72, frozen=True)], frozen=True,
  beat=("lösning", "du drar Dex två fot åt sidan"))
S("At 33 Mississippi you breathe. The sedan slides past, and Dex has no idea why he's still alive.",
  "intersection", 0.3, "worried", "down", friends=[dict(DEX, x=0.72, expr="shock")], props=[{"type": "sedan", "x": 0.45, "drive_to": 0.9}],
  beat=("vändning", "sedanen glider förbi"))
R("Crashes like this aren't rare. In 2024, 1,075 bicyclists were killed in crashes with motor vehicles in the U.S.",
  "1,075", "bicyclists killed in U.S. crashes, 2024", "IIHS, 'Fatality Facts 2024: Bicyclists'")
R("And 81 percent of them were killed in urban areas, on city streets a lot like this one.",
  "81% URBAN", "of U.S. bicyclist deaths in 2024", "IIHS, 'Fatality Facts 2024: Bicyclists'")
S("Dex looks at you, pale as the snow, and for the first time he calls you by your real name.",
  "intersection", 0.35, "neutral", "down", friends=[dict(DEX, x=0.62, expr="shock", say="...thanks, man.")],
  beat=("människor", "Dex säger ditt namn"))
S("Level three verdict: one breath can save a life, and locked wheels go wherever they want to go.",
  "intersection", 0.3, "smirk", "down", 0.38, beat=("hot", "dom nivå 3 (låsta hjul – planterat)"))

# ================= NIVÅ 4 =================
hud(11, "0:38", "$310")
D("Day 11, and Marisol calls you into the dispatch office with a printout in her hand.", 11, "the printout", chapter="Level 4: The stopwatch")
L("Level four is Marisol and her stopwatch, because numbers don't lie, and your numbers are impossible.", "LEVEL 4", "MARISOL VANCE: 1 stopwatch, 0 excuses")
S("Your GPS log shows you three blocks away from a drop-off, and then at the drop-off, with zero seconds in between.",
  "dispatch_office", 0.3, "worried", "down", 0.34, friends=[dict(MARISOL, x=0.68, hold="printout")], beat=("hot", "GPS: 3 kvarter på 0 sekunder"))
P("Your phone logged 4:12:07 at Jackson, then 4:12:07 again at Wacker. Same second, three blocks apart.",
  "GPS LOG, DAY 10", ["4:12:07  JACKSON", "4:12:07  WACKER", "DISTANCE: 3 BLOCKS", "TIME: 0 SEC"], hot=3)
R("GPS is fussy about time anyway. Because of relativity, satellite clocks tick about 38 microseconds a day fast.",
  "38 MICROSECONDS", "per day, GPS clocks vs ground clocks", "Ohio State University, Prof. Richard Pogge, 'GPS and Relativity'")
R("If nobody corrected for that, GPS positions would drift by about 10 kilometers, roughly 6 miles, every day.",
  "10 KM A DAY", "the error if relativity were ignored", "Ohio State University, Prof. Richard Pogge, 'GPS and Relativity'",
  beat=("vändning", "utan korrigering: 10 km fel per dag"))
R("Time really does run at different speeds. In 1971, atomic clocks flown east around the world lost 59 nanoseconds.",
  "59 NANOSECONDS", "lost by atomic clocks flown east, 1971", "Hafele & Keating, Science (1972), via HyperPhysics, Georgia State University")
R("Flown west, they gained 273 nanoseconds. Your problem is that you just gained three whole blocks.",
  "+273 NS", "gained flying west", "Hafele & Keating, Science (1972), via HyperPhysics")
S("Marisol doesn't ask how you did it. She slides a contract across the desk and asks how much of it you can do.",
  "dispatch_office", 0.3, "doubt", "down", friends=[dict(MARISOL, x=0.66, expr="smirk", hold="contract")],
  beat=("vändning", "Marisol frågar inte hur – hon vill köpa det"))
B("Her offer is the rush route. Every package under 15 minutes pays 40 dollars, and the big ones pay 500.",
  "THE RUSH ROUTE", ["under 15 minutes: $40", "big clients: $500", "rule: never late"], "how many can you do?")
S("So you start freezing time 30 times a day, and by Friday your pay for the week is 1,840 dollars.",
  "halsted_street", 0.2, "smirk", "down", 0.6, props=[{"type": "bike", "x": 0.2}], beat=("hot", "30 frysningar/dag, $1 840"))
hud(13, "0:38", "$1,840")
C("You also start getting headaches, and twice this week the edges of the room have gone gray before you breathed.",
  "apartment_window", "worried", "GRAY EDGES", beat=("hot", "huvudvärk, grått i kanterna"))
R("That's a real warning sign. An Ohio State doctor says that if you hold your breath long enough, you could pass out.",
  "YOU COULD PASS OUT", "from holding your breath too long", "Ohio State Wexner Medical Center, Dr. Jonathan Parsons (2024)")
R("He also says one minute is probably the limit, and that you might reach 90 seconds without getting into trouble.",
  "1 MINUTE", "probably the limit; maybe 90 seconds", "Ohio State Wexner Medical Center, Dr. Jonathan Parsons (2024)")
S("Level four verdict: the power pays very well, but every freeze takes a little something back from you.",
  "dispatch_office", 0.3, "worried", "down", 0.36, beat=("hot", "dom nivå 4: kraften tar något tillbaka"))

# ================= NIVÅ 5 =================
hud(15, "0:38", "$1,840")
D("Day 15, at the Route 8 bus stop on Halsted, at 4:40 in the afternoon.", 15, "the bench", chapter="Level 5: Hal")
L("Level five is Hal Benning, who is 74 and the only person who ever notices you breathing.", "LEVEL 5", "HAL BENNING: 74, the 4:40 bus")
S("Hal waits for the same bus every day at 4:40. He sees you gasp after a freeze and offers you a mint.",
  "bus_shelter", 0.3, "worried", "head", 0.38, friends=[dict(HAL, x=0.68, say="Mint?")], props=[SHELTER],
  beat=("människor", "Hal och mintpastillerna (planterat 4:40)"))
S("He coached swimming at a YMCA for 40 years, and he says you breathe like a kid who just learned to dive.",
  "bus_shelter", 0.32, "doubt", "down", friends=[dict(HAL, x=0.66, expr="smirk")], props=[SHELTER])
S("Then he says something that stops you cold. Breathe, kid. Never hold it past the edge, and never alone.",
  "bus_shelter", 0.32, "shock", "down", friends=[dict(HAL, x=0.66, say="Breathe, kid.")], props=[SHELTER],
  beat=("gåta", "'Breathe, kid. Never past the edge alone.' (planterat)"))
R("He isn't being dramatic. The CDC found 16 swimmers in New York State hurt in underwater breath-holding incidents, and 4 died.",
  "16 SWIMMERS", "dangerous breath-holding, New York State, 1988–2011: 4 died", "CDC, MMWR Vol. 64, No. 19 (2015)",
  beat=("hot", "CDC: 16 simmare, 4 döda"))
R("Breathing fast before a breath-hold lowers your carbon dioxide, so the urge to breathe comes late, and you can black out first.",
  "HYPERVENTILATION", "lowers CO2, delays the urge, risks blackout", "CDC, MMWR Vol. 64, No. 19 (2015)")
L("So, for real: never practice holding your breath in water, and never hyperventilate before you try.",
  "NEVER IN WATER", "and never breathe fast first", fact=True)
S("Hal teaches you on dry land, on the bench, with slow breaths and loose shoulders, and you stop before it hurts.",
  "bus_shelter", 0.32, "neutral", "down", friends=[dict(HAL, x=0.62, arms="point")], props=[SHELTER])
R("He also shows you a trick. Cold water on your face can start the diving reflex, which slows the heart 10 percent or more.",
  "DIVING REFLEX", "cold water on the face: heart rate down 10% or more", "Scientific American, 'Breath-holding: the diving reflex'",
  beat=("vändning", "dykreflexen"))
R("In some marine mammals, that same reflex slows the heart by roughly 90 percent.",
  "90%", "heart-rate drop in some diving mammals", "Scientific American, 'Breath-holding: the diving reflex'")
S("In one week your limit goes from 38 seconds to 1 minute and 25. You still stop the second it starts to burn.",
  "apartment_window", 0.35, "smirk", "down", 0.4, props=[{"type": "sink", "x": 0.6}], beat=("vändning", "gränsen 0:38 → 1:25"))
hud(21, "1:25", "$4,100")
R("Trained free divers go much further, holding for 4 to 8 minutes or more without breathing oxygen first.",
  "4 TO 8 MINUTES", "trained free divers, no oxygen beforehand", "Smithsonian Magazine, 'What's the longest you can hold your breath?'")
R("In 2009, Stéphane Mifsud held his breath for 11 minutes and 35 seconds, with no pure oxygen beforehand.",
  "11:35", "static breath-hold, 2009, no oxygen", "Scientific American, 'Breath-holding: the diving reflex'")
R("The Guinness record is 24 minutes and 37 seconds, set in 2021 in Croatia by a 56-year-old free diver, Budimir Šobat.",
  "24:37", "Guinness record breath-hold, 2021", "Guinness World Records (May 2021)")
R("But he breathed pure oxygen before the attempt, which the record's rules allow for up to 30 minutes.",
  "PURE OXYGEN", "allowed for 30 minutes before the attempt", "Guinness World Records (May 2021)",
  beat=("vändning", "rekordet med rent syre"))
S("Hal hears all of this and says he's 74, his personal record is a nap, and his bus is late again.",
  "bus_shelter", 0.3, "smirk", "down", friends=[dict(HAL, x=0.66, expr="smirk", say="My record is a nap.")], props=[SHELTER],
  beat=("humor", "Hals rekord är en tupplur"))
S("Level five verdict: the power grows with training, and the man who trains you sits in that glass box every day at 4:40.",
  "bus_shelter", 0.3, "neutral", "down", 0.36, friends=[dict(HAL, x=0.7)], props=[SHELTER], beat=("gåta", "dom nivå 5: glaslådan kl 4:40"))

# ================= NIVÅ 6 =================
hud(22, "1:25", "$4,100")
D("Day 22, on the icy stairs up to a train platform, with a package in each hand.", 22, "the fall", chapter="Level 6: The fall")
L("Level six is the fall, and it teaches you the one thing your power can't do.", "LEVEL 6", "THE FALL: 0 seconds of air")
S("Your foot hits a patch of ice on the top step, and you go over backward down the stairs.",
  "train_stairs", 0.5, "shock", "up", 0.3, props=[{"type": "packages", "x": 0.5, "flying": True}], beat=("hot", "du halkar baklänges"), sfx="boom")
S("You try to freeze it, but you just shouted, and your lungs are empty. Time doesn't stop at all.",
  "train_stairs", 0.4, "shock", "up", 0.3, beat=("vändning", "tomma lungor – tiden stannar inte"))
S("And yet the fall feels slow. You see every step, every rivet in the railing, and a pigeon taking off.",
  "train_stairs", 0.35, "shock", "up", 0.25, props=[{"type": "pigeon", "x": 0.7}])
S("You land on a pile of shoveled snow at the bottom, sore but whole, and lie there for a full minute.",
  "train_stairs", 0.2, "worried", "down", props=[{"type": "snowpile", "x": 0.2}])
R("That slow feeling has been tested. In 2007, researchers dropped volunteers 150 feet into a safety net.",
  "150 FEET", "free fall into a net, 2007 study", "National Geographic, on Stetson, Fiesta & Eagleman, PLoS ONE (2007)",
  beat=("vändning", "forskarna som släppte folk 150 fot"))
R("People guessed that their own fall had lasted 36 percent longer than the falls they watched other people take.",
  "+36%", "how much longer their own fall seemed", "National Geographic, on Stetson et al., PLoS ONE (2007)")
R("But a flickering number on their wrists was just as hard to read as it was on the ground. Time didn't slow down.",
  "TIME DIDN'T SLOW", "they read the numbers no better than on the ground", "National Geographic, on Stetson et al., PLoS ONE (2007)")
R("The researchers think frightening moments leave denser memories, so the moment only seems longer afterward.",
  "MEMORY", "fear makes the moment seem longer later", "National Geographic, on Stetson et al., PLoS ONE (2007)")
S("Level six verdict: no breath, no power. From now on, before every corner, you keep a full breath ready.",
  "train_stairs", 0.3, "neutral", "down", 0.38, beat=("hot", "dom nivå 6: ingen luft, ingen kraft"))
S("That night Marisol calls. Day 30 has a 500 dollar rush package for Wacker Drive, due at exactly 4:45.",
  "apartment_window", 0.35, "doubt", "hold", props=[{"type": "phone", "x": 0.4, "screen": "MARISOL"}],
  beat=("gåta", "$500-paketet kl 4:45 – Hal väntar 4:40"))

# ================= NIVÅ 7 =================
hud(30, "1:25", "$4,100")
D("Day 30, 4:38 in the afternoon, 31 degrees with freezing drizzle, and Halsted is glazed with black ice.", 30, "the ice", chapter="Level 7: The ice")
L("Level seven is the ice, and it's the moment you saw at the very start of this video.", "LEVEL 7", "THE ICE: 5 people, 9 feet")
S("You're 6 blocks from Wacker with the 500 dollar package, and you sprint the bike the whole way.",
  "halsted_street", 0.1, "worried", "down", 0.4, props=[{"type": "bike", "x": 0.1, "drive_to": 0.4}], beat=("hot", "sprint 6 kvarter"))
R("Winter driving guides put it plainly. It's harder to control or stop a vehicle on a slick surface, so leave more distance.",
  "SLOW DOWN", "slick roads: harder to control, harder to stop", "NHTSA, 'Winter Driving Tips'")
S("At Halsted, a box truck brakes for the light, and its back end swings out toward the bus stop.",
  "halsted_street", 0.4, "shock", "point", 0.45, props=[dict(TRUCK, x=0.1, drive_to=0.3), SHELTER], threat="truck_skid",
  beat=("hot", "lastbilen sladdar mot busskuren"), sfx="horn")
S("Hal is in the shelter with four other people: a nurse, a man with groceries, a student, and a mail carrier.",
  "halsted_street", 0.45, "shock", "down", friends=[dict(HAL, x=0.74)], props=[SHELTER])
S("You breathe in and hold it. But you just sprinted 6 blocks, and the burn starts almost right away.",
  "halsted_street", 0.42, "worried", "head", 0.5, props=[TRUCK, SHELTER, SNOW], frozen=True,
  beat=("vändning", "fryst – men sprinten tog luften"), silence=True)
hud(30, "0:41", "$4,100")
P("You count what you've got. About 41 seconds of air, a truck 9 feet from the glass, and five people inside.",
  "4:41 P.M.", ["AIR: ~41 SEC", "TRUCK: 9 FT", "PEOPLE: 5", "PACKAGE DUE: 4:45"], hot=1, beat=("hot", "41 s, 9 fot, 5 personer"))
S("You can't push a truck that weighs as much as a small house. You try anyway, and nothing moves at all.",
  "halsted_street", 0.25, "worried", "reach", 0.28, props=[TRUCK, SNOW], frozen=True, beat=("hot", "lastbilen rör sig inte"))
S("Then you remember Dex and the sedan. The truck's wheels aren't turning, because the driver is standing on the brake.",
  "truck_cab", 0.35, "doubt", "point", props=[{"type": "pedal", "x": 0.5, "pressed": True}], frozen=True,
  beat=("callback", "Dex och sedanen – låsta hjul"))
R("NHTSA's advice: with antilock brakes, keep firm pressure and steer. Without them, you may need to pump the brakes as wheels lock.",
  "PUMP OR STEER", "no ABS: wheels can lock. with ABS: press firmly and steer", "NHTSA, 'Antilock Brake Systems' and 'Winter Driving Tips'")
S("Locked wheels can't steer. So you climb into the cab and pull the driver's boots off the brake pedal.",
  "truck_cab", 0.4, "neutral", "reach", 0.46, friends=[{"name": "Driver", "x": 0.65, "outfit": "work", "frozen": True}],
  beat=("lösning", "du lyfter förarens fot från bromsen"))
S("Then you turn the steering wheel a quarter turn toward the snowbank, while you count 33 Mississippi, 34.",
  "truck_cab", 0.42, "worried", "reach", props=[{"type": "steering_wheel", "turn": 0.25}], frozen=True,
  beat=("callback", "Mississippi-räkningen"))
S("You breathe out. The world jumps forward one second, and the truck slides one more foot toward the glass.",
  "halsted_street", 0.3, "shock", "down", props=[dict(TRUCK, x=0.24, drive_to=0.3), SHELTER, {"type": "measure", "text": "8 FT"}],
  beat=("hot", "ett andetag = en fot närmare"), sfx="horn")
S("You breathe in again. Now the wheels are rolling, and the truck has started to turn, but not fast enough.",
  "halsted_street", 0.35, "worried", "point", 0.4, props=[dict(TRUCK, x=0.3, steer="left"), SHELTER, SNOW], frozen=True,
  beat=("vändning", "hjulen rullar, men för sakta"), silence=True)
R("In breath-hold blackouts, the CDC says the cause is the oxygen in your arteries dropping too low.",
  "BLACKOUT", "caused by arterial oxygen dropping too low", "CDC, MMWR Vol. 64, No. 19 (2015)")
S("Its back corner will still clip the shelter, right where Hal is sitting with his paper bag of mints.",
  "halsted_street", 0.5, "shock", "point", 0.56, friends=[dict(HAL, x=0.76, frozen=True)], props=[dict(TRUCK, x=0.3), SHELTER, SNOW], frozen=True,
  beat=("hot", "hörnet träffar Hals plats"))
S("Hal is a big man, and dragging him across the ice will take longer than your lungs can last.",
  "bus_shelter", 0.5, "worried", "reach", 0.6, friends=[dict(HAL, x=0.68, frozen=True)], props=[SHELTER, SNOW], frozen=True)
B("So you have a choice. Hold past the edge alone and maybe black out, or breathe and give the truck another second.",
  "THE CHOICE", ["A: hold past the edge, alone", "B: breathe, lose 1 second"], "Hal's rule?", beat=("gåta", "valet: förbi gränsen eller andas"))
C("You hear Hal's voice in your head, and it's annoyingly calm. Breathe, kid. Never past the edge alone.",
  "bus_shelter", "neutral", "BREATHE, KID", bad=False, beat=("callback", "Hals regel"), frozen=True)
S("So you breathe after every 20 Mississippi. Each breath, the truck slides a few inches. Each freeze, you drag Hal a little farther.",
  "bus_shelter", 0.55, "worried", "reach", 0.42, friends=[dict(HAL, x=0.62, walk_to=0.48, frozen=True)], props=[SHELTER, SNOW], frozen=True,
  beat=("lösning", "20 Mississippi i taget"))
R("Doctors compare the last stage of a very long breath-hold to a kind of carbon dioxide narcosis, a foggy, heavy feeling.",
  "CO2 NARCOSIS", "how a very long breath-hold can feel", "Smithsonian Magazine, quoting Mayo Clinic's Dr. Clayton Cowl")
S("The ice helps here. Hal slides like a sofa on a polished floor, out of the shelter and into the snow.",
  "halsted_street", 0.45, "smirk", "reach", 0.3, friends=[dict(HAL, x=0.55, walk_to=0.35, frozen=True)], props=[SHELTER, SNOW], frozen=True,
  beat=("humor", "Hal glider som en soffa"))
S("Then the nurse, then the man with the groceries, then the student, then the mail carrier, one breath at a time.",
  "halsted_street", 0.6, "worried", "reach", 0.4, props=[SHELTER, SNOW, {"type": "people_moved", "n": 5}], frozen=True,
  beat=("hot", "fem personer, ett andetag i taget"))
S("On the last breath you let go. The truck rolls into the snowbank, and the shelter glass cracks with nobody inside.",
  "halsted_street", 0.3, "shock", "down", props=[dict(TRUCK, x=0.55, drive_to=0.62, steer="left"), dict(SHELTER, people=0, cracked=True), {"type": "snowbank", "x": 0.65}],
  beat=("vändning", "lastbilen i snövallen, kuren tom"), sfx="crash")
S("Hal sits up in the snow, looks at the empty shelter, then at you, and says it one more time. Breathe, kid.",
  "halsted_street", 0.3, "smirk", "down", friends=[dict(HAL, x=0.58, say="Breathe, kid.")], props=[dict(SHELTER, people=0, cracked=True)],
  beat=("callback", "'Breathe, kid.'"), silence=True)

# ================= VALET / EFTERÅT =================
S("You reach Wacker Drive at 4:49 with the package. Marisol's silver stopwatch says you're exactly 4 minutes late.",
  "dispatch_office", 0.3, "neutral", "hold", 0.36, friends=[dict(MARISOL, x=0.68, say="4 minutes.")],
  beat=("hot", "4 minuter sen"), chapter="The choice")
S("She says the rush route needs someone who never misses a deadline. You slide the contract back across her desk.",
  "dispatch_office", 0.32, "smirk", "reach", friends=[dict(MARISOL, x=0.66, expr="shock", hold="contract")],
  beat=("vändning", "du lämnar tillbaka kontraktet"))
S("Dex takes the rush route. On his first day he stops at a red light, and he waves at you with his whole arm.",
  "intersection", 0.3, "smirk", "wave", friends=[dict(DEX, x=0.6, arms="wave")], beat=("callback", "Dex stannar vid rött"))
R("The 2024 total of bicyclist deaths was the third-highest number IIHS has ever recorded.",
  "3RD HIGHEST", "U.S. bicyclist deaths, 2024", "IIHS, 'Fatality Facts 2024: Bicyclists'")
S("And every day at 4:40, Hal saves you the seat at the end of the bench, the one farthest from the road.",
  "bus_shelter", 0.3, "smirk", "down", friends=[dict(HAL, x=0.62, say="Mint?")], props=[dict(SHELTER, cracked=False)],
  beat=("callback", "Hal sparar platsen längst från vägen"))
L("Hal, Marisol, Dex and the frozen truck are made up. The breathing, the brakes and the clocks are all real.",
  "MADE UP", "the power and the people are fiction. the facts are real.", bad=False)
L("And one more time, because it's real: never practice breath-holding in water, and never on your own.",
  "NEVER IN WATER", "never alone", fact=True)
B("Your turn. On day 30, would you hold past your limit to save Hal faster, or breathe every 20 seconds like he said? A or B.",
  "WHAT WOULD YOU DO?", ["A: hold past the edge", "B: breathe every 20"], "comment A or B", beat=("gåta", "frågan till tittaren"))
L("Level 8 is coming next. What if the Earth stopped spinning, for just one second?", "LEVEL 8", "???", beat=("gåta", "Level 8: ???"))
R("And tonight, look at a clock with a second hand. That first tick can seem to hang, by up to half a second.",
  "STOPPED CLOCK", "the first second you see can last up to 0.5 s longer", "Wikipedia, 'Chronostasis' (Yarrow et al.)")
S("That's chronostasis, the closest any of us will get to stopping time, and you don't even have to hold your breath.",
  "halsted_street", 0.35, "smirk", "wave", 0.42, props=[{"type": "street_clock", "x": 0.7}], beat=("callback", "klockan – kraften utan andning"))

# ---------------- faktaremsor (nedre tredjedel, THAT'S REAL + SOURCE) och strykningar ----------------
CUT = set()
STRIPS = {}
CLOSE = set()
exec(open("tli_strips.py").read()) if __import__("os").path.exists("tli_strips.py") else None
SC2 = []
for i, s in enumerate(SC):
    if i in CUT: continue
    if i in STRIPS:
        s["visual"]["fact_strip"] = {"head": "THAT'S REAL", "text": STRIPS[i][0], "source": STRIPS[i][1]}
        s["_fact"] = True
    if i in CLOSE and s["visual"]["type"] == "scene":
        v = s["visual"]
        s["visual"] = {"type": "closeup", "location": v["location"], "expr": v["hero"]["expr"], "look": -1, "thought": CLOSE_T.get(i, ""), "bad": True, "hud": v["hud"]}
        if v.get("frozen"): s["visual"]["frozen"] = True
        if "fact_strip" in v: s["visual"]["fact_strip"] = v["fact_strip"]
    SC2.append(s)
SC[:] = SC2

# ---------------- beats + tider + kontroller ----------------
def dur(s):
    return max(len(s["say"].split()) / WPS + 0.45, 2.0)

t = 0.0; beats = []; facts = []
for s in SC:
    b = s.pop("_beat"); f = s.pop("_fact")
    if b:
        beats.append({"t": f"{int(t // 60)}:{int(t % 60):02d}", "typ": b[0], "text": b[1]})
    if f: facts.append(t)
    t += dur(s)
TOTAL = t
json.dump({"SC": SC, "beats": beats, "total": TOTAL}, open("parts.json", "w"), ensure_ascii=False, indent=1)
says = [len(s["say"].split()) for s in SC]
from collections import Counter
print("scenes", len(SC), "words", sum(says), "min", round(TOTAL / 60, 2), "beats", len(beats))
print("avg words/say", round(sum(says) / len(SC), 1), "say<6:", sum(1 for n in says if n < 6))
gaps = [b - a for a, b in zip([0.0] + facts, facts + [TOTAL])]
print("faktaskyltar", len(facts), "största lucka", round(max(gaps), 1), "s vid", [round(x) for x, g in zip([0.0] + facts, gaps) if g > 30])
print(Counter(s["visual"]["type"] for s in SC))
