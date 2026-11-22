# Usage: python drive_to_github_patch.py IN.pdf OUT.pdf [map.json]  (map: drive_id -> {"path": repo-relative mp3})
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pypdf import PdfWriter
from pypdf.generic import NameObject, TextStringObject
import qrcode
from PIL import Image
from qrutil import load, is_qr_candidate, qdec
m = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[3] if len(sys.argv) > 3 else "travel_drive_map.json")))
BASE = "https://contatospeakenglishschool-droid.github.io/speak-audio/"
new = {i: BASE + v["path"] for i, v in m.items()}
def did(u):
    x = re.search(r"/d/([A-Za-z0-9_-]+)", u) or re.search(r"[?&]id=([A-Za-z0-9_-]+)", u)
    return x.group(1) if x else None
src, dst = sys.argv[1], sys.argv[2]
w = PdfWriter(clone_from=src)
nl = nq = 0; missing = []; undecoded = 0
for pg in w.pages:
    for a in pg.get("/Annots") or []:
        A = a.get_object().get("/A")
        if A and A.get_object().get("/URI"):
            u = str(A.get_object()["/URI"])
            if "google" in u:
                i = did(u)
                if i in new: A.get_object()[NameObject("/URI")] = TextStringObject(new[i]); nl += 1
                else: missing.append(u)
    for im in pg.images:
        arr = load(im)
        if not is_qr_candidate(arr): continue
        d = qdec(arr)
        if not d: undecoded += 1; continue
        if "google" not in d: continue
        i = did(d)
        if i not in new: missing.append(d); continue
        q = qrcode.make(new[i], box_size=6, border=1).get_image().convert("RGB").resize(arr.shape[::-1], Image.NEAREST)
        im.replace(q); nq += 1
w.write(dst)
print(f"{os.path.basename(src)}: links {nl}, qr {nq}, missing {len(missing)}, undecoded {undecoded}")
