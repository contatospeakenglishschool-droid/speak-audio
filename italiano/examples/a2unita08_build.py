# Speak! Ponte A2 - Unità 08 "Mi scusi…" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
from mappa import mappa
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 08", audio_json=os.path.join(HERE, "audio_it-a2-unita-08.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'ufficio postale", "ufficio postale"), ("B", "la lettera", "lettera"), ("C", "il modulo", "modulo"), ("D", "il numero", "numero"),
          ("E", "la fila", "fila"), ("F", "i francobolli", "francobolli"), ("G", "le Due Torri", "Due Torri"), ("H", "le tagliatelle al ragù", "tagliatelle")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-08"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["08.1 Dialogo"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S082 = [x.split(": ", 1)[1] for x in _r["08.2 Ripeti con gentilezza"].split("\n")]
S083 = [x.split(": ", 1)[1] for x in _r["08.3 Tu o Lei"].split("\n")]


def _key(w):
    w = w.split(" ", 1)[1] if " " in w and not w.startswith("l'") else w
    return w.replace("l'", "").lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 08", "Mi scusi…", "Uffici, negozi e strade · <b>l'imperativo formale (Lei)</b>",
                       [("SAI FARE", "chiedere e dare istruzioni e indicazioni stradali in modo formale"),
                        ("LINGUA", "Mi scusi… · Firmi qui. · Vada dritto e giri a destra. · Non si preoccupi."),
                        ("PRONUNCIA", "la gentilezza nella voce · tu o Lei?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: all'ufficio postale", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Quando sei andato/a l'ultima volta all'ufficio postale? Che cosa hai fatto?</li><li>Fai spesso la fila? Dove?</li><li>Quando visiti una città nuova, chiedi indicazioni alle persone o usi il telefono?</li></ol>""",
    22, """<ol><li>A: <i>il numero</i> = il biglietto con il numero per la fila (<i>prendere il numero</i>). <i>Le Due Torri</i> sono il simbolo di Bologna.</li>
<li>B: ripasso del passato prossimo; lo studente può usare <i>bisogna</i> (unità 07).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: uffici e servizi</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>All'ufficio postale · Luca chiede la strada · il caffè dalla signora Rossi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>L'imperativo formale: forme, negativo, pronomi</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>-are → -i, -ere/-ire → -a · irregolari · pronomi prima · confronto con tu</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>La voce gentile · tu o Lei?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Imperativo + pronome · indicazioni sulla mappa · le parole degli uffici</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Allo sportello (gioco di ruolo) · Mi scusi, per andare a…?</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine febbraio. Júlia è tornata dal Brasile e deve rinnovare il permesso di soggiorno: all'ufficio postale l'impiegato le dà istruzioni (<i>mi dia il passaporto, firmi qui, non chiuda la busta, conservi la ricevuta</i>) e le ricorda di prendere il numero. Sabato Luca e Sara visitano Bologna: una signora spiega a Luca come arrivare a Santo Stefano e gli consiglia le tagliatelle al ragù, perché gli spaghetti alla bolognese a Bologna non esistono. La sera Júlia porta il caffè brasiliano alla signora Rossi, che vuole vedere le foto del Carnevale e le dà la posta: solo la bolletta della luce.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>In Brasile si usa poco il trattamento formale (<i>você</i> va bene quasi sempre), quindi lo studente usa il <i>tu</i> anche all'ufficio postale. La forma è simile al portoghese (<i>o senhor assine, vire à direita</i>), ma attenzione a <i>vadi, facci</i> (→ <b>vada, faccia</b>) e ai pronomi: <b>mi dia</b>, non <i>dia mi</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>In Italia il <b>permesso di soggiorno</b> si rinnova all'ufficio postale con il <b>kit</b> (una busta gialla); serve una <b>marca da bollo</b> da 16 euro. Negli uffici si prende il <b>numero</b> e si aspetta il proprio turno. A Bologna gli <i>spaghetti alla bolognese</i> non esistono: il ragù si mangia con le <b>tagliatelle</b>. Santo Stefano è un complesso di sette chiese, chiamato anche «Sette Chiese».</div>
<div class="box"><h4>AUDIO</h4>Traccia 08.1 Tre dialoghi (lento e naturale) · Traccia 08.2 Con gentilezza · Traccia 08.3 Tu o Lei?</div>""")

    # Page 2
    st = [("Che cosa deve fare Júlia all'ufficio postale?", "rinnovare il permesso di soggiorno"), ("Che cosa le chiede l'impiegato?", "il passaporto e la fotocopia; di firmare"),
          ("Che cosa non deve fare? Che cosa deve conservare?", "non deve chiudere la busta; la ricevuta")]
    stl = "".join(f"<li>{q} {A(a, 'min-width:58mm')}</li>" for q, a in st)
    vf = [("Santo Stefano è molto lontano.", "F"), ("Luca deve andare dritto fino alle Due Torri.", "V"), ("Alle Due Torri deve girare a sinistra.", "F"),
          ("La signora consiglia le tagliatelle al ragù.", "V"), ("Gli spaghetti alla bolognese sono tipici di Bologna.", "F")]
    vfl = "".join(f"<tr><td>{s}</td><td style='width:14mm;text-align:center'>{A(v, 'min-width:7mm')}</td></tr>" for s, v in vf)
    b.page(f"""{sec(2, "Ascolto: mi dia il passaporto", "10 min")}
<p>Júlia è all'ufficio postale, Luca chiede la strada a una signora e la signora Rossi aspetta il caffè brasiliano.</p>
{audiocard(["08.1 · SLOW", "08.1 · NATURAL"])}
{sub("A", "Dialogo 1. Ascolta e rispondi alle domande.", "3 min", "08.1 · SLOW")}
<ol style="line-height:1.55">{stl}</ol>
{sub("B", "Dialogo 2. Vero (V) o falso (F)?", "4 min", "08.1 · NATURAL")}
<table style="margin:0">{vfl}</table>
{sub("C", "Dialogo 3. Che cosa chiede di vedere la signora Rossi? Che cosa c'è nella posta?", "3 min")}
<div class="wline">{R("le foto del Carnevale · una lettera: la bolletta della luce")}</div>""",
    22, """<ol><li>A: versione <b>lenta</b>. Far notare <i>mi dia, firmi, non chiuda, conservi, prenda</i>: tutte con il <i>Lei</i>.</li>
<li>B: versione <b>naturale</b>. Correggere le frasi false. 3: alle Due Torri gira a <b>destra</b>.</li></ol>""")

    # Page 3
    rules = [("<i>Firmi, paghi, giri</i> (verbi in <b>-are</b>) finiscono in", ["-i", "-a"], "-i"),
             ("<i>Prenda, chiuda</i> (verbi in <b>-ere</b>) finiscono in", ["-a", "-i"], "-a"),
             ("Il negativo (<i>non chiuda, non ordini</i>) è", ["non + la forma di Lei", "non + l'infinito"], "non + la forma di Lei"),
             ("<i>Vada, faccia, mi dia</i> sono", ["irregolari", "regolari"], "irregolari"),
             ("Con il <b>Lei</b> i pronomi (<i>mi, si, la</i>) vanno", ["prima del verbo", "dopo il verbo, attaccati"], "prima del verbo"),
             ("Usiamo il <b>Lei</b> con", ["le persone che non conosciamo bene", "gli amici e la famiglia"], "le persone che non conosciamo bene")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Gira!", "Giri!"), ("Prendi!", "Prenda!"), ("Scusa!", "Scusi!"), ("Senti!", "Senta!"), ("Vieni!", "Venga!"), ("Va'!", "Vada!")]
    ccl = [f'<li value="{i+1}">{a} → {A(c, "min-width:22mm")}</li>' for i, (a, c) in enumerate(cc)]
    b.page(f"""{sec(3, "Grammatica: l'imperativo formale", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Firmi</b> qui e qui. · <b>Paghi</b> qui. · Lì <b>giri</b> a destra. · <b>Continui</b> dritto.<br>
2. <b>Prenda</b> il numero all'ingresso. · <b>Prenda</b> le tagliatelle al ragù!<br>
3. <b>Non chiuda</b> la busta! · <b>Non ordini</b> gli spaghetti alla bolognese!<br>
4. <b>Vada</b> dritto. · <b>Mi dia</b> il passaporto. · <b>Mi faccia</b> vedere le foto! · <b>Si sieda</b> qui. · <b>Non si preoccupi</b>.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Dal tu al Lei. Scrivi la forma formale.", "3 min")}
{twocol(ccl, 4)}
<div class="box sand"><h4>REGOLA</h4>Imperativo formale (<b>Lei</b>): <b>-are → -i</b> (<i>firmi, giri</i>) · <b>-ere / -ire → -a</b> (<i>prenda, senta</i>). Negativo: <b>non</b> + la stessa forma (<i>non chiuda</i>). Irregolari: <i>vada, faccia, dia, stia, dica, venga, esca, sia, abbia</i>. I pronomi vanno <b>prima</b>: <i>mi dia, si sieda, non si preoccupi</i>. Tutto: pagina 4.</div>""",
    20, """<ol><li>B: far notare lo «scambio» di vocali rispetto al <i>tu</i>: <i>gira → giri</i>, <i>prendi → prenda</i>.</li>
<li>C: 5–6: <i>venga, vada</i> vengono da <i>(io) vengo, vado</i>.</li></ol>""")

    grammar_ref_it.imperativo_formale(b)

    # Page 5
    ans3 = ["tu", "Lei", "Lei", "tu", "tu", "Lei"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Scusa, signora, dov'è la posta?</td><td><b>Scusi, signora, dov'è la posta?</b></td><td>Con chi non conosci: <i>Lei</i>.</td></tr>
<tr><td>Vadi dritto e giri a destra.</td><td><b>Vada dritto e giri a destra.</b></td><td>Irregolare: <i>vada</i>.</td></tr>
<tr><td>Dia mi il passaporto.</td><td><b>Mi dia il passaporto.</b></td><td>Il pronome va prima.</td></tr>
<tr><td>Signore, prende il numero!</td><td><b>Signore, prenda il numero!</b></td><td><i>prende</i> è il presente.</td></tr>
<tr><td>Non si preoccupa!</td><td><b>Non si preoccupi!</b></td><td>-are → -i.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["08.2", "08.3"])}
{sub("A", "La voce gentile. Ascolta e ripeti: voce morbida, sorriso, «per favore».", "2 min", "08.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S082)}</div>
{sub("B", "Tu o Lei? Ascolta e scegli.", "2 min", "08.3")}
{twocol([f'<li value="{i+1}">{ch(["tu", "Lei"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>prende</i> (presente, «lui prende») e <i>prenda</i> (imperativo, «Lei, prenda!») si confondono facilmente.</li>
<li>4B: le frasi sono 1 gira, 2 giri, 3 prenda, 4 prendi, 5 scusa / sai, 6 scusi / sa.</li></ol>""")

    # Page 6
    pr = [("Il modulo? (compilare qui)", "Lo compili qui."), ("La busta? (non chiudere)", "Non la chiuda."), ("La ricevuta? (conservare bene)", "La conservi bene."),
          ("(sedersi, prego)", "Si sieda, prego."), ("(non preoccuparsi)", "Non si preoccupi.")]
    prl = "".join(f"<li>{a} → {A(c, 'min-width:38mm')}</li>" for a, c in pr)
    dr = [("Giri a destra e prenda la prima a sinistra, via Verdi. Vada dritto: dopo via Dante, è sulla sinistra.", "la farmacia"),
          ("Giri a destra e prenda la seconda a sinistra, corso Garibaldi. Vada dritto fino in fondo: è sulla destra.", "il museo"),
          ("Giri a destra e vada sempre dritto fino a via Manzoni. Giri a sinistra: è subito sulla destra.", "la trattoria")]
    drl = "".join(f"<li>{a} {A(c, 'min-width:26mm')}</li>" for a, c in dr)
    wb = [("lo sportello", "dove l'impiegato serve i clienti"), ("la ricevuta", "il foglio che prova che hai pagato"), ("la marca da bollo", "una tassa: un francobollo speciale"),
          ("la fila", "le persone che aspettano una dietro l'altra"), ("firmare", "scrivere il proprio nome su un documento"), ("spedire", "mandare una lettera o un pacco"),
          ("la bolletta", "il conto della luce, del gas, dell'acqua"), ("l'impiegato", "la persona che lavora in un ufficio")]
    wbl = [f'<li value="{i+1}">{A(w, "min-width:24mm")}: {d}</li>' for i, (w, d) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "All'ufficio postale. Scrivi l'imperativo formale con il pronome.", "3 min")}
<ol style="line-height:1.7">{prl}</ol>
{sub("B", "Indicazioni. Parti da SEI QUI, leggi e scrivi dove arrivi.", "3 min")}
{mappa()}
<ol style="line-height:1.55;margin-top:1mm">{drl}</ol>
{sub("C", "Le parole degli uffici. Scrivi la parola giusta.", "3 min")}
<div class="bank">la bolletta · firmare · la fila · l'impiegato · la marca da bollo · la ricevuta · spedire · lo sportello</div>
{twocol(wbl, 5)}""",
    20, """<ol><li>A: ricordare il contrasto con il <i>tu</i>: <i>compilalo, non chiuderla, siediti</i>.</li>
<li>B: prima della lettura, ripassare <i>a destra, a sinistra, dritto, la prima / la seconda, fino a, all'angolo, in fondo</i>.</li></ol>""")

    # Page 7
    cards = [("1", "All'ufficio postale: vuoi spedire un pacco in Brasile."), ("2", "In farmacia: hai mal di gola e la tosse."),
             ("3", "In banca: vuoi aprire un conto corrente."), ("4", "In albergo: la doccia della tua camera non funziona.")]
    cl = "".join(f'<div class="msg" style="max-width:none;padding:1.5mm 3mm;font-size:9pt"><b>{n}.</b> {t}</div>' for n, t in cards)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Allo sportello. Scegli una situazione: tu sei il cliente, l'insegnante è l'impiegato e ti dà istruzioni con il Lei. Poi cambiate.", "6 min")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5mm;margin-top:1mm">{cl}</div>
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Buongiorno, mi scusi… · Vorrei… · Che cosa devo fare? · Prenda… · Compili… · Firmi… · Mi dia… · Torni domani. · Non si preoccupi. · Prego, si accomodi. · Grazie mille! · Si figuri!</div>
{sub("B", "Mi scusi, per andare a…? Usa la mappa della pagina 6. Chiedi la strada per il cinema, l'ospedale, la chiesa e l'albergo. L'insegnante ti dà le indicazioni. Poi cambiate.", "4 min")}
{sub("C", "Tu o Lei? L'insegnante dice una situazione (un amico, un poliziotto, tua nonna, un commesso…): tu dai un'istruzione con il tu o con il Lei.", "2 min")}""",
    22, """<ol><li>A: l'insegnante usa almeno tre imperativi formali per ogni situazione. Lo studente comincia con <i>Buongiorno, mi scusi…</i> e chiude con <i>Grazie mille!</i></li>
<li>B: tutti partono da SEI QUI. Cinema e ospedale sono in via Manzoni; la chiesa è vicino all'ufficio postale.</li></ol>""")

    # Page 8
    pc = [("A2 · 06", "So usare sapere, conoscere e ci vuole."), ("A2 · 07", "So parlare dei miei progetti con il futuro."),
          ("A2 · 08", "So dare istruzioni con il Lei: firmi, prenda, vada."), ("A2 · 08", "So chiedere e dare indicazioni stradali."),
          ("A2 · 08", "So usare i pronomi con il Lei: mi dia, si sieda, non si preoccupi.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Signora, firma qui, per favore.", "Signora, firmi qui…"), ("Mi scusi, sa dov'è la stazione?", "✓"),
          ("Vadi dritto per via Roma.", "Vada dritto…"), ("Dia mi la ricevuta, per favore.", "Mi dia la ricevuta…"),
          ("Non si preoccupi, signore!", "✓"), ("Professore, prende un caffè!", "Professore, prenda un caffè!")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Come arrivare a casa mia (50–75 parole).</b> Un nuovo collega deve venire a casa tua o al tuo lavoro. Scrivigli un'e-mail formale con le indicazioni: <i>Prenda l'autobus…, scenda…, giri…, vada dritto…</i></p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge l'e-mail; l'insegnante segue le indicazioni su una mappa vera. Unità 09: <i>Secondo me…</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("08.1", "Mi dia il passaporto (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("08.2", "Con gentilezza")}
<p>{" · ".join(S082)}</p>
{sub("08.3", "Tu o Lei?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S083))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 08 - Mi scusi")
