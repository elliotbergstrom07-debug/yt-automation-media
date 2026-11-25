"""Miniatyrer ls-2026-11-25 'Trapped In a Prison For 100 Days' (Ferris-stilen / MINIATYR_REGLER 0):
A: ljus fängelsegård, de döda trycker mot gallergrinden med vit pil OUT, hjälten stor höger, 'THEY ONLY PUSH'.
B: split DAY 1 (besökshallen, glasdörrarna) | DAY 100 (gården, bussarna går).  C: cellblocket, '212 LOCKED IN'.
Körs: cd ytauto && python3 ls25_thumbs.py ut/ls-2026-11-25"""
import sys, math
sys.path.insert(0, '.')
import skia
import engine as E, charstyle, atmos
import importlib
for n in ('mine', 'bakery', 'pier', 'ls21', 'prison'):
    m = importlib.import_module(n); getattr(m, 'enable', lambda: None)()
charstyle.enable(); atmos.enable()
import prison
from engine import W, H, poly
from charstyle import draw_face, fill, ink
from mine import _silhouette

ANTON = skia.Typeface.MakeFromFile("fonts/Anton-Regular.ttf")
BANG = skia.Typeface.MakeFromFile("fonts/Bangers-Regular.ttf")
NAVY, CAP, BAND = 0xFF263248, 0xFF1A2235, 0xFF2B3A55


def text(c, s, x, y, size, col=0xFFFFFFFF, stroke=0xFF111111, sw=22, align="left", tf=ANTON):
    f = skia.Font(tf, size); w = f.measureText(s)
    if align == "right": x -= w
    if align == "center": x -= w / 2
    blob = skia.TextBlob.MakeFromString(s, f)
    c.drawTextBlob(blob, x + 8, y + 10, skia.Paint(AntiAlias=True, Color=0x88000000))
    c.drawTextBlob(blob, x, y, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=sw, Color=stroke, StrokeJoin=skia.Paint.kRound_Join))
    c.drawTextBlob(blob, x, y, skia.Paint(AntiAlias=True, Color=col))


def bust(c, cx, r, expr="scared", look=-1, cy=H * 0.44):
    torso = poly([(cx - r * 1.15, H + 30), (cx - r * 0.85, cy + r * 1.05), (cx + r * 0.85, cy + r * 1.05), (cx + r * 1.15, H + 30)], close=True)
    fill(c, torso, NAVY); ink(c, torso, 14)
    # axelmärke + nyckelknippa
    c.drawRect(skia.Rect.MakeXYWH(cx - r * 0.75, cy + r * 1.35, r * 0.3, r * 0.22), skia.Paint(AntiAlias=True, Color=0xFFE8C23A))
    draw_face(c, cx, cy, r, "hero", expr, look, 0.0, cap=CAP, band=BAND)


def scene(c, loc, v):
    v = dict(v, location=loc, type="scene", shot="wide")
    E.BG[loc](c, 2.0, v)


def bright(c, a=0x18FFF2D0):
    c.drawRect(skia.Rect.MakeWH(W, H), skia.Paint(Color=a))


def A(out):
    s = skia.Surface(W, H); c = s.getCanvas()
    scene(c, "prison_yard", {"fence": True})
    for i, x in enumerate((0.04, 0.13, 0.22, 0.31, 0.40, 0.46)):
        _silhouette(c, W * x, H * 0.98, 560 + (i % 2) * 40, 1.0, 70 + i, look=1, arms="up")
    prison._arrow(c, W * 0.52 + 110, H * 0.5, "out", 230)
    bust(c, W * 0.79, H * 0.25, "scared", -1)
    bright(c)
    text(c, "THEY ONLY PUSH", 60, 210, 170)
    s.makeImageSnapshot().save(out, skia.kPNG)


def B(out):
    s = skia.Surface(W, H); c = s.getCanvas()
    L = skia.Surface(W, H); lc = L.getCanvas()
    scene(lc, "visitor_lobby", {"window_dead": True})
    E.stickman(lc, W * 0.8, H * 0.82, 520, vest=None, hat=CAP, outfit=NAVY, expr="scared", face=-1, arms="up")
    R = skia.Surface(W, H); rc = R.getCanvas()
    scene(rc, "prison_yard", {"buses": 2, "fence": True})
    for i, x in enumerate((0.05, 0.15, 0.25, 0.35)):
        _silhouette(rc, W * x, H * 0.98, 520, 1.0, 80 + i, look=1, arms="up")
    E.stickman(rc, W * 0.5, H * 0.86, 560, vest=None, hat=CAP, outfit=NAVY, face=1, arms="up")
    c.drawImageRect(L.makeImageSnapshot(), skia.Rect.MakeXYWH(W * 0.25, 0, W * 0.5, H), skia.Rect.MakeXYWH(0, 0, W / 2, H))
    c.drawImageRect(R.makeImageSnapshot(), skia.Rect.MakeXYWH(W * 0.25, 0, W * 0.5, H), skia.Rect.MakeXYWH(W / 2, 0, W / 2, H))
    c.drawRect(skia.Rect.MakeXYWH(W / 2 - 14, 0, 28, H), skia.Paint(Color=0xFF111111))
    c.drawRect(skia.Rect.MakeXYWH(W / 2 - 6, 0, 12, H), skia.Paint(Color=0xFFFFFFFF))
    bright(c)
    text(c, "DAY 1", W * 0.25, 210, 170, align="center")
    text(c, "DAY 100", W * 0.75, 210, 170, col=0xFFFFE43C, align="center")
    s.makeImageSnapshot().save(out, skia.kPNG)


def C(out):
    s = skia.Surface(W, H); c = s.getCanvas()
    scene(c, "cellblock", {"cell_faces": 10, "cell_shout": True})
    bust(c, W * 0.22, H * 0.26, "terror", 1)
    bright(c)
    text(c, "212", W - 60, 300, 280, col=0xFFFFE43C, align="right")
    text(c, "LOCKED IN", W - 60, 470, 150, align="right")
    s.makeImageSnapshot().save(out, skia.kPNG)


if __name__ == "__main__":
    o = sys.argv[1]
    for k, f in (("A", A), ("B", B), ("C", C)):
        f(o + f".{k}.png"); print(o + f".{k}.png")
