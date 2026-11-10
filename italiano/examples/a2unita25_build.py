# Speak! Ponte A2 - Unità 25 "Me lo presti?" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 25", audio_json=os.path.join(HERE, "audio_it-a2-unita-25.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la borsa frigo", "borsa frigo"), ("B", "l'ombrellone", "ombrellone"), ("C", "la sdraio", "sdraio"), ("D", "la bici", "bici"),
          ("E", "le chiavi", "chiavi"), ("F", "la cartolina", "cartolina"), ("G", "il computer", "computer"), ("H", "la gomma bucata", "gomma bucata")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-25"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["25.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S252 = [x.split(": ", 1)[1] for x in _r["25.2 Ripeti"].split("\n")]
S253 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["25.3 Che cosa"].split("\n")]


def _key(w):
    if w.startswith("l'"):
        return w[2:].lower()
    a, _, rest = w.partition(" ")
    return (rest if a in ("la", "il", "i", "gli", "lo", "le") else w).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 25", "Me lo presti?", "Prestare e chiedere in prestito · <b>me lo · te la · glielo · ce la</b>",
                       [("SAI FARE", "chiedere una cosa in prestito, prestare o dire di no con gentilezza, promettere di restituire, capire i pronomi combinati"),
                        ("LINGUA", "Me la presti? — Te la presto. · Te lo do io. · Te le lascio. · Glielo riporto domenica."),
                        ("PRONUNCIA", "il ritmo dei pronomi: me lo PRÈSti? te lo PRÈSto")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: mi serve…", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Presti le tue cose agli amici? Che cosa sì e che cosa no?</li><li>Che cosa hai chiesto in prestito l'ultima volta? A chi?</li><li>Qualcuno non ti ha mai restituito qualcosa?</li></ol>""",
    28, """<ol><li>A: <i>la sdraio</i> è femminile (la sedia a sdraio); <i>la gomma bucata</i> = la ruota senza aria; <i>prestare</i> = dare per un po' di tempo; <i>restituire / riportare</i> = dare indietro.</li>
<li>B: domanda 3: tutti hanno una storia (libri, soldi, ombrelli!). Far raccontare al passato prossimo.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: le cose da prestare</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Dalla signora Rossi · la telefonata di Bruno</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>I pronomi combinati (ricettivo)</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Me lo, te lo, glielo, ce lo, ve lo</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Il ritmo dei pronomi · che cosa?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Abbina · rispondi con te lo / te la · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Me lo presti? · le mie regole</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine agosto. Sabato Júlia e Marco partono per una settimana a Rimini: hanno affittato una casetta vicino al mare (unità 26). Júlia chiede alla signora Rossi la borsa frigo: <i>te la presto volentieri</i>. La signora Rossi, che da bambina andava a Rimini ogni estate (unità A2 02), le dà anche l'ombrellone dalla cantina: <i>te lo do io</i>. Júlia: <i>Glielo riporto domenica prossima</i>; promette una cartolina (<i>gliela mando il primo giorno</i>). La macchina? <i>La mamma di Marco ce la presta.</i> La sera Bruno chiede la bici (la sua ha una gomma bucata): <i>te la presto, ma trattala bene</i>; le chiavi: <i>te le lascio dalla signora Rossi</i>. Il computer no: <i>non te lo presto</i>, Júlia lo porta con sé. Bruno ha un esame a settembre (unità 20).</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Nel portoghese parlato i pronomi combinati non si usano (<i>Me empresta? — Empresto.</i> / <i>Te empresto ela.</i>): lo studente omette il pronome (<i>Sì, presto</i>) o lo mette nell'ordine sbagliato (<i>lo te presto</i>, <i>mi lo presti</i>). In questa unità l'obiettivo è <b>capire</b> e usare <i>me lo / te lo / me la / te la</i>; <i>glielo</i> solo in comprensione.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Sulla Riviera romagnola (Rimini, Riccione, Cesenatico) le spiagge sono quasi tutte <b>stabilimenti balneari</b>: si paga ogni giorno o ogni settimana un <b>ombrellone</b> con due lettini, in file ordinate e colorate. Le spiagge libere sono poche. Molte famiglie italiane tornano nello stesso stabilimento per anni: il bagnino conosce tutti per nome.</div>
<div class="box"><h4>AUDIO</h4>Traccia 25.1 I due dialoghi (lento e naturale) · Traccia 25.2 Ascolta e ripeti · Traccia 25.3 Che cosa?</div>""")

    # Page 2
    p1 = [("Júlia e Marco vanno a Rimini per", "una settimana"), ("La signora Rossi presta a Júlia la borsa frigo e", "l'ombrellone"),
          ("L'ombrellone è in", "cantina"), ("Júlia promette di mandarle", "una cartolina"), ("La macchina la presta", "la mamma di Marco")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("La bici di Bruno ha una gomma bucata.", "V"), ("Júlia non presta la bici a Bruno.", "F"), ("Júlia lascia le chiavi alla signora Rossi.", "V"),
          ("Júlia presta il computer a Bruno.", "F"), ("Bruno deve studiare per un esame.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: prima del mare", "10 min")}
{audiocard(["25.1 · SLOW", "25.1 · NATURAL"])}
{sub("A", "Prima parte. Júlia bussa alla porta della signora Rossi. Completa.", "4 min", "25.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Bruno telefona a Júlia. Vero (V) o falso (F)?", "4 min", "25.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Perché Júlia non presta il computer a Bruno?", "2 min")}
<div class="wline">{R("Perché lo porta con sé a Rimini.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Júlia dà del <i>Lei</i> alla signora Rossi (<i>Posso chiederLe…? Glielo riporto</i>); la signora le dà del <i>tu</i>.</li>
<li>B: frase 4: <i>quello non te lo presto</i>: far notare il tono deciso ma gentile.</li></ol>""")

    # Page 3
    rules = [("<i>Mi presti la bici? — <b>Te la</b> presto.</i> <i>La</i> è", ["la bici", "Júlia"], "la bici"),
             ("<i>Te la presto</i> = presto", ["la bici a te", "te alla bici"], "la bici a te"),
             ("Nei pronomi combinati <i>mi</i> e <i>ti</i> diventano", ["me e te", "mi e ti"], "me e te"),
             ("Prima viene il pronome", ["indiretto (a chi?)", "diretto (che cosa?)"], "indiretto (a chi?)"),
             ("<i><b>Glielo</b> riporto.</i> = riporto", ["l'ombrellone a Lei", "Lei all'ombrellone"], "l'ombrellone a Lei"),
             ("<i>Gli / le / Le</i> + <i>lo</i> diventa", ["glielo (una parola)", "gli lo"], "glielo (una parola)")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Mi presti il computer? — No, non", ["te lo", "lo te"], "te lo", "presto."), ("Mi lasci le chiavi? — Sì,", ["te le", "te la"], "te le", "lascio."),
          ("Mi dai la borsa frigo? — Certo,", ["te la", "te lo"], "te la", "do."), ("Chi vi presta la macchina? —", ["Ce la", "Ce lo"], "Ce la", "presta la mamma di Marco.")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: i pronomi combinati", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Ha una borsa frigo? — <b>Te la</b> presto volentieri. · L'ombrellone? <b>Te lo</b> do io. · Mi presti la bici? — <b>Te la</b> presto.<br>
2. Le chiavi? <b>Me le</b> lasci? — <b>Te le</b> lascio dalla signora Rossi. · Il computer? Non <b>te lo</b> presto.<br>
3. L'ombrellone? <b>Glielo</b> riporto domenica. · La cartolina? <b>Gliela</b> mando il primo giorno. · La macchina? <b>Ce la</b> presta la mamma di Marco.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4>Indiretto + diretto: <b>me lo, te la, ce li, ve le</b> (mi → me, ti → te, ci → ce, vi → ve). <b>gli / le / Le</b> + lo, la, li, le → <b>glielo, gliela, glieli, gliele</b> (una parola). Il diretto (<i>lo, la, li, le</i>) dipende dalla cosa: <i>la bici → la, le chiavi → le</i>. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: scrivere alla lavagna <i>presto + la bici + a te</i> → <i>te la presto</i>. Poi cancellare le parole lunghe e lasciare i pronomi.</li>
<li>C: obiettivo ricettivo: lo studente deve <b>capire</b> a che cosa si riferisce il pronome (genere e numero della cosa).</li></ol>""")

    grammar_ref_it.pronomi_combinati(b)

    # Page 5
    opts3 = [["la bici", "il libro"], ["il caricabatterie", "le chiavi"], ["le chiavi", "il computer"],
             ["l'ombrellone", "la borsa frigo"], ["i piatti", "la macchina"], ["la cartolina", "il regalo"]]
    ans3 = ["la bici", "il caricabatterie", "le chiavi", "l'ombrellone", "i piatti", "la cartolina"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Mi lo presti?</td><td><b>Me lo presti?</b></td><td><i>mi</i> → <i>me</i> davanti a <i>lo</i>.</td></tr>
<tr><td>Lo te presto.</td><td><b>Te lo presto.</b></td><td>Prima l'indiretto.</td></tr>
<tr><td>Sì, presto. (la bici)</td><td><b>Sì, te la presto.</b></td><td>Il pronome serve.</td></tr>
<tr><td>Te lo presto. (la bici)</td><td><b>Te la presto.</b></td><td><i>la bici</i> → <i>la</i>.</td></tr>
<tr><td>Gli lo riporto.</td><td><b>Glielo riporto.</b></td><td>Una parola sola.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["25.2", "25.3"])}
{sub("A", "Ascolta e ripeti. I pronomi non hanno accento: si dicono veloci, attaccati al verbo.", "2 min", "25.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S252)}</div>
{sub("B", "Che cosa? Ascolta e scegli la cosa giusta.", "2 min", "25.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 4: l'errore più frequente; far controllare sempre il genere della cosa.</li>
<li>4A: far battere le mani solo sulla sillaba accentata del verbo: <i>te lo PRE-sto</i>.</li>
<li>4B: decidere con il genere e il numero: <i>la → la bici</i>, <i>le → le chiavi</i>, <i>li → i piatti</i>.</li></ol>""")

    # Page 6
    mt = [("Mi presti il libro?", "Sì, te lo presto."), ("Mi presti la penna?", "Sì, te la presto."),
          ("Mi presti i soldi?", "No, non te li presto!"), ("Mi presti le scarpe?", "Sì, te le presto.")]
    mtl = "".join(f"<li>{q} {A(a, 'min-width:46mm')}</li>" for q, a in mt)
    rp = [("Mi dai il caricabatterie? (sì)", "Sì, te lo do."), ("Mi presti la macchina? (no)", "No, non te la presto."),
          ("Mi lasci le chiavi? (sì)", "Sì, te le lascio."), ("Mi presti il computer? (no)", "No, non te lo presto.")]
    rpl = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in rp)
    wb = [("prestare", "il prestito"), ("restituire", "la restituzione"), ("affittare", "l'affitto"), ("riparare", "la riparazione")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Rispondi con il pronome giusto: te lo, te la, te li, te le.", "3 min")}
<ol style="line-height:1.7">{mtl}</ol>
{sub("B", "Rispondi sì o no, con il pronome.", "4 min")}
<ol style="line-height:1.45">{rpl}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: i soldi → <i>li</i>; le scarpe → <i>le</i>. Far notare che <i>te</i> non cambia, cambia solo il diretto.</li>
<li>C: <i>in prestito</i> (chiedere / prendere in prestito); <i>l'affitto</i> come la casetta di Rimini.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Me lo presti? Vai al mare (o in montagna) per una settimana e non hai niente. Chiedi all'insegnante cinque cose in prestito. L'insegnante presta alcune cose e altre no, e spiega perché. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Mi presti…? · Me lo / me la presti? · Te lo presto volentieri. · Mi dispiace, non te lo presto: mi serve. · Quando me lo riporti? · Te lo riporto lunedì. · Trattalo bene! · Grazie mille, sei un tesoro!</div>
{sub("B", "Le mie regole. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Che cosa presti facilmente? Che cosa non presti mai?</li><li>Presti la macchina o la bici agli amici?</li><li>Presti i libri? Te li restituiscono sempre?</li><li>Hai mai perso o rotto una cosa che qualcuno ti ha prestato?</li><li>Nel tuo palazzo i vicini si prestano le cose?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: l'insegnante risponde sempre con il pronome combinato (<i>Te la presto, ma…</i>), così lo studente lo sente molte volte; lo studente può rispondere in modo più semplice.</li>
<li>B: domanda 4: passato prossimo + imperfetto (unità 03).</li></ol>""")

    # Page 8
    pc = [("A2 · 24", "So usare qualche, ogni, nessuno, niente."), ("A2 · 25", "So chiedere una cosa in prestito."),
          ("A2 · 25", "So prestare o dire di no con gentilezza."), ("A2 · 25", "So usare me lo, te lo, te la."),
          ("A2 · 25", "Capisco glielo, gliela, ce la.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Mi lo presti?", "Me lo presti?"), ("Te la presto volentieri. (la bici)", "✓"),
          ("Lo te do domani.", "Te lo do domani."), ("Mi presti la penna? — Sì, te lo presto.", "Sì, te la presto."),
          ("Gli lo riporto domenica.", "Glielo riporto domenica."), ("Le chiavi? Te le lascio.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Un messaggio a un amico (50–75 parole).</b> Parti per una settimana. Scrivi a un amico: che cosa gli chiedi in prestito? Che cosa gli presti tu (chiavi, piante, bici)? Quando glielo restituisci? Usa almeno tre volte <i>me lo / te lo / te la / te le</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il messaggio; l'insegnante chiede <i>E quando me lo restituisci?</i> Unità 26: <i>Una casetta al mare</i> (nomi alterati, plurali irregolari).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("25.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("25.2", "Ascolta e ripeti")}
<p>{" · ".join(S252)}</p>
{sub("25.3", "Che cosa?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S253))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 25 - Me lo presti?")
