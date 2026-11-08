# Speak! Ponte A2 - Unità 11 "Ti va di uscire?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 11", audio_json=os.path.join(HERE, "audio_it-a2-unita-11.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il cinema", "cinema"), ("B", "la mostra", "mostra"), ("C", "il museo", "museo"), ("D", "il concerto", "concerto"),
          ("E", "l'aperitivo", "aperitivo"), ("F", "la pizza", "pizza"), ("G", "il teatro", "teatro"), ("H", "la partita", "partita")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-11"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["11.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S112 = [x.split(": ", 1)[1] for x in _r["11.2 Ripeti"].split("\n")]
S113 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["11.3 Che cosa"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if w.startswith("l'") else w.split(" ", 1)[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 11", "Ti va di uscire?", "Il tempo libero · <b>l'ho visto, l'ho vista · già, non… ancora, appena</b>",
                       [("SAI FARE", "proporre un'uscita, dire che cosa hai già fatto e che cosa non ancora, organizzare una serata"),
                        ("LINGUA", "L'ho già visto. · Non l'ho ancora vista. · Li ho presi ieri. · I biglietti li compro io."),
                        ("PRONUNCIA", "l'ho visto / l'ho vista: ascoltare la vocale finale")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: il fine settimana", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Che cosa fai di solito il sabato sera?</li><li>Qual è l'ultimo film che hai visto? E l'ultimo concerto?</li><li>C'è una mostra o un museo che non hai ancora visto?</li></ol>""",
    26, """<ol><li>A: <i>la mostra</i> = l'esposizione di quadri o foto (port. <i>exposição</i>, non <i>mostra</i> nel senso di "mostrar"). <i>La partita</i> = il gioco di calcio.</li>
<li>B: domanda 2: lo studente dice <i>ho visto…</i>; domanda 3: <i>non ho ancora visto…</i>. Annotare le frasi: tornano a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il tempo libero</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>L'invito di Giulia · al museo · in pizzeria</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Pronomi diretti + passato prossimo · già, non… ancora, appena</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Forme · accordo del participio · già / ancora / appena · i biglietti li compro io</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>l'ho visto / l'ho vista</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Rispondi con il pronome · già, ancora o appena? · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Organizziamo la serata · hai già…?</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio aprile. Giulia invita Júlia a uscire sabato sera. Il film <i>Notte a Napoli</i>? Júlia l'ha già visto con Marco. La mostra di fotografia al MAMbo su Bologna negli anni Cinquanta? Non l'ha ancora vista: ci vanno insieme e Giulia compra i biglietti online. Davide non viene: lavora al ristorante. Al museo Júlia trova una foto di piazza Maggiore nel 1952, piena di biciclette, e la fotografa per la signora Rossi. Dopo, in pizzeria, arrivano Bruno e Chiara. Bruno dice che ha letto tutto il libro di Storia medievale per l'esame di giugno, ma Chiara lo smaschera: è a pagina cento. Le birre le paga lui.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In portoghese diciamo <i>Já vi</i> o <i>Eu vi ele</i>, senza accordo del participio. In italiano il pronome va <b>prima</b> di <i>avere</i> e il participio si accorda: <b>l'ho vista</b> (la mostra), <b>li ho presi</b> (i biglietti). Errori tipici: <i>ho visto lo</i>, <i>la mostra? l'ho visto</i>, <i>ancora non ho visto</i> (→ <b>non ho ancora visto</b>). <i>Mostra</i> in italiano è la <i>exposição</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Il <b>MAMbo</b> è il Museo d'Arte Moderna di Bologna, nell'ex forno del pane. Molti musei italiani hanno <b>ingresso gratuito</b> la prima domenica del mese. Il sabato sera gli italiani escono tardi: aperitivo verso le 19, cena dopo le 20.30. Chi invita spesso paga: <i>Offro io!</i></div>
<div class="box"><h4>AUDIO</h4>Traccia 11.1 Tre dialoghi (lento e naturale) · Traccia 11.2 Ascolta e ripeti · Traccia 11.3 Di che cosa parla?</div>""")

    # Page 2
    st = [("Perché Júlia non vuole andare al cinema?", "ha già visto il film (con Marco)"), ("Che cosa decidono di fare?", "vedere la mostra di fotografia al MAMbo"),
          ("Perché Davide non viene?", "lavora al ristorante")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    vf = [("Giulia ha comprato i biglietti il giorno prima.", "V"), ("Giulia non ha visto nessuna foto della mostra.", "F"),
          ("La foto di piazza Maggiore è del 1952.", "V"), ("Quando arrivano Bruno e Chiara, Júlia e Giulia hanno già ordinato.", "F"),
          ("Bruno ha letto tutto il libro.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: l'ho già visto!", "10 min")}
<p>È venerdì pomeriggio. Giulia ha voglia di uscire e telefona a Júlia.</p>
{audiocard(["11.1 · SLOW", "11.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "11.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialoghi 2 e 3. Vero (V) o falso (F)?", "4 min", "11.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Che cosa dice Chiara di Bruno? Chi paga le birre?", "3 min")}
<div class="wline">{R("Non ha ancora finito il libro: ieri era a pagina cento. Le birre le paga Bruno.")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>L'ho già visto</i> (il film) e <i>non l'ho ancora vista</i> (la mostra): perché <i>-o</i> e <i>-a</i>?</li>
<li>B: versione <b>naturale</b>. 2: <i>alcune le ho viste</i>. 4: <i>non ancora, siamo appena arrivate</i>. <i>Gliela mostro</i> (dialogo 2) è solo da capire: i pronomi doppi arrivano nell'unità 25.</li></ol>""")

    # Page 3
    rules = [("Con il passato prossimo il pronome <i>lo / la</i> va", ["prima di avere: l'ho visto", "dopo il participio: ho visto lo"], "prima di avere: l'ho visto"),
             ("<i>La mostra? L'ho vista.</i> Il participio finisce in <i>-a</i> perché la mostra è", ["femminile", "maschile"], "femminile"),
             ("<i>I biglietti? Li ho presi.</i> Con <i>li</i> il participio finisce in", ["-i", "-o"], "-i"),
             ("<i>Già, ancora, appena</i> vanno", ["tra avere e il participio", "alla fine della frase"], "tra avere e il participio"),
             ("Per una cosa non fatta diciamo", ["non l'ho ancora vista", "ancora non l'ho vista"], "non l'ho ancora vista"),
             ("<i>Ho appena sentito Davide</i> vuol dire che l'ho sentito", ["un momento fa", "tanto tempo fa"], "un momento fa")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Il film? L'ho", ["visto", "vista"], "visto", "ieri."), ("La pizza? L'ho", ["mangiato", "mangiata"], "mangiata", "tutta."),
          ("I biglietti? Li ho", ["comprato", "comprati"], "comprati", "online."), ("Le foto? Le ho", ["viste", "visti"], "viste", "su internet.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: l'ho visto, l'ho vista", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Il film? <b>L'ho già visto</b>. · La mostra? <b>Non l'ho ancora vista</b>.<br>
2. I biglietti? <b>Li ho presi</b> ieri. · Le foto? Alcune <b>le ho viste</b>.<br>
3. Davide? <b>L'ho appena sentito</b>. · <b>Siamo appena arrivate</b>.<br>
4. <b>I biglietti li</b> compro io. · <b>Le birre le</b> pago io!</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli il participio giusto.", "3 min")}
{twocol([f'<li value="{i+1}">' + x[4:] for i, x in enumerate(ccl.split('</li>')[:-1])], 3)}
<div class="box sand"><h4>REGOLA</h4><b>lo / la</b> + avere → <b>l'ho</b>. Il participio si accorda con il pronome diretto: <b>l'ho visto, l'ho vista, li ho visti, le ho viste</b>. <b>già · non… ancora · appena</b> vanno tra <i>avere</i> e il participio. Nel parlato: <i>I biglietti <b>li</b> compro io</i>. Tutto: pagina 4.</div>""",
    27, """<ol><li>B: chiedere allo studente di trovare nei dialoghi altri esempi: <i>l'ha conosciuta, l'ho appena fatta, l'ho letto tutto, non l'hai ancora finito</i>.</li>
<li>C: lo studente pensa prima al nome: <i>la pizza</i> → femminile singolare → <i>-a</i>.</li></ol>""")

    grammar_ref_it.pronomi_diretti_passato(b)

    # Page 5
    opts = [("il film", "la mostra"), ("il film", "la mostra"), ("i biglietti", "le foto"), ("i biglietti", "le foto"), ("il libro", "la pizza"), ("Davide", "Giulia")]
    ans = ["la mostra", "il film", "i biglietti", "le foto", "il libro", "Giulia"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho visto lo ieri.</td><td><b>L'ho visto ieri.</b></td><td>Il pronome va prima di <i>avere</i>.</td></tr>
<tr><td>La mostra? L'ho visto.</td><td><b>La mostra? L'ho vista.</b></td><td>Accordo: femminile.</td></tr>
<tr><td>I biglietti? Li ho comprato.</td><td><b>Li ho comprati.</b></td><td>Accordo: maschile plurale.</td></tr>
<tr><td>Ancora non ho visto il film.</td><td><b>Non ho ancora visto il film.</b></td><td><i>non… ancora</i>.</td></tr>
<tr><td>I biglietti compro io.</td><td><b>I biglietti li compro io.</b></td><td>Il pronome riprende la cosa.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["11.2", "11.3"])}
{sub("A", "Ascolta e ripeti. L'ho si pronuncia come una parola sola: [lò].", "2 min", "11.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S112)}</div>
{sub("B", "Di che cosa parla? Ascolta la vocale finale e scegli.", "2 min", "11.3")}
{twocol([f'<li value="{i+1}">{ch(list(o), a)}</li>' for i, (o, a) in enumerate(zip(opts, ans))], 4)}""",
    28, """<ol><li>Errori: <i>ancora non</i> esiste nel parlato di alcune regioni, ma la forma standard è <i>non… ancora</i>.</li>
<li>4B: l'unica differenza è la vocale finale del participio (<i>vista / visto, comprati, viste, finito, chiamata</i>): farla ripetere esagerando.</li></ol>""")

    # Page 6
    qa = [("Hai visto la mostra al MAMbo? (sì)", "Sì, l'ho vista."), ("Hai comprato i biglietti? (sì, ieri)", "Sì, li ho comprati ieri."),
          ("Hai finito il libro? (no)", "No, non l'ho ancora finito."), ("Avete invitato Davide e Giulia? (sì)", "Sì, li abbiamo invitati."),
          ("Hai preso le pizze? (sì, un momento fa)", "Sì, le ho appena prese.")]
    qal = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in qa)
    ga = [("È tardi! Il film è ___ cominciato.", "già"), ("Non ho ___ visto il nuovo museo.", "ancora"), ("Ciao! Sono ___ arrivata: dove sei?", "appena"),
          ("Hai ___ mangiato? È solo mezzogiorno!", "già")]
    gal = "".join(f"<li>{s.replace('___', A(a, 'min-width:16mm'))}</li>" for s, a in ga)
    wb = [("uscire", "l'uscita"), ("invitare", "l'invito"), ("prenotare", "la prenotazione"), ("ordinare", "l'ordine")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:24mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Rispondi con il pronome (lo, la, li, le) e il passato prossimo.", "4 min")}
<ol style="line-height:1.45">{qal}</ol>
{sub("B", "Già, ancora o appena?", "3 min")}
<ol style="line-height:1.7">{gal}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    25, """<ol><li>A: con <i>avete invitato Davide e Giulia</i>: un maschile e un femminile → <i>li</i> e <i>-i</i>.</li>
<li>B: <i>già</i> può voler dire anche "così presto!" (frase 4). C: <i>la prenotazione</i> → anche <i>prenotare un tavolo</i>, unità 22 dell'A1.</li></ol>""")

    # Page 7
    todo = ["prenotare il tavolo", "comprare i biglietti del concerto", "invitare Bruno e Chiara", "scegliere il film", "chiamare Davide", "fare la spesa per l'aperitivo"]
    tdl = "".join(f"<li>{t}</li>" for t in todo)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Organizziamo il sabato sera. L'insegnante ha una lista di cose da fare. Chiedi: Hai già…? L'insegnante risponde: Sì, l'ho già… / No, non l'ho ancora… Poi cambiate con la tua lista.", "6 min")}
<div class="two"><div class="box" style="margin-top:1mm"><h4>LA LISTA DELL'INSEGNANTE</h4><ol style="margin:0">{tdl}</ol></div>
<div class="box" style="margin-top:1mm"><h4>PAROLE UTILI</h4>Ti va di…? · Che ne dici di…? · Perché non…? · Volentieri! · Ottima idea! · L'ho già visto/a. · Non l'ho ancora… · Ci vediamo alle… · I biglietti li compro io. · Offro io!</div></div>
{sub("B", "Ti va di uscire? Invita l'insegnante a fare una cosa delle foto di pagina 1. L'insegnante risponde: l'ha già fatta o no? Trovate una cosa che non avete ancora fatto.", "6 min")}
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: l'insegnante decide le risposte (metà sì, metà no) e usa il pronome giusto: <i>il tavolo → l'ho prenotato; i biglietti → li ho comprati</i>.</li>
<li>B: alla fine lo studente scrive sulle righe il piano deciso: <i>Sabato andiamo… I biglietti li compro io.</i></li></ol>""")

    # Page 8
    pc = [("A2 · R1", "Ho ripassato le unità 01–09."), ("A2 · 11", "So proporre un'uscita e rispondere."),
          ("A2 · 11", "So usare lo, la, li, le con il passato prossimo (l'ho vista)."), ("A2 · 11", "So dire già, non… ancora, appena."),
          ("A2 · 11", "Sento la differenza tra l'ho visto e l'ho vista.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("La mostra? L'ho visto ieri.", "L'ho vista ieri."), ("Ho già comprato i biglietti.", "✓"),
          ("Ancora non ho finito il libro.", "Non ho ancora finito il libro."), ("Le pizze? Le ho ordinato.", "Le ho ordinate."),
          ("Ho visto lo al cinema.", "L'ho visto al cinema."), ("I biglietti li compro io.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio a un amico (50–75 parole).</b> Invita un amico a uscire questo fine settimana. Racconta che cosa hai già visto o fatto questo mese e che cosa non hai ancora fatto. Proponi un programma: <i>Ti va di…? I biglietti li compro io.</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il messaggio e l'insegnante risponde all'invito. Unità 12: <i>Volevo, ma…</i> (volevo / ho voluto; <i>ne</i> con le quantità).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("11.1", "L'ho già visto! (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("11.2", "Ascolta e ripeti")}
<p>{" · ".join(S112)}</p>
{sub("11.3", "Di che cosa parla?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S113))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 11 - Ti va di uscire")
