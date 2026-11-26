"""QM 26 nov (mall qm25) – How Much House Can You Afford by Salary? Ursprung: QM 25 nov – miniatyrer A/B/C för "How Broke Are Americans, Really? (On a $64K Salary)" (pris mot lön, samma mall som 24/11).
Mall (FORMAT_BLUEPRINT QM / TREND_2026-11-24): ljus, nästan vit bild, PRIS MOT LÖN – stor röd siffra överst,
grön lön under, maskoten framför ett ljust hus med SOLD-skylt. python3 qm24_thumbs.py -> ut/qm-2026-11-25.{A,B,C}.png"""
import os, skia
import engine as E
from engine import W, H
import qmday as D
import qmhouse as HS
import qm20 as Z
from qm_thumb import P, rrect, INK, BANGERS

NAME = "qm-2026-11-26"
RED, GREEN = 0xFFD0312D, 0xFF1E8A3C


def bgimg(c, loc):
    c.drawImage(D.bg_image(loc), 0, 0)
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, H), P(0x33FFFFFF))


def word(c, s, x, y, size, col, rot=-3):
    f = skia.Font(BANGERS, size); tw = f.measureText(s)
    c.save(); c.translate(x - tw / 2, y); c.rotate(rot)
    c.drawString(s, 10, 12, f, P(0x44000000, size * 0.12))
    c.drawString(s, 0, 0, f, P(0xFFFFFFFF, size * 0.22))
    c.drawString(s, 0, 0, f, P(INK, size * 0.11))
    c.drawString(s, 0, 0, f, P(col))
    c.restore()


def panel(c, x, y, w, h):
    r = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), 30, 30)
    c.drawRRect(r, P(0xFF16223A)); c.drawRRect(r, P(INK, 10))


def thumb_A(c):
    bgimg(c, "suburb_street")
    gy = H * 0.97
    HS.house(c, W * 0.24, gy - 10, W * 0.4, 0xFFB9D3EA, None)
    HS.sale_sign(c, W * 0.44, gy - 10, "$416,700")
    panel(c, W * 0.52, H * 0.06, W * 0.46, H * 0.88)
    HS.house(c, W * 0.63, H * 0.93, W * 0.24, 0xFFE9D9A6, None)
    D.mascot(c, W * 0.2, gy, H * 0.6, "shock", "point", 1, 0.6)
    word(c, "$64K PAY =", W * 0.75, H * 0.3, 160, GREEN)
    word(c, "$174K HOUSE", W * 0.75, H * 0.58, 150, RED)


def thumb_B(c):
    bgimg(c, "suburb_street")
    gy = H * 0.97
    HS.house(c, W * 0.38, gy - 10, W * 0.58, 0xFFB9D3EA, None)
    HS.sale_sign(c, W * 0.84, gy - 10, "$416,700")
    D.mascot(c, W * 0.16, gy, H * 0.55, "doubt", "point", 1, 0.6)
    word(c, "$140,800", W * 0.5, H * 0.26, 230, RED)
    word(c, "TO BUY THIS?", W * 0.5, H * 0.46, 120, 0xFF16223A)


def thumb_C(c):
    bgimg(c, "suburb_street")
    gy = H * 0.97
    panel(c, W * 0.52, H * 0.1, W * 0.46, H * 0.8)
    D.mascot(c, W * 0.2, gy, H * 0.62, "worried", "point", 1, 0.6)
    word(c, "-$27,748", W * 0.75, H * 0.46, 200, RED)
    word(c, "SAME PAY?", W * 0.75, H * 0.76, 140, GREEN)


def make():
    os.makedirs("ut", exist_ok=True); out = []
    for k, fn in (("A", thumb_A), ("B", thumb_B), ("C", thumb_C)):
        s = skia.Surface(W, H); c = s.getCanvas(); c.clear(0xFFFFFFFF); fn(c)
        p = f"ut/{NAME}.{k}.png"; s.makeImageSnapshot().resize(1280, 720).save(p, skia.kPNG); out.append(p)
    return out


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    HS.enable(); Z.enable()
    print(make())
