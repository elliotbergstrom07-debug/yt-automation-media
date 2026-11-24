"""Monetiseringsspärr – körs före varje publicering, efter granskning.py.

  python3 monetisering.py manus/qm-2026-11-15.json [ut/qm-2026-11-15.png]

Mål: inget i kanalen ska kunna läsas som "inauthentic content" (YouTube, juli 2025/2026):
  1. generiskt/repetitivt innehåll  2. otillfredsställande innehåll  3. AI-personor kring känsliga ämnen.
YouTube bedömer HELA kanalen (formatlikhet, upprepning, minimal redigering), så varje manus jämförs
med kanalens tidigare manus. Avslutar med kod 1 om något är UNDERKÄNT – då publiceras inget.
Regler: automation/MONETISERING.md.
"""
import glob, json, os, re, sys
from collections import Counter

PREFIX = {"Last Shift": "ls", "The Quiet Math": "qm", "Survive the Era": "ste"}
ADVICE = re.compile(r"\b(you should (buy|invest|sell)|buy (this|these|now)|guaranteed (return|profit)s?|risk[- ]free|get rich|financial advice:)\b", re.I)
GORE = re.compile(r"\b(?<!letting )(blood(?![- ]?letting)|bloody|gore|guts|decapitat\w*|dismember\w*)\b", re.I)

def words(m):
    return re.findall(r"[a-z']+", " ".join(s.get("say", "") for s in m["scenes"]).lower())

def grams(w, n=5):
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}

def vseq(m):
    return [s.get("visual", {}).get("type", "?") for s in m["scenes"]]

def seq_sim(a, b):
    import difflib
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()

def previous(path, m):
    p = PREFIX.get(m.get("channel"), os.path.basename(path).split("-")[0])
    short = "short" in os.path.basename(path)
    out = []
    for f in sorted(glob.glob(f"{os.path.dirname(path) or '.'}/{p}-*.json")):
        if os.path.abspath(f) == os.path.abspath(path) or ("short" in os.path.basename(f)) != short:
            continue
        try:
            out.append((f, json.load(open(f))))
        except Exception:
            pass
    return out[-14:]

def check(path, thumb=None):
    m = json.load(open(path)); bad, warn = [], []
    w = words(m); g = grams(w); seq = vseq(m)
    seo = m.get("seo", {}); title = (seo.get("title") or m.get("title") or "").lower()
    first = " ".join(w[:25])
    for f, o in previous(path, m):
        ow = words(o); og = grams(ow)
        if g and og:
            ov = len(g & og) / len(g)
            if ov > 0.12:
                bad.append(f"{ov:.0%} av manusets 5-ordsfraser finns redan i {os.path.basename(f)} – skriv om (max 12 %)")
        if first and first == " ".join(ow[:25]):
            bad.append(f"samma öppning som {os.path.basename(f)}")
        ot = (o.get("seo", {}).get("title") or o.get("title") or "").lower()
        if title and ot and seq_sim(title.split(), ot.split()) > 0.7:
            bad.append(f"titeln är för lik \"{ot}\" ({os.path.basename(f)})")
        s = seq_sim(seq, vseq(o))
        if s > 0.8:
            bad.append(f"bildföljden är {s:.0%} lik {os.path.basename(f)} – samma mall igen (max 80 %); byt ordning/typer")
        elif s > 0.65:
            warn.append(f"bildföljden är {s:.0%} lik {os.path.basename(f)}")
    if seq and m.get("style") == "sm":
        # berättarkanaler: berättelser ÄR scener (även hos konkurrenterna) – upprepningsrisken är samma plats + samma utsnitt
        vis = [s.get("visual", {}) for s in m["scenes"]]
        locs = Counter(v.get("location") for v in vis if v.get("location"))
        keys = [(v.get("type"), v.get("location"), v.get("shot")) for v in vis]
        run = best = 1
        for a, b in zip(keys, keys[1:]):
            run = run + 1 if a == b else 1; best = max(best, run)
        if len(locs) < 3:
            bad.append(f"bara {len(locs)} platser i hela videon – minst 3 (annars ser varje minut likadan ut)")
        elif locs.most_common(1)[0][1] / sum(locs.values()) > 0.6:
            l, n = locs.most_common(1)[0]
            warn.append(f"{n / sum(locs.values()):.0%} av bilderna på \"{l}\" – sprid berättelsen över fler platser")
        if best > 4:
            bad.append(f"{best} bilder i rad med samma plats + samma utsnitt – byt utsnitt (wide/medium/close/closeup) minst var 4:e bild")
        if len(set((k[0], k[2]) for k in keys)) < 4:
            bad.append("för få bildutsnitt – blanda wide, medium, close, closeup och kartor/kort")
    elif seq:
        typ, n = Counter(seq).most_common(1)[0]
        share = n / len(seq)
        if share > 0.5:
            bad.append(f"{share:.0%} av scenerna är \"{typ}\" – ser mallgjort ut (max 50 %, helst < 35 %)")
        elif share > 0.35:
            warn.append(f"{share:.0%} av scenerna är \"{typ}\" – variera mer (< 35 %)")
        if len(set(seq)) < 5 and len(seq) > 20:
            bad.append(f"bara {len(set(seq))} bildtyper i hela videon – minst 5")
    allsay = " ".join(s.get("say", "") for s in m["scenes"])
    if GORE.search(allsay) or GORE.search(title):
        bad.append(f"blod/gore i texten (\"{GORE.search(allsay + ' ' + title).group(0)}\") – inte tillåtet (annonsvänlighet)")
    if m.get("channel") == "The Quiet Math":
        if ADVICE.search(allsay):
            bad.append(f"låter som finansiell rådgivning: \"{ADVICE.search(allsay).group(0)}\"")
        if not seo.get("disclaimer"):
            bad.append("QM saknar disclaimer (inte finansiell rådgivning) i beskrivningen")
        if not seo.get("sources"):
            bad.append("QM saknar källor – varje siffra ska gå att spåra")
    if m.get("channel") == "Survive the Era" and not seo.get("sources"):
        warn.append("STE saknar källor i beskrivningen – lägg till 2–3 historiska källor")
    minlen = 60 if "short" in os.path.basename(path) else 120
    desc = seo.get("summary") or seo.get("description") or ""
    if len(desc) < minlen:
        bad.append(f"beskrivningen är tom eller för kort (< {minlen} tecken) – skriv en unik sammanfattning av just den här videon")
    fb = m.get("forbattring") or {}
    if not fb.get("andring"):
        warn.append("forbattring.andring saknas – dokumenterad mänsklig/kreativ förändring per video stärker att kanalen inte är massproducerad")
    if thumb and os.path.exists(thumb):
        try:
            import skia, numpy as np
            def h(p):
                a = skia.Image.open(p).resize(16, 9).toarray()[..., :3].mean(axis=2)
                return a > a.mean()
            me = h(thumb); p = PREFIX.get(m.get("channel"), "")
            for f in sorted(glob.glob(f"ut/**/{p}*.png", recursive=True))[-30:]:
                if os.path.abspath(f) != os.path.abspath(thumb) and (h(f) != me).mean() < 0.08:
                    bad.append(f"thumbnailen är nästan identisk med {f}")
                    break
        except Exception as e:
            warn.append(f"kunde inte jämföra thumbnails: {e}")
    return bad, warn

if __name__ == "__main__":
    bad, warn = check(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    for b in bad: print("UNDERKÄNT:", b)
    for x in warn: print("VARNING:", x)
    print("GODKÄNT" if not bad else f"{len(bad)} fel")
    sys.exit(1 if bad else 0)
