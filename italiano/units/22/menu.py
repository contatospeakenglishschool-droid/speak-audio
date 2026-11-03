# The menu of the Trattoria Il Portico for Unità 22 (at the restaurant) - a printed menu card in two columns.
MENU = [("Antipasti", [("Tagliere di salumi", "14"), ("Crescentine", "7")]),
        ("Primi", [("Tagliatelle al ragù", "12"), ("Tortellini in brodo", "13"), ("Lasagne", "12")]),
        ("Secondi", [("Cotoletta alla bolognese", "16"), ("Pollo arrosto", "13")]),
        ("Contorni", [("Patate al forno", "5"), ("Insalata mista", "5")]),
        ("Dolci", [("Tiramisù", "6"), ("Panna cotta", "5")]),
        ("Bevande", [("Vino rosso della casa (bottiglia)", "16"), ("Acqua naturale / frizzante", "2"), ("Caffè", "1,50")])]


def section(name, items):
    rows = "".join(f'<div style="display:flex;font-size:9.5pt;line-height:1.5"><span>{d}</span>'
                   f'<span style="flex:1;border-bottom:0.3mm dotted #9AA3A8;margin:0 1.5mm 1.2mm"></span><span>€ {p}</span></div>' for d, p in items)
    return f'<div style="margin-bottom:2mm"><div style="font-weight:700;color:#1F5F6B;font-size:9pt;letter-spacing:.08em;text-transform:uppercase">{name}</div>{rows}</div>'


def menu_card():
    left = "".join(section(n, i) for n, i in MENU[:3])
    right = "".join(section(n, i) for n, i in MENU[3:])
    return (f'<div style="border:0.5mm double #C9A96E;border-radius:2mm;background:#FBF8F1;padding:3mm 5mm;margin:1mm 0 3mm">'
            f'<div style="text-align:center;font-family:Georgia,serif;font-size:14pt;font-weight:700;color:#1F5F6B">Trattoria Il Portico</div>'
            f'<div style="text-align:center;font-size:8.5pt;color:#6B7478;margin-bottom:2mm">cucina bolognese · via Santo Stefano</div>'
            f'<div style="display:flex;gap:8mm"><div style="flex:1">{left}</div><div style="flex:1">{right}</div></div>'
            f'<div style="text-align:center;font-size:8.5pt;color:#6B7478">Coperto € 2 a persona · Si accettano carte</div></div>')
