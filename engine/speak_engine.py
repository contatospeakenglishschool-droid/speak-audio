# Speak! Essentials - shared layout engine (Student Book + Teacher's Guide).
# Usage in a unit script:
#   import sys; sys.path.insert(0, ENGINE_DIR); from speak_engine import *
#   setup(band="A1 · UNIT 21", audio_json="audio_u21.json", img_dir="u21img")
#   then define PHOTOS (via set_photos) and build(teacher) using Book.
# One source -> Student Book and Teacher's Guide with identical page layouts.
import base64, glob, os, sys
from weasyprint import HTML

TEAL, TEAL_D, AQUA, SAND, INK = "#176074", "#0f4a5a", "#77acb5", "#cbbca0", "#1f2528"
RED = "#B3261E"
IMG_DIR = "img"
BAND = "A1"

PHOTOS = []

import qrcode, io as _io
import json as _json, os as _os
AUDIO = {}
def setup(band, audio_json=None, img_dir="img"):
    """band: text after 'SPEAK! ESSENTIALS · ', e.g. 'A1 · UNIT 21' or 'A1 · REVIEW 3'."""
    global BAND, IMG_DIR
    BAND, IMG_DIR = band, img_dir
    AUDIO.clear()
    if audio_json and _os.path.exists(audio_json):
        AUDIO.update(_json.load(open(audio_json)))
def aurl(k):
    if k not in AUDIO: return ""
    v = AUDIO[k]
    return v if v.startswith("http") else f"https://drive.google.com/file/d/{v}/view"
def qr(k):
    if k not in AUDIO: return ""
    img = qrcode.make(aurl(k), box_size=6, border=1)
    b = _io.BytesIO(); img.save(b, format="PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode()
def audiocard(keys):
    cells = "".join(f'<a class="qa" href="{aurl(k)}">{('<img src="'+qr(k)+'">') if k in AUDIO else '<span class="qph">QR</span>'}<span><b>&#9654; PLAY</b><br>AUDIO {k}</span></a>' for k in keys)
    return f'<div class="acard"><div class="al">AUDIO<br><small>Scan or click</small></div>{cells}</div>'

def photo(letter):
    for f in glob.glob(f"{IMG_DIR}/{letter}-*") + glob.glob(f"{IMG_DIR}/{letter}.*"):
        ext = f.rsplit(".", 1)[-1].lower().replace("jpg", "jpeg")
        if ext in ("jpeg", "png", "webp"):
            return f"data:image/{ext};base64," + base64.b64encode(open(f, "rb").read()).decode()
    return None

CAMERA = (f'<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="{AQUA}" stroke-width="1.6" '
          'stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h3l2-2.5h6L17 8h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>')

CSS = f"""
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Inter, sans-serif; font-size: 10pt; line-height: 1.45; color: {INK}; }}
.page {{ width: 210mm; height: 297mm; position: relative; overflow: hidden; break-after: page; background: #fff; }}
.page:last-child {{ break-after: auto; }}
.band {{ position: absolute; top: 0; left: 0; right: 0; height: 11mm; background: {TEAL}; color: #fff;
        display: flex; align-items: center; justify-content: space-between; padding: 0 16mm;
        font-size: 7.5pt; font-weight: 700; letter-spacing: .14em; }}
.band .lbl {{ color: {SAND}; }}
.band.tg {{ background: {TEAL_D}; }}
.body {{ position: absolute; top: 18mm; left: 16mm; right: 16mm; }}
.foot {{ position: absolute; bottom: 7mm; left: 16mm; right: 16mm; border-top: 1.2pt solid {SAND};
        padding-top: 1.6mm; display: flex; justify-content: space-between; font-size: 7pt; color: #7d858a; }}
.foot b {{ color: {TEAL}; font-size: 8.5pt; }}
/* cover */
.cover {{ position: absolute; top: 0; left: 0; right: 0; height: 84mm; background: {TEAL}; color: #fff; overflow: hidden; }}
.pattern {{ position: absolute; top: -4mm; left: -6mm; right: -6mm; font-size: 30pt; font-weight: 800; line-height: 1.05;
           color: #1c6d83; letter-spacing: .06em; white-space: nowrap; }}
.cover .in {{ position: absolute; left: 16mm; right: 16mm; top: 13mm; }}
.logo {{ font-size: 15pt; font-weight: 800; }} .logo span {{ color: {SAND}; }} .logo i {{ font-style: normal; font-weight: 400; color: #d7e9ec; }}
.kick {{ margin-top: 7mm; font-size: 8pt; font-weight: 700; letter-spacing: .16em; color: {SAND}; }}
.title {{ font-size: 36pt; font-weight: 800; line-height: 1; margin-top: 2mm; letter-spacing: -.02em; }}
.subt {{ font-size: 11pt; color: #d7e9ec; margin-top: 2.5mm; }}
.chips {{ position: absolute; left: 16mm; right: 16mm; bottom: 6mm; display: flex; gap: 3mm; }}
.chips div {{ flex: 1; background: {TEAL_D}; border-radius: 2mm; padding: 2mm 3mm; font-size: 8.3pt; }}
.chips b {{ display: block; color: {SAND}; font-size: 7pt; letter-spacing: .12em; }}
/* sections */
.sec {{ display: flex; align-items: center; background: {TEAL}; color: #fff; border-radius: 2mm; padding: 1.8mm 3mm; margin: 0 0 3mm; }}
.sec .n {{ width: 7mm; height: 7mm; line-height: 7mm; border-radius: 50%; background: {SAND}; color: {TEAL_D}; text-align: center;
          font-weight: 800; font-size: 10pt; margin-right: 3mm; }}
.sec .tx {{ font-size: 13pt; font-weight: 700; }}
.sec .time {{ margin-left: auto; }}
.time {{ white-space: nowrap; flex-shrink: 0; margin-left: 2mm; background: #ffe28a; color: #6b4e00; font-size: 7.5pt; font-weight: 800; padding: .7mm 2.2mm; border-radius: 3mm; letter-spacing: .03em; }}
.sub {{ display: flex; align-items: center; margin: 3.2mm 0 1.5mm; font-weight: 700; font-size: 10.3pt; color: {TEAL_D}; }}
.sub .l {{ display: inline-block; width: 5.5mm; height: 5.5mm; line-height: 5.5mm; text-align: center; border-radius: 1.2mm;
          background: {AQUA}; color: #fff; font-size: 8.5pt; margin-right: 2mm; }}
.sub .time {{ margin-left: auto; }}
.inst {{ font-weight: 600; margin: 0 0 1.8mm; }}
p {{ margin: 0 0 1.8mm; }}
ol {{ margin: 0 0 1.5mm; padding-left: 6mm; }} li {{ margin-bottom: 1.1mm; }}
.two {{ display: flex; gap: 6mm; }} .two > div {{ flex: 1; }}
.bank {{ background: #e6f0f2; border: .8pt solid #c9dfe3; border-radius: 2mm; padding: 2mm 3.5mm; font-weight: 700; color: {TEAL_D}; margin: 0 0 2.5mm; }}
.box {{ background: #e6f0f2; border-left: 3.5pt solid {TEAL}; border-radius: 0 2mm 2mm 0; padding: 2.5mm 3.5mm; margin: 2mm 0; }}
.box h4 {{ margin: 0 0 1.2mm; font-size: 8.5pt; color: {TEAL}; letter-spacing: .08em; }}
.box.sand {{ background: #f1eadc; border-left-color: #a88f62; }} .box.sand h4 {{ color: #7d6640; }}
table {{ border-collapse: collapse; width: 100%; margin: 1.5mm 0 2mm; font-size: 9.3pt; }}
th {{ background: {TEAL}; color: #fff; text-align: left; padding: 1.5mm 2.5mm; font-weight: 700; }}
td {{ padding: 1.4mm 2.5mm; border-bottom: .6pt solid #d5dcdf; vertical-align: top; }}
tr:nth-child(odd) td {{ background: #f2f6f7; }}
.box.sand th {{ background: #a88f62; }} .box.sand tr:nth-child(odd) td {{ background: #f8f3ea; }}
.blank {{ display: inline-block; min-width: 19mm; border-bottom: .8pt solid #7d858a; text-align: center; font-weight: 800; color: {RED}; }}
.red {{ color: {RED}; font-weight: 800; }}
.wline {{ border-bottom: .8pt dotted #8d959a; min-height: 6.5mm; padding-top: 1mm; }}
.audio {{ white-space: nowrap; flex-shrink: 0; display: inline-block; background: {TEAL_D}; color: #fff; font-size: 7pt; font-weight: 800; letter-spacing: .08em;
         padding: .5mm 2mm; border-radius: 1mm; margin-left: 2mm; }}
.msg {{ background: #fff; border: 1pt solid #c9dfe3; border-radius: 3mm 3mm 3mm 0; padding: 3mm 4mm; max-width: 130mm; box-shadow: 1.5mm 1.5mm 0 #e6f0f2; }}
.audio {{ text-decoration: none; }}
.acard {{ display: flex; align-items: center; gap: 4mm; background: {TEAL_D}; color: #fff; border-radius: 2mm; padding: 2mm 3mm; margin: 2mm 0 1mm; }}
.acard .al {{ font-size: 8pt; font-weight: 800; letter-spacing: .12em; color: {SAND}; width: 22mm; line-height: 1.3; }}
.acard .al small {{ font-weight: 500; letter-spacing: 0; color: #d7e9ec; }}
.qa {{ display: flex; align-items: center; gap: 2mm; color: #fff; text-decoration: none; font-size: 7.5pt; line-height: 1.3; }}
.qa img {{ width: 15mm; height: 15mm; background: #fff; border-radius: 1mm; }}
.qa b {{ color: {SAND}; }}
.pt {{ margin: -1.2mm 0 1.6mm 7.5mm; font-size: 8.3pt; color: #6b7377; font-style: italic; }}
.qph {{ width: 15mm; height: 15mm; background: #fff; color: #9aa; border-radius: 1mm; display: inline-block; text-align: center; line-height: 15mm; font-weight: 800; }}
.word {{ font-size: 12pt; }}
.tree {{ margin: 2mm 0 2.5mm; }}
.trow {{ display: flex; justify-content: space-around; align-items: center; }}
.tcpl {{ display: flex; align-items: center; gap: 1.5mm; }}
.tbox {{ width: 27mm; border: 1pt solid {TEAL}; border-radius: 1.5mm; text-align: center; padding: 1mm 0 .8mm; background: #fff; }}
.tbox .nm {{ font-weight: 800; color: {TEAL_D}; min-height: 4.6mm; font-size: 9.5pt; }}
.tbox .nm.blank2 {{ border-bottom: .8pt solid #8d959a; margin: 0 3mm; color: {RED}; }}
.tbox .rl {{ font-size: 7pt; color: #6b7377; }}
.tplus {{ font-weight: 800; color: {AQUA}; }}
.tline {{ height: 4mm; border-left: 1.2pt solid {AQUA}; margin: 0 auto; width: 0; }}
.clk {{ display:flex; flex-wrap:wrap; gap:2.5mm; }}
.clk .c {{ width:41.5mm; border:.8pt solid #c9dfe3; border-radius:2mm; padding:1.5mm; text-align:center; }}
.clk .c .wline {{ font-size:8.5pt; }}
.sched td {{ padding:1.2mm 2.5mm; }}
.ad {{ border:1pt solid {TEAL}; border-radius:2mm; padding:2mm 3mm; font-size:9pt; }}
.ad b.t {{ display:block; color:{TEAL}; font-size:10pt; }}
.chat p {{ margin:0 0 1.3mm; }} .chat .m {{ background:#f1f4f5; border-radius:2mm; padding:1.2mm 2.5mm; display:inline-block; }}
.chat .l {{ background:#e6f0f2; border-radius:2mm; padding:1.2mm 2.5mm; display:inline-block; }}
.ck td {{ text-align:center; }} .ck td:first-child {{ text-align:left; }}
/* photo cards */
.grid {{ display: flex; flex-wrap: wrap; gap: 2.6mm; }}
.card {{ width: 42mm; border-radius: 2mm; overflow: hidden; border: .8pt solid #c9dfe3; background: #fff; }}
.ph {{ height: 29mm; background: #dfeaed; position: relative; }}
.ph img {{ width: 100%; height: 29mm; object-fit: cover; display: block; }}
.ph .ltr {{ position: absolute; top: 1.5mm; left: 1.5mm; background: {TEAL}; color: #fff; font-weight: 800; font-size: 8pt;
           width: 5.5mm; height: 5.5mm; line-height: 5.5mm; text-align: center; border-radius: 1mm; }}
.ph .brief {{ position: absolute; left: 2mm; right: 2mm; bottom: 1.8mm; font-size: 6.3pt; color: #4c6a72; line-height: 1.25; }}
.ph .cam {{ position: absolute; top: 7mm; left: 0; right: 0; text-align: center; }}
.card .w {{ height: 7.5mm; margin: 0 2mm; border-bottom: .8pt solid #8d959a; text-align: center; padding-top: 1.6mm; font-weight: 800; color: {RED}; font-size: 9pt; }}
.card .pad {{ height: 2mm; }}
/* notes zone */
.notes {{ position: absolute; left: 16mm; right: 16mm; bottom: 15mm; border-radius: 2.5mm; overflow: hidden; }}
.notes.sb {{ border: 1pt dashed {SAND}; padding: 2mm 3.5mm; background:
            repeating-linear-gradient(to bottom, transparent 0, transparent 6.8mm, #e4dccb 6.8mm, #e4dccb 7.1mm); }}
.notes.sb .h {{ font-size: 7.5pt; font-weight: 800; letter-spacing: .14em; color: #a88f62; background: #fff; display: inline-block; padding-right: 2mm; }}
.notes.tg {{ background: #fff4c7; border: 1.2pt solid #e5c24f; padding: 2.5mm 3.8mm; font-size: 8.7pt; line-height: 1.38; }}
.notes.tg .h {{ font-size: 7.5pt; font-weight: 800; letter-spacing: .14em; color: #8a6a00; margin-bottom: 1mm; }}
.notes.tg ol, .notes.tg ul {{ margin: 0 0 1mm; padding-left: 5mm; }} .notes.tg li {{ margin-bottom: .6mm; }}
.notes.tg p {{ margin: 0 0 1mm; }}
.notes.tg table {{ font-size: 8.3pt; margin: 1mm 0; }} .notes.tg th {{ background: #a07c00; padding: 1mm 2mm; }}
.notes.tg td {{ padding: 1mm 2mm; border-bottom: .5pt solid #ecd27a; }} .notes.tg tr:nth-child(odd) td {{ background: #fff9e0; }}
.check {{ list-style: none; padding-left: 0; }} .check li:before {{ content: "☐  "; color: {TEAL}; font-weight: 800; }}
.small {{ font-size: 8.6pt; color: #4d5559; }}
"""

class Book:
    def __init__(self, teacher):
        self.T = teacher
        self.pages = []
        self.sb_no = 0

    # helpers -----------------------------------------------------------
    def A(self, ans, w=""):
        return f'<span class="blank" style="{w}">{ans if self.T else "&nbsp;"}</span>'
    def R(self, txt):
        return f'<span class="red">{txt}</span>' if self.T else ""
    def time(self, t):
        return f'<span class="time">{t}</span>' if (self.T and t) else ""
    def sec(self, n, title, t):
        return f'<div class="sec"><span class="n">{n}</span><span class="tx">{title}</span>{self.time(t)}</div>'
    def sub(self, l, title, t="", audio="", pt=""):
        if audio and audio in AUDIO:
            a = f'<a class="audio" href="{aurl(audio)}">&#9654; PLAY {audio}</a>'
        elif audio:
            a = f'<span class="audio">&#9654; AUDIO {audio}</span>'
        else:
            a = ""
        p = f'<div class="pt">{pt}</div>' if pt else ""
        return f'<div class="sub"><span class="l">{l}</span>{title}{a}{self.time(t) if t else ""}</div>{p}'

    def page(self, body, notes_h, tnotes, cover=""):
        """A mirrored page: same body in both books; the notes zone is 'My notes' (SB) or teacher notes (TG)."""
        self.sb_no += 1
        label = "TEACHER'S GUIDE" if self.T else "STUDENT BOOK"
        band = "" if cover else f'<div class="band {"tg" if self.T else ""}"><span>SPEAK! ESSENTIALS · {BAND}</span><span class="lbl">{label}</span></div>'
        if self.T:
            notes = f'<div class="notes tg" style="height:{notes_h}mm"><div class="h">TEACHER\'S NOTES</div>{tnotes}</div>'
            foot_r = f"Student Book p. {self.sb_no}"
        else:
            notes = f'<div class="notes sb" style="height:{notes_h}mm"><span class="h">MY NOTES</span></div>'
            foot_r = f"<b>{self.sb_no}</b>"
        top = "style='top:92mm'" if cover else ""
        self.pages.append(f'<div class="page">{band}{cover}<div class="body" {top}>{body}</div>{notes}'
                          f'<div class="foot"><span>© Speak! English School · speakenglishschool.lovable.app</span><span>{foot_r}</span></div></div>')

    def extra(self, title, body):
        """Teacher-only page (overview, scripts)."""
        if not self.T:
            return
        self.pages.append(f'<div class="page"><div class="band tg"><span>SPEAK! ESSENTIALS · {BAND}</span><span class="lbl">TEACHER\'S GUIDE</span></div>'
                          f'<div class="body">{self.sec("T", title, "")}{body}</div>'
                          f'<div class="foot"><span>© Speak! English School · speakenglishschool.lovable.app</span><span>Teacher only</span></div></div>')

    def html(self):
        import re
        h = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(self.pages)}</body></html>"
        return re.sub(r'<li value="?(\d+)"?>', lambda m: f'<li style="list-style:none;margin-left:-5mm">{m.group(1)}.&nbsp; ', h)















def twocol(items, split):
    h = "".join(items)
    k = h.index(f'<li value="{split}">')
    return f'<div class="two"><div><ol>{h[:k]}</ol></div><div><ol>{h[k:]}</ol></div></div>'

def cover_html(T, kick, title, subt, chips):
    """chips: list of 3 (label, text)."""
    pattern = "<br>".join(["SPEAK SPEAK SPEAK SPEAK SPEAK SPEAK"] * 8)
    ch = "".join(f"<div><b>{a}</b>{b}</div>" for a, b in chips)
    return (f'<div class="cover"><div class="pattern">{pattern}</div><div class="in"><div class="logo">Speak<span>!</span> <i>Essentials</i></div>'
            f'<div class="kick">{kick} · {"TEACHER\'S GUIDE" if T else "STUDENT BOOK"}</div><div class="title">{title}</div><div class="subt">{subt}</div></div>'
            f'<div class="chips">{ch}</div></div>')

def photo_grid(T, photos):
    """photos: list of (letter, answer_word, brief)."""
    cards = ""
    for l, w, brief in photos:
        src = photo(l)
        inner = f'<img src="{src}">' if src else f'<div class="cam">{CAMERA}</div><div class="brief">{brief}</div>'
        cards += f'<div class="card"><div class="ph">{inner}<div class="ltr">{l}</div></div><div class="w">{w if T else ""}</div><div class="pad"></div></div>'
    return f'<div class="grid">{cards}</div>'

def render(build, out_prefix):
    """build(teacher)->html. Writes '<out_prefix> - SB_draft.pdf' and '- TB_draft.pdf'."""
    for teacher, name in [(False, "SB"), (True, "TB")]:
        HTML(string=build(teacher)).write_pdf(f"{out_prefix} - {name}_draft.pdf")
        print("ok", name)
