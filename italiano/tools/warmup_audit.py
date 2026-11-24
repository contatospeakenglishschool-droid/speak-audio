import sys, re, subprocess, glob, os, html, unicodedata, json
ART = re.compile(r"^(il|lo|la|i|gli|le|un|uno|una)\s+|^(l'|un'|l’)", re.I)
def key(w):
    w = ART.sub("", w.strip())
    return unicodedata.normalize("NFD", w).encode("ascii", "ignore").decode().lower()
def lines(pdf, page):
    x = subprocess.run(["pdftotext", "-f", str(page), "-l", str(page), "-bbox-layout", pdf, "/dev/stdout"], capture_output=True, text=True).stdout
    out = []
    for m in re.finditer(r'<line xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</line>', x, re.S):
        ws = [html.unescape(w) for w in re.findall(r'>([^<]+)</word>', m.group(5))]
        out.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), " ".join(ws)))
    return out
def audit(pdf):
    for page in (1, 2, 3):
        L = lines(pdf, page)
        pos = {}
        for x, y, _, t in L:
            if len(t) == 1 and t in "ABCDEFGH": pos.setdefault(t, []).append((x, y))
        let = None
        for ax, ay in pos.get("A", []):
            r1 = {c: next((p for p in pos.get(c, []) if abs(p[1] - ay) < 3), None) for c in "BCD"}
            if None in r1.values(): continue
            ey = [p for p in pos.get("E", []) if 60 < p[1] - ay < 160]
            if not ey: continue
            ey = ey[0][1]
            r2 = {c: next((p for p in pos.get(c, []) if abs(p[1] - ey) < 3), None) for c in "EFGH"}
            if None in r2.values(): continue
            let = {"A": (ax, ay), **r1, **r2}; break
        if let and "Riscaldamento" in " ".join(t for *_, t in L):
            break
    else:
        return None
    # rows check: A-D same y
    if abs(let["A"][1] - let["D"][1]) > 3 or abs(let["E"][1] - let["H"][1]) > 3:
        return None
    ans = []
    for c in "ABCDEFGH":
        lx, ly = let[c]
        parts = [(y, x, t) for x, y, x2, t in L if ly + 40 < y < ly + 105 and lx - 10 <= x <= lx + 115 and t not in "ABCDEFGH"]
        ans.append(" ".join(t for _, _, t in sorted(parts)))
    # bank: lines between instruction (sub A) and row A letters, containing '·'
    top = let["A"][1]
    bank_lines = [(y, x, t) for x, y, x2, t in L if top - 80 < y < top - 2 and ("·" in t or True)]
    bank_lines = [b for b in sorted(bank_lines) if "min" not in b[2] or "·" in b[2]]
    # keep the contiguous block just above the grid
    blk = []
    for y, x, t in reversed(bank_lines):
        if blk and blk[-1][0] - y > 16: break
        blk.append((y, x, t))
    bank_txt = " ".join(t for _, _, t in sorted(blk))
    bank = [w.strip() for w in bank_txt.split("·") if w.strip()]
    return bank, ans
def _main():
  res = {}
  for pdf in sys.argv[1:]:
      r = audit(pdf)
      name = os.path.basename(pdf)[:-7]
      if r is None:
          res[name] = None; print(f"{name}: no A-H grid"); continue
      bank, ans = r
      issues = []
      if [key(w) for w in bank] != sorted(key(w) for w in bank): issues.append("bank not alphabetical")
      sb = sorted(bank, key=key)
      try:
          p = [sb.index(a) for a in ans]
      except ValueError:
          issues.append(f"answer/bank mismatch"); p = None
      if p:
          if any(p[k] == k for k in range(8)): issues.append("photo in same position as word")
          if any(p[k + 1] == p[k] + 1 for k in range(7)): issues.append("consecutive photos in bank order")
      res[name] = dict(bank=bank, ans=ans, issues=issues)
      print(f"{name}: {'OK' if not issues else '; '.join(issues)}")
      if issues: print("   bank:", " | ".join(bank)); print("   photos:", " | ".join(ans))
  json.dump(res, open(os.environ.get("OUT", "/dev/null"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    _main()
