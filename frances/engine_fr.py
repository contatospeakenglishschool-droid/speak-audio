# Speak! Essentiel (French line) - French layer over the shared engine.
# The shared engine is used read-only: French labels are swapped in the final HTML,
# so the English output of speak_engine.py never changes.
# Usage in a unit script:
#   import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
#   from engine_fr import *
#   setup(band="A1 · UNITÉ 01", audio_json="audio_fr-a1-unite-01.json", img_dir="img", lang="fr-FR")
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import speak_engine as _se
from speak_engine import *

# Non-English lines use the new school name and website (footer link + PDF author)
_se.SCHOOL = "Speak! Language School"
_se.SITE = "speaklanguageschool.lovable.app"

_se.FLAGS["fr-FR"] = ("FRANÇAIS", '<svg viewBox="0 0 15 10" width="15" height="10" style="width:4.2mm;height:2.8mm;vertical-align:-0.35mm;border-radius:.35mm;box-shadow:0 0 0 .2mm rgba(255,255,255,.35)">'
                                  '<rect width="5" height="10" fill="#002395"/><rect x="5" width="5" height="10" fill="#fff"/><rect x="10" width="5" height="10" fill="#ED2939"/></svg>')

LABELS = [
    ("SPEAK! ESSENTIALS", "SPEAK! ESSENTIEL"),
    ("<i>Essentials</i>", "<i>Essentiel</i>"),
    ("TEACHER'S GUIDE", "GUIDE DE L'ENSEIGNANT"),
    ("TEACHER\\'S GUIDE", "GUIDE DE L'ENSEIGNANT"),
    ("STUDENT'S BOOK", "LIVRE DE L'ÉLÈVE"),
    ("TEACHER'S NOTES", "NOTES POUR L'ENSEIGNANT"),
    ("MY NOTES", "MES NOTES"),
    ("Student Book p. ", "Livre de l'élève p. "),
    ("<span>Teacher only</span>", "<span>Pour l'enseignant</span>"),
    ("<small>Scan or click</small>", "<small>Scannez ou cliquez</small>"),
    ("&#9654; PLAY</b>", "&#9654; ÉCOUTER</b>"),
    ("&#9654; PLAY ", "&#9654; ÉCOUTER "),
    (" · SLOW", " · LENT"),
    (" · NATURAL", " · NATUREL"),
]

# French typography: narrow no-break space before ? ! : (and before ; when the source has a space),
# text only: never inside tags, CSS, entities (&nbsp;) or the brand name "Speak!".
_PUNCT = re.compile(r"(?<![Ss][Pp][Ee][Aa][Kk])(?<=[\w…»)\]]) ?([?!:])(?=[\s<]|$)| ;(?=[\s<]|$)")


def _fr_spacing(h):
    i = h.rfind("</style>")
    head, body = (h[:i], h[i:]) if i >= 0 else ("", h)
    body = re.sub(r">([^<]+)<", lambda m: ">" + _PUNCT.sub(lambda p: "\u202f" + (p.group(1) or ";"), m.group(1)) + "<", body)
    return head + body


class BookFR(_se.Book):
    def html(self):
        h = super().html()
        for en, fr in LABELS:
            h = h.replace(en, fr)
        return _fr_spacing(h)


Book = BookFR
