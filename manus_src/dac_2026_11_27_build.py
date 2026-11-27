import json
b = json.load(open("body.json"))
sc, beats, dur = b["scenes"], b["beats"], b["dur"]
words = [len(s["say"].split()) for s in sc]
FACT = ("real", "label", "board", "plan", "daycard")
# största lucka mellan faktaskyltar
t = 0.0; last = 0.0; gap = 0.0; nf = 0; nreal = 0
for s in sc:
    v = s["visual"]
    if v["type"] in FACT or "note_card" in v:
        gap = max(gap, t - last); last = t; nf += 1
    if v["type"] == "real": nreal += 1
    t += max(len(s["say"].split()) / 2.6 + 0.45, 2.0)
TITLE = "Your Life at Every Level of an IRS Letter ($6,420)"
m = {
 "channel": "Day After Court", "title": TITLE, "standard": "DAC_STANDARD",
 "format": "FORMAT_BLUEPRINT – DAC (Your Life at Every Level of …, nivåkort, siffror på föremål) + DUI-mallen (vanlig händelse i tidsordning)",
 "style": "qm", "look": "dac_semireal", "voice": "am_michael", "speed": 0.97, "lang": "en-us", "music": "calm", "music_level": 0.06,
 "beats": beats, "scenes": sc,
 "seo": {
  "title": TITLE,
  "title_b": "The IRS Says Someone Paid You $21,400. Every Level After",
  "sokfras": "your life at every level of",
  "sokfras_kalla": "YouTubes sökförslag hämtade 27/11 (web-fetch av suggestqueries, client=firefox&ds=yt): 'your life at every level of' (frasen själv är förslag nr 2), 'what happens if you get audited' → 'what happens when you get audited', 'what happens if you don't pay taxes', 'irs letter'. TREND_2026-11-27 fanns inte när manuset skrevs (Last Shift-körningen kördes om samtidigt).",
  "hook": "An IRS envelope on your counter says you owe $6,420, and you have 30 days to answer. This is every level that follows, from the CP2000 to the day you find out who paid you $21,400.",
  "summary": "An IRS CP2000 letter says you didn't report $21,400 from a payment app, and proposes $6,420 in tax and penalty. This video follows a made-up wedding photographer through every level of an IRS letter, in time order: what a CP2000 is (a proposal, not a bill) and its 30-day response window, what Form 1099-K reports and the $20,000 / 200-transaction threshold, the 20% accuracy-related penalty and the $5,000 substantial-understatement line (26 U.S.C. 6662), the 7% underpayment interest rate compounded daily, the Statutory Notice of Deficiency sent by certified mail (6212) and the 90-day deadline to petition the U.S. Tax Court that cannot be extended (6213), the $60 filing fee, small tax cases up to $50,000 a year with no appeal, why roommates repaying rent are personal payments and not taxable income, settlement with IRS counsel, the failure-to-pay penalty (0.5% a month, 25% cap, 0.25% under a payment plan), payment plan setup fees, and what happens to people who never open the envelopes: federal tax liens, the 30-day notice before a levy (6330), the 10-year collection period and passport denial for seriously delinquent tax debt over $66,000 in 2026.\n\nEveryone in this story is made up, and so are the payment app, the dollar amounts ($6,420, $5,350, $21,400, $17,500, $3,900, $1,170), the dates and the case number. The laws, deadlines, fees and IRS rules come from the sources listed below. Real cases depend on the facts and the tax year.",
  "disclaimer": "This video explains general U.S. federal tax rules and Tax Court procedures for education and entertainment. It is not legal or tax advice. Rules, thresholds, fees and interest rates change, often every year. If you receive an IRS notice, read the notice itself, check IRS.gov, and talk to a qualified tax professional or a Low Income Taxpayer Clinic.",
  "keywords": ["your life at every level of", "your life at every level", "irs letter", "irs cp2000", "cp2000 notice", "what happens when you get audited", "what happens if you don't pay taxes", "notice of deficiency", "90 day letter irs", "tax court", "form 1099-k", "1099-k roommate rent", "irs payment plan", "irs passport $66,000"],
  "sources": [
   {"title": "IRS – Understanding your CP2000 notice", "url": "https://www.irs.gov/individuals/understanding-your-cp2000-series-notice"},
   {"title": "IRS – Topic no. 652, Notice of underreported income – CP2000 (not a bill; 30/60 days; Statutory Notice of Deficiency)", "url": "https://www.irs.gov/taxtopics/tc652"},
   {"title": "IRS – Understanding your Form 1099-K ($20,000 / 200 transactions; roommate repaying rent is not taxable)", "url": "https://www.irs.gov/businesses/understanding-your-form-1099-k"},
   {"title": "IRS – Form 1099-K FAQs: Common situations (A3)", "url": "https://www.irs.gov/newsroom/form-1099-k-faqs-common-situations"},
   {"title": "IRS – Accuracy-related penalty", "url": "https://www.irs.gov/payments/accuracy-related-penalty"},
   {"title": "26 U.S.C. 6662 (20%; substantial understatement)", "url": "https://www.law.cornell.edu/uscode/text/26/6662"},
   {"title": "IRS – Interest rates remain the same for the fourth quarter of 2026 (IR-2026-98: 7%, compounded daily)", "url": "https://www.irs.gov/newsroom/interest-rates-remain-the-same-for-the-fourth-quarter-of-2026"},
   {"title": "26 U.S.C. 6212 (notice of deficiency by certified or registered mail)", "url": "https://www.law.cornell.edu/uscode/text/26/6212"},
   {"title": "26 U.S.C. 6213 (90 days / 150 days to petition the Tax Court)", "url": "https://www.law.cornell.edu/uscode/text/26/6213"},
   {"title": "U.S. Tax Court – Starting a case (no extensions; fee waiver)", "url": "https://www.ustaxcourt.gov/petitioners-start/"},
   {"title": "U.S. Tax Court – Fees and charges ($60)", "url": "https://ustaxcourt.gov/fees-and-charges"},
   {"title": "U.S. Tax Court – About the Court (independent; S cases not appealable; most cases settle; 79 cities)", "url": "https://www.ustaxcourt.gov/petitioners-about/"},
   {"title": "U.S. Tax Court – Case procedure ($50,000 or less per year)", "url": "https://www.ustaxcourt.gov/case-procedure/"},
   {"title": "IRS – Failure to pay penalty (0.5%, 25%, 0.25% under a plan, 1% after intent to levy)", "url": "https://www.irs.gov/payments/failure-to-pay-penalty"},
   {"title": "26 U.S.C. 6651 (a)(2) and (h)", "url": "https://www.law.cornell.edu/uscode/text/26/6651"},
   {"title": "IRS – Payment plans and installment agreements (setup fees)", "url": "https://www.irs.gov/payments/payment-plans-installment-agreements"},
   {"title": "IRS – Understanding a federal tax lien", "url": "https://www.irs.gov/businesses/small-businesses-self-employed/understanding-a-federal-tax-lien"},
   {"title": "26 U.S.C. 6330 (notice and hearing before levy, 30 days)", "url": "https://www.law.cornell.edu/uscode/text/26/6330"},
   {"title": "IRS – Time IRS can collect tax (10 years)", "url": "https://www.irs.gov/filing/time-irs-can-collect-tax"},
   {"title": "IRS – Revocation or denial of passport in cases of certain unpaid taxes ($66,000 for 2026; CP508C)", "url": "https://www.irs.gov/businesses/small-businesses-self-employed/revocation-or-denial-of-passport-in-cases-of-certain-unpaid-taxes"}
  ],
  "question": "Is there a letter in your house right now that you haven't opened yet?",
  "pinned_comment": "Be honest: is there an envelope in your house right now that you haven't opened? (Roommates: which button do you press?)",
  "hashtags": ["#irs", "#lawexplained", "#taxes"],
  "playlist": "What Really Happens After... (Every Stage, U.S. Law Explained)",
  "chapters_note": "kapitel = 'chapter'-fälten (Level 1: The envelope … Level 10: The man on the bench, The end: What it cost)"
 },
 "thumb": {
  "kind": "dac_semireal",
  "klickfraga": "Ett IRS-kuvert säger att någon betalade dig $21 400 som du aldrig redovisat – vem var det, och vad händer på varje nivå om du lägger brevet i en skokartong?",
  "hot_i_bild": "Det öppnade IRS-kuvertet med CP2000-brevet, jättestort i förgrunden (vänster halva) med beloppet $6,420 synligt på papperet; hjälten stor i höger tredjedel (≈60 % av höjden) i köket, chockad, och skokartongen 'TAXES?' på kylskåpet bakom.",
  "hjalte_andel": 60, "textord": 3,
  "skiljer_sig": "Förra DAC (dac-26, Mexiko): utomhus i starkt dagsljus, två bilar och en polis, texten '48 HOURS'. Före det (K2lPH0w1HYk): butik, röd väst, '$38.47'. Nu: inomhus i ett varmt lägenhetskök, ETT föremål (brevet) som hot i stället för en person, och en frist ('30 DAYS') i stället för ett belopp eller timmar.",
  "jamfor_ark": "chk/jamfor-dac-2026-11-27.png",
  "jamfor_mot": ["DqyGPrK3LGQ (Baldy POV, Every Pilot Rank)", "Your Life at Every Level of Living Off the Grid (Honest Life POV, 678 751 – Action 23/11)", "K2lPH0w1HYk (vår självkasse-video)"],
  "forsta_scen_matchar": "Scen 1 (0–6 s) är miniatyr A i rörelse: samma kök (apt_kitchen), hjälten med det öppnade IRS-brevet där $6,420 syns, kylskåpet med skokartongen 'TAXES?' och hyrestavlan i bakgrunden.",
  "soktest": "D0 från WebSearch 27/11 + sökförslag: ingen video med titeln 'Your Life at Every Level of an IRS Letter' hittades; närmaste förslag gäller audits ('what happens when you get audited'). YouTube-topplistan kunde inte läsas från molnet – render-körningen gör om D0/C3 i Chrome.",
  "variants": [
   {"id": "A", "layout": "IRS-brevet jättestort till vänster (beloppet $6,420 på papperet), hjälten stor i höger tredjedel, text uppe till vänster", "text": "LEVEL 1", "label": "30 DAYS (gul undertitel)", "scene": "varmt upplyst lägenhetskök på eftermiddagen, kylskåp med whiteboard (två gröna bockar) och skokartong 'TAXES?'; hjälten (grå henley) chockad; inga logotyper utom texten INTERNAL REVENUE SERVICE på kuvertet"},
   {"id": "B", "layout": "ANNAN bild: telefonskärm jättestor i förgrunden med en lista av betalningar 'GOODS & SERVICES', hjälten liten och pekar", "text": "LEVEL 6", "label": "WRONG BUTTON (gul)", "scene": "skrivbord vid fönstret på kvällen, laptop och telefon"},
   {"id": "C", "layout": "ANNAN bild: brevbäraren håller fram en signaturskärm, tjockt kuvert med 'NOTICE OF DEFICIENCY'", "text": "90 DAYS?", "label": None, "scene": "trappan utanför huset i oktober, löv (DAC får ha fråga)"}
  ]
 },
 "forbattring": {
  "forra_videon": "Senast publicerade DAC: K2lPH0w1HYk 'Your Life at Every Level of a $38 Self-Checkout Arrest' (26/11 00:30) – 1 exponering vid 2 h-kontrollen enligt PUBLICERAT_2026-11-25; b1w06aHERrc 3 exp på 14 h. dac-26 (Mexiko) är skriven men ännu inte publicerad. DAC 28 d (TITTARTID_ANALYS 23/11): 663 exp, 3,8 % CTR, 4:37 snitt.",
  "problem": "De senaste DAC-videorna får nästan inga exponeringar; ämnena (en delstats regler, ett gripande) är smala och skrämmer bort annonsörer och tittare som inte känner igen sig.",
  "andring": "Ett ämne som gäller alla amerikaner i alla delstater (federal skatt, IRS, U.S. Tax Court) och som miljontals får i brevlådan (CP2000), med en vardaglig orsak som tittaren kan känna igen (rumskamraten som trycker 'goods and services' i betalappen). Två klockor (30 och 90 dagar) i stället för en, och en gåta ($21 400 – vem betalade dig?) som löses av ett föremål från första bilden (hyrestavlan på kylskåpet).",
  "forvantat": "CTR ≥ 4 % (IRS-brev + belopp + trendtitel), ≥ 55 % kvar vid 0:30, ≥ 35 % vid 2:00, snittvisning ≥ 5:00; högre RPM än brottsämnena (skatt/privatekonomi).",
  "referens": "Honest Life POV 'Your Life at Every Level of Living Off the Grid' (678 751 visningar, månad, Action 23/11) + Baldy POV DqyGPrK3LGQ. Transkript kunde inte hämtas: ingen Chrome i molnkörningen (youtube-transcriber kräver den) och vidIQ användes inte. Kroken 0/5/10/20/30 s enligt DAC_STANDARD 2 och FORMAT_BLUEPRINT DAC: 0 s föremål + insats i du-form ($6 420, 30 dagar), ~6 s klockan går redan, ~12 s en annan person reagerar, ~17 s löftet, ~22 s gåtan, ~30 s motivet (hyrestavlan).",
  "vi_slår_den_med": "Verkliga frister och belopp som tittaren kan använda samma dag (30 dagar på CP2000, 90 dagar som domstolen inte kan förlänga, $60, $50 000-gränsen, 0,5 %/0,25 %/1 %, $0–$178 i planavgift, 10 år, $66 000) – 20 öppnade källor med paragraf på skärmen; plus ett twistslut där samma regel som gav straffavgiften tar bort den ($5 000-gränsen).",
  "trend": {
   "fras": "your life at every level of + what happens when you get audited / what happens if you don't pay taxes",
   "kalla": "Egen analys 27/11 (TREND_2026-11-27 saknades): YouTubes sökförslag via suggestqueries (web-fetch) + TREND_2026-11-26 (Action-siffror 23/11).",
   "trendvideo": "Your Life at Every Level of Living Off the Grid – Honest Life POV – 678 751 (månad); Your Life at Every Level of Financing a $71,850 Backyard Pool – Mr.Beanie – 17 021 (vecka) (pengar + 'Every Level'-mallen)",
   "andrat": "'Your Life at Every Level of …' i ett pengar/juridik-ämne med belopp i titeln (som poolvideon), flyttat till IRS-brevet. Titeln 'Your Life at Every Level of a $6,420 IRS Letter' valdes bort: titellikhet 0,70 mot dac-23 (originalitet.py max 0,70)."
  }
 },
 "experiment": {"variable": "federalt vardagsämne (IRS-brev) i stället för ett gripande/en delstat", "metric": "CTR, exponeringar, 0:30-andel, snittvisning", "decide_at": "48 h + jämförelse mot K2lPH0w1HYk och dac-26"},
 "hooks_kandidater": {
  "A_vald": "An IRS envelope on your counter says you owe 6,420 dollars, and 30 days to answer. (stakes + countdown; föremålet i miniatyren; siffror inom 3 s)",
  "B": "Somebody told the IRS they paid you 21,400 dollars, and you've never heard of them. (curiosity gap – starkare gåta men inget föremål i bild; används som scen 5–6)",
  "C": "A CP2000 isn't a bill. That's the first thing nobody tells you about it. (contradiction – abstrakt, första bilden blir ett kort; kommer som real-kort vid ~0:40)",
  "val": "A – miniatyrens scen från bildruta 0, belopp + frist inom 3 s, löftet vid ~17 s; B blir gåtan vid ~22 s, C första regeln vid ~40 s."
 },
 "standard_check": {
  "miniatyr": "FORMAT_BLUEPRINT DAC: 'LEVEL 1' vit + gul undertitel '30 DAYS', halvrealistisk man ≈60 % höjd i höger tredjedel, 3 ord; hotet (brevet med $6,420) störst; ljus inomhusmiljö; B/C andra bilder. Texten upprepar inte titeln (titeln har beloppet, bilden fristen).",
  "krok": "du-form från första meningen; föremål + belopp + frist inom 3 s; ingen presentation de första 12 s; löftet i klartext ~17 s; gåtan ~22 s; första verkliga regeln (CP2000 = proposal, IRS) ~40 s och note_card ~17 s.",
  "nivåer": "10 nivåer + slut: The envelope, The math, The shoebox, The signature, The court nobody mentions, The app, The other side, The new number, The plan, The man on the bench, What it cost – varje nivå: första ögonblick → svårast → verklig regel → insidersanning → känsloslag.",
  "motiv": "skokartongen 'TAXES?' på kylskåpet (nivå 1, 3, 4, 9, slutet: bara kvittot 'DAY 52' kvar), hyrestavlan 'JULES PAID / DEV PAID' (0:30, nivå 6 där gåtan löses, nivå 9 'USE: FRIENDS', slutet), brevet vikt i tredjedelar (nivå 3 och 4), bröllopen (nivå 3, 7, 9, Walt).",
  "slut": "gåtan löst (Jules hyra markerad 'goods and services'), $17 500 struken men $3 900 riktig inkomst, straffavgiften faller på samma $5 000-regel som skapade den; Walt som den värre versionen (panträtt, 30 dagar före utmätning, 10 år, passet vid $66 000); cykeln: nya rumskamraten Priya tvekar vid samma knapp, alla pekar på tavlan; fråga till tittaren.",
  "källor": "20 källor i beskrivningen; källrad på varje real/label-kort.",
  "miljöer": "apt_kitchen, wedding_barn, desk_room, front_stoop, post_office, federal_lobby",
  "tittartid": "första 30 s: 6 helbildsscener i köket (alla med walk_to), ingen medium/närbild, byte var ~4,5–6 s; första note_card ~17 s, första real-kort ~40 s.",
  "innehall": {
   "snittord_per_say": round(sum(words) / len(words), 1),
   "say_under_6_ord": sum(1 for w in words if w < 6),
   "say_under_6_ord_kommentar": "nivåkortens repliker ('Level six. The app.') – under 1 per minut",
   "faktaskyltar": nf, "verkliga_regelkort_real": nreal, "storsta_lucka_s": round(gap, 1),
   "kommentar": f"Beräknat med granskning.py:s tempo (2,6 ord/s + 0,45 s). Faktaskylt = real/label/board/plan/daycard eller note_card. Längd ≈{dur / 60:.1f} min."
  }
 },
 "notes": {
  "påhittat": "alla personer (du, Jules, Dev, farbrodern, brevbäraren Rosa, Theresa, posttjänstemannen, Mr. Abara, Walt, Priya), betalappen 'Payment Apps Inc.', beloppen ($6 420, $5 350, $1 070, $21 400, $17 500, $3 900, $1 170, $800-hyran, +$350), 214 rader, 11 bröllop, datumen (AUG 8, dag 52, DEC 2), målnumret 0412-S, Lissabon.",
  "uträkningar": "$5 350 × 20 % = $1 070; $5 350 + $1 070 = $6 420; $5 350 − $5 000 = $350; $21 400 − $3 900 = $17 500; 25 % av $1 170 = $292,50; 12 × $800 = $9 600 (bara på skärmen, ingen summa påstås).",
  "osäkert": "Skattebeloppen ($5 350 på $21 400, $1 170 på $3 900) är påhittade och inte uträknade med skattetabeller – manuset nämner aldrig någon skattesats. Att $5 350 överstiger gränsen förutsätter att 10 % av rätt skatt är under $5 000 (hjältens skatt < $50 000) – rimligt för en bröllopsfotograf men inte sagt. 'Office of Chief Counsel' företräder IRS i Tax Court (allmänt känt, ingen öppnad källa citeras på skärmen). Avgiften 0,5 % gäller efter räkningen (6651(a)(3) för underskott efter notice and demand) – manuset säger 'can start'. 0,25 % gäller bara den som lämnat deklarationen i tid (sägs). 'Stipulated decision' i ett S case är berättelse. 1099-K-gränsen $20 000/200 gäller för 2025 enligt IRS (OBBB återinförde den retroaktivt). Räntan 7 % är Q4 2026 (IR-2026-98) – sägs som 'in late 2026'.",
  "motor": "Nya bakgrunder (fallback inom parentes): apt_kitchen – varmt lägenhetskök med kylskåp (whiteboard-text + skokartong 'TAXES?' ovanpå), bänk, fönster (MÅSTE finnas: scen 1 + miniatyr A; fallback keisha_kitchen/sister_kitchen), wedding_barn – ladugård med ljusslingor (fallback cafe), desk_room – skrivbord med laptop och väggkalender (fallback apartment), front_stoop – trappa utanför flerfamiljshus med löv (fallback front_door), post_office – postdisk (fallback bank), federal_lobby – federal byggnad med bänk och säkerhetskontroll (fallback court_hall). Rekvisita: envelope (text med '|'), fridge (whiteboard, shoebox), shoebox (text, open), camera_bag, wall_calendar (text), receipt, stamp; letter/laptop/phone finns. hero holding: letter/phone/camera. Bifigurer: Jules (gul, lockigt hår), Dev (grön, glasögon), farbror (kostym, grått hår), Rosa (blå, keps, knut), Theresa (bara telefon), posttjänsteman (navy), Walt (brun, grått hår, glasögon), Priya (röd, långt hår). sfx: paper, click. 10 nivåkort som daycard. Inga Shorts.",
  "humanizer": "humanizer:humanizer-reglerna tillämpade på alla say 27/11: inga tankstreck, inga 'Here's the thing'/'Let's dive in', inga tretal av adjektiv, inga 'not X but Y'-aforismer utom där regeln själv säger det ('a proposal, not a bill' är IRS ord); siffror, källor och fakta oförändrade.",
  "research": "27/11: tre web-fetch-underagenter (alla sidor HTTP 200): irs.gov (CP2000-sidan, Topic 652, 1099-K-sidan + FAQ, accuracy-related penalty, failure to pay penalty, IR-2026-98, payment plans, passport, time IRS can collect, federal tax lien), ustaxcourt.gov (petitioners-start, fees-and-charges, petitioners-about, case-procedure), Cornell LII (26 U.S.C. 6212, 6213, 6330, 6651, 6662) och YouTubes sökförslag (suggestqueries). Citat finns i körningens logg; inget belopp i en real/label-ruta kommer från annat än dessa sidor.",
  "spärrar": "27/11 ~23:00: originalitet.py GODKÄNT mot dac-26, dac-25 (kompakt kopia av projektfilen: titel + say + bildtyp/plats), dac-24, dac-23 (dac-21/20 fanns inte lokalt – render-körningen kör igen mot dem): fraser ≤ 0,1 %, titel ≤ 0,63, upplägg ≤ 0,25, slut ≤ 0,15. granskning.py GODKÄNT utom thumb.jamfor_ark (chk/jamfor-dac-2026-11-27.png – skapas vid rendering; varning 10 nivåkort). monetisering.py GODKÄNT (varning 49 % scene). B4 (tittartidsgranskning): inga luckor > 30 s utan faktaskylt (största 27 s), inga meningar > 25 ord, första bilden = miniatyrens scen.",
  "publicering": "Reserv för DAC:s nästa L3. KÖ_ÄNDRING_2026-11-27_FORSENAT säger att DAC inte är i rotationen för 28/11, och dac-26 (Mexiko) väntar redan – driften bestämmer ordningen.",
  "render_kontroll": "(a) Mätrad-mallen (TITTARTID_REGLER SATSNINGSTILLÄGG p. 2) ifylld i PUBLICERAT före uppladdning; (b) gäller LS/STE – för DAC: ljushet och hjälte mäts ändå och skrivs i Mätraden; (c) teckenkontroll 7.8 (pilar, ≤ ≥, bockar m.fl.) före rendering – manuset är skrivet utan sådana tecken (bockar = 'PAID', pil = 'USE: FRIENDS'), antal ersatta i Mätraden; (d) gäller QM; (e) disclaimern finns kvar i den uppladdade beskrivningen; (f) inga Shorts för DAC; (g) SATSNING-raden."
 }
}
json.dump(m, open("manus/dac-2026-11-27.json", "w"), ensure_ascii=False, indent=1)
print(m["standard_check"]["innehall"])
