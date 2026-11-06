# Speak! Ponte A2 07: Júlia's February 2027 calendar (Feb 1 = Monday, 28 days, 4 weeks)
C1, C2, C3, INK = "#176074", "#77acb5", "#cbbca0", "#3b4246"
EV = {5: ("partenza", "Bologna → BH"), 6: ("arrivo:", "festa in famiglia"), 9: ("Carnevale", "con le cugine"),
      14: ("compleanno", "della mamma"), 16: ("gita a", "Ouro Preto"), 19: ("ritorno", "a Bologna"), 26: ("arrivano", "Luca e Sara")}
DAYS = ["lun", "mar", "mer", "gio", "ven", "sab", "dom"]


def calendario():
    W, H, X0, Y0 = 74, 50, 4, 40
    p = [f'<text x="{X0 + 3.5 * W}" y="16" font-size="15" font-weight="700" fill="{C1}" text-anchor="middle">FEBBRAIO · l\'agenda di Júlia</text>']
    for i, d in enumerate(DAYS):
        p.append(f'<text x="{X0 + i * W + W / 2}" y="{Y0 - 6}" font-size="10" fill="{INK}" text-anchor="middle" font-weight="700">{d}</text>')
    for n in range(1, 29):
        r, c = divmod(n - 1, 7)
        x, y = X0 + c * W, Y0 + r * H
        ev = EV.get(n)
        fill = "#e8f1f2" if ev else "#fff"
        p.append(f'<rect x="{x}" y="{y}" width="{W - 3}" height="{H - 3}" rx="4" fill="{fill}" stroke="{C2}" stroke-width="1"/>'
                 f'<text x="{x + 5}" y="{y + 13}" font-size="11" font-weight="700" fill="{C1 if ev else INK}">{n}</text>')
        if ev:
            p.append(f'<text x="{x + W / 2 - 1}" y="{y + 28}" font-size="8.6" fill="{INK}" text-anchor="middle" font-weight="700">{ev[0]}</text>'
                     f'<text x="{x + W / 2 - 1}" y="{y + 39}" font-size="8.2" fill="{INK}" text-anchor="middle">{ev[1]}</text>')
    return (f'<svg viewBox="0 0 {X0 * 2 + 7 * W} {Y0 + 4 * H + 2}" width="100%" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Inter, sans-serif" style="display:block;max-height:86mm">{"".join(p)}</svg>')
