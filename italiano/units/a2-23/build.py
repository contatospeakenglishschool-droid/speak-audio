# Speak! Ponte A2 - Unità 23 "Che bello!" (tutto in italiano) - shared engine + Italian layer
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
from engine_it import *
import speak_engine as _se
import grammar_ref_it
_se.SERIES = "Ponte"
setup(band="A2 · UNITÀ 23", audio_json=os.path.join(HERE, "audio_it-a2-unita-23.json"), img_dir=os.path.join(HERE, "img"), lang="it-IT")

PHOTOS = [("A", "il concerto all'aperto", "concerto"), ("B", "il palco", "palco"), ("C", "la cantante", "cantante"), ("D", "il pubblico", "pubblico"),
          ("E", "i fuochi d'artificio", "fuochi"), ("F", "il cinema all'aperto", "cinema"), ("G", "le orecchiette", "orecchiette"), ("H", "la costa", "costa")]

_r = json.load(open(os.path.join(HERE, "roteiro.json")))["units"]["it-a2-unita-23"]
SCRIPT = [tuple(x.split(": ", 1)) for x in _r["23.1 Dialoghi"].split("\n")]
SCRIPT = [("Narratore" if n == "Narrator" else n, t.replace("...", "…")) for n, t in SCRIPT]
S232 = [x.split(": ", 1)[1] for x in _r["23.2 Ripeti"].split("\n")]
S233 = [x.split(": ", 1)[1].split(". ", 1)[1] for x in _r["23.3 Esclamazione o domanda"].split("\n")]


def _key(w):
    a, _, rest = w.partition(" ")
    return (rest if a in ("la", "il", "i", "gli", "lo", "le") else w).lower()


def build(teacher):
    b = Book(teacher)
    T, A, R, sub, sec = teacher, b.A, b.R, b.sub, b.sec
    def ch(opts, ans):
        return "<b>" + " / ".join(R(f"<u>{x}</u>") if (T and x == ans) else x for x in opts) + "</b>"

    # Page 1
    cover = cover_html(T, "LIVELLO A2 · UNITÀ 23", "Che bello!", "Concerti, feste e vacanze · <b>che…! · quanto…! · com'è…! · bello, buono, grande</b>",
                       [("SAI FARE", "esprimere entusiasmo e sorpresa, commentare foto e vacanze, parlare di concerti e feste d'estate, fare complimenti"),
                        ("LINGUA", "Che bel mare! · Quanta gente! · Com'è brava la cantante! · Che begli occhiali! · Buon'idea!"),
                        ("PRONUNCIA", "esclamazione o domanda? Com'è brava! / Com'è il concerto?")])
    words = [w for _, w, _ in PHOTOS]
    b.page(f"""{sec(1, "Riscaldamento: le sere d'estate", "8 min")}
{sub("A", "Guarda, ascolta e ripeti. Poi scrivi la parola sotto la foto.", "4 min")}
<div class="bank">{" &nbsp;·&nbsp; ".join(x.replace(" ", "&nbsp;") for x in sorted(words, key=_key))}</div>
{photo_grid(T, PHOTOS)}
{sub("B", "Parla con l'insegnante.", "4 min")}
<ol><li>Ti piacciono i concerti all'aperto? Qual è l'ultimo concerto che hai visto?</li><li>Nella tua città ci sono feste o festival d'estate?</li><li>Hai mai visto un film al cinema all'aperto?</li></ol>""",
    26, """<ol><li>A: <i>il palco</i> = dove suonano i musicisti; <i>il pubblico</i> = le persone che guardano (singolare!); <i>le orecchiette</i> = pasta tipica della Puglia.</li>
<li>B: reagire alle risposte con esclamazioni (<i>Che bello! Che fortuna!</i>): primo contatto con la lingua dell'unità.</li></ol>""", cover=cover)

    b.extra("Panoramica della lezione · 55 min", """
<table><tr><th>Fase</th><th>Tempo</th><th>Obiettivo</th><th>Pagina</th></tr>
<tr><td>1 Riscaldamento</td><td>8 min</td><td>8 foto: le sere d'estate</td><td>1</td></tr>
<tr><td>2 Ascolto</td><td>10 min</td><td>Le foto della Puglia · il concerto alla Montagnola</td><td>2</td></tr>
<tr><td>3 Grammatica</td><td>10 min</td><td>Che / quanto / com'è…! · bel, bello, bell', begli</td><td>3</td></tr>
<tr><td>+ Riferimento grammaticale</td><td>–</td><td>Esclamazioni · bello · buono · grande</td><td>4</td></tr>
<tr><td>4 Laboratorio di pronuncia</td><td>4 min</td><td>Esclamazioni · esclamazione o domanda?</td><td>5</td></tr>
<tr><td>5 Pratica</td><td>9 min</td><td>Bello e buono · reagisci! · costruisci le parole</td><td>6</td></tr>
<tr><td>6 Parlare</td><td>12 min</td><td>Le foto delle vacanze · la mia festa preferita</td><td>7</td></tr>
<tr><td>7 Conclusione</td><td>2 min</td><td>Autovalutazione e compiti</td><td>8</td></tr></table>
<div class="box sand"><h4>LA STORIA CONTINUA</h4>Inizio agosto. Giulia e Davide sono tornati dalla Puglia (unità 21) e al bar mostrano le foto a Júlia e Marco: Polignano a Mare (<i>che bel mare!</i>), le orecchiette e il vino (<i>che buon vino!</i>), un <i>bell'albergo</i> con un grande balcone sul mare. Giulia ha <i>begli occhiali</i> nuovi: quelli vecchi sono rimasti a Bologna! La sera vanno tutti e quattro al concerto all'aperto nel parco della Montagnola: <i>quanta gente! com'è brava la cantante!</i> Davide porta le birre (<i>buon'idea!</i>). La band suona una bossa nova che la mamma di Júlia cantava sempre (all'unità 02 Júlia sognava di fare la cantante): Júlia canta il ritornello.</div>
<div class="box"><h4>IL PROBLEMA PER I BRASILIANI</h4>Le esclamazioni sono quasi uguali al portoghese (<i>Que lindo! Quanta gente! Como é bonita!</i>). Gli errori sono nelle forme: <i>bello mare</i> (→ <b>bel mare</b>), <i>belli occhiali</i> (→ <b>begli occhiali</b>), <i>un buono vino</i> (→ <b>un buon vino</b>), e l'articolo dopo <i>che</i>: <i>che una bella voce</i> (→ <b>che bella voce</b>). Attenzione: <i>lindo</i> → <b>bello</b> (in italiano <i>lindo</i> vuol dire pulito, ordinato).</div>
<div class="box"><h4>LA REALTÀ ITALIANA</h4>D'estate le città italiane si riempiono di eventi all'aperto: concerti nei parchi, <b>cinema all'aperto</b> (a Bologna in piazza Maggiore), sagre di paese con cibo tipico e balli. In agosto, per <b>Ferragosto</b>, in molte città ci sono i <b>fuochi d'artificio</b>. Spesso gli eventi sono gratuiti.</div>
<div class="box"><h4>AUDIO</h4>Traccia 23.1 I due dialoghi (lento e naturale) · Traccia 23.2 Ascolta e ripeti · Traccia 23.3 Esclamazione o domanda?</div>""")

    # Page 2
    p1 = [("Júlia: Che bel", "mare"), ("Davide: Che buone le", "orecchiette"), ("Giulia e Davide hanno dormito in un bell'", "albergo"),
          ("La camera aveva un grande", "balcone sul mare"), ("Giulia ha comprato gli occhiali nuovi a", "Lecce")]
    p1l = "".join(f"<tr><td>{a}</td><td>{A(x, 'min-width:44mm')}</td></tr>" for a, x in p1)
    vf = [("Il concerto è in un parco.", "V"), ("Secondo Marco, ci saranno cento persone.", "F"), ("Davide ha portato quattro birre.", "V"),
          ("La band suona una canzone brasiliana.", "V"), ("Júlia non conosce la canzone.", "F")]
    vfr = "".join(f"<tr><td>{i+1}. {s}</td><td style='width:16mm;text-align:center'>{ch(['V', 'F'], a)}</td></tr>" for i, (s, a) in enumerate(vf))
    b.page(f"""{sec(2, "Ascolto: bentornati!", "10 min")}
{audiocard(["23.1 · SLOW", "23.1 · NATURAL"])}
{sub("A", "Prima parte. Al bar, le foto della Puglia. Completa.", "4 min", "23.1 · SLOW")}
<table style="margin:0;width:94%">{p1l}</table>
{sub("B", "Seconda parte. Il concerto alla Montagnola. Vero (V) o falso (F)?", "4 min", "23.1 · NATURAL")}
<table style="margin:0">{vfr}</table>
{sub("C", "Perché Júlia conosce la canzone?", "2 min")}
<div class="wline">{R("La cantava sempre sua madre.")}</div>""",
    22, """<ol><li>A: prima versione <b>lenta</b>. Gli occhiali: ricordare l'unità 21 (Giulia li aveva dimenticati alla partenza).</li>
<li>B: frase 2: <i>ci saranno mille persone</i>: il futuro di supposizione dell'unità 22.</li></ol>""")

    # Page 3
    rules = [("<i><b>Che</b> bel mare! · <b>Che</b> bella voce!</i> Dopo <i>che</i>", ["non c'è l'articolo", "c'è l'articolo"], "non c'è l'articolo"),
             ("<i><b>Quanta</b> gente! · <b>Quanti</b> ricordi!</i> <i>Quanto</i> davanti al nome", ["cambia come un aggettivo", "non cambia mai"], "cambia come un aggettivo"),
             ("<i><b>Com'è</b> brava la cantante!</i> Dopo <i>com'è</i> c'è", ["un aggettivo", "un nome"], "un aggettivo"),
             ("<i>un <b>bel</b> mare · un <b>bell'</b>albergo · <b>begli</b> occhiali</i>: <i>bello</i> prima del nome cambia come", ["l'articolo il / l' / gli", "un verbo"], "l'articolo il / l' / gli"),
             ("<i>un <b>buon</b> vino · <b>buon'</b>idea</i>: <i>buono</i> prima del nome cambia come", ["un / un'", "il / l'"], "un / un'"),
             ("<i>Il mare è <b>bello</b>.</i> Dopo il verbo <i>essere</i>, <i>bello</i>", ["non cambia", "diventa bel"], "non cambia")]
    rl = "".join(f"<li>{s} {ch(o, a)}.</li>" for s, o, a in rules)
    cc = [("Che", ["bel", "bello"], "bel", "concerto!"), ("Che", ["begli", "belli"], "begli", "occhiali!"),
          ("", ["Quanta", "Quanto"], "Quanta", "gente!"), ("Che", ["buon", "buono"], "buon", "caffè!")]
    ccl = "".join(f"<li>{a} {ch(o, r)} {z}</li>" for a, o, r, z in cc)
    b.page(f"""{sec(3, "Grammatica: che…! quanto…! com'è…! · bello e buono", "10 min")}
{sub("A", "Studia le frasi dei dialoghi.", "2 min")}
<div class="box" style="margin-top:1mm;font-size:9pt;line-height:1.6">1. <b>Che</b> bel mare! · <b>Che</b> buone le orecchiette! · <b>Che</b> bella idea! · <b>Che</b> bella voce! · <b>Che</b> vergogna!<br>
2. <b>Quanto</b> siete abbronzati! · <b>Quanta</b> gente! · <b>Quanti</b> ricordi! · <b>Com'è</b> blu l'acqua! · <b>Com'è</b> brava la cantante!<br>
3. un <b>bel</b> mare · un <b>bell'</b>albergo · <b>begli</b> occhiali · <b>bella</b> voce · un <b>buon</b> vino · <b>Buon'</b>idea! · un <b>grande</b> balcone</div>
{sub("B", "Scegli l'opzione corretta per completare le regole.", "5 min")}
<ol style="line-height:1.6">{rl}</ol>
{sub("C", "Scegli l'opzione corretta.", "3 min")}
<ol style="line-height:1.6">{ccl}</ol>
<div class="box sand"><h4>REGOLA</h4><b>Che</b> + nome / aggettivo (senza articolo) · <b>quanto, quanta, quanti, quante</b> + nome · <b>com'è</b> + aggettivo. Prima del nome <b>bello</b> cambia come <i>il</i> (bel, bello, bell', bei, begli, bella, belle) e <b>buono</b> come <i>un</i> (buon, buono, buona, buon'). Tutto: pagina 4.</div>""",
    22, """<ol><li>B: regola 4: scrivere alla lavagna <i>il mare → bel mare, l'albergo → bell'albergo, gli occhiali → begli occhiali, i ricordi → bei ricordi</i>.</li>
<li>C: frase 4: <i>caffè</i> è maschile → <i>buon</i>. <i>Buon caffè</i> come <i>buon appetito</i>, <i>buon viaggio</i>.</li></ol>""")

    grammar_ref_it.esclamazioni_bello_buono(b)

    # Page 5
    ans3 = ["esclamazione", "domanda", "esclamazione", "domanda", "esclamazione", "domanda"]
    b.page(f"""{sub("D", "Errori comuni dei brasiliani", "2 min")}
<div class="box sand"><h4>ATTENZIONE: ERRORI COMUNI</h4>
<table style="margin:0"><tr><th>Non dire</th><th>Di'</th><th>Perché?</th></tr>
<tr><td>Che bello mare!</td><td><b>Che bel mare!</b></td><td><i>il mare</i> → <i>bel</i>.</td></tr>
<tr><td>Che belli occhiali!</td><td><b>Che begli occhiali!</b></td><td><i>gli occhiali</i> → <i>begli</i>.</td></tr>
<tr><td>Che una bella voce!</td><td><b>Che bella voce!</b></td><td>Dopo <i>che</i> niente articolo.</td></tr>
<tr><td>Quanto gente!</td><td><b>Quanta gente!</b></td><td><i>la gente</i>: femminile.</td></tr>
<tr><td>Un buono vino.</td><td><b>Un buon vino.</b></td><td><i>un vino</i> → <i>buon</i>.</td></tr></table></div>
<div style="height:1mm"></div>
{sec(4, "Laboratorio di pronuncia", "4 min")}
{audiocard(["23.2", "23.3"])}
{sub("A", "Ascolta e ripeti. Nelle esclamazioni la voce sale forte sulla parola importante e poi scende.", "2 min", "23.2")}
<div class="bank" style="font-weight:600;background:#fff">{" &nbsp;·&nbsp; ".join(S232)}</div>
{sub("B", "Esclamazione o domanda? Ascolta e scegli.", "2 min", "23.3")}
{twocol([f'<li value="{i+1}">{ch(["esclamazione", "domanda"], a)}</li>' for i, a in enumerate(ans3)], 4)}""",
    28, """<ol><li>Errori: <i>la gente</i> è femminile singolare anche se sono tante persone: <i>Quanta gente! La gente è simpatica.</i></li>
<li>4A: far esagerare l'entusiasmo; gli italiani usano anche le mani!</li>
<li>4B: 1 e 2 hanno le stesse parole (<i>Com'è…</i>): solo la voce dice se è domanda.</li></ol>""")

    # Page 6
    fl = [("un ___ ragazzo (bello)", "bel"), ("una ___ pizza (buono)", "buona"), ("un ___ albergo (bello)", "bell'"),
          ("dei ___ ricordi (bello)", "bei"), ("un ___ amico (buono)", "buon"), ("degli ___ spettacoli (bello)", "begli")]
    fll = [f'<li value="{i+1}">{s.replace("___", A(a, "min-width:12mm"))}</li>' for i, (s, a) in enumerate(fl)]
    re = [("Il tuo amico ti mostra la foto di una spiaggia bellissima.", "Che bella spiaggia! / Che bel mare!"), ("Al concerto ci sono diecimila persone.", "Quanta gente!"),
          ("Assaggi un gelato buonissimo.", "Che buono! / Com'è buono!"), ("Una cantante canta benissimo.", "Com'è brava! / Che bella voce!")]
    rel = "".join(f"<li>{q}<div class='wline'>{R(a)}</div></li>" for q, a in re)
    wb = [("cantare", "la canzone / il cantante"), ("suonare", "il suono"), ("festeggiare", "la festa"), ("ballare", "il ballo")]
    wbl = [f'<li value="{i+1}">{v} → {A(n, "min-width:30mm")}</li>' for i, (v, n) in enumerate(wb)]
    b.page(f"""{sec(5, "Pratica", "9 min")}
{sub("A", "Bello o buono? Scrivi la forma giusta.", "3 min")}
{twocol(fll, 4)}
{sub("B", "Reagisci! Scrivi un'esclamazione.", "4 min")}
<ol style="line-height:1.45">{rel}</ol>
{sub("C", "Costruisci le parole. Dal verbo al nome.", "2 min")}
{twocol(wbl, 3)}""",
    22, """<ol><li>A: frase 4: <i>i ricordi</i> → <i>bei</i>; frase 6: <i>gli spettacoli</i> (s + consonante) → <i>begli</i>.</li>
<li>B: accettare tutte le esclamazioni corrette; premiare quelle con <i>bel / begli</i>.</li></ol>""")

    # Page 7
    b.page(f"""{sec(6, "Parlare", "12 min")}
{sub("A", "Le foto delle vacanze. Mostra all'insegnante tre o quattro foto sul telefono (vacanze, feste, cibo). L'insegnante reagisce con esclamazioni e fa domande. Poi cambiate.", "6 min")}
<div class="box" style="font-size:9pt;margin-top:1.5mm"><h4>PAROLE UTILI</h4>Che bel…! · Che bella…! · Che begli…! · Quanta gente! · Quanti…! · Com'è…! · Che buono! · Che fortuna! · Che invidia! · Dov'è? · Con chi eri?</div>
{sub("B", "La mia festa preferita. Parla con l'insegnante.", "6 min")}
<ol style="line-height:1.55"><li>Qual è la festa più bella della tua città?</li><li>Che musica si ascolta? Che cosa si mangia?</li><li>Qual è il concerto più bello della tua vita?</li><li>C'è una canzone che ti ricorda la tua famiglia?</li><li>Preferisci i concerti grandi o i piccoli locali?</li></ol>
<div class="wline"></div><div class="wline"></div>""",
    22, """<ol><li>A: se lo studente non ha foto, usare le foto della pagina 1. Pretendere almeno cinque esclamazioni diverse.</li>
<li>B: domanda 4 richiama la bossa nova della mamma di Júlia. Le feste brasiliane (Carnevale, festa junina) danno molto da dire.</li></ol>""")

    # Page 8
    pc = [("A2 · 22", "So fare una supposizione con il futuro (sarà, avrà)."), ("A2 · 23", "So esprimere entusiasmo con che…!, quanto…!, com'è…!"),
          ("A2 · 23", "So usare bel, bello, bell', bei, begli."), ("A2 · 23", "So usare buon, buono, buona, buon'."),
          ("A2 · 23", "So parlare di concerti e feste.")]
    pcr = "".join(f"<tr><td><b>{u}</b></td><td>{s}</td><td>☐</td><td>☐</td><td>☐</td></tr>" for u, s in pc)
    hw = [("Che bello mare!", "Che bel mare!"), ("Quanta gente!", "✓"),
          ("Che belli occhiali!", "Che begli occhiali!"), ("Un buono vino.", "Un buon vino."),
          ("Che una bella voce!", "Che bella voce!"), ("Com'è brava la cantante!", "✓")]
    hwl = "".join(f"<li>{a} {A(c, 'min-width:42mm')}</li>" for a, c in hw)
    b.page(f"""{sec(7, "Conclusione e compiti", "2 min")}
{sub("A", "Autovalutazione", "1 min")}
<table class="ck"><tr><th style="width:20mm"></th><th>In italiano…</th><th style="width:18mm">Facile!</th><th style="width:18mm">A volte</th><th style="width:18mm">Non ancora</th></tr>{pcr}</table>
{sub("B", "Compiti", "1 min")}
<p><b>1. Correggi gli errori. Due frasi sono corrette.</b></p>
<ol style="line-height:1.6">{hwl}</ol>
<p style="margin-top:2mm"><b>2. Una bella serata (50–75 parole).</b> Racconta un concerto, una festa o una serata speciale. Dove eri? Con chi? Com'era? Usa almeno tre esclamazioni e le forme di <i>bello</i> e <i>buono</i>.</p>
<div class="wline"></div><div class="wline"></div><div class="wline"></div><div class="wline"></div>""",
    18, """<p>Prossima lezione: lo studente legge il racconto; l'insegnante reagisce con esclamazioni. Unità 24: <i>Il mio quartiere</i> (qualche, ogni, nessuno, qualcuno, niente).</p>""")

    b.extra("Trascrizioni audio", f"""
{sub("23.1", "I due dialoghi (lento e naturale)")}
<p style="line-height:1.4">{"<br>".join(f"<b>{n}:</b> {t}" for n, t in SCRIPT)}</p>
{sub("23.2", "Ascolta e ripeti")}
<p>{" · ".join(S232)}</p>
{sub("23.3", "Esclamazione o domanda?")}
<p>{" · ".join(f"{i+1}. {s}" for i, s in enumerate(S233))}</p>""")
    return b.html()


if __name__ == "__main__":
    render(build, sys.argv[1] if len(sys.argv) > 1 else "A2 Ponte 23 - Che bello!")
