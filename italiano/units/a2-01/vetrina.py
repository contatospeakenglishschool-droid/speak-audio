# Vetrina del negozio (A2 Ponte 01): tre coppie di vestiti con il prezzo, stile pulito e adulto.

def _dress(x, y, c):
    return (f'<path d="M{x-9} {y} L{x+9} {y} L{x+12} {y+16} L{x+24} {y+72} L{x-24} {y+72} L{x-12} {y+16} Z" fill="{c}"/>'
            f'<path d="M{x-9} {y} Q{x} {y+8} {x+9} {y}" fill="none" stroke="#fff" stroke-width="1.2" opacity=".6"/>')


def _jacket(x, y, c):
    return (f'<path d="M{x-14} {y} L{x+14} {y} L{x+30} {y+10} L{x+34} {y+60} L{x+24} {y+60} L{x+22} {y+26} L{x+20} {y+70} L{x-20} {y+70} L{x-22} {y+26} L{x-24} {y+60} L{x-34} {y+60} L{x-30} {y+10} Z" fill="{c}"/>'
            f'<path d="M{x-14} {y} L{x} {y+34} L{x+14} {y}" fill="none" stroke="#fff" stroke-width="1.4" opacity=".7"/>'
            f'<circle cx="{x}" cy="{y+44}" r="1.8" fill="#fff" opacity=".8"/><circle cx="{x}" cy="{y+54}" r="1.8" fill="#fff" opacity=".8"/>')


def _shoes(x, y, c):
    one = lambda dx: (f'<path d="M{x+dx-20} {y+50} L{x+dx-20} {y+30} Q{x+dx-14} {y+26} {x+dx-6} {y+34} Q{x+dx+6} {y+42} {x+dx+20} {y+44} Q{x+dx+26} {y+46} {x+dx+24} {y+52} L{x+dx-20} {y+52} Z" fill="{c}"/>')
    return one(-12) + one(14)


def _hanger(x, y):
    return (f'<path d="M{x} {y-14} q0 -6 5 -6 q5 0 5 5 q0 4 -5 6 L{x} {y-8}" fill="none" stroke="#7d858a" stroke-width="1.3"/>'
            f'<path d="M{x-22} {y} L{x} {y-8} L{x+22} {y}" fill="none" stroke="#7d858a" stroke-width="1.6"/>')


def _tag(x, y, price):
    return (f'<rect x="{x-20}" y="{y}" width="40" height="17" rx="3" fill="#fff" stroke="#cbbca0" stroke-width="1.2"/>'
            f'<text x="{x}" y="{y+12.5}" font-size="11" font-weight="700" text-anchor="middle" fill="#0f4a5a">{price} €</text>')


def vetrina():
    items = [(_jacket, "#2b2f33", "giacca nera", 120, True), (_jacket, "#8c9296", "giacca grigia", 85, True),
             (_dress, "#1f3f73", "vestito blu", 90, True), (_dress, "#4f7d5c", "vestito verde", 65, True),
             (_shoes, "#7a4b2a", "scarpe marroni", 75, False), (_shoes, "#1d1d1f", "scarpe nere", 140, False)]
    out = []
    for i, (fn, c, label, price, hang) in enumerate(items):
        x = 52 + i * 86 + (i // 2) * 14
        top = 40
        if hang:
            out.append(_hanger(x, top))
            out.append(fn(x, top, c))
        else:
            out.append(fn(x, top + 22, c))
        out.append(_tag(x, 122, price))
        out.append(f'<text x="{x}" y="156" font-size="9.5" text-anchor="middle" fill="#3b4246" letter-spacing=".6">{label.upper()}</text>')
    seps = "".join(f'<line x1="{x}" y1="18" x2="{x}" y2="164" stroke="#d9e4e6" stroke-width="1"/>' for x in (188, 374))
    return f"""<svg viewBox="0 0 560 172" width="100%" height="47mm" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif">
<rect x="2" y="2" width="556" height="168" rx="8" fill="#f6f3ec" stroke="#cbbca0" stroke-width="1.5"/>
<line x1="12" y1="22" x2="548" y2="22" stroke="#7d858a" stroke-width="1.5"/>
<text x="280" y="15" font-size="9" text-anchor="middle" fill="#9a7b4f" letter-spacing="2" font-weight="700">BOUTIQUE INDIPENDENZA · NUOVA COLLEZIONE</text>
{seps}{"".join(out)}</svg>"""
