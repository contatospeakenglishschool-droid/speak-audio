# Giulia's birthday invitation for Unità 25 (feste) - a card with balloons, read-and-answer on page 5.
BALLOONS = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 90 60" style="width:26mm;height:17.3mm;display:block;margin:0 auto 1mm">'
            '<path d="M22 34 Q25 46 40 58 M45 30 Q44 44 40 58 M68 34 Q60 46 40 58" fill="none" stroke="#9AA3A8" stroke-width="1"/>'
            '<ellipse cx="22" cy="20" rx="11" ry="14" fill="#E07A5F"/><ellipse cx="45" cy="16" rx="11" ry="14" fill="#F2C14E"/>'
            '<ellipse cx="68" cy="20" rx="11" ry="14" fill="#2E7FA8"/>'
            '<path d="M19 13 Q20 10 23 9 M42 9 Q43 6 46 5 M65 13 Q66 10 69 9" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round"/></svg>')


def invito():
    rows = "".join(f'<div style="display:flex;gap:2mm;padding:0.8mm 0;border-bottom:0.3mm dotted #C9A96E"><b style="width:17mm;flex:none">{k}</b><span>{v}</span></div>'
                   for k, v in (("Quando", "sabato 13 giugno"), ("Ora", "alle 20:00"), ("Dove", "a casa mia, sul terrazzo"), ("Che cosa", "torta, musica e… balliamo!")))
    return (f'<div style="border:0.4mm solid #C9A96E;border-radius:2mm;background:#FBF8F1;padding:3mm 4mm;margin:1mm 0;font-size:9.5pt">'
            f'{BALLOONS}<div style="text-align:center;font-weight:800;font-size:13pt;color:#1F5F6B">Festa per i miei 30 anni!</div>'
            f'<div style="text-align:center;margin-bottom:1.5mm">Cari amici, vi invito alla mia festa di compleanno.</div>{rows}'
            f'<div style="margin-top:1.5mm">Non bisogna portare niente: solo il sorriso!<br>Rispondete entro giovedì. Un abbraccio, <b>Giulia</b></div></div>')
