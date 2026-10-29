# Speak! Essenziale A1 - Unità 15 "La casa" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
from stanza import thestanza
setup(band="A1 · UNITÀ 15", audio_json=os.path.join(HERE, "audio_it-a1-unita-15.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il soggiorno", "soggiorno"), ("B", "la cucina", "cucina"), ("C", "la camera da letto", "camera da letto"), ("D", "il bagno", "bagno"),
          ("E", "il balcone", "balcone"), ("F", "il divano", "divano"), ("G", "la lampada", "lampada"), ("H", "lo specchio", "specchio")]

SCRIPT = [("Narratore", "Dialogo uno. La signora Rossi mostra un appartamento a Júlia."), ("Signora Rossi", "Ecco l'appartamento, Júlia. È al terzo piano, proprio sopra il Suo."),
          ("Júlia", "Che bello! È molto luminoso."), ("Signora Rossi", "Questo è il soggiorno. C'è un divano, ci sono due poltrone e c'è anche un balcone."),
          ("Júlia", "E la cucina dov'è?"), ("Signora Rossi", "È accanto al soggiorno. E qui ci sono due camere da letto e un bagno."),
          ("Júlia", "Quanto costa l'affitto?"), ("Signora Rossi", "Settecento euro al mese."),
          ("Narratore", "Dialogo due. Al telefono."), ("Marco", "Allora, Júlia, com'è la casa nuova?"),
          ("Júlia", "È grande e luminosa! Ci sono due camere da letto, così mio fratello Bruno può venire a trovarmi."), ("Marco", "C'è una lavatrice?"),
          ("Júlia", "Sì, è in bagno. E il divano è rosso e le poltrone sono verdi. Molto italiano!"),
          ("Narratore", "Dialogo tre. Il giorno del trasloco."), ("Davide", "Júlia, dove metto questa lampada?"), ("Júlia", "Accanto al divano, per favore."),
          ("Davide", "E lo specchio?"), ("Júlia", "Dietro la porta del bagno."), ("Davide", "E questa scatola? Che cosa c'è dentro?"),
          ("Júlia", "Ci sono i miei libri. Sotto il letto, grazie!"), ("Davide", "Ecco fatto! E adesso una pizza sul balcone?"), ("Júlia", "Perfetto!")]
S152 = ["stanza", "terrazza", "piazza", "zona", "mezzo", "pranzo", "Una stanza con terrazza in zona piazza Maggiore."]
S153 = ["C'è un balcone.", "Ci sono due camere da letto.", "La cucina è accanto al soggiorno.", "La lampada è accanto al divano.", "Lo specchio è dietro la porta.",
        "Il divano è rosso e le poltrone sono verdi."]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 15", "La casa", "Descrivere la casa · <b>c'è un balcone, ci sono due camere</b>",
                       [("SAI FARE", "descrivere una casa, dire dove sono le cose e chiedere informazioni su un appartamento"),
                        ("LINGUA", "c'è / ci sono · accanto al, sotto, sopra, dietro, davanti a · i colori"),
                        ("PRONUNCIA", "la Z: stanza, terrazza, zona · descrivere la casa")])
    words = ["il bagno", "il balcone", "la camera da letto", "la cucina", "il divano", "la lampada", "il soggiorno", "lo specchio"]
    rd = [("Dormi nella", "camera da letto"), ("Prepari la cena nella", "cucina"), ("Ti fai la doccia nel", "bagno"),
          ("Guardi la TV nel", "soggiorno"), ("Prendi il sole sul", "balcone"), ("Entri in casa dall'", "ingresso")]
    rl = [f'<li value="{i+1}">{a} {A(x, "min-width:28mm")}.</li>' for i, (a, x) in enumerate(rd)]
    b.page(f"""{sec(1, "Riscaldamento: la casa", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi le parole sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Dove sei? Completa.", "4 min")}
<div class="bank" style="background:#fff">bagno · balcone · camera da letto · cucina · ingresso · soggiorno</div>
{twocol(rl, 4)}""",
    24, """<ol><li>A: <b>la camera (da letto)</b> = dove dormi; <i>la stanza</i> = qualsiasi locale della casa. Attenzione: <i>il quarto</i> in italiano è solo ¼.</li>
<li>B: far notare le preposizioni articolate già viste: <i>nella, nel, sul, dall'</i> (unità 8).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: stanze e mobili</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Il nuovo appartamento di Júlia: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>c'è / ci sono · preposizioni di luogo · i colori</td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>La Z · descrivere la casa</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Il disegno del soggiorno · c'è / ci sono · i colori</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Un annuncio (domande) · la tua casa</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 12–15) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Júlia vuole una casa più grande per ospitare la sua famiglia: suo fratello Bruno vuole venire a trovarla. La signora Rossi le mostra un appartamento al terzo piano, proprio sopra il suo: soggiorno con balcone, due camere da letto, settecento euro al mese. Júlia racconta a Marco che il divano è rosso e le poltrone sono verdi. Il giorno del trasloco Davide la aiuta a mettere a posto le cose; alla fine, una pizza sul balcone.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Ci è un balcone</i> ✗ → <b>c'è un balcone</b>. <i>C'è due camere</i> ✗ → <b>ci sono due camere</b> (plurale). <i>Accanto il divano</i> ✗ → <b>accanto al divano</b>. <i>Le sedie sono rossa</i> ✗ → <b>rosse</b>: i colori si accordano come gli altri aggettivi (tranne <i>blu, rosa, viola</i>).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Nelle città italiane quasi tutti abitano in un <b>appartamento in condominio</b>. Il <b>piano terra</b> è a livello della strada; il primo piano è sopra. Spesso l'affitto non comprende le <b>spese condominiali</b> e le bollette: bisogna sempre chiedere.</div>
<div class="box"><h4>AUDIO</h4>Traccia 15.1 Tre dialoghi (lento e naturale) · Traccia 15.2 La Z · Traccia 15.3 Descrivere la casa</div>""")

    # Page 2
    vf = [("L'appartamento è al terzo piano.", "V"), ("Nel soggiorno ci sono due divani.", "F"), ("La cucina è accanto al soggiorno.", "V"),
          ("Ci sono tre camere da letto.", "F"), ("L'affitto è di settecento euro al mese.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    gp = [("C'è anche un", "balcone", "."), ("Il divano è", "rosso", "e le poltrone sono verdi."), ("Accanto", "al", "divano, per favore."),
          ("", "Dietro", "la porta del bagno."), ("", "Ci sono", "i miei libri.")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:18mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: la casa nuova", "10 min")}
<p>La signora Rossi mostra a Júlia un appartamento libero nel suo palazzo. Poi Júlia telefona a Marco e Davide la aiuta con il trasloco.</p>
{audiocard(["15.1 · SLOW", "15.1 · NATURAL"])}
{sub("A", "Ascolta. Vero (V) o falso (F)?", "4 min", "15.1 · SLOW")}
<table style="margin:0">{vfr}</table>
{sub("B", "Ascolta di nuovo e completa.", "4 min", "15.1 · NATURAL")}
{twocol(gl, 4)}
{sub("C", "Perché Júlia vuole due camere da letto?", "2 min")}
<div class="wline">{R("Perché così suo fratello Bruno può venire a trovarla (e dormire da lei).")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. 2: c'è <b>un</b> divano e ci sono due <b>poltrone</b>. 4: le camere sono <b>due</b>. La signora Rossi dà del <i>Lei</i>: <i>sopra il Suo</i> (appartamento).</li>
<li>B: versione <b>naturale</b>. <i>Il trasloco</i> = quando cambi casa e porti tutte le tue cose.</li>
<li>C: collegamento con l'unità 14 (Bruno, il fratello più giovane di Júlia).</li></ol>""")

    # Page 3
    pr = [("sopra", "La finestra è sopra il divano."), ("sotto", "Il gatto è sotto il tavolino."), ("davanti a", "Il tappeto è davanti al divano."),
          ("dietro", "Lo specchio è dietro la porta."), ("accanto a", "La lampada è accanto al divano."), ("tra", "Il divano è tra il tavolino e la lampada.")]
    tpr = "".join(f"<tr><td><b>{p}</b></td><td><i>{e}</i></td></tr>" for p, e in pr)
    co = [("rosso", "rossa", "rossi", "rosse"), ("bianco", "bianca", "bianchi", "bianche"), ("verde", "verde", "verdi", "verdi"), ("blu", "blu", "blu", "blu")]
    tco = "".join(f"<tr><td><b>{a}</b></td><td><b>{bb}</b></td><td><b>{c}</b></td><td><b>{d}</b></td></tr>" for a, bb, c, d in co)
    rules = [("Nel soggiorno", "c'è un divano", "ci è un divano"), ("In casa", "ci sono due bagni", "c'è due bagni"),
             ("La lampada è", "accanto al divano", "accanto il divano"), ("Le poltrone sono", "verdi", "verde")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    b.page(f"""{sec(3, "Grammatica: c'è / ci sono · dov'è? · i colori", "10 min")}
<div class="two"><div>{sub("A", "C'è / ci sono.", "2 min")}
<p><b>c'è</b> + singolare: <i>c'è un balcone</i><br><b>ci sono</b> + plurale: <i>ci sono due camere</i><br>
<i>C'è una lavatrice? — Sì, c'è. / No, non c'è.</i><br><i>Quante camere ci sono? — Ci sono due camere.</i></p></div>
<div>{sub("C", "I colori.", "2 min")}<table style="margin:0"><tr><th>m. sing.</th><th>f. sing.</th><th>m. pl.</th><th>f. pl.</th></tr>{tco}</table>
<p class="small" style="margin-top:1mm">Come <i>blu</i>: <b>rosa, viola</b> (non cambiano mai).</p></div></div>
{sub("B", "Dov'è? Le preposizioni di luogo.", "3 min")}
<table style="margin:0">{tpr}</table>
<div class="box" style="margin-top:1.5mm"><h4>ATTENZIONE</h4><b>accanto a, davanti a</b> + articolo: <i>accanto <b>al</b> divano, davanti <b>alla</b> finestra</i>. <b>su</b> + articolo: <i><b>sul</b> tavolo, <b>sulla</b> sedia</i>. <b>sopra, sotto, dietro, tra</b> + articolo: <i>sotto il letto</i>.</div>
{sub("D", "Scegli l'opzione corretta.", "3 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>""",
    27, """<ol><li>A: <i>c'è</i> = <i>ci + è</i>, con l'apostrofo. Per gli oggetti di una casa si può dire anche <i>la casa <b>ha</b> un balcone</i>: è corretto.</li>
<li>B: mostrare con oggetti veri sul tavolo (la penna è sotto il libro, accanto al telefono…).</li>
<li>C: l'aggettivo di colore va <b>dopo</b> il nome: <i>il divano rosso</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("E", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ci è un balcone.</td><td><b>C'è un balcone.</b></td><td><i>ci + è = c'è</i>.</td></tr>
<tr><td>C'è due camere da letto.</td><td><b>Ci sono due camere da letto.</b></td><td>Plurale: <i>ci sono</i>.</td></tr>
<tr><td>Il mio quarto è piccolo.</td><td><b>La mia camera è piccola.</b></td><td><i>Il quarto</i> = ¼.</td></tr>
<tr><td>La lampada è accanto il divano.</td><td><b>La lampada è accanto al divano.</b></td><td><i>accanto a + il = al</i>.</td></tr>
<tr><td>Le sedie sono rossa.</td><td><b>Le sedie sono rosse.</b></td><td>Il colore si accorda.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["15.2", "15.3"])}
{sub("A", "La Z italiana. Ascolta e ripeti: STANZA, TERRAZZA, ZONA.", "2 min", "15.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S152)}</div>
{sub("B", "Descrivere la casa. Ascolta e ripeti.", "3 min", "15.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S153)}</div>""",
    38, """<ol><li>Errori: l'errore più frequente è <i>c'è</i> con il plurale. Far ripetere in coppia: <i>c'è un… / ci sono due…</i></li>
<li>4A: la <b>z</b> italiana non è mai una <i>s</i> sonora: in <i>stanza, terrazza, piazza, pranzo</i> suona «ts»; in <i>zona, mezzo</i> suona «dz». La doppia (<i>terrazza, piazza</i>) è più lunga e forte.</li>
<li>4B: <i>piazza Maggiore</i> è la piazza principale di Bologna.</li></ol>""")

    # Page 5
    sp = [("La finestra è", "sopra", "il divano."), ("La lampada è", "accanto al", "divano."), ("Il gatto è", "sotto il", "tavolino."),
          ("La pianta è", "sul", "tavolino."), ("Il tappeto è", "davanti al", "divano."), ("Il divano è", "tra", "il tavolino e la lampada.")]
    spl = [f'<li value="{i+1}">{a} {A(x, "min-width:20mm")} {c}</li>' for i, (a, x, c) in enumerate(sp)]
    cs = [("Nel soggiorno", "c'è", "un quadro."), ("Nella libreria", "ci sono", "molti libri."), ("Sul tavolino", "c'è", "una pianta."), ("In cucina", "ci sono", "quattro sedie.")]
    csl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} {c}</li>' for i, (a, x, c) in enumerate(cs)]
    cl = [("il divano", "rosso", "rosso"), ("le poltrone", "verde", "verdi"), ("le sedie", "bianco", "bianche"), ("i tappeti", "blu", "blu")]
    cll = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} <span class="small">({n})</span></li>' for i, (a, n, x) in enumerate(cl)]
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Guarda il soggiorno di Júlia e completa.", "4 min")}
<div style="margin:1mm 0 2mm">{thestanza(62)}</div>
<div class="bank" style="background:#fff">accanto al · davanti al · sopra · sotto il · sul · tra</div>
{twocol(spl, 4)}
{sub("B", "C'è o ci sono?", "2 min")}
{twocol(csl, 3)}
{sub("C", "Scrivi il colore nella forma corretta.", "2 min")}
{twocol(cll, 3)}""",
    22, """<ol><li>A: dopo l'esercizio, l'insegnante chiede: <i>Dov'è il quadro?</i> (sopra il tavolino) <i>Dov'è la libreria?</i> (accanto alla lampada).</li>
<li>C: <i>bianco → bianche</i>: al plurale si scrive <b>-che</b> per mantenere il suono duro.</li></ol>""")

    # Page 6
    ad = [("A che piano è?", "al secondo piano"), ("Quante camere da letto ci sono?", "una"), ("Quanti bagni ci sono?", "uno, con la doccia"),
          ("C'è un balcone?", "no, ma c'è una terrazza"), ("Com'è la cucina?", "grande, con la lavatrice"), ("Quanto costa l'affitto?", "550 euro al mese")]
    adr = "".join(f"<tr><td style='width:62mm'><b>{q}</b></td><td>{A(a, 'min-width:60mm')}</td></tr>" for q, a in ad)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "AFFITTASI: appartamento in via Verdi. L'insegnante ha le informazioni. Fai le domande e completa. Poi decidi: è una buona casa per te?", "7 min")}
<table style="margin:1mm 0 2mm">{adr}</table>
<div class="bank" style="background:#fff">Mi scusi, … · Posso vedere l'appartamento? · È luminoso? · Ci sono le spese condominiali?</div>
{sub("B", "La tua casa. Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Abiti in una casa o in un appartamento? A che piano?</li><li>Quante stanze ci sono? C'è un balcone?</li><li>Com'è il tuo soggiorno? Che cosa c'è? Di che colore è il divano?</li><li>Qual è la tua stanza preferita? Perché?</li></ol>""",
    26, """<ol><li>A: l'insegnante fa il proprietario e usa il <i>Lei</i>; le risposte in rosso sono solo per l'insegnante. Domanda extra: le spese condominiali sono 60 euro al mese.</li>
<li>B: correggere <i>c'è / ci sono</i> e l'accordo dei colori. Lo studente può mostrare una foto della sua casa sul telefono.</li></ol>""")

    # Page 7
    pc = [("Unità 12", "So spiegare una ricetta semplice."), ("Unità 13", "So descrivere la mia giornata tipo."), ("Unità 14", "So presentare la mia famiglia."),
          ("Unità 15", "So descrivere la mia casa con c'è / ci sono."), ("Unità 15", "So dire dove sono le cose: accanto al, sotto, sopra…")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Nel bagno ci è una lavatrice.", "Nel bagno c'è una lavatrice."), ("Nel soggiorno c'è due poltrone.", "Nel soggiorno ci sono due poltrone."),
          ("Il tappeto è davanti il divano.", "Il tappeto è davanti al divano."), ("Le mie sedie sono bianca.", "Le mie sedie sono bianche."),
          ("La lampada è accanto la finestra.", "La lampada è accanto alla finestra."), ("Quante camere c'è?", "Quante camere ci sono?")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La mia casa.</b> Scrivi 6 frasi sulla tua casa: quante stanze ci sono, che cosa c'è nel soggiorno, dove sono le cose, di che colore sono.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante descrive una stanza e lo studente dice che cosa c'è e dove: <i>Nella mia camera c'è un letto. Accanto al letto…</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("15.1", "La casa nuova (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("15.2", "La Z")}
<p>{" · ".join(S152)}</p>
{sub("15.3", "Descrivere la casa")}
<p>{" ".join(S153)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 15 - La casa")
