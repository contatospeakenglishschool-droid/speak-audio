# Replace the old header (cover kick line + top band) of an existing Speak! Essentials PDF
# with the new one (bullets, flag + ENGLISH, STUDENT'S BOOK), keeping all page content.
# usage: python3 retitle.py IN.pdf OUT.pdf
import sys, re, io, subprocess, secrets
sys.path.insert(0, "/home/claude/speak-audio/engine")
import speak_engine as E
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as P

def unit_label(name):
    n = int(re.search(r"Essentials (\d+)", name).group(1))
    reviews = {9: 1, 18: 2, 27: 3, 36: 4, 45: 5}
    return f"REVIEW {reviews[n]}" if n in reviews else f"UNIT {n}"

def band_pages(path):
    """indexes of pages whose top band contains SPEAK! ESSENTIALS text"""
    out = subprocess.run(["pdftotext", "-bbox", path, "-"], capture_output=True, text=True).stdout
    pages = out.split("<page ")[1:]
    res = []
    for i, p in enumerate(pages):
        top = [w for y, w in re.findall(r'yMin="([\d.-]+)"[^>]*>([^<]*)<', p) if float(y) < 25]
        if "".join(top).replace(" ", "").startswith("SPEAK!ESSENTIALS"):
            res.append(i)
    return res

def overlay(T, label, cover):
    E.BAND = f"A1 · {label}"
    css = E.CSS + ".page{background:transparent!important}"
    if cover:
        kick = f"LEVEL A1 · {label}"
        inner = E.cover_html(T, kick, "", "", [("", ""), ("", ""), ("", "")])
        body = ('<div class="page"><div style="position:absolute;top:26.8mm;left:0;width:210mm;height:5.9mm;overflow:hidden">'
                f'<div style="position:absolute;top:-26.8mm;left:0;width:210mm;height:84mm">{inner}</div></div></div>')
    else:
        lab = "TEACHER'S GUIDE" if T else "STUDENT'S BOOK"
        band = f'<div class="band {"tg" if T else ""}"><span>SPEAK! ESSENTIALS{E.SEP}{E.BAND.replace(" · ", E.SEP)}{E.SEP}{E.lang_tag()}</span><span class="lbl">{lab}</span></div>'
        body = f'<div class="page">{band}</div>'
    pdf = HTML(string=f"<html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>").write_pdf()
    return PdfReader(io.BytesIO(pdf)).pages[0]

def main(src, dst):
    name = src.rsplit("/", 1)[-1]
    T = name.endswith("TB.pdf")
    label = unit_label(name)
    bands = band_pages(src)
    r = PdfReader(src)
    if r.is_encrypted:
        r.decrypt("")
    cov, ban = overlay(T, label, True), overlay(T, label, False)
    w = PdfWriter()
    for i, pg in enumerate(r.pages):
        if i == 0 and i not in bands:
            pg.merge_page(cov)
        elif i in bands:
            pg.merge_page(ban)
        w.add_page(pg)
    for pg in w.pages:
        pg.compress_content_streams()
    w.compress_identical_objects(remove_identicals=True, remove_orphans=True)
    w.add_metadata({"/Author": "Speak! English School", "/Title": name[:-4]})
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS
    w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), permissions_flag=perms, algorithm="AES-256")
    with open(dst, "wb") as f:
        w.write(f)
    print("ok", name, label, "band pages:", len(bands), "of", len(r.pages))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
