"""Last Shift – fängelset (manus ls-2026-11-25, 'Trapped In a Prison For 100 Days').
Platser: visitor_lobby, prison_yard, prison_map, sally_port, control_room, cellblock, staff_exit, fence,
kitchen, kitchen_dock, laundry, roof, hallway, parking_lot. Ljus miljö (betong, gult, marinblått), natt = blått
med gröna nödlampor, aldrig svart. crowd 'people' = människor. Visualtypen 'map' ritas som planritning.
Laddas av run_ls.py (före atmos.enable)."""
import math, random, json
import skia
import engine as E
from engine import W, H, fill, ink, box, line, poly
from mine import _p, _grad, _glow, _dust, _sign, _silhouette

INK = E.INK
GROUND = H * 0.78
NAVY = 0xFF2B3A55


def _n(v):
    return bool(v.get("night"))


def _wall(c, v, day=0xFFE8E2D4, night=0xFF566577, band=True):
    fill(c, skia.Rect.MakeWH(W, H), night if _n(v) else day)
    for k in range(10):   # betongblock
        y = 60 + k * 70
        line(c, 0, y, W, y, 2, 0x1A000000)
        off = 0 if k % 2 else 80
        for x in range(off, int(W), 160):
            line(c, x, y, x, y + 70, 2, 0x14000000)
    if band:
        fill(c, skia.Rect.MakeXYWH(0, H * 0.6, W, GROUND - H * 0.6), 0xFF3F5470 if _n(v) else 0xFF9DB1C9)


def _floor(c, v, day=0xFFBDB8AC, night=0xFF6F7A86):
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), night if _n(v) else day)
    for k in range(6):
        c.drawRect(skia.Rect.MakeXYWH(100 + k * 320, GROUND + 34, 170, 10), _p(0x2EFFFFFF))
    line(c, 0, GROUND, W, GROUND, 5)


def _lights(c, v, n=5):
    if v.get("lights") == "off":
        return
    for k in range(n):
        x = 120 + k * (W - 240) / max(1, n - 1) - 110
        on = not _n(v) or k % 2 == 0
        r = skia.Rect.MakeXYWH(x, 18, 220, 22)
        fill(c, r, 0xFFF6FAFF if on else 0xFF52606C); ink(c, r, 3)
        if on:
            _glow(c, x + 110, 60, 260, 0x44FFF8E0)


def _exit(c, x, y):
    r = skia.Rect.MakeXYWH(x, y, 120, 46); fill(c, r, 0xFF1F9D55); ink(c, r, 3)
    E.draw_text(c, "EXIT", x + 60, y + 36, E.font(E.FONT_BOLD, 32), color=0xFFFFFFFF)


def _bars(c, x, y, w, h, gap=34, col=0xFF4A5560, lw=7):
    ink(c, skia.Rect.MakeXYWH(x, y, w, h), lw + 2, col)
    k = x + gap / 2
    while k < x + w:
        line(c, k, y, k, y + h, lw, col); k += gap
    line(c, x, y + h * 0.5, x + w, y + h * 0.5, lw, col)


def _people(c, t, n=6, y=None, s=240, seed=3):
    rnd = random.Random(seed)
    cols = [0xFFE07B39, 0xFFE8E8E8, 0xFF5C8DBF, 0xFFE07B39, 0xFF8C6BB1, 0xFFE07B39]
    for i in range(n):
        x = W * (0.08 + 0.84 * (i + 0.5) / n) + rnd.uniform(-30, 30)
        E.stickman(c, x, (y or H * 0.8) - (i % 2) * 18, s * rnd.uniform(0.85, 1.0), vest=None, hat=None,
                   outfit=cols[i % len(cols)], face=-1 if i % 2 else 1, arms="down")


def _dead(c, t, n, gy, s, x0, x1, look=1, seed=0, up=0.0):
    for i in range(int(n)):
        f = (i + 0.5) / max(1, n)
        x = W * (x0 + (x1 - x0) * f) + math.sin(i * 1.9 + seed) * 8
        _silhouette(c, x, gy + (i % 2) * 10, s * (0.9 + 0.1 * (i % 3)), t, i + seed, look=look, up=up,
                    arms="up" if i % 2 else None)


def _arrow(c, x, y, direction="out", size=150, col=0xFFFFFFFF):
    d = -1 if direction in ("out", "left") else 1
    pts = [(x - d * size * 0.5, y - size * 0.18), (x + d * size * 0.15, y - size * 0.18), (x + d * size * 0.15, y - size * 0.4),
           (x + d * size * 0.55, y), (x + d * size * 0.15, y + size * 0.4), (x + d * size * 0.15, y + size * 0.18),
           (x - d * size * 0.5, y + size * 0.18)]
    p = poly(pts, close=True); fill(c, p, col); ink(c, p, 6)


def _board(c, v, x=W * 0.6, y=H * 0.14, w=W * 0.34, h=H * 0.3):
    if not v.get("board"):
        return
    r = skia.Rect.MakeXYWH(x, y, w, h); fill(c, r, 0xFFFDFDF8, ); ink(c, r, 6, 0xFF8E979E)
    f = E.font(E.FONT_BOLD, 34)
    parts = [s.strip() for s in str(v["board"]).split("·")]
    for i, s in enumerate(parts[:5]):
        for j, ln in enumerate(E.wrap(s, f, w - 50)[:2]):
            E.draw_text(c, ln, x + 26, y + 58 + i * 52 + j * 36, f, color=0xFF1F4FA0, align="left")


def _sky(c, v):
    if _n(v):
        cols = [0xFF1E2A44, 0xFF3A4C6E]
    elif v.get("dusk") or v.get("dawn"):
        cols = [0xFF6D84B8, 0xFFF2B38A]
    elif v.get("rain"):
        cols = [0xFF8E9AA8, 0xFFC4CBD3]
    else:
        cols = [0xFF8CC4EA, 0xFFE2F1F8]
    _grad(c, (0, 0, W, H * 0.7), cols)


def _rain(c, t, v):
    if not v.get("rain"):
        return
    rnd = random.Random(5)
    for k in range(160):
        x = rnd.uniform(0, W); y = (rnd.uniform(0, H) + t * 900) % H
        c.drawLine(x, y, x - 8, y + 34, _p(0x66FFFFFF, 2))


def _bus(c, x, y, s=1.0, col=0xFFF2B33D, label=None):
    r = skia.Rect.MakeXYWH(x, y - 170 * s, 460 * s, 150 * s); fill(c, r, col); ink(c, r, 5)
    for k in range(6):
        w_ = skia.Rect.MakeXYWH(x + 20 * s + k * 72 * s, y - 150 * s, 56 * s, 50 * s); fill(c, w_, 0xFF2E3A48); ink(c, w_, 3)
    for wx in (x + 80 * s, x + 380 * s):
        c.drawCircle(wx, y - 18 * s, 30 * s, _p(0xFF222222)); c.drawCircle(wx, y - 18 * s, 12 * s, _p(0xFFAAAAAA))
    if label:
        E.draw_text(c, label, x + 230 * s, y - 60 * s, E.font(E.FONT_BOLD, int(30 * s)), color=INK)


def _truck(c, x, y, s=1.0, label="BREAD"):
    cab = skia.Rect.MakeXYWH(x + 330 * s, y - 150 * s, 140 * s, 130 * s); fill(c, cab, 0xFFD9443A); ink(c, cab, 5)
    win = skia.Rect.MakeXYWH(x + 380 * s, y - 135 * s, 70 * s, 50 * s); fill(c, win, 0xFF9CC3D5); ink(c, win, 3)
    bx = skia.Rect.MakeXYWH(x, y - 210 * s, 330 * s, 190 * s); fill(c, bx, 0xFFF5EED8); ink(c, bx, 5)
    E.draw_text(c, label, x + 165 * s, y - 100 * s, E.font(E.FONT_BLACK, int(54 * s)), color=0xFFB0542A)
    for wx in (x + 70 * s, x + 400 * s):
        c.drawCircle(wx, y - 18 * s, 32 * s, _p(0xFF222222)); c.drawCircle(wx, y - 18 * s, 12 * s, _p(0xFFAAAAAA))


def _generator(c, x, y):
    box(c, x, y - 140, 220, 140, 0xFFD4A62A, 6, 10)
    E.draw_text(c, "GEN", x + 110, y - 58, E.font(E.FONT_BOLD, 40), color=INK)


def _smoke(c, t, x, y):
    for k in range(7):
        ph = (t * 0.3 + k / 7) % 1
        c.drawCircle(x + math.sin(k * 2 + t) * 40, y - ph * 300, 40 + ph * 70, _p(0x44606060))


def _fire(c, t, x, y):
    for k in range(5):
        h = 70 + 30 * math.sin(t * 9 + k)
        p = poly([(x + k * 26 - 20, y), (x + k * 26, y - h), (x + k * 26 + 20, y)], close=True)
        fill(c, p, 0xFFF28C28 if k % 2 else 0xFFFFC34A)
    _glow(c, x + 50, y - 40, 200, 0x55FFA040)


# ------------------------------------------------------------------ platserna

def bg_visitor_lobby(c, t, v):
    _wall(c, v, band=False)
    _lights(c, v)
    # glasfront med två par glasdörrar
    gx, gy, gw, gh = W * 0.04, H * 0.16, W * 0.6, GROUND - H * 0.16
    _grad(c, (gx, gy, gw, gh), [0xFF7F98B0, 0xFFB7C8D6] if not _n(v) else [0xFF26324A, 0xFF3E5068])
    if v.get("window_dead"):
        _dead(c, t, 6, GROUND - 6, 330, 0.06, 0.6, look=1, seed=4)
        for i in range(6):
            c.drawCircle(W * (0.08 + 0.09 * i), H * 0.42 + (i % 2) * 30, 16, _p(0x44FFFFFF))
    for k in range(1, 4):
        line(c, gx + k * gw / 4, gy, gx + k * gw / 4, GROUND, 10, 0xFF8E979E)
    ink(c, skia.Rect.MakeXYWH(gx, gy, gw, gh), 12, 0xFF8E979E)
    for k in range(4):   # dörrhandtag (dörrarna öppnas inåt)
        line(c, gx + (k + 0.5) * gw / 4 + (18 if k % 2 else -18), H * 0.44, gx + (k + 0.5) * gw / 4 + (18 if k % 2 else -18), H * 0.56, 8, 0xFFC0C6CC)
    if v.get("glass"):
        cx, cy = W * 0.3, H * 0.4
        for k in range(9):
            a = k * 0.7
            c.drawLine(cx, cy, cx + math.cos(a) * 160, cy + math.sin(a) * 160, _p(0xCCFFFFFF, 3))
    E.draw_text(c, "VISITOR ENTRANCE", gx + gw / 2, gy - 22, E.font(E.FONT_BOLD, 40), color=INK)
    # disk och bord
    desk = skia.Rect.MakeXYWH(W * 0.7, H * 0.5, W * 0.26, GROUND - H * 0.5); fill(c, desk, 0xFF7C8FA6); ink(c, desk, 6)
    top = skia.Rect.MakeXYWH(W * 0.69, H * 0.48, W * 0.28, 26); fill(c, top, 0xFFEFEFEF); ink(c, top, 4)
    for k in range(int(v.get("tables", 2) or 0) if isinstance(v.get("tables"), (int, float)) else 2):
        x = W * 0.12 + k * 300
        box(c, x, GROUND + 40, 200, 22, 0xFFB8C0C6, 4, 3)
    if _n(v):
        _exit(c, W * 0.78, H * 0.12)
    _floor(c, v)


def bg_prison_yard(c, t, v):
    _sky(c, v)
    # bortre mur + vakttorn
    fill(c, skia.Rect.MakeXYWH(0, H * 0.34, W, GROUND - H * 0.34), 0xFFCFC8B8 if not _n(v) else 0xFF5E6878)
    for x in range(0, int(W), 240):
        line(c, x, H * 0.34, x, GROUND, 3, 0x22000000)
    line(c, 0, H * 0.34, W, H * 0.34, 6)
    tw = skia.Rect.MakeXYWH(W * 0.82, H * 0.08, 150, H * 0.26); fill(c, tw, 0xFFB7AE9C); ink(c, tw, 5)
    cab = skia.Rect.MakeXYWH(W * 0.82 - 30, H * 0.02, 210, 80); fill(c, cab, 0xFF8E979E); ink(c, cab, 5)
    win = skia.Rect.MakeXYWH(W * 0.82 - 10, H * 0.035, 170, 45); fill(c, win, 0xFF9CC3D5 if not _n(v) else 0xFFFFE6A8); ink(c, win, 3)
    for k in range(int(W / 60) + 1):   # taggtråd
        c.drawCircle(k * 60 + 30, H * 0.32, 24, _p(0xFF6A737C, 3))
    if v.get("sign"):
        pass   # regeln visas som skylt-overlay
    # gårdsplan
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFFB9B4A6 if not _n(v) else 0xFF6F7A86)
    line(c, 0, GROUND, W, GROUND, 5)
    for k in range(4):
        line(c, W * 0.1 + k * 420, GROUND + 60, W * 0.1 + k * 420 + 200, GROUND + 60, 6, 0xFFF2F2F2)
    if v.get("fence"):   # inre staket med grind (öppnas utåt mot de döda)
        fy = H * 0.42
        for x in range(0, int(W * 0.52), 90):
            line(c, x, fy, x, GROUND, 6, 0xFF6A737C)
        for y in range(int(fy), int(GROUND), 40):
            line(c, 0, y, W * 0.52, y + 40, 2, 0x886A737C); line(c, 0, y + 40, W * 0.52, y, 2, 0x886A737C)
        line(c, 0, fy, W * 0.52, fy, 8, 0xFF6A737C)
        _bars(c, W * 0.52, fy, 220, GROUND - fy, gap=44, lw=8)
        _arrow(c, W * 0.52 + 110, H * 0.55, "out", 140)
    if v.get("generator"):
        _generator(c, W * 0.62, GROUND + 10)
    if v.get("buses"):
        for k in range(min(3, int(v["buses"]))):
            _bus(c, W * 0.55 + k * 60, GROUND - 4 - k * 6, 0.8, label="CORRECTIONS" if k == 0 else None)
    if v.get("bread_truck") or v.get("truck_moving"):
        _truck(c, W * 0.58 + (t * 40 if v.get("truck_moving") else 0), GROUND + 10, 0.9)
    if v.get("carts"):
        for k in range(int(v["carts"]) if isinstance(v["carts"], (int, float)) else 3):
            box(c, W * 0.3 + k * 130, GROUND - 80, 110, 70, 0xFFB8C0C6, 4, 6)
    if v.get("exit_signs"):
        _exit(c, W * 0.05, H * 0.38); _exit(c, W * 0.4, H * 0.38)
    _rain(c, t, v)


def bg_prison_map(c, t, v):
    fill(c, skia.Rect.MakeWH(W, H), 0xFFEAF0F6)
    for k in range(0, int(W), 60):
        c.drawLine(k, 0, k, H, _p(0x221F4FA0, 1))
    for k in range(0, int(H), 60):
        c.drawLine(0, k, W, k, _p(0x221F4FA0, 1))
    marks = [str(m) for m in (v.get("marks") or [])]
    n = max(1, len(marks))
    cols = 3
    pos = []
    for i, m in enumerate(marks):
        r_, c_ = divmod(i, cols)
        x = W * (0.08 + 0.3 * c_); y = H * (0.14 + 0.38 * r_)
        rr = skia.Rect.MakeXYWH(x, y, W * 0.25, H * 0.28)
        fill(c, rr, 0xFFFFFFFF); ink(c, rr, 6, 0xFF1F4FA0)
        f = E.font(E.FONT_BOLD, 44)
        E.draw_text(c, m.upper(), x + W * 0.125, y + H * 0.16, f, color=0xFF1F4FA0)
        pos.append((x + W * 0.125, y + H * 0.24))
    if v.get("route") and len(pos) > 1:
        for (a, b) in zip(pos, pos[1:]):
            c.drawLine(a[0], a[1], b[0], b[1], _p(0xFFD8342A, 9))
        c.drawCircle(pos[-1][0], pos[-1][1], 22, _p(0xFFD8342A))
    E.draw_text(c, "FACILITY PLAN", W / 2, H * 0.08, E.font(E.FONT_BLACK, 52), color=0xFF1F4FA0)


def bg_sally_port(c, t, v):
    _wall(c, v)
    _lights(c, v, 4)
    n = int(v.get("gates", 2) or 2)
    n = max(2, min(6, n))
    for k in range(n):   # gallergrindar i rad – längre bort = mindre
        sc = 1 - k * 0.12
        w_, h_ = 520 * sc, (GROUND - H * 0.16) * sc
        x = W * 0.5 - w_ / 2 + (k - (n - 1) / 2) * 40
        y = GROUND - h_
        _bars(c, x, y, w_, h_, gap=40 * sc, lw=max(4, 8 * sc), col=0xFF3F4852 if k == 0 else 0xFF6A737C)
    yel = skia.Rect.MakeXYWH(0, GROUND + 50, W, 18); fill(c, yel, 0xFFF2C230)
    E.draw_text(c, "SALLY PORT", W * 0.5, H * 0.12, E.font(E.FONT_BOLD, 44), color=INK)
    _floor(c, v)
    fill(c, skia.Rect.MakeXYWH(0, GROUND + 50, W, 14), 0xFFF2C230)


def bg_control_room(c, t, v):
    _wall(c, v, day=0xFFDDE3E8, night=0xFF46566A, band=False)
    n = int(v.get("cctv", 12) or 12)
    cols = 4 if n <= 12 else 6
    rows = math.ceil(n / cols)
    for i in range(n):
        r_, c_ = divmod(i, cols)
        x = W * 0.05 + c_ * 150; y = H * 0.1 + r_ * 110
        scr = skia.Rect.MakeXYWH(x, y, 136, 96); fill(c, scr, 0xFF1C2A36); ink(c, scr, 4)
        rnd = random.Random(i)
        fill(c, skia.Rect.MakeXYWH(x + 8, y + 60, 120, 28), 0xFF3E5A50)
        for k in range(rnd.randint(0, 3)):   # små siluetter i bilden
            px = x + 20 + rnd.uniform(0, 90)
            c.drawCircle(px, y + 50, 7, _p(0xFF0E141A)); c.drawRect(skia.Rect.MakeXYWH(px - 5, y + 56, 10, 26), _p(0xFF0E141A))
        c.drawCircle(x + 122, y + 12, 5, _p(0xFFE53935))
    _board(c, v, x=W * 0.6, y=H * 0.1)
    desk = skia.Rect.MakeXYWH(W * 0.02, H * 0.6, W * 0.96, GROUND - H * 0.6); fill(c, desk, 0xFF5B6C80); ink(c, desk, 6)
    top = skia.Rect.MakeXYWH(0, H * 0.58, W, 26); fill(c, top, 0xFFCFD6DC); ink(c, top, 4)
    for k in range(5):   # knappanel
        c.drawCircle(W * 0.1 + k * 60, H * 0.64, 14, _p([0xFF2E9E4F, 0xFFE53935, 0xFFF2C230, 0xFF2E9E4F, 0xFF4E8FCB][k]))
    _floor(c, v, day=0xFF9AA3AA)


def bg_cellblock(c, t, v):
    _wall(c, v, day=0xFFE4DECF, night=0xFF4E5C6E, band=False)
    _lights(c, v)
    tiers = int(v.get("tiers", 2) or 2)
    th = (GROUND - H * 0.1) / tiers
    faces = int(v.get("cell_faces", 0) or 0) if not isinstance(v.get("cell_faces"), bool) else (6 if v.get("cell_faces") else 0)
    k = 0
    for tr in range(tiers):
        y0 = H * 0.1 + tr * th
        if tr < tiers - 1:   # gångbrygga med räcke
            fill(c, skia.Rect.MakeXYWH(0, y0 + th - 24, W, 24), 0xFF8E979E); line(c, 0, y0 + th - 24, W, y0 + th - 24, 4)
            line(c, 0, y0 + th - 80, W, y0 + th - 80, 5, 0xFF6A737C)
            for x in range(0, int(W), 60):
                line(c, x, y0 + th - 80, x, y0 + th - 24, 3, 0xFF6A737C)
        for i in range(7):
            x = 40 + i * 270
            cell = skia.Rect.MakeXYWH(x, y0 + 20, 220, th - 60)
            fill(c, cell, 0xFF3A4450 if (v.get("lights") == "off" or _n(v)) else 0xFF8E8778)
            if k < faces:
                hx = x + 110; hy = y0 + th * 0.45
                E.stickman(c, hx, y0 + th - 40, th * 0.9, vest=None, hat=None, outfit=0xFFE07B39, face=1 if i % 2 else -1,
                           arms="up" if (v.get("cell_shout") and k % 2 == 0) else "down",
                           expr="scared" if v.get("cell_shout") else None)
            k += 1
            _bars(c, x, y0 + 20, 220, th - 60, gap=30, lw=6)
            plate = skia.Rect.MakeXYWH(x + 70, y0 + 2, 80, 26); fill(c, plate, 0xFFFFFFFF); ink(c, plate, 3)
            E.draw_text(c, f"B{tr + 1}{i + 1:02d}", x + 110, y0 + 24, E.font(E.FONT_BOLD, 22), color=INK)
            if v.get("food_slot"):
                fill(c, skia.Rect.MakeXYWH(x + 80, y0 + th * 0.55, 60, 18), 0xFFF2C230)
    _board(c, v, x=W * 0.62, y=H * 0.05, w=W * 0.34, h=H * 0.26)
    _floor(c, v)


def bg_staff_exit(c, t, v):
    _wall(c, v)
    _lights(c, v, 3)
    d = skia.Rect.MakeXYWH(W * 0.36, H * 0.2, 340, GROUND - H * 0.2); fill(c, d, 0xFF7C8FA6); ink(c, d, 7)
    line(c, W * 0.36 + 40, H * 0.5, W * 0.36 + 300, H * 0.5, 12, 0xFFC0C6CC)   # panikregel
    plate = skia.Rect.MakeXYWH(W * 0.36 + 40, H * 0.25, 260, 60); fill(c, plate, 0xFFFFFFFF); ink(c, plate, 3)
    E.draw_text(c, "STAFF ONLY", W * 0.36 + 170, H * 0.25 + 44, E.font(E.FONT_BOLD, 36), color=0xFFD8342A)
    _exit(c, W * 0.36 + 110, H * 0.1)
    if v.get("door_arrow"):
        _arrow(c, W * 0.36 + 170, H * 0.66, v.get("door_arrow") if isinstance(v.get("door_arrow"), str) else "out", 160)
    _floor(c, v)


def bg_fence(c, t, v):
    _sky(c, v)
    fill(c, skia.Rect.MakeXYWH(0, H * 0.5, W, GROUND - H * 0.5), 0xFF8DB36B if not _n(v) else 0xFF3F5A3A)
    fy = H * 0.24
    for x in range(0, int(W), 80):
        line(c, x, fy, x, GROUND, 6, 0xFF6A737C)
    for y in range(int(fy), int(GROUND), 46):
        line(c, 0, y, W, y + 46, 2, 0x886A737C); line(c, 0, y + 46, W, y, 2, 0x886A737C)
    for k in range(int(W / 60) + 1):
        c.drawCircle(k * 60 + 30, fy - 20, 24, _p(0xFF6A737C, 3))
    _bars(c, W * 0.4, fy, 380, GROUND - fy, gap=46, lw=9)
    if v.get("gate") == "closed" or v.get("gate"):
        lock = skia.Rect.MakeXYWH(W * 0.4 + 170, H * 0.5, 40, 50); fill(c, lock, 0xFFE8C23A); ink(c, lock, 4)
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFFB9B4A6 if not _n(v) else 0xFF6F7A86)
    line(c, 0, GROUND, W, GROUND, 5)
    _rain(c, t, v)


def _kitchen_base(c, v):
    _wall(c, v, day=0xFFF1EEE6, night=0xFF5A6878, band=False)
    for x in range(0, int(W), 60):   # kakel
        line(c, x, H * 0.36, x, H * 0.6, 2, 0x18000000)
    for y in range(int(H * 0.36), int(H * 0.6), 60):
        line(c, 0, y, W, y, 2, 0x18000000)
    _lights(c, v)


def bg_kitchen(c, t, v):
    _kitchen_base(c, v)
    # storköksbänk i rostfritt
    bench = skia.Rect.MakeXYWH(W * 0.02, H * 0.6, W * 0.62, GROUND - H * 0.6)
    c.drawRect(bench, skia.Paint(Shader=skia.GradientShader.MakeLinear([(0, H * 0.6), (0, GROUND)], [0xFFD5DBE0, 0xFFA9B2BA]))); ink(c, bench, 6)
    top = skia.Rect.MakeXYWH(0, H * 0.58, W * 0.66, 24); fill(c, top, 0xFFE8EDF0); ink(c, top, 4)
    # spisar + kokkärl
    for k in range(3):
        x = W * 0.06 + k * 300
        pot = skia.Rect.MakeXYWH(x, H * 0.46, 180, 110); fill(c, pot, 0xFFB8C0C6); ink(c, pot, 5)
        line(c, x - 20, H * 0.48, x + 200, H * 0.48, 6, 0xFF8E979E)
    if v.get("kettle"):
        c.drawCircle(W * 0.5, H * 0.52, 50, _p(0xFF8E979E)); ink(c, skia.Path().addCircle(W * 0.5, H * 0.52, 50), 5)
    if v.get("steam") or v.get("kettle"):
        for k in range(6):
            c.drawCircle(W * 0.1 + k * 110, H * 0.38 - (k % 3) * 30, 36 + (k % 2) * 14, _p(0x55FFFFFF))
    if v.get("sink"):
        sk = skia.Rect.MakeXYWH(W * 0.48, H * 0.6, 200, 60); fill(c, sk, 0xFF9AA3AA); ink(c, sk, 4)
    if v.get("pantry"):   # torrförrådshylla
        px = W * 0.68
        shelf = skia.Rect.MakeXYWH(px, H * 0.12, W * 0.3, GROUND - H * 0.12); fill(c, shelf, 0xFFB7A68A); ink(c, shelf, 6)
        colsb = [0xFFF5EED8, 0xFFD9443A, 0xFFF2B33D, 0xFF6BAA5A]
        for r in range(4):
            y = H * 0.12 + 30 + r * 150
            line(c, px, y + 110, px + W * 0.3, y + 110, 6)
            for k in range(6):
                box(c, px + 20 + k * 92, y + 30, 70, 80, colsb[(k + r) % 4], 4, 6)
    if v.get("flour_sacks"):
        for k in range(4):
            sx = W * 0.3 + (k % 2) * 120; sy = GROUND - 10 - (k // 2) * 90
            r_ = skia.Rect.MakeXYWH(sx, sy - 100, 110, 100); fill(c, r_, 0xFFF3ECDD); ink(c, r_, 4)
            E.draw_text(c, "FLOUR", sx + 55, sy - 40, E.font(E.FONT_BOLD, 24), color=0xFF8B5A2B)
    _board(c, v, x=W * 0.66 if not v.get("pantry") else W * 0.3, y=H * 0.06, w=W * 0.32, h=H * 0.26)
    _floor(c, v, day=0xFFC9B9A0)


def bg_kitchen_dock(c, t, v):
    _kitchen_base(c, v)
    # lastport (böjs inåt)
    dx, dw = W * 0.2, W * 0.5
    door = skia.Rect.MakeXYWH(dx, H * 0.16, dw, GROUND - H * 0.16)
    fill(c, door, 0xFF9AA8B6); ink(c, door, 7)
    bend = 1.0 if v.get("door") in ("bending", True) else 0.0
    for k in range(9):
        y = H * 0.16 + k * (GROUND - H * 0.16) / 9
        p = skia.Path(); p.moveTo(dx, y)
        p.quadTo(dx + dw / 2, y + bend * 40 * math.sin(k / 8 * math.pi), dx + dw, y)
        ink(c, p, 4, 0xFF6A737C)
    if bend:
        for k in range(3):
            c.drawCircle(dx + dw * (0.3 + 0.2 * k), H * 0.5 + k * 20, 30, _p(0x33000000))
    if v.get("bread_truck"):
        _truck(c, W * 0.72, GROUND + 6, 0.7)
    if v.get("buses"):
        _bus(c, W * 0.72, GROUND - 4, 0.6)
    E.draw_text(c, "DOCK 2", dx + dw / 2, H * 0.12, E.font(E.FONT_BOLD, 40), color=INK)
    _floor(c, v, day=0xFFC9B9A0)


def bg_laundry(c, t, v):
    _wall(c, v, day=0xFFE6E8EA, night=0xFF4E5C6E, band=False)
    _lights(c, v)
    for k in range(4):   # industritvättmaskiner
        x = W * 0.04 + k * 230
        m = skia.Rect.MakeXYWH(x, H * 0.4, 200, GROUND - H * 0.4); fill(c, m, 0xFFDDE2E6); ink(c, m, 5)
        c.drawCircle(x + 100, H * 0.56, 64, _p(0xFF6E8CA6)); ink(c, skia.Path().addCircle(x + 100, H * 0.56, 64), 6)
    gx = W * 0.62
    gd = skia.Rect.MakeXYWH(gx, H * 0.18, W * 0.34, GROUND - H * 0.18)
    up = v.get("garage_door") == "up"
    if up:
        _grad(c, (gx, H * 0.18, W * 0.34, GROUND - H * 0.18), [0xFF8CC4EA, 0xFFCFC8B8])
        fill(c, skia.Rect.MakeXYWH(gx, H * 0.18, W * 0.34, 60), 0xFF9AA8B6)
    else:
        fill(c, gd, 0xFF9AA8B6)
        for k in range(8):
            line(c, gx, H * 0.18 + k * 70, gx + W * 0.34, H * 0.18 + k * 70, 4, 0xFF6A737C)
    ink(c, gd, 7)
    if v.get("generator"):
        _generator(c, W * 0.42, GROUND + 6)
    if v.get("smoke"):
        _smoke(c, t, W * 0.5, H * 0.4)
    if v.get("fire_small"):
        _fire(c, t, W * 0.46, GROUND + 4)
    _floor(c, v)


def bg_roof(c, t, v):
    _sky(c, v)
    # stadens/landskapets kontur
    for k in range(9):
        x = k * 230; h = 80 + (k * 53) % 120
        fill(c, skia.Rect.MakeXYWH(x, H * 0.5 - h, 200, h), 0xFF9AA8B6 if not _n(v) else 0xFF2E3A4E)
    fill(c, skia.Rect.MakeXYWH(0, H * 0.5, W, GROUND - H * 0.5), 0xFF8DB36B if not _n(v) else 0xFF3F5A3A)
    roof = skia.Rect.MakeXYWH(0, GROUND - 40, W, H - GROUND + 40); fill(c, roof, 0xFF9C958A if not _n(v) else 0xFF5E6878)
    if v.get("gravel"):
        rnd = random.Random(8)
        for k in range(400):
            c.drawCircle(rnd.uniform(0, W), rnd.uniform(GROUND - 30, H), rnd.uniform(2, 4), _p(0x55000000))
    line(c, 0, GROUND - 40, W, GROUND - 40, 6)
    for x in range(0, int(W), 120):   # takkant
        line(c, x, GROUND - 90, x, GROUND - 40, 4, 0xFF6A737C)
    line(c, 0, GROUND - 90, W, GROUND - 90, 5, 0xFF6A737C)
    if v.get("hatch"):
        hr = skia.Rect.MakeXYWH(W * 0.62, GROUND + 20, 200, 60); fill(c, hr, 0xFF7C8FA6); ink(c, hr, 5)
    if v.get("can_32"):
        for k in range(8):
            for j in range(4):
                box(c, W * 0.12 + k * 34, GROUND + 60 - j * 46, 30, 42, 0xFFD9443A, 3, 3)
    _rain(c, t, v)


def bg_hallway(c, t, v):
    _wall(c, v)
    _lights(c, v)
    for k in range(5):   # celldörrar längs korridoren
        x = 60 + k * 380
        if v.get("new_door") and k == 2:
            continue
        d = skia.Rect.MakeXYWH(x, H * 0.26, 200, GROUND - H * 0.26); fill(c, d, 0xFF8FA6B8 if not _n(v) else 0xFF5A6E82); ink(c, d, 5)
        win = skia.Rect.MakeXYWH(x + 70, H * 0.32, 60, 90); fill(c, win, 0xFF2E3A48); ink(c, win, 3)
    if v.get("new_door"):
        x = 60 + 2 * 380 - 40
        d = skia.Rect.MakeXYWH(x, H * 0.2, 280, GROUND - H * 0.2); fill(c, d, 0xFFF2C230); ink(c, d, 7)
        txt = v.get("door_text") or "ONE DOOR AT A TIME"
        f = E.font(E.FONT_BLACK, 34)
        for j, ln in enumerate(E.wrap(str(txt), f, 250)[:3]):
            E.draw_text(c, ln, x + 140, H * 0.3 + j * 44, f, color=INK)
        if v.get("door_arrow"):
            _arrow(c, x + 140, H * 0.58, v["door_arrow"] if isinstance(v["door_arrow"], str) else "out", 150)
    if v.get("crowd") == "people":
        _people(c, t, 6, s=250, seed=11)
    if v.get("marks"):
        for k in range(int(v["marks"]) if isinstance(v["marks"], (int, float)) else 5):
            line(c, W * 0.8 + k * 18, H * 0.5, W * 0.8 + k * 18, H * 0.6, 5, 0xFFD8342A)
    _board(c, v, x=W * 0.64, y=H * 0.06, w=W * 0.32, h=H * 0.2)
    _floor(c, v)


def bg_parking_lot(c, t, v):
    _sky(c, v)
    fill(c, skia.Rect.MakeXYWH(0, H * 0.36, W, GROUND - H * 0.36), 0xFFCFC8B8)
    line(c, 0, H * 0.36, W, H * 0.36, 6)
    for k in range(int(W / 60) + 1):
        c.drawCircle(k * 60 + 30, H * 0.34, 22, _p(0xFF6A737C, 3))
    fill(c, skia.Rect.MakeXYWH(0, GROUND, W, H - GROUND), 0xFF8E9199)
    line(c, 0, GROUND, W, GROUND, 5)
    for k in range(7):
        line(c, 80 + k * 280, GROUND + 20, 40 + k * 280, H, 6, 0xFFF2F2F2)
    cols = [0xFF4E8FCB, 0xFFD9443A, 0xFFE8E8E8, 0xFF6BAA5A]
    for k in range(4):   # bilar mot muren
        x = 60 + k * 470
        body = skia.Rect.MakeXYWH(x, GROUND - 120, 300, 90); fill(c, body, cols[k]); ink(c, body, 5)
        top = skia.Rect.MakeXYWH(x + 60, GROUND - 170, 170, 60); fill(c, top, cols[k]); ink(c, top, 5)
        fill(c, skia.Rect.MakeXYWH(x + 75, GROUND - 160, 140, 42), 0xFF9CC3D5)
        for wx in (x + 60, x + 240):
            c.drawCircle(wx, GROUND - 28, 28, _p(0xFF222222))
    if v.get("buses"):
        _bus(c, W * 0.6, GROUND - 4, 0.8)
    if v.get("crowd") == "people":
        _people(c, t, 7, y=H * 0.86, s=230, seed=21)


PLACES = {"visitor_lobby": bg_visitor_lobby, "prison_yard": bg_prison_yard, "prison_map": bg_prison_map,
          "sally_port": bg_sally_port, "control_room": bg_control_room, "cellblock": bg_cellblock,
          "staff_exit": bg_staff_exit, "fence": bg_fence, "kitchen": bg_kitchen, "kitchen_dock": bg_kitchen_dock,
          "laundry": bg_laundry, "roof": bg_roof, "hallway": bg_hallway, "parking_lot": bg_parking_lot}
OUTDOOR = {"prison_yard", "fence", "roof", "parking_lot", "prison_map"}

# ------------------------------------------------------------------ föremål i handen

def _i_clipboard(c, hx, hy, s, lw):
    box(c, hx - s * 0.02, hy - s * 0.12, s * 0.13, s * 0.17, 0xFFC49A5C, lw * 0.4, 3)
    fill(c, skia.Rect.MakeXYWH(hx, hy - s * 0.1, s * 0.09, s * 0.12), 0xFFFFFFFF)


def _i_marker(c, hx, hy, s, lw):
    line(c, hx, hy, hx + s * 0.1, hy - s * 0.1, lw * 0.9, 0xFF1F4FA0)


def _i_tray(c, hx, hy, s, lw):
    box(c, hx - s * 0.08, hy - s * 0.02, s * 0.26, s * 0.04, 0xFFB8C0C6, lw * 0.4, 3)


def _i_cart(c, hx, hy, s, lw):
    box(c, hx, hy - s * 0.02, s * 0.3, s * 0.18, 0xFFB8C0C6, lw * 0.5, 4)
    c.drawCircle(hx + s * 0.05, hy + s * 0.2, s * 0.03, _p(INK)); c.drawCircle(hx + s * 0.25, hy + s * 0.2, s * 0.03, _p(INK))


def _i_ladle(c, hx, hy, s, lw):
    line(c, hx, hy, hx + s * 0.04, hy - s * 0.22, lw * 0.6, 0xFF8E979E)
    c.drawCircle(hx + s * 0.04, hy + s * 0.02, s * 0.04, _p(0xFF8E979E))


def _i_mop(c, hx, hy, s, lw):
    line(c, hx, hy - s * 0.2, hx + s * 0.08, hy + s * 0.5, lw * 0.6, 0xFF8B5A2B)
    fill(c, skia.Rect.MakeXYWH(hx + s * 0.02, hy + s * 0.46, s * 0.14, s * 0.06), 0xFFE8E2D4)


def _i_wrench(c, hx, hy, s, lw):
    line(c, hx, hy + s * 0.04, hx + s * 0.16, hy - s * 0.14, lw * 0.9, 0xFF8E979E)
    c.drawCircle(hx + s * 0.17, hy - s * 0.15, s * 0.035, _p(0xFF8E979E, lw * 0.5))


def _i_extinguisher(c, hx, hy, s, lw):
    box(c, hx - s * 0.02, hy - s * 0.14, s * 0.08, s * 0.22, 0xFFD8342A, lw * 0.4, 6)
    line(c, hx + s * 0.02, hy - s * 0.14, hx + s * 0.1, hy - s * 0.2, lw * 0.5)


def _i_brush(c, hx, hy, s, lw):
    line(c, hx, hy, hx + s * 0.12, hy - s * 0.12, lw * 0.6, 0xFF8B5A2B)
    fill(c, skia.Rect.MakeXYWH(hx + s * 0.1, hy - s * 0.18, s * 0.08, s * 0.05), 0xFFF2C230)


ITEMS = {"clipboard": _i_clipboard, "marker": _i_marker, "tray": _i_tray, "cart": _i_cart, "ladle": _i_ladle,
         "mop": _i_mop, "wrench": _i_wrench, "extinguisher": _i_extinguisher, "brush": _i_brush}


def _map_scene(c, t, d, v):
    v2 = dict(v); v2["type"] = "scene"; v2.setdefault("location", "prison_map"); v2["hero"] = None; v2["shot"] = "wide"
    E.SM["scene"](c, t, d, v2)


HERO = {"outfit": 4280232516, "hat": 4279509309, "vest": None, "x": 0.35}


def _dead_prop(c, t, px, prop):
    """De döda som mörka silhuetter med lysande ögon (ägarens order) – ritas efter bakgrunden, före figurerna."""
    try:
        import charstyle
        k = charstyle.SCALE
    except Exception:
        k = 1.0
    for i, z in enumerate(prop.get("z", [])):
        sp = z.get("speed", 20)
        x = W * z.get("x", 0.8) - sp * t
        if z.get("lunge"):
            x -= max(0.0, math.sin(t * 3.0 + i)) * 26
        s = z.get("size", 330) * k
        _silhouette(c, x, H * 0.82, s, t, 60 + i, look=-1, arms="up" if z.get("lunge") else "forward")


def _wrap(orig):
    def scene(c, t, d, v):
        if v.get("location") not in PLACES:
            return orig(c, t, d, v)
        v2 = dict(v); s = v2.pop("sign", None)
        if isinstance(v2.get("day"), bool):   # manuset: day=true betyder dagsljus, inte dagnummer
            v2.pop("day")
        if "hero" not in v2 and v2.get("location") != "prison_map":
            v2["hero"] = dict(HERO)
        zs = v2.pop("zombies_in", None)
        if zs:
            v2["props"] = list(v2.get("props", [])) + [{"type": "prison_dead", "z": zs}]
        orig(c, t, d, v2)
        if s:
            try:
                import ls21
                ls21._sign_overlay(c, t, d, v)
            except Exception:
                _sign(c, W / 2, 44, s, size=46, maxw=W * 0.72)
    scene._prison = True
    return scene


def enable():
    E.BG.update(PLACES)
    for k, f in ITEMS.items():
        E.EXTRA_ITEMS.setdefault(k, f)
    E.SM["map"] = _map_scene
    E.EXTRA_PROPS["prison_dead"] = _dead_prop
    try:
        import atmos
        for k in PLACES:
            if k in OUTDOOR:
                atmos.MOOD[k] = dict(light=(0.6, 0.15), lc=0xFFFFF4D6, dark=0.22, mood=None, fg=None)
                atmos.OUTDOOR.add(k)
            else:
                atmos.MOOD[k] = dict(light=(0.5, 0.1), lc=0xFFF2F6FF, dark=0.28, mood="cold", fg="frame")
        atmos.MOOD["prison_map"] = dict(light=(0.5, 0.2), lc=0xFFFFFFFF, dark=0.05, mood=None, fg=None)
        old = atmos._bg_key

        def _bg_key(v):
            return old(v) + json.dumps({k: v.get(k) for k in (
                "window_dead", "glass", "tables", "fence", "generator", "rain", "carts", "exit_signs", "bread_truck", "buses",
                "marks", "route", "gates", "cctv", "board", "tiers", "cell_faces", "cell_shout", "food_slot", "lights",
                "door_arrow", "gate", "pantry", "flour_sacks", "kettle", "steam", "sink", "garage_door", "smoke",
                "fire_small", "gravel", "hatch", "can_32", "new_door", "door_text", "crowd")}, default=str)
        atmos._bg_key = _bg_key
    except Exception as e:
        print("prison atmos:", e)


def enable_late():
    """Körs efter atmos/ls21 – lägger skylt-overlayn runt den färdiga scenen."""
    if not getattr(E.SM["scene"], "_prison", False):
        E.SM["scene"] = _wrap(E.SM["scene"])
