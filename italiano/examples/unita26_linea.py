# Júlia's year in Bologna for Unità 26 - a timeline from June to June, drawn as SVG.
EVENTS = [("giugno", "arriva a Bologna", "#2E7FA8"), ("luglio", "cinema in piazza Maggiore", "#F2C14E"), ("dicembre", "i genitori a Bologna · Firenze", "#E07A5F"),
          ("febbraio", "arriva Bruno", "#2E7FA8"), ("Pasqua", "Napoli e Capri", "#F2C14E"), ("giugno", "festa junina · un anno!", "#E07A5F")]


def timeline():
    w, n = 600, len(EVENTS)
    xs = [40 + i * (w - 80) / (n - 1) for i in range(n)]
    parts = [f'<line x1="20" y1="44" x2="{w - 20}" y2="44" stroke="#1F5F6B" stroke-width="3"/>',
             f'<path d="M{w - 20} 38 L{w - 8} 44 L{w - 20} 50 Z" fill="#1F5F6B"/>']
    for i, ((m, t, c), x) in enumerate(zip(EVENTS, xs)):
        parts.append(f'<circle cx="{x:.0f}" cy="44" r="9" fill="{c}" stroke="#fff" stroke-width="2"/>'
                     f'<text x="{x:.0f}" y="48" text-anchor="middle" font-size="10" font-weight="800" fill="#fff">{i + 1}</text>'
                     f'<text x="{x:.0f}" y="24" text-anchor="middle" font-size="12" font-weight="800" fill="#1F5F6B">{m}</text>')
        words, lines, cur = t.split(" "), [], ""
        for wd in words:
            if len(cur) + len(wd) > 14 and cur:
                lines.append(cur); cur = wd
            else:
                cur = (cur + " " + wd).strip()
        lines.append(cur)
        for j, ln in enumerate(lines):
            parts.append(f'<text x="{x:.0f}" y="{70 + j * 13}" text-anchor="middle" font-size="10.5" fill="#333">{ln}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 110" style="width:100%;display:block;margin:1mm 0 2mm;'
            f'background:#FBF8F1;border:0.4mm solid #C9A96E;border-radius:2mm;font-family:Inter,sans-serif">{"".join(parts)}</svg>')
