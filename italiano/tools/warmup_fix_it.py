# wrapper: run engine/warmup_fix.py with Italian page detection (repo file untouched)
import sys, os
eng = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "engine")
sys.path.insert(0, eng)
src = open(os.path.join(eng, "warmup_fix.py")).read().replace('"Warm-up" in', '"Riscaldamento" in')
assert '"Riscaldamento" in' in src
g = {"__name__": "wf", "__file__": os.path.join(eng, "warmup_fix.py")}
exec(compile(src, "warmup_fix.py", "exec"), g)
g["main"]()
