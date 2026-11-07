# Speak! Essenziale A1 30: enrolment form (modulo d'iscrizione) as SVG; teacher=True fills Bruno's data
C1, C2, INK, RED = "#176074", "#77acb5", "#3b4246", "#c0392b"
FIELDS = [("Cognome", "SOUZA"), ("Nome", "BRUNO"), ("Luogo di nascita", "BELO HORIZONTE (BRASILE)"), ("Data di nascita", "14 / 03 / 2006"),
          ("Nazionalità", "BRASILIANA"), ("Indirizzo a Bologna", "VIA SANTO STEFANO"), ("Corso di laurea", "STORIA"), ("E-mail", "bruno.souza@studio.unibo.it")]


def modulo(teacher=False):
    W, RH, p = 360, 24, []
    p.append(f'<rect width="{W}" height="{40 + RH * len(FIELDS) + 8}" rx="6" fill="#fff" stroke="{C2}" stroke-width="1.4"/>'
             f'<rect width="{W}" height="28" rx="6" fill="{C1}"/><rect y="20" width="{W}" height="8" fill="{C1}"/>'
             f'<text x="12" y="19" font-size="11.5" font-weight="700" fill="#fff">UNIVERSITÀ DI BOLOGNA · MODULO D\'ISCRIZIONE</text>')
    for i, (lab, val) in enumerate(FIELDS):
        y = 40 + i * RH
        p.append(f'<text x="12" y="{y + 12}" font-size="9.5" fill="{INK}">{lab}</text>'
                 f'<line x1="120" y1="{y + 15}" x2="{W - 12}" y2="{y + 15}" stroke="{C2}" stroke-width="1"/>')
        if teacher:
            p.append(f'<text x="124" y="{y + 12}" font-size="10" fill="{RED}" font-weight="700">{val}</text>')
    return (f'<svg viewBox="0 0 {W} {40 + RH * len(FIELDS) + 8}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:70mm">{"".join(p)}</svg>')
