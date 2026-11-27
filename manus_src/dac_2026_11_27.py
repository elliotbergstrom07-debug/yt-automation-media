import json
WPS = 2.6
sc = []
def H(x=0.3, expr="neutral", arms="down", walk=None, hold=None):
    h = {"x": x, "expr": expr, "arms": arms}
    if walk is not None: h["walk_to"] = walk
    if hold: h["holding"] = hold
    return h
def F(name, x, outfit, say=None, walk=None, **kw):
    f = {"x": x, "outfit": outfit, "name": name}
    if walk is not None: f["walk_to"] = walk
    if say: f["say"] = say
    f.update(kw); return f
def S(say, loc, hero, props=None, friends=None, note=None, b=None, **kw):
    v = {"type": "scene", "location": loc, "shot": "wide", "hero": hero}
    if props: v["props"] = props
    if friends: v["friends"] = friends
    if note: v["note_card"] = {"text": note}
    d = {"say": say, "visual": v}
    d.update(kw); d["_b"] = b; sc.append(d)
def V(say, visual, b=None, **kw):
    d = {"say": say, "visual": visual}; d.update(kw); d["_b"] = b; sc.append(d)
def real(head, big, text, src): return {"type": "real", "head": head, "big": big, "text": text, "source": src}
def label(big, text, src, bad=False): return {"type": "label", "big": big, "text": text, "source": src, "bad": bad}
def close(loc, expr, thought): return {"type": "closeup", "location": loc, "expr": expr, "look": -1, "thought": thought, "bad": True}
def card(n, sub): return {"type": "daycard", "label": "LEVEL " + n, "sub": sub}

JULES = dict(hair="curly"); DEV = dict(hair="short", glasses=True)
CP = "IRS, Understanding your CP2000 notice"
T652 = "IRS Tax Topic 652 (CP2000)"
ENV = {"type": "envelope", "x": 0.5, "text": "INTERNAL REVENUE SERVICE|CP2000|$6,420"}

# ---------- KROK (0–60 s) ----------
S("An IRS letter on your counter says you owe 6,420 dollars, within 30 days.",
  "apt_kitchen", H(0.26, "shock", "hold", 0.34, "letter"), [ENV, {"type": "fridge", "x": 0.82, "whiteboard": "RENT: JULES PAID DEV PAID", "shoebox": "TAXES?"}],
  b=("hot", "IRS-kuvertet: $6 420, 30 dagar"), chapter="Level 1: The envelope", sfx="paper")
S("That clock has been running for a week already.",
  "apt_kitchen", H(0.3, "worried", "hold", 0.4, "letter"), [{"type": "letter", "x": 0.56, "title": "CP2000", "tag": "RESPOND BY AUG 8"}],
  b=("hot", "klockan går redan"))
S("Your roommate Jules walks in with groceries, sees the logo, and drops a lemon.",
  "apt_kitchen", H(0.3, "shock", "hold", 0.34, "letter"), friends=[F("Jules", 0.8, "yellow", "Is that the IRS?", walk=0.62, **JULES)],
  b=("människor", "Jules ser loggan"), sfx="click")
S("This is your life at every level of an IRS letter.",
  "apt_kitchen", H(0.32, "worried", "hold", 0.3, "letter"), friends=[F("Jules", 0.66, "yellow", walk=0.6, **JULES)],
  note="IRS: A CP2000 ISN'T A BILL. IT'S A PROPOSAL.", b=("hot", "löftet: varje nivå"))
S("By the end, you'll know who paid you 21,400 dollars last year.",
  "apt_kitchen", H(0.3, "doubt", "point", 0.4, "letter"), [{"type": "letter", "x": 0.58, "title": "PAYMENT APP INC.", "tag": "$21,400"}],
  b=("gåta", "gåtan: vem betalade dig $21 400?"))
S("The letter says somebody did, and you have no idea who.",
  "apt_kitchen", H(0.3, "doubt", "hold", 0.38, "letter"), [{"type": "letter", "x": 0.58, "title": "FORM 1099-K", "tag": "$21,400"}],
  b=("gåta", "ingen aning vem"))
S("On the fridge, the rent board still shows two check marks in green marker, one for Jules and one for Dev.",
  "apt_kitchen", H(0.28, "doubt", "down", 0.4), [{"type": "fridge", "x": 0.66, "whiteboard": "RENT: JULES PAID DEV PAID", "shoebox": "TAXES?"}],
  b=("gåta", "hyrestavlan med två bockar"))
S("You shoot weddings on weekends, and you reported every client you could remember. 21,400 dollars is not a number you remember.",
  "apt_kitchen", H(0.3, "worried", "hold", 0.36, "letter"), [{"type": "camera_bag", "x": 0.58}],
  note="IRS TOPIC 652: RESPOND WITHIN 30 DAYS OF THE NOTICE", b=("hot", "du minns inte $21 400"))
V("The IRS has a name for this letter. A CP2000 isn't a bill, it's a proposal to adjust your income, payments, credits or deductions.",
  real("U.S. GOVERNMENT", "NOT A BILL", "a CP2000 is a proposal to adjust your return", T652), b=("vändning", "CP2000 är inte en räkning"))
V("Level one. The envelope.", card("ONE", "the envelope"), b=("hot", "nivåkort 1"))
V("It exists because someone else sent the IRS a number. A bank, an app or a client reported something that doesn't match your return.",
  real("U.S. GOVERNMENT", "MISMATCH", "third-party information doesn't match your return", CP), b=("vändning", "tredjepartsuppgifter matchar inte"))
S("The page lists it plainly. Payment Apps Incorporated, Form 1099-K, 21,400 dollars, and next to it, the words not reported.",
  "apt_kitchen", H(0.3, "shock", "hold", hold="letter"), [{"type": "letter", "x": 0.56, "title": "FORM 1099-K", "tag": "NOT REPORTED"}],
  note="IRS: THIRD-PARTY INFO DIDN'T MATCH YOUR RETURN", b=("hot", "1099-K: ej redovisat"))
V("A 1099-K is a report of payments you received for goods or services, through cards, payment apps or online marketplaces.",
  real("U.S. GOVERNMENT", "FORM 1099-K", "payments received for goods or services", "IRS, Understanding your Form 1099-K"), b=("vändning", "vad 1099-K rapporterar"))
V("And the app only had to send one if your goods and services payments went over 20,000 dollars, in more than 200 transactions.",
  label("$20,000 + 200", "payments for goods or services before a 1099-K is required", "IRS, Understanding your Form 1099-K"), b=("gåta", "200 betalningar – vilka?"))
S("You didn't have 200 clients. You had 11 weddings and one dog's birthday party, and you have the photos to prove it.",
  "apt_kitchen", H(0.3, "doubt", "point"), [{"type": "laptop", "x": 0.56, "text": "CLIENTS 2025|12"}],
  b=("gåta", "11 bröllop, inte 200 kunder"))
# ---------- NIVÅ 2 ----------
V("Level two. The math.", card("TWO", "the math"), chapter="Level 2: The math", b=("hot", "nivåkort 2"))
S("Page three is where your stomach drops. The proposed tax is 5,350 dollars, and below it sits a second line called a penalty.",
  "apt_kitchen", H(0.3, "shock", "hold", hold="letter"), [{"type": "letter", "x": 0.58, "title": "PROPOSED TAX $5,350", "tag": "PENALTY $1,070"}],
  b=("hot", "skatt $5 350 + straffavgift"))
V("That penalty has a fixed size. The accuracy-related penalty is 20 percent of the part of the underpayment it applies to.",
  real("U.S. LAW", "20%", "accuracy-related penalty on the underpayment", "26 U.S.C. 6662(a)"), b=("hot", "20 % straffavgift"))
V("For individuals, one trigger is called a substantial understatement. You came up short by more than 10 percent of the correct tax or 5,000 dollars, whichever is greater.",
  real("U.S. LAW", "$5,000", "or 10% of the correct tax, whichever is greater", "26 U.S.C. 6662(d)(1)(A)"), b=("vändning", "gränsen $5 000"))
S("Your proposed shortfall is 5,350 dollars. That's 350 dollars over the line, which is why the 1,070 dollar penalty is on the page.",
  "apt_kitchen", H(0.3, "sad", "hold", hold="letter"), [{"type": "letter", "x": 0.56, "title": "$5,350 > $5,000", "tag": "PENALTY 20%"}],
  note="26 U.S.C. 6662(d): MORE THAN $5,000 OR 10% = SUBSTANTIAL", b=("hot", "$350 över gränsen"))
V("Then there's interest. For individuals, the IRS rate on underpayments in late 2026 is 7 percent a year, compounded daily.",
  real("U.S. GOVERNMENT", "7%", "a year on underpayments, compounded daily (Q4 2026)", "IRS news release IR-2026-98"), b=("hot", "7 % ränta per dag"))
V("Add it up and the letter proposes 6,420 dollars before interest. It's more than you made from all 11 weddings combined.",
  {"type": "board", "title": "THE PROPOSAL", "lines": ["proposed tax: $5,350", "accuracy penalty, 20%: $1,070", "interest: 7% a year, daily"], "result": "$6,420 + interest"},
  b=("hot", "$6 420 – mer än alla bröllop"))
S("Dev comes home, reads it over your shoulder, and says the only thing anyone says. Just don't open the next one.",
  "apt_kitchen", H(0.28, "worried", "hold", hold="letter"), friends=[F("Dev", 0.7, "green", "Don't open the next one.", walk=0.6, **DEV)],
  b=("människor", "Dev: öppna inte nästa"))
# ---------- NIVÅ 3 ----------
V("Level three. The shoebox.", card("THREE", "the shoebox"), chapter="Level 3: The shoebox", b=("hot", "nivåkort 3"))
S("You fold the letter in thirds and put it in the shoebox on top of the fridge. The one that says taxes, with a question mark.",
  "apt_kitchen", H(0.36, "sad", "reach", 0.6, "letter"), [{"type": "fridge", "x": 0.68, "shoebox": "TAXES?", "whiteboard": "RENT: JULES PAID DEV PAID"}],
  b=("hot", "brevet i skokartongen"), silence=True)
V("The IRS spells out what it expects. Respond within 30 days of the date on the notice, or 60 days if you live outside the United States.",
  real("U.S. GOVERNMENT", "30 DAYS", "to respond to a CP2000 (60 if outside the U.S.)", T652), b=("hot", "30 dagar (60 utomlands)"))
V("You could have asked for more time. The IRS page on the CP2000 says you can send an extension request with the reply form.",
  label("MORE TIME", "an extension request can go in with the reply", CP), b=("vändning", "man kan be om mer tid"))
S("Instead you shoot two weddings in a row in August. At the second one, the bride's uncle asks what you do for taxes, as a joke.",
  "wedding_barn", H(0.3, "smirk", "hold", 0.4, "camera"), friends=[F("Uncle", 0.72, "suit", "Cash only, right?", walk=0.6, hair="gray")],
  note="IRS: RESPOND WITHIN 30 DAYS OF THE NOTICE DATE", b=("hot", "farbroderns skämt"))
S("You laugh along. The response date on the letter in the shoebox passes on a Saturday while you're editing photos at 1 in the morning.",
  "desk_room", H(0.4, "neutral", "down"), [{"type": "laptop", "x": 0.6, "text": "EXPORT 412 PHOTOS"}, {"type": "wall_calendar", "x": 0.82, "text": "AUG 8"}],
  b=("hot", "svarsdatumet passerar"))
V("The IRS says what comes next, too. If it doesn't hear from you by the response date, it sends a Statutory Notice of Deficiency.",
  real("U.S. GOVERNMENT", "NEXT STEP", "no reply by the date, then a Statutory Notice of Deficiency", T652), b=("hot", "nästa: deficiency notice"))
V("That notice can't arrive in an ordinary envelope. The law says the IRS may send it by certified or registered mail.",
  label("CERTIFIED MAIL", "how a notice of deficiency is sent", "26 U.S.C. 6212(a)", True), b=("hot", "rekommenderat brev"))
# ---------- NIVÅ 4 ----------
V("Level four. The signature.", card("FOUR", "the signature"), chapter="Level 4: The signature", b=("hot", "nivåkort 4"))
S("In October, the mail carrier rings instead of leaving it. She holds out a small screen and a stylus for your signature.",
  "front_stoop", H(0.3, "worried", "down", 0.42), friends=[F("Rosa", 0.74, "blue", "Sign here, please.", walk=0.6, hair="bun", cap=True)],
  b=("hot", "brevbäraren ringer på"), sfx="click")
S("The envelope is thicker. The first line in bold says Notice of Deficiency, and the next page has a date on it, 90 days away.",
  "front_stoop", H(0.3, "shock", "hold", hold="letter"), [{"type": "letter", "x": 0.56, "title": "NOTICE OF DEFICIENCY", "tag": "90 DAYS"}],
  b=("hot", "90-dagarsbrevet"))
V("The number is real. Within 90 days after the notice is mailed, or 150 if it's addressed outside the United States, you can petition the Tax Court.",
  real("U.S. LAW", "90 DAYS", "to petition the Tax Court (150 if addressed abroad)", "26 U.S.C. 6213(a)"), b=("hot", "90 dagar till Tax Court"))
V("And this clock is harder than the first one. The court's own guidance says that by law, it can't extend the time to file a petition.",
  label("NO EXTENSIONS", "the Tax Court cannot extend the petition deadline", "U.S. Tax Court, Starting a Case", True), b=("hot", "ingen förlängning"), silence=True)
S("You count it on the wall calendar with a pencil. Day 90 lands on a Tuesday in January, three days after Dev's birthday.",
  "desk_room", H(0.36, "worried", "point", 0.5), [{"type": "wall_calendar", "x": 0.7, "text": "JAN|DAY 90"}],
  note="26 U.S.C. 6213(a): 90 DAYS FROM THE MAILING DATE", b=("hot", "dag 90 i januari"))
S("You take the shoebox down for the first time and pour it out on the table. Receipts, two old W-2s and the CP2000, still folded in thirds.",
  "apt_kitchen", H(0.3, "worried", "hold", 0.4), [{"type": "shoebox", "x": 0.56, "text": "TAXES?", "open": True}],
  note="26 U.S.C. 6212: SENT BY CERTIFIED OR REGISTERED MAIL", b=("vändning", "skokartongen töms"), sfx="paper")
V("You read both letters side by side. For the first time you see it, the same 21,400 dollars and the same payer on each.",
  close("apt_kitchen", "doubt", "WHO PAID ME?"), b=("gåta", "samma betalare på båda"))
# ---------- NIVÅ 5 ----------
V("Level five. The court nobody mentions.", card("FIVE", "the court nobody mentions"), chapter="Level 5: The Tax Court", b=("hot", "nivåkort 5"))
S("A coworker from your old job, Theresa, used to do bookkeeping. On the phone she says two words you've never heard together. Tax Court.",
  "desk_room", H(0.36, "doubt", "hold", hold="phone"), [{"type": "phone", "x": 0.56, "text": "THERESA|CALLING"}],
  b=("människor", "Theresa: Tax Court"))
V("The Tax Court describes itself as an independent judicial forum, and says it is not controlled by or connected with the IRS.",
  real("U.S. TAX COURT", "INDEPENDENT", "not controlled by or connected with the IRS", "U.S. Tax Court, About the Court"), b=("vändning", "domstolen är oberoende"))
V("Filing a petition costs 60 dollars, and the court may waive that fee if you show you can't pay it.",
  real("U.S. TAX COURT", "$60", "filing fee for a petition (can be waived)", "U.S. Tax Court, Fees and Charges"), b=("vändning", "$60 i avgift"))
V("There's a simpler track for disputes of 50,000 dollars or less for any one year. The court calls them small tax cases, or S cases.",
  real("U.S. TAX COURT", "$50,000", "or less per year: the small tax case option", "U.S. Tax Court, Case Procedure"), b=("vändning", "S case under $50 000"))
V("It comes with a trade. Decisions entered under the small tax case procedures are not appealable. You get one shot, not two.",
  label("NO APPEAL", "small tax case decisions are not appealable", "U.S. Tax Court, About the Court", True), b=("hot", "ingen överklagan"))
S("Theresa reads the court's website out loud while you type. Its judges hold trials in 79 cities, and one of them is 20 minutes from your apartment.",
  "desk_room", H(0.36, "neutral", "hold", hold="phone"), [{"type": "laptop", "x": 0.58, "text": "TRIAL CITIES|79"}],
  note="U.S. TAX COURT: TRIALS IN 79 U.S. CITIES", b=("vändning", "79 städer, en nära"))
S("You fill in the petition at the post office counter, pay with a money order, and ask for a receipt with the date on it.",
  "post_office", H(0.3, "neutral", "hold", 0.4, "letter"), [{"type": "receipt", "x": 0.56, "text": "MONEY ORDER $60|DEC 2"}],
  friends=[F("Clerk", 0.8, "navy", "Certified?", hair="short")], b=("lösning", "petitionen skickas"))
S("It's day 52 of 90. The clerk stamps it, and you realize this is the first IRS deadline in five months you didn't let pass.",
  "post_office", H(0.32, "smirk", "down", 0.46), [{"type": "stamp", "x": 0.6, "text": "DAY 52"}],
  note="U.S. TAX COURT: FILING FEE $60, MAY BE WAIVED", b=("vändning", "dag 52 av 90"))
# ---------- NIVÅ 6 ----------
V("Level six. The app.", card("SIX", "the app"), chapter="Level 6: The app", b=("gåta", "nivåkort 6"))
S("Back home, you download a full year of history from the payment app. It's a spreadsheet with 214 rows, and most of them aren't clients.",
  "desk_room", H(0.36, "doubt", "down"), [{"type": "laptop", "x": 0.58, "text": "HISTORY 2025|214 ROWS"}],
  b=("gåta", "214 rader – mest inte kunder"))
S("They're Jules. Rent, every month. Half the power bill. Pizza. Concert tickets. All of it marked goods and services.",
  "desk_room", H(0.36, "shock", "point"), [{"type": "laptop", "x": 0.58, "text": "JULES → YOU|GOODS & SERVICES"}],
  b=("vändning", "gåtan löst: Jules betalningar"), silence=True)
S("You call her into the room. She looks at the screen and covers her mouth. She's been pressing the wrong button since the day she moved in.",
  "desk_room", H(0.3, "doubt", "point"), friends=[F("Jules", 0.7, "yellow", "That's the default!", walk=0.6, **JULES)],
  note="IRS: A 1099-K REPORTS PAYMENTS FOR GOODS OR SERVICES", b=("människor", "Jules har tryckt fel i ett år"))
V("The IRS has a line for exactly this. Getting repaid by a roommate for rent or a household bill is a personal payment, and these payments aren't taxable income.",
  real("U.S. GOVERNMENT", "NOT INCOME", "a roommate repaying rent or a household bill", "IRS, Understanding your Form 1099-K"), b=("vändning", "hyra från rumskamrat = inte inkomst"))
V("The IRS also says payments to friends and family for gifts and reimbursements should not be reported on a Form 1099-K at all.",
  label("SHOULDN'T BE THERE", "gifts and reimbursements don't belong on a 1099-K", "IRS, Form 1099-K FAQs (A3)"), b=("vändning", "borde inte ens rapporterats"))
S("Then you sort the column by name, and the good news gets smaller. 3,900 dollars came from real clients who paid through the same app.",
  "desk_room", H(0.36, "sad", "down"), [{"type": "laptop", "x": 0.58, "text": "CLIENTS|$3,900"}],
  note="IRS: ROOMMATE REPAYING RENT = PERSONAL, NOT TAXABLE", b=("hot", "men $3 900 var riktiga kunder"))
S("You never reported those. You had them in your head as tips, because they came in the week after each wedding, through your phone.",
  "desk_room", H(0.36, "sad", "down"), [{"type": "phone", "x": 0.58, "text": "+$350|THANK YOU!!"}],
  b=("hot", "du räknade dem som dricks"))
V("So the letter was wrong about 17,500 dollars and right about 3,900, and you're the only person in the building who knows which is which.",
  {"type": "board", "title": "THE $21,400", "lines": ["Jules: rent, bills, pizza: $17,500", "real wedding clients: $3,900"], "result": "only $3,900 is income"},
  b=("vändning", "$17 500 fel, $3 900 rätt"))
# ---------- NIVÅ 7 ----------
V("Level seven. The other side.", card("SEVEN", "the other side"), chapter="Level 7: The other side", b=("hot", "nivåkort 7"))
S("In February, a letter comes from the IRS Office of Chief Counsel. An attorney named Mr. Abara asks for a call about your case.",
  "desk_room", H(0.36, "worried", "hold", hold="letter"), [{"type": "letter", "x": 0.58, "title": "OFFICE OF CHIEF COUNSEL", "tag": "DOCKET NO. 0412-S"}],
  b=("hot", "IRS:s jurist hör av sig"))
V("That call is normal. The court's own page says most cases are settled by mutual agreement without trial.",
  real("U.S. TAX COURT", "MOST SETTLE", "by mutual agreement, without a trial", "U.S. Tax Court, About the Court"), b=("vändning", "de flesta förlikas"))
S("You put him on speaker at the kitchen table. Jules sits next to you with her phone open to the app, in case he asks.",
  "apt_kitchen", H(0.3, "worried", "hold", hold="phone"), [{"type": "phone", "x": 0.5, "text": "SPEAKER|IRS COUNSEL"}],
  friends=[F("Jules", 0.72, "yellow", **JULES)], b=("människor", "samtalet på högtalare"))
S("He asks one question three different ways. Can you show the 17,500 dollars was rent and bills, and not photography?",
  "apt_kitchen", H(0.3, "doubt", "hold", hold="phone"), [{"type": "phone", "x": 0.5, "text": "CAN YOU SHOW IT?"}],
  note="U.S. TAX COURT: MOST CASES SETTLE WITHOUT TRIAL", b=("hot", "kan du visa det?"))
S("You email him the lease with three names on it, the power bills split in thirds, and 12 rent payments that match to the dollar.",
  "desk_room", H(0.36, "neutral", "point"), [{"type": "laptop", "x": 0.58, "text": "LEASE|3 NAMES|12 × $800"}],
  b=("lösning", "hyreskontraktet + 12 betalningar"))
S("Then you send the 3,900 too, with the wedding dates next to each payment. Theresa told you a number you hide is the one they find.",
  "desk_room", H(0.36, "sad", "point"), [{"type": "laptop", "x": 0.58, "text": "CLIENTS|$3,900|SENT"}],
  note="U.S. TAX COURT: INDEPENDENT OF THE IRS", b=("vändning", "du redovisar även $3 900"))
V("For eleven days, nothing comes back. You check your email in the bathroom at a wedding and miss the first kiss.",
  close("wedding_barn", "worried", "11 DAYS"), b=("hot", "11 dagars tystnad"))
# ---------- NIVÅ 8 ----------
V("Level eight. The new number.", card("EIGHT", "the new number"), chapter="Level 8: The new number", b=("hot", "nivåkort 8"))
S("The answer arrives as a stipulated decision, a form you both sign. The 17,500 dollars is gone. The tax on the 3,900 is 1,170 dollars.",
  "apt_kitchen", H(0.3, "smirk", "hold", 0.36, "letter"), [{"type": "letter", "x": 0.58, "title": "STIPULATED DECISION", "tag": "$1,170"}],
  b=("vändning", "nya beloppet: $1 170"))
S("The penalty line says zero. You read it three times before you understand why, and it's the same rule that put it there.",
  "apt_kitchen", H(0.3, "doubt", "hold", hold="letter"), [{"type": "letter", "x": 0.58, "title": "PENALTY", "tag": "$0"}],
  b=("gåta", "straffavgiften är noll – varför?"))
V("A substantial understatement for an individual has to exceed the greater of 5,000 dollars or 10 percent of the correct tax. 1,170 dollars doesn't come close.",
  real("U.S. LAW", "UNDER THE LINE", "$1,170 is below the $5,000 floor", "26 U.S.C. 6662(d)(1)(A)"), b=("vändning", "under $5 000-gränsen"))
V("The interest doesn't go away. On what you really owed, it keeps running at 7 percent a year, compounded daily.",
  label("STILL RUNNING", "interest on what you really owed, 7% a year, daily", "IRS news release IR-2026-98", True), b=("hot", "räntan löper ändå"))
S("Dev reads the decision and asks why you're not celebrating. You say you are. You just don't have 1,170 dollars this month.",
  "apt_kitchen", H(0.3, "sad", "down"), friends=[F("Dev", 0.7, "green", "So we won?", walk=0.62, **DEV)],
  note="26 U.S.C. 6662(d): $5,000 OR 10% LINE NOT CROSSED", b=("hot", "du har inte $1 170"))
S("A month later, the bill comes. It's a plain envelope this time, and the amount due is 1,170 dollars plus the interest, counted to the day.",
  "front_stoop", H(0.3, "worried", "hold", 0.4, "letter"), [{"type": "letter", "x": 0.58, "title": "AMOUNT DUE", "tag": "$1,170 + INTEREST"}],
  b=("hot", "räkningen kommer"))
V("Once it's a bill, a second penalty can start. Failure to pay is half a percent of the unpaid tax for each month or part of a month.",
  real("U.S. GOVERNMENT", "0.5%", "a month for failure to pay, up to 25%", "IRS, Failure to pay penalty"), b=("hot", "0,5 % per månad"))
V("It stops growing at 25 percent of the unpaid tax. On 1,170 dollars, that ceiling is 292 dollars and 50 cents.",
  label("25% CAP", "on 1,170 dollars, the most it can reach is $292.50", "26 U.S.C. 6651(a)(2)"), b=("vändning", "taket 25 %"))
# ---------- NIVÅ 9 ----------
V("Level nine. The plan.", card("NINE", "the plan"), chapter="Level 9: The plan", b=("hot", "nivåkort 9"))
S("You open the IRS payment page at the kitchen table, next to the empty shoebox. It has two kinds of plans, and the prices are printed.",
  "apt_kitchen", H(0.3, "neutral", "hold", hold="phone"), [{"type": "laptop", "x": 0.58, "text": "PAYMENT PLANS"}, {"type": "shoebox", "x": 0.82, "text": "TAXES?"}],
  b=("vändning", "betalningssidan"))
V("A short-term plan, 180 days or less, has a zero dollar setup fee when an individual applies online.",
  real("U.S. GOVERNMENT", "$0", "setup fee, short-term plan of 180 days or less", "IRS, Payment plans"), b=("vändning", "kort plan: $0"))
V("A long-term plan costs more to start. Online with direct debit it's 29 dollars. Online with other payments, 69. By phone or mail, 107 or 178.",
  {"type": "board", "title": "LONG-TERM PLAN SETUP", "lines": ["online, direct debit: $29", "online, other payment: $69", "phone or mail, direct debit: $107", "phone or mail, other: $178"], "result": "IRS, Payment plans"},
  b=("hot", "lång plan: $29–$178"))
V("While an approved plan is in place, the failure to pay penalty shrinks. For an individual who filed on time, it drops from half a percent to a quarter percent a month.",
  real("U.S. LAW", "0.25%", "a month while an installment agreement is in effect", "26 U.S.C. 6651(h)"), b=("vändning", "0,25 % under plan"))
S("You pick 180 days. Four wedding deposits and one dog party later, the balance reads zero, and you screenshot it twice.",
  "desk_room", H(0.36, "smirk", "hold", hold="phone"), [{"type": "phone", "x": 0.56, "text": "BALANCE|$0.00"}],
  note="IRS: SHORT-TERM PLAN (UP TO 180 DAYS), $0 SETUP ONLINE", b=("lösning", "skulden betald"))
S("Jules buys a new green marker and adds a third column to the rent board. It says FRIENDS, underlined, with an arrow.",
  "apt_kitchen", H(0.28, "smirk", "down", 0.36), [{"type": "fridge", "x": 0.66, "whiteboard": "RENT: JULES PAID DEV PAID | USE: FRIENDS", "shoebox": "TAXES?"}],
  friends=[F("Jules", 0.84, "yellow", "Never again.", **JULES)], b=("callback", "tredje kolumnen på tavlan"))
# ---------- NIVÅ 10 ----------
V("Level ten. The man on the bench.", card("TEN", "the man on the bench"), chapter="Level 10: The man on the bench", b=("hot", "nivåkort 10"))
S("Back in January, you dropped a copy of your paperwork at the federal building. On the bench outside sat a man named Walt, holding a stack of envelopes.",
  "federal_lobby", H(0.3, "neutral", "down", 0.42), friends=[F("Walt", 0.72, "brown", "First one?", hair="gray", glasses=True)],
  b=("människor", "Walt på bänken"))
S("His were the version of this story where nobody opens anything. He'd stopped counting at the envelope with a red stripe.",
  "federal_lobby", H(0.3, "doubt", "down"), [{"type": "letter", "x": 0.56, "title": "FINAL NOTICE", "tag": "INTENT TO LEVY"}],
  friends=[F("Walt", 0.74, "brown", hair="gray", glasses=True)], b=("hot", "Walts version: inget öppnas"))
V("When a tax is assessed and a bill goes unpaid, the government gets a lien. The IRS calls it a legal claim against your property.",
  real("U.S. GOVERNMENT", "LIEN", "the government's legal claim against your property", "IRS, Understanding a federal tax lien"), b=("hot", "panträtt"))
V("The IRS can also file a public Notice of Federal Tax Lien, to alert creditors. Its own page says that may limit your ability to get credit.",
  label("PUBLIC NOTICE", "alerts creditors; may limit your ability to get credit", "IRS, Understanding a federal tax lien", True), b=("hot", "offentlig notis till långivare"))
V("Before the IRS takes money from wages or a bank account, it has to warn you. The notice comes at least 30 days before the first levy, with the right to ask for a hearing.",
  real("U.S. LAW", "30 DAYS", "notice and a right to a hearing before the first levy", "26 U.S.C. 6330(a)"), b=("vändning", "30 dagar före utmätning"))
V("Ten days after that notice of intent to levy, if the tax still isn't paid, the failure to pay penalty doubles. It becomes 1 percent a month.",
  label("1% A MONTH", "10 days after a notice of intent to levy", "IRS, Failure to pay penalty", True), b=("hot", "1 % efter 10 dagar"))
V("And it lasts. The IRS generally has 10 years from the date a tax was assessed to collect it, including penalties and interest.",
  real("U.S. GOVERNMENT", "10 YEARS", "to collect, from the date the tax was assessed", "IRS, Time IRS can collect tax"), b=("hot", "10 år"))
V("Walt's stack had one more envelope, and he tapped it. For 2026, unpaid federal tax debt of more than 66,000 dollars, with penalties and interest, can cost you your passport.",
  real("U.S. GOVERNMENT", "$66,000", "seriously delinquent tax debt (2026): passport at risk", "IRS, Revocation or denial of passport"), b=("hot", "passet vid $66 000"))
V("The IRS mails a notice called CP508C when it certifies that debt to the State Department. Walt's daughter was getting married in Lisbon in June.",
  close("federal_lobby", "sad", "LISBON"), b=("människor", "Walts dotter i Lissabon"), silence=True)
S("He asked what you did for a living. When you said weddings, he laughed for the first time and asked if you'd ever shot one in Portugal.",
  "federal_lobby", H(0.3, "smirk", "down"), friends=[F("Walt", 0.72, "brown", "Ever been to Lisbon?", hair="gray", glasses=True)],
  note="IRS: CP508C = DEBT CERTIFIED TO THE STATE DEPT", b=("människor", "Walt skrattar"))
# ---------- SLUT ----------
V("Your version cost 1,170 dollars and a 60 dollar filing fee. It also cost five months of a shoebox and a year of waiting for envelopes.",
  {"type": "board", "title": "ONE WRONG BUTTON", "lines": ["first proposal: $6,420", "final tax: $1,170", "penalty: $0", "Tax Court fee: $60"], "result": "plus interest, 7% a year, daily"},
  chapter="The end: What it cost", b=("vändning", "summeringen"))
S("In September, Dev moves out and a new roommate, Priya, moves in with two suitcases and a cactus she calls Gerald.",
  "apt_kitchen", H(0.28, "smirk", "down", 0.34), friends=[F("Priya", 0.76, "red", "Hi! Where's the rent go?", walk=0.62, hair="long")],
  b=("callback", "nya rumskamraten Priya"))
S("On the first of the month, she opens the payment app at the counter. Before she sends the rent, the app asks the question.",
  "apt_kitchen", H(0.28, "doubt", "down"), [{"type": "phone", "x": 0.6, "text": "$800|GOODS & SERVICES?|FRIENDS?"}],
  friends=[F("Priya", 0.76, "red", hair="long")], note="IRS: ROOMMATE REPAYING RENT ISN'T TAXABLE INCOME", b=("callback", "appen frågar"))
S("Her thumb hovers over the wrong button. Jules looks at you, you look at the rent board, and nobody says anything for a second.",
  "apt_kitchen", H(0.28, "shock", "down"), [{"type": "fridge", "x": 0.56, "whiteboard": "USE: FRIENDS", "shoebox": "TAXES?"}],
  friends=[F("Priya", 0.76, "red", hair="long"), F("Jules", 0.9, "yellow", **JULES)], b=("callback", "tummen över fel knapp"), silence=True)
S("Then all three of you point at the board at the same time, and Priya laughs, and presses friends.",
  "apt_kitchen", H(0.28, "smirk", "point"), [{"type": "fridge", "x": 0.56, "whiteboard": "USE: FRIENDS", "shoebox": "TAXES?"}],
  friends=[F("Priya", 0.76, "red", "Friends. Got it.", hair="long"), F("Jules", 0.9, "yellow", **JULES)], b=("callback", "Priya trycker friends"))
S("The shoebox is still on top of the fridge. It has one thing in it now, the stamped receipt from the post office that says day 52.",
  "apt_kitchen", H(0.3, "neutral", "reach", 0.5), [{"type": "shoebox", "x": 0.62, "text": "DAY 52", "open": True}],
  note="26 U.S.C. 6213: 90 DAYS, AND NO EXTENSIONS", b=("callback", "kvittot dag 52 i kartongen"))
V("So tell the truth in the comments. Is there a letter in your house right now that you haven't opened yet?",
  label("UNOPENED?", "is there a letter you haven't opened yet?", None), b=("callback", "fråga till tittaren"))

# ---------- tider + beats ----------
t = 0.0; beats = []
for s in sc:
    typ, txt = s.pop("_b")
    beats.append({"t": f"{int(t)//60}:{int(t)%60:02d}", "typ": typ, "text": txt})
    t += max(len(s["say"].split()) / WPS + 0.45, 2.0)
words = sum(len(s["say"].split()) for s in sc)
print("scener", len(sc), "ord", words, "min", round(t / 60, 2))
json.dump({"scenes": sc, "beats": beats, "dur": t}, open("body.json", "w"), ensure_ascii=False)
