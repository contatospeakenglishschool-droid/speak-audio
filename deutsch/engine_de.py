# Speak! Essenziell (German line) - German layer over the shared engine.
# The shared engine is used read-only: German labels are swapped in the final HTML,
# so the English output of speak_engine.py never changes.
# Usage in a unit script:
#   import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
#   from engine_de import *
#   setup(band="A1 · EINHEIT 01", audio_json="audio_de-a1-einheit-01.json", img_dir="img", lang="de-DE")
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import speak_engine as _se
from speak_engine import *

_se.FLAGS["de-DE"] = ("DEUTSCH", '<svg viewBox="0 0 15 9" width="15" height="9" style="width:4.2mm;height:2.6mm;vertical-align:-0.35mm;border-radius:.35mm;box-shadow:0 0 0 .2mm rgba(255,255,255,.35)">'
                                 '<rect width="15" height="3" fill="#000"/><rect y="3" width="15" height="3" fill="#DD0000"/><rect y="6" width="15" height="3" fill="#FFCE00"/></svg>')

LABELS = [
    ("SPEAK! ESSENTIALS", "SPEAK! ESSENZIELL"),
    ("<i>Essentials</i>", "<i>Essenziell</i>"),
    ("TEACHER'S GUIDE", "LEHRERHANDBUCH"),
    ("TEACHER\\'S GUIDE", "LEHRERHANDBUCH"),
    ("STUDENT'S BOOK", "KURSBUCH"),
    ("TEACHER'S NOTES", "NOTIZEN FÜR DIE LEHRKRAFT"),
    ("MY NOTES", "MEINE NOTIZEN"),
    ("Student Book p. ", "Kursbuch S. "),
    ("<span>Teacher only</span>", "<span>Nur für die Lehrkraft</span>"),
    ("<small>Scan or click</small>", "<small>Scannen oder klicken</small>"),
    ("&#9654; PLAY</b>", "&#9654; ANHÖREN</b>"),
    ("&#9654; PLAY ", "&#9654; ANHÖREN "),
    (" · SLOW", " · LANGSAM"),
    (" · NATURAL", " · NATÜRLICH"),
]


class BookDE(_se.Book):
    def html(self):
        h = super().html()
        for en, de in LABELS:
            h = h.replace(en, de)
        return h


Book = BookDE
