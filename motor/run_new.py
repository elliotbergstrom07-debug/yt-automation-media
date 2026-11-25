"""Day After Court / The Long If: CHAN=dac|tli python3 run_new.py long|thumbs manus.json ut/x
Laddar qmday + chanstyle (kanalens hjälte, platser, daycard/label)."""
import os, sys, json
man = json.load(open(sys.argv[2]))
os.environ.setdefault("CHAN", "tli" if man.get("channel") == "The Long If" else "dac")
import engine, qmday, chanstyle, produce, dacli2
import importlib as _il
# 23 nov: tli1123 (Denver i dag) – för 23 nov-manuset laddas bara den (inga 1850-platser), annars båda
_tli = ('tli1123',) if '2026-11-23' in os.path.basename(sys.argv[2]) else ('tli1850', 'tli1123')
for _n in (('dac20', 'dac21', 'dac25') if os.environ['CHAN'] == 'dac' else _tli):   # 20 nov: dagens platsmoduler
    try:
        _m = _il.import_module(_n)
        if hasattr(_m, 'enable'): _m.enable()
    except ImportError as _e:
        print('platsmodul saknas:', _n, _e)
mode, manus, out = sys.argv[1], sys.argv[2], sys.argv[3]
if mode == "thumbs":
    produce.make_thumbs(man, out)
else:
    produce.produce(manus, out)
