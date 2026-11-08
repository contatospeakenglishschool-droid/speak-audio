# Speak! Essenziale A1 - Ripasso 4 (Unità 28-35), tutto in italiano - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · RIPASSO 4", audio_json=os.path.join(HERE, "audio_it-a1-ripasso-4.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la valigia", "Unità 28"), ("B", "la stanza", "Unità 29"), ("C", "il modulo", "Unità 30"), ("D", "la SIM", "Unità 31"),
          ("E", "l'autobus", "Unità 32"), ("F", "il cinema", "Unità 33"), ("G", "la lampada", "Unità 34"), ("H", "l'invito", "Unità 35")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-ripasso-4"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S43 = lines("R4.1 Intervista"), lines("R4.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R4.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A1 · RIPASSO 4", "Ripasso 4", "Unità 28–35 · il ritorno · la stanza · l'università · il telefono · l'autobus · il cinema · il mercatino · l'invito",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 28–35 e chiudere il livello A1"),
                        ("LINGUA", "perché / per · i numeri grandi · chi, quale, quanto · mi serve · da… a… · mi è piaciuto · questo / quello · le date"),
                        ("PRONUNCIA", "dettato di frasi · al telefono e al cinema")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">l'autobus · il cinema · l'invito · la lampada · il modulo · la SIM · la stanza · la valigia</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Esempio:</b> la stanza → <i>La stanza di Bruno costa 380 euro al mese.</i></p>""",
    22, """<p>Le foto A–H vengono dalle unità 28–35, in ordine. Accettare qualsiasi frase corretta: <i>Júlia ha fatto la valigia. Come si scrive il tuo nome? Mi serve una SIM. Prendo l'autobus e scendo alla Fiera. Il film mi è piaciuto. Quanto costa quella lampada? È arrivato l'invito.</i> Correggere <i>perché studiare</i>, <i>ho piaciuto</i>, <i>quello tappeto</i>.</p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>28–35</td><td>1</td></tr>
<tr><td>2 Ascolto: l'intervista a Bruno</td><td>10 min</td><td>28–35</td><td>2</td></tr>
<tr><td>3 Grammatica: perché / per, numeri, domande, mi serve</td><td>10 min</td><td>28–31</td><td>3</td></tr>
<tr><td>4 Grammatica: autobus, mi è piaciuto, questo / quello, date</td><td>10 min</td><td>32–35</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>28–35</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>8 min</td><td>28–35</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>28–35</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Settembre. Júlia torna dal Brasile perché arriva Bruno, che viene a Bologna per studiare (unità 28). Bruno cerca una stanza e trova quella di Paolo in via Zamboni, 380 euro spese incluse (29); si iscrive a Storia: Souza, con la zeta (30); compra una SIM italiana (31) e un abbonamento per l'autobus 20 (32); va al cinema con Chiara (33) e al mercatino per arredare la stanza (34). Arriva l'invito al matrimonio di Luca e Sara, sabato 26 settembre a Firenze (35). Domenica 20 Davide intervista Bruno per il suo progetto sui primi giorni in Italia, come aveva fatto con Júlia nel Ripasso 1. Il matrimonio continua nell'A2 Ponte, unità 1.</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Viene perché studiare</i> → <b>per studiare</b> 2. <i>Mi serve molti giga</i> → <b>Mi servono</b> 3. <i>Ho piaciuto il film</i> → <b>Mi è piaciuto</b> 4. <i>quello tappeto</i> → <b>quel tappeto</b> 5. <i>in 26 di settembre</i> → <b>il 26 settembre</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia R4.1 Intervista (lenta e naturale) · Traccia R4.2 Dettato di frasi · Traccia R4.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("l'università", True), ("il cognome", True), ("la stanza e l'affitto", True), ("l'autobus", True), ("il tempo", False),
              ("le cose che servono", True), ("un matrimonio", True), ("il cinema", True), ("pagare al bar", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Bruno studia Medicina.", "F: studia Storia."), ("Souza si scrive con la zeta.", "V"),
          ("La stanza costa 380 euro, spese escluse.", "F: spese incluse."), ("Bruno ha comprato le cose della stanza al mercatino.", "V"),
          ("Per il centro sportivo Bruno prende il 20.", "V"), ("Il matrimonio di Luca è domenica.", "F: è sabato 26."),
          ("A Bruno la commedia non è piaciuta.", "F: gli è piaciuta, ma la fine no."), ("Bruno paga i caffè.", "F: offre Giulia.")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: l'intervista a Bruno", "10 min")}
<p>Domenica 20 settembre. Al bar di Giulia, Davide fa un'intervista a Bruno per il suo progetto: i primi giorni in Italia.</p>
{audiocard(["R4.1 · SLOW", "R4.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) otto argomenti. Un argomento è in più.", "3 min", "R4.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R4.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nell'intervista un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>per + infinito</td><td>{R("Sono venuto per studiare Storia.")}</td></tr><tr><td>un numero grande</td><td>{R("trecentottanta euro")}</td></tr>
<tr><td>mi servono</td><td>{R("Mi servono dei libri per l'università.")}</td></tr><tr><td>mi è piaciuto / piaciuta</td><td>{R("Mi è piaciuta molto, ma la fine no.")}</td></tr></table>""",
    18, """<p>A: argomento in più = <span class="red">il tempo</span>. B: lo studente corregge a voce le frasi false; 7: <i>gli è piaciuta</i> solo da capire. C: se serve, lo studente può leggere la trascrizione nell'ultima pagina della guida.</p>""")

    # Page 3: grammar 28-31
    pp = [("Bruno è a Bologna ___ studiare.", ["per"]), ("Júlia è tornata ___ arriva Bruno.", ["perché"]),
          ("Ho comprato un adattatore ___ caricare il telefono.", ["per"]), ("Stasera non esco ___ devo studiare.", ["perché"])]
    ppl = "".join(f"<li>{fill(s, a)}</li>" for s, a in pp)
    nm = [("380 €", "trecentottanta euro"), ("1.000 €", "mille euro"), ("2.500 €", "duemilacinquecento euro"), ("700 €", "settecento euro")]
    nml = [f'<li value="{i+1}">{n} {A(x, "min-width:42mm")}</li>' for i, (n, x) in enumerate(nm)]
    qw = [("___ è il tuo indirizzo?", ["Qual"]), ("___ corsi avete?", ["Quali"]), ("___ anni hai?", ["Quanti"]),
          ("___ costa la stanza?", ["Quanto"]), ("___ studi? — Storia.", ["Che cosa"]), ("___ è Chiara? — La ragazza di Bruno.", ["Chi"])]
    qwl = [f'<li value="{i+1}">{fill(s, a, "16mm")}</li>' for i, (s, a) in enumerate(qw)]
    sv = [("Mi ___ una SIM.", ["serve"]), ("Mi ___ molti giga.", ["servono"]), ("Scusi, ___ ripetere? (Lei)", ["può"]), ("___ pagare con la carta?", ["Posso"])]
    svl = "".join(f"<li>{fill(s, a, '16mm')}</li>" for s, a in sv)
    b.page(f"""{sec(3, "Grammatica: unità 28–31", "10 min")}
<div class="two"><div>{sub("A", "Unità 28. Perché o per?", "2 min")}<ol>{ppl}</ol></div>
<div>{sub("B", "Unità 31. Mi serve, mi servono, posso, può.", "2 min")}<ol>{svl}</ol></div></div>
{sub("C", "Unità 29. Scrivi i prezzi in lettere.", "3 min")}
{twocol(nml, 3)}
{sub("D", "Unità 30. Completa con: chi, che cosa, qual, quali, quanto, quanti.", "3 min")}
{twocol(qwl, 4)}""",
    24, """<ol><li>A: <i>per</i> + infinito (lo scopo), <i>perché</i> + frase (la ragione). B: <i>mi serve</i> + singolare, <i>mi servono</i> + plurale; con <i>Lei</i>: <i>può</i>.</li>
<li>C: i numeri si scrivono attaccati: <i>duemilacinquecento</i>; <i>mille</i> → <i>duemila</i>. D: <i>qual è</i> senza apostrofo.</li></ol>""")

    # Page 4: grammar 32-35
    bs = [("L'autobus passa ___ sei ___ ventitré.", ["dalle", "alle"]), ("Vado ___ via Rizzoli ___ centro sportivo.", ["da", "al"]),
          ("Scendo ___ sesta fermata.", ["alla"]), ("Vado all'università ___ piedi.", ["a"])]
    bsl = "".join(f"<li>{fill(s, a, '11mm')}</li>" for s, a in bs)
    pi = [("Il film mi ___.", ["è piaciuto"]), ("La commedia mi ___.", ["è piaciuta"]), ("Gli attori mi ___.", ["sono piaciuti"]), ("Le scene al parco mi ___.", ["sono piaciute"])]
    pil = "".join(f"<li>{fill(s, a, '24mm')}</li>" for s, a in pi)
    qq = [("Mi piace ___ (lontano) tappeto ___ (blu).", ["quel", "blu"]), ("___ (vicino) sedie sono ___ (bianco).", ["Queste", "bianche"]),
          ("Quanto costa ___ (lontano) specchio?", ["quello"]), ("Preferisco ___ (lontano) libri ___ (rosso).", ["quei", "rossi"])]
    qql = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in qq)
    dt = [("Il matrimonio è ___ 26 settembre.", ["il"]), ("La festa è ___ ottobre (1/10).", ["il primo"]), ("___ 8 marzo è la festa della donna.", ["L'"]),
          ("Vieni alla festa? — Sì, ___ volentieri!", ["vengo"])]
    dtl = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in dt)
    mk = [("Bruno viene perché studiare.", "Bruno viene per studiare."), ("La stanza costa duemille euro all'anno.", "duemila euro"),
          ("Qual'è il tuo indirizzo?", "Qual è il tuo indirizzo?"), ("Ho piaciuto il film.", "Mi è piaciuto il film."), ("Quello tappeto è bello.", "Quel tappeto è bello.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 32–35", "10 min")}
<div class="two"><div>{sub("A", "Unità 32. In autobus.", "2 min")}<ol>{bsl}</ol></div>
<div>{sub("B", "Unità 33. Mi è piaciuto…", "2 min")}<ol>{pil}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 34. Questo, quello e i colori.", "2 min")}<ol>{qql}</ol></div>
<div>{sub("D", "Unità 35. Le date e gli inviti.", "2 min")}<ol>{dtl}</ol></div></div>
{sub("E", "Unità 28–35. Correggi gli errori.", "2 min")}
<ol>{mkl}</ol>""",
    28, """<ol><li>A: <i>da… a…</i> per i luoghi, <i>dalle… alle…</i> per le ore; <i>a piedi</i>, <i>in autobus</i>. B: il participio concorda con la cosa che piace.</li>
<li>C: <i>quello</i> davanti al nome cambia come l'articolo (<i>il → quel, i → quei</i>); <i>blu</i> non cambia. D: chi è invitato risponde <i>vengo</i>.</li></ol>""")

    # Page 5: vocabulary
    cats = [("La casa", "l'affitto · le spese · la cauzione"), ("Il telefono", "la SIM · i giga · il caricabatterie"),
            ("L'autobus", "la fermata · l'abbonamento · l'autista"), ("Il cinema", "la commedia · l'horror · lo schermo")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    df = [("Lo paghi ogni mese per la stanza.", "l'affitto"), ("Con questo prendi l'autobus tutto il mese.", "l'abbonamento"),
          ("Un film che fa ridere.", "la commedia"), ("Il mercato delle cose usate.", "il mercatino"),
          ("Gli anelli degli sposi.", "le fedi"), ("Serve quando la presa è diversa.", "l'adattatore")]
    dfl = [f'<li value="{i+1}">{a} {A(x, "min-width:24mm")}</li>' for i, (a, x) in enumerate(df)]
    od = [("rosso · verde · bianco · la lampada", "la lampada (non è un colore)"), ("il giallo · l'horror · la commedia · la fermata", "la fermata"),
          ("il matrimonio · gli sposi · le fedi · la cauzione", "la cauzione")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    sp = [("zeta · a · emme · bi · o · enne · i", "Zamboni"), ("ci · i · enne · e · emme · a", "cinema"), ("effe · i · erre · e · enne · zeta · e", "Firenze")]
    spl = "".join(f"<li>{a} → {A(x, 'min-width:24mm')}</li>" for a, x in sp)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 29–33. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">l'abbonamento · l'affitto · l'autista · il caricabatterie · la cauzione · la commedia · la fermata · i giga · l'horror · lo schermo · le spese · la SIM</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Unità 29–35. Che cos'è?", "2 min")}
{twocol(dfl, 4)}
<div class="two"><div>{sub("C", "Unità 33–35. Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div>
<div>{sub("D", "Unità 30. Come si scrive? Scrivi la parola.", "1 min")}<ol>{spl}</ol></div></div>""",
    20, """<p>A: accettare anche <i>il biglietto</i> se lo studente lo aggiunge (autobus e cinema). B: <i>l'affitto</i> ≠ <i>le spese</i> (luce, gas, acqua). D: lo studente fa lo spelling del suo nome e cognome, come Bruno all'università.</p>""")

    # Page 6: dictation + social Italian
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Luca", "Ciao Bruno! Júlia mi ha detto che vieni al matrimonio. Sei contento?", ""), ("Bruno", "Sì, moltissimo! Grazie per invitare.", "Grazie per l'invito"),
          ("Luca", "Ti serve qualcosa per sabato?", ""), ("Bruno", "Sì, io servo una cravatta!", "mi serve"),
          ("Luca", "Ah ah! Chiedi a Júlia. Allora ci vediamo sabato?", ""), ("Bruno", "Sì, in ventisei di settembre. Arriviamo alle nove e mezza.", "sabato ventisei")]
    d2 = [("Chiara", "Buonasera. Due biglietti per la commedia delle diciannove e trenta, per favore.", ""), ("Cassiere", "Siete studenti? Allora sei euro l'uno.", ""),
          ("Bruno", "(dopo il film) Hai piaciuto il film?", "Ti è piaciuto"), ("Chiara", "Sì! Mi è piaciuto molto gli attori.", "Mi sono piaciuti"),
          ("Bruno", "Andiamo a casa in piedi?", "a piedi"), ("Chiara", "Sì, è vicino.", "")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "8 min")}
{audiocard(["R4.2", "R4.3"])}
{sub("A", "Unità 28–35. Dettato. Ascolta e scrivi le frasi.", "3 min", "R4.2")}
<ol style="line-height:1.35">{dal}</ol>
{sub("B", "Unità 31, 33 e 35. Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R4.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: al telefono</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: al cinema</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un altro invito, un altro film.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Ogni frase ripassa un'unità, dalla 28 alla 35. Controllare <i>trecentottanta</i> (una parola), le doppie (<i>adattatore, quella</i>) e <i>è</i> con l'accento.</li>
<li>B: dialogo 1: <i>Grazie per l'invito</i>, <i>mi serve</i>, <i>sabato ventisei</i> (senza <i>in</i> e <i>di</i>). Dialogo 2: <i>Ti è piaciuto</i>, <i>Mi sono piaciuti</i>, <i>a piedi</i>. L'audio ha le versioni corrette.</li></ol>""")

    # Page 7: reflect
    cd = [("28", "So spiegare perché faccio una cosa (perché…, per…)."), ("29", "So capire un annuncio e i numeri grandi."),
          ("30", "So compilare un modulo e fare lo spelling del mio nome."), ("31", "So dire che cosa mi serve e chiedere il permesso."),
          ("32", "So prendere l'autobus e spiegare un percorso."), ("33", "So dire che cosa mi è piaciuto e che cosa no."),
          ("34", "So comprare e scegliere: questo o quello? Di che colore?"), ("35", "So dire le date e rispondere a un invito.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi per l'A2. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>Le mie prime settimane.</b> Immagina di arrivare in una città italiana. Scrivi un'e-mail a un amico (60–80 parole):</p>
<ol><li>perché sei lì (per… / perché…);</li><li>dove abiti e quanto costa;</li><li>come vai all'università o al lavoro (autobus, a piedi…);</li><li>una cosa che ti è piaciuta e una che non ti è piaciuta;</li><li>un invito con la data (Ti va di… il…?).</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività di ripasso prima dell'A2. Il compito usa la grammatica delle unità 28–35: correggerlo e conservarlo come esempio di scrittura di fine A1. Prossimo livello: <b>A2 Ponte · 01 Che cosa mi metto?</b> (la settimana prima del matrimonio di Luca e Sara).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R4.1", "L'intervista a Bruno (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R4.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R4.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S43)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 36 - Ripasso 4")
