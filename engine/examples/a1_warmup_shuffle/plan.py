import json, random, re
A = json.load(open("analysis.json"))
def key(w): return re.sub(r"^(a|an|the)\s+", "", w.lower())
GROUPS = {35: [[0, 1, 6], [2, 3, 4, 5, 7]]}  # keep the TB yes/no answers per letter
plan = {}
for n, d in A.items():
    n = int(n); st = d["status"]
    if n in (10, 14): st = "SHUFFLE+SORT"
    if n == 19: st = "SHUFFLE"
    if st == "OK": continue
    item = {}
    if "SORT" in st: item["sort"] = d["sorted"]
    if "SHUFFLE" in st:
        rank = {w: i for i, w in enumerate(d["sorted"])}
        rnd = random.Random(1000 + n)
        while True:
            if n in GROUPS:
                perm = list(range(8))
                for g in GROUPS[n]:
                    sh = g[:]; rnd.shuffle(sh)
                    for a, b in zip(g, sh): perm[a] = b
            else:
                perm = list(range(8)); rnd.shuffle(perm)
            r = [rank[d["grid"][i]] for i in perm]
            if all(r[j] != j for j in range(8)) and all(r[j + 1] != r[j] + 1 and r[j + 1] != r[j] - 1 for j in range(7)):
                break
        item["perm"] = perm
        item["new_grid"] = [d["grid"][i] for i in perm]
    plan[n] = item
    print(n, st, item.get("new_grid", d["grid"]))
json.dump(plan, open("plan.json", "w"), indent=1)
