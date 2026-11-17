# Speak! Progresso B1 - Unità 09 "Modi di dire" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 09", audio_json=os.path.join(HERE, "audio_it-b1-unita-09.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-09"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["09.1 Modi di dire"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S092 = [x.split(": ", 1)[1] for x in _r["09.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 09", "Modi di dire", "Carnevale, gesti e modi di dire · <b>da + infinito</b>",
                       [("SAI FARE", "capire e spiegare modi di dire, chiedere il significato, fare gli auguri, capire i gesti"),
                        ("LINGUA", "Vuoi qualcosa da bere? · Non c'è niente da fare. · Una città da vedere. · In bocca al lupo!"),
                        ("PRONUNCIA", "«da» e «dà»: preposizione e verbo")])
    kw = [("dolci fritti con lo zucchero, tipici del Carnevale bolognese", "le sfrappole"), ("un oggetto che copre il viso", "una maschera"),
          ("un piatto grande per portare i dolci", "un vassoio"), ("una frase che non vuol dire quello che dicono le parole", "un modo di dire"),
          ("un movimento delle mani che comunica", "un gesto"), ("un periodo di lavoro per imparare una professione", "un tirocinio"),
          ("una cosa fatta per ridere", "uno scherzo"), ("smettere di provare, accettare di aver perso", "arrendersi")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: il Carnevale", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Ti piace il Carnevale? Come lo passi di solito?</li><li>Conosci già qualche modo di dire italiano?</li><li>Quale modo di dire brasiliano è impossibile da tradurre?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">arrendersi · un gesto · una maschera · un modo di dire · le sfrappole · uno scherzo · un tirocinio · un vassoio</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Che gesti usi quando parli? Mostrane uno all'insegnante.", "1 min")}""",
    25, """<ol><li>A: l'anno scorso Júlia ha passato il Carnevale in Brasile (A2 07-08): chiedere allo studente il confronto tra i due Carnevali.</li>
<li>B: <i>sfrappole</i>: il nome bolognese; altrove <i>chiacchiere, frappe, crostoli, bugie</i>. <i>Tirocinio</i> = <i>estágio</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione sul Carnevale · parole chiave</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Modi di dire: martedì grasso al bar di Giulia</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>Da + infinito · da o per? · da o di?</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Da + infinito (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Modi di dire con animali e corpo · calchi dal portoghese · da / dà</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Camila da Venezia · completare con da + infinito</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Modi di dire brasiliani · il gioco dei gesti</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Martedì 9 febbraio, martedì grasso. Giulia ha fatto un vassoio di sfrappole; Camila arriva con una maschera da gatto e «una fame da lupi». Domani ha il colloquio per il tirocinio: Giulia le dice «In bocca al lupo» e Davide le insegna a rispondere «Crepi!». Júlia ha preso un granchio: ha comprato due biglietti del treno per il carnevale di Venezia per sabato prossimo, ma il carnevale finisce oggi; i biglietti sono costati un occhio della testa e non si possono cambiare. Giulia e Davide mostrano due gesti (<i>ma che dici?</i> · <i>buonissimo</i>). Júlia va a Venezia lo stesso e Camila va con lei: «due piccioni con una fava». Camila: «Basta, mi arrendo!»</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il portoghese dice <i>algo para beber, nada para fazer</i>: lo studente traduce <i>qualcosa per bere, niente a fare</i>; in italiano serve <i>da</i>. I modi di dire non si traducono parola per parola: <i>matar dois coelhos com uma cajadada</i> → <i>prendere due piccioni con una fava</i>; <i>custar os olhos da cara</i> → <i>costare un occhio della testa</i>; <i>pagar mico</i> → <i>fare una figuraccia</i>. A <i>in bocca al lupo</i> non si risponde <i>grazie</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il Carnevale finisce il martedì grasso; il giorno dopo, mercoledì delle Ceneri, comincia la Quaresima. Eccezione: a Milano il Carnevale ambrosiano finisce il sabato successivo. Vicino a Bologna è famoso il Carnevale di Cento, con i carri allegorici. A Venezia, nei bar (<i>bacari</i>), si mangiano i <i>cicchetti</i>, piccoli assaggi con un bicchiere di vino. I gesti italiani sono tantissimi: alcuni ricercatori ne hanno contati più di 250.</div>
<div class="box"><h4>AUDIO</h4>Traccia 09.1 Modi di dire (prima naturale, poi lenta) · Traccia 09.2 Ripeti: da + infinito</div>""")

    # Pagina 2 - Ascolto
    gi = [("i dolci di Carnevale", True), ("una partita di calcio", False), ("un colloquio", True), ("un viaggio a Venezia", True), ("un nuovo lavoro per Giulia", False), ("i gesti italiani", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Le sfrappole sono dolci bolognesi di Carnevale.", "V"), ("Domani Camila ha un esame all'università.", "F"),
          ("A «In bocca al lupo» si risponde «Grazie».", "F"), ("Júlia ha comprato i biglietti per il giorno sbagliato.", "V"),
          ("I biglietti del treno si possono cambiare.", "F"), ("Sabato Camila va a Venezia con Júlia.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Modi di dire", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["09.1 · NATURAL", "09.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Martedì grasso, al bar di Giulia. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "09.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Perché Camila chiede «Quanti lupi ci sono in Italia?» {R("Ha sentito due modi di dire con il lupo in un minuto.") if T else ""}</li>
<li>Perché, secondo te, i modi di dire sono così difficili per uno straniero? {R("Il significato non si capisce dalle parole; risposta libera.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Ecco la gatta! · …anzi, tre. · A Carnevale ogni scherzo vale. · In bocca al lupo! — Crepi! · Scommetto che… · lo stesso · Basta, mi arrendo!</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: dolci di Carnevale, colloquio, viaggio a Venezia, gesti italiani.</li>
<li>B: 2 un colloquio per il tirocinio · 3 si risponde «Crepi!» · 5 non si possono cambiare.</li>
<li>Espressioni: <i>anzi</i> = <i>aliás, ou melhor</i>; <i>lo stesso</i> = <i>mesmo assim</i>.</li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Vuoi qualcosa <u>da bere</u>?", "qualcosa che si può bere"), ("Le sfrappole sono <u>da provare</u>.", "si devono provare"),
          ("Non c'è niente <u>da fare</u>.", "non è possibile fare niente"), ("Venezia è una città <u>da vedere</u>.", "una città che si deve vedere"),
          ("Sabato non ho niente <u>da fare</u>.", "sono libera")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:46mm')}</li>" for s, a in ex)
    bank3 = "non è possibile fare niente · qualcosa che si può bere · si devono provare · sono libera · una città che si deve vedere"
    rules = [("Dopo <i>qualcosa, niente, molto</i> si usa", ["da", "per"], "da", "+ infinito."),
             ("<i>Una città da vedere</i> è una città che", ["si deve vedere", "vede"], "si deve vedere", "."),
             ("<i>Una maschera da gatto</i> indica", ["il tipo di maschera", "il materiale"], "il tipo di maschera", "."),
             ("Per lo scopo di un'azione si usa", ["per", "da"], "per", ": <i>sono venuta per salutarti</i>.")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("Hai qualcosa", ["da", "per"], "da", "leggere in treno?"),
          ("Sono passata", ["per", "da"], "per", "salutarti."),
          ("Ho comprato degli occhiali", ["da", "di"], "da", "sole.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: da + infinito", "8 min")}
{sub("A", "Frasi dal dialogo. Che cosa vuol dire la parte sottolineata? Usa le parole del riquadro.", "3 min")}
<div class="bank">{bank3}</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la preposizione giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>da + infinito</b> = una cosa che si deve o si può fare: <i>qualcosa da bere, niente da fare, una città da vedere, le sfrappole sono da provare, ho un biglietto da usare</i>. <b>da + nome</b> = uso o tipo: <i>una maschera da gatto, occhiali da sole</i>. Per lo scopo di chi agisce: <b>per</b> + infinito. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: far notare che in tutte le frasi la cosa «subisce» l'azione: le sfrappole vengono provate, la città viene vista.</li>
<li>C: frase 2: lo scopo di chi agisce (io passo per salutarti) → <i>per</i>. Ricordare anche <i>fame da lupi</i>: <i>da</i> + nome = «come quella dei lupi».</li></ol>""")

    grammar_ref_it.da_infinito(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["in bocca al lupo", "prendere un granchio", "costare un occhio della testa", "prendere due piccioni con una fava", "avere le mani bucate", "non vedere l'ora"]
    rgt = ["spendere troppo", "costare moltissimo", "buona fortuna", "aspettare con impazienza", "sbagliare", "ottenere due risultati con una sola azione"]
    ans = {"in bocca al lupo": "buona fortuna", "prendere un granchio": "sbagliare", "costare un occhio della testa": "costare moltissimo",
           "prendere due piccioni con una fava": "ottenere due risultati con una sola azione", "avere le mani bucate": "spendere troppo", "non vedere l'ora": "aspettare con impazienza"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: animali e corpo", "4 min")}
{sub("A", "Unisci i modi di dire al loro significato.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Hai le mani bucate?</li><li>Che cosa ti è costato un occhio della testa?</li><li>Quando hai preso un granchio?</li><li>Che cosa non vedi l'ora di fare?</li></ol>
<div class="box sand"><h4>ATTENZIONE: CALCHI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>In bocca al lupo! — Grazie!</td><td><b>In bocca al lupo! — Crepi!</b></td><td>«grazie» porta sfortuna!</td></tr>
<tr><td>Uccidere due conigli con un colpo.</td><td><b>Prendere due piccioni con una fava.</b></td><td>i modi di dire non si traducono.</td></tr>
<tr><td>Costa gli occhi della faccia.</td><td><b>Costa un occhio della testa.</b></td><td>un occhio, della testa.</td></tr>
<tr><td>Vuoi qualcosa per bere?</td><td><b>Vuoi qualcosa da bere?</b></td><td><i>qualcosa</i> + <i>da</i> + infinito.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: da e dà", "4 min")}
<p class="small" style="margin:.3mm 0">La preposizione <b>da</b> non ha accento e si lega alla parola successiva: <i>qualcosa da <b>be</b>re · niente da <b>fa</b>re</i>. Il verbo <b>dà</b> (<i>lui dà</i>, da <i>dare</i>) ha l'accento e si sente: <i>Giulia <b>dà</b> una sfrappola a Camila</i>.</p>
{audiocard(["09.2"])}
{sub("A", "Ascolta e ripeti. Poi l'insegnante dice una frase con «da» o con «dà»: tu dici quale hai sentito.", "4 min", "09.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S092))}</p>""",
    29, """<ol><li>A: in bocca al lupo c · prendere un granchio e · costare un occhio della testa b · due piccioni f · le mani bucate a · non vedere l'ora d.</li>
<li>Pronuncia: frasi per il gioco: <i>Giulia dà le sfrappole · le sfrappole da provare · Davide dà un consiglio · un consiglio da seguire · Chi mi dà una mano? · niente da fare.</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["da", "per"], "da"), (["fava", "pietra"], "fava"), (["testa", "faccia"], "testa"), (["da", "di"], "da"),
          (["da", "per"], "da"), (["da", "per"], "da"), (["da", "per"], "da"), (["l'ora", "il tempo"], "l'ora")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Hai qualcosa …? Ho sete.", "da bere"), ("Questo film è …: è bellissimo.", "da non perdere"),
          ("In cucina ci sono ancora i piatti …", "da lavare"), ("Domenica non ho niente …", "da fare"),
          ("Mi presti un libro … in vacanza?", "da leggere"), ("Roma è una città … almeno una volta.", "da vedere")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:28mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Sabato Camila scrive a Pietro da Venezia. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Camila:</b> Ciao Pietro! Sono a Venezia con Júlia. È davvero una città {p[0]} vedere almeno una volta nella vita. Júlia ha preso un granchio con le date, ma alla fine abbiamo preso due piccioni con una {p[1]}: niente folla e prezzi più bassi. Il caffè in piazza San Marco però è costato un occhio della {p[2]}! Ho comprato una maschera {p[3]} gatto vera, fatta a mano, e un libro {p[4]} leggere in treno. Adesso cerchiamo qualcosa {p[5]} mangiare: Júlia dice che i cicchetti sono {p[6]} provare. Ah, il colloquio di mercoledì è andato bene! Non vedo {p[7]} di raccontarti tutto.</div>
{sub("B", "Completa con da + infinito. Verbi: bere, fare, lavare, leggere, non perdere, vedere.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: gap 2 e 3: i modi di dire si imparano interi, non si cambia neanche una parola. I <i>cicchetti</i> sono gli assaggi dei bar veneziani.</li>
<li>B: far notare <i>da non perdere</i>: la negazione va tra <i>da</i> e l'infinito.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: modi di dire e gesti", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>chiedere il significato</th><th>spiegare</th><th>fare gli auguri</th><th>reagire</th></tr>
<tr><td><i>Che cosa vuol dire…? · In che senso? · Si usa spesso? · Come si dice…?</i></td><td><i>Vuol dire che… · Si dice quando… · Letteralmente… · È come…</i></td><td><i>In bocca al lupo! — Crepi! · Incrociamo le dita! · Forza! · Buon divertimento!</i></td><td><i>Che sfortuna! · Che figuraccia! · Non c'è niente da fare. · Mi arrendo!</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi spiega per due minuti tre modi di dire brasiliani a un amico italiano.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>che cosa vogliono dire letteralmente</li><li>che cosa significano davvero</li><li>quando si usano (un esempio)</li><li>se esiste qualcosa di simile in italiano</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Il gioco dei gesti. L'insegnante fa un gesto italiano: tu indovini il significato. Poi tu fai un gesto brasiliano e lo spieghi in italiano.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: 1 punte delle dita unite, mano su e giù = Ma che cosa dici? · 2 indice sulla guancia che gira = Buonissimo! · 3 pollice verso la bocca = Beviamo qualcosa? · 4 dorso della mano sotto il mento, verso fuori = Non me ne importa niente.") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Il Carnevale è una festa da bambini o da adulti?</li><li>I gesti sono utili o un po' maleducati?</li><li>Quale modo di dire italiano ti piace di più? Perché?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8). Idee: <i>pagar mico, chutar o balde, enfiar o pé na jaca, cair a ficha</i>.</li>
<li>B: le battute dell'insegnante sono in rosso: fare il gesto senza parlare, poi dire la frase solo dopo il tentativo dello studente.</li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare da + infinito (qualcosa da bere, una città da vedere).",
          "So spiegare un modo di dire e fare gli auguri."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Un post sui modi di dire.</b> Scrivi un post per un blog di lingue: spiega tre modi di dire (italiani o brasiliani) a chi impara la lingua. Prima leggi il post di Camila.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i><b>Quanti lupi ci sono in Italia?</b> Da quando vivo a Bologna, ogni giorno scopro un modo di dire da imparare. Il primo è stato «in bocca al lupo»: lo dici prima di un esame o di un colloquio, e l'altra persona risponde «crepi!», non «grazie». Poi c'è «una fame da lupi», quando hai tantissima fame. La mia amica Júlia, invece, ha preso un granchio: vuol dire che ha sbagliato, non che ha comprato un granchio! Il mio preferito è «prendere due piccioni con una fava»: nella mia lingua l'idea è la stessa, ma con due conigli. Il mio consiglio? Tenete sempre in tasca un quaderno da usare per le parole nuove: c'è sempre qualcosa da scrivere. E se non capite, fate il gesto: ma che dici?</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ tre modi di dire spiegati &nbsp;☐ almeno tre <i>da</i> + infinito &nbsp;☐ un esempio di situazione &nbsp;☐ un consiglio finale &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far sottolineare nel modello <i>un modo di dire da imparare, un quaderno da usare, qualcosa da scrivere</i>. La prossima lezione è il <b>Ripasso 1</b> (unità 01–09): ricordare allo studente di rileggere i registri degli errori.</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("09.1", "Modi di dire (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("09.2", "Ripeti: da + infinito")}
<p>{" · ".join(S092)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 09 - Modi di dire")
