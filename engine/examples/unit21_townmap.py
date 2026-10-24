def bld(x, y, w, h, c, label, icon=""):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{c}" stroke="#0f4a5a" stroke-width="1"/>'
            f'<text x="{x+w/2}" y="{y+h/2+3}" text-anchor="middle" font-size="7.6" font-weight="800" fill="#0f4a5a" font-family="Inter,sans-serif">{label}</text>')
def light(x, y):
    return (f'<rect x="{x-3}" y="{y-9}" width="6" height="16" rx="2" fill="#1f2528"/>'
            f'<circle cx="{x}" cy="{y-5}" r="1.8" fill="#E53935"/><circle cx="{x}" cy="{y-1}" r="1.8" fill="#FFC72C"/><circle cx="{x}" cy="{y+3}" r="1.8" fill="#27AE60"/>')
def townmap():
    o = '<rect width="400" height="260" fill="#EEF3E8"/>'
    # roads
    o += '<rect x="0" y="118" width="400" height="26" fill="#9AA5AB"/><rect x="170" y="0" width="26" height="260" fill="#9AA5AB"/><rect x="300" y="0" width="26" height="260" fill="#9AA5AB"/>'
    o += '<line x1="0" y1="131" x2="400" y2="131" stroke="#fff" stroke-width="1.5" stroke-dasharray="6 5"/>'
    o += '<line x1="183" y1="0" x2="183" y2="260" stroke="#fff" stroke-width="1.5" stroke-dasharray="6 5"/><line x1="313" y1="0" x2="313" y2="260" stroke="#fff" stroke-width="1.5" stroke-dasharray="6 5"/>'
    o += '<text x="70" y="128" font-size="7" fill="#fff" font-weight="700" font-family="Inter,sans-serif">MAIN STREET</text>'
    o += '<text x="187" y="40" font-size="7" fill="#fff" font-weight="700" font-family="Inter,sans-serif" transform="rotate(90 187 40)">OAK STREET</text>'
    o += '<text x="317" y="200" font-size="7" fill="#fff" font-weight="700" font-family="Inter,sans-serif" transform="rotate(90 317 200)">LAKE STREET</text>'
    # top-left block
    o += bld(8, 66, 50, 48, "#F7D9A8", "BAKERY") + bld(62, 66, 52, 48, "#D9E4F5", "POST OFFICE") + bld(118, 66, 48, 48, "#C8E6C9", "BANK")
    o += bld(8, 10, 158, 50, "#E8E2D6", "")  # houses
    o += '<text x="87" y="38" text-anchor="middle" font-size="7" fill="#7d858a" font-family="Inter,sans-serif">houses</text>'
    # top-middle block
    o += bld(200, 66, 50, 48, "#F8C8C8", "MOVIE THEATER".replace(" THEATER", "")) + bld(254, 66, 42, 48, "#FFE7B3", "CAFÉ")
    o += '<text x="225" y="104" text-anchor="middle" font-size="6.6" font-weight="800" fill="#0f4a5a" font-family="Inter,sans-serif">THEATER</text>'
    o += bld(200, 10, 96, 50, "#E8E2D6", "")
    # top-right block
    o += bld(330, 40, 64, 74, "#E1D5F2", "MUSEUM")
    # bottom-left block
    o += bld(8, 148, 50, 46, "#D7F0EE", "PHARMACY") + bld(62, 148, 104, 46, "#F3E5C8", "HOTEL")
    # bottom-middle: park + supermarket
    o += '<rect x="200" y="148" width="50" height="104" rx="3" fill="#A5D6A7" stroke="#0f4a5a" stroke-width="1"/>'
    o += "".join(f'<circle cx="{x}" cy="{y}" r="7" fill="#66BB6A"/>' for x, y in [(212, 165), (236, 180), (214, 210), (238, 232)])
    o += '<text x="225" y="200" text-anchor="middle" font-size="7.6" font-weight="800" fill="#0f4a5a" font-family="Inter,sans-serif">PARK</text>'
    o += bld(254, 148, 42, 60, "#FFD8B0", "SUPER-") + '<text x="275" y="190" text-anchor="middle" font-size="7.6" font-weight="800" fill="#0f4a5a" font-family="Inter,sans-serif">MARKET</text>'
    o += bld(330, 148, 64, 46, "#E8E2D6", "") + '<text x="362" y="174" text-anchor="middle" font-size="7" fill="#7d858a" font-family="Inter,sans-serif">houses</text>'
    # traffic lights
    o += light(166, 112) + light(296, 112)
    # you are here
    o += '<polygon points="30,123 33,129 40,129 34.5,133 36.5,140 30,136 23.5,140 25.5,133 20,129 27,129" fill="#E53935" stroke="#fff" stroke-width="1"/>'
    o += '<rect x="8" y="228" width="80" height="18" rx="3" fill="#fff" stroke="#E53935"/><text x="48" y="240" text-anchor="middle" font-size="7.5" font-weight="800" fill="#E53935" font-family="Inter,sans-serif">★ = YOU ARE HERE</text>'
    # compass arrow east
    o += '<text x="360" y="252" font-size="7" fill="#0f4a5a" font-family="Inter,sans-serif">walking →</text>'
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 260">' + o + '</svg>'
if __name__ == "__main__":
    open("/home/claude/u21/townmap.svg", "w").write(townmap())
