import re, json, sys
def key(w): return re.sub(r"^(a|an|the)\s+", "", w.lower())
res = {}
for n in range(1, 37):
    L = open(f"peek/t{n:02d}.txt").read().splitlines()
    gi = next((i for i, l in enumerate(L) if re.match(r"^\s*A\s{3,}B\s{3,}C", l)), None)
    if gi is None: continue
    bl = [i for i, l in enumerate(L[:gi]) if "·" in l and "Look" not in l and "Olhe" not in l and "photo" not in l.lower()]
    bank = " ".join(L[i].strip() for i in range(bl[0], gi)) if bl else ""
    bank = [w.strip() for w in bank.split("·") if w.strip()]
    if len(bank) != 8: print(n, "bank?", bank); continue
    # grid words: split row lines by 3+ spaces
    def row(l): return [x.strip() for x in re.split(r"\s{3,}", l.strip()) if x.strip()]
    r1 = row(L[gi+1]); ei = next(i for i in range(gi+1, len(L)) if re.match(r"^\s*E\s{3,}F", L[i])); r2 = row(L[ei+1])
    grid = r1 + r2
    srt = sorted(bank, key=key)
    same_set = sorted(grid) == sorted(bank)
    fixed = sum(a == b for a, b in zip(srt, grid))
    status = ("OK" if bank == srt and fixed <= 1 else "SORT" if fixed <= 1 else "SHUFFLE"+("+SORT" if bank != srt else ""))
    res[n] = dict(bank=bank, grid=grid, sorted=srt, status=status, fixed=fixed, same=same_set)
    print(f"{n:02d} {status:7s} fixed={fixed} set_ok={same_set} alpha={bank==srt}")
json.dump(res, open("analysis.json", "w"), indent=1)
