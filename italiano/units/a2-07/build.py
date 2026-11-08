# Speak! Ponte A2 - Unità 07 "Progetti" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
from calendario import calendario
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 07", audio_json=os.path.join(HERE, "audio_it-a2-unita-07.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la valigia", "valigia"), ("B", "l'agenda", "agenda"), ("C", "il Carnevale", "Carnevale"), ("D", "la maratona", "maratona"),
          ("E", "l'annaffiatoio", "annaffiatoio"), ("F", "il passaporto", "passaporto"), ("G", "l'esame", "esame"), ("H", "la colomba", "colomba")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-07"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["07.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S072 = [x.split(": ", 1)[1] for x in _r["07.2 Ripeti il futuro"].split("\n")]
S073 = [x.split(": ", 1)[1] for x in _r["07.3 Presente o futuro"].split("\n")]


def _key(w):
    return w.split("'")[-1] if w.startswith("l'") else w.split()[-1]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 07", "Progetti", "Piani e promesse · <b>il futuro semplice, se…, bisogna</b>",
                       [("SAI FARE", "parlare dei tuoi progetti per i prossimi mesi e fare promesse"),
                        ("LINGUA", "Partirò il 5 febbraio. · Se finisco tutto, partirò tranquilla. · Bisogna comprare i regali."),
                        ("PRONUNCIA", "l'accento finale del futuro · presente o futuro?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: un anno nuovo", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=lambda w: _key(w).lower()))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quali di queste cose sono nei tuoi progetti per quest'anno?</li><li>Hai un viaggio in programma? Dove vuoi andare?</li><li>Che cosa ti piacerebbe imparare quest'anno?</li></ol>""",
    22, """<ol><li>A: <i>la colomba</i> è il dolce di Pasqua (a forma di colomba), come il panettone a Natale. <i>L'esame</i>: all'università gli esami sono spesso orali.</li>
<li>B: lo studente usa il presente o il condizionale (unità 05): il futuro arriva nell'ascolto.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: viaggi e progetti</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il biglietto per il Brasile · i progetti degli amici · un favore alla signora Rossi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Il futuro semplice · se + presente · bisogna + infinito</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forme · irregolari · usi · se… e bisogna</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento finale: tornerò · presente o futuro?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Il piano di Davide · se… · che cosa bisogna fare prima di un viaggio?</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>L'agenda di Júlia · i tuoi progetti · la catena del «se»</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine gennaio. Júlia ha comprato il biglietto: partirà il 5 febbraio e tornerà il 19, due settimane a Belo Horizonte per il Carnevale. Marco le ricorda che bisogna finire il progetto del Comune; a fine febbraio verranno a Bologna Luca e Sara. Al bar Davide annuncia che a ottobre correrà la maratona di Bologna (otto mesi di allenamento, sveglia alle sei); Giulia farà un corso di pasticceria e a Pasqua venderà le sue colombe; Bruno a giugno darà il suo primo esame all'università. La sera prima della partenza Júlia lascia le chiavi alla signora Rossi, che innaffierà le piante e prenderà la posta. Júlia le porterà un pacco di caffè brasiliano.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nel parlato brasiliano il futuro si fa quasi sempre con <i>ir + infinito</i> (<i>vou voltar</i>): lo studente dice <i>vado a tornare</i>, che in italiano non esiste. Altri errori: <i>tornarò</i> (→ <b>tornerò</b>), <i>poterò</i> (→ <b>potrò</b>), l'accento dimenticato nello scritto (<i>tornero</i>) e <i>bisognamo</i> (<i>bisogna</i> non cambia).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Anche in Italia c'è il <b>Carnevale</b>: i più famosi sono quelli di Venezia (le maschere) e di Viareggio (i carri). A Carnevale si mangiano le <b>chiacchiere</b> (o <i>sfrappole</i> a Bologna). All'università gli <b>esami</b> sono spesso orali e il voto va da 18 a 30 (il massimo è <i>30 e lode</i>).</div>
<div class="box"><h4>AUDIO</h4>Traccia 07.1 Tre dialoghi (lento e naturale) · Traccia 07.2 Il futuro · Traccia 07.3 Presente o futuro?</div>""")

    # Page 2
    st = [("Quando parte Júlia? Quando torna?", "il 5 febbraio; il 19"), ("Che cosa bisogna fare prima della partenza?", "finire il progetto del Comune"),
          ("Chi verrà a Bologna a fine febbraio?", "Luca e Sara (il fratello di Marco e sua moglie)")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    who = [("comincerà ad allenarsi a febbraio", "Davide"), ("farà un corso di pasticceria", "Giulia"), ("deve ancora comprare i regali", "Júlia"),
           ("darà il primo esame a giugno", "Bruno"), ("si alzerà ogni mattina alle sei", "Davide")]
    wl = "".join(f"<tr><td>{s}</td><td style='width:26mm;text-align:center'>{A(w, 'min-width:18mm')}</td></tr>" for s, w in who)
    b.page(f"""{sec(2, "Ascolto: partirò il cinque febbraio", "10 min")}
<p>Júlia ha comprato il biglietto per il Brasile, gli amici raccontano i loro progetti e la signora Rossi farà un favore a Júlia.</p>
{audiocard(["07.1 · SLOW", "07.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "07.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Chi? Davide, Giulia, Júlia o Bruno?", "4 min", "07.1 · NATURAL")}
<table style="margin:0">{wl}</table>
{sub("C", "Dialogo 3. Che cosa farà la signora Rossi? Che cosa le porterà Júlia?", "3 min")}
<div class="wline">{R("innaffierà le piante il lunedì e il giovedì e prenderà la posta · un pacco di caffè brasiliano")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>partirò</i> e <i>tornerò</i>: l'accento cade sull'ultima sillaba.</li>
<li>B: versione <b>naturale</b>. Davide e la maratona: un richiamo ai consigli dell'unità 04.</li></ol>""")

    # Page 3
    rules = [("<i>Partirò, tornerò, farai, sarà</i> parlano di", ["progetti e previsioni", "abitudini nel passato"], "progetti e previsioni"),
             ("Nei verbi in <b>-are</b> (<i>tornare, comprare</i>) il futuro ha", ["-erò", "-arò"], "-erò"),
             ("<i>Verranno, vorrò, potrò, andrò</i> hanno la stessa radice del", ["condizionale", "passato prossimo"], "condizionale"),
             ("Dopo <b>se</b>, per un futuro vicino, si usa spesso", ["il presente", "l'imperfetto"], "il presente"),
             ("<b>Bisogna</b> + infinito vuol dire", ["è necessario", "è possibile"], "è necessario"),
             ("<i>Bisogna</i> con <i>noi</i> o con <i>loro</i>", ["non cambia", "diventa bisognamo, bisognano"], "non cambia")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("(io, partire) ", "partirò"), ("(tu, comprare) ", "comprerai"), ("(lei, essere) ", "sarà"),
          ("(noi, fare) ", "faremo"), ("(voi, venire) ", "verrete"), ("(loro, andare) ", "andranno")]
    ccl = [f'<li value="{i+1}">{a}{A(c, "min-width:26mm")}</li>' for i, (a, c) in enumerate(cc)]
    b.page(f"""{sec(3, "Grammatica: il futuro semplice", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Partirò</b> il cinque febbraio e <b>tornerò</b> il diciannove. · Che cosa <b>farai</b> a febbraio?<br>
2. A fine mese <b>verranno</b> Luca e Sara. · <b>Ci vorranno</b> otto mesi. · <b>Sarà</b> un anno pieno di novità!<br>
3. <b>Se finisco</b> tutto entro il quattro, <b>partirò</b> tranquilla. · <b>Se</b> il cliente <b>telefona</b>, lo <b>chiamerò</b> io.<br>
4. <b>Bisogna finire</b> il progetto. · <b>Bisogna</b> ancora <b>comprare</b> i regali.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scrivi il futuro.", "3 min")}
{twocol(ccl, 4)}
<div class="box sand"><h4>REGOLA</h4>Il <b>futuro semplice</b> parla di progetti, previsioni e promesse. Desinenze: <b>-ò, -ai, -à, -emo, -ete, -anno</b> (<i>-are</i> → <b>-erò</b>). Irregolari come il condizionale: <i>andrò, avrò, potrò, vorrò, verrò, sarò, farò</i>. <b>Se + presente</b>, poi futuro (o presente). <b>Bisogna + infinito</b> = è necessario. Tutto: pagina 4.</div>""",
    20, """<ol><li>B: far confrontare <i>vorrei / vorrò</i>, <i>andrei / andrò</i>: la radice è la stessa.</li>
<li>C: 5: <i>venire → verrete</i>, doppia <b>r</b>. Ricordare l'accento scritto su <i>partirò, sarà</i>.</li></ol>""")

    grammar_ref_it.futuro_semplice(b)

    # Page 5
    ans3 = ["presente", "futuro", "futuro", "presente", "futuro", "presente"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Vado a tornare il 19.</td><td><b>Tornerò / Torno il 19.</b></td><td>Futuro o presente.</td></tr>
<tr><td>Comprarò i regali.</td><td><b>Comprerò i regali.</b></td><td><i>-are</i> → <i>-erò</i>.</td></tr>
<tr><td>Poterò venire.</td><td><b>Potrò venire.</b></td><td>Irregolare: <i>potr-</i>.</td></tr>
<tr><td>Bisognamo partire presto.</td><td><b>Bisogna partire presto.</b></td><td><i>bisogna</i> non cambia.</td></tr>
<tr><td>Se avrò tempo, ti chiamarò.</td><td><b>Se avrò tempo, ti chiamerò.</b></td><td><i>-are</i> → <i>-erò</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["07.2", "07.3"])}
{sub("A", "L'accento finale del futuro. Ascolta e ripeti: partiRÒ, torneRÒ, saRÀ.", "2 min", "07.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S072)}</div>
{sub("B", "Presente o futuro? Ascolta e scegli.", "2 min", "07.3")}
{twocol([f'<li value="{i+1}">{ch(["presente", "futuro"], a)}</li>' for i, a in enumerate(ans3)], 4)}
<p class="small" style="margin:1mm 0">Aiuto: <i>TORno</i> (presente) · <i>torneRÒ</i> (futuro). Nel futuro la voce si ferma con forza sull'ultima sillaba.</p>""",
    28, """<ol><li>Errori: <i>vado a…</i> + infinito in italiano vuol dire «vado (in un posto) per…»: <i>vado a comprare il pane</i>.</li>
<li>4B: le parole sono 1 torno, 2 tornerò, 3 parlerà, 4 parla, 5 finirò, 6 finisco.</li></ol>""")

    # Page 6
    pl = [("A febbraio Davide ", "(cominciare)", "comincerà", " ad allenarsi. Ogni mattina "), ("", "(alzarsi)", "si alzerà", " alle sei e "),
          ("", "(correre)", "correrà", " per un'ora sotto i portici. A marzo "), ("", "(comprare)", "comprerà", " scarpe nuove e "),
          ("", "(fare)", "farà", " una visita dal medico. Lui e Bruno "), ("", "(andare)", "andranno", " in palestra tre volte alla settimana. Ci "),
          ("", "(volere)", "vorranno", " otto mesi, ma a ottobre Davide "), ("", "(essere)", "sarà", " pronto!")]
    plt = "".join(f"{a}<i class='small'>{v}</i> {A(c, 'min-width:20mm')}{z}" for a, v, c, z in pl)
    se = [("Se piove domenica,", "resterò a casa a studiare."), ("Se Bruno passa il primo esame,", "faremo una grande festa."),
          ("Se Giulia fa le colombe,", "le comprerò per tutta la famiglia."), ("Se la signora Rossi innaffia le piante,", "Júlia le porterà un regalo.")]
    left = "".join(f"<li>{a}</li>" for a, _ in se)
    rgt = [se[1][1], se[3][1], se[0][1], se[2][1]]
    right = "".join(f"<div style='margin:0 0 .4mm'><b>{l}.</b> {x}</div>" for l, x in zip("abcd", rgt))
    bank = "cambiare i soldi · fare la valigia · innaffiare le piante · lasciare le chiavi a un vicino · prenotare il volo · rinnovare il passaporto"
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Il piano di Davide. Scrivi il futuro.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9.2pt;line-height:2">{plt}</div>
{sub("B", "Se… Unisci le due parti (1–4 con a–d).", "2 min")}
<div class="two"><ol style="margin:0">{left}</ol><div>{right}</div></div>
<p class="small" style="margin:.5mm 0">{R("1 c · 2 a · 3 d · 4 b") if T else ""}</p>
{sub("C", "Prima di un viaggio: che cosa bisogna fare? Scrivi tre frasi con bisogna.", "3 min")}
<div class="bank">{bank}</div>
<div class="wline">{R("Bisogna prenotare il volo un mese prima.")}</div><div class="wline"></div><div class="wline"></div>""",
    20, """<ol><li>A: <i>si alzerà</i>: il pronome riflessivo resta prima del verbo. <i>Ci vorranno</i> = futuro di <i>ci vogliono</i> (unità 06).</li>
<li>C: aggiungere a voce: <i>Se vai in Brasile, che cosa bisogna portare?</i></li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "L'agenda di Júlia. Fai domande all'insegnante e rispondi: Che cosa farà Júlia il 9 febbraio? Quando tornerà?", "4 min")}
{calendario()}
{sub("B", "I tuoi progetti. Rispondi e fai le stesse domande all'insegnante.", "5 min")}
<ol style="line-height:1.6"><li>Che cosa farai questo fine settimana?</li><li>Dove andrai in vacanza quest'anno? Con chi?</li><li>Che cosa bisogna fare per imparare bene l'italiano?</li><li>Dove sarai fra cinque anni? Che lavoro farai?</li></ol>
{sub("C", "La catena del «se». L'insegnante comincia, tu continui: Se domani piove, resterò a casa. → Se resto a casa, guarderò un film. → Se guardo un film…", "3 min")}""",
    22, """<ol><li>A: risposte modello: <i>Il 9 andrà al Carnevale con le cugine. Il 14 festeggerà il compleanno della mamma. Il 16 farà una gita a Ouro Preto.</i></li>
<li>C: la catena continua finché uno dei due sbaglia la forma o non trova un'idea.</li></ol>""")

    # Page 8
    pc = [("A2 · 05", "So chiedere in modo gentile con il condizionale."), ("A2 · 06", "So usare sapere, conoscere e ci vuole."),
          ("A2 · 07", "So parlare dei miei progetti con il futuro."), ("A2 · 07", "So fare frasi con se: Se piove, resterò a casa."),
          ("A2 · 07", "So dire che cosa bisogna fare.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("L'anno prossimo vado a studiare in Italia. (= futuro)", "…studierò in Italia."), ("Se finisco presto, ti chiamerò.", "✓"),
          ("Domani mangiarò da mia nonna.", "Domani mangerò…"), ("Bisognano prenotare il ristorante.", "Bisogna prenotare…"),
          ("Ci vorranno due ore per arrivare.", "✓"), ("Quando poterai venire?", "Quando potrai venire?")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. I miei progetti per quest'anno (50–75 parole).</b> Che cosa farai? Dove andrai? Che cosa bisogna fare per realizzare i tuoi progetti? Usa il futuro, almeno una frase con <i>se</i> e una con <i>bisogna</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il testo; l'insegnante fa domande (<i>E se non avrai tempo?</i>). Unità 08: <i>Mi scusi…</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("07.1", "Partirò il cinque febbraio (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("07.2", "Il futuro")}
<p>{" · ".join(S072)}</p>
{sub("07.3", "Presente o futuro?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S073))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 07 - Progetti")
