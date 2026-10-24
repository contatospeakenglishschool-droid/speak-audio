def person(x, y, shirt, skin="#E0AC7E", hair="#3B2A20", pose="stand"):
    s = ""
    if pose == "stand":
        s += f'<line x1="{x-3}" y1="{y+22}" x2="{x-5}" y2="{y+36}" stroke="#2D4A5A" stroke-width="3.2" stroke-linecap="round"/>'
        s += f'<line x1="{x+3}" y1="{y+22}" x2="{x+5}" y2="{y+36}" stroke="#2D4A5A" stroke-width="3.2" stroke-linecap="round"/>'
        s += f'<rect x="{x-6}" y="{y+7}" width="12" height="16" rx="3" fill="{shirt}"/>'
    s += f'<circle cx="{x}" cy="{y}" r="6.5" fill="{skin}"/><path d="M{x-6.5} {y-1} Q{x} {y-10} {x+6.5} {y-1}" fill="{hair}"/>'
    return s
def badge(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="7" fill="#176074"/><text x="{x}" y="{y+3.4}" font-size="9.5" text-anchor="middle" fill="#fff" font-weight="800" font-family="Inter,sans-serif">{n}</text>'
def beach():
    o = '<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8FD3F4"/><stop offset="1" stop-color="#D6F1FB"/></linearGradient></defs>'
    o += '<rect width="400" height="200" fill="#BFE7F8"/>'
    o += '<circle cx="355" cy="30" r="16" fill="#FFC72C"/>' + "".join(f'<line x1="355" y1="30" x2="355" y2="4" stroke="#FFC72C" stroke-width="3" stroke-linecap="round" transform="rotate({a} 355 30)"/>' for a in range(0,360,40))
    o += '<path d="M20 30 q8 -10 16 0 q8 -10 16 0" fill="none" stroke="#fff" stroke-width="3"/>'
    o += '<rect y="70" width="400" height="55" fill="#2F9ED8"/>'
    o += "".join(f'<path d="M{x} {y} q6 -5 12 0 q6 -5 12 0" fill="none" stroke="#BFE6F7" stroke-width="2"/>' for x, y in [(20,85),(120,80),(200,100),(270,82),(150,112),(40,110)])
    o += '<path d="M0 118 Q100 110 200 120 T400 116 L400 200 L0 200 Z" fill="#F3DCA8"/>'
    # 1 swimming
    o += '<circle cx="70" cy="96" r="6.5" fill="#E0AC7E"/><path d="M63.5 95 Q70 86 76.5 95" fill="#3B2A20"/>'
    o += '<path d="M55 100 q6 -10 12 -2" fill="none" stroke="#E0AC7E" stroke-width="3" stroke-linecap="round"/><path d="M76 99 q8 -2 12 -10" fill="none" stroke="#E0AC7E" stroke-width="3" stroke-linecap="round"/>'
    o += '<path d="M50 102 q10 -4 20 0 q10 -4 20 0" fill="none" stroke="#fff" stroke-width="2"/>' + badge(70, 78, 1)
    # 6 surfing
    o += '<ellipse cx="330" cy="104" rx="24" ry="4" fill="#FF7A45" stroke="#C4512A" stroke-width="1.2"/>' + person(330, 66, "#7B4FBF", hair="#C9A13B")
    o += '<line x1="324" y1="76" x2="312" y2="70" stroke="#E0AC7E" stroke-width="3" stroke-linecap="round"/><line x1="336" y1="76" x2="348" y2="70" stroke="#E0AC7E" stroke-width="3" stroke-linecap="round"/>' + badge(352, 56, 6)
    # 2 sunbathing on towel
    o += '<rect x="40" y="160" width="70" height="18" rx="2" fill="#E94B6A"/><rect x="40" y="166" width="70" height="4" fill="#fff"/>'
    o += '<rect x="58" y="162" width="30" height="11" rx="5" fill="#F2C94C"/><line x1="88" y1="167" x2="106" y2="167" stroke="#E0AC7E" stroke-width="5" stroke-linecap="round"/>'
    o += '<circle cx="51" cy="167" r="6.5" fill="#E0AC7E"/><rect x="46" y="163" width="10" height="3" rx="1" fill="#1f2528"/>' + badge(75, 150, 2)
    # 3 reading under umbrella
    o += '<line x1="165" y1="120" x2="165" y2="178" stroke="#7a5a3a" stroke-width="3"/><path d="M135 122 Q165 92 195 122 Z" fill="#E53935"/><path d="M155 122 Q165 96 175 122 Z" fill="#fff"/>'
    o += '<rect x="168" y="150" width="30" height="8" rx="2" fill="#3A8D5C"/>' + person(182, 134, "#2F80C9")
    o += '<rect x="186" y="140" width="10" height="8" fill="#fff" stroke="#176074" stroke-width="1.2"/><line x1="191" y1="140" x2="191" y2="148" stroke="#176074" stroke-width="1"/>' + badge(205, 126, 3)
    # 4 selfie
    o += person(245, 140, "#F2994A", hair="#111")
    o += '<line x1="251" y1="150" x2="262" y2="134" stroke="#E0AC7E" stroke-width="3" stroke-linecap="round"/><rect x="259" y="124" width="7" height="12" rx="1.5" fill="#1f2528"/>' + badge(232, 128, 4)
    # 5 ice cream
    o += person(305, 142, "#27AE60")
    o += '<line x1="311" y1="153" x2="318" y2="146" stroke="#E0AC7E" stroke-width="3" stroke-linecap="round"/><polygon points="314,146 322,146 318,158" fill="#D9A066"/><circle cx="318" cy="143" r="5" fill="#F48FB1"/>' + badge(292, 130, 5)
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200">' + o + '</svg>'
if __name__ == "__main__":
    open("/home/claude/beach_u20.svg", "w").write(beach())
