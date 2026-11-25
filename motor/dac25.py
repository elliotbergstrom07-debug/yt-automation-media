"""Day After Court 25 nov – "Your Life at Every Level of a $38 Self-Checkout Arrest" (Illinois).

Laddas av run_new.py (CHAN=dac, enable()). Registrerar allt här, ändrar inga delade filer.
Platser: store_exit (glasdörrar, larmbågar, självkassor i bakgrunden), store_selfcheckout (4 kassor, LANE 4),
  store_backroom (litet rum, skärm med kamerarutor), squad_car (gata, polisbil utan text),
  car_interior (parkering i skymning bredvid bilen), keisha_kitchen, pd_office, warehouse, hr_office.
Rekvisita: cart (undre hylla, tag → laddare+batterier inringade), receipt, kiosk, scanner, wall_phone,
  bag, fridge (notes = antal papper), laptop. Håll: receipt. Bifigurer: red/navy/purple + cap.
Inga logotyper eller varumärken.
"""
import math, random
import skia
import engine as E
from engine import W, H
import qmday as D
import qm_thumb as Q
import chanstyle as CS
import dacli2 as L
from qm_thumb import P, path, shape, rrect, INK, BANGERS
from dacli2 import _txt, _sign, _floor, _clock

RED = 0xFFD62A2A
YEL = 0xFFF2C230


def _lin(c, x0, y0, x1, y1, cols, rect=None):
    sh = skia.GradientShader.MakeLinear([(x0, y0), (x1, y1)], cols)
    c.drawRect(rect or skia.Rect.MakeWH(W, H), skia.Paint(Shader=sh, AntiAlias=True))


def _glow(c, x, y, r, col):
    sh = skia.GradientShader.MakeRadial((x, y), r, [col, col & 0x00FFFFFF])
    c.drawCircle(x, y, r, skia.Paint(Shader=sh, AntiAlias=True))


def _ceiling_lights(c, n=5, y=H * 0.035):
    for k in range(n):
        x = W * (0.08 + k * 0.84 / max(1, n - 1))
        rrect(c, x - 110, y, 220, 26, 6, 0xFFFFFFF4, 3)
        _glow(c, x, y + 40, 260, 0x30FFF6D8)


def _kiosk(c, x, base, s=1.0, text=None, lit=False, num=None):
    """Självkassa: pelare, skärm, skanner, påsställ."""
    w = 150 * s
    rrect(c, x - w / 2, base - 430 * s, w, 430 * s, 10 * s, 0xFFDCE1E6, 5)
    rrect(c, x - w * 0.42, base - 410 * s, w * 0.84, 150 * s, 8 * s, 0xFF2A2D33, 4)
    c.drawRect(skia.Rect.MakeXYWH(x - w * 0.36, base - 396 * s, w * 0.72, 122 * s), P(0xFF9FE0B0 if lit else 0xFFBFE3F5))
    if text:
        f = skia.Font(BANGERS, 30 * s)
        lines = text.split("|")
        for j, ln in enumerate(lines):
            while f.measureText(ln) > w * 0.68 and f.getSize() > 10:
                f.setSize(f.getSize() - 1)
            c.drawString(ln, x - f.measureText(ln) / 2, base - 330 * s + (j - (len(lines) - 1) / 2) * 34 * s, f, P(INK))
    rrect(c, x - w * 0.5 - 30 * s, base - 250 * s, w + 60 * s, 28 * s, 6, 0xFF8A949E, 4)        # skannerytan
    c.drawRect(skia.Rect.MakeXYWH(x - 30 * s, base - 246 * s, 60 * s, 18 * s), P(0xFFE0574A))   # laserfönster
    # påsställ till höger
    c.drawLine(x + w / 2 + 20 * s, base - 222 * s, x + w / 2 + 20 * s, base - 120 * s, P(INK, 5))
    c.drawLine(x + w / 2 + 120 * s, base - 222 * s, x + w / 2 + 120 * s, base - 120 * s, P(INK, 5))
    shape(c, [(x + w / 2 + 25 * s, base - 215 * s), (x + w / 2 + 115 * s, base - 215 * s), (x + w / 2 + 108 * s, base - 120 * s), (x + w / 2 + 32 * s, base - 120 * s)], 0xFFF4F1EA, 3)
    # lampa på stång
    c.drawLine(x - w * 0.35, base - 430 * s, x - w * 0.35, base - 500 * s, P(INK, 5))
    c.drawCircle(x - w * 0.35, base - 512 * s, 16 * s, P(0xFFE0574A if lit else 0xFF6FCB7A))
    c.drawCircle(x - w * 0.35, base - 512 * s, 16 * s, P(INK, 3))
    if lit:
        _glow(c, x - w * 0.35, base - 512 * s, 60 * s, 0x66FF6A4A)
    if num is not None:
        rrect(c, x - 30 * s, base - 600 * s, 60 * s, 60 * s, 8, 0xFF1F2A44, 4)
        _txt(c, str(num), x, base - 552 * s, 46 * s, 0xFFFFFFFF)


# ================================================================== platser
def bg_store_exit(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFF3EEE3))
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, H * 0.09), P(0xFFE3DDD0))
    _ceiling_lights(c, 5)
    # bakvägg: självkassorna långt bak (mindre, ljusare)
    for k in range(4):
        _kiosk(c, W * (0.08 + k * 0.1), H * 0.62, 0.55, num=k + 1)
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.18, W * 0.46, H * 0.44), P(0x22FFFFFF))
    _sign(c, W * 0.1, H * 0.12, W * 0.24, H * 0.06, "SELF CHECKOUT", 0xFF2F7D4A)
    # stora glasdörrar till höger med parkeringen utanför
    gx, gw, gy0 = W * 0.5, W * 0.46, H * 0.14
    rrect(c, gx - 14, gy0 - 14, gw + 28, H * 0.5 + 14, 4, 0xFF9AA3AD, 6)
    _lin(c, 0, gy0, 0, H * 0.64, [0xFF9ED3F2, 0xFFE4F4FB], skia.Rect.MakeXYWH(gx, gy0, gw, H * 0.5))
    # parkering + bilar + träd genom glaset
    c.save(); c.clipRect(skia.Rect.MakeXYWH(gx, gy0, gw, H * 0.5))
    c.drawRect(skia.Rect.MakeXYWH(gx, H * 0.5, gw, H * 0.14), P(0xFFB9BDC2))
    for k in range(6):
        c.drawLine(gx + k * 160, H * 0.5, gx + k * 160 - 40, H * 0.64, P(0xFFFFFFFF, 5))
    for k, col in enumerate((0xFFC22A2A, 0xFF2F5FA8, 0xFFEDEFF2, 0xFF2A2D33)):
        D.car(c, gx + 120 + k * 220, H * 0.6, 0.55, col)
    for k in range(5):
        tx = gx + 80 + k * 190
        c.drawCircle(tx, H * 0.34, 60, P(0xFF7DB86A)); c.drawLine(tx, H * 0.38, tx, H * 0.5, P(0xFF6E4A2A, 10))
    c.restore()
    c.drawLine(gx + gw / 2, gy0, gx + gw / 2, H * 0.64, P(0xFF9AA3AD, 12))
    for k in range(2):
        c.drawLine(gx + 40 + k * gw / 2, gy0 + 40, gx + 140 + k * gw / 2, gy0 + 10, P(0x88FFFFFF, 8))
    _sign(c, gx + gw * 0.38, gy0 - 76, gw * 0.24, 60, "EXIT", 0xFF2F7D4A)
    # larmbågar (pedestaler) vid dörren
    for x in (gx + 30, gx + gw * 0.5 - 30, gx + gw - 60):
        rrect(c, x, H * 0.36, 34, H * 0.52, 12, 0xFFE9ECEF, 4)
        c.drawRect(skia.Rect.MakeXYWH(x + 8, H * 0.42, 18, H * 0.06), P(0xFF8FB8D8))
    # golv: ljusa plattor
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.64, W, H * 0.36), P(0xFFE5E0D6))
    for k in range(0, W + 400, 150):
        c.drawLine(k, H * 0.64, k - 200, H, P(0x16000000, 3))
    for y in (H * 0.72, H * 0.83, H * 0.95):
        c.drawLine(0, y, W, y, P(0x16000000, 3))
    c.drawLine(0, H * 0.64, W, H * 0.64, P(INK, 5))
    # gul golvmarkering vid utgången
    c.drawRect(skia.Rect.MakeXYWH(gx, H * 0.66, gw, 14), P(YEL))


def bg_store_selfcheckout(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFF1ECE1))
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, H * 0.09), P(0xFFE3DDD0))
    _ceiling_lights(c, 4)
    # hyllor långt bak
    for k in range(3):
        x = W * (0.02 + k * 0.17)
        rrect(c, x, H * 0.2, W * 0.15, H * 0.3, 4, 0xFFCFC6B4, 4)
        for j in range(3):
            c.drawLine(x, H * 0.27 + j * H * 0.08, x + W * 0.15, H * 0.27 + j * H * 0.08, P(INK, 3))
            for b in range(6):
                rrect(c, x + 10 + b * 44, H * 0.22 + j * H * 0.08, 34, H * 0.05, 3,
                      (0xFFE0574A, 0xFF4B7BE5, 0xFFE9B23A, 0xFF2BA39A)[(b + j + k) % 4], 2)
    _sign(c, W * 0.55, H * 0.12, W * 0.3, H * 0.07, "SELF CHECKOUT  1-4", 0xFF2F7D4A)
    # rad med kassor (nummerskyltar) – kassa 4 längst till höger
    for k in range(3):
        _kiosk(c, W * (0.5 + k * 0.1), H * 0.64, 0.62, num=k + 1)
    rrect(c, 0, H * 0.6, W, 14, 4, 0xFF8A949E, 3)
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.64, W, H * 0.36), P(0xFFE5E0D6))
    for k in range(0, W + 400, 150):
        c.drawLine(k, H * 0.64, k - 200, H, P(0x16000000, 3))
    c.drawLine(0, H * 0.64, W, H * 0.64, P(INK, 5))
    _sign(c, W * 0.86, H * 0.22, W * 0.1, H * 0.08, "4", 0xFF1F2A44)


def bg_store_backroom(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFD9DED8))
    for y in range(0, int(H * 0.64), 60):
        off = 0 if (y // 60) % 2 else 70
        for x in range(-off, W, 140):
            c.drawRect(skia.Rect.MakeXYWH(x, y, 140, 60), P(0x12000000, 2))
    rrect(c, W * 0.5, H * 0.04, W * 0.2, 60, 6, 0xFFFFFFF4, 3)
    _glow(c, W * 0.6, H * 0.12, 420, 0x30FFF6D8)
    # skärm med kamerarutor
    rrect(c, W * 0.42, H * 0.16, W * 0.26, H * 0.24, 8, 0xFF2A2D33, 6)
    for i in range(4):
        x = W * 0.43 + (i % 2) * W * 0.12; y = H * 0.175 + (i // 2) * H * 0.11
        c.drawRect(skia.Rect.MakeXYWH(x, y, W * 0.115, H * 0.1), P(0xFF7E8C99 if i != 3 else 0xFF97A7B4))
        c.drawRect(skia.Rect.MakeXYWH(x + 20, y + H * 0.06, 60, 20), P(0xFFBFC8CF))
        _txt(c, f"CAM {i + 1}", x + 50, y + 26, 22, 0xFFFFFFFF)
    rrect(c, W * 0.53, H * 0.4, W * 0.04, H * 0.04, 2, 0xFF2A2D33, 4)
    # skrivbord
    rrect(c, W * 0.36, H * 0.44, W * 0.4, H * 0.05, 4, 0xFF8B5A2B, 5)
    for lx in (W * 0.38, W * 0.73):
        c.drawLine(lx, H * 0.49, lx, H * 0.64, P(INK, 8))
    rrect(c, W * 0.6, H * 0.4, 120, 40, 4, 0xFFFFFFFF, 3)          # blankett
    # arkivskåp + väggklocka + anslag
    rrect(c, W * 0.82, H * 0.2, W * 0.13, H * 0.44, 4, 0xFF8D949C, 5)
    for j in range(3):
        rrect(c, W * 0.835, H * 0.24 + j * H * 0.13, W * 0.1, H * 0.1, 3, 0xFF9DA4AC, 3)
        c.drawLine(W * 0.865, H * 0.29 + j * H * 0.13, W * 0.915, H * 0.29 + j * H * 0.13, P(INK, 5))
    _clock(c, W * 0.12, H * 0.16, 60, 6, 44)
    rrect(c, W * 0.06, H * 0.28, W * 0.14, H * 0.16, 3, 0xFFFFFFFF, 3)
    _txt(c, "STAFF ONLY", W * 0.13, H * 0.33, 30, RED)
    for j in range(3):
        c.drawLine(W * 0.075, H * 0.36 + j * 20, W * 0.185, H * 0.36 + j * 20, P(0x44000000, 3))
    _floor(c, H * 0.64, 0xFFB7B3A8)


def bg_squad_car(c):
    _lin(c, 0, 0, 0, H * 0.6, [0xFF7FA6D6, 0xFFF5C99A])
    rnd = random.Random(7)
    for k in range(9):                                                       # stadssilhuett i två lager
        x = k * W / 8 - 40; h = rnd.uniform(0.18, 0.34) * H
        c.drawRect(skia.Rect.MakeXYWH(x, H * 0.6 - h, W / 8 - 20, h), P(0xFF9AA8BD))
    for k in range(7):
        x = k * W / 6 + 30; h = rnd.uniform(0.12, 0.24) * H
        c.drawRect(skia.Rect.MakeXYWH(x, H * 0.6 - h, W / 7, h), P(0xFFB7C0CC))
        for j in range(int(h // 60)):
            c.drawRect(skia.Rect.MakeXYWH(x + 30, H * 0.6 - h + 20 + j * 60, 40, 26), P(0xFFFFE9A8))
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.6, W, H * 0.04), P(0xFFC9C4B8))           # trottoar
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.64, W, H * 0.36), P(0xFF6E737C))
    c.drawLine(0, H * 0.64, W, H * 0.64, P(INK, 5))
    for k in range(0, W, 260):
        c.drawRect(skia.Rect.MakeXYWH(k, H * 0.9, 140, 12), P(0xFFF2D24A))
    # polisbil (vit/svart, ljusbalk, ingen text) till vänster
    bx, by = W * 0.06, H * 0.78
    shape(c, [(bx, by), (bx + 40, by - 120), (bx + 520, by - 120), (bx + 600, by - 40), (bx + 600, by)], 0xFFF4F4F4, 6)
    shape(c, [(bx + 120, by - 120), (bx + 170, by - 210), (bx + 400, by - 210), (bx + 460, by - 120)], 0xFF2A2D33, 6)
    c.drawRect(skia.Rect.MakeXYWH(bx + 190, by - 200, 90, 70), P(0xFFBFE3F5)); c.drawRect(skia.Rect.MakeXYWH(bx + 300, by - 200, 90, 70), P(0xFFBFE3F5))
    c.drawRect(skia.Rect.MakeXYWH(bx + 20, by - 90, 560, 40), P(0xFF2A2D33))
    rrect(c, bx + 230, by - 240, 60, 28, 6, RED, 4); rrect(c, bx + 290, by - 240, 60, 28, 6, 0xFF2F5FA8, 4)
    _glow(c, bx + 260, by - 226, 120, 0x55FF4040); _glow(c, bx + 320, by - 226, 120, 0x554060FF)
    for wx in (bx + 120, bx + 470):
        c.drawCircle(wx, by, 58, P(0xFF2A2D33)); c.drawCircle(wx, by, 26, P(0xFFB0B5BC))


def bg_car_interior(c):
    """Parkeringen i skymning bredvid den egna bilen (figurerna står bredvid bilen)."""
    _lin(c, 0, 0, 0, H * 0.62, [0xFF6C79B8, 0xFFF0A97A])
    _glow(c, W * 0.7, H * 0.56, 300, 0x66FFD49A)
    for k in range(6):                                                       # lyktstolpar
        x = W * (0.05 + k * 0.19)
        c.drawLine(x, H * 0.2, x, H * 0.62, P(0xFF3B3F48, 8))
        c.drawCircle(x, H * 0.2, 16, P(0xFFFFE9A8)); _glow(c, x, H * 0.2, 90, 0x55FFE9A8)
    c.drawRect(skia.Rect.MakeXYWH(W * 0.55, H * 0.36, W * 0.45, H * 0.26), P(0xFFB7AFA2))  # butiksfasaden långt bort
    for k in range(5):
        c.drawRect(skia.Rect.MakeXYWH(W * 0.58 + k * 160, H * 0.44, 110, 90), P(0xFFFFE9A8))
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.62, W, H * 0.38), P(0xFF7E838C))
    c.drawLine(0, H * 0.62, W, H * 0.62, P(INK, 5))
    for k in range(-1, 8):
        c.drawLine(W * 0.08 + k * 300, H * 0.66, W * 0.02 + k * 300, H, P(0xFFEDEFF2, 6))
    # egna bilen (blå sedan) i mitten bakom figurerna
    D.car(c, W * 0.5, H * 0.8, 1.15, 0xFF4F7CAC)


def bg_keisha_kitchen(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFF3E6D6))
    for y in range(int(H * 0.3), int(H * 0.46), 40):
        for x in range(int(W * 0.3), W, 80):
            c.drawRect(skia.Rect.MakeXYWH(x, y, 80, 40), P(0x14000000, 2))
    Q.window(c, W * 0.06, H * 0.1, W * 0.2, H * 0.3)
    for k in range(4):                                                       # överskåp
        rrect(c, W * (0.32 + k * 0.16), H * 0.06, W * 0.14, H * 0.2, 6, 0xFF9C7BB8, 5)
        c.drawCircle(W * (0.32 + k * 0.16) + W * 0.12, H * 0.2, 8, P(0xFFE9C46A))
    rrect(c, W * 0.3, H * 0.46, W * 0.7, H * 0.18, 4, 0xFFF4F1EA, 5)          # bänk
    c.drawRect(skia.Rect.MakeXYWH(W * 0.3, H * 0.46, W * 0.7, 18), P(0xFF6E737C))
    for k in range(4):
        rrect(c, W * (0.33 + k * 0.17), H * 0.5, W * 0.13, H * 0.12, 4, 0xFFB79AD0, 4)
    rrect(c, W * 0.5, H * 0.38, 120, 80, 10, 0xFFE07A4A, 4)                 # kastrull
    c.drawCircle(W * 0.42, H * 0.4, 30, P(0xFF5FA84A))                       # kruka
    _clock(c, W * 0.86, H * 0.36, 40, 7, 10)
    _floor(c, H * 0.64, 0xFFC79E6E)


def bg_pd_office(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFE8E4DA))
    Q.window(c, W * 0.06, H * 0.1, W * 0.22, H * 0.3)
    for k in range(6):                                                       # persienner
        c.drawLine(W * 0.06, H * 0.12 + k * H * 0.05, W * 0.28, H * 0.12 + k * H * 0.05, P(0x55FFFFFF, 6))
    _sign(c, W * 0.38, H * 0.06, W * 0.26, H * 0.07, "PUBLIC DEFENDER", 0xFF1F2A44)
    rrect(c, W * 0.72, H * 0.08, W * 0.24, H * 0.5, 4, 0xFF8B5A2B, 5)         # bokhylla
    for j in range(4):
        y = H * 0.12 + j * H * 0.11
        c.drawLine(W * 0.72, y + H * 0.09, W * 0.96, y + H * 0.09, P(INK, 4))
        for b in range(9):
            rrect(c, W * 0.73 + b * 48, y, 38, H * 0.09, 2, (0xFF2F5FA8, 0xFFC22A2A, 0xFF2F7D4A, 0xFFE9B23A)[(b + j) % 4], 2)
    rrect(c, W * 0.34, H * 0.44, W * 0.34, H * 0.05, 4, 0xFF6E431E, 5)       # skrivbord med pärmhögar
    for lx in (W * 0.36, W * 0.65):
        c.drawLine(lx, H * 0.49, lx, H * 0.64, P(INK, 8))
    for k in range(3):
        for j in range(3 + k):
            rrect(c, W * (0.38 + k * 0.08), H * 0.42 - j * 22, 120, 20, 2, (0xFFF4EEDF, 0xFFE8D9A8)[j % 2], 3)
    for k in range(3):                                                       # flyttkartonger med akter
        rrect(c, W * (0.05 + k * 0.08), H * 0.5, 130, 110, 3, 0xFFC49A5C, 4)
        _txt(c, "FILES", W * (0.05 + k * 0.08) + 65, H * 0.56, 26, INK)
    _floor(c, H * 0.64, 0xFF9FA7AF)


def bg_warehouse(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFE2E4E2))
    for k in range(6):                                                       # höga fönster
        rrect(c, W * (0.04 + k * 0.16), H * 0.03, W * 0.12, H * 0.08, 3, 0xFFCDEBFA, 4)
        _glow(c, W * (0.1 + k * 0.16), H * 0.12, 200, 0x22FFFFFF)
    for k in range(3):                                                       # pallställ med lådor
        x = W * (0.02 + k * 0.34)
        for lx in (x, x + W * 0.3):
            rrect(c, lx, H * 0.14, 22, H * 0.5, 2, 0xFF2F5FA8, 3)
        for j in range(3):
            y = H * (0.28 + j * 0.15)
            rrect(c, x, y, W * 0.3 + 22, 18, 2, 0xFFE07A2A, 3)
            for b in range(4):
                rrect(c, x + 30 + b * W * 0.07, y - H * 0.1, W * 0.06, H * 0.1, 3, 0xFFC49A5C, 3)
                c.drawLine(x + 30 + b * W * 0.07, y - H * 0.06, x + 30 + b * W * 0.07 + W * 0.06, y - H * 0.06, P(0x55000000, 3))
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.64, W, H * 0.36), P(0xFFB4B7B9))
    c.drawLine(0, H * 0.64, W, H * 0.64, P(INK, 5))
    for y in (H * 0.7, H * 0.96):
        c.drawRect(skia.Rect.MakeXYWH(0, y, W, 14), P(YEL))
    # gaffeltruck till höger (bakom figurer)
    fx, fy = W * 0.84, H * 0.86
    rrect(c, fx - 120, fy - 170, 200, 130, 10, YEL, 5)
    c.drawLine(fx - 100, fy - 170, fx - 100, fy - 300, P(INK, 8)); c.drawLine(fx + 40, fy - 170, fx + 40, fy - 300, P(INK, 8))
    c.drawLine(fx - 100, fy - 300, fx + 40, fy - 300, P(INK, 8))
    c.drawLine(fx + 100, fy - 300, fx + 100, fy - 20, P(INK, 10)); c.drawLine(fx + 100, fy - 30, fx + 200, fy - 30, P(INK, 10))
    for wx in (fx - 80, fx + 40):
        c.drawCircle(wx, fy - 30, 36, P(0xFF2A2D33))


def bg_hr_office(c):
    c.drawRect(skia.Rect.MakeWH(W, H), P(0xFFEEF0F2))
    c.drawRect(skia.Rect.MakeXYWH(W * 0.04, H * 0.08, W * 0.4, H * 0.5), P(0xFFD6EAF4))   # glasvägg
    for k in range(4):
        c.drawLine(W * 0.04 + k * W * 0.133, H * 0.08, W * 0.04 + k * W * 0.133, H * 0.58, P(0xFF9AA3AD, 8))
    c.drawRect(skia.Rect.MakeXYWH(W * 0.04, H * 0.08, W * 0.4, H * 0.5), P(INK, 4))
    for k in range(3):
        c.drawLine(W * (0.07 + k * 0.13), H * 0.15, W * (0.12 + k * 0.13), H * 0.1, P(0x88FFFFFF, 6))
    _sign(c, W * 0.5, H * 0.08, W * 0.26, H * 0.07, "HUMAN RESOURCES", 0xFF2F7D4A)
    rrect(c, W * 0.82, H * 0.12, W * 0.12, H * 0.16, 4, 0xFFFFFFFF, 4)           # tavla
    shape(c, [(W * 0.83, H * 0.26), (W * 0.86, H * 0.18), (W * 0.89, H * 0.22), (W * 0.93, H * 0.15), (W * 0.93, H * 0.26)], 0xFF8DBF4A, 3)
    rrect(c, W * 0.5, H * 0.44, W * 0.36, H * 0.05, 4, 0xFFF4F1EA, 5)            # skrivbord
    for lx in (W * 0.52, W * 0.83):
        c.drawLine(lx, H * 0.49, lx, H * 0.64, P(INK, 8))
    rrect(c, W * 0.9, H * 0.48, 80, 100, 8, 0xFFE0E0E0, 4)
    for a in range(5):
        c.drawCircle(W * 0.9 + 40 + math.cos(a) * 40, H * 0.43 - a * 14, 36, P(0xFF5FA84A))
    _floor(c, H * 0.64, 0xFFB9C2CB)


D.BGS.update({"store_exit": bg_store_exit, "store_selfcheckout": bg_store_selfcheckout,
              "store_backroom": bg_store_backroom, "squad_car": bg_squad_car, "car_interior": bg_car_interior,
              "keisha_kitchen": bg_keisha_kitchen, "pd_office": bg_pd_office, "warehouse": bg_warehouse,
              "hr_office": bg_hr_office})


# ================================================================== rekvisita
def cart(c, x, gy, s=1.0, tag=None, receipt=False):
    """Kundvagn i profil: korg, handtag, undre hylla (med laddare + batterier), hjul."""
    k = s
    base = gy - 40 * k
    c.drawCircle(x - 150 * k, gy - 22 * k, 22 * k, P(0xFF2A2D33)); c.drawCircle(x + 130 * k, gy - 22 * k, 22 * k, P(0xFF2A2D33))
    c.drawLine(x - 150 * k, base, x - 120 * k, base - 330 * k, P(0xFF8A949E, 9 * k))
    c.drawLine(x + 130 * k, base, x + 150 * k, base - 330 * k, P(0xFF8A949E, 9 * k))
    c.drawLine(x - 170 * k, base, x + 150 * k, base, P(0xFF8A949E, 9 * k))
    # undre hyllan
    shelf_y = base - 70 * k
    c.drawLine(x - 150 * k, shelf_y, x + 140 * k, shelf_y, P(0xFF8A949E, 8 * k))
    for j in range(7):
        c.drawLine(x - 140 * k + j * 40 * k, shelf_y, x - 140 * k + j * 40 * k, shelf_y + 14 * k, P(0xFF8A949E, 4 * k))
    # korgen (galler)
    top, bot = base - 330 * k, base - 160 * k
    bp = [(x - 200 * k, top), (x + 210 * k, top), (x + 170 * k, bot), (x - 150 * k, bot)]
    c.drawPath(path(bp), P(0x33C9D2DA)); c.drawPath(path(bp), P(0xFF6E7883, 7 * k))
    for j in range(1, 9):
        fx = j / 9
        c.drawLine(x - 200 * k + fx * 410 * k, top, x - 150 * k + fx * 320 * k, bot, P(0xFF8A949E, 3 * k))
    for j in range(1, 4):
        fy = j / 4
        c.drawLine(x - 200 * k + fy * 50 * k, top + fy * (bot - top), x + 210 * k - fy * 40 * k, top + fy * (bot - top), P(0xFF8A949E, 3 * k))
    c.drawLine(x - 150 * k, bot, x - 150 * k, shelf_y, P(0xFF8A949E, 7 * k))
    # handtag till vänster (röd plast)
    c.drawLine(x - 200 * k, top, x - 250 * k, top - 50 * k, P(0xFF6E7883, 7 * k))
    c.drawLine(x - 262 * k, top - 62 * k, x - 238 * k, top - 38 * k, P(RED, 16 * k))
    # varor i korgen (påsar)
    for j, col in enumerate((0xFFF4F1EA, 0xFFEFE6D2)):
        shape(c, [(x - 110 * k + j * 140 * k, top + 10 * k), (x - 10 * k + j * 140 * k, top + 10 * k), (x - 20 * k + j * 140 * k, top - 90 * k), (x - 100 * k + j * 140 * k, top - 90 * k)], col, 4 * k)
    c.drawCircle(x + 160 * k, top - 30 * k, 34 * k, P(0xFF5FA84A)); c.drawCircle(x + 160 * k, top - 30 * k, 34 * k, P(INK, 3 * k))
    if tag:
        # laddare (låda) + batteripaket på undre hyllan, inringade
        rrect(c, x - 110 * k, shelf_y - 62 * k, 110 * k, 60 * k, 4, 0xFFFFFFFF, 3 * k)
        c.drawLine(x - 90 * k, shelf_y - 40 * k, x - 30 * k, shelf_y - 40 * k, P(0xFF2A2D33, 6 * k))
        rrect(c, x + 10 * k, shelf_y - 54 * k, 100 * k, 52 * k, 4, 0xFFE9B23A, 3 * k)
        for j in range(4):
            rrect(c, x + 18 * k + j * 23 * k, shelf_y - 46 * k, 18 * k, 36 * k, 3, 0xFF2A2D33, 2)
        ring = skia.Rect.MakeXYWH(x - 140 * k, shelf_y - 100 * k, 280 * k, 130 * k)
        c.drawOval(ring, P(RED, 10 * k))
        f = skia.Font(BANGERS, 64 * k); tw = f.measureText(tag)
        tx, ty = x - tw / 2 - 15 * k, top - 230 * k
        c.drawLine(x, ty + 76 * k, x - 20 * k, shelf_y - 100 * k, P(RED, 6 * k))
        rrect(c, tx, ty, tw + 30 * k, 76 * k, 10, YEL, 5)
        c.drawString(tag, tx + 15 * k, ty + 58 * k, f, P(INK))
    if receipt:
        c.save(); c.rotate(8, x + 200 * k, top - 40 * k)
        rrect(c, x + 180 * k, top - 140 * k, 50 * k, 160 * k, 2, 0xFFFFFFFF, 3 * k)
        for j in range(6):
            c.drawLine(x + 188 * k, top - 120 * k + j * 22 * k, x + 222 * k, top - 120 * k + j * 22 * k, P(0x55000000, 3 * k))
        c.restore()


def receipt(c, x, gy, total="$112.60", s=1.0):
    top = gy - 640 * s; w = 220 * s
    pts = [(x - w / 2, top), (x + w / 2, top)]
    for j in range(9):
        pts.append((x + w / 2 - j * w / 8, gy - 240 * s + (12 * s if j % 2 else 0)))
    c.drawPath(path(pts), P(0xFFFFFFFF)); c.drawPath(path(pts), P(INK, 5))
    _txt(c, "RECEIPT", x, top + 50 * s, 40 * s, 0xFF5B5F66)
    for j in range(7):
        c.drawLine(x - w * 0.38, top + 90 * s + j * 30 * s, x + w * (0.1 if j % 2 else 0.25), top + 90 * s + j * 30 * s, P(0x55000000, 4))
        c.drawLine(x + w * 0.28, top + 90 * s + j * 30 * s, x + w * 0.4, top + 90 * s + j * 30 * s, P(0x55000000, 4))
    c.drawLine(x - w * 0.4, top + 320 * s, x + w * 0.4, top + 320 * s, P(INK, 3))
    f = skia.Font(BANGERS, 50 * s)
    while f.measureText(total) > w * 0.86:
        f.setSize(f.getSize() - 1)
    col = 0xFF1E8A3C if total.upper() == "PAID" else INK
    c.drawString(total, x - f.measureText(total) / 2, top + 380 * s, f, P(col))


def scanner(c, x, gy):
    rrect(c, x - 20, gy - 380, 40, 380, 4, 0xFF6E7A86, 4)
    rrect(c, x - 150, gy - 470, 300, 110, 14, 0xFF2A2D33, 5)
    c.drawRect(skia.Rect.MakeXYWH(x - 110, gy - 450, 220, 70), P(0xFF6BFF8A))
    _glow(c, x, gy - 415, 160, 0x446BFF8A)
    for j in range(4):
        c.drawArc(skia.Rect.MakeXYWH(x - 26 - j * 10, gy - 440 - j * 6, 52 + j * 20, 60 + j * 12), 200, 140, False, P(0xFF1E5A2A, 3))


def wall_phone(c, x, gy):
    rrect(c, x - 90, gy - 640, 180, 260, 10, 0xFF8D949C, 5)
    rrect(c, x - 60, gy - 610, 50, 200, 20, 0xFF2A2D33, 4)                  # lur
    for r in range(4):
        for k in range(3):
            rrect(c, x + 8 + k * 24, gy - 600 + r * 40, 18, 28, 4, 0xFFEDEFF2, 2)
    c.drawPath(path([(x - 35, gy - 410), (x - 50, gy - 360), (x - 20, gy - 330), (x - 45, gy - 290)], close=False), P(INK, 4))
    rrect(c, x - 110, gy - 720, 220, 60, 6, 0xFFFFFFFF, 3)
    _txt(c, "3 FREE CALLS", x, gy - 678, 36, RED)


def bag(c, x, gy, tag="PROPERTY"):
    shape(c, [(x - 130, gy - 520), (x + 130, gy - 520), (x + 150, gy - 230), (x - 150, gy - 230)], 0xCCE8F1F6, 5)
    c.drawLine(x - 130, gy - 490, x + 130, gy - 490, P(RED, 8))
    rrect(c, x - 60, gy - 420, 120, 60, 8, 0xFF2A2D33, 3)                    # plånbok
    c.drawCircle(x + 50, gy - 300, 26, P(0xFFE9C46A)); c.drawCircle(x + 50, gy - 300, 26, P(INK, 3))   # nycklar
    rrect(c, x - 90, gy - 330, 70, 110, 10, 0xFF2A2D33, 3)                  # telefon
    rrect(c, x - 90, gy - 600, 180, 60, 6, YEL, 4)
    _txt(c, tag, x, gy - 556, 40, INK)


def fridge(c, x, gy, notes=2):
    rrect(c, x - 150, gy - 720, 300, 720, 16, 0xFFF4F6F8, 6)
    c.drawLine(x - 150, gy - 470, x + 150, gy - 470, P(INK, 5))
    for y0, y1 in ((gy - 680, gy - 520), (gy - 430, gy - 260)):
        c.drawLine(x + 120, y0, x + 120, y1, P(0xFF8A949E, 10))
    for j in range(int(notes)):
        px, py = x - 110 + j * 110, gy - 680 + j * 20
        c.save(); c.rotate(-6 + j * 9, px + 50, py + 60)
        rrect(c, px, py, 100, 130, 2, (0xFFFFFFFF, 0xFFFFF3B0)[j % 2], 3)
        for r in range(4):
            c.drawLine(px + 12, py + 30 + r * 22, px + 88, py + 30 + r * 22, P(0x55000000, 3))
        c.drawCircle(px + 50, py + 8, 10, P(RED))
        c.restore()
    for j, col in enumerate((0xFF2F5FA8, 0xFF5FA84A, 0xFFE9B23A)):
        c.drawCircle(x - 90 + j * 60, gy - 380, 14, P(col))


def laptop(c, x, gy, text=""):
    rrect(c, x - 220, gy - 380, 440, 30, 6, 0xFFF4F1EA, 4)                  # bordsskiva
    for lx in (x - 200, x + 200):
        c.drawLine(lx, gy - 350, lx, gy, P(INK, 8))
    shape(c, [(x - 160, gy - 380), (x + 160, gy - 380), (x + 190, gy - 400), (x - 190, gy - 400)], 0xFF8D949C, 4)
    rrect(c, x - 170, gy - 640, 340, 240, 10, 0xFF2A2D33, 5)
    c.drawRect(skia.Rect.MakeXYWH(x - 154, gy - 624, 308, 208), P(0xFFF4F6F8))
    f = skia.Font(BANGERS, 34)
    for j, ln in enumerate((text or "").split("|")):
        while f.measureText(ln) > 290 and f.getSize() > 12:
            f.setSize(f.getSize() - 1)
        c.drawString(ln, x - f.measureText(ln) / 2, gy - 560 + j * 60, f, P(RED if j == 0 else 0xFF1E8A3C))
        f = skia.Font(BANGERS, 34)


_prop0 = CS.prop2


def prop2(c, t, pr, gy):
    k = pr.get("type"); x = W * pr.get("x", 0.6)
    if k == "cart":
        cart(c, x, gy, 1.0, pr.get("tag"), pr.get("receipt"))
    elif k == "receipt":
        receipt(c, x, gy, pr.get("total", "$112.60"))
    elif k == "kiosk":
        _kiosk(c, x, gy, 1.3, pr.get("text"), lit=pr.get("text") in ("HELP",))
    elif k == "scanner":
        scanner(c, x, gy)
    elif k == "wall_phone":
        wall_phone(c, x, gy)
    elif k == "bag":
        bag(c, x, gy, pr.get("tag", "PROPERTY"))
    elif k == "fridge":
        fridge(c, x, gy, pr.get("notes", 2))
    elif k == "laptop":
        laptop(c, x, gy, pr.get("text", ""))
    else:
        _prop0(c, t, pr, gy)


# ------------------------------------------------------------------ hålla kvitto
_held0 = CS.held


def held(c, x, y, s, what, t):
    if what == "receipt":
        w = s * 0.09
        pts = [(x - w / 2, y - s * 0.16), (x + w / 2, y - s * 0.16)]
        for j in range(7):
            pts.append((x + w / 2 - j * w / 6, y + s * 0.12 + (s * 0.008 if j % 2 else 0)))
        c.drawPath(path(pts), P(0xFFFFFFFF)); c.drawPath(path(pts), P(INK, s * 0.008))
        for j in range(6):
            c.drawLine(x - w * 0.35, y - s * 0.12 + j * s * 0.035, x + w * 0.35, y - s * 0.12 + j * s * 0.035, P(0x55000000, s * 0.006))
    else:
        _held0(c, x, y, s, what, t)


# ------------------------------------------------------------------ bifigurer: färger + keps
CS.SHIRTS.update({"red": 0xFFD62A2A, "navy": 0xFF22345A, "purple": 0xFF7A4FB0})
_adult0 = CS.adult


def adult(c, x, gy, s, fr, t):
    _adult0(c, x, gy, s, fr, t)
    if fr.get("cap"):
        r = s * 0.17; hy = gy - s * 0.58 - r * 0.95
        c.drawArc(skia.Rect.MakeXYWH(x - r * 1.02, hy - r * 1.05, r * 2.04, r * 1.6), 180, 180, True, P(0xFF1F2A44))
        c.drawLine(x - r * 1.0, hy - r * 0.3, x - r * 1.6, hy - r * 0.25, P(0xFF1F2A44, s * 0.03))
        c.drawCircle(x, hy - r * 0.75, r * 0.16, P(0xFFE9C46A))
    if fr.get("outfit") == "red" and fr.get("name") == "Marcus":
        pass


_enabled = False


def enable():
    global _enabled
    if _enabled:
        return
    _enabled = True
    CS.prop2 = prop2
    CS.held = held
    CS.adult = adult
