# Speak! Essenziale A1 - Unità 21 "Le vacanze" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from cartolina import postcard
setup(band="A1 · UNITÀ 21", audio_json=os.path.join(HERE, "audio_it-a1-unita-21.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "al mare", "mare"), ("B", "in montagna", "montagna"), ("C", "fare il bagno", "bagno"), ("D", "il traghetto", "traghetto"),
          ("E", "la valigia", "valigia"), ("F", "prendere il sole", "sole"), ("G", "fare le foto", "foto"), ("H", "il campeggio", "campeggio")]

SCRIPT = [("Narratore", "Dialogo uno. Allo studio, il martedì dopo Pasqua."), ("Marco", "Ciao, Júlia! Com'è andato il ponte di Pasqua? Dove sei andata?"),
          ("Júlia", "Sono andata a Napoli con Giulia! Siamo partite venerdì e siamo tornate ieri sera."), ("Marco", "Che bello! Come siete andate? In treno?"),
          ("Júlia", "Sì, con il Frecciarossa. Tre ore e mezza."), ("Marco", "E che cosa avete fatto?"),
          ("Júlia", "Abbiamo visitato il centro storico, abbiamo mangiato la pizza… e domenica abbiamo preso il traghetto per Capri!"),
          ("Marco", "Capri! Io ci sono stato dieci anni fa. È bellissima."), ("Júlia", "E tu? Che cosa hai fatto?"),
          ("Marco", "Niente di speciale. Sono rimasto a Bologna e ho dormito molto!"),
          ("Narratore", "Dialogo due. Sulle scale."), ("Davide", "Júlia! Allora, Napoli? Com'è andata?"),
          ("Júlia", "Benissimo! Siamo andate alla pizzeria di tuo zio, in via dei Tribunali."), ("Davide", "E com'è la pizza di mio zio?"),
          ("Júlia", "La migliore della mia vita!"), ("Davide", "Siete salite sul Vesuvio?"), ("Júlia", "No, non ci siamo state. Sabato ha piovuto tutto il giorno."),
          ("Davide", "Che peccato! Allora la prossima volta."), ("Júlia", "E tu, quando sei tornato a Napoli l'ultima volta?"),
          ("Davide", "A Natale, quattro mesi fa. Mia madre mi aspetta!"),
          ("Narratore", "Dialogo tre. Al bar."), ("Signora Rossi", "Giulia, sei andata a Napoli con Júlia, vero?"),
          ("Giulia", "Sì, signora. Abbiamo fatto un viaggio bellissimo. Lei conosce Napoli?"), ("Signora Rossi", "Certo! Ci sono stata in viaggio di nozze, quarant'anni fa."),
          ("Giulia", "Davvero? E dove siete andati?"), ("Signora Rossi", "Siamo stati a Napoli, a Capri e a Sorrento. Abbiamo fatto il bagno tutti i giorni."),
          ("Giulia", "E l'estate scorsa? Dov'è andata in vacanza?"), ("Signora Rossi", "Sono andata in montagna, in Trentino, con mia sorella. Ma Capri… Capri è un'altra cosa!")]
S212 = ["Che bello!", "Che peccato!", "Che fortuna!", "Che buono!", "Che caldo!", "Siamo andate a Capri. Che bello!"]
S213 = ["Dove sei andato in vacanza?", "Sono andata a Napoli con un'amica.", "Siamo partite venerdì e siamo tornate lunedì.",
        "Abbiamo visitato il centro e abbiamo mangiato la pizza.", "Ci sono stato dieci anni fa.", "Non ci sono mai stata."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 21", "Le vacanze", "Raccontare un viaggio · <b>sono andata a Napoli, abbiamo visitato il centro</b>",
                       [("SAI FARE", "raccontare una vacanza o un viaggio e fare domande sulle vacanze degli altri"),
                        ("LINGUA", "passato prossimo con essere e avere · fa, scorso · ci sono stato/a, non ci sono mai stato/a"),
                        ("PRONUNCIA", "le esclamazioni: Che bello! Che peccato! · raccontare un viaggio")])
    words = [w for _, w, _ in PHOTOS]
    wh = [("Sono andato", "al mare", "in montagna"), ("Abbiamo dormito", "in albergo", "in campeggio"), ("Siamo partiti", "in treno", "in macchina"),
          ("Ho fatto", "il bagno", "le foto")]
    whl = "".join(f'<li>{a} <b>{x}</b> / <b>{y}</b> … {A("", "min-width:40mm")}</li>' for a, x, y in wh)
    b.page(f"""{sec(1, "Riscaldamento: in vacanza", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1]))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "E tu? Nell'ultima vacanza… Sottolinea e completa.", "4 min")}
<ol>{whl}</ol>""",
    29, """<ol><li>A: <i>al mare</i> ma <i>in montagna, in campagna, in città</i>. <i>Fare il bagno</i> = nuotare al mare o in piscina (anche fare la doccia/il bagno a casa).</li>
<li>B: solo da leggere e completare liberamente (<i>…con la mia famiglia, due anni fa</i>). La grammatica del passato con <i>essere</i> è a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: mare, montagna, traghetto… · l'ultima vacanza</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Tre racconti: Napoli e Capri, la pizzeria, il viaggio di nozze</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>passato prossimo con essere / avere · fa, scorso · ci sono stato/a</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Le esclamazioni · raccontare un viaggio</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Una cartolina da Napoli · quando?</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Intervista: la tua ultima vacanza · ci sei mai stato/a?</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Per il ponte di Pasqua Júlia e Giulia sono andate a Napoli in Frecciarossa: centro storico, pizza e una gita a Capri in traghetto. Marco invece è rimasto a Bologna. Davide (che è di Napoli) chiede della pizzeria di suo zio; il Vesuvio no, perché ha piovuto. Al bar la signora Rossi racconta a Giulia il suo viaggio di nozze a Capri, quarant'anni fa.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Ho andato</i> ✗ → <b>sono andata</b> (i verbi di movimento vogliono <i>essere</i>). <i>Siamo andato</i> ✗ → Júlia e Giulia <b>siamo andate</b>. <i>Ho stato</i> ✗ → <b>sono stato</b>. <i>L'anno passato</i> → più naturale <b>l'anno scorso</b>. <i>Fa dieci anni</i> ✗ → <b>dieci anni fa</b> (<i>fa</i> va dopo). <i>In Capri</i> ✗ → <b>a Capri</b> (città e piccole isole).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>lunedì di Pasquetta</b> si fa una gita fuori porta con gli amici. Un <b>ponte</b> è un giorno libero tra la festa e il fine settimana. Le grandi vacanze sono ad agosto: a <b>Ferragosto</b> (15 agosto) molte città sono vuote e molti negozi sono chiusi.</div>
<div class="box"><h4>AUDIO</h4>Traccia 21.1 Tre dialoghi (lento e naturale) · Traccia 21.2 Le esclamazioni · Traccia 21.3 Raccontare un viaggio</div>""")

    # Page 2
    ord_ = [("Hanno preso il traghetto per Capri.", "4"), ("Sono partite venerdì.", "1"), ("Sono tornate lunedì sera.", "5"), ("Hanno visitato il centro storico.", "2"),
            ("Hanno mangiato la pizza.", "3")]
    ordr = "".join(f"<tr><td>{s}</td><td style='width:16mm;text-align:center'>{A(n, 'min-width:9mm')}</td></tr>" for s, n in ord_)
    vf = [("Marco è andato a Capri l'anno scorso.", "F"), ("Marco è rimasto a Bologna per Pasqua.", "V"), ("Júlia e Giulia sono salite sul Vesuvio.", "F"),
          ("Davide è tornato a Napoli a Natale.", "V"), ("La signora Rossi è stata a Capri in viaggio di nozze.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: com'è andata?", "10 min")}
<p>Júlia e Giulia sono tornate da Napoli. Allo studio, sulle scale e al bar raccontano il viaggio.</p>
{audiocard(["21.1 · SLOW", "21.1 · NATURAL"])}
{sub("A", "Ascolta il dialogo uno. Metti in ordine il viaggio di Júlia e Giulia (1–5).", "4 min", "21.1 · SLOW")}
<table style="margin:0">{ordr}</table>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)?", "4 min", "21.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Perché Júlia e Giulia non sono salite sul Vesuvio?", "2 min")}
<div class="wline">{R("Perché sabato ha piovuto tutto il giorno.")}</div>""",
    24, """<ol><li>A: versione <b>lenta</b>. Basta il dialogo uno per l'ordine. <i>Ieri sera</i> = lunedì (il dialogo è martedì).</li>
<li>B: versione <b>naturale</b>. 1: Marco ci è stato <b>dieci anni fa</b>. 3: <b>non ci sono state</b>. <i>Il ponte</i>: vedere «La realtà italiana».</li></ol>""")

    # Page 3
    es = ["andare → <b>andato/a</b>", "partire → <b>partito/a</b>", "tornare → <b>tornato/a</b>", "arrivare → <b>arrivato/a</b>", "rimanere → <b>rimasto/a</b>",
          "stare / essere → <b>stato/a</b>", "salire → <b>salito/a</b>"]
    av = ["visitare → <b>visitato</b>", "mangiare → <b>mangiato</b>", "dormire → <b>dormito</b>", "fare → <b>fatto</b>", "prendere → <b>preso</b>", "vedere → <b>visto</b>"]
    acc = [("io / tu", "sono / sei andato", "sono / sei andata"), ("lui / lei / Lei", "è andato", "è andata"), ("noi / voi", "siamo / siete andati", "siamo / siete andate"),
           ("loro", "sono andati", "sono andate")]
    tacc = "".join(f"<tr><td><b>{p}</b></td><td>{m}</td><td>{f}</td></tr>" for p, m, f in acc)
    rules = [("Júlia", "è partita", "ha partito"), ("Marco", "è rimasto", "ha rimasto"), ("Noi", "abbiamo visitato", "siamo visitati"), ("Giulia e Júlia", "sono tornate", "sono tornati"),
             ("Io (Marco)", "sono stato", "ho stato")]
    rl = "".join(f"<li>{s} <i>{ch([r, w] if i % 2 == 0 else [w, r], r)}</i> …</li>" for i, (s, r, w) in enumerate(rules))
    b.page(f"""{sec(3, "Grammatica: raccontare il passato", "10 min")}
<div class="two"><div>{sub("A", "Con ESSERE: i verbi di movimento e stare.", "3 min")}
<p style="line-height:1.55">{"<br>".join(es)}</p></div>
<div>{sub("B", "Con AVERE: quasi tutti gli altri verbi.", "2 min")}
<p style="line-height:1.55">{"<br>".join(av)}</p>
<p class="small">Con <i>avere</i> il participio non cambia: <i>Júlia <b>ha</b> visitato</i>.</p></div></div>
{sub("C", "Con essere il participio cambia come un aggettivo.", "2 min")}
<table style="margin:0"><tr><th></th><th>maschile</th><th>femminile</th></tr>{tacc}</table>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{rl}</ol>""",
    29, """<ol><li>A: ripasso dell'unità 11 (passato prossimo con <i>avere</i>). Regola pratica: <i>essere</i> con i verbi di movimento verso un luogo (<i>andare, partire, tornare, arrivare, salire</i>) e con <i>stare, essere, rimanere</i>.</li>
<li>C: Júlia e Giulia → <b>andate</b>; Júlia e Marco → <b>andati</b> (un maschile basta). <i>Essere</i> e <i>stare</i> hanno lo stesso participio: <b>stato</b>.</li></ol>""")

    # Page 4: time expressions + mistakes
    tl = [("<b>fa</b> (dopo il tempo)", "due giorni fa · una settimana fa · dieci anni fa"), ("<b>scorso / scorsa</b>", "lunedì scorso · la settimana scorsa · il mese scorso · l'estate scorsa · l'anno scorso"),
          ("<b>ci</b> = in quel posto", "Sei mai stato a Capri? – Sì, <b>ci</b> sono stato. / No, non <b>ci</b> sono <b>mai</b> stato.")]
    ttl = "".join(f"<tr><td style='width:42mm'>{a}</td><td>{x}</td></tr>" for a, x in tl)
    b.page(f"""{sub("E", "Quando? fa · scorso · ci sono stato", "2 min")}
<table style="margin:0">{ttl}</table>
<div style="height:2mm"></div>
{sub("F", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho andato a Napoli.</td><td><b>Sono andata a Napoli.</b></td><td>Movimento: <i>essere</i>.</td></tr>
<tr><td>Io e Giulia siamo andato.</td><td><b>Io e Giulia siamo andate.</b></td><td>Accordo: femminile plurale.</td></tr>
<tr><td>Ho stato a Capri.</td><td><b>Sono stato a Capri.</b></td><td><i>stare / essere</i> → <i>essere</i>.</td></tr>
<tr><td>Fa dieci anni sono stato lì.</td><td><b>Ci sono stato dieci anni fa.</b></td><td><i>fa</i> va dopo il tempo.</td></tr>
<tr><td>Sono stata in Capri.</td><td><b>Sono stata a Capri.</b></td><td>Città e piccole isole: <i>a</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["21.2", "21.3"])}
{sub("A", "Le esclamazioni. Ascolta e ripeti con la voce che sale e poi scende: Che BEL-lo!", "2 min", "21.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S212)}</div>
{sub("B", "Raccontare un viaggio. Ascolta e ripeti.", "3 min", "21.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S213)}</div>""",
    30, """<ol><li>E: <i>scorso</i> concorda: <i>il mese scorso, la settimana scorsa</i>. <i>Ci</i> si mette prima del verbo: <i>ci sono stata</i>.</li>
<li>4A: l'accento forte cade sulla parola importante (<i>Che BELlo!</i>). Reagire così anche ai racconti dello studente nella pagina 6.</li></ol>""")

    # Page 5
    pcg = [("siamo arrivate", "arrivare"), ("siamo salite", "salire"), ("abbiamo mangiato", "mangiare"), ("abbiamo preso", "prendere"), ("abbiamo fatto", "fare"),
           ("è stata", "essere")]
    gaps = [A(x, "min-width:25mm") + f" <span class='small'>({v})</span>" for x, v in pcg]
    when = [("Oggi è il 7 aprile. Júlia è partita il 3 aprile:", "quattro giorni fa"), ("Bruno è arrivato a febbraio, a marzo è tornato in Brasile:", "il mese scorso"),
            ("Davide è andato a Napoli a Natale:", "quattro mesi fa"), ("La signora Rossi è stata in Trentino ad agosto:", "l'estate scorsa")]
    wl = [f'<li value="{i+1}">{s} {A(x, "min-width:30mm")}</li>' for i, (s, x) in enumerate(when)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Una cartolina da Napoli. Completa con il passato prossimo.", "5 min")}
{postcard(gaps)}
{sub("B", "Quando? Scrivi con fa o scorso.", "3 min")}
<ol>{"".join(wl)}</ol>""",
    24, """<ol><li>A: Júlia scrive alla mamma in Brasile. Ricordare l'accordo: Júlia e Giulia = <b>-e</b>. <i>Capri è stata</i> (Capri è femminile).</li>
<li>B: accettare anche <i>il mese scorso</i> per Davide se lo studente conta male; insistere su <b>fa</b> dopo il tempo.</li></ol>""")

    # Page 6
    qs = ["Dove sei andato/a?", "Quando sei partito/a?", "Con chi?", "Come sei andato/a? (treno, aereo…)", "Dove hai dormito?", "Che cosa hai fatto?", "Che cosa hai mangiato?",
          "Quando sei tornato/a?"]
    pl = ["a Roma", "a Venezia", "in Sicilia", "a Capri", "in Toscana", "a Milano"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "La tua ultima vacanza. Prepara le risposte, poi l'insegnante ti fa le domande.", "5 min")}
<table style="margin:1mm 0 2mm">{"".join(f"<tr><td style='width:60mm'><b>{q}</b></td><td></td></tr>" for q in qs)}</table>
{sub("B", "Ci sei mai stato/a? Fai le domande all'insegnante e rispondi anche tu.", "4 min")}
<div class="bank" style="background:#fff">{" · ".join(pl)}</div>
<p class="small">– Sei mai stato/a a Venezia? – Sì, ci sono stato/a due anni fa. / No, non ci sono mai stato/a.</p>
{sub("C", "Rispondi all'insegnante.", "3 min")}
<ol style="line-height:1.65"><li>Preferisci il mare o la montagna? Perché?</li><li>Che cosa hai fatto lo scorso fine settimana?</li><li>Qual è il viaggio più bello della tua vita?</li></ol>""",
    26, """<ol><li>A: l'insegnante reagisce con le esclamazioni della pagina 4 (<i>Che bello! Che peccato!</i>). Correggere <i>essere</i> / <i>avere</i> e l'accordo.</li>
<li>B: anche l'insegnante racconta un viaggio vero in Italia. C: <i>il più bello</i> = superlativo, solo da capire.</li></ol>""")

    # Page 7
    pc = [("Unità 20", "So descrivere una persona."), ("Unità 21", "So raccontare una vacanza."), ("Unità 21", "So scegliere tra essere e avere al passato."),
          ("Unità 21", "So dire quando: fa, scorso."), ("Unità 21", "So dire se ci sono stato/a.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ho andato al mare.", "Sono andato al mare."), ("Giulia è tornato ieri.", "Giulia è tornata ieri."), ("Siamo visitato Sorrento.", "Abbiamo visitato Sorrento."),
          ("Ho stato a Capri.", "Sono stato a Capri."), ("Fa due anni sono andata a Roma.", "Due anni fa sono andata a Roma."), ("L'estate scorso ho fatto il bagno.", "L'estate scorsa ho fatto il bagno.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La tua cartolina.</b> Scrivi una cartolina (6 frasi) da un viaggio vero o immaginario: dove sei andato/a, con chi, che cosa hai fatto.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente legge la sua cartolina e l'insegnante fa due domande. Poi si parla dei ristoranti (unità 22).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("21.1", "Com'è andata? (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("21.2", "Le esclamazioni")}
<p>{" · ".join(S212)}</p>
{sub("21.3", "Raccontare un viaggio")}
<p>{" ".join(S213)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 21 - Le vacanze")
