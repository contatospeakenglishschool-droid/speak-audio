# Speak! Essenziale A1 - Ripasso 3 (Unità 19-26), tutto in italiano - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · RIPASSO 3", audio_json=os.path.join(HERE, "audio_it-a1-ripasso-3.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'aperitivo", "Unità 19"), ("B", "gli occhiali", "Unità 20"), ("C", "il traghetto", "Unità 21"), ("D", "il conto", "Unità 22"),
          ("E", "mescolare", "Unità 23"), ("F", "il nuoto", "Unità 24"), ("G", "il compleanno", "Unità 25"), ("H", "il brindisi", "Unità 26")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-ripasso-3"]
NAMES = {"Narrator": "Narratore"}
def lines(k):
    return [(NAMES.get(n, n), t.replace("...", "…")) for n, t in (x.split(": ", 1) for x in _r[k].split("\n"))]
SCRIPT, S33 = lines("R3.1 Conversazione"), lines("R3.3 Dialoghi")
DETT = [x.split(": ", 1)[1] for x in _r["R3.2 Dettato"].split("\n")][1:]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec

    # Page 1: cover + photo memory
    cover = cover_html(T, "LIVELLO A1 · RIPASSO 3", "Ripasso 3", "Unità 19–26 · inviti · persone · vacanze · ristorante · istruzioni · sport · feste · un anno",
                       [("SAI FARE", "controllare che cosa hai imparato nelle unità 19–26"),
                        ("LINGUA", "volere, potere, dovere · è / ha / porta · ci sono stato · vorrei · gira, non girare · giocare a / fare · buon / buona · fa, da, tra"),
                        ("PRONUNCIA", "dettato di frasi · a casa e all'aperitivo")])
    b.page(f"""{sec(1, "Riscaldamento: memoria fotografica", "5 min")}
{sub("A", "Una foto per ogni unità. Scrivi la parola. Poi di' una frase con la parola.", "5 min")}
<div class="bank">l'aperitivo · il brindisi · il compleanno · il conto · gli occhiali · il nuoto · il traghetto · mescolare</div>
{photo_grid(T, PHOTOS)}
<p class="small" style="margin-top:2mm"><b>Esempio:</b> il traghetto → <i>A Pasqua Júlia ha preso il traghetto per Capri.</i></p>""",
    22, """<p>Le foto A–H vengono dalle unità 19–26, in ordine. Accettare qualsiasi frase corretta: <i>Ti va di fare un aperitivo? L'ingegnere Ferri porta gli occhiali. Il conto, per favore. Mescola lo zucchero e le uova. Faccio nuoto due volte alla settimana. Tanti auguri! Cin cin!</i> Correggere <i>ha andato</i>, <i>gioco a nuoto</i>, <i>buono compleanno</i>.</p>""", cover=cover)

    b.extra("Panoramica del ripasso · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Unità</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento: memoria fotografica</td><td>5 min</td><td>19–26</td><td>1</td></tr>
<tr><td>2 Ascolto: Júlia e Marco prima delle vacanze</td><td>10 min</td><td>19–26</td><td>2</td></tr>
<tr><td>3 Grammatica: modali, descrizioni, passato prossimo, al ristorante</td><td>10 min</td><td>19–22</td><td>3</td></tr>
<tr><td>4 Grammatica: imperativo, sport, auguri, fa / da / tra</td><td>10 min</td><td>23–26</td><td>4</td></tr>
<tr><td>5 Lessico</td><td>7 min</td><td>19–26</td><td>5</td></tr>
<tr><td>6 Dettato e italiano sociale</td><td>8 min</td><td>19–26</td><td>6</td></tr>
<tr><td>7 Riflessione e compiti</td><td>5 min</td><td>19–26</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. È un ripasso: non spiegare tutto di nuovo. Lo studente lavora da solo; tu correggi gli errori che tornano.</div>
<div class="box sand"><h4>LA STORIA FINORA</h4>Fine luglio, l'ultimo giorno prima delle vacanze. Marco invita Júlia a un aperitivo (unità 19); Júlia descrive Chiara, la ragazza di Bruno (20); Marco racconta le Dolomiti, dove è già stato (21); Júlia promette una cena al Portico per il compleanno di Marco (22). Prima di partire per il Brasile lascia le chiavi a Davide con le istruzioni per le piante (23). In Brasile farà nuoto (24); a tutti: <i>buone vacanze!</i> (25). È la fine del primo anno di Júlia in Italia (26).</div>
<div class="box"><h4>I 5 ERRORI DA CONTROLLARE</h4>1. <i>Posso di venire?</i> → <b>Posso venire?</b> 2. <i>Bruno tiene la barba</i> → <b>Bruno ha la barba</b> 3. <i>Non gira!</i> → <b>Non girare!</b> 4. <i>Gioco calcio</i> → <b>Gioco a calcio</b> 5. <i>Sono arrivata fa un anno</i> → <b>un anno fa</b>.</div>
<div class="box"><h4>AUDIO</h4>Traccia R3.1 Conversazione (lenta e naturale) · Traccia R3.2 Dettato di frasi · Traccia R3.3 Due dialoghi</div>""")

    # Page 2: listening
    topics = [("un invito", True), ("la descrizione di una persona", True), ("le vacanze in Brasile", True), ("lo sport", True), ("un viaggio passato", True),
              ("una ricetta", False), ("un ristorante", True), ("un compleanno", True), ("gli auguri", True)]
    tl = " &nbsp; ".join(f"{'☒' if (T and ok) else '☐'} {t}" for t, ok in topics)
    tf = [("Júlia parte per il Brasile domenica.", "F: parte sabato mattina."), ("L'aperitivo è alle sette in piazza Santo Stefano.", "V"),
          ("Marco conosce Chiara.", "F: non la conosce."), ("Chiara è alta e bionda.", "F: è bassa e ha i capelli lunghi e rossi."),
          ("In Brasile Júlia va anche al mare.", "V"), ("Marco sa sciare.", "F: non sa sciare."), ("Marco è già stato nelle Dolomiti.", "V"),
          ("Per il compleanno di Marco, Júlia prenota un tavolo al Portico.", "V")]
    tfl = "".join(f"<li>{s} <b>V / F</b> {R(a)}</li>" for s, a in tf)
    b.page(f"""{sec(2, "Ascolto: prima delle vacanze", "10 min")}
<p>È la fine di luglio. Domani lo studio chiude per le vacanze. Júlia e Marco parlano prima di andare a casa.</p>
{audiocard(["R3.1 · SLOW", "R3.1 · NATURAL"])}
{sub("A", "Ascolta. Di che cosa parlano? Segna (✓) otto argomenti. Un argomento è in più.", "3 min", "R3.1 · SLOW")}
<div class="bank" style="background:#fff;line-height:1.7">{tl}</div>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min", "R3.1 · NATURAL")}
<ol>{tfl}</ol>
{sub("C", "Trova nella conversazione un esempio di…", "2 min")}
<table style="table-layout:fixed"><tr><td>un invito</td><td>{R("Ti va di fare un aperitivo stasera?")}</td></tr><tr><td>una descrizione</td><td>{R("È bassa e ha i capelli lunghi e rossi.")}</td></tr>
<tr><td>sapere + infinito</td><td>{R("Non so sciare.")}</td></tr><tr><td>ci sono stato / già</td><td>{R("Ci sei già stato? · Sì, ci sono stato due anni fa.")}</td></tr></table>""",
    18, """<p>A: argomento in più = <span class="red">una ricetta</span>. B: lo studente corregge a voce le frasi false. C: se serve, lo studente può leggere la trascrizione nell'ultima pagina della guida.</p>""")

    # Page 3: grammar 19-22
    md = [("io", "voglio", "posso", "devo"), ("tu", "vuoi", "puoi", "devi"), ("noi", "vogliamo", "possiamo", "dobbiamo")]
    mdr = "".join(f"<tr><td>{p}</td><td>{A(a, 'min-width:16mm')}</td><td>{A(c, 'min-width:16mm')}</td><td>{A(d, 'min-width:16mm')}</td></tr>" for p, a, c, d in md)
    ds = [("Chiara", "è", "bassa."), ("Chiara", "ha", "i capelli rossi."), ("Bruno", "ha", "la barba."), ("L'ingegnere Ferri", "porta", "gli occhiali.")]
    dsl = "".join(f"<li>{a} {A(x, 'min-width:12mm')} {c}</li>" for a, x, c in ds)
    pp = [("A Pasqua Júlia e Giulia", "sono andate", "a Napoli.", "andare"), ("Sabato", "ha piovuto", ": niente Vesuvio.", "piovere"),
          ("Marco", "è rimasto", "a Bologna.", "rimanere"), ("Noi", "abbiamo preso", "il traghetto.", "prendere")]
    ppl = [f'<li value="{i+1}">{a} {A(v, "min-width:28mm")}{"" if c.startswith(":") else " "}{c} <span class="small">({n})</span></li>' for i, (a, v, c, n) in enumerate(pp)]
    rs = [("Cameriere: Che cosa", "prendete", "?"), ("Giulia:", "Per me", "le tagliatelle, per favore."), ("Marco: Io", "vorrei", "il pollo arrosto."),
          ("Júlia: Il tiramisù?", "Lo", "prendo anch'io!")]
    rsl = "".join(f"<li>{a} {A(x, 'min-width:16mm')} {c}</li>" for a, x, c in rs)
    b.page(f"""{sec(3, "Grammatica: unità 19–22", "10 min")}
<div class="two"><div>{sub("A", "Unità 19. Volere, potere, dovere.", "2 min")}
<table style="margin:0"><tr><th></th><th>volere</th><th>potere</th><th>dovere</th></tr>{mdr}</table></div>
<div>{sub("B", "Unità 20. È, ha o porta?", "2 min")}<ol>{dsl}</ol></div></div>
{sub("C", "Unità 21. Il passato prossimo: avere o essere?", "3 min")}
{twocol(ppl, 2)}
{sub("D", "Unità 22. Al ristorante. Completa con: lo, per me, prendete, vorrei.", "3 min")}
<ol>{rsl}</ol>""",
    24, """<ol><li>A: dopo i modali l'infinito <b>senza preposizione</b>: <i>posso venire</i>, non <i>posso di venire</i>. B: <i>essere</i> + aggettivo, <i>avere</i> + capelli / occhi / barba, <i>portare</i> + occhiali (non <i>tenere</i>).</li>
<li>C: <i>piovere</i> va bene con <i>avere</i> (anche <i>è piovuto</i>). D: <i>vorrei</i> è più gentile di <i>voglio</i>; il pronome <i>lo</i> va prima del verbo.</li></ol>""")

    # Page 4: grammar 23-26
    im = [("girare", "gira", "girate", "non girare"), ("prendere", "prendi", "prendete", "non prendere"), ("aprire", "apri", "aprite", "non aprire"), ("fare", "fai", "fate", "non fare")]
    imr = "".join(f"<tr><td><b>{v}</b></td><td>{A(a, 'min-width:16mm')}</td><td>{A(c, 'min-width:16mm')}</td><td>{A(d, 'min-width:22mm')}</td></tr>" for v, a, c, d in im)
    sp = [("Davide", "gioca a", "basket il giovedì."), ("La signora Rossi", "fa", "yoga."), ("Davide non", "sa", "nuotare."), ("Giulia non fa", "mai", "sport.")]
    spl = "".join(f"<li>{a} {A(x, 'min-width:14mm')} {c}</li>" for a, x, c in sp)
    fd = [("", "Buone", "vacanze!"), ("", "Buon", "compleanno!"), ("Júlia abita a Bologna", "da", "un anno."), ("È arrivata un anno", "fa", "."),
          ("Bruno torna", "tra", "tre mesi."), ("Ho", "già", "visto Firenze.")]
    fdl = [f'<li value="{i+1}">{a} {A(x, "min-width:13mm")}{"" if c == "." else " "}{c}</li>' for i, (a, x, c) in enumerate(fd)]
    mk = [("Posso di venire alla festa?", "Posso venire alla festa?"), ("Bruno tiene la barba.", "Bruno ha la barba."), ("Davide, non gira a sinistra!", "Davide, non girare a sinistra!"),
          ("Gioco calcio con i colleghi.", "Gioco a calcio con i colleghi."), ("Sono arrivata fa un anno.", "Sono arrivata un anno fa.")]
    mkl = "".join(f"<li>{a} {R('→ ' + c)}</li>" for a, c in mk)
    b.page(f"""{sec(4, "Grammatica: unità 23–26", "10 min")}
{sub("A", "Unità 23. L'imperativo.", "3 min")}
<table style="margin:0"><tr><th></th><th>tu</th><th>voi</th><th>tu, negativo</th></tr>{imr}</table>
<div class="two"><div>{sub("B", "Unità 24. Lo sport.", "2 min")}<ol>{spl}</ol></div>
<div>{sub("C", "Unità 25–26. Completa.", "2 min")}<ol>{"".join(fdl)}</ol></div></div>
{sub("D", "Unità 19–26. Correggi gli errori.", "3 min")}
<ol>{mkl}</ol>""",
    22, """<ol><li>A: il negativo con <i>tu</i> = <b>non + infinito</b>; con <i>voi</i> = <i>non girate</i>. B: <i>giocare a</i> con la palla, <i>fare</i> con gli altri sport; <i>sapere</i> per un'abilità.</li>
<li>D: chiedere allo studente <i>perché?</i> per ogni correzione. Sono gli errori più frequenti delle unità 19–26.</li></ol>""")

    # Page 5: vocabulary
    ct = [("alto", "basso"), ("lunghi", "corti"), ("giovane", "anziano"), ("ricci", "lisci")]
    ctl = "".join(f"<li>{a} ≠ {A(x, 'min-width:18mm')}</li>" for a, x in ct)
    mn = [("la bruschetta", "antipasto"), ("le tagliatelle al ragù", "primo"), ("il pollo arrosto", "secondo"), ("le patate al forno", "contorno"), ("il tiramisù", "dolce")]
    mnl = "".join(f"<li>{a} → {A(x, 'min-width:18mm')}</li>" for a, x in mn)
    df = [("Lo sport con la racchetta.", "il tennis"), ("Si gioca in cinque, la sera, con i colleghi.", "il calcetto"), ("Si fa in piscina.", "il nuoto"),
          ("La festa del 25 dicembre.", "Natale"), ("Il 15 agosto.", "Ferragosto"), ("Lo dici quando bevi con gli amici.", "Cin cin!")]
    dfl = [f'<li value="{i+1}">{a} {A(x, "min-width:24mm")}</li>' for i, (a, x) in enumerate(df)]
    od = [("il calcio · il tennis · la pallavolo · lo yoga", "lo yoga (fare, non giocare a)"), ("Natale · Pasqua · Capodanno · il contorno", "il contorno"),
          ("gira · attraversa · prendi · la valigia", "la valigia")]
    odl = "".join(f"<li>{a} {R('→ ' + x)}</li>" for a, x in od)
    b.page(f"""{sec(5, "Lessico", "7 min")}
<div class="two"><div>{sub("A", "Unità 20. I contrari.", "1 min")}
<div class="bank" style="background:#fff">anziano · basso · corti · lisci</div><ol>{ctl}</ol></div>
<div>{sub("B", "Unità 22. Il menù: antipasto, primo, secondo, contorno o dolce?", "2 min")}<ol>{mnl}</ol></div></div>
{sub("C", "Unità 24–26. Che cos'è?", "2 min")}
{twocol(dfl, 3)}
{sub("D", "Unità 22–25. Qual è la parola diversa?", "2 min")}
<ol>{odl}</ol>""",
    20, """<p>A: <i>anziano</i> è più gentile di <i>vecchio</i> per le persone. B: in Italia il contorno si ordina a parte, con il secondo. D: chiedere perché: <i>lo yoga si fa, non si gioca!</i></p>""")

    # Page 6: dictation + social Italian
    dal = "".join(f'<li>{R(x.split(". ", 1)[1]) if T else ""}<div class="wline"></div></li>' if not T else f'<li>{R(x.split(". ", 1)[1])}</li>' for x in DETT)
    d1 = [("Júlia", "Davide, ecco le chiavi di casa mia.", ""), ("Davide", "Grazie! Che cosa devo di fare?", "devo fare"),
          ("Júlia", "Innaffia le piante il lunedì e il giovedì. E mette la posta sul tavolo.", "metti"), ("Davide", "Va bene. E le finestre?", ""),
          ("Júlia", "Non apri le finestre se piove!", "Non aprire"), ("Davide", "Tranquilla. Buon viaggio, Júlia!", "")]
    d2 = [("Cameriere", "Buonasera! Che cosa prendete?", ""), ("Giulia", "Per me un spritz, per favore.", "uno spritz"), ("Davide", "Io voglio una birra media.", "vorrei"),
          ("Cameriere", "Volete anche qualcosa di mangiare?", "da mangiare"), ("Marco", "Sì, un tagliere di salumi e formaggi per tutti.", ""),
          ("Júlia", "E alla fine il conto, per favore. Offro io!", "")]
    def dl(rows): return "".join(f"<div><b>{n}:</b> {t} {R('→ ' + c) if c else ''}</div>" for n, t, c in rows)
    b.page(f"""{sec(6, "Dettato e italiano sociale", "8 min")}
{audiocard(["R3.2", "R3.3"])}
{sub("A", "Unità 19–26. Dettato. Ascolta e scrivi le frasi.", "3 min", "R3.2")}
<ol style="line-height:1.35">{dal}</ol>
{sub("B", "Unità 19, 22 e 23. Ogni dialogo ha tre errori. Correggi. Poi ascolta e controlla.", "3 min", "R3.3")}
<div class="two"><div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 1: sulle scale</b>{dl(d1)}</div>
<div class="msg" style="max-width:none;padding:2mm 3mm;line-height:1.55"><b style="color:{TEAL}">Dialogo 2: all'aperitivo</b>{dl(d2)}</div></div>
{sub("C", "Fai i dialoghi con l'insegnante. Poi cambia i dettagli: che cosa deve fare il tuo vicino? Che cosa ordini?", "2 min")}""",
    28, """<ol><li>A: c'è una pausa dopo ogni frase. Ogni frase ripassa un'unità, dalla 19 alla 26. Controllare le doppie (<i>occhiali, scorso</i>) e gli accenti.</li>
<li>B: dialogo 1: <i>devo fare</i> (modale senza <i>di</i>), <i>metti</i> e <i>non aprire</i> (imperativo). Dialogo 2: <i>uno spritz</i> (S + consonante), <i>vorrei</i>, <i>da mangiare</i> (port. <i>de comer</i>). L'audio ha le versioni corrette.</li></ol>""")

    # Page 7: reflect
    cd = [("19", "So invitare, accettare e rifiutare un invito."), ("20", "So descrivere una persona."), ("21", "So raccontare una vacanza con il passato prossimo."),
          ("22", "So ordinare al ristorante e chiedere il conto."), ("23", "So dare istruzioni con l'imperativo."), ("24", "So parlare degli sport che faccio e che so fare."),
          ("25", "So fare gli auguri e invitare a una festa."), ("26", "So raccontare un anno: passato, presente e progetti.")]
    cdr = "".join(f"<tr><td><b>Unità {u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in cd)
    b.page(f"""{sec(7, "Riflessione e compiti", "5 min")}
{sub("A", "Come va? Segna una casella per ogni riga.", "2 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei obiettivi per le prossime unità. Che cosa vuoi ripassare ancora? Scrivi due cose.", "2 min")}
<div class="wline"></div><div class="wline"></div>
{sub("C", "Compiti", "1 min")}
<p><b>Una cartolina dalle vacanze.</b> Scrivi a un amico italiano (60–80 parole):</p>
<ol><li>dove sei e con chi (descrivi una persona);</li><li>che cosa hai fatto ieri (passato prossimo);</li><li>che sport fai qui e quante volte;</li><li>un invito per quando torni (ti va di…?) e gli auguri.</li></ol>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Guardare le righe «Non ancora» e preparare due brevi attività di ripasso prima dell'unità 28. Il compito usa la grammatica delle unità 19–26: correggerlo e conservarlo come esempio di scrittura. Prossima lezione: <b>Unità 28 · Il ritorno</b> (settembre: Bruno arriva a Bologna).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("R3.1", "Júlia e Marco prima delle vacanze (lenta e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("R3.2", "Dettato (con una pausa dopo ogni frase)")}
<p>{" ".join(DETT)}</p>
{sub("R3.3", "Due dialoghi (versioni corrette)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in S33)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 27 - Ripasso 3")
