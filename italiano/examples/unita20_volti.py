# Six simple flat portraits for Unità 20 (describing people) - same flat style as the other unit drawings.
F = 'font-family="Inter,sans-serif"'
SKIN = "#E9C3A0"


def face(name, hair="", hair_back="", glasses=False, beard="", moustache="", skin=SKIN):
    o = '<rect width="120" height="140" rx="8" fill="#F2F0EB"/>'
    o += hair_back
    o += '<rect x="48" y="86" width="24" height="18" fill="%s"/>' % skin  # neck
    o += '<path d="M18 140 Q20 104 60 100 Q100 104 102 140 Z" fill="#5B7FA6"/>'  # shoulders
    o += f'<ellipse cx="60" cy="62" rx="27" ry="32" fill="{skin}"/>'
    o += beard + moustache
    o += '<circle cx="50" cy="60" r="2.6" fill="#3C4448"/><circle cx="70" cy="60" r="2.6" fill="#3C4448"/>'
    o += '<path d="M52 79 Q60 84 68 79" fill="none" stroke="#9A5B4A" stroke-width="2" stroke-linecap="round"/>'
    if glasses:
        o += '<g fill="none" stroke="#3C4448" stroke-width="2"><circle cx="50" cy="60" r="7.5"/><circle cx="70" cy="60" r="7.5"/><path d="M57.5 60 H62.5"/></g>'
    o += hair
    o += f'<text x="60" y="134" text-anchor="middle" font-size="10" font-weight="700" fill="#fff" {F}>{name}</text>'
    return o


def people():
    blond, red, black, brown, grey = "#E2C26A", "#C2502E", "#2B2626", "#7A4E2D", "#B9B9B9"
    short = lambda c: f'<path d="M33 58 Q32 28 60 27 Q88 28 87 58 Q84 40 60 40 Q36 40 33 58 Z" fill="{c}"/>'
    longh = lambda c: (f'<path d="M30 60 Q28 26 60 25 Q92 26 90 60 Q86 42 60 40 Q34 42 30 60 Z" fill="{c}"/>',
                       f'<path d="M30 50 Q26 100 34 112 L86 112 Q94 100 90 50 Z" fill="{c}"/>')
    curly = "".join(f'<circle cx="{x}" cy="{y}" r="9" fill="{black}"/>' for x, y in ((38, 44), (48, 34), (60, 30), (72, 34), (82, 44), (34, 56), (86, 56)))
    beard = f'<path d="M34 68 Q38 98 60 100 Q82 98 86 68 Q80 84 60 86 Q40 84 34 68 Z" fill="{black}"/>'
    must = f'<path d="M48 74 Q60 68 72 74 Q60 72 48 74 Z" fill="{grey}" stroke="{grey}" stroke-width="3"/>'
    rows = [face("Anna", short(blond), glasses=True), face("Chiara", longh(red)[0], longh(red)[1]), face("Paolo", curly, beard=beard),
            face("Sergio", "", moustache=must), face("Lucia", longh(brown)[0], longh(brown)[1], glasses=True), face("Tommaso", short(black))]
    o = ""
    for i, r in enumerate(rows):
        o += f'<g transform="translate({i*128} 0)">{r}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 140">{o}</svg>'


def thepeople(w):
    return people().replace('viewBox="0 0 760 140">', f'viewBox="0 0 760 140" style="width:{w}mm;height:{w*140/760:.1f}mm;display:block;margin:0 auto">', 1)
