"""Miniatyrer A/B/C för dac-2026-11-25 -> ut/dac25.A/B/C.png (1280x720). DAC-mallen: 'LEVEL N' vit Anton + gul undertitel,
hjälten stor i höger tredjedel, ljus miljö."""
import sys, os, json
sys.path.insert(0, '/home/claude/ytauto'); os.environ['CHAN'] = 'dac'
import engine as E, qmday as D, chanstyle as CS, produce, dacli2, dac20, dac25, skia
dac20.enable(); dac25.enable()
from qm_thumb import P, rrect, INK, BANGERS
W, H = E.W, E.H
ANTON = skia.Typeface.MakeFromFile('/home/claude/ytauto/fonts/Anton-Regular.ttf')


def txt(c, s, x, y, size, col):
    f = skia.Font(ANTON, size); b = skia.TextBlob.MakeFromString(s, f)
    c.drawTextBlob(b, x + 8, y + 10, skia.Paint(AntiAlias=True, Color=0x88000000))
    c.drawTextBlob(b, x, y, skia.Paint(AntiAlias=True, Style=skia.Paint.kStroke_Style, StrokeWidth=size * 0.09, Color=0xFF111111, StrokeJoin=skia.Paint.kRound_Join))
    c.drawTextBlob(b, x, y, skia.Paint(AntiAlias=True, Color=col))


def save(s, name):
    out = skia.Surface(1280, 720)
    out.getCanvas().drawImageRect(s.makeImageSnapshot(), skia.Rect.MakeWH(1280, 720), skia.SamplingOptions(skia.FilterMode.kLinear))
    out.makeImageSnapshot().save('/home/claude/ytauto/ut/' + name, skia.kPNG)


def base(loc, zoom=1.12, cx=0.55):
    s = skia.Surface(W, H); c = s.getCanvas()
    c.save(); c.translate(W * cx, H * 0.6); c.scale(zoom, zoom); c.translate(-W * cx, -H * 0.6)
    c.drawImage(D.bg_image(loc), 0, 0); c.restore()
    return s, c


def big_hero(c, x, expr, holding=None, arms="hold"):
    CS.hero(c, x, H * 1.06, H * 1.0, expr, arms, -1, 1.5, holding=holding)


os.makedirs('/home/claude/ytauto/ut', exist_ok=True)
# A: LEVEL 1 – röd väst + kundvagnen med laddaren inringad, hjälten chockad med kvittot
s, c = base("store_exit")
CS.adult(c, W * 0.15, H * 1.02, H * 0.78, {"outfit": "red", "name": "Marcus", "hair": "short", "expr": "angry"}, 0)
dac25.cart(c, W * 0.44, H * 0.98, 1.6, "$38.47")
big_hero(c, W * 0.78, "shock", "receipt")
txt(c, "LEVEL 1", 50, 230, 210, 0xFFFFFFFF)
save(s, "dac25.A.png")

# B: LEVEL 3 – fingeravtryck
s, c = base("booking")
dac25.scanner(c, W * 0.42, H * 1.0)
c.save(); c.translate(W * 0.42, H * 0.56); c.scale(1.6, 1.6); c.translate(-W * 0.42, -H * 0.56)
c.restore()
big_hero(c, W * 0.78, "sad", None, "down")
txt(c, "LEVEL 3", 50, 230, 210, 0xFFFFFFFF); txt(c, "FINGERPRINTED", 60, 360, 100, 0xFFFFD22E)
save(s, "dac25.B.png")

# C: kvittot jättestort – VOID
s, c = base("store_selfcheckout")
dac25.receipt(c, W * 0.42, H * 1.15, "-$38.47", 1.25)
f = skia.Font(BANGERS, 120)
c.save(); c.rotate(-14, W * 0.42, H * 0.6)
rrect(c, W * 0.42 - 190, H * 0.6 - 110, 380, 140, 12, 0x00FFFFFF, 10)
c.drawString("VOID", W * 0.42 - f.measureText("VOID") / 2, H * 0.6, f, P(0xFFD62A2A)); c.restore()
big_hero(c, W * 0.78, "shock", None, "head")
txt(c, "LEVEL 9", 50, 230, 210, 0xFFFFFFFF); txt(c, "THE LOG", 60, 360, 110, 0xFFFFD22E)
save(s, "dac25.C.png")
print("klart")
