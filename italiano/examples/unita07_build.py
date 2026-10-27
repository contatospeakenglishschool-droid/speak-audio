# Speak! Essenziale A1 - Unità 07 "In città" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from mappa import themap
setup(band="A1 · UNITÀ 07", audio_json=os.path.join(HERE, "audio_it-a1-unita-07.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la farmacia", "farmacia"), ("B", "il bancomat", "bancomat"), ("C", "l'ufficio postale", "ufficio postale"), ("D", "il supermercato", "supermercato"),
          ("E", "la chiesa", "chiesa"), ("F", "la piazza", "piazza"), ("G", "il forno", "forno"), ("H", "la stazione", "stazione")]

SCRIPT = [("Narratore", "Dialogo uno. Sabato mattina, davanti a casa."), ("Júlia", "Signora Rossi, scusi, c'è una farmacia qui vicino?"),
          ("Signora Rossi", "Sì, c'è una farmacia in via Santo Stefano, nella piazza piccola."), ("Júlia", "E un supermercato?"),
          ("Signora Rossi", "Ci sono due supermercati in via Castiglione. E nel centro ci sono molti negozi."), ("Júlia", "E il bancomat?"),
          ("Signora Rossi", "Il bancomat è nella banca, accanto al bar di Giulia."), ("Júlia", "Grazie mille, signora!"),
          ("Narratore", "Dialogo due. In centro."), ("Júlia", "Scusi, dov'è l'ufficio postale?"),
          ("Uomo", "Allora… va dritto, prende la seconda strada a destra, e l'ufficio postale è lì, di fronte alla chiesa."), ("Júlia", "Può ripetere, per favore?"),
          ("Uomo", "Certo. Dritto, la seconda a destra, di fronte alla chiesa."), ("Júlia", "È lontano?"), ("Uomo", "No, no. Cinque minuti a piedi."),
          ("Narratore", "Dialogo tre. Al telefono."), ("Marco", "Pronto, Júlia? Dove sei?"), ("Júlia", "Sono in piazza Maggiore. Posso arrivare allo studio alle tre?"),
          ("Marco", "Sì, certo. Ma puoi comprare il pane? C'è un forno nella prima strada a sinistra."), ("Júlia", "Va bene. Il pane e poi lo studio!")]
S072 = ["Roma", "ristorante", "ripetere", "strada", "destra", "terzo", "ferrovia", "Può ripetere?"]
S073 = ["Scusi, c'è una farmacia qui vicino?", "Scusi, dov'è la stazione?", "Ci sono negozi qui?", "Può ripetere, per favore?", "È lontano?", "Grazie mille!"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 07", "In città", "I luoghi della città · <b>chiedere e dare indicazioni</b>",
                       [("SAI FARE", "chiedere dov'è un posto e capire le indicazioni"), ("LINGUA", "c'è / ci sono · dov'è? · nel, nella… · posso, puoi, può · primo, secondo"),
                        ("PRONUNCIA", "la R italiana · domande gentili per strada")])
    words = ["il bancomat", "il forno", "il supermercato", "l'ufficio postale", "la chiesa", "la farmacia", "la piazza", "la stazione"]
    qs = [("non stai bene", "la farmacia"), ("vuoi spedire una lettera", "l'ufficio postale"), ("hai bisogno di soldi", "il bancomat"),
          ("prendi il treno", "la stazione"), ("vuoi comprare il pane", "il forno"), ("vuoi fare la spesa", "il supermercato")]
    ql = [f'<li value="{i+1}">… {q}? {R("→ " + a) if T else ""}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: i luoghi della città", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi il luogo sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Dove vai se…", "4 min")}
{twocol(ql, 4)}""",
    26, """<ol><li>A: <b>il forno</b> = negozio del pane (a Bologna; altrove anche <i>la panetteria</i>). <b>Il bancomat</b> = la macchina per prendere i soldi. Foto F: piazza Maggiore, a Bologna.</li>
<li>B: rispondere con l'articolo. Chiedere: <i>C'è una farmacia vicino a casa tua?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 luoghi della città con foto</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il sabato di Júlia in centro: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td><i>c'è / ci sono</i> · <i>dov'è?</i> · <i>in</i> + articolo · <i>potere</i> · indicazioni · ordinali</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>La R italiana · domande gentili</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>La mappa: completare i dialoghi</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Gioco di ruolo con la mappa · la tua città</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 04–07) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Sabato mattina Júlia chiede alla signora Rossi dove sono la farmacia, i supermercati e il bancomat. In centro chiede a un signore la strada per l'ufficio postale e gli chiede di ripetere. Poi Marco la chiama: può arrivare allo studio alle tre, ma prima deve comprare il pane nel forno della prima strada a sinistra.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Tiene una farmacia qui?</i> ✗ → <b>C'è una farmacia qui?</b> <i>C'è due supermercati</i> ✗ → <b>Ci sono due supermercati</b>. <i>In la piazza</i> ✗ → <b>nella piazza</b>. <i>La primo strada</i> ✗ → <b>la prima strada</b>. E la <b>R</b>: in italiano non è mai come la R di «Rio» in portoghese.</div>
<div class="box"><h4>AUDIO</h4>Traccia 07.1 Tre dialoghi (lento e naturale) · Traccia 07.2 La R · Traccia 07.3 Domande per strada</div>""")

    # Page 2
    pl = [("1", "la farmacia", "via Santo Stefano"), ("1", "due supermercati", "via Castiglione"), ("1", "il bancomat", "accanto al bar di Giulia"),
          ("2", "l'ufficio postale", "seconda a destra, di fronte alla chiesa"), ("3", "il forno", "prima strada a sinistra")]
    pr = "".join(f"<tr><td style='width:18mm;text-align:center'>{n}</td><td style='width:42mm'><b>{p}</b></td><td>{A(w, 'min-width:70mm')}</td></tr>" for n, p, w in pl)
    gp = [("", "C'è", "una farmacia qui vicino?"), ("", "Ci sono", "due supermercati in via Castiglione."), ("Il bancomat è", "nella", "banca."),
          ("", "Può", "ripetere, per favore?"), ("", "Posso", "arrivare allo studio alle tre?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: sabato in centro", "10 min")}
<p>È sabato. Júlia ha bisogno di alcune cose e non conosce ancora bene Bologna.</p>
{audiocard(["07.1 · SLOW", "07.1 · NATURAL"])}
{sub("A", "Ascolta. Dov'è? Scrivi il posto.", "4 min", "07.1 · SLOW")}
<table style="margin:0"><tr><th>Dialogo</th><th>Che cosa?</th><th>Dove?</th></tr>{pr}</table>
{sub("B", "Ascolta di nuovo e completa.", "4 min", "07.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Che cosa deve fare Júlia prima di andare allo studio?", "2 min")}
<div class="wline">{R("Deve comprare il pane nel forno della prima strada a sinistra.")}</div>""",
    28, """<ol><li>A: versione <b>lenta</b>. Accettare risposte brevi (<i>via Castiglione</i>).</li>
<li>B: versione <b>naturale</b>. 3: <i>nella</i> = <i>in + la</i> (pagina 3). <i>Pronto?</i> = si dice quando si risponde al telefono.</li>
<li>C: <i>deve</i> = verbo <i>dovere</i>: solo da capire (unità 9).</li></ol>""")

    # Page 3
    ci = [("C'è + singolare", "C'è una farmacia qui vicino?"), ("Ci sono + plurale", "Ci sono due supermercati."), ("Dov'è + il / la…", "Dov'è la stazione?")]
    pa = [("il", "nel", "nel centro"), ("lo", "nello", "nello studio"), ("la", "nella", "nella piazza"), ("l'", "nell'", "nell'ufficio"), ("i", "nei", "nei negozi"), ("le", "nelle", "nelle strade")]
    po = [("io", "posso"), ("tu", "puoi"), ("lui / lei / Lei", "può")]
    di = [("↑", "Va dritto. / Vai dritto."), ("←", "Gira a sinistra. / Giri a sinistra."), ("→", "Gira a destra. / Giri a destra."), ("⇢", "Prende la prima / la seconda strada.")]
    rules = [("", "Ci sono due banche.", "C'è due banche."), ("", "nella piazza", "in la piazza"), ("", "la seconda strada", "la secondo strada"), ("Signore, ", "può ripetere?", "puoi ripetere?")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s}<b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    tc = "".join(f"<tr><td class='small'><b>{a}</b></td><td>{e}</td></tr>" for a, e in ci)
    tp = "".join(f"<tr><td>in + {a}</td><td><b>{x}</b></td><td class='small'>{e}</td></tr>" for a, x, e in pa)
    to = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in po)
    td = "".join(f'<tr><td style="width:8mm;text-align:center;font-size:12pt;color:{TEAL}">{a}</td><td>{t}</td></tr>' for a, t in di)
    b.page(f"""{sec(3, "Grammatica: c'è, ci sono · nel, nella · potere", "10 min")}
<div class="two"><div>{sub("A", "C'è o ci sono?", "2 min")}<table style="margin:0">{tc}</table>
{sub("B", "Indicazioni (tu / Lei).", "2 min")}<table style="margin:0">{td}</table></div>
<div>{sub("C", "in + articolo", "2 min")}<table style="margin:0">{tp}</table>
<table style="margin-top:2mm"><tr><th colspan="2">potere</th></tr>{to}</table></div></div>
{sub("D", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>DOVE?</h4><b>accanto a</b> · <b>di fronte a</b> · <b>vicino a</b> · <b>tra</b> … <b>e</b> … · <b>lontano</b> · <b>a piedi</b>. Ordinali: <b>primo, secondo, terzo, quarto, quinto</b> — come un aggettivo: <i>la prima strada, il secondo semaforo</i>.</div>""",
    18, """<ol><li>B: <i>Va / Gira</i> (Lei, formale) e <i>Vai / Giri</i> (tu): sono forme del presente, molto usate per dare indicazioni.</li>
<li>C: stessa logica degli articoli. <i>accanto al bar = a + il</i>: le altre preposizioni articolate arrivano nell'unità 8.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Tiene una farmacia qui?</td><td><b>C'è una farmacia qui?</b></td><td>Esistere = <i>c'è</i>.</td></tr>
<tr><td>C'è due supermercati.</td><td><b>Ci sono due supermercati.</b></td><td>Plurale = <i>ci sono</i>.</td></tr>
<tr><td>Il bancomat è in la banca.</td><td><b>…è nella banca.</b></td><td><i>in + la = nella</i>.</td></tr>
<tr><td>La primo strada a destra.</td><td><b>La prima strada a destra.</b></td><td>Strada è femminile.</td></tr>
<tr><td>Dove è la stazione?</td><td><b>Dov'è la stazione?</b></td><td>Si dice con l'apostrofo.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["07.2", "07.3"])}
{sub("A", "La R italiana. Ascolta e ripeti: la punta della lingua vibra dietro i denti.", "2 min", "07.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S072)}</div>
{sub("B", "Domande gentili per strada. Ascolta e ripeti. Comincia con Scusi.", "3 min", "07.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S073)}</div>""",
    38, """<ol><li>Errori: <i>tiene</i> è un errore tipico di chi parla portoghese o spagnolo. In italiano <i>tenere</i> non indica che una cosa esiste.</li>
<li>4A: la R iniziale di <i>Roma, ristorante</i> e la RR di <i>ferrovia</i> si fanno con la lingua, mai con la gola. Esercizio: ripetere <i>tre, tre, tre</i> e poi <i>terzo, strada</i>.</li>
<li>4B: <i>Scusi</i> (Lei) per le persone che non conosci; <i>scusa</i> (tu) con gli amici.</li></ol>""")

    # Page 5
    gw = ["c'è", "dritto", "sinistra", "accanto", "lontano", "prima", "seconda", "destra", "sono", "di fronte"]
    def g(i): return f"({i+1}) {A(gw[i], 'min-width:18mm')}"
    dls = [("1 · La banca", [("A", f"Scusi, {g(0)} una banca qui vicino?"), ("B", f"Sì. Va {g(1)}. La banca è a {g(2)}, tra il forno e il bar.")]),
           ("2 · La farmacia", [("A", "Scusi, dov'è la farmacia?"), ("B", f"Va dritto e attraversa via Verdi. La farmacia è a sinistra, {g(3)} alla chiesa."), ("A", f"È {g(4)}?"), ("B", "No, due minuti a piedi.")]),
           ("3 · La stazione", [("A", "Scusi, come arrivo alla stazione?"), ("B", f"Va dritto. Passa la {g(5)} strada, via Verdi, e la {g(6)}, via Dante. La stazione è a {g(7)}.")]),
           ("4 · Il supermercato", [("A", f"Ci {g(8)} negozi qui?"), ("B", f"Sì, c'è un supermercato a destra, {g(9)} alla farmacia.")])]
    dh = "".join(f'<p style="margin:1.2mm 0 .3mm;font-weight:800;color:{TEAL}">{t}</p>' + "".join(f"<div style='line-height:1.9'><b>{n}:</b> {x}</div>" for n, x in rows) for t, rows in dls)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Guarda la mappa. Tu sei alla X. Completa i dialoghi con le parole.", "8 min")}
<div style="margin:1mm 0 2mm">{themap(64)}</div>
<div class="bank">accanto · c'è · destra · di fronte · dritto · lontano · prima · seconda · sinistra · sono</div>
<div class="msg" style="max-width:none;padding:1mm 4mm 2mm">{dh}</div>""",
    18, """<p>Leggere i dialoghi insieme e seguire ogni percorso con il dito. Si cammina verso destra (est): sopra via Roma = <i>a sinistra</i>.</p>""")

    # Page 6
    tasks = ["l'albergo", "il museo", "l'ufficio postale", "la piazza", "il bar", "la chiesa"]
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Gioco di ruolo. Tu sei alla X. Chiedi all'insegnante la strada per un posto. Poi scambiate i ruoli.", "7 min")}
<div style="margin:1mm 0 2mm">{themap(64)}</div>
<div class="bank">{" &nbsp;·&nbsp; ".join(tasks)}</div>
<div class="bank" style="background:#fff">Scusi, c'è un… qui vicino? · Dov'è…? · È lontano? · Può ripetere, per favore? · Va dritto · Giri a destra / a sinistra · accanto a · di fronte a</div>
{sub("B", "La tua città. Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>C'è una farmacia vicino a casa tua? Dov'è?</li><li>Che cosa c'è nel centro della tua città?</li><li>Quando non trovi una strada, chiedi alle persone o usi il telefono?</li></ol>""",
    27, """<ol><li>A: prima lo studente chiede e l'insegnante dà le indicazioni a velocità naturale (così lo studente usa <i>Può ripetere?</i>). Poi lo studente dà le indicazioni. Soluzioni: l'albergo è a destra prima di via Verdi; il museo è a sinistra dopo via Dante; l'ufficio postale è a destra, subito.</li>
<li>B: correggere <i>c'è / ci sono</i> e <i>nel / nella</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 05", "So dire l'ora e parlare della mia giornata."), ("Unità 06", "So dire che cosa mi piace."),
          ("Unità 07", "So chiedere se c'è un posto e dov'è."), ("Unità 07", "So capire e dare indicazioni semplici."), ("Unità 07", "So usare c'è / ci sono e nel / nella.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Tiene un bancomat qui vicino?", "C'è un bancomat qui vicino?"), ("C'è tre chiese in piazza.", "Ci sono tre chiese in piazza."), ("Il museo è in il centro.", "Il museo è nel centro."),
          ("Prende la primo strada.", "Prende la prima strada."), ("Dove è la farmacia?", "Dov'è la farmacia?"), ("Signora, puoi ripetere?", "Signora, può ripetere?")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Da casa tua.</b> Scrivi le indicazioni da casa tua a un posto vicino (forno, farmacia, supermercato…) in 3–4 frasi.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi lo studente legge le indicazioni e l'insegnante «cammina» con il dito: <i>Allora, vado dritto… e poi?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("07.1", "Sabato in centro (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("07.2", "La R")}
<p>{" · ".join(S072)}</p>
{sub("07.3", "Domande per strada")}
<p>{" ".join(S073)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 07 - In città")
