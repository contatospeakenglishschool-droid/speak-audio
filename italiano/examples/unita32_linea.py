# Speak! Essenziale A1 32: bus line 20 (fictional route) with timetable blanks; teacher=True fills them in red
C1, C2, INK, RED, SAND = "#176074", "#77acb5", "#3b4246", "#c0392b", "#f3ede3"
STOPS = ["Via Rizzoli", "Via Indipendenza", "Stazione Centrale", "Ponte", "Via Ferrarese", "Fiera", "Centro Sportivo"]
INFO = [("Passa ogni", "12", "minuti"), ("dalle", "6", ""), ("alle", "23", ""), ("Il viaggio dura", "25", "minuti"),
        ("Abbonamento mensile studenti:", "27", "€")]


def linea(teacher=False):
    W, H, p = 360, 122, []
    x0, x1, y = 22, W - 22, 42
    p.append(f'<rect x="0" y="0" width="34" height="20" rx="4" fill="{C1}"/><text x="17" y="14.5" font-size="11" font-weight="700" fill="#fff" text-anchor="middle">20</text>'
             f'<text x="42" y="14" font-size="10.5" font-weight="700" fill="{C1}">LINEA 20 · Via Rizzoli → Centro Sportivo</text>'
             f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{C1}" stroke-width="4" stroke-linecap="round"/>')
    step = (x1 - x0) / (len(STOPS) - 1)
    for i, s in enumerate(STOPS):
        x = x0 + i * step
        end = i in (0, len(STOPS) - 1)
        p.append(f'<circle cx="{x}" cy="{y}" r="{5.5 if end else 4.2}" fill="#fff" stroke="{C1}" stroke-width="2.2"/>')
        parts = s.split(" ", 1) if len(s) > 10 else [s]
        for j, t in enumerate(parts):
            p.append(f'<text x="{x}" y="{y + 15 + j * 9}" font-size="7.6" fill="{INK}" text-anchor="middle"{" font-weight=\"700\"" if end else ""}>{t}</text>')
    p.append(f'<rect x="0" y="76" width="{W}" height="{H - 76}" rx="6" fill="{SAND}" stroke="{C2}" stroke-width="1"/>')
    pos = [(10, 92), (142, 92), (222, 92), (10, 112), (170, 112)]
    for (lab, val, unit), (x, yy) in zip(INFO, pos):
        lw = len(lab) * 4.6
        p.append(f'<text x="{x}" y="{yy}" font-size="9" fill="{INK}">{lab}</text>'
                 f'<line x1="{x + lw + 4}" y1="{yy + 2}" x2="{x + lw + 34}" y2="{yy + 2}" stroke="{INK}" stroke-width="0.8"/>'
                 f'<text x="{x + lw + 38}" y="{yy}" font-size="9" fill="{INK}">{unit}</text>')
        if teacher:
            p.append(f'<text x="{x + lw + 19}" y="{yy}" font-size="10" font-weight="700" fill="{RED}" text-anchor="middle">{val}</text>')
    return (f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:48mm">{"".join(p)}</svg>')
