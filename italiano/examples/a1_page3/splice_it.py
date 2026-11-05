# Italian version of engine/examples/a1_page3_units01-20/splice.py.
# Replaces page 3 ("3 Grammatica…") of a published, locked SB/TB with the same page of a new draft, then locks again.
# usage: splice_it.py "<draft prefix>" "<published SB.pdf>" "<published TB.pdf>" "<out dir>"
import os, re, secrets, sys
from pypdf import PdfReader, PdfWriter
from pypdf.constants import UserAccessPermissions as P


def p3(reader):
    hits = [i for i, pg in enumerate(reader.pages) if re.search(r"^3 Grammatica", pg.extract_text() or "", re.M)
            and "Panoramica della lezione" not in (pg.extract_text() or "")]
    if len(hits) != 1:
        raise SystemExit(f"page 3 not found unambiguously: {hits}")
    return hits[0]


def main(draft, sb, tb, out):
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS
    for k, pub in (("SB", sb), ("TB", tb)):
        new = PdfReader(f"{draft} - {k}_draft.pdf")
        old = PdfReader(pub)
        if old.is_encrypted:
            old.decrypt("")
        i_new, i_old = p3(new), p3(old)
        w = PdfWriter()
        for i, pg in enumerate(old.pages):
            w.add_page(new.pages[i_new] if i == i_old else pg)
        w.add_metadata({k2: v for k2, v in (old.metadata or {}).items() if isinstance(v, str)})
        w.encrypt(user_password="", owner_password=secrets.token_urlsafe(24), permissions_flag=perms, algorithm="AES-256")
        dst = os.path.join(out, os.path.basename(pub))
        w.write(dst)
        print(k, "page", i_old + 1, "replaced ->", dst, f"({len(old.pages)} pages)")


if __name__ == "__main__":
    main(*sys.argv[1:5])
