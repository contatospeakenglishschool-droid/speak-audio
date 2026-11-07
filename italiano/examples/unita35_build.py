# Speak! Essenziale A1 - Unità 35 "Arriva l'invito" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from invito import invito
setup(band="A1 · UNITÀ 35", audio_json=os.path.join(HERE, "audio_it-a1-unita-35.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'invito", "invito"), ("B", "la lettera", "lettera"), ("C", "gli sposi", "sposi"), ("D", "la chiesa", "chiesa"),
          ("E", "l'agenda", "agenda"), ("F", "le fedi", "fedi"), ("G", "la torta nuziale", "torta"), ("H", "la telefonata", "telefonata")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a1-unita-35"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["35.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S352 = [x.split(": ", 1)[1] for x in _r["35.2 Ripeti"].split("\n")]
S353 = [x.split(": ", 1)[1] for x in _r["35.3 Dettato"].split("\n")]


def _key(w):
    return (w.split("'")[-1] if "'" in w.split()[0] else w.split()[1]).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 35", "Arriva l'invito", "Il matrimonio di Luca e Sara · <b>le date · rispondere a un invito · i programmi</b>",
                       [("SAI FARE", "leggere un invito, dire la data, accettare o rifiutare un invito, parlare dei programmi"),
                        ("LINGUA", "il 26 settembre, il primo ottobre · Vengo volentieri! · Mi dispiace, non posso · Sabato partiamo alle 8.30"),
                        ("PRONUNCIA", "dettato delle date: ventuno, ventotto, trentuno")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: un matrimonio", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Sei andato/a a un matrimonio? Quando? Dove?</li><li>Che cosa c'è a un matrimonio in Brasile?</li><li>Quando è il tuo compleanno?</li></ol>""",
    22, """<ol><li>A: <i>gli sposi</i> = lo sposo e la sposa. <i>Le fedi</i> = gli anelli del matrimonio. <i>Sposarsi</i>: Luca <i>si sposa</i> (unità 28).</li>
<li>B: domanda 3: prima risposta libera; la regola delle date arriva a pagina 3.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: il matrimonio</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>L'invito · la telefonata a Luca · Bruno e il calcetto</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Le date · il presente per i programmi</td><td>3</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>Dettato delle date</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Rispondere agli inviti · i programmi</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Un invito al telefono (gioco di ruolo) · la mia agenda</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Metà settembre: la signora Rossi dà a Júlia una lettera da Firenze. È l'invito di Luca, il fratello di Marco, e di Sara: si sposano sabato 26 settembre alle 11 nella chiesa di San Miniato al Monte; dopo, pranzo e festa a Villa Le Rose, a Fiesole. Bisogna rispondere entro il 20. Júlia telefona subito a Luca: viene volentieri con Bruno. Partono sabato con il treno delle 8.30 e Marco li va a prendere alla stazione. Al pranzo in famiglia della domenica, invece, non possono andare: lunedì Bruno comincia le lezioni. Bruno all'inizio protesta (sabato ha il calcetto con Stefano!), vuole portare Chiara (ma l'invito è per due) e non ha niente di elegante. «Ci penso io», dice Júlia: continua nell'A2, unità 1.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Dia 26 de setembro</i> → <b>il 26 settembre</b> (senza <i>di</i>, con l'articolo); <i>dia primeiro</i> → <b>il primo</b>; <i>dia 8</i> → <b>l'8</b> (l'otto). <i>Vou viajar sábado</i> → <b>Sabato parto</b>: per i programmi basta il presente. Quando qualcuno ci invita rispondiamo <b>Sì, vengo!</b>, non <i>Sì, vado!</i> (= <i>Sim, eu vou!</i>). <i>Obrigado pelo convite</i> → <b>Grazie per l'invito</b>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia l'invito al matrimonio si chiama anche <b>partecipazione</b>. Gli sposi spesso fanno una <b>lista nozze</b> o chiedono un contributo per il <b>viaggio di nozze</b>. Alla fine gli ospiti ricevono la <b>bomboniera</b> con cinque <b>confetti</b> (salute, felicità, fertilità, ricchezza, lunga vita). Gli ospiti gridano «<i>Viva gli sposi!</i>» e non si veste di bianco: è il colore della sposa.</div>
<div class="box"><h4>AUDIO</h4>Traccia 35.1 Tre dialoghi (lento e naturale) · Traccia 35.2 Ascolta e ripeti · Traccia 35.3 Dettato delle date</div>""")

    # Page 2
    vf = [("Júlia e Bruno partono venerdì sera.", "F"), ("Marco va a prendere Júlia e Bruno alla stazione.", "V"),
          ("Domenica Júlia e Bruno vanno al pranzo in famiglia.", "F"), ("Lunedì Bruno comincia le lezioni.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Vengo volentieri!", "10 min")}
<p>La signora Rossi ha una lettera per Júlia. Viene da Firenze…</p>
{audiocard(["35.1 · SLOW", "35.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e completa l'invito.", "4 min", "35.1 · SLOW")}
{invito(T)}
{sub("B", "Dialogo 2. Vero (V) o falso (F)?", "3 min", "35.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Dialogo 3. Perché Bruno all'inizio non è contento? Che cosa chiede a Júlia?", "3 min")}
<div class="wline">{R("Sabato ha la partita di calcetto con Stefano. Chiede se può portare Chiara.")}</div>""",
    30, """<ol><li>A: versione <b>lenta</b>. Il 20 settembre è domenica: Júlia deve rispondere subito.</li>
<li>B: versione <b>naturale</b>. 1: partono sabato alle 8.30 (venerdì Júlia lavora fino alle 7). 2: Luca si sposa, quindi viene Marco. 3: non possono.</li>
<li>C: Chiara non può venire: l'invito è per due persone. <i>Ci penso io</i> = me ne occupo io (vedi A2, unità 1).</li></ol>""")

    # Page 3
    dt = [("la data", "<b>il</b> 26 settembre · <b>il</b> 20 · <b>l'</b>8 maggio · <b>l'</b>11 novembre"),
          ("il giorno 1", "<b>il primo</b> ottobre (non <i>il uno</i>)"),
          ("il giorno + la data", "sabato 26 settembre · Oggi è martedì 15 settembre."),
          ("domanda", "Che giorno è oggi? · Quando è il matrimonio? — <b>Il</b> 26.")]
    dtr = "".join(f"<tr><td><b>{a}</b></td><td>{x}</td></tr>" for a, x in dt)
    pg = [("Sabato <b>partiamo</b> alle 8.30.", "Marco <b>arriva</b> venerdì sera."), ("Lunedì Bruno <b>comincia</b> le lezioni.", "Domenica non <b>possiamo</b>.")]
    pgr = "".join(f"<tr><td>{a}</td><td>{x}</td></tr>" for a, x in pg)
    ck = [("Il matrimonio è ", ["il", "al"], "il", " 26 settembre."), ("Il compleanno di Bruno è ", ["il uno", "il primo"], "il primo", " marzo? No, il 14!"),
          ("", ["Il", "L'"], "L'", "8 marzo è la festa della donna."), ("Domani Júlia ", ["parte", "va a partire"], "parte", " per Firenze.")]
    ckl = "".join(f"<li>{a}{ch(o, r)}{z}</li>" for a, o, r, z in ck)
    b.page(f"""{sec(3, "Grammatica: le date e i programmi", "10 min")}
{sub("A", "Leggi la spiegazione.", "5 min")}
<table style="margin:.5mm 0 0">{dtr}</table>
<p style="margin:1.5mm 0 .5mm"><b>I programmi</b>: per il futuro vicino usiamo il <b>presente</b> con un'espressione di tempo (sabato, domani, lunedì, il 26…).</p>
<table style="margin:0">{pgr}</table>
<div class="box sand" style="margin-top:1.5mm"><h4>REGOLA</h4>La data: <b>il</b> + numero + mese, senza <i>di</i>: <i>il 26 settembre</i>. Con 8 e 11 diciamo <b>l'</b>: <i>l'8, l'11</i>. Il giorno 1 è <b>il primo</b>. I mesi si scrivono con la lettera minuscola. Per i programmi basta il presente: <i>Sabato parto.</i> Rispondere a un invito: <b>Sì, vengo volentieri! · Con piacere! · Mi dispiace, non posso. · Purtroppo lavoro.</b></div>
{sub("B", "Controlla. Scegli l'opzione corretta.", "2 min")}
<ol>{ckl}</ol>
{sub("C", "Scrivi la data in lettere.", "3 min")}
<ol><li>1/10: {A("il primo ottobre", "min-width:34mm")}</li><li>8/3: {A("l'otto marzo", "min-width:34mm")}</li><li>21/6: {A("il ventuno giugno", "min-width:34mm")}</li><li>25/12: {A("il venticinque dicembre", "min-width:34mm")}</li></ol>""",
    24, """<ol><li>A: far trovare nei dialoghi: <i>sabato ventisei settembre, entro il venti, partiamo sabato mattina, Marco arriva venerdì sera, lunedì Bruno comincia</i>.</li>
<li>B: il compleanno di Bruno è il 14 marzo (unità 30). C: in Italia la data si scrive giorno/mese, come in Brasile.</li></ol>""")

    # Page 4
    dl = [f'<li value="{i+1}">{A(w, "min-width:24mm")}</li>' for i, w in enumerate(["21/3", "1/5", "8/8", "31/12", "28/2", "19/7"])]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Il matrimonio è in 26 di settembre.</td><td><b>Il matrimonio è il 26 settembre.</b></td><td><i>il</i> + data, senza <i>di</i>.</td></tr>
<tr><td>il uno ottobre</td><td><b>il primo ottobre</b></td><td>Il giorno 1 è <i>il primo</i>.</td></tr>
<tr><td>il otto maggio</td><td><b>l'otto maggio</b></td><td>8 e 11: <i>l'</i>.</td></tr>
<tr><td>Sabato vado a partire.</td><td><b>Sabato parto.</b></td><td>Per i programmi: presente.</td></tr>
<tr><td>Vieni alla festa? — Sì, vado!</td><td><b>Sì, vengo!</b></td><td>Rispondo a chi mi invita: <i>venire</i>.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["35.2", "35.3"])}
{sub("A", "Ascolta e ripeti. Attenzione: venti + uno = ventuno, venti + otto = ventotto.", "2 min", "35.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S352)}</div>
{sub("B", "Dettato. Ascolta e scrivi la data in numeri (giorno/mese).", "3 min", "35.3")}
{twocol(dl, 4)}""",
    34, """<ol><li>Errori: l'ultimo è tipico: in portoghese <i>Sim, eu vou!</i>; in italiano chi è invitato risponde dal punto di vista di chi invita: <i>vengo</i>.</li>
<li>4: davanti a <i>uno</i> e <i>otto</i> i numeri perdono la vocale: <i>ventuno, ventotto, trentuno, trentotto</i>.</li></ol>""")

    # Page 5
    iv = [("Vieni alla mia festa sabato sera? (✓)", "Sì, vengo volentieri! Grazie!"), ("Venite a cena da noi domenica? (✗ lavoro)", "Mi dispiace, non possiamo: lavoriamo."),
          ("Vuoi venire al cinema stasera? (✓)", "Con piacere! A che ora?"), ("Vieni al mio matrimonio il 3 ottobre? (✗ Brasile)", "Purtroppo non posso: il 3 sono in Brasile.")]
    ivl = "".join(f'<li>{q}<div class="wline">{R(a)}</div></li>' for q, a in iv)
    pr = [("Sabato Júlia e Bruno ___ (partire) alle otto e mezza.", "partono"), ("Il treno ___ (arrivare) alle nove e mezza.", "arriva"),
          ("Marco ___ (venire) venerdì sera.", "viene"), ("Domenica noi non ___ (potere).", "possiamo"),
          ("Lunedì Bruno ___ (cominciare) le lezioni.", "comincia"), ("E tu, che cosa ___ (fare) sabato?", "fai")]
    prl = "".join(f"<li>{s.replace('___', A(a, 'min-width:22mm'))}</li>" for s, a in pr)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Rispondi agli inviti: ✓ = accetti, ✗ = non puoi (e spieghi perché).", "4 min")}
<ol style="line-height:1.5">{ivl}</ol>
{sub("B", "I programmi del fine settimana. Completa con il presente.", "4 min")}
<ol style="line-height:1.75">{prl}</ol>""",
    22, """<ol><li>A: risposte libere; accettare anche <i>Certo!</i>, <i>Grazie per l'invito!</i>, <i>Peccato, non posso</i>.</li>
<li>B: <i>venire</i> e <i>potere</i> sono irregolari: <i>viene, possiamo</i>.</li></ol>""")

    # Page 6
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Un invito al telefono. L'insegnante ti invita (una festa, una cena, un matrimonio…). Chiedi la data, l'ora e il posto. Poi accetta o rifiuta con gentilezza. Poi cambiate.", "5 min")}
<div class="box" style="font-size:9pt"><h4>PAROLE UTILI</h4>Pronto? · Ti invito a… · Quando è? · A che ora? · Dove? · Sì, vengo volentieri! · Con piacere! · Grazie per l'invito! · Mi dispiace, non posso. · Purtroppo… · Peccato! · Ci vediamo il…!</div>
{sub("B", "La mia agenda. Scrivi tre programmi per il prossimo mese, con la data. Poi racconta: Il 12 ottobre vado a… ", "4 min")}
<div class="wline"></div><div class="wline"></div><div class="wline"></div>
{sub("C", "Le date importanti. Quando è il tuo compleanno? E il compleanno di tua madre? Quando è Natale? E il Carnevale in Brasile?", "3 min")}""",
    24, """<ol><li>A: l'insegnante sceglie la data e lo studente la ripete per controllare: <i>Il 21? Va bene!</i></li>
<li>C: Natale è il 25 dicembre; il Carnevale cambia ogni anno (febbraio o marzo).</li></ol>""")

    # Page 7
    pc = [("Unità 34", "So usare questo e quello e i colori."), ("Unità 35", "So dire e scrivere le date."),
          ("Unità 35", "So accettare o rifiutare un invito."), ("Unità 35", "So parlare dei miei programmi con il presente."),
          ("Unità 35", "So capire le date quando le ascolto.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Il mio compleanno è in 5 di aprile.", "Il mio compleanno è il 5 aprile."), ("La festa è il uno giugno.", "La festa è il primo giugno."),
          ("Vieni a cena? — Sì, vado!", "Sì, vengo!"), ("Domenica vado a visitare mia nonna.", "✓ corretta"),
          ("Il matrimonio è il undici luglio.", "Il matrimonio è l'undici luglio."), ("Grazie per invitare!", "Grazie per l'invito!")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> Una frase è corretta.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Rispondi a Luca.</b> Scrivi un messaggio a Luca: grazie per l'invito, vieni o no, quando arrivi a Firenze (giorno e ora).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: <b>Ripasso 4</b> (unità 28–35), l'ultimo dell'A1. Poi si comincia l'A2 Ponte: il matrimonio di Luca e Sara continua nell'unità 1.</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("35.1", "Arriva l'invito (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("35.2", "Ascolta e ripeti")}
<p>{" · ".join(S352)}</p>
{sub("35.3", "Dettato delle date")}
<p>{" · ".join(S353)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 35 - Arriva l'invito")
