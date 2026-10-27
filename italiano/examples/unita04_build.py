# Speak! Essenziale A1 - Unità 04 "Al bar" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 04", audio_json=os.path.join(HERE, "audio_it-a1-unita-04.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il caffè", "caffè"), ("B", "il cappuccino", "cappuccino"), ("C", "il cornetto", "cornetto"), ("D", "la spremuta", "spremuta"),
          ("E", "l'acqua", "acqua"), ("F", "il tramezzino", "tramezzino"), ("G", "lo zucchero", "zucchero"), ("H", "lo scontrino", "scontrino")]

SCRIPT = [("Narratore", "Dialogo uno. Al banco, la mattina."), ("Giulia", "Buongiorno, ragazzi! Che cosa prendete?"),
          ("Júlia", "Vorrei un cappuccino e un cornetto, per favore."), ("Marco", "Per me un caffè."), ("Giulia", "Il cornetto vuoto o alla crema?"),
          ("Júlia", "Alla crema, grazie."), ("Marco", "Júlia, in Brasile prendi il caffè piccolo così?"),
          ("Júlia", "No, in Brasile il caffè è grande! Ma questo è buonissimo."),
          ("Narratore", "Dialogo due. Alla cassa."), ("Júlia", "Quant'è?"),
          ("Giulia", "Allora: un cappuccino, un caffè e un cornetto… sono tre euro e settanta."), ("Júlia", "Ecco cinque euro."),
          ("Giulia", "E un euro e trenta di resto. Ecco lo scontrino. Grazie!"), ("Marco", "Grazie, Júlia! Domani offro io."),
          ("Narratore", "Dialogo tre. Il pomeriggio, al tavolo."), ("Giulia", "Ciao, Júlia! Ciao, Davide! Che cosa prendete?"),
          ("Júlia", "Vorrei un cappuccino, per favore."), ("Giulia", "Un cappuccino? Alle quattro del pomeriggio? Va bene… sei brasiliana!"),
          ("Davide", "Io prendo un tramezzino e due bottiglie d'acqua frizzante."), ("Giulia", "Perfetto. Due acque, un tramezzino e un cappuccino."),
          ("Davide", "Il conto, per favore."), ("Giulia", "Sono dodici euro."), ("Davide", "Dodici euro? Ah, è vero: al tavolo costa di più!")]
S042 = ["venti", "ventuno", "ventotto", "trenta", "trentatré", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta", "cento",
        "un euro e venti", "tre euro e settanta", "dodici euro e cinquanta"]
S043 = ["Vorrei un caffè, per favore.", "Per me un cappuccino.", "Prendo un cornetto alla crema.", "Quant'è?", "Quanto costa un tramezzino?",
        "Posso pagare con la carta?", "Il conto, per favore."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 04", "Al bar", "Ordinare e pagare · <b>i numeri fino a 100</b>",
                       [("SAI FARE", "ordinare al bar, chiedere il prezzo e pagare"), ("LINGUA", "il / lo / la / l' · i plurali · prendo, prendi, prende · vorrei"),
                        ("PRONUNCIA", "i numeri fino a 100 e i prezzi · ordinare con gentilezza")])
    words = ["il caffè", "il cappuccino", "il cornetto", "il tramezzino", "la spremuta", "l'acqua", "lo scontrino", "lo zucchero"]
    items = ["il caffè", "il cornetto", "la spremuta", "il tramezzino", "l'acqua", "il cappuccino"]
    drink = "il caffè, la spremuta, l'acqua, il cappuccino"
    food = "il cornetto, il tramezzino"
    b.page(f"""{sec(1, "Riscaldamento: al bar", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Da bere o da mangiare? Scrivi le parole nella colonna giusta.", "4 min")}
<div class="bank" style="background:#fff">{" · ".join(items)}</div>
<table style="margin:0"><tr><th style="width:50%">Da bere</th><th>Da mangiare</th></tr><tr><td style="height:9mm">{R(drink)}</td><td>{R(food)}</td></tr></table>""",
    28, """<ol><li>A: in Italia <b>il caffè</b> = l'espresso, piccolo. <b>Il cornetto</b> (a Bologna anche <i>la brioche</i>) è la colazione tipica. <b>Lo scontrino</b> = la ricevuta del bar.</li>
<li>A: far notare l'articolo: <b>lo</b> zucchero, <b>lo</b> scontrino (come <i>uno studente</i>, unità 3). B: chiedere: <i>Che cosa prendi a colazione?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 parole del bar con foto · da bere / da mangiare</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Ordinare e pagare al bar di Giulia: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Articolo determinativo singolare · plurale dei nomi · <i>prendere</i> · <i>vorrei</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Numeri fino a 100 e prezzi · frasi per ordinare</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Articoli · plurali · <i>prendere</i></td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Il listino del Bar Giulia: gioco di ruolo · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 01–04) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>La mattina Júlia e Marco fanno colazione al banco del Bar Giulia: cappuccino, cornetto e caffè. Paga Júlia (3,70 €) e Marco promette: «Domani offro io». Il pomeriggio Júlia ordina un cappuccino alle quattro… e Giulia ride. Davide paga 12 € al tavolo e scopre che al tavolo costa di più.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Io quero un caffè</i> ✗ → <b>Vorrei un caffè</b>. <i>Tre euros</i> ✗ → <b>tre euro</b> (euro non cambia al plurale). <i>Due caffès</i> ✗ → <b>due caffè</b>. <i>Lo cappuccino / il acqua</i> ✗ → <b>il cappuccino / l'acqua</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Al <b>banco</b> (in piedi) costa meno che al <b>tavolo</b>. Il <b>cappuccino</b> si prende di solito solo la mattina. In molti bar si paga prima alla <b>cassa</b> e poi si dà lo scontrino al barista. I prezzi si scrivono con la virgola: <b>3,70 €</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia 04.1 Tre dialoghi (lento e naturale) · Traccia 04.2 Numeri e prezzi · Traccia 04.3 Ordinare</div>""")

    # Page 2
    who = [("Júlia (mattina)", "un cappuccino e un cornetto alla crema"), ("Marco", "un caffè"), ("Júlia (pomeriggio)", "un cappuccino"), ("Davide", "un tramezzino e due acque frizzanti")]
    wr = "".join(f"<tr><td style='width:36mm'><b>{n}</b></td><td>{A(x, 'min-width:80mm')}</td></tr>" for n, x in who)
    pr = [("Dialogo 2: la colazione costa", "3,70 €"), ("Júlia dà", "5,00 €"), ("Il resto è", "1,30 €"), ("Dialogo 3: il conto è", "12,00 €")]
    pl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")}</li>' for i, (a, x) in enumerate(pr)]
    b.page(f"""{sec(2, "Ascolto: al Bar Giulia", "10 min")}
<p>La mattina Júlia e Marco fanno colazione al bar di Giulia. Il pomeriggio Júlia torna con Davide.</p>
{audiocard(["04.1 · SLOW", "04.1 · NATURAL"])}
{sub("A", "Ascolta. Che cosa prendono?", "4 min", "04.1 · SLOW")}
<table style="margin:0">{wr}</table>
{sub("B", "Ascolta di nuovo. Scrivi i prezzi.", "4 min", "04.1 · NATURAL")}
{twocol(pl, 3)}
{sub("C", "Perché Giulia dice «Un cappuccino? Alle quattro del pomeriggio?»", "2 min")}
<div class="wline">{R("Perché in Italia il cappuccino si prende di solito solo la mattina, a colazione.")}</div>""",
    28, """<ol><li>A: versione <b>lenta</b>. <i>Che cosa prendete?</i> = domanda a due persone (voi): solo da capire. <i>Cornetto vuoto</i> = senza crema.</li>
<li>B: versione <b>naturale</b>. Scrivere i prezzi con la virgola. <i>Offro io</i> = pago io per te.</li>
<li>C: aprire una breve discussione: <i>E in Brasile? Quando prendi il caffè con il latte?</i></li></ol>""")

    # Page 3
    art = [("il", "il caffè, il cornetto, il tramezzino", "maschile + consonante"), ("lo", "lo zucchero, lo scontrino, lo yogurt", "maschile + s + consonante, z, y"),
           ("la", "la spremuta, la brioche, la cassa", "femminile + consonante"), ("l'", "l'acqua, l'aranciata, l'espresso", "maschile o femminile + vocale")]
    plu = [("-o → -i", "il cornetto → due cornett<b>i</b>"), ("-a → -e", "la spremuta → due spremut<b>e</b>"), ("-e → -i", "il bicchiere → due bicchier<b>i</b>"),
           ("non cambia", "il caffè → due caffè · il bar → due bar")]
    pv = [("io", "prendo"), ("tu", "prendi"), ("lui / lei", "prende"), ("Lei (formale)", "prende")]
    rules = [("", "il cappuccino", "lo cappuccino"), ("", "l'acqua", "la acqua"), ("due", "cornetti", "cornetto"), ("tre", "caffè", "caffès")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    ta = "".join(f"<tr><td><b>{a}</b></td><td>{e}</td><td class='small'>{n}</td></tr>" for a, e, n in art)
    tp = "".join(f"<tr><td class='small'><b>{a}</b></td><td>{e}</td></tr>" for a, e in plu)
    tv = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in pv)
    b.page(f"""{sec(3, "Grammatica: il, lo, la, l' · plurale · prendere", "10 min")}
{sub("A", "L'articolo determinativo (singolare).", "3 min")}
<table style="margin:0"><tr><th style="width:12mm"></th><th>Esempi</th><th>Quando?</th></tr>{ta}</table>
{sub("B", "Il plurale dei nomi.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="2">Singolare → plurale</th></tr>{tp}</table></div>
<div><table style="margin:0"><tr><th colspan="2">prendere (verbi in -ere)</th></tr>{tv}</table>
<div class="box" style="margin-top:2mm"><h4>VORREI</h4><b>Vorrei</b> + cosa = modo gentile per ordinare. Anche: <b>Per me…</b> / <b>Prendo…</b></div></div></div>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>REGOLA</h4>Le parole con l'accento finale (<i>caffè, tè</i>) e le parole straniere (<i>bar, toast</i>) <b>non cambiano</b> al plurale. Anche <b>euro</b> non cambia: <i>un euro, tre euro</i>.</div>""",
    22, """<ol><li>A: <i>lo</i> segue la stessa regola di <i>uno</i> (unità 3). <i>l'</i> davanti a vocale per maschile e femminile.</li>
<li>B: altri verbi in <i>-ere</i>: <i>leggere, scrivere, vedere</i>. Gli altri plurali degli articoli (<i>i, gli, le</i>) arrivano nella prossima unità.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Io quero un caffè.</td><td><b>Vorrei un caffè.</b></td><td><i>Vorrei</i> è più gentile.</td></tr>
<tr><td>Sono tre euros.</td><td><b>Sono tre euro.</b></td><td><i>Euro</i> non cambia.</td></tr>
<tr><td>Due caffès, per favore.</td><td><b>Due caffè, per favore.</b></td><td>Accento finale: non cambia.</td></tr>
<tr><td>Il acqua frizzante.</td><td><b>L'acqua frizzante.</b></td><td>Vocale = <i>l'</i>.</td></tr>
<tr><td>Quanto è?</td><td><b>Quant'è? / Quanto costa?</b></td><td>Si dice con l'apostrofo.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["04.2", "04.3"])}
{sub("A", "Numeri e prezzi. Ascolta e ripeti.", "2 min", "04.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S042)}</div>
{sub("B", "Ordinare con gentilezza. Ascolta e ripeti.", "3 min", "04.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S043)}</div>""",
    38, """<ol><li>Errori: <i>euros</i> è l'errore più frequente. In italiano <i>euro</i> è invariabile.</li>
<li>4A: davanti a <i>uno</i> e <i>otto</i> le decine perdono la vocale: <i>ventuno, ventotto, trentuno</i>. <i>Trentatré</i> ha l'accento. Prezzi: <i>tre euro e settanta</i> (3,70 €). Dettare 4 prezzi allo studente.</li>
<li>4B: attenzione alle doppie: <i>cappuccino, frizzante, cornetto</i> (una sola T!). L'intonazione gentile sale alla fine: <i>per favore ↗</i>.</li></ol>""")

    # Page 5
    aw = ["il", "lo", "la", "l'", "il", "lo", "la", "l'"]
    an = ["tramezzino", "zucchero", "cassa", "acqua", "bar", "scontrino", "brioche", "aranciata"]
    al = [f'<li value="{i+1}">{A(aw[i], "min-width:12mm")} {an[i]}</li>' for i in range(8)]
    pw = [("un cornetto", "due cornetti"), ("una spremuta", "tre spremute"), ("un caffè", "due caffè"), ("un bicchiere", "quattro bicchieri"), ("un tramezzino", "due tramezzini"), ("un euro", "dieci euro")]
    pl5 = [f'<li value="{i+1}">{a} → {A(x, "min-width:30mm")}</li>' for i, (a, x) in enumerate(pw)]
    vw = [("Io", "prendo", "un caffè."), ("Che cosa", "prendi", ", Davide?"), ("Marco", "prende", "un cornetto vuoto."), ("Signora, Lei che cosa", "prende", "?")]
    vl = "".join(f'<li>{a} {A(v, "min-width:18mm")} {c}</li>' for a, v, c in vw)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con il, lo, la o l'.", "2 min")}
{twocol(al, 5)}
{sub("B", "Scrivi il plurale.", "3 min")}
{twocol(pl5, 4)}
{sub("C", "Completa con il verbo prendere.", "3 min")}
<ol>{vl}</ol>""",
    24, """<ol><li>A: 5 <i>il bar</i> (parola straniera, consonante); 7 <i>la brioche</i> (parola francese, femminile).</li>
<li>B: 3 e 6: <i>caffè</i> ed <i>euro</i> non cambiano. C: chiedere allo studente: <i>E tu, che cosa prendi al bar?</i></li></ol>""")

    # Page 6
    menu = [("Caffè (espresso)", "1,10", "2,50"), ("Cappuccino", "1,40", "3,50"), ("Cornetto", "1,20", "2,50"), ("Spremuta d'arancia", "3,00", "5,00"),
            ("Tramezzino", "3,50", "5,00"), ("Acqua frizzante (bottiglia)", "1,00", "1,75")]
    mt = "".join(f"<tr><td>{n}</td><td style='text-align:right'>{a} €</td><td style='text-align:right'>{t} €</td></tr>" for n, a, t in menu)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Il listino del Bar Giulia. Gioco di ruolo: tu sei il cliente, l'insegnante è il barista. Ordina, chiedi il prezzo e paga. Poi scambiate i ruoli.", "7 min")}
<div class="ad" style="max-width:130mm;margin:1mm auto 2mm"><b class="t" style="text-align:center">BAR GIULIA · LISTINO PREZZI</b>
<table style="margin:1mm 0 0"><tr><th></th><th style="text-align:right">al banco</th><th style="text-align:right">al tavolo</th></tr>{mt}</table></div>
<div class="bank" style="background:#fff">Buongiorno! · Vorrei… · Per me… · Prendo… · Quanto costa…? · Quant'è? · Posso pagare con la carta? · Il conto, per favore. · Ecco…</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Che cosa prendi a colazione? A casa o al bar?</li><li>Quanto costa un caffè nella tua città?</li><li>Prendi il caffè con lo zucchero?</li><li>Al bar preferisci il banco o il tavolo? Perché?</li></ol>""",
    30, """<ol><li>A: situazione 1 al banco (2 cose), situazione 2 al tavolo (3–4 cose, con il conto). Lo studente calcola il totale: es. cappuccino + cornetto al banco = <b>2,60 €</b>; al tavolo = <b>6,00 €</b>. I prezzi sono quelli dei dialoghi: colazione di Júlia al banco = 3,70 €; conto di Davide al tavolo = 12,00 €. Con lo studente come barista, l'insegnante paga con 10 € e chiede il resto.</li>
<li>B: correggere articoli e <i>euro</i>. <i>Preferisci</i> = verbo in <i>-ire</i> (prossima unità).</li></ol>""")

    # Page 7
    pc = [("Unità 02", "So dire di dove sono e la nazionalità."), ("Unità 03", "So dire che lavoro faccio e dove abito."),
          ("Unità 04", "So ordinare al bar e chiedere il prezzo."), ("Unità 04", "So usare il, lo, la, l' e il plurale dei nomi."), ("Unità 04", "So capire i prezzi (numeri fino a 100).")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Io quero un cappuccino.", "Vorrei un cappuccino."), ("Sono cinque euros.", "Sono cinque euro."), ("Lo cornetto è buonissimo.", "Il cornetto è buonissimo."),
          ("Due tramezzino, per favore.", "Due tramezzini, per favore."), ("Il acqua costa un euro.", "L'acqua costa un euro."), ("Marco prendi un caffè.", "Marco prende un caffè.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Al bar.</b> Scrivi un breve dialogo (5–6 battute) tra te e il barista: ordini, chiedi il prezzo e paghi.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi leggere il dialogo insieme: lo studente è il cliente, l'insegnante è il barista e cambia il prezzo per far usare i numeri.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("04.1", "Al Bar Giulia (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("04.2", "Numeri e prezzi")}
<p>{" · ".join(S042)}</p>
{sub("04.3", "Ordinare")}
<p>{" ".join(S043)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 04 - Al bar")
