# Speak! Esencial (Spanish line, Latin American Spanish) - Spanish layer over the shared engine.
# The shared engine is used read-only: Spanish labels are swapped in the final HTML,
# so the English output of speak_engine.py never changes.
# Usage in a unit script:
#   import os, sys; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
#   from engine_es import *
#   setup(band="A1 · UNIDAD 01", audio_json="audio_es-a1-unidad-01.json", img_dir="img", lang="es-419")
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import speak_engine as _se
from speak_engine import *

# Non-English lines use the new school name and website (footer link + PDF author)
_se.SCHOOL = "Speak! Language School"
_se.SITE = "speaklanguageschool.lovable.app"

# es-419 = Latin American Spanish; home base Mexico City, so the Mexican flag
_se.FLAGS["es-419"] = ("ESPAÑOL", '<svg viewBox="0 0 15 9" width="15" height="9" style="width:4.2mm;height:2.6mm;vertical-align:-0.35mm;border-radius:.35mm;box-shadow:0 0 0 .2mm rgba(255,255,255,.35)">'
                                  '<rect width="5" height="9" fill="#006847"/><rect x="5" width="5" height="9" fill="#fff"/><rect x="10" width="5" height="9" fill="#CE1126"/>'
                                  '<circle cx="7.5" cy="4.5" r="1.1" fill="#8C5A2B"/></svg>')

LABELS = [
    ("SPEAK! ESSENTIALS", "SPEAK! ESENCIAL"),
    ("<i>Essentials</i>", "<i>Esencial</i>"),
    ("TEACHER'S GUIDE", "GUÍA DEL PROFESOR"),
    ("TEACHER\\'S GUIDE", "GUÍA DEL PROFESOR"),
    ("STUDENT'S BOOK", "LIBRO DEL ALUMNO"),
    ("TEACHER'S NOTES", "NOTAS PARA EL PROFESOR"),
    ("MY NOTES", "MIS NOTAS"),
    ("Student Book p. ", "Libro del alumno p. "),
    ("<span>Teacher only</span>", "<span>Solo para el profesor</span>"),
    ("<small>Scan or click</small>", "<small>Escanea o haz clic</small>"),
    ("&#9654; PLAY</b>", "&#9654; ESCUCHA</b>"),
    ("&#9654; PLAY ", "&#9654; ESCUCHA "),
    (" · SLOW", " · LENTO"),
    (" · NATURAL", " · NATURAL"),
]


class BookES(_se.Book):
    def html(self):
        h = super().html()
        for en, es in LABELS:
            h = h.replace(en, es)
        return h


Book = BookES
