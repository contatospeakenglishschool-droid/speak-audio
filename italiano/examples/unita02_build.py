# Speak! Essenziale A1 - Unità 02 "Di dove sei?" (tutto in italiano) - built with the shared engine + Italian layer
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
from engine_it import *
setup(band="A1 · UNITÀ 02", audio_json=os.path.join(HERE, "audio_it-a1-unita-02.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "l'Italia", "Italia"), ("B", "il Brasile", "Brasile"), ("C", "il Portogallo", "Portogallo"), ("D", "la Francia", "Francia"),
          ("E", "la Spagna", "Spagna"), ("F", "la Germania", "Germania"), ("G", "gli Stati Uniti", "Stati Uniti"), ("H", "il Giappone", "Giappone")]

SCRIPT = [("Narratore", "Dialogo uno."), ("Marco", "Júlia, tu di dove sei? Di Rio de Janeiro?"), ("Júlia", "No, sono di Belo Horizonte."),
          ("Marco", "Belo Horizonte? Dov'è?"), ("Júlia", "È nel sud-est del Brasile, vicino a Rio."), ("Marco", "E parli inglese?"),
          ("Júlia", "Sì, e un po' di spagnolo. E tu, Marco? Sei di Bologna?"), ("Marco", "Sì, sono bolognese. Ma mia madre è francese, di Lione."),
          ("Narratore", "Dialogo due."), ("Davide", "Ciao! Sei la nuova vicina?"), ("Júlia", "Sì, sono Júlia. Piacere!"),
          ("Davide", "Piacere, io sono Davide. Senti, hai la password del Wi-Fi?"), ("Júlia", "No, non ho la password. Ho un problema anche io!"),
          ("Davide", "Ah, va bene. Sei spagnola?"), ("Júlia", "No, sono brasiliana."), ("Davide", "Brasiliana! Io ho un'amica brasiliana, Bia. È di Salvador."),
          ("Júlia", "E tu? Sei di Bologna?"), ("Davide", "No, sono di Napoli. Sono qui per l'università."),
          ("Narratore", "Dialogo tre."), ("Signora Rossi", "Signora Souza, ha un documento, per il contratto?"), ("Júlia", "Sì, ho il passaporto. Ecco."),
          ("Signora Rossi", "Grazie. Ma questo è un passaporto italiano!"), ("Júlia", "Sì, ho la cittadinanza italiana. Mio nonno è italiano, di Treviso."),
          ("Signora Rossi", "Ah, che bello! Allora Lei è italiana e brasiliana!"), ("Júlia", "Esatto!")]
S022 = ["ho", "o", "hai", "ai", "ha", "a", "Ho un passaporto.", "Hai la password?", "Lei ha un documento?"]
S023 = ["italiano, italiana", "brasiliano, brasiliana", "spagnolo, spagnola", "tedesco, tedesca", "americano, americana", "francese", "inglese", "portoghese", "giapponese"]


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A1 · UNITÀ 02", "Di dove sei?", "Paesi e nazionalità · <b>essere di… · avere</b>",
                       [("SAI FARE", "dire e chiedere la nazionalità e la città di origine"), ("LINGUA", "Di dove sei? · Sono di… · italiano / italiana · francese · ho, hai, ha"),
                        ("PRONUNCIA", "la H non si pronuncia: ho, hai, ha · l'accento delle nazionalità")])
    words = ["la Francia", "la Germania", "gli Stati Uniti", "il Brasile", "il Giappone", "il Portogallo", "la Spagna", "l'Italia"]
    qs = [("La pizza è", "italiana"), ("La caipirinha è", "brasiliana"), ("Il croissant è", "francese"),
          ("La paella è", "spagnola"), ("Il sushi è", "giapponese"), ("Il pastel de nata è", "portoghese")]
    ql = [f'<li value="{i+1}">{q} {A(a, "min-width:24mm")}.</li>' for i, (q, a) in enumerate(qs)]
    b.page(f"""{sec(1, "Riscaldamento: paesi e bandiere", "8 min")}
{sub("A", "Guarda le bandiere. Scrivi il nome del paese sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in words)}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Di dove sono? Completa con la nazionalità.", "4 min")}
<div class="bank" style="background:#fff">brasiliana · francese · giapponese · italiana · portoghese · spagnola</div>
{twocol(ql, 4)}""",
    26, """<ol><li>A: i nomi dei paesi hanno l'articolo: <b>l'</b>Italia, <b>il</b> Brasile, <b>gli</b> Stati Uniti. Far ripetere con l'articolo.</li>
<li>B: anticipa la regola di pagina 3: la pizza (femminile) → itali<b>ana</b>; il croissant → frances<b>e</b>. Chiedere: <i>E il pão de queijo?</i> → <i>brasiliano</i>.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 paesi con le bandiere · nazionalità del cibo</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Júlia parla di dove è: tre dialoghi</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td><i>Di dove sei? Sono di…</i> · aggettivi in -o/-a ed -e · <i>avere</i></td><td>3–4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>5 min</td><td>La H muta · l'accento delle nazionalità</td><td>4</td></tr>
<tr><td>5 Pratica</td><td>8 min</td><td>Nazionalità al maschile e al femminile · <i>avere</i> · presentarsi</td><td>5</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Carte d'identità (tu o Lei?) · domande personali</td><td>6</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione (unità 01–02) e compiti</td><td>7</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Allo studio Marco chiede a Júlia di dove è. Marco è di Bologna, ma la mamma è francese. Sulle scale Júlia conosce Davide, il vicino: è di Napoli e studia a Bologna. Alla fine, per il contratto, la signora Rossi scopre che Júlia ha il passaporto italiano: il nonno è di Treviso!</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4><i>Sono de São Paulo</i> ✗ → <b>Sono di São Paulo</b>. <i>Io tengo un passaporto</i> ✗ → <b>Ho un passaporto</b>. <i>Lei è francesa</i> ✗ → <b>Lei è francese</b> (in -e: uguale per uomo e donna). E la <b>H</b> di <i>ho, hai, ha</i> non si pronuncia.</div>
<div class="box"><h4>LA REALTÀ DEI BRASILIANI</h4>Molti brasiliani hanno un nonno o un bisnonno italiano e chiedono la <b>cittadinanza italiana</b>. È un buon argomento di conversazione: <i>Hai un nonno italiano? Di dov'è?</i></div>
<div class="box"><h4>AUDIO</h4>Traccia 02.1 Tre dialoghi (lento e naturale) · Traccia 02.2 La H muta · Traccia 02.3 Le nazionalità</div>""")

    # Page 2
    tf = [("Júlia è di Rio de Janeiro.", "F"), ("Júlia parla inglese e un po' di spagnolo.", "V"), ("La mamma di Marco è francese.", "V"),
          ("Davide è di Bologna.", "F"), ("Bia, l'amica di Davide, è brasiliana.", "V"), ("Júlia ha un passaporto italiano.", "V")]
    tfr = "".join(f'<tr><td>{i+1}. {s}</td><td style="width:24mm;text-align:center;white-space:nowrap">{ch(["V", "F"], a)}</td></tr>' for i, (s, a) in enumerate(tf))
    gp = [("Davide: Senti,", "hai", "la password del Wi-Fi?"), ("Júlia: No, non", "ho", "la password."), ("Davide: Io", "ho", "un'amica brasiliana."),
          ("Signora Rossi:", "ha", "un documento?")]
    gl = [f'<li value="{i+1}">{a} {A(x, "min-width:16mm")} {c}</li>' for i, (a, x, c) in enumerate(gp)]
    b.page(f"""{sec(2, "Ascolto: di dove sei?", "10 min")}
<p>È il secondo giorno di Júlia a Bologna. Parla con Marco allo studio, con Davide, il vicino, e con la signora Rossi per il contratto della casa.</p>
{audiocard(["02.1 · SLOW", "02.1 · NATURAL"])}
{sub("A", "Ascolta. Vero (V) o falso (F)?", "4 min", "02.1 · SLOW")}
<table class="ck" style="margin:0">{tfr}</table>
{sub("B", "Ascolta di nuovo e completa con il verbo avere.", "4 min", "02.1 · NATURAL")}
{twocol(gl, 3)}
{sub("C", "Perché la signora Rossi dice «Lei è italiana e brasiliana»?", "2 min")}
<div class="wline">{R("Perché Júlia ha la cittadinanza (e il passaporto) italiana: il nonno è di Treviso.")}</div>""",
    26, """<ol><li>A: versione <b>lenta</b>. Correggere le frasi false: 1 → <i>di Belo Horizonte</i>; 4 → <i>di Napoli</i>.</li>
<li>B: versione <b>naturale</b>. Far notare che si scrive <b>ho, hai, ha</b> ma si dice «o, ai, a».</li>
<li>C: <i>bolognese</i> = di Bologna (anche <i>napoletano</i>, <i>milanese</i>, <i>romano</i>). <i>Mio nonno</i> = solo da capire, i possessivi arrivano più avanti.</li></ol>""")

    # Page 3
    asks = [("tu", "Di dove sei?", "Sono di Belo Horizonte."), ("Lei", "Di dov'è?", "Sono di Treviso."), ("tu", "Sei italiano?", "No, sono brasiliano.")]
    nat = [("italiano", "italiana"), ("brasiliano", "brasiliana"), ("spagnolo", "spagnola"), ("tedesco", "tedesca"), ("americano", "americana")]
    nate = ["francese", "inglese", "portoghese", "giapponese", "cinese"]
    av = [("io", "ho", "Ho il passaporto."), ("tu", "hai", "Hai la password?"), ("lui / lei", "ha", "Davide ha un'amica brasiliana."), ("Lei (formale)", "ha", "Ha un documento?")]
    rules = [("Città:", "Sono di Napoli.", "Sono da Napoli."), ("Una donna del Portogallo è", "portoghese", "portoghesa"),
             ("Un uomo della Spagna è", "spagnolo", "spagnola"), ("La H di ho, hai, ha", "non si pronuncia", "si pronuncia")]
    def rule(i, s, right, wrong):
        o = [right, wrong] if i % 2 == 0 else [wrong, right]
        o = [R(f"<u>{x}</u>") if (T and x == right) else x for x in o]
        return f"<li>{s} <b><i>{o[0]}</i></b> / <b><i>{o[1]}</i></b></li>"
    ta = "".join(f"<tr><td class='small'>{p}</td><td><b>{q}</b></td><td>{r}</td></tr>" for p, q, r in asks)
    tn = "".join(f"<tr><td>{m}</td><td>{f}</td></tr>" for m, f in nat)
    tv = "".join(f"<tr><td>{p}</td><td><b>{v}</b></td><td class='small'>{e}</td></tr>" for p, v, e in av)
    b.page(f"""{sec(3, "Grammatica: di dove sei? · nazionalità · avere", "10 min")}
{sub("A", "Chiedere e dire l'origine.", "2 min")}
<table style="margin:0"><tr><th></th><th>Domanda</th><th>Risposta</th></tr>{ta}</table>
{sub("B", "Le nazionalità: maschile e femminile.", "4 min")}
<div class="two"><div><table style="margin:0"><tr><th>-o (uomo)</th><th>-a (donna)</th></tr>{tn}</table></div>
<div><table style="margin:0"><tr><th>-e (uomo e donna)</th></tr>{"".join(f"<tr><td>{x}</td></tr>" for x in nate)}</table>
<table style="margin-top:2mm"><tr><th colspan="3">avere</th></tr>{tv}</table></div></div>
{sub("C", "Scegli l'opzione corretta.", "4 min")}
<ol>{"".join(rule(i, *r) for i, r in enumerate(rules))}</ol>
<div class="box"><h4>REGOLA</h4>Città → <b>di</b>: <i>Sono di Bologna.</i> Paese → nazionalità: <i>Sono brasiliana.</i> Le nazionalità si scrivono con la <b>lettera minuscola</b>: <i>italiano</i>, non <i>Italiano</i>. La lingua = la forma maschile: <i>parlo italiano, inglese, spagnolo</i>.</div>""",
    23, """<ol><li>B: chiedere allo studente: <i>E tu? Sei brasiliano o brasiliana?</i> Le nazionalità in <b>-e</b> non cambiano.</li>
<li>Avere: i brasiliani pensano a «tenere», ma <i>tenere</i> = avere in mano. Per il possesso si usa <b>avere</b>: <i>Io tengo</i> ✗ → <i>Ho</i>.</li></ol>""")

    # Page 4
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Sono de São Paulo.</td><td><b>Sono di São Paulo.</b></td><td>In italiano: <i>di</i>.</td></tr>
<tr><td>Io tengo un passaporto.</td><td><b>Ho un passaporto.</b></td><td>Possesso = <i>avere</i>.</td></tr>
<tr><td>Lei è francesa.</td><td><b>Lei è francese.</b></td><td>-e: uguale per uomo e donna.</td></tr>
<tr><td>Sono Brasiliana.</td><td><b>Sono brasiliana.</b></td><td>Nazionalità con la minuscola.</td></tr>
<tr><td>[h]o un'amica.</td><td><b>Ho un'amica.</b> («o»)</td><td>La H è muta.</td></tr></table></div>
<div style="height:2mm"></div>
{sec(4, "Laboratorio di pronuncia", "5 min")}
{audiocard(["02.2", "02.3"])}
{sub("A", "La H muta. Ascolta e ripeti: ho e o hanno lo stesso suono.", "2 min", "02.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S022)}</div>
{sub("B", "Le nazionalità. Ascolta e ripeti. Attenzione all'accento: italiAno, franCEse.", "3 min", "02.3")}
<div class="bank" style="font-weight:600">{" &nbsp;·&nbsp; ".join(S023)}</div>""",
    40, """<ol><li>Errori: <i>de</i> per <i>di</i> è molto frequente perché le due lingue sono vicine. Correggere sempre.</li>
<li>4A: in italiano la H non ha mai suono. Serve solo nella scrittura: <i>ho</i> (verbo) ≠ <i>o</i> (congiunzione), <i>ha</i> ≠ <i>a</i>.</li>
<li>4B: l'accento cade sulla penultima sillaba: brasili<b>A</b>no, ingl<b>E</b>se, giappon<b>E</b>se. Attenzione: <i>tedesco</i> ha il suono K (non «tedeʃo»).</li></ol>""")

    # Page 5
    gw = ["italiana", "francese", "spagnolo", "inglese", "tedesca", "portoghese"]
    gs = [("Marco è italiano. Sua sorella è", ""), ("Pierre è francese. Sua moglie è", ""), ("Carmen è spagnola. Suo marito è", ""),
          ("Emma è inglese. Suo padre è", ""), ("Hans è tedesco. Sua figlia è", ""), ("João è portoghese. Sua madre è", "")]
    gl5 = [f'<li value="{i+1}">{a} {A(gw[i], "min-width:22mm")}.</li>' for i, (a, c) in enumerate(gs)]
    hv = [("Io", "ho", "un'amica italiana."), ("Tu", "hai", "il passaporto?"), ("Davide", "ha", "un problema con il Wi-Fi."), ("Signora, Lei", "ha", "un documento?")]
    hl5 = "".join(f'<li>{a} {A(x, "min-width:16mm")} {c}</li>' for a, x, c in hv)
    b.page(f"""{sec(5, "Pratica", "8 min")}
{sub("A", "Completa con la nazionalità.", "3 min")}
{twocol(gl5, 4)}
{sub("B", "Completa con il verbo avere.", "2 min")}
<ol>{hl5}</ol>
{sub("C", "Presentati. Scrivi 3 frasi.", "3 min")}
<div class="msg" style="max-width:none">Mi chiamo <span class="blank" style="min-width:30mm">&nbsp;</span>. Sono <span class="blank" style="min-width:30mm">&nbsp;</span> (nazionalità). Sono di <span class="blank" style="min-width:30mm">&nbsp;</span> (città).<br>
<div style="margin-top:2mm">{R("Esempio: Mi chiamo Ana. Sono brasiliana. Sono di Curitiba.")}</div></div>""",
    22, """<ol><li>A: <i>sua sorella, suo marito</i> = solo da capire. Ricordare: le nazionalità in <b>-e</b> non cambiano (frasi 2, 4, 6).</li>
<li>C: lo studente legge ad alta voce. Chiedere: <i>E la tua famiglia? Di dov'è?</i></li></ol>""")

    # Page 6
    cards = [("Pierre Martin", "francese", "Lione", "tu", "un amico di Marco"), ("Signor Kenji Tanaka", "giapponese", "Osaka", "Lei", "un cliente dello studio"),
             ("Emma Smith", "inglese", "Londra", "tu", "una studentessa"), ("Signora Carmen López", "spagnola", "Siviglia", "Lei", "una nuova vicina")]
    cd = "".join(f'<div class="ad" style="flex:1"><b class="t">{n}</b><span class="small">{w}</span><br>Nazionalità: <b>{na}</b><br>Città: <b>{c}</b><br>{R("→ " + ("Di dove sei?" if tl == "tu" else "Di dov&#39;è?"))}</div>' for n, na, c, tl, w in cards)
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Carte d'identità. L'insegnante è una di queste persone. Fai domande: tu o Lei? Poi scambiate i ruoli.", "7 min")}
<div style="display:flex;gap:2.5mm;margin:1mm 0 2mm">{cd}</div>
<div class="bank" style="background:#fff">Come ti chiami? / Come si chiama? · Di dove sei? / Di dov'è? · Sei…? / È…? · Sono di… · Sono…</div>
{sub("B", "E tu? Rispondi all'insegnante.", "5 min")}
<ol style="line-height:1.65"><li>Di dove sei? Dov'è la tua città?</li><li>Hai un nonno o una nonna di un altro paese? Di dov'è?</li><li>Che lingue parli?</li><li>Hai un amico o un'amica straniera? Di dov'è?</li></ol>""",
    30, """<ol><li>A: l'insegnante sceglie una carta in segreto. Lo studente fa domande e indovina la persona. Con il signor Tanaka e la signora López si usa il <b>Lei</b>.</li>
<li>B: domanda 2 per la realtà brasiliana (cittadinanza italiana). Correggere <i>de / di</i> e l'accordo della nazionalità.</li></ol>""")

    # Page 7
    pc = [("Unità 01", "So salutare e presentarmi (tu e Lei)."), ("Unità 02", "So dire di dove sono: Sono di…"),
          ("Unità 02", "So dire e chiedere la nazionalità."), ("Unità 02", "So usare ho, hai, ha.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Sono de Recife.", "Sono di Recife."), ("Maria è portoghesa.", "Maria è portoghese."), ("Io tengo un'amica italiana.", "Ho un'amica italiana."),
          ("Paolo è Italiano.", "Paolo è italiano."), ("Signora, tu hai un documento?", "Signora, Lei ha un documento?"), ("Julia è brasiliano.", "Julia è brasiliana.")]
    hl = "".join(f'<li>{s} {R("→ " + a) if T else ""}</li>' for s, a in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:17mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori.</b> In ogni frase c'è un errore.</p>
<ol>{hl}</ol>
<p style="margin-top:2mm"><b>2. La mia famiglia.</b> Scrivi 3–4 frasi su due persone della tua famiglia o due amici: come si chiamano, di dove sono, la nazionalità.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    22, """<p>Prossima lezione: controllare le correzioni. Poi l'insegnante fa domande sulle persone del testo: <i>Di dov'è tua madre? È brasiliana?</i></p>""")

    b.extra("Trascrizioni audio", f"""
{sub("02.1", "Di dove sei? (lento e naturale)")}
<p style="line-height:1.45">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("02.2", "La H muta")}
<p>{" · ".join(S022)}</p>
{sub("02.3", "Le nazionalità")}
<p>{" · ".join(S023)}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A1 Essenziale 02 - Di dove sei")
