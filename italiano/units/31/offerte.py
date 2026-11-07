# Speak! Essenziale A1 31: three phone offers (fictional operator); teacher=True fills giga and price in red
C1, C2, INK, RED, SAND = "#176074", "#77acb5", "#3b4246", "#c0392b", "#f3ede3"
OFFERS = [("GIGA 150", "150", "minuti e SMS illimitati", "9,99"),
          ("MONDO 50", "50", "200 minuti verso l'estero", "12,99"),
          ("BASE 20", "20", "500 minuti", "5,99")]


def offerte(teacher=False):
    W, H, cw, gap, p = 360, 118, 112, 12, []
    p.append(f'<text x="0" y="12" font-size="11" font-weight="700" fill="{C1}">LINEAPIÙ · LE NOSTRE OFFERTE</text>')
    for i, (name, gb, extra, price) in enumerate(OFFERS):
        x = i * (cw + gap)
        p.append(f'<rect x="{x}" y="20" width="{cw}" height="{H - 22}" rx="7" fill="{SAND}" stroke="{C2}" stroke-width="1.3"/>'
                 f'<rect x="{x}" y="20" width="{cw}" height="22" rx="7" fill="{C1}"/><rect x="{x}" y="34" width="{cw}" height="8" fill="{C1}"/>'
                 f'<text x="{x + cw / 2}" y="35" font-size="11" font-weight="700" fill="#fff" text-anchor="middle">{name}</text>'
                 f'<line x1="{x + 14}" y1="64" x2="{x + 54}" y2="64" stroke="{INK}" stroke-width="0.9"/>'
                 f'<text x="{x + 58}" y="63" font-size="10" fill="{INK}">giga</text>'
                 f'<text x="{x + cw / 2}" y="80" font-size="8.6" fill="{INK}" text-anchor="middle">{extra}</text>'
                 f'<line x1="{x + 14}" y1="104" x2="{x + 54}" y2="104" stroke="{INK}" stroke-width="0.9"/>'
                 f'<text x="{x + 58}" y="103" font-size="10" fill="{INK}">€ al mese</text>')
        if teacher:
            p.append(f'<text x="{x + 34}" y="61" font-size="11" font-weight="700" fill="{RED}" text-anchor="middle">{gb}</text>'
                     f'<text x="{x + 34}" y="101" font-size="11" font-weight="700" fill="{RED}" text-anchor="middle">{price}</text>')
    return (f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:46mm">{"".join(p)}</svg>')
