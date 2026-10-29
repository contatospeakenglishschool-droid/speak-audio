# Small flat weather icons for Unità 17 (inline SVG, same palette as the other unit drawings).
SUN = '<circle cx="20" cy="20" r="8" fill="#E8B23A"/>' + "".join(
    f'<rect x="19" y="3" width="2" height="6" rx="1" fill="#E8B23A" transform="rotate({a} 20 20)"/>' for a in range(0, 360, 45))
CLOUD = '<path d="M10 28 a7 7 0 0 1 2-13.5 a9 9 0 0 1 17 1.5 a6 6 0 0 1 1 12 Z" fill="{c}"/>'
ICONS = {
    "sole": SUN,
    "nuvoloso": '<circle cx="14" cy="14" r="6" fill="#E8B23A"/>' + CLOUD.format(c="#A9B4BA"),
    "pioggia": CLOUD.format(c="#8E9AA1").replace("28", "24") + "".join(f'<rect x="{x}" y="27" width="2" height="7" rx="1" fill="#5B7FA6" transform="rotate(15 {x} 30)"/>' for x in (13, 19, 25)),
    "neve": CLOUD.format(c="#A9B4BA").replace("28", "24") + "".join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#7FA7C9"/>' for x, y in ((13, 29), (19, 33), (25, 29), (16, 36), (23, 36))),
    "nebbia": "".join(f'<rect x="{x}" y="{y}" width="{w}" height="3" rx="1.5" fill="#A9B4BA"/>' for x, y, w in ((6, 12, 26), (10, 19, 24), (5, 26, 28), (9, 33, 20))),
    "vento": "".join(f'<path d="M5 {y} H{l} a4 4 0 1 0 -4 -4" fill="none" stroke="#7FA7C9" stroke-width="2.4" stroke-linecap="round"/>' for y, l in ((15, 28), (23, 33), (31, 24))),
    "temporale": CLOUD.format(c="#6F7B82").replace("28", "24") + '<path d="M21 25 L15 33 H20 L17 39 L26 29 H21 L24 25 Z" fill="#E8B23A"/>',
}


def icon(name, size=12):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" style="width:{size}mm;height:{size}mm;vertical-align:middle">{ICONS[name]}</svg>'
