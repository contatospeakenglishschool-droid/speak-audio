# Speak! Essenziale A1 33: programme of a fictional cinema; genres and student price blank, teacher=True fills them in red
C1, C2, INK, RED, SAND = "#176074", "#77acb5", "#3b4246", "#c0392b", "#f3ede3"
FILMS = [("Il silenzio della casa", "horror", "22:30"), ("Pianeta rosso", "fantascienza", "20:00 · 22:40"),
         ("Notte a Napoli", "giallo", "18:30 · 21:15"), ("Il cane di Marta", "commedia", "17:00 · 19:30 · 22:00")]


def programma(teacher=False):
    W, RH, top, p = 360, 21, 46, []
    H = top + RH * len(FILMS) + 30
    p.append(f'<rect width="{W}" height="{H}" rx="6" fill="#fff" stroke="{C2}" stroke-width="1.3"/>'
             f'<rect width="{W}" height="26" rx="6" fill="{C1}"/><rect y="18" width="{W}" height="8" fill="{C1}"/>'
             f'<text x="12" y="17.5" font-size="11.5" font-weight="700" fill="#fff">CINEMA DUE TORRI · PROGRAMMA DI VENERDÌ</text>'
             f'<text x="12" y="40" font-size="8.5" font-weight="700" fill="{C1}">FILM</text>'
             f'<text x="160" y="40" font-size="8.5" font-weight="700" fill="{C1}">GENERE</text>'
             f'<text x="252" y="40" font-size="8.5" font-weight="700" fill="{C1}">ORARI</text>')
    for i, (t, g, o) in enumerate(FILMS):
        y = top + i * RH
        if i % 2 == 0:
            p.append(f'<rect x="4" y="{y - 2}" width="{W - 8}" height="{RH}" fill="{SAND}"/>')
        p.append(f'<text x="12" y="{y + 12}" font-size="10" font-weight="700" fill="{INK}">{t}</text>'
                 f'<line x1="160" y1="{y + 14}" x2="240" y2="{y + 14}" stroke="{INK}" stroke-width="0.8"/>'
                 f'<text x="252" y="{y + 12}" font-size="9.5" fill="{INK}">{o}</text>')
        if teacher:
            p.append(f'<text x="164" y="{y + 12}" font-size="10" font-weight="700" fill="{RED}">{g}</text>')
    y = top + RH * len(FILMS) + 14
    p.append(f'<text x="12" y="{y}" font-size="9.5" fill="{INK}">Biglietto intero: 9 €  ·  Ridotto studenti:</text>'
             f'<line x1="196" y1="{y + 2}" x2="226" y2="{y + 2}" stroke="{INK}" stroke-width="0.8"/><text x="230" y="{y}" font-size="9.5" fill="{INK}">€</text>')
    if teacher:
        p.append(f'<text x="211" y="{y}" font-size="10" font-weight="700" fill="{RED}" text-anchor="middle">6</text>')
    return (f'<svg viewBox="0 0 {W} {H}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:50mm">{"".join(p)}</svg>')
