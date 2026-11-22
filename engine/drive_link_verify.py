import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pypdf import PdfReader
from qrutil import load, is_qr_candidate, qdec
for f in sys.argv[1:]:
    r = PdfReader(f); links = []; qrs = []
    for pg in r.pages:
        for a in pg.get("/Annots") or []:
            A = a.get_object().get("/A")
            if A and A.get_object().get("/URI"): links.append(str(A.get_object()["/URI"]))
        for im in pg.images:
            arr = load(im)
            if is_qr_candidate(arr): qrs.append(qdec(arr) or "UNDECODED")
    bad = [x for x in links + qrs if "google" in x or x == "UNDECODED"]
    print(os.path.basename(f), "links", len(links), "qrs", len(qrs), "BAD", len(bad))
