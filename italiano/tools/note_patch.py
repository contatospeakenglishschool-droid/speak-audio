# replace single words in the TB teacher-note box of page 1 (overlay), keep the lock
import sys, io, json, secrets, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "engine"))
import speak_engine as E
from weasyprint import HTML
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as P
from pypdf.generic import NameObject, DecodedStreamObject
inp, out, edits = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
r = PdfReader(inp); r.decrypt("") if r.is_encrypted else None
spans = "".join(f'<div style="position:absolute;left:{x0-0.4}pt;top:{y0}pt;width:{x1-x0+0.8}pt;height:{y1-y0}pt;background:#fff4c7"></div>'
                f'<div style="position:absolute;left:{x0}pt;top:{y0}pt;font-size:8.7pt;line-height:{y1-y0}pt;white-space:nowrap">{t}</div>'
                for x0, y0, x1, y1, t in edits)
html = f"<html><head><style>{E.CSS} @page {{ size: A4; margin: 0 }} body {{ margin:0 }}</style></head><body>{spans}</body></html>"
ov = PdfReader(io.BytesIO(HTML(string=html).write_pdf())).pages[0]
w = PdfWriter()
for p in r.pages: w.add_page(p)
pg = w.pages[0]; pg.merge_page(ov)
st = DecodedStreamObject(); st.set_data(pg.get_contents().get_data()); pg[NameObject("/Contents")] = w._add_object(st)
w.add_metadata({k: v for k, v in (r.metadata or {}).items() if isinstance(v, str)})
w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), permissions_flag=P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS, algorithm="AES-256")
w.write(out); print("patched", os.path.basename(out))
