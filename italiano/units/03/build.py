# Speak! Essenziale A1 - Unità 03 "Che lavoro fai?" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 03", audio_json=os.path.join(HERE, "audio_it-a1-unita-03.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "un'architetta", "architetta"), ("B", "un medico", "medico"), ("C", "un cameriere", "cameriere"), ("D", "un insegnante", "insegnante"),
          ("E", "un'infermiera", "infermiera"), ("F", "uno studente", "studente"), ("G", "un cuoco", "cuoco"), ("H", "un commesso", "commesso")]

SCRIPT = [("Narratore", "Dialogo uno."), ("Giulia", "Ciao, Júlia! Un caffè?"), ("Júlia", "Sì, grazie. Oggi lavoro molto!"), ("Giulia", "Che lavoro fai?"),
          ("Júlia", "Sono architetta. Lavoro in uno studio in via Indipendenza."), ("Giulia", "Che bello! E abiti qui vicino, vero?"),
          ("Júlia", "Sì, abito in via Santo Stefano. E tu abiti a Bologna?"), ("Giulia", "No, abito a Casalecchio. Arrivo in autobus, tutti i giorni."),
          ("Narratore", "Dialogo due."), ("Marco", "Júlia, questo è Luca, mio fratello."), ("Luca", "Ciao, Júlia! Piacere."), ("Júlia", "Piacere! Anche tu sei architetto?"),
          ("Luca", "No, no! Sono capotreno. Lavoro sui treni tra Bologna e Firenze."), ("Júlia", "E abiti a Bologna?"),
          ("Luca", "No, abito a Firenze. Ma oggi pranzo con Marco!"), ("Marco", "E paga lui!"),
          ("Narratore", "Dialogo tre."), ("Júlia", "Ciao, Davide! Studi oggi?"),
          ("Davide", "Sì, studio ingegneria all'università. Ma il sabato lavoro come cameriere in una pizzeria."), ("Júlia", "Ah! E parli inglese con i turisti?"),
          ("Davide", "Sì, un po'. Senti, hai il mio numero di telefono?"), ("Júlia", "No, non ho il tuo numero."),
          ("Davide", "Allora: tre, quattro, sette… uno, cinque, otto… dodici, venti."), ("Júlia", "Tre, quattro, sette, uno, cinque, otto, dodici, venti. Perfetto, grazie!")]
NUMS = ["zero", "uno", "due", "tre", "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci",
        "undici", "dodici", "tredici", "quattordici", "quindici", "sedici", "diciassette", "diciotto", "diciannove", "venti"]
S033 = ["sete / sette", "nono / nonno", "caro / carro", "pala / palla", "architetto", "commesso", "pizzeria", "Abito a Firenze.", "Lavoro in uno studio."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 03", "Che lavoro fai?", "Il lavoro e la casa · <b>i numeri da 0 a 20</b>",
                       [("SAI FARE", "dire il tuo lavoro e dove abiti; dare un numero di telefono"), ("LINGUA", "un / uno / una / un' · verbi in -are · abito a… / in…"),
                        ("PRONUNCIA", "i numeri da 0 a 20 · le doppie: sete / sette, nono / nonno")])
    words = ["un'architetta", "un cameriere", "un cuoco", "un'infermiera", "un insegnante", "un medico", "un commesso", "uno studente"]
    qs = [("in ospedale", "il medico, l'infermiera"), ("in un ristorante", "il cameriere, il cuoco"), ("a scuola", "l'insegnante"),
          ("in un negozio", "il commesso"), ("in uno studio", "l'architetta"), ("all'università", "lo studente")]
    ql = [f'<li value="{i+1}">… {q}? {R("→ " + a) if T else ""}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: i lavori", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi il lavoro sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Chi lavora…", "4 min")}
{twocol(ql, 4)}""",
    30, """<ol><li>A: i lavori hanno quasi sempre il maschile e il femminile: <i>architetto / architetta, cameriere / cameriera, commesso / commessa</i>. <i>insegnante</i> è uguale per uomo e donna: <i>un insegnante</i> (m., senza apostrofo) / <i>un'insegnante</i> (f.). <i>studente</i> → f. <i>studentessa</i>.</li>
<li>B: rispondere con l'articolo determinativo (<i>il medico</i>). Chiedere: <i>E chi lavora in un bar?</i> → <i>il barista</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 lavori con foto · dove lavorano</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Lavoro, città e un numero di telefono: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Articolo indeterminativo · verbi in <i>-are</i> · <i>abitare a / in</i> · numeri 0–20</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Numeri da 0 a 20 · le doppie</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Articoli · verbi in <i>-are</i> · presentarsi</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Biglietti da visita (domande con i numeri) · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 01–03) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Al bar Giulia chiede a Júlia che lavoro fa: Júlia è architetta e abita in via Santo Stefano; Giulia abita a Casalecchio. Allo studio Marco presenta suo fratello Luca, capotreno, che abita a Firenze. Sulle scale Davide racconta che studia ingegneria e il sabato fa il cameriere, e dà a Júlia il suo numero di telefono.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Abito in Bologna</i> ✗ → <b>Abito a Bologna</b> (città = <i>a</i>; via = <i>in</i>). <i>Lavoro de cameriere</i> ✗ → <b>Lavoro come cameriere</b>. <i>Un studente</i> ✗ → <b>uno studente</b>. E le <b>doppie</b>: <i>sete</i> (sede) ≠ <i>sette</i> (7).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>I numeri di cellulare in Italia cominciano con il <b>3</b> (<i>347, 333, 320…</i>) e si dicono spesso a gruppi: <i>tre-quattro-sette… dodici, venti</i>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 03.1 Tre dialoghi (lento e naturale) · Traccia 03.2 I numeri da 0 a 20 · Traccia 03.3 Le doppie</div>""")

    # Page 2
    ppl = [("Júlia", "architetta", "Bologna"), ("Giulia", "lavora al bar", "Casalecchio"), ("Luca", "capotreno", "Firenze"), ("Davide", "studente e cameriere", "Bologna")]
    pr = "".join(f"<tr><td><b>{n}</b></td><td>{A(l, 'min-width:42mm')}</td><td>{A(c, 'min-width:30mm')}</td></tr>" for n, l, c in ppl)
    b.page(f"""{sec(2, "Ascolto: che lavoro fai?", "10 min")}
<p>Júlia parla con Giulia al bar, conosce Luca, il fratello di Marco, e incontra Davide sulle scale.</p>
{audiocard(["03.1 · SLOW", "03.1 · NATURAL"])}
{sub("A", "Ascolta. Che lavoro fanno? Dove abitano? Completa la tabella.", "5 min", "03.1 · SLOW")}
<table style="margin:0"><tr><th style="width:28mm">Persona</th><th>Lavoro</th><th>Città (abita a…)</th></tr>{pr}</table>
{sub("B", "Ascolta di nuovo il dialogo 3. Scrivi il numero di telefono di Davide.", "3 min", "03.1 · NATURAL")}
<div class="msg" style="max-width:90mm;font-size:13pt;letter-spacing:.08em">&#9742;&nbsp; {A("347 158 12 20", "min-width:55mm")}</div>
{sub("C", "Marco dice «E paga lui!». Che cosa vuol dire?", "2 min")}
<div class="wline">{R("È uno scherzo: Luca pranza con Marco e Marco dice che paga Luca.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Giulia: accettare <i>barista</i> o <i>lavora al bar</i> (è la proprietaria). Davide: studia ingegneria e il sabato fa il cameriere.</li>
<li>B: versione <b>naturale</b>. Ripetere il numero con lo studente a gruppi: <i>tre-quattro-sette / uno-cinque-otto / dodici / venti</i>.</li>
<li>C: <i>pagare</i> è un verbo in <i>-are</i> come <i>lavorare</i>: <i>lui paga</i>.</li></ol>""")

    # Page 3
    art = [("un", "un medico, un cameriere, un architetto", "maschile"), ("uno", "uno studente, uno studio, uno zaino", "maschile + s + consonante, z"),
           ("una", "una commessa, una cameriera, una pizzeria", "femminile"), ("un'", "un'architetta, un'infermiera, un'insegnante", "femminile + vocale")]
    vb = [("io", "lavoro", "abito"), ("tu", "lavori", "abiti"), ("lui / lei", "lavora", "abita"), ("Lei (formale)", "lavora", "abita")]
    rules = [("Città:", "Abito a Firenze.", "Abito in Firenze."), ("Via:", "Abito in via Santo Stefano.", "Abito a via Santo Stefano."),
             ("Lavoro", "come cameriere", "de cameriere"), ("È", "uno studente", "un studente")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    ta = "".join(f"<tr><td><b>{a}</b></td><td>{e}</td><td class='small'>{n}</td></tr>" for a, e, n in art)
    tv = "".join(f"<tr><td>{p}</td><td><b>{x}</b></td><td><b>{y}</b></td></tr>" for p, x, y in vb)
    b.page(f"""{sec(3, "Grammatica: un, uno, una, un' · verbi in -are", "10 min")}
{sub("A", "L'articolo indeterminativo.", "3 min")}
<table style="margin:0"><tr><th style="width:14mm"></th><th>Esempi</th><th>Quando?</th></tr>{ta}</table>
{sub("B", "I verbi in -are: lavorare e abitare.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th></th><th>lavorare</th><th>abitare</th></tr>{tv}</table></div>
<div class="box" style="margin:0"><h4>COME LAVORARE</h4>Anche: <b>studiare</b> (studio, studi, studia), <b>parlare</b>, <b>pagare</b>, <b>arrivare</b>, <b>pranzare</b>.<br><i>Che lavoro fai?</i> → <b>Sono</b> architetta. / <b>Lavoro come</b> architetta.</div></div>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>DOVE?</h4><b>abitare a</b> + città: <i>a Bologna, a Firenze</i>. <b>abitare in</b> + via / paese: <i>in via Santo Stefano, in Brasile, in Italia</i>. <b>lavorare in</b> + luogo: <i>in uno studio, in una pizzeria</i>.</div>""",
    22, """<ol><li>A: <i>uno</i> anche davanti a <i>ps, gn, y</i>, ma all'A1 basta <i>s + consonante</i> e <i>z</i>. Con <i>essere</i> + lavoro spesso non c'è l'articolo: <i>Sono architetta</i>.</li>
<li>B: <i>studiare</i>: io studio, tu studi (una sola <i>i</i>). C: <i>in Brasile</i> ma <i>a São Paulo</i>.</li></ol>""")

    # Page 4
    nt = "".join(f'<td style="text-align:center;padding:1.2mm 1mm"><b style="color:{TEAL}">{i}</b><br><span class="small">{n}</span></td>' + ("</tr><tr>" if i in (6, 13) else "") for i, n in enumerate(NUMS))
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Abito in Bologna.</td><td><b>Abito a Bologna.</b></td><td>Città = <i>a</i>.</td></tr>
<tr><td>Lavoro de cameriere.</td><td><b>Lavoro come cameriere.</b></td><td>Il lavoro = <i>come</i>.</td></tr>
<tr><td>È un studente.</td><td><b>È uno studente.</b></td><td><i>s</i> + consonante = <i>uno</i>.</td></tr>
<tr><td>Lui lavori in ospedale.</td><td><b>Lui lavora in ospedale.</b></td><td>lui / lei / Lei = <i>-a</i>.</td></tr>
<tr><td>Il mio numero è sete…</td><td><b>…è sette…</b></td><td><i>sette</i> (7) ha la doppia.</td></tr></table></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["03.2", "03.3"])}
{sub("A", "I numeri da 0 a 20. Ascolta e ripeti.", "2 min", "03.2")}
<table style="margin:0 0 1mm"><tr>{nt}</tr></table>
{sub("B", "Le doppie. Ascolta e ripeti. La doppia è più lunga e più forte.", "3 min", "03.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S033)}</div>""",
    32, """<ol><li>Numeri: attenzione a <i>sei</i> (6, non «seis»), <i>sette</i>, <i>diciassette</i>, <i>diciannove</i>. Dettare 5 numeri allo studente e poi invertire i ruoli.</li>
<li>4B: le doppie sono molto importanti in italiano e i brasiliani tendono a non sentirle: <i>nono</i> (9º) ≠ <i>nonno</i> (il padre del padre). Far battere le mani sulla doppia.</li></ol>""")

    # Page 5
    aw = ["un", "uno", "una", "un'", "uno", "un"]
    an = ["cuoco", "studio", "pizzeria", "infermiera", "zaino", "ospedale"]
    al = [f'<li value="{i+1}">{A(aw[i], "min-width:12mm")} {an[i]}</li>' for i in range(6)]
    vw = [("Io", "abito", "a Bologna.", "abitare"), ("Luca", "lavora", "sui treni.", "lavorare"), ("Tu", "parli", "inglese?", "parlare"),
          ("Davide", "studia", "ingegneria.", "studiare"), ("Signora, Lei dove", "abita", "?", "abitare"), ("Io", "lavoro", "in uno studio.", "lavorare")]
    vl = "".join(f'<li>{a} {A(v, "min-width:18mm")} {c} <span class="small">({inf})</span></li>' for a, v, c, inf in vw)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con un, uno, una o un'.", "2 min")}
{twocol(al, 4)}
{sub("B", "Completa con il verbo.", "3 min")}
<ol>{vl}</ol>
{sub("C", "E tu? Scrivi 3 frasi: lavoro, luogo di lavoro, città.", "3 min")}
<div class="msg" style="max-width:none">Sono <span class="blank" style="min-width:30mm">&nbsp;</span>. Lavoro in <span class="blank" style="min-width:30mm">&nbsp;</span>. Abito a <span class="blank" style="min-width:30mm">&nbsp;</span>.<br>
<div style="margin-top:2mm">{R("Esempio: Sono infermiera. Lavoro in un ospedale. Abito a Recife.")}</div></div>""",
    25, """<ol><li>A: 2 <i>uno studio</i> e 5 <i>uno zaino</i> (s + consonante, z); 6 <i>un ospedale</i>: maschile + vocale = <i>un</i>, senza apostrofo!</li>
<li>C: lo studente legge ad alta voce. Chi non lavora può dire <i>Sono studente / Sono in pensione</i>.</li></ol>""")

    # Page 6
    cards = [("Sara Conti", "insegnante", "una scuola", "Modena", "339 14 07 18"), ("Dottor Paolo Neri", "medico", "un ospedale", "Bologna", "320 16 11 09"),
             ("Kenji", "cuoco", "un ristorante giapponese", "Milano", "347 20 13 05"), ("Signora Anna Galli", "commessa", "un negozio", "Parma", "333 19 02 15")]
    cd = "".join(f'<div class="ad" style="flex:1;font-size:8.6pt"><b class="t">{n}</b>Lavoro: {A(l, "min-width:24mm")}<br>Lavora in: {A(w, "min-width:24mm")}<br>Abita a: {A(c, "min-width:20mm")}<br>&#9742; {A(t, "min-width:26mm")}</div>' for n, l, w, c, t in cards)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Biglietti da visita. L'insegnante ha le informazioni. Fai domande e completa. Tu o Lei?", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{cd}</div>
<div class="bank" style="background:#fff">Che lavoro fai / fa? · Dove lavori / lavora? · Dove abiti / abita? · Qual è il tuo / il Suo numero di telefono?</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Che lavoro fai? Dove lavori?</li><li>Dove abiti? In una città grande o piccola?</li><li>Parli inglese o spagnolo al lavoro?</li><li>Che lavoro fa una persona della tua famiglia?</li></ol>""",
    30, """<ol><li>A: le soluzioni sono in rosso solo qui. L'insegnante risponde come la persona della carta. Con il dottor Neri e la signora Galli si usa il <b>Lei</b>: <i>Che lavoro fa? Qual è il Suo numero?</i></li>
<li>B: correggere <i>abito a / in</i> e la terza persona: <i>mia madre lavora…</i></li></ol>""")

    # Page 7
    pc = [("Unità 01", "So salutare e presentarmi (tu e Lei)."), ("Unità 02", "So dire di dove sono e la nazionalità."),
          ("Unità 03", "So dire che lavoro faccio, dove lavoro e dove abito."), ("Unità 03", "So dire e capire un numero di telefono (0–20).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Abito in Milano.", "Abito a Milano."), ("Marco è un studente.", "Marco è uno studente."), ("Lavoro de commessa.", "Lavoro come commessa."),
          ("Lei lavori in ospedale?", "Lei lavora in ospedale?"), ("Il mio numero è tre, sete, nove…", "…tre, sette, nove…"), ("È una infermiera.", "È un'infermiera.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Una persona che conosci.</b> Scrivi 3–4 frasi: come si chiama, che lavoro fa, dove lavora, dove abita.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante fa domande sulla persona del testo: <i>Dove lavora? Abita a…?</i> e detta due numeri di telefono.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("03.1", "Che lavoro fai? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("03.2", "I numeri da 0 a 20")}
<p>{" · ".join(NUMS)}</p>
{sub("03.3", "Le doppie")}
<p>{" · ".join(S033)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 03 - Che lavoro fai")
