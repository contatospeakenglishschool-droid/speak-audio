# Speak! Essenziale (Italian line) - Italian layer over the shared engine.
# The shared engine is used read-only: Italian labels are swapped in the final HTML,
# so the English output of speak_engine.py never changes.
# Usage in a unit script:
#   import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
#   from engine_it import *
#   setup(band="A1 · UNITÀ 01", audio_json="audio_it-a1-unita-01.json", img_dir="img", lang="it-IT")
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import speak_engine as _se
from speak_engine import *

_se.FLAGS["it-IT"] = ("ITALIANO", '<svg viewBox="0 0 15 10" width="15" height="10" style="width:4.2mm;height:2.8mm;vertical-align:-0.35mm;border-radius:.35mm;box-shadow:0 0 0 .2mm rgba(255,255,255,.35)">'
                                  '<rect width="5" height="10" fill="#009246"/><rect x="5" width="5" height="10" fill="#fff"/><rect x="10" width="5" height="10" fill="#CE2B37"/></svg>')

LABELS = [
    ("SPEAK! ESSENTIALS", "SPEAK! ESSENZIALE"),
    ("<i>Essentials</i>", "<i>Essenziale</i>"),
    ("TEACHER'S GUIDE", "GUIDA DELL'INSEGNANTE"),
    ("TEACHER\\'S GUIDE", "GUIDA DELL'INSEGNANTE"),
    ("STUDENT'S BOOK", "LIBRO DELLO STUDENTE"),
    ("TEACHER'S NOTES", "NOTE PER L'INSEGNANTE"),
    ("MY NOTES", "I MIEI APPUNTI"),
    ("Student Book p. ", "Libro dello studente p. "),
    ("<span>Teacher only</span>", "<span>Solo per l'insegnante</span>"),
    ("<small>Scan or click</small>", "<small>Scansiona o clicca</small>"),
    ("&#9654; PLAY</b>", "&#9654; ASCOLTA</b>"),
    ("&#9654; PLAY ", "&#9654; ASCOLTA "),
    (" · SLOW", " · LENTO"),
    (" · NATURAL", " · NATURALE"),
]


class BookIT(_se.Book):
    def html(self):
        h = super().html()
        for en, it in LABELS:
            h = h.replace(en, it)
        return h


Book = BookIT
