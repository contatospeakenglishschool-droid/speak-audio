# Speak! Ponte A2 04: front-view body figure with 12 numbered pointers (il corpo)
SKIN, LINE, NUM = "#f1dcc4", "#5b4a3a", "#176074"

# (number, target x, y, label x, y)
PTS = [(1, 150, 22, 70, 18), (2, 141, 40, 70, 44), (3, 125, 44, 70, 70), (4, 150, 49, 230, 30), (5, 150, 60, 230, 56),
       (6, 150, 78, 230, 82), (7, 103, 120, 50, 118), (8, 88, 178, 40, 176), (9, 150, 140, 230, 140),
       (10, 136, 220, 70, 222), (11, 172, 236, 232, 236), (12, 133, 288, 70, 290)]


def corpo(height="62mm"):
    p = []
    for n, x, y, lx, ly in PTS:
        p.append(f'<line x1="{lx}" y1="{ly}" x2="{x}" y2="{y}" stroke="{NUM}" stroke-width="1"/><circle cx="{x}" cy="{y}" r="2" fill="{NUM}"/>'
                 f'<circle cx="{lx}" cy="{ly}" r="9" fill="{NUM}"/><text x="{lx}" y="{ly + 3.5}" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">{n}</text>')
    body = f"""<g stroke="{LINE}" stroke-width="1.6" fill="{SKIN}">
<rect x="140" y="66" width="20" height="18" rx="4"/>
<path d="M112 86 Q150 76 188 86 L196 150 L104 150 Z" fill="#9ec5cc"/>
<path d="M112 88 L94 150 L86 172" fill="none" stroke-width="12" stroke="{SKIN}"/><path d="M112 88 L94 150 L86 172" fill="none"/>
<path d="M188 88 L206 150 L214 172" fill="none" stroke-width="12" stroke="{SKIN}"/><path d="M188 88 L206 150 L214 172" fill="none"/>
<ellipse cx="86" cy="180" rx="8" ry="10"/><ellipse cx="214" cy="180" rx="8" ry="10"/>
<path d="M104 150 L196 150 L192 176 L108 176 Z" fill="#cbbca0"/>
<rect x="114" y="176" width="28" height="104" rx="10"/><rect x="158" y="176" width="28" height="104" rx="10"/>
<ellipse cx="128" cy="236" rx="9" ry="6" fill="none"/><ellipse cx="172" cy="236" rx="9" ry="6" fill="none"/>
<ellipse cx="124" cy="290" rx="18" ry="8"/><ellipse cx="176" cy="290" rx="18" ry="8"/>
<ellipse cx="124" cy="44" rx="5" ry="9"/><ellipse cx="176" cy="44" rx="5" ry="9"/>
<circle cx="150" cy="42" r="26"/>
<path d="M124 34 Q130 12 150 14 Q172 12 176 34 Q164 22 150 24 Q136 22 124 34 Z" fill="#6b4b33"/>
<circle cx="141" cy="40" r="2.6" fill="{LINE}" stroke="none"/><circle cx="159" cy="40" r="2.6" fill="{LINE}" stroke="none"/>
<path d="M150 43 L147 52 L152 52" fill="none" stroke-width="1.3"/><path d="M142 60 Q150 66 158 60" fill="none" stroke-width="1.5"/></g>"""
    return (f'<svg viewBox="30 4 220 300" height="{height}" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;margin:0 auto">{body}{"".join(p)}</svg>')
