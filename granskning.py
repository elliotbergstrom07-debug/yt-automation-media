"""Kvalitetsspärr före rendering/publicering – krok (tittartid) och thumbnail (klickfrekvens).

  python3 granskning.py manus/ls-2026-11-13.json            # granskar manusets första minut
  python3 granskning.py --thumb ut/ls-2026-11-13.png sm      # granskar thumbnail (sm = stickman, qm = Quiet Math)

Avslutar med kod 1 om något UNDERKÄNT finns. Del A ska skriva om manuset tills det går igenom;
del B renderar inte ett underkänt manus och publicerar inte en underkänd thumbnail.
Regler: LÄRDOMAR.md "Tidiga signaler" + TILLVÄXT.md avsnitt 4 + MÅLPLAN.md avsnitt 6 (förbättringsblocket).
"""
import os
import json, re, sys

WPS = 2.6  # ord per sekund i berättarrösten (uppmätt ~2,5–2,7)
FLASHBACK = re.compile(r"\b(ago|earlier (that|this)|hours? before|the night before|yesterday|let me back up|rewind|flashback|it started)\b", re.I)
STAKES = re.compile(r"\b(\d+|one|two|three|four|five|ten|thirty|hundred)\b.*\b(days?|seats?|hours?|people|survivors?|chances?|minutes?|left|only)\b", re.I)

def check_manus(path):
    m = json.load(open(path)); style = m.get("style", "qm")
    bad, warn, t, flashbacks = [], [], 0.0, []
    first8, first30, scenes30, moving, long_lines = "", [], 0, 0, 0
    for s in m["scenes"]:
        say = s.get("say", "").strip(); n = len(say.split()); dur = max(n / WPS + 0.45, 2.0)
        if t < 8: first8 += " " + say
        if t < 60 and FLASHBACK.search(say):
            msg = f"tillbakablick vid ~{t:.0f}s: \"{say[:70]}\""
            if t < 8:
                bad.append(msg + " – första 8 s ska vara nuet + insatsen")
            else:
                flashbacks.append(msg)
        if t < 30:
            scenes30 += 1
            if n > 16: long_lines += 1
            v = s.get("visual", {})
            if v.get("type") != "scene" or any(k in v for k in ("zombies_in", "snowfall")) or "walk_to" in (v.get("hero") or {}) \
               or any("walk_to" in f for f in v.get("friends", [])) or v.get("type") in ("number", "bars", "compare", "iceberg", "network", "price"):
                moving += 1
        t += dur
    sc30, tt = [], 0.0
    for s in m["scenes"]:
        if tt >= 30: break
        sc30.append(s); tt += max(len(s.get("say", "").split()) / WPS + 0.45, 2.0)
    vis30 = [s.get("visual", {}) for s in sc30]
    nonwide = [v for v in vis30 if v.get("type") in ("scene", "closeup") and (v.get("type") == "closeup" or v.get("shot", "medium") != "wide")]
    if len(nonwide) > 1:
        bad.append(f"{len(nonwide)} scener med 'medium'/närbild första 30 s – max 1. Resten 'shot': 'wide' (helfigur i miljön, hotet/insatsen syns) – TITTARTID_REGLER.md 2")
    v0 = vis30[0] if vis30 else {}
    if style == "sm":
        if not any(v0.get(k) for k in ("window_dead", "dead", "zombies_in", "threat", "fire", "wave", "flood", "avalanche", "crowd")):
            bad.append("första scenen visar inget hot – den ska vara miniatyrens scen i rörelse (samma plats, samma hot) – TITTARTID_REGLER.md 1")
    elif v0.get("type") != "scene":
        bad.append(f"första bilden är '{v0.get('type')}' – den ska vara miniatyrens scen (figuren i miljön med insatsen synlig), inte tavla/kort/närbild – TITTARTID_REGLER.md 1")
    th0 = (m.get("thumb") or {}).get("forsta_scen_matchar")
    if not th0:
        bad.append("thumb.forsta_scen_matchar saknas – skriv hur första bilden (0–3 s) visar exakt det miniatyren lovar – TITTARTID_REGLER.md 1")
    expo = re.compile(r"\b(you'?re the|you are the|you are a|you'?re a|zombie outbreak\.|this is the quiet math|this is day after court)\b", re.I)
    first12 = " ".join(s.get("say", "") for s in sc30[:3])
    if expo.search(first12):
        bad.append(f"presentation/exposition de första ~12 s (\"{expo.search(first12).group(0)}\") – börja med handling, presentera vem du är efter första händelsen – TITTARTID_REGLER.md 3")
    nmin = max(1.0, sum(max(len(s.get("say", "").split()) / WPS + 0.45, 2.0) for s in m["scenes"]) / 60)
    types = [s.get("visual", {}).get("type") for s in m["scenes"]]
    ch = m.get("channel", "")
    if True:
        nclose = types.count("closeup")
        if nclose > nmin:
            bad.append(f"{nclose} 'closeup' (jättehuvud) på {nmin:.0f} min – max 1 per minut; vinnarna visar figuren i miljön – KONKURRENT_DJUPANALYS.md")
    if ch == "Day After Court" and types.count("board") > nmin / 3:
        bad.append(f"{types.count('board')} tavlor på {nmin:.0f} min – max 1 per 3 min; referensen (Baldy POV) har ingen text i bild, bara miljöer – säg siffran i berättelsen och visa den på ett föremål (brev, skylt, telefon)")
    if ch == "The Long If" and types.count("board") > nmin / 2:
        bad.append(f"{types.count('board')} tavlor på {nmin:.0f} min – max 1 per 2 min (DOOMPERK: ett kort per nivå, resten miljö och kameravinklar)")
    th = m.get("thumb") or {}
    for k, why in (("klickfraga", "EN mening: vad missar tittaren om hen inte klickar? (måste synas i bilden på 1 sekund)"),
                   ("hot_i_bild", "vad är det STÖRSTA i bilden – hotet/insatsen, inte gubben"),
                   ("skiljer_sig", "hur layouten skiljer sig från kanalens förra miniatyr (inte samma mall)"),
                   ("jamfor_ark", "sökväg till jamfor.py-arket mot 2–3 vinnare i 168×94")):
        if not str(th.get(k, "")).strip():
            bad.append(f"thumb.{k} saknas – {why}")
    if th.get("jamfor_ark") and not os.path.exists(th["jamfor_ark"]):
        bad.append(f"thumb.jamfor_ark finns inte: {th['jamfor_ark']}")
    fb = m.get("forbattring") or {}
    if not all(fb.get(k) for k in ("forra_videon", "problem", "andring", "forvantat")):
        bad.append("blocket \"forbattring\" saknas eller är ofullständigt (MÅLPLAN.md avsnitt 6) – varje video ska ha en dokumenterad förbättring mot förra videon")
    if not (fb.get("referens") and fb.get("vi_slår_den_med")):
        bad.append("forbattring.referens och forbattring.vi_slår_den_med saknas – varje video ska slå dagens referensvideo (BERÄTTELSE.md, 'Slå konkurrenten')")
    if len(flashbacks) > 1:
        bad.append(f"{len(flashbacks)} tillbakablickar första minuten – högst EN mening bakgrund, sedan nuet (KONKURRENTER.md)")
    elif flashbacks:
        warn.append(flashbacks[0] + " – ok som EN mening, men nästa scen måste vara tillbaka i nuet")
    if not STAKES.search(first8):
        bad.append(f"premiss/insats saknas de första 8 s (\"{first8.strip()[:90]}\") – säg vad som står på spel med en siffra")
    if scenes30 < 6:
        bad.append(f"bara {scenes30} scener första 30 s – byt bild var 3–5 s (minst 6)")
    if long_lines:
        warn.append(f"{long_lines} repliker > 16 ord första 30 s – korta dem")
    if scenes30 and moving / scenes30 < 0.6:
        bad.append(f"för lite rörelse första 30 s ({moving}/{scenes30} scener) – lägg walk_to / zombies_in / snowfall")
    allsay = " ".join(s.get("say", "") for s in m["scenes"])
    words = len(allsay.split()); minutes = words / WPS / 60
    lim = {"sm": (1300, 2100), "qm": (1100, 1900)}.get(style, (1100, 2100))
    if style == "sm" and m.get("voice") == "bm_fable":
        lim = (1500, 2400)
    if m.get("channel") in ("Day After Court", "The Long If"):
        lim = (2000, 2800)
    if m.get("channel") == "Last Shift":
        lim = (1100, 1500)
    if m.get("standard") == "QM_STANDARD":
        lim = (2400, 3500)
    import re as _re
    seo = m.get("seo", {}); title = (seo.get("title") or "").strip(); tl = title.lower()
    if len(title) > 60:
        bad.append(f"titeln är {len(title)} tecken – max 60 (syns hel i förslagslistan på mobil)")
    if m.get("channel") == "Last Shift":
        if tl.startswith("zombie outbreak"):
            bad.append("titeln börjar med \"Zombie Outbreak\" – nischen är full av kloner med exakt den starten (minst 7 \"30 Days … Supermarket\" senaste månaden); tittaren tror att hen redan sett den")
        if _re.search(r"\b\d+ days (trapped|locked) (in|inside|on)( a| an| the)? (supermarket|grocery|school|mall|30th floor|rooftop|basement|stadium|costco)", tl):
            bad.append("titeln kopierar en konkurrents plats + mall – välj en arbetsplats och ett fysiskt problem som ingen annan har")
    if not lim[0] <= words <= lim[1]:
        bad.append(f"{words} ord ≈ {minutes:.1f} min – ska vara {lim[0]}–{lim[1]} ord (vinnarna är 8–11 min, MÅLPLAN/KONKURRENTER)")
    full = [s for s in m["scenes"] if s.get("visual", {}).get("type") in ("fact", "inventory")]
    if len(full) > max(1, int(minutes / 4)):
        bad.append(f"{len(full)} helskärmskort (fact/inventory) – högst 1 per 4 min; säg fakta som EN mening i berättelsen i stället (vinnarna har inga faktarutor)")
    days = [s for s in m["scenes"] if s.get("visual", {}).get("type") == "daycard"]
    if len(days) > 7:
        warn.append(f"{len(days)} dagkort – varje svart kort är ett utgångsläge för tittaren; använd dag-märket i hörnet i stället")
    nums = len(re.findall(r"\b\d[\d,.:]*\b", allsay))
    if nums < minutes * 3:
        warn.append(f"bara {nums} siffror (≈{nums / max(minutes, 1):.1f}/min) – vinnarna har 4–8 konkreta siffror per minut (40 000 produkter, 90 minuter, 1 ton) – skriv siffror med siffror")
    if style == "sm" and len(re.findall(r"\b(first|second|third|fourth|fifth|new|next) problem\b", allsay, re.I)) < 3:
        warn.append("saknar numrerade problem (\"First problem, the glass.\") – vinnarnas ryggrad: varje block = problem → lösning med platsens egna saker → ny komplikation")
    beats = m.get("beats") or []
    if not beats:
        bad.append("\"beats\" saknas – skriv händelselistan FÖRST (automation/BERÄTTELSE.md): [{\"t\": \"0:00\", \"typ\": \"hot|lösning|vändning|gåta|människor|humor|callback\", \"text\": \"…\"}]")
    else:
        def sec(x):
            p = str(x.get("t", "0:00")).split(":"); return int(p[0]) * 60 + int(p[1]) if len(p) == 2 else 0
        need = int(minutes * 2.5)
        if len(beats) < need:
            bad.append(f"bara {len(beats)} händelser – minst {need} (≈ en var 20–25:e sekund, som vinnarna)")
        gaps = [sec(b) - sec(a) for a, b in zip(beats, beats[1:])]
        if gaps and max(gaps) > 45:
            i = gaps.index(max(gaps))
            bad.append(f"{max(gaps)} s utan ny händelse efter {beats[i].get('t')} – max 45 s")
        hot = [b for b in beats if b.get("typ") in ("hot", "vändning")]
        if not hot or sec(hot[0]) > 10:
            bad.append("första hotet ska komma inom 10 s")
        hook = [b for b in beats if b.get("typ") in ("hot", "vändning", "gåta")]
        hgaps = [(sec(b) - sec(a), a.get("t")) for a, b in zip(hook, hook[1:])]
        if hook and minutes * 60 - sec(hook[-1]) > 90:
            hgaps.append((minutes * 60 - sec(hook[-1]), hook[-1].get("t")))
        for g, t0 in hgaps:
            if g > 90:
                bad.append(f"{g:.0f} s utan återkrok (hot/vändning/gåta) efter {t0} – max 90 s")
                break
        early = [b for b in hot if sec(b) <= minutes * 60 * 0.35]
        if len(early) < 4:
            bad.append(f"bara {len(early)} hot/vändningar i första tredjedelen – hotet ska trappas upp tidigt (vinnarna: 200 zombier vid 3:35, strömmen tillbaka och 300 vänder sig vid 5:17)")
        if style == "sm" and not any(b.get("typ") == "människor" and 0.45 <= sec(b) / max(minutes * 60, 1) <= 0.75 for b in beats):
            warn.append("inga \"människor\"-händelser i mitten (45–75 %) – andra överlevande som både hot och hopp")
        for typ in ("gåta", "callback"):
            if not any(b.get("typ") == typ for b in beats):
                warn.append(f"ingen \"{typ}\"-händelse – vinnarna har en gåta som avslöjas bit för bit och ett callback-slut")
    first60 = allsay[: int(60 * WPS * 6)]
    if not re.search(r"\b(on day|by day|until day|day \d+|the end|last|final|only one|gets out|survive)\b", first60[:1200], re.I):
        warn.append("inget löfte om slutet de första ~30 s (\"…and on day 30 …\")")
    return bad, warn

def check_thumb(path, style):
    import skia, numpy as np
    img = skia.Image.open(path); a = img.toarray()[..., :3].astype(float) / 255
    lum = (0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2])
    bad, warn = [], []
    if True:
        if lum.mean() < 0.25:
            bad.append(f"för mörk thumbnail (ljushet {lum.mean():.2f} < 0.25) – hjälten och hotet måste synas i 168×94")
        if lum.std() < 0.2:
            warn.append(f"låg kontrast ({lum.std():.2f})")
    small = img.resize(168, 94).toarray()[..., :3].astype(float) / 255
    if small.std() < 0.15:
        bad.append("thumbnailen flyter ihop i liten storlek (168×94) – större motiv/text")
    return bad, warn

if __name__ == "__main__":
    a = sys.argv[1:]
    bad, warn = check_thumb(a[1], a[2] if len(a) > 2 else "sm") if a[0] == "--thumb" else check_manus(a[0])
    for b in bad: print("UNDERKÄNT:", b)
    for w in warn: print("VARNING:", w)
    print("GODKÄNT" if not bad else f"{len(bad)} fel")
    sys.exit(1 if bad else 0)
