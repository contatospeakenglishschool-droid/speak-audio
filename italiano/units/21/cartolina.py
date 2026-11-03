# A postcard from Naples for Unità 21 (holidays) - text with gaps on the left, stamp and address on the right.
STAMP = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 72" style="width:17mm;height:20.4mm;display:block;margin-left:auto">'
         '<rect x="1" y="1" width="58" height="70" fill="#fff" stroke="#C9A96E" stroke-width="2" stroke-dasharray="3 2"/>'
         '<rect x="6" y="6" width="48" height="50" fill="#BFE0EC"/><circle cx="42" cy="18" r="6" fill="#F2C14E"/>'
         '<path d="M6 46 L22 24 L27 28 L32 23 L46 46 Z" fill="#7A6A5A"/><path d="M27 28 Q29 18 26 12 M29 26 Q33 17 31 10" fill="none" stroke="#9AA3A8" stroke-width="2"/>'
         '<rect x="6" y="46" width="48" height="10" fill="#2E7FA8"/>'
         '<text x="30" y="66" text-anchor="middle" font-size="7" font-weight="700" fill="#1F5F6B" font-family="Inter,sans-serif">ITALIA</text></svg>')


def postcard(g):
    text = (f"Cara mamma,<br>sono a Napoli con Giulia! Venerdì {g[0]} in treno. Sabato ha piovuto e non {g[1]} sul Vesuvio, "
            f"ma {g[2]} una pizza fantastica. Oggi {g[3]} il traghetto per Capri e {g[4]} il bagno… freddissimo! "
            f"Capri {g[5]} bellissima. Domani torniamo a Bologna.<br>Un bacio, Júlia")
    addr = "".join(f'<div style="border-bottom:0.3mm solid #9AA3A8;height:6mm;font-size:9pt;padding-top:1mm">{x}</div>'
                   for x in ("Sig.ra Lúcia Souza", "Rua da Bahia 1020", "Belo Horizonte – MG", "BRASILE"))
    return (f'<div style="display:flex;gap:4mm;border:0.4mm solid #C9A96E;border-radius:2mm;background:#FBF8F1;padding:3mm 4mm;margin:1mm 0 3mm">'
            f'<div style="flex:1.7;line-height:1.9;font-size:10pt;border-right:0.3mm solid #C9A96E;padding-right:4mm">{text}</div>'
            f'<div style="flex:1">{STAMP}<div style="margin-top:3mm">{addr}</div></div></div>')
