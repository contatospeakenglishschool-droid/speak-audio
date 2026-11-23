import json, subprocess, sys, glob, os
R, S = sys.argv[1], sys.argv[2]
units = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else None
plan = json.load(open("plan.json"))
for n, it in plan.items():
    if units and int(n) not in units: continue
    for kind in ("Student's book", "Teacher's book"):
        src = glob.glob(f"{R}/{kind}/A1 Essentials {int(n):02d} - *.pdf")[0]
        args = [f"{S}/venv/bin/python", f"{S}/speak-audio/engine/warmup_fix.py", src, "final/" + os.path.basename(src)]
        if "sort" in it: args += ["--sort", "|".join(it["sort"])]
        if "perm" in it: args += ["--perm", ",".join(map(str, it["perm"]))]
        print(subprocess.run(args, capture_output=True, text=True).stdout.strip() or "ERR " + src)
