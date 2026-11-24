import json, random, sys
sys.path.insert(0, sys.argv[1])
from audit_wu import key
R = json.load(open(sys.argv[2]))
FIXED = {"A2 Ponte 31 - Un po' di storia -": {0, 1, 2, 3}, "A1 Essenziale 01 - Piacere -": {6}, "A1 Essenziale 07 - In città -": {5}, "A1 Essenziale 11 - Il fine settimana -": {0, 7}}
def ok(q): return all(q[j] != j for j in range(8)) and all(q[j+1] != q[j] + 1 for j in range(7))
plan = {}
for name, r in R.items():
    if not r or not r["issues"] or "Ripasso" in name: continue
    bank, ans = r["bank"], r["ans"]
    sb = sorted(bank, key=key)
    q0 = [sb.index(a) for a in ans]
    perm = None
    if not ok(q0):
        fx = FIXED.get(name, set()); rnd = random.Random(name)
        for t in range(400000):
            if t == 200000 and fx: print("  !! letters cannot stay fixed:", name); fx = set()
            free = [i for i in range(8) if i not in fx]; sh = free[:]; rnd.shuffle(sh)
            p = list(range(8)); 
            for a, b in zip(free, sh): p[a] = b
            if p != list(range(8)) and ok([q0[i] for i in p]): perm = p; break
        else: raise SystemExit("no perm for " + name)
    plan[name] = dict(sort="|".join(sb), perm=None if perm is None else ",".join(map(str, perm)),
                      new=[ans[i] for i in (perm or range(8))])
    print(name, "sort only" if perm is None else perm)
json.dump(plan, open(sys.argv[3], "w"), ensure_ascii=False, indent=1)
