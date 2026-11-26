"""Generator: manus/dac-2026-11-26.json – Your Life at Every Level of a Rental Car Crash in Mexico."""
import json, os

WPS = 2.6
H = lambda x, expr="worried", arms="down", walk=None, hold=None: {k: v for k, v in dict(x=x, expr=expr, arms=arms, walk_to=walk, holding=hold).items() if v is not None}

def F(name, x, outfit, say=None, walk=None, **kw):
    d = dict(x=x, outfit=outfit, name=name)
    if walk is not None: d["walk_to"] = walk
    if say: d["say"] = say
    d.update(kw); return d

HEC = dict(hair="short", cap=True)          # Héctor, taxichauffören
RIOS = dict(cap=True)                       # tránsito-polisen
ORT = dict(hair="long", glasses=True)       # försvararen Ortega
DANA = dict(hair="bun")                     # konsulatstjänstemannen

def scene(loc, hero, friends=None, props=None, note=None):
    v = {"type": "scene", "location": loc, "shot": "wide", "hero": hero}
    if props: v["props"] = props
    if friends: v["friends"] = friends
    if note: v["note_card"] = {"text": note}
    return v

def real(head, big, text, src): return {"type": "real", "head": head, "big": big, "text": text, "source": src}
def label(big, text, src=None, bad=True): return {"type": "label", "big": big, "text": text, "source": src, "bad": bad}
def day(n, sub): return {"type": "daycard", "label": f"LEVEL {n}", "sub": sub}
def close(loc, expr, thought): return {"type": "closeup", "location": loc, "expr": expr, "look": -1, "thought": thought, "bad": True}

S = []   # (say, visual, beat_typ, beat_text, extra)
def add(say, vis, typ, txt, **extra): S.append((say, vis, typ, txt, extra))

MX = "MEXICO RULE"; QR = "QUINTANA ROO RULE"; US = "U.S. RULE"; INTL = "TREATY RULE"
SD = "U.S. State Dept, Mexico Travel Advisory (2026)"

# ---------------- LEVEL 1 ----------------
add("12 minutes out of the Cancún airport, your rental car and a taxi bump.",
    scene("roundabout", H(0.24, "shock", walk=0.36), [F("Héctor", 0.7, "white", walk=0.62, **HEC)], [{"type": "rental_car", "x": 0.34, "dent": True}, {"type": "taxi", "x": 0.6, "dashcam": True}]),
    "hot", "hyrbilen och taxin stöter ihop i rondellen", chapter="Level 1: The roundabout", sfx="crash")
add("At 4 miles an hour, the taxi driver still climbs out holding his neck.",
    scene("roundabout", H(0.3, "worried", walk=0.4), [F("Héctor", 0.66, "white", walk=0.58, **HEC)], [{"type": "taxi", "x": 0.56}]),
    "hot", "chauffören håller sig om nacken")
add("3 minutes later, a police truck pulls up behind you with its lights on.",
    scene("roundabout", H(0.3, "shock", walk=0.36), [F("Officer Ríos", 0.9, "navy", walk=0.76, **RIOS)], [{"type": "police_truck", "x": 0.86}, {"type": "taxi", "x": 0.56}]),
    "hot", "polisen kommer", sfx="siren")
add("Your life at every level of a rental car crash in Mexico starts here.",
    scene("roundabout", H(0.32, "worried", walk=0.28), [F("Officer Ríos", 0.78, "navy", walk=0.66, **RIOS)], [{"type": "taxi", "x": 0.58, "dashcam": True}]),
    "hot", "löftet: varje nivå från rondellen")
add("By the end, you'll know what the taxi's dash camera saw.",
    scene("roundabout", H(0.3, "doubt", walk=0.4), [F("Héctor", 0.7, "white", walk=0.64, **HEC)], [{"type": "taxi", "x": 0.56, "dashcam": True}]),
    "gåta", "gåtan: vad såg taxins kamera?")
add("On its windshield, a red light blinks once every 2 seconds, and nobody mentions it.",
    scene("roundabout", H(0.3, "doubt", walk=0.42), [F("Héctor", 0.7, "white", **HEC)], [{"type": "taxi", "x": 0.56, "dashcam": True, "blink": True}]),
    "gåta", "den röda lampan blinkar")
add("Officer Ríos asks for your license, your rental papers and your Mexican insurance.",
    scene("roundabout", H(0.3, "worried", "hold", 0.38, "phone"), [F("Officer Ríos", 0.7, "navy", walk=0.6, say="Seguro?", **RIOS)]),
    "hot", "polisen vill se mexikansk försäkring")
add("Your license is fine. The State Department says a U.S. driver's license is valid in Mexico, so that part takes 10 seconds.",
    scene("roundabout", H(0.3, "neutral", "hold", 0.34, "phone"), [F("Officer Ríos", 0.66, "navy", walk=0.6, **RIOS)], note="U.S. DRIVER'S LICENSES ARE VALID IN MEXICO (STATE DEPT)"),
    "vändning", "körkortet duger")
add("Then you hold up your phone with your car insurance card from home, and Ríos shakes his head slowly without even reading it.",
    scene("roundabout", H(0.3, "shock", "hold", 0.36, "phone"), [F("Officer Ríos", 0.66, "navy", say="Mexicano.", **RIOS)], [{"type": "phone", "x": 0.46, "text": "AUTO INSURANCE|POLICY 4471|USA"}]),
    "hot", "det amerikanska försäkringskortet räknas inte")
add("The State Department's page on Mexico is blunt about this. Mexican car insurance is required for all vehicles.",
    real("U.S. GOVERNMENT", "REQUIRED", "Mexican car insurance, for all vehicles", SD), "vändning", "regeln: mexikansk försäkring krävs")
add("Level one. The roundabout.", day("ONE", "the roundabout"), "hot", "nivåkort 1")
add("The same page has the line that matters most right now. Uninsured drivers involved in car accidents, major or minor, may be subject to arrest.",
    real("U.S. GOVERNMENT", "MAY BE ARRESTED", "uninsured drivers in accidents, major or minor", SD), "hot", "oförsäkrade kan gripas")
add("The same page says something worse for you. Arrests can happen regardless of who is at fault.",
    label("ANY FAULT", "arrests can happen regardless of who is at fault", SD), "vändning", "oavsett vem som är skyldig", silence=True)
add("Héctor, the taxi driver, tells Ríos in fast Spanish that you hit him from behind. You catch the word atrás, behind, and not much else.",
    scene("roundabout", H(0.28, "doubt"), [F("Héctor", 0.56, "white", say="¡Por atrás!", **HEC), F("Officer Ríos", 0.78, "navy", **RIOS)], [{"type": "taxi", "x": 0.44}]),
    "hot", "Héctor: du körde på mig bakifrån")
add("You were sure the taxi rolled backward into you while you waited, but your foot was on the brake and you didn't see his wheels.",
    close("roundabout", "doubt", "BACKWARD?"), "gåta", "rullade taxin bakåt?")
add("Ríos says something to his partner and gestures at the truck. In broken English, he tells you to relax, because it's only paperwork.",
    scene("roundabout", H(0.3, "worried", walk=0.5), [F("Officer Ríos", 0.7, "navy", walk=0.62, say="Only paperwork.", **RIOS)], [{"type": "police_truck", "x": 0.82}]),
    "hot", "'only paperwork' – och lastbilen väntar")

# ---------------- LEVEL 2 ----------------
add("Level two. The yellow copy.", day("TWO", "the yellow copy"), "hot", "nivåkort 2", chapter="Level 2: The yellow copy")
add("Ríos asks for the rental contract. It's in the glove box, a yellow carbon copy folded in 4 with your initials in 6 places.",
    scene("car_interior", H(0.3, "worried", "hold", hold="letter"), props=[{"type": "contract", "x": 0.62, "title": "RENTAL AGREEMENT", "tag": "YELLOW COPY"}]),
    "hot", "hyreskontraktet i handskfacket", sfx="paper")
add("Next to a line called third party liability, your initials sit beside the word declined. 19 dollars a day you decided not to pay.",
    scene("car_interior", H(0.3, "shock", "hold", hold="letter"), props=[{"type": "contract", "x": 0.62, "title": "THIRD PARTY LIABILITY", "tag": "DECLINED"}], note="THIRD PARTY LIABILITY: DECLINED"),
    "vändning", "du tackade nej till ansvarsförsäkringen")
add("At the counter that morning, the agent asked twice if you were sure. You said your card back home had you covered.",
    scene("rental_counter", H(0.3, "smirk", "hold", 0.4, "phone"), [F("Counter agent", 0.74, "green", say="You're sure?", hair="short")], [{"type": "key_tag", "x": 0.56, "text": "#27"}]),
    "gåta", "minnet: disken, 'are you sure?'")
add("Mexican federal law requires every vehicle on federal roads and highways to carry insurance that covers damage to other people and their property.",
    real(MX, "THIRD PARTIES", "insurance required on federal roads and bridges", "Ley de Caminos, Puentes y Autotransporte Federal, Art. 63 Bis"), "vändning", "lag: ansvarsförsäkring krävs")
add("That same article puts the duty to buy that insurance on the vehicle's owner. Here, that means the rental company, which is why it was on the form.",
    label("THE OWNER", "must buy the third-party insurance", "Ley de Caminos, Art. 63 Bis", bad=False), "vändning", "ägaren ska köpa den")
add("What the form actually did was move the risk from the rental company onto you, and in a crash, that risk has a face, and it's Héctor's.",
    scene("roundabout", H(0.3, "sad"), [F("Héctor", 0.66, "white", **HEC)], [{"type": "taxi", "x": 0.54}], note="LEY DE CAMINOS, ART. 63 BIS: THIRD-PARTY INSURANCE ON FEDERAL ROADS"),
    "hot", "risken flyttade till dig")
add("Ríos takes the yellow copy, reads the word declined, and puts it in his shirt pocket. Then he opens the back door of the truck.",
    scene("roundabout", H(0.3, "shock", walk=0.6), [F("Officer Ríos", 0.74, "navy", walk=0.66, **RIOS)], [{"type": "police_truck", "x": 0.82, "door_open": True}]),
    "hot", "polisen öppnar bakdörren", silence=True, sfx="click")

# ---------------- LEVEL 3 ----------------
add("Level three. The truck.", day("THREE", "the truck"), "hot", "nivåkort 3", chapter="Level 3: The truck")
add("Nobody reads you rights in English in the truck. You sit on a metal bench, and your rental car keys are still in your hand.",
    scene("police_truck_back", H(0.4, "sad", "hold", hold="keys"), [F("Partner", 0.74, "navy", cap=True)]),
    "hot", "på metallbänken med nycklarna")
add("Mexico's Constitution lets anyone detain a person caught committing a crime, or right after, as long as they're handed over without delay.",
    real(MX, "WITHOUT DELAY", "a person caught in the act must be handed over at once", "Constitución (CPEUM), Art. 16"), "vändning", "flagrans: utan dröjsmål")
add("The same paragraph says the next stop is the Ministerio Público, the public prosecutor, and that the detention has to be recorded right away.",
    label("RECORDED", "the detention must be logged immediately", "CPEUM, Art. 16", bad=False), "vändning", "gripandet ska registreras")
add("A crash with an injury claim counts here. If someone is hurt, the question isn't only money anymore, it's a possible crime called lesiones.",
    scene("police_truck_back", H(0.4, "worried", "hold", hold="keys"), note="CPEUM ART. 16: HANDED OVER WITHOUT DELAY, DETENTION RECORDED"),
    "hot", "skada = möjligt brott, lesiones")
add("Through the small back window you watch the roundabout get smaller, and the taxi's red light blink on and off one last time.",
    scene("police_truck_back", H(0.42, "sad", "hold", hold="keys"), props=[{"type": "taxi", "x": 0.8, "small": True, "dashcam": True, "blink": True}]),
    "gåta", "den röda lampan blinkar en sista gång")
add("The truck stops outside a low concrete building with the word Fiscalía on the wall. That's the prosecutor's office, not a jail.",
    scene("fiscalia_outside", H(0.3, "worried", walk=0.5), [F("Partner", 0.18, "navy", walk=0.4, cap=True)], [{"type": "sign", "x": 0.6, "text": "FISCALÍA GENERAL"}]),
    "hot", "Fiscalía – åklagarens kontor")
add("Inside, an officer writes your name and the time, 2:14 in the afternoon, in a large book and on a computer screen.",
    scene("fiscalia_hall", H(0.3, "worried", walk=0.4), [F("Desk officer", 0.74, "navy", glasses=True)], [{"type": "laptop", "x": 0.6, "text": "DETENIDO|2:14 PM"}]),
    "hot", "registrerad 14:14")
add("They take your phone, your belt and the rental keys, and they put them in a clear bag with a number written on it in marker.",
    scene("fiscalia_hall", H(0.3, "sad", walk=0.36), [F("Desk officer", 0.74, "navy", glasses=True)], [{"type": "bag", "x": 0.6, "tag": "#27"}]),
    "hot", "telefonen i en påse")

# ---------------- LEVEL 4 ----------------
add("Level four. The clock.", day("FOUR", "the clock"), "hot", "nivåkort 4", chapter="Level 4: The clock")
add("They put you in a room with a bench and a wall clock that runs 4 minutes fast. It's the only thing in here you can read.",
    scene("holding_room", H(0.34, "sad", walk=0.44), props=[{"type": "wall_clock", "x": 0.7, "time": "2:31"}]),
    "hot", "väntrummet med klockan som går 4 min fel")
add("Mexico's Constitution sets a hard limit. The prosecutor may hold you for no more than 48 hours before releasing you or bringing you to a judge.",
    real(MX, "48 HOURS", "the most the prosecutor may hold you", "CPEUM, Art. 16"), "hot", "48 timmar")
add("If a judge takes over, the Constitution gives the judge 72 hours to decide whether to bind you over for trial, unless you ask for more time.",
    real(MX, "72 HOURS", "for a judge's order to keep you in the case", "CPEUM, Art. 19"), "hot", "sedan 72 timmar hos domaren")
add("And if the jail doesn't receive that order in time, it has to warn the judge, and 3 hours later it has to let you go.",
    label("3 MORE HOURS", "then the jail must release you without the order", "CPEUM, Art. 19", bad=False), "vändning", "3 timmar sedan frisläppning")
add("An investigator comes in with a form in Spanish. You say you don't speak Spanish, and he sighs and leaves to find someone who does.",
    scene("holding_room", H(0.3, "doubt"), [F("Investigator", 0.72, "suit", walk=0.62, hair="short")], [{"type": "summons", "x": 0.56, "title": "DECLARACIÓN"}], note="CPEUM ART. 16: 48 HOURS MAX WITH THE PROSECUTOR"),
    "hot", "ett formulär på spanska")
add("He has to. Mexico's national criminal code says that when someone doesn't speak or understand Spanish, a translator or interpreter must be provided.",
    real(MX, "INTERPRETER", "must be provided if you don't speak Spanish", "Código Nacional de Procedimientos Penales (CNPP), Art. 45"), "vändning", "tolk krävs")
add("Another article in the same code lists it as your right, and adds that the interpreter is free, which matters when you have 900 dollars.",
    label("FREE", "a translator or interpreter at no cost to you", "CNPP, Art. 113, fr. XII", bad=False), "vändning", "gratis")
add("Two more rights sit in the Constitution itself. You're presumed innocent until a judge rules otherwise, and you may make a statement or stay silent.",
    real(MX, "SILENCE", "presumed innocent; free to speak or stay silent", "CPEUM, Art. 20(B), fr. I and II"), "vändning", "oskuldspresumtion och tystnad")
add("An hour later the interpreter, a woman named Lupita, sits down next to you. You decide you won't sign anything until you've talked to a lawyer.",
    scene("holding_room", H(0.3, "neutral"), [F("Lupita", 0.6, "teal", walk=0.54, say="I'll translate.", hair="bun"), F("Investigator", 0.82, "suit", hair="short")], note="CNPP ART. 45: AN INTERPRETER MUST BE PROVIDED"),
    "människor", "tolken Lupita")
add("The clock on the wall says 4:02. By the real time it's 3:58, and you have used up almost 2 of your 48 hours.",
    close("holding_room", "worried", "46 HOURS"), "hot", "46 timmar kvar")

# ---------------- LEVEL 5 ----------------
add("Level five. The embassy.", day("FIVE", "the embassy"), "hot", "nivåkort 5", chapter="Level 5: The embassy")
add("Through Lupita, you ask the investigator to call the U.S. consulate. He nods like he's heard it a thousand times, and writes it down.",
    scene("holding_room", H(0.3, "doubt", "point"), [F("Lupita", 0.56, "teal", hair="bun"), F("Investigator", 0.8, "suit", say="Consulado.", hair="short")]),
    "vändning", "du ber om konsulatet")
add("The State Department's advice is exactly that. If you are arrested or detained, ask the police or prison officials to inform the U.S. Embassy or nearest consulate immediately.",
    real("U.S. GOVERNMENT", "ASK", "police must be asked to tell the embassy or consulate", SD), "vändning", "be polisen informera ambassaden")
add("Mexican law backs you up. When a detainee is a foreigner, the prosecutor must tell them without delay about their right to consular help.",
    real(MX, "CONSULAR HELP", "a foreign detainee must be told without delay", "CNPP, Art. 151"), "vändning", "konsulär hjälp utan dröjsmål")
add("The prosecutor also has to notify the embassy or consulate itself and keep proof that it did, unless you and your lawyer ask them not to.",
    label("PROOF", "the notice to the consulate must be recorded", "CNPP, Art. 151", bad=False), "vändning", "beviset på underrättelsen")
add("Behind both rules is a 1963 treaty. If you ask, the local authorities must inform your consulate without delay that you've been detained.",
    real(INTL, "WITHOUT DELAY", "your consulate is told if you ask", "Vienna Convention on Consular Relations (1963), Art. 36(1)(b)"), "vändning", "Wienkonventionen")
add("According to the United Nations treaty records, 183 countries are party to that convention, so this rule follows you almost anywhere you travel.",
    label("183", "countries party to the Vienna Convention on Consular Relations", "UN Treaty Collection, ch. III-6", bad=False), "vändning", "183 länder")
add("Night comes. They give you a bottle of water and a sandwich in plastic wrap, and you lie on the bench watching the clock run 4 minutes fast.",
    scene("holding_room", H(0.4, "sad", walk=0.5), props=[{"type": "wall_clock", "x": 0.72, "time": "11:44"}], note="VIENNA CONVENTION ART. 36: CONSULATE TOLD WITHOUT DELAY IF YOU ASK"),
    "hot", "natten på bänken")
add("You think about the taxi's camera again. If it shows what you think it shows, why hasn't anyone asked for it?",
    close("holding_room", "doubt", "THE CAMERA"), "gåta", "varför har ingen frågat efter kameran?")

# ---------------- LEVEL 6 ----------------
add("Level six. The consul.", day("SIX", "the consul"), "hot", "nivåkort 6", chapter="Level 6: The consul")
add("At 9 the next morning, a woman from the U.S. consulate named Dana comes to the visiting room with a folder and a clipboard.",
    scene("visit_room", H(0.3, "neutral", walk=0.42), [F("Dana", 0.74, "suit", walk=0.62, say="Are you okay?", **DANA)], [{"type": "clipboard", "x": 0.56}]),
    "människor", "Dana från konsulatet kommer")
add("The treaty gives her that right. Consular officers may visit a detained national, talk with them, write to them and arrange for their legal representation.",
    real(INTL, "VISIT", "consuls may visit, talk with you and arrange a lawyer", "Vienna Convention on Consular Relations, Art. 36(1)(c)"), "vändning", "rätt att besöka")
add("You ask her the only question you've had since yesterday. Can you get me out of here today?",
    close("visit_room", "worried", "TODAY?"), "gåta", "kan du få ut mig?")
add("Her answer is printed on a State Department page. Consular officers cannot get U.S. citizens out of detention.",
    real("U.S. GOVERNMENT", "CANNOT", "get U.S. citizens out of detention", "travel.state.gov, Arrest or Detention of a U.S. Citizen Abroad"), "hot", "konsuln kan inte få ut dig", silence=True)
add("The same list keeps going. They can't tell a court anyone is guilty or innocent, they can't give legal advice or represent you, and they can't pay your fees.",
    {"type": "board", "title": "THE CONSUL CANNOT", "lines": ["get you out of detention", "tell a court you're guilty or innocent", "give legal advice or represent you", "act as your official interpreter", "pay legal, medical or other fees"], "result": "travel.state.gov – Arrest or Detention"},
    "hot", "listan över vad konsuln inte kan")
add("A federal regulation goes further. It prohibits consular officers from acting as anyone's agent or attorney, even when they'd like to help.",
    label("NOT YOUR LAWYER", "consular officers may not act as agents or attorneys", "22 CFR 92.81 (per 7 FAM 417)"), "hot", "konsuln är inte din advokat")
add("Dana can still do a few things. She hands you a list of local attorneys who speak English, and promises to visit on a regular schedule.",
    scene("visit_room", H(0.3, "doubt", "hold", hold="letter"), [F("Dana", 0.72, "suit", **DANA)], [{"type": "letter", "x": 0.54, "title": "ENGLISH-SPEAKING ATTORNEYS"}], note="CONSULS CAN: ATTORNEY LIST, REGULAR VISITS (STATE DEPT)"),
    "vändning", "listan med advokater")
add("She also asks if she can call your family. The State Department says they contact family, friends or employers, normally with written permission from the detainee.",
    real("U.S. GOVERNMENT", "WRITTEN PERMISSION", "before they contact your family, normally", "travel.state.gov, Arrest or Detention of a U.S. Citizen Abroad"), "vändning", "skriftligt tillstånd för att ringa familjen")
add("You sign her form and write your sister Maya's number from memory. It's the one number you never had to save in your phone.",
    scene("visit_room", H(0.3, "neutral", "hold", hold="letter"), [F("Dana", 0.72, "suit", say="Maya. Got it.", **DANA)], note="22 CFR 92.81: A CONSUL CAN'T BE YOUR ATTORNEY"),
    "människor", "systern Maya")

# ---------------- LEVEL 7 ----------------
add("Level seven. The lawyer.", day("SEVEN", "the lawyer"), "hot", "nivåkort 7", chapter="Level 7: The lawyer")
add("The attorneys on the list want a retainer you can't pay from a cell. So you ask Lupita what happens to people who can't pay anyone.",
    scene("holding_room", H(0.3, "worried", "hold", hold="letter"), [F("Lupita", 0.7, "teal", say="Defensor público.", hair="bun")]),
    "hot", "ingen råd med advokat")
add("Mexico's Constitution gives you the right to a lawyer of your choice from the moment of detention. If you can't name one, the judge appoints a public defender.",
    real(MX, "PUBLIC DEFENDER", "if you can't name a lawyer, one is appointed", "CPEUM, Art. 20(B), fr. VIII"), "vändning", "offentlig försvarare")
add("Before noon, a defender named Ortega arrives in a gray suit with your file under her arm. She reads it standing up, then sits down.",
    scene("fiscalia_office", H(0.3, "doubt", walk=0.38), [F("Ortega", 0.74, "suit", walk=0.6, say="Let's see.", **ORT)], [{"type": "laptop", "x": 0.52, "text": "CARPETA|LESIONES|DAÑOS"}], note="CPEUM ART. 20(B) VIII: A PUBLIC DEFENDER IF YOU CAN'T NAME ONE"),
    "människor", "försvararen Ortega")
add("Through Lupita, she explains the two possible charges. Lesiones for Héctor's neck, and daños, damage to property, for the taxi's bumper.",
    scene("fiscalia_office", H(0.3, "worried"), [F("Ortega", 0.6, "suit", say="Lesiones. Daños.", **ORT), F("Lupita", 0.82, "teal", hair="bun")]),
    "hot", "två möjliga brott")
add("In Quintana Roo, the state where Cancún sits, both injury and property damage are on the short list of crimes the law can punish even when they're accidental.",
    real(QR, "ACCIDENTAL", "injuries and damage can be punished as negligent crimes", "Código Penal de Quintana Roo, Art. 55"), "hot", "oaktsamhetsbrott")
add("For accidental crimes, the state code sets the penalty at one quarter of what the intentional version would carry.",
    real(QR, "1/4", "of the penalty, for negligent crimes", "Código Penal de Quintana Roo, Art. 54"), "vändning", "en fjärdedel av straffet")
add("Then Ortega taps the file twice. The minor injury charge can only go forward if the injured person files a complaint, a querella.",
    real(QR, "QUERELLA", "minor injuries are prosecuted only on the victim's complaint", "Código Penal de Quintana Roo, Art. 104"), "vändning", "bara efter klagomål")
add("Property damage works the same way. The state code lists it among crimes that can only be prosecuted if the owner files a complaint.",
    label("COMPLAINT", "property damage needs the owner's complaint", "Código Penal de Quintana Roo, Art. 163", bad=False), "vändning", "skadegörelse likaså")
add("That puts most of what happens to you next in Héctor's hands, more than in the prosecutor's.",
    close("fiscalia_office", "shock", "HÉCTOR"), "gåta", "Héctor bestämmer")
add("You tell Ortega about the camera on his windshield and the red light. She writes one word in big letters on her notepad, cámara, and underlines it twice.",
    scene("fiscalia_office", H(0.3, "neutral", "point"), [F("Ortega", 0.7, "suit", say="Cámara.", **ORT)], [{"type": "notepad", "x": 0.54, "text": "CÁMARA"}], note="QUINTANA ROO ART. 104: MINOR INJURIES NEED THE VICTIM'S COMPLAINT"),
    "gåta", "Ortega skriver 'cámara'")

# ---------------- LEVEL 8 ----------------
add("Level eight. The number.", day("EIGHT", "the number"), "hot", "nivåkort 8", chapter="Level 8: The number")
add("At 3 in the afternoon, Héctor's cousin comes to the office with a number written on paper. 2,800 dollars for the bumper, the neck and the days without fares.",
    scene("fiscalia_office", H(0.3, "shock"), [F("Héctor's cousin", 0.72, "orange", walk=0.6, say="Dos mil ochocientos.", hair="short")], [{"type": "letter", "x": 0.54, "title": "REPARACIÓN", "tag": "$2,800"}]),
    "hot", "kravet: $2 800")
add("Ortega explains the deal on the table. Mexico's criminal code allows a repair agreement, an acuerdo reparatorio, between the victim and the person accused.",
    real(MX, "ACUERDO", "a repair agreement between victim and accused", "CNPP, Art. 186"), "vändning", "acuerdo reparatorio")
add("Once the prosecutor or a judge approves the agreement and you've done everything it says, the criminal case is over for good.",
    label("CASE ENDED", "once the agreement is approved and fully kept", "CNPP, Art. 186", bad=False), "vändning", "fallet upphör")
add("These agreements are only allowed for some crimes, and accidental crimes are one of them. So are crimes that need a complaint or can be forgiven by the victim.",
    real(MX, "NEGLIGENT", "accidental crimes qualify for repair agreements", "CNPP, Art. 187, fr. I–II"), "vändning", "oaktsamma brott kvalificerar")
add("There's also a window. A repair agreement can be made from the moment the complaint is filed until right before the order that opens a trial.",
    label("BEFORE TRIAL", "the window for a repair agreement", "CNPP, Art. 188"), "hot", "fönstret före rättegången")
add("You don't have 2,800 dollars in your checking account. You have 900 dollars and a credit card the Fiscalía can't take.",
    {"type": "board", "title": "HÉCTOR'S NUMBER", "lines": ["the bumper and the neck: $2,800", "your checking account: $900", "hours left on the 48-hour clock: 23"], "result": "you're $1,900 short"},
    "hot", "du saknar $1 900")
add("Dana calls Maya in Ohio. Maya can't wire money to a prosecutor's office, but the State Department runs a way to send money to a U.S. citizen abroad.",
    scene("sister_kitchen", H(0.3, "worried", "hold", hold="phone"), [F("Maya", 0.72, "purple", say="How much?", hair="long")]),
    "människor", "Maya i Ohio")
add("The money goes through the State Department in Washington to the embassy or consulate, by Western Union, money order or cashier's check.",
    real("U.S. GOVERNMENT", "VIA WASHINGTON", "money for a citizen abroad goes through the State Dept", "travel.state.gov, Sending Money to a U.S. Citizen Abroad"), "vändning", "pengar via utrikesdepartementet")
add("The State Department charges a 30 dollar processing fee, once per fiscal year. Western Union charges its own fee on top of that.",
    real("U.S. GOVERNMENT", "$30", "processing fee, once per fiscal year (+ Western Union's fee)", "travel.state.gov, Sending Money to a U.S. Citizen Abroad"), "hot", "avgiften $30")
add("Maya sends 1,000 dollars that night. It's her car payment, and she tells you not to say anything about it until you're home.",
    scene("sister_kitchen", H(0.3, "sad", "hold", hold="phone"), [F("Maya", 0.72, "purple", say="Just get home.", hair="long")], [{"type": "phone", "x": 0.52, "text": "WESTERN UNION|$1,000|SENT"}], note="STATE DEPT: $30 FEE ONCE PER FISCAL YEAR + WESTERN UNION FEE"),
    "människor", "Maya skickar sin billån-betalning")
add("You still need 900 more, and the clock on the wall says 10:12, which means the real time is 10:08 at night.",
    close("holding_room", "worried", "$900 SHORT"), "hot", "fortfarande $900 kort")

# ---------------- LEVEL 9 ----------------
add("Level nine. The camera.", day("NINE", "the camera"), "hot", "nivåkort 9", chapter="Level 9: The camera")
add("The next morning, Ortega asks the prosecutor to request the video from the taxi's dash camera. Héctor's cousin brings a phone instead of a memory card.",
    scene("fiscalia_office", H(0.3, "doubt"), [F("Ortega", 0.6, "suit", **ORT), F("Héctor's cousin", 0.82, "orange", walk=0.72, hair="short")], [{"type": "phone", "x": 0.46, "text": "DASHCAM|14:02"}]),
    "gåta", "videon från kameran")
add("On the screen, the taxi stops at the roundabout. Then the picture drifts slowly backward, and the hood of your rental car fills the frame.",
    {"type": "plan", "title": "DASHCAM, 2:02 PM", "items": [{"box": [0.04, 0.3, 0.28, 0.4], "label": "2:02:10 TAXI STOPS"}, {"box": [0.36, 0.3, 0.28, 0.4], "label": "2:02:14 TAXI ROLLS BACK"}, {"box": [0.68, 0.3, 0.28, 0.4], "label": "2:02:16 CONTACT", "hot": True}]},
    "vändning", "gåtan löst: taxin rullade bakåt", silence=True)
add("The taxi rolled back into you. Your foot was on the brake the whole time, exactly like you thought, and the camera was recording it all along.",
    close("fiscalia_office", "shock", "BACKWARD"), "vändning", "det var taxin som rullade")
add("It doesn't undo the arrest. Remember the line from the State Department page. Arrests can happen regardless of who is at fault, and yours did.",
    scene("fiscalia_office", H(0.3, "sad"), [F("Ortega", 0.72, "suit", say="Still counts.", **ORT)], note="STATE DEPT: ARRESTS CAN HAPPEN REGARDLESS OF WHO IS AT FAULT"),
    "hot", "gripandet står kvar ändå")
add("But it changes the number. Héctor's cousin makes a phone call in the hallway, comes back, and crosses out 2,800 dollars. He writes 900.",
    scene("fiscalia_office", H(0.3, "smirk"), [F("Héctor's cousin", 0.72, "orange", say="Novecientos.", hair="short")], [{"type": "letter", "x": 0.54, "title": "REPARACIÓN", "tag": "$900"}]),
    "vändning", "kravet sänks till $900")
add("You sign the repair agreement with Lupita reading every line out loud. 900 dollars for the bumper, and Héctor withdraws his complaint about the neck.",
    scene("fiscalia_office", H(0.3, "neutral", "hold", hold="letter"), [F("Lupita", 0.6, "teal", hair="bun"), F("Ortega", 0.82, "suit", **ORT)], note="CNPP ART. 187: NEGLIGENT CRIMES CAN END WITH A REPAIR AGREEMENT"),
    "lösning", "avtalet skrivs under")
add("The state code says the pardon of the offended person ends the criminal case for crimes that can only be prosecuted by complaint.",
    real(QR, "PERDÓN", "the victim's pardon ends a complaint-only case", "Código Penal de Quintana Roo, Art. 73"), "vändning", "förlåtelsen avslutar fallet")
add("The prosecutor stamps the agreement at 1:20 in the afternoon. Counting from the roundabout, you were held for about 23 hours.",
    scene("fiscalia_hall", H(0.3, "smirk", walk=0.5), [F("Desk officer", 0.74, "navy", glasses=True)], [{"type": "bag", "x": 0.58, "tag": "#27"}]),
    "lösning", "fri efter 23 timmar")
add("They hand back your phone, your belt and the clear bag with the number on it. The rental keys aren't in it, because the car is in a police lot.",
    scene("fiscalia_outside", H(0.3, "doubt", walk=0.56, hold="phone"), props=[{"type": "sign", "x": 0.7, "text": "FISCALÍA GENERAL"}], note="QUINTANA ROO ART. 73: THE VICTIM'S PARDON ENDS A COMPLAINT-ONLY CASE"),
    "hot", "bilen står på polisens uppställningsplats")

# ---------------- LEVEL 10 ----------------
add("Level ten. The long way home.", day("TEN", "the long way home"), "hot", "nivåkort 10", chapter="Level 10: The long way home")
add("On the plane, you read about the version of this story where Héctor doesn't sign, and the case goes all the way to a sentence.",
    scene("airplane", H(0.4, "worried", "hold", hold="phone")), "hot", "versionen där han inte skriver under")
add("Americans sentenced in Mexico can sometimes serve the rest of it in the United States, under a prisoner transfer treaty that took effect on November 30, 1977.",
    real(INTL, "1977", "U.S.–Mexico prisoner transfer treaty in force (Nov 30)", "7 FAM 480, State Dept Foreign Affairs Manual"), "vändning", "fångöverföringsavtalet")
add("There are conditions. The sentencing country, the receiving country and the prisoner must all agree, and Mexico requires all fines to be paid before a transfer.",
    {"type": "board", "title": "A TRANSFER HOME NEEDS", "lines": ["Mexico says yes", "the U.S. says yes", "you say yes", "every fine paid first"], "result": "7 FAM 480"},
    "hot", "alla tre måste säga ja")
add("Your consent is checked in Mexico by a U.S. magistrate judge. Once it's verified, federal law says that consent can't be taken back.",
    real(US, "IRREVOCABLE", "your consent to transfer, once verified", "18 U.S.C. 4100(b); 4108(a)"), "hot", "samtycket kan inte dras tillbaka")
add("And only the country that convicted you can change or cancel the conviction. A U.S. court can't reopen a Mexican case.",
    label("ONLY MEXICO", "can modify or set aside a Mexican conviction", "18 U.S.C. 4108(b)"), "hot", "bara Mexiko kan ändra domen")
add("There's one more rule in that story, for people the government lends money to get home. If you default on that loan, your next passport can be refused.",
    real(US, "PASSPORT REFUSED", "if you're in default on a repatriation loan", "22 CFR 51.60(a)(1)"), "hot", "pass nekas vid obetalt hemresellån")
add("Your version cost 900 dollars, 1,000 borrowed from Maya, 23 hours on a bench and a 4 minute fast clock you will see in your sleep for weeks.",
    {"type": "board", "title": "ONE ROUNDABOUT", "lines": ["the repair agreement: $900", "borrowed from Maya: $1,000", "State Dept fee: $30", "held: about 23 hours"], "result": "a $19-a-day box on a yellow copy"},
    "vändning", "summeringen", chapter="The end: What it cost")
add("You pay Maya back in 4 months. She frames the Western Union receipt and hangs it in her kitchen, which you pretend not to find funny.",
    scene("sister_kitchen", H(0.3, "smirk", walk=0.5), [F("Maya", 0.72, "purple", say="Never again.", hair="long")], [{"type": "frame", "x": 0.56, "text": "$1,000"}]),
    "människor", "du betalar tillbaka Maya")
add("A year later you fly into Cancún for a wedding. At the rental counter, the agent slides the same yellow form across the desk.",
    scene("rental_counter", H(0.3, "neutral", walk=0.4), [F("Counter agent", 0.74, "green", hair="short")], [{"type": "contract", "x": 0.56, "title": "THIRD PARTY LIABILITY"}]),
    "callback", "tillbaka vid hyrdisken")
add("This time you initial the box that says accept, and you read every line before you sign, the way Lupita read the agreement to you.",
    scene("rental_counter", H(0.32, "smirk", "hold", hold="letter"), [F("Counter agent", 0.74, "green", say="All set.", hair="short")], [{"type": "contract", "x": 0.56, "title": "THIRD PARTY LIABILITY", "tag": "ACCEPTED"}], note="MEXICAN CAR INSURANCE IS REQUIRED FOR ALL VEHICLES (STATE DEPT)"),
    "callback", "du kryssar i 'accept'")
add("At the next counter, a man in a ball cap waves off the same line with a laugh and tells the agent his card back home has him covered.",
    scene("rental_counter", H(0.24, "doubt"), [F("Tourist", 0.62, "blue", say="I'm covered.", cap=True), F("Counter agent", 0.86, "green", hair="short")]),
    "callback", "nästa turist tackar nej – cykeln fortsätter")
add("You think about saying something, and then the agent asks him twice if he's sure, exactly like she asked you.",
    scene("rental_counter", H(0.24, "doubt", walk=0.3), [F("Tourist", 0.62, "blue", cap=True), F("Counter agent", 0.86, "green", say="You're sure?", hair="short")], [{"type": "key_tag", "x": 0.74, "text": "#28"}]),
    "callback", "'are you sure?' – callback")
add("So answer this one honestly in the comments. Have you ever said no to rental car insurance abroad, and would you say it again after this?",
    label("WOULD YOU?", "say no to rental insurance abroad again?", None, bad=False), "callback", "fråga till tittaren")

# extra faktaskyltar (INNEHÅLLSORDER 2: ny fakta minst var 30:e s)
EXTRA = {3: "STATE DEPT: UNINSURED DRIVERS IN CRASHES MAY BE ARRESTED",
         15: "STATE DEPT: ARRESTS CAN HAPPEN REGARDLESS OF WHO IS AT FAULT",
         29: "CPEUM ART. 16: NEXT STOP, THE MINISTERIO PÚBLICO",
         31: "CPEUM ART. 16: THE DETENTION IS LOGGED AT ONCE",
         105: "LEY DE CAMINOS ART. 63 BIS: THIRD-PARTY INSURANCE ON FEDERAL ROADS"}
for i, txt in EXTRA.items():
    assert S[i][1]["type"] == "scene" and "note_card" not in S[i][1], i
    S[i][1]["note_card"] = {"text": txt}

# ---------------- bygg ----------------
scenes, beats, t = [], [], 0.0
for say, vis, typ, txt, extra in S:
    sc = {"say": say, "visual": vis}
    for k in ("chapter", "sfx", "silence"):
        if k in extra: sc[k] = extra[k]
    scenes.append(sc)
    beats.append({"t": f"{int(t // 60)}:{int(t % 60):02d}", "typ": typ, "text": txt})
    t += max(len(say.split()) / WPS + 0.45, 2.0)

TITLE = "Your Life at Every Level of a Rental Car Crash in Mexico"
sources = [
    ("U.S. State Dept – Mexico Travel Advisory / country information (Mexican car insurance required; uninsured drivers in accidents may be arrested; arrests regardless of fault; U.S. licenses valid; ask police to inform the embassy)", "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/mexico-travel-advisory.html"),
    ("U.S. State Dept – Arrest or Detention of a U.S. Citizen Abroad (what consular officers can and cannot do)", "https://travel.state.gov/content/passports/en/emergencies/arrest.html"),
    ("U.S. State Dept – Sending Money to a U.S. Citizen Abroad ($30 processing fee once per fiscal year)", "https://travel.state.gov/content/travel/en/international-travel/while-abroad/sending-money-abroad.html"),
    ("7 FAM 410 (consular officers; 22 CFR 92.81)", "https://fam.state.gov/fam/07fam/07fam0410.html"),
    ("7 FAM 480 (international prisoner transfer; U.S.–Mexico treaty in force 11/30/1977; fines paid first)", "https://fam.state.gov/fam/07fam/07fam0480.html"),
    ("Vienna Convention on Consular Relations (1963), Art. 36", "https://hrlibrary.umn.edu/instree/vienna-consularrelations.html"),
    ("UN Treaty Collection – Vienna Convention on Consular Relations, status (183 parties)", "https://treaties.un.org/doc/Publication/MTDSG/Volume%20I/Chapter%20III/iii-6.en.xml"),
    ("Constitución Política de los Estados Unidos Mexicanos, Art. 16 (flagrancia; 48 horas)", "https://www.scjn.gob.mx/sites/default/files/cpeum/documento/CPEUM-016_0.pdf"),
    ("CPEUM, Art. 19 (72 horas; auto de vinculación a proceso)", "https://www.scjn.gob.mx/sites/default/files/cpeum/documento/CPEUM-019_0.pdf"),
    ("CPEUM, Art. 20(B) (presunción de inocencia; silencio; defensor público)", "https://www.scjn.gob.mx/sites/default/files/cpeum/documento/CPEUM-020_0.pdf"),
    ("Código Nacional de Procedimientos Penales, Arts. 45, 113, 151, 186–189 (intérprete; asistencia consular; acuerdos reparatorios)", "https://paot.org.mx/centro/codigos/federal/pdf/2025/COD_NAC_PROC_PENA_16_12_2024.pdf"),
    ("Ley de Caminos, Puentes y Autotransporte Federal, Art. 63 Bis (seguro de responsabilidad civil)", "https://mley.mx/LCPAF/articulo/63-bis/"),
    ("Código Penal para el Estado de Quintana Roo, Arts. 54, 55, 73, 99, 104, 163", "https://documentos.congresoqroo.gob.mx/codigos/C6-XVIII-09102024-20241021T160708-C1720241009250.pdf"),
    ("18 U.S.C. 4100 (consent to transfer irrevocable)", "https://www.law.cornell.edu/uscode/text/18/4100"),
    ("18 U.S.C. 4108 (verification of consent by a U.S. magistrate judge; only sentencing country may modify)", "https://www.law.cornell.edu/uscode/text/18/4108"),
    ("22 CFR 51.60 (passport refused when in default on a repatriation loan)", "https://www.law.cornell.edu/cfr/text/22/51.60"),
]

m = {
    "channel": "Day After Court", "title": TITLE, "standard": "DAC_STANDARD",
    "format": "FORMAT_BLUEPRINT – DAC (Your Life at Every Level of …, nivåkort, siffer-bubblor) + DUI-mallen (vanlig händelse i tidsordning)",
    "style": "qm", "look": "dac_semireal", "voice": "am_michael", "speed": 0.97, "lang": "en-us",
    "music": "calm", "music_level": 0.06,
    "beats": beats, "scenes": scenes,
}
json.dump(m, open("/tmp/claude-0/-home-claude-yt-automation-media/9432bb76-090e-52eb-aa36-a311db6808ff/scratchpad/dac26_core.json", "w"), ensure_ascii=False)
print(len(scenes), "scener", round(t / 60, 1), "min", sum(len(s["say"].split()) for s in scenes), "ord")

# ---------------- metadata ----------------
FACT = ("real", "label", "board", "plan", "daycard")
tt, last, gaps, nfact = 0.0, 0.0, [], 0
for s in scenes:
    v = s["visual"]
    if v["type"] in FACT or v.get("note_card"):
        gaps.append(tt - last); last = tt; nfact += 1
    tt += max(len(s["say"].split()) / WPS + 0.45, 2.0)
gaps.append(tt - last)
nw = [len(s["say"].split()) for s in scenes]
innehall = {"snittord_per_say": round(sum(nw) / len(nw), 1), "say_under_6_ord": sum(1 for n in nw if n < 6),
            "say_under_6_ord_kommentar": "alla är nivåkortens repliker ('Level four. The clock.') – ≈0,6 per minut",
            "faktaskyltar": nfact, "verkliga_regelkort_real": sum(1 for s in scenes if s["visual"]["type"] == "real"),
            "storsta_lucka_s": round(max(gaps), 1),
            "kommentar": f"Beräknat med granskning.py:s tempo (2,6 ord/s + 0,45 s). Faktaskylt = real/label/board/plan/daycard eller note_card. Längd ≈{tt/60:.1f} min."}

m["seo"] = {
    "title": TITLE,
    "title_b": "Arrested After a 4 MPH Crash in Mexico: Every Level, 48 Hours",
    "hook": "Twelve minutes out of the Cancún airport, your rental car and a taxi bump at a roundabout. This is every level that follows, from the roundabout to the day you find out what the taxi's dash camera saw.",
    "summary": "A 4 mph bump with a taxi at a roundabout outside Cancún, and you declined the rental counter's third-party liability insurance. This video follows a made-up American tourist through every level of a rental car crash arrest in Mexico, in time order: why the U.S. State Department says Mexican car insurance is required and that uninsured drivers in accidents may be arrested regardless of who is at fault, Mexico's federal insurance rule (Ley de Caminos, Art. 63 Bis), arrest in the act and the prosecutor's 48-hour limit (Constitution Art. 16), the judge's 72 hours (Art. 19), the right to a free interpreter (CNPP Arts. 45 and 113), silence, presumption of innocence and the public defender (Art. 20), consular notification under CNPP Art. 151 and the Vienna Convention Art. 36, what a U.S. consul can and cannot do, sending money through the State Department ($30 fee), Quintana Roo's rules on negligent injuries and property damage (complaint, one-quarter penalty, the victim's pardon), the repair agreement (acuerdo reparatorio, CNPP Arts. 186–188), the U.S.–Mexico prisoner transfer treaty (in force Nov 30, 1977; 18 U.S.C. 4100 and 4108) and the passport rule for unpaid repatriation loans (22 CFR 51.60).\n\nEveryone in this story is made up, and so are the rental company, the taxi, the dollar amounts (the $19 a day insurance, the $2,800 and $900 demands, the $1,000 from Maya), the times and the dash camera video. The laws, deadlines and government rules come from the sources listed below. Real cases depend on the facts, the state and the authorities involved.",
    "disclaimer": "This video explains general Mexican, Quintana Roo, U.S. and treaty rules for education and entertainment. It is not legal advice. Laws differ by state and country and change over time. If you or someone you know is detained abroad, ask the authorities to notify the nearest U.S. embassy or consulate and contact a licensed local attorney.",
    "keywords": ["your life at every level of", "your life at every level", "what happens if you get arrested in another country", "what happens if you get arrested", "car accident in mexico", "arrested in mexico", "rental car insurance mexico", "mexican car insurance", "third party liability mexico", "us embassy arrested abroad", "vienna convention consular notification", "48 hours mexico ministerio publico", "acuerdo reparatorio", "prisoner transfer mexico"],
    "sources": [{"title": a, "url": b} for a, b in sources],
    "question": "Have you ever said no to rental car insurance abroad, and would you say it again after this?",
    "pinned_comment": "Be honest: have you ever declined the rental counter's insurance on a trip abroad? Would you do it again after this?",
    "hashtags": ["#mexico", "#lawexplained", "#cancun"],
    "playlist": "What Really Happens After... (Every Stage, U.S. Law Explained)",
    "chapters_note": "kapitel = 'chapter'-fälten (Level 1: The roundabout … Level 10: The long way home, The end: What it cost)",
    "sokfras": "your life at every level of",
    "sokfras_kalla": "TREND_2026-11-26 (YouTubes sökförslag 26/11 för 'your life at every level of' och 'what happens if you get arrested' → 'in another country'). Titeln innehåller förslagsfrasen 'your life at every level of'; 'what happens if you get arrested in another country' ligger i keywords. Egen hämtning av sökförslag för 'arrested in mexico' misslyckades i körningen (proxy 403 / WebFetch-timeout i underagent).",
}

m["thumb"] = {
    "kind": "dac_semireal",
    "klickfraga": "En krock i 6 km/h med en taxi i Cancún – och du sitter hos åklagaren med en 48-timmarsklocka. Vad händer på varje nivå, och vad såg taxins kamera?",
    "hot_i_bild": "Den mexikanska polisen med handen höjd mellan hyrbilen och taxin i rondellen, taxins bakre stötfångare intryckt och den röda kameralampan i vindrutan; hjälten stor i höger tredjedel (≈60 % av höjden) med det gula hyreskontraktet i handen, chockad.",
    "hjalte_andel": 60,
    "textord": 3,
    "skiljer_sig": "Förra DAC (K2lPH0w1HYk, självkassan): inomhus i en butik med röd väst och kundvagn, siffran '$38.47'. Nu: utomhus i starkt mexikanskt dagsljus (turkos himmel, palmer, rondell), två bilar, en uniformerad polis, och en tid ('48 HOURS') i stället för ett belopp.",
    "jamfor_ark": "chk/jamfor-dac-2026-11-26.png",
    "jamfor_mot": ["DqyGPrK3LGQ (Baldy POV, Every Pilot Rank)", "uKBrXDWCWlw (Miles Unnoticed – How Getting Arrested on a Cruise Ship Destroys Your Life at Every Level)", "K2lPH0w1HYk (vår förra DAC)"],
    "forsta_scen_matchar": "Scen 1 (0–5 s) är miniatyr A i rörelse: samma rondell (roundabout), hyrbilen och taxin med den röda kameralampan; scen 2 visar polisen som kommer – samma tre element som i miniatyren.",
    "variants": [
        {"id": "A", "layout": "hjälten stor höger tredjedel, polisen + de två bilarna till vänster, text uppe till vänster", "text": "LEVEL 1", "label": "48 HOURS (gul undertitel)", "scene": "ljus rondell i Cancún, palmer och turkos himmel, vit hyrbil mot en taxi med intryckt stötfångare och röd lampa i vindrutan, polis med höjd hand; hjälten (grå henley) chockad med gult kontrakt; inga logotyper"},
        {"id": "B", "layout": "ANNAN bild: väggklocka stor i förgrunden, hjälten liten på bänken i väntrummet", "text": "LEVEL 4", "label": "4 MIN FAST (gul)", "scene": "Fiscalías väntrum, betongvägg, klocka, metallbänk, vattenflaska"},
        {"id": "C", "layout": "ANNAN bild: telefonskärm med kamerans bild jättestor i förgrunden, hjälten pekar", "text": "WHO HIT WHO?", "label": None, "scene": "dashcam-bild på en telefon, tidsstämpel 2:02:14, taxins bakdel närmar sig (DAC får ha fråga)"},
    ],
}

m["forbattring"] = {
    "forra_videon": "Your Life at Every Level of a $38 Self-Checkout Arrest (K2lPH0w1HYk, publicerad 26 nov 00:30) – enligt PUBLICERAT_2026-11-25: 1 exponering vid 2 h-kontrollen; förra DAC före den: b1w06aHERrc 3 exp på 14 h. DAC 28 d: 663 exp, 3,8 % CTR, 4:37 snitt.",
    "problem": "Två DAC-videor i rad har knappt fått exponeringar; båda är inomhus (trapphus, butik) med lokala delstatsregler som bara gäller en delstat (Kalifornien, Illinois), vilket gör ämnet smalt för publiken i hela USA/Kanada.",
    "andring": "Ämnet gäller alla amerikaner och kanadensare som reser (hyrbil i Mexiko, ett av de vanligaste resmålen) och följer dagens trendfras 'what happens if you get arrested in another country'. Ny miljö (utomhus, starkt dagsljus), nytt rättssystem (Mexiko + delstaten Quintana Roo + USA:s konsulära regler + fördrag), en tydlig nedräkning (48 h-klockan) som håller spänningen över nivå 4–9, och en gåta som löses av ett föremål i första bilden (taxins kamera).",
    "forvantat": "CTR ≥ 4 % (resa + Mexiko + trendtitel), ≥ 55 % kvar vid 0:30, ≥ 35 % vid 2:00, snittvisning ≥ 5:00.",
    "referens": "Miles Unnoticed 'How Getting Arrested on a Cruise Ship Destroys Your Life at Every Level' (uKBrXDWCWlw, 11 694 visningar vecka 23/11, närmast i ämne: gripen på resa) + Honest Life POV 'Your Life at Every Level of Living Off the Grid' (678 751 månad) + Baldy POV DqyGPrK3LGQ. Transkript kunde inte hämtas: ingen Chrome i molnkörningen (youtube-transcriber kräver den), vidIQ 3 krediter (sökning kostar 5). Kroken 0/5/10/20/30 s enligt FORMAT_BLUEPRINT DAC: 0 s plats + hot i du-form, ~5 s polisen, ~10 s löftet, ~17 s gåtan (kameran), ~25 s första verkliga regeln.",
    "vi_slår_den_med": "En verklig klocka från lagen (48 h, Art. 16) som tittaren ser ticka på väggen; 16 öppnade källor med paragraf på skärmen (State Dept, CPEUM 16/19/20, CNPP 45/113/151/186–188, Quintana Roo 54/55/73/104/163, Wienkonventionen 36, 18 U.S.C. 4100/4108, 22 CFR 51.60); och konkret, användbar kunskap för nästa resa (mexikansk ansvarsförsäkring, be polisen ringa konsulatet, vad konsuln inte kan, $30-avgiften).",
    "trend": {
        "fras": "your life at every level of + what happens if you get arrested in another country",
        "kalla": "automation/TREND_2026-11-26.md (DAC: sökförslag 26/11 'what happens if you get arrested' → 'in another country'; titelförslag 2 'What Happens If You Get Arrested in Another Country?')",
        "trendvideo": "How Getting Arrested on a Cruise Ship Destroys Your Life at Every Level – Miles Unnoticed – 11 694 (vecka, Action 23/11); Your Life at Every Level of Living Off the Grid – Honest Life POV – 678 751 (månad)",
        "andrat": "Trendfilens vinkel 'gripen utomlands' i 'Your Life at Every Level of …'-mallen, konkretiserad till den vanligaste situationen (hyrbilskrock i Mexiko). Titeln 'Your Life at Every Level of Getting Arrested in Mexico' valdes bort: teckenlikhet 0,77 mot dac-24 (originalitet.py max 0,70). Ingen video med titeln hittades vid webbsök.",
    },
}
m["experiment"] = {"variable": "resa/utomlands + nedräkningsklocka i stället för en enskild delstats regler", "metric": "CTR, 0:30-andel, snittvisning, exponeringar", "decide_at": "48 h + jämförelse mot K2lPH0w1HYk och b1w06aHERrc"}
m["hooks_kandidater"] = {
    "A_vald": "12 minutes out of the Cancún airport, your rental car and a taxi bump. + At 4 miles an hour, the taxi driver still climbs out holding his neck. (stakes + specificity; bild = miniatyren; siffror inom 5 s)",
    "B": "A 4 mile an hour bump can start a 48 hour clock in Mexico. (curiosity – men första bilden blir ett kort)",
    "C": "In Mexico, an uninsured driver in a crash can be arrested no matter who caused it. (contrarian/stakes – abstrakt, ingen person i bild; kommer i stället vid ~0:45)",
    "val": "A – miniatyrens scen från bildruta 0, insats med siffror inom 5 s, löftet vid ~10 s; B:s klocka i nivå 4, C:s regel i nivå 1.",
}
m["standard_check"] = {
    "miniatyr": "FORMAT_BLUEPRINT DAC: 'LEVEL 1' vit + gul undertitel '48 HOURS', halvrealistisk man; hjälten ≈60 % höjd i höger tredjedel, 3 ord, ljus dagsmiljö; hotet (polisen + bilarna + kameralampan) störst; B/C andra bilder.",
    "krok": "du-form från första meningen; plats + händelse + siffror inom 5 s ('12 minutes', '4 miles an hour'); polisen ~5 s; löftet i klartext ~10 s; gåtan (kameran) ~17 s; första verkliga regel (State Dept) ~30 s; ingen presentation de första 12 s.",
    "nivåer": "10 nivåer + slut: The roundabout, The yellow copy, The truck, The clock, The embassy, The consul, The lawyer, The number, The camera, The long way home, What it cost – varje nivå: första ögonblick → svårast → verklig regel → insidersanning → känsloslag.",
    "motiv": "taxins röda kameralampa (0:12, nivå 3, 5, 7, löses nivå 9), väggklockan som går 4 minuter fel (nivå 4, 5, 8, slutet), det gula kontraktet (nivå 2, slutet), 'Are you sure?' vid disken (nivå 2 och slutet), påsen #27 / nyckelbricka #28.",
    "slut": "gåtan löst (taxin rullade bakåt 2:02:14), avtal $900, fri efter ~23 h, men gripandet skedde ändå ('regardless of who is at fault'); fångöverföring + pass-regeln som den värre versionen; callback vid hyrdisken, cykeln fortsätter med nästa turist, fråga till tittaren.",
    "källor": "16 källor i beskrivningen; källrad på varje real/label-kort.",
    "miljöer": "roundabout, car_interior, rental_counter, police_truck_back, fiscalia_outside, fiscalia_hall, holding_room, visit_room, fiscalia_office, sister_kitchen, airplane",
    "tittartid": "första 30 s: 6 helbildsscener i rondellen (alla med walk_to), ingen medium/närbild, byte var ~4–6 s; första faktaskylten (note_card) vid ~16 s, första real-kort ~45 s.",
    "innehall": innehall,
}
m["notes"] = {
    "påhittat": "alla personer (du, Héctor, hans kusin, Ríos, utredaren, Lupita, Dana, Ortega, Maya, disk-agenten, turisten), hyrfirman, taxin, beloppen ($19/dag, $2 800, $900, $1 000, $900 på kontot), tider (14:02, 14:14, 13:20), 23 timmar, kameravideon, klockan som går 4 minuter fel, 12 minuter, 4 mph.",
    "uträkningar": "$2 800 − $900 = $1 900; 14:02 → 13:20 nästa dag ≈ 23 h.",
    "osäkert": "State Dept-raderna ('Mexican car insurance is required…', 'Uninsured drivers … may be subject to arrest', 'Arrests can happen regardless of who is at fault', 'U.S. driver's licenses are valid in Mexico', 'ask the police or prison officials to inform…') lästa på State Dept-spegeln adoption.state.gov (Mexico Travel Advisory 29 maj 2026) – travel.state.gov själv nekade underagenten. Konsulns kan/kan inte-lista från travel.state.gov/content/passports/en/emergencies/arrest.html. Privacy Act-formuleringen undveks (bara 'normally with written permission'). '144 timmar' används inte (står inte i författningen). 63 Bis gäller federala vägar – manuset säger 'federal roads and highways'. Att lesiones i berättelsen är 'minor' (Art. 99, läker inom 15 dagar) och att Art. 104 kräver querella gäller just den första delen av Art. 99. Art. 189-numret för extinción ej använt på skärmen (bara 186–188). Fångöverföringsåret: FAM 11/30/1977 (ikraftträdande) – DOJ säger programmet började nov 1976; manuset säger 'took effect on November 30, 1977'. Att utredaren går för att hämta tolk, att ingen läser rättigheter i bilen, att kusinen sänker kravet och att polisen tar kontraktet är berättelse.",
    "motor": "Nya bakgrunder (fallback inom parentes): roundabout – ljus rondell i Cancún med palmer, fontän, turkos himmel (MÅSTE finnas: scen 1 + miniatyr A; fallback intersection från dac-21/city_street), rental_counter – hyrdisk på flygplats (fallback bank), police_truck_back – flak/bakdel på polisens pickup med metallbänk (fallback squad_car), fiscalia_outside – låg betongbyggnad med skylt (fallback court_hall), fiscalia_hall (fallback booking), holding_room – väntrum med bänk och väggklocka (fallback booking), visit_room – besöksrum (fallback collector_office), fiscalia_office (fallback pd_office), sister_kitchen (fallback keisha_kitchen/apartment), airplane (fallback car_interior); car_interior finns. Rekvisita: rental_car (vit, dent), taxi (vit/grön, dashcam med blinkande röd lampa, small), police_truck (pickup, door_open), contract (gult hyreskontrakt med title/tag), key_tag, wall_clock (time), clipboard, notepad (text), sign (text), frame; phone/letter/summons/laptop/bag finns. Bifigurer: Héctor (vit skjorta, keps), Ríos + partner (navy, keps), utredare (kostym), Lupita (teal, knut), Dana (kostym, knut), Ortega (grå kostym, glasögon), kusinen (orange), Maya (lila), disk-agent (grön), turist (blå, keps). hero holding: keys/letter/phone. sfx: crash (mjuk), siren, paper, click. Inga handbojor i närbild, inget våld, inget blod. 10 nivåkort som daycard. Inga Shorts.",
    "humanizer": "humanizer:humanizer kört över say 26/11: 'Not paused, over', 'And then the part nobody expects', 'isn't the prosecutor. It's Héctor', 'What Dana can do is shorter, but it's real' och fragmentet 'Free.' omskrivna; inga tankstreck; första repliken ändrad så att den inte avslöjar gåtan (bilen och taxin 'bump'). Siffror/källor oförändrade.",
    "research": "Två underagenter 26/11 (WebSearch/WebFetch): State Dept-spegeln adoption.state.gov (Mexiko), travel.state.gov/content/passports/en/emergencies/arrest.html, sending-money-abroad, fam.state.gov 7 FAM 410/480, hrlibrary.umn.edu (VCCR), treaties.un.org, scjn.gob.mx (CPEUM 16/19/20), paot.org.mx (CNPP, reform 16-12-2024), mley.mx (63 Bis, + DOF Acuerdo 07/2014), congresoqroo.gob.mx (Código Penal QRoo, reform 09-10-2024), Cornell LII (18 U.S.C. 4100/4108, 22 CFR 51.60). Sökförslag och YouTube-topplista kunde inte hämtas (proxy 403, WebFetch-timeout, vidIQ 3 krediter < 5).",
}
out = "manus/dac-2026-11-26.json"
json.dump(m, open(out, "w"), ensure_ascii=False, indent=None)
print("skrev", out, innehall)
