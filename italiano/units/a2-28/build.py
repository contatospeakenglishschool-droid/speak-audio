# Speak! Ponte A2 - Ripasso 3 (Unità 20-27), tutto in italiano - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
import speak_engine as _se
_se.SERIES = "Ponte"
setup(band="A2 · RIPASSO 3", audio_json=os.path.join(HERE, "audio_it-a2-ripasso-3.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "gli appunti", "Unità 20"), ("B", "la valigia", "Unità 21"), ("C", "il ventilatore", "Unità 22"), ("D", "i fuochi d'artificio", "Unità 23"),
          ("E", "l'anguria", "Unità 24"), ("F", "l'ombrellone", "Unità 25"), ("G", "la casetta", "Unità 26"), ("H", "il campanello", "Unità 27")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-ripasso-3"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S33 = lines("R3.1 Conversazione"), lines("R3.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R3.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def fill(s, ans, w="14mm"):
        parts = s.split("___")
        return "".join(p + (A(ans[i], f"min-width:{w}") if i < len(ans) else "") for i, p in enumerate(parts))
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A2 · RIPASSO 3", "Ripasso 3", "Unità 20–27 · esami · partenze · caldo · estate · quartiere · prestiti · mare · notizie",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 20–27 dell'A2"),
                        ("LINGUA", "cominciare a, smettere di · prima di + infinito · sarà · che bello! · qualche, nessuno · te lo · casetta, le braccia · dice che, per te"),
                        ("PRONUNCIA", "dettato di frasi · sulle scale e al telefono")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">l'anguria · gli appunti · il campanello · la casetta · i fuochi d'artificio · l'ombrellone · la valigia · il ventilatore</div>
{photo_grid(T, PHOTOS)}""",
    30, """<p>Le foto A–H vengono dalle unità 20–27, in ordine. Chiedere una frase con la grammatica dell'unità: <i>Ho finito di ripassare gli appunti (20). Prima di partire, preparo la valigia (21). Il ventilatore non funziona: sarà rotto (22). Che belli i fuochi d'artificio! (23). Ognuno porta qualcosa: io porto l'anguria (24). L'ombrellone? Te lo presto (25). Abbiamo una casetta al mare (26). Bruno dice che il campanello è un regalo per lei (27).</i></p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>20–27</td><td>1</td></tr>
<tr><td>2 Ascolto: festa per Bruno</td><td>10 min</td><td>20–27</td><td>2</td></tr>
<tr><td>3 Grammatica: verbi + a / di, prima di, futuro, esclamazioni</td><td>10 min</td><td>20–23</td><td>3</td></tr>
<tr><td>4 Grammatica: indefiniti, pronomi combinati, alterati, dice che</td><td>10 min</td><td>24–27</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>20–27</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>8 min</td><td>20–27</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>20–27</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano. Il ripasso non ha la pagina di riferimento grammaticale: se serve, tornare alla pagina 4 dell'unità.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Fine giugno: il primo esame di Bruno, ventotto (unità 20). Luglio: Giulia e Davide partono per la Puglia, Júlia annaffia le piante (21); l'ondata di caldo, l'aria condizionata rotta in ufficio (22). Agosto: le foto della Puglia e il concerto alla Montagnola (23); il pranzo di Ferragosto in cortile (24); la signora Rossi presta a Júlia la borsa frigo e l'ombrellone, Júlia presta la bici a Bruno (25); la settimana nella casetta di Rimini (26). Settembre: le novità del palazzo (il signor Neri va a Milano, arriva una nuova vicina) e il campanello regalato da Bruno (27). Oggi, giovedì: Bruno ha l'ultimo esame dell'estate e prende ventinove; festa al bar di Giulia.</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Ho finito studiare</i> → <b>Ho finito di studiare</b> 2. <i>Prima di parto</i> → <b>Prima di partire</b> 3. <i>Te lo presto</i> (la bici) → <b>Te la presto</b> 4. <i>Ho i bracci rossi</i> → <b>Ho le braccia rosse</b> 5. <i>Vieni con io?</i> → <b>Vieni con me?</b></div>
<div class="box"><h4>AUDIO</h4>Traccia R3.1 Conversazione (lenta e naturale) · Traccia R3.2 Dettato di frasi · Traccia R3.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("l'esame di Bruno", True), ("lo studio d'estate", True), ("il mare", True), ("un dolce", True), ("la bici", True),
              ("una gita in bici", True), ("un brindisi", True), ("la nuova vicina", False)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Bruno non risponde al telefono.", "V"), ("Bruno ha preso trenta.", "F: ha preso ventinove."),
          ("Ad agosto Bruno usciva tutte le sere.", "F: ha smesso di uscire la sera."), ("Prima dell'esame Bruno ha ripassato tutti i capitoli.", "V"),
          ("Giulia regala a Bruno un tortino al cioccolato.", "V"), ("Júlia non presta più la bici a Bruno.", "F: gliela presta ancora."),
          ("Marco propone una gita in bici per domani.", "V"), ("Domani Bruno vuole studiare tutto il giorno.", "F: vuole dormire.")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: festa per Bruno", "10 min")}
<p>Giovedì sera, metà settembre. Al bar di Giulia, Júlia e Marco aspettano Bruno: oggi ha l'ultimo esame dell'estate.</p>
{audiocard(["R3.1 · SLOW", "R3.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) sette argomenti. Un argomento è in più.", "3 min", "R3.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R3.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>verbo + a / di + infinito</td><td>{R("ho cominciato a studiare · ho smesso di uscire · ho deciso di dormire")}</td></tr>
<tr><td>futuro di supposizione</td><td>{R("Sarà ancora all'università.")}</td></tr><tr><td>esclamazione</td><td>{R("Che bella notizia! Quanto sono contenta!")}</td></tr>
<tr><td>pronome combinato</td><td>{R("me la presti? · Te la presto.")}</td></tr><tr><td>discorso indiretto</td><td>{R("La signora Rossi dice che eri sempre al mare.")}</td></tr></table>""",
    22, """<p>A: argomento in più = <span class="red">la nuova vicina</span> (arriva nella pagina 6). B: lo studente corregge a voce le frasi false. C: altri esempi: <i>prima di entrare</i> (21), <i>se domani farà bel tempo</i> (22), <i>qualche giorno, nessuno</i> (24), <i>un tortino, un tortone</i> (26), <i>per te, per me</i> (27).</p>""")

    # Page 3: grammar 20-23
    vp = [("Ho cominciato ___ studiare a maggio.", ["a"]), ("Smetti ___ preoccuparti!", ["di"]), ("Non riesco ___ dormire.", ["a"]), ("Ho deciso ___ partire domani.", ["di"])]
    vpl = "".join(f"<li>{fill(s, a, '10mm')}</li>" for s, a in vp)
    pd = [("(partire) Prima di ___, chiudo il gas.", ["partire"]), ("(cena) Prima ___ cena, annaffio le piante.", ["di"]),
          ("(vestirsi) Prima di ___, faccio la doccia.", ["vestirmi"]), ("(uscire) Prima di ___, controllo i documenti.", ["uscire"])]
    pdl = "".join(f"<li>{fill(s, a, '18mm')}</li>" for s, a in pd)
    fs = [("Dov'è Marco? — Non lo so, ", ["sarà", "è stato"], "sarà", " in ufficio."), ("Quanti anni ha? — ", ["Avrà", "Ha avuto"], "Avrà", " trent'anni."),
          ("Se domani ", ["farà", "fa stato"], "farà", " caldo, andremo al mare.")]
    fsl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in fs)
    eb = [("Che ___ albergo! (bello)", ["bell'"]), ("Che ___ occhiali! (bello)", ["begli"]), ("Che ___ idea! (buono)", ["buon'"]), ("___ gente! (quanto)", ["Quanta"])]
    ebl = "".join(f"<li>{fill(s, a, '14mm')}</li>" for s, a in eb)
    b.page(f"""{sec(3, "Grammatica: unità 20–23", "10 min")}
<div class="two"><div>{sub("A", "Unità 20. A o di?", "2 min")}<ol>{vpl}</ol></div>
<div>{sub("B", "Unità 21. Prima di + infinito o nome.", "3 min")}<ol>{pdl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 22. Il futuro: supposizione e se. Scegli.", "2 min")}<ol>{fsl}</ol></div>
<div>{sub("D", "Unità 23. Esclamazioni: bello, buono, quanto.", "3 min")}<ol>{ebl}</ol></div></div>""",
    26, """<ol><li>A: <i>cominciare, riuscire, provare, imparare</i> + <b>a</b>; <i>finire, smettere, decidere, ricordarsi</i> + <b>di</b>. B: con i riflessivi il pronome si attacca all'infinito: <i>prima di vestir<b>mi</b></i>.</li>
<li>C: <i>sarà / avrà</i> = probabilmente è / ha. D: <i>bello</i> come l'articolo: <i>bell'albergo</i> (l'albergo), <i>begli occhiali</i> (gli occhiali); <i>buon'idea</i> con l'apostrofo (femminile).</li></ol>""")

    # Page 4: grammar 24-27
    ind = [("In cortile c'è ancora ___ vicino.", ["qualche"]), ("___ negozio è chiuso per ferie.", ["Ogni"]), ("Non c'è ___ in casa: sono tutti al mare.", ["nessuno"]),
           ("Hai fame? — No, non voglio ___.", ["niente"])]
    indl = "".join(f"<li>{fill(s, a, '16mm')}</li>" for s, a in ind)
    pc = [("Mi presti la bici? — Sì,", ["te la", "te lo"], "te la", "presto."), ("Mi lasci le chiavi? — Sì,", ["te le", "te li"], "te le", "lascio."),
          ("Mi dai il caricabatterie? — No, non", ["te lo", "lo te"], "te lo", "do."), ("L'ombrellone? Júlia", ["glielo", "gli lo"], "glielo", "riporta domenica.")]
    pcl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in pc)
    al = [("Una casa piccola: una ___.", ["casetta"]), ("Un letto grande: un ___.", ["lettone"]), ("Mi fanno male le ___. (braccio)", ["braccia"]),
          ("Ho comprato sei ___. (uovo)", ["uova"])]
    all_ = "".join(f"<li>{fill(s, a, '16mm')}</li>" for s, a in al)
    di = [("«Vado a Milano.» → Neri dice che ___ a Milano.", ["va"]), ("«Il mio esame è giovedì.» → Dice che ___ esame è giovedì.", ["il suo"]),
          ("Vieni al cinema con ___ (io)?", ["me"]), ("Questo regalo è per ___ (tu).", ["te"])]
    dil = "".join(f"<li>{fill(s, a, '12mm')}</li>" for s, a in di)
    mk = [("Ho finito studiare.", "Ho finito di studiare."), ("Prima di parto, chiudo il gas.", "Prima di partire, chiudo il gas."),
          ("La bici? Te lo presto.", "La bici? Te la presto."), ("Ho i bracci rossi.", "Ho le braccia rosse."), ("Vieni con io?", "Vieni con me?")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 24–27", "10 min")}
<div class="two"><div>{sub("A", "Unità 24. Qualche, ogni, nessuno, niente.", "2 min")}<ol>{indl}</ol></div>
<div>{sub("B", "Unità 25. I pronomi combinati. Scegli.", "2 min")}<ol>{pcl}</ol></div></div>
<div class="two"><div>{sub("C", "Unità 26. Nomi alterati e plurali in -a.", "2 min")}<ol>{all_}</ol></div>
<div>{sub("D", "Unità 27. Dice che… e i pronomi tonici.", "2 min")}<ol>{dil}</ol></div></div>
{sub("E", "Unità 20–27. Correggi gli errori.", "2 min")}
<ol>{mkl}</ol>""",
    26, """<ol><li>A: <i>qualche</i> + singolare (<i>qualche vicino</i> = alcuni vicini); doppia negazione: <i>non c'è nessuno, non voglio niente</i>. B: il diretto segue la cosa: <i>la bici → la, le chiavi → le</i>; <i>glielo</i> in una parola.</li>
<li>C: <i>le braccia, le uova</i> sono femminili. D: nel discorso indiretto cambiano la persona e il possessivo, non il tempo; dopo la preposizione: <i>me, te</i>.</li></ol>""")

    # Page 5: vocabulary
    cats = [("Lo studio", "gli appunti · l'evidenziatore · l'aula"), ("Il caldo", "il ventilatore · la zanzara · il ventaglio"),
            ("Il mare", "l'ombrellone · il lettino · la crema solare"), ("Il palazzo", "il cortile · il vicino · il padrone di casa")]
    cth = "".join(f"<th>{c}</th>" for c, _ in cats)
    ctd = "".join(f"<td style='height:15mm;vertical-align:top'>{R(w) if T else ''}</td>" for _, w in cats)
    wb = [("prestare", "il prestito"), ("restituire", "la restituzione"), ("festeggiare", "la festa"), ("trasferirsi", "il trasferimento"),
          ("affittare", "l'affitto"), ("riparare", "la riparazione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:26mm")}</li>' for i, (v, n) in enumerate(wb)]
    df = [("Il tempo con molto vento:", "ventoso"), ("Il letto della spiaggia:", "il lettino"), ("Si dice prima di bere insieme:", "Cin cin! (il brindisi)"),
          ("Il cartello dei negozi ad agosto:", "chiuso per ferie")]
    dfl = "".join(f"<li>{a} {A(x, 'min-width:24mm')}</li>" for a, x in df)
    od = [("la valigia · il costume · i sandali · il termometro", "il termometro (non va in valigia)"), ("casetta · lettone · tempaccio · panino", "panino (falso alterato)"),
          ("le braccia · le dita · le uova · le mani", "le mani (plurale in -i)")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
{sub("A", "Unità 20–27. Metti le parole nella colonna giusta.", "2 min")}
<div class="bank" style="background:#fff">gli appunti · l'aula · il cortile · la crema solare · l'evidenziatore · il lettino · l'ombrellone · il padrone di casa · il ventaglio · il ventilatore · il vicino · la zanzara</div>
<table style="table-layout:fixed;margin:0"><tr>{cth}</tr><tr>{ctd}</tr></table>
{sub("B", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 4)}
<div class="two"><div>{sub("C", "Che cos'è?", "1 min")}<ol>{dfl}</ol></div>
<div>{sub("D", "Qual è la parola diversa?", "2 min")}<ol>{odl}</ol></div></div>""",
    20, """<p>B: parole dalle unità 25, 26 e 27. C: unità 26, 26, 27, 24. D: chiedere sempre perché.</p>""")

    # Page 6: dictation + social Italian
    dal = "".join(f'<li>{R(x.split(". ", 1)[1])}</li>' if T else '<li><div class="wline"></div></li>' for x in DETT)
    d1 = [("Signora Rossi", "Júlia, lo sai che la nuova vicina arriva il primo ottobre?", ""), ("Júlia", "Davvero? Come lo sa?", ""),
          ("Signora Rossi", "Mi lo ha detto il padrone di casa. Dice che sono una ragazza molto simpatica.", "Me l'ha detto · è una ragazza"),
          ("Júlia", "Che bello notizia! Se avrà bisogno di qualcosa, la aiuterò io.", "Che bella notizia")]
    d2 = [("Marco", "Júlia, dove sei? Il film comincia tra dieci minuti!", ""), ("Júlia", "Sono in bici, arrivo. Ho finito lavorare tardi.", "finito di lavorare"),
          ("Marco", "Prima di vieni, compri due bottiglietti d'acqua?", "Prima di venire · bottigliette"), ("Júlia", "Va bene. E Giulia? Viene anche lei?", ""),
          ("Marco", "Non lo so, non risponde. Sarà ancora al bar.", "")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "8 min")}
{audiocard(["R3.2", "R3.3"])}
{sub("A", "Unità 20–27. Dettato. Ascolta e scrivi le frasi.", "3 min", "R3.2")}
<ol style="line-height:1.3">{dal}</ol>
{sub("B", "Unità 20, 21, 23, 25, 26 e 27. Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R3.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: sulle scale</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: al telefono</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: un'altra notizia, un altro appuntamento.", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Ogni frase ripassa un'unità, dalla 20 alla 27. Controllare le preposizioni (<i>decidere di</i>), le doppie (<i>casetta, terrazzino</i>) e i pronomi (<i>te la</i>).</li>
<li>B: dialogo 1: <i>Me l'ha detto</i> (25), <i>dice che è</i> (27), <i>Che bella notizia</i> (23). Dialogo 2: <i>finito di</i> (20), <i>prima di venire</i> (21), <i>bottigliette</i> (26). L'audio ha le versioni corrette. Novità: la nuova vicina arriva il primo ottobre.</li></ol>""")

    # Page 7: reflect
    cd = [("20", "So parlare di studio con cominciare a, finire di, smettere di."), ("21", "So organizzare una partenza con prima di + infinito."),
          ("22", "So fare ipotesi con il futuro (sarà, avrà) e con se."), ("23", "So esprimere entusiasmo (che bello!, quanta gente!)."),
          ("24", "So parlare del quartiere con qualche, ogni, nessuno."), ("25", "So chiedere e prestare con me lo, te la."),
          ("26", "So usare casetta, lettone, le braccia, le uova."), ("27", "So riportare notizie con dice che e usare per me, con te.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>La mia estate.</b> Scrivi una mail a un amico italiano (50–75 parole) e raccontagli:</p>
<ol><li>che cosa hai fatto prima di partire o prima di una cosa importante (<i>prima di…</i>);</li><li>una cosa bella dell'estate (<i>Che bello…! Quanta gente…!</i>);</li><li>una cosa che hai prestato o chiesto in prestito (<i>te l'ho prestato…</i>);</li><li>una notizia che ti hanno dato (<i>Mi ha detto che…</i>). Usa almeno un nome alterato.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività prima dell'unità 29. Il compito usa la grammatica delle unità 20–27. Prossima lezione: <b>Unità 29 · Il giardino è pronto</b> (il congiuntivo presente dopo penso che, credo che, spero che).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R3.1", "Festa per Bruno (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R3.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R3.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S33)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 28 - Ripasso 3")
