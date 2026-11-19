"""Lean B1 format helpers (approved 2026-11-19).
SB: 1 Warm-up · 2 Listening/Reading · 3 Grammar reference (in class) · 4 Practice · 5 Speaking · H Homework (at home).
Timings 7 / 12 / 8 / 10 / 18 min + 3 min oral wrap-up."""


def talk(qs, title="TALK ABOUT IT"):
    return (f'<div class="box sand" style="margin-top:1.5mm"><h4>{title}</h4><ol style="margin:0;line-height:1.5;font-size:8.9pt">'
            + "".join(f"<li>{q}</li>" for q in qs) + "</ol></div>")


def grammar_in_class(b, fn, n=3, time="8 min"):
    """Render a grammar_ref page as section n of the class (instead of '+')."""
    _sec = b.sec
    b.sec = lambda num, t, tm="": _sec(n, t, time) if num == "+" else _sec(num, t, tm)
    try:
        fn(b)
    finally:
        b.sec = _sec


FORMAT_BOX = """<div class="box"><h4>B1 FORMAT</h4>This unit has <b>5 pages for the class</b> (warm-up, listening or reading, grammar reference, practice, speaking) and <b>1 page for home</b>. Each class page ends with a box of questions so the student speaks most of the time. Extra practice, word choice and writing are homework: check it in 3–5 minutes at the start of the next class.</div>"""


def overview(rows, unit_story, key_problem, audio):
    """rows: list of (stage, where, time, aim, page)."""
    tr = "".join(f"<tr><td>{s}</td><td>{w}</td><td>{t}</td><td>{a}</td><td>{p}</td></tr>" for s, w, t, a, p in rows)
    return (f"""<table><tr><th>Stage</th><th>Where</th><th>Time</th><th>Aim</th><th>SB page</th></tr>{tr}</table>
{FORMAT_BOX}
<div class="box sand"><h4>THE STORY</h4>{unit_story}</div>
<div class="box"><h4>KEY PROBLEM FOR BRAZILIANS</h4>{key_problem}</div>
<div class="box"><h4>AUDIO</h4>{audio}</div>""")


def std_rows(listen_aim, grammar, practice_aim, speak_aim, hw_aim, listen_label="Listening"):
    return [("1 Warm-up", "class", "7 min", "Discussion · key words · questions with the words", "1"),
            (f"2 {listen_label}", "class", "12 min", listen_aim, "2"),
            ("3 Grammar reference", "class", "8 min", grammar, "3"),
            ("4 Practice", "class", "10 min", practice_aim, "4"),
            ("5 Speaking", "class", "18 min", speak_aim, "5"),
            ("Wrap-up", "class", "3 min", "Two corrections from your notes · can-do question", "–"),
            ("Homework", "home", "–", hw_aim, "H")]


def watch_out(rows, title="WATCH OUT: WORD CHOICE"):
    tr = "".join(f"<tr><td>{a}</td><td><b>{b_}</b></td><td>{c}</td></tr>" for a, b_, c in rows)
    return (f'<div class="box sand" style="margin:1mm 0"><h4>{title}</h4><table style="margin:0;font-size:8.1pt">'
            f"<tr><th>Don't say</th><th>Say</th><th>Why?</th></tr>{tr}</table></div>")


def writing_task(sub, task, start, checks, cando):
    ck = " &nbsp;".join(f"☐ {c}" for c in checks)
    return (f"""{sub("C", f"Writing (100–150 words, in your notebook). {task}", "")}
<p class="small" style="margin:.3mm 0"><b>Start like this:</b> <i>{start}</i> &nbsp;{ck}</p>
<p class="small" style="margin:.3mm 0"><b>Can do:</b> {cando} ☐ Easy! ☐ Sometimes ☐ Not yet</p>""")
