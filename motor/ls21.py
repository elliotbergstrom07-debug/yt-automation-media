"""Last Shift – 7 nattjobb (manus ls-2026-11-21, 'How Long Would You Survive in a Zombie Apocalypse? (7 Jobs)').
Byggd 22 nov (rendering B). Filmisk papperslook som pier.py: gradienthimmel, lager, ljuspunkter, de döda som
mörka silhuetter med lysande ögon (mine._silhouette via pier.pier_stick).

Platser (E.BG statiskt + rörligt lager via pier_live):
  dispatch       larmcentral: 12 bord, linjetavla med 40 lampor (phones_lit N blinkar), glasvägg mot parkeringen
                 till höger – de döda ritas BAKOM glaset (glass_flex, glass_crack), breaker (mörkt + nödljus), radio.
  dispatch_roof  taket: lucka med stege, fläktar, antenn, stadens siluett.
  garage         parkeringshus: pelare, bilar, ramp, bås + bom (booth), alarm_lights N (varningsljus), key_cabinet.
  street         nattgata med butiker och gatlyktor.
  truckstop      rader med lastbilar under natriumljus, DIESEL-tak; reefer_on, logbook (insert), sfx_vis 'hiss'.
  cab            sovhytt inifrån: brits, gardin, fönster; door_hits (händer mot rutan), cb_radio.
  highway        motorväg i gryning: truck_moving, car (kombi), hjälten i hytten (hero.on 'cab').
  diner          dygnet-runt-diner: bås, disk, jukebox, fönster mot parkeringen (window_dead), dörr med klocka
                 (door_open), timers N, jukebox-insert.
  diner_lot      dinern utifrån med neonskylt; throw_items N (äggklockor i luften).
  diner_back     bakgården: fettfat, kombi; radio.
  zoo            lejonklippan med vallgrav (moat), lion_roar / lion_lying.
  zoo_path       skötarstigen mellan bodar, grind 4, wheelbarrow, radio.
  zoo_stage      sjölejonscenen: läktare, bassäng, högtalare (speakers), sound_waves.
  drawbridge     klaffbro: manöverhus (hero.on 'control_house'), leaves down|rising|up, control_panel (insert),
                 truck_far, edge (crowd).
  river          fiskebåt på floden (boat), öppen bro i bakgrunden, sound_waves.
  riverbank      strandbanken.
  lookout        brandtorn av stål över skogen (hero.on 'cab'), stairs, storm/lightning, tower_legs.
  lookout_cab    glashytten inifrån: firefinder, stool (pall med glasfötter, hero.on 'stool'), ridge_tower, radio.
  forest         skog i lager, wind, storm.
  ridge_tower    Walts hytt: tally (streck på väggen, antal ur sign 'TALLY: N').
Kort: daycard med card 'problem' (rangnummer + jobb) och 'end'.
Skyltar (sign) ritas i skärmkoordinater ovanpå scenen (syns även i medium/close): 'VERDICT: …' = rött band.
Laddas av run_ls.py EFTER pier (pier.enable() först) – kopplar in sig i pier.PLACES / pier_live.
"""
import math, random, json, os, re
import skia
import engine as E
from engine import W, H, INK, poly
from mine import _p, _grad, _glow, _dust, _sign, _silhouette
import pier
from pier import _sky, _mode, _a, _blur

GY = H * 0.82
STASH = {"z": [], "v": {}, "d": 6.0}
GLASS_LOCS = ("dispatch", "diner", "cab")
_BANGERS = None


def _bangers(sz):
    global _BANGERS
    if _BANGERS is None:
        f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts", "Bangers-Regular.ttf")
        _BANGERS = skia.Typeface.MakeFromFile(f) if os.path.exists(f) else E.FONT_BLACK
    return E.font(_BANGERS, sz)


def _rect(c, x, y, w, h, col, stroke=4, r=4, scol=INK):
    rr = skia.Rect.MakeXYWH(x, y, w, h)
    c.drawRoundRect(rr, r, r, _p(col))
    if stroke:
        c.drawRoundRect(rr, r, r, _p(scol, stroke))


def _night(v):
    return _mode(v) in ("night", "storm")


# ------------------------------------------------------------------ gemensamma föremål
def _skyline(c, base, v, seed=1, h0=120, h1=330, col=None, x0=0, x1=W):
    rnd = random.Random(seed)
    night = _night(v)
    col = col or (0xFF243150 if night else 0xFF7F93B0)
    x = x0 - 20
    while x < x1:
        w = rnd.uniform(70, 170); h = rnd.uniform(h0, h1)
        c.drawRect(skia.Rect.MakeXYWH(x, base - h, w, h + 2), _p(col))
        if night:
            for wy in range(int(base - h + 18), int(base - 14), 26):
                for wx in range(int(x + 10), int(x + w - 14), 22):
                    if rnd.random() < 0.35:
                        c.drawRect(skia.Rect.MakeXYWH(wx, wy, 10, 12), _p(0xCCFFD98A))
        x += w + rnd.uniform(4, 18)


def _pine(c, x, base, h, col=0xFF2F6A48, dark=False, sway=0.0):
    col = 0xFF1C3A30 if dark else col
    c.drawRect(skia.Rect.MakeXYWH(x - h * 0.03, base - h * 0.22, h * 0.06, h * 0.22), _p(0xFF5A3A24))
    for j in range(4):
        y1 = base - h * 0.15 - j * h * 0.2
        w = h * (0.34 - j * 0.06)
        top = y1 - h * 0.32
        tri = poly([(x - w, y1), (x + sway * (j + 1) * 6, top), (x + w, y1)], close=True)
        c.drawPath(tri, _p(col)); c.drawPath(tri, _p(INK, 3))


def _ridges(c, base, v, seed=4):
    m = _mode(v)
    cols = {"day": (0xFF8FA8C8, 0xFF6F8EA8), "dusk": (0xFF7A5A8A, 0xFF5A4A72), "dawn": (0xFF9A88B0, 0xFF6E6A98),
            "night": (0xFF24304E, 0xFF1A2440), "storm": (0xFF3A4252, 0xFF2A3040)}[m]
    rnd = random.Random(seed)
    for k, col in enumerate(cols):
        p = skia.Path(); p.moveTo(0, base)
        y = base - 140 + k * 60
        for x in range(0, W + 80, 80):
            y = max(base - 300 + k * 80, min(base - 40, y + rnd.uniform(-40, 40)))
            p.lineTo(x, y)
        p.lineTo(W, base + 2); p.lineTo(0, base + 2); p.close()
        c.drawPath(p, _p(col))


def _truck(c, x, base, s=1.0, col=0xFFC0392B, reefer=False, night=True, trailer=True):
    """Lastbil från sidan, hytten åt höger. Returnerar (fönstrets mitt x, y, bredd, höjd)."""
    wr = 34 * s
    if trailer:
        _rect(c, x, base - 2 * wr - 250 * s, 700 * s, 250 * s, 0xFFE8E2D4, 4 * s, 6 * s)
        c.drawRect(skia.Rect.MakeXYWH(x + 6 * s, base - 2 * wr - 90 * s, 688 * s, 18 * s), _p(col))
        c.drawRect(skia.Rect.MakeXYWH(x + 40 * s, base - 2 * wr - 10 * s, 640 * s, 10 * s), _p(0xFF3A3A3A))
        if reefer:
            _rect(c, x + 640 * s, base - 2 * wr - 240 * s, 50 * s, 120 * s, 0xFFB8BCC4, 3 * s, 4 * s)
            for k in range(5):
                c.drawLine(x + 648 * s, base - 2 * wr - (225 - k * 22) * s, x + 682 * s, base - 2 * wr - (225 - k * 22) * s, _p(INK, 3 * s))
        for wx in (80, 150, 560, 630):
            c.drawCircle(x + wx * s, base - wr, wr, _p(0xFF1E1E22)); c.drawCircle(x + wx * s, base - wr, wr * 0.45, _p(0xFF9A9AA2))
    cx = x + (710 if trailer else 0) * s
    cab = skia.Path()
    cab.moveTo(cx, base - wr * 1.2); cx2 = cx + 210 * s
    cab.lineTo(cx, base - wr - 240 * s); cab.lineTo(cx + 150 * s, base - wr - 240 * s)
    cab.lineTo(cx + 175 * s, base - wr - 150 * s); cab.lineTo(cx2, base - wr - 135 * s); cab.lineTo(cx2, base - wr * 1.2); cab.close()
    c.drawPath(cab, _p(col)); c.drawPath(cab, _p(INK, 4 * s))
    win = (cx + 85 * s, base - wr - 225 * s, 80 * s, 70 * s)
    c.drawRect(skia.Rect.MakeXYWH(*win), _p(0xFF3A4A66 if night else 0xFFA8D0E8)); c.drawRect(skia.Rect.MakeXYWH(*win), _p(INK, 3 * s))
    c.drawLine(cx + 20 * s, base - wr - 240 * s, cx + 20 * s, base - wr - 330 * s, _p(INK, 12 * s))
    c.drawLine(cx + 20 * s, base - wr - 240 * s, cx + 20 * s, base - wr - 330 * s, _p(0xFFC8C8D0, 7 * s))
    for wx in (60, 170):
        c.drawCircle(cx + wx * s, base - wr, wr, _p(0xFF1E1E22)); c.drawCircle(cx + wx * s, base - wr, wr * 0.45, _p(0xFF9A9AA2))
    if night:
        _glow(c, cx2 + 10 * s, base - wr * 2.2, 90 * s, 0x99FFF0C0)
        c.drawCircle(cx2, base - wr * 2.2, 10 * s, _p(0xFFFFF4D0))
    return (win[0] + win[2] / 2, win[1] + win[3], win[2], win[3]), (cx + 20 * s, base - wr - 330 * s)


def _car(c, x, base, s=1.0, col=0xFF4E7FB8, night=True, wagon=False):
    wr = 26 * s
    body = skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, base - wr - 70 * s, 300 * s, 70 * s), 18 * s, 18 * s)
    c.drawRRect(body, _p(col)); c.drawRRect(body, _p(INK, 4 * s))
    top = poly([(x + 60 * s, base - wr - 70 * s), (x + 95 * s, base - wr - 125 * s),
                (x + (270 if wagon else 210) * s, base - wr - 125 * s), (x + (285 if wagon else 245) * s, base - wr - 70 * s)], close=True)
    c.drawPath(top, _p(col)); c.drawPath(top, _p(INK, 4 * s))
    gw = poly([(x + 75 * s, base - wr - 74 * s), (x + 100 * s, base - wr - 116 * s),
               (x + (260 if wagon else 200) * s, base - wr - 116 * s), (x + (272 if wagon else 232) * s, base - wr - 74 * s)], close=True)
    c.drawPath(gw, _p(0xFF2E3A52 if night else 0xFFB8DCEC)); c.drawPath(gw, _p(INK, 3 * s))
    if wagon:
        c.drawRect(skia.Rect.MakeXYWH(x + 20 * s, base - wr - 52 * s, 260 * s, 22 * s), _p(0xFF9A6A3A))
    for wx in (65, 235):
        c.drawCircle(x + wx * s, base - wr, wr, _p(0xFF1E1E22)); c.drawCircle(x + wx * s, base - wr, wr * 0.4, _p(0xFF9A9AA2))
    return [(x + 8 * s, base - wr - 45 * s), (x + 292 * s, base - wr - 45 * s)]


def _waves(c, x, y, t, col=0xCCFFFFFF, n=3, r0=30, sp=60, face=1, w=6):
    """Ljudvågor (bågar) som rör sig utåt."""
    for k in range(n):
        ph = ((t * 1.3 + k / n) % 1.0)
        r = r0 + ph * sp * n
        a = (1 - ph)
        rect = skia.Rect.MakeXYWH(x - r, y - r, 2 * r, 2 * r)
        st = -50 if face > 0 else 130
        c.drawArc(rect, st, 100, False, _p(_a(col, a * ((col >> 24) / 255.0)), w))


def _storm(c, t, v, bolt_area=(0, 0, W, H * 0.5)):
    if not (v.get("storm") or v.get("lightning")):
        return
    k = int(t * 0.55)
    ph = t * 0.55 - k
    rnd = random.Random(k * 31 + 7)
    for i in range(70):   # regn
        x = (rnd.uniform(0, W) + t * 300) % W; y = (rnd.uniform(0, H) + t * 900 + i * 37) % H
        c.drawLine(x, y, x - 10, y + 34, _p(0x55C8D8F0, 2))
    if ph < 0.12:
        a = 1 - ph / 0.12
        c.drawRect(skia.Rect.MakeWH(W, H), _p(_a(0xFFE8F0FF, 0.45 * a)))
        x0, y0, bw, bh = bolt_area
        x = x0 + rnd.uniform(0.15, 0.85) * bw; y = y0
        pts = [(x, y)]
        while y < y0 + bh:
            x += rnd.uniform(-60, 60); y += rnd.uniform(40, 90); pts.append((x, y))
        path = poly(pts)
        c.drawPath(path, _p(_a(0xFFBFD8FF, a), 14)); c.drawPath(path, _p(_a(0xFFFFFFFF, a), 5))


def _floor(c, y0, top, bottom):
    _grad(c, (0, y0, W, H - y0), [top, bottom])


def _glass_overlay(c, rect, t, v, mull=4, flex=False, crack=False):
    x, y, w, h = rect
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w, h))
    c.drawRect(skia.Rect.MakeXYWH(x, y, w, h), _p(0x2A9CC8E8))
    for k in range(4):   # reflexer
        sx = x + w * (0.1 + 0.24 * k)
        p = poly([(sx, y), (sx + 60, y), (sx - 140, y + h), (sx - 200, y + h)], close=True)
        c.drawPath(p, _p(0x14FFFFFF))
    if flex:
        f = 0.5 + 0.5 * math.sin(t * 7)
        for k in range(mull):
            cx = x + w * (k + 0.5) / mull
            c.drawOval(skia.Rect.MakeXYWH(cx - w / mull * 0.35, y + h * 0.3, w / mull * 0.7, h * 0.4), _p(_a(0xFFFFFFFF, 0.08 + 0.12 * f), 5))
    c.restore()
    for k in range(mull + 1):
        mx = x + w * k / mull
        c.drawLine(mx, y, mx, y + h, _p(INK, 12)); c.drawLine(mx, y, mx, y + h, _p(0xFF8A94A4, 6))
    c.drawLine(x, y + h * 0.42, x + w, y + h * 0.42, _p(INK, 10)); c.drawLine(x, y + h * 0.42, x + w, y + h * 0.42, _p(0xFF8A94A4, 5))
    if crack:
        rnd = random.Random(5)
        px, py = x + w * 0.05, y + 10
        pts = [(px, py)]
        for i in range(9):
            px += w * 0.1 + rnd.uniform(-20, 20); py += h * 0.1 + rnd.uniform(-25, 25); pts.append((px, py))
        path = poly(pts)
        c.drawPath(path, _p(0xCC10141C, 7)); c.drawPath(path, _p(0xEEFFFFFF, 3))
        for (bx, by) in pts[2::2]:
            br = poly([(bx, by), (bx + rnd.uniform(-90, 90), by + rnd.uniform(-90, 90))])
            c.drawPath(br, _p(0xDDFFFFFF, 2))


def _glass_dead(c, t, rect, zs, gy, s=430, seed=0, extra=0, up=0.0):
    """De döda bakom glaset: rad längst bak + de som manuset anger, klippta till glaset."""
    x, y, w, h = rect
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w, h))
    rnd = random.Random(seed)
    for i in range(extra):
        zx = x + (i + 0.5) * w / max(1, extra) + rnd.uniform(-30, 30)
        _silhouette(c, zx, gy - 70, s * 0.72, t, 300 + seed + i, look=-1, up=up, arms="forward")
    for i, z in enumerate(zs):
        zx = W * z.get("x", 0.8) - z.get("speed", 0) * t
        if z.get("lunge"):
            zx += -12 * abs(math.sin(t * 2.2 + i))
        zx = max(x + 60, min(x + w - 40, zx))
        _silhouette(c, zx, gy, s, t, 40 + i + seed, look=-1, up=up, arms="up" if z.get("lunge") else "forward")
        if z.get("lunge"):   # händer mot glaset
            for k in (-1, 1):
                c.drawOval(skia.Rect.MakeXYWH(zx - 40 + k * 46, gy - s * 0.86, 34, 44), _p(0x88E8EEF4))
    c.restore()


# ------------------------------------------------------------------ 1. larmcentralen
GL_D = (W * 0.56, H * 0.1, W * 0.44, GY - H * 0.1)
PH_GRID = [(W * 0.07 + (i % 8) * 52, H * 0.2 + (i // 8) * 46) for i in range(40)]


def _lot_view(c, v, rect, seed=2):
    x, y, w, h = rect
    c.save(); c.clipRect(skia.Rect.MakeXYWH(x, y, w, h))
    _sky(c, v, bottom=y + h * 0.55, top=y)
    _skyline(c, y + h * 0.55, v, seed, 60, 200, x0=x, x1=x + w)
    _grad(c, (x, y + h * 0.55, w, h * 0.45), [0xFF3C4250, 0xFF2A2E38])
    for k in range(6):
        lx = x + w * (0.15 + 0.17 * k)
        c.drawLine(lx, y + h * 0.75, lx - 60, y + h, _p(0xAAE8E0B0, 4))
    for lx in (x + w * 0.25, x + w * 0.8):
        pier._lamp(c, lx, y + h * 0.6, h * 0.42, True, 0xFFFFC870)
    c.restore()


def bg_dispatch(c, t, v):
    if v.get("type") == "crowd":
        _lot_view(c, v, (0, 0, W, H), seed=3)
        return
    _grad(c, (0, 0, W, GY), [0xFF34415E, 0xFF4A5876])
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, H * 0.06), _p(0xFF262E40))
    for k in range(4):
        c.drawRect(skia.Rect.MakeXYWH(W * 0.04 + k * W * 0.13, H * 0.065, W * 0.1, 10), _p(0xFFE8F0FF))
        _glow(c, W * 0.09 + k * W * 0.13, H * 0.08, 200, 0x33DDE8FF)
    _floor(c, GY, 0xFF505868, 0xFF333844)
    _lot_view(c, v, GL_D)
    # linjetavlan
    _rect(c, W * 0.05, H * 0.15, 8 * 52 + 20, 5 * 46 + 30, 0xFF1C2230, 5, 8)
    E.draw_text(c, "LINES 1–40", W * 0.05 + 214, H * 0.15 - 12, E.font(E.FONT_BOLD, 30), color=0xFFE8E8E8)
    for (px, py) in PH_GRID:
        c.drawCircle(px + 18, py + 30, 13, _p(0xFF3A2224)); c.drawCircle(px + 18, py + 30, 13, _p(INK, 3))
    # borden (två rader)
    for row, (yb, sc) in enumerate(((GY - 190, 0.8), (GY - 110, 1.0))):
        for k in range(3):
            dx = W * 0.03 + k * W * 0.175 + row * W * 0.04
            dw = W * 0.15 * sc
            _rect(c, dx, yb, dw, 22 * sc, 0xFF8A6A4A, 4, 3)
            c.drawLine(dx + 14, yb + 22 * sc, dx + 14, yb + 110 * sc, _p(INK, 7))
            c.drawLine(dx + dw - 14, yb + 22 * sc, dx + dw - 14, yb + 110 * sc, _p(INK, 7))
            for mk in range(2):
                mx = dx + 20 + mk * dw * 0.48
                _rect(c, mx, yb - 92 * sc, dw * 0.42, 80 * sc, 0xFF16202E, 4, 4)
                c.drawRect(skia.Rect.MakeXYWH(mx + 6, yb - 86 * sc, dw * 0.42 - 12, 68 * sc), _p(0xFF3A78B8))
                _glow(c, mx + dw * 0.21, yb - 52 * sc, 120 * sc, 0x553A9AE8)
            _rect(c, dx + dw * 0.4, yb - 16 * sc, 50 * sc, 16 * sc, 0xFF2A2A2E, 3, 3)
    if v.get("breaker"):
        _rect(c, W * 0.47, H * 0.3, 120, 190, 0xFF9AA0A8, 5, 6)
        c.drawLine(W * 0.47 + 60, H * 0.3 + 60, W * 0.47 + 60, H * 0.3 + 150, _p(INK, 16))
        c.drawRect(skia.Rect.MakeWH(W, H), _p(0x8A050814))
        _glow(c, W * 0.3, H * 0.08, 420, 0x66FF3030)
        c.drawCircle(W * 0.3, H * 0.07, 18, _p(0xFFFF4A3A))


def live_dispatch(c, t, v, d):
    if v.get("type") == "crowd":
        return
    n = int(v.get("phones_lit", 0) or 0)
    for i, (px, py) in enumerate(PH_GRID[:n]):
        on = math.sin(t * 9 + i * 1.7) > -0.2
        if on:
            _glow(c, px + 18, py + 30, 46, 0x99FF4030)
            c.drawCircle(px + 18, py + 30, 12, _p(0xFFFF4A3A))
    if n:
        _glow(c, W * 0.25, H * 0.3, 520, _a(0xFFFF3020, 0.10 + 0.05 * math.sin(t * 9)))
    zs = STASH.get("z") or []
    glass = v.get("glass_wall") or zs or v.get("glass_flex") or v.get("glass_crack")
    if glass:
        extra = 6 if (v.get("glass_flex") or len(zs) >= 4) else (3 if zs else 0)
        _glass_dead(c, t, GL_D, zs, GY + 20, 470, seed=1, extra=extra)
    _glass_overlay(c, GL_D, t, v, mull=4, flex=v.get("glass_flex"), crack=v.get("glass_crack"))
    if v.get("radio"):
        rx, ry = W * 0.33, GY - 130
        _rect(c, rx, ry, 90, 60, 0xFF2A2E36, 4, 6)
        c.drawCircle(rx + 30, ry + 30, 16, _p(0xFF505860)); c.drawLine(rx + 70, ry, rx + 80, ry - 60, _p(INK, 5))
        _waves(c, rx + 90, ry + 20, t, 0xDDFFE08A)
    if v.get("shot") == "close" and not glass and STASH["v"].get("sign"):
        _glow(c, W * 0.5, H * 0.5, 600, 0x223A9AE8)


# ------------------------------------------------------------------ 2. taket
def bg_dispatch_roof(c, t, v):
    _sky(c, v, bottom=H * 0.62)
    _skyline(c, H * 0.62, v, 6, 80, 260)
    _grad(c, (0, H * 0.6, W, H * 0.04), [0xFF5A6070, 0xFF4A505E])
    _floor(c, H * 0.64, 0xFF6A6E78, 0xFF44474F)
    for (x, w) in ((W * 0.07, 260), (W * 0.72, 320)):
        _rect(c, x, GY - 210, w, 170, 0xFFA8ACB4, 5, 8)
        c.drawCircle(x + w / 2, GY - 125, 55, _p(0xFF6E727A)); c.drawCircle(x + w / 2, GY - 125, 55, _p(INK, 4))
    _rect(c, W * 0.42, GY - 40, 240, 60, 0xFF3A3E48, 5, 4)   # luckan
    for k in (W * 0.44, W * 0.54):
        c.drawLine(k, GY - 40, k, GY - 130, _p(INK, 10)); c.drawLine(k, GY - 40, k, GY - 130, _p(0xFFB8BCC4, 5))
    c.drawLine(W * 0.62, GY - 60, W * 0.62, H * 0.18, _p(INK, 8))


def live_dispatch_roof(c, t, v, d):
    if math.sin(t * 3) > 0:
        _glow(c, W * 0.62, H * 0.18, 60, 0xCCFF3030); c.drawCircle(W * 0.62, H * 0.18, 9, _p(0xFFFF4A3A))
    _dust(c, t, 4, 30, (0, 0, W, H * 0.6), 0x44FFFFFF)


# ------------------------------------------------------------------ 3. parkeringshuset
CARS = [(W * 0.02, 0xFFC0392B), (W * 0.2, 0xFF2E86C8), (W * 0.38, 0xFFE8E8E8), (W * 0.56, 0xFF3A9A5A), (W * 0.74, 0xFFE8B63A)]


def bg_garage(c, t, v):
    crowd = v.get("type") == "crowd"
    _grad(c, (0, 0, W, GY), [0xFF5A606A, 0xFF7A808A])
    c.drawRect(skia.Rect.MakeXYWH(0, 0, W, H * 0.12), _p(0xFF4A4E56))
    for k in range(6):
        c.drawRect(skia.Rect.MakeXYWH(W * 0.05 + k * W * 0.16, H * 0.12, W * 0.1, 12), _p(0xFFF0F6FF))
        _glow(c, W * 0.1 + k * W * 0.16, H * 0.14, 240, 0x44E8F4FF)
    # öppningen mot staden (bakvägg med räcke)
    c.save(); c.clipRect(skia.Rect.MakeXYWH(0, H * 0.18, W, H * 0.22))
    _sky(c, v, bottom=H * 0.4, top=H * 0.18); _skyline(c, H * 0.4, v, 8, 30, 120)
    c.restore()
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.4, W, 20), _p(0xFF8A8E96))
    _floor(c, GY, 0xFF6A6E76, 0xFF3E4148)
    for k in range(7):
        x = W * (0.02 + 0.155 * k)
        c.drawLine(x, GY + 10, x - 90, H, _p(0xCCF2E8B0, 5))
    for k in range(5):
        px = W * (0.17 + 0.18 * k)
        _rect(c, px, H * 0.12, 46, GY - H * 0.12, 0xFF9A9EA6, 4, 2)
        c.drawRect(skia.Rect.MakeXYWH(px, GY - 120, 46, 26), _p(0xFFE8C23A))
    if not crowd:
        for (x, col) in CARS:
            _car(c, x, GY - 30, 0.95, col, night=True)
    else:
        for (x, col) in CARS[:3]:
            _car(c, x + W * 0.1, H * 0.6, 0.6, col, night=True)
    if v.get("ramp") or crowd:
        rp = poly([(W * 0.62, GY), (W, GY - H * 0.36), (W, GY - H * 0.28), (W * 0.7, GY)], close=True)
        c.drawPath(rp, _p(0xFF8A8E96)); c.drawPath(rp, _p(INK, 5))
        E.draw_text(c, "UP ▲", W * 0.88, GY - H * 0.33, E.font(E.FONT_BOLD, 40), color=0xFFF2E8B0)
    if v.get("booth"):
        _rect(c, W * 0.0, GY - 300, 230, 300, 0xFFE8E2D0, 5, 6)
        c.drawRect(skia.Rect.MakeXYWH(20, GY - 270, 190, 120), _p(0xFFB8D8EC))
        _glow(c, 115, GY - 210, 160, 0x66FFE8B0)
        c.drawRect(skia.Rect.MakeXYWH(230, GY - 140, W * 0.18, 18), _p(0xFFFFFFFF))
        for k in range(5):
            c.drawRect(skia.Rect.MakeXYWH(240 + k * W * 0.036, GY - 140, W * 0.018, 18), _p(0xFFD8342A))
    if v.get("key_cabinet"):
        cx, cy = W * 0.3, H * 0.3
        _rect(c, cx, cy, W * 0.4, H * 0.42, 0xFF7A5A3A, 6, 8)
        c.drawRect(skia.Rect.MakeXYWH(cx + 16, cy + 16, W * 0.4 - 32, H * 0.42 - 32), _p(0xFFE8DCC0))
        for i in range(80):
            kx = cx + 40 + (i % 10) * (W * 0.4 - 80) / 9; ky = cy + 50 + (i // 10) * 50
            c.drawCircle(kx, ky, 6, _p(INK))
            c.drawRect(skia.Rect.MakeXYWH(kx - 7, ky + 6, 14, 22), _p([0xFFD8342A, 0xFF2E86C8, 0xFF3A9A5A, 0xFFE8B63A][i % 4]))


def live_garage(c, t, v, d):
    n = int(v.get("alarm_lights", 0) or 0)
    if v.get("type") == "crowd":
        n = 3
    pts = []
    for (x, col) in CARS:
        pts += [(x + 8, GY - 30 - 26 - 45), (x + 290, GY - 30 - 26 - 45)]
    order = [2, 3, 1, 4, 0]
    for j in range(min(n, len(CARS))):
        i = order[j]
        on = math.sin(t * 8 + i * 1.3) > 0
        for (lx, ly) in pts[2 * i:2 * i + 2]:
            if on:
                _glow(c, lx, ly, 90, 0xCCFFA020); c.drawCircle(lx, ly, 11, _p(0xFFFFC040))
        if on:
            _waves(c, CARS[i][0] + 150, GY - 220, t + i * 0.3, 0xBBFFC040, n=2, r0=40, sp=50)
    if n > len(CARS):
        _glow(c, W * 0.5, H * 0.25, 700, _a(0xFFFFA020, 0.08 + 0.06 * math.sin(t * 8)))


def bg_street(c, t, v):
    _sky(c, v, bottom=H * 0.5)
    _skyline(c, H * 0.5, v, 11, 120, 300)
    for k in range(5):
        x = W * (0.02 + 0.2 * k)
        _rect(c, x, H * 0.3, W * 0.18, GY - H * 0.3, [0xFF8A5A4A, 0xFF5A6A8A, 0xFF7A6A5A, 0xFF4A6A6A, 0xFF8A7A5A][k], 5, 2)
        c.drawRect(skia.Rect.MakeXYWH(x + 20, GY - 170, W * 0.18 - 40, 130), _p(0xFFFFD98A if k % 2 else 0xFF2A3448))
        _glow(c, x + W * 0.09, GY - 110, 160, 0x55FFD98A if k % 2 else 0x00000000)
        _rect(c, x + 10, H * 0.32, W * 0.18 - 20, 40, [0xFFE8382E, 0xFF2E86C8, 0xFFE8B63A, 0xFF3A9A5A, 0xFFE8E8E8][k], 3, 4)
    _floor(c, GY, 0xFF8A8A8A, 0xFF3A3C44)
    c.drawRect(skia.Rect.MakeXYWH(0, GY + 50, W, 10), _p(0xFFB0B0B0))
    for x in (W * 0.15, W * 0.55, W * 0.92):
        pier._lamp(c, x, GY + 20, H * 0.5, True, 0xFFFFC870)


# ------------------------------------------------------------------ 4. lastbilsparkeringen
def bg_truckstop(c, t, v):
    _sky(c, v, bottom=H * 0.5)
    _ridges(c, H * 0.5, v, 7)
    _grad(c, (0, H * 0.5, W, H * 0.5), [0xFF3E4250, 0xFF2A2C34])
    # tak med DIESEL
    _rect(c, W * 0.68, H * 0.2, W * 0.34, 50, 0xFFE8E8E8, 5, 4)
    E.draw_text(c, "DIESEL", W * 0.85, H * 0.2 + 40, E.font(E.FONT_BLACK, 40), color=0xFFD8342A)
    for x in (W * 0.72, W * 0.97):
        c.drawRect(skia.Rect.MakeXYWH(x, H * 0.2 + 50, 22, H * 0.3), _p(0xFFB8BCC4))
    _glow(c, W * 0.85, H * 0.32, 420, 0x66FFF0C0)
    pier._lamp(c, W * 0.1, H * 0.62, H * 0.4, True, 0xFFFFB060)
    pier._lamp(c, W * 0.5, H * 0.6, H * 0.38, True, 0xFFFFB060)
    _glow(c, W * 0.1, H * 0.25, 500, 0x33FFA040); _glow(c, W * 0.5, H * 0.25, 500, 0x33FFA040)
    cols = [0xFFC0392B, 0xFF2E6AB8, 0xFF3A8A5A, 0xFFE8B63A, 0xFF8A4AB0]
    for k in range(4):
        _truck(c, W * (-0.05 + 0.27 * k), H * 0.6, 0.42, cols[k % 5], reefer=(k == 2))
    if v.get("type") != "crowd":
        for k in range(2):
            _truck(c, W * (-0.12 + 0.55 * k), H * 0.76, 0.66, cols[(k + 2) % 5], reefer=(k == 1))
    if v.get("logbook"):
        lx, ly, lw, lh = W * 0.3, H * 0.27, W * 0.4, H * 0.48
        _rect(c, lx, ly, lw, lh, 0xFFFBF6E8, 6, 8)
        E.draw_text(c, "DRIVER'S DAILY LOG", lx + lw / 2, ly + 56, E.font(E.FONT_BOLD, 40), color=INK)
        labels = ["OFF DUTY", "SLEEPER", "DRIVING", "ON DUTY"]
        for i, lb in enumerate(labels):
            yy = ly + 110 + i * 70
            c.drawLine(lx + 190, yy, lx + lw - 30, yy, _p(0xFF8A8A8A, 2))
            E.draw_text(c, lb, lx + 30, yy + 10, E.font(E.FONT_BOLD, 26), color=INK, align="left")
        seg = [(0, 0, 0.12), (2, 0.12, 0.58), (3, 0.58, 0.62), (0, 0.62, 1.0)]
        x0, x1 = lx + 190, lx + lw - 30
        for (row, a, b) in seg:
            yy = ly + 110 + row * 70
            c.drawLine(x0 + (x1 - x0) * a, yy, x0 + (x1 - x0) * b, yy, _p(0xFF2E6AB8, 9))


def live_truckstop(c, t, v, d):
    stacks = []
    for k in range(4):
        stacks.append((W * (-0.05 + 0.27 * k) + (710 + 20) * 0.42, H * 0.6 - 34 * 0.42 - 330 * 0.42, 0.42))
    if v.get("type") != "crowd":
        for k in range(2):
            stacks.append((W * (-0.12 + 0.55 * k) + (710 + 20) * 0.66, H * 0.76 - 34 * 0.66 - 330 * 0.66, 0.66))
    for i, (sx, sy, s) in enumerate(stacks):
        for j in range(4):
            ph = (t * 0.5 + j / 4 + i * 0.13) % 1
            c.drawCircle(sx + ph * 40 * s, sy - ph * 180 * s, (10 + ph * 40) * s, _p(_a(0xFFB8BCC8, 0.35 * (1 - ph))))
    if v.get("reefer_on"):
        rx = W * (-0.12 + 0.55) + 665 * 0.66; ry = H * 0.76 - 2 * 34 * 0.66 - 180 * 0.66
        jit = math.sin(t * 60) * 3
        _glow(c, rx, ry, 160, 0x66FFFFFF)
        _waves(c, rx + jit, ry, t, 0xEEFFFFFF, n=3, r0=40, sp=70, face=-1, w=8)
        _waves(c, rx + jit, ry, t + 0.3, 0xEEFFFFFF, n=3, r0=40, sp=70, face=1, w=8)
    if STASH["v"].get("sfx_vis") == "hiss":
        for j in range(8):
            ph = (t * 1.4 + j / 8) % 1
            c.drawCircle(W * 0.5 + ph * 160, GY - 40 - ph * 60, 12 + ph * 50, _p(_a(0xFFFFFFFF, 0.5 * (1 - ph))))
    if v.get("cb_radio"):
        _waves(c, W * 0.5, H * 0.25, t, 0xCCFFE08A, n=3, r0=30, sp=40)
    hv = STASH["v"].get("hero") or {}
    if hv.get("on") == "cab":
        x = W * hv.get("x", 0.5) - (710 + 125) * 0.9
        win, _ = _truck(c, x, GY + 40, 0.9, 0xFF2E6AB8)
        pier._draw_fig(c, win[0], win[1] + 70, 0.45, t, hv, face=1)
        c.drawRect(skia.Rect.MakeXYWH(win[0] - win[2] / 2 - 6, win[1], win[2] + 12, 150), _p(0xFF2E6AB8))
        c.drawLine(win[0] - win[2] / 2 - 6, win[1], win[0] + win[2] / 2 + 6, win[1], _p(INK, 4))


# ------------------------------------------------------------------ 5. sovhytten
WIN_CAB = (W * 0.6, H * 0.16, W * 0.32, H * 0.42)


def bg_cab(c, t, v):
    _grad(c, (0, 0, W, GY), [0xFF4A3A34, 0xFF6A5244])
    c.save(); c.clipRect(skia.Rect.MakeXYWH(*WIN_CAB))
    _grad(c, WIN_CAB, [0xFF1C2A4A, 0xFF34466E])
    for k in range(3):
        _glow(c, WIN_CAB[0] + WIN_CAB[2] * (0.2 + 0.3 * k), WIN_CAB[1] + WIN_CAB[3] * 0.5, 120, 0x88FFB060)
    c.restore()
    _floor(c, GY, 0xFF3A2E2A, 0xFF241C1A)
    _rect(c, W * 0.0, GY - 170, W * 0.42, 120, 0xFF6A4A8A, 5, 14)    # britsen
    _rect(c, W * 0.02, GY - 200, 220, 60, 0xFFE8E2D0, 4, 20)
    c.drawRect(skia.Rect.MakeXYWH(W * 0.44, H * 0.05, 30, GY - H * 0.05), _p(0xFF8A3A2E))   # gardin
    for k in range(6):
        c.drawLine(W * 0.44 + 5 + k * 5, H * 0.05, W * 0.44 + 5 + k * 5, GY, _p(0x55000000, 2))
    _rect(c, W * 0.46, H * 0.02, W * 0.2, 70, 0xFF2A2A2E, 4, 6)   # konsol med CB
    E.draw_text(c, "CB 19", W * 0.56, H * 0.02 + 48, E.font(E.FONT_BOLD, 30), color=0xFF8AE88A)
    _glow(c, W * 0.25, H * 0.1, 300, 0x44FFD9A0)


def live_cab(c, t, v, d):
    zs = STASH.get("z") or []
    if zs or v.get("door_hits"):
        c.save(); c.clipRect(skia.Rect.MakeXYWH(*WIN_CAB))
        for i, z in enumerate(zs or [{"x": 0.8}, {"x": 0.9}]):
            zx = WIN_CAB[0] + WIN_CAB[2] * (0.3 + 0.4 * i)
            _silhouette(c, zx, WIN_CAB[1] + WIN_CAB[3] + 420, 720, t, 90 + i, look=-1, up=0.2, arms="up")
        if v.get("door_hits"):
            for i in range(3):
                ph = (t * 2.4 + i * 0.37) % 1
                if ph < 0.4:
                    hx = WIN_CAB[0] + WIN_CAB[2] * (0.2 + 0.3 * i); hy = WIN_CAB[1] + WIN_CAB[3] * (0.35 + 0.15 * (i % 2))
                    c.drawOval(skia.Rect.MakeXYWH(hx - 30, hy - 40, 60, 80), _p(0xEE2A2E36))
                    c.drawOval(skia.Rect.MakeXYWH(hx - 30, hy - 40, 60, 80), _p(0xFF8A9AB8, 3))
        c.restore()
    _glass_overlay(c, WIN_CAB, t, v, mull=1)
    c.drawRect(skia.Rect.MakeXYWH(*WIN_CAB), _p(INK, 10))
    if v.get("cb_radio"):
        _glow(c, W * 0.56, H * 0.05, 140, _a(0xFF8AE88A, 0.4 + 0.3 * math.sin(t * 12)))
        _waves(c, W * 0.66, H * 0.06, t, 0xCCFFE08A, n=3, r0=24, sp=36)


# ------------------------------------------------------------------ 6. motorvägen
def bg_highway(c, t, v):
    _sky(c, v, bottom=H * 0.52)
    _ridges(c, H * 0.52, v, 12)
    _grad(c, (0, H * 0.52, W, H * 0.48), [0xFF7A9A5A, 0xFF5A7A42])
    road = poly([(W * 0.46, H * 0.52), (W * 0.54, H * 0.52), (W * 1.3, H), (-W * 0.3, H)], close=True)
    c.drawPath(road, _p(0xFF4A4C54))
    for k in range(8):
        f0 = (k / 8) ** 1.8; f1 = ((k + 0.5) / 8) ** 1.8
        y0 = H * 0.52 + (H * 0.48) * f0; y1 = H * 0.52 + (H * 0.48) * f1
        c.drawLine(W * 0.5, y0, W * 0.5, y1, _p(0xFFF2D04A, 3 + 14 * f1))
    c.drawRect(skia.Rect.MakeXYWH(0, GY - 40, W, 14), _p(0xFFB8BCC4))
    for k in range(12):
        c.drawRect(skia.Rect.MakeXYWH(k * W / 12, GY - 40, 10, 50), _p(0xFF8A8E96))
    c.drawRect(skia.Rect.MakeXYWH(0, GY - 6, W, H - GY + 6), _p(0xFF55575E))


def live_highway(c, t, v, d):
    hv = STASH["v"].get("hero") or {}
    if v.get("truck_moving") or hv.get("on") == "cab":
        if hv.get("on") == "cab":
            x = W * 0.5 - (710 + 125) * 0.62
        else:
            x = W * (-0.35 + 0.5 * E.ease(t / max(d, 1)))
        win, _ = _truck(c, x, GY + 30, 0.62, 0xFFC0392B, night=False)
        if hv.get("on") == "cab":
            pier._draw_fig(c, win[0], win[1] + 70, 0.34, t, hv, face=1)
            _truck_window_mask(c, win)
    if v.get("car"):
        x = W * (0.1 + 0.4 * E.ease(t / max(d, 1)))
        _car(c, x, GY + 20, 1.1, 0xFFC8A060, night=False, wagon=True)


def _truck_window_mask(c, win):
    cx, by, w, h = win
    c.drawRect(skia.Rect.MakeXYWH(cx - w / 2 - 6, by, w + 12, 120), _p(0xFFC0392B))
    c.drawLine(cx - w / 2 - 6, by, cx + w / 2 + 6, by, _p(INK, 4))


# ------------------------------------------------------------------ 7. dinern
DW = (W * 0.24, H * 0.14, W * 0.72, H * 0.34)      # fönsterbandet
DOOR = (W * 0.03, H * 0.22, W * 0.12, GY - H * 0.22)


def bg_diner(c, t, v):
    if v.get("type") == "crowd":
        bg_diner_lot(c, t, v)
        return
    _grad(c, (0, 0, W, GY), [0xFFE8D8B8, 0xFFF2E4C8])
    c.drawRect(skia.Rect.MakeXYWH(0, DW[1] + DW[3], W, 40), _p(0xFFD8342A))
    c.drawRect(skia.Rect.MakeXYWH(0, DW[1] + DW[3] + 40, W, 14), _p(0xFFC8CCD4))
    _lot_view(c, v, DW, seed=9)
    # golv i schackrutor
    _floor(c, GY, 0xFFEFEFEF, 0xFFD8D8D8)
    sq = 70
    for i in range(0, W // sq + 2):
        for j in range(0, int((H - GY) // sq) + 2):
            if (i + j) % 2 == 0:
                c.drawRect(skia.Rect.MakeXYWH(i * sq - (j * 18) % sq, GY + j * sq, sq, sq), _p(0xFF2A2A2E))
    # bås
    for k in range(3):
        bx = W * (0.25 + 0.12 * k)
        _rect(c, bx, GY - 200, 40, 200, 0xFFD8342A, 4, 8); _rect(c, bx + 130, GY - 200, 40, 200, 0xFFD8342A, 4, 8)
        _rect(c, bx + 40, GY - 120, 90, 18, 0xFFE8E8E8, 3, 3)
    # disk + jukebox
    _rect(c, W * 0.66, GY - 150, W * 0.34, 150, 0xFFE8382E, 5, 6)
    c.drawRect(skia.Rect.MakeXYWH(W * 0.66, GY - 160, W * 0.34, 18), _p(0xFFC8CCD4))
    for k in range(4):
        sx = W * (0.68 + 0.08 * k)
        c.drawLine(sx, GY - 60, sx, GY, _p(INK, 8)); c.drawOval(skia.Rect.MakeXYWH(sx - 34, GY - 76, 68, 22), _p(0xFFD8342A))
    cl = STASH["v"].get("shot") == "close"
    jx, jy = (W * 0.44, H * 0.3) if cl else (W * 0.6, GY - 260)
    js = 1.7 if cl else 1.0
    arch = skia.Path(); arch.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(jx, jy, 120 * js, 260 * js), 60 * js, 60 * js))
    c.drawPath(arch, _p(0xFF8A4A2A)); c.drawPath(arch, _p(INK, 5))
    c.drawRect(skia.Rect.MakeXYWH(jx + 20 * js, jy + 70 * js, 80 * js, 60 * js), _p(0xFF2A2A2E))
    # dörren
    _rect(c, DOOR[0], DOOR[1], DOOR[2], DOOR[3], 0xFFC8CCD4, 6, 4)
    c.drawRect(skia.Rect.MakeXYWH(DOOR[0] + 18, DOOR[1] + 20, DOOR[2] - 36, DOOR[3] * 0.55), _p(0xFF2A3448))
    c.drawCircle(DOOR[0] + DOOR[2] / 2, DOOR[1] - 18, 16, _p(0xFFE8C23A)); c.drawCircle(DOOR[0] + DOOR[2] / 2, DOOR[1] - 18, 16, _p(INK, 3))
    _glow(c, W * 0.5, H * 0.08, 600, 0x44FFE8B0)


def live_diner(c, t, v, d):
    zs = STASH.get("z") or []
    if v.get("window_dead") or zs:
        _glass_dead(c, t, DW, [z for z in zs if not v.get("door_open")], DW[1] + DW[3] + 330, 420, seed=5,
                    extra=8 if v.get("window_dead") else 0)
    _glass_overlay(c, DW, t, v, mull=6)
    if v.get("door_open"):
        gx = DOOR[0] + 18; gw = DOOR[2] - 36
        c.drawRect(skia.Rect.MakeXYWH(gx, DOOR[1] + 20, gw, DOOR[3] - 20), _p(0xFF141A26))
        c.save(); c.clipRect(skia.Rect.MakeXYWH(gx, DOOR[1] + 20, gw, DOOR[3] - 20))
        _silhouette(c, gx + gw * (0.3 + 0.2 * E.ease(t / max(d, 1))), GY, 400, t, 77, look=1, arms="forward")
        c.restore()
        sw = math.sin(t * 14) * 10
        c.drawCircle(DOOR[0] + DOOR[2] / 2 + sw, DOOR[1] - 18, 16, _p(0xFFFFE08A))
        _waves(c, DOOR[0] + DOOR[2] / 2, DOOR[1] - 18, t, 0xDDFFE08A, n=2, r0=24, sp=30)
    else:
        c.drawRect(skia.Rect.MakeXYWH(DOOR[0] + 18, DOOR[1] + 20, DOOR[2] - 36, DOOR[3] * 0.55), _p(0x22FFFFFF))
    if v.get("jukebox"):
        cl = STASH["v"].get("shot") == "close"
        js = 1.7 if cl else 1.0
        jx, jy = (W * 0.44, H * 0.3) if cl else (W * 0.6, GY - 260)
        for k in range(6):
            col = [0xFFFF4A6A, 0xFFFFC040, 0xFF4AE8FF][(k + int(t * 4)) % 3]
            c.drawCircle(jx + (20 + k * 16) * js, jy + 40 * js, 7 * js, _p(col))
        _glow(c, jx + 60 * js, jy + 120 * js, 260 * js, 0x55FF60A0)
        _waves(c, jx + 130 * js, jy + 100 * js, t, 0xCCFFFFFF, n=3, r0=30, sp=50)
        _rect(c, jx + 15 * js, jy + 150 * js, 90 * js, 34 * js, 0xFFFFF6E0, 3, 4)
        E.draw_text(c, "4:00", jx + 60 * js, jy + 176 * js, E.font(E.FONT_BOLD, int(26 * js)), color=0xFFD8342A)
    n = int(v.get("timers", 0) or 0)
    for i in range(n):
        tx = W * 0.67 + (i % 6) * 95; ty = GY - 190 - (i // 6) * 70
        c.drawCircle(tx, ty, 28, _p(0xFFFFFFFF)); c.drawCircle(tx, ty, 28, _p(0xFFD8342A, 6))
        a = t * (1 + i * 0.3) + i
        c.drawLine(tx, ty, tx + 20 * math.sin(a), ty - 20 * math.cos(a), _p(INK, 4))


def bg_diner_lot(c, t, v):
    _sky(c, v, bottom=H * 0.6)
    _skyline(c, H * 0.6, v, 13, 40, 140)
    _grad(c, (0, H * 0.6, W, H * 0.4), [0xFF3C4250, 0xFF2A2E38])
    bx, by, bw, bh = W * 0.14, H * 0.34, W * 0.6, H * 0.24
    _rect(c, bx, by, bw, bh, 0xFFC8CCD4, 6, 30)
    c.drawRect(skia.Rect.MakeXYWH(bx, by + bh * 0.72, bw, 18), _p(0xFFD8342A))
    for k in range(7):
        c.drawRect(skia.Rect.MakeXYWH(bx + 30 + k * (bw - 60) / 7, by + 26, (bw - 60) / 7 - 16, bh * 0.5), _p(0xFFFFE2A0))
    _glow(c, bx + bw / 2, by + bh * 0.4, 600, 0x66FFD890)
    _rect(c, bx + bw * 0.3, by - 120, bw * 0.4, 90, 0xFF2A2A34, 5, 10)
    c.drawRect(skia.Rect.MakeXYWH(bx + bw * 0.5 - 8, by - 30, 16, 30), _p(INK))
    for k in range(5):
        c.drawLine(k * W / 5 + 40, H * 0.66, k * W / 5 - 40, H * 0.8, _p(0xAAE8E0B0, 4))
    c.drawRect(skia.Rect.MakeXYWH(0, GY + 30, W, 8), _p(0xFFF2D04A))


def live_diner_lot(c, t, v, d):
    bx, by, bw = W * 0.14, H * 0.34, W * 0.6
    fl = 0.8 + 0.2 * math.sin(t * 13) * math.sin(t * 5)
    _glow(c, bx + bw / 2, by - 75, 380, _a(0xFFFF4A9A, 0.45 * fl))
    E.draw_text(c, "DINER", bx + bw / 2, by - 50, _bangers(84), color=_a(0xFFFF7AC0, fl))
    E.draw_text(c, "OPEN 24 HRS", bx + bw / 2, by - 135, E.font(E.FONT_BOLD, 36), color=_a(0xFF7AE8FF, fl))
    n = int(v.get("throw_items", 0) or 0)
    hv = STASH["v"].get("hero") or {}
    x0 = W * hv.get("x", 0.2)
    for i in range(n):
        ph = (t * 0.45 + i * 0.28) % 1
        x = x0 + ph * W * (0.45 + 0.1 * i); y = GY - 260 - math.sin(ph * math.pi) * H * 0.35
        c.drawCircle(x, y, 22, _p(0xFFFFFFFF)); c.drawCircle(x, y, 22, _p(0xFFD8342A, 5))
    if n or v.get("zombies_in"):
        for i in range(2):
            ph = (t * 0.8 + i * 0.5) % 1
            _waves(c, W * (0.75 + 0.15 * i), GY - 40, t + i * 0.4, 0xCCFFE08A, n=2, r0=30, sp=40)


def bg_diner_back(c, t, v):
    _grad(c, (0, 0, W, GY), [0xFF6A4A3E, 0xFF8A5E4A])
    for row in range(0, int(GY), 40):
        for k in range(0, W, 110):
            c.drawRect(skia.Rect.MakeXYWH(k + (55 if (row // 40) % 2 else 0), row, 104, 34), _p(0x22000000), )
    _floor(c, GY, 0xFF4A4C54, 0xFF2E3036)
    _rect(c, W * 0.08, GY - 330, 170, 330, 0xFF5A6A7A, 6, 4)
    _glow(c, W * 0.08 + 85, GY - 370, 260, 0x88FFD890); c.drawCircle(W * 0.08 + 85, GY - 370, 18, _p(0xFFFFE8B0))
    for k in range(3):
        bx = W * (0.24 + 0.08 * k)
        _rect(c, bx, GY - 150, 110, 150, 0xFF3A5A3A, 5, 10)
        E.draw_text(c, "GREASE", bx + 55, GY - 70, E.font(E.FONT_BOLD, 22), color=0xFFE8E8E8)
    _car(c, W * 0.6, GY + 10, 1.3, 0xFFC8A060, night=True, wagon=True)


def live_diner_back(c, t, v, d):
    if v.get("radio"):
        _glow(c, W * 0.75, GY - 120, 160, _a(0xFF8AE8FF, 0.5 + 0.3 * math.sin(t * 10)))
        _waves(c, W * 0.8, GY - 150, t, 0xCCFFE08A, n=3, r0=30, sp=45)


# ------------------------------------------------------------------ 8. zoot
def _lion(c, x, y, s, mode, t):
    body = skia.Rect.MakeXYWH(x - 120 * s, y - 90 * s, 240 * s, 90 * s)
    if mode == "lying":
        body = skia.Rect.MakeXYWH(x - 140 * s, y - 60 * s, 280 * s, 60 * s)
    c.drawOval(body, _p(0xFFD8A048)); c.drawOval(body, _p(INK, 4 * s))
    if mode != "lying":
        for lx in (-90, -50, 60, 95):
            c.drawRect(skia.Rect.MakeXYWH(x + lx * s, y - 30 * s, 22 * s, 30 * s), _p(0xFFD8A048))
    hx, hy = (x + 140 * s, y - 70 * s) if mode == "lying" else (x + 120 * s, y - 120 * s)
    if mode == "roar":
        hy -= 20 * s
    c.drawCircle(hx, hy, 70 * s, _p(0xFF8A4A1E)); c.drawCircle(hx, hy, 70 * s, _p(INK, 4 * s))
    c.drawCircle(hx + 8 * s, hy, 42 * s, _p(0xFFE8B058)); c.drawCircle(hx + 8 * s, hy, 42 * s, _p(INK, 3 * s))
    if mode == "lying":
        c.drawLine(hx - 6 * s, hy - 6 * s, hx + 10 * s, hy - 8 * s, _p(INK, 4 * s))
    else:
        c.drawCircle(hx + 18 * s, hy - 12 * s, 6 * s, _p(INK))
    if mode == "roar":
        c.drawOval(skia.Rect.MakeXYWH(hx + 14 * s, hy + 4 * s, 30 * s, 32 * s), _p(0xFF5A1E1E))
    c.drawLine(x - 120 * s, y - 50 * s, x - 190 * s, y - 100 * s, _p(INK, 8 * s))


def bg_zoo(c, t, v):
    _sky(c, v, bottom=H * 0.55)
    _ridges(c, H * 0.55, v, 21)
    dark = _mode(v) != "day"
    for k in range(9):
        _pine(c, W * (0.03 + 0.12 * k), H * 0.58, 190, 0xFF3E8A4E, dark)
    rock = poly([(W * 0.3, H * 0.62), (W * 0.42, H * 0.32), (W * 0.6, H * 0.28), (W * 0.74, H * 0.38), (W * 0.84, H * 0.62)], close=True)
    c.drawPath(rock, _p(0xFFC8A47A)); c.drawPath(rock, _p(INK, 6))
    for k in range(4):
        c.drawLine(W * (0.4 + 0.08 * k), H * (0.4 + 0.03 * k), W * (0.45 + 0.08 * k), H * (0.5 + 0.02 * k), _p(0x55000000, 4))
    _grad(c, (0, H * 0.62, W, H * 0.06), [0xFF3A8AB8, 0xFF2A6A98])   # vallgraven
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.68, W, H * 0.05), _p(0xFFB8A88A))
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.68, W, H * 0.05), _p(INK, 4))
    _floor(c, H * 0.73, 0xFFD8C8A0, 0xFFB8A880)
    mode = "lying" if v.get("lion_lying") else ("roar" if v.get("lion_roar") else "stand")
    _lion(c, W * 0.56, H * 0.3, 0.9, mode, t)


def live_zoo(c, t, v, d):
    if v.get("lion_roar"):
        _waves(c, W * 0.56 + 140, H * 0.3 - 130, t, 0xEEFFFFFF, n=4, r0=60, sp=80, face=1, w=10)
        _waves(c, W * 0.56 + 100, H * 0.3 - 130, t + 0.2, 0xEEFFFFFF, n=4, r0=60, sp=80, face=-1, w=10)
    _dust(c, t, 22, 26, (0, 0, W, H * 0.6), 0x44FFF6D0)


def bg_zoo_path(c, t, v):
    _sky(c, v, bottom=H * 0.45)
    for k in range(10):
        _pine(c, W * (0.0 + 0.11 * k), H * 0.5, 230, 0xFF3E8A4E, _mode(v) != "day")
    for k in range(3):
        sx = W * (0.04 + 0.34 * k)
        _rect(c, sx, H * 0.4, W * 0.24, GY - H * 0.4 - 20, 0xFF4E8A5A, 5, 4)
        roof = poly([(sx - 20, H * 0.4), (sx + W * 0.12, H * 0.3), (sx + W * 0.24 + 20, H * 0.4)], close=True)
        c.drawPath(roof, _p(0xFF8A4A2E)); c.drawPath(roof, _p(INK, 5))
        _rect(c, sx + W * 0.08, GY - 190, 110, 170, 0xFF7A5A3A, 4, 4)
    for k in range(0, W, 60):
        c.drawLine(k, GY - 90, k + 60, GY - 30, _p(0x66A0A8B0, 2)); c.drawLine(k + 60, GY - 90, k, GY - 30, _p(0x66A0A8B0, 2))
    c.drawLine(0, GY - 90, W, GY - 90, _p(0xFF8A8E96, 5))
    _floor(c, GY - 30, 0xFFD8C8A0, 0xFFA8986E)
    _rect(c, W * 0.9, GY - 300, 26, 300, 0xFF8A8E96, 4, 2)
    _rect(c, W * 0.88, GY - 220, 70, 90, 0xFF2A2E36, 3, 6)


def live_zoo_path(c, t, v, d):
    if v.get("wheelbarrow"):
        hv = STASH["v"].get("hero") or {}
        x = W * hv.get("x", 0.5) + 150
        tray = poly([(x, GY - 120), (x + 200, GY - 120), (x + 170, GY - 60), (x + 30, GY - 60)], close=True)
        c.drawPath(tray, _p(0xFF3A8A5A)); c.drawPath(tray, _p(INK, 5))
        c.drawCircle(x + 180, GY - 30, 30, _p(0xFF2A2A2E))
        c.drawLine(x, GY - 110, x - 70, GY - 150, _p(INK, 9))
        c.drawOval(skia.Rect.MakeXYWH(x + 40, GY - 150, 120, 40), _p(0xFFC85A5A))
    if v.get("radio"):
        hv = STASH["v"].get("hero") or {}
        x = W * hv.get("x", 0.5)
        _waves(c, x + 40, GY - 200, t, 0xEEFFE08A, n=3, r0=30, sp=50)


def bg_zoo_stage(c, t, v):
    _sky(c, v, bottom=H * 0.4)
    for r in range(6):
        y = H * (0.18 + 0.05 * r)
        c.drawRect(skia.Rect.MakeXYWH(0, y, W, H * 0.03), _p(0xFFB8BCC4 if r % 2 else 0xFF9AA0AA))
        c.drawLine(0, y, W, y, _p(INK, 3))
    _grad(c, (0, H * 0.48, W, H * 0.16), [0xFF4AB8D8, 0xFF2A8AB8])
    for k in range(10):
        c.drawLine(W * 0.1 * k, H * 0.52 + (k % 3) * 20, W * 0.1 * k + 70, H * 0.52 + (k % 3) * 20, _p(0x88FFFFFF, 3))
    _rect(c, 0, H * 0.64, W, GY - H * 0.64 + 6, 0xFFE8E2D0, 5, 2)
    _floor(c, GY, 0xFFC8BC9A, 0xFFA89C7A)
    for x in (W * 0.08, W * 0.86):
        c.drawLine(x + 50, H * 0.64, x + 50, H * 0.34, _p(INK, 12))
        _rect(c, x, H * 0.18, 100, 170, 0xFF2A2A30, 5, 8)
        for k in range(2):
            c.drawCircle(x + 50, H * 0.18 + 45 + k * 75, 30, _p(0xFF5A5A62)); c.drawCircle(x + 50, H * 0.18 + 45 + k * 75, 30, _p(INK, 4))


def live_zoo_stage(c, t, v, d):
    if v.get("sound_waves"):
        for x, f in ((W * 0.08 + 100, 1), (W * 0.86, -1)):
            _waves(c, x, H * 0.18 + 85, t, 0xEEFFFFFF, n=4, r0=50, sp=90, face=f, w=10)


# ------------------------------------------------------------------ 9. klaffbron
HL, HR, LEAF = W * 0.36, W * 0.64, W * 0.14


def _leaf_angle(v, t, d):
    st = v.get("leaves", "down")
    if st == "up":
        return 72.0
    if st == "rising":
        return 72.0 * E.ease(t / max(d * 0.85, 1))
    return 0.0


def bg_drawbridge(c, t, v):
    _sky(c, v, bottom=H * 0.56)
    _skyline(c, H * 0.56, v, 31, 120, 380)
    _grad(c, (0, H * 0.56, W, H * 0.44), [0xFF3A6A9A, 0xFF1E3A5A] if _night(v) else [0xFF5A9AC8, 0xFF2E6A98])
    for k in range(30):
        rnd = random.Random(k)
        y = H * 0.6 + rnd.uniform(0, H * 0.38)
        c.drawLine(rnd.uniform(0, W), y, rnd.uniform(0, W) % W, y, _p(0x33FFFFFF, 2))
    for x0, x1 in ((0, HL), (HR, W)):
        c.drawRect(skia.Rect.MakeXYWH(x0, GY, x1 - x0, H - GY), _p(0xFF8A8072))
        for k in range(int(x0), int(x1), 60):
            for j in range(int(GY + 40), H, 40):
                c.drawRect(skia.Rect.MakeXYWH(k + (30 if (j // 40) % 2 else 0), j, 56, 36), _p(0x22000000))
        c.drawRect(skia.Rect.MakeXYWH(x0, GY, x1 - x0, 36), _p(0xFF4A4C54)); c.drawLine(x0, GY, x1, GY, _p(INK, 5))
        c.drawLine(x0, GY - 60, x1, GY - 60, _p(0xFFB8BCC4, 8))
        for k in range(int(x0), int(x1), 70):
            c.drawLine(k, GY - 60, k, GY, _p(0xFFB8BCC4, 5))
    # manöverhuset
    hx, hy, hw, hh = W * 0.06, H * 0.36, W * 0.16, GY - H * 0.36
    _rect(c, hx, hy, hw, hh, 0xFFE8D8B8, 6, 4)
    roof = poly([(hx - 20, hy), (hx + hw / 2, hy - 80), (hx + hw + 20, hy)], close=True)
    c.drawPath(roof, _p(0xFF5A6A7A)); c.drawPath(roof, _p(INK, 5))
    c.drawRect(skia.Rect.MakeXYWH(hx + 18, hy + 30, hw - 36, 140), _p(0xFFFFE2A0 if _night(v) else 0xFFB8DCEC))
    c.drawRect(skia.Rect.MakeXYWH(hx + 18, hy + 30, hw - 36, 140), _p(INK, 4))
    if _night(v):
        _glow(c, hx + hw / 2, hy + 100, 260, 0x66FFD890)
    if v.get("truck_far"):
        _car(c, W * 0.8, GY - 4, 0.8, 0xFF3A6AB8, night=_night(v))


def live_drawbridge(c, t, v, d):
    ang = _leaf_angle(v, t, d)
    for hinge, sgn in ((HL, 1), (HR, -1)):
        c.save(); c.translate(hinge, GY); c.rotate(-ang * sgn)
        x0 = 0 if sgn > 0 else -LEAF
        c.drawRect(skia.Rect.MakeXYWH(x0, 0, LEAF, 36), _p(0xFF4A4C54)); c.drawRect(skia.Rect.MakeXYWH(x0, 0, LEAF, 36), _p(INK, 5))
        c.drawRect(skia.Rect.MakeXYWH(x0, -60, LEAF, 8), _p(0xFFD8342A))
        for k in range(0, int(LEAF), 50):
            c.drawLine(x0 + k, -60, x0 + k + 50, 0, _p(0xFFD8342A, 5))
        c.restore()
    c.drawRect(skia.Rect.MakeXYWH(HL - 40, GY, 40, H - GY), _p(0xFF6A6458)); c.drawRect(skia.Rect.MakeXYWH(HR, GY, 40, H - GY), _p(0xFF6A6458))
    if ang > 5:
        on = math.sin(t * 6) > 0
        for x in (HL - 80, HR + 80):
            c.drawLine(x, GY, x, GY - 170, _p(INK, 8))
            c.drawCircle(x, GY - 175, 16, _p(0xFFFF4A3A if on else 0xFF5A1E1E))
            if on:
                _glow(c, x, GY - 175, 80, 0xAAFF3020)
    if STASH["v"].get("shake") and v.get("leaves") == "rising":
        _waves(c, W * 0.14, H * 0.3, t, 0xEEFFFFFF, n=3, r0=40, sp=70)
    hv = STASH["v"].get("hero") or {}
    if hv.get("on") == "control_house":
        hx, hy, hw = W * 0.06, H * 0.36, W * 0.16
        c.save(); c.clipRect(skia.Rect.MakeXYWH(hx + 18, hy + 30, hw - 36, 140))
        pier._draw_fig(c, hx + hw / 2, hy + 220, 0.42, t, hv, face=1)
        c.restore()
    if v.get("control_panel"):
        px, py, pw, ph = W * 0.27, H * 0.28, W * 0.46, H * 0.46
        _rect(c, px, py, pw, ph, 0xFF5A6470, 8, 12)
        c.drawRect(skia.Rect.MakeXYWH(px + 20, py + 20, pw - 40, ph - 40), _p(0xFF3A424E))
        labels = [("RAISE", 0xFF3AB85A), ("LOWER", 0xFFE8B63A), ("HORN", 0xFFD8342A), ("GATES", 0xFF2E86C8)]
        for i, (lb, col) in enumerate(labels):
            bx = px + 80 + i * (pw - 160) / 3
            lit = (i == 0 and v.get("leaves") != "down") or (i == 2 and math.sin(t * 5) > 0.3)
            if lit:
                _glow(c, bx, py + ph * 0.45, 90, _a(col, 0.8))
            c.drawCircle(bx, py + ph * 0.45, 44, _p(col)); c.drawCircle(bx, py + ph * 0.45, 44, _p(INK, 5))
            E.draw_text(c, lb, bx, py + ph * 0.45 + 90, E.font(E.FONT_BOLD, 30), color=0xFFFFFFFF)
        if v.get("radio"):
            _waves(c, px + pw - 60, py + 70, t, 0xEEFFE08A, n=3, r0=24, sp=40)


def bg_river(c, t, v):
    _sky(c, v, bottom=H * 0.5)
    _skyline(c, H * 0.5, v, 41, 100, 260)
    _grad(c, (0, H * 0.5, W, H * 0.5), [0xFF5A9AC8, 0xFF2E6A98])
    c.drawRect(skia.Rect.MakeXYWH(0, H * 0.47, W * 0.4, H * 0.05), _p(0xFF8A8072))
    c.drawRect(skia.Rect.MakeXYWH(W * 0.6, H * 0.47, W * 0.4, H * 0.05), _p(0xFF8A8072))
    for hinge, sgn in ((W * 0.4, 1), (W * 0.6, -1)):
        c.save(); c.translate(hinge, H * 0.47); c.rotate(-72 * sgn)
        x0 = 0 if sgn > 0 else -W * 0.07
        c.drawRect(skia.Rect.MakeXYWH(x0, 0, W * 0.07, 18), _p(0xFF4A4C54)); c.drawRect(skia.Rect.MakeXYWH(x0, -20, W * 0.07, 5), _p(0xFFD8342A))
        c.restore()
    for k in range(40):
        rnd = random.Random(k + 5)
        y = H * 0.55 + rnd.uniform(0, H * 0.45)
        x = rnd.uniform(0, W)
        c.drawLine(x, y, x + 60, y, _p(0x44FFFFFF, 2))


def live_river(c, t, v, d):
    if v.get("boat"):
        bx = W * (0.3 + 0.1 * E.ease(t / max(d, 1)))
        bob = math.sin(t * 2) * 6
        hull = poly([(bx - 80, GY + bob), (bx + 720, GY + bob), (bx + 640, GY + 120 + bob), (bx, GY + 120 + bob)], close=True)
        c.drawPath(hull, _p(0xFFF2F2F2)); c.drawPath(hull, _p(INK, 6))
        c.drawRect(skia.Rect.MakeXYWH(bx - 60, GY + 40 + bob, 760, 16), _p(0xFF2E86C8))
        _rect(c, bx + 440, GY - 200 + bob, 220, 200, 0xFFE8E2D0, 5, 8)
        c.drawRect(skia.Rect.MakeXYWH(bx + 470, GY - 170 + bob, 160, 70), _p(0xFFB8DCEC))
        c.drawLine(bx + 600, GY - 200 + bob, bx + 600, GY - 320 + bob, _p(INK, 8))
        if v.get("sound_waves") or True:
            _waves(c, bx + 610, GY - 300 + bob, t, 0xEEFFFFFF, n=3, r0=30, sp=60, w=8)
    _dust(c, t, 9, 20, (0, H * 0.5, W, H * 0.5), 0x55FFFFFF)


def bg_riverbank(c, t, v):
    _sky(c, v, bottom=H * 0.42)
    _skyline(c, H * 0.42, v, 51, 60, 180)
    _grad(c, (0, H * 0.42, W, H * 0.24), [0xFF5A9AC8, 0xFF2E6A98])
    _grad(c, (0, H * 0.66, W, H * 0.34), [0xFF8AB86A, 0xFF5A8A42])
    for k in range(40):
        rnd = random.Random(k)
        x = rnd.uniform(0, W)
        c.drawLine(x, H * 0.7, x + rnd.uniform(-10, 10), H * 0.64, _p(0xFF4A7A32, 4))


def live_riverbank(c, t, v, d):
    _waves(c, W * 0.05, H * 0.5, t, 0xBBFFFFFF, n=3, r0=30, sp=50, face=-1)


# ------------------------------------------------------------------ 10. brandtornet
CAB = (W * 0.42, H * 0.2, W * 0.16, H * 0.17)


def _tower(c, v, cab=CAB, base=GY, s=1.0, lit=False):
    x, y, w, h = cab
    bx0, bx1 = x - w * 0.25, x + w * 1.25
    for (a, b) in ((bx0, x + w * 0.1), (bx1, x + w * 0.9)):
        c.drawLine(a, base, b, y + h, _p(INK, 12 * s)); c.drawLine(a, base, b, y + h, _p(0xFFB8BCC4, 6 * s))
    for k in range(6):
        f0 = k / 6; f1 = (k + 1) / 6
        ya = base - (base - y - h) * f0; yb = base - (base - y - h) * f1
        la = bx0 + (x + w * 0.1 - bx0) * f0; ra = bx1 + (x + w * 0.9 - bx1) * f0
        lb = bx0 + (x + w * 0.1 - bx0) * f1; rb = bx1 + (x + w * 0.9 - bx1) * f1
        c.drawLine(la, ya, rb, yb, _p(0xFF8A8E96, 4 * s)); c.drawLine(ra, ya, lb, yb, _p(0xFF8A8E96, 4 * s))
        c.drawLine(la, ya, ra, ya, _p(0xFF8A8E96, 4 * s))
    _rect(c, x - 20, y + h - 10, w + 40, 16, 0xFF8A8E96, 3, 2)
    _rect(c, x, y, w, h, 0xFFE8D8B8, 5, 4)
    c.drawRect(skia.Rect.MakeXYWH(x + 10, y + 12, w - 20, h * 0.55), _p(0xFFFFE2A0 if lit else 0xFFB8DCEC))
    for k in range(1, 4):
        c.drawLine(x + 10 + (w - 20) * k / 4, y + 12, x + 10 + (w - 20) * k / 4, y + 12 + h * 0.55, _p(INK, 3))
    roof = poly([(x - 24, y), (x + w / 2, y - h * 0.45), (x + w + 24, y)], close=True)
    c.drawPath(roof, _p(0xFF5A6A7A)); c.drawPath(roof, _p(INK, 5))
    if lit:
        _glow(c, x + w / 2, y + h * 0.35, 220, 0x77FFD890)


def bg_lookout(c, t, v):
    _sky(c, v, bottom=H * 0.62)
    _ridges(c, H * 0.62, v, 61)
    dark = _mode(v) not in ("day",)
    for k in range(14):
        _pine(c, W * (-0.02 + 0.075 * k), H * 0.7, 210 + (k % 3) * 30, 0xFF3E7A4E, dark)
    _grad(c, (0, H * 0.7, W, H * 0.3), [0xFF4E7A3E, 0xFF34542A] if not dark else [0xFF22342A, 0xFF16221C])
    if v.get("type") == "crowd" or v.get("shot") in ("medium", "close"):
        _tower(c, v, (W * 0.38, -H * 0.3, W * 0.24, H * 0.25), GY + 40, 1.6, lit=_night(v))
        if v.get("stairs") or v.get("shot") == "medium":
            for k in range(6):
                y = GY - k * 70
                c.drawLine(W * 0.46, y, W * 0.54, y - 35, _p(0xFF8A8E96, 8)); c.drawLine(W * 0.54, y - 35, W * 0.46, y - 70, _p(0xFF8A8E96, 8))
    else:
        _tower(c, v, lit=_night(v))
    for k in range(10):
        _pine(c, W * (0.02 + 0.105 * k), H * 0.98, 170, 0xFF2F6A40, dark)


def live_lookout(c, t, v, d):
    hv = STASH["v"].get("hero") or {}
    if hv.get("on") == "cab" and v.get("shot", "wide") == "wide":
        x, y, w, h = CAB
        c.save(); c.clipRect(skia.Rect.MakeXYWH(x + 10, y + 12, w - 20, h * 0.55))
        pier._draw_fig(c, x + w / 2, y + h * 0.95, 0.42, t, hv, face=1)
        c.restore()
    if _night(v) and not v.get("storm"):
        _glow(c, CAB[0] + CAB[2] / 2, CAB[1] + 40, 160, _a(0xFFFFD890, 0.4 + 0.1 * math.sin(t * 3)))
    _storm(c, t, v)


def bg_lookout_cab(c, t, v):
    wy0, wy1 = H * 0.1, H * 0.58
    c.save(); c.clipRect(skia.Rect.MakeXYWH(0, wy0, W, wy1 - wy0))
    _sky(c, v, bottom=wy1, top=wy0)
    _ridges(c, wy1, v, 71)
    if v.get("ridge_tower"):
        _tower(c, v, (W * 0.76, H * 0.36, W * 0.035, H * 0.04), H * 0.5, 0.35, lit=True)
    c.restore()
    for k in range(7):
        x = W * k / 6
        c.drawLine(x, wy0, x, wy1, _p(INK, 14)); c.drawLine(x, wy0, x, wy1, _p(0xFFC8A47A, 8))
    _grad(c, (0, 0, W, wy0), [0xFF7A5A3A, 0xFF8A6A48])
    _grad(c, (0, wy1, W, GY - wy1), [0xFFB8885A, 0xFFA87848])
    for k in range(0, W, 90):
        c.drawLine(k, wy1, k, GY, _p(0x33000000, 3))
    _floor(c, GY, 0xFF8A6440, 0xFF6A4A2E)
    # firefinder
    c.drawRect(skia.Rect.MakeXYWH(W * 0.2 - 16, GY - 200, 32, 200), _p(0xFF6A4A2E))
    c.drawOval(skia.Rect.MakeXYWH(W * 0.2 - 150, GY - 240, 300, 70), _p(0xFFE8DCC0)); c.drawOval(skia.Rect.MakeXYWH(W * 0.2 - 150, GY - 240, 300, 70), _p(INK, 5))
    _rect(c, W * 0.8, wy1 + 30, 220, 26, 0xFF6A4A2E, 3, 2)
    _rect(c, W * 0.82, wy1 - 40, 110, 70, 0xFF2A2E36, 4, 6)
    if v.get("stool"):
        close = STASH["v"].get("shot") == "close"
        sx, sy, k = (W * 0.5, H * 0.64, 1.8) if close else (W * 0.5, GY, 1.0)
        top = sy - 80 * k
        _rect(c, sx - 110 * k, top - 20 * k, 220 * k, 24 * k, 0xFF9A6A3A, 4, 4)
        for lx in (-90, -30, 30, 90):
            c.drawLine(sx + lx * k, top, sx + lx * k * 1.1, sy - 30 * k, _p(INK, 9 * k)); c.drawLine(sx + lx * k, top, sx + lx * k * 1.1, sy - 30 * k, _p(0xFF9A6A3A, 5 * k))
            ins = skia.Rect.MakeXYWH(sx + lx * k * 1.1 - 22 * k, sy - 34 * k, 44 * k, 34 * k)
            c.drawRoundRect(ins, 10 * k, 10 * k, _p(0xCC8AE8C8)); c.drawRoundRect(ins, 10 * k, 10 * k, _p(INK, 3 * k))


def live_lookout_cab(c, t, v, d):
    if v.get("ridge_tower"):
        _glow(c, W * 0.76 + W * 0.0175, H * 0.37, 90, _a(0xFFFFD890, 0.6 + 0.3 * math.sin(t * 2.5)))
    if v.get("radio"):
        _glow(c, W * 0.82 + 55, H * 0.58 - 5, 130, _a(0xFF8AE88A, 0.4 + 0.3 * math.sin(t * 11)))
        _waves(c, W * 0.82 + 110, H * 0.58 - 10, t, 0xEEFFE08A, n=3, r0=26, sp=40)
    if v.get("storm"):
        c.save(); c.clipRect(skia.Rect.MakeXYWH(0, H * 0.1, W, H * 0.48))
        _storm(c, t, v, (0, H * 0.1, W, H * 0.4))
        c.restore()
    hv = STASH["v"].get("hero") or {}
    if hv.get("on") == "stool":
        pier._draw_fig(c, W * 0.5, GY - 100, 1.0, t, hv, face=1)


def bg_forest(c, t, v):
    _sky(c, v, bottom=H * 0.5)
    _ridges(c, H * 0.5, v, 81)
    dark = _mode(v) not in ("day", "dawn")
    for row, (base, h, col) in enumerate(((H * 0.58, 200, 0xFF4E8A5E), (H * 0.7, 280, 0xFF3E7A4E), (H * 0.86, 360, 0xFF2F6A40))):
        for k in range(12 - row * 2):
            _pine(c, W * (0.04 + k * (1.0 / (12 - row * 2))) + row * 40, base, h, col, dark)
    _grad(c, (0, H * 0.86, W, H * 0.14), [0xFF5A7A3E, 0xFF3A5A2A] if not dark else [0xFF1E2E22, 0xFF141E18])


def live_forest(c, t, v, d):
    if v.get("wind"):
        rnd = random.Random(3)
        for k in range(40):
            x = (rnd.uniform(0, W) + t * rnd.uniform(160, 300)) % W
            y = rnd.uniform(H * 0.2, H * 0.9) + math.sin(t * 3 + k) * 20
            c.drawOval(skia.Rect.MakeXYWH(x, y, 18, 8), _p(0xCC8AB85A))
        for k in range(6):
            y = H * (0.25 + 0.1 * k)
            x = (t * 400 + k * 330) % (W + 400) - 200
            c.drawLine(x, y, x + 220, y - 10, _p(0x55FFFFFF, 4))
    _storm(c, t, v)


def bg_ridge_tower(c, t, v):
    wy0, wy1 = H * 0.1, H * 0.52
    c.save(); c.clipRect(skia.Rect.MakeXYWH(0, wy0, W, wy1 - wy0))
    _sky(c, v, bottom=wy1, top=wy0)
    _ridges(c, wy1, v, 91)
    _tower(c, v, (W * 0.2, H * 0.32, W * 0.03, H * 0.04), H * 0.46, 0.3, lit=_night(v))
    c.restore()
    for k in range(5):
        x = W * k / 4
        c.drawLine(x, wy0, x, wy1, _p(INK, 14)); c.drawLine(x, wy0, x, wy1, _p(0xFF8A6440, 8))
    _grad(c, (0, 0, W, wy0), [0xFF5A3E2A, 0xFF6A4A32])
    _grad(c, (0, wy1, W, GY - wy1), [0xFF9A6A42, 0xFF8A5E38])
    _floor(c, GY, 0xFF6A4A2E, 0xFF4A3420)
    _glow(c, W * 0.5, H * 0.3, 700, 0x33FFD890 if _night(v) else 0x00000000)
    # tally-arket på väggen
    close = STASH["v"].get("shot") == "close"
    tx, ty, tw, th = (W * 0.27, H * 0.24, W * 0.46, H * 0.48) if close else (W * 0.68, H * 0.56, W * 0.26, H * 0.2)
    if v.get("tally"):
        _rect(c, tx, ty, tw, th, 0xFFFBF6E8, 5, 6)
        E.draw_text(c, "VOICES", tx + tw / 2, ty + th * 0.16, E.font(E.FONT_BOLD, int(th * 0.11)), color=INK)
        m = re.search(r"(\d+)", str(STASH["v"].get("sign", "") or ""))
        n = int(m.group(1)) if m else (21 if _night(v) else 31)
        gw = tw / 8.5
        for i in range(n):
            g, r = i // 5, i % 5
            col_i, row_i = g % 7, g // 7
            gx = tx + gw * 0.6 + col_i * gw * 1.1; gy = ty + th * 0.3 + row_i * th * 0.3
            if r < 4:
                c.drawLine(gx + r * gw * 0.18, gy, gx + r * gw * 0.18, gy + th * 0.2, _p(0xFF2A2A2E, max(3, tw * 0.008)))
            else:
                c.drawLine(gx - gw * 0.08, gy + th * 0.16, gx + gw * 0.62, gy + th * 0.04, _p(0xFFD8342A, max(3, tw * 0.008)))


def live_ridge_tower(c, t, v, d):
    if _night(v):
        _glow(c, W * 0.2 + W * 0.015, H * 0.34, 70, _a(0xFFFFD890, 0.5 + 0.3 * math.sin(t * 2)))


# ------------------------------------------------------------------ registrering
PLACES = {"dispatch": bg_dispatch, "dispatch_roof": bg_dispatch_roof, "garage": bg_garage, "street": bg_street,
          "truckstop": bg_truckstop, "cab": bg_cab, "highway": bg_highway, "diner": bg_diner, "diner_lot": bg_diner_lot,
          "diner_back": bg_diner_back, "zoo": bg_zoo, "zoo_path": bg_zoo_path, "zoo_stage": bg_zoo_stage,
          "drawbridge": bg_drawbridge, "river": bg_river, "riverbank": bg_riverbank, "lookout": bg_lookout,
          "lookout_cab": bg_lookout_cab, "forest": bg_forest, "ridge_tower": bg_ridge_tower}
LIVE = {"dispatch": live_dispatch, "dispatch_roof": live_dispatch_roof, "garage": live_garage, "truckstop": live_truckstop,
        "cab": live_cab, "highway": live_highway, "diner": live_diner, "diner_lot": live_diner_lot, "diner_back": live_diner_back,
        "zoo": live_zoo, "zoo_path": live_zoo_path, "zoo_stage": live_zoo_stage, "drawbridge": live_drawbridge,
        "river": live_river, "riverbank": live_riverbank, "lookout": live_lookout, "lookout_cab": live_lookout_cab,
        "forest": live_forest, "ridge_tower": live_ridge_tower}
SIL_K = {"lookout": 0.42, "highway": 0.75, "forest": 0.8, "drawbridge": 0.85, "zoo": 0.85, "riverbank": 0.85}
INDOOR = {"dispatch", "garage", "cab", "diner", "lookout_cab", "ridge_tower"}


def _sign_overlay(c, t, d, v):
    s = v.get("sign")
    if not s:
        return
    a = E.prog(t, 0.15, 0.4)
    if a <= 0:
        return
    c.saveLayerAlpha(None, int(255 * a))
    up = str(s).upper()
    if up.startswith("VERDICT"):
        f = _bangers(92)
        tw = E.text_w(up, f)
        r = skia.Rect.MakeXYWH(W / 2 - tw / 2 - 50, 40, tw + 100, 128)
        c.drawRoundRect(r.makeOffset(8, 10), 14, 14, _p(0x66000000))
        c.drawRoundRect(r, 14, 14, _p(0xFFD8342A)); c.drawRoundRect(r, 14, 14, _p(INK, 7))
        E.draw_text(c, up, W / 2, 40 + 100, f, color=0xFFFFFFFF)
    elif re.match(r"^DAY \d+$", up):
        f = E.font(E.FONT_BLACK, 64)
        E.box(c, 50, 46, E.text_w(up, f) + 60, 100, 0xFF111111, 0, 14)
        E.draw_text(c, up, 80, 118, f, color=0xFFFFFFFF, align="left")
    else:
        big = v.get("shot") == "close"
        _sign(c, W / 2, 44, s, size=64 if big else 46, bg=0xFFFFF4D8 if big else 0xFFF2E6C8, maxw=W * 0.72)
    c.restore()


def _wrap(orig):
    def scene(c, t, d, v):
        loc = v.get("location")
        if loc not in PLACES:
            return orig(c, t, d, v)
        v2 = dict(v)
        v2.pop("sign", None)
        if loc == "diner" and v.get("door_open"):
            v2["shot"] = "wide"
        if loc in GLASS_LOCS:
            STASH["z"] = list(v.get("zombies_in") or []); v2["zombies_in"] = []
        else:
            STASH["z"] = []
        STASH["v"] = v; STASH["d"] = d
        try:
            orig(c, t, d, v2)
        finally:
            pass
        _sign_overlay(c, t, d, v)
    scene._ls21 = True
    return scene


_pier_live = None


def _live(c, t, px, prop):
    v = pier.CTX.get("v") or {}
    loc = v.get("location")
    if loc in LIVE:
        try:
            LIVE[loc](c, t, v, pier.CTX.get("d", 6.0))
        except Exception as e:
            print("ls21 live", loc, e)
        return
    return _pier_live(c, t, px, prop)


def _card(orig):
    def fn(c, t, d, v):
        kind = v.get("card")
        if kind not in ("problem", "end"):
            return orig(c, t, d, v)
        _grad(c, (0, 0, W, H), [0xFFF6EEDC, 0xFFEADCC0])
        rnd = random.Random(2)
        for k in range(160):
            c.drawCircle(rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(1, 3), _p(0x14000000))
        a = E.prog(t, 0, 0.35) * (1 - E.prog(t, d - 0.3, 0.3))
        sub = str(v.get("sub", ""))
        c.saveLayerAlpha(None, int(255 * max(0, min(1, a))))
        sc = 1 + 0.04 * E.ease(t / max(d, 1))
        c.save(); c.translate(W / 2, H / 2); c.scale(sc, sc); c.translate(-W / 2, -H / 2)
        if kind == "problem":
            m = re.match(r"^(#\d+)\s*[–-]\s*(.+)$", sub)
            num, job = (m.group(1), m.group(2)) if m else ("", sub)
            E.draw_text(c, str(v.get("label", "NIGHT SHIFT RANKING")), W / 2, H * 0.2, E.font(E.FONT_BOLD, 44), color=0xFF8A6A4A)
            f = _bangers(330)
            E.draw_text(c, num, W / 2 + 8, H * 0.6 + 10, f, color=0xFF1A1A1A)
            E.draw_text(c, num, W / 2, H * 0.6, f, color=0xFFD8342A)
            fj = _bangers(110)
            tw = E.text_w(job.upper(), fj)
            r = skia.Rect.MakeXYWH(W / 2 - tw / 2 - 40, H * 0.68, tw + 80, 140)
            c.drawRoundRect(r, 12, 12, _p(0xFF1A1A1A))
            E.draw_text(c, job.upper(), W / 2, H * 0.68 + 112, fj, color=0xFFFFFFFF)
        else:
            f = _bangers(120)
            lines = E.wrap(sub.upper(), f, W * 0.8)
            for i, ln in enumerate(lines):
                E.draw_text(c, ln, W / 2, H * 0.42 + i * 130, f, color=0xFF1A1A1A)
            E.draw_text(c, str(v.get("next", "NEXT SHIFT: THE ICE RINK")), W / 2, H * 0.8, E.font(E.FONT_BOLD, 52), color=0xFFD8342A)
        c.restore(); c.restore()
    return fn


def _item_binoculars(c, hx, hy, s, lw):
    for k in (0, 1):
        c.drawRoundRect(skia.Rect.MakeXYWH(hx - s * 0.02 + k * s * 0.07, hy - s * 0.05, s * 0.06, s * 0.1), s * 0.02, s * 0.02, _p(0xFF2A2A2E))


def _item_keys(c, hx, hy, s, lw):
    c.drawCircle(hx + s * 0.02, hy, s * 0.03, _p(INK, lw * 0.4))
    c.drawRect(skia.Rect.MakeXYWH(hx + s * 0.03, hy - s * 0.01, s * 0.08, s * 0.02), _p(0xFFE8C23A))


def _item_spatula(c, hx, hy, s, lw):
    c.drawLine(hx, hy + s * 0.04, hx + s * 0.16, hy - s * 0.12, _p(INK, lw * 0.6))
    c.drawRect(skia.Rect.MakeXYWH(hx + s * 0.13, hy - s * 0.2, s * 0.08, s * 0.08), _p(0xFFB8BCC4))


def _item_box(c, hx, hy, s, lw):
    E.box(c, hx - s * 0.05, hy - s * 0.12, s * 0.2, s * 0.16, 0xFFC49A5C, lw * 0.5, 3)


def enable():
    global _pier_live
    if getattr(pier, "_ls21", False):
        return
    pier.PLACES.update(PLACES)
    E.BG.update(PLACES)
    _pier_live = pier._live
    E.EXTRA_PROPS["pier_live"] = _live
    for k, f in (("binoculars", _item_binoculars), ("keys", _item_keys), ("spatula", _item_spatula), ("box", _item_box)):
        E.EXTRA_ITEMS.setdefault(k, f)
    E.SM["scene"] = _wrap(E.SM["scene"])
    E.SM["daycard"] = _card(E.SM["daycard"])
    _orig_sil = pier._sil_size

    def _sil(s):
        loc = (pier.CTX.get("v") or {}).get("location")
        if loc in SIL_K and not pier.CTX.get("crowd"):
            import charstyle
            return s * charstyle.SCALE * SIL_K[loc]
        return _orig_sil(s)
    pier._sil_size = _sil
    try:
        import atmos
        for k in PLACES:
            if k in INDOOR:
                atmos.MOOD[k] = dict(light=(0.5, 0.3), lc=0xFFFFE6B8, dark=0.3, mood=None, fg=None)
            else:
                atmos.MOOD[k] = dict(light=(0.5, 0.45), lc=0xFFFFD08A, dark=0.28, mood=None, fg=None)
                atmos.OUTDOOR.add(k)
        old = atmos._bg_key

        def _bg_key(v):
            return old(v) + json.dumps({k: v.get(k) for k in (
                "glass_wall", "breaker", "levels", "booth", "ramp", "key_cabinet", "trucks", "logbook", "control_house",
                "moat", "lion_lying", "lion_roar", "speakers", "boat", "tower_full", "stairs", "stool", "ridge_tower",
                "tally", "window_dead", "jukebox", "neon", "door_open", "wheelbarrow", "truck_far", "storm", "lightning",
                "tower_legs", "edge", "type", "shot")}, default=str)
        atmos._bg_key = _bg_key
    except Exception as e:
        print("ls21 atmos:", e)
    pier._ls21 = True
