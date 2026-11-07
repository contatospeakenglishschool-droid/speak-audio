# Speak! Essenziale A1 29: four room ads (invented) as cards
C1, C2, C3, INK = "#176074", "#77acb5", "#cbbca0", "#3b4246"
ADS = [("1", "via San Vitale", "stanza singola · 14 m²", "350 €/mese", "spese escluse (circa 60 €)", "cauzione 2 mesi"),
       ("2", "via Mascarella", "monolocale · 28 m²", "480 €/mese", "spese incluse", "cauzione 3 mesi"),
       ("3", "via Zamboni", "stanza singola · 12 m²", "380 €/mese", "spese incluse", "cauzione 1 mese"),
       ("4", "Bolognina", "stanza doppia · 20 m²", "260 €/mese", "spese escluse (circa 50 €)", "cauzione 2 mesi")]


def annunci():
    W, H, G = 170, 92, 10
    p = []
    for i, (n, via, tipo, prezzo, spese, cauz) in enumerate(ADS):
        x, y = (i % 2) * (W + G), (i // 2) * (H + G)
        p.append(f'<g transform="translate({x},{y})"><rect width="{W}" height="{H}" rx="8" fill="#fff" stroke="{C2}" stroke-width="1.4"/>'
                 f'<rect width="{W}" height="22" rx="8" fill="{C1}"/><rect y="12" width="{W}" height="10" fill="{C1}"/>'
                 f'<text x="10" y="15" font-size="10.5" font-weight="700" fill="#fff">AFFITTASI · {n}</text>'
                 f'<text x="{W - 10}" y="15" font-size="10.5" font-weight="700" fill="#fff" text-anchor="end">{prezzo}</text>'
                 f'<text x="10" y="38" font-size="10.5" font-weight="700" fill="{INK}">{via}</text>'
                 f'<text x="10" y="54" font-size="9.5" fill="{INK}">{tipo}</text>'
                 f'<text x="10" y="69" font-size="9.5" fill="{INK}">{spese}</text>'
                 f'<text x="10" y="84" font-size="9.5" fill="#9a7b4f">{cauz}</text></g>')
    return (f'<svg viewBox="0 0 {2 * W + G} {2 * H + G}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:80mm">{"".join(p)}</svg>')
