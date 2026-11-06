# Fumetto in 4 vignette (A2 Ponte 03): «La giornata storta di Davide». Stile pulito, linee sottili, colori tenui.
C1, C2, C3, INK = "#176074", "#77acb5", "#cbbca0", "#3b4246"


def _panel(x, n, label, body):
    return (f'<g transform="translate({x},0)"><rect x="2" y="2" width="128" height="118" rx="6" fill="#fff" stroke="{C2}" stroke-width="1.4"/>'
            f'<circle cx="16" cy="16" r="9" fill="{C1}"/><text x="16" y="20" font-size="11" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>'
            f'{body}<text x="66" y="112" font-size="9" fill="{INK}" text-anchor="middle" letter-spacing=".5">{label}</text></g>')


def fumetto():
    clock = (f'<circle cx="66" cy="54" r="26" fill="#f6f3ec" stroke="{INK}" stroke-width="2"/><line x1="66" y1="54" x2="66" y2="38" stroke="{INK}" stroke-width="2.4"/>'
             f'<line x1="66" y1="54" x2="80" y2="58" stroke="{INK}" stroke-width="2"/><circle cx="48" cy="26" r="6" fill="{C3}"/><circle cx="84" cy="26" r="6" fill="{C3}"/>'
             f'<text x="104" y="40" font-size="10" fill="{C1}" font-weight="700">zzz</text>')
    rain = "".join(f'<line x1="{x}" y1="{y}" x2="{x-4}" y2="{y+9}" stroke="{C2}" stroke-width="1.5"/>' for x, y in [(30, 28), (52, 22), (74, 30), (96, 24), (110, 34), (40, 40), (88, 40)])
    bus = (f'{rain}<rect x="26" y="50" width="80" height="34" rx="5" fill="{C1}"/><rect x="32" y="56" width="16" height="12" fill="#fff" opacity=".85"/>'
           f'<rect x="52" y="56" width="16" height="12" fill="#fff" opacity=".85"/><rect x="72" y="56" width="16" height="12" fill="#fff" opacity=".85"/>'
           f'<circle cx="42" cy="86" r="6" fill="{INK}"/><circle cx="90" cy="86" r="6" fill="{INK}"/><text x="112" y="16" font-size="9" fill="{INK}" text-anchor="end">8:40</text>')
    phone = (f'<rect x="46" y="30" width="40" height="66" rx="6" fill="{INK}"/><rect x="50" y="38" width="32" height="50" rx="2" fill="#fff"/>'
             f'<rect x="53" y="44" width="26" height="16" rx="3" fill="{C3}"/><text x="66" y="55" font-size="5.2" fill="{INK}" text-anchor="middle">LEZIONE</text>'
             f'<text x="66" y="70" font-size="5.2" fill="#b0413e" text-anchor="middle" font-weight="700">ANNULLATA</text>')
    bed = (f'<rect x="20" y="62" width="92" height="20" rx="3" fill="{C2}"/><rect x="20" y="52" width="10" height="38" fill="{INK}"/><rect x="104" y="58" width="8" height="32" fill="{INK}"/>'
           f'<ellipse cx="42" cy="58" rx="12" ry="7" fill="#fff" stroke="{C2}"/><circle cx="44" cy="52" r="8" fill="{C3}"/>'
           f'<text x="66" y="40" font-size="12" fill="{C1}" font-weight="700">zzz</text><circle cx="100" cy="28" r="9" fill="#e9c46a"/>')
    ps = [("SVEGLIA ALLE 8:15", clock), ("AUTOBUS IN RITARDO", bus), ("UN MESSAGGIO", phone), ("A CASA, A LETTO", bed)]
    g = "".join(_panel(4 + i * 136, i + 1, l, body) for i, (l, body) in enumerate(ps))
    return f'<svg viewBox="0 0 552 124" width="100%" height="44mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">{g}</svg>'
