# Speak! Progresso B1 - Unità 11 "Comunicare a distanza" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 11", audio_json=os.path.join(HERE, "audio_it-b1-unita-11.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-11"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["11.1 Comunicare a distanza"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S112 = [x.split(": ", 1)[1] for x in _r["11.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 11", "Comunicare a distanza", "Videochiamate e vocali · <b>il congiuntivo imperfetto</b>",
                       [("SAI FARE", "gestire una videochiamata, dare notizie a distanza, fare paragoni irreali"),
                        ("LINGUA", "Parlava come se fossimo sulla luna. · Mi sento come se avessi quindici anni."),
                        ("PRONUNCIA", "la doppia s: «fossi», «avessi», «sentissimo»")])
    kw = [("una telefonata in cui ci si vede", "una videochiamata"), ("il collegamento a internet", "la connessione"),
          ("un messaggio registrato con la voce", "un vocale"), ("l'occhio del computer o del telefono", "la telecamera"),
          ("la parte alta di una stanza", "il soffitto"), ("ripetere la stessa cosa perché si è sicuri", "insistere"),
          ("dal vivo, non attraverso uno schermo", "di persona"), ("parlare a voce molto alta", "urlare")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: vicini e lontani", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Con chi fai videochiamate? Quanto spesso?</li><li>Preferisci i messaggi scritti o i vocali? Perché?</li><li>Che cosa ti dà fastidio nelle chiamate con la famiglia?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">la connessione · di persona · insistere · il soffitto · la telecamera · urlare · una videochiamata · un vocale</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Hai mai avuto una videochiamata disastrosa? Che cosa è successo?", "1 min")}""",
    25, """<ol><li>A: lasciare parlare lo studente; se dice <i>come se è</i> o <i>come se fosse</i> spontaneamente, annotarlo: oggi si vede il congiuntivo imperfetto.</li>
<li>B: <i>un vocale</i> = <i>um áudio</i> (WhatsApp); <i>la telecamera</i> = <i>a câmera</i> (la <i>camera</i> in italiano è la stanza!).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione su videochiamate e vocali · parole chiave</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Comunicare a distanza: la videochiamata con Belo Horizonte</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Il congiuntivo imperfetto · come se</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Il congiuntivo imperfetto (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Telefono e computer · falsi amici · la doppia s</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Bruno a Chiara · completare con come se</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La mia famiglia a distanza · gioco di ruolo: una videochiamata disastrosa</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizia il secondo blocco (marzo–maggio). Domenica 7 marzo, sera, a casa di Júlia. Júlia e Bruno hanno appena finito la videochiamata con i genitori a Belo Horizonte: la connessione andava e veniva, la mamma parlava «come se fossimo sulla luna» e urlava; il papà ha cercato la telecamera per dieci minuti e ha chiesto se a Bologna nevicasse ancora. Camila racconta i cinquanta vocali al giorno di sua madre. La grande notizia: ad aprile i genitori vengono a Bologna per due settimane; la mamma vuole vedere tutta l'Italia e dormire da Júlia. Camila: «Darei qualunque cosa perché mia madre venisse qui». Novità di marzo: Tommaso vive con Bruno, Elena lavora al bar, Camila ha cominciato il tirocinio.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La regola è uguale al portoghese (<i>como se fosse, como se tivesse</i>), quindi lo studente capisce subito; il problema è la forma: <i>avesse</i> (non <i>tivesse</i>), la doppia <i>s</i>, <i>stessi / dessi</i> (non <i>stassi</i>). Falsi amici del telefono: <i>atender</i> → <i>rispondere</i> (<i>attendere</i> = aspettare); <i>ligar</i> → <i>chiamare, telefonare</i>; <i>mandar um áudio</i> → <i>mandare un vocale</i>; <i>câmera</i> → <i>telecamera</i> (<i>camera</i> = stanza).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia WhatsApp è l'app più usata e i vocali sono amatissimi… e odiatissimi: molti italiani chiedono «scrivimi, non mandarmi vocali!». Tra Italia e Brasile ci sono 4 ore di differenza in inverno e 5 ore dall'ultima domenica di marzo, quando in Italia comincia l'ora legale (il Brasile non la usa più). Per chiamare l'Italia dal Brasile: +39.</div>
<div class="box"><h4>AUDIO</h4>Traccia 11.1 Comunicare a distanza (prima naturale, poi lenta) · Traccia 11.2 Ripeti: come se + congiuntivo imperfetto</div>""")

    # Pagina 2 - Ascolto
    gi = [("la connessione", True), ("un nuovo lavoro", False), ("i messaggi vocali", True), ("il tempo a Bologna", True), ("una festa", False), ("la visita dei genitori", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Durante la chiamata la connessione era perfetta.", "F"), ("La madre di Camila manda molti messaggi vocali.", "V"),
          ("Il padre non trovava la telecamera.", "V"), ("A Bologna nevica ancora.", "F"),
          ("I genitori arrivano ad aprile per due settimane.", "V"), ("La madre vuole dormire in albergo.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Comunicare a distanza", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["11.1 · NATURAL", "11.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Domenica sera, a casa di Júlia, dopo una videochiamata. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "11.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché Júlia si sente «come se avesse ancora quindici anni»? {R("La madre la tratta come una ragazzina, le dà ordini e consigli.") if T else ""}</li>
<li>Camila dice: «Darei qualunque cosa perché mia madre venisse qui». Che cosa capiamo di lei? {R("Le manca la sua famiglia; è lontana da Recife.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>La connessione andava e veniva. · Come sempre. · Che bello! · di persona · Dai, sarà bellissimo. · È che… · Anzi… · un vocale</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: connessione, messaggi vocali, tempo a Bologna, visita dei genitori.</li>
<li>B: 1 andava e veniva · 4 il padre lo chiedeva, ma non nevica più · 6 vuole dormire da Júlia.</li>
<li>Espressioni: <i>andava e veniva</i> = <i>caía toda hora</i>; <i>È che…</i> = <i>É que…</i> (uguale!).</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("come se <u>fossimo</u> sulla luna", "essere"), ("come se non la <u>sentissimo</u>", "sentire"), ("come se <u>avessi</u> tempo", "avere"),
          ("mi ha chiesto se a Bologna <u>nevicasse</u>", "nevicare"), ("perché mia madre <u>venisse</u> qui", "venire")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:24mm')}</li>" for s, a in ex)
    rules = [("Dopo <i>come se</i> si usa", ["il congiuntivo", "l'indicativo"], "il congiuntivo", "."),
             ("Il congiuntivo imperfetto di <i>essere</i> con <i>io</i> è", ["fossi", "sia"], "fossi", "."),
             ("Le desinenze <i>-assi, -essi, -issi</i> hanno", ["la doppia s", "una s sola"], "la doppia s", "."),
             ("<i>Stare</i> con <i>io</i> fa", ["stessi", "stassi"], "stessi", ".")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" .", ".") for a, o, r, z in rules)
    cc = [("Bruno mangia come se non", ["mangiasse", "mangia"], "mangiasse", "da una settimana."),
          ("Camila parla italiano come se", ["fosse", "è"], "fosse", "italiana."),
          ("Mi guardi come se", ["avessi", "ho"], "avessi", "detto una cosa strana.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: il congiuntivo imperfetto", "8 min")}
{sub("A", "Frasi dal dialogo. Scrivi l'infinito del verbo sottolineato.", "3 min")}
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>Congiuntivo imperfetto</b>: <i>-are</i> → <b>-assi</b>, <i>-ere</i> → <b>-essi</b>, <i>-ire</i> → <b>-issi</b> (<i>parlassi, avessi, sentissi</i>). <i>Essere</i> → <b>fossi</b>; <i>fare, dire, bere</i> → <i>facessi, dicessi, bevessi</i>; <i>dare, stare</i> → <i>dessi, stessi</i>. <b>Come se</b> + congiuntivo imperfetto = un paragone con una situazione irreale: <i>parla come se fossimo sulla luna</i>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: far notare che la radice è quella dell'imperfetto indicativo: <i>sentivo → sentissi, facevo → facessi, bevevo → bevessi</i>.</li>
<li>C: in tutte le frasi la situazione non è vera: Bruno ha mangiato, Camila non è italiana. Il portoghese funziona uguale: <i>como se fosse</i>.</li></ol>""")

    grammar_ref_it.congiuntivo_imperfetto(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["fare", "mandare", "disattivare", "condividere", "lasciare", "ricaricare"]
    rgt = ["lo schermo", "il telefono", "una videochiamata", "un messaggio in segreteria", "il microfono", "un vocale"]
    ans = {"fare": "una videochiamata", "mandare": "un vocale", "disattivare": "il microfono", "condividere": "lo schermo",
           "lasciare": "un messaggio in segreteria", "ricaricare": "il telefono"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: telefono e computer", "4 min")}
{sub("A", "Unisci i verbi alle parole giuste.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Mandi spesso vocali? Lunghi o corti?</li><li>Quando disattivi il microfono?</li><li>Lasci messaggi in segreteria?</li><li>Quante volte al giorno ricarichi il telefono?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Non ho atteso il telefono.</td><td><b>Non ho risposto al telefono.</b></td><td><i>attendere</i> = aspettare.</td></tr>
<tr><td>Mia madre mi ha ligato.</td><td><b>Mia madre mi ha chiamato.</b></td><td><i>ligar</i> → <i>chiamare, telefonare</i>.</td></tr>
<tr><td>Ti mando un audio.</td><td><b>Ti mando un vocale.</b></td><td>su WhatsApp si dice <i>vocale</i>.</td></tr>
<tr><td>Parla come se è stanca.</td><td><b>Parla come se fosse stanca.</b></td><td><i>come se</i> + congiuntivo.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: la doppia s", "4 min")}
<p class="small" style="margin:.3mm 0">Il congiuntivo imperfetto ha sempre la <b>doppia s</b>: <i>fo<b>ss</b>i, ave<b>ss</b>i, senti<b>ss</b>imo</i>. La <i>ss</i> è sorda e lunga. La <i>s</i> semplice tra due vocali, nel Nord Italia, è sonora: <i>ca<b>s</b>a, co<b>s</b>a</i> [z]. Non dire <i>fo[z]e</i>!</p>
{audiocard(["11.2"])}
{sub("A", "Ascolta e ripeti. Poi leggi ad alta voce: casa · cassa · rosa · rossa · fosse · avesse · stessimo.", "4 min", "11.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S112))}</p>""",
    29, """<ol><li>A: fare c · mandare f · disattivare e · condividere a · lasciare d · ricaricare b. <i>Segreteria</i> = <i>caixa postal</i>.</li>
<li>Pronuncia: coppie minime <i>casa / cassa, rosa / rossa</i>: la doppia è più lunga e sempre sorda.</li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["fossi", "sono"], "fossi"), (["abitassimo", "abitiamo"], "abitassimo"), (["facesse", "fa"], "facesse"),
          (["avessimo", "abbiamo"], "avessimo"), (["fosse", "è"], "fosse"), (["fossi", "sei"], "fossi"),
          (["dovesse", "deve"], "dovesse"), (["regge", "reggesse"], "regge")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Mio fratello mangia come se… (non mangiare da giorni)", "non mangiasse da giorni"), ("Mi parli come se… (io, essere un bambino)", "fossi un bambino"),
          ("Spende soldi come se… (essere ricco)", "fosse ricco"), ("Corrono come se… (avere paura)", "avessero paura"),
          ("Ci saluta come se… (non conoscerci)", "non ci conoscesse"), ("Parla di Roma come se… (abitarci)", "ci abitasse")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:36mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Domenica notte Bruno scrive a Chiara. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Bruno:</b> Ciao amore! Videochiamata con i miei appena finita. La mamma mi guardava come se {p[0]} dimagrito dieci chili: «Bruno, mangi?». Papà parlava a voce altissima, come se {p[1]} su un altro pianeta. Poi mi ha chiesto se a Bologna {p[2]} ancora freddo. Ad aprile vengono a trovarci! La mamma vuole vedere tutto, come se {p[3]} un mese di vacanza. Júlia fa come se {p[4]} contenta, ma secondo me è un po' preoccupata. Tu vuoi conoscerli? Ti avverto: ti tratteranno come se {p[5]} già della famiglia, e papà ti farà mille domande, come se {p[6]} scrivere un libro su di te. Ti chiamo domani, se la connessione {p[7]}!</div>
{sub("B", "Completa con come se + congiuntivo imperfetto.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: gap 3: <i>chiedere se</i> nel passato → congiuntivo imperfetto (registro curato; nel parlato anche <i>se fa</i>). Gap 8: <i>se la connessione regge</i> è una condizione reale → indicativo: <i>se</i> da solo non vuole sempre il congiuntivo!</li>
<li>B: frase 5: il pronome va prima del verbo (<i>non ci conoscesse</i>); frase 6: <i>ci abitasse</i> (<i>ci</i> = a Roma).</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: chiamate a distanza", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>cominciare</th><th>problemi tecnici</th><th>dare una notizia</th><th>chiudere</th></tr>
<tr><td><i>Mi senti? · Mi vedi? · Ci sei? · Pronto, chi parla?</i></td><td><i>Ti sento a tratti. · Si è bloccato lo schermo. · Sei muto/a! · Ti richiamo.</i></td><td><i>Indovina chi viene? · Ho una notizia… · Sai che…? · Ti devo dire una cosa.</i></td><td><i>Ci sentiamo domani. · Salutami tutti. · Un abbraccio. · Ti mando un vocale.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi parla per due minuti di come comunichi con le persone lontane.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>con chi, come e quanto spesso</li><li>che cosa ti dà fastidio (usa <i>come se</i>)</li><li>la chiamata più divertente o più disastrosa</li><li>chiamata, messaggio o lettera: che cosa preferisci?</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. Un amico italiano ti chiama da lontano, ma la connessione è pessima. Devi dargli una notizia importante.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: Pronto? Mi senti? · Ti vedo tutto bloccato! · Non ti sento, sei muto/a! · Hai una notizia? Dimmi! · Come? Ripeti, per favore! · Ma parli come se fossi in una galleria… · Ti richiamo tra cinque minuti, va bene?") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Le videochiamate avvicinano o allontanano le persone?</li><li>I messaggi vocali sono comodi o un po' maleducati?</li><li>Una notizia importante: meglio una telefonata o un messaggio?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>come se è / come se avevo</i>.</li>
<li>B: le battute dell'insegnante sono in rosso; interrompere spesso lo studente come se la connessione saltasse: deve ripetere e riformulare.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So formare il congiuntivo imperfetto e usare come se.",
          "So gestire una chiamata con problemi tecnici e dare una notizia."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Una mail a chi è lontano.</b> Scrivi a un amico o a un parente lontano: dagli una notizia, racconta una chiamata e fagli una domanda. Prima leggi la mail di Júlia a Luca.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Ciao Luca, come stai? E Sara? Ti scrivo per darti una bella notizia: ad aprile arrivano i miei genitori dal Brasile! Ieri sera abbiamo fatto una videochiamata. La connessione andava e veniva e la mamma parlava come se fossimo sulla luna. Papà, come sempre, non trovava la telecamera: per dieci minuti ho visto solo il soffitto della cucina! Mia madre vuole vedere tutto, come se l'Italia fosse un quartiere, e naturalmente anche Firenze. Pensavo di portarli lì un sabato: mi consigli un posto tranquillo per pranzare? E se hai tempo, prendiamo un caffè tutti insieme. Mi trattano ancora come se avessi quindici anni, quindi preparati: ti faranno mille domande! Un abbraccio a te e a Sara, Júlia</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno tre <i>come se</i> + congiuntivo imperfetto &nbsp;☐ una notizia &nbsp;☐ una domanda o una richiesta &nbsp;☐ saluti informali &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far sottolineare nel modello i tre <i>come se</i>. Luca e Sara si sono sposati a Firenze (A1 35): lo studente può ricordarlo. Prossima unità: <i>Credevo che…</i> (pensavo che + congiuntivo imperfetto).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("11.1", "Comunicare a distanza (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("11.2", "Ripeti: come se + congiuntivo imperfetto")}
<p>{" · ".join(S112)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 11 - Comunicare a distanza")
