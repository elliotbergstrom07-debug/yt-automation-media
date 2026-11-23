"""Generator: The Long If 23 nov 2026 – What If Earth Stopped Spinning Because of You?
python3 tli_2026_11_23.py -> parts.json (scener + beats + kontroller)."""
import json

WPS = 2.6
SC = []
HUD = {"day": "30 / 30", "a": ["DAY", "30 HRS"], "b": ["PAY", "$0"]}

def hud(day, length, pay):
    global HUD
    HUD = {"day": f"{day} / 30", "a": ["DAY", length], "b": ["PAY", pay]}

def add(say, v, beat=None, chapter=None, fact=False, **kw):
    v = dict(v); v["hud"] = dict(HUD)
    s = {"say": say, "visual": v}
    if chapter: s["chapter"] = chapter
    s.update(kw)
    s["_beat"] = beat; s["_fact"] = fact
    SC.append(s)

HERO = {"outfit": "window_washer", "harness": True, "hold": "brass_watch"}
ROSA = {"name": "Rosa", "outfit": "crew_boss", "hardhat": True, "hair": "bun"}
PRIYA = {"name": "Priya", "outfit": "hospital_it", "lanyard": True, "hair": "long", "hold": "laptop"}
ABE = {"name": "Abe", "outfit": "cardigan", "age": "old", "hat": "flat_cap", "hold": "chalk"}
VOLE = {"name": "Grant Vole", "outfit": "suit", "hair": "slick", "hold": "phone"}

def S(say, loc, x=0.3, expr="neutral", arms="down", walk=None, shot="wide", friends=None, props=None,
      beat=None, chapter=None, sky=None, strip=None, **kw):
    h = dict(HERO, x=x, expr=expr, arms=arms)
    if walk is not None: h["walk_to"] = walk
    v = {"type": "scene", "location": loc, "hero": h, "shot": shot, "sky": sky or "day"}
    if friends: v["friends"] = friends
    if props: v["props"] = props
    extra = {k: kw.pop(k) for k in list(kw) if k in ("silence", "sfx")}
    v.update(kw)
    fact = False
    if strip:
        v["fact_strip"] = {"head": "THAT'S REAL", "text": strip[0], "source": strip[1]}; fact = True
    add(say, v, beat, chapter, fact=fact, **extra)

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

def C(say, loc, expr, thought, bad=True, beat=None):
    add(say, {"type": "closeup", "location": loc, "expr": expr, "look": -1, "thought": thought, "bad": bad}, beat)

def D(say, day, sub, chapter=None, beat=None):
    add(say, {"type": "daycard", "day": day, "sub": sub}, beat, chapter)

SUN9 = {"type": "sun_stuck", "x": 0.7, "y": 0.28, "clock": "9:00 PM"}
CROWD = {"type": "crowd_phones", "x": 0.5, "n": 40, "expr": "shock"}
PEND = {"type": "pendulum", "x": 0.6, "pegs": True}
SRC_AST = "Astronomy magazine, 'What happens if Earth stops rotating?' (Feb 2026)"
SRC_JPL = "NASA JPL, 'NASA Details Earthquake Effects on the Earth' (2005)"
SRC_LS = "Wikipedia, 'Leap second'"
SRC_AGU = "AGU, 'Ancient shell shows days were half-hour shorter 70 million years ago' (2020)"
SRC_SPC = "Space.com, 'What would happen if Earth stopped spinning?' (2024)"
SRC_SA = "Scientific American, 'If I stop the world, will I melt with you?'"
SRC_APS = "APS News, 'February 3, 1851: Léon Foucault Demonstrates That Earth Rotates'"

# ================= KROK (dag 30, miniatyrens scen) =================
hud(30, "30 HRS", "$0")
S("It's 9 p.m. in Denver, the sun is still up, and today will last 30 hours.",
  "street_16th", 0.4, "worried", "point", 0.48, props=[SUN9, CROWD], sky="stuck_evening", threat="sun_stuck",
  beat=("hot", "solen står kvar kl 21, dagen blir 30 timmar"), chapter="The sun that won't set", sfx="crowd")
S("Thousands of people on 16th Street are filming a sunset that never came.",
  "street_16th", 0.48, "shock", "down", 0.56, props=[SUN9, dict(CROWD, n=60)], sky="stuck_evening", threat="sun_stuck",
  beat=("vändning", "solnedgången som aldrig kom"))
S("This is every level of slowing the planet, and the real science behind each one.",
  "tower_platform", 0.4, "neutral", "down", 0.46, props=[SUN9], sky="stuck_evening",
  beat=("gåta", "löftet: varje nivå + verklig vetenskap"))
S("Your watch is stuck. The day keeps stretching, 4 more minutes every hour.",
  "tower_platform", 0.46, "worried", "hold", 0.52, props=[SUN9, {"type": "watch_big", "x": 0.3, "spin": "backward"}], sky="stuck_evening",
  beat=("hot", "kronan sitter fast, +4 min i timmen (slutlöfte)"))
S("Grant Vole is offering you 2 million dollars to leave the planet exactly like this.",
  "tower_platform", 0.4, "doubt", "hold", 0.46, props=[SUN9, {"type": "phone", "x": 0.42, "screen": "GRANT VOLE"}], sky="stuck_evening",
  beat=("gåta", "Vole: $2 miljoner för att låta det vara"))
R("The ground at the equator moves about 1,037 miles per hour. In New York City, about 794.",
  "1,037 MPH", "Earth's spin at the equator (794 mph in New York City)", SRC_AST)
S("And across town, an 82-year-old man named Abe is on his knees beside a pendulum, drawing chalk lines on the floor.",
  "museum_hall", 0.25, "worried", "down", 0.32, friends=[dict(ABE, x=0.66, kneel=True)], props=[PEND, {"type": "chalk_lines", "x": 0.6}],
  beat=("gåta", "Abe och kritstrecken vid pendeln"))
L("So, what if Earth stopped spinning because of you?", "SLOWER", "the planet's brake is on your wrist", bad=False)

# ================= NIVÅ 1 =================
hud(1, "24 HRS", "$0")
D("Day 1 is a short gray afternoon in November, 31 stories up the side of a glass tower in downtown Denver.", 1, "the watch",
  chapter="Level 1: One millisecond")
L("Level one is a single millisecond, and it's so small that nobody on Earth can feel it.", "LEVEL 1", "ONE MILLISECOND: nobody notices")
S("You wash windows for a living, and you get paid by the pane, so every minute of daylight is money in your pocket.",
  "tower_platform", 0.3, "neutral", "reach", 0.36, props=[{"type": "squeegee", "x": 0.34}],
  beat=("människor", "fönsterputsare, betalt per ruta"))
S("Rosa Delgado runs the crew. Every afternoon she taps her hard hat at the sky and says the same four words. The sun's the boss.",
  "tower_platform", 0.3, "smirk", "down", friends=[dict(ROSA, x=0.68, say="The sun's the boss.")],
  beat=("humor", "Rosas replik (planterad)"))
S("At lunch you find an old brass wristwatch in a planter box on the 31st floor, and nobody in the building has ever seen it.",
  "office_floor", 0.3, "doubt", "reach", 0.4, props=[{"type": "planter", "x": 0.45, "watch": True}],
  beat=("gåta", "mässingsklockan i blomlådan (planterad)"))
S("Out of habit, you wind the crown backward one click. The second hand stutters, and for a moment the whole city seems to sigh.",
  "tower_platform", 0.35, "shock", "hold", 0.4, props=[{"type": "watch_big", "x": 0.3, "spin": "stutter"}], silence=True,
  beat=("vändning", "ett klick bakåt – staden suckar"))
R("A normal day is already a little longer than 24 hours. On average, it runs about two thousandths of a second over.",
  "+0.002 SEC", "an average day, compared with exactly 24 hours", "timeanddate.com, 'Leap seconds' (Dr. Bruce Warrington)")
S("Nothing looks different. Rosa is still yelling about streaks on the 30th floor, and the sun goes down right on schedule.",
  "tower_platform", 0.3, "doubt", "reach", friends=[dict(ROSA, x=0.7, arms="point")], sky="sunset",
  strip=("The extra bit adds up to one whole second in about 1.5 years", "timeanddate.com, 'Leap seconds'"))
R("Earth's speed really does wobble. The shortest day ever recorded was June 29, 2022, at 1.59 milliseconds under 24 hours.",
  "JUNE 29, 2022", "the shortest day on record: 1.59 ms under 24 hours", SRC_LS, beat=("vändning", "rekorddagen 2022"))
R("Big events nudge it too. NASA calculated that the 2004 Sumatra earthquake shortened every day by 2.68 microseconds.",
  "2.68 µs", "shorter days after the 2004 Sumatra earthquake", SRC_JPL)
R("NASA compared it to a spinning skater pulling her arms closer to her body. Move mass toward the middle, and the spin speeds up.",
  "THE SKATER", "pull the mass in, spin faster", SRC_JPL)
S("That night you test it at your kitchen table. One click backward, and an atomic clock app on your phone shows the day stretch a hair.",
  "apartment_kitchen", 0.35, "shock", "hold", 0.4, props=[{"type": "phone", "x": 0.45, "screen": "+0.001 s"}],
  beat=("vändning", "testet vid köksbordet"))
R("Even a dam could do it. NASA worked out that filling China's Three Gorges reservoir would make the day 0.06 microseconds longer.",
  "0.06 µs", "the Three Gorges reservoir, filled (40 cubic km of water)", SRC_JPL)
S("Level one verdict: one click makes the day a millisecond longer, and not one person on the planet notices a thing.",
  "apartment_kitchen", 0.3, "smirk", "down", 0.36, beat=("hot", "dom nivå 1"))

# ================= NIVÅ 2 =================
hud(3, "24 HRS +1 S", "$0")
D("Day 3, and you get a little greedy. You give the crown a thousand clicks backward before your morning coffee.", 3, "the extra second",
  chapter="Level 2: One second")
L("Level two is one extra second, and it turns out that the world's computers really hate surprises.", "LEVEL 2", "ONE SECOND: 86,401")
R("A day with a leap second really has 86,401 seconds in it, instead of the usual 86,400.",
  "86,401", "seconds in a day with a leap second", "timeanddate.com, 'Leap seconds'")
S("Your neighbor Priya Shah runs the night computers at a hospital downtown, and at midnight her phone starts ringing nonstop.",
  "apartment_hall", 0.3, "worried", "down", 0.36, friends=[dict(PRIYA, x=0.68, arms="head", say="Every screen?")],
  beat=("människor", "Priya, sjukhusets nattdatorer"))
S("Every clock in her building now disagrees with every other clock, and the medicine carts are waiting on screens that freeze.",
  "hospital_it", 0.3, "worried", "point", 0.4, friends=[dict(PRIYA, x=0.64, expr="shock")], props=[{"type": "server_racks", "x": 0.8}],
  beat=("hot", "sjukhusets klockor går isär"))
R("The first real leap second was added on June 30, 1972. There have been 27 so far, and the last was December 31, 2016.",
  "27 LEAP SECONDS", "June 30, 1972 to December 31, 2016", "NIST, 'Leap Seconds'; Wikipedia, 'Leap second'")
R("They exist to keep atomic clock time within 0.9 seconds of the time set by the Earth's actual spin.",
  "±0.9 SEC", "how close UTC is kept to Earth's spin (UT1)", "NIST, 'Leap Seconds'")
R("Extra seconds have caused real trouble. After the June 2012 leap second, Qantas, Mozilla and many Linux sites reported problems.",
  "JUNE 30, 2012", "Qantas, Mozilla and Linux sites hit by flawed software", SRC_LS, beat=("vändning", "verkligt: 2012"))
S("By 3 a.m. Priya has it fixed. She tapes a note above her desk that just says 86,401, and draws an angry face next to it.",
  "hospital_it", 0.3, "smirk", "down", friends=[dict(PRIYA, x=0.66)], props=[{"type": "note", "x": 0.5, "text": "86,401 >:("}],
  beat=("gåta", "lappen 86,401 (planterad)"))
S("Over coffee in the hallway you tell her the truth. She thinks you're joking, but she still gives you one rule.",
  "apartment_hall", 0.3, "worried", "hold", friends=[dict(PRIYA, x=0.66, hold="coffee")],
  strip=("In 2015, Netflix, Amazon and Apple's Beats 1 also had interruptions around a leap second", SRC_LS))
S("If you ever touch a clock again, change it one second at a time, slowly, and never all in one big jump.",
  "apartment_hall", 0.32, "doubt", "down", friends=[dict(PRIYA, x=0.64, say="One second at a time.")],
  beat=("gåta", "Priyas regel: en sekund i taget (planterad)"))
R("The world's timekeepers have had enough too. In 2022 they voted to drop leap seconds in or before 2035.",
  "BY 2035", "leap seconds to be dropped (CGPM, 2022)", SRC_LS)
S("Level two verdict: one second is too small to feel, but big enough to make an entire hospital panic for three hours.",
  "hospital_it", 0.3, "worried", "down", 0.36, beat=("hot", "dom nivå 2"))

# ================= NIVÅ 3 =================
hud(6, "24 HRS +1 M", "$0")
D("Day 6, at the science museum, where your crew is washing the big glass dome over the main hall.", 6, "the pendulum",
  chapter="Level 3: Abe")
L("Level three is one whole minute, and a very old man with a box of chalk.", "LEVEL 3", "ONE MINUTE: Abe notices")
S("In the middle of the hall, a heavy brass ball swings on a long wire above a ring of little wooden pegs.",
  "museum_hall", 0.2, "neutral", "down", 0.3, props=[PEND], beat=("gåta", "pendeln och pinnarna"))
S("Abe Lindqvist has volunteered here for 31 years. Every hour, he marks on the floor which peg the pendulum just knocked over.",
  "museum_hall", 0.3, "neutral", "down", friends=[dict(ABE, x=0.62, kneel=True)], props=[PEND, {"type": "chalk_lines", "x": 0.6}],
  beat=("människor", "Abe och kritmärkena (planterad)"))
R("That's a real experiment. In 1851, Léon Foucault hung a 28 kilogram brass bob on a 67 meter wire to show the Earth turning.",
  "1851", "a 28 kg bob on a 67 m wire, Paris", SRC_APS)
R("The swing keeps its direction while the floor turns underneath it. In Paris, that swing turns about 270 degrees in a day.",
  "270°", "how far Foucault's pendulum turns in a day in Paris", SRC_APS)
R("At the North Pole it would turn a full circle in 24 hours. At the equator, it wouldn't turn at all.",
  "360° IN 24 H", "at the North Pole. At the equator: never.", SRC_APS)
S("That morning, hanging from the dome, you click the crown back sixty thousand times, and the day gets one minute longer.",
  "museum_dome", 0.4, "smirk", "hold", 0.46, props=[{"type": "watch_big", "x": 0.3, "spin": "backward"}],
  beat=("vändning", "en minut längre"))
S("Down below, Abe stares at his chalk marks. The pegs are falling late. He checks his pocket watch twice, then looks straight up at you.",
  "museum_hall", 0.6, "shock", "down", friends=[dict(ABE, x=0.4, expr="doubt", look="up")], props=[PEND],
  beat=("gåta", "Abe tittar upp på dig"))
C("He doesn't say a word. He writes LATE on the floor in chalk, underlines it twice, and keeps on watching you.",
  "museum_hall", "worried", "LATE?", beat=("hot", "LATE på golvet"))
S("At lunch he sits next to you on the museum steps and says the floor doesn't lie. Something slowed down, and it was you.",
  "museum_steps", 0.3, "worried", "down", friends=[dict(ABE, x=0.62, say="The floor doesn't lie.")],
  strip=("At the poles, the ground's spinning speed drops to zero", SRC_AST))
S("Then Abe makes you a deal. He'll keep chalk marks every hour, and you'll tell him every time you touch that watch.",
  "museum_steps", 0.32, "doubt", "down", friends=[dict(ABE, x=0.62, hold="chalk")],
  beat=("gåta", "avtalet med Abe (planterat)"))
S("Level three verdict: one minute is the first change a careful person can measure, and Abe is the most careful person you know.",
  "museum_steps", 0.3, "smirk", "down", 0.36, beat=("hot", "dom nivå 3"))

# ================= NIVÅ 4 =================
hud(10, "25 HRS", "$310")
D("Day 10, and you finally do the thing you wanted on day 1. You turn the crown back a full hour.", 10, "the 25-hour day",
  chapter="Level 4: The 25-hour day")
L("Level four is one whole hour, and a day that lasts 25 of them.", "LEVEL 4", "25 HOURS: more daylight")
S("The afternoon stretches out like taffy, and you squeeze in another 40 windows before it gets dark.",
  "tower_platform", 0.2, "smirk", "reach", 0.6, props=[{"type": "squeegee", "x": 0.4}], sky="long_afternoon",
  beat=("vändning", "eftermiddagen töjer sig"))
S("Rosa does the math on a napkin. At three dollars a pane, the crew makes 120 dollars more every day, and she's thrilled.",
  "crew_van", 0.3, "smirk", "down", friends=[dict(ROSA, x=0.66, hold="napkin", say="$120 a day!")])
hud(12, "25 HRS", "$1,440")
R("Earth really did spin faster once. 70 million years ago, a day lasted only about 23 and a half hours.",
  "23.5 HOURS", "the length of a day 70 million years ago", SRC_AGU)
R("Scientists got that from a fossil rudist clam that lived more than nine years and grew a thin layer every single day.",
  "1 LAYER A DAY", "a fossil rudist clam, 9+ years of growth", SRC_AGU)
R("Counting those layers gave 372 days in a year back then, compared with our 365.",
  "372 DAYS", "in a year, 70 million years ago", SRC_AGU, beat=("vändning", "372 dagar om året"))
R("The Moon is the brake. It drifts away from Earth by about 3.82 centimeters, or one and a half inches, every year.",
  "1.5 INCHES", "how far the Moon moves away each year", SRC_AGU)
R("Tidal friction from the Moon alone would lengthen the day by about 2.3 milliseconds every century.",
  "2.3 MS", "per century, from tidal friction alone", SRC_LS)
S("Then the news picks it up. Atomic clocks all over the world are drifting, and the experts on TV don't have a good answer.",
  "apartment_kitchen", 0.3, "worried", "down", props=[{"type": "tv", "x": 0.66, "screen": "WHY ARE CLOCKS DRIFTING?"}],
  beat=("hot", "nyheterna: klockorna driver"))
S("The next morning Grant Vole calls. He owns Vole Freight, all 9,000 trucks, and he saw a museum photo of you on the dome.",
  "vole_office", 0.3, "doubt", "down", friends=[dict(VOLE, x=0.68, say="Nice watch.")],
  beat=("hot", "Grant Vole hittar dig"))
B("His offer is simple. Keep the day at 25 hours forever, and he'll pay you a million dollars a year to do it.",
  "VOLE'S OFFER", ["the day stays 25 hours", "$1,000,000 a year", "more hours to drive"], "deal?")
S("His trucks would get an extra hour every day, and so would his drivers, whether they wanted one or not.",
  "vole_office", 0.32, "worried", "down", friends=[dict(VOLE, x=0.66, expr="smirk")],
  strip=("500 million years ago, each day was about 22 hours long", "xkcd What If?, 'Leap Seconds' (Randall Munroe)"))
C("A million dollars a year. You've never even seen one hundred thousand in one place.", "vole_office", "doubt", "$1,000,000?",
  beat=("gåta", "frestelsen"))
S("Level four verdict: one extra hour feels like a gift, and somebody already wants to buy it from you.",
  "crew_van", 0.3, "worried", "down", 0.36, beat=("hot", "dom nivå 4"))

# ================= NIVÅ 5 =================
hud(18, "27 HRS", "$1,440")
D("Day 18. Vole sends a bonus check anyway, and you click the crown back two more hours, just to see what happens.", 18, "the wind",
  chapter="Level 5: The weather")
L("Level five is a 27-hour day, and the sky starts acting strange.", "LEVEL 5", "27 HOURS: the wind changes")
S("Up on the tower, the wind keeps coming from directions Rosa has never seen, so she ties every line on the platform twice.",
  "tower_platform", 0.3, "worried", "reach", 0.4, friends=[dict(ROSA, x=0.7, arms="reach")], wind=0.7, sky="odd_clouds",
  beat=("hot", "vinden från fel håll"), sfx="wind")
R("Earth's spin shapes the weather. Air and ocean currents are strongly influenced by the planet's rotation.",
  "SPIN = WEATHER", "air and ocean currents follow Earth's rotation", SRC_SPC)
R("The spin is also why big storms twist. They spin counterclockwise in the Northern Hemisphere and clockwise in the Southern.",
  "THE TWIST", "storms: counterclockwise north, clockwise south", "NOAA SciJinks, 'A Powerful Force'")
R("The reason is that different parts of the Earth move at different speeds, which bends the air flowing into a storm.",
  "DIFFERENT SPEEDS", "that deflection is what makes cyclones spin", "NOAA NESDIS, 'What is the Coriolis Effect?'")
L("The slow, gentle change in this story is made up. Everything on a card like this one is real.",
  "MADE UP", "the watch is fiction. the cards are real.", bad=False)
S("Abe calls you to the museum at closing time. His hourly chalk marks have turned into a long, crooked line across the floor.",
  "museum_hall", 0.3, "worried", "down", 0.36, friends=[dict(ABE, x=0.62, arms="point")], props=[PEND, {"type": "chalk_lines", "x": 0.6, "crooked": True}],
  beat=("gåta", "kritlinjen kröker sig"))
S("He points at the pegs and says, every hour you add, my pendulum gets lazier. And after the pendulum, it's the oceans.",
  "museum_hall", 0.32, "shock", "down", friends=[dict(ABE, x=0.62, say="Then the oceans.")], props=[PEND],
  beat=("hot", "Abe: sedan haven"))
R("Earth is fatter at the equator than at the poles. NOAA says that bulge comes from the force of the planet's constant spin.",
  "THE BULGE", "Earth's spin makes it bulge at the equator", "NOAA Ocean Service, 'Is the Earth round?'")
R("If the spin stopped, that would fade, and Astronomy magazine says ocean water would migrate rapidly toward the poles.",
  "OCEANS MOVE", "toward the poles, if Earth stopped spinning", SRC_AST, beat=("vändning", "haven mot polerna"))
S("Priya shows you the hospital logs. Every system she runs now has to be corrected by hand, three times a day.",
  "hospital_it", 0.3, "worried", "down", friends=[dict(PRIYA, x=0.66, hold="laptop", expr="angry")],
  strip=("Earth's magnetic field is linked to flowing liquid metal in the outer core", SRC_SPC))
S("Level five verdict: every hour you add makes the sky, the sea and every clock on Earth work harder to keep up with you.",
  "hospital_it", 0.3, "worried", "down", 0.36, beat=("hot", "dom nivå 5"))

# ================= NIVÅ 6 =================
hud(24, "27 HRS", "$1,440")
D("Day 24, and Vole wants more. He sends a black car to bring you up to his office on the 50th floor.", 24, "the offer",
  chapter="Level 6: Grant Vole")
L("Level six is Grant Vole, a man who thinks a planet is just a very big truck.", "LEVEL 6", "GRANT VOLE: wants it to stop")
S("He wants a 30-hour day, and he has done the math. Every extra hour means more deliveries out of every driver.",
  "vole_office", 0.3, "doubt", "down", friends=[dict(VOLE, x=0.66, arms="point")], props=[{"type": "chart", "x": 0.8}],
  beat=("hot", "Vole vill ha 30 timmar"))
S("Then he leans in and asks what happens if you just stop it, because a day that never ends could be very good for business.",
  "vole_office", 0.32, "shock", "down", friends=[dict(VOLE, x=0.62, expr="smirk", say="Just stop it.")],
  beat=("vändning", "Vole: stoppa den helt"))
R("Scientists have worked that out. If Earth stopped suddenly, the equator would get winds of more than 1,000 miles per hour.",
  "1,000+ MPH", "winds at the equator after a sudden stop", SRC_AST)
R("The air, water and buildings would all keep moving at their old speed, and almost all structures would collapse at once.",
  "EVERYTHING KEEPS MOVING", "almost all structures would collapse at once", SRC_AST)
R("If it slowed down gradually instead, days and nights would keep stretching until each one lasted six months.",
  "6 MONTHS", "of day, then 6 months of night", SRC_SPC, beat=("vändning", "sex månader dag"))
R("Stopping Earth would take a lot of energy. Scientific American puts its spin energy at about 200 octillion joules.",
  "2 × 10²⁹ J", "the energy stored in Earth's spin", SRC_SA)
R("That's roughly a million times the energy of the asteroid that hit Earth 66 million years ago.",
  "×1,000,000", "the dinosaur-killing asteroid's energy", SRC_SA)
S("You say no and walk out. In the elevator, you try to click the crown forward, back toward 24 hours.",
  "elevator", 0.4, "neutral", "hold", 0.46, props=[{"type": "watch_big", "x": 0.3, "spin": "none"}])
S("It won't move. The crown is jammed tight, and the second hand is creeping backward all on its own.",
  "elevator", 0.4, "shock", "hold", props=[{"type": "watch_big", "x": 0.3, "spin": "backward"}], silence=True,
  beat=("hot", "kronan har fastnat – klockan går bakåt själv"))
P("Abe works it out from his chalk marks. The day is getting about a minute longer every hour, and the rate keeps climbing.",
  "THE CHALK MARKS", ["DAY 24: 27 HOURS", "+1 MIN EVERY HOUR", "DAY 30: 30 HOURS", "CROWN: JAMMED"], hot=3,
  beat=("hot", "+1 min i timmen och stigande"))
S("Level six verdict: a sudden stop would wreck the planet, and now the watch is slowing it down without you.",
  "museum_steps", 0.3, "worried", "down", 0.36, friends=[dict(ABE, x=0.66, expr="worried")],
  strip=("There is no natural force that would stop the Earth from spinning", "Live Science (2021)"))

# ================= NIVÅ 7 =================
hud(30, "30 HRS", "$1,440")
D("Day 30, 9 p.m., and the sun still hasn't set over 16th Street.", 30, "the long day", chapter="Level 7: The longest day")
L("Level seven is the moment you saw at the very start of this video, and the watch is still turning backward.",
  "LEVEL 7", "30 HOURS: and growing", beat=("hot", "nivå 7: kroken"))
S("Down on the street, thousands of people are filming the sky. Up on your tower, Rosa holds the platform steady in the wind.",
  "tower_platform", 0.3, "worried", "hold", 0.36, friends=[dict(ROSA, x=0.7)], props=[SUN9], sky="stuck_evening", wind=0.5)
S("Vole calls again. Two million dollars to stop at 30 hours. You hang up, because this was never his day to sell.",
  "tower_platform", 0.34, "neutral", "hold", props=[SUN9, {"type": "phone", "x": 0.4, "screen": "GRANT VOLE"}], sky="stuck_evening",
  beat=("vändning", "du lägger på"))
S("You could smash the watch, but you have no idea what one sudden jump would do to a planet that has been slowing for a month.",
  "tower_platform", 0.36, "worried", "hold", props=[SUN9, {"type": "watch_big", "x": 0.3, "spin": "backward"}], sky="stuck_evening",
  beat=("hot", "ett plötsligt hopp?"),
  strip=("A sudden stop: winds of more than 1,000 mph at the equator", SRC_AST))
S("Then you remember the note above Priya's desk. 86,401. Change it one second at a time, and never in one big jump.",
  "hospital_it", 0.3, "smirk", "down", props=[{"type": "note", "x": 0.5, "text": "86,401 >:("}],
  beat=("callback", "Priyas lapp och regel"))
S("You call her, and she drives to the museum with a laptop and a tiny screwdriver from the hospital's repair kit.",
  "museum_hall", 0.2, "worried", "down", 0.36, friends=[dict(PRIYA, x=0.8, walk_to=0.6, hold="screwdriver")], props=[PEND])
S("Abe is already there, on his knees beside the pendulum, with a fresh box of chalk and his old pocket watch.",
  "museum_hall", 0.3, "neutral", "down", friends=[dict(ABE, x=0.62, kneel=True)], props=[PEND, {"type": "chalk_lines", "x": 0.6, "crooked": True}],
  beat=("callback", "Abe och kritan"),
  strip=("In 1851, Foucault's pendulum showed the Earth turning, in Paris", SRC_APS))
S("Priya opens the back of the watch. The crown isn't broken at all. A single grain of grit is wedged against one gear.",
  "museum_hall", 0.4, "shock", "down", friends=[dict(PRIYA, x=0.56, hold="screwdriver")], props=[{"type": "watch_open", "x": 0.5, "grit": True}],
  beat=("lösning", "ett sandkorn i kugghjulet"))
S("She can pull it out, but then the gear will snap forward to 24 hours all at once, unless someone holds it back by hand.",
  "museum_hall", 0.42, "worried", "down", friends=[dict(PRIYA, x=0.6, expr="worried")], props=[{"type": "watch_open", "x": 0.5, "grit": True}],
  beat=("hot", "kugghjulet vill slå tillbaka i ett hopp"))
B("So that's the choice. Let the gear snap back in one jump, or hold it and let it creep forward one click at a time, all night.",
  "THE CHOICE", ["A: one jump back to 24 hours", "B: one click at a time, all night"], "Priya's rule?",
  beat=("gåta", "valet: ett hopp eller ett klick i taget"))
S("You hold the crown with your thumbnail. Priya pulls the grit free. The gear shoves hard against your thumb, and you don't let go.",
  "museum_hall", 0.42, "worried", "hold", friends=[dict(PRIYA, x=0.6, hold="tweezers")], props=[{"type": "watch_open", "x": 0.5}], silence=True,
  beat=("vändning", "du håller emot"))
S("One click. Abe calls out the chalk mark. One more click, and he calls it again. You keep that rhythm for nine hours.",
  "museum_hall", 0.4, "neutral", "hold", friends=[dict(ABE, x=0.66, kneel=True, say="Mark.")], props=[PEND],
  beat=("callback", "en sekund i taget"))
hud(30, "26 HRS", "$1,440")
R("Earth's spin has been speeding up lately. In 2020 the planet had the 28 shortest days measured since 1960.",
  "28 SHORT DAYS", "in 2020, the most since 1960", SRC_LS)
R("That speed-up is why Astronomy magazine says a leap second might even have to be subtracted, possibly in 2029.",
  "2029?", "a negative leap second has never happened", SRC_AST, beat=("vändning", "negativ skottsekund"))
S("Around 4 a.m. the pegs start falling on time again. Abe stops writing LATE. He writes OK, and then he writes it again.",
  "museum_hall", 0.3, "smirk", "down", friends=[dict(ABE, x=0.62, kneel=True)], props=[PEND, {"type": "chalk_lines", "x": 0.6, "text": "OK"}],
  beat=("callback", "LATE blir OK"))
hud(30, "24 HRS", "$1,440")
S("At sunrise Priya checks the hospital clocks. 86,400 seconds. A normal day, give or take a couple of milliseconds.",
  "hospital_it", 0.3, "smirk", "down", friends=[dict(PRIYA, x=0.66, say="86,400.")],
  beat=("vändning", "en vanlig dag igen"),
  strip=("An average day runs about 0.002 seconds over 24 hours", "timeanddate.com, 'Leap seconds'"))
S("The sun comes up over the Rocky Mountains right where it should, and down on 16th Street, people finally go to bed.",
  "street_16th", 0.4, "smirk", "wave", 0.46, sky="sunrise", props=[{"type": "crowd_phones", "x": 0.5, "n": 10, "expr": "sleepy"}])

# ================= EFTERÅT =================
S("Vole sends one last message. He says you just threw away two million dollars. You send him a photo of the sunrise.",
  "tower_platform", 0.3, "smirk", "hold", props=[{"type": "phone", "x": 0.4, "screen": "SUNRISE.JPG"}], sky="sunrise",
  beat=("callback", "solnedgångsbilden till Vole"), chapter="The choice")
S("Rosa taps her hard hat at the sky, exactly the way she did on day 1, and says it again. The sun's the boss.",
  "tower_platform", 0.3, "smirk", "down", friends=[dict(ROSA, x=0.68, say="The sun's the boss.")], sky="day",
  beat=("callback", "Rosas replik"))
S("You give the watch to Abe. He locks it in the glass case next to the pendulum, with a little card that says do not wind.",
  "museum_hall", 0.3, "smirk", "down", friends=[dict(ABE, x=0.62)], props=[PEND, {"type": "glass_case", "x": 0.8, "card": "DO NOT WIND"}],
  beat=("callback", "DO NOT WIND"))
L("Rosa, Priya, Abe, Grant Vole and the watch are made up. The spinning Earth, the clocks and the clam are all real.",
  "MADE UP", "the people and the watch are fiction. the science is real.", bad=False)
R("And one more real one. Spinning in an office chair really does change Earth's rotation, just not enough to matter.",
  "YOUR CHAIR", "temporarily alters Earth's spin, not enough to matter", "xkcd What If?, 'Leap Seconds' (Randall Munroe)")
B("Your turn. On day 30, would you let the gear snap back in one jump, or hold it all night, one click at a time? A or B.",
  "WHAT WOULD YOU DO?", ["A: one jump", "B: one click at a time"], "comment A or B", beat=("gåta", "frågan till tittaren"))
L("Level 8 is coming next. What if you were the last man on earth, and every clock still kept running?", "LEVEL 8", "???",
  beat=("gåta", "Level 8: ???"))
S("Until then, watch a sunset tonight. Every one of them is the Earth turning at about a thousand miles an hour, right on time.",
  "street_16th", 0.4, "smirk", "wave", 0.46, sky="sunset",
  strip=("Earth spins at around 1,000 mph at the equator", SRC_SPC), beat=("callback", "solnedgången"))


# ---------------- faktaremsor + närbilder (efter index) ----------------
LS_ = "Live Science, 'What would happen if Earth stopped spinning?' (2021)"
STRIPS = {
 3: ("Earth makes one full turn every 23 hours, 56 minutes and 4.09 seconds", LS_),
 6: ("Léon Foucault first showed Earth turning with a pendulum on February 3, 1851, in Paris", SRC_APS),
 10: ("NASA: the 2004 Sumatra earthquake shifted the mean North Pole about 1 inch", SRC_JPL),
 12: ("Earth's spin energy was gained as the planet formed 4.6 billion years ago", SRC_SA),
 21: ("A filled Three Gorges reservoir would also shift the pole about 0.8 inch", SRC_JPL),
 34: ("UTC currently runs 37 seconds behind atomic time (TAI)", "NIST, 'Leap Seconds'"),
 37: ("In 1851 Foucault also hung a 28 kg ball inside the dome of the Panthéon in Paris", "Britannica, 'Foucault pendulum'"),
 43: ("At the equator the ground moves about 1,000 to 1,100 mph, depending on the source", "Space.com (2024); Live Science (2021)"),
 47: ("In 100 years, each day is predicted to be about 0.004 seconds longer on average", "timeanddate.com, 'Leap seconds'"),
 50: ("The rudist clam lived for over nine years in a shallow tropical seabed", SRC_AGU),
 57: ("The length of a day has been increasing by about 1.4 to 1.7 ms per century", SRC_LS),
 60: ("The day has gotten longer because of tidal forces from the Moon", "xkcd What If?, 'Leap Seconds' (Randall Munroe)"),
 62: ("Half a billion years ago, each day was about 22 hours long", "xkcd What If?, 'Leap Seconds' (Randall Munroe)"),
 65: ("Hurricanes and typhoons are low-pressure systems", "NOAA NESDIS, 'What is the Coriolis Effect?'"),
 70: ("If Earth stopped, the poles would likely be the least affected places", SRC_SPC),
 75: ("Earth's magnetic field protects us from harmful radiation from space", SRC_SPC),
 78: ("A sudden stop would likely trigger tsunamis and earthquakes", SRC_SPC),
 85: ("A Falcon 9 rocket can generate about a trillion joules of energy", SRC_SA),
 91: ("Earth will never actually stop rotating", SRC_AST),
 98: ("The 28th CGPM, set for 2026, is expected to review the new leap-second limit", SRC_LS),
 100: ("Russia asked to push the end of leap seconds back to 2040", SRC_LS),
 106: ("NASA: the 2004 quake made Earth about one part in 10 billion less flattened", SRC_JPL),
 108: ("It takes about a decade for Earth's core to sync up with its crust", "xkcd What If?, 'Leap Seconds' (Randall Munroe)"),
}
CLOSE = {32: "ONE SECOND AT A TIME", 86: "JAMMED", 98: "ONE JUMP?"}
for i, s in enumerate(SC):
    v = s["visual"]
    if i in STRIPS:
        assert v["type"] == "scene", (i, v["type"])
        v["fact_strip"] = {"head": "THAT'S REAL", "text": STRIPS[i][0], "source": STRIPS[i][1]}; s["_fact"] = True
    if i in CLOSE:
        assert v["type"] == "scene", (i, v["type"])
        nv = {"type": "closeup", "location": v["location"], "expr": v["hero"]["expr"], "look": -1, "thought": CLOSE[i], "bad": True, "hud": v["hud"]}
        if "fact_strip" in v: nv["fact_strip"] = v["fact_strip"]
        s["visual"] = nv

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
says = [len(s["say"].split()) for s in SC]
gaps = [b - a for a, b in zip([0.0] + facts, facts + [TOTAL])]
stats = {"scenes": len(SC), "words": sum(says), "min": round(TOTAL / 60, 2), "beats": len(beats),
         "avg": round(sum(says) / len(SC), 1), "lt6": sum(1 for n in says if n < 6), "facts": len(facts),
         "maxgap": round(max(gaps), 1), "gaps30": [round(x) for x, g in zip([0.0] + facts, gaps) if g > 30]}
json.dump({"SC": SC, "beats": beats, "total": TOTAL, "stats": stats}, open("parts.json", "w"), ensure_ascii=False, indent=1)
from collections import Counter
print(stats)
print(Counter(s["visual"]["type"] for s in SC))
