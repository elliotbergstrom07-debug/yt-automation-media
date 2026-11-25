"""QM 25 nov – miniatyrer A/B/C för "How Broke Are Americans, Really? (On a $64K Salary)" (pris mot lön, samma mall som 24/11).
Mall (FORMAT_BLUEPRINT QM / TREND_2026-11-24): ljus, nästan vit bild, PRIS MOT LÖN – stor röd siffra överst,
grön lön under, maskoten framför ett ljust hus med SOLD-skylt. python3 qm24_thumbs.py -> ut/qm-2026-11-25.{A,B,C}.png"""
import os, skia
import engine as E
from engine import W, H
import qmday as D
import qmhouse as HS
import qm20 as Z
from qm_thumb import P, rrect, INK, BANGERS

NAME = "qm-2026-11-25"
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
    bgimg(c, "grocery")
    gy = H * 0.97
    panel(c, W * 0.52, H * 0.1, W * 0.46, H * 0.8)
    D.mascot(c, W * 0.2, gy, H * 0.62, "shock", "point", 1, 0.6)
    word(c, "$64K PAY", W * 0.75, H * 0.38, 190, GREEN)
    word(c, "$500 LEFT?", W * 0.75, H * 0.74, 170, RED)


def thumb_B(c):
    bgimg(c, "kitchen_table")
    gy = H * 0.97
    panel(c, W * 0.52, H * 0.1, W * 0.46, H * 0.8)
    D.mascot(c, W * 0.2, gy, H * 0.62, "worried", "point", 1, 0.6)
    word(c, "1.2", W * 0.75, H * 0.48, 330, RED)
    word(c, "MONTHS?", W * 0.75, H * 0.78, 150, 0xFFFFE033)


def thumb_C(c):
    bgimg(c, "suburb_street")
    gy = H * 0.97
    panel(c, W * 0.52, H * 0.1, W * 0.46, H * 0.8)
    D.mascot(c, W * 0.2, gy, H * 0.62, "doubt", "point", 1, 0.6)
    word(c, "$263", W * 0.75, H * 0.46, 280, RED)
    word(c, "SAME PAY?", W * 0.75, H * 0.78, 140, GREEN)


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
