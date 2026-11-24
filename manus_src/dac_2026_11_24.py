"""Generator for manus/dac-2026-11-24.json – Day After Court:
Your Life at Every Level of Getting Sued by a Debt Collector (California, 2026 rules).
Run: python3 manus_src/dac_2026_11_24.py  -> manus/dac-2026-11-24.json
"""
import json, os

WPS = 2.6
scenes = []


def dur(say):
    return max(len(say.split()) / WPS + 0.45, 2.0)


def S(say, vis, beat=None, **kw):
    sc = {"say": say, "visual": vis}
    sc.update(kw)
    if beat:
        sc["_beat"] = beat
    scenes.append(sc)


def hero(x=0.3, expr="neutral", arms="down", walk_to=None, holding=None):
    h = {"x": x, "expr": expr, "arms": arms}
    if walk_to is not None:
        h["walk_to"] = walk_to
    if holding:
        h["holding"] = holding
    return h


def scene(loc, h=None, shot="wide", props=None, friends=None, note=None):
    v = {"type": "scene", "location": loc, "shot": shot}
    if h:
        v["hero"] = h
    if props:
        v["props"] = props
    if friends:
        v["friends"] = friends
    if note:
        v["note_card"] = {"text": note}
    return v


def real(head, big, text, source):
    return {"type": "real", "head": head, "big": big, "text": text, "source": source}


def label(big, text, source=None, bad=True):
    return {"type": "label", "big": big, "text": text, "source": source, "bad": bad}


def close(loc, expr, thought, bad=True):
    return {"type": "closeup", "location": loc, "expr": expr, "look": -1, "thought": thought, "bad": bad}


def level(n, word, sub):
    return {"type": "daycard", "label": f"LEVEL {word}", "sub": sub}


CA, FED = "CALIFORNIA RULE", "FEDERAL RULE"
DANTE = {"outfit": "orange", "name": "Dante", "hair": "short", "cap": True}
INEZ = {"outfit": "purple", "name": "Inez", "hair": "bun", "glasses": True}
ENV_H = {"type": "envelope", "x": 0.66, "n": 1, "stamp": "HARBORLINE ASSET RECOVERY"}
MAILBOX = {"type": "mailbox_bank", "x": 0.62, "open": "14B"}

# ---------------- COLD OPEN (Level 1) ----------------
S("Mailbox 14B has never closed right. Tonight an envelope is sticking out of it.",
  scene("mailroom", hero(0.2, "doubt", "down", walk_to=0.42), props=[MAILBOX]),
  ("hot", "kuvertet sticker ut ur brevlåda 14B"), chapter="Level 1: The letter", sfx="paper")
S("It says you owe 3,812 dollars, and you have 30 days.",
  scene("mailroom", hero(0.42, "shock", "hold", walk_to=0.36, holding="letter"), props=[MAILBOX, {"type": "summons", "x": 0.74, "title": "YOU OWE", "tag": "$3,812"}]),
  ("hot", "$3,812 och 30 dagar"))
S("This is your life at every level of getting sued by a debt collector, from this envelope to your paycheck.",
  scene("mailroom", hero(0.36, "worried", "hold", walk_to=0.3, holding="letter"), props=[MAILBOX]),
  ("hot", "löftet: från kuvertet till lönen"))
S("The sender is Harborline Asset Recovery. You've never heard of them.",
  scene("mailroom", hero(0.3, "doubt", "hold", walk_to=0.26, holding="letter"), props=[ENV_H]),
  ("gåta", "vem är Harborline?"))
S("Your phone buzzes again. Same 916 number, the eighth call in six days.",
  label("8 CALLS", "same 916 number, six days"), ("hot", "8 samtal på 6 dagar"), sfx="buzz")
S("By the end you'll know what Harborline probably paid for your debt, and the number will make you angry.",
  label("PAID?", "what the company suing you paid for your debt"), ("gåta", "löfte: vad Harborline betalade"))
S("Federal law gives a collector five days after first contacting you to send a notice like this, with the amount and the creditor's name.",
  real(FED, "5 DAYS", "to send you the validation notice", "15 U.S.C. 1692g(a) (FDCPA)"), ("vändning", "valideringsbrevet – 5 dagar"))
S("Level one. The letter.", level(1, "ONE", "the letter"))
S("At the kitchen counter you read the rest. The original creditor is Copperleaf Bank, a card you cut in half back in 2023.",
  scene("apartment", hero(0.3, "doubt", "hold", walk_to=0.38, holding="letter"), props=[{"type": "summons", "x": 0.68, "title": "ORIGINAL CREDITOR", "tag": "COPPERLEAF BANK"}]),
  ("hot", "Copperleaf-kortet från 2023"))
S("You remember the card. You don't remember owing anyone named Harborline a single dollar of it.",
  close("apartment", "doubt", "WHO?"), ("gåta", "du har aldrig haft med Harborline att göra"))
S("The notice also starts a clock. You get 30 days after you receive it to dispute the debt, and the rules assume the mail takes five business days.",
  real(FED, "30 DAYS", "to dispute after you receive the notice", "12 CFR 1006.34(b)(5) (Regulation F)"), ("hot", "30 dagar att bestrida"))
S("If you dispute it in writing inside that window, the collector has to stop collecting until it mails you verification of the debt.",
  label("IN WRITING", "a written dispute pauses collection", "15 U.S.C. 1692g(b)", bad=False), ("vändning", "skriftligt bestridande = paus"))
S("You put the letter in the kitchen drawer, on top of the takeout menus, and tell yourself you'll call them tomorrow.",
  scene("apartment", hero(0.34, "neutral", "hold", walk_to=0.5, holding="letter"), props=[{"type": "drawer", "x": 0.62, "open": True}],
        note="30 DAYS TO DISPUTE IN WRITING (REG F)"),
  ("gåta", "lådan med hämtmatsmenyerna"))

# ---------------- LEVEL 2 ----------------
S("Level two. The calls.", level(2, "TWO", "the calls"), chapter="Level 2: The calls")
S("Day 9. You're on the loading dock at the warehouse, wrapping pallets, when the 916 number calls for the ninth time.",
  scene("loading_dock", hero(0.3, "worried", "hold", walk_to=0.4, holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "UNKNOWN|(916)|CALL 9"}],
        note="REG F: 30 DAYS TO DISPUTE AFTER YOU GET THE NOTICE"),
  ("hot", "nionde samtalet på lastkajen"), sfx="buzz")
S("Your coworker Dante watches you decline it again. He has driven a forklift for 22 years, and he only says one thing. Paper beats phone.",
  scene("loading_dock", hero(0.3, "doubt"), friends=[dict(DANTE, x=0.74, walk_to=0.64, say="Paper beats phone.")],
        note="A WRITTEN DISPUTE STOPS COLLECTION UNTIL VERIFICATION (15 U.S.C. 1692g(b))"),
  ("människor", "Dante: 'Paper beats phone.'"))
S("There is a federal rule about this. Calling more than seven times in seven days is presumed to be harassment under Regulation F, unless the collector can show otherwise.",
  real(FED, "7 IN 7", "calls in 7 days presumed harassment", "12 CFR 1006.14(b)(2)"), ("vändning", "7 samtal på 7 dagar"))
S("You've had nine of them. You don't know that rule yet, so on your lunch break you finally pick up.",
  close("loading_dock", "worried", "9 CALLS"), ("hot", "du svarar"))
S("A man named Kyle says he's calling for Harborline. He's friendly and he talks fast. He can settle the whole thing today for 400 dollars down.",
  scene("collector_office", friends=[{"x": 0.5, "outfit": "blue", "name": "Kyle", "hair": "short", "headset": True, "say": "$400 down, today?", "walk_to": 0.44}],
        note="REG F: MORE THAN 7 CALLS IN 7 DAYS = PRESUMED VIOLATION"),
  ("hot", "Kyle: 400 dollar idag"))
S("In California, a debt collector needs a state license from the Department of Financial Protection and Innovation, which began taking applications in September 2021.",
  real(CA, "LICENSED", "debt collectors need a DFPI license", "DFPI – Debt Collection Licensing Act (Fin. Code 100000 et seq.)"), ("vändning", "licenskravet i Kalifornien"))
S("California's own collection law, the Rosenthal Act, pulls most of the federal rules in, so the same limits on calls and threats apply under state law too.",
  real(CA, "ROSENTHAL", "state law adopts the federal FDCPA rules", "Cal. Civ. Code 1788.17"), ("vändning", "Rosenthal Act"))
S("You tell Kyle you'll think about it and hang up. You write nothing down, and you send nothing in writing.",
  scene("loading_dock", hero(0.32, "neutral", "hold", walk_to=0.24, holding="phone"), friends=[dict(DANTE, x=0.78)]),
  ("gåta", "inget skriftligt"))
S("On day 35 the dispute window closes. Nothing happens that day, which is exactly the problem.",
  label("DAY 35", "the 30-day dispute window closes"), ("vändning", "fönstret stängs dag 35"))
S("Because you only argued on the phone, Harborline never had to stop and prove anything. Dante's line turns out to be a rule.",
  label("NO PAUSE", "no written dispute, no verification", "15 U.S.C. 1692g(b)"), ("vändning", "Dantes replik var en regel"))

# ---------------- LEVEL 3 ----------------
S("Level three. The old card.", level(3, "THREE", "the old card"), chapter="Level 3: The old card")
S("That night you dig through your old bank app. Your last payment on the Copperleaf card was 55 dollars, back in March 2023.",
  scene("apartment", hero(0.3, "doubt", "hold", walk_to=0.36, holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "LAST PAYMENT|MAR 2023|$55.00"}],
        note="CA DEBT BUYERS MUST LIST THE DATE OF DEFAULT OR LAST PAYMENT (CIV. CODE 1788.58)"),
  ("gåta", "sista betalningen mars 2023"))
S("That was the spring the warehouse cut everyone to 28 hours a week. The rent got paid first, and the card got nothing after that.",
  close("apartment", "sad", "28 HRS"), ("människor", "timmarna kapades"))
S("At that point the balance was about 3,400 dollars. Late fees and interest pushed it to 3,812 by the time the bank stopped expecting you to pay.",
  scene("apartment", hero(0.3, "sad", "hold", holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "COPPERLEAF|$3,400|LATE FEE"}]), ("hot", "$3 400 blir $3 812"))
S("A few months later the bank charged the account off. That's an accounting entry. The debt still exists, and the bank is allowed to sell it.",
  label("CHARGED OFF", "written off by the bank, then sold"), ("vändning", "avskriven och såld"))
S("On your credit report, a collection account can stay for seven years, counted from 180 days after the delinquency began.",
  real(FED, "7 YEARS", "+180 days: how long a collection account can be reported", "15 U.S.C. 1681c(a)(4), (c)(1) (FCRA)"), ("hot", "7 år i kreditupplysningen"))
S("California gives a creditor four years to sue on a written contract like a card agreement. Once that time runs out, the law says nobody can sue you for it.",
  real(CA, "4 YEARS", "to sue on a written contract", "Cal. Code Civ. Proc. 337(a), (d)"), ("vändning", "4 års preskription"))
S("Federal rules say the same thing to the collector. A debt collector must not sue, or threaten to sue, over a time barred debt.",
  real(FED, "TIME-BARRED", "no lawsuits or threats over expired debt", "12 CFR 1006.26(b); Cal. Civ. Code 1788.56"), ("vändning", "inga stämningar efter fristen"))
S("You count on your fingers. March 2023 to March 2027. You are still inside the window, by about four months.",
  {"type": "plan", "title": "YOUR CLOCK", "items": [
      {"box": [0.04, 0.3, 0.28, 0.4], "label": "LAST PAYMENT MAR 2023"},
      {"box": [0.36, 0.3, 0.28, 0.4], "label": "TODAY NOV 2026"},
      {"box": [0.68, 0.3, 0.28, 0.4], "label": "4 YEARS: MAR 2027", "hot": True}]},
  ("hot", "du är innanför fönstret – 4 månader kvar"))
S("You're not unusual. Pew researchers found debt cases grew from one in nine civil cases in 1993 to one in four by 2013.",
  real("PEW RESEARCH", "1 IN 4", "civil cases were debt cases by 2013", "Pew Charitable Trusts, 'How Debt Collectors Are Transforming the Business of State Courts' (2020)"),
  ("vändning", "1 av 4 civilmål"))

# ---------------- LEVEL 4 ----------------
S("Level four. The summons.", level(4, "FOUR", "the summons"), chapter="Level 4: The summons")
S("Day 52. A woman in a yellow raincoat is waiting by the mailboxes. She says your full name like a question, and you say yes before you can stop yourself.",
  scene("mailroom", hero(0.26, "shock", "down", walk_to=0.36), props=[MAILBOX], friends=[{"x": 0.76, "outfit": "yellow", "name": "Process server", "hair": "long", "walk_to": 0.62, "say": "That's you?"}]),
  ("hot", "delgivningen vid brevlådorna"), sfx="paper", silence=True)
S("She hands you a stack of paper and walks away. The top page is a California summons, form SUM-100, with your name in capital letters.",
  scene("mailroom", hero(0.36, "shock", "hold", holding="letter"), props=[{"type": "summons", "x": 0.68, "title": "SUMMONS", "tag": "SUM-100"}]),
  ("hot", "SUM-100"))
S("The summons gives you 30 days after you're served to file a written answer with the court. That clock started the moment you said yes.",
  real(CA, "30 DAYS", "to file a written answer after you're served", "Cal. Code Civ. Proc. 412.20(a)(3)"), ("hot", "30 dagar att svara"))
S("Under it is the complaint. Harborline Asset Recovery versus you. They're asking for 4,486 dollars, which is more than 3,812.",
  label("$4,486", "what Harborline asks the court for"), ("hot", "kravet har vuxit till $4,486"))
S("California makes debt buyers spell that out. The balance at charge off, and any interest and fees added after it, have to be stated separately.",
  real(CA, "SEPARATE", "charge-off balance vs. interest and fees added after", "Cal. Civ. Code 1788.58(a)"), ("vändning", "posterna måste anges var för sig"))
S("The complaint also has to give the date of default or the date of your last payment. Harborline's says March 2023, the month of your 55 dollar payment.",
  real(CA, "LAST PAYMENT", "date of default or last payment must be in the complaint", "Cal. Civ. Code 1788.58(a)"), ("callback", "mars 2023 igen"))
S("So it's right there in two lines. 3,812 dollars from the card, and 674 dollars added since the bank let go of it.",
  {"type": "board", "title": "THE COMPLAINT", "lines": ["balance at charge-off: $3,812", "interest and fees after: $674"], "result": "$4,486"},
  ("hot", "674 dollar påslag"))
S("Because the amount is under 35,000 dollars, this is a limited civil case in superior court. You expected small claims, and it isn't.",
  real(CA, "$35,000", "or less = limited civil case", "California Courts Self-Help Guide – Civil lawsuits"), ("gåta", "varför inte small claims?"))
S("California doesn't let someone who bought a claim file it in small claims court. So a debt buyer comes to regular court, with a lawyer.",
  real(CA, "NO BUYERS", "assignees can't sue in small claims", "Cal. Code Civ. Proc. 116.420(a)"), ("vändning", "köpta fordringar får inte gå till small claims"))

# ---------------- LEVEL 5 ----------------
S("Level five. The paper trail.", level(5, "FIVE", "the paper trail"), chapter="Level 5: The paper trail")
S("You spread the complaint across the kitchen table. Behind it is a copy of your old card agreement, 31 pages of small print you never read.",
  scene("apartment", hero(0.3, "doubt", "hold", walk_to=0.38, holding="letter"), props=[{"type": "summons", "x": 0.68, "title": "EXHIBIT A", "tag": "31 PAGES"}]),
  ("gåta", "31 sidor avtal"))
S("California requires a debt buyer to attach the contract, or the document that proves the debt, to the complaint itself.",
  real(CA, "ATTACHED", "the contract goes with the complaint", "Cal. Civ. Code 1788.58(b)"), ("vändning", "avtalet ska bifogas"))
S("Page three answers the question from the mailbox. The law makes a debt buyer list every company that bought your debt after the charge off.",
  scene("apartment", hero(0.3, "shock", "hold", holding="letter"), props=[{"type": "summons", "x": 0.68, "title": "PAGE 3", "tag": "ALL OWNERS"}],
        note="DEBT BUYER MUST NAME EVERY BUYER AFTER CHARGE-OFF (CIV. CODE 1788.58)"),
  ("vändning", "sidan 3 löser gåtan: ägarkedjan"))
S("Copperleaf Bank sold it to a company called Meridian Receivables. Meridian sold it to Harborline. Your old card has had three owners, and you met none of them.",
  {"type": "plan", "title": "WHO OWNED YOUR $3,812", "items": [
      {"box": [0.04, 0.3, 0.28, 0.4], "label": "COPPERLEAF BANK"},
      {"box": [0.36, 0.3, 0.28, 0.4], "label": "MERIDIAN RECEIVABLES"},
      {"box": [0.68, 0.3, 0.28, 0.4], "label": "HARBORLINE", "hot": True}]},
  ("vändning", "tre ägare"))
S("The complaint also has to say that Harborline is the only owner, or has the owners' permission to sue, plus the bank's name and the full account number.",
  real(CA, "SOLE OWNER", "plus the charge-off creditor and account number", "Cal. Civ. Code 1788.58(a)"), ("hot", "ensam ägare"))
S("You stare at the list and wonder what a stranger pays for somebody else's old credit card. You'll find out at the very end.",
  close("apartment", "doubt", "WHAT PRICE?"), ("gåta", "vad betalar en främling?"))
S("At work you show Dante the stack. He doesn't read it. He taps the top page twice and says it again. Paper beats phone.",
  scene("loading_dock", hero(0.3, "worried", "hold", holding="letter"), friends=[dict(DANTE, x=0.72, walk_to=0.6, say="Paper beats phone.")],
        note="DEBT BUYER MUST ATTACH THE CONTRACT (CIV. CODE 1788.58(b))"),
  ("människor", "Dante igen"))

# ---------------- LEVEL 6 ----------------
S("Level six. The drawer.", level(6, "SIX", "the drawer"), chapter="Level 6: The drawer")
S("Day 60. You look up how to answer. The court's self help site has a form for exactly this, an answer to a contract complaint, PLD-C-010.",
  scene("self_help_center", hero(0.26, "doubt", "hold", walk_to=0.4, holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "ANSWER|CONTRACT|PLD-C-010"}]),
  ("lösning", "svarsblanketten PLD-C-010"))
S("Filing it costs money. Under the 2026 statewide fee schedule, a defendant's first paper in a limited case up to 10,000 dollars is 225 dollars.",
  real(CA, "$225", "to file an answer, limited case up to $10,000", "Judicial Council – Statewide Civil Fee Schedule, eff. Jan 1, 2026"), ("hot", "225 dollar i avgift"))
S("If you get public benefits, or your household income is under a set limit, you can ask the court to waive that fee with form FW-001.",
  real(CA, "FW-001", "request to waive court fees", "California Courts Self-Help Guide – Fee waivers"), ("lösning", "avgiftsbefrielse"))
S("The courthouse also has a free self help center where staff explain the forms. You've walked past it twice. Both times you were late for a shift.",
  scene("self_help_center", hero(0.24, "neutral", "down", walk_to=0.6), note="FREE COURT SELF-HELP CENTERS EXPLAIN THE FORMS"), ("gåta", "självhjälpscentret du går förbi"))
S("You check your account. 612 dollars until Friday. You tell yourself you'll deal with the court next week, when things calm down.",
  scene("apartment", hero(0.3, "sad", "hold", holding="phone"), props=[{"type": "bank_app", "x": 0.72, "balance": "$612.40"}]),
  ("hot", "612 dollar till fredag"))
S("The summons goes into the kitchen drawer, on top of Harborline's first letter and the takeout menus.",
  scene("apartment", hero(0.34, "neutral", "hold", walk_to=0.5, holding="letter"), props=[{"type": "drawer", "x": 0.62, "open": True}],
        note="ANSWER DUE 30 DAYS AFTER SERVICE (CCP 412.20)"),
  ("callback", "samma låda"))
S("That's the most common ending for these cases. Pew found courts decided more than 70 percent of debt collection lawsuits by default judgment.",
  real("PEW RESEARCH", "70%+", "of debt collection lawsuits ended in default", "Pew Charitable Trusts (2020)"), ("vändning", "70 % förloras utan svar"))
S("Fewer than 10 percent of the people sued in these cases have a lawyer. Most of them go through it alone, or don't show up at all.",
  label("UNDER 10%", "of defendants have a lawyer", "Pew Charitable Trusts (2020)"), ("hot", "under 10 % har advokat"))
S("The same report has one more number. In Utah, defendants who had a lawyer won 53 percent of the time, and those without one won 19 percent.",
  label("53% vs 19%", "Utah: defendants with a lawyer vs. without", "Pew Charitable Trusts (2020)"), ("vändning", "Utah 53 % mot 19 %"))
S("Day 70 goes by in the middle of a double shift. Day 82 goes by on a Sunday. The drawer stays closed the whole time.",
  {"type": "plan", "title": "THE 30 DAYS", "items": [
      {"box": [0.04, 0.3, 0.28, 0.4], "label": "DAY 52 SERVED"},
      {"box": [0.36, 0.3, 0.28, 0.4], "label": "DAY 70"},
      {"box": [0.68, 0.3, 0.28, 0.4], "label": "DAY 82 DEADLINE", "hot": True}]},
  ("hot", "dag 82 passerar"), silence=True)

# ---------------- LEVEL 7 ----------------
S("Level seven. The default.", level(7, "SEVEN", "the default"), chapter="Level 7: The default")
S("On day 90, Harborline's lawyer files a request to enter your default. There's no hearing and no phone call, just a form called CIV-100.",
  scene("court_hall", props=[{"type": "summons", "x": 0.5, "title": "CIV-100", "tag": "REQUEST FOR DEFAULT"}]),
  ("hot", "CIV-100"))
S("The court's own guide says the other side has to wait at least 30 days after you were served. Harborline waited 38.",
  real(CA, "WAIT 30", "days after service before asking for default", "California Courts Self-Help Guide – Debt lawsuits: default"), ("vändning", "Harborline väntade 38 dagar"))
S("A California debt buyer can't win a default on its word alone. It needs business records backed by a sworn declaration, plus a copy of the contract.",
  real(CA, "SWORN", "business records + contract before a default judgment", "Cal. Civ. Code 1788.60"), ("vändning", "bevis krävs även vid tredskodom"))
S("Harborline has all of that, because it's the same 31 pages that have been sitting in your kitchen drawer since day 52.",
  label("THEY HAD IT", "the 31-page agreement, exhibit A"), ("callback", "samma 31 sidor"))
S("A default judgment means the court never heard your side. Anything you might have said about that extra 674 dollars was never said by anyone.",
  label("YOUR SIDE", "never heard by the court"), ("hot", "din sida hördes aldrig"))
S("The judgment comes by mail a few weeks later. 4,486 dollars, plus 412 in court costs. 4,898 dollars owed to a company you've never met.",
  close("apartment", "shock", "$4,898"), ("hot", "dom: $4,898"), silence=True, sfx="paper")
S("From now on the judgment grows. For a personal credit card judgment under 50,000 dollars, California sets interest at 5 percent a year instead of 10.",
  real(CA, "5%", "a year on credit card judgments under $50,000", "Cal. Code Civ. Proc. 685.010(a)(2)"), ("hot", "5 % ränta"))
S("Months later, a clerk at the courthouse self help center tells you about a rule you wish you had heard about sooner.",
  scene("self_help_center", hero(0.3, "worried", "down", walk_to=0.4), friends=[{"x": 0.74, "outfit": "teal", "name": "Clerk", "glasses": True, "say": "Six months."}]),
  ("gåta", "regeln du borde ha känt till"))
S("A court can set aside a default for mistake, surprise or excusable neglect, but you have to ask within a reasonable time, and never more than six months.",
  real(CA, "6 MONTHS", "outer limit to ask to set aside a default", "Cal. Code Civ. Proc. 473(b)"), ("vändning", "6 månader"))
S("You count again. It has been eight months since the default. That door closed while the summons was still in the drawer.",
  close("self_help_center", "sad", "MONTH 8"), ("hot", "för sent"))

# ---------------- LEVEL 8 ----------------
S("Level eight. The paycheck.", level(8, "EIGHT", "the paycheck"), chapter="Level 8: The paycheck")
S("Your supervisor calls you into the office with a sheet of paper. Payroll got an earnings withholding order. Harborline is coming for your wages.",
  scene("loading_dock", hero(0.3, "shock", "hold", walk_to=0.38, holding="letter"), props=[{"type": "summons", "x": 0.68, "title": "EARNINGS WITHHOLDING", "tag": "HARBORLINE"}]),
  ("hot", "löneutmätning"), sfx="paper")
S("California caps the amount. They can take the lesser of 20 percent of your disposable pay, or 40 percent of what you earn above 48 times the state minimum wage, each week.",
  real(CA, "20% / 40%", "whichever takes less from your weekly pay", "Cal. Code Civ. Proc. 706.050(a)"), ("vändning", "taket 20 % / 40 %"))
S("In 2026 the California minimum wage is 16.90 an hour. Times 48, that's 811 dollars and 20 cents of weekly pay the formula leaves alone.",
  real(CA, "$16.90", "x 48 = $811.20 a week protected by the formula", "Calif. Dept. of Industrial Relations, news release 2025-118"), ("hot", "$811,20 skyddas"))
S("After taxes your pay is 1,050 dollars a week. 20 percent would be 210. 40 percent of the part above 811 is 95 dollars and 52 cents. The smaller number wins.",
  {"type": "board", "title": "YOUR WEEK", "lines": ["disposable pay: $1,050", "20%: $210", "40% of ($1,050 - $811.20): $95.52"], "result": "$95.52 a week"},
  ("hot", "$95,52 i veckan"))
S("Federal law caps garnishment at 25 percent of disposable pay. California's formula takes less here, so it's the one that sets your number.",
  real(FED, "25%", "federal cap on wage garnishment", "15 U.S.C. 1673(a)"), ("vändning", "federala taket 25 %"))
S("Dante sees your face at lunch. You tell him it's 95 dollars a week for about a year. He just nods and hands you half his sandwich.",
  scene("loading_dock", hero(0.3, "sad"), friends=[dict(DANTE, x=0.7, walk_to=0.6, say="Half?")]),
  ("människor", "Dantes smörgås"))
S("There's a form for people who can't live on what's left. It's a claim of exemption, WG-006, filed with a financial statement that lists your real bills.",
  real(CA, "WG-006", "claim of exemption, with a financial statement", "California Courts Self-Help Guide – Wage garnishment exemption"), ("lösning", "undantagsansökan WG-006"))
S("You fill it out at the kitchen table, right next to the drawer, and list every bill. Rent alone is 1,640 dollars a month.",
  scene("apartment", hero(0.3, "worried", "hold", holding="letter"), props=[{"type": "summons", "x": 0.68, "title": "WG-006", "tag": "RENT $1,640"}]),
  ("hot", "hyran $1 640"))
S("Once you file it, the creditor gets 10 days to oppose your claim. Harborline does, and a hearing is set for a Tuesday morning.",
  label("10 DAYS", "for the creditor to oppose your claim", "California Courts Self-Help Guide – Wage garnishment exemption"), ("vändning", "Harborline överklagar"))
S("At the hearing, a commissioner goes through your budget line by line and lowers the weekly amount to 60 dollars. The payments get smaller, and the debt lasts longer.",
  scene("courtroom", hero(0.4, "worried"), friends=[{"x": 0.5, "outfit": "robe", "name": "Commissioner", "hair": "short", "say": "$60 a week."}],
        note="CLAIM OF EXEMPTION: THE COURT CAN LOWER THE AMOUNT"),
  ("vändning", "sänks till 60 dollar"))

# ---------------- LEVEL 9 ----------------
S("At 60 dollars a week, 4,898 dollars plus interest takes more than a year and a half of Fridays to pay off.",
  label("82 FRIDAYS", "$4,898 at $60 a week, before interest"), ("hot", "82 fredagar"))
S("Level nine. The bank.", level(9, "NINE", "the bank"), chapter="Level 9: The bank")
S("Then comes the bank account. One morning your banking app shows a hold on almost everything in checking. Harborline has levied the account.",
  scene("bank", hero(0.3, "shock", "hold", walk_to=0.38, holding="phone"), props=[{"type": "bank_app", "x": 0.72, "balance": "LEVY HOLD"}]),
  ("hot", "kontot är fryst"))
S("California protects part of it automatically. For levies from July 1, 2026, the first 2,325 dollars in your account can't be taken.",
  real(CA, "$2,325", "protected automatically in a bank account", "Cal. Code Civ. Proc. 704.220; Judicial Council 2026 adjustment"), ("vändning", "$2 325 skyddas"))
S("That number moves with prices. Until the end of June 2026 it was 2,244 dollars, and the Judicial Council raised it this summer to keep up with the cost of living.",
  label("$2,244", "the protected amount before July 1, 2026", "Judicial Council of California, June 2026 adjustment"), ("vändning", "höjt från $2 244"))
S("You had 2,610 dollars in there because you were saving for a car. The levy takes 285 of it.",
  label("-$285", "what the levy actually takes"), ("hot", "285 dollar tas"))
S("If you think more of it should be protected, you file a claim of exemption, form EJ-160, within 15 days if you were served in person, or 20 if by mail.",
  real(CA, "15 DAYS", "to claim an exemption (20 if served by mail)", "Cal. Code Civ. Proc. 703.520(a)"), ("vändning", "15 dagar"))
S("At the mailboxes, your neighbor Inez from 14C asks if a collector could empty her account too. She lives on her Social Security.",
  scene("mailroom", hero(0.3, "neutral", "down", walk_to=0.38), props=[MAILBOX], friends=[dict(INEZ, x=0.74, walk_to=0.64, say="Mine too?")]),
  ("människor", "grannen Inez"))
S("Federal rules give her a shield. When a garnishment order arrives, her bank has to protect two months of directly deposited federal benefits like Social Security.",
  real(FED, "2 MONTHS", "of direct-deposited federal benefits protected", "31 CFR 212.6 and Appendix C"), ("vändning", "2 månaders förmåner skyddas"))
S("Inez taps your mailbox lid, the one that never closes, and says somebody ought to fix that. You say you will, and then you don't.",
  close("mailroom", "smirk", "14B", bad=False), ("callback", "locket på 14B"))

# ---------------- LEVEL 10 ----------------
S("Level ten. The long shadow.", level(10, "TEN", "the long shadow"), chapter="Level 10: The long shadow")
S("Two years later the garnishment is nearly done. You start looking at small condos, and a loan officer pulls your credit report.",
  scene("bank", hero(0.3, "neutral", "down", walk_to=0.4), friends=[{"x": 0.74, "outfit": "suit", "name": "Loan officer", "hair": "long", "say": "Is it paid?"}]),
  ("hot", "lånehandläggaren"))
S("A California money judgment can be enforced for 10 years from the day it's entered, and it can be renewed.",
  real(CA, "10 YEARS", "a judgment stays enforceable, renewable", "Cal. Code Civ. Proc. 683.020, 683.110"), ("hot", "10 år"))
S("For personal debt judgments under 50,000 dollars, the law now allows that renewal only once, which puts the outside limit at roughly 20 years.",
  real(CA, "ONCE", "renewal limit for personal debt under $50,000", "Cal. Code Civ. Proc. 683.110(c)"), ("vändning", "förnyelse bara en gång"))
S("And if Harborline records an abstract of the judgment with the county recorder, it becomes a lien on real property you own in that county, for 10 years.",
  real(CA, "LIEN", "on real property, for 10 years", "Cal. Code Civ. Proc. 697.310"), ("hot", "panträtt i bostaden"))
S("The collection account itself has its own clock. It drops off your credit report seven years and 180 days after you first fell behind, somewhere around the fall of 2030.",
  label("FALL 2030", "when the collection account leaves your report", "15 U.S.C. 1681c(c)(1)"), ("vändning", "hösten 2030"))
S("The loan officer asks if the judgment is fully paid. You say almost. She says almost is the word that makes underwriters nervous.",
  close("bank", "worried", "ALMOST"), ("hot", "'almost'"))
S("So you finish it. You pay the last 340 dollars of the judgment and the interest straight to Harborline's lawyer, and you ask for it in writing.",
  scene("apartment", hero(0.3, "neutral", "hold", walk_to=0.36, holding="phone"), props=[{"type": "phone", "x": 0.72, "text": "FINAL PAYMENT|$340.00|SENT"}],
        note="JUDGMENT LIEN: RECORDED ABSTRACT, 10 YEARS (CCP 697.310)"),
  ("lösning", "sista betalningen"))
S("Two weeks later the paper comes, a filed satisfaction of judgment. You read it twice. For once, you're the one holding the paper.",
  label("PAID", "satisfaction of judgment, on paper", bad=False), ("callback", "papperet"))

# ---------------- ENDING ----------------
S("One night you add it all up. 3,812 on the card, 674 added before court, 412 in costs, and interest on top, paid out over almost two years of smaller paychecks.",
  {"type": "board", "title": "ONE OLD CARD", "lines": ["on the card: $3,812", "added before court: $674", "court costs: $412", "plus 5% a year"], "result": "almost 2 years of paychecks"},
  ("hot", "hela notan"), chapter="The end: What it cost")
S("Then you find the answer to the question from page three. The FTC studied debt buyers and found they paid about 4 cents on the dollar, and even less for older debt.",
  real("FTC STUDY", "4 CENTS", "average paid per dollar of debt; older debt sold for less", "Federal Trade Commission, debt buying study press release, Jan 30, 2013"),
  ("vändning", "gåtan löst: 4 cent per dollar"))
S("If Harborline paid that average, your 3,812 dollar card cost them about 152 dollars. You paid them more than thirty times that.",
  close("apartment", "shock", "$152"), ("vändning", "$152 mot över $4 898"), silence=True)
S("On a Saturday you finally fix the lid on mailbox 14B. It takes one screwdriver and eleven minutes.",
  scene("mailroom", hero(0.3, "smirk", "hold", walk_to=0.5, holding="tool"), props=[MAILBOX],
        note="FTC 2013: DEBT BUYERS PAID ABOUT 4 CENTS PER DOLLAR"),
  ("callback", "du lagar locket"))
S("A week later, a new tenant from 14A is standing at the mailboxes holding an envelope from a company she has never heard of.",
  scene("mailroom", hero(0.26, "neutral", "down"), props=[MAILBOX], friends=[{"x": 0.72, "outfit": "green", "name": "New tenant", "hair": "long", "walk_to": 0.6, "say": "Who are these people?"}],
        note="A COLLECTOR MUST SEND A VALIDATION NOTICE WITHIN 5 DAYS (15 U.S.C. 1692g)"),
  ("callback", "ny granne, nytt kuvert"))
S("She asks if she should just call them back. You hear yourself say it before you can stop. Paper beats phone, and don't put it in a drawer.",
  scene("mailroom", hero(0.34, "smirk", "point"), props=[MAILBOX], friends=[{"x": 0.66, "outfit": "green", "name": "New tenant", "hair": "long"}],
        note="DISPUTE IN WRITING · ANSWER WITHIN 30 DAYS"),
  ("callback", "'Paper beats phone' – cykeln"))
S("So tell us honestly. Is there an envelope sitting in a drawer at your place right now that you keep meaning to open?",
  label("YOUR DRAWER?", "what's in it right now?", bad=False), ("callback", "fråga till tittaren"))

# ---------------- beats from scenes ----------------
beats, t = [], 0.0
for sc in scenes:
    b = sc.pop("_beat", None)
    if b:
        beats.append({"t": f"{int(t // 60)}:{int(t % 60):02d}", "typ": b[0], "text": b[1]})
    t += dur(sc["say"])

allsay = " ".join(s["say"] for s in scenes)
nwords = len(allsay.split())

manus = {
    "channel": "Day After Court",
    "title": "Your Life at Every Level of Getting Sued by a Debt Collector",
    "standard": "DAC_STANDARD",
    "format": "FORMAT_BLUEPRINT – DAC (Your Life at Every Level of …, nivåkort, siffer-bubblor) + DUI-mallen (vanlig händelse i tidsordning)",
    "style": "qm",
    "look": "dac_semireal",
    "voice": "am_michael",
    "speed": 0.97,
    "lang": "en-us",
    "music": "calm",
    "music_level": 0.06,
    "beats": beats,
    "scenes": scenes,
}
here = os.path.dirname(os.path.abspath(__file__))
extra = json.load(open(os.path.join(here, "dac_2026_11_24_meta.json")))
manus.update(extra)
out = os.path.join(here, "..", "manus", "dac-2026-11-24.json")
json.dump(manus, open(out, "w"), ensure_ascii=False, indent=1)
print(out, len(scenes), "scener", nwords, "ord", f"{t/60:.1f} min", len(beats), "beats")
