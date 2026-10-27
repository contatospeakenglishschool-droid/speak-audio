# Patch the footer of existing locked Speak! PDFs (any language), keeping all page content:
#  - makes the website in the footer a clickable link
#  - optionally swaps the school name and website (e.g. to Speak! Language School)
# usage: python3 footer_patch.py IN.pdf OUT.pdf [--school "Speak! Language School" --site speaklanguageschool.lovable.app]
# Without --school/--site the footer text stays the same and only the link is added.
# The overlay is rendered with the same CSS font stack as the engine, so on the same machine it matches the original.
import argparse, io, re, secrets, subprocess
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter
from pypdf.annotations import Link
from pypdf.constants import UserAccessPermissions as P

OLD_SCHOOL, OLD_SITE = "Speak! English School", "speakenglishschool.lovable.app"


def footer_lines(path):
    """per page: (x0, y0, x1, y1, site_x0, site_x1) of the footer line '© … lovable.app' in pt, top-left origin, or None"""
    out = subprocess.run(["pdftotext", "-bbox", path, "-"], capture_output=True, text=True).stdout
    res = []
    for p in out.split("<page ")[1:]:
        words = [(float(a), float(b), float(c), float(d), w) for a, b, c, d, w in
                 re.findall(r'xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">([^<]*)<', p)]
        site = [w for w in words if "lovable.app" in w[4] and w[1] > 760]
        copy = [w for w in words if w[4] == "©" and w[1] > 760]
        if site and copy:
            s, c = site[0], copy[0]
            res.append((c[0], c[1], s[2], s[3], s[0], s[2]))
        else:
            res.append(None)
    return res


def overlay(line, school, site, page_w, page_h):
    """a transparent page with the new footer text on a white strip over the old one; returns (page, link rect)"""
    x0, y0, x1, y1 = line[:4]
    h = y1 - y0
    html = (f"<html><head><meta charset='utf-8'><style>@page{{size:{page_w}pt {page_h}pt;margin:0}}body{{margin:0}}"
            f".f{{position:absolute;left:{x0 - 1}pt;top:{y0 - 1}pt;min-width:{x1 - x0 + 4}pt;height:{h + 2}pt;line-height:{h + 2}pt;"
            f"background:#fff;padding:0 2pt 0 1pt;white-space:nowrap;font-family:Inter,sans-serif;font-size:7pt;color:#7d858a}}"
            f"a{{color:inherit;text-decoration:none}}</style></head><body>"
            f"<div class='f'>© {school} · <a href='https://{site}'>{site}</a></div></body></html>")
    pg = PdfReader(io.BytesIO(HTML(string=html).write_pdf())).pages[0]
    rect = None
    for a in pg.get("/Annots") or []:
        a = a.get_object()
        if site in str(a.get("/A", {}).get("/URI", "")):
            rect = [float(v) for v in a["/Rect"]]
    if "/Annots" in pg:
        del pg["/Annots"]
    return pg, rect


def main(src, dst, school=None, site=None):
    lines = footer_lines(src)
    r = PdfReader(src)
    if r.is_encrypted:
        r.decrypt("")
    swap = bool(school or site)
    school, site = school or OLD_SCHOOL, site or OLD_SITE
    w = PdfWriter()
    rects = []
    for pg, line in zip(r.pages, lines):
        pw, ph = float(pg.mediabox.width), float(pg.mediabox.height)
        rect = None
        if line and swap:
            ov, rect = overlay(line, school, site, pw, ph)
            pg.merge_page(ov)
        elif line:
            rect = [line[4], ph - line[3], line[5], ph - line[1]]
        w.add_page(pg)
        rects.append(rect)
    for i, rect in enumerate(rects):
        if rect:
            w.add_annotation(i, Link(rect=rect, url=f"https://{site}"))
    for pg in w.pages:
        pg.compress_content_streams()
    w.compress_identical_objects(remove_identicals=True, remove_orphans=True)
    meta = dict(r.metadata or {})
    w.add_metadata({"/Author": school, "/Title": meta.get("/Title") or dst.rsplit("/", 1)[-1][:-4]})
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS
    w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), permissions_flag=perms, algorithm="AES-256")
    with open(dst, "wb") as f:
        w.write(f)
    return sum(1 for x in rects if x), len(rects)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--school"); ap.add_argument("--site")
    a = ap.parse_args()
    n, t = main(a.src, a.dst, a.school, a.site)
    print("ok", a.dst.rsplit("/", 1)[-1], f"links on {n}/{t} pages")
