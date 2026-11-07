# Speak! Essenziale A1 34: Bruno's shopping list at the flea market; colours and prices blank, teacher=True fills them in red
C1, C2, INK, RED, SAND = "#176074", "#77acb5", "#3b4246", "#c0392b", "#f3ede3"
ROWS = [("la lampada", "verde", "20 €", "15 €"), ("il tappeto + la sedia", "blu + bianca", "40 €", "35 €"), ("tre libri (per Chiara)", "—", "2 € l'uno", "6 €")]
COLS = [(12, "COSA"), (140, "COLORE"), (232, "PREZZO"), (296, "CON LO SCONTO")]


def spesa(teacher=False):
    W, RH, top, p = 360, 24, 44, []
    H = top + RH * len(ROWS) + 26
    p.append(f'<rect width="{W}" height="{H}" rx="6" fill="#fff" stroke="{C2}" stroke-width="1.3"/>'
             f'<rect width="{W}" height="26" rx="6" fill="{C1}"/><rect y="18" width="{W}" height="8" fill="{C1}"/>'
             f'<text x="12" y="17.5" font-size="11.5" font-weight="700" fill="#fff">AL MERCATINO · CHE COSA COMPRA BRUNO?</text>')
    for x, t in COLS:
        p.append(f'<text x="{x}" y="38" font-size="8.3" font-weight="700" fill="{C1}">{t}</text>')
    for i, row in enumerate(ROWS):
        y = top + i * RH
        if i % 2 == 0:
            p.append(f'<rect x="4" y="{y}" width="{W - 8}" height="{RH}" fill="{SAND}"/>')
        p.append(f'<text x="12" y="{y + 15}" font-size="10" font-weight="700" fill="{INK}">{row[0]}</text>')
        for k, (x, _) in enumerate(COLS[1:], start=1):
            if row[k] == "—" or (i == 2 and k == 2):
                p.append(f'<text x="{x + 2}" y="{y + 15}" font-size="9.5" fill="{INK}">{row[k]}</text>')
                continue
            w = 80 if k == 1 else 52
            p.append(f'<line x1="{x}" y1="{y + 17}" x2="{x + w}" y2="{y + 17}" stroke="{INK}" stroke-width="0.8"/>')
            if teacher:
                p.append(f'<text x="{x + 3}" y="{y + 14}" font-size="10" font-weight="700" fill="{RED}">{row[k]}</text>')
    y = top + RH * len(ROWS) + 16
    p.append(f'<text x="12" y="{y}" font-size="9.5" fill="{INK}">Bruno spende in tutto:</text>'
             f'<line x1="118" y1="{y + 2}" x2="170" y2="{y + 2}" stroke="{INK}" stroke-width="0.8"/>')
    if teacher:
        p.append(f'<text x="122" y="{y}" font-size="10" font-weight="700" fill="{RED}">50 €</text>')
    return (f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:46mm">{"".join(p)}</svg>')
