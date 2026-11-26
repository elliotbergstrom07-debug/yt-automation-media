import sys, json, os
MAN, IDX, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
sys.argv = ["run_ls.py", "none", "x", "y"]
src = open("run_ls.py").read().split("import json as _mj")[0]
exec(compile(src, "run_ls_setup", "exec"))
import engine as E, skia
m = json.load(open(MAN))
os.makedirs(OUT, exist_ok=True)
idx = range(len(m["scenes"])) if IDX == "all" else [int(x) for x in IDX.split(",")]
for i in idx:
    v = m["scenes"][i]["visual"]
    s = skia.Surface(E.W, E.H); c = s.getCanvas(); c.clear(0xFF000000)
    fn = E.SM.get(v.get("type"))
    try:
        fn(c, 1.2, 5.0, v)
    except Exception as e:
        print(i, "FEL", e); continue
    img = s.makeImageSnapshot().resize(640, 360)
    img.save(f"{OUT}/s{i:02d}.png")
print("ok")
