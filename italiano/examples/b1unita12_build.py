# Speak! Progresso B1 - Unità 12 "Credevo che…" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 12", audio_json=os.path.join(HERE, "audio_it-b1-unita-12.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-12"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["12.1 Credevo che..."].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S122 = [x.split(": ", 1)[1] for x in _r["12.2 Ripeti"].split("\n")]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"
    def img(l, w, h):
        return f'<div style="width:{w}mm;flex-shrink:0;border-radius:2mm;overflow:hidden;border:.8pt solid #c9dfe3"><img src="{photo(l)}" style="width:{w}mm;height:{h}mm;object-fit:cover;display:block"></div>'
    def lines(n):
        return '<div class="wline"></div>' * n


    # Pagina 1 - Riscaldamento
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 12", "Credevo che…", "Prime impressioni e stereotipi · <b>la concordanza dei tempi</b>",
                       [("SAI FARE", "raccontare le prime impressioni, parlare di stereotipi, dire che hai cambiato idea"),
                        ("LINGUA", "Pensavo che fosse timida. · Credevo che parlaste con le mani. · Credevo di essere…"),
                        ("PRONUNCIA", "l'intonazione del contrasto: «credevo che… e invece…»")])
    kw = [("l'idea che hai di una persona appena la conosci", "una prima impressione"), ("un'idea fissa su un gruppo di persone", "uno stereotipo"),
          ("per dire la verità", "sinceramente"), ("che fa fatica a parlare con persone nuove", "timido"),
          ("il contrario di simpatico", "antipatico"), ("attento solo a quello che sta facendo", "concentrato"),
          ("alzare i bicchieri per festeggiare", "brindare"), ("eccetto, a parte", "tranne")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: prima e dopo", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Guarda la foto. Dove sono queste persone? Che cosa bevono?</li><li>Che cosa pensavi dell'Italia prima di studiare italiano?</li><li>Che cosa pensano gli stranieri dei brasiliani?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">antipatico · brindare · concentrato · una prima impressione · sinceramente · uno stereotipo · timido · tranne</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "La tua prima impressione su una persona di solito è giusta o sbagliata?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; annotare se dice <i>pensavo che era</i>: oggi si vede <i>pensavo che fosse</i>.</li>
<li>B: <i>tranne</i> = <i>exceto, menos</i>; <i>brindare</i> = <i>brindar</i> (con <i>a</i>: <i>brindiamo agli amici</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione su prime impressioni e stereotipi · parole chiave</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Credevo che… Il primo aperitivo al bar di Giulia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>La concordanza dei tempi: penso che sia / pensavo che fosse</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>La concordanza dei tempi (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Il carattere · scelta delle parole · l'intonazione del contrasto</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Le prime impressioni di Camila · dal presente al passato</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Prima e dopo · gioco di ruolo: un italiano pieno di stereotipi</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Sabato 13 marzo, sera: il primo aperitivo serale del bar di Giulia; Elena, la nuova barista, porta gli spritz. Al tavolo Júlia, Marco, Camila e Davide parlano di stereotipi. Camila credeva che l'aperitivo fosse solo un bicchiere di vino e che gli italiani parlassero con le mani (vero!). Giulia pensava che in Brasile facesse caldo tutto l'anno; Júlia pensava che gli italiani mangiassero la pasta due volte al giorno (Marco quasi sì) e che fossero sempre in ritardo (Davide sì). Le prime impressioni di Marco e Júlia: lui pensava che lei fosse timida (non capiva niente!), lei pensava che lui fosse antipatico (era concentrato). Brindisi «agli stereotipi sbagliati».</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La concordanza è uguale al portoghese (<i>achava que fosse</i>), ma il brasiliano parlato preferisce l'indicativo (<i>achava que era</i>): lo studente dice <i>pensavo che era</i>. È diffuso anche nel parlato italiano: accettarlo nella conversazione veloce, correggerlo nello scritto. Altri errori: mischiare i tempi (<i>pensavo che sia</i>) e <i>credevo che io fossi</i> invece di <i>credevo di essere</i>. Lessico: <i>chato</i> → <i>noioso, pesante</i>; <i>bravo</i> (arrabbiato) ≠ <i>bravo</i> (competente).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>L'aperitivo è nato a Torino e a Milano; lo spritz viene dal Veneto. A Bologna con l'aperitivo arrivano taglieri di salumi e formaggi, e per molti studenti diventa una cena: l'<i>apericena</i>. Gli italiani mangiano circa 23 kg di pasta a testa all'anno, il consumo più alto al mondo. All'università c'è il «quarto d'ora accademico»: le lezioni cominciano un quarto d'ora dopo l'orario scritto.</div>
<div class="box"><h4>AUDIO</h4>Traccia 12.1 Credevo che… (prima naturale, poi lenta) · Traccia 12.2 Ripeti: pensavo che + congiuntivo imperfetto</div>""")

    # Pagina 2 - Ascolto
    gi = [("l'aperitivo", True), ("un viaggio a Roma", False), ("gli stereotipi sugli italiani", True), ("il clima in Brasile", True), ("il lavoro di Elena", False), ("il primo incontro di Marco e Júlia", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("È il primo aperitivo serale del bar.", "V"), ("Camila pensava che l'aperitivo fosse una cena completa.", "F"),
          ("Secondo Júlia, a Belo Horizonte fa sempre caldo.", "F"), ("Marco mangia la pasta quasi tutti i giorni.", "V"),
          ("Davide è sempre puntuale.", "F"), ("Il primo giorno Marco pensava che Júlia fosse timida.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Credevo che…", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["12.1 · NATURAL", "12.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Sabato sera, il primo aperitivo al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "12.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché Júlia parlava pochissimo il primo giorno? {R("Non capiva niente: non era timida.") if T else ""}</li>
<li>Giulia dice: «Le prime impressioni non valgono niente». Sei d'accordo? {R("Risposta libera.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Sinceramente… · E invece eccoci qui. · Che altro…? · E infatti è vero! · Tranne me. · un caso speciale · Vedete? · Brindiamo a…!</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti: aperitivo, stereotipi, clima in Brasile, primo incontro.</li>
<li>B: 2 pensava che fosse solo un bicchiere di vino · 3 d'inverno, di notte, ci sono anche dieci gradi · 5 è sempre in ritardo.</li>
<li><i>e invece</i> = <i>mas na verdade</i>.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("<u>Credevo</u> che <u>fosse</u> solo un'idea.", "credevo → fosse"), ("<u>Pensavo</u> che in Brasile <u>facesse</u> caldo.", "pensavo → facesse"),
          ("<u>Non immaginavo</u> che si <u>mangiasse</u> così tanto.", "immaginavo → mangiasse"), ("<u>Credevo</u> che <u>parlaste</u> con le mani.", "credevo → parlaste"),
          ("<u>Pensavo</u> che tu <u>fossi</u> antipatico.", "pensavo → fossi")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:38mm')}</li>" for s, a in ex)
    rules = [("Se il verbo principale è al presente, si usa il congiuntivo", ["presente", "imperfetto"], "presente", "."),
             ("Se il verbo principale è al passato, si usa il congiuntivo", ["imperfetto", "presente"], "imperfetto", "."),
             ("In <i>Credevo di essere in ritardo</i> il soggetto delle due parti è", ["lo stesso", "diverso"], "lo stesso", "."),
             ("Per un'azione precedente nel passato si usa il congiuntivo", ["trapassato", "presente"], "trapassato", ": <i>pensavo che avesse già mangiato</i>.")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("Penso che Marco sia simpatico.", "Pensavo che Marco fosse simpatico."), ("Credo che gli italiani parlino con le mani.", "Credevo che gli italiani parlassero con le mani."),
          ("Ho paura che faccia freddo.", "Avevo paura che facesse freddo.")]
    ccl = "".join(f"<li>{a} → {A(r, 'min-width:62mm')}</li>" for a, r in cc)
    b.page(f"""{sec(3, "Grammatica: la concordanza dei tempi", "8 min")}
{sub("A", "Frasi dal dialogo. Scrivi il verbo principale e il verbo al congiuntivo.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Porta le frasi al passato.", "2 min")}
<ol style="line-height:1.85;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Verbo principale al <b>presente</b> → congiuntivo <b>presente</b>: <i>penso che sia</i>. Verbo principale al <b>passato</b> (imperfetto, passato prossimo, condizionale) → congiuntivo <b>imperfetto</b>: <i>pensavo che fosse, non immaginavo che si mangiasse</i>. Stesso soggetto → <b>di + infinito</b>: <i>credevo di essere in ritardo</i>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: far notare che tutti i verbi principali sono all'imperfetto: raccontano un'idea del passato, poi corretta con <i>e invece</i>.</li>
<li>C: far dire anche la seconda parte con il presente indicativo: <i>Pensavo che facesse freddo… e invece fa caldo!</i></li></ol>""")

    grammar_ref_it.concordanza_tempi(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["timido", "antipatico", "puntuale", "chiuso", "serio", "tirchio"]
    rgt = ["generoso", "aperto", "estroverso", "spiritoso", "simpatico", "ritardatario"]
    ans = {"timido": "estroverso", "antipatico": "simpatico", "puntuale": "ritardatario", "chiuso": "aperto", "serio": "spiritoso", "tirchio": "generoso"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: il carattere", "4 min")}
{sub("A", "Trova il contrario di ogni aggettivo.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Sei più timido/a o estroverso/a?</li><li>Conosci una persona tirchia?</li><li>Sei puntuale o ritardatario/a?</li><li>Che cosa pensavano di te il primo giorno al lavoro?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Pensavo che sia timida.</td><td><b>Pensavo che fosse timida.</b></td><td>passato → congiuntivo imperfetto.</td></tr>
<tr><td>Credevo che io fossi in ritardo.</td><td><b>Credevo di essere in ritardo.</b></td><td>stesso soggetto → <i>di</i> + infinito.</td></tr>
<tr><td>Il film era molto chato.</td><td><b>Il film era molto noioso.</b></td><td><i>chato</i> → <i>noioso, pesante</i>.</td></tr>
<tr><td>Il capo è bravissimo con me (= arrabbiato).</td><td><b>Il capo ce l'ha con me.</b></td><td><i>bravo</i> = competente.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: credevo che… e invece…", "4 min")}
<p class="small" style="margin:.3mm 0">Quando raccontiamo un'idea sbagliata, la prima parte resta <b>sospesa</b> (la voce sale: <i>Pensavo che facesse caldo…</i>) e la seconda <b>scende</b> con forza su <i>e invece</i>: <i>…e in<b>VE</b>ce fa freddo!</i></p>
{audiocard(["12.2"])}
{sub("A", "Ascolta e ripeti. Poi completa ogni frase a voce con «e invece…».", "4 min", "12.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S122))}</p>""",
    29, """<ol><li>A: timido c · antipatico e · puntuale f · chiuso b · serio d · tirchio a. <i>Tirchio</i> = <i>pão-duro</i>; <i>spiritoso</i> = <i>engraçado, espirituoso</i>.</li>
<li>Pronuncia: esempi per la seconda parte: <i>…e invece è solo concentrato · …e invece a Belo Horizonte fa freddo · …e invece è vero!</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["fosse", "sia"], "fosse"), (["cenassero", "cenano"], "cenassero"), (["avesse", "ha"], "avesse"), (["fossero", "sono"], "fossero"),
          (["di non capire", "che non capissi"], "di non capire"), (["fosse", "sia"], "fosse"), (["sia", "fosse"], "sia"), (["vengano", "venissero"], "vengano")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Penso che l'italiano sia facile.", "Pensavo che l'italiano fosse facile."), ("Credo che i bolognesi mangino tanto.", "Credevo che i bolognesi mangiassero tanto."),
          ("Mi sembra che Davide abbia ragione.", "Mi sembrava che Davide avesse ragione."), ("Ho paura che piova.", "Avevo paura che piovesse."),
          ("Spero che tu venga.", "Speravo che tu venissi."), ("Credo di sapere la risposta.", "Credevo di sapere la risposta.")]
    dxl = "".join(f"<li>{s} → {A(r, 'min-width:58mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Camila scrive sul suo blog: «Cinque mesi a Bologna». Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><i>Quando sono arrivata a Bologna, a ottobre, pensavo che la città {p[0]} piccola e tranquilla. Credevo che gli italiani {p[1]} presto, e invece qui si cena alle nove! Non immaginavo che l'università {p[2]} più di novecento anni. Avevo paura che le persone {p[3]} fredde con gli stranieri, ma Giulia mi ha accolta come una figlia. All'inizio credevo {p[4]} mai il dialetto bolognese… e infatti non lo capisco ancora! Pensavo anche che Pietro {p[5]} timido: ora so che è solo distratto. Oggi penso che Bologna {p[6]} la mia seconda casa e spero che i miei genitori {p[7]} presto a trovarmi.</i></div>
{sub("B", "Porta le frasi al passato.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: gap 1–4 e 6: verbo principale al passato → congiuntivo imperfetto. Gap 5: stesso soggetto → <i>di</i> + infinito. Gap 7–8: <i>oggi penso, spero</i> → congiuntivo presente.</li>
<li>B: frase 6: <i>credevo di</i>: con lo stesso soggetto cambia solo il primo verbo.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: stereotipi e prime impressioni", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>prime impressioni</th><th>cambiare idea</th><th>parlare di stereotipi</th><th>non generalizzare</th></tr>
<tr><td><i>All'inizio pensavo che… · Mi sembrava che… · Mi ha fatto una buona impressione.</i></td><td><i>E invece… · Poi ho capito che… · Mi sbagliavo. · Ho cambiato idea.</i></td><td><i>Si dice che… · Molti pensano che… · È un luogo comune.</i></td><td><i>In generale… · Dipende dalla persona. · Non si può generalizzare.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti di un'idea che avevi e che è cambiata: un paese, una città, un lavoro o una persona.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>che cosa pensavi prima</li><li>da dove veniva quell'idea</li><li>che cosa è successo, e invece…</li><li>che cosa pensi oggi</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. Un amico italiano è appena arrivato in Brasile ed è pieno di stereotipi. Correggilo con gentilezza.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Pensavo che in Brasile si ballasse la samba tutti i giorni! · Credevo che tutti giocassero a calcio sulla spiaggia. · Pensavo che la capitale fosse Rio! · Non immaginavo che a São Paulo facesse freddo. · E il caffè? Credevo che andasse tutto all'estero…") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Gli stereotipi hanno sempre un po' di verità?</li><li>Qual è lo stereotipo sui brasiliani più sbagliato?</li><li>Al lavoro, la prima impressione conta molto?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>pensavo che era / pensavo che sia</i>.</li>
<li>B: le battute dell'insegnante sono in rosso; lo studente corregge con <i>In realtà… · Non è vero per tutti · E invece…</i> e spiega la realtà brasiliana.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare pensavo / credevo che + congiuntivo imperfetto.",
          "So parlare di stereotipi senza generalizzare."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Prima e dopo.</b> Racconta un'idea che avevi su un paese, una città o una persona e com'è cambiata. Prima leggi il testo di Davide.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Prima di conoscere Júlia, sapevo pochissimo del Brasile. Pensavo che tutti i brasiliani fossero allegri e rumorosi, che ballassero sempre e che in Brasile facesse caldo dodici mesi all'anno. Poi, più di due anni fa, Júlia è venuta ad abitare nel mio palazzo. La prima volta che l'ho vista, mi sembrava che fosse molto seria: portava sempre disegni e progetti sotto il braccio. E invece è una persona spiritosa e generosa. Non balla mai la samba, ma cucina un pão de queijo fantastico, beve caffè a tutte le ore e soffre il freddo più di me. Oggi penso che gli stereotipi siano come le prime impressioni: a volte hanno un po' di verità, ma quasi sempre si sbagliano. Davide</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno quattro <i>pensavo / credevo che</i> + congiuntivo imperfetto &nbsp;☐ un <i>e invece</i> &nbsp;☐ un presente finale (<i>oggi penso che</i> + congiuntivo presente) &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far notare nel modello il passaggio <i>pensavo che fossero</i> (allora) → <i>oggi penso che siano</i> (adesso). Prossima unità: <i>Magari!</i> (vorrei che + congiuntivo imperfetto).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("12.1", "Credevo che… (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("12.2", "Ripeti: pensavo che + congiuntivo imperfetto")}
<p>{" · ".join(S122)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 12 - Credevo che")
