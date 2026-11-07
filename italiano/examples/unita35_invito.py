# Speak! Essenziale A1 35: Luca and Sara's wedding invitation; key details blank, teacher=True fills them in red
C1, C2, INK, RED, GOLD = "#176074", "#77acb5", "#3b4246", "#c0392b", "#b08d57"
ROWS = [("Quando:", "sabato", "26 settembre", ""), ("Ora:", "alle", "11", ""), ("Dove:", "chiesa di", "San Miniato al Monte", ", Firenze"),
        ("Dopo:", "pranzo e festa a", "Villa Le Rose", ", Fiesole"), ("Rispondete entro il", "", "20 settembre", "")]


def invito(teacher=False):
    W, H, p = 360, 186, []
    p.append(f'<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="4" fill="#fffdf8" stroke="{GOLD}" stroke-width="1.4"/>'
             f'<rect x="6" y="6" width="{W - 12}" height="{H - 12}" rx="3" fill="none" stroke="{GOLD}" stroke-width="0.6"/>'
             f'<text x="{W / 2}" y="30" text-anchor="middle" font-family="Georgia, serif" font-style="italic" font-size="20" fill="{C1}">Luca &amp; Sara</text>'
             f'<text x="{W / 2}" y="46" text-anchor="middle" font-size="9" fill="{INK}">sono felici di invitarvi al loro matrimonio</text>'
             f'<line x1="140" y1="54" x2="220" y2="54" stroke="{GOLD}" stroke-width="0.8"/>')
    for i, (lab, pre, ans, post) in enumerate(ROWS):
        y = 74 + i * 18
        p.append(f'<text x="22" y="{y}" font-size="9.5" font-weight="700" fill="{C1}">{lab}</text>')
        x = 128 if i == 4 else 70
        if pre:
            p.append(f'<text x="{x}" y="{y}" font-size="9.5" fill="{INK}">{pre}</text>')
            x += len(pre) * 4.9 + 6
        w = max(60, len(ans) * 5.6 + 10)
        p.append(f'<line x1="{x}" y1="{y + 2}" x2="{x + w}" y2="{y + 2}" stroke="{INK}" stroke-width="0.8"/>')
        if teacher:
            p.append(f'<text x="{x + 3}" y="{y - 1}" font-size="9.5" font-weight="700" fill="{RED}">{ans}</text>')
        if post:
            p.append(f'<text x="{x + w + 2}" y="{y}" font-size="9.5" fill="{INK}">{post}</text>')
    p.append(f'<text x="{W / 2}" y="{H - 13}" text-anchor="middle" font-size="8.5" fill="{INK}">Luca · 347 218 5530</text>')
    return (f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:62mm">{"".join(p)}</svg>')
