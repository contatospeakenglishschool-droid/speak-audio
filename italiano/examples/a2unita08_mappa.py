# Speak! Ponte A2 08: small invented town map for asking and giving directions (Lei)
C1, C2, C3, INK, ROAD = "#176074", "#77acb5", "#cbbca0", "#3b4246", "#e9e4da"
# blocks: (col, row, label)
BLOCKS = [(0, 0, "stazione"), (1, 0, "albergo"), (2, 0, "museo"), (0, 1, "farmacia"), (1, 1, "PIAZZA"), (2, 1, "banca"),
          (0, 2, "ufficio postale"), (1, 2, "chiesa"), (2, 2, "supermercato"), (3, 0, "cinema"), (3, 1, "ospedale"), (3, 2, "trattoria")]


def mappa():
    X0, Y0, BW, BH, R = 24, 24, 110, 62, 22
    p = [f'<rect x="0" y="0" width="{X0 + 4 * (BW + R) + 2}" height="{Y0 + 3 * (BH + R) + 2}" fill="{ROAD}" rx="8"/>']
    for c, r, lab in BLOCKS:
        x, y = X0 + c * (BW + R), Y0 + r * (BH + R)
        sq = lab == "PIAZZA"
        p.append(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="5" fill="{"#f6f3ec" if sq else "#fff"}" stroke="{C2}" stroke-width="1.2"/>'
                 f'<text x="{x + BW / 2}" y="{y + BH / 2 + 4}" font-size="{11 if not sq else 12}" fill="{C1 if sq else INK}" text-anchor="middle" font-weight="{700 if sq else 600}">{lab}</text>')
    streets = [("via Roma", X0 - 6, Y0 + BH + R / 2 + 3.5, 0), ("via Dante", X0 - 6, Y0 + 2 * BH + 1.5 * R + 3.5, 0),
               ("via Verdi", X0 + BW + R / 2 + 3.5, Y0 + 2, 90), ("corso Garibaldi", X0 + 2 * BW + 1.5 * R + 3.5, Y0 + 2, 90), ("via Manzoni", X0 + 3 * BW + 2.5 * R + 3.5, Y0 + 2, 90)]
    for name, x, y, rot in streets:
        if rot:
            p.append(f'<text x="{x}" y="{y + 40}" font-size="8.5" fill="#9a7b4f" font-style="italic" transform="rotate(90 {x} {y + 40})">{name}</text>')
        else:
            p.append(f'<text x="{x + 30}" y="{y}" font-size="8.5" fill="#9a7b4f" font-style="italic">{name}</text>')
    sx, sy = X0 + BW / 2, Y0 + 3 * (BH + R) - R / 2 + 1
    p.append(f'<circle cx="{sx}" cy="{sy}" r="7" fill="#c0392b"/><text x="{sx + 11}" y="{sy + 4}" font-size="10" font-weight="700" fill="#c0392b">SEI QUI</text>')
    W = X0 + 4 * (BW + R) + 2
    return (f'<svg viewBox="0 0 {W} {Y0 + 3 * (BH + R) + 2}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:64mm">{"".join(p)}</svg>')
