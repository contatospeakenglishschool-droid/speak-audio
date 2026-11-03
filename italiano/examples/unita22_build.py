# Speak! Essenziale A1 - Unità 22 "Al ristorante" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from menu import menu_card
setup(band="A1 · UNITÀ 22", audio_json=os.path.join(HERE, "audio_it-a1-unita-22.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'antipasto", "antipasto"), ("B", "il primo", "primo"), ("C", "il secondo", "secondo"), ("D", "il contorno", "contorno"),
          ("E", "il dolce", "dolce"), ("F", "il conto", "conto"), ("G", "il cameriere", "cameriere"), ("H", "il menù", "menù")]

SCRIPT = [("Narratore", "Dialogo uno. Al telefono."), ("Cameriere", "Trattoria Il Portico, buonasera!"), ("Júlia", "Buonasera. Vorrei prenotare un tavolo per sabato sera."),
          ("Cameriere", "Per quante persone?"), ("Júlia", "Per tre persone."), ("Cameriere", "A che ora?"), ("Júlia", "Alle otto e mezza."),
          ("Cameriere", "Mi dispiace, alle otto e mezza è tutto pieno. Alle nove va bene?"), ("Júlia", "Sì, va bene."), ("Cameriere", "A che nome?"),
          ("Júlia", "Souza. S, O, U, Z, A."), ("Cameriere", "Perfetto. Tre persone, sabato alle nove. Arrivederci!"),
          ("Narratore", "Dialogo due. Sabato sera, alla trattoria."), ("Cameriere", "Buonasera! Ecco il menù. Che cosa vi porto da bere?"),
          ("Marco", "Una bottiglia di vino rosso della casa e un'acqua frizzante, per favore."), ("Cameriere", "Come antipasto?"),
          ("Luca", "Un tagliere di salumi per tutti."), ("Cameriere", "E di primo?"), ("Júlia", "Io vorrei le tagliatelle al ragù."), ("Luca", "Per me i tortellini in brodo."),
          ("Marco", "Io non prendo il primo. Di secondo prendo la cotoletta alla bolognese."), ("Cameriere", "Con un contorno? Abbiamo patate al forno o insalata mista."),
          ("Marco", "Le patate al forno, grazie."), ("Júlia", "Scusi, il tiramisù è fatto in casa?"), ("Cameriere", "Sì, signora, lo facciamo noi."),
          ("Júlia", "Allora dopo lo prendo!"), ("Luca", "Lo prendo anch'io."),
          ("Narratore", "Dialogo tre. Il conto."), ("Marco", "Scusi, il conto, per favore."), ("Cameriere", "Subito. Ecco: sono novantasei euro, con il coperto."),
          ("Júlia", "Facciamo alla romana? Trentadue euro a testa."), ("Luca", "No, no! Stasera offro io. Oggi è il compleanno di Marco!"),
          ("Júlia", "Davvero? Tanti auguri, Marco!"), ("Marco", "Grazie! E grazie, Luca. Finalmente paghi tu!"), ("Luca", "Si può pagare con la carta?"),
          ("Cameriere", "Certo, nessun problema.")]
S222 = ["acqua", "quanto", "qualcosa", "quattro", "cinquanta", "Quanto costa un'acqua? Quattro euro."]
S223 = ["Vorrei prenotare un tavolo per due.", "Che cosa ci consiglia?", "Per me le tagliatelle al ragù.", "Di secondo prendo la cotoletta.", "Il conto, per favore.",
        "Si può pagare con la carta?"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 22", "Al ristorante", "Prenotare, ordinare, pagare · <b>vorrei le tagliatelle, il conto per favore</b>",
                       [("SAI FARE", "prenotare un tavolo, ordinare da mangiare e da bere e chiedere il conto"),
                        ("LINGUA", "vorrei · prendo · per me · antipasto, primo, secondo, contorno, dolce · lo / la (capire)"),
                        ("PRONUNCIA", "QU e CQU: acqua, quanto, qualcosa · al ristorante")])
    words = [w for _, w, _ in PHOTOS]
    cat = [("le tagliatelle al ragù", "primo"), ("le patate al forno", "contorno"), ("il tiramisù", "dolce"), ("la cotoletta", "secondo"), ("il tagliere di salumi", "antipasto"),
           ("i tortellini in brodo", "primo")]
    catl = [f'<li value="{i+1}">{a} → {A(x, "min-width:22mm")}</li>' for i, (a, x) in enumerate(cat)]
    b.page(f"""{sec(1, "Riscaldamento: il menù", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: w.split()[-1].lstrip("l'")))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Antipasto, primo, secondo, contorno o dolce?", "4 min")}
{twocol(catl, 4)}""",
    28, """<ol><li>A: il pasto italiano ha più parti: <b>antipasto → primo</b> (pasta, riso, minestra) <b>→ secondo</b> (carne o pesce) <b>con contorno → dolce → caffè</b>. Non è obbligatorio prendere tutto.</li>
<li>B: chiedere allo studente che cosa mangia di solito a pranzo in Brasile e come si dice in italiano (<i>riso e fagioli</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: le parti del menù, il conto, il cameriere</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Prenotare al telefono · ordinare · il conto</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>vorrei / prendo / per me · prenotare · lo, la, li, le (capire)</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>QU e CQU · frasi al ristorante</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il menù della trattoria · il conto · un dialogo</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Gioco di ruolo: prenotare e ordinare</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Júlia prenota un tavolo per tre alla Trattoria Il Portico: alle otto e mezza è tutto pieno, va bene alle nove. Sabato sera Júlia, Marco e suo fratello Luca (il capotreno di Firenze, unità 03) ordinano tagliatelle, tortellini, cotoletta e tiramisù. Al momento del conto Júlia propone di fare alla romana, ma Luca offre: è il compleanno di Marco! E Marco ricorda la battuta dell'unità 03: «finalmente paghi tu».</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Voglio la pasta</i> ✗ → al ristorante è troppo diretto: <b>vorrei</b> / <b>prendo</b>. <i>Un tavolo para due</i> ✗ → <b>per due</b>. <i>Il tiramisù? Prendo lui</i> ✗ → <b>lo prendo</b>. <i>È molto gostoso</i> ✗ → <b>è buonissimo</b>. <i>Pagare separato</i> ✗ → <b>pagare separatamente</b> o <b>fare alla romana</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Sul conto c'è spesso il <b>coperto</b> (pane e servizio, 2–3 euro a persona). La <b>mancia</b> non è obbligatoria. L'acqua al ristorante si paga: <b>naturale o frizzante?</b> Dopo pranzo gli italiani prendono un <b>caffè</b> (espresso), non il cappuccino. Si cena tardi: alle 20.30–21.</div>
<div class="box"><h4>AUDIO</h4>Traccia 22.1 Tre dialoghi (lento e naturale) · Traccia 22.2 QU e CQU · Traccia 22.3 Frasi al ristorante</div>""")

    # Page 2
    bk = [("Giorno", "sabato"), ("Ora", "alle nove (21.00)"), ("Persone", "tre"), ("Nome", "Souza")]
    bkr = "".join(f"<tr><th style='width:30mm'>{k}</th><td>{A(v, 'min-width:50mm')}</td></tr>" for k, v in bk)
    who = [("Júlia", "le tagliatelle al ragù", "—", "il tiramisù"), ("Luca", "i tortellini in brodo", "—", "il tiramisù"), ("Marco", "—", "la cotoletta + le patate al forno", "—")]
    whr = "".join(f"<tr><td style='width:18mm'><b>{n}</b></td><td>{A(p, 'min-width:38mm')}</td><td>{A(s, 'min-width:48mm')}</td><td>{A(d, 'min-width:20mm')}</td></tr>"
                  for n, p, s, d in who)
    vf = [("Il conto è di novantasei euro.", "V"), ("Júlia, Marco e Luca pagano alla romana.", "F"), ("Oggi è il compleanno di Luca.", "F"), ("Luca paga con la carta.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: un tavolo per tre", "10 min")}
<p>Júlia telefona a una trattoria. Sabato sera va a cena con Marco e suo fratello Luca.</p>
{audiocard(["22.1 · SLOW", "22.1 · NATURAL"])}
{sub("A", "Dialogo uno. Completa la prenotazione.", "2 min", "22.1 · SLOW")}
<table style="margin:0;width:90mm">{bkr}</table>
{sub("B", "Dialogo due. Che cosa ordinano?", "4 min", "22.1 · SLOW")}
<table style="margin:0"><tr><th></th><th>Primo</th><th>Secondo e contorno</th><th>Dolce</th></tr>{whr}</table>
{sub("C", "Dialogo tre. Ascolta la versione naturale. Vero (V) o falso (F)?", "4 min", "22.1 · NATURAL")}
<table style="margin:0">{vfr}</table>""",
    30, """<ol><li>A–B: versione <b>lenta</b>. Tutti prendono il tagliere di salumi come antipasto; da bere vino rosso della casa e acqua frizzante.</li>
<li>C: versione <b>naturale</b>. <i>Alla romana</i> = ognuno paga la stessa parte. <i>Offro io</i> = pago io per tutti. 3: è il compleanno di <b>Marco</b>.</li></ol>""")

    # Page 3
    ordr = [("<b>Vorrei</b> …", "Vorrei le tagliatelle al ragù.", "gentile, sempre giusto"), ("<b>Prendo</b> …", "Di secondo prendo la cotoletta.", "normale, molto usato"),
            ("<b>Per me</b> …", "Per me i tortellini in brodo.", "veloce, quando ordinano tutti")]
    tor = "".join(f"<tr><td style='width:22mm'>{a}</td><td>{x}</td><td class='small'>{n}</td></tr>" for a, x, n in ordr)
    cw = [("il cliente", "Vorrei prenotare un tavolo per… · Il conto, per favore. · Si può pagare con la carta? · Che cosa ci consiglia?"),
          ("il cameriere", "Per quante persone? · A che ora? · A che nome? · Che cosa vi porto da bere? · E di primo?")]
    tcw = "".join(f"<tr><td style='width:22mm'><b>{a}</b></td><td>{x}</td></tr>" for a, x in cw)
    pr = [("il tiramisù", "<b>lo</b> prendo"), ("la cotoletta", "<b>la</b> prendo"), ("i tortellini", "<b>li</b> prendo"), ("le patate", "<b>le</b> prendo")]
    tpr = "".join(f"<tr><td>{a}? → {x}</td></tr>" for a, x in pr)
    rules = [("Cameriere, ", "vorrei", "voglio", " un'acqua naturale, per favore."), ("Un tavolo ", "per", "para", " quattro persone."),
             ("Il tiramisù? ", "Lo", "La", " prendo anch'io."), ("Le tagliatelle? ", "Le", "Li", " facciamo noi."), ("", "Il conto", "La conta", ", per favore.")]
    rl = "".join(f"<li>{a}<i>{ch([r, w] if i % 2 == 0 else [w, r], r)}</i>{z}</li>" for i, (a, r, w, z) in enumerate(rules))
    b.page(f"""{sec(3, "Grammatica: ordinare e prenotare", "10 min")}
{sub("A", "Ordinare: tre modi.", "3 min")}
<table style="margin:0">{tor}</table>
{sub("B", "Le domande al ristorante.", "2 min")}
<table style="margin:0">{tcw}</table>
<div class="two"><div>{sub("C", "Lo, la, li, le: per non ripetere.", "2 min")}
<table style="margin:0">{tpr}</table>
<p class="small" style="margin-top:1mm">Prima del verbo. Basta capirli: in A2 si studiano bene.</p></div>
<div>{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{rl}</ol></div></div>""",
    30, """<ol><li>A: <i>voglio</i> esiste, ma con il cameriere sembra un ordine: meglio <b>vorrei</b> o <b>prendo</b>. <i>Per me…</i> si usa quando si ordina insieme.</li>
<li>C: <b>lo, la, li, le</b> = il tiramisù, la cotoletta… (come <i>non la conosco</i> nell'unità 20, solo da capire). Nel dialogo: <i>lo facciamo noi · lo prendo anch'io</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Voglio la pasta.</td><td><b>Vorrei la pasta.</b></td><td>Più gentile con il cameriere.</td></tr>
<tr><td>Un tavolo para due.</td><td><b>Un tavolo per due.</b></td><td><i>para</i> non esiste: <i>per</i>.</td></tr>
<tr><td>Il tiramisù? Prendo lui.</td><td><b>Il tiramisù? Lo prendo.</b></td><td>Per le cose: <i>lo / la</i> prima del verbo.</td></tr>
<tr><td>La pasta è molto gostosa.</td><td><b>La pasta è buonissima.</b></td><td><i>gostoso</i> → <i>buono</i>.</td></tr>
<tr><td>Possiamo pagare separato?</td><td><b>Possiamo pagare separatamente?</b></td><td>O: <i>facciamo alla romana</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["22.2", "22.3"])}
{sub("A", "QU e CQU. Ascolta e ripeti: si pronuncia sempre «cu» + vocale: AC-qua, QUAN-to.", "2 min", "22.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S222)}</div>
{sub("B", "Frasi al ristorante. Ascolta e ripeti.", "3 min", "22.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S223)}</div>""",
    40, """<ol><li>Errori: <i>gostoso</i> non esiste in italiano. Per il cibo: <i>buono, buonissimo, ottimo</i>.</li>
<li>4A: in <i>acqua</i> la C e la Q fanno un suono solo, un po' più lungo (come una doppia). Non dire «água» né «aqua».</li></ol>""")

    # Page 5
    dl = [("Cameriere", "Buonasera! Avete prenotato?", ""), ("Giulia", "Sì, un tavolo per due, a nome Bianchi.", ""),
          ("Cameriere", "Prego. Che cosa vi porto da bere?", ""), ("Giulia", "", "Un'acqua naturale, per favore."), ("Cameriere", "E da mangiare?", ""),
          ("Giulia", "", "Vorrei le lasagne e, come dolce, la panna cotta.")]
    dll = "".join(f"<tr><td style='width:22mm'><b>{n}:</b></td><td>{t if t else A(x, 'min-width:110mm')}</td></tr>" for n, t, x in dl)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Leggi il menù della trattoria.", "1 min")}
{menu_card()}
{sub("B", "Il conto. Quanto pagano? Guarda il menù (con il coperto).", "3 min")}
<ol><li>Júlia, Marco e Luca: tagliere, tagliatelle, tortellini, cotoletta, patate, due tiramisù, vino e acqua. Totale: {A("€ 96", "min-width:22mm")}</li>
<li>Giulia: lasagne, panna cotta e acqua naturale. Totale: {A("€ 21", "min-width:22mm")}</li></ol>
{sub("C", "Completa il dialogo. Giulia ordina (vedi l'esercizio B, numero 2).", "4 min")}
<table style="margin:0">{dll}</table>""",
    24, """<ol><li>B1: 14 + 12 + 13 + 16 + 5 + 6 + 6 + 16 + 2 = 90 + coperto 6 (3 × 2) = <b>96</b>, come nel dialogo. B2: 12 + 5 + 2 + 2 = <b>21</b>.</li>
<li>C: accettare <i>prendo / per me</i>. Chi finisce prima legge il dialogo ad alta voce con l'insegnante.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Al telefono. Prenota un tavolo alla Trattoria Il Portico. L'insegnante è il cameriere.", "4 min")}
<div class="box"><b>Studente:</b> giorno? · quante persone? · a che ora? · a nome di…<br><b>Insegnante:</b> a quell'ora è tutto pieno: proponi un'altra ora.</div>
{sub("B", "Alla trattoria. Ordina con il menù della pagina 5: da bere, un primo o un secondo, un contorno e un dolce. Poi chiedi il conto e paga con la carta.", "5 min")}
<p class="small">Che cosa ci consiglia? · È fatto in casa? · Per me… · Vorrei… · Il conto, per favore. · Si può pagare con la carta?</p>
{sub("C", "Rispondi all'insegnante.", "3 min")}
<ol style="line-height:1.65"><li>Qual è il tuo ristorante preferito? Che cosa prendi di solito?</li><li>In Brasile si paga il coperto? E la mancia?</li><li>Hai mai mangiato le tagliatelle al ragù o i tortellini?</li></ol>""",
    28, """<ol><li>A: l'insegnante fa il cameriere e rende la prenotazione un po' difficile (tutto pieno, il nome da compitare). Poi si cambiano i ruoli.</li>
<li>B: mettere sul tavolo un menù vero o quello della pagina 5. Correggere <i>voglio → vorrei</i>. C: in Brasile il servizio è spesso del 10% sul conto.</li></ol>""")

    # Page 7
    pc = [("Unità 21", "So raccontare una vacanza."), ("Unità 22", "So prenotare un tavolo."), ("Unità 22", "So ordinare da mangiare e da bere."),
          ("Unità 22", "So chiedere il conto e pagare."), ("Unità 22", "So le parti del menù italiano.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Voglio un caffè, cameriere.", "Vorrei un caffè."), ("Un tavolo para tre, per favore.", "Un tavolo per tre."), ("Il tiramisù? Prendo lui.", "Lo prendo."),
          ("La pizza è molto gostosa!", "La pizza è buonissima!"), ("La conta, per favore.", "Il conto, per favore."), ("Di primo prendo la cotoletta.", "Di secondo prendo la cotoletta.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Il tuo menù.</b> Scrivi il menù di una cena speciale per i tuoi amici: un antipasto, un primo, un secondo con contorno e un dolce.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: lo studente presenta il suo menù e l'insegnante ordina. Poi si passa alle istruzioni e all'imperativo (unità 23).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("22.1", "Un tavolo per tre (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("22.2", "QU e CQU")}
<p>{" · ".join(S222)}</p>
{sub("22.3", "Frasi al ristorante")}
<p>{" ".join(S223)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 22 - Al ristorante")
