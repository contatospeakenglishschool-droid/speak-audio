# Speak! Progresso B1 - Unità 08 "Mica male!" (tutto in italiano) - formato B1 (2026-11-16), shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Progresso"
setup(band="B1 · UNITÀ 08", audio_json=os.path.join(HERE, "audio_it-b1-unita-08.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-b1-unita-08"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["08.1 Mica male!"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S082 = [x.split(": ", 1)[1] for x in _r["08.2 Ripeti"].split("\n")]


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
    cover = cover_html(T, "LIVELLO B1 · UNITÀ 08", "Mica male!", "L'italiano parlato · <b>la negazione rafforzata</b>",
                       [("SAI FARE", "dire di no con forza, dare giudizi informali, reagire con le parole del parlato"),
                        ("LINGUA", "Non è mica piccola. · Non è affatto il mio stile. · Non c'è neanche un piatto. · Neanch'io!"),
                        ("PRONUNCIA", "l'accento sulla parola che nega")])
    kw = [("una persona che si presenta per un posto o una stanza", "un candidato"), ("dove si lavano i piatti in cucina", "il lavandino"),
          ("il sistema che scalda la casa d'inverno", "il riscaldamento"), ("il pulsante che suona alla porta", "il campanello"),
          ("la persona che abita vicino a te", "il vicino"), ("il ristorante economico dell'università", "la mensa"),
          ("il contrario di allegro e scherzoso", "serio"), ("fare un sorriso", "sorridere")]
    kwl = [f'<li value="{i+1}">{d} {A(w, "min-width:22mm")}</li>' for i, (d, w) in enumerate(kw)]
    b.page(f"""{sec(1, "Riscaldamento: la lingua di tutti i giorni", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start">{img('A', 58, 38)}<div style="flex:1">
{sub("A", "Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.45;font-size:8.9pt;margin:0"><li>Guarda la foto. Che registro usano queste amiche: formale o informale?</li><li>Quali parole usi solo con gli amici, in portoghese?</li><li>Quando visiti una casa, che cosa controlli per prima cosa?</li></ol></div></div>
{sub("B", "Parole chiave. Scrivi le parole del riquadro accanto alle definizioni.", "4 min")}
<div class="bank">il campanello · un candidato · il lavandino · la mensa · il riscaldamento · serio · sorridere · il vicino</div>
<div style="font-size:8.6pt">{twocol(kwl, 5)}</div>
{sub("C", "Che cosa non sopporteresti mai in un coinquilino?", "1 min")}""",
    25, """<ol><li>A: far notare che in portoghese il parlato ha le sue negazioni (<i>não é pequeno, não</i>; <i>nem eu</i>): oggi vediamo quelle dell'italiano.</li>
<li>B: <i>il lavandino</i> = <i>a pia</i>; <i>il campanello</i> = <i>a campainha</i>; <i>la mensa</i> = <i>o bandejão, o restaurante universitário</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 60 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>Conversazione sul registro informale · parole chiave</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>12 min</td><td>Mica male! Il primo candidato per la stanza di Bruno</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>8 min</td><td>La negazione rafforzata: mica, affatto, per niente, neanche, nemmeno, neppure</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>La negazione rafforzata (da studiare a casa)</td><td>4</td></tr>
<tr><td>4 Laboratorio di lessico + pronuncia</td><td>8 min</td><td>Le parole del parlato · falsi amici · l'accento sulla negazione</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il messaggio di Tommaso · anch'io o neanch'io?</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La mia casa · gioco di ruolo: un candidato pignolo</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>4 min</td><td>Autovalutazione · i miei errori · compiti scritti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Sabato 6 febbraio, pomeriggio, in via Zamboni. Bruno ha pulito tutto («non c'è neanche un piatto nel lavandino») e Júlia è venuta ad aiutarlo. Arriva il primo candidato, Tommaso, studente di Medicina: la stanza «non è mica piccola», il tappeto blu di Paolo «non è affatto il suo stile», i vicini non fanno rumore (la signora del piano di sopra ha novant'anni). Tommaso non fuma e non fa feste; Bruno dice che neanche lui ne fa, «quasi mai» — Júlia: «Mica tanto!». Tommaso non sa neanche cucinare: mangia alla mensa; Bruno gli insegnerà il feijão. Per Bruno è perfetto; per Júlia è un po' troppo serio. Lunedì Bruno gli scrive.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Calco di <i>eu também não</i>: lo studente dice <i>anche io no</i> invece di <i>neanch'io</i>, e <i>anche a me no</i> invece di <i>neanche a me</i>. Falsi amici forti: <i>affatto</i> (= per niente) ≠ <i>de fato</i> (= <i>infatti</i>); <i>uffa</i> (noia, fastidio) ≠ <i>ufa</i> (sollievo). La doppia negazione brasiliana (<i>não é pequeno não</i>) aiuta a capire <i>non è mica piccolo</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4><i>Mica</i> viene dal latino <i>mica</i> = briciola: «non è mica» = «non è neanche una briciola». È molto usato al Nord e al Centro, meno al Sud. Le mense universitarie, gestite dalle aziende regionali per il diritto allo studio, offrono un pasto completo a pochi euro. <i>Boh</i>, <i>mah</i> e <i>uffa</i> si usano in tutta Italia, ma solo nel registro informale.</div>
<div class="box"><h4>AUDIO</h4>Traccia 08.1 Mica male! (prima naturale, poi lenta) · Traccia 08.2 Ripeti: la negazione rafforzata</div>""")

    # Pagina 2 - Ascolto
    gi = [("la pulizia della cucina", True), ("un esame di Tommaso", False), ("la stanza", True), ("i vicini", True), ("una festa di compleanno", False), ("chi lava i piatti", True)]
    gil = " &nbsp; ".join(f"☐ {R('<b>✓</b> ') if (T and a) else ''}{t}" for t, a in gi)
    vf = [("Quando arriva Tommaso, la cucina è sporca.", "F"), ("A Tommaso la stanza sembra piccola.", "F"),
          ("A Tommaso piace molto il tappeto blu.", "F"), ("La vicina del piano di sopra fa molto rumore.", "F"),
          ("Tommaso mangia quasi sempre alla mensa.", "V"), ("Secondo Júlia, Tommaso è un po' troppo serio.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: Mica male!", "12 min")}
<div style="display:flex;gap:3mm;align-items:center"><div style="flex:1">{audiocard(["08.1 · NATURAL", "08.1 · SLOW"])}</div>{img('B', 36, 21)}</div>
{sub("A", "Sabato pomeriggio, a casa di Bruno. Ascolta la versione naturale. Di che cosa parlano? Segna quattro argomenti.", "3 min", "08.1 · NATURAL")}
<p style="margin:.5mm 0;font-size:8.8pt;line-height:1.7">{gil}</p>
{sub("B", "Ascolta di nuovo. Vero (V) o falso (F)? Correggi le frasi false.", "5 min")}
<table style="margin:0;font-size:8.8pt">{vfr}</table>
{sub("C", "Pensaci. Parla con l'insegnante.", "4 min")}
<ol style="line-height:1.45;font-size:8.8pt;margin:0"><li>Júlia dice «Mica tanto!». Che cosa pensa delle feste di Bruno? {R("Che Bruno ne fa più di quanto dice.") if T else ""}</li>
<li>Tu prenderesti Tommaso come coinquilino? Perché? {R("Risposta libera.") if T else ""}</li></ol>
<div class="box sand" style="margin-top:1.5mm"><h4>NOTA: ESPRESSIONI UTILI</h4><i>Mica male! · Ah, però. · Mica tanto! · Per niente. · Dai… · Una settimana per uno. · Che te ne pare? · Va benissimo.</i></div>""",
    29, """<ol><li>A: prima la versione <b>naturale</b>, senza testo. Argomenti corretti: pulizia della cucina, stanza, vicini, chi lava i piatti.</li>
<li>B: 1 non c'è neanche un piatto · 2 non è mica piccola · 3 non è affatto il suo stile · 4 non sente nemmeno il campanello.</li>
<li>Espressioni: <i>Ah, però</i> = sorpresa positiva (<i>olha só!</i>); <i>Che te ne pare?</i> = <i>o que você achou?</i></li></ol>""")

    # Pagina 3 - Grammatica
    ex = [("Mica male!", "abbastanza bene, una bella sorpresa"), ("Non è <u>mica</u> piccola.", "non è piccola (e io pensavo di sì)"),
          ("Non è <u>affatto</u> il mio stile.", "non è assolutamente il mio stile"), ("Non c'è <u>neanche</u> un piatto.", "zero piatti"),
          ("<u>Neanch'io</u> faccio feste.", "anch'io non faccio feste")]
    exl = "".join(f"<li>{s} {A(a, 'min-width:58mm')}</li>" for s, a in ex)
    bank3 = "abbastanza bene, una bella sorpresa · anch'io non faccio feste · non è assolutamente il mio stile · non è piccola (e io pensavo di sì) · zero piatti"
    rules = [("Se <i>mica</i> è dopo il verbo, prima del verbo serve", ["non", "niente"], "non", ": <i>non è mica piccola</i>."),
             ("Se <i>neanche</i> è all'inizio della frase,", ["non si usa", "si usa"], "non si usa", "<i>non</i>: <i>neanche tu sorridevi</i>."),
             ("<i>Eu também não</i> in italiano si dice", ["Neanch'io", "Anch'io no"], "Neanch'io", "."),
             ("<i>Affatto</i> vuol dire", ["per niente", "infatti"], "per niente", ".")]
    rl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace(" :", ":").replace(" .", ".") for a, o, r, z in rules)
    cc = [("", ["Neanche", "Non neanche"], "Neanche", "Marco lo sapeva."),
          ("Non mi piace il tappeto. —", ["Neanche a me", "Anche a me no"], "Neanche a me", "."),
          ("Non ho", ["nemmeno", "neanche non"], "nemmeno", "un euro in tasca.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>".replace("<li> ", "<li>").replace(" .", ".") for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: la negazione rafforzata", "8 min")}
{sub("A", "Frasi dal dialogo. Che cosa vogliono dire? Usa le parole del riquadro.", "3 min")}
<div class="bank">{bank3}</div>
<ol style="line-height:1.75;font-size:8.9pt;margin:0">{exl}</ol>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "3 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{rl}</ol>
{sub("C", "Scegli la forma giusta.", "2 min")}
<ol style="line-height:1.7;font-size:8.9pt;margin:0">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>non + verbo + mica / affatto / per niente / neanche / nemmeno / neppure</b>: <i>non è mica piccola, non è affatto il mio stile, non sente nemmeno il campanello</i>. Se <i>mica</i> o <i>neanche</i> vengono <b>prima</b> del verbo, niente <i>non</i>: <i>Mica è un problema! · Neanche tu sorridevi.</i> <b>Neanch'io / neanche a me</b> = <i>eu também não</i>. Tutto alla pagina successiva: <b>Riferimento grammaticale</b>.</div>""",
    29, """<ol><li>A: far ripetere ogni frase con il tono giusto: <i>mica</i> spesso aggiunge sorpresa o ironia. Registro informale: con il capo o con un cliente meglio <i>non è per niente…</i></li>
<li>C: frase 2: con <i>piacere</i> si risponde <i>neanche a me / anche a me</i>, non <i>neanch'io</i>.</li></ol>""")

    grammar_ref_it.negazione_rinforzata(b)

    # Pagina 5 - Laboratorio di lessico + pronuncia
    lft = ["Ah, però!", "Boh!", "Mah…", "Ma va'!", "Figurati!", "Uffa!"]
    rgt = ["Non ci credo!", "Che noia, sono stufo/a!", "Che bella sorpresa!", "Di niente, nessun problema.", "Non lo so.", "Ho dei dubbi, non sono convinto/a."]
    ans = {"Ah, però!": "Che bella sorpresa!", "Boh!": "Non lo so.", "Mah…": "Ho dei dubbi, non sono convinto/a.", "Ma va'!": "Non ci credo!",
           "Figurati!": "Di niente, nessun problema.", "Uffa!": "Che noia, sono stufo/a!"}
    mm = " &nbsp; ".join(f"<b>{chr(97+i)}</b> {x}" for i, x in enumerate(rgt))
    cll = "".join(f"<li>{x} {A(chr(97 + rgt.index(ans[x])), 'min-width:6mm')}</li>" for x in lft)
    b.page(f"""{sec(4, "Laboratorio di lessico: le parole del parlato", "4 min")}
{sub("A", "Unisci le espressioni al loro significato.", "2 min")}
<p style="margin:.3mm 0;font-size:8.6pt;line-height:1.6">{mm}</p>
<ol style="line-height:1.5;font-size:8.7pt;margin:0;column-count:2">{cll}</ol>
{sub("B", "Rispondi con l'insegnante.", "2 min")}
<ol style="line-height:1.45;font-size:8.7pt;margin:0;column-count:2"><li>Quando dici «uffa»?</li><li>Che cosa rispondi a «grazie mille»?</li><li>Una notizia per cui diresti «ma va'!»?</li><li>Queste parole si usano anche con il capo?</li></ol>
<div class="box sand"><h4>ATTENZIONE: FALSI AMICI E SCELTA DELLE PAROLE</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Uffa! Finalmente a casa.</td><td><b>Meno male! Finalmente a casa.</b></td><td><i>uffa</i> = noia, non sollievo (<i>ufa</i>).</td></tr>
<tr><td>Affatto, hai ragione.</td><td><b>Infatti, hai ragione.</b></td><td><i>affatto</i> = per niente; <i>de fato</i> = <i>infatti</i>.</td></tr>
<tr><td>Non fumo. — Anche io no.</td><td><b>Neanch'io.</b></td><td><i>eu também não</i> = <i>neanch'io</i>.</td></tr>
<tr><td>Non mica è piccola.</td><td><b>Non è mica piccola.</b></td><td><i>mica</i> va dopo il verbo.</td></tr></table></div>
{sec(5, "Laboratorio di pronuncia: l'accento sulla negazione", "4 min")}
<p class="small" style="margin:.3mm 0">Nella negazione rafforzata la voce mette l'accento più forte sulla parola che nega: <i>non è <b>MI</b>ca piccola · non è af<b>FAT</b>to il mio stile · non c'è <b>NEAN</b>che un piatto</i>. Così il no diventa più deciso, o più ironico.</p>
{audiocard(["08.2"])}
{sub("A", "Ascolta e ripeti con lo stesso accento. Poi l'insegnante dice una frase normale e tu la ripeti con la negazione rafforzata.", "4 min", "08.2")}
<p style="margin:.3mm 0;font-size:8.8pt;line-height:1.6">{" &nbsp;·&nbsp; ".join(f"<b>{i+1}</b> {x}" for i, x in enumerate(S082))}</p>""",
    29, """<ol><li>A: Ah, però c · Boh e · Mah f · Ma va' a · Figurati d · Uffa b. Tutte informali: con il capo meglio <i>Non lo so</i> o <i>Si figuri</i>.</li>
<li>Pronuncia: frasi per il gioco: <i>La stanza non è piccola → non è mica piccola · Non ho un euro → non ho neanche un euro · Il film non mi è piaciuto → non mi è piaciuto per niente.</i></li></ol>""")

    # Pagina 6 - Pratica
    pc = [(["Mica male", "Mica bene"], "Mica male"), (["mica", "anche"], "mica"), (["per niente", "niente per"], "per niente"),
          (["affatto", "infatti"], "affatto"), (["nemmeno", "anche"], "nemmeno"), (["neanche", "anche"], "neanche"),
          (["neanche lui", "anche lui no"], "neanche lui"), (["Mica", "Non mica"], "Mica")]
    p = [ch(o, a) for o, a in pc]
    dx = [("Non fumo.", "Neanch'io. / Io sì."), ("Mi piace cucinare.", "Anche a me. / A me no."),
          ("Non mi piacciono le feste.", "Neanche a me. / A me sì."), ("Non sono mai stato/a a Torino.", "Neanch'io. / Io sì."),
          ("Studio tutte le sere.", "Anch'io. / Io no."), ("Non mi piace il tappeto blu.", "Neanche a me. / A me sì.")]
    dxl = "".join(f"<li>{s} {A(r, 'min-width:46mm')}</li>" for s, r in dx)
    b.page(f"""{sec(6, "Pratica", "8 min")}
<div style="display:flex;gap:3mm;align-items:flex-start"><div style="flex:1">
{sub("A", "Domenica Tommaso scrive a sua sorella Marta. Scegli la forma giusta.", "5 min")}</div>{img('C', 30, 20)}</div>
<div class="box" style="line-height:1.95;font-size:9pt"><b>Tommaso:</b> Ciao Marta! Ieri ho visto la stanza in via Zamboni. {p[0]}! Non è {p[1]} piccola, c'è tanta luce e il prezzo non è {p[2]} alto: 380 euro, spese incluse. Il tappeto blu non è {p[3]} bello, ma pazienza. La vicina del piano di sopra non sente {p[4]} il campanello, quindi posso studiare in pace. E la cucina? Non c'era {p[5]} un piatto sporco! Il coinquilino, Bruno, è brasiliano e vuole insegnarmi a fare il feijão. Io non so cucinare, e {p[6]}, secondo me! {p[7]} mi dirai anche tu che è una scelta sbagliata?</div>
{sub("B", "Reagisci con anch'io, neanch'io, anche a me o neanche a me. Poi di' la verità su di te.", "3 min")}
<ol style="line-height:1.85;font-size:8.8pt;margin:0">{dxl}</ol>""",
    26, """<ol><li>A: gap 7: <i>neanche lui</i> = <i>nem ele</i>. Gap 8: <i>mica</i> all'inizio della frase, senza <i>non</i>, in una domanda preoccupata.</li>
<li>B: con <i>piacere</i>: <i>anche a me / neanche a me</i>; con gli altri verbi: <i>anch'io / neanch'io</i>. Per dire il contrario: <i>io sì / io no, a me sì / a me no</i>.</li></ol>""")

    # Pagina 7 - Parlare
    b.page(f"""{sec(7, "Parlare: il candidato pignolo", "12 min")}
<div class="box sand" style="margin-top:0"><h4>LINGUA PER COMUNICARE</h4>
<table style="margin:0;font-size:8.4pt"><tr><th>dire di no con forza</th><th>giudizi informali</th><th>sorprendersi</th><th>essere d'accordo nel no</th></tr>
<tr><td><i>Per niente! · Niente affatto! · Neanche per sogno! · Assolutamente no!</i></td><td><i>Mica male! · Mica tanto. · Non è un granché. · Niente di speciale.</i></td><td><i>Ah, però! · Ma va'! · Davvero? · Non ci credo!</i></td><td><i>Neanch'io. · Neanche a me. · Nemmeno io. · Io neppure.</i></td></tr></table></div>
<div style="display:flex;gap:3mm;align-items:flex-start;margin-top:1mm"><div style="flex:1">
{sub("A", "Monologo. Prepara per un minuto, poi descrivi per due minuti la tua casa a una persona che vuole affittare una stanza. Usa almeno cinque negazioni rafforzate.", "5 min")}
<ul style="line-height:1.45;font-size:8.9pt;margin:0"><li>la luce e lo spazio</li><li>il rumore e i vicini</li><li>il riscaldamento o l'aria condizionata</li><li>i problemi (sii sincero/a!)</li></ul></div>{img('D', 34, 24)}</div>
{sub("B", "Gioco di ruolo. L'insegnante visita la tua casa per affittare una stanza ed è molto pignolo/a. Rispondi in modo informale.", "4 min")}
<p style="margin:.3mm 0;font-size:8.6pt">{R("Insegnante: La stanza è un po' piccola, no? · C'è rumore la sera? · Il riscaldamento funziona? · I vicini sono simpatici? · Posso portare il mio gatto? · Io non so neanche fare un uovo: è un problema? · Mah… mica male. Ci penso.") if T else ""}</p>
{sub("C", "Opinioni. Parla con l'insegnante.", "3 min")}
<ol style="line-height:1.5;font-size:8.9pt;margin:0"><li>Si possono usare <i>mica, boh, uffa</i> con persone che non conosci?</li><li>Meglio vivere con amici o con sconosciuti?</li><li>Che cosa non è affatto importante, per te, in una casa?</li></ol>""",
    28, """<ol><li>A: non interrompere; annotare gli errori per il registro (pagina 8), soprattutto <i>anche io no</i> e la posizione di <i>mica</i>.</li>
<li>B: le battute dell'insegnante sono in rosso; registro informale (tu). Reagire alle risposte con <i>Ah, però! · Ma va'!</i></li></ol>""")

    # Pagina 8 - Conclusione
    cd = ["So capire una conversazione informale alla velocità naturale.", "So usare mica, affatto, per niente, neanche, nemmeno.",
          "So reagire con le espressioni del parlato."]
    cdr = "".join(f"<tr><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for s in cd)
    b.page(f"""{sec(8, "Conclusione e compiti", "4 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck" style="font-size:8.6pt"><tr><th>In italiano…</th><th style="width:16mm">Facile!</th><th style="width:16mm">A volte</th><th style="width:16mm">Non ancora</th></tr>{cdr}</table>
{sub("B", "I miei errori. Scrivi tre correzioni della lezione di oggi.", "2 min")}
<div style="display:flex;gap:5mm;font-size:8.6pt"><div style="flex:1"><b>Ho detto…</b>{lines(3)}</div><div style="flex:1"><b>Meglio:</b>{lines(3)}</div></div>
{sub("C", "Compiti: scrittura (100–150 parole)", "1 min")}
<p style="margin:.3mm 0"><b>Un messaggio informale.</b> Scrivi a un amico e racconta una visita: una casa, un ristorante, un negozio o un posto nuovo. Prima leggi il messaggio di Bruno a Paolo.</p>
<div class="box" style="font-size:8.6pt;line-height:1.4;margin:.5mm 0"><i>Ciao Paolo! Come va dai tuoi? Oggi è venuto il primo candidato per la tua stanza: si chiama Tommaso e studia Medicina. Mica male, devo dire! Non è affatto un tipo da feste: studia sempre, non sa neanche cucinare e mangia alla mensa. La stanza gli è piaciuta, anche se il tuo tappeto blu non gli piace per niente (neanche a me, a dire la verità!). Júlia dice che è troppo serio: non ha sorriso nemmeno una volta. Ma io non cerco mica un comico, cerco uno che lavi i piatti! E la cucina: non c'era neanche un piatto nel lavandino. Mica ci credi, vero? Lunedì gli scrivo. Ci vediamo domenica sera! Bruno</i></div>
<p class="small" style="margin:.3mm 0">Lista di controllo: ☐ almeno cinque negazioni rafforzate &nbsp;☐ <i>neanch'io</i> o <i>neanche a me</i> &nbsp;☐ un'espressione del parlato (<i>Ah, però! · Boh · Ma va'!</i>) &nbsp;☐ tono informale &nbsp;☐ 100–150 parole</p>
{lines(6)}""",
    30, """<ol><li>B (registro degli errori): annotare 3–5 errori reali della lezione; lo studente prova prima ad autocorreggersi.</li>
<li>C: far sottolineare nel modello tutte le negazioni (<i>mica, affatto, neanche, per niente, nemmeno</i>) e notare <i>cerco uno che lavi</i> (unità 07). Prossima unità: <i>Modi di dire</i> (Carnevale; <i>da</i> + infinito).</li></ol>""")

    b.extra("Trascrizioni audio", f"""
{sub("08.1", "Mica male! (naturale e lenta)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("08.2", "Ripeti: la negazione rafforzata")}
<p>{" · ".join(S082)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "B1 Progresso 08 - Mica male")
