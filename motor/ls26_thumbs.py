"""(mall från ls25) Miniatyrer ls-2026-11-26 Airport Hotel; ursprung: ls-2026-11-25 'Trapped In a Prison For 100 Days' (Ferris-stilen / MINIATYR_REGLER 0):
A: ljus fängelsegård, de döda trycker mot gallergrinden med vit pil OUT, hjälten stor höger, 'THEY ONLY PUSH'.
B: split DAY 1 (besökshallen, glasdörrarna) | DAY 100 (gården, bussarna går).  C: cellblocket, '212 LOCKED IN'.
Körs: cd ytauto && python3 ls25_thumbs.py ut/ls-2026-11-25"""
import sys, math
sys.path.insert(0, '.')
import skia
import engine as E, charstyle, atmos
import importlib
for n in ('mine', 'bakery', 'pier', 'ls21', 'prison', 'hotel'):
    m = importlib.import_module(n); getattr(m, 'enable', lambda: None)()
charstyle.enable(); atmos.enable()
import prison, hotel
from engine import W, H, poly
from charstyle import draw_face, fill, ink
from mine import _silhouette

ANTON = skia.Typeface.MakeFromFile("fonts/Anton-Regular.ttf")
BANG = skia.Typeface.MakeFromFile("fonts/Bangers-Regular.ttf")
NAVY, CAP, BAND = 0xFF263248, 0xFF1A2235, 0xFF2B3A55
WINE_J = 0xFF8C2F3A


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
    fill(c, torso, WINE_J); ink(c, torso, 14)
    # axelmärke + nyckelknippa
    c.drawRect(skia.Rect.MakeXYWH(cx - r * 0.75, cy + r * 1.35, r * 0.3, r * 0.22), skia.Paint(AntiAlias=True, Color=0xFFE8C23A))
    draw_face(c, cx, cy, r, "hero", expr, look, 0.0, cap=CAP, band=BAND)



def scene(c, loc, v):
    v = dict(v, location=loc, type="scene", shot="wide")
    E.BG[loc](c, 2.0, v)


def bright(c, a=0x18FFF2D0):
    c.drawRect(skia.Rect.MakeWH(W, H), skia.Paint(Color=a))


def frozen_row(c, xs, size=560, seed=70, gy=H * 0.98):
    for i, x in enumerate(xs):
        _silhouette(c, W * x, gy, size + (i % 2) * 40, 0.0, seed + i, look=1, arms="forward")


def bust(c, cx, r, expr="scared", look=-1, cy=H * 0.44, cap=False):
    torso = poly([(cx - r * 1.15, H + 30), (cx - r * 0.85, cy + r * 1.05), (cx + r * 0.85, cy + r * 1.05), (cx + r * 1.15, H + 30)], close=True)
    fill(c, torso, WINE_J); ink(c, torso, 14)
    c.drawRect(skia.Rect.MakeXYWH(cx - r * 0.75, cy + r * 1.35, r * 0.34, r * 0.2), skia.Paint(AntiAlias=True, Color=0xFFE8C23A))
    draw_face(c, cx, cy, r, "hero", expr, look, 0.0)


def switch(c, x, y, s=1.0, label="LOBBY"):
    r = skia.Rect.MakeXYWH(x, y, 150 * s, 220 * s); fill(c, r, 0xFFF7F3EA); ink(c, r, 10)
    k = skia.Rect.MakeXYWH(x + 45 * s, y + 40 * s, 60 * s, 80 * s); fill(c, k, 0xFF1F9D55); ink(c, k, 6)
    text(c, label, x + 75 * s, y + 200 * s, 44 * s, sw=8, align="center")


def A(out):
    s = skia.Surface(W, H); c = s.getCanvas()
    scene(c, "hotel_lobby", {"chandelier": "on", "night": False})
    frozen_row(c, (0.05, 0.15, 0.25, 0.35, 0.45, 0.55), 560)
    bust(c, W * 0.8, H * 0.25, "terror", -1)
    switch(c, W * 0.6, H * 0.5, 1.2)
    bright(c)
    text(c, "KEEP IT LIT", 60, 230, 190)
    s.makeImageSnapshot().save(out, skia.kPNG)


def B(out):
    s = skia.Surface(W, H); c = s.getCanvas()
    L = skia.Surface(W, H); lc = L.getCanvas()
    scene(lc, "hotel_lobby", {"chandelier": "on"})
    for i, x in enumerate((0.3, 0.42, 0.54)):
        _silhouette(lc, W * x, H * 0.98, 520, 0.0, 80 + i, look=1, arms="forward")
    E.stickman(lc, W * 0.75, H * 0.86, 560, vest=None, hat=None, outfit=WINE_J, expr="terror", face=-1, arms="up")
    R = skia.Surface(W, H); rc = R.getCanvas()
    scene(rc, "airfield", {"dusk": True, "runway_lights": True, "taxi_lights": "blue", "jet": "climbing"})
    for i, x in enumerate((0.3, 0.38, 0.62, 0.7)):
        _silhouette(rc, W * x, H * 0.98, 460, 0.0, 90 + i, look=1, arms="forward")
    E.stickman(rc, W * 0.5, H * 0.9, 600, vest=None, hat=None, outfit=WINE_J, face=1, arms="up")
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
    scene(c, "hallway", {"hall_lights": "on", "door_number": "714"})
    c.drawRect(skia.Rect.MakeXYWH(W * 0.5, 0, W * 0.5, H), skia.Paint(Color=0xAA101828))
    for i, x in enumerate((0.62, 0.72, 0.82, 0.92)):
        c.drawCircle(W * x - 12, H * 0.42, 9, skia.Paint(AntiAlias=True, Color=0xFFFFE43C)); c.drawCircle(W * x + 12, H * 0.42, 9, skia.Paint(AntiAlias=True, Color=0xFFFFE43C))
    _silhouette(c, W * 0.46, H * 0.98, 600, 0.0, 77, look=-1, arms="forward")
    bust(c, W * 0.2, H * 0.26, "terror", 1)
    bright(c)
    text(c, "3:02 AM", W - 60, 300, 260, col=0xFFFFE43C, align="right")
    s.makeImageSnapshot().save(out, skia.kPNG)


if __name__ == "__main__":
    o = sys.argv[1]
    for k, f in (("A", A), ("B", B), ("C", C)):
        f(o + f".{k}.png"); print(o + f".{k}.png")
