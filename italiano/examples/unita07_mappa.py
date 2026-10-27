# Italian town map for Unità 07 - same clean street-map style as engine/examples/unit21_townmap.py, Italian labels.
F = 'font-family="Inter,sans-serif"'


def bld(x, y, w, h, label, fill="#E4E1DA", label2=""):
    t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="{fill}" stroke="#C9C4BA" stroke-width=".8"/>'
    if label:
        cy = y + h / 2 + (0 if label2 else 3)
        t += f'<text x="{x+w/2}" y="{cy}" text-anchor="middle" font-size="6.6" font-weight="700" fill="#3C4448" letter-spacing=".3" {F}>{label}</text>'
        if label2:
            t += f'<text x="{x+w/2}" y="{cy+8}" text-anchor="middle" font-size="6.6" font-weight="700" fill="#3C4448" letter-spacing=".3" {F}>{label2}</text>'
    return t


def mappa():
    o = '<rect width="400" height="260" fill="#F2F0EB"/>'
    for r in ['<rect x="-2" y="118" width="404" height="26"/>', '<rect x="170" y="-2" width="26" height="264"/>', '<rect x="300" y="-2" width="26" height="264"/>']:
        o += r.replace('/>', ' fill="#FFFFFF" stroke="#D3CEC4" stroke-width="1"/>')
    o += '<rect x="171" y="119" width="24" height="24" fill="#fff"/><rect x="301" y="119" width="24" height="24" fill="#fff"/>'
    o += f'<text x="74" y="133.5" font-size="6.5" fill="#8A9094" font-weight="600" letter-spacing="1" {F}>VIA ROMA</text>'
    o += f'<text x="186" y="22" font-size="6.5" fill="#8A9094" font-weight="600" letter-spacing="1" {F} transform="rotate(90 186 22)">VIA VERDI</text>'
    o += f'<text x="316" y="182" font-size="6.5" fill="#8A9094" font-weight="600" letter-spacing="1" {F} transform="rotate(90 316 182)">VIA DANTE</text>'
    for x0 in (160, 198, 290, 328):
        o += "".join(f'<rect x="{x0}" y="{122+i*4}" width="8" height="2" fill="#D3CEC4"/>' for i in range(5))
    # north side of Via Roma (left when you walk east from the X)
    o += bld(8, 8, 158, 54, "", "#E9E6DF") + bld(200, 8, 96, 54, "", "#E9E6DF") + bld(330, 8, 64, 26, "", "#E9E6DF")
    o += bld(8, 66, 50, 48, "FORNO") + bld(62, 66, 52, 48, "BANCA") + bld(118, 66, 48, 48, "BAR")
    o += bld(200, 66, 50, 48, "CHIESA") + bld(254, 66, 42, 48, "FARMA-", label2="CIA")
    o += bld(330, 40, 64, 74, "MUSEO")
    # south side of Via Roma (right)
    o += bld(8, 148, 106, 46, "UFFICIO", label2="POSTALE") + bld(118, 148, 48, 46, "ALBERGO")
    o += bld(8, 198, 158, 54, "", "#E9E6DF")
    o += f'<rect x="200" y="148" width="50" height="104" rx="1.5" fill="#E6DCC6" stroke="#CDBF9F" stroke-width=".8"/><text x="225" y="203" text-anchor="middle" font-size="6.6" font-weight="700" fill="#6B5A35" letter-spacing=".3" {F}>PIAZZA</text>'
    o += bld(254, 148, 42, 60, "SUPER-", label2="MERCATO") + bld(254, 212, 42, 40, "", "#E9E6DF")
    o += bld(330, 148, 64, 104, "STAZIONE", "#DCE5E8")
    o += '<g stroke="#111" stroke-width="3.2" stroke-linecap="round"><line x1="24" y1="125" x2="36" y2="137"/><line x1="36" y1="125" x2="24" y2="137"/></g>'
    o += (f'<rect x="10" y="232" width="76" height="16" rx="2" fill="#fff" stroke="#3C4448" stroke-width=".8"/>'
          f'<g stroke="#111" stroke-width="2" stroke-linecap="round"><line x1="16" y1="236" x2="24" y2="244"/><line x1="24" y1="236" x2="16" y2="244"/></g>'
          f'<text x="29" y="243" font-size="7" font-weight="700" fill="#111" {F}>= Tu sei qui</text>')
    o += f'<text x="392" y="254" text-anchor="end" font-size="6.5" fill="#8A9094" {F}>N ↑</text>'
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">' + o + '</svg>'


def themap(h):
    return mappa().replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">',
                           f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260" style="width:{h*400/260:.0f}mm;height:{h}mm;display:block;margin:0 auto;border-radius:2mm">')
