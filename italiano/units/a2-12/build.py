# Speak! Ponte A2 - Unità 12 "Volevo, ma…" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 12", audio_json=os.path.join(HERE, "audio_it-a2-unita-12.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la stazione", "stazione"), ("B", "il pullman", "pullman"), ("C", "la gondola", "gondola"), ("D", "il canale", "canale"),
          ("E", "l'ombrello", "ombrello"), ("F", "la fila", "fila"), ("G", "le cartoline", "cartoline"), ("H", "il Palazzo Ducale", "Palazzo Ducale")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-12"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["12.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S122 = [x.split(": ", 1)[1] for x in _r["12.2 Ripeti"].split("\n")]
S123 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["12.3 Ascolta"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split(" ", 1)[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 12", "Volevo, ma…", "Un viaggio andato storto · <b>volevo / ho voluto · dovevo / ho dovuto · ne</b>",
                       [("SAI FARE", "raccontare un viaggio con dei problemi, dire che cosa volevi fare e che cosa hai dovuto fare, parlare di quantità"),
                        ("LINGUA", "Volevo entrare, ma c'era la fila. · Abbiamo dovuto prendere il pullman. · Ne ho fatte trecento."),
                        ("PRONUNCIA", "l'accento dell'imperfetto: volévo, volevàmo, volévano")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: in viaggio", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Sei mai stato/a a Venezia? Che cosa sai di questa città?</li><li>Hai mai avuto problemi in un viaggio? Che cosa è successo?</li><li>Quando viaggi, fai tante foto? Compri cartoline?</li></ol>""",
    24, """<ol><li>A: <i>il pullman</i> = l'autobus per i viaggi lunghi (port. <i>ônibus de viagem</i>). <i>Fare la fila</i> = aspettare il proprio turno.</li>
<li>B: domanda 2: lasciar raccontare liberamente; le frasi con <i>volevo…, ma…</i> arrivano a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: un viaggio a Venezia</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Lo sciopero · la pioggia e i cicchetti · il racconto a Marco</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>volevo / ho voluto, dovevo / ho dovuto, potevo / ho potuto · ne</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forme · imperfetto o passato prossimo · ne e l'accordo</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>L'accento dell'imperfetto · intenzione o fatto?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>La gita di Davide · rispondi con ne · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Un viaggio andato storto · quanti?</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Il 25 aprile, festa della Liberazione, Júlia e Giulia vanno a Venezia per il fine settimana: finalmente Júlia vede la città che voleva vedere dall'anno scorso (A1, unità 26). Ma alla stazione il treno è cancellato per sciopero: dovevano arrivare alle nove, prendono il pullman delle otto (restano tre biglietti, ne comprano due). A Venezia piove e Júlia ha dimenticato l'ombrello; la gondola costa ottanta euro, quindi mangiano i cicchetti in un bacaro. Lunedì Júlia racconta tutto a Marco: non ha potuto vedere il Palazzo Ducale per la fila, ma domenica c'era il sole e ha voluto vedere tutto (venti chilometri a piedi). Ha fatto trecento foto e ha comprato cinque cartoline: una è per Marco.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>La differenza <i>volevo / ho voluto</i> è come <i>eu queria / eu quis</i>: qui il portoghese aiuta. Il vero problema è <b>ne</b>, che il portoghese non ha: lo studente dice <i>ho uno</i> (→ <b>ne ho uno</b>), <i>ho fatto trecento</i> (→ <b>ne ho fatte trecento</b>). Attenzione anche all'accento: <i>volévamo</i> ✗ → <b>volevàmo</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>25 aprile</b> è la festa della Liberazione (1945). Quando una festa è vicina al fine settimana, gli italiani fanno il <b>ponte</b>. Gli <b>scioperi</b> dei treni sono annunciati qualche giorno prima: conviene controllare sul sito. A Venezia i <b>bacari</b> sono piccoli bar dove si mangiano i <b>cicchetti</b> (piccoli assaggi) e si beve un'<b>ombra</b>, un bicchiere di vino.</div>
<div class="box"><h4>AUDIO</h4>Traccia 12.1 Tre dialoghi (lento e naturale) · Traccia 12.2 Ascolta e ripeti · Traccia 12.3 Intenzione o fatto?</div>""")

    # Page 2
    st = [("Perché Júlia e Giulia non prendono il treno?", "è cancellato per sciopero"), ("Che cosa voleva fare Júlia a Venezia alle nove?", "colazione in piazza San Marco"),
          ("Quanti biglietti del pullman restano? Quanti ne comprano?", "ne restano tre, ne comprano due")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:52mm')}</li>" for q, a in st)
    vf = [("Júlia ha portato l'ombrello.", "F"), ("Fanno un giro in gondola.", "F"), ("Al bacaro prendono sei cicchetti.", "V"),
          ("Júlia è entrata nel Palazzo Ducale.", "F"), ("Domenica Júlia ha camminato tantissimo.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: un viaggio particolare", "10 min")}
<p>È il 25 aprile, festa della Liberazione. Júlia e Giulia vogliono passare il fine settimana a Venezia…</p>
{audiocard(["12.1 · SLOW", "12.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "12.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialoghi 2 e 3. Vero (V) o falso (F)?", "4 min", "12.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Quante foto ha fatto Júlia? Quante cartoline ha comprato? Per chi è una cartolina?", "3 min")}
<div class="wline">{R("Ne ha fatte trecento. Ne ha comprate cinque: una è per Marco.")}</div>""",
    27, """<ol><li>A: versione <b>lenta</b>. Far notare <i>Dovevamo arrivare alle nove</i>: era il programma, ma non è successo.</li>
<li>B: versione <b>naturale</b>. 2: costa ottanta euro. 4: <i>volevo entrare, ma… non ho potuto</i>. Chiedere: <i>Che cosa sono i cicchetti?</i></li></ol>""")

    # Page 3
    rules = [("<i>Volevo entrare, ma c'era la fila.</i> Júlia", ["non è entrata", "è entrata"], "non è entrata"),
             ("<i>Abbiamo dovuto prendere il pullman.</i> Lo hanno preso?", ["sì", "non sappiamo"], "sì"),
             ("Per un programma o un'intenzione usiamo", ["l'imperfetto (volevo, dovevo)", "il passato prossimo (ho voluto)"], "l'imperfetto (volevo, dovevo)"),
             ("Per una cosa successa davvero usiamo", ["il passato prossimo (ho dovuto)", "l'imperfetto (dovevo)"], "il passato prossimo (ho dovuto)"),
             ("<i>Quanti cicchetti? Ne prendiamo sei.</i> <i>Ne</i> sostituisce", ["di cicchetti (una quantità)", "i cicchetti (tutti)"], "di cicchetti (una quantità)"),
             ("<i>Le foto? Ne ho fatte trecento.</i> Il participio finisce in <i>-e</i> perché", ["le foto sono femminili plurali", "è sempre così"], "le foto sono femminili plurali")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("", ["Volevo", "Ho voluto"], "Volevo", "partire alle sette, ma il treno non c'era."), ("Per lo sciopero", ["dovevamo", "abbiamo dovuto"], "abbiamo dovuto", "prendere il pullman."),
          ("Quanti ombrelli hai? —", ["Ho uno.", "Ne ho uno."], "Ne ho uno.", ""), ("Le cartoline? Ne ho", ["comprato", "comprate"], "comprate", "cinque.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: volevo o ho voluto? · ne", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Dovevamo</b> arrivare alle nove. · <b>Volevo</b> fare colazione in piazza San Marco. · <b>Volevo</b> entrare, ma c'era una fila di due ore.<br>
2. <b>Abbiamo dovuto</b> prendere il pullman. · <b>Non ho potuto</b> vederlo. · <b>Ho voluto</b> vedere tutto.<br>
3. Ne sono rimasti tre. · <b>Ne</b> prendiamo due. · Io <b>ne</b> ho uno piccolo. · <b>Ne</b> ho fatt<b>e</b> trecento! · <b>Ne</b> ho comprat<b>e</b> cinque.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>volevo, dovevo, potevo</b> (imperfetto) = un programma o un'intenzione, spesso con <i>ma…</i>. <b>ho voluto, ho dovuto, (non) ho potuto</b> (passato prossimo) = è successo davvero. <b>ne</b> = una quantità di qualcosa: <i>ne prendo due</i>; al passato il participio si accorda: <i>ne ho fatte trecento</i>. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: frase 1: chiedere <i>È entrata? Come lo sai?</i> → per il <i>ma</i>. Ricordare <i>non sono potuta entrare</i> (con <i>essere</i>) come alternativa corretta.</li>
<li>C: <i>Ho uno</i> è l'errore più frequente: in italiano la quantità senza nome vuole sempre <i>ne</i>.</li></ol>""")

    grammar_ref_it.modali_passato_ne(b)

    # Page 5
    ans3 = ["intenzione", "fatto", "intenzione", "fatto", "intenzione", "fatto"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Quanti ombrelli? Ho uno.</td><td><b>Ne ho uno.</b></td><td>Una quantità: <i>ne</i>.</td></tr>
<tr><td>Le foto? Ne ho fatto trecento.</td><td><b>Ne ho fatte trecento.</b></td><td>Accordo con le foto.</td></tr>
<tr><td>Ho dovuto partire alle sette, ma il treno era cancellato.</td><td><b>Dovevo partire alle sette, ma…</b></td><td>Programma non realizzato.</td></tr>
<tr><td>Volevamo (volévamo) partire.</td><td><b>Volevàmo partire.</b></td><td>L'accento.</td></tr>
<tr><td>Non ho potuto di entrare.</td><td><b>Non ho potuto entrare.</b></td><td>Modale + infinito, senza <i>di</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["12.2", "12.3"])}
{sub("A", "Ascolta e ripeti. Attenzione all'accento: volévo, volevàmo, volévano.", "2 min", "12.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S122)}</div>
{sub("B", "Intenzione (forse non è successo) o fatto (è successo)? Ascolta e scegli.", "2 min", "12.3")}
{twocol([f'<li value="{i+1}">{ch(["intenzione", "fatto"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>dovevo / ho dovuto</i> sono simili a <i>tinha que / tive que</i>: usare il confronto con il portoghese.</li>
<li>4A: nella prima e terza persona plurale l'accento si sposta: <i>volevàmo, volevàte</i>, ma <i>volévano</i>. 4B: imperfetto = intenzione, passato prossimo = fatto.</li></ol>""")

    # Page 6
    st6 = [("Sabato Davide ", "(volere)", "voleva", " andare al mare. "), ("", "(dovere)", "Doveva", " partire alle otto, ma la macchina non partiva: "),
           ("", "(dovere)", "ha dovuto", " chiamare il meccanico. Così non "), ("", "(potere)", "è potuto / ha potuto", " andare al mare. Domenica però "),
           ("", "(volere)", "ha voluto", " riprovare: è partito alle sei ed è arrivato al mare per primo!")]
    stt = "".join(f"{a}<i class='small'>{v}</i> {A(c, 'min-width:22mm')}{z}" for a, v, c, z in st6)
    qn = [("Quanti caffè bevi al giorno? (2)", "Ne bevo due."), ("Quante foto hai fatto a Venezia? (300)", "Ne ho fatte trecento."),
          ("Quanti biglietti avete comprato? (2)", "Ne abbiamo comprati due."), ("Hai fratelli? (no)", "No, non ne ho.")]
    qnl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qn)
    wb = [("scioperare", "lo sciopero"), ("piovere", "la pioggia"), ("camminare", "la camminata"), ("viaggiare", "il viaggio")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:24mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "La gita di Davide. Imperfetto o passato prossimo? Scrivi il verbo.", "4 min")}
<div class="box" style="margin-top:1mm;font-size:9.2pt;line-height:2">{stt}</div>
{sub("B", "Rispondi con ne.", "3 min")}
<ol style="line-height:1.45">{qnl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: <i>voleva / doveva</i> = il programma; <i>ha dovuto, (non) è potuto, ha voluto</i> = i fatti. Con <i>andare</i> va bene anche <i>non è potuto andare</i>.</li>
<li>B: <i>Non ne ho</i> = zero. C: <i>la pioggia</i> e <i>lo sciopero</i> sono nei dialoghi.</li></ol>""")

    # Page 7
    cards = ["Volevi andare in spiaggia, ma…", "Dovevi prendere l'aereo alle 9, ma…", "Volevi vedere un museo, ma…", "Dovevi incontrare un amico, ma…"]
    cl = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>{i+1}.</b> {t}</div>' for i, t in enumerate(cards))
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Un viaggio andato storto. Scegli una situazione e racconta: che cosa volevi fare? Che cosa è successo? Che cosa hai dovuto fare? Poi racconta un tuo viaggio vero.", "7 min")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:1mm">{cl}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Volevo…, ma… · Dovevo…, invece… · Ho dovuto… · Non ho potuto… · Per fortuna… · Purtroppo… · Alla fine… · Che sfortuna! · È stato un viaggio particolare!</div>
{sub("B", "Quanti? Fai le domande all'insegnante e rispondi con ne: libri letti quest'anno · paesi visitati · lingue parlate · caffè al giorno · foto sul telefono.", "5 min")}""",
    22, """<ol><li>A: l'insegnante fa domande per far usare i due tempi: <i>E poi? Sei riuscito/a a…? Che cosa hai dovuto fare?</i></li>
<li>B: pretendere sempre <i>ne</i>: <i>Ne ho letti cinque. Non ne ho visitato nessuno.</i></li></ol>""")

    # Page 8
    pc = [("A2 · 11", "So usare l'ho visto, l'ho vista, già, ancora, appena."), ("A2 · 12", "So dire che cosa volevo fare e che cosa ho dovuto fare."),
          ("A2 · 12", "So usare ne con le quantità (ne ho due)."), ("A2 · 12", "So raccontare un viaggio con dei problemi."),
          ("A2 · 12", "So mettere l'accento giusto nell'imperfetto.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Quante sorelle hai? Ho due.", "Ne ho due."), ("Volevo partire, ma c'era lo sciopero.", "✓"),
          ("Ho dovuto prendere il treno, ma era cancellato.", "Dovevo prendere il treno…"), ("Le foto? Ne ho fatto cento.", "Ne ho fatte cento."),
          ("Non ho potuto di vedere il museo.", "Non ho potuto vedere il museo."), ("Ne abbiamo comprati due.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un viaggio particolare (50–75 parole).</b> Racconta un viaggio in cui qualcosa è andato storto. Che cosa volevi fare? Che cosa hai dovuto fare? Che cosa non hai potuto fare? Usa anche <i>ne</i> (foto, cartoline, giorni…).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il racconto; l'insegnante fa domande con <i>quanti…?</i> per far usare <i>ne</i>. Unità 13: <i>Che tipo sei?</i> (comparativi, superlativo, meglio / migliore).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("12.1", "Un viaggio particolare (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("12.2", "Ascolta e ripeti")}
<p>{" · ".join(S122)}</p>
{sub("12.3", "Intenzione o fatto?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S123))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 12 - Volevo, ma")
