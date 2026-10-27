# Speak! Essenziale A1 - Unità 01 "Piacere!" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 01", audio_json=os.path.join(HERE, "audio_it-a1-unita-01.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "Ciao!", "ciao"), ("B", "Buongiorno!", "buongiorno"), ("C", "Buonasera!", "buonasera"), ("D", "Buonanotte!", "buonanotte"),
          ("E", "Arrivederci!", "arrivederci"), ("F", "Piacere!", "piacere"), ("G", "Grazie!", "grazie"), ("H", "Benvenuta!", "benvenuta")]

SCRIPT = [("Narratore", "Dialogo uno."), ("Signora Rossi", "Buongiorno! Lei è la signora Souza?"), ("Júlia", "Sì, sono io. Buongiorno!"),
          ("Signora Rossi", "Piacere, sono Paola Rossi."), ("Júlia", "Piacere! Mi chiamo Júlia."), ("Signora Rossi", "Come sta, signora?"),
          ("Júlia", "Bene, grazie. E Lei?"), ("Signora Rossi", "Molto bene, grazie. Benvenuta a Bologna!"),
          ("Narratore", "Dialogo due."), ("Marco", "Ciao! Tu sei Júlia, la nuova architetta?"), ("Júlia", "Sì, sono io. Ciao! E tu come ti chiami?"),
          ("Marco", "Mi chiamo Marco. Piacere!"), ("Júlia", "Piacere, Marco."), ("Marco", "Allora, come stai? È il primo giorno!"),
          ("Júlia", "Bene, grazie. Un po' stanca. E tu?"), ("Marco", "Benissimo!"),
          ("Narratore", "Dialogo tre."), ("Giulia", "Buonasera!"), ("Júlia", "Buonasera! Un tè, per favore."), ("Giulia", "Ecco. Lei è nuova qui?"),
          ("Júlia", "Sì, sono Júlia. Sono brasiliana."), ("Giulia", "Júlia? Come me! Io mi chiamo Giulia. Ma diamoci del tu!"), ("Júlia", "Volentieri!"),
          ("Giulia", "Allora… ciao, Júlia! A domani!"), ("Júlia", "Arrivederci… ehm, no: ciao, Giulia! A domani!")]
S012 = ["ciao", "piacere", "arrivederci", "buongiorno", "Giulia", "mi chiamo", "che cosa", "Bologna", "signora"]
S013 = ["Come ti chiami?", "Come si chiama?", "Come stai?", "Come sta?", "E tu?", "E Lei?", "Tu sei Marco?", "Lei è la signora Rossi?"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 01", "Piacere!", "Salutare e presentarsi · <b>tu o Lei?</b>",
                       [("SAI FARE", "salutare, presentarti e chiedere come sta una persona"), ("LINGUA", "essere · chiamarsi · io / tu / Lei · Come stai? / Come sta?"),
                        ("PRONUNCIA", "ci / ce · gi · chi / che · gn · l'intonazione delle domande")])
    words = ["Arrivederci!", "Benvenuta!", "Buonanotte!", "Buonasera!", "Buongiorno!", "Ciao!", "Grazie!", "Piacere!"]
    qs = [("Sono le 8 di mattina. Entri in un bar.", "Buongiorno!"), ("Sono le 21. Entri in un ristorante.", "Buonasera!"),
          ("Vai a dormire.", "Buonanotte!"), ("Esci da un negozio.", "Arrivederci!"), ("Conosci una persona nuova.", "Piacere!")]
    ql = [f'<li value="{i+1}">{q} {R("→ " + a) if T else ""}</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: i saluti", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi il saluto sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Che cosa dici?", "4 min")}
{twocol(ql, 4)}""",
    28, """<ol><li>A: l'insegnante legge ogni parola, lo studente ripete e scrive. <b>Buongiorno</b> fino a circa le 14–15, poi <b>Buonasera</b>. <b>Buonanotte</b> solo per andare a dormire. Foto G: <i>Grazie e arrivederci</i> sulle scatole della pizza!</li>
<li>B: accettare anche <i>Ciao!</i> quando la situazione è informale. Chiedere: <i>E in Brasile?</i></li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 saluti ed espressioni con foto</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il primo giorno di Júlia a Bologna: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td><i>essere</i> · <i>chiamarsi</i> · tu o Lei?</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>ci / gi / chi / gn · intonazione delle domande</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Completare, ordinare, trasformare (tu → Lei)</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Quattro situazioni: tu o Lei? · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>7</td></tr></table>
<div class="box"><h4>COME FUNZIONA QUESTA GUIDA</h4>Ogni pagina è uguale alla pagina del Libro dello studente con lo stesso numero. Le tue note sono nel <b>riquadro giallo</b>.
<span class="red">Le soluzioni in rosso</span> non sono nel libro dello studente. Le etichette <span class="time">5 min</span> indicano il tempo di ogni attività. Le trascrizioni audio sono nell'ultima pagina.</div>
<div class="box sand"><h4>LA STORIA COMINCIA</h4>Júlia Souza è un'architetta brasiliana di Belo Horizonte. Arriva a Bologna per lavorare in uno studio di architettura. La mattina conosce la padrona di casa, la signora Rossi (Lei). Allo studio conosce Marco, un collega (tu). La sera, al bar sotto casa, conosce Giulia… che ha il suo stesso nome in italiano!</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Io chiamo Júlia</i> ✗ → <b>Mi chiamo Júlia</b>. <i>Lei sei…?</i> ✗ → <b>Lei è…?</b> Il <b>Lei</b> formale usa il verbo della terza persona. E <i>Ciao</i> non va bene con una persona che non conosci.</div>
<div class="box"><h4>AUDIO</h4>Traccia 01.1 Tre dialoghi (lento e naturale) · Traccia 01.2 Suoni · Traccia 01.3 Domande</div>""")

    # Page 2
    who = [("1", "Júlia e la signora Rossi", "Lei"), ("2", "Júlia e Marco", "tu"), ("3", "Júlia e Giulia", "Lei → tu")]
    wr = "".join(f'<td style="width:33%"><b>Dialogo {n}</b><br><span class="small">{p}</span><br>{ch(["tu", "Lei"], a) if a != "Lei → tu" else (R("<u>Lei → tu</u>") if T else "<b>tu / Lei</b>")}</td>' for n, p, a in who)
    gp = [("", "Piacere", ", sono Paola Rossi."), ("Come", "sta", ", signora?"), ("E tu come", "ti chiami", "?"),
          ("", "Mi chiamo", "Marco."), ("", "Benvenuta", "a Bologna!"), ("Ma diamoci", "del tu", "!")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:22mm")}{c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: il primo giorno di Júlia", "10 min")}
<p>Júlia è brasiliana. Oggi è il suo primo giorno a Bologna. Conosce tre persone: la padrona di casa, un collega e la proprietaria del bar sotto casa.</p>
{audiocard(["01.1 · SLOW", "01.1 · NATURAL"])}
{sub("A", "Ascolta. In ogni dialogo usano il tu o il Lei?", "3 min", "01.1 · SLOW")}
<table class="ck"><tr>{wr}</tr></table>
{sub("B", "Ascolta di nuovo e completa.", "5 min", "01.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Alla fine Júlia dice «Arrivederci… ehm, no: ciao!». Perché?", "2 min")}
<div class="wline">{R("Perché Giulia dice «diamoci del tu»: adesso parlano in modo informale, e con il tu si dice «Ciao!».")}</div>""",
    29, """<ol><li>A: versione <b>lenta</b>. Nel dialogo 3 Giulia comincia con il <b>Lei</b> (<i>Lei è nuova qui?</i>) e poi propone il tu.</li>
<li>B: versione <b>naturale</b>. <i>Benvenuta</i> perché Júlia è una donna (Benvenuto a un uomo).</li>
<li>C: <i>Diamoci del tu!</i> = usiamo il tu. In Italia è normale proporlo dopo pochi minuti tra persone della stessa età.</li></ol>""")

    # Page 3
    ess = [("io", "sono", "Sono Júlia."), ("tu", "sei", "Tu sei Marco?"), ("lui / lei", "è", "Lei è brasiliana."), ("Lei (formale)", "è", "Lei è la signora Rossi?")]
    chi = [("io", "mi chiamo"), ("tu", "ti chiami"), ("lui / lei", "si chiama"), ("Lei (formale)", "si chiama")]
    reg = [("Ciao!", "Buongiorno! / Buonasera!"), ("Come stai?", "Come sta?"), ("Come ti chiami?", "Come si chiama?"), ("E tu?", "E Lei?"), ("Ciao! A domani!", "Arrivederci!")]
    rules = [("A un amico:", "Come stai?", "Come sta?"), ("A una signora che non conosci:", "Lei è italiana?", "Lei sei italiana?"),
             ("Per dire il tuo nome:", "Mi chiamo Júlia.", "Io chiamo Júlia."), ("Il Lei formale si scrive con la", "L maiuscola", "l minuscola")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    te = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in ess)
    tc = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td></tr>" for p, v in chi)
    tr_ = "".join(f"<tr><td>{a}</td><td>{f}</td></tr>" for a, f in reg)
    b.page(f"""{sec(3, "Grammatica: essere, chiamarsi, tu o Lei?", "10 min")}
{sub("A", "I verbi essere e chiamarsi. Leggi le frasi dei dialoghi.", "3 min")}
<div class="two"><div><table style="margin:0"><tr><th colspan="3">essere</th></tr>{te}</table></div>
<div><table style="margin:0"><tr><th colspan="2">chiamarsi</th></tr>{tc}</table></div></div>
{sub("B", "Informale o formale?", "3 min")}
<table style="margin:0"><tr><th>tu (informale)</th><th>Lei (formale)</th></tr>{tr_}</table>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>TU O LEI?</h4><b>tu</b> = amici, famiglia, colleghi giovani, bambini. <b>Lei</b> = persone che non conosci, persone più anziane, negozi, uffici. Con il <b>Lei</b> il verbo è come per <i>lui / lei</i>: Lei <b>è</b>, Lei <b>si chiama</b>. Il soggetto spesso non si dice: <i>(Io) sono Júlia.</i></div>""",
    24, """<ol><li>A: far notare che <i>Lei è</i> e <i>lei è</i> hanno la stessa forma: il contesto (e la maiuscola) aiuta.</li>
<li>B/C: chiedere allo studente esempi della sua vita: <i>Con il tuo medico usi il tu o il Lei?</i></li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Io chiamo Júlia.</td><td><b>Mi chiamo Júlia.</b></td><td><i>chiamarsi</i> ha sempre <i>mi / ti / si</i>.</td></tr>
<tr><td>Lei sei italiana?</td><td><b>Lei è italiana?</b></td><td>Con il <i>Lei</i>: verbo alla terza persona.</td></tr>
<tr><td>Buono giorno!</td><td><b>Buongiorno!</b></td><td>Una sola parola.</td></tr>
<tr><td>Ciao, signora Rossi! (prima volta)</td><td><b>Buongiorno, signora Rossi!</b></td><td><i>Ciao</i> è solo informale.</td></tr>
<tr><td>Come stai, signora?</td><td><b>Come sta, signora?</b></td><td><i>signora</i> = Lei.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["01.2", "01.3"])}
{sub("A", "I suoni. Ascolta e ripeti: ci / gi come in ciao, chi / che come in chiamo, gn come in Bologna.", "2 min", "01.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S012)}</div>
{sub("B", "Le domande. Ascolta e ripeti. La voce sale alla fine ↗.", "3 min", "01.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S013)}</div>""",
    40, """<ol><li>Errori: <i>Io chiamo</i> è l'errore più frequente (in portoghese il verbo non è riflessivo). Correggere subito, con gentilezza.</li>
<li>4A: <b>ci, ce</b> = come in <i>tchau</i>; <b>chi, che</b> = suono K (<i>chiamo</i> non è «tchamo»!); <b>gi</b> in <i>Giulia, buongiorno</i>; <b>gn</b> in <i>Bologna, signora</i> = come <i>nh</i> in portoghese.</li>
<li>4B: nelle domande senza parola interrogativa (<i>Tu sei Marco?</i>) l'intonazione è l'unica differenza con l'affermazione.</li></ol>""")

    # Page 5
    gw = ["sono", "sei", "è", "chiami", "chiamo", "chiama", "è", "è"]
    gs = [("Io", "Júlia."), ("Tu", "Marco?"), ("Lei", "la signora Rossi?"), ("Come ti", "?"), ("Mi", "Giulia."),
          ("Come si", ", signora?"), ("Lui", "Davide, il vicino di Júlia."), ("Júlia", "brasiliana.")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:18mm")} {c}</li>' for i, (a, c) in enumerate(gs)]
    od = [("chiami / ti / come / ?", "Come ti chiami?"), ("sta / come / Lei / ?", "Come sta Lei?"), ("Marco / io / sono / ciao,", "Ciao, io sono Marco."), ("nuova / è / qui / Lei / ?", "Lei è nuova qui?")]
    ol5 = "".join(f'<li>{s}<div class="wline">{R(a)}</div></li>' for s, a in od)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con essere o chiamarsi.", "3 min")}
<div class="bank">chiama · chiami · chiamo · è · è · è · sei · sono</div>
{twocol(gl5, 5)}
{sub("B", "Metti le parole in ordine.", "2 min")}
<ol>{ol5}</ol>
{sub("C", "Trasforma il dialogo: dal tu al Lei.", "3 min")}
<div class="two"><div class="msg"><b>A:</b> Ciao! Come ti chiami?<br><b>B:</b> Mi chiamo Luca. E tu?<br><b>A:</b> Io sono Júlia. Come stai?<br><b>B:</b> Bene, grazie!</div>
<div><div class="wline">{R("A: Buongiorno! Come si chiama?")}</div><div class="wline">{R("B: Mi chiamo Luca Bianchi. E Lei?")}</div><div class="wline">{R("A: Io sono Júlia Souza. Come sta?")}</div><div class="wline">{R("B: Bene, grazie!")}</div></div></div>""",
    20, """<ol><li>A: frase 8: <i>Júlia è brasiliana</i> (aggettivo femminile: <i>brasiliano / brasiliana</i>, unità 2).</li>
<li>C: con il Lei è naturale usare anche il cognome. Accettare <i>Buonasera</i>.</li></ol>""")

    # Page 6
    sit = [("1", "Al bar, ore 8:00", "Ordini un caffè. Il barista è un signore anziano."), ("2", "Al lavoro, primo giorno", "Conosci una collega giovane."),
           ("3", "In albergo, ore 21:00", "Arrivi alla reception."), ("4", "A una festa", "Conosci l'amico di un amico.")]
    st = "".join(f'<div class="ad" style="flex:1"><b class="t">{n} · {t}</b>{d}<br>{R("→ " + ("Lei · Buongiorno!" if n == "1" else "tu · Ciao!" if n in "24" else "Lei · Buonasera!"))}</div>' for n, t, d in sit)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Gioco di ruolo. Leggi la situazione: tu o Lei? Saluta, presentati e chiedi come sta. Poi scambiate i ruoli.", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{st}</div>
<div class="bank" style="background:#fff">Buongiorno! / Ciao! · Mi chiamo… · Piacere! · Come stai? / Come sta? · Bene, grazie. E tu? / E Lei? · Arrivederci! / Ciao!</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Come ti chiami?</li><li>Come stai oggi?</li><li>Nel tuo lavoro usi il tu o il Lei? Con chi?</li><li>Conosci un italiano o un'italiana? Come si chiama?</li></ol>""",
    30, """<ol><li>A: l'insegnante fa l'altra persona. Nella situazione 1 rispondere con il Lei; nella 4 rispondere con il tu. Poi lo studente fa il barista, il receptionist, ecc.</li>
<li>B: domande 3 e 4 per riutilizzare <i>tu / Lei</i> e <i>si chiama</i>. Correggere <i>Io chiamo</i> e <i>Lei sei</i>.</li></ol>""")

    # Page 7
    pc = [("Unità 01", "So salutare in modo formale e informale."), ("Unità 01", "So dire il mio nome e chiedere il nome."),
          ("Unità 01", "So chiedere e dire come sto."), ("Unità 01", "So scegliere tra tu e Lei.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Io chiamo Paolo.", "Mi chiamo Paolo."), ("Buono giorno, signora!", "Buongiorno, signora!"), ("Lei sei il signor Bianchi?", "Lei è il signor Bianchi?"),
          ("Come stai, professore?", "Come sta, professore?"), ("Tu ti chiama Marco?", "Tu ti chiami Marco?"), ("Ciao, dottore! Piacere!", "Buongiorno, dottore! Piacere!")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio.</b> Scrivi un breve messaggio a Giulia: saluta, presentati e chiedi come sta (3–4 frasi, con il tu).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Lo studente legge il messaggio e l'insegnante risponde come Giulia (<i>Ciao, Júlia! Io sto bene, grazie…</i>).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("01.1", "Il primo giorno di Júlia (lento e naturale)")}
<p style="line-height:1.5">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("01.2", "I suoni")}
<p>{" · ".join(S012)}</p>
{sub("01.3", "Le domande")}
<p>{" ".join(S013)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 01 - Piacere")
