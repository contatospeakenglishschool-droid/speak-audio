# Clean, adult street-map style (Google-Maps-like): muted palette, white roads, labeled blocks, black X = you are here.
F = 'font-family="Inter,sans-serif"'
def bld(x, y, w, h, label, fill="#E4E1DA", label2=""):
    t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="1.5" fill="{fill}" stroke="#C9C4BA" stroke-width=".8"/>'
    if label:
        cy = y + h / 2 + (0 if label2 else 3)
        t += f'<text x="{x+w/2}" y="{cy}" text-anchor="middle" font-size="7" font-weight="700" fill="#3C4448" letter-spacing=".3" {F}>{label}</text>'
        if label2:
            t += f'<text x="{x+w/2}" y="{cy+8}" text-anchor="middle" font-size="7" font-weight="700" fill="#3C4448" letter-spacing=".3" {F}>{label2}</text>'
    return t
def light(x, y):
    return (f'<rect x="{x-2.5}" y="{y-7}" width="5" height="13" rx="1.2" fill="#3C4448"/>'
            f'<circle cx="{x}" cy="{y-4}" r="1.3" fill="#D9534F"/><circle cx="{x}" cy="{y-.5}" r="1.3" fill="#E8B84A"/><circle cx="{x}" cy="{y+3}" r="1.3" fill="#5BA36B"/>')
def townmap():
    o = '<rect width="400" height="260" fill="#F2F0EB"/>'
    # roads (white with light outline)
    for r in ['<rect x="-2" y="118" width="404" height="26"/>', '<rect x="170" y="-2" width="26" height="264"/>', '<rect x="300" y="-2" width="26" height="264"/>']:
        o += r.replace('/>', ' fill="#FFFFFF" stroke="#D3CEC4" stroke-width="1"/>')
    o += '<rect x="171" y="119" width="24" height="24" fill="#fff"/><rect x="301" y="119" width="24" height="24" fill="#fff"/>'
    o += f'<text x="70" y="133.5" font-size="6.5" fill="#8A9094" font-weight="600" letter-spacing="1" {F}>MAIN STREET</text>'
    o += f'<text x="186" y="30" font-size="6.5" fill="#8A9094" font-weight="600" letter-spacing="1" {F} transform="rotate(90 186 30)">OAK STREET</text>'
    o += f'<text x="316" y="190" font-size="6.5" fill="#8A9094" font-weight="600" letter-spacing="1" {F} transform="rotate(90 316 190)">LAKE STREET</text>'
    # crosswalks
    for x0, y0, vert in [(160, 120, True), (198, 120, True), (290, 120, True), (328, 120, True)]:
        o += "".join(f'<rect x="{x0}" y="{y0+2+i*4}" width="8" height="2" fill="#D3CEC4"/>' for i in range(5))
    # blocks
    o += bld(8, 8, 158, 54, "", "#E9E6DF") + bld(200, 8, 96, 54, "", "#E9E6DF") + bld(330, 8, 64, 26, "", "#E9E6DF")
    o += bld(8, 66, 50, 48, "BAKERY") + bld(62, 66, 52, 48, "POST", label2="OFFICE") + bld(118, 66, 48, 48, "BANK")
    o += bld(200, 66, 50, 48, "MOVIE", label2="THEATER") + bld(254, 66, 42, 48, "CAFÉ")
    o += bld(330, 40, 64, 74, "MUSEUM")
    o += bld(8, 148, 50, 46, "PHARMACY") + bld(62, 148, 104, 46, "HOTEL")
    o += bld(8, 198, 158, 54, "", "#E9E6DF")
    o += f'<rect x="200" y="148" width="50" height="104" rx="1.5" fill="#CFE3C8" stroke="#B5CDAC" stroke-width=".8"/><text x="225" y="203" text-anchor="middle" font-size="7" font-weight="700" fill="#3F6B45" letter-spacing=".3" {F}>PARK</text>'
    o += bld(254, 148, 42, 60, "SUPER-", label2="MARKET") + bld(254, 212, 42, 40, "", "#E9E6DF")
    o += bld(330, 148, 64, 104, "", "#E9E6DF")
    # traffic lights
    o += light(165, 112) + light(295, 112)
    # you are here: black X
    o += '<g stroke="#111" stroke-width="3.2" stroke-linecap="round"><line x1="24" y1="125" x2="36" y2="137"/><line x1="36" y1="125" x2="24" y2="137"/></g>'
    o += (f'<rect x="10" y="232" width="74" height="16" rx="2" fill="#fff" stroke="#3C4448" stroke-width=".8"/>'
          f'<g stroke="#111" stroke-width="2" stroke-linecap="round"><line x1="16" y1="236" x2="24" y2="244"/><line x1="24" y1="236" x2="16" y2="244"/></g>'
          f'<text x="29" y="243" font-size="7" font-weight="700" fill="#111" {F}>= You are here</text>')
    o += f'<text x="392" y="254" text-anchor="end" font-size="6.5" fill="#8A9094" {F}>N ↑</text>'
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">' + o + '</svg>'
if __name__ == "__main__":
    open("/home/claude/u21/townmap.svg", "w").write(townmap())
