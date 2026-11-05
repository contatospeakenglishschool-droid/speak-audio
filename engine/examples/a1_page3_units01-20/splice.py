# Replace page 3 of a published (locked) SB/TB with page 3 of a new draft, then lock again.
# usage: splice.py "<draft prefix>" "<published SB.pdf>" "<published TB.pdf>" "<out dir>"
import os, re, secrets, sys
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as P


def p3(reader, teacher):
    for i, pg in enumerate(reader.pages):
        t = pg.extract_text() or ""
        if teacher and "Student Book p. 3" in t:
            return i
    if not teacher:
        return 2
    raise SystemExit(f"page 3 not found ({'TB' if teacher else 'SB'})")


def main(draft, sb, tb, out):
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS
    for k, pub, teacher in (("SB", sb, False), ("TB", tb, True)):
        new = PdfReader(f"{draft} - {k}_draft.pdf")
        old = PdfReader(pub)
        if old.is_encrypted:
            old.decrypt("")
        i_new, i_old = p3(new, teacher), p3(old, teacher)
        w = PdfWriter()
        for i, pg in enumerate(old.pages):
            w.add_page(new.pages[i_new] if i == i_old else pg)
        meta = {k2: v for k2, v in (old.metadata or {}).items() if isinstance(v, str)}
        w.add_metadata(meta)
        w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), permissions_flag=perms, algorithm="AES-256")
        dst = os.path.join(out, os.path.basename(pub))
        w.write(dst)
        print(k, "page", i_old + 1, "replaced ->", dst, f"({len(old.pages)} pages)")


if __name__ == "__main__":
    main(*sys.argv[1:5])
