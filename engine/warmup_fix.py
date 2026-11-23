# Fix the Warm-up photo grid of a published (locked) A1 unit, in place on page 1:
#   --sort  "w1|w2|..."  : cover the word bank with the same words in alphabetical order (overlay, same CSS)
#   --perm  "5,2,7,..."  : move the 8 photo cards (photo + red answer word in the TB) so that new card j shows old card perm[j]
# The rest of the PDF is untouched; the output is locked again (AES-256, print + annotate).
# usage: warmup_fix.py IN.pdf OUT.pdf [--sort "..."] [--perm "..."]
import argparse, io, re, secrets, sys, os
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as P
from pypdf.generic import ContentStream, NameObject, DecodedStreamObject

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import speak_engine as E
from weasyprint import HTML

NUM = r"-?[\d.]+"
IMG = re.compile(rf"({NUM}) ({NUM}) ({NUM}) ({NUM}) re\nW\nn\nq\n(/\S+ gs)\n1 0 0 1 ({NUM}) ({NUM}) cm\nq\n({NUM}) 0 0 ({NUM}) 0 ({NUM}) cm\n/(\S+) Do")
TXT = re.compile(rf"BT\n1 0 0 -1 ({NUM}) ({NUM}) Tm\n.*?ET\n", re.S)
RED = "0.701961 0.14902 0.117647 rg"
BANK_BG = "0.901961 0.941176 0.94902 rg"


def f(x):
    return f"{x:.6f}".rstrip("0").rstrip(".")


def cards(c):
    out = [m for m in IMG.finditer(c) if abs(float(m.group(3)) - 156.606824) < 2]
    if len(out) != 8:
        raise SystemExit(f"expected 8 photo cards, found {len(out)}")
    return out


def move_cards(c, perm):
    ms = cards(c)
    geo = [(float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4))) for m in ms]
    # red answer words under each card (TB only): whole BT...ET blocks
    words = {}
    for m in TXT.finditer(c):
        x, y = float(m.group(1)), float(m.group(2))
        if RED not in c[max(0, m.start() - 120):m.start()]:
            continue
        for i, (cx, cy, w, h) in enumerate(geo):
            if cx <= x <= cx + w and cy + h <= y <= cy + h + 45:
                words.setdefault(i, []).append(m)
    edits = []  # (start, end, text)
    for j, m in enumerate(ms):
        i = perm[j]
        s = ms[i]
        cx_i, cy_i = geo[i][0], geo[i][1]
        cx_j, cy_j = geo[j][0], geo[j][1]
        tx = float(s.group(6)) - cx_i + cx_j
        ty = float(s.group(7)) - cy_i + cy_j
        new = (f"{m.group(1)} {m.group(2)} {m.group(3)} {m.group(4)} re\nW\nn\nq\n{m.group(5)}\n1 0 0 1 {f(tx)} {f(ty)} cm\nq\n"
               f"{s.group(8)} 0 0 {s.group(9)} 0 {s.group(10)} cm\n/{s.group(11)} Do")
        edits.append((m.start(), m.end(), new))
    # words: the text of card perm[j] is written in place of the text of card j (inside j's clip)
    def shifted(m, dx, dy):
        return re.sub(rf"1 0 0 -1 ({NUM}) ({NUM}) Tm", lambda t: f"1 0 0 -1 {f(float(t.group(1)) + dx)} {f(float(t.group(2)) + dy)} Tm", m.group(0))
    if words:
        assert sorted(words) == list(range(8)), f"red words found for cards {sorted(words)}"
        for j in range(8):
            i = perm[j]
            dx, dy = geo[j][0] - geo[i][0], geo[j][1] - geo[i][1]
            new = "".join(shifted(m, dx, dy) for m in words[i])
            for k, m in enumerate(words[j]):
                edits.append((m.start(), m.end(), new if k == 0 else ""))
    for a, b, t in sorted(edits, reverse=True):
        c = c[:a] + t + c[b:]
    return c, len(words)


def bank_box(c):
    first_card_y = float(cards(c)[0].group(2))
    for m in re.finditer(re.escape(BANK_BG) + r"\n(.*?)\n(?:f|f\*)\n", c, re.S):
        nums = [float(v) for v in re.findall(NUM, m.group(1))]
        if " re" in m.group(1):  # background drawn as the border-box rectangle
            x0, y0, x1, y1 = nums[0], nums[1], nums[0] + nums[2], nums[1] + nums[3]
        else:
            xs, ys = nums[0::2], nums[1::2]
            x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
        if y1 < first_card_y and x1 - x0 > 400 and y0 > 300:
            return (x0, y0, x1, y1)
    raise SystemExit("word bank not found")


def overlay(box, words):
    x0, y0, x1, y1 = box
    b = 0  # the background rectangle is the border-box
    text = " &nbsp;·&nbsp; ".join(w.replace(" ", "&nbsp;") for w in words)
    html = f"""<html><head><style>{E.CSS}
.fix {{ position: absolute; left: {x0 - b}px; top: {y0 - b}px; width: {x1 - x0 + 2 * b}px; height: {y1 - y0 + 2 * b}px;
        box-sizing: border-box; margin: 0; }}</style></head><body><div class="bank fix">{text}</div></body></html>"""
    return PdfReader(io.BytesIO(HTML(string=html).write_pdf())).pages[0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp"); ap.add_argument("out")
    ap.add_argument("--sort"); ap.add_argument("--perm")
    a = ap.parse_args()
    r = PdfReader(a.inp)
    if r.is_encrypted:
        r.decrypt("")
    pi = next(i for i, p in enumerate(r.pages) if "Warm-up" in (p.extract_text() or ""))
    page = r.pages[pi]
    c = page.get_contents().get_data().decode("latin1")
    info = []
    box = bank_box(c) if a.sort else None
    if a.perm:
        perm = [int(v) for v in a.perm.split(",")]
        assert sorted(perm) == list(range(8))
        c, nw = move_cards(c, perm)
        info.append(f"cards moved (red words: {nw})")
    w = PdfWriter()
    for i, p in enumerate(r.pages):
        w.add_page(p)
    pg = w.pages[pi]
    if a.perm:
        st = DecodedStreamObject(); st.set_data(c.encode("latin1"))
        pg[NameObject("/Contents")] = w._add_object(st)
    if a.sort:
        pg.merge_page(overlay(box, a.sort.split("|")))
        st = DecodedStreamObject(); st.set_data(pg.get_contents().get_data())  # pin the merged stream (encrypt drops it otherwise)
        pg[NameObject("/Contents")] = w._add_object(st)
        info.append(f"bank sorted at {tuple(round(v) for v in box)}")
    meta = {k: v for k, v in (r.metadata or {}).items() if isinstance(v, str)}
    w.add_metadata(meta)
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS
    w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), permissions_flag=perms, algorithm="AES-256")
    w.write(a.out)
    print(os.path.basename(a.out), f"page {pi + 1}:", "; ".join(info))


if __name__ == "__main__":
    main()
