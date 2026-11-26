"""Originalitetsspärr (YouTube 'inauthentic content', förtydligad juli 2026).
python3 originalitet.py manus/ny.json manus/gammal1.json manus/gammal2.json ...
"""
import json, re, sys
from difflib import SequenceMatcher

PERSONA = re.compile(r"\b(i am|i'm|as) (a |an |your )?(lawyer|attorney|financial advisor|financial adviser|doctor|accountant|cpa)\b"
                     r"|\byou should (invest|buy|sell|sue|file|refinance|take out)\b|\bmy advice\b", re.I)
OUTRO = re.compile(r"subscribe|in the comments|made up|not legal advice|not financial advice|tell (me|us)", re.I)


def words(t):
    return re.findall(r"[a-z0-9$%']+", t.lower())


def ngrams(ws, n=6):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def load(p):
    d = json.load(open(p))
    sc = d.get("scenes", [])
    say = " ".join(s.get("say", "") for s in sc)
    plan = [(s.get("visual", {}) or {}).get("type", "") + ":" + str((s.get("visual", {}) or {}).get("location", "")) for s in sc]
    story = [s for s in sc if not OUTRO.search(s.get("say", ""))]
    end = " ".join(s.get("say", "") for s in story[-3:])
    title = (d.get("seo", {}) or {}).get("title") or d.get("title", "")
    return d, say, plan, end, title


def main(new, olds):
    d, say, plan, end, title = load(new)
    ch = d.get("channel", "")
    fel, info = [], []
    ng = ngrams(words(say))
    for o in olds:
        try:
            _, osay, oplan, oend, otitle = load(o)
        except Exception as e:
            info.append(f"kunde inte läsa {o}: {e}")
            continue
        ov = len(ng & ngrams(words(osay))) / max(1, len(ng))
        tl = SequenceMatcher(None, title.lower(), otitle.lower()).ratio()
        pl = SequenceMatcher(None, plan, oplan).ratio()
        en = SequenceMatcher(None, words(end), words(oend)).ratio()
        info.append(f"{o}: fraser {ov:.1%}, titel {tl:.2f}, upplägg {pl:.2f}, slut {en:.2f}")
        if ov > 0.04: fel.append(f"för många återanvända fraser mot {o} ({ov:.1%} > 4 %)")
        if tl > 0.70: fel.append(f"titeln liknar '{otitle}' ({tl:.2f} > 0,70)")
        if pl > 0.60: fel.append(f"samma scenupplägg som {o} ({pl:.2f} > 0,60) – risk 'samma situation om och om igen'")
        if en > 0.35: fel.append(f"slutet liknar {o} ({en:.2f} > 0,35) – risk 'samma utfall'")
    if ch in ("The Quiet Math", "Day After Court"):
        for s in d.get("scenes", []):
            if PERSONA.search(s.get("say", "")):
                fel.append(f"AI-persona/råd: \"{s['say'][:90]}\"")
    print("\n".join(info))
    if fel:
        print("UNDERKÄNT – originalitet:\n- " + "\n- ".join(fel))
        return 1
    print(f"GODKÄNT – originalitet ({len(olds)} tidigare manus jämförda)")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2:]))
