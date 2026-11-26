"""Last Shift: python3 run_ls.py long|short manus.json ut
Laddar vattenparken (waterpark.py) och stor-huvud-stilen (charstyle.py, ägarens beslut 13 nov):
större figurer med uttrycksfulla ansikten + scentyperna "closeup" och "crowd"."""
import sys
import engine, waterpark, airport, megastore, charstyle, produce, shorts
import importlib as _il
for _n in ('ferry', 'mine', 'bakery', 'pier', 'ls21', 'prison', 'hotel'):   # 20 nov: valfria platsmoduler (saknas de hoppas de över)
    try:
        _m = _il.import_module(_n)
        if hasattr(_m, 'enable'): _m.enable()
    except ImportError as _e:
        print('platsmodul saknas:', _n, _e)
charstyle.enable()
import atmos; atmos.enable(); atmos.enable_qm()
import motion; motion.enable()   # 16 nov: figurerna gör saker (ägarens order: gör videorna intressanta)
import hospital; hospital.enable()   # 16 nov: sjukhuset (våning 9)
try:
    import prison; prison.enable_late()   # 25 nov: fängelset (skylt-overlay)
except ImportError as _e:
    print('platsmodul saknas: prison', _e)
import json as _mj, os as _mo
if len(sys.argv) > 2 and sys.argv[1] == "long":
    _m = _mj.load(open(sys.argv[2])); _r = motion.auto_actions(_m)
    sys.argv[2] = "/tmp/" + _mo.path.basename(sys.argv[2]).replace(".json", ".motion.json"); _mj.dump(_m, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
    print("motion: %d handlingar satta, täckning %.0f%% -> %.0f%%" % (_r[0], _r[1] * 100, _r[2] * 100))   # 13 nov 15:02: stämning och djup (ägarens beslut)
mode, manus, out = sys.argv[1], sys.argv[2], sys.argv[3]
if mode == "thumbs":   # 3 miniatyrer: run_*.py thumbs manus.json ut/x -> ut/x.A/B/C.png
    import json as _j; produce.make_thumbs(_j.load(open(manus)), out)
elif mode == "long":
    produce.produce(manus, out)
else:
    shorts.build_short(manus, out if out.endswith(".mp4") else out + ".mp4")
