import sys, json, os
MAN, OUT = sys.argv[1], sys.argv[2]
sys.argv = ["x", "none", "a", "b"]
exec(open("run_qm.py").read().split("mode, manus, out")[0])
import engine as E, skia
m = json.load(open(MAN)); os.makedirs(OUT, exist_ok=True)
for i, s_ in enumerate(m["scenes"]):
    v = s_["visual"]; s = skia.Surface(E.W, E.H); c = s.getCanvas(); c.clear(0xFF000000)
    try: E.QM[v["type"]](c, 2.5, 5.0, v)
    except Exception as e: print(i, "FEL", repr(e)); continue
    s.makeImageSnapshot().resize(640, 360).save(f"{OUT}/s{i:02d}.png")
print("ok")
