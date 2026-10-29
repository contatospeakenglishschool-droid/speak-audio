# Front view of a living room for Unità 15 (prepositions of place) - same flat style as the Unità 07 map.
F = 'font-family="Inter,sans-serif"'


def lab(x, y, t, c="#3C4448"):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="7" font-weight="700" fill="{c}" letter-spacing=".4" {F}>{t}</text>'


def stanza():
    o = '<rect width="400" height="220" fill="#F2F0EB"/>'
    o += '<rect x="0" y="190" width="400" height="30" fill="#E4E1DA"/>'
    # window above the sofa
    o += '<rect x="150" y="22" width="100" height="78" rx="2" fill="#DCE9EE" stroke="#9FB3BB" stroke-width="2"/>'
    o += '<line x1="200" y1="22" x2="200" y2="100" stroke="#9FB3BB" stroke-width="2"/><line x1="150" y1="61" x2="250" y2="61" stroke="#9FB3BB" stroke-width="2"/>'
    o += lab(200, 15, "FINESTRA")
    # picture above the small table
    o += '<rect x="42" y="45" width="56" height="42" rx="1.5" fill="#fff" stroke="#8A7B66" stroke-width="3"/>'
    o += '<path d="M48 80 L62 62 L72 72 L80 64 L92 80 Z" fill="#B9C9A3"/><circle cx="84" cy="55" r="5" fill="#E8C468"/>'
    o += lab(70, 38, "QUADRO")
    # sofa (red) under the window
    o += '<rect x="128" y="128" width="144" height="26" rx="6" fill="#B84A3A"/>'
    o += '<rect x="120" y="148" width="160" height="32" rx="6" fill="#C8553D"/>'
    o += '<rect x="126" y="180" width="8" height="10" fill="#6B4F3A"/><rect x="266" y="180" width="8" height="10" fill="#6B4F3A"/>'
    o += lab(200, 169, "DIVANO", "#fff")
    # rug in front of the sofa
    o += '<ellipse cx="200" cy="203" rx="78" ry="9" fill="#5B7FA6"/>'
    o += lab(200, 205.5, "TAPPETO", "#fff")
    # small table with a plant on it and a cat under it
    o += '<rect x="34" y="142" width="72" height="6" rx="1" fill="#8A6A4F"/><rect x="40" y="148" width="5" height="42" fill="#8A6A4F"/><rect x="95" y="148" width="5" height="42" fill="#8A6A4F"/>'
    o += '<rect x="62" y="124" width="16" height="18" rx="2" fill="#B57A52"/><ellipse cx="64" cy="114" rx="9" ry="12" fill="#5E8C5A"/><ellipse cx="77" cy="112" rx="8" ry="13" fill="#6FA06A"/>'
    o += lab(70, 97, "PIANTA") + lab(70, 159, "TAVOLINO")
    o += '<ellipse cx="70" cy="183" rx="15" ry="7" fill="#7A7A7A"/><circle cx="83" cy="176" r="6" fill="#7A7A7A"/>'
    o += '<path d="M79 171 L80 165 L83 170 Z M84 170 L87 165 L88 171 Z" fill="#7A7A7A"/>'
    o += lab(70, 202, "GATTO")
    # floor lamp next to the sofa
    o += '<path d="M290 72 L318 72 L312 52 L296 52 Z" fill="#E8C468"/><rect x="302" y="72" width="4" height="114" fill="#555"/><rect x="292" y="186" width="24" height="4" rx="1" fill="#555"/>'
    o += lab(304, 45, "LAMPADA")
    # bookcase on the right
    o += '<rect x="336" y="40" width="52" height="150" fill="#A98463"/>'
    for i, y in enumerate((48, 86, 124, 162)):
        o += f'<rect x="341" y="{y}" width="42" height="30" fill="#EFE6D8"/>'
        o += "".join(f'<rect x="{344+j*7}" y="{y+8-(j%2)*3}" width="5" height="{22+(j%2)*3}" fill="{["#5B7FA6","#C8553D","#5E8C5A","#E8C468","#8A6A4F"][(i+j)%5]}"/>' for j in range(5))
    o += lab(362, 33, "LIBRERIA")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 220">{o}</svg>'


def thestanza(h):
    return stanza().replace('viewBox="0 0 400 220">', f'viewBox="0 0 400 220" style="width:{h*400/220:.0f}mm;height:{h}mm;display:block;margin:0 auto;border-radius:2mm">', 1)
