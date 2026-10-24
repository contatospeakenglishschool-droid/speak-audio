"""Speak! Essentials - small tools.

  python3 speak_tools.py lock "<out_prefix>"   -> locks '<prefix> - SB_draft.pdf'/'TB_draft.pdf' into final PDFs (print + annotate only)
  python3 speak_tools.py pad SRC DST [bg]                     -> pads an image to 1.45:1 so the photo card does not cut the subject
  python3 speak_tools.py sheet OUT_PREFIX                     -> PNG contact sheets of SB and TB pages (for visual QA)
"""
import glob, os, subprocess, sys


def lock(prefix, pwfile):
    from pypdf import PdfWriter
    from pypdf.constants import UserAccessPermissions as P
    import secrets
    pw = open(pwfile).read().strip() if pwfile and os.path.exists(pwfile) else secrets.token_urlsafe(24)  # random owner password: nobody needs it later
    perms = P.PRINT | P.PRINT_TO_REPRESENTATION | P.ADD_OR_MODIFY | P.FILL_FORM_FIELDS
    for k in ("SB", "TB"):
        n = f"{prefix} - {k}"
        w = PdfWriter(clone_from=n + "_draft.pdf")
        w.add_metadata({"/Author": "Speak! English School", "/Title": os.path.basename(n)})
        w.encrypt(user_password="", owner_password=pw, permissions_flag=perms, algorithm="AES-256")
        w.write(n + ".pdf")
        os.remove(n + "_draft.pdf")
        print("locked", n + ".pdf")


def pad(src, dst, bg="white"):
    from PIL import Image
    im = Image.open(src).convert("RGB"); w, h = im.size
    W = max(w, int(h * 1.45)); H = max(h, int(W / 1.45))
    out = Image.new("RGB", (W, H), bg); out.paste(im, ((W - w) // 2, (H - h) // 2)); out.save(dst, quality=92)


def sheet(prefix):
    from PIL import Image
    d = os.path.dirname(prefix) or "."
    os.makedirs(f"{d}/_png", exist_ok=True)
    for k in ("SB", "TB"):
        pdf = f"{prefix} - {k}_draft.pdf"
        subprocess.run(["pdftoppm", "-r", "60", "-png", pdf, f"{d}/_png/{k}"], check=True)
        ims = [Image.open(f) for f in sorted(glob.glob(f"{d}/_png/{k}-*.png"))]
        w, h = ims[0].size; rows = (len(ims) + 4) // 5
        sh = Image.new("RGB", (w * 5, h * rows), "white")
        for i, im in enumerate(ims):
            sh.paste(im, ((i % 5) * w, (i // 5) * h))
        sh.save(f"{d}/_png/{k}_sheet.png"); print(f"{d}/_png/{k}_sheet.png")


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "lock": lock(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    elif cmd == "pad": pad(*sys.argv[2:])
    elif cmd == "sheet": sheet(sys.argv[2])
