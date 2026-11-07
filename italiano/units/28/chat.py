# Speak! Essenziale A1 28: phone chat between Bruno and Júlia (text only, Bruno has no voice)
C1, C2, INK = "#176074", "#e8f1f2", "#3b4246"
MSG = [("B", "Ciao Júlia! Arrivo sabato alle 18:40, stazione Centrale."), ("J", "Perfetto! Vengo alla stazione per prenderti."),
       ("B", "Grazie! Porto due valigie e la chitarra."), ("J", "La chitarra? Perché?"),
       ("B", "Per suonare con Chiara, naturalmente!"), ("J", "Ah, ecco! Quando arrivi, andiamo a mangiare da Giulia.")]


def chat():
    y, p = 30, []
    for who, t in MSG:
        w = 7.0 * len(t) * 0.78 + 20
        right = who == "J"
        x = 330 - w if right else 20
        p.append(f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="10" fill="{C1 if right else C2}"/>'
                 f'<text x="{x + 10}" y="{y + 17}" font-size="11" fill="{"#fff" if right else INK}">{t}</text>')
        y += 34
    head = (f'<rect x="0" y="0" width="350" height="22" rx="6" fill="{C1}"/>'
            f'<text x="175" y="15" font-size="11" font-weight="700" fill="#fff" text-anchor="middle">Bruno</text>')
    return (f'<svg viewBox="0 0 350 {y + 4}" width="100%" xmlns="http://www.w3.org/2000/svg" font-family="Inter, sans-serif" '
            f'style="display:block;max-height:62mm;background:#fafafa;border-radius:8px">{head}{"".join(p)}</svg>')
