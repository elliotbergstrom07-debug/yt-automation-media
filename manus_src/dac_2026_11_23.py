import json

def H(x=0.3, expr="neutral", arms="down", **k):
    d = {"x": x, "expr": expr, "arms": arms}; d.update(k); return d

def sc(loc, hero=None, friends=None, props=None, shot="wide", note=None):
    v = {"type": "scene", "location": loc, "shot": shot}
    if hero: v["hero"] = hero
    if friends: v["friends"] = friends
    if props: v["props"] = props
    if note: v["note_card"] = {"text": note}
    return v

def F(name, outfit, x=0.74, **k):
    d = {"x": x, "outfit": outfit, "name": name}; d.update(k); return d

def real(big, text, src, head="CALIFORNIA RULE"):
    return {"type": "real", "head": head, "big": big, "text": text, "source": src}

def label(big, text, bad=True, src=None):
    return {"type": "label", "big": big, "text": text, "source": src, "bad": bad}

def close(loc, expr, thought, bad=True):
    return {"type": "closeup", "location": loc, "expr": expr, "look": -1, "thought": thought, "bad": bad}

def day(lbl, sub):
    return {"type": "daycard", "label": lbl, "sub": sub}

PATROL = {"type": "patrol_car", "x": 0.7, "lights": True}
TICKET = lambda tag="$247": {"type": "summons", "x": 0.64, "title": "NOTICE TO APPEAR", "tag": tag}
OFF = lambda x=0.74, **k: F("Officer Pruitt", "uniform", x, hair="short", **k)
DEZ = lambda x=0.74, **k: F("Dez", "orange", x, hair="short", cap=True, **k)
OKA = lambda x=0.74, **k: F("Mrs. Okafor", "green", x, hair="bun", glasses=True, **k)
JO = lambda x=0.74, **k: F("Jo", "pink", x, hair="long", **k)

SRC = {
 "dmv65": "CA DMV Driver's Handbook – 65 mph unless posted",
 "jcfaq": "Judicial Council of California – Traffic Program FAQ",
 "glenn": "Glenn County Superior Court – 2026 Uniform Bail and Penalty Schedule",
 "self": "selfhelp.courts.ca.gov – Traffic",
 "sc": "Santa Clara + Sacramento Superior Court traffic FAQs",
 "dmvaddr": "CA DMV Driver's Handbook – changing your address",
 "ts": "selfhelp.courts.ca.gov – Traffic school",
 "tsfee": "Calaveras + Sacramento Superior Court traffic pages",
 "twd": "selfhelp.courts.ca.gov – Trial by written declaration",
 "pc196": "Calaveras Superior Court (Penal Code 19.6)",
 "pts": "CA DMV – Negligent operator (Vehicle Code 12810)",
 "negop": "CA DMV – Negligent operator actions (VC 12810.5)",
 "rec": "CA DMV Driver's Handbook – laws and rules of the road",
 "civ": "Riverside Superior Court – AB 199 notice (Penal Code 1214.1)",
 "ab103": "Mariposa Superior Court – AB 103 notice (2017)",
 "chp": "CHP Highway Patrol Manual 81.2, chapter 2",
 "r4335": "California Rules of Court, rule 4.335",
 "atp": "selfhelp.courts.ca.gov – Ask to lower your fine (MyCitations)",
 "reissue": "CA DMV – Reissue fees",
 "csr": "Judicial Council – 2026 Court Statistics Report",
}

S = []
def add(say, visual, beat=None, **extra):
    d = {"say": say, "visual": visual}; d.update(extra)
    S.append((d, beat))

# ---------------- LEVEL 1: THE STOP ----------------
add("79 in a 65, and red and blue lights fill your mirror.",
    sc("highway", H(0.22, "shock", "head", walk_to=0.32), props=[PATROL]), ("hot", "blåljus i backspegeln – 79 i en 65"),
    chapter="Level 1: The stop", sfx="siren")
add("Your shift starts in 11 minutes. The officer walks up slowly.",
    sc("highway", H(0.32, "worried", walk_to=0.28), [OFF(0.82, walk_to=0.6)], [PATROL]), ("hot", "polisen går fram – 11 minuter till skiftet"))
add("This one stop becomes a 247 dollar fine, a suspended license, and a towed car.",
    real("$247", "the real total for 1–15 mph over in Glenn County", SRC["glenn"], "WHAT THIS STOP COSTS"), ("hot", "löftet: $247, indraget körkort, bärgad bil"))
add("By the end, you'll know how one folded paper did all three.",
    sc("highway", H(0.28, "worried", "hold", holding="card", walk_to=0.34), [OFF(0.6)], [PATROL]), ("gåta", "hur ett vikt papper gjorde alla tre"))
add("He writes 79 where the speed limit sign says 65.",
    sc("highway", H(0.3, "doubt", walk_to=0.36), [OFF(0.6, say="79 in a 65.")], [PATROL], note="79 MPH IN A 65 ZONE = 14 OVER"), ("vändning", "79 skrivs in"))
add("In California, 65 is the top speed on most highways unless a sign says otherwise.",
    real("65 MPH", "the top speed on most California highways unless posted", SRC["dmv65"]), ("vändning", "65 är standardgränsen"))
add("Then he turns the pad around and hands you a pen. Sign here, he says.",
    sc("highway", H(0.34, "worried", "hold", holding="letter", walk_to=0.4), [OFF(0.6, say="Sign here.")], [PATROL]), ("gåta", "underskriften"))
add("He says it the way he must say it all day. Your signature is a promise to show up, and it has a date on it.",
    sc("highway", H(0.34, "doubt", "hold", holding="letter"), [OFF(0.6)], [PATROL], note="SIGNING = A PROMISE TO APPEAR"))
add("The state's own court page puts it plainly. By signing the traffic citation, you have given your promise that you will appear.",
    real("A PROMISE", "your signature means you promise to appear", SRC["jcfaq"]), ("vändning", "signatur = löfte att infinna sig"))
add("You sign it fast. Your hand is shaking a little, so your name looks like someone else wrote it.",
    close("highway", "worried", "SIGNED"))
add("He tears off the pink copy and taps the bottom of it twice. There's a date down there, in small print, with a court address.",
    sc("highway", H(0.34, "doubt", "hold", holding="letter"), [OFF(0.62, say="Date's at the bottom.")], [PATROL], note="THE DATE ON THE TICKET IS YOUR DEADLINE"), ("gåta", "datumet längst ned"))
add("Then he says the thing he probably says twenty times a week. Slow is cheaper. And he walks back to his car.",
    sc("highway", H(0.3, "doubt"), [OFF(0.7, say="Slow is cheaper.", walk_to=0.82)], [PATROL], note="A SPEEDING CONVICTION = 1 POINT ON YOUR RECORD"), ("människor", "Pruitts replik: Slow is cheaper"))
add("You fold the ticket in half, then in half again, and push it into the cup holder under an old coffee lid.",
    sc("car_interior", H(0.4, "neutral", "hold", holding="letter"), props=[{"type": "cup_holder", "x": 0.6, "ticket": True}]), ("gåta", "biljetten i mugghållaren"))
add("You make it to work 6 minutes late. Your coworker Dez is already at the loading dock, holding two coffees.",
    sc("loading_dock", H(0.3, "worried", walk_to=0.42), [DEZ(0.76, say="You're late.")]))
add("Dez has had three tickets. He waves his hand at yours like it's a parking stub. They mail you a reminder, he says. Wait for the letter.",
    sc("loading_dock", H(0.32, "doubt"), [DEZ(0.72, say="Wait for the letter.")], note="1–15 MPH OVER: $35 BASE FINE"), ("gåta", "Dez: vänta på brevet"))
add("It sounds like good advice. It's the advice that costs you the most in this whole story.",
    label("WAIT FOR THE LETTER", "the advice that costs the most"), ("hot", "rådet som kostar mest"))

# ---------------- LEVEL 2: THE CUP HOLDER ----------------
add("Level 2. The cup holder.", day("LEVEL 2", "the cup holder"), ("vändning", "nivå 2"), chapter="Level 2: The cup holder")
add("The ticket rides around with you for a week. It goes to the grocery store, the gym, and a gas station in Willows.",
    sc("car_interior", H(0.4, "neutral"), props=[{"type": "cup_holder", "x": 0.6, "ticket": True}]))
add("You're also moving that week. Your lease ended, so you carry boxes from your old apartment to a new place across town.",
    sc("front_door", H(0.3, "neutral", "hold", holding="box", walk_to=0.5), props=[{"type": "boxes", "x": 0.7}]), ("människor", "flytten"))
add("Your old neighbor, Mrs. Okafor, watches from her door with a cup of tea. She asks if you've changed your address yet. You say, soon.",
    sc("front_door", H(0.4, "smirk", "hold", holding="box"), [OKA(0.78, say="Changed your address?")], note="CA DMV: NEW ADDRESS WITHIN 10 DAYS OF MOVING"), ("gåta", "Mrs. Okafor frågar om adressen"))
add("Soon isn't a date. The DMV handbook gives you an actual one. If you move, you must tell DMV your new address within ten days.",
    real("10 DAYS", "to tell DMV your new address after you move", SRC["dmvaddr"]), ("vändning", "10 dagar att anmäla adress"))
add("Day 11 comes and goes. Your address with the DMV is still the old apartment, the one with Mrs. Okafor's tea next door.",
    sc("apartment", H(0.3, "neutral", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "DMV ADDRESS|OLD APT|DAY 11"}]), ("hot", "dag 11 – fel adress kvar"))
add("Meanwhile you wait for the reminder, the way Dez told you. The court's self help page says it may take 30 days or longer to get one.",
    real("30+ DAYS", "how long a courtesy notice can take to arrive", SRC["self"]), ("vändning", "påminnelsen kan ta 30+ dagar"))
add("And here is the part nobody tells you at the side of the road. The reminder is not the deadline. The date on the ticket is.",
    label("NOT THE DEADLINE", "the reminder is a courtesy, the ticket date is the rule"), ("hot", "påminnelsen är inte fristen"))
add("County court pages say it the same way. Resolve your case on or before the date on your ticket, and if no notice has come by then, contact the court.",
    real("THE TICKET DATE", "resolve on or before it, notice or no notice", SRC["sc"]), ("vändning", "lös fallet före datumet på lappen"))
add("You don't know any of that yet. To you, the pink paper under the coffee lid is just a bill that hasn't arrived.",
    close("car_interior", "neutral", "LATER", False))

# ---------------- LEVEL 3: THE PRICE ----------------
add("Level 3. The price.", day("LEVEL 3", "the price"), ("vändning", "nivå 3"), chapter="Level 3: The price")
add("One night you finally unfold the ticket at the kitchen counter and look up what 14 miles over actually costs.",
    sc("apartment", H(0.3, "doubt", "hold", holding="letter"), props=[TICKET("14 OVER")]), ("hot", "vad kostar 14 över?"))
add("The base fine for 1 to 15 miles per hour over the limit is 35 dollars. You almost laugh. Then you keep reading.",
    real("$35", "base fine, 1–15 mph over", SRC["glenn"]), ("vändning", "grundboten $35"))
add("In Glenn County's 2026 schedule, that 35 dollar fine becomes a total of 247 dollars once everything else is added on.",
    sc("apartment", H(0.3, "shock", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "BASE $35|TOTAL $247"}]), ("hot", "$35 blir $247"))
add("The extras have names. A 40 dollar court operations fee, a 35 dollar conviction assessment, a 30 dollar fee for the county, and state and county penalty assessments on top.",
    {"type": "board", "title": "79 IN A 65", "lines": ["base fine: $35", "court operations: $40", "conviction assessment: $35", "county TAP fee: $30", "penalty assessments: the rest"], "result": "$247 total (Glenn County 2026)"},
    ("vändning", "varför $35 blir $247"))
add("Every county adds its own penalty assessments. The same ticket in neighboring Tehama County totals 225 dollars.",
    real("$225", "same speed, same base fine, Tehama County 2026", "Tehama County Superior Court – 2026 Uniform Bail and Penalty Schedule"), ("vändning", "grannlänet: $225"))
add("And the next step up is steep. At 16 to 25 over, the base fine doubles to 70 dollars, and the Glenn County total jumps to 364.",
    real("$364", "16–25 mph over in Glenn County", SRC["glenn"]), ("hot", "en mil till: $364"))
add("You were going 79. Two more miles per hour and this exact piece of paper would cost you 117 dollars more.",
    label("+$117", "two more mph: 16 over = $364 in Glenn County"))
add("You fold it up again and put it back in the cup holder, which makes no sense, but it's where it lives now.",
    close("car_interior", "sad", "AGAIN"))

# ---------------- LEVEL 4: THE CHOICES ----------------
add("Level 4. The three doors.", day("LEVEL 4", "the three doors"), ("vändning", "nivå 4"), chapter="Level 4: The three doors")
add("Before the date on the ticket, you actually have choices. Most people only ever hear about the first one, which is just paying it.",
    {"type": "plan", "title": "BEFORE THE DATE", "items": [
        {"box": [0.04, 0.3, 0.28, 0.4], "label": "PAY IT"},
        {"box": [0.36, 0.3, 0.28, 0.4], "label": "TRAFFIC SCHOOL", "hot": True},
        {"box": [0.68, 0.3, 0.28, 0.4], "label": "FIGHT IT"}]}, ("gåta", "tre dörrar"))
add("Paying the bail counts as a conviction. And in California, a speeding conviction puts one point on your driving record.",
    real("1 POINT", "for a speeding conviction", SRC["pts"]), ("hot", "betala = dom + 1 poäng"))
add("Door two is traffic school. You can usually choose it if you haven't gone to traffic school in the last 18 months.",
    real("18 MONTHS", "since your last traffic school", SRC["ts"]), ("vändning", "trafikskola – 18 månader"))
add("You still pay the full bail, plus a 52 dollar traffic school fee to the court. In return, insurance companies can't see the point.",
    sc("dmv_office", H(0.3, "doubt", "hold", holding="letter"), props=[{"type": "summons", "x": 0.64, "title": "TRAFFIC SCHOOL", "tag": "+$52"}], note="TRAFFIC SCHOOL: FULL BAIL + $52 FEE – POINT HIDDEN FROM INSURERS"),
    ("vändning", "+$52, poängen döljs"))
add("Door three is fighting it. You can even do that on paper, with a trial by written declaration, without ever standing in front of a judge.",
    sc("apartment", H(0.3, "smirk", "hold", holding="letter"), props=[{"type": "summons", "x": 0.64, "title": "WRITTEN DECLARATION", "tag": "TR-205"}]))
add("But the state's self help page warns you that you usually have to pay the full fine when you turn in that paperwork. You get it back if you win.",
    real("PAY FIRST", "the usual rule for a trial by written declaration", SRC["twd"]), ("vändning", "kämpa = betala först"))
add("And this isn't a criminal case yet. It's an infraction. That means no jury, and no lawyer appointed for you.",
    real("NO JURY", "and no appointed lawyer for an infraction", SRC["pc196"]), ("vändning", "infraktion: ingen jury"))
add("Three doors, and every one of them is open until the date at the bottom of the pink paper. You don't pick any of them.",
    label("NO DOOR", "you wait for a letter instead"), ("hot", "du väljer ingen dörr"))
add("Dez asks you about it at lunch. You tell him you're still waiting for the reminder. He nods like that's the plan.",
    sc("loading_dock", H(0.3, "neutral"), [DEZ(0.72, say="Still waiting? Smart.")]))

# ---------------- LEVEL 5: THE DATE PASSES ----------------
add("Level 5. The date.", day("LEVEL 5", "the date"), ("hot", "nivå 5 – datumet"), chapter="Level 5: The date")
add("The date on the ticket is a Friday. You're at work, loading a truck, and you don't think about it once.",
    sc("loading_dock", H(0.4, "neutral", "push"), props=[{"type": "boxes", "x": 0.7}]), ("hot", "fredagen passerar"))
add("At 4 o'clock the clerk's window closes. Nobody calls you. Nothing beeps. The case just turns into a different kind of case.",
    sc("court_hall", note="4:00 PM – THE WINDOW CLOSES"), ("vändning", "luckan stänger – fallet byter karaktär"), silence=True)
add("Missing the date without a good reason is called a failure to appear. And it has its own price tag, separate from the ticket.",
    label("FAILURE TO APPEAR", "a new problem, stacked on the old one"), ("hot", "failure to appear"))
add("The court can add a civil assessment of up to 100 dollars. Until July 2022, that number was as high as 300.",
    real("UP TO $100", "civil assessment for missing the date (was $300 before July 1, 2022)", SRC["civ"]), ("vändning", "civil assessment upp till $100"))
add("That's the money part. The Judicial Council's own FAQ also lists what can happen to you for missing a promise to appear.",
    sc("court_hall", H(0.3, "worried", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "FAILED TO APPEAR|CASE UPDATED"}]))
add("You may be arrested and punished with up to 6 months in jail and a fine of up to 1,000 dollars, and your license may be suspended.",
    real("6 MONTHS", "jail and/or a $1,000 fine for failing to appear", SRC["jcfaq"]), ("hot", "upp till 6 mån fängelse / $1 000"))
add("All of that over a 247 dollar ticket, a pink piece of paper sitting under a coffee lid.",
    close("car_interior", "shock", "$1,000?"))
add("But you don't know any of this. Because every letter about it is going to the old apartment.",
    sc("front_door", props=[{"type": "envelope", "x": 0.5, "n": 1, "stamp": "SUPERIOR COURT"}]), ("gåta", "breven går till fel dörr"))

# ---------------- LEVEL 6: THE STACK ----------------
add("Level 6. The stack of mail.", day("LEVEL 6", "the stack of mail"), ("vändning", "nivå 6"), chapter="Level 6: The stack of mail")
add("Six weeks after the stop, Mrs. Okafor texts you a photo. It's a pile of envelopes on her hall table, held down by a jar of honey.",
    sc("apartment", H(0.3, "doubt", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "MRS. OKAFOR|PHOTO|4 LETTERS"}]), ("hot", "fotot på brevhögen"))
add("She writes, the new tenant keeps leaving these by my door. Some of them look official. I didn't open them.",
    sc("front_door", H(0.32, "worried", walk_to=0.46), [OKA(0.78, say="These look official.")], props=[{"type": "envelope", "x": 0.6, "n": 4, "stamp": "COURT · DMV"}]))
add("You drive over that night. The top envelope is the courtesy notice. It arrived weeks ago, on time, at the address you never changed.",
    sc("front_door", H(0.36, "shock", "hold", holding="letter"), [OKA(0.78)], props=[{"type": "envelope", "x": 0.6, "n": 3, "stamp": "COURTESY NOTICE"}]), ("vändning", "påminnelsen kom – till fel adress"), silence=True)
add("So Dez was right, they do mail you a reminder. It just goes to wherever the DMV thinks you live.",
    label("IT CAME", "to the address you never changed"), ("vändning", "Dez hade rätt – nästan"))
add("The second envelope is a notice that you failed to appear. The third is from the court again, with the civil assessment added on.",
    sc("front_door", H(0.36, "sad", "hold", holding="letter"), props=[{"type": "summons", "x": 0.64, "title": "FAILURE TO APPEAR", "tag": "+$100"}]))
add("The fourth one has the DMV seal on it. You open it right there in the hallway, under Mrs. Okafor's porch light.",
    sc("front_door", H(0.36, "worried", "hold", holding="letter"), [OKA(0.8)], props=[{"type": "envelope", "x": 0.6, "n": 1, "stamp": "DMV"}]), ("hot", "DMV-kuvertet"))
add("The DMV handbook says it in one line. If you get a ticket and fail to appear in court, DMV may suspend your driving privilege until you appear.",
    real("UNTIL YOU APPEAR", "DMV may suspend your driving privilege after a missed court date", SRC["rec"]), ("hot", "körkortet indraget tills du infinner dig"))
add("Your license is suspended. The date on the letter was nine days ago. You drove here tonight.",
    close("front_door", "shock", "9 DAYS"), ("hot", "du har kört i 9 dagar"), silence=True)
add("Mrs. Okafor reads your face and puts the kettle on. She doesn't say I told you. She says, sit down before you drive anywhere.",
    sc("apartment", H(0.3, "sad"), [OKA(0.74, say="Sit down first.")]), ("människor", "Mrs. Okafor sätter på tevattnet"))
add("There's one strange detail in the letter. California stopped suspending licenses just for unpaid tickets back in 2017. This one isn't about money.",
    real("AB 103 (2017)", "ended suspensions for failure to PAY – not for failure to appear", SRC["ab103"]), ("vändning", "inte pengarna – löftet"))
add("It's about the signature you gave on the side of the highway, the promise to appear, which you broke without noticing.",
    label("THE SIGNATURE", "the promise is what got you suspended"), ("gåta", "underskriften var det"))

# ---------------- LEVEL 7: THE SECOND STOP ----------------
add("Level 7. The second stop.", day("LEVEL 7", "the second stop"), ("hot", "nivå 7"), chapter="Level 7: The second stop")
add("You tell yourself you'll fix it Monday. On Saturday, you drive four blocks to the store for milk, because it's four blocks.",
    sc("city_street", H(0.3, "neutral", walk_to=0.42)), ("hot", "fyra kvarter för mjölk"))
add("Your rear tag light is out. Red and blue lights fill the mirror again, and this time your stomach knows before you do.",
    sc("city_street", H(0.3, "shock", "head"), props=[PATROL]), ("hot", "blåljusen igen"), sfx="siren")
add("A different officer this time. She runs your license, comes back, and asks you to step out of the car.",
    sc("city_street", H(0.32, "worried", walk_to=0.38), [F("Officer", "uniform", 0.72, hair="bun", say="Step out, please.")], [PATROL], note="MISSED COURT DATE: DMV MAY SUSPEND UNTIL YOU APPEAR"))
add("Driving on a suspended license is a crime, not an infraction. And the car itself is now part of the problem.",
    label("NOT AN INFRACTION", "driving while suspended is a crime"), ("vändning", "brott, inte förseelse"))
add("The highway patrol's own manual says a vehicle is subject to a 30 day impound when the driver has a suspended or revoked license.",
    real("30 DAYS", "possible impound when the driver's license is suspended", SRC["chp"]), ("hot", "30 dagars beslag"))
add("Some suspensions are treated differently, so it can happen, not that it always will. Tonight it happens.",
    sc("city_street", H(0.3, "sad"), props=[{"type": "tow_truck", "x": 0.66, "car": True}]), ("hot", "bilen bärgas"), sfx="crash")
add("You watch a tow truck winch your car onto its bed. The ticket is still in the cup holder, folded in four, riding away without you.",
    sc("city_street", H(0.28, "sad"), props=[{"type": "tow_truck", "x": 0.7, "car": True}], note="DRIVING WHILE SUSPENDED: CAR CAN BE IMPOUNDED 30 DAYS"), ("callback", "biljetten åker iväg i mugghållaren"))
add("You walk home with the milk. Four blocks feels a lot longer when you have a citation for a misdemeanor in your back pocket.",
    close("city_street", "sad", "4 BLOCKS"))
add("You call Dez. He's quiet for a long time. Then he says, I always had my mail forwarded. I didn't think to tell you that part.",
    sc("apartment", H(0.3, "sad", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "DEZ|CALLING"}]), ("vändning", "Dez hade eftersändning"))

# ---------------- LEVEL 8: THE COURTHOUSE ----------------
add("Level 8. The courthouse.", day("LEVEL 8", "the courthouse"), ("vändning", "nivå 8"), chapter="Level 8: The courthouse")
add("Monday morning you take two buses to the courthouse. You get there before the doors open and stand in a line that's already 20 people long.",
    sc("court_hall", H(0.3, "worried", walk_to=0.4), [F("", "grey", 0.6), F("", "blue", 0.7), F("", "teal", 0.8)]), ("hot", "kön är redan 20 personer"))
add("Everyone in this line has a piece of paper. California courts handled more than 3 million infraction cases in one year.",
    real("3,055,653", "infraction filings in California, fiscal year 2024–25", SRC["csr"], "CALIFORNIA COURTS"), ("vändning", "3 miljoner infraktioner per år"))
add("At the window, the clerk pulls up both cases. The speeding ticket, with the civil assessment. And the new one from Saturday night.",
    sc("court_hall", H(0.34, "worried", "hold", holding="letter"), [F("Clerk", "teal", 0.74, glasses=True, say="Two cases.")]))
add("You ask her the only question you have left. Is there any way to make this smaller?",
    close("court_hall", "worried", "SMALLER?"))
add("There is. Under California Rules of Court, rule 4.335, the court must consider your ability to pay when you ask on an infraction.",
    real("RULE 4.335", "on request, the court must consider your ability to pay", SRC["r4335"]), ("vändning", "rätten måste pröva betalningsförmåga"))
add("The court can lower the fine, give you more time, set up a payment plan, or let you do community service instead of paying.",
    sc("court_hall", H(0.34, "doubt"), [F("Clerk", "teal", 0.74, glasses=True, say="You can ask.")], note="ABILITY TO PAY: LOWER FINE · MORE TIME · PAYMENT PLAN · COMMUNITY SERVICE"), ("vändning", "fyra vägar"))
add("Many courts let you make that request online, through a program called MyCitations. You had that option the whole time, from your couch.",
    real("MyCitations", "ask to lower the ticket online", SRC["atp"]), ("gåta", "det fanns hela tiden"))
add("Today you fill out the paper version at a counter with a pen chained to it. You list your rent, your pay, and the bus pass you now need.",
    label("THE FORM", "rent, pay, and the bus pass you now need", False))
add("A few weeks later, the answer comes. To the right address this time. A payment plan, and a hearing date for the misdemeanor.",
    sc("apartment", H(0.3, "smirk", "hold", holding="letter"), props=[{"type": "envelope", "x": 0.7, "n": 1, "stamp": "NEW ADDRESS"}]), ("vändning", "rätt adress den här gången"))
add("The misdemeanor is the part you can't fix with a form. For that one, you get a lawyer, because now a lawyer can be appointed.",
    label("A LAWYER", "crimes get one, infractions don't"), ("hot", "brottet kräver advokat"))
add("Your appointed lawyer reads the file for about 40 seconds, then looks up and asks you one question. Did you change your address?",
    sc("courtroom", H(0.4, "sad"), [F("Your lawyer", "suit", 0.78, hair="short", say="Address?")]), ("gåta", "advokaten frågar om adressen"))

# ---------------- LEVEL 9: THE DMV ----------------
add("Level 9. The DMV.", day("LEVEL 9", "the DMV"), ("vändning", "nivå 9"), chapter="Level 9: The DMV")
add("Once the court reports that you appeared, the DMV can lift the suspension. But lifting it isn't free either.",
    sc("dmv_office", H(0.3, "worried", "hold", holding="letter")), ("hot", "suspensionen kostar att lyfta"))
add("The DMV charges a 55 dollar reissue fee to restore a license that was suspended. You pay it with a card that's been working very hard lately.",
    real("$55", "DMV reissue fee to restore a suspended license", SRC["reissue"]), ("vändning", "$55 för att få tillbaka körkortet"))
add("You take a number. It's G 212. The screen says G 140. A man next to you has brought a folding chair, which tells you everything.",
    sc("dmv_office", H(0.3, "doubt", "hold", holding="letter"), [F("", "grey", 0.78)], props=[{"type": "phone", "x": 0.7, "text": "NOW SERVING|G 140|YOU: G 212"}]))
add("While you wait, you finally do the thing that would have saved all of this. You change your address with the DMV on your phone, in about four minutes.",
    sc("dmv_office", H(0.3, "neutral", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "ADDRESS|UPDATED|4 MIN"}], note="MOVED? TELL DMV WITHIN 10 DAYS"), ("callback", "adressbytet på fyra minuter"))
add("Four minutes, against two cases, a tow, a 30 day impound, a bus pass, and a lawyer who asked the obvious question.",
    close("dmv_office", "sad", "4 MIN"))
add("Your car comes back from the impound lot a month later. You open the door, and the ticket is still in the cup holder, under the coffee lid.",
    sc("tow_yard", H(0.3, "doubt", walk_to=0.44), props=[{"type": "cup_holder", "x": 0.62, "ticket": True}], note="IMPOUND: UP TO 30 DAYS FOR DRIVING WHILE SUSPENDED"), ("callback", "biljetten ligger kvar"))
add("You unfold it one last time. The date at the bottom is in small print, exactly where the officer tapped it twice.",
    close("car_interior", "sad", "THE DATE"))

# ---------------- LEVEL 10: THE POINTS ----------------
add("Level 10. The record.", day("LEVEL 10", "the record"), ("vändning", "nivå 10"), chapter="Level 10: The record")
add("Because you never went to traffic school, the speeding point is on your record, where your insurance company can see it.",
    sc("apartment", H(0.3, "sad", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "RECORD|SPEEDING|1 POINT"}]), ("hot", "poängen syns för försäkringsbolaget"))
add("And the DMV handbook says traffic convictions stay on your record for 36 months or longer, depending on the type.",
    real("36 MONTHS", "or longer – how long a conviction stays on your record", SRC["rec"]), ("vändning", "36 månader"))
add("The record now counts against you in a new way. California treats a driver as a negligent operator at 4 points in 12 months, 6 in 24, or 8 in 36.",
    real("4 / 6 / 8", "points in 12 / 24 / 36 months = negligent operator", SRC["negop"]), ("hot", "4/6/8 poäng"))
add("For a negligent operator, the usual action is a one year probation that includes a six month suspension. You do that math every time you merge.",
    sc("highway", H(0.3, "worried", walk_to=0.36), note="NEGLIGENT OPERATOR: 1-YEAR PROBATION INCLUDING A 6-MONTH SUSPENSION"), ("hot", "6 månaders indragning till"))
add("So you drive differently now. You drive 64 in a 65 and let the whole highway pass you, and you don't care who honks.",
    label("64 IN A 65", "the whole highway passes you", False), ("vändning", "64 i en 65"))
add("Once, on the same stretch near Willows, a patrol car sits on the shoulder with its lights off. You recognize the man leaning against it.",
    sc("highway", H(0.3, "doubt"), [OFF(0.72)], [{"type": "patrol_car", "x": 0.7, "lights": False}]), ("människor", "Pruitt vid vägkanten"))
add("Officer Pruitt doesn't recognize you. He's probably handed out a few thousand pink copies since then. He just raises two fingers off his coffee cup.",
    sc("highway", H(0.34, "smirk"), [OFF(0.7, say="(two fingers)")], [{"type": "patrol_car", "x": 0.72, "lights": False}]), ("callback", "Pruitt lyfter två fingrar"))
add("You think of the line he said twenty times a week. Slow is cheaper. It turned out to be the most accurate thing anyone said to you all year.",
    label("SLOW IS CHEAPER", "the one piece of advice that was true", False), ("callback", "Slow is cheaper"))

# ---------------- THE CYCLE ----------------
add("The ending. Your sister Jo.", day("THE END", "your sister Jo"), ("vändning", "slutet"), chapter="The end: Your sister Jo")
add("The next spring your little sister Jo gets her first ticket. She calls you from the shoulder, still holding it, half laughing.",
    sc("highway", H(0.3, "smirk", "hold", holding="phone"), [JO(0.74, say="It's just a ticket!")], [PATROL]), ("människor", "Jo får sin första lapp"))
add("She says her friend told her not to worry, because they mail you a reminder. You tell her to read you the date at the bottom. Out loud. Right now.",
    sc("apartment", H(0.3, "neutral", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "JO|THE DATE?"}]), ("callback", "läs datumet högt"))
add("Then you make her put it in her phone calendar while you're still on the call, with two alerts, a week before and the day before.",
    label("2 ALERTS", "a week before, and the day before", False))
add("And you ask the question that nobody asked you. Is the address on your license the place you actually live?",
    close("apartment", "neutral", "ADDRESS?", False), ("callback", "adressfrågan"))
add("There's a long pause. Jo moved in August. She says, I'll do it tonight. You say, do it now, it takes four minutes.",
    sc("apartment", H(0.3, "smirk", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "JO|MOVED IN AUGUST"}]), ("vändning", "Jo flyttade i augusti"))
add("She does it while you wait. Then she sends you a photo of her ticket, unfolded, flat on her kitchen table. Not in a cup holder.",
    sc("apartment", H(0.3, "smirk", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "PHOTO|TICKET|ON THE TABLE"}]), ("callback", "inte i en mugghållare"))
add("Your own pink copy is still in your car. You never threw it out. It's in the glove box now, flat, under the registration, where you can see the date.",
    sc("car_interior", H(0.4, "smirk", "hold", holding="letter"), props=[TICKET("KEPT")]), ("callback", "din lapp ligger kvar – platt"))
add("So tell us. Is the address on your driver's license the place you actually live right now? Check it, then tell us in the comments.",
    label("YOUR ADDRESS?", "is it the one on your license?", False))

scenes = [d for d, b in S]

WPS = 2.6
t = 0.0; beats = []
for d, b in S:
    if b:
        beats.append({"t": f"{int(t // 60)}:{int(t % 60):02d}", "typ": b[0], "text": b[1]})
    t += max(len(d["say"].split()) / WPS + 0.45, 2.0)
TOTAL = t

SOURCES = [
 {"title": "CA DMV Driver's Handbook – 65 mph maximum on most highways unless posted", "url": "https://www.dmv.ca.gov/portal/handbook/california-driver-handbook/safe-driving-cont2/"},
 {"title": "Judicial Council of California – Traffic Program FAQ (signing = promise to appear; failure to appear: arrest, up to 6 months jail and/or $1,000 fine, license may be suspended; written declaration: submit bail)", "url": "https://courts.ca.gov/traffic-program-frequently-asked-questions"},
 {"title": "Glenn County Superior Court – 2026 Uniform Bail and Penalty Schedule (speeding 1–15 over: $35 base / $247 total; 16–25 over: $70 / $364)", "url": "https://www.glenn.courts.ca.gov/system/files/forms-and-filings/ubps-2026-final.pdf"},
 {"title": "Tehama County Superior Court – 2026 Uniform Bail and Penalty Schedule (1–15 over: $225 total)", "url": "https://www.tehama.courts.ca.gov/system/files/forms-and-filings/2026-ubps-final.pdf"},
 {"title": "California Courts Self-Help – Traffic (courtesy notice may take 30 days or longer)", "url": "https://selfhelp.courts.ca.gov/traffic"},
 {"title": "Santa Clara Superior Court – Traffic FAQs (no courtesy notice by the date: contact the court)", "url": "https://santaclara.courts.ca.gov/divisions/traffic-division/traffic-faqs"},
 {"title": "Sacramento Superior Court – Traffic FAQs (resolve on or before the date on your ticket)", "url": "https://www.saccourt.ca.gov/divisions/traffic/traffic-court-faqs"},
 {"title": "CA DMV Driver's Handbook – Notify DMV of a new address within 10 days", "url": "https://www.dmv.ca.gov/portal/handbook/california-driver-handbook/changing-replacing-and-renewing-your-drivers-license/"},
 {"title": "California Courts Self-Help – Traffic school (no traffic school in the last 18 months; point hidden from insurers)", "url": "https://selfhelp.courts.ca.gov/traffic/traffic-school"},
 {"title": "Calaveras Superior Court – Traffic division (bail + $52 traffic school fee; no jury trial or appointed counsel on infractions, PC 19.6)", "url": "https://calaveras.courts.ca.gov/divisions/traffic-division-other-infractions"},
 {"title": "California Courts Self-Help – Trial by written declaration (usually pay the full fine first)", "url": "https://selfhelp.courts.ca.gov/traffic/trial-declaration"},
 {"title": "CA DMV – Negligent operator (VC 12810: one point; VC 12810.5: 4/6/8 points)", "url": "https://dmv.ca.gov/portal/driver-education-and-safety/dmv-safety-guidelines-actions/negligence/"},
 {"title": "CA DMV – Negligent operator actions (one-year probation including a six-month suspension)", "url": "https://www.dmv.ca.gov/portal/driver-education-and-safety/dmv-safety-guidelines-actions/negligence/negligent-operator-actions/"},
 {"title": "CA DMV Driver's Handbook – Laws and rules of the road (FTA → DMV may suspend until you appear; convictions stay 36 months or longer)", "url": "https://www.dmv.ca.gov/portal/handbook/california-driver-handbook/laws-and-rules-of-the-road-cont2/"},
 {"title": "Riverside Superior Court – AB 199 notice (civil assessment max $300 → $100, effective July 1, 2022, PC 1214.1)", "url": "https://riverside.courts.ca.gov/system/files/public-notice_ab-199-civil-assessment.pdf"},
 {"title": "Mariposa Superior Court – AB 103 (2017): no more license suspensions for failure to pay", "url": "https://www.mariposa.courts.ca.gov/system/files/dmvftp2018.pdf"},
 {"title": "CHP Highway Patrol Manual 81.2, ch. 2 (30-day impoundment, suspended or revoked license)", "url": "https://www.chp.ca.gov/siteassets/policy/hpm/hpm-81.2/hpm-81.2-ch-2-new.pdf"},
 {"title": "California Rules of Court, rule 4.335 (ability-to-pay determinations for infractions)", "url": "https://courts.ca.gov/cms/rules/index/four/rule4_335"},
 {"title": "California Courts Self-Help – Ask to lower your fine (MyCitations)", "url": "https://selfhelp.courts.ca.gov/traffic/ask-lower-fine"},
 {"title": "CA DMV – Reissue fees ($55 to restore a suspended license)", "url": "https://dmv.ca.gov/portal/dmv-virtual-office/reissue-fees/"},
 {"title": "Judicial Council – 2026 Court Statistics Report (3,055,653 infraction filings, FY 2024–25)", "url": "https://courts.ca.gov/system/files/file/csr_2026.pdf"},
]

TITLE = "Your Life at Every Level of Ignoring a $247 Speeding Ticket"

M = {
 "channel": "Day After Court", "title": TITLE, "standard": "DAC_STANDARD", "style": "qm", "look": "stickman_day",
 "voice": "am_michael", "speed": 0.97, "lang": "en-us", "music": "calm", "music_level": 0.06,
 "beats": beats, "scenes": scenes,
 "seo": {
  "title": TITLE,
  "title_b": "What Happens If You Ignore a Speeding Ticket in California?",
  "hook": "79 in a 65, one signature on the side of the highway, and a reminder letter sent to the wrong door. This is every level of what follows in California.",
  "summary": ("You get pulled over doing 79 in a 65 in California, sign the ticket, fold it into the cup holder and wait for the reminder letter your coworker says will come. "
              "This video follows every level in time order: what your signature actually means (a promise to appear), why the $35 base fine becomes $247 in Glenn County's 2026 bail schedule "
              "($225 in Tehama County, $364 at 16–25 over), the three choices before the date on the ticket (pay and take 1 point, traffic school for the full bail plus a $52 fee if you haven't gone in 18 months, "
              "or a trial by written declaration where you usually pay first), why an infraction has no jury and no appointed lawyer, what happens on the day the date passes "
              "(failure to appear, a civil assessment of up to $100, and up to 6 months in jail and/or a $1,000 fine), why the DMV can suspend your license until you appear, "
              "the 10-day rule for changing your address, the possible 30-day impound for driving while suspended, asking the court to lower the fine under rule 4.335 or online with MyCitations, "
              "the $55 DMV reissue fee, and how points add up to a negligent operator action at 4, 6 or 8 points.\n\n"
              "Everyone in this story is made up, and so are the story's details (the 11 minutes, the dates, the queue numbers). The fines, fees and rules come from the California court, DMV and CHP pages listed below. "
              "Bail amounts differ by county and change every year."),
  "disclaimer": ("This video explains general California traffic rules for education and entertainment. It is not legal advice. Fines differ by county, and rules change. "
                 "If you have a ticket, a failure-to-appear notice or a suspension letter, contact the court on your ticket, the California DMV, a legal aid office or a licensed California attorney."),
  "keywords": ["your life at every level", "speeding ticket california", "what happens if you ignore a speeding ticket", "what happens if you don't pay a speeding ticket",
               "failure to appear traffic ticket california", "suspended license california", "traffic school california", "courtesy notice traffic ticket",
               "trial by written declaration", "mycitations", "dmv points california", "negligent operator", "speeding ticket cost"],
  "sources": SOURCES,
  "question": "Is the address on your driver's license the place you actually live right now?",
  "hashtags": ["#speedingticket", "#lawexplained", "#california"],
  "playlist": "What Really Happens After... (Every Stage, U.S. Law Explained)",
  "chapters_note": "kapitel = 'chapter'-fälten (Level 1–10 + The end)",
  "sokfras": "your life at every level",
  "sokfras_kalla": "trend/sammanfattning.md (GitHub, niche-trends 23 nov 09:25 UTC), DAC: YouTubes sökförslag för 'your life at every level' (förslag: 'your life at every level', '… of wealth', '… of fame'). TRENDANALYS.md v48: frasen VÄXER MEST (9 nya videor/9 kanaler). Webbsök 23 nov: ingen video 'Your Life at Every Level of … Speeding Ticket' hittad."
 },
 "thumb": {
  "kind": "dac3",
  "klickfraga": "Du skrev under en fortkörningslapp och väntar på påminnelsen – men den går till din gamla adress. Hur kan en lapp på 79 i en 65 sluta med att bilen bärgas?",
  "hot_i_bild": "Bärgningsbilen som lyfter hjälten bil (≈50 % av bilden) under blåljus, i förgrunden en jättelik rosa fortkörningslapp med stort '79' i rutan för hastighet; hjälten liten i helfigur med mjölkpaket i handen.",
  "skiljer_sig": "Förra DAC (crash, 21/11): korsning snett ovanifrån, krocken + telefonen 'POLICY CANCELED', siffra $11,900. Nu: kvällsgata i blåljus, hotet är bärgningsbilen + lappen (papper, inte skärm), siffran är hastigheten '79' i stället för ett belopp, och titelns belopp ($247) upprepas inte i bilden.",
  "jamfor_ark": "chk/jamfor-dac-2026-11-23.png",
  "jamfor_mot": ["-2r1E9_4Dcc (Honest Life POV, Your Life at Every Level of Living Off the Grid, 678 751)", "DAC DUI Arrest (vår bästa, 3,8 % CTR)", "DAC Sued After an Uninsured Crash (21/11)"],
  "forsta_scen_matchar": "Scen 1 (0–3 s) är motorvägen med polisbilen och blåljus bakom hjälten i helbild – samma blåljus och samma rosa lapp som i miniatyren; lappen syns i bild från scen 6–8 (≈0:20), bärgningen som miniatyr A lovar betalas av i nivå 7, och löftet ('$247 … a suspended license, and a car on a tow truck') sägs vid ~0:07.",
  "variants": [
   {"id": "A", "layout": "bärgningsbil störst, jättelapp i förgrunden, hjälten liten", "text": "79 IN A 65 (på lappen)", "label": "DAY 46",
    "scene": "kvällsgata i blåljus: bärgningsbil som lyfter hjältens bil, hjälten (grå luvtröja) liten med mjölkpaket, i förgrunden en jättelik rosa lapp med '79'"},
   {"id": "B", "layout": "split vänster/höger", "text": "DAY 1 | DAY 46", "label": None,
    "scene": "ANNAN bild: vänster = vägkant i solljus, polisen räcker fram pennan; höger = samma hjälte i en hall med en hög kuvert (COURT, DMV) under en burk honung"},
   {"id": "C", "layout": "närbild på hotet, hjälten liten", "text": "WRONG DOOR?", "label": None,
    "scene": "ANNAN bild: en jättelik dörr med en hög officiella kuvert på tröskeln, hjälten liten på trottoaren med flyttkartong (DAC får ha fråga)"}
  ]
 },
 "forbattring": {
  "forra_videon": "What Happens If You Get Sued After an Uninsured Crash? (publicerad 22/11 21:00, L2): 0 visningar, 1 exponering efter 2 h – ingen dom än (mäts 25/11). DUI Arrest (vår bästa, 3,8 % CTR, 4:50 snitt) har stannat på ~80 visningar.",
  "problem": "Krockvideon hade bra innehåll men en frågetitel utan trendformat och 14 närbilder; DUI har slutat växa och DAC behöver en ny video i exakt DUI-mallen för att få nästa våg från startsidan (VECKA_2026-48).",
  "andring": "Följer TITTARTID_REGLER FORMATORDER, raden Day After Court (DUI-formatet: vanlig händelse – en fortkörningsbot som man ignorerar – steg för steg i tidsordning, verkliga avgifter/frister med källa) + TRENDORDER (titelformatet 'Your Life at Every Level of …' med belopp i titeln). Numrerade nivåer 1–10 med dom efter varje (som DUI), trafik-ämne nära DUI-publiken, Kalifornien (största delstaten) i stället för Florida/Texas.",
  "forvantat": "CTR ≥ 3,8 % (DUI-nivån), ≥ 55 % kvar vid 0:30 och ≥ 35 % vid 2:00, snittvisning ≥ 4:30; startsidetrafik från DUI-tittarna (samma ämnesområde: trafik + körkort).",
  "referens": "Trend: 'Your Life at Every Level of Living Off the Grid' (Honest Life POV, -2r1E9_4Dcc, 678 751 visningar, 27:36, månad, +7 %/dygn) + 'How Getting Arrested on a Cruise Ship Destroys Your Life at Every Level' (Miles Unnoticed, uKBrXDWCWlw, 11 694, vecka). Egen: DAC DUI Arrest (3,8 % CTR, 4:50 snitt). DAC_STANDARD: Baldy POV DqyGPrK3LGQ. Transkript kunde inte hämtas: ingen Chrome i molnkörningen (youtube-transcriber kräver den) och vidIQ-transkript användes inte (krediter sparas). Krokstruktur 0/5/10/20/30 s ur DAC_STANDARD 2 (Baldy): 0 s nivån direkt, ~5 s sinnesdetaljer, ~10 s 'everyone starts here', ~20 s insatsen med pris, ~30 s insiderdetalj.",
  "vi_slår_den_med": "Hotet i första bilden (blåljus, 79 i en 65) i stället för en lugn öppning, löftet med verklig siffra vid 0:07 ($247 → indraget körkort → bärgad bil), en verklig regel med källa på skärmen minst var 30:e s (20 öppnade källor: DMV, Judicial Council, länens bötesscheman 2026, CHP, Rules of Court), och en gåta som alla kan råka ut för (påminnelsen går till den gamla adressen) som löses av en verklig 10-dagarsregel.",
  "trend": {
   "fras": "your life at every level",
   "kalla": "GitHub trend/sammanfattning.md 23 nov 09:25 UTC (TREND_2026-11-23.md kunde inte sparas i projektet – fullt) + TRENDANALYS.md v48",
   "trendvideo": "Your Life at Every Level of Living Off the Grid – Honest Life POV – 678 751 visningar – månad (+7 %/dygn); veckan: Your Life at Every Level as a Rancher (Mateo POV Boy, 17 165), … of Financing a $71,850 Backyard Pool (Mr.Beanie, 17 021), Getting Arrested on a Cruise Ship … at Every Level (Miles Unnoticed, 11 694)",
   "andrat": "Titelformatet 'Your Life at Every Level of …' + belopp i titeln (som '$71,850 Backyard Pool', '$650 a Month'); innehållet = DUI-mallen enligt TRENDORDER 5."
  }
 },
 "experiment": {"variable": "trendtiteln 'Your Life at Every Level of …' med belopp på DUI-mallen", "metric": "CTR mot DAC-snittet 3,8 %, 0:30-andel, snittvisning", "decide_at": "48 h (25–26/11)"},
 "hooks_kandidater": {
  "A_vald": "79 in a 65. Red and blue lights fill your mirror, 11 minutes before your shift starts. (bild = blåljusen direkt, siffror, funkar utan ljud; mekanism: stakes + specificity)",
  "B": "A reminder letter with your name on it is already going to the wrong door. (curiosity gap – men första bilden blir ett kuvert, inte hotet)",
  "C": "One signature on the side of a highway costs you 247 dollars, your license and your car. (stakes – för mycket av slutet direkt)",
  "val": "A – hotet i bildruta 0 (TITTARTID_REGLER 1); C:s löfte läggs som scen 3 och B:s gåta planteras i nivå 2 och löses i nivå 6."
 },
 "standard_check": {
  "miniatyr": "DAC_STANDARD 6 + MINIATYR_REGLER: hotet (bärgningsbilen + jättelappen) störst, hjälten liten i helfigur, kväll i blåljus men ljus (ej mörk), 'DAY 46' som etikett; B split DAY 1 | DAY 46, C fråga 'WRONG DOOR?'; titelns $247 upprepas inte i bilden.",
  "krok": "situationen direkt (79 i en 65, blåljus, 11 minuter), insats med siffra ($247, körkort, bil) vid ~0:07, slutlöfte före 0:20, insidersanning (signaturen är ett löfte, påminnelsen är inte fristen), gåta (rådet 'wait for the letter').",
  "nivåer": "10 numrerade nivåer (The stop → The record) + slutet; varje nivå: första ögonblick → svåraste → verklig regel med källa (CALIFORNIA RULE-kort) → insidersanning → känsloslag → övergång.",
  "motiv": "lappen i mugghållaren (nivå 1, 2, 3, 7, 9, slutet i handskfacket – platt), Pruitts 'Slow is cheaper' (nivå 1, 10), Dez 'Wait for the letter' (nivå 1, 4, 6, 7), adressen/Mrs. Okafor (nivå 2, 6, 8, 9, slutet), de fyra minuterna (nivå 9, slutet).",
  "slut": "cykeln: lillasyster Jo får sin första lapp – samma 'they mail you a reminder' – du låter henne läsa datumet högt och byta adress på fyra minuter; fäst fråga till tittaren om adressen på körkortet.",
  "källor": "21 källor i beskrivningen (DMV ×5, Judicial Council ×2, länsdomstolar ×7, CHP, Rules of Court, Court Statistics Report); källrad på varje regelkort.",
  "miljöer": "highway (ny), car_interior (ny), loading_dock (ny), front_door, apartment, court_hall, courtroom, dmv_office, city_street, tow_yard.",
  "tittartid": "första 30 s bara helbild/kort (ingen medium, ingen närbild), ingen presentation de första 12 s, byte var ~5 s, löftet i klartext vid ~0:07, slutlöfte före 0:20.",
  "innehall": {}
 },
 "notes": {
  "påhittat": "alla personer (du, Officer Pruitt, Dez, Mrs. Okafor, Jo, den andra polisen, expediten, advokaten), 11 minuter, 6 minuter sen, dag 11/46, 'six weeks', fredagen, kö 20 personer, G 212/G 140, 40 sekunder, fyra minuter (adressbytet), honungsburken, 'Willows' som plats i Glenn County.",
  "uträkningar": "79 − 65 = 14 över → nivån 1–15 ($247 Glenn 2026); 16–25 över = $364; $364 − $247 = $117. Glenn-summan innehåller $40 court operations, $35 conviction assessment, $30 TAP (resten = straffavgifter).",
  "osäkert": "Lagtexten på leginfo.legislature.ca.gov kunde inte öppnas (blockerad) – reglerna citeras från DMV-, domstols- och CHP-sidor, inte paragraftexten. 'Driving while suspended is a crime' (VC 14601.1) är inte citerat ur lagtext – videon säger bara 'a crime, not an infraction' och 'a citation for a misdemeanor'; straffet för 14601.1 nämns inte. Avbetalningsplanen och advokaten i nivå 8 är berättelse, inte ett utfall som lagen lovar. 30-dagarsbeslaget: CHP-manualen undantar vissa suspensionstyper – därför 'can happen, not that it always will'. MyCitations finns i många men inte alla domstolar ('Many courts').",
  "motor": "Nytt att bygga i huvudchatten (fallback inom parentes): platsen 'highway' – ljus Sacramento Valley-motorväg, 65-skylt, vägkant, fält (fallback city_street); rekvisitan 'patrol_car' med fältet lights true/false – blåljus (MÅSTE finnas för scen 1 och miniatyr A; fallback: ingen); 'car_interior' – förarplats, mugghållare (fallback apartment); rekvisitan 'cup_holder' med 'ticket': true (rosa vikt lapp under ett kaffelock); 'loading_dock' (lastkaj, fallback city_street); 'tow_truck' med 'car': true (finns kanske i tow_yard-modulen från 21/11; fallback: ingen); 'boxes'; hero 'holding': 'box'; outfit green/pink/teal finns. sfx siren/crash från 21/11."
 }
}

# innehållsmått
wl = [len(s["say"].split()) for s in scenes]
t = 0.0; facts_t = []
for s in scenes:
    v = s["visual"]
    if v.get("type") in ("real", "label", "board", "plan") or v.get("note_card") or v.get("type") == "scene" and any(p.get("type") in ("phone", "summons", "envelope") for p in v.get("props", [])):
        facts_t.append(t)
    t += max(len(s["say"].split()) / WPS + 0.45, 2.0)
gaps = [b - a for a, b in zip(facts_t, facts_t[1:])] + [TOTAL - facts_t[-1]]
M["standard_check"]["innehall"] = {
 "snittord_per_say": round(sum(wl) / len(wl), 1),
 "say_under_6_ord": sum(1 for n in wl if n < 6),
 "faktaskyltar": len(facts_t),
 "verkliga_regelkort": sum(1 for s in scenes if s["visual"].get("type") == "real"),
 "storsta_lucka_s": round(max(gaps), 1),
 "kommentar": f"≈{TOTAL/60:.1f} min ({sum(wl)} ord, 2,6 ord/s + 0,45 s/scen). Faktaskylt = real/label/board/plan, note_card eller föremål med siffra (telefon/lapp/kuvert). Korta repliker = nivåkorten ('Level 2. The cup holder.') – ett per nivå."
}
json.dump(M, open("/home/claude/w/manus/dac-2026-11-23.json", "w"), ensure_ascii=False, indent=1)
print(len(scenes), sum(wl), round(TOTAL / 60, 1), len(beats), M["standard_check"]["innehall"], len(TITLE))
