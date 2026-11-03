# Simple flat map of a park for Unità 23 (giving directions) - gate, paths, small lake, bar and four lettered places.
F = 'font-family="Inter,sans-serif"'


def label(x, y, t, size=11, w=700, c="#3C4448"):
    return f'<text x="{x}" y="{y}" text-anchor="middle" font-size="{size}" font-weight="{w}" fill="{c}" {F}>{t}</text>'


def pin(x, y, letter):
    return (f'<circle cx="{x}" cy="{y}" r="11" fill="#1F5F6B"/>' + label(x, y + 4, letter, 12, 700, "#fff"))


def tree(x, y, r=14):
    return f'<rect x="{x-3}" y="{y}" width="6" height="12" fill="#7A4E2D"/><circle cx="{x}" cy="{y-4}" r="{r}" fill="#6FA35A"/>'


def park():
    o = '<rect width="600" height="250" rx="10" fill="#E8F1DF"/>'
    path = 'fill="none" stroke="#E9DDC4" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"'
    o += f'<path d="M300 250 V150 M300 150 H110 M300 150 H490 M300 112 V40" {path}/>'
    o += '<ellipse cx="300" cy="128" rx="44" ry="20" fill="#9CCBE0"/>' + label(300, 132, "laghetto", 10, 600, "#1F5F6B")
    o += '<path d="M300 150 Q255 150 256 128 Q258 108 300 108" fill="none" stroke="#E9DDC4" stroke-width="10"/>'
    o += '<rect x="190" y="160" width="40" height="26" rx="3" fill="#C2502E"/>' + label(210, 178, "BAR", 10, 700, "#fff")
    o += tree(70, 120, 26) + tree(40, 200) + tree(560, 60) + tree(150, 60) + tree(460, 210) + tree(520, 200, 12)
    o += '<rect x="450" y="100" width="70" height="36" fill="#B9D4A0" stroke="#fff" stroke-width="2"/><path d="M485 100 V136" stroke="#fff" stroke-width="2"/>'
    o += '<circle cx="300" cy="32" r="12" fill="#9CCBE0" stroke="#B9B9B9" stroke-width="3"/>'
    o += '<rect x="360" y="200" width="50" height="30" rx="4" fill="#F2C14E"/>' + label(385, 220, "giochi", 9, 600)
    o += '<path d="M272 246 V226 Q300 212 328 226 V246" fill="none" stroke="#3C4448" stroke-width="3"/>' + label(250, 244, "cancello", 10, 600)
    o += pin(100, 112, "A") + pin(522, 150, "B") + pin(330, 32, "C") + pin(385, 186, "D")
    o += label(374, 246, "TU SEI QUI", 9, 700, "#C2502E")
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 250">{o}</svg>'


def themap(w):
    return park().replace('viewBox="0 0 600 250">', f'viewBox="0 0 600 250" style="width:{w}mm;height:{w*250/600:.1f}mm;display:block;margin:0 auto">', 1)
