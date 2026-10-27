# Speak! Essenziale A1 - Unità 10 "Al mercato" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 10", audio_json=os.path.join(HERE, "audio_it-a1-unita-10.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il prosciutto", "prosciutto"), ("B", "il parmigiano", "parmigiano"), ("C", "il pane", "pane"), ("D", "i pomodori", "pomodori"),
          ("E", "la frutta", "frutta"), ("F", "il vino", "vino"), ("G", "l'olio", "olio"), ("H", "il mercato", "mercato")]

SCRIPT = [("Narratore", "Dialogo uno. Al bar, la mattina."), ("Giulia", "Allora, Júlia, che cosa fai oggi?"),
          ("Júlia", "Devo fare la spesa. Stasera ceno a casa con i miei genitori e con Marco. Sai dov'è un buon mercato?"),
          ("Giulia", "Sì! Vai al Mercato delle Erbe, in via Ugo Bassi. E devi provare il parmigiano: è molto buono."),
          ("Narratore", "Dialogo due. Al mercato."), ("Salumiere", "Buongiorno, signora. Desidera?"),
          ("Júlia", "Buongiorno. Vorrei un etto di prosciutto crudo e mezzo chilo di parmigiano."), ("Salumiere", "Ecco. Altro?"),
          ("Júlia", "Sì, del pane, per favore. Mezzo chilo."), ("Salumiere", "E dei pomodori? Sono molto buoni oggi."),
          ("Júlia", "No, grazie, i pomodori ci sono già a casa. Basta così. Quant'è?"), ("Salumiere", "Sono diciotto euro e cinquanta."),
          ("Narratore", "Dialogo tre. Al telefono."), ("Marco", "Júlia, devo portare qualcosa stasera?"),
          ("Júlia", "Sì, puoi portare del vino? E… sai cucinare i tortellini?"), ("Marco", "Certo che so cucinare i tortellini! Sono bolognese!"),
          ("Júlia", "Perfetto. Allora stasera cucini tu!"), ("Marco", "Ah… Va bene.")]
S102 = ["bottiglia", "aglio", "famiglia", "voglio", "luglio", "biglietto", "Vorrei una bottiglia d'olio."]
S103 = ["Desidera?", "Vorrei un etto di prosciutto.", "Mezzo chilo di parmigiano, per favore.", "Altro?", "No, basta così, grazie.", "Quant'è?"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 10", "Al mercato", "Fare la spesa · <b>un etto, mezzo chilo, una bottiglia</b>",
                       [("SAI FARE", "comprare il cibo al mercato e chiedere le quantità"), ("LINGUA", "del, dello, della, dell' · devo, devi, deve · so, sai, sa · molto / molta / molti"),
                        ("PRONUNCIA", "il suono GLI: bottiglia, famiglia · frasi per fare la spesa")])
    words = ["i pomodori", "il mercato", "il pane", "il parmigiano", "il prosciutto", "il vino", "l'olio", "la frutta"]
    qs = [("un etto di", "prosciutto"), ("mezzo chilo di", "parmigiano"), ("un chilo di", "pomodori"), ("una bottiglia di", "vino / olio"), ("un pacco di", "pasta"), ("un po' di", "pane, frutta…")]
    ql = [f'<li value="{i+1}">{q} {A(a, "min-width:26mm")}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: al mercato", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Le quantità. Completa con una parola della lista A (o con pasta).", "4 min")}
{twocol(ql, 4)}""",
    28, """<ol><li>A: <b>un etto</b> = 100 grammi (molto usato per salumi e formaggi). <b>Il parmigiano</b> e <b>il prosciutto</b> sono prodotti dell'Emilia-Romagna, la regione di Bologna.</li>
<li>B: accettare ogni risposta logica. Chiedere: <i>Che cosa compri al chilo? E all'etto?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 parole del mercato con foto · le quantità</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Júlia fa la spesa per la cena con i genitori: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Partitivo (<i>del, della…</i>) · <i>dovere</i> · <i>sapere</i> · <i>molto</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Il suono GLI · frasi per fare la spesa</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Partitivo · <i>dovere / sapere</i> · la lista della spesa</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Al banco della salumeria: gioco di ruolo · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 07–10) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>I genitori di Júlia sono a Bologna. Stasera Júlia prepara una cena a casa con loro e con Marco. Giulia le consiglia il Mercato delle Erbe. Al banco Júlia compra prosciutto, parmigiano e pane (18,50 €). Poi chiede a Marco di portare del vino… e scopre che Marco sa cucinare i tortellini: allora cucina lui!</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Devo de comprare</i> ✗ → <b>Devo comprare</b>. <i>Un etto de prosciutto</i> ✗ → <b>un etto di prosciutto</b>. <i>Vorrei de pane</i> ✗ → <b>Vorrei del pane</b>. <i>Mezza chilo</i> ✗ → <b>mezzo chilo</b>. <i>Molto pomodori</i> ✗ → <b>molti pomodori</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>A Bologna i mercati storici sono il <b>Mercato delle Erbe</b> e il <b>Quadrilatero</b>, vicino a piazza Maggiore. Al banco si dice <i>Desidera?</i> e alla fine <i>Altro?</i> – <i>No, basta così.</i></div>
<div class="box"><h4>AUDIO</h4>Traccia 10.1 Tre dialoghi (lento e naturale) · Traccia 10.2 Il suono GLI · Traccia 10.3 Fare la spesa</div>""")

    # Page 2
    sl = [("prosciutto crudo", "un etto"), ("parmigiano", "mezzo chilo"), ("pane", "mezzo chilo")]
    slr = "".join(f"<tr><td style='width:50mm'>{A(q, 'min-width:30mm')}</td><td><b>di {p}</b></td></tr>" for p, q in sl)
    gp = [("Devo", "fare", "la spesa."), ("", "Sai", "dov'è un buon mercato?"), ("E", "devi", "provare il parmigiano."), ("Sì,", "del", "pane, per favore."),
          ("Sono", "diciotto euro e cinquanta", "."), ("Certo che", "so", "cucinare i tortellini!")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: una cena speciale", "10 min")}
<p>I genitori di Júlia sono a Bologna. Stasera Júlia prepara una cena a casa con loro e con Marco.</p>
{audiocard(["10.1 · SLOW", "10.1 · NATURAL"])}
{sub("A", "Ascolta il dialogo 2. Che cosa compra Júlia? Scrivi le quantità.", "3 min", "10.1 · SLOW")}
<table style="margin:0;max-width:120mm">{slr}</table>
{sub("B", "Ascolta di nuovo e completa.", "5 min", "10.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Chi cucina i tortellini stasera? Perché?", "2 min")}
<div class="wline">{R("Marco, perché sa cucinare i tortellini: è bolognese.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Júlia non compra i pomodori: <i>ci sono già a casa</i>.</li>
<li>B: versione <b>naturale</b>. 1 e 3: <i>devo / devi</i> + infinito; 2 e 6: <i>sapere</i> (pagina 3). <i>Certo che…!</i> = naturalmente.</li></ol>""")

    # Page 3
    par = [("il", "del", "del pane, del vino"), ("lo", "dello", "dello zucchero"), ("la", "della", "della frutta"), ("l'", "dell'", "dell'olio, dell'acqua"),
           ("i", "dei", "dei pomodori"), ("le", "delle", "delle mele")]
    tp = "".join(f"<tr><td>di + {a}</td><td><b>{x}</b></td><td class='small'>{e}</td></tr>" for a, x, e in par)
    ds = [("io", "devo", "so"), ("tu", "devi", "sai"), ("lui / lei / Lei", "deve", "sa")]
    tds = "".join(f"<tr><td>{p}</td><td><b>{d}</b></td><td><b>{s}</b></td></tr>" for p, d, s in ds)
    rules = [("", "Devo comprare il pane.", "Devo di comprare il pane."), ("Un etto", "di prosciutto", "de prosciutto"), ("", "mezzo chilo", "mezza chilo"), ("Ci sono", "molti pomodori", "molto pomodori")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: del, della · dovere · sapere · molto", "10 min")}
<div class="two"><div>{sub("A", "Il partitivo (= un po' di).", "3 min")}<table style="margin:0">{tp}</table></div>
<div>{sub("B", "dovere e sapere + infinito.", "3 min")}<table style="margin:0"><tr><th></th><th>dovere</th><th>sapere</th></tr>{tds}</table>
<div class="box" style="margin-top:2mm"><h4>ESEMPI</h4><b>Devo</b> fare la spesa. · <b>Devi</b> provare il parmigiano! · <b>Sai</b> cucinare? · <b>Sai</b> dov'è il mercato? · <b>Non so</b>.</div></div></div>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>QUANTITÀ E MOLTO</h4><b>un etto di</b> · <b>mezzo chilo di</b> · <b>un chilo di</b> (due <b>chili</b>) · <b>una bottiglia di</b> · <b>un pacco di</b> · <b>un po' di</b>. Dopo la quantità: solo <b>di</b>, senza articolo. <b>Molto</b> + aggettivo non cambia (<i>è molto buono</i>); <b>molto</b> + nome è come un aggettivo: <i>molto pane, molta frutta, molti pomodori, molte mele</i>.</div>""",
    20, """<ol><li>A: <i>del pane</i> = un po' di pane. Stessa logica delle preposizioni articolate (unità 8).</li>
<li>B: <i>sapere</i> + infinito = avere la capacità (<i>So nuotare</i>). <i>Potere</i> = è possibile (<i>Posso venire</i>).</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Devo di comprare il pane.</td><td><b>Devo comprare il pane.</b></td><td><i>dovere</i> + infinito, senza <i>di</i>.</td></tr>
<tr><td>Un etto de prosciutto.</td><td><b>Un etto di prosciutto.</b></td><td>In italiano: <i>di</i>.</td></tr>
<tr><td>Vorrei de pane.</td><td><b>Vorrei del pane.</b></td><td>Partitivo: <i>di + il = del</i>.</td></tr>
<tr><td>Mezza chilo di parmigiano.</td><td><b>Mezzo chilo di parmigiano.</b></td><td><i>chilo</i> è maschile.</td></tr>
<tr><td>Ci sono molto pomodori.</td><td><b>Ci sono molti pomodori.</b></td><td><i>molto</i> + nome cambia.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["10.2", "10.3"])}
{sub("A", "Il suono GLI. Ascolta e ripeti.", "2 min", "10.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S102)}</div>
{sub("B", "Fare la spesa. Ascolta e ripeti.", "3 min", "10.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S103)}</div>""",
    38, """<ol><li>Errori: <i>de</i> per <i>di</i> torna spesso: correggere sempre, anche nelle quantità.</li>
<li>4A: <b>gli</b> = suono molto simile alla <i>lh</i> portoghese. Non dire «bot-ti-glia» con la G dura né «botilia».</li>
<li>4B: <i>Desidera?</i> = che cosa vuole? (formale). <i>Basta così</i> = non voglio altro.</li></ol>""")

    # Page 5
    pw = ["del", "della", "dello", "dell'", "dei", "delle"]
    pn = ["pane", "frutta", "zucchero", "olio", "pomodori", "mele"]
    pl5 = [f'<li value="{i+1}">Vorrei {A(pw[i], "min-width:14mm")} {pn[i]}.</li>' for i in range(6)]
    vw = [("Io", "devo", "fare la spesa.", "dovere"), ("Tu", "sai", "dov'è il mercato?", "sapere"), ("Marco", "sa", "cucinare i tortellini.", "sapere"),
          ("Júlia", "deve", "comprare il pane.", "dovere"), ("Signora, Lei", "sa", "parlare inglese?", "sapere"), ("Tu", "devi", "provare il parmigiano!", "dovere")]
    vl = "".join(f'<li>{a} {A(v, "min-width:16mm")} {c} <span class="small">({n})</span></li>' for a, v, c, n in vw)
    lq = [("un", "etto", "di mortadella"), ("mezzo", "chilo", "di parmigiano"), ("due", "chili", "di pomodori"), ("una", "bottiglia", "di vino"), ("un", "pacco", "di pasta")]
    lql = "".join(f'<li>{a} {A(x, "min-width:20mm")} {c}</li>' for a, x, c in lq)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con del, dello, della, dell', dei, delle.", "2 min")}
{twocol(pl5, 4)}
{sub("B", "Completa con dovere o sapere.", "3 min")}
<ol>{vl}</ol>
{sub("C", "La lista della spesa di Júlia. Completa con bottiglia, chili, chilo, etto, pacco.", "3 min")}
<div class="msg" style="max-width:100mm"><b style="color:{TEAL}">Lista della spesa</b><ol style="margin-top:1mm">{lql}</ol></div>""",
    22, """<ol><li>A: 3 <i>dello zucchero</i> (lo zucchero, unità 4); 4 <i>dell'olio</i>.</li>
<li>C: <i>chilo → chili</i> (plurale in <i>-i</i>). Poi lo studente scrive la sua lista della spesa e la legge.</li></ol>""")

    # Page 6
    pr = [("Prosciutto crudo", "3,50 € all'etto"), ("Mortadella", "2,00 € all'etto"), ("Parmigiano", "24,00 € al chilo"), ("Pane", "6,00 € al chilo"),
          ("Pomodori", "3,00 € al chilo"), ("Olio d'oliva", "9,00 € la bottiglia"), ("Vino rosso", "8,00 € la bottiglia")]
    prt = "".join(f"<tr><td>{n}</td><td style='text-align:right'>{p}</td></tr>" for n, p in pr)
    cards = [("Lista 1", "2 etti di prosciutto crudo · 1 chilo di pomodori · 1 bottiglia d'olio", "19,00 €"), ("Lista 2", "mezzo chilo di parmigiano · 1 etto di mortadella · 1 bottiglia di vino", "22,00 €")]
    cdh = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b>{l}<br>Totale: {A(t, "min-width:18mm")}</div>' for n, l, t in cards)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Al banco della Salumeria Bassi. L'insegnante è il salumiere. Compra le cose della lista 1. Poi scambiate i ruoli con la lista 2.", "7 min")}
<div class="two"><div class="ad"><b class="t">SALUMERIA BASSI · PREZZI</b><table style="margin:1mm 0 0">{prt}</table></div>
<div style="display:flex;flex-direction:column;gap:2.5mm">{cdh}</div></div>
<div class="bank" style="background:#fff;margin-top:2mm">Desidera? · Vorrei… · Un etto / mezzo chilo di… · Altro? · No, basta così. · Quant'è? · Sono…</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Dove fai la spesa? Al supermercato o al mercato?</li><li>Che cosa devi comprare questa settimana?</li><li>Sai cucinare? Che cosa sai cucinare?</li><li>C'è un cibo brasiliano che i tuoi amici italiani devono provare?</li></ol>""",
    26, """<ol><li>A: lista 1 = 7,00 + 3,00 + 9,00 = <b>19,00 €</b>; lista 2 = 12,00 + 2,00 + 8,00 = <b>22,00 €</b>. L'insegnante come salumiere chiede sempre <i>Altro?</i> e propone un prodotto in più.</li>
<li>B: correggere <i>devo + infinito</i> e <i>so + infinito</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 07", "So chiedere e dare indicazioni."), ("Unità 08", "So prenotare una camera in albergo."), ("Unità 10", "So comprare il cibo al mercato con le quantità."),
          ("Unità 10", "So usare del, della, dei…"), ("Unità 10", "So dire che cosa devo fare e che cosa so fare.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Devo di fare la spesa.", "Devo fare la spesa."), ("Vorrei un etto de mortadella.", "Vorrei un etto di mortadella."), ("Vorrei de vino rosso.", "Vorrei del vino rosso."),
          ("Mezza chilo di pomodori, per favore.", "Mezzo chilo di pomodori, per favore."), ("Al mercato ci sono molto pomodori.", "Al mercato ci sono molti pomodori."), ("Marco sai cucinare.", "Marco sa cucinare.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Una cena a casa tua.</b> Inviti tre amici a cena. Scrivi che cosa devi comprare (con le quantità) e che cosa sai cucinare (4–5 frasi).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Frase 5: <i>molto</i> + nome plurale → <i>molti</i>. Poi lo studente legge la sua lista e l'insegnante fa il salumiere.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("10.1", "Una cena speciale (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("10.2", "Il suono GLI")}
<p>{" · ".join(S102)}</p>
{sub("10.3", "Fare la spesa")}
<p>{" ".join(S103)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 10 - Al mercato")
