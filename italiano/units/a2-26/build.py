# Speak! Ponte A2 - Unità 26 "Una casetta al mare" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 26", audio_json=os.path.join(HERE, "audio_it-a2-unita-26.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "la casetta", "casetta"), ("B", "il terrazzino", "terrazzino"), ("C", "il lettone", "lettone"), ("D", "i lettini", "lettini"),
          ("E", "la crema solare", "crema solare"), ("F", "il dito", "dito"), ("G", "le uova", "uova"), ("H", "il temporale", "temporale")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-26"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["26.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S262 = [x.split(": ", 1)[1] for x in _r["26.2 Ripeti"].split("\n")]
S263 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["26.3 Piccolo o grande"].split("\n")]


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
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 26", "Una casetta al mare", "Vacanze al mare · <b>casetta · lettone · tempaccio · le braccia · le uova</b>",
                       [("SAI FARE", "descrivere una casa delle vacanze, parlare della spiaggia e del tempo, dire che cosa ti fa male, scrivere una cartolina"),
                        ("LINGUA", "una casetta, un lettone, che tempaccio! · le braccia, le dita, le ginocchia, le uova"),
                        ("PRONUNCIA", "le doppie nei suffissi: casetta, lettone, tempaccio")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: al mare", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Preferisci il mare, la montagna o la città? Perché?</li><li>In vacanza dormi in albergo, in una casa in affitto o da amici?</li><li>Ti sei mai scottato al sole? Che cosa hai fatto?</li></ol>""",
    28, """<ol><li>A: <i>il lettino</i> = il letto della spiaggia (i lettini sotto l'ombrellone); <i>il lettone</i> = il letto matrimoniale grande; <i>scottarsi</i> = diventare rossi per il sole.</li>
<li>A: <i>il dito → le dita</i>, <i>l'uovo → le uova</i>: anticipare che il plurale è strano (pagina 3).</li>
<li>B: domanda 3: passato prossimo con <i>essere</i> (<i>mi sono scottato/a</i>).</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: la casa e la spiaggia</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>La casetta · in spiaggia · la cartolina</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Nomi alterati e plurali in -a</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>-ino, -etto, -one, -accio · le braccia, le uova</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Le doppie nei suffissi · piccolo o grande?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Altera i nomi · i plurali · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>La mia casa delle vacanze · al mare</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Fine agosto, Rimini. Júlia e Marco arrivano alla casetta in affitto (unità 25): un giardinetto, un cucinino piccolissimo, un lettone enorme e un terrazzino da cui si vede il mare. In spiaggia usano l'ombrellone della signora Rossi. Martedì Júlia ha le braccia e le ginocchia rosse (niente crema!) e Marco, dopo la pallavolo, ha due dita gonfie. La sera Júlia compra sei uova per una frittatina; Marco ha fame e vuole un frittatone. Mercoledì c'è un temporale e Júlia scrive la cartolina promessa alla signora Rossi: <i>tutti i vicini di spiaggia ce lo invidiano</i> (l'ombrellone), <i>un abbraccione</i>.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Il brasiliano usa il diminutivo continuamente (<i>cafezinho, rapidinho</i>) e tende a inventare forme in <i>-ino</i>: in italiano gli alterati sono meno frequenti e molti sono "falsi" (<i>panino, bottone</i>). Poi il plurale: <i>os braços, os dedos, os ovos</i> sono maschili, quindi lo studente dice <i>i bracci, i diti, gli uovi</i> e <i>le uova sono freschi</i>. Insistere sul femminile: <i>le braccia rosse</i>.</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>Rimini è la capitale delle vacanze al mare dagli anni Cinquanta: 15 km di spiaggia, centinaia di stabilimenti numerati, il lungomare, le discoteche. È anche la città di Federico Fellini (il film <i>Amarcord</i> racconta la Rimini della sua infanzia). Il cibo tipico è la <b>piadina romagnola</b>, che si mangia anche sotto l'ombrellone.</div>
<div class="box"><h4>AUDIO</h4>Traccia 26.1 I tre dialoghi (lento e naturale) · Traccia 26.2 Ascolta e ripeti · Traccia 26.3 Piccolo o grande?</div>""")

    # Page 2
    p1 = [("La casetta ha un piccolo giardino:", "un giardinetto"), ("La cucina è piccolissima: è", "un cucinino"),
          ("Nella camera c'è", "un lettone"), ("Dal terrazzino si vede", "il mare")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("Júlia ha le braccia rosse.", "V"), ("Júlia ha messo la crema.", "F"), ("A Marco fanno male due dita.", "V"),
          ("Júlia ha comprato dodici uova.", "F"), ("Marco vuole una frittata grande.", "V")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: una settimana a Rimini", "10 min")}
{audiocard(["26.1 · SLOW", "26.1 · NATURAL"])}
{sub("A", "Prima parte. Júlia e Marco arrivano alla casetta. Completa.", "3 min", "26.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. In spiaggia. Vero (V) o falso (F)?", "4 min", "26.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Terza parte. La cartolina. Che tempo fa mercoledì? Come stanno Júlia e Marco?", "3 min")}
<div class="wline">{R("C'è un temporale: piove e tira vento.")}</div>
<div class="wline">{R("Marco ha due dita gonfie, Júlia le braccia rosse, ma sono felici.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Far notare che ogni parola con il suffisso ha la sua forma normale: <i>giardino, cucina, letto, terrazzo</i>.</li>
<li>B: frase 4: <i>sei uova</i>, non dodici. Frase 5: <i>un frittatone</i> = una frittata grande.</li>
<li>C: nella cartolina Júlia dà del <i>Lei</i> alla signora Rossi (<i>il Suo ombrellone</i>).</li></ol>""")

    # Page 3
    rules = [("<i>Una casetta</i> è una casa", ["piccola e carina", "grande"], "piccola e carina"),
             ("<i>Un lettone</i> è un letto", ["piccolo", "grande"], "grande"),
             ("<i>Che tempaccio!</i> Il tempo è", ["bello", "brutto"], "brutto"),
             ("<i>Il braccio</i> al plurale è", ["le braccia", "i bracci"], "le braccia"),
             ("<i>Le braccia</i>, <i>le dita</i>, <i>le uova</i> sono", ["femminili", "maschili"], "femminili"),
             ("Quindi si dice <i>le braccia</i>", ["rosse", "rossi"], "rosse")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Mi fanno male due", ["dita", "diti"], "dita", "."), ("Per la frittata servono quattro", ["uova", "uovi"], "uova", "."),
          ("Dopo la corsa mi fanno male", ["le ginocchia", "i ginocchi"], "le ginocchia", "."), ("Abbiamo un piccolo giardino: è un", ["giardinetto", "giardinone"], "giardinetto", ".")]
    ccl = "".join(f"<li>{a} {ch(o, r)}{z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: nomi alterati e plurali in -a", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. Una <b>casetta</b> bianca con un <b>giardinetto</b>. · La cucina è un <b>cucinino</b>. · C'è anche un <b>terrazzino</b>.<br>
2. C'è un <b>lettone</b> enorme! · Facciamo un <b>frittatone</b>! · Un <b>abbraccione</b>. · Oggi c'è un <b>tempaccio</b>.<br>
3. Guarda le mie <b>braccia</b>: sono tutte rosse. · Mi fanno male due <b>dita</b>. · Ho comprato sei <b>uova</b>. · Anche le <b>ginocchia</b> sono rosse.</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>-ino, -etto</b> = piccolo, carino (<i>casetta, terrazzino</i>) · <b>-one</b> = grande (<i>lettone</i>) · <b>-accio</b> = brutto (<i>tempaccio</i>). Alcuni nomi hanno il plurale in <b>-a</b> e sono <b>femminili</b>: <i>il braccio → le braccia rosse, il dito → le dita, l'uovo → le uova, il ginocchio → le ginocchia</i>. Tutto: pagina 4.</div>""",
    22, """<ol><li>B: scrivere alla lavagna tre colonne (piccolo · grande · brutto) e far mettere le parole del dialogo nella colonna giusta.</li>
<li>B: frasi 4–6: chiedere di leggere ad alta voce <i>le braccia sono rosse</i>: l'articolo e l'aggettivo sono femminili.</li></ol>""")

    grammar_ref_it.nomi_alterati(b)

    # Page 5
    opts3 = [["piccolo", "grande", "brutto"]] * 6
    ans3 = ["piccolo", "grande", "brutto", "piccolo", "grande", "brutto"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Ho i bracci rossi.</td><td><b>Ho le braccia rosse.</b></td><td>Plurale in <i>-a</i>, femminile.</td></tr>
<tr><td>Mi fanno male due diti.</td><td><b>Mi fanno male due dita.</b></td><td><i>il dito → le dita</i>.</td></tr>
<tr><td>Ho comprato sei uovi.</td><td><b>Ho comprato sei uova.</b></td><td><i>l'uovo → le uova</i>.</td></tr>
<tr><td>Le uova sono freschi.</td><td><b>Le uova sono fresche.</b></td><td>Aggettivo femminile.</td></tr>
<tr><td>Vuoi un pane piccolo? (panino)</td><td><b>Vuoi un panino?</b></td><td><i>Panino</i> è una parola nuova.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["26.2", "26.3"])}
{sub("A", "Ascolta e ripeti. Nei suffissi la consonante doppia è lunga: casetta, lettone, tempaccio.", "2 min", "26.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S262)}</div>
{sub("B", "Piccolo, grande o brutto? Ascolta e scegli.", "2 min", "26.3")}
{twocol([f'<li value="{i+1}">{ch(o, a)}</li>' for i, (o, a) in enumerate(zip(opts3, ans3))], 4)}""",
    28, """<ol><li>Errori: riga 5: lo studente brasiliano tende a capire <i>panino</i> come <i>pãozinho</i>; in italiano è il sandwich.</li>
<li>4A: far tenere un attimo la doppia: <i>caset-ta</i>, non <i>caseta</i> (in portoghese le doppie non si pronunciano).</li>
<li>4B: 1 giardinetto · 2 lettone · 3 tempaccio · 4 tavolino · 5 bicchierone · 6 parolacce.</li></ol>""")

    # Page 6
    al = [("una casa piccola e carina", "una casetta"), ("un letto grande", "un lettone"), ("un tempo brutto", "un tempaccio"),
          ("un tavolo piccolo", "un tavolino"), ("una parola brutta", "una parolaccia"), ("un bicchiere grande", "un bicchierone")]
    all_ = "".join(f"<li>{q} → {A(a, 'min-width:34mm')}</li>" for q, a in al)
    pl = [("Dopo la pallavolo mi fanno male le", "(mano)", "mani"), ("Ho le", "(braccio) rosse.", "braccia"),
          ("Per il dolce servono tre", "(uovo).", "uova"), ("Al mare ci sono molti", "(uomo) con la pancia.", "uomini"),
          ("Ho comprato due", "(paio) di occhiali.", "paia")]
    pll = "".join(f"<li>{a} {A(r, 'min-width:22mm')} {z}</li>" for a, z, r in pl)
    wb = [("il sole", "soleggiato"), ("il vento", "ventoso"), ("la pioggia", "piovoso"), ("la nuvola", "nuvoloso")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:28mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Una parola sola. Scrivi il nome alterato.", "3 min")}
<ol style="line-height:1.7">{all_}</ol>
{sub("B", "Scrivi il plurale.", "4 min")}
<ol style="line-height:1.7">{pll}</ol>
{sub("C", "Costruisci le parole. Dal nome all'aggettivo: che tempo fa?", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: accettare anche <i>una casina</i>; far notare che <i>-etto</i> e <i>-ino</i> sono spesso possibili tutti e due, ma l'uso decide.</li>
<li>B: <i>le mani</i> e <i>gli uomini</i> sono irregolari ma non in <i>-a</i>; <i>le paia</i> è come <i>le uova</i>.</li>
<li>C: <i>Oggi è nuvoloso, domani sarà soleggiato</i> (futuro, unità 22).</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "La mia casa delle vacanze. Descrivi all'insegnante una casa per le vacanze (vera o dei sogni): dov'è, com'è, che cosa c'è dentro e fuori. Usa almeno quattro nomi alterati. L'insegnante fa domande. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>una casetta · una villetta · un terrazzino · un giardinetto · un cucinino · un lettone · un salottino · un tavolino · un divanetto · È piccolina ma carinissima! · Da qui si vede il mare / la montagna.</div>
{sub("B", "Al mare. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Com'è la spiaggia che preferisci? Spiaggia libera o stabilimento?</li><li>Che cosa porti sempre in spiaggia?</li><li>In vacanza ti sei mai fatto male? Che cosa ti faceva male?</li><li>Hai mai trovato un tempaccio in vacanza? Che cosa hai fatto?</li><li>Scrivi ancora le cartoline? A chi?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: correggere solo gli alterati inventati (<i>un divanino</i> va bene, <i>un panone</i> no); lodare <i>-issimo</i> (<i>carinissima</i>).</li>
<li>B: domanda 3: <i>mi facevano male le gambe / le ginocchia / le braccia</i>: insistere sul plurale femminile.</li></ol>""")

    # Page 8
    pc = [("A2 · 25", "So usare me lo, te lo, te la."), ("A2 · 26", "So descrivere una casa delle vacanze."),
          ("A2 · 26", "So usare -ino, -etto, -one, -accio."), ("A2 · 26", "So dire le braccia, le dita, le uova."),
          ("A2 · 26", "So scrivere una cartolina.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Ho i bracci rossi.", "Ho le braccia rosse."), ("Abbiamo una casetta con un terrazzino.", "✓"),
          ("Mi fanno male tre diti.", "Mi fanno male tre dita."), ("Ho comprato dieci uovi.", "Ho comprato dieci uova."),
          ("Le uova sono freschi.", "Le uova sono fresche."), ("Che tempaccio! Piove da tre giorni.", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:38mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Una cartolina dalle vacanze (50–75 parole).</b> Sei in vacanza. Scrivi una cartolina a un amico o a un vicino: dove sei, com'è la casa, che tempo fa, che cosa fai. Usa almeno tre nomi alterati e un plurale in <i>-a</i> (<i>le braccia, le dita, le uova…</i>).</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge la cartolina; l'insegnante chiede <i>Com'era la casetta?</i> Unità 27: <i>Lo sai che…?</i> (il discorso indiretto: dice che, ha detto che; i pronomi tonici).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("26.1", "I tre dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("26.2", "Ascolta e ripeti")}
<p>{" · ".join(S262)}</p>
{sub("26.3", "Piccolo o grande?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S263))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 26 - Una casetta al mare")
