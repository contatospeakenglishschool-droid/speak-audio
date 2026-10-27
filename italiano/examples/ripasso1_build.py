# Speak! Essenziale A1 - Ripasso 1 (Unità 01-08), tutto in italiano - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · RIPASSO 1", audio_json=os.path.join(HERE, "audio_it-a1-ripasso-1.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "Piacere!", "Unità 01"), ("B", "l'Italia", "Unità 02"), ("C", "un medico", "Unità 03"), ("D", "il cappuccino", "Unità 04"),
          ("E", "andare in bicicletta", "Unità 05"), ("F", "leggere", "Unità 06"), ("G", "la piazza", "Unità 07"), ("H", "la valigia", "Unità 08")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-ripasso-1"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S13 = lines("R1.1 Intervista"), lines("R1.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R1.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A1 · RIPASSO 1", "Ripasso 1", "Unità 01–08 · presentarsi · la giornata · i gusti · la città · l'albergo",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 01–08 e decidere che cosa ripassare"),
                        ("LINGUA", "essere · avere · verbi in -are, -ere, -ire · mi piace · c'è / ci sono · al, nel, dal…"),
                        ("PRONUNCIA", "numeri, ore e prezzi · al bar e per strada")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola o l'espressione. Poi di' una frase con la parola.", "5 min")}
<div class="bank">andare in bicicletta · il cappuccino · l'Italia · la piazza · la valigia · leggere · un medico · Piacere!</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Esempio:</b> il cappuccino → <i>La mattina prendo un cappuccino al bar.</i></p>""",
    22, """<p>Le foto A–H vengono dalle unità 01–08, in ordine. Accettare qualsiasi frase corretta: <i>Il medico lavora in ospedale. Mi piace leggere. Vado allo studio in bicicletta. In piazza c'è una chiesa.</i> Correggere gli articoli e la terza persona dei verbi.</p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>01–08</td><td>1</td></tr>
<tr><td>2 Ascolto: l'intervista di Davide</td><td>10 min</td><td>01–08</td><td>2</td></tr>
<tr><td>3 Grammatica: essere, avere, articoli, plurale</td><td>8 min</td><td>01–04</td><td>3</td></tr>
<tr><td>4 Grammatica: verbi, piacere, c'è / ci sono, preposizioni</td><td>10 min</td><td>05–08</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>8 min</td><td>02–08</td><td>5</td></tr>
<tr><td>6 Pronuncia e italiano sociale</td><td>9 min</td><td>03–07</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>01–08</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Dicembre. Davide fa un progetto per l'università, «Stranieri a Bologna», e intervista Júlia: il nome e il passaporto italiano (unità 01–02), il lavoro allo studio (03), la colazione al bar di Giulia (04), la sua giornata (05), che cosa le piace di Bologna (06), che cosa c'è vicino a casa (07) e i genitori all'Hotel Due Torri (08).</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Io chiamo…</i> → <b>Mi chiamo…</b> 2. <i>Sono de…</i> → <b>Sono di…</b> 3. <i>Mi piace i…</i> → <b>Mi piacciono i…</b> 4. <i>C'è due…</i> → <b>Ci sono due…</b> 5. <i>in la / a il</i> → <b>nella / al</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia R1.1 Intervista (lenta e naturale) · Traccia R1.2 Dettato di numeri e ore · Traccia R1.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("nome e origine", True), ("il lavoro", True), ("la giornata", True), ("le vacanze al mare", False), ("i gusti", True), ("il quartiere", True), ("la famiglia", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Júlia è di Rio de Janeiro.", "F: è di Belo Horizonte."), ("Júlia ha il passaporto italiano.", "V"), ("Lo studio è in via Indipendenza.", "V"),
          ("La colazione costa tre euro e settanta.", "F: costa due euro e sessanta."), ("Júlia finisce di lavorare alle sei.", "V"), ("A Júlia piace la mortadella.", "F: non le piace."),
          ("Vicino a casa ci sono due supermercati.", "V"), ("I genitori dormono a casa di Júlia.", "F: dormono all'Hotel Due Torri.")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: l'intervista", "10 min")}
<p>È dicembre. Davide fa un progetto per l'università: «Stranieri a Bologna». Intervista Júlia.</p>
{audiocard(["R1.1 · SLOW", "R1.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) sei argomenti. Un argomento è in più.", "3 min", "R1.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R1.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nell'intervista un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>chiamarsi / avere</td><td>{R("Mi chiamo Júlia Souza · ho anche il passaporto italiano")}</td></tr><tr><td>un verbo in -are / -ire</td><td>{R("Lavoro in uno studio · apro lo studio · Finisco alle sei")}</td></tr>
<tr><td>mi piace / mi piacciono</td><td>{R("Mi piacciono i portici · non mi piace la mortadella")}</td></tr><tr><td>c'è / ci sono · preposizione articolata</td><td>{R("C'è una farmacia, ci sono due supermercati · all'Hotel, nel centro")}</td></tr></table>""",
    18, """<p>A: argomento in più = <span class="red">le vacanze al mare</span>. B: lo studente corregge a voce le frasi false. C: se serve, lo studente può leggere la trascrizione nell'ultima pagina della guida.</p>""")

    # Page 3: grammar 01-04
    vt = [("io", "sono", "ho", "mi chiamo"), ("tu", "sei", "hai", "ti chiami"), ("lui / lei / Lei", "è", "ha", "si chiama")]
    vtr = "".join(f"<tr><td>{p}</td><td>{A(a, 'min-width:16mm')}</td><td>{A(bb, 'min-width:16mm')}</td><td>{A(c, 'min-width:24mm')}</td></tr>" for p, a, bb, c in vt)
    nn = [("studente", "lo", "uno"), ("acqua", "l'", "un'"), ("cornetto", "il", "un"), ("zucchero", "lo", "uno"), ("architetta", "l'", "un'"), ("pizzeria", "la", "una"), ("ospedale", "l'", "un"), ("scontrino", "lo", "uno")]
    nnr = "".join(f"<tr><td>{A(d, 'min-width:10mm')} / {A(i, 'min-width:10mm')} {n}</td></tr>" for n, d, i in nn)
    pl = [("un cornetto", "due cornetti"), ("una pizza", "tre pizze"), ("un caffè", "due caffè"), ("un cameriere", "due camerieri"), ("una nazionalità", "tre nazionalità"), ("un euro", "cinque euro")]
    pll = "".join(f"<li>{a} → {A(x, 'min-width:28mm')}</li>" for a, x in pl)
    tl_ = [("Ciao! Come ti chiami?", "Buongiorno! Come si chiama?"), ("Come stai?", "Come sta?"), ("Di dove sei? Sei brasiliano?", "Di dov'è? È brasiliano?")]
    tll = "".join(f"<li>{a}<div class='wline'>{R(x)}</div></li>" for a, x in tl_)
    b.page(f"""{sec(3, "Grammatica: unità 01–04", "8 min")}
{sub("A", "Unità 01–02. Completa la tabella.", "2 min")}
<table style="margin:0"><tr><th></th><th>essere</th><th>avere</th><th>chiamarsi</th></tr>{vtr}</table>
<div class="two"><div>{sub("B", "Unità 03–04. Scrivi l'articolo determinativo e indeterminativo.", "2 min")}
<table style="margin:0">{nnr}</table></div>
<div>{sub("C", "Unità 04. Scrivi il plurale.", "2 min")}<ol>{pll}</ol>
{sub("D", "Unità 01. Dal tu al Lei.", "2 min")}<ol>{tll}</ol></div></div>""",
    26, """<ol><li>B: <i>ospedale</i> = maschile + vocale → <i>l'ospedale / un ospedale</i> (senza apostrofo). <i>architetta</i> = femminile + vocale → <i>un'architetta</i>.</li>
<li>C: parole con l'accento (<i>caffè, nazionalità</i>) ed <i>euro</i> non cambiano. D: il <b>Lei</b> usa il verbo della terza persona.</li></ol>""")

    # Page 4: grammar 05-08
    vw = [("Tu dove", "lavori", "?", "lavorare"), ("Marco", "prende", "un caffè al banco.", "prendere"), ("Io", "finisco", "alle sei.", "finire"), ("Io la sera", "esco", "con gli amici.", "uscire"),
          ("Tu", "vai", "in palestra?", "andare"), ("Da dove", "vieni", ", Davide?", "venire"), ("Davide", "dorme", "fino alle dieci.", "dormire"), ("Lei", "capisce", "l'italiano?", "capire")]
    vl = [f'<li value="{i+1}">{a} {A(v, "min-width:16mm")} {c} <span class="small">({n})</span></li>' for i, (a, v, c, n) in enumerate(vw)]
    pw = [("Mi", "piacciono", "i film italiani."), ("Ti", "piace", "cucinare?"), ("Non mi", "piace", "il calcio."), ("A Júlia", "piacciono", "i portici.")]
    pwl = "".join(f'<li>{a} {A(x, "min-width:20mm")} {c}</li>' for a, x, c in pw)
    cw = [("Nel centro", "ci sono", "molti negozi."), ("", "C'è", "un bancomat qui vicino?"), ("La camera è", "al", "secondo piano."), ("Il bancomat è", "nella", "banca."),
          ("I genitori vengono", "dal", "Brasile."), ("La colazione è", "dalle", "sette alle dieci.")]
    cwl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")} {c}</li>' for i, (a, x, c) in enumerate(cw)]
    mk = [("Io mai vado in palestra.", "Non vado mai in palestra."), ("Sono l'una e mezza.", "È l'una e mezza."), ("Abito in Bologna.", "Abito a Bologna."),
          ("Io tengo un passaporto italiano.", "Ho un passaporto italiano."), ("Vorrei reservare una camera.", "Vorrei prenotare una camera.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 05–08", "10 min")}
{sub("A", "Unità 03–08. Completa con il verbo.", "3 min")}
{twocol(vl, 5)}
<div class="two"><div>{sub("B", "Unità 06. Piace o piacciono?", "2 min")}<ol>{pwl}</ol></div>
<div>{sub("C", "Unità 07–08. Completa con c'è, ci sono, al, nella, dal, dalle.", "2 min")}<ol>{"".join(cwl)}</ol></div></div>
{sub("D", "Unità 02–08. Correggi gli errori.", "3 min")}
<ol>{mkl}</ol>""",
    22, """<ol><li>A: irregolari da controllare: <i>esco, vai, vieni</i>; <i>finire</i> e <i>capire</i> con <i>-isc-</i>.</li>
<li>D: chiedere allo studente <i>perché?</i> per ogni correzione. Sono gli errori più frequenti delle unità 02–08.</li></ol>""")

    # Page 5: vocabulary
    nat = [("Italia", "italiano", "italiana"), ("Brasile", "brasiliano", "brasiliana"), ("Francia", "francese", "francese"), ("Spagna", "spagnolo", "spagnola"), ("Giappone", "giapponese", "giapponese")]
    natr = "".join(f"<tr><td>{p}</td><td>{A(m, 'min-width:24mm')}</td><td>{A(f, 'min-width:24mm')}</td></tr>" for p, m, f in nat)
    jb = [("lavora in ospedale e aiuta il medico.", "l'infermiera / l'infermiere"), ("porta il caffè al tavolo.", "il cameriere"), ("lavora in un negozio.", "il commesso / la commessa"), ("lavora sui treni.", "il capotreno")]
    jbl = "".join(f'<li>Chi {a} {A(x, "min-width:34mm")}</li>' for a, x in jb)
    df = [("Compri le medicine qui.", "la farmacia"), ("Prendi i soldi qui.", "il bancomat"), ("Compri il pane qui.", "il forno"), ("Prendi il treno qui.", "la stazione"),
          ("In albergo, per due persone.", "la camera doppia"), ("In albergo, per andare al quarto piano.", "l'ascensore")]
    dfl = [f'<li value="{i+1}">{a} {A(x, "min-width:28mm")}</li>' for i, (a, x) in enumerate(df)]
    od = [("il caffè · il cornetto · la spremuta · la chiesa", "la chiesa"), ("leggere · ballare · nuotare · la valigia", "la valigia"), ("dritto · a destra · a sinistra · in pensione", "in pensione")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "8 min")}
<div class="two"><div>{sub("A", "Unità 02. Le nazionalità.", "2 min")}
<table style="margin:0"><tr><th>Paese</th><th>uomo</th><th>donna</th></tr>{natr}</table></div>
<div>{sub("B", "Unità 03. Chi è?", "2 min")}<ol>{jbl}</ol></div></div>
{sub("C", "Unità 04, 07, 08. Che cos'è?", "2 min")}
{twocol(dfl, 4)}
{sub("D", "Unità 04–07. Qual è la parola diversa?", "2 min")}
<ol>{odl}</ol>""",
    20, """<p>A: le nazionalità in <b>-e</b> sono uguali per uomo e donna. B: accettare il maschile o il femminile. D: chiedere perché: <i>la chiesa non si mangia!</i></p>""")

    # Page 6: pronunciation + social Italian
    da = ["8:30", "1:00", "1,40 €", "333 19 15 07", "camera 21 · 2° piano", "17 studenti", "7:00–10:00", "90 € a notte"]
    dal = [f'<li value="{i+1}">{A(x, "min-width:38mm")}</li>' for i, x in enumerate(da)]
    d1 = [("A", "Buongiorno! Io quero un caffè e un cornetto, per favore.", "Vorrei un caffè"), ("B", "Il cornetto vuoto o a la crema?", "alla crema"), ("A", "Vuoto. Quanto è?", "Quant'è?"),
          ("B", "Sono due euros e trenta.", "due euro"), ("A", "Ecco. Posso di pagare con la carta?", "Posso pagare")]
    d2 = [("A", "Scusi, tiene una farmacia qui vicino?", "c'è una farmacia"), ("B", "Sì, c'è due farmacie. Una è in via Verdi, accanto a la chiesa.", "ci sono due · accanto alla"),
          ("A", "È lontano?", ""), ("B", "No. Va dritto e prende la primo strada a sinistra.", "la prima strada")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Pronuncia e italiano sociale", "9 min")}
{audiocard(["R1.2", "R1.3"])}
{sub("A", "Unità 03–05, 08. Dettato. Ascolta e scrivi i numeri, le ore e i prezzi.", "3 min", "R1.2")}
{twocol(dal, 5)}
{sub("B", "Unità 04 e 07. Ogni dialogo ha degli errori. Correggi. Poi ascolta e controlla.", "4 min", "R1.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: al bar</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: per strada</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: il tuo bar, una farmacia vicino a casa tua.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Accettare l'ora in cifre o in lettere. Poi lo studente detta all'insegnante tre numeri di telefono o prezzi.</li>
<li>B: 5 errori nel dialogo 1 e 4 nel dialogo 2 (la frase B del dialogo 2 ne ha due). L'audio ha le versioni corrette.</li></ol>""")

    # Page 7: reflect
    cd = [("01", "So salutare e presentarmi con il tu e con il Lei."), ("02", "So dire di dove sono e la nazionalità."), ("03", "So dire che lavoro faccio e dove abito; so i numeri 0–20."),
          ("04", "So ordinare al bar e pagare; so i numeri fino a 100."), ("05", "So dire l'ora e parlare della mia giornata."), ("06", "So dire che cosa mi piace e reagire."),
          ("07", "So chiedere e dare indicazioni in città."), ("08", "So prenotare una camera in albergo.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>Un messaggio a Davide.</b> Anche tu partecipi al progetto «Stranieri a Bologna». Scrivi a Davide (60–80 parole):</p>
<ol><li>come ti chiami, di dove sei e che lavoro fai;</li><li>com'è la tua giornata (con le ore);</li><li>che cosa ti piace e che cosa non ti piace;</li><li>che cosa c'è vicino a casa tua.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività di ripasso per le prossime lezioni. Il compito usa tutta la grammatica delle unità 01–08: correggerlo con attenzione e conservarlo come esempio di scrittura.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R1.1", "L'intervista (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R1.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R1.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S13)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 09 - Ripasso 1")
