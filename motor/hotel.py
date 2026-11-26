"""Last Shift – flygplatshotellet (manus ls-2026-11-26, 'Trapped In an Airport Hotel For 100 Days').
Platser: hotel_lobby, front_desk, hallway, stairwell, parking_garage, loading_dock, kitchen, breakfast_room,
electrical_room, guest_room, basement, parking_lot, hotel_roof, airfield, hotel_exterior, hotel_map, airfield_map.
Zombier med "frozen": true = stillastående silhuett mitt i steget (arm framåt) – regeln: de stelnar i ljus.
Ljus miljö: natt = blått + varmt lampsken, aldrig svart. Laddas av run_ls.py EFTER prison (lånar dess hjälpare)."""
import math, random, json
import skia
import engine as E
from engine import W, H, fill, ink, box, line, poly
from mine import _p, _grad, _glow, _silhouette
import prison as P

INK = E.INK
GROUND = P.GROUND
WINE = 0xFF8C2F3A
GOLD = 0xFFE8B84A


def _n(v):
    return bool(v.get("night"))


def _room(c, v, day=0xFFF1E6D2, night=0xFF5B6680, wain=0xFFB98E5E, wain_n=0xFF4A4F68):
    fill(c, skia.Rect.MakeWH(W, H), night if _n(v) else day)
    for k in range(0, int(W), 90):   # tapetrand
        line(c, k, 0, k, H * 0.56, 2, 0x12000000)
    fill(c, skia.Rect.MakeXYWH(0, H * 0.56, W, GROUND - H * 0.56), wain_n if _n(v) else wain)
    line(c, 0, H * 0.56, W, H * 0.56, 5)


def _carpet(c, v, col=WINE):
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFF5E2430 if _n(v) else col)
    for k in range(9):
        x = 60 + k * 230
        p = poly([(x, GROUND + 70), (x + 40, GROUND + 40), (x + 80, GROUND + 70), (x + 40, GROUND + 100)], close=True)
        fill(c, p, 0x33F2C230)
    line(c, 0, GROUND, W, GROUND, 5)


def _concrete_floor(c, v):
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFF6F7682 if _n(v) else 0xFFB4B2AA)
    line(c, 0, GROUND, W, GROUND, 5)


def _chandelier(c, x, y, state="on", s=1.0):
    line(c, x, 0, x, y - 40 * s, 4, 0xFF6B5A3A)
    arm = skia.Rect.MakeXYWH(x - 110 * s, y - 40 * s, 220 * s, 26 * s); fill(c, arm, GOLD); ink(c, arm, 4)
    for k in range(5):
        bx = x - 100 * s + k * 50 * s
        on = state == "on" or (state == "flicker" and k % 2 == 0)
        c.drawCircle(bx, y, 18 * s, _p(0xFFFFF3B0 if on else 0xFF8A8A7A)); c.drawCircle(bx, y, 18 * s, _p(INK, 3))
        for j in range(2):
            line(c, bx, y + 18 * s, bx + (j - 0.5) * 10, y + 50 * s, 3, 0xAAFFFFFF)
    if state in ("on", "flicker"):
        _glow(c, x, y + 20, 330 * s if state == "on" else 200 * s, 0x55FFE7A0 if state == "on" else 0x33FFE7A0)


def _exit_sign(c, x, y):
    P._exit(c, x, y)


def _emergency(c, x, y):
    box(c, x, y, 110, 34, 0xFFEFEFEF, 3, 6)
    for k in (x + 22, x + 88):
        c.drawCircle(k, y + 17, 14, _p(0xFFFFF39A)); _glow(c, k, y + 40, 120, 0x44FFF39A)


def _flashlight(c, x0, y0, x1, y1, w=260):
    p = poly([(x0, y0), (x1, y1 - w / 2), (x1, y1 + w / 2)], close=True)
    fill(c, p, 0x44FFF6C8)
    _glow(c, x1, y1, w * 0.8, 0x33FFF6C8)


def _lantern(c, x, y, s=1.0, lit=True):
    line(c, x, y - 40 * s, x, y - 26 * s, 3)
    r = skia.Rect.MakeXYWH(x - 16 * s, y - 26 * s, 32 * s, 44 * s); fill(c, r, 0xFFFFE08A if lit else 0xFF6A6A6A); ink(c, r, 3)
    if lit:
        _glow(c, x, y, 110 * s, 0x55FFD070)


def _shuttle(c, x, y, s=1.0, lights=False):
    P._bus(c, x, y, s, col=0xFFF2F2F2, label="HOTEL SHUTTLE")
    stripe = skia.Rect.MakeXYWH(x, y - 70 * s, 460 * s, 16 * s); fill(c, stripe, 0xFF2F7FD0)
    if lights:
        p = poly([(x + 460 * s, y - 60 * s), (x + 1100 * s, y - 180 * s), (x + 1100 * s, y + 40 * s)], close=True)
        fill(c, p, 0x55FFF6C8)
        c.drawCircle(x + 452 * s, y - 50 * s, 14 * s, _p(0xFFFFF6C8))


def _jet(c, x, y, s=1.0, ang=0.0):
    c.save(); c.translate(x, y); c.rotate(ang)
    body = skia.Rect.MakeXYWH(-260 * s, -34 * s, 520 * s, 68 * s)
    c.drawRoundRect(body, 34 * s, 34 * s, _p(0xFFF7F7F7)); c.drawRoundRect(body, 34 * s, 34 * s, _p(INK, 5))
    wing = poly([(-40 * s, 0), (60 * s, 0), (-60 * s, 150 * s), (-120 * s, 150 * s)], close=True); fill(c, wing, 0xFFDADDE2); ink(c, wing, 4)
    tail = poly([(-250 * s, -20 * s), (-190 * s, -20 * s), (-240 * s, -130 * s), (-280 * s, -130 * s)], close=True); fill(c, tail, 0xFF2F7FD0); ink(c, tail, 4)
    for k in range(9):
        c.drawCircle(-150 * s + k * 40 * s, -8 * s, 8 * s, _p(0xFF2E3A48))
    c.drawCircle(250 * s, 0, 6 * s, _p(0xFFFF4040))
    c.restore()


def _sky(c, v):
    P._sky(c, v)


# ------------------------------------------------------------------ platserna

def bg_hotel_lobby(c, t, v):
    _room(c, v)
    # svängdörr i glas till vänster
    gx, gy, gw, gh = W * 0.03, H * 0.2, W * 0.34, GROUND - H * 0.2
    _grad(c, (gx, gy, gw, gh), [0xFF26324A, 0xFF3E5068] if _n(v) else [0xFF8FB5D8, 0xFFCFE2EE])
    ink(c, skia.Rect.MakeXYWH(gx, gy, gw, gh), 10, 0xFFB8A070)
    cx = gx + gw / 2
    ang = (t * 2.2) if v.get("revolving_door") == "spinning" else 0.4
    for k in range(4):
        a = ang + k * math.pi / 2
        line(c, cx, gy + 20, cx + math.cos(a) * gw * 0.42, gy + 20, 0, 0)
        xx = cx + math.cos(a) * gw * 0.42
        line(c, xx, gy + 30, xx, GROUND - 10, 8, 0xFFB8A070)
    line(c, cx, gy + 30, cx, GROUND - 10, 10, 0xFFB8A070)
    E.draw_text(c, "WELCOME", cx, gy - 20, E.font(E.FONT_BOLD, 40), color=INK)
    st = v.get("chandelier", "on" if not _n(v) else "on")
    for x in (W * 0.5, W * 0.78):
        _chandelier(c, x, H * 0.2, st, 1.0)
    # bar/disk till höger
    bar = skia.Rect.MakeXYWH(W * 0.62, H * 0.56, W * 0.34, GROUND - H * 0.56); fill(c, bar, 0xFF6B3E2A); ink(c, bar, 6)
    top = skia.Rect.MakeXYWH(W * 0.61, H * 0.54, W * 0.36, 24); fill(c, top, 0xFFD9C29A); ink(c, top, 4)
    for k in range(3):   # fåtöljer
        box(c, W * 0.4 + k * 120, GROUND - 70, 90, 70, 0xFF2F6B5E, 4, 12)
    if v.get("emergency_lights"):
        _emergency(c, W * 0.08, H * 0.1); _emergency(c, W * 0.86, H * 0.1)
    if _n(v):
        _exit_sign(c, W * 0.44, H * 0.1)
    if v.get("flashlight"):
        _flashlight(c, W * 0.74, H * 0.6, W * 0.25, H * 0.62)
    _carpet(c, v)


def bg_front_desk(c, t, v):
    _room(c, v, day=0xFFEFE3CE)
    # nyckelskåp
    if v.get("key_rack", True):
        kr = skia.Rect.MakeXYWH(W * 0.06, H * 0.12, W * 0.26, H * 0.32); fill(c, kr, 0xFF8A5A36); ink(c, kr, 5)
        for i in range(5):
            for j in range(6):
                x = W * 0.075 + j * W * 0.04; y = H * 0.15 + i * H * 0.058
                fill(c, skia.Rect.MakeXYWH(x, y, W * 0.032, H * 0.045), 0xFFF1E6D2)
                line(c, x + W * 0.016, y + 8, x + W * 0.016, y + 28, 3, GOLD)
    # CCTV-väggen
    n = int(v.get("cctv") or 9)
    cols = 4 if n >= 16 else 3
    rows = math.ceil(n / cols)
    for k in range(n):
        r_, c_ = divmod(k, cols)
        x = W * 0.62 + c_ * 92; y = H * 0.1 + r_ * 66
        m = skia.Rect.MakeXYWH(x, y, 84, 58); fill(c, m, 0xFF3D5A70 if k % 3 else 0xFF4F7088); ink(c, m, 3)
        line(c, x + 10, y + 46, x + 74, y + 46, 2, 0x55FFFFFF)
    # disken
    desk = skia.Rect.MakeXYWH(W * 0.04, H * 0.58, W * 0.92, GROUND - H * 0.58); fill(c, desk, 0xFF7A4A2E); ink(c, desk, 6)
    top = skia.Rect.MakeXYWH(W * 0.03, H * 0.56, W * 0.94, 26); fill(c, top, 0xFFE3D2B0); ink(c, top, 4)
    E.draw_text(c, "RECEPTION", W * 0.5, H * 0.68, E.font(E.FONT_BOLD, 46), color=GOLD)
    if v.get("bell", True):
        bx = W * 0.44
        p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(bx - 40, H * 0.5, 80, 70), 180, 180)
        c.drawPath(p, _p(GOLD)); c.drawPath(p, _p(INK, 4)); box(c, bx - 50, H * 0.555, 100, 10, 0xFF8A7040, 3, 2)
        c.drawCircle(bx, H * 0.495, 8, _p(GOLD))
    ph = v.get("phones")
    for k in range(3):
        x = W * 0.22 + k * 70
        box(c, x, H * 0.52, 54, 32, 0xFF2B3A55, 3, 6)
        if ph == "ringing":
            for j in range(3):
                line(c, x + 27 - 20 + j * 20, H * 0.5, x + 27 - 30 + j * 30, H * 0.46 - (j % 2) * 10, 3, 0xFFD8342A)
    if v.get("switch_panel"):
        sp = skia.Rect.MakeXYWH(W * 0.36, H * 0.14, W * 0.2, H * 0.26); fill(c, sp, 0xFFC8CCD2); ink(c, sp, 5)
        E.draw_text(c, "LIGHTS", W * 0.46, H * 0.19, E.font(E.FONT_BOLD, 30), color=INK)
        for k in range(8):
            r_, c_ = divmod(k, 4)
            x = W * 0.375 + c_ * W * 0.045; y = H * 0.23 + r_ * H * 0.08
            box(c, x, y, 34, 48, 0xFFFFFFFF, 3, 4)
            fill(c, skia.Rect.MakeXYWH(x + 8, y + (6 if k % 3 else 24), 18, 18), 0xFF1F9D55 if k % 3 else 0xFFD8342A)
    if v.get("salt_shakers"):
        for k in range(5):
            x = W * 0.55 + k * 46
            box(c, x, H * 0.49, 30, 46, 0xFFFFFFFF, 3, 8)
            fill(c, skia.Rect.MakeXYWH(x + 4, H * 0.485, 22, 10), 0xFF9AA4AE)
    if _n(v):
        _exit_sign(c, W * 0.44, H * 0.04)
    _carpet(c, v)


def bg_hallway(c, t, v):
    hl = v.get("hall_lights", "on" if not _n(v) else "on")
    dark = hl == "off"
    _room(c, v, day=0xFFF3EAD8, night=0xFF46506A if dark else 0xFF5F6B88, wain=0xFFC9A77A, wain_n=0xFF3E4560)
    num0 = 701 if v.get("door_number") else 210
    for k in range(5):
        x = 80 + k * 380
        d = skia.Rect.MakeXYWH(x, H * 0.24, 190, GROUND - H * 0.24); fill(c, d, 0xFF8A5A36 if not dark else 0xFF5A3E2E); ink(c, d, 5)
        c.drawCircle(x + 160, H * 0.56, 9, _p(GOLD))
        lab = str(v["door_number"]) if (v.get("door_number") and k == 2) else str(num0 + k * 2)
        plate = skia.Rect.MakeXYWH(x + 55, H * 0.29, 80, 40); fill(c, plate, GOLD); ink(c, plate, 3)
        E.draw_text(c, lab, x + 95, H * 0.29 + 32, E.font(E.FONT_BOLD, 28), color=INK)
        if v.get("doors_closed"):
            box(c, x + 40, H * 0.4, 110, 30, 0xFFFFFFFF, 2, 4)
            E.draw_text(c, "DO NOT DISTURB", x + 95, H * 0.4 + 22, E.font(E.FONT_BOLD, 13), color=0xFFD8342A)
    for k in range(4):   # vägglampetter
        x = 270 + k * 380
        on = hl == "on" or (hl == "flicker" and k % 2 == 0)
        p = poly([(x - 26, H * 0.2), (x + 26, H * 0.2), (x + 16, H * 0.15), (x - 16, H * 0.15)], close=True)
        fill(c, p, 0xFFFFF1C2 if on else 0xFF7A7A70); ink(c, p, 3)
        if on:
            _glow(c, x, H * 0.22, 220, 0x55FFE7A0)
    if v.get("sensor"):
        sx, sy = W * 0.86, H * 0.12
        c.drawCircle(sx, sy, 34, _p(0xFFF4F4F4)); c.drawCircle(sx, sy, 34, _p(INK, 4))
        c.drawCircle(sx, sy, 10, _p(0xFFD8342A if (int(t * 2) % 2 == 0) else 0xFF8A2A2A))
        for r in (60, 90):
            p = skia.Path(); p.addArc(skia.Rect.MakeXYWH(sx - r, sy - r, 2 * r, 2 * r), 100, 70)
            c.drawPath(p, _p(0x88D8342A, 4))
        E.draw_text(c, "MOTION SENSOR", sx, sy + 66, E.font(E.FONT_BOLD, 22), color=0xFFFFFFFF if _n(v) else INK)
    if v.get("ice_machine"):
        im = skia.Rect.MakeXYWH(W * 0.82, H * 0.38, 170, GROUND - H * 0.38); fill(c, im, 0xFFDCE6EE); ink(c, im, 5)
        E.draw_text(c, "ICE", W * 0.82 + 85, H * 0.46, E.font(E.FONT_BLACK, 44), color=0xFF2F7FD0)
    if v.get("candles"):
        for k in range(6):
            x = 200 + k * 290
            box(c, x, GROUND - 46, 18, 46, 0xFFFFF8E8, 2, 3)
            c.drawCircle(x + 9, GROUND - 56, 8, _p(0xFFFFC34A)); _glow(c, x + 9, GROUND - 56, 90, 0x55FFC34A)
    if v.get("smoke"):
        P._smoke(c, t, W * 0.5, H * 0.5); P._smoke(c, t + 1.3, W * 0.25, H * 0.45)
    if v.get("alarm_light"):
        on = int(t * 3) % 2 == 0
        c.drawCircle(W * 0.5, H * 0.06, 26, _p(0xFFD8342A if on else 0xFF7A2A2A))
        if on:
            _glow(c, W * 0.5, H * 0.1, 400, 0x44FF4040)
    if v.get("exit_sign") or _n(v):
        _exit_sign(c, W * 0.06, H * 0.08)
    if v.get("crowd") == "people":
        P._people(c, t, 6, s=250, seed=11)
    if v.get("flashlight"):
        _flashlight(c, W * 0.3, H * 0.55, W * 0.8, H * 0.6)
    _carpet(c, v, col=0xFF2F5E6B)


def bg_stairwell(c, t, v):
    fill(c, skia.Rect.MakeWH(W, H), 0xFF5C6680 if _n(v) else 0xFFE6E2D8)
    for k in range(6):   # trappsteg diagonalt
        x = W * 0.25 + k * 130; y = GROUND - k * 70
        box(c, x, y - 70, 140, 70, 0xFF9AA0A8 if _n(v) else 0xFFC4C2BA, 4, 0)
    line(c, W * 0.25, GROUND - 120, W * 0.25 + 6 * 130, GROUND - 120 - 6 * 70, 8, 0xFFD9443A)
    if v.get("door_numbers"):
        for k, num in enumerate(("6", "7", "8")):
            x = W * 0.05 + k * W * 0.0
            d = skia.Rect.MakeXYWH(W * 0.04, H * 0.22, 200, GROUND - H * 0.22)
        d = skia.Rect.MakeXYWH(W * 0.04, H * 0.22, 220, GROUND - H * 0.22); fill(c, d, 0xFF9DB1C9); ink(c, d, 5)
        E.draw_text(c, "7", W * 0.04 + 110, H * 0.42, E.font(E.FONT_BLACK, 140), color=INK)
        E.draw_text(c, "FLOOR", W * 0.04 + 110, H * 0.27, E.font(E.FONT_BOLD, 34), color=INK)
        big = skia.Rect.MakeXYWH(W * 0.8, H * 0.14, 220, 160); fill(c, big, 0xFFF2C230); ink(c, big, 5)
        E.draw_text(c, "8", W * 0.8 + 110, H * 0.14 + 130, E.font(E.FONT_BLACK, 120), color=INK)
    if v.get("exit_sign") or _n(v):
        _exit_sign(c, W * 0.44, H * 0.08)
    if v.get("flashlight"):
        _flashlight(c, W * 0.3, H * 0.55, W * 0.75, H * 0.35)
    _concrete_floor(c, v)


def bg_parking_garage(c, t, v):
    lit = v.get("garage_lights") != "off"
    fill(c, skia.Rect.MakeWH(W, H), (0xFF4E5870 if not lit else 0xFF6A7488) if _n(v) else 0xFFC9C6BE)
    fill(c, skia.Rect.MakeXYWH(0, 0, W, H * 0.12), 0xFF8E9199)   # tak
    line(c, 0, H * 0.12, W, H * 0.12, 5)
    for k in range(5):   # pelare
        x = 80 + k * 440
        box(c, x, H * 0.12, 80, GROUND - H * 0.12, 0xFFB4B2AA if not _n(v) else 0xFF7C8494, 5, 0)
        fill(c, skia.Rect.MakeXYWH(x, H * 0.5, 80, 40), 0xFFF2C230)
        E.draw_text(c, "P%d" % (k + 1), x + 40, H * 0.5 + 32, E.font(E.FONT_BOLD, 26), color=INK)
    for k in range(4):   # taklampor
        x = 280 + k * 440
        r = skia.Rect.MakeXYWH(x - 70, H * 0.12, 140, 16); fill(c, r, 0xFFF6FAFF if lit else 0xFF52606C); ink(c, r, 3)
        if lit:
            _glow(c, x, H * 0.18, 240, 0x44FFF8E0)
    n = int(v.get("lanterns") or 0)
    out = int(v.get("lanterns_out") or 0)
    if n:
        m = 14
        for k in range(m):
            x = 60 + k * (W - 120) / (m - 1); y = GROUND - 10 + (k % 2) * 14
            _lantern(c, x, y, 0.9, lit=not (out and k in (5, 6, 7)[:out]))
    if v.get("lantern_light"):
        _lantern(c, W * 0.5, H * 0.5, 1.4); _glow(c, W * 0.5, H * 0.55, 420, 0x44FFD070)
    if v.get("shuttle_parked") or v.get("shuttle_moving"):
        sx = W * 0.42
        if v.get("shuttle_moving"):
            sx = W * 0.2 + (t * 60) % (W * 0.3)
        _shuttle(c, sx, GROUND - 4, 0.95, lights=bool(v.get("headlights") or v.get("shuttle_moving")))
    elif v.get("headlights"):
        _shuttle(c, W * 0.1, GROUND - 4, 0.95, lights=True)
    if v.get("flashlight"):
        _flashlight(c, W * 0.3, H * 0.55, W * 0.8, H * 0.62)
    _concrete_floor(c, v)
    for k in range(6):
        line(c, 120 + k * 330, GROUND + 30, 80 + k * 330, H, 6, 0xFFF2F2F2)


def bg_loading_dock(c, t, v):
    _sky(c, v)
    wall = skia.Rect.MakeXYWH(0, H * 0.14, W * 0.7, GROUND - H * 0.14); fill(c, wall, 0xFFB9A88E if not _n(v) else 0xFF5E6276); ink(c, wall, 5)
    for k in range(2):
        dr = skia.Rect.MakeXYWH(60 + k * 520, H * 0.3, 420, GROUND - H * 0.3); fill(c, dr, 0xFF8E979E); ink(c, dr, 5)
        for j in range(8):
            line(c, 60 + k * 520, H * 0.3 + j * 50, 480 + k * 520, H * 0.3 + j * 50, 2, 0x33000000)
    E.draw_text(c, "LOADING DOCK", W * 0.35, H * 0.24, E.font(E.FONT_BOLD, 46), color=INK)
    if v.get("generator"):
        gx = W * 0.72
        box(c, gx, GROUND - 200, 380, 200, 0xFFD4A62A, 6, 12)
        E.draw_text(c, "DIESEL GENERATOR", gx + 190, GROUND - 130, E.font(E.FONT_BOLD, 30), color=INK)
        if v.get("gauge"):
            cx, cy = gx + 190, GROUND - 60
            c.drawCircle(cx, cy, 44, _p(0xFFFFFFFF)); c.drawCircle(cx, cy, 44, _p(INK, 4))
            a = math.radians(200 if v.get("gauge") == "low" else 270)
            line(c, cx, cy, cx + math.cos(a) * 36, cy + math.sin(a) * 36, 5, 0xFFD8342A)
            E.draw_text(c, "E", cx - 30, cy + 12, E.font(E.FONT_BOLD, 22), color=0xFFD8342A)
            E.draw_text(c, "F", cx + 30, cy + 12, E.font(E.FONT_BOLD, 22), color=INK)
        if v.get("cord"):
            p = skia.Path(); p.moveTo(gx, GROUND - 60); p.cubicTo(W * 0.5, GROUND + 60, W * 0.3, GROUND - 20, W * 0.1, GROUND - 120)
            c.drawPath(p, _p(0xFFF28C28, 9))
        P._smoke(c, t, gx + 340, GROUND - 210)
    if v.get("emergency_lights"):
        _emergency(c, W * 0.3, H * 0.16)
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFF7E8188 if _n(v) else 0xFFB8B6AE)
    line(c, 0, GROUND, W, GROUND, 5)


def bg_kitchen(c, t, v):
    fill(c, skia.Rect.MakeWH(W, H), 0xFFE9EEF1 if not _n(v) else 0xFF5C6A7E)
    for k in range(0, int(W), 70):
        for j in range(0, int(H * 0.56), 70):
            ink(c, skia.Rect.MakeXYWH(k, j, 70, 70), 1, 0x18000000)
    if v.get("walk_in", True):
        wi = skia.Rect.MakeXYWH(W * 0.04, H * 0.14, W * 0.24, GROUND - H * 0.14); fill(c, wi, 0xFFC9D1D8); ink(c, wi, 6)
        line(c, W * 0.25, H * 0.4, W * 0.25, H * 0.56, 10, 0xFF8E979E)
        E.draw_text(c, "WALK-IN", W * 0.16, H * 0.22, E.font(E.FONT_BOLD, 40), color=0xFF2F7FD0)
        E.draw_text(c, "COOLER", W * 0.16, H * 0.27, E.font(E.FONT_BOLD, 34), color=0xFF2F7FD0)
    fz = v.get("freezer")
    if fz:
        fr = skia.Rect.MakeXYWH(W * 0.32, H * 0.3, W * 0.18, GROUND - H * 0.3); fill(c, fr, 0xFFE4ECF2); ink(c, fr, 5)
        E.draw_text(c, "FREEZER", W * 0.41, H * 0.36, E.font(E.FONT_BOLD, 32), color=0xFF2F7FD0)
        lvl = 0.5 if fz == "half" else 0.92
        bx = skia.Rect.MakeXYWH(W * 0.34, H * 0.4, W * 0.14, (GROUND - H * 0.42))
        ink(c, bx, 3, 0xFF8E979E)
        hh = (GROUND - H * 0.42) * lvl
        fill(c, skia.Rect.MakeXYWH(W * 0.34, GROUND - H * 0.02 - hh, W * 0.14, hh), 0xFF9FD0F0)
        E.draw_text(c, "1/2" if fz == "half" else "FULL", W * 0.41, GROUND - 30, E.font(E.FONT_BLACK, 40), color=INK)
    # spis och bänk
    cnt = skia.Rect.MakeXYWH(W * 0.54, H * 0.56, W * 0.44, GROUND - H * 0.56); fill(c, cnt, 0xFFB8C0C6); ink(c, cnt, 5)
    if v.get("grill"):
        g = skia.Rect.MakeXYWH(W * 0.58, H * 0.52, W * 0.2, 30); fill(c, g, 0xFF3A3A3A); ink(c, g, 4)
        for k in range(8):
            line(c, W * 0.58 + 20 + k * 44, H * 0.52 + 4, W * 0.58 + 20 + k * 44, H * 0.52 + 26, 3, 0xFFF28C28)
    if v.get("steam"):
        for k in range(5):
            ph = (t * 0.4 + k / 5) % 1
            c.drawCircle(W * 0.66 + math.sin(k * 2 + t) * 30, H * 0.5 - ph * 260, 30 + ph * 50, _p(0x55FFFFFF))
    for k in range(5):   # kastruller på hylla
        x = W * 0.56 + k * 150
        box(c, x, H * 0.2, 110, 70, 0xFF9AA4AE, 4, 10)
    line(c, W * 0.54, H * 0.29, W * 0.98, H * 0.29, 6)
    if v.get("clock"):
        cx, cy = W * 0.9, H * 0.1
        c.drawCircle(cx, cy, 56, _p(0xFFFFFFFF)); c.drawCircle(cx, cy, 56, _p(INK, 5))
        line(c, cx, cy, cx, cy - 40, 5); line(c, cx, cy, cx + 30, cy, 6)
        E.draw_text(c, str(v["clock"]), cx, cy + 96, E.font(E.FONT_BOLD, 36), color=INK)
    P._board(c, v, x=W * 0.56, y=H * 0.32, w=W * 0.4, h=H * 0.2) if v.get("board") else None
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFFCCC8BE if not _n(v) else 0xFF6F7A86)
    line(c, 0, GROUND, W, GROUND, 5)


def bg_breakfast_room(c, t, v):
    _room(c, v, day=0xFFF6EBD6, night=0xFF6A6F88)
    for k in range(3):   # fönster
        w_ = skia.Rect.MakeXYWH(W * 0.08 + k * W * 0.3, H * 0.1, W * 0.22, H * 0.36)
        _grad(c, (w_.left(), w_.top(), w_.width(), w_.height()), [0xFF26324A, 0xFF3E5068] if _n(v) else [0xFF8CC4EA, 0xFFE2F1F8])
        ink(c, w_, 6, 0xFFFFFFFF)
    E.draw_text(c, "BREAKFAST", W * 0.5, H * 0.54, E.font(E.FONT_BOLD, 44), color=GOLD)
    for x in (W * 0.5, W * 0.8):
        _chandelier(c, x, H * 0.08, "on" if v.get("lights") != "off" else "off", 0.7)
    for k in range(4):
        x = W * 0.1 + k * W * 0.23
        box(c, x, GROUND + 30, 260, 22, 0xFFFFFFFF, 4, 4)
    if v.get("crowd") == "people":
        P._people(c, t, 8, s=230, seed=31)
    _carpet(c, v)


def bg_electrical_room(c, t, v):
    fill(c, skia.Rect.MakeWH(W, H), 0xFFD9D6CC if not _n(v) else 0xFF566577)
    pn = skia.Rect.MakeXYWH(W * 0.08, H * 0.1, W * 0.5, GROUND - H * 0.16); fill(c, pn, 0xFF9AA4AE); ink(c, pn, 6)
    E.draw_text(c, "BREAKER PANEL – FLOOR 7", W * 0.33, H * 0.17, E.font(E.FONT_BOLD, 36), color=INK)
    for k in range(16):
        r_, c_ = divmod(k, 4)
        x = W * 0.11 + c_ * W * 0.115; y = H * 0.22 + r_ * H * 0.12
        box(c, x, y, W * 0.09, H * 0.09, 0xFFEFEFEF, 3, 4)
        fill(c, skia.Rect.MakeXYWH(x + W * 0.035, y + 10, W * 0.02, H * 0.035), INK)
    if v.get("override"):
        ov = skia.Rect.MakeXYWH(W * 0.64, H * 0.24, W * 0.28, H * 0.34); fill(c, ov, 0xFFF2C230); ink(c, ov, 6)
        E.draw_text(c, "OVERRIDE", W * 0.78, H * 0.32, E.font(E.FONT_BLACK, 50), color=INK)
        on = str(v.get("override")).upper() == "ON"
        sw = skia.Rect.MakeXYWH(W * 0.74, H * 0.36, W * 0.08, H * 0.16); fill(c, sw, 0xFFFFFFFF); ink(c, sw, 5)
        fill(c, skia.Rect.MakeXYWH(W * 0.75, H * 0.37 if on else H * 0.44, W * 0.06, H * 0.07), 0xFF1F9D55 if on else 0xFFD8342A)
        E.draw_text(c, "ON" if on else "AUTO", W * 0.78, H * 0.56, E.font(E.FONT_BOLD, 36), color=INK)
    _concrete_floor(c, v)


def bg_guest_room(c, t, v):
    _room(c, v, day=0xFFF4ECDD)
    bed = skia.Rect.MakeXYWH(W * 0.05, GROUND - 160, W * 0.36, 160); fill(c, bed, 0xFFFFFFFF); ink(c, bed, 5)
    fill(c, skia.Rect.MakeXYWH(W * 0.05, GROUND - 160, W * 0.36, 40), WINE)
    hb = skia.Rect.MakeXYWH(W * 0.05, GROUND - 300, 40, 300); fill(c, hb, 0xFF8A5A36); ink(c, hb, 4)
    if v.get("bathroom", True):
        bt = skia.Rect.MakeXYWH(W * 0.5, H * 0.12, W * 0.46, GROUND - H * 0.12); fill(c, bt, 0xFFE8F1F6); ink(c, bt, 6)
        for k in range(0, int(W * 0.46), 60):
            line(c, W * 0.5 + k, H * 0.12, W * 0.5 + k, GROUND, 1, 0x22000000)
        # toalett med cistern
        cs = skia.Rect.MakeXYWH(W * 0.62, H * 0.4, 170, 120); fill(c, cs, 0xFFFFFFFF); ink(c, cs, 5)
        E.draw_text(c, "TANK", W * 0.62 + 85, H * 0.4 + 72, E.font(E.FONT_BOLD, 30), color=0xFF2F7FD0)
        bowl = skia.Rect.MakeXYWH(W * 0.62 + 10, H * 0.4 + 120, 150, GROUND - H * 0.4 - 120); fill(c, bowl, 0xFFFFFFFF); ink(c, bowl, 5)
        box(c, W * 0.82, H * 0.42, 150, 60, 0xFFFFFFFF, 4, 8)   # handfat
    _carpet(c, v, col=0xFF9C8A70)


def bg_basement(c, t, v):
    fill(c, skia.Rect.MakeWH(W, H), 0xFF56607A if _n(v) else 0xFFC8C2B4)
    for k in range(5):   # rör i taket
        line(c, 0, 40 + k * 24, W, 40 + k * 24, 10, 0xFF8E979E)
    n = int(v.get("boilers") or 2)
    for k in range(n):
        x = W * 0.5 + k * 360
        r = skia.Rect.MakeXYWH(x, H * 0.24, 280, GROUND - H * 0.24)
        c.drawRoundRect(r, 60, 60, _p(0xFFB8C0C6)); c.drawRoundRect(r, 60, 60, _p(INK, 6))
        E.draw_text(c, "WATER", x + 140, H * 0.42, E.font(E.FONT_BOLD, 34), color=INK)
        E.draw_text(c, "HEATER %d" % (k + 1), x + 140, H * 0.47, E.font(E.FONT_BOLD, 28), color=INK)
        c.drawCircle(x + 140, H * 0.58, 26, _p(0xFFFFFFFF)); c.drawCircle(x + 140, H * 0.58, 26, _p(INK, 4))
    if v.get("lantern_light"):
        _lantern(c, W * 0.2, H * 0.5, 1.4); _glow(c, W * 0.2, H * 0.55, 420, 0x44FFD070)
    if v.get("flashlight"):
        _flashlight(c, W * 0.12, H * 0.55, W * 0.55, H * 0.55)
    _concrete_floor(c, v)


def bg_parking_lot(c, t, v):
    _sky(c, v)
    # hotellfasaden i bakgrunden
    fa = skia.Rect.MakeXYWH(W * 0.05, H * 0.1, W * 0.4, GROUND - H * 0.1); fill(c, fa, 0xFFD9CDB8 if not _n(v) else 0xFF6A6F88); ink(c, fa, 5)
    for i in range(7):
        for j in range(5):
            fill(c, skia.Rect.MakeXYWH(W * 0.07 + j * W * 0.075, H * 0.14 + i * H * 0.075, W * 0.05, H * 0.045), 0xFFFFE7A0 if (i + j) % 3 == 0 else 0xFF3E5068)
    lit = v.get("lot_lights") != "off"
    for k in range(3):
        x = W * 0.55 + k * W * 0.16
        line(c, x, GROUND, x, H * 0.24, 8, 0xFF6A737C)
        box(c, x - 40, H * 0.22, 80, 20, 0xFFF6FAFF if lit else 0xFF52606C, 3, 4)
        if lit:
            _glow(c, x, H * 0.3, 260, 0x44FFF8E0)
    if v.get("floodlight"):
        fx, fy = W * 0.48, H * 0.2
        box(c, fx - 50, fy - 30, 100, 60, 0xFFF6FAFF, 4, 6)
        p = poly([(fx, fy), (W * 0.05, GROUND + 60), (W * 0.45, GROUND + 60)], close=True); fill(c, p, 0x44FFF6C8)
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFF6E727A if _n(v) else 0xFF8E9199)
    line(c, 0, GROUND, W, GROUND, 5)
    for k in range(7):
        line(c, 80 + k * 280, GROUND + 20, 40 + k * 280, H, 6, 0xFFF2F2F2)
    cols = [0xFF4E8FCB, 0xFFD9443A, 0xFFE8E8E8]
    for k in range(3):
        x = W * 0.5 + k * 320
        body = skia.Rect.MakeXYWH(x, GROUND - 100, 260, 80); fill(c, body, cols[k]); ink(c, body, 5)
        for wx in (x + 50, x + 210):
            c.drawCircle(wx, GROUND - 22, 24, _p(0xFF222222))


def _runway(c, v, t, y0=GROUND - 40):
    fill(c, skia.Rect.MakeXYWH(0, H * 0.55, W, H * 0.45), 0xFF6F8F5A if not _n(v) else 0xFF3E5246)   # gräs
    rw = poly([(W * 0.0, H * 0.98), (W * 1.0, H * 0.98), (W * 0.78, H * 0.6), (W * 0.22, H * 0.6)], close=True)
    fill(c, rw, 0xFF5A5E66 if _n(v) else 0xFF7E8288); ink(c, rw, 5)
    for k in range(6):   # mittlinje
        f = k / 6
        y = H * 0.6 + (H * 0.38) * f
        line(c, W / 2, y + 6, W / 2, y + 22 + 20 * f, 6 + 6 * f, 0xFFFFFFFF if v.get("centerline") != "green" else 0xFF3FD27A)
    if v.get("runway_lights") or v.get("end_lights"):
        for k in range(10):
            f = k / 9
            y = H * 0.6 + H * 0.38 * f
            xl = W * 0.22 - W * 0.22 * f; xr = W * 0.78 + W * 0.22 * f
            for x in (xl, xr):
                c.drawCircle(x, y, 7 + 9 * f, _p(0xFFFFFFFF)); _glow(c, x, y, 40 + 60 * f, 0x66FFFFFF)
    if v.get("end_lights"):
        for k in range(8):
            x = W * 0.24 + k * W * 0.075
            col = 0xFF3FD27A if k % 2 == 0 else 0xFFD8342A
            c.drawCircle(x, H * 0.6, 9, _p(col)); _glow(c, x, H * 0.6, 50, (col & 0x00FFFFFF) | 0x66000000)
    if v.get("taxi_lights"):
        for k in range(14):
            x = W * 0.02 + k * W * 0.07
            c.drawCircle(x, H * 0.57, 8, _p(0xFF3F7BFF)); _glow(c, x, H * 0.57, 46, 0x663F7BFF)


def bg_airfield(c, t, v):
    _sky(c, v)
    # terminal + torn långt bort
    fill(c, skia.Rect.MakeXYWH(W * 0.62, H * 0.4, W * 0.34, H * 0.15), 0xFFB8C0C6 if not _n(v) else 0xFF4E5870)
    for k in range(10):
        fill(c, skia.Rect.MakeXYWH(W * 0.63 + k * W * 0.033, H * 0.43, W * 0.022, H * 0.05), 0xFFFFE7A0)
    box(c, W * 0.86, H * 0.2, 46, H * 0.2, 0xFFB8C0C6, 4, 0); box(c, W * 0.84, H * 0.16, 100, 50, 0xFF9CC3D5, 4, 6)
    _runway(c, v, t)
    j = v.get("jet")
    if j == "takeoff":
        _jet(c, W * 0.5 + (t * 40) % 300, H * 0.6 - min(60, t * 10), 0.9, -0.08)
    elif j == "climbing":
        _jet(c, W * 0.35 + t * 50, H * 0.28 - t * 14, 0.7, -0.22)
    elif j:
        _jet(c, W * 0.5, H * 0.62, 0.9, 0)
    if v.get("shuttle_moving"):
        _shuttle(c, W * 0.2 + t * 40, H * 0.7, 0.8, lights=True)


def bg_hotel_roof(c, t, v):
    _sky(c, v)
    if v.get("airfield_view", True):
        fill(c, skia.Rect.MakeXYWH(0, H * 0.42, W, H * 0.2), 0xFF6F8F5A)
        line(c, W * 0.1, H * 0.52, W * 0.9, H * 0.48, 22, 0xFF7E8288)
        for k in range(12):
            x = W * 0.1 + k * W * 0.073
            c.drawCircle(x, H * 0.52 - k * 3.6, 6, _p(0xFFFFFFFF)); _glow(c, x, H * 0.52 - k * 3.6, 30, 0x66FFFFFF)
        _jet(c, W * 0.7, H * 0.46, 0.35, 0)
    roof = skia.Rect.MakeXYWH(0, H * 0.62, W, H * 0.38); fill(c, roof, 0xFF9A968C); ink(c, roof, 5)
    for k in range(3):
        box(c, W * 0.06 + k * 200, H * 0.52, 140, H * 0.1, 0xFFB8C0C6, 4, 6)   # ventilation
    line(c, 0, H * 0.62, W, H * 0.62, 10, 0xFFD9443A)


def bg_hotel_exterior(c, t, v):
    _sky(c, v)
    fa = skia.Rect.MakeXYWH(W * 0.2, H * 0.08, W * 0.6, GROUND - H * 0.08); fill(c, fa, 0xFFD9CDB8); ink(c, fa, 6)
    for i in range(9):
        for j in range(8):
            lit = v.get("windows_lit") and (i * 3 + j * 5) % 4 != 0
            fill(c, skia.Rect.MakeXYWH(W * 0.23 + j * W * 0.07, H * 0.11 + i * H * 0.068, W * 0.045, H * 0.04),
                 0xFFFFE08A if lit else 0xFF3E5068)
    sg = skia.Rect.MakeXYWH(W * 0.36, H * 0.02, W * 0.28, 60); fill(c, sg, WINE); ink(c, sg, 4)
    E.draw_text(c, "AIRPORT HOTEL", W / 2, H * 0.02 + 46, E.font(E.FONT_BOLD, 40), color=GOLD)
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFF8E9199); line(c, 0, GROUND, W, GROUND, 5)


def _plan(title):
    def bg(c, t, v):
        P.bg_prison_map(c, t, v)
        fill(c, skia.Rect.MakeXYWH(W * 0.2, H * 0.02, W * 0.6, H * 0.08), 0xFFEAF0F6)
        E.draw_text(c, title, W / 2, H * 0.08, E.font(E.FONT_BLACK, 52), color=0xFF1F4FA0)
    return bg


PLACES = {"hotel_lobby": bg_hotel_lobby, "front_desk": bg_front_desk, "hallway": bg_hallway, "stairwell": bg_stairwell,
          "parking_garage": bg_parking_garage, "loading_dock": bg_loading_dock, "kitchen": bg_kitchen,
          "breakfast_room": bg_breakfast_room, "electrical_room": bg_electrical_room, "guest_room": bg_guest_room,
          "basement": bg_basement, "parking_lot": bg_parking_lot, "hotel_roof": bg_hotel_roof, "airfield": bg_airfield,
          "hotel_exterior": bg_hotel_exterior, "hotel_map": _plan("HOTEL PLAN"), "airfield_map": _plan("AIRFIELD PLAN")}
OUTDOOR = {"loading_dock", "parking_lot", "hotel_roof", "airfield", "hotel_exterior", "hotel_map", "airfield_map"}
MAPS = {"hotel_map", "airfield_map"}

# ------------------------------------------------------------------ föremål


def _i_keycard(c, hx, hy, s, lw):
    box(c, hx - s * 0.01, hy - s * 0.06, s * 0.1, s * 0.065, 0xFFFFFFFF, lw * 0.4, 3)
    fill(c, skia.Rect.MakeXYWH(hx, hy - s * 0.05, s * 0.08, s * 0.015), 0xFF2F7FD0)


def _i_flashlight(c, hx, hy, s, lw):
    line(c, hx, hy, hx + s * 0.12, hy - s * 0.04, lw * 1.2, 0xFF2B2B2B)
    c.drawCircle(hx + s * 0.13, hy - s * 0.045, s * 0.025, _p(0xFFFFF6C8))


def _i_phone(c, hx, hy, s, lw):
    box(c, hx - s * 0.01, hy - s * 0.09, s * 0.05, s * 0.09, 0xFF2B2B2B, lw * 0.3, 3)


def _i_towels(c, hx, hy, s, lw):
    for k in range(3):
        box(c, hx - s * 0.05, hy - s * 0.02 - k * s * 0.03, s * 0.16, s * 0.03, 0xFFFFFFFF, lw * 0.3, 3)


def _i_candle(c, hx, hy, s, lw):
    box(c, hx, hy - s * 0.08, s * 0.025, s * 0.08, 0xFFFFF8E8, lw * 0.3, 2)
    c.drawCircle(hx + s * 0.012, hy - s * 0.095, s * 0.012, _p(0xFFFFC34A))


def _i_ice_bag(c, hx, hy, s, lw):
    box(c, hx - s * 0.03, hy - s * 0.06, s * 0.1, s * 0.12, 0xFFD6EEFF, lw * 0.3, 8)


def _i_spatula(c, hx, hy, s, lw):
    line(c, hx, hy, hx + s * 0.04, hy - s * 0.16, lw * 0.5, 0xFF2B2B2B)
    box(c, hx + s * 0.02, hy - s * 0.22, s * 0.05, s * 0.06, 0xFFB8C0C6, lw * 0.3, 2)


def _i_plate(c, hx, hy, s, lw):
    c.drawOval(skia.Rect.MakeXYWH(hx - s * 0.06, hy - s * 0.02, s * 0.16, s * 0.04), _p(0xFFFFFFFF))
    c.drawOval(skia.Rect.MakeXYWH(hx - s * 0.06, hy - s * 0.02, s * 0.16, s * 0.04), _p(INK, lw * 0.3))


def _i_bucket(c, hx, hy, s, lw):
    box(c, hx - s * 0.03, hy - s * 0.02, s * 0.1, s * 0.1, 0xFF4E8FCB, lw * 0.4, 4)


def _i_lantern(c, hx, hy, s, lw):
    _lantern(c, hx + s * 0.02, hy + s * 0.04, s / 330 * 1.1)


def _i_pitcher(c, hx, hy, s, lw):
    box(c, hx - s * 0.02, hy - s * 0.08, s * 0.07, s * 0.1, 0xFFD6EEFF, lw * 0.3, 4)


def _i_blanket(c, hx, hy, s, lw):
    box(c, hx - s * 0.06, hy - s * 0.04, s * 0.18, s * 0.08, 0xFF8C6BB1, lw * 0.3, 6)


def _i_bell(c, hx, hy, s, lw):
    c.drawCircle(hx + s * 0.02, hy - s * 0.02, s * 0.035, _p(GOLD))


def _i_keys(c, hx, hy, s, lw):
    c.drawCircle(hx, hy, s * 0.02, _p(GOLD, lw * 0.3)); line(c, hx, hy, hx + s * 0.05, hy + s * 0.03, lw * 0.4, GOLD)


def _i_battery(c, hx, hy, s, lw):
    box(c, hx - s * 0.02, hy - s * 0.04, s * 0.04, s * 0.08, 0xFFF28C28, lw * 0.3, 2)


ITEMS = {"keycard": _i_keycard, "flashlight": _i_flashlight, "phone": _i_phone, "towels": _i_towels, "candle": _i_candle,
         "ice_bag": _i_ice_bag, "spatula": _i_spatula, "plate": _i_plate, "bucket": _i_bucket, "lantern": _i_lantern,
         "pitcher": _i_pitcher, "blanket": _i_blanket, "bell": _i_bell, "keys": _i_keys, "battery": _i_battery}

# ------------------------------------------------------------------ de döda (frozen = stillastående)


def _dead_prop(c, t, px, prop):
    try:
        import charstyle
        k = charstyle.SCALE
    except Exception:
        k = 1.0
    for i, z in enumerate(prop.get("z", [])):
        s = z.get("size", 330) * k
        if z.get("frozen"):
            x = W * z.get("x", 0.8)
            # stelnad mitt i steget: ingen svajning (t fryst), arm framåt
            _silhouette(c, x, H * 0.82, s, 0.0, 60 + i, look=-1, arms="forward")
            continue
        sp = z.get("speed", 20)
        x = W * z.get("x", 0.8) - sp * t
        if z.get("lunge"):
            x -= max(0.0, math.sin(t * 3.0 + i)) * 26
        _silhouette(c, x, H * 0.82, s, t, 60 + i, look=-1, arms="up" if z.get("lunge") else "forward")


_ORIG_PRISON_DEAD = None


def _dead_any(c, t, px, prop):
    if any(z.get("frozen") for z in prop.get("z", [])):
        return _dead_prop(c, t, px, prop)
    return _ORIG_PRISON_DEAD(c, t, px, prop)


def enable():
    global _ORIG_PRISON_DEAD
    E.BG.update(PLACES)
    P.PLACES.update(PLACES)          # prisons scen-wrapper (skylt, zombies_in, standardhjälte) gäller hotellet
    for k, f in ITEMS.items():
        E.EXTRA_ITEMS[k] = f
    _ORIG_PRISON_DEAD = E.EXTRA_PROPS.get("prison_dead", P._dead_prop)
    E.EXTRA_PROPS["prison_dead"] = _dead_any
    try:
        import atmos
        for k in PLACES:
            if k in MAPS:
                atmos.MOOD[k] = dict(light=(0.5, 0.2), lc=0xFFFFFFFF, dark=0.05, mood=None, fg=None)
            elif k in OUTDOOR:
                atmos.MOOD[k] = dict(light=(0.6, 0.15), lc=0xFFFFF4D6, dark=0.18, mood=None, fg=None)
                atmos.OUTDOOR.add(k)
            else:
                atmos.MOOD[k] = dict(light=(0.5, 0.1), lc=0xFFFFF0D8, dark=0.2, mood="warm" if False else None, fg=None)
                atmos.OUTDOOR.discard(k)
        _oc = atmos.clutter

        def _clutter(c, t, v, m):
            if v.get("location") in PLACES:
                return
            return _oc(c, t, v, m)
        atmos.clutter = _clutter
        old = atmos._bg_key

        def _bg_key(v):
            return old(v) + json.dumps({k: v.get(k) for k in (
                "revolving_door", "chandelier", "emergency_lights", "flashlight", "key_rack", "cctv", "bell", "phones",
                "switch_panel", "salt_shakers", "hall_lights", "door_number", "doors_closed", "sensor", "ice_machine",
                "candles", "alarm_light", "exit_sign", "door_numbers", "garage_lights", "lanterns", "lanterns_out",
                "lantern_light", "shuttle_parked", "shuttle_moving", "headlights", "generator", "gauge", "cord",
                "walk_in", "freezer", "grill", "clock", "breaker_panel", "override", "bathroom", "boilers",
                "lot_lights", "floodlight", "runway_lights", "taxi_lights", "centerline", "end_lights", "jet",
                "airfield_view", "windows_lit", "dusk", "day", "night")}, default=str)
        atmos._bg_key = _bg_key
    except Exception as e:
        print("hotel atmos:", e)
